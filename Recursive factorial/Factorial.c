#include <stdio.h>

int getFactorial(int); //Prototipo

int main(int argc, char** argv){

  int x = 5;
  printf("El factorial de %d, es = %d\n",x, getFactorial(x));
  return 0;
}

int getFactorial(int numero){
  return (numero > 0) ? numero*getFactorial(numero -1) : 1;
}
