package Uninter.POO_Java.Aula5.A05.class_abstrata;

public class Desktop extends Computador{
    double acessorios;

    // Construtor desta classe segue o mesmo padrao de qq classe, mesmo que herdada em 
    // de uma classe abstrata

    public Desktop(int gbMemoria, int numProcessadores, double acessorios) {
        super(gbMemoria, numProcessadores);
        this.acessorios = acessorios;
    }

    // Uso esta marcacao "@Override" para determinar que estou sobre escrevendo
    // um metodo. Abaixo dele eu preciso implementar os metodos que eu impus na
    // classe abstrata criada em "Computador.java"
    @Override
    double calculaValor() {
        double total = 200*gbMemoria + 400*numProcessadores + acessorios;
        return total;
    }
}
