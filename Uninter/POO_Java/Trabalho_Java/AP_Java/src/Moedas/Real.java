package Moedas;
import Classes_Abstratadas.*;

public class Real extends Moeda {
    double vlr_convert_reais;

    public Real(double valor, String tipoMoeda) {
        super(valor, tipoMoeda);
    }

    @Override
    public void info() {
        System.out.println("Tipo de Moeda: " + tipoMoeda + ">>>> Valor: R$" + valor);
    }

    @Override
    public double converter() {
        vlr_convert_reais = valor;
        return vlr_convert_reais;
    }

}
