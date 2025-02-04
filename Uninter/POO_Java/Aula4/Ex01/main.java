package Uninter.POO_Java.Aula4.Ex01;

public class main {
    public static void main(String[] args) {
        // maneira de criar um obj dentro de outro objeto em uma instancia
        LivroDigital ldig = new LivroDigital("Matrix",
        new Autor("RR Paul", "EUA", "peganomeu@gmail.com"),
        "Acao", 2, 5000, 2.50);

        ldig.info();
    }

}
