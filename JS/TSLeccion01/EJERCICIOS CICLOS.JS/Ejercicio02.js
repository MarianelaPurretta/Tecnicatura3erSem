/*Ej 2: Leer un número e indicar si es positivo o negativo hasta introducir "0"*/
let numero = parseInt(prompt("Ingrese un numero: "))

while (numero != 0) {
    if (numero > 0) {
        alert(numero + " Es un numero positivo");
    }
    else {
        alert(numero + " Es un numero negativo");
    }

    numero = parseInt(prompt("Ingrese un numero: "))
}
alert("Fin del programa, ingresó 0");