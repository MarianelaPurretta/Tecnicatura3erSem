/*Leer números hasta introducir 0
Para cada uno indicar si es par o impar*/

let numero = parseInt(prompt("Ingrese un numero: "))

while (numero != 0) {
    if (numero % 2 == 0) {
        alert("El número " + numero + " es par");
    }
    else {
        alert("El número " + numero + " es impar");
    }

    numero = parseInt(prompt("Ingrese un numero: "))
}
alert("Fin del programa");