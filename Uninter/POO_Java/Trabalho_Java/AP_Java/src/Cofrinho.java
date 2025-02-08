
import Classes_Abstratadas.Moeda;
import java.lang.classfile.instruction.ExceptionCatch;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

// Classe que controla o cofre
public class Cofrinho {
    // Todos os objetos guardados no cofre precisam respeitar a tipagem da classe abstrada Moeda
    // Esta classe que personifica o que entra aqui e as moedas que circula no programa
    private ArrayList<Moeda> listaMoedas = new ArrayList();
    // Variavel apenas para receber a somantoria das moedas do cofre
    double vlr_total;

    // Metodo para adicionar moeda apos as validacoes
    public void adicionar(Moeda itemValor) {
        listaMoedas.add(itemValor);
    }

    // Listar moedas existentes do cofre, independente da nacionalidade delas
    // Mostra tipo da moeda e valor
    public void listagemMoedas() {
        System.out.println("________________________________________________________");
        System.out.println("LISTA DE MOEDAS NO COFRE:");
        System.out.println("---------------------------------------------------------");
        for(Moeda i : listaMoedas) {
            i.info();            
        }
        System.out.println("---------------------------------------------------------");

    }

    // Metodo para converter os valores de moedas que estao no cofre em valor 
    // de REAIS
    public void totalconvertido() {
        vlr_total = 0;
        System.out.println("\n________________________________________________________");
        for(Moeda i : listaMoedas) {
            vlr_total += i.converter();            
        }
        System.out.println("\n>>>>>> HÁ NO COFRE R$" + vlr_total + " <<<<<<\n");
    }
    
    // Metodo para remover do cofre as moedas pelo seu index
    public void remover() {
        Scanner teclado = new Scanner(System.in);
        // Variavel para pegar o input de escolha da moeda a ser removida
        int remocaoUser;
        boolean solicitarMaisEntrada;
        // Controladora para validar se devemos continuar a inserir moedas
        solicitarMaisEntrada = true;
        
        // Funcao isoalada para listagem de moedas a ser removida, a todo momento 
        // e necessario buscar a listagem para cada removacao, devido ao 
        // tamanho dinamico da lista de moedas no cofre
        listaMoedasParaRemover();

        solicitarMaisEntrada = true;
        
        // Laco de validacao da entrada de teclado do usuario para escolha das moedas
        // a ser removida, eliminamos entradas que estao fora do range da lista e 
        // string que nao representa o index de cada objeto do cofre
        while (solicitarMaisEntrada == true) {

            System.out.println("    \n DIGITE UM ÍNDICE DE 0 À " + (listaMoedas.size()-1) + " OU 999 PARA SAIR");
            try {
                // Valida se e um inteiro
                remocaoUser = teclado.nextInt();
                // Deixa passar valores dentro do range e codigo para abortar (999)
                if(remocaoUser <= (listaMoedas.size()-1) || remocaoUser == 999) {
                    // Abortar remocao de moeda
                    if(remocaoUser == 999) {
                        break;
                    }
                    // Trecho que remove moedas pelo indice
                    else if(remocaoUser <= (listaMoedas.size()-1)) {
                        listaMoedas.remove(remocaoUser);
                        System.out.println("REMOVENDO O ITEM DE ÍNDICE [ " + remocaoUser + " ]. REMOVER MAIS UM ÍNDICE ou 999 PARA SAIR");
                        // Atualizacao da lista de moedas para o usuario saber a nova posicao 
                        listaMoedasParaRemover();
                    }
                    else{
                        // Levanta uma excessao se o range do index nao foi respeitado pelo usuario
                        throw new RuntimeException("999");
                    }
                }
                
            } catch (InputMismatchException e) {
                // Tratamento para inputs que nao respeitam a entreda de numeros inteiros                           
                solicitarMaisEntrada = true;
                
                System.out.println("\n          >>>>>> DIGITE APENAS INTEIROS ! <<<<<<");
                teclado.nextLine();
            }
            
            catch (RuntimeException e) {
                // Tratamento para inputs que nao respeita o range anunciado no menu                           
                solicitarMaisEntrada = true;
                
                System.out.println("\n          >>>>>> ACEITO APENAS INDICES DE 0 À " + (listaMoedas.size()-1) + " <<<<<<");
                teclado.nextLine();
                }
                
            }
    }
        
    
    // Metodo para listar o index de moedas para remocao
    public void listaMoedasParaRemover() {
        int indice;
        indice = 0;
        
        System.out.println("\n>>>>>> DIGITE O [ INDICE ] DA MOEDA A SER REMOVIDA: <<<<<<\n");
        for(Moeda i : listaMoedas) {
            System.out.println("[ " + indice + " ] :"); 
            i.info();
            indice ++;
        }

    }
}
