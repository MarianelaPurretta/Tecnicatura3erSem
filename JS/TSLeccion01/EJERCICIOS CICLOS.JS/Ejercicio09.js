/*
Ejercicio 9: Pedir el día, mes y año de una fecha e indicar si es correcta
suponiendo que todos los meses son de 30 días*/
let dia = parseInt(prompt("Ingrese en día: "))
let mes = parseInt(prompt("Ingrese un mes: "))
let anio = parseInt(prompt("Ingrese un anio: "))

if ((dia != 0) && (dia <= 30)) {
    if ((mes != 0) && (mes <= 12)) {
        if ((anio != 0) && (anio <= 2023)) {
            alert("La fecha ingresada es: " + dia + "/" + mes + "/" + anio)
        } else {
            alert("Fecha incorrecta, año incorrecto")
        }
    } else {
        alert("Fecha incorrecta, mes incorrecto")
    }
} else {
    alert("Fecha incorrecta, día incorrecto")
}