package empresa;

public class Aluno {
    String nome, curso;
    Avaliacao aval;

    Aluno(String nome, String curso, Avaliacao aval){
        this.nome = nome;
        this.curso = curso;
        this.aval = aval;
    }

    // metodo comeca com "VOID" porque ele nao retorna nada
    void info(){
        System.err.println();
        System.out.println("Nome: " + nome);
        System.out.println("Curso: " + curso);
        System.out.println("Media aritimetica: " + aval.mediaAritimetica());
        System.out.println("Media ponderada: " + aval.mediaPoderada());

    }

}
