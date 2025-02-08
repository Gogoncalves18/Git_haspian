package Moedas;
import Classes_Abstratadas.*;

public class Euro extends Moeda {
    double vlr_convert_reais;

    public Euro(double valor, String tipoMoeda) {
        super(valor, tipoMoeda);
    }

    @Override
    public void info() {
        System.out.println("Tipo de Moeda: " + tipoMoeda + ">>>> Valor: EU$" + valor);
    }

    @Override
    public double converter() {
        vlr_convert_reais = valor * 6;
        return vlr_convert_reais;
    }

}
