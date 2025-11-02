game_matrix = [["-" for j in range(3)] for i in range(3)]


def game_matrix_print(matrix):
    """A beautifully designed graphic display of the game matrix

    Args:
        matrix (game_matrix Previously initiated): Task to display on the screen
    """
    print("      y1  y2  y3")
    for i in range(3):
        print("x", i + 1, end='')
        for j in range(3):
            print("  ",matrix[i][j], end='')
        print()
    print()
        
        
def check_input(player, coordinates):
    """Input validation. The function returns only the specified 
       required values.

    Args:
        player (_type_): Player index.
        coordinates (_type_): The coordinate axis.

    Returns:
        Str : The function returns only the specified required 
              values, necessary for gameplay.
    """
    list_of_char = ("1", "2", "3", "q", "Q")
    x=''
    while x not in list_of_char:
        x = input(f'Player {player} inter number  {coordinates}: ')
        if x in list_of_char:
            return x
        else:
            print('Ошибка ввода!!! Введите 1, 2, 3.')     

    
def сhecking_game_end():
    """Checks the logic of the game's ending. Checks for 16 victory options. 
       Checks for the game matrix being filled.
    """
    
    def upper_cells(a1 ,b1 , a2, b2, a3, b3, index):
        """This function raises the winning line for a more attractive 
           display.

        Args:
            a1 (int): Win line coordinate
            b1 (int): Win line coordinate
            a2 (int): Win line coordinate
            b2 (int): Win line coordinate
            a3 (int): Win line coordinate
            b3 (int): Win line coordinate
            index (char): Player symbol
        """
        game_matrix[a1][b1] = index
        game_matrix[a2][b2] = index
        game_matrix[a3][b3] = index
# Checks the logic of the game's ending.        
    if not any ('-' in i for i in game_matrix):
        print('There is no Winner. DRAW')
        return False
#1 Checks for 16 victory options.   
    if game_matrix[0][0] == game_matrix[0][1] == game_matrix[0][2] == 'x':
        print('Player 1 WIN!!!')
        upper_cells(0 ,0 , 0, 1, 0, 2, "Х")
        game_matrix_print(game_matrix)
        return False
    if game_matrix[0][0] == game_matrix[0][1] == game_matrix[0][2] == 'o':
        print('Player 2 WIN!!!')
        upper_cells(0 ,0 , 0, 1, 0, 2, "O")
        game_matrix_print(game_matrix)
        return False
#2
    if game_matrix[1][0] == game_matrix[1][1] == game_matrix[1][2] == 'x':
        print('Player 1 WIN!!!')
        upper_cells(1 ,0 , 1, 1, 1, 2, "Х")
        game_matrix_print(game_matrix)
        return False
    if game_matrix[1][0] == game_matrix[1][1] == game_matrix[1][2] == 'o':
        print('Player 2 WIN!!!')
        upper_cells(1 ,0 , 1, 1, 1, 2, "O")
        game_matrix_print(game_matrix)
        return False
 #3   
    if game_matrix[2][0] == game_matrix[2][1] == game_matrix[2][2] == 'x':
        print('Player 1 WIN!!!')
        upper_cells(2 ,0 , 2, 1, 2, 2, "Х")
        game_matrix_print(game_matrix)
        return False
    if game_matrix[2][0] == game_matrix[2][1] == game_matrix[2][2] == 'o':
        print('Player 2 WIN!!!')
        upper_cells(2 ,0 , 2, 1, 2, 2, "O")
        game_matrix_print(game_matrix)
        return False  
#4    
    if game_matrix[0][0] == game_matrix[1][0] == game_matrix[2][0] == 'x':
        print('Player 1 WIN!!!')
        upper_cells(0 ,0 , 1, 0, 2, 0, "Х")
        game_matrix_print(game_matrix)
        return False
    if game_matrix[0][0] == game_matrix[1][0] == game_matrix[2][0] == 'o':
        print('Player 2 WIN!!!')
        upper_cells(0 ,0 , 1, 0, 2, 0, "O")
        game_matrix_print(game_matrix)
        return False 
#5    
    if game_matrix[0][1] == game_matrix[1][1] == game_matrix[2][1] == 'x':
        print('Player 1 WIN!!!')
        upper_cells(0 ,1 , 1, 1, 2, 1, "Х")
        game_matrix_print(game_matrix)
        return False
    if game_matrix[0][1] == game_matrix[1][1] == game_matrix[2][1] == 'o':
        print('Player 2 WIN!!!')
        upper_cells(0 ,1 , 1, 1, 2, 1, "O")
        game_matrix_print(game_matrix)
        return False
#6    
    if game_matrix[0][2] == game_matrix[1][2] == game_matrix[2][2] == 'x':
        print('Player 1 WIN!!!')
        upper_cells(0 ,2 , 1, 2, 2, 2, "Х")
        game_matrix_print(game_matrix)
        return False
    if game_matrix[0][2] == game_matrix[1][2] == game_matrix[2][2] == 'o':
        print('Player 2 WIN!!!')
        upper_cells(0 ,2 , 1, 2, 2, 2, "O")
        game_matrix_print(game_matrix)
        return False
#7    
    if game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2] == 'x':
        print('Player 1 WIN!!!')
        upper_cells(0 ,0 , 1, 1, 2, 2, "Х")
        game_matrix_print(game_matrix)
        return False
    if game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2] == 'o':
        print('Player 2 WIN!!!')
        upper_cells(0 ,0 , 1, 1, 2, 2, "O")
        game_matrix_print(game_matrix)
        return False
#8    
    if game_matrix[0][2] == game_matrix[1][1] == game_matrix[2][0] == 'x':
        print('Player 1 WIN!!!')
        upper_cells(0 ,2 , 1, 1, 2, 0, "Х")
        game_matrix_print(game_matrix)
        return False
    if game_matrix[0][2] == game_matrix[1][1] == game_matrix[2][0] == 'o':
        print('Player 2 WIN!!!')
        upper_cells(0 ,2 , 1, 1, 2, 0, "O")
        game_matrix_print(game_matrix)
        return False

    return True
      

def run_game():
    print("Game has begun")    
    player_index = 1
    
    while сhecking_game_end():
        
        game_matrix_print(game_matrix)
    
        print(f"Player {player_index} Ready")
#Entering coordinates, checking for an emergency exit.
        x = check_input(player_index, "X")
        if x == 'Q' or x == 'q':
            return
        y = check_input(player_index, "Y")
        if y == 'Q' or y == 'q':
            return
#Checking the cell occupancy. Switching to re-entry
        if game_matrix[int(x) - 1][int(y) - 1] != '-':
            print('Указанные кординаты ужe заняты!!!')
            continue
#Player change. Entering the player's actions into the game matrix.        
        if player_index == 1:
            game_matrix[int(x) - 1][int(y) - 1] = "x"
            player_index = 2
        else:
            player_index = 1
            game_matrix[int(x) - 1][int(y) - 1] = "o"
    

run_game()   