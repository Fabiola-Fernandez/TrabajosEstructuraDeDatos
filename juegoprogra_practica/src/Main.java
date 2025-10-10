class Tablero25 {
    public static void main(String[] args) {
        int n = 25; // tamaño del tablero (n x n)

        // Para cada fila del tablero
        for (int fila = 0; fila < n; fila++) {
            // línea superior de las celdas
            for (int col = 0; col < n; col++) {
                System.out.print("+---");
            }
            System.out.println("+");

            // línea con puntos dentro de las celdas
            for (int col = 0; col < n; col++) {
                System.out.print("| . ");
            }
            System.out.println("|");
        }

        // línea inferior final del tablero
        for (int col = 0; col < n; col++) {
            System.out.print("+---");
        }
        System.out.println("+");
    }
}