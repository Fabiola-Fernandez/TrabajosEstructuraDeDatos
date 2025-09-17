F, C = 6, 7
#board: para inicializar una matriz
board = [['.' for _ in range(C)] for _ in range(F)]

#print_board: funcion para mostrar el tablero del juego
#row: cada fila de la matriz 
#.join.row: une cada las filas para que se vea mejor
def print_board():
    
    print('\n'.join(' '.join(row) for row in board))
    
    #aqui generamos los numeros que se mostraran abajo
    print(' '.join(map(str, range(1, C+1))))

#funcion para colocar alguna ficha
#j: jugador
def drop(col, j):
    
    #el for va recorrido de abajo a arriba
    for f in range(F-1, -1, -1):
        
        #revisa si esta libre el lugar 
        if board[f][col] == '.':
            #si esta libre coloca la ficha
            board[f][col] = j
            return f
            
    #columna llena
    return None

#funcion para comprobar si alguien gano
def win(f, c, j):
    
    #direcciones por revisar
    dirs = [(0,1),(1,0),(1,1),(1,-1)]
    
    #revisa cada direccion
    #df: cambio de fila
    #dc: cambio de columna
    for df, dc in dirs:
        #cuenta la ficha puesta
        cnt = 1
        
        #revisa hacia los dos lados
        for s in (1, -1):
            
            #nf, nc: nueva fila y columna por revisar
            nf, nc = f + df*s, c + dc*s
            
            #para no salir de la filas ni de las columnas
            #board para contar la fichas del mismo Jugador
            while 0 <= nf < F and 0 <= nc < C and board[nf][nc] == j:
                cnt += 1
                nf += df*s; nc += dc*s
                
        #comprobar si gana
        if cnt >= 4: return True
    return False

#alternar turnos
players = ['X','O']; turn = 0

#este while es hasta que alguien haga un True de arriba
while True:
    print_board()
    
    #input: pide al Jugador la columna donde quiere colocar su ficha
    try:
        col = int(input(f"Jugador {players[turn]} - elige columna (1-{C}): ")) - 1
        if not 0 <= col < C:
            
            #si el número no esta
            print("Columna inválida.")
            continue
        
    #si el Jugador no Introduce un número 
    except ValueError:
        print("Introduce un número.")
        continue

    #drop la funcion para colocar la ficha en la Columna
    fila = drop(col, players[turn])
    if fila is None:
        print("Columna llena. Elige otra")
        continue
    
    
    #llama a la funcion win para si gano el Jugador
    if win(fila, col, players[turn]):
        print_board()
        print(f"Jugador {players[turn]} gana")
        break

    # revisa cada fila de cada Columna si esta llena Empate
    if all(board[0][c] != '.' for c in range(C)):
        print_board()
        print("Empate.")
        break

    #cambio de turnos
    turn = 1 - turn