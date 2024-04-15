/*Pedir números hasta que se ingrese un negativo, mostrar cuántos se han
ingresado.*/
let contar = 0
let numero = parseInt(prompt("Ingrese un número: "))
while (numero >= 0) {
    alert("El número: " + numero + " es positivo")
    contar++
    numero = parseInt(prompt("Ingrese un numero: "))

}
alert("Ha ingresado " + contar + " números positivos")