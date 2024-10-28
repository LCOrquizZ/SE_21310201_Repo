console.log("¡El script se ha cargado correctamente!");

let jugadores = JSON.parse(localStorage.getItem('jugadores')) || [];

// Asignar eventos a los botones después de que se cargue el DOM
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("btnAgregar").addEventListener("click", mostrarAgregarJugador);
    document.getElementById("btnMostrar").addEventListener("click", mostrarJugadores);
    document.getElementById("btnPreguntar").addEventListener("click", hacerPreguntas);
    document.getElementById("btnSalir").addEventListener("click", salir);
});

// Guardar jugadores en localStorage
function guardarJugadores() {
    localStorage.setItem('jugadores', JSON.stringify(jugadores));
}

// Mostrar el formulario de agregar jugador
function mostrarAgregarJugador() {
    document.getElementById("contenido").innerHTML = `
        <h2>Agregar Jugador</h2>
        <form onsubmit="agregarJugador(event)">
            <label>Nombre:</label>
            <input type="text" id="nombre" required><br>
            <label>¿Está retirado?</label>
            <select id="retirado">
                <option value="true">Sí</option>
                <option value="false">No</option>
            </select><br>
            <label>Conferencia:</label>
            <select id="conferencia">
                <option value="este">Este</option>
                <option value="oeste">Oeste</option>
                <option value="ambas">Ambas</option>
            </select><br>
            <label>Número de campeonatos ganados:</label>
            <input type="number" id="campeonatos" min="0" value="0" required><br>
            <label>Altura en metros:</label>
            <input type="number" step="0.01" id="altura" min="1.6" value="1.6" required><br>
            <button type="submit">Agregar</button>
        </form>
    `;
}

// Agregar un nuevo jugador con validación de altura
function agregarJugador(event) {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value.trim();
    const retirado = document.getElementById("retirado").value === 'true';
    const conferencia = document.getElementById("conferencia").value;
    const campeonatos = parseInt(document.getElementById("campeonatos").value.trim());
    const altura = parseFloat(document.getElementById("altura").value.trim());

    if (altura < 1.6) {
        const confirmar = confirm("La altura ingresada es menor a 1.6 metros. ¿Estás seguro que es correcta?");
        if (!confirmar) return;
    }

    const nuevoJugador = { nombre, retirado, conferencia, campeonatos, altura };

    if (!jugadorYaExiste(nuevoJugador)) {
        jugadores.push(nuevoJugador);
        guardarJugadores();
        alert(`${nombre} fue agregado exitosamente.`);
        imprimirTablaConsola();
    } else {
        alert("Este jugador ya está en la base de datos.");
    }
}

// Verificar si el jugador ya existe
function jugadorYaExiste(nuevoJugador) {
    return jugadores.some(jugador =>
        jugador.nombre.toLowerCase() === nuevoJugador.nombre.toLowerCase() &&
        jugador.campeonatos === nuevoJugador.campeonatos &&
        jugador.altura === nuevoJugador.altura
    );
}

// Imprimir jugadores en la consola como tabla
function imprimirTablaConsola() {
    console.table(jugadores);
}

// Mostrar la lista de jugadores con opción de eliminar
function mostrarJugadores() {
    if (jugadores.length === 0) {
        alert("No hay jugadores registrados.");
        return;
    }

    let contenido = "<h2>Lista de Jugadores</h2><ul>";
    jugadores.forEach((jugador, index) => {
        contenido += `
            <li>
                ${jugador.nombre} - ${jugador.altura}m, ${jugador.campeonatos} campeonatos
                <button onclick="eliminarJugador(${index})">Eliminar</button>
            </li>
        `;
    });
    contenido += "</ul>";

    document.getElementById("contenido").innerHTML = contenido;
}

// Eliminar un jugador por su índice
function eliminarJugador(index) {
    const confirmar = confirm("¿Estás seguro que deseas eliminar este jugador?");
    if (confirmar) {
        jugadores.splice(index, 1);
        guardarJugadores();
        mostrarJugadores();
    }
}

// Iniciar preguntas para adivinar el jugador
function hacerPreguntas() {
    const retirado = confirm("¿El jugador está retirado?");
    const conferencia = prompt("¿Conferencia (Este/Oeste/Ambas)?").trim().toLowerCase();
    const campeonatos = parseInt(prompt("¿Cuántos campeonatos ha ganado?").trim());
    const altura = parseFloat(prompt("¿Cuál es su altura en metros?").trim());

    let jugadoresFiltrados = jugadores.filter(jugador =>
        jugador.retirado === retirado &&
        (conferencia === 'ambas' || jugador.conferencia === conferencia) &&
        jugador.campeonatos === campeonatos &&
        jugador.altura === altura
    );

    if (jugadoresFiltrados.length === 1) {
        const jugador = jugadoresFiltrados[0];
        const respuesta = confirm(`¿Es ${jugador.nombre} el jugador en el que estabas pensando?`);
        if (!respuesta) mostrarAgregarJugador();
    } else {
        alert("No se encontró un jugador con estas características. Por favor ingresa nuevamente los datos para registrarlo en la base de jugadores.");
        mostrarAgregarJugador(); // Redirige al formulario para ingresar los datos del nuevo jugador
    }
}

// Recargar la página para salir del menú
function salir() {
    location.reload();
}
