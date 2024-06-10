import java.util.Scanner;

public class CalculadoraUTN {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); // Pedimos al usuario los números
        while (true) {
            System.out.println("******* Aplicacion Calculadora *******");
            mostrarMenu(); // Llamamos al método

            try { //Colocamos las excepciones de tipo e
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {

                    //Colocamos el swich para los casos de opracion a realizar:
                    ejecutarOperacion(operacion, entrada); //Llamamos anl metodo, le pasamos la var y el objeto
                } // FIN DEL IF
                else if (operacion == 5) {
                    System.out.println("Hasta pronto!");
                    break; //Colocamos el break en la opcion de salir, rompe el ciclo y sale
                } else {
                    System.out.println("Opcion erronea: " + operacion);
                }
                //imprimimos salto de linea antes de repetir el menu
                System.out.println();
            } catch(Exception e){ //FIN TRY
                System.out.println("Ocurrio un error: "+e.getMessage());
                System.out.println();
            } //FIN CATCH
        } //FIN DE WHILE
    } //FIN MAIN

    private static void mostrarMenu(){  //Creamos un metodo para mostrar menú
        //MOSTRAMOS EL MENÚ
        System.out.println("""
                    1. Suma
                    2. Resta
                    3. Multiplicacion
                    4. Division
                    5. Salir
                    """);
        System.out.print("Operacion a realizar? ");
    } //FINN METODO MOSTRAR MENU
    // Creamos otro metodo para ejecutar
    private static void ejecutarOperacion(int operacion, Scanner entrada){
        System.out.print("Digite el valor para el operando1: ");
        var operando1 = Double.parseDouble(entrada.nextLine()); //Guardamos lo números ingresados por el usuario
        System.out.print("Digite el valor para el operando2: ");
        var operando2 = Double.parseDouble(entrada.nextLine());
        double resultado;
        switch (operacion) {
            case 1 -> {
                resultado = operando1 + operando2;
                System.out.println("Resultado de la suma: " + resultado);
            }
            case 2 -> {
                resultado = operando1 - operando2;
                System.out.println("Resultado de la resta: " + resultado);
            }
            case 3 -> {
                resultado = operando1 * operando2;
                System.out.println("Resultado de la multiplicacion:4 " + resultado);
            }
            case 4 -> {
                resultado = operando1 / operando2;
                System.out.println("Resultado de la division: " + resultado);
            }
            //en caso de opcion invalida:
            default -> System.out.println("Opcion erronea> " + operacion);
        } //FIN DEL SWITCH
    } // FIN METODO EJECUTAR
} // FIN CLASS

