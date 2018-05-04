import sys
map_dict = {"7": [0, 0], "8": [0, 1], "9": [0, 2],
            "4": [1, 0], "5": [1, 1], "6": [1, 2],
            "1": [2, 0], "2": [2, 1], "3": [2, 2]
            }
if sys.version_info[0] == 2:
    input = raw_input # python 2 compatibility


class Grid():
    def __init__(self, not_taken_symbol_input=" ", you_symbol_input="X", pc_symbol_input="O"):
        self.not_taken_symbol = str(not_taken_symbol_input)
        self.you_symbol = str(you_symbol_input)
        self.pc_symbol = str(pc_symbol_input)
        self.grid = [
                     [self.not_taken_symbol, self.not_taken_symbol, self.not_taken_symbol],
                     [self.not_taken_symbol, self.not_taken_symbol, self.not_taken_symbol],
                     [self.not_taken_symbol, self.not_taken_symbol, self.not_taken_symbol]
                    ]

    def change_value(self, input_index, input_id):
        """0: pc........ 1: me ......... 3: none"""  
        working_index_list = map_dict[str(input_index)]
        working_id = int(input_id)
        edit_sign = " "
        #  self.not_taken_symbol = str(not_taken_symbol_input)
        # self.you_symbol = str(you_symbol_input)
        # self.pc_symbol = str(pc_symbol_input)
        if working_id == 0:
            edit_sign = self.pc_symbol
        elif working_id == 1:
            edit_sign = self.you_symbol
        elif working_id == 2:
            edit_sign = self.not_taken_symbol 
        else:
            assert 0
        self.grid[working_index_list[0]][working_index_list[1]] = edit_sign

    def print_grid(self):
        print('   |   |   ')
        print(' {} | {} | {} '.format(self.grid[0][0], self.grid[0][1], self.grid[0][2]))
        print('   |   |   ')
        print('---+---+---')
        print('   |   |   ')
        print(' {} | {} | {} '.format(self.grid[1][0], self.grid[1][1], self.grid[1][2]))
        print('   |   |   ')
        print('---+---+---')
        print('   |   |   ')
        print(' {} | {} | {} '.format(self.grid[2][0], self.grid[2][1], self.grid[2][2]))
        print('   |   |   ')
        print('---+---+---')

        print('Enter the number of your move:')
        print('  7|8|9')
        print('  -+-+-')
        print('  4|5|6')
        print('  -+-+-')
        print('  1|2|3')
