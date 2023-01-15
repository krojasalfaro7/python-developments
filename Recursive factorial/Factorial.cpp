#include <iostream>

using namespace std;

class factorial{
  public:
    static int getFactorial(int numero){
      return (numero > 0) ? numero*getFactorial(numero - 1) : 1;
    }
};

int main(int argc, char** argv){
  int x = 5;
  printf("Este es el factorial de %d = %d\n", x, factorial::getFactorial(x));
  return 0;
}
