package Uninter.POO_Java.Aula3.ex03.matricula;

public class Aluno {
    String nome;
    int matricula;
    double desconto;
    Curso curso_matriculado;

    Aluno(String nome, int matricula, double desconto, Curso curso_matriculado) {
        super();
        this.nome = nome;
        this.matricula = matricula;
        this.desconto = desconto;
        this.curso_matriculado = curso_matriculado;
    }

    void info(){
        System.out.println("Nome Aluno: " + nome);
        System.out.println("Matricula Aluno: " + matricula);
        System.out.println("Desconto Aluno: " + desconto);
        curso_matriculado.info();
    }

      // Como vou retornar algo, nao uso o DOUBLE
      double pagamento(){
        return curso_matriculado.mensalidade * (1 - desconto);
    }
}
