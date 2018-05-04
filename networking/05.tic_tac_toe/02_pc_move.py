import re
# f = open("working_base.txt", 'r')
# f =
# a = re.split("^if move == '[0-9]':$", "working_base.txt")


pc_map_dict = {"print('O moves on the top-left space.')\n": [0, 0],
               "print('O moves on the top-center space.')\n": [0, 1],
               "print('O moves on the top-right space.')\n": [0, 2],
               "print('O moves on the left space.')\n": [1, 0],
               "print('O moves on the center space.')\n": [1, 1],
               "print('O moves on the right space.')\n": [1, 2],
               "print('O moves on the bottom-left space.')\n": [2, 0],
               "print('O moves on the bottom-center space.')\n": [2, 1],
               "print('O moves on the bottom-right space.')\n": [2, 2]
               }
outfile = open("pc_txt.txt", 'w')
words_dict = dict()
with open("working_base.txt", "r", encoding="utf-8") as file:
    for line in file:
        outfile.write(line)
        if(re.match("^\s+print\('O.+$", line)):
        # outfile.write(line)
        # outfile.write("*"*50+"\n")
            white_space_countr = 0
            word = ""
            flag = 0
            for letter in line:
                if letter == " " and flag == 0:
                    white_space_countr += 1
                else:
                    flag = 1
                    word = word + letter
            outfile.write(" " * white_space_countr + word)
            words_dict[word] = white_space_countr
print(words_dict)
                    
