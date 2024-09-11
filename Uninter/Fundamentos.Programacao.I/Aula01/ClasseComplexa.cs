namespace Aula01;

// Class criada atraves da Solution, via criar arquivo tipo class

// Forma de criar a classe e fazer ela herdar uma interface da funcao
// ImprimirValores que esta dentro do Interface.cs
public class ClasseComplexa : ImprimirValores
{
    // Esta propriedade esta definida como privada, nem ela e nem 
    // protegida permitirao acessar ou escrever seus dados atraves de 
    // herancas para outras funcoes. O { get; set; } e para definir valores
    // e obter valores da propriedade
    private int PropInt { get; set; }
    protected bool PropBool { get; set; }
    public decimal PropDecimal { get; set; }
    protected DateTime dataAtual;
    float FloatField;

    public Direcoes Direcao { get; set; }

    // Como eu herdei o ImprimirValores acima, aqui preciso torna-la 
    // acessivel dentro desta funcao, sendo que este PropInterface e 
    // uma propriedade de outra funcao
    public string PropInterface { get; set; }

    // Toda propriedade tipo ENUM se comporta como uma dict
    public enum Direcoes
    {
        Cima = 1,
        Baixo = 10,
        LadoEsquerdo = 20,
        LadoDireito = 67,
    }
}
