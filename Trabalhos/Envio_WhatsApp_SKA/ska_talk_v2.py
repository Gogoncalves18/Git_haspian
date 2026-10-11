#!/usr/bin/env python3
"""
SKA Talk - Assistente de WhatsApp Web
Versão 0.2

Estrutura:
    ska_talk.py
    SKA_talk.xlsx
    campanha/
        campanha.json
        imagem.jpg

Você só altera o conteúdo da pasta "campanha".
O script permanece o mesmo.
"""

import json
import re
import sys
import webbrowser
import zipfile
from pathlib import Path
from urllib.parse import quote
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import xml.etree.ElementTree as ET


ARQUIVO_EXCEL = "SKA_talk.xlsx"
PASTA_CAMPANHA = "campanha"
ARQUIVO_CAMPANHA = "campanha.json"
ARQUIVO_PROGRESSO = "ska_talk_progresso.json"


def coluna_excel_para_indice(ref):
    letras = re.match(r"([A-Z]+)", ref)
    if not letras:
        return None
    n = 0
    for c in letras.group(1):
        n = n * 26 + (ord(c) - ord("A") + 1)
    return n - 1


def ler_xlsx(caminho):
    caminho = Path(caminho)
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

    with zipfile.ZipFile(caminho, "r") as z:
        shared_strings = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            for si in root.findall("m:si", ns):
                partes = []
                for t in si.iter(
                    "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t"
                ):
                    partes.append(t.text or "")
                shared_strings.append("".join(partes))

        workbook = ET.fromstring(z.read("xl/workbook.xml"))
        rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))

        rel_ns = {
            "r": "http://schemas.openxmlformats.org/package/2006/relationships"
        }
        rid_to_target = {}
        for rel in rels.findall("r:Relationship", rel_ns):
            rid_to_target[rel.attrib["Id"]] = rel.attrib["Target"]

        sheets = workbook.find("m:sheets", ns)
        if sheets is None or len(sheets) == 0:
            raise ValueError("Nenhuma aba encontrada no Excel.")

        sheet_elem = None
        for s in sheets:
            if s.attrib.get("name") == "Contatos":
                sheet_elem = s
                break
        if sheet_elem is None:
            sheet_elem = sheets[0]

        rid = sheet_elem.attrib.get(
            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
        )
        target = rid_to_target[rid].lstrip("/")
        if not target.startswith("xl/"):
            target = "xl/" + target

        root = ET.fromstring(z.read(target))
        sheet_data = root.find("m:sheetData", ns)

        linhas = []
        if sheet_data is None:
            return linhas

        for row in sheet_data.findall("m:row", ns):
            valores = {}
            for c in row.findall("m:c", ns):
                ref = c.attrib.get("r", "")
                idx = coluna_excel_para_indice(ref)
                if idx is None:
                    continue

                tipo = c.attrib.get("t")
                v = c.find("m:v", ns)

                if tipo == "inlineStr":
                    is_elem = c.find("m:is", ns)
                    texto = ""
                    if is_elem is not None:
                        texto = "".join(
                            t.text or ""
                            for t in is_elem.iter(
                                "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t"
                            )
                        )
                    valor = texto
                elif v is None:
                    valor = ""
                elif tipo == "s":
                    valor = shared_strings[int(v.text)]
                else:
                    valor = v.text or ""

                valores[idx] = valor

            if valores:
                max_idx = max(valores)
                linha = [""] * (max_idx + 1)
                for idx, valor in valores.items():
                    linha[idx] = valor
                linhas.append(linha)

    return linhas


def normalizar_telefone(valor):
    digitos = re.sub(r"\D", "", str(valor or ""))
    if not digitos:
        return None

    if digitos.startswith("55") and len(digitos) in (12, 13):
        telefone = digitos
    else:
        telefone = "55" + digitos

    if len(telefone) not in (12, 13):
        return None

    return telefone


def carregar_contatos(caminho):
    linhas = ler_xlsx(caminho)
    if not linhas:
        return []

    cabecalho = [str(x).strip() for x in linhas[0]]

    def achar(nome):
        try:
            return cabecalho.index(nome)
        except ValueError:
            return None

    idx_nome = achar("Primeiro Nome")
    idx_empresa = achar("Empresa")
    idx_tel = achar("Telefones")

    if idx_tel is None:
        raise ValueError("Não encontrei a coluna 'Telefones'.")

    contatos = []
    vistos = set()

    for numero_linha, row in enumerate(linhas[1:], start=2):
        def obter(idx):
            if idx is None or idx >= len(row):
                return ""
            return str(row[idx]).strip()

        telefone = normalizar_telefone(obter(idx_tel))
        if not telefone or telefone in vistos:
            continue

        vistos.add(telefone)

        contatos.append({
            "linha_excel": numero_linha,
            "nome": obter(idx_nome),
            "empresa": obter(idx_empresa),
            "telefone": telefone,
        })

    return contatos


