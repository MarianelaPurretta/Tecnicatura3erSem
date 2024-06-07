import java.util.Scanner;

public class CalculadoraUTN {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); // Pedimos al usuario los números
        System.out.println("******* Aplicacion Calculadora *******");
        //MOSTRAMOS EL MENÚ
        System.out.println("""
                1. Suma
                2. Resta
                3. Multiplicacion
                4. Division
                5. Salir
                """);
        System.out.println("Operacion a realizar?");
        var operacion = Integer.parseInt(entrada.nextLine());
        System.out.print("Digite el valor para el operando1: ");
        var operando1 = Integer.parseInt(entrada.nextLine()); //Guardamos lo números ingresados por el usuario
        System.out.print("Digite el valor para el operando2: ");
        var operando2 = Integer.parseInt(entrada.nextLine());
        var resultado = operando1 + operando2;
        System.out.println("resultado = " + resultado);
    }
}

