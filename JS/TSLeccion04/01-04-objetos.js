let x = 10; // var tipo primitivo
console.log(x.lenght);
console.log('Tipos Primitivos');
//Objeto con sus propiedades:
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    nombreCompleto: function () { //metodo o funcion
        return this.nombre + ' ' + this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');

//Creamos otro objeto y agregamos las propiedades
let persona2 = new Object(); //
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '2324747588';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');

//Accedemos a las propiedaddes de un objeto:
console.log(persona['apellido']) //Como si fuera un arreglo
console.log('Usamos ciclo for in');
//for in:
//para acceder a las propiedades pero no a lo que contiene
for (propiedad in persona) {
    console.log(propiedad)
    //Accedemos al valor de la propiedad
    console.log(persona[propiedad]);
}
console.log('Cambiamos y eliminamos error');
//Agregar nueva propiedad:
persona.apellida = 'Betancud'; //CAMBIAMOS DINÁMICAMENTE EL VALOR DE UN OBJETO
delete persona.apellida; //Eliminamos la propiedad y el valor
console.log(persona);

//Distintas maneras de imprimir un objeto
//Número1: La más sencilla: 
//_CONCATENAR CADA VALOR DE CADA PROPIEDAD:
console.log('Distintas maneras de imprimir un objeto: forma 1');
console.log(persona.nombre + ', ' + persona.apellido);

//Número2: 
//_A TRAVES DEL CICLO FOR IN:
console.log('Distintas maneras de imprimir un objeto: forma 2');
for (nombrePropiedad in persona) {
    console.log(persona[nombrePropiedad]);
}

//Número3: Con un método: 
//_FUNCIÓN Object.values():
console.log('Distintas maneras de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Número3: 
//_Método JSON.stringify:
console.log('Distintas maneras de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);