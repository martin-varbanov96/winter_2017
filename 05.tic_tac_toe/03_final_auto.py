import re
# f = open("working_base.txt", 'r')
# f =
# a = re.split("^if move == '[0-9]':$", "working_base.txt")


pc_map_dict = {"print('O moves on the top-left space.')\n": 7,
               "print('O moves on the top-center space.')\n": 8,
               "print('O moves on the top-right space.')\n": 9,
               "print('O moves on the left space.')\n": 4,
               "print('O moves on the center space.')\n": 5,
               "print('O moves on the right space.')\n": 6,
               "print('O moves on the bottom-left space.')\n": 1,
               "print('O moves on the bottom-center space.')\n": 2,
               "print('O moves on the bottom-right space.')\n": 3
               }

human_map_dict = {"if move == '2':\n": 2,
                  "if move == '4':\n": 4,
                  "if move == '1':\n": 1,
                  "if move == '3':\n": 3,
                  "if move == '9':\n": 9,
                  "if move == '6':\n": 6,
                  "if move == '8':\n": 8,
                  "if move == '7':\n": 7,
                  "if move == '5':\n": 5}

outfile = open("pc_txt.txt", 'w')
words_dict = dict()
with open("working_base.txt", "r", encoding="utf-8") as file:
    for line in file:
        if(re.match("^\s+print\('O.+$", line)):
            white_space_countr = 0
            word = ""
            flag = 0
            for letter in line:
                if letter == " " and flag == 0:
                    white_space_countr += 1
                else:
                    flag = 1
                    word = word + letter
            # outfile.write(" " * white_space_countr + word)
                # grid.change_value(9, 0)
            outfile.write(" " * white_space_countr +
                          "grid.change_value({}, 0)\n".format(pc_map_dict[word]))
            outfile.write(" " * white_space_countr + "grid.print_grid()\n")
            words_dict[word] = white_space_countr

        elif(re.match("^\s+if move == '[0-9]':$", line)):
            outfile.write(line)
            word = ""
            white_space_countr = 0
            flag = 0
            for letter in line:
                if letter == " " and flag == 0:
                    white_space_countr += 1
                else:
                    flag = 1
                    word = word + letter
            outfile.write(" " * white_space_countr + " " * 4 +
                          "grid.change_value({}, 1)\n".format(human_map_dict[word]))

        elif(re.match("^\s+print\('.+$", line) or re.match("^\s+$", line)):
            pass
        else:
            outfile.write(line)
print(words_dict)
