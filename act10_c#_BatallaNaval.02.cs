using System;

class BatallaNaval
{
    const int TAM = 10;
    static char[,] tablero1 = new char[TAM, TAM];
    static char[,] tablero2 = new char[TAM, TAM];
    static char[,] disparos1 = new char[TAM, TAM];
    static char[,] disparos2 = new char[TAM, TAM];

    static (string nombre, int tamaño)[] barcos = {
        ("Portaviones", 5),
        ("Acorazado", 4),
        ("Crucero", 3),
        ("Submarino", 3),
        ("Destructor", 2)
    };

    static void Main()
    {
        Console.WriteLine("BATALLA NAVAL");

        InicializarTablero(tablero1);
        InicializarTablero(tablero2);
        InicializarTablero(disparos1);
        InicializarTablero(disparos2);

        Console.WriteLine("\n--- Jugador 1 coloca sus barcos ---");
        ColocarBarcos(tablero1);

        Console.Clear();
        Console.WriteLine("\n--- Jugador 2 coloca sus barcos ---");
        ColocarBarcos(tablero2);

        Console.Clear();
        Console.WriteLine("BATALLA\n");

        bool juegoTerminado = false;
        int turno = 1;

        while (!juegoTerminado)
        {
            if (turno == 1)
            {
                Console.WriteLine("\nJugador 1");
                juegoTerminado = Disparar(tablero2, disparos1);
                turno = 2;
            }
            else
            {
                Console.WriteLine("\nJugador 2");
                juegoTerminado = Disparar(tablero1, disparos2);
                turno = 1;
            }
        }

        Console.WriteLine("\nFin del juego");
    }

    static void InicializarTablero(char[,] tablero)
    {
        for (int i = 0; i < TAM; i++)
            for (int j = 0; j < TAM; j++)
                tablero[i, j] = '.';
    }

    static void MostrarTablero(char[,] tablero)
    {
        Console.WriteLine("\n   1 2 3 4 5 6 7 8 9 10");
        for (int i = 0; i < TAM; i++)
        {
            Console.Write((i + 1).ToString().PadLeft(2) + " ");
            for (int j = 0; j < TAM; j++)
            {
                Console.Write(tablero[i, j] + " ");
            }
            Console.WriteLine();
        }
    }

    static void ColocarBarcos(char[,] tablero)
    {
        foreach (var barco in barcos)
        {
            bool colocado = false;
            while (!colocado)
            {
                MostrarTablero(tablero);
                Console.WriteLine($"\nColocando {barco.nombre} (tamaño {barco.tamaño})");

                Console.Write("Fila (1-10): ");
                int fila = int.Parse(Console.ReadLine()) - 1;

                Console.Write("Columna (1-10): ");
                int columna = int.Parse(Console.ReadLine()) - 1;

                Console.Write("Ingrese la posicion que desea (H/V): ");
                char orientacion = char.ToUpper(Console.ReadKey().KeyChar);
                Console.WriteLine();

                if (orientacion == 'H')
                {
                    if (columna + barco.tamaño <= TAM)
                    {
                        bool libre = true;
                        for (int j = columna; j < columna + barco.tamaño; j++)
                            if (tablero[fila, j] == '0') libre = false;

                        if (libre)
                        {
                            for (int j = columna; j < columna + barco.tamaño; j++)
                                tablero[fila, j] = '0';
                            colocado = true;
                        }
                        else Console.WriteLine("Esa posición está ocupada.");
                    }
                    else Console.WriteLine("No cabe en H");
                }
                else if (orientacion == 'V')
                {
                    if (fila + barco.tamaño <= TAM)
                    {
                        bool libre = true;
                        for (int i = fila; i < fila + barco.tamaño; i++)
                            if (tablero[i, columna] == '0') libre = false;

                        if (libre)
                        {
                            for (int i = fila; i < fila + barco.tamaño; i++)
                                tablero[i, columna] = '0';
                            colocado = true;
                        }
                        else Console.WriteLine("Esa posición esta ocupada");
                    }
                    else Console.WriteLine("No cabe en V");
                }
                else
                {
                    Console.WriteLine("No puede colocar aquí");
                }
            }
            Console.Clear();
        }
    }

    static bool Disparar(char[,] tableroOponente, char[,] tableroDisparos)
    {
        MostrarTablero(tableroDisparos);
        Console.Write("\nFila a disparar (1-10): ");
        int fila = int.Parse(Console.ReadLine()) - 1;
        Console.Write("Columna a disparar (1-10): ");
        int columna = int.Parse(Console.ReadLine()) - 1;

        if (tableroOponente[fila, columna] == '0')
        {
            Console.WriteLine("Disporo");
            tableroOponente[fila, columna] = 'X';
            tableroDisparos[fila, columna] = 'X';
        }
        else if (tableroOponente[fila, columna] == '.')
        {
            Console.WriteLine("Fallaste");
            tableroOponente[fila, columna] = 'O';
            tableroDisparos[fila, columna] = 'O';
        }
        else
        {
            Console.WriteLine("Ya disparaste ahí");
        }

        if (HaPerdido(tableroOponente))
        {
            Console.WriteLine("\nHas hundido todos los barcos");
            return true;
        }

        Console.WriteLine("Presiona para continuar");
        Console.ReadKey();
        Console.Clear();
        return false;
    }

    static bool HaPerdido(char[,] tablero)
    {
        for (int i = 0; i < TAM; i++)
            for (int j = 0; j < TAM; j++)
                if (tablero[i, j] == '0') return false;
        return true;
    }
}