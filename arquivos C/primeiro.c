#include <stdio.h>
#include <locale.h>

int main()
{
  setlocale(LC_ALL, "Portuguese");
  int N;

  printf("Digite o valor de N: ");
  scanf("%d",&N);


  return 0;
}

