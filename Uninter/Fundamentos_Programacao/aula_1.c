#include <stdio.h>
/*
obter as notas
calcular a media
verificar sse reprovou
*/
int main(void) //Preciso usar o main como padrao da funcao
{
    float nota1, nota2, media; //Declaracao de variaveis
    printf("Digite a primeira nota:"); //Pego no terminal o input
    scanf("%f", &nota1); //Escrevo na variavel o valor 

    printf("Digite a segunda nota:"); //Pego no terminal o input
    scanf("%f", &nota2); //Escrevo na variavel o valor 

media = (nota1 + nota2)/2;

if(media >= 7)
printf("Aprovado");
else
printf("Reprovado");    

    return 0;
}