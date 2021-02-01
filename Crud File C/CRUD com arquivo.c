#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <locale.h>

int cont=0;
int p=0;
int x=0;

struct jogos{
    char nome[40];
    char genero[40];
    int codigo;
    int ano;
    char valido;
}game[200];

void pesquisa1(){
    setlocale(LC_ALL, "Portuguese");
    int a;
    char nome[40];
    system("cls");
    printf("-PROCURANDO O JOGO-\n");
    printf("\n");
    printf("Digite Jogo: ");
    fflush(stdin);
    gets(nome);
    printf("\nBUSCANDO......................... Acesse -> www.vitiss.com.br ......<-   ");
    Sleep(1000);
    for(a=0;a<200;a++){
        if(game[a].valido=='C'){
            if(!strcmp(nome,game[a].nome)){
                printf("\n-------------------------------------------------------------------\n");
                printf("\nJogo: %s\n", game[a].nome);
                printf("\nGenero: %s\n", game[a].genero);
                printf("\nCódigo: %d\n", game[a].codigo);
                printf("\nAno de Lançamento: %d\n", game[a].ano);
                printf("\n-------------------------------------------------------------------\n");
                system("pause");
                return;
           }
        }
    }
    printf("\nJogo nao encontrado.\n");
    Sleep(2000);
    return;
}

int pesquisa4(char nome[40]){
    setlocale(LC_ALL, "Portuguese");
    int a;
    for(a=0;a<200;a++){
        if(!strcmp(nome,game[a].nome)){
            x=a;
            return 1;
        }
    }
    return 0;
}

void alterar(){
    setlocale(LC_ALL, "Portuguese");
    char nome[40],generonew[40];
    int resultado,codigonew;
    int resp;
    system("cls");
    printf("-POWER BOMB GAMES-\n");
    printf("-ALTERAÇÃO DOS JOGOS-\n");
    printf("\n");
    printf("Nome do Jogo \n");
    fflush(stdin);
    gets(nome);
    pesquisa4(nome);
    resultado=pesquisa4(nome);
    if(resultado==1){
        printf("Alterar Genero ou Código ?\n\n");
        printf("\tGenero__________[1]\n");
        printf("\tCódigo__________[2]\n");
        printf("\n__________________________\n");
        scanf("%d", &resp);
        switch(resp)
{
	case 1:
	printf("Novo Genero: ");
        fflush(stdin);
        gets(generonew);
        strcpy(game[x].genero,generonew);
        printf("\nAlteração concluída com sucesso.\n");
        Sleep(1000);
	break;

	case 2:
	printf("Novo Código: ");
        fflush(stdin);
        scanf("%d", &codigonew);
        game[x].codigo=codigonew;
        printf("\nAlteração concluída com sucesso.\n");
        Sleep(1000);
	break;
}
    printf("\nAlterado com Sucesso. - POWER BOMB GAMES -\n");
    Sleep(2000);
    return;
}
}
int pesquisa3 (char nome[40]){
    setlocale(LC_ALL, "Portuguese");
    int a;
    for(a=0;a<200;a++){
        if(!strcmp(nome, game[a].nome)){
            p=a;
            return 1;
        }
    }
    return 0;
}

void excluir(){
    setlocale(LC_ALL, "Portuguese");
    char nome[40];
    int result;
    system("cls");
    printf("-POWER BOMB GAMES-\n");
    printf("-EXCLUSÃO DE JOGOS-\n");
    printf("\n");
    printf("Jogo que deseja exluir: ");
    fflush(stdin);
    gets(nome);
    pesquisa3(nome);
    result=pesquisa3(nome);
    if(result==1){
        game[p].valido='E';
        printf("Jogo Exluído.\n");
        Sleep(2000);
        return;
    }
    printf("Jogo não encontrado\n.");
    Sleep(2000);
    return;
}

int pesquisa2(char nome[40]){
    int a;
    for(a=0;a<200;a++){
        if(!strcmp(nome,game[a].nome)){
            return 1;
        }
    }
    return 0;
}

void incluir(){
    setlocale(LC_ALL, "Portuguese");
    int resultado;
    char nome[40];
    system("cls");
    printf("-CADASTRO DE JOGOS-                       |\n");
    printf("-POWER BOMB GAMES- Ligue[3221-2011]       |\n");
    printf("-ACESSE www.vitiss.com.br                 |\n");
    printf("__________________________________________");
    printf("\n");
    printf("\nDigite o nome do Jogo: ");
    fflush(stdin);
    gets(nome);
    pesquisa2(nome);
    resultado=pesquisa2(nome);
    if (resultado==1){
        printf("Jogo ja cadastrado.");
        system("pause");
        return;
    }
    strcpy(game[cont].nome,nome);
    printf("\n");
    printf("\nDigite o genero do Jogo: ");
    scanf("%s", &game[cont].genero);
    printf("\n");
    printf("\nDigite o Código do Jogo: ");
    scanf("%d", &game[cont].codigo);
    printf("\n");
    printf("\nDigite o Ano de Lançamento: ");
    scanf("%d", &game[cont].ano);
    printf("\n");
    game[cont].valido='C';
    printf("\nCadastro completo.\n");
    cont++;
    Sleep(2000);
}

void listar (){
    setlocale(LC_ALL, "Portuguese");
    int a;
    system("cls");
    printf("-POWER BOMB GAMES-\n");
    printf("-LISTAGEM DOS JOGOS-\n");
    printf("\n");
    for(a=0;a<200;a++){
        if(game[a].valido=='C'){
            printf("----------------------------------------------------------------------\n");
            printf("Jogo: %s\n", game[a].nome);
            printf("Genero: %s\n", game[a].genero);
            printf("Código: %d\n", game[a].codigo);
            printf("Ano de Lançamento: %d\n", game[a].ano);
            printf("----------------------------------------------------------------------\n");
            printf("\n");

        }
    }
    printf("- POWER BOMB GAMES - Ligue: [3221-2011]\n");
    system ("pause");
    return;
}

void menu(){
    setlocale(LC_ALL, "Portuguese");
   int opcao;
   do{
    system ("cls");
    printf("--------------------------------------------------\n");
    printf("\tPOWER BOMB GAMES                         |\n");
    printf("\tVender Barato é Tradição                 |\n");
    printf("\t3221-2011                                |\n");
    printf("\tACESSE www.vitiss.com.br                 |\n");
    printf("--------------------------------------------------\n");
    printf("\tCadastrar ______________________ [1]     |\n");
    printf("\tPesquisar ______________________ [2]     |\n");
    printf("\tAlterar ________________________ [3]     |\n");
    printf("\tExcluir ________________________ [4]     |\n");
    printf("\tListar _________________________ [5]     |\n");
    printf("\tSair ___________________________ [0]     |\n");
    printf("--------------------------------------------------\n");
    printf("Digite sua opcao: ");
    scanf("%d", &opcao);
    switch(opcao){
        case 1: incluir(); break;
        case 2: pesquisa1(); break;
        case 3: alterar ();break;
        case 4: excluir ();break;
        case 5: listar ();break;
        case 0: exit(1);
        default: printf("ERROR\n");
    }
   }while (opcao!=0);
}

void main(){
    system("color e4");
    menu();
}
