import Moedas.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Variavel para sair do laco principal
        Boolean sair;
        Scanner teclado = new Scanner(System.in);
        // todas respostas do teclado estao usando esta variavel
        int respUser;
        // variavel para receber os valores de cada moeda
        double vlr;
        // Classe que contem os metodos de opcoes do menu do programa
        opcoesUser opt = new opcoesUser();
        // Classe com os metodos relacionados diretamente com cofre, ele precisa receber obj do tipo Moeda
        Cofrinho cofre = new Cofrinho();

        // Controle para sair do laco
        sair = false;
        OUTER:
        while (sair == false) {
            String resp;
            // Metodo para apenas apresentar opcoes para o usuario, podendo ser chamado de qq classe
            opt.abrirOpcoes();
            // Variavel recebe input do teclado, precisa ser uma entrada de int, neste nivel nao ha tratamento de entrada
            respUser = teclado.nextInt();
            // Primeiro nivel ddo menu, para excutar a escolha do usuario
            switch (respUser) {
                // Finalizacao do programa
                case 0 -> {
                    System.out.println("\nPROGRAMA FINALIZADO");
                    break OUTER;
                }
                // Validacao do tipo de moeda que entrara no cofre, tipo e valor
                case 1 -> {
                    // Metodo para receber o tipo de moeda que daremos entrada no cofre
                    resp = opt.tipoMoeda();
                    // Cada tipo de moeda abaixo usa as mesma funcoes para validar o valor da moeda
                    // E aciona classes diferentes para adicionar a moeda ao cofre, porem com mesmas 
                    // entradas
                    if (resp == "Dólar") {
                        while (true) {
                            // Valida o valor de entrada da moeda ou encerra o programa
                            vlr = opt.recebeValor();
                            if (vlr == 0){
                                break;
                            }
                            else {
                                cofre.adicionar(new Dolar(vlr, resp));
                            }
                        }
                    }
                    else if (resp == "Real") {
                        while (true) {
                            // Valida o valor de entrada da moeda ou encerra o programa
                            vlr = opt.recebeValor();
                            if (vlr == 0){
                                break;
                            }
                            else {
                                cofre.adicionar(new Real(vlr, resp));
                            }
                        }
                    }
                    else{
                        while (true) {
                            // Valida o valor de entrada da moeda ou encerra o programa
                            vlr = opt.recebeValor();
                            if (vlr == 0){
                                break;
                            }
                            else {
                                cofre.adicionar(new Euro(vlr, resp));
                           }
                        }
                    }
                }
                // Remocao de moedas do cofre
                case 2 -> cofre.remover();
                // Menu de listagem de moedas do cofre
                case 3 -> cofre.listagemMoedas();
                // Menu de conversao do valor total no cofre em REAIS
                case 4 -> cofre.totalconvertido();
                default -> { 
                }
            }
        }
    }
}
