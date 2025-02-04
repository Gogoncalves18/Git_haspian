package Uninter.POO_Java.Aula3.ex04;

public class main {
    public static void main(String[] args) {
        Cofrinho cof = new Cofrinho();

        cof.add(new Moeda("Euro", 0.5));
        cof.add(new Moeda("Euro", 1));
        cof.add(new Moeda("Euro", 0.1));
        cof.add(new Moeda("Euro", 0.05));

        // para formatar a saida do dado é necessario usar o "PRINTF" e dentro
        // da expressao usar '%.2f \n",'
        System.out.printf("O total no cofre é: %.2f \n", + cof.calcularTotal());
    }

}
