package Uninter.POO_Java.Aula5.Ex02;

public class main {
    public static void main(String[] args) {
        // Neste codigo vamos implementar uma interface que é utilizada
        // por 3 metodos totalmente diferentes um do outro

        Funcionario f = new Funcionario("Ricardao", "222.435.999-22");
        Carro c = new Carro("Fusca", "Preto", 2);
        Quadrado q = new Quadrado(10);

        // Crio uma referencia para a interface e a partir dela instancio as classes.
        // este tambem é um caso de polimorfismo

        Imprimivel imp;
        imp = f;
        f.imprimir();
        imp = c;
        c.imprimir();
        imp = q;
        q.imprimir();
        Double res;
        res = q.resultdobrado();
        System.out.println("Valor = "+ res);
    }
}
