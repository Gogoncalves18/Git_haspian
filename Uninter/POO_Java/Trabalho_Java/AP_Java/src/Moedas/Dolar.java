package Moedas;
import Classes_Abstratadas.*;

public class Dolar extends Moeda {
    double vlr_convert_reais;

    public Dolar(double valor, String tipoMoeda) {
        super(valor, tipoMoeda);
    }

    @Override
    public void info() {
        System.out.println("Tipo de Moeda: " + tipoMoeda + ">>>> Valor: US$" + valor);
    }

    @Override
    public double converter() {
        vlr_convert_reais = valor * 4;
        return vlr_convert_reais;
    }

}
