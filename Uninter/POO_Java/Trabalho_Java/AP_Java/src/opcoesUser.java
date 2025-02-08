import java.util.InputMismatchException;
import java.util.Scanner;

public class opcoesUser {
    Scanner teclado = new Scanner(System.in);
    int respUser;
    double vlrUser;

    // Metodo para dar opcoes para o usuario
    public void abrirOpcoes() {
        System.out.println("________________________________________________________");
        System.out.println("\nDIGITE UMA DAS OPÇÕES ABAIXO:");
        System.out.println("0  >>>> Para Sair");
        System.out.println("1  >>>> Adicionar Moedas");
        System.out.println("2  >>>> Remover Moedas");
        System.out.println("3  >>>> Listar todas Moedas do Cofre");
        System.out.println("4  >>>> Total do Cofre em Reais");
        System.out.println("");
    }

    // Metodo para definir o tipo de moeda que o usuario quer guardar
    public String tipoMoeda() {
        // Laco para validacao da entrada do tipo de moeda, ele aceita somente
        // INT de entrada e retorna STR de saida com 3 tipos de moedas.
        // Neste laco ha validacao do tipo de entrada para o usuario nao errar
        while (true){
            
            System.out.println("\n#################");
            System.out.println("QUAL TIPO DE MOEDA VOCÊ DESEJA:");
            System.out.println("    [ 1 ]  >>>> REAL (R$)");
            System.out.println("    [ 2 ]  >>>> DÓLAR (US$)");
            System.out.println("    [ 3 ]  >>>> EURO (EU$)\n");

            try {
                // Testa se e um inteiro, qq coisa diferente ele refaz o menu
                respUser = teclado.nextInt();
            } catch(InputMismatchException e) {
                teclado.nextLine();
                
            }
        // Retorno do tipo de moeda    
        if(respUser == 1) {
            return "Real";
        }
        else if(respUser == 2) {
            return "Dólar";
        }
        else if(respUser == 3) {
            return "Euro";
        }
        else{System.out.println("\nDIGITE UMA OPÇÃO VÁLIDA !!!!!!!!");
        }
        }
    }

    // Metodo para validar o valor de entrada da moeda e para encerrar o loop
    // que fica inserindo moedas no cofre
    public double recebeValor() {
        while (true) {
            System.out.println("        DIGITE O VALOR ou [ 0 ] para sair: ");
            try {
                vlrUser = teclado.nextDouble();
                return vlrUser;
                
            } catch (InputMismatchException e) {
                System.out.println("\n          DIGITE UM VALOR INTEIRO OU COM ',' !");
                teclado.nextLine();
            }
            
        }
    }
}
