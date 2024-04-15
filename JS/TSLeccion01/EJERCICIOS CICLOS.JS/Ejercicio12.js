/*Ejercico 12: Pedir un número y calcular su factorial*/
let factorial = 1
let numero = parseInt(prompt("Ingrese un número: "))
for (let i = 1; i <= numero; i++) {
    factorial *= i
    //numero = parseInt(prompt("Ingrese un número: "))
}
alert("Ela factorial de " + numero + " es: " + factorial)