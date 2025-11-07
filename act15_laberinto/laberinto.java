import java.util.Scanner;
import java.io.*;


class Laberinto {
    static final int TAM = 25;
    static char[][] tablero = new char[TAM][TAM]; 
    static boolean[][] revelado = new boolean[TAM][TAM]; // para saber que partes del mapa se van mostrando
    static int jugadorFila = 0, jugadorCol = 0; // Posicion del jugador
    static int nivel = 1; 
    static int vidas = 3; 

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        generarNivel(nivel); // generamos el primer nivel
        limpiarConsola();
        mostrarEncabezado();
        mostrarTablero();

        boolean jugando = true;

        while (jugando) {
            moverCursor(TAM + 3, 0);
            System.out.print("\033[K");
            System.out.println("Mover (w/a/s/d), guardar (g), mostrar (m), salir (x): ");
            String input = sc.nextLine();

            int anteriorFila = jugadorFila;
            int anteriorCol = jugadorCol;

            // para que se pueda mover el jugador
            switch (input) {
                case "w": moverJugador(-1, 0); break;
                case "s": moverJugador(1, 0); break;
                case "a": moverJugador(0, -1); break;
                case "d": moverJugador(0, 1); break;
                case "g": guardarProgreso(); break;
                case "m": mostrarProgreso(); break;
                case "x": jugando = false; continue;
                default:
                    moverCursor(TAM + 4, 0);
                    System.out.println("Opción inválida.");
                    continue;
            }

            char celda = tablero[jugadorFila][jugadorCol];

            // como funciona el juego y sus reglas 
            if (celda == 'x') {
                vidas--;
                moverCursor(TAM + 4, 0);
                System.out.println("Chocaste con una bomba, vidas restantes: " + vidas);
                jugadorFila = anteriorFila;
                jugadorCol = anteriorCol;
                actualizarPosicion(anteriorFila, anteriorCol);
                mostrarEncabezado();

                if (vidas <= 0) {
                    moverCursor(TAM + 5, 0);
                    System.out.println("Juego terminado, has muerto");
                    jugando = false;
                }

            } else if (celda == '#') {
                // se va mostrando las paredes cuando se choca con ellas 
                revelado[jugadorFila][jugadorCol] = true;
                moverCursor(jugadorFila + 2, jugadorCol * 2 + 1);
                System.out.print("# ");

                moverCursor(TAM + 4, 0);
                System.out.println("Hay una pared");

                // regresamos al jugador a su posicion 
                jugadorFila = anteriorFila;
                jugadorCol = anteriorCol;
                actualizarPosicion(anteriorFila, anteriorCol);

            } else if (celda == 'y') {
                moverCursor(TAM + 4, 0);
                System.out.println("¡Nivel completado!");
                nivel++;
                if (nivel > 3) {
                    moverCursor(TAM + 5, 0);
                    System.out.println("¡Ganaste el juego!");
                    jugando = false;
                } else {
                    jugadorFila = 0;
                    jugadorCol = 0;
                    generarNivel(nivel);
                    limpiarConsola();
                    mostrarEncabezado();
                    mostrarTablero();
                }
            }

            mostrarEncabezado();
            actualizarPosicion(anteriorFila, anteriorCol);
        }

        sc.close();
    }

    /**
     * va generando niveles diferentes
     */
    static void generarNivel(int nivel) {
        for (int i = 0; i < TAM; i++) {
            for (int j = 0; j < TAM; j++) {
                tablero[i][j] = '.';
                revelado[i][j] = false;
            }
        }

        // Obstaculos
        for (int i = 0; i < nivel * 40; i++) {
            int x = (int)(Math.random() * TAM);
            int y = (int)(Math.random() * TAM);
            if (x != 0 || y != 0) tablero[x][y] = 'x';
        }

        // Paredes
        for (int i = 0; i < nivel * 50; i++) {
            int x = (int)(Math.random() * TAM);
            int y = (int)(Math.random() * TAM);
            if (tablero[x][y] == '.') tablero[x][y] = '#';
        }

        
        tablero[TAM - 1][TAM - 1] = 'y';
    }

    /**
     * para que e muestren las vidas
     */
    static void mostrarEncabezado() {
        moverCursor(1, 0);
        System.out.print("\033[K");
        System.out.println("Nivel: " + nivel + " | Vidas: " + vidas);
        moverCursor(2, 0);
    }

    /**
     * va dibujando el tablero 
     */
    static void mostrarTablero() {
        for (int i = 0; i < TAM; i++) {
            for (int j = 0; j < TAM; j++) {
                if (i == jugadorFila && j == jugadorCol) {
                    System.out.print("j ");
                } else if (revelado[i][j] && tablero[i][j] == '#') {
                    System.out.print("# ");
                } else {
                    System.out.print(". ");
                }
            }
            System.out.println();
        }
    }

    /**
     * se va actualizando la posicion del jugador
     */
    static void actualizarPosicion(int anteriorFila, int anteriorCol) {
        // va limpiando
        moverCursor(anteriorFila + 2, anteriorCol * 2 + 1);
        if (revelado[anteriorFila][anteriorCol] && tablero[anteriorFila][anteriorCol] == '#') {
            System.out.print("# ");
        } else {
            System.out.print(". ");
        }

        // Dibuja al jugador solo si la celda actual no es una pared
        if (tablero[jugadorFila][jugadorCol] != '#') {
            moverCursor(jugadorFila + 2, jugadorCol * 2 + 1);
            System.out.print("j ");
        }

        moverCursor(TAM + 3, 0);
    }

    /**
     * para que le jugador no salga de los limites permitidos
     */
    static void moverJugador(int df, int dc) {
        int nf = jugadorFila + df;
        int nc = jugadorCol + dc;
        if (nf >= 0 && nf < TAM && nc >= 0 && nc < TAM) {
            jugadorFila = nf;
            jugadorCol = nc;
        }
    }

    /**
     * se va guardando el procesos del jugador
     */
    static void guardarProgreso() {
        try (PrintWriter pw = new PrintWriter("progreso.txt")) {
            pw.println("Jugador en: " + jugadorFila + "," + jugadorCol);
            pw.println("Nivel: " + nivel);
            pw.println("Vidas: " + vidas);
            System.out.println("Se a guardado");
        } catch (IOException e) {
            System.out.println("Hay un error");
        }
    }

    /**
     * para mostrar el proceso del jugador
     */
    static void mostrarProgreso() {
        try (BufferedReader br = new BufferedReader(new FileReader("progreso.txt"))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            System.out.println("No se a gurdado");
        }
    }

    // para que no se este reimprimiendo el tablero 
    static void limpiarConsola() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    static void moverCursor(int fila, int col) {
        System.out.printf("\033[%d;%dH", fila, col);
        System.out.flush();
    }
}

