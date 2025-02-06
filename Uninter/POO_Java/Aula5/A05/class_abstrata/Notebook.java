package Uninter.POO_Java.Aula5.A05.class_abstrata;

public class Notebook extends Computador{
    int polegadasTela;

    // Construtor desta classe segue o mesmo padrao de qq classe, mesmo que herdada em 
    // de uma classe abstrata
    public Notebook(int gbMemoria, int numProcessadores, int polegadasTela) {
        super(gbMemoria, numProcessadores);
        this.polegadasTela = polegadasTela;
    }

    // Uso esta marcacao "@Override" para determinar que estou sobre escrevendo
    // um metodo. Abaixo dele eu preciso implementar os metodos que eu impus na
    // classe abstrata criada em "Computador.java"
    @Override
    double calculaValor() {
        double total = 250*gbMemoria + 500*numProcessadores + 100*polegadasTela;
        return total;
    }
}
