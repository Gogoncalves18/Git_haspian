public class main {

    public static void main(String[] args) {
        Conta c1 = new Conta(111, "Valquiria", 2000, 500);

        c1.info();
        // Condicional para validar se é verdadeiro ou não o retorno
        if(!c1.sacar(200)){
            System.out.println("");
            System.out.println("Problemas ao sacar!!!!");
        }
        

        c1.depositar(500);

        c1.info();
    }
}
