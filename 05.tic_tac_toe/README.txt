base.txt - this is our base code, I never change it. (BTW Can I make a file chmod ?-w) so that NO ONE can change it, ever again, including sudo ?




              ==============01.py:=====================



After that I've made class Grid, which will:
    - save the data;
    - print the current status of the game;
    - change the values;
    - change the symbol of each user's mark e.g. X or O, you can convert it to T, S, whatever you like

the map_dict receives integer from the old grid, and converts it to the new matrix grid

        print('Enter the number of your move:')
        print('  7|8|9')
        print('  -+-+-')
        print('  4|5|6')
        print('  -+-+-')
        print('  1|2|3')

        |
        |
        |

        print('Enter the number of your move:')
        print('  [0, 0]|[0, 1]|[0, 2]')
        print('  -+-+-')
        print('  [1, 0]|[1, 1]|[1, 2]')
        print('  -+-+-')
        print('  [2, 0]|[2, 1]|[2, 2]')


Started grinding the changes one by one, made a couple and I started googleing for regex





              ==============02_pc+move.py and 02_pc_move.py:=====================
              	NOTHING SPECIAL

          Initial testing with regex, nothing special, just testing how 
          this and that would work in this and that situation like 
          printing checking if I could check the ifs and print them(output.txt)
          or failed, check (piece_of_art.txt)






              ==============03.py:=====================
              			THE TRUE SHORTENER

      		 So, I read the base.txt line by line, if I get a line which has the 
      		  * if move == 'X': - write it and write a new line after that which changes the value of this X square to be player square
      		  * print('O moves on....') - use my class to assign that value to the matrix for pc
      		  * else if print..... or whitespaces line only - I skip it
      		  * else I print the line, it's either sys.sth or something neccesary. 

      		  this produces working_base.txt. After that I create a new python script




              ==============10.working.py:=====================
              				stable

		Here I had to include my class, manually write some lines which failed to be produced. And run it


		=========================Features==================

		  I made added it to the PATH as you told I can launch it from anywhere

		  ============Problems===================

		  UX sucks, no good handle if any mistakes are made
		  





 

