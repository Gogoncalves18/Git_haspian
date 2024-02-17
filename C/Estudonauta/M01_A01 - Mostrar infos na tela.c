// PRINTF(""); - comando para apresentar o print no terminal

#include <stdio.h>
#include <locale.h> //Biblioteca para definir a linguagem para os caracteres de saida 

void main() {
    setlocale(LC_ALL, "Portuguese"); //Cmd para definir localidade e lingua para as saidas de print
    printf("Ola nova linguagem! \nTudo bem contigo. \nSera que vou te dominar\nLa vamos nos\n C e \n\"SUPER\" \nFacil! ");
    //E necessario colocar "\n" para fazer o print pular de linha, mesmo que se usarmos varios comando do print
    /*
    Segue comandos da linguagem para formatar a saida do print:
    \n - Nova linha
    \t - Tabulacao, para adicionar 4 espacos como se fosse um tab
    \b - backspace
    \\ - para colocar barra no print
    \" - para usar aspas na saida 
    \? - interrogacao
    \a - emite um beep
    %%  - para colocar um % no print
    \r - retorno do carro, o que estiver a frente de "\r", voltara para o inicio da saida na mesma linha
    */
}