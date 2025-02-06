package Uninter.POO_Java.Aula5.Ex02;

public class Quadrado implements  Imprimivel{
    int medidalado;

    public Quadrado(int medidalado) {
        this.medidalado = medidalado;
    }

    @Override
    public void imprimir() {
        System.out.println("");
        System.out.println(" Quadrado com: " + medidalado + "mm");
        System.out.println("###################");
    }

     public double resultdobrado() {
        return medidalado*2;
    }

}
