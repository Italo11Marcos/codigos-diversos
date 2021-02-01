#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DIM 10

using namespace std;


void PreencherGrafo(int grafo[][DIM])
{
	int v1,v2,opt;
	system("cls");
	while(1)
	{
	system("cls");
	cout<<"1 - Inserir Conexão entre os Vertices"<<endl;
	cout<<"0 - Voltar ao Menu"<<endl;
	cout<<"\n"<<endl;
	cout<<"Digite a Opção"<<endl;
	cin>>opt;
	 if(opt==0)
			break;
	 if(opt==1){
			system("cls");
			cout<<"Digite a conexão entre os Vertices"<<endl;
				cin>>v1>>v2;
				if(v1==v2)
					cout<<"Inválido"<<endl;
				else{
					grafo[v1][v2]=1;
					grafo[v2][v1]=1;
				}
	}
	}
}

void Exibir(int grafo[][DIM],int vertices)
{
	system("cls");
	for(int i=0; i<vertices;i++)
           if(i==0){
               printf("|\tV0");
            }else if(i!=DIM){
               printf("\tV%d",i);
           }else{
              printf("\tV%d\t|",i);
           }


     for(int i=0; i<vertices;i++){
             printf("\n|V%d\t",i);
       for (int j=0;j<vertices;j++){
        printf("%d\t",grafo[i][j]);
        }
        printf("|");
        }
}

void GrauVertice(int grafo[][DIM],int vertices)
{
	system("cls");
	cout<<"\n"<<"Digite o vertice que você quer saber o grau"<<endl;
    int GVertice,cont=0;
    cin>>GVertice;
    for(int i=0; i<vertices; i++){
            if(grafo[GVertice][i]!=0){
                cont++;
            }
    }
    if(cont==0)
        cout<<"Vertice "<<GVertice<<" isolado"<<endl;
    else
        cout<<"Vertice "<<GVertice<<" tem GRAU: "<<cont<<endl;
}

void SigmaDeltaRegularTamanho(int grafo[][DIM], int vertices)
{
	system("cls");
	int vet[vertices],sigma,delta,contArestas=0,cont=0,aux;
	memset(vet, 0, sizeof(vet));
    for(int i=0; i<vertices; i++){
		cont=0;
        for(int j=0; j<vertices; j++){
            if(grafo[i][j]!=0){
				cont++;
				vet[i]=cont;
            }
        }
    }
    for(int i=0; i<vertices; i++){
		for(int j=0; j<vertices; j++){
		if(vet[i]<vet[j]){
			aux=vet[j];
			vet[j]=vet[i];
			vet[i]=aux;
		}
		if(grafo[i][j]==1){
			contArestas++;
		}

	}
}
	sigma=vet[0];
	delta=vet[vertices-1];
	cout<<"Sigma = "<<sigma<<endl;
	cout<<"Delta = "<<delta<<endl;
	if(sigma==delta)
		cout<<"O Grafo é regular - "<<"\t"<<"K"<<vertices<<endl;
	else
		cout<<"O grafo não é regular"<<endl;
	cout<<"O Tamanho do Grafo é: "<<contArestas/2<<endl;
}

void ExibirComplemento(int grafo[][DIM], int vertices)
{
	system("cls");
	int grafoComplementar[DIM][DIM];
	for(int i=0; i<vertices; i++){
        for(int j=0; j<vertices; j++){
            if(grafo[i][j]==1)
				grafoComplementar[i][j]=0;
			else
				grafoComplementar[i][j]=1;
        }
    }

    cout<<"Grafo Complementar"<<endl;
    for(int i=0; i<vertices;i++)
           if(i==0){
               printf("|\tV0");
            }else if(i!=vertices){
               printf("\tV%d",i);
           }else{
              printf("\tV%d\t|",i);
           }


     for(int i=0; i<vertices;i++){
             printf("\n|V%d\t",i);
       for (int j=0;j<vertices;j++){
        printf("%d\t",grafoComplementar[i][j]);
        }
        printf("|");
        }
}

void passeio(int grafo[][DIM])
{
	system("cls");
	int a, b;
	cout<<"Digite os Vertices "<<endl;
	cin>>a>>b;
	if(grafo[a][b]==1)
		cout<<"Exite Caminho"<<endl;
	else
		cout<<"Não Existe Caminho"<<endl;
}

void menu()
{
	system("cls");
	int vertices;
	int grafo[DIM][DIM];
	for(int i=0; i<DIM ;i++){
		for(int j=0; j<DIM; j++){
				grafo[i][j]=0;
			}
		}
	cout<<"Digite a quantidade de Vertices"<<endl;
	cin>>vertices;
	int opt;
	while(1)
	{
		cout<<"\n"<<endl;
		cout<<"0 - Sair"<<endl;
		cout<<"1 - Preencher Grafo"<<endl;
		cout<<"2 - Exibir Grafo"<<endl;
		cout<<"3 - Verificar Grau"<<endl;
		cout<<"4 - Verificar Sigma, Delta, K-Regular e Tamanho"<<endl;
		cout<<"5 - Exibir Grafo Complementar"<<endl;
		cout<<"6 - Passeio"<<endl;
		cout<<"\n"<<endl;
		cout<<"Digite a sua opção"<<endl;
	cin>>opt;
	if(opt==1)
		PreencherGrafo(grafo);
	if(opt==2)
		Exibir(grafo, vertices);
	if(opt==0)
		exit (0);
	if(opt==3)
		GrauVertice(grafo, vertices);
	if(opt==4)
		SigmaDeltaRegularTamanho(grafo, vertices);
	if(opt==5)
		ExibirComplemento(grafo, vertices);
	if(opt==6)
		passeio(grafo);
	}
}

int main(){

    cout<<"GRAFOS - ROTINAS EM C"<<endl;
    menu();

}
