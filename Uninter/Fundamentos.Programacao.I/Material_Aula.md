# Fundamentos de Programação com C#
## Array

- Estrutura de armazenamento de tamnho fixo em implementação nativa CLR, do mesmo tipo
- Ele é um conjunto contiguo de elementos na memória  e é herdado da class System.Array
- Dentro dos array nós temos coleções como pilhas, filas...
- Mesmo sendo de uma classe, ela implementa algumas "interfaces" do universo da collection
![alt text](image.png)
- Um array não pode aumentar de tamanho

## Generics
- Mecanicanimos para auxiliar na reutilização de códigos com Heranças e Genéricos
- Eles são como templates, o uso de generics é representado como "<T>"
- Exemplo de uma Pilha Customizada usando "Generics"
- O "T" podem ser substituido por qualquer type desde que seja em tempo de compilação do código
![alt text](image-1.png)
- A vantagem de trabalhar com uma "Generic" ao invés de uma "OBJ" é que quando manipulo uma array, eu preciso me atentar ao type do dado, caso contrário posso levantar uma excessão caso não defina o que estou manipulando em caso de estar mexendo em array com mais de um tipo de dado.
- Há maneira de limitar os Generics com constraints, como o exemplo abaixo:
![alt text](image-2.png)
    - Neste caso os ":" são utilizados para herança ou implementação 
    ![alt text](image-3.png) 

## Arrays, List, Sets, Dicts e Collections

- A Colection IEnumerator é uma protocolo que percorre um array de maneira sequencial:
![alt text](image-4.png)
- Sempre que utilizamos o IEnumarable, ele gera internamente um IEnumarator para enumerar os itens para percorrer o array
![alt text](image-5.png)
- A interface IList permite acessarmos:
    ![alt text](image-6.png)
- HashSet é uma class que implementa um array que guarda o valor e sua posição, sua característica é de não permitir a duplicação de elementos e sua performance é excelente
- As Dict é uma estruct:    
    ![alt text](image-7.png)
- ![alt text](image-8.png)

## Conversões entre Collection

- Todas as Collection são armazenados em Array

## LINQ

- LINQ permite que consulte qualquer coleção que implemente IEnumerable<T>, Array, Lista ou XML DOM, fontes de dados remota, BD SQL. Ele é a unificação da tipagem em tempode compilação e composição de consultas dinâmicas em coleções.
- Há dois de notações para LINQ:
    - Fluent Syntax
        - É a principal forma de percorrer uma Collection ou filtrar uma Collection
        -----------------------
        ![alt text](image-9.png)
        -----------------------
        - Nesta notação podemos encadear os operadores em uma forma de *PIPELINE*,  (uma espécie de fluxo ou esteira dos dados), com os operadores podemos: **Filtrar, Ordenar, Agregar, Agrupar, Unir e Converter**
        -----------------------
        ![alt text](image-10.png)
        -----------------------
        - Importante destacar que sempre que a Function tiver **2 param**, o primeiro será o de entrada e o segundo o de retorno da function, como o exemplo abaixo, o retorno será um boleano:
        -----------------------
        ![alt text](image-11.png)

        ![alt text](image-12.png)
        -----------------------
        - Um operador de consulta LINQ **NUNCA** altera a sequência de entrada, ele só retornará uma nova sequência de dados, mas respeitando a primeira.
        - Também posso ter uma entrada "T" e uma saída "Y" na tipagem de dados, o ex abaixo mostra uma entrada em STR leio os items da listar e retorno os comprimentos de cada dado, sua saída está sendo convertida para um INT por isto que ele está dentro de <> e ainda está sendo implementado um IEnumerable para podermos interar sobre ela.
        -----------------------
        ![alt text](image-13.png)
        -----------------------

    - Query Expression
        - Síntaxe parecida como escrever SQL. Abaixo um exemplo parecido com o de cima.
        ------------------------
        ![alt text](image-14.png)

        ![alt text](image-15.png)
        - No exemplo abaixo estamos utilizando um mix das duas linguagem, na funcao **mixQueries**, estamos:
            - percorrendo um "N" in uma "ARRAY"
            - Executando um JOIN do NOMEY in um novo ARRAY
            - Este segundo array vem um uma função lambda que retorna palavras que contem a letra Y
            - O join jogará o resultado de N sobre as palavras igual do resultado de NOMEY
            - Depois ele seleciona o resultado para elementos que possui mais que 3 letras com WHERE
            - E por fim jogamos o resultado para maiusculo com n.ToUpper e ordenamos de forma descrescente
            ![alt text](image-16.png)



- No LINQ é impressendível trabalharmos com LAMBDA que podemos ter as seguintes expressões:
    - (input-param) => expression
    - (input-param) => { <sequencia de codigo>}
- Há dois métodos de encapsulamento:
    - ACITION e ACTION<T> - este pode receber param e *não retornar* valores
    - FUNC<T> - este pode receber param e *retornar* _valores_

## Execução Tardia ( Deffered Execution ou Lazzi Execution)