grid = Grid(" ", "X", "0")
print('Welcome to Tic Tac Toe!')
grid.print_grid()
move = input()
if move == '1':
    grid.change_value(9, 0)
    grid.change_value(1, 1)
    grid.print_grid()
    move = input()
    if move == '2':
        grid.change_value(2, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
    if move == '3':
        grid.change_value(3, 1)
        grid.change_value(2, 0)
        grid.print_grid()
        move = input()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
    if move == '4':
        grid.change_value(4, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
    if move == '5':
        grid.change_value(5, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
    if move == '6':
        grid.change_value(6, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
    if move == '7':
        grid.change_value(7, 1)
        grid.change_value(4, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
    if move == '8':
        grid.change_value(8, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
if move == '2':
    grid.change_value(1, 0)
    grid.change_value(2, 1)
    grid.print_grid()
    move = input()
    if move == '3':
        grid.change_value(3, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
    if move == '4':
        grid.change_value(4, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            move = input()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
    if move == '5':
        grid.change_value(5, 1)
        grid.change_value(8, 0)
        grid.print_grid()
        move = input()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            move = input()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
    if move == '6':
        grid.change_value(6, 1)
        grid.change_value(9, 0)
        grid.print_grid()
        move = input()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
    if move == '7':
        grid.change_value(7, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
    if move == '8':
        grid.change_value(8, 1)
        grid.change_value(5, 0)
        grid.print_grid()
        move = input()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                sys.exit()
    if move == '9':
        grid.change_value(9, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                sys.exit()
if move == '3':
    grid.change_value(9, 0)
    grid.change_value(3, 1)
    grid.print_grid()
    move = input()
    if move == '1':
        grid.change_value(1, 1)
        grid.change_value(2, 0)
        grid.print_grid()
        move = input()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
    if move == '2':
        grid.change_value(2, 1)
        grid.change_value(1, 0)
        grid.print_grid()
        move = input()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
    if move == '4':
        grid.change_value(4, 1)
        grid.change_value(1, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
    if move == '5':
        grid.change_value(5, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
    if move == '6':
        grid.change_value(6, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
    if move == '7':
        grid.change_value(7, 1)
        grid.change_value(5, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            sys.exit()
    if move == '8':
        grid.change_value(8, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
if move == '4':
    grid.change_value(3, 0)
    grid.change_value(4, 1)
    grid.print_grid()
    move = input()
    if move == '1':
        grid.change_value(1, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
    if move == '2':
        grid.change_value(2, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
    if move == '5':
        grid.change_value(5, 1)
        grid.change_value(6, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
    if move == '6':
        grid.change_value(6, 1)
        grid.change_value(5, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
    if move == '7':
        grid.change_value(7, 1)
        grid.change_value(1, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
    if move == '8':
        grid.change_value(8, 1)
        grid.change_value(9, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
    if move == '9':
        grid.change_value(9, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
if move == '5':
    grid.change_value(9, 0)
    grid.change_value(5, 1)
    grid.print_grid()
    move = input()
    if move == '1':
        grid.change_value(1, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
    if move == '2':
        grid.change_value(2, 1)
        grid.change_value(8, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
    if move == '3':
        grid.change_value(3, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
    if move == '4':
        grid.change_value(4, 1)
        grid.change_value(6, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
    if move == '6':
        grid.change_value(6, 1)
        grid.change_value(4, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
    if move == '7':
        grid.change_value(7, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
    if move == '8':
        grid.change_value(8, 1)
        grid.change_value(2, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                move = input()
                if move == '7':
                    grid.change_value(7, 1)
                    sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
if move == '6':
    grid.change_value(1, 0)
    grid.change_value(6, 1)
    grid.print_grid()
    move = input()
    if move == '2':
        grid.change_value(2, 1)
        grid.change_value(7, 0)
        grid.print_grid()
        move = input()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
    if move == '3':
        grid.change_value(3, 1)
        grid.change_value(9, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
    if move == '4':
        grid.change_value(4, 1)
        grid.change_value(5, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
    if move == '5':
        grid.change_value(5, 1)
        grid.change_value(4, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            sys.exit()
    if move == '7':
        grid.change_value(7, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
    if move == '8':
        grid.change_value(8, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
            if move == '7':
                grid.change_value(7, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(7, 0)
                grid.print_grid()
                sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
    if move == '9':
        grid.change_value(9, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(7, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '7':
            grid.change_value(7, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
if move == '7':
    grid.change_value(3, 0)
    grid.change_value(7, 1)
    grid.print_grid()
    move = input()
    if move == '1':
        grid.change_value(1, 1)
        grid.change_value(4, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                sys.exit()
    if move == '2':
        grid.change_value(2, 1)
        grid.change_value(1, 0)
        grid.print_grid()
        move = input()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(8, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
    if move == '4':
        grid.change_value(4, 1)
        grid.change_value(1, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            sys.exit()
    if move == '5':
        grid.change_value(5, 1)
        grid.change_value(9, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
    if move == '6':
        grid.change_value(6, 1)
        grid.change_value(9, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
    if move == '8':
        grid.change_value(8, 1)
        grid.change_value(9, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
    if move == '9':
        grid.change_value(9, 1)
        grid.change_value(8, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
if move == '8':
    grid.change_value(7, 0)
    grid.change_value(8, 1)
    grid.print_grid()
    move = input()
    if move == '1':
        grid.change_value(1, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
    if move == '2':
        grid.change_value(2, 1)
        grid.change_value(5, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
    if move == '3':
        grid.change_value(3, 1)
        grid.change_value(1, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '6':
                    grid.change_value(6, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
    if move == '4':
        grid.change_value(4, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
    if move == '5':
        grid.change_value(5, 1)
        grid.change_value(2, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(9, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                move = input()
                if move == '9':
                    grid.change_value(9, 1)
                    sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(9, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
            if move == '9':
                grid.change_value(9, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
        if move == '9':
            grid.change_value(9, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                sys.exit()
    if move == '6':
        grid.change_value(6, 1)
        grid.change_value(9, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(3, 0)
                grid.print_grid()
                sys.exit()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(1, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '1':
                grid.change_value(1, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                move = input()
                if move == '1':
                    grid.change_value(1, 1)
                    sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                sys.exit()
    if move == '9':
        grid.change_value(9, 1)
        grid.change_value(1, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
if move == '9':
    grid.change_value(7, 0)
    grid.change_value(9, 1)
    grid.print_grid()
    move = input()
    if move == '1':
        grid.change_value(1, 1)
        grid.change_value(5, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            sys.exit()
    if move == '2':
        grid.change_value(2, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
    if move == '3':
        grid.change_value(3, 1)
        grid.change_value(6, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(2, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '4':
                    grid.change_value(4, 1)
                    sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
    if move == '4':
        grid.change_value(4, 1)
        grid.change_value(1, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(6, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                move = input()
                if move == '2':
                    grid.change_value(2, 1)
                    sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(3, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(5, 0)
                grid.print_grid()
                sys.exit()
            if move == '5':
                grid.change_value(5, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
    if move == '5':
        grid.change_value(5, 1)
        grid.change_value(1, 0)
        grid.print_grid()
        move = input()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '3':
            grid.change_value(3, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(6, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(8, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
            if move == '3':
                grid.change_value(3, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '8':
                    grid.change_value(8, 1)
                    sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                move = input()
                if move == '3':
                    grid.change_value(3, 1)
                    sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(4, 0)
            grid.print_grid()
            sys.exit()
    if move == '6':
        grid.change_value(6, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                grid.change_value(4, 0)
                grid.print_grid()
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                sys.exit()
            if move == '8':
                grid.change_value(8, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
        if move == '8':
            grid.change_value(8, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
    if move == '8':
        grid.change_value(8, 1)
        grid.change_value(3, 0)
        grid.print_grid()
        move = input()
        if move == '1':
            grid.change_value(1, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '2':
            grid.change_value(2, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '4':
            grid.change_value(4, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
        if move == '5':
            grid.change_value(5, 1)
            grid.change_value(1, 0)
            grid.print_grid()
            move = input()
            if move == '2':
                grid.change_value(2, 1)
                sys.exit()
            if move == '4':
                grid.change_value(4, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
            if move == '6':
                grid.change_value(6, 1)
                grid.change_value(2, 0)
                grid.print_grid()
                sys.exit()
        if move == '6':
            grid.change_value(6, 1)
            grid.change_value(5, 0)
            grid.print_grid()
            sys.exit()
