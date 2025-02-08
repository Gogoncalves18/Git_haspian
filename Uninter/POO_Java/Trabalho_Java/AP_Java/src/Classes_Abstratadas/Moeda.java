package Classes_Abstratadas;

public abstract class Moeda {
    // Classe para definir o que precisa para uma moeda ser considerada moeda
    // Necessario tipo e valor, cada moeda possui sua variavel de conversao para real
    public double valor;
    public String tipoMoeda;

    public Moeda(double valor, String tipoMoeda) {
        this.valor = valor;
        this.tipoMoeda = tipoMoeda;
    }

    // Metodo para apresentar as informações sobre o objeto moeda
    public abstract void info();

    // Metodo para executar a conversao para real
    public abstract double converter();
}