- Conceito deste tipo de execução é que ela não é executada no momento que é construída, é executada somente após chamarmos ela. O exemplo abaixo define isto, CORREÇÃO, no lugar da query em foreach, é o nome do segundo VAR:
    ![alt text](image-17.png)
    - Assim podemos reutiliza-la e reprogramar os dados dentro dela sempre que precisarmos

- Agora se queremos mantê-la integra, precisamos aplicar o Tolist ou ToArray, como este caso, que força uma nova coleção interna:
    ![alt text](image-18.png)

## Operadores LINQ

- Há 3 tipos de categorias de operadores:
    - "Coleção in", "Coleção Out"
    - "Coleção in", "Elemento Out"
    - Sem param, "Coleção Out"

- **Operadores de filtro**, sempre retornarão com dados na mesma qtd ou menor e sempre do mesmo TYPE:
    ![alt text](image-19.png)

- **Operadores de Projeção**, Transforma o TYPE de entrada e um novo TYPE de saída
    ![alt text](image-20.png)
    - Um operador SELECT pode retornar um TYPE ANÔNIMO que é um SYSTEM.OBJECT que possui apenas propriedades criadas em tempo de execução, para isto ele precisa ser combinado com a palavra "newm {...}"
    ![alt text](image-21.png)
    OBS.: CULTUREINFO é as linguagens instaladas no computador. Neste caso estamos montando um objeto com suas propriedades. Importante: **Neste tipo de objeto não conseguimos altera-lo e nem atribuir valores para suas propriedades**

- **Operadores de combinação**
    ![alt text](image-22.png)

- **Operadores de ordenação**
    ![alt text](image-23.png)

- **Operadores de conversão**, a grande maioria implementarão a coleção uma enumeração aos dados
    ![alt text](image-24.png)

- **Operadores de agregação**
    ![alt text](image-25.png)

## Treads

- O computador executa um processo chamado Preempção para poder executar várias tarefas ao mesmo tempo através do algotítmo Round Robin

- Diferença entre **Processos e Threads**
    - Processos são containers que executam um programa
    - A thread compõe o processo, isto é, um processo pode possuir várias threads
    - O SO realiza a preempção entre os espaços de espera das Threads

- Cada Processo possui seu próprio contexto de execução, assim o SO isola ela 

- Em C# podemos escrever várias threads e fazer o SO esperar ela ser finalizada com o método .Join() que está dentro da Threads:
![alt text](image-26.png)
- Thread.Sleep() é outra forma de espera, colocando um tempo determinado para a thread em execução
- A thread possui alguns status **Unstarded, Running, WaitSleepJoin, Stopped**
- Blocking de Threads é qq pause feito na thread
- Uma Thread é uma operação de baixo nível e não conseguimos ter retorno de valores dela, não conseguimos orquestra-las. Por esta razão o C# trabalha também com **Task** que é uma abstração de nível mais alto, estas podem ser tipadas, podem ser encadeadas e podem retornar valores
    ![alt text](image-28.png)
------------------
![alt text](image-29.png)

![alt text](image-30.png)

## Processos Assincronos e Await

- Este recurso é utilizado principalmente para processamentos pesados e para conexão com I/O para troca de dados.
- O Async/Await existem para facilitar a manipulação das Tasks e um dos benefícios é que este recurso libera a Thread, que está tocando a Task, para outros processos enquanto ela está em espera.
- **Thread Pool** é uma estrutura gerenciada pela CLR, que toda dot net tem. Ela controla a qtd de Threads disponíveis e as em execução e é ele que faz a alocação de uma nova Thread junto com o SO.
    ![alt text](image-31.png)

    ![alt text](image-32.png)

## Async/Await e Bounded Conext

![alt text](image-33.png)
![alt text](image-34.png)
![alt text](image-35.png)
![alt text](image-36.png)

- O controle dos I/O estão dentro do system.io
    ![alt text](image-37.png)

- Async/Await é indicado ser usado para esperar um I/O principalmente nos seguintes casos:
    ![alt text](image-38.png)

## CONEXÃO A BD via .NET

- Estudo sobre o **Entity Frameworks**
    ![alt text](image-39.png)
    ![alt text](image-40.png)
    *Lembrando que um NUGET é um framework fora

- Modelos de BD:
    ![alt text](image-41.png)
    ![alt text](image-42.png)

- Polimorfismo e herança não são funções que possui uma representação real no BD, assim como na POO

- Cenário para aula:
    ![alt text](image-43.png)

- Método mais importante do Framework:
    ![alt text](image-44.png)
    ![alt text](image-45.png)

- Como instanciar uma class do DB
    ![alt text](image-46.png)
    ![alt text](image-47.png)
    ![alt text](image-48.png)
    ![alt text](image-49.png)

- Correlação mais completa entre tabelas:
    ![alt text](image-50.png)

- Além do EF, temos o Dapper e o ADO.NET como Framework para conexão com o SQL
    ![alt text](image-51.png)
    ![alt text](image-52.png)
    ![alt text](image-53.png)
    ![alt text](image-54.png)
    