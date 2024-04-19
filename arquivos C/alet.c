#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <time.h>

int main() {
setlocale(LC_ALL, "Portuguese");
int numero,vida,palpite;

srand(time(NULL));
numero= rand() % 100 + 1; // Gera um número aleatório de 1 a 100
printf("Número aleatório: %d\n", numero);

vida=5;
while (vida!=0){
    printf("Digite seu palpite: ");
    scanf("%d",&palpite);
    if(palpite>numero){
        printf("%d e maior do que o valor\n",palpite);
    }
    else if(palpite<numero){
        printf("%d e menor do que o valor\n",palpite);
    }
    else if(palpite==numero){
        printf("voce acertou");
        return 0;
    }
    else if(vida==0){
        printf("voce perdeu, o numero era %d\n",numero);
    }
    vida--;

}




//printf("Número aleatório: %d\n", numero_aleatorio);

return 0;
}