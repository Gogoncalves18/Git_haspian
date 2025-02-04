package empresa;

// Classe de inicializacao
public class Principal {
    // metodo para inicializar
    public static void main(String[] args) {
        // cria uma classe chamada "Avaliacao" ao qual instacia Mario em um construtor
        // Exercicio 01
        Avaliacao mario = new Avaliacao(7, 4, 10);
        
        // Print dos dados
        System.out.println("Media Aritimetica do Mario: "+ mario.mediaAritimetica());
        System.out.println("Media Ponderada do Mario: " + mario.mediaPoderada());
        
        // Exercicio 02
        Aluno a1 = new Aluno("Rique", "Encanador", new Avaliacao(9, 10, 3));
        Aluno a2 = new Aluno("Ze", "Encanador", new Avaliacao(4, 1, 10));
        
        a1.info();
        a2.info();
    }
}
