
public class Conta {
    int num_cc;
    String cliente;
    int saldo;
    int lim;

    public Conta(int num_cc, String cliente, int saldo, int lim) {
        this.num_cc = num_cc;
        this.cliente = cliente;
        this.saldo = saldo;
        this.lim = lim;
    }

    void info(){
        System.out.println("Valor em CC >> R$" + saldo);
    }

    // Maneira para retornar um boleano do metodo
    boolean sacar(int valor) {
        // Se eu determinar o retorno de boleano, preciso entrar com o RETURN nas partes do metodo
        if(valor > lim || valor > saldo) {
            return false;
        }
        saldo -= valor;
        return true;
    }

    boolean depositar(int valor) {
        if(valor < 0 ) {
            return false;
        }
        saldo += valor;
        return true;
    }
}
