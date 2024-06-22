// Función aleatorio
function aleatorio(max, min) {
    let numero = Math.floor(Math.random() * (max - min + 1) + min);
    return numero;
}

// Función eleccion
function eleccion(jugada) {
    let resultado = "";
    if (jugada == 1) {
        resultado = "Piedra 🥌";
    } else if (jugada == 2) {
        resultado = "Papel 📜";
    } else if (jugada == 3) {
        resultado = "Tijera ✂";
    } else {
        resultado = "Mal elegido";
    }
    return resultado;
}

// Función para iniciar el juego
function iniciarJuego() {
    let jugador = 0;
    let pc = 0;
    let triunfos = 0;
    let perdidas = 0;

    while (triunfos < 3 && perdidas < 3) {
        pc = aleatorio(3, 1);
        jugador = prompt("Elije: 1 piedra, 2 papel, 3 tijera");

        alert("Pc elige: " + eleccion(pc));
        alert("Tu eliges: " + eleccion(jugador));

        // Combate
        if (pc == jugador) {
            alert("EMPATE");
        } else if ((jugador == 1 && pc == 3) || (jugador == 2 && pc == 1) || (jugador == 3 && pc == 2)) {
            alert("Ganaste");
            triunfos++;
        } else {
            alert("Perdiste");
            perdidas++;
        }
    }
    alert("Ganaste " + triunfos + " veces. Perdiste " + perdidas + " veces.");
}

saludo = "Hola";
profesor = "Profe";
alert (saludo + " " + profesor);