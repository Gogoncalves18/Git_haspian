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
- No LINQ é impressendível trabalharmos com LAMBDA que podemos ter as seguintes expressões:
    - (input-param) => expression
    - (input-param) => { <sequencia de codigo>}
- Há dois métodos de encapsulamento:
    - ACITION e ACTION<T> - este pode receber param e *não retornar* valores
    - FUNC<T> - este pode receber param e *retornar* _valores_
