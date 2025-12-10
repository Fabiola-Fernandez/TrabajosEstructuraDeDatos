using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;

namespace JuegoSnake
{
    class Programa
    {
        const int Ancho = 60;
        const int Alto = 20;
        const int TamanoInicial = 5;
        const int ComidasParaSubirNivel = 5;
        const int DelayInicialMs = 150;
        const int ReduccionDelayPorNivel = 10;
        const int DelayMinimoMs = 40;

        static Random rnd = new Random();
        const string ArchivoRanking = "ranking.txt";

        static void Main()
        {
            bool seguirJugando = true;
            string nombreJugador = "Jugador";

            while (seguirJugando)
            {
             
                Console.SetWindowSize(80, 40);
                Console.SetBufferSize(80, 40);

                Console.Clear();
                Console.Write("Escribe tu nombre: ");
                nombreJugador = Console.ReadLine()?.Trim();
                if (string.IsNullOrEmpty(nombreJugador))
                    nombreJugador = "Jugador";

                
                // Juego
                Console.CursorVisible = false;
                Console.Title = $"Snake - {nombreJugador}";
                Console.Clear();
                DibujarBorde();

                var serpiente = new List<Position>();
                int inicioX = Ancho / 2;
                int inicioY = Alto / 2;

                for (int i = 0; i < TamanoInicial; i++)
                    serpiente.Add(new Position(inicioX - (TamanoInicial - 1) + i, inicioY));

                Direccion direccion = Direccion.Derecha;
                int puntaje = 0;
                int comidasEsteNivel = 0;
                int nivel = 1;
                int delay = DelayInicialMs;

                Position comida = GenerarPosicionLibre(serpiente);
                Position trampa = GenerarPosicionLibre(serpiente, new List<Position> { comida });

                bool finJuego = false;

                DibujarSerpiente(serpiente);
                DibujarEn(comida, 'O');
                DibujarEn(trampa, 'X');
                DibujarEstadisticas(puntaje, nivel);

                while (!finJuego)
                {
                    DateTime inicioFrame = DateTime.Now;

                    if (Console.KeyAvailable)
                    {
                        var tecla = Console.ReadKey(true).Key;
                        var nueva = direccion;

                        if (tecla == ConsoleKey.UpArrow || tecla == ConsoleKey.W) nueva = Direccion.Arriba;
                        if (tecla == ConsoleKey.DownArrow || tecla == ConsoleKey.S) nueva = Direccion.Abajo;
                        if (tecla == ConsoleKey.LeftArrow || tecla == ConsoleKey.A) nueva = Direccion.Izquierda;
                        if (tecla == ConsoleKey.RightArrow || tecla == ConsoleKey.D) nueva = Direccion.Derecha;

                        if (!EsDireccionOpuesta(direccion, nueva))
                            direccion = nueva;
                    }

                    Position cabeza = serpiente.Last();
                    Position nuevaCabeza = cabeza;

                    switch (direccion)
                    {
                        case Direccion.Arriba: nuevaCabeza = new Position(cabeza.X, cabeza.Y - 1); break;
                        case Direccion.Abajo: nuevaCabeza = new Position(cabeza.X, cabeza.Y + 1); break;
                        case Direccion.Izquierda: nuevaCabeza = new Position(cabeza.X - 1, cabeza.Y); break;
                        case Direccion.Derecha: nuevaCabeza = new Position(cabeza.X + 1, cabeza.Y); break;
                    }

                    
                    if (nuevaCabeza.X < 1) nuevaCabeza.X = Ancho - 2;
                    if (nuevaCabeza.X > Ancho - 2) nuevaCabeza.X = 1;
                    if (nuevaCabeza.Y < 1) nuevaCabeza.Y = Alto - 2;
                    if (nuevaCabeza.Y > Alto - 2) nuevaCabeza.Y = 1;

                    // Choque
                    if (serpiente.Contains(nuevaCabeza))
                    {
                        finJuego = true;
                        break;
                    }

                    serpiente.Add(nuevaCabeza);
                    DibujarEn(nuevaCabeza, 'O');

                    bool comio = nuevaCabeza.Equals(comida);
                    bool trampaTocada = nuevaCabeza.Equals(trampa);

                    if (comio)
                    {
                        puntaje++;
                        comidasEsteNivel++;
                        comida = GenerarPosicionLibre(serpiente, new List<Position> { trampa });
                        DibujarEn(comida, 'O');
                    }
                    else
                    {
                        var cola = serpiente[0];
                        LimpiarEn(cola);
                        serpiente.RemoveAt(0);
                    }

                    if (trampaTocada)
                    {
                        int reducir = Math.Max(1, nivel);
                        for (int i = 0; i < reducir; i++)
                        {
                            if (serpiente.Count > 0)
                            {
                                LimpiarEn(serpiente[0]);
                                serpiente.RemoveAt(0);
                            }
                        }

                        if (serpiente.Count < 1)
                        {
                            finJuego = true;
                            break;
                        }

                        trampa = GenerarPosicionLibre(serpiente, new List<Position> { comida });
                        DibujarEn(trampa, 'X');
                    }

                    if (comidasEsteNivel >= ComidasParaSubirNivel)
                    {
                        nivel++;
                        comidasEsteNivel = 0;
                        delay = Math.Max(DelayMinimoMs, delay - ReduccionDelayPorNivel);

                        comida = GenerarPosicionLibre(serpiente);
                        trampa = GenerarPosicionLibre(serpiente, new List<Position> { comida });

                        DibujarEn(comida, 'O');
                        DibujarEn(trampa, 'X');

                        MostrarMensajeTemporal($"¡SUBES AL NIVEL {nivel}!", 800);
                    }

                    DibujarEstadisticas(puntaje, nivel);

                    int transcurrido = (int)(DateTime.Now - inicioFrame).TotalMilliseconds;
                    if (delay - transcurrido > 0)
                        Thread.Sleep(delay - transcurrido);
                }

        
                // Final del juego
                Console.CursorVisible = true;

                // Limpiar 
                for (int i = Alto; i < Alto + 10; i++)
                {
                    Console.SetCursorPosition(0, i);
                    Console.Write(new string(' ', Ancho));
                }

                Console.SetCursorPosition(0, Alto + 1);
                Console.WriteLine("              GAME OVER             ");
                Console.WriteLine($"Jugador: {nombreJugador}");
                Console.WriteLine($"Puntaje: {puntaje}");
                Console.WriteLine();

                // Guardar y mostrar ranking
                GuardarEnRanking(nombreJugador, puntaje);
                MostrarRankingFinal();

                Console.WriteLine();
                Console.WriteLine("Presiona cualquier tecla para salir...");
                Console.ReadKey(true);

                // termina el programa
                seguirJugando = false;


                
                //FUNCIONES

                static void DibujarBorde()
        {
            for (int x = 0; x < Ancho; x++)
            {
                Console.SetCursorPosition(x, 0); Console.Write('#');
                Console.SetCursorPosition(x, Alto - 1); Console.Write('#');
            }
            for (int y = 0; y < Alto; y++)
            {
                Console.SetCursorPosition(0, y); Console.Write('#');
                Console.SetCursorPosition(Ancho - 1, y); Console.Write('#');
            }
        }

        static void DibujarSerpiente(List<Position> serpiente)
        {
            foreach (var p in serpiente)
                DibujarEn(p, 'O');
        }

        static void DibujarEn(Position p, char c)
        {
            Console.SetCursorPosition(p.X, p.Y);
            Console.Write(c);
        }

        static void LimpiarEn(Position p)
        {
            Console.SetCursorPosition(p.X, p.Y);
            Console.Write(' ');
        }

        static Position GenerarPosicionLibre(List<Position> serp, List<Position> prohibidas = null)
        {
            prohibidas ??= new List<Position>();
            Position pos;
            do
            {
                pos = new Position(rnd.Next(1, Ancho - 1), rnd.Next(1, Alto - 1));
            } while (serp.Contains(pos) || prohibidas.Contains(pos));
            return pos;
        }

        static void DibujarEstadisticas(int puntaje, int nivel)
        {
            Console.SetCursorPosition(0, Alto);
            Console.Write(new string(' ', Ancho));
            Console.SetCursorPosition(0, Alto);
            Console.Write($"Puntaje: {puntaje}   Nivel: {nivel}");
        }

        static void MostrarMensajeTemporal(string msg, int ms)
        {
            Console.SetCursorPosition((Ancho - msg.Length) / 2, Alto);
            Console.Write(msg);
            Thread.Sleep(ms);
            Console.SetCursorPosition((Ancho - msg.Length) / 2, Alto);
            Console.Write(new string(' ', msg.Length));
        }

        static bool EsDireccionOpuesta(Direccion a, Direccion b)
        {
            return (a == Direccion.Izquierda && b == Direccion.Derecha) ||
                   (a == Direccion.Derecha && b == Direccion.Izquierda) ||
                   (a == Direccion.Arriba && b == Direccion.Abajo) ||
                   (a == Direccion.Abajo && b == Direccion.Arriba);
        }

        static void GuardarEnRanking(string nombre, int puntaje)
        {
            File.AppendAllLines(ArchivoRanking, new[] { $"{nombre};{puntaje}" });
        }

        static void MostrarRankingFinal()
        {
            Console.WriteLine("RANKING");

            if (!File.Exists(ArchivoRanking))
            {
                Console.WriteLine("(No hay datos aún)");
                return;
            }

            var datos = File.ReadAllLines(ArchivoRanking)
                .Select(l =>
                {
                    var p = l.Split(';');
                    return (nombre: p[0], puntaje: int.Parse(p[1]));
                })
                .OrderByDescending(x => x.puntaje)
                .Take(10)
                .ToList();

            if (datos.Count == 0)
            {
                Console.WriteLine("(Vacío)");
                return;
            }

            int i = 1;
            foreach (var r in datos)
            {
                Console.WriteLine($"{i}. {r.nombre} - {r.puntaje}");
                i++;
            }
        }
    }
        }

        struct Position : IEquatable<Position>
    {
        public int X;
        public int Y;
        public Position(int x, int y) { X = x; Y = y; }

        public bool Equals(Position other) => X == other.X && Y == other.Y;
        public override bool Equals(object obj) => obj is Position p && Equals(p);
        public override int GetHashCode() => (X << 16) ^ Y;
    }

    enum Direccion { Arriba, Abajo, Izquierda, Derecha }
}
}


