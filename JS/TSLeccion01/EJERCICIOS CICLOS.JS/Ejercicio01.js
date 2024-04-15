/*
Ejercicio 1: Leer un numero y comprar su cuadrado, repetir
el proceso hasta que se introduzca un numero negativo
*/

let numero = parseInt(prompt("Ingrese un numero: "))

while (numero > 0) {
    let cuadrado = Math.pow(numero, 2);
    alert("El cuadrado del " + numero + " es " + cuadrado);
    numero = parseInt(prompt("Ingrese un numero: "))
}
alert("Fin del programa por ingreso de número negativo");