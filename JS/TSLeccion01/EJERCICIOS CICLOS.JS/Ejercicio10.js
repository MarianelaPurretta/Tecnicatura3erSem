/*Ejercicio 10: Pedir 10 números y escribir la suma total*/
let suma = 0
for (let i = 0; i < 10; i++) {
    let numero = parseInt(prompt("Ingrese un número: "))
    suma += numero
}
alert("La suma de los números es: " + suma)