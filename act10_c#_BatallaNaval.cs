using System;

class BatallaNaval
{
    const int TAM = 10;
    static char[,] tablero1 = new char[TAM, TAM];
    static char[,] tablero2 = new char[TAM, TAM];

    static void Main()
    {
        // Inicializamos tableros
        Inicializar(tablero1);
        Inicializar(tablero2);

        // Jugador 1 coloca barcos
        Console.WriteLine("Jugador 1 coloca sus barcos:");
        ColocarBarcos(tablero1);

        Console.Clear();

        // Jugador 2 coloca barcos
        Console.WriteLine("Jugador 2 coloca sus barcos:");
        ColocarBarcos(tablero2);

        // Mostramos tableros para verificar
        Console.Clear();
        Console.WriteLine("Tablero del Jugador 1:");
        Mostrar(tablero1);
        Console.WriteLine("\nTablero del Jugador 2:");
        Mostrar(tablero2);

        Console.WriteLine("\nTodos los barcos colocados. Fin del programa.");
    }

    // Inicializamos tablero con puntos (agua)
    static void Inicializar(char[,] t)
    {
        for (int i = 0; i < TAM; i++)
            for (int j = 0; j < TAM; j++)
                t[i, j] = '.';
    }

    // Mostramos el tablero con números del 1 al 10
    static void Mostrar(char[,] t)
    {
        Console.Write("   ");
        for (int i = 1; i <= TAM; i++) Console.Write(i + " ");
        Console.WriteLine();

        for (int i = 0; i < TAM; i++)
        {
            Console.Write((i + 1).ToString().PadLeft(2) + " ");
            for (int j = 0; j < TAM; j++)
            {
                char simbolo = t[i, j];
                if (simbolo == 'B') simbolo = '8'; // cambiamos barco a 8
                Console.Write(simbolo + " ");
            }
            Console.WriteLine();
        }
    }

    // Función para colocar barcos
    static void ColocarBarcos(char[,] t)
    {
        // Barcos y sus tamaños
        int[] barcos = { 5, 4, 3, 3, 2 };
        string[] nombres = { "Portaviones", "Acorazado", "Crucero", "Submarino", "Destructor" };

        for (int b = 0; b < barcos.Length; b++)
        {
            bool colocado = false;
            while (!colocado)
            {
                Mostrar(t);
                Console.WriteLine($"Coloca tu {nombres[b]} de tamaño {barcos[b]}");
                Console.Write("Fila inicial (1-10): ");
                int fila = int.Parse(Console.ReadLine()) - 1;
                Console.Write("Columna inicial (1-10): ");
                int col = int.Parse(Console.ReadLine()) - 1;
                Console.Write("Orientación (H=horizontal, V=vertical): ");
                char o = char.ToUpper(Console.ReadKey().KeyChar);
                Console.WriteLine();

                if (SePuedeColocar(t, fila, col, o, barcos[b]))
                {
                    Poner(t, fila, col, o, barcos[b]);
                    colocado = true;
                }
                else
                {
                    Console.WriteLine("No se puede colocar ahí. Intenta otra vez.");
                }
            }
        }
    }

    // Verificamos si se puede colocar un barco
    static bool SePuedeColocar(char[,] t, int f, int c, char o, int tam)
    {
        if (o == 'H')
        {
            if (c + tam > TAM) return false;
            for (int i = 0; i < tam; i++)
                if (t[f, c + i] != '.') return false;
        }
        else
        {
            if (f + tam > TAM) return false;
            for (int i = 0; i < tam; i++)
                if (t[f + i, c] != '.') return false;
        }
        return true;
    }

    // Ponemos el barco en el tablero
    static void Poner(char[,] t, int f, int c, char o, int tam)
    {
        if (o == 'H')
            for (int i = 0; i < tam; i++) t[f, c + i] = 'B';
        else
            for (int i = 0; i < tam; i++) t[f + i, c] = 'B';
    }
}
 