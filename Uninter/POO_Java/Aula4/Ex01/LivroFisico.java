package Uninter.POO_Java.Aula4.Ex01;

// Esta classe é uma heranca da classe livro, desta forma abaixo que herdamos de outra 
// classe os atributos "extends"
public class LivroFisico extends Livro {
    private int tiragem;
    private int peso;

    // o construtor de uma heranca deve receber todos os atributos anteriores e mais os atuais
    public LivroFisico(String titulo, Autor autor, String genero, int edicao, int tiragem, int peso) {
        // aqui entra o super para pegar os atributos do pai
        super(titulo, autor, genero, edicao);
        this.tiragem = tiragem;
        this.peso = peso;
    }


    public int getTiragem() {
        return tiragem;
    }
    public void setTiragem(int tiragem) {
        this.tiragem = tiragem;
    }

    public int getPeso() {
        return peso;
    }
    public void setPeso(int peso) {
        this.peso = peso;
    }

    public void info() {
        super.infolivro();
        System.out.println("Tiragem: " + tiragem);
        System.out.println("Peso: " + peso);
    }
}
