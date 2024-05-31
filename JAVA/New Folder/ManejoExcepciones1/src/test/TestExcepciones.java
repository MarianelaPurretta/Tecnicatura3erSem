
package test;

// Si el programa encuentra una excepción puede seguir ejecutando hacia abajo, muestra la excepción y continua

import static aritmetica.Aritmetica.division;

public class TestExcepciones { 
    public static void main(String[] args) {
        int resultado = 0;
        try{
            resultado = division(10, 0);
        } catch(Exception e){
            System.out.println("Ocurrio un error");
            e.printStackTrace(System.out); // Pila se excepciones
            System.out.println(e.getMessage());
        }
        System.out.println("La varible de resultado tiene como valor: " + resultado);
        
        //El compilador no muestra error porque no sabe de estas excepciones hasta que ejecuta
    }
}
