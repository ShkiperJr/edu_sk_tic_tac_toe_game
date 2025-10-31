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
        
        
def check_input(input_x):
    list_of_char = ("1", "2", "3", "q", "Q")
    if input_x =="0":
        return False
    if input_x not in list_of_char:
        print('Ошибка ввода!!! Введите 1, 2, 3.')
        return False
    return True

    

def сhecking_game_end(x,y,player):
    if game_matrix[x][y] != '-':
        print('Указанные кординаты ужe заняты!!!')
        return True
    
    return True


def run_game():
    print("Game has begun")    
    print("Player 1 Ready")
    xx = "0"
    while not check_input(xx): 
        xx = input('Player 1 inter number  X: ')
        if xx == 'q':
            return
    
    yy = input('Player 1 inter number  Y: ')
    if yy == 'q':
        return




game_matrix_print(game_matrix) 

run_game()   


#print(game_matrix)