package Uninter.POO_Java.Aula3.ex04;
import java.util.ArrayList;

public class Cofrinho {
    // arraylist é uma biblioteca de construção de array ao qual posso adicionar objetos
    // e o arraylista esta tipado com classe moeda
    private ArrayList<Moeda> moedas = new ArrayList();

    // como possuo um obj criado acima chamado moedas, insiro uma os
    // valores la dentro
    void add(Moeda m) {
        moedas.add(m);
    }

    public double calcularTotal() {
        double totalMoedas = 0;
        // no for eu declaro o que eu estou percorrendo (no caso a classe moeda)
        // sendo que vlr representa os valores dentro do Arraylist
        for(Moeda vlr : moedas) {
            // o "getValor()" é uma função do arraylist
            totalMoedas += vlr.getValor();
        }
        return totalMoedas;
    }
}
