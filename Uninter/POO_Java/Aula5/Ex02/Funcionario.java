package Uninter.POO_Java.Aula5.Ex02;

// Veja que a maneira de implementar uma interface é diferente que implementar 
// uma classe abstrata
public class Funcionario implements Imprimivel{
    String nome;
    String cpf;

    public Funcionario(String nome, String cpf) {
        this.nome = nome;
        this.cpf = cpf;
    }

    @Override
    public void imprimir() {
        System.out.println("");
        System.out.println(" Nome: " + nome + "com CPF" + cpf);
        System.out.println("###################");
    }

}