def carregar_campanha(base_dir):
    pasta = base_dir / PASTA_CAMPANHA
    config_path = pasta / ARQUIVO_CAMPANHA

    if not config_path.exists():
        raise FileNotFoundError(
            f"Arquivo da campanha não encontrado:\n{config_path}"
        )

    dados = json.loads(config_path.read_text(encoding="utf-8"))

    obrigatorios = ["imagem", "link", "texto"]
    faltando = [x for x in obrigatorios if x not in dados]
    if faltando:
        raise ValueError(
            "Campos ausentes em campanha.json: " + ", ".join(faltando)
        )

    imagem = pasta / dados["imagem"]
    if not imagem.exists():
        raise FileNotFoundError(
            f"Imagem da campanha não encontrada:\n{imagem}"
        )

    return {
        "imagem": imagem,
        "link": str(dados["link"]).strip(),
        "texto": str(dados["texto"]).strip(),
    }


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("SKA Talk - WhatsApp")
        self.root.geometry("850x650")

        self.base_dir = Path(__file__).resolve().parent
        self.excel_path = self.base_dir / ARQUIVO_EXCEL
        self.progresso_path = self.base_dir / ARQUIVO_PROGRESSO

        self.contatos = []
        self.campanha = None
        self.indice = 0
        self.etapa = 0
        self.limite = 250

        self.criar_interface()
        self.carregar()

    def criar_interface(self):
        topo = ttk.Frame(self.root, padding=12)
        topo.pack(fill="x")

        ttk.Label(topo, text="Excel:").grid(row=0, column=0, sticky="w")
        self.lbl_arquivo = ttk.Label(topo, text=str(self.excel_path))
        self.lbl_arquivo.grid(row=0, column=1, sticky="w", padx=8)
        ttk.Button(topo, text="Escolher...", command=self.escolher_excel).grid(
            row=0, column=2
        )

        ttk.Button(
            topo,
            text="Recarregar campanha",
            command=self.recarregar_campanha,
        ).grid(row=1, column=2, pady=(10, 0))

        self.lbl_campanha = ttk.Label(topo, text="")
        self.lbl_campanha.grid(
            row=1, column=0, columnspan=2, sticky="w", pady=(10, 0)
        )

        ttk.Separator(self.root).pack(fill="x", padx=12, pady=4)

        contato = ttk.Frame(self.root, padding=12)
        contato.pack(fill="x")

        self.lbl_progresso = ttk.Label(
            contato, text="", font=("Arial", 12, "bold")
        )
        self.lbl_progresso.pack(anchor="w")

        self.lbl_nome = ttk.Label(
            contato, text="", font=("Arial", 16, "bold")
        )
        self.lbl_nome.pack(anchor="w", pady=(8, 2))

        self.lbl_empresa = ttk.Label(contato, text="")
        self.lbl_empresa.pack(anchor="w")

        self.lbl_tel = ttk.Label(contato, text="")
        self.lbl_tel.pack(anchor="w")

        box = ttk.LabelFrame(self.root, text="Conteúdo atual", padding=12)
        box.pack(fill="both", expand=True, padx=12, pady=8)

        self.lbl_etapa = ttk.Label(
            box, text="", font=("Arial", 12, "bold")
        )
        self.lbl_etapa.pack(anchor="w")

        self.txt = tk.Text(box, height=11, wrap="word")
        self.txt.pack(fill="both", expand=True, pady=8)

        acoes = ttk.Frame(box)
        acoes.pack(fill="x")

        self.btn_acao = ttk.Button(
            acoes,
            text="Executar etapa",
            command=self.executar_etapa,
        )
        self.btn_acao.pack(side="left")

        ttk.Button(
            acoes,
            text="Marcar etapa concluída",
            command=self.marcar_concluida,
        ).pack(side="left", padx=10)

        nav = ttk.Frame(self.root, padding=12)
        nav.pack(fill="x")

        ttk.Button(
            nav, text="← Contato anterior", command=self.anterior
        ).pack(side="left")

        ttk.Button(
            nav, text="Próximo contato →", command=self.proximo
        ).pack(side="right")

        self.lbl_status = ttk.Label(
            self.root, text="", padding=(12, 0, 12, 12)
        )
        self.lbl_status.pack(anchor="w")

    def escolher_excel(self):
        arquivo = filedialog.askopenfilename(
            title="Escolha a planilha",
            filetypes=[("Excel", "*.xlsx")],
        )
        if arquivo:
            self.excel_path = Path(arquivo)
            self.lbl_arquivo.config(text=str(self.excel_path))
            self.carregar()

    def carregar(self):
        try:
            self.contatos = carregar_contatos(self.excel_path)
            self.campanha = carregar_campanha(self.base_dir)
        except Exception as e:
            messagebox.showerror("Erro", str(e))
            return

        progresso = self.ler_progresso()
        self.indice = progresso.get("indice", 0)
        self.etapa = progresso.get("etapa", 0)

        if self.indice >= self.total():
            self.indice = 0
            self.etapa = 0

        self.atualizar_tela()

    def recarregar_campanha(self):
        try:
            self.campanha = carregar_campanha(self.base_dir)
            self.lbl_status.config(
                text="Campanha recarregada com sucesso."
            )
            self.atualizar_tela()
        except Exception as e:
            messagebox.showerror("Erro na campanha", str(e))

    def total(self):
        return min(self.limite, len(self.contatos))

    def contato_atual(self):
        if not self.contatos or self.total() == 0:
            return None
        self.indice = max(0, min(self.indice, self.total() - 1))
        return self.contatos[self.indice]

    def texto_personalizado(self):
        c = self.contato_atual()
        if not c:
            return ""

        return self.campanha["texto"].format(
            nome=c["nome"] or "",
            empresa=c["empresa"] or "",
        )

    def atualizar_tela(self):
        c = self.contato_atual()
        if not c or not self.campanha:
            return

        nomes_etapa = [
            "1 de 3 — IMAGEM",
            "2 de 3 — LINK",
            "3 de 3 — TEXTO",
        ]

        self.lbl_progresso.config(
            text=f"Contato {self.indice + 1} de {self.total()}"
        )
        self.lbl_nome.config(text=c["nome"] or "(sem nome)")
        self.lbl_empresa.config(text=c["empresa"])
        self.lbl_tel.config(text=f"+{c['telefone']}")
        self.lbl_etapa.config(text=nomes_etapa[self.etapa])

        self.lbl_campanha.config(
            text=f"Campanha: {self.campanha['imagem'].name}"
        )

        self.txt.delete("1.0", "end")

        if self.etapa == 0:
            self.txt.insert(
                "1.0",
                f"Imagem:\n{self.campanha['imagem']}\n\n"
                "O botão abaixo abrirá a conversa do WhatsApp "
                "e também abrirá a imagem para você anexar."
            )
            self.btn_acao.config(text="Abrir WhatsApp + imagem")

        elif self.etapa == 1:
            self.txt.insert("1.0", self.campanha["link"])
            self.btn_acao.config(text="Abrir WhatsApp com link")

        else:
            self.txt.insert("1.0", self.texto_personalizado())
            self.btn_acao.config(text="Abrir WhatsApp com texto")

    def abrir_conversa(self, texto=None):
        c = self.contato_atual()
        if not c:
            return

        url = f"https://web.whatsapp.com/send?phone={c['telefone']}"

        if texto:
            url += f"&text={quote(texto)}"

        webbrowser.open(url)

    def abrir_arquivo(self, caminho):
        try:
            if sys.platform.startswith("win"):
                import os
                os.startfile(caminho)
            elif sys.platform == "darwin":
                import subprocess
                subprocess.Popen(["open", str(caminho)])
            else:
                import subprocess
                subprocess.Popen(["xdg-open", str(caminho)])
        except Exception as e:
            messagebox.showerror("Erro ao abrir arquivo", str(e))

    def executar_etapa(self):
        if self.etapa == 0:
            self.abrir_conversa()
            self.abrir_arquivo(self.campanha["imagem"])
            self.lbl_status.config(
                text="WhatsApp e imagem abertos. Anexe a imagem e envie."
            )

        elif self.etapa == 1:
            self.abrir_conversa(self.campanha["link"])
            self.lbl_status.config(
                text="Link preparado no WhatsApp. Confira e envie."
            )

        else:
            texto = self.texto_personalizado()
            self.abrir_conversa(texto)
            self.lbl_status.config(
                text="Texto preparado no WhatsApp. Confira e envie."
            )

    def marcar_concluida(self):
        if self.etapa < 2:
            self.etapa += 1
        else:
            self.etapa = 0
            if self.indice < self.total() - 1:
                self.indice += 1
            else:
                messagebox.showinfo(
                    "Concluído",
                    f"Final dos {self.total()} contatos."
                )

        self.salvar_progresso()
        self.atualizar_tela()

    def anterior(self):
        if self.indice > 0:
            self.indice -= 1
            self.etapa = 0
            self.salvar_progresso()
            self.atualizar_tela()

    def proximo(self):
        if self.indice < self.total() - 1:
            self.indice += 1
            self.etapa = 0
            self.salvar_progresso()
            self.atualizar_tela()

    def ler_progresso(self):
        if not self.progresso_path.exists():
            return {}
        try:
            return json.loads(
                self.progresso_path.read_text(encoding="utf-8")
            )
        except Exception:
            return {}

    def salvar_progresso(self):
        dados = {
            "indice": self.indice,
            "etapa": self.etapa,
        }
        self.progresso_path.write_text(
            json.dumps(dados, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
