package Uninter.POO_Java.Aula5.A05.class_abstrata;

// Maneira para criar uma classe abstrata para uso no codigo
public abstract class Computador {
    int gbMemoria;
    int numProcessadores;

    // Construtores da classe abstrata é igual a classe normal

    public Computador(int gbMemoria, int numProcessadores) {
        this.gbMemoria = gbMemoria;
        this.numProcessadores = numProcessadores;
    }

    // Iniciando o metodo por "abstract", eu indico que obrigatoriamente este 
    // metodo devera ser implementado por qualquer instancia que herdar esta classe
    abstract double calculaValor();
}
