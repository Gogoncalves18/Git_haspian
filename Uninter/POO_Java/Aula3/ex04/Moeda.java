package Uninter.POO_Java.Aula3.ex04;

public class Moeda {
    private String nome;
    private double valor;

    public Moeda(String nome, double valor) {
        super();
        this.nome = nome;
        this.valor = valor;
    }
    // metodos para manipular os atributos privados
    public String getNome(){
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;

    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

}
