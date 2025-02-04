package Uninter.POO_Java.Aula4.Ex01;

public class Autor {
    private String nome;
    private String nacionalidade;
    private String email;

    // Instancio um obj sem paramentro e abaixo outro com o parametro,
    // assim a clase aceita das duas formas
    public Autor() {}

    public Autor(String nome, String nacionalidade, String email) {
        super();
        this.nome = nome;
        this.nacionalidade = nacionalidade;
        this.email = email;
    }

    // Metodos para setar e obter atributos
    public String getNome() {
        return nome;
    }

    public void setNome(String name) {
        this.nome = name;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public void setNacionalidade(String pais) {
        this.nacionalidade = pais;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail (String mail) {
        this.email = mail;
    }

    void info() {
        System.err.println("");
        System.out.println("Nome Autor: " + nome);
        System.out.println("Nacionalidade: " + nacionalidade);
        System.out.println("Email Autor: " + email);
        System.err.println("");
    }
}
