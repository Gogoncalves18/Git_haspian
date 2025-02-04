package empresa;

public class Avaliacao {
    // Aqui escrevemos os atributos da classe
    double n1, n2, n3;

    // Maneira que escrevo o construtor da classe
    Avaliacao(double n1, double n2, double n3) {
        this.n1 = n1;
        this.n2 = n2;
        this.n3 = n3;
    }

    // Metodos
    public double mediaAritimetica() {
        return (n1 + n2 + n3)/3;
    }

    public double mediaPoderada() {
        return (n1*2 + n2*3 + n3*4) / 9;
    }
}
