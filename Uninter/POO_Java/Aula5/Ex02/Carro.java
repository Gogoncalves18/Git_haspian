package Uninter.POO_Java.Aula5.Ex02;

public class Carro implements Imprimivel{
    String marca;
    String cor;
    int portas;

    public Carro(String marca, String cor, int portas) {
        this.marca = marca;
        this.cor = cor;
        this.portas = portas;
    }

    @Override
    public void imprimir() {
        System.out.println("");
        System.out.println(" Carro: " + marca + "tem cor" + cor + "com n portas" + portas);
        System.out.println("###################");
    }
}
