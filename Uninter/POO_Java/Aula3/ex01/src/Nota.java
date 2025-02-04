public class Nota {
    // Com este declaracao, nao consiguirei setar o valor de nota no main 
    // sem um metodo
    private double  nota1;
    private double  nota2;
    private int faltas;

    // Metodo que recebe atriutos privados
    void resultado() {
        double media = (nota1 + nota2)/2;

        if(media < 4) {
            System.out.println("REPROVADO");
        }
        else if(media < 7) {
            System.out.println("EXAME FINAL");
        }
        else if(faltas > 7){
            System.out.println("REPROVADO POR FALTAS");
        }
        else {
            System.out.println("Aprovado");
        }
    }
    // Metodos para setar nota ou obter nota para atributo que e privado
    public void setNota1(double nota) {
        nota1 = nota;
    }

    public void setNota2(double nota) {
        nota2 = nota;
    }

    public double getNota1() {
        return nota1;
    }

    public double getNota2() {
        return nota2;
    }

    // Exercicio 02
    public void setFaltas(int num) {
        faltas = num;
    }

    public double getFaltas() {
        return faltas;
    }

}
