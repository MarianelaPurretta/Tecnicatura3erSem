//Intentamos hacer hosting pero no se permite antes de la clase
//let persona3 = new Persona('Carla', 'Ponce');

class Persona { //CLASE PADRE
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    //Agregamos get y set
    get nombre() {
        return this._nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
}

class Empleado extends Persona { //CLASE HIJA
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido); //||SE DEBE LLAMAR EN LA PRIMER LÍNEA DEL CONSTRUCTOR DE LA CLASE HIJA A LA CLASE PADRE||
        this._departamento = departamento;
    }

    get deprtamento() {
        return this._departamento;
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
}
//Creamos los objetos
let persona1 = new Persona('Martín', 'Perez');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = 'María Laura';
console.log(persona2.nombre);
//console.log(persona2);
console.log(persona1.apellido);
persona1.apellido = 'López';
console.log(persona1.apellido);

console.log(persona2.apellido);
persona1.apellido = 'García';
console.log(persona1.apellido);

let empleado1 = new Empleado('María', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombre);