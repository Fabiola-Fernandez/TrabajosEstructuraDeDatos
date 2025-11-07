import java.util.Random;
import java.util.Scanner;

class TreasureHunter {
    public static void main(String[] args) {
        // Tamaño del tablero
        final int SIZE = 25;
        // Creamos el tablero
        char[][] board = new char[SIZE][SIZE];

        // Inicializamos las posiciones del jugador y la salida
        int playerX = 0, playerY = 0;
        int exitX, exitY;
        Random random = new Random();

        // Llenamos el tablero con puntos (vacío)
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                board[i][j] = '.';
            }
        }

        // Colocamos las paredes (representadas por '#')
        int walls = 50;  // Número de paredes
        for (int i = 0; i < walls; i++) {
            int x = random.nextInt(SIZE);
            int y = random.nextInt(SIZE);
            if ((x != 0 || y != 0)) { // Evitar poner la pared en la posición inicial
                board[x][y] = '#';
            }
        }

        // Colocamos la salida (representada por 'E')
        do {
            exitX = random.nextInt(SIZE);
            exitY = random.nextInt(SIZE);
        } while (board[exitX][exitY] == '#' || (exitX == 0 && exitY == 0)); // Evitar que la salida esté en la posición inicial

        board[exitX][exitY] = 'E';

        // Colocamos al jugador en la posición inicial
        board[playerX][playerY] = 'P';

        // Imprimimos el tablero inicial
        printBoard(board);

        Scanner scanner = new Scanner(System.in);

        // Bucle del juego
        boolean gameOver = false;
        while (!gameOver) {
            System.out.println("Usa las teclas WASD para moverte (W=Arriba, A=Izquierda, S=Abajo, D=Derecha): ");
            char move = scanner.next().toUpperCase().charAt(0);

            // Limpiar la posición anterior del jugador
            board[playerX][playerY] = '.';

            // Mover al jugador según la tecla presionada
            switch (move) {
                case 'W': // Arriba
                    if (playerX > 0 && board[playerX - 1][playerY] != '#') {
                        playerX--;
                    }
                    break;
                case 'A': // Izquierda
                    if (playerY > 0 && board[playerX][playerY - 1] != '#') {
                        playerY--;
                    }
                    break;
                case 'S': // Abajo
                    if (playerX < SIZE - 1 && board[playerX + 1][playerY] != '#') {
                        playerX++;
                    }
                    break;
                case 'D': // Derecha
                    if (playerY < SIZE - 1 && board[playerX][playerY + 1] != '#') {
                        playerY++;
                    }
                    break;
                default:
                    System.out.println("Movimiento inválido.");
                    break;
            }

            // Colocar al jugador en la nueva posición
            board[playerX][playerY] = 'P';

            // Verificar si el jugador ha llegado a la salida
            if (playerX == exitX && playerY == exitY) {
                System.out.println("¡Felicidades! Has encontrado la salida.");
                gameOver = true;
            }

            // Imprimir el tablero después de cada movimiento
            printBoard(board);
        }

        scanner.close();
    }

    // Función para imprimir el tablero
    public static void printBoard(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }
}
