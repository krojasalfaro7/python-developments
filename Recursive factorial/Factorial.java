package factorial;

public class Factorial{
  // Método privado estatico
  private static Integer getFactorial(int numero){
    return (numero > 0) ? numero*getFactorial(numero - 1) : 1;
  }
  
  public static void main(String args[]){
    Integer x = 6; //Valor donde se alamacerá el número a obtenr el factorial
    System.out.println("El factorial del numero "+x.toString()+" es = "+getFactorial(x).toString()); 
  }
}
