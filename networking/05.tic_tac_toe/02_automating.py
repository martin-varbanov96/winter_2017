import re
# f = open("working_base.txt", 'r')
# f =
# a = re.split("^if move == '[0-9]':$", "working_base.txt")
words_dict=dict()
outfile = open("output.txt", 'w')
with open("working_base.txt", "r", encoding="utf-8") as file:
    for line in file:
        if(re.match("^\s+if move == '[0-9]':$", line)):
            # This is the patter
            # TODO:: recognize number
            # grid.change_value(move, 1)
            outfile.write(line)
            word = ""
            flag = 0
            white_space_countr = 0
            for letter in line:
                if letter == " " and flag == 0:
                    white_space_countr += 1
                else:
                    flag = 1
                    word = word + letter
            outfile.write(" " * white_space_countr + word)
            words_dict[word] = white_space_countr
print(words_dict)