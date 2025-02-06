package Uninter.POO_Java.Aula5.A05.class_abstrata;

public class main {

    public static void main(String[] args) {
        // Criamos os objetos que vamos instaciar para classes desktop e notebook

        Desktop compA = new Desktop(8, 4, 600);
        Notebook compB = new Notebook(8, 4, 15);
        
        // Aqui para deixar o codigo mais simples para baixo, é criado uma
        // variavel "comp" baseada na classe "Computador", assim eu posso
        // Instaciar nela tanto o objeto "compA" como o objeto "compB". A 
        // classe abstrata me ajuda a manter a logica da estrutura, ao qual
        // garante que os mesmos metodos que tenho em uma classe, existao em 
        // outra classe
        Computador comp;

        comp = compA;
        System.out.println("");
        System.out.println("Valor Desk = " + comp.calculaValor());
        System.out.println("*************************");

        comp = compB;
        System.out.println("");
        System.out.println("Valor Note = " + comp.calculaValor());
        System.out.println("¨¨¨¨¨¨¨¨¨¨¨¨¨¨");
    }
}
