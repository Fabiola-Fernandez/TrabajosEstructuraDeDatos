#include <iostream>

char tablero[3][3] = { {'1','2','3'}, {'4','5','6'}, {'7','8','9'} };

// Función para mostrar el tablero
void mostrarTablero() {
    std::cout << std::endl;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            std::cout << tablero[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

// Función para tomar la jugada del jugador
void jugar(char jugador) {
    int eleccion;
    std::cout << "Jugador " << jugador << ", elige un numero: ";
    std::cin >> eleccion;

    int fila = (eleccion - 1) / 3;
    int col = (eleccion - 1) % 3;

    if(tablero[fila][col] != 'X' && tablero[fila][col] != 'O') {
        tablero[fila][col] = jugador;
    } else {
        std::cout << "Esa posicion ya esta ocupada, elige de nuevo\n";
        jugar(jugador); // Repetir hasta que la jugada sea valida
    }
}

// Función para comprobar si hay un ganador
bool hayGanador(char jugador) {
    // Revisar filas y columnas
    for(int i = 0; i < 3; i++) {
        if((tablero[i][0] == jugador && tablero[i][1] == jugador && tablero[i][2] == jugador) ||
           (tablero[0][i] == jugador && tablero[1][i] == jugador && tablero[2][i] == jugador)) {
            return true;
        }
    }
    // Revisar diagonales
    if((tablero[0][0] == jugador && tablero[1][1] == jugador && tablero[2][2] == jugador) ||
       (tablero[0][2] == jugador && tablero[1][1] == jugador && tablero[2][0] == jugador)) {
        return true;
    }

    return false;
}

// Función para comprobar empate
bool empate() {
    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            if(tablero[i][j] != 'X' && tablero[i][j] != 'O')
                return false;
    return true;
}

int main() {
    char jugador = 'X';
    while(true) {
        mostrarTablero();
        jugar(jugador);

        if(hayGanador(jugador)) {
            mostrarTablero();
            std::cout << "Jugador " << jugador << " gano\n";
            break;
        }

        if(empate()) {
            mostrarTablero();
            std::cout << "Empate\n";
            break;
        }

        // Cambiar de jugador
        jugador = (jugador == 'X') ? 'O' : 'X';
    }

    return 0;
}