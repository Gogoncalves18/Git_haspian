# SKA Talk — Versão 0.2

A ideia desta versão é simples:

**o código não muda. Você só alimenta a pasta `campanha`.**

## Estrutura

    SKA_Talk/
    ├── ska_talk.py
    ├── SKA_talk.xlsx
    ├── ska_talk_progresso.json   <- criado automaticamente
    └── campanha/
        ├── campanha.json
        └── imagem.jpg

## O que você troca para uma nova campanha

### 1. Imagem

Coloque sua imagem dentro da pasta:

    campanha/

Exemplo:

    campanha/folder_agosto.jpg

### 2. Link

Abra:

    campanha/campanha.json

E altere o campo:

    "link": "https://seulink.com"

### 3. Texto

No mesmo arquivo, altere:

    "texto": "Olá, {nome}! Tudo bem? ..."

Você pode usar:

- `{nome}` para inserir automaticamente o primeiro nome;
- `{empresa}` para inserir automaticamente a empresa.

### Exemplo completo

    {
      "imagem": "folder_agosto.jpg",
      "link": "https://ska.com.br/evento",
      "texto": "Olá, {nome}! Tudo bem?\n\nQuero compartilhar uma novidade com você."
    }

## Sequência de cada contato

O programa trabalha sempre nesta ordem:

1. IMAGEM
2. LINK
3. TEXTO

Depois passa automaticamente para o próximo contato.

## Trocar a campanha

Você não precisa mexer no `ska_talk.py`.

Basta:

1. trocar a imagem dentro da pasta `campanha`;
2. editar `campanha.json`;
3. clicar em **Recarregar campanha** no programa.

