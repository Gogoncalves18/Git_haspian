package Uninter.POO_Java.Aula5.Ex02;

// A ideia aqui é que uma "interface" é quase igual a um metodo abstrato. A diferenca
// e que interface eu posso implementar varios dentro das classe e o "abstrato" eu posso
// usar um apenas por classe. Neste caso estamos forcando a implementacao do 
// metodo "imprimir()" em 3 classes que sao totalmente diferentes uma da outra
public interface Imprimivel {
    void imprimir();
}
