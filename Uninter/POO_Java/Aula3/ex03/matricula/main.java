package Uninter.POO_Java.Aula3.ex03.matricula;

public class main {
    public static void main(String[] args) {
        Aluno a1 = new Aluno("Gus", 111, 0.1, new Curso("Engenharia", 1000));

        // Este info aqui é da classe aluno, dentro dela eu chamo outra classe que
        // o mesmo metodo
        a1.info();

        System.out.println("Pagamento: " + a1.pagamento());
    }
}
