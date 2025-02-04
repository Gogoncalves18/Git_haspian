package Uninter.POO_Java.Aula4.Ex01;

public class LivroDigital extends Livro {
    private int download;
    private double tamanho;

    // o construtor de uma heranca deve receber todos os atributos anteriores e mais os atuais
    public LivroDigital(String titulo, Autor autor, String genero, int edicao, int download, double tamanho) {
        // aqui entra o super para pegar os atributos do pai
        super(titulo, autor, genero, edicao);
        this.download = download;
        this.tamanho = tamanho;
    }


    public int getDownload() {
        return download;
    }
    public void setDownload(int download) {
        this.download = download;
    }

    public double getTamanho() {
        return tamanho;
    }
    public void setTamanho(double tamanho) {
        this.tamanho = tamanho;
    }

    public void info() {
        super.infolivro();
        System.out.println("DOWN: " + download);
        System.out.println("GBytes: " + tamanho);
    }
}
