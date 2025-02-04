public class main {

    public static void main(String[] args) {
        // aqui estou instaciando sem parametros, ai nao preciso do construtor na classe Nota
        Nota mario = new Nota();
        mario.setNota1(9);
        mario.setNota2(10);

        mario.resultado();

        mario.setNota1(2);

        mario.resultado();

        // Exercicio 02

        mario.setFaltas(10);

        mario.resultado();

    }
}
