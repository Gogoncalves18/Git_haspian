package Uninter.POO_Java.Aula4.Ex01;

public class Livro {
    private String titulo;
    private Autor autor;
    private String genero;
    private int edicao;

    public Livro(String titulo, Autor autor, String genero, int edicao) {
        this.autor = autor;
        this.titulo = titulo;
        this.genero = genero;
        this.edicao = edicao;
    }

    public Autor getAutor() {
        return autor;
    }

    // maneira de setar uma instancia de obj no atributo privado
    public void setAutor(Autor autor) {
        this.autor = autor;
    }

    public String getTitulo() {
        return titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }


    public String getGenero() {
        return genero;
    }
    public void setGenero(String genero) {
        this.genero = genero;
    }
    
    public int getEdicao() {
        return edicao;
    }
    public void setEdicao(int edicao) {
        this.edicao = edicao;
    }

    void infolivro() {
        System.err.println("");
        System.out.println("Titulo Livro: " + titulo);
        System.out.println("Genero livro: " + genero);
        System.out.println("Edicao: " + edicao);
        // vaja que a linha de baixo eu estou pegando o nome do autor que esta
        // dentro da classe autor no atributo do objeto que pertence aquela classe
        System.out.println("Nome Autor: " + autor.getNome());
        System.err.println("");
    }

}    

