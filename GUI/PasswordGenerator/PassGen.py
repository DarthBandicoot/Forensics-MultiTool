import string
import random
from PassInfo import *
from PassBoot import *
import settings

Directory = '/PasswordGenerator'
PWNum_Combo = Directory + settings.PATH + '/PasswordGenerator/PWNumCombo.txt'
PWSpec_Combo = Directory + settings.PATH + '/PasswordGenerator/PWSpecCombo.txt'
# PwMulti_Combo = ''
Pass(Directory)

words = []
characters = []
password = ""
complexity = 2

word_list = open('FileStorage/keywords.txt', 'r')

keywordPath = 'FileStorage/keywords.txt'

Symbols = open('FileStorage/SpecChar.txt', 'r')

SymbolPath = 'FileStorage/SpecChar.txt'

num_lines1 = sum(1 for line in word_list)
num_lines2 = sum(1 for line in Symbols)

word_list = open(keywordPath, "r")
for i in range(num_lines1):
    line = word_list.readline()
    if len(line) > 3:
        words.append(line)

Symbols = open(SymbolPath, "r")
for j in range(num_lines2):
    line = Symbols.readline()
    characters.append(line)


class PassGenClass():

    @staticmethod
    def PWNumCombo():

        output_file = open("PasswordGenerator/PWNumCombo.txt", "a+")

        for k in range(50):
            index = random.randrange(len(words))
            password = words[index][:-1]
            index = random.randrange(10, 99)
            password = password + str(index)

            output_file.write(password + "\n")
        # output_file.close()

    @staticmethod
    def PWSpecCombo():

        output_file = open("PasswordGenerator/PWSpecCombo.txt", "a+")

        for k in range(50):
            flag = 0
            while flag == 0:
                index = random.randrange(len(words))
                password = words[index]
                decision = random.randrange(14)

                for f in range(len(password)):
                    if password[f] == "a" or password[f] == "i" or password[f] == "s" or password[f] == "A" or password[
                        f] == "I" or password[f] == "S":
                        flag = flag + 1

                    if decision <= 2:
                        password = password.replace("i", "!")
                        password = password.replace("I", "!")
                        password = password.replace("s", "$")
                        password = password.replace("S", "$")
                        password = password.replace("a", "@")
                        password = password.replace("A", "@")
                    elif decision > 2 and decision <= 4:
                        password = password.replace("i", "!")
                        password = password.replace("I", "!")
                        password = password.replace("s", "$")
                        password = password.replace("S", "$")
                    elif decision > 4 and decision <= 6:
                        password = password.replace("i", "!")
                        password = password.replace("I", "!")
                        password = password.replace("a", "@")
                        password = password.replace("A", "@")
                    elif decision > 6 and decision <= 8:
                        password = password.replace("s", "$")
                        password = password.replace("S", "$")
                        password = password.replace("a", "@")
                        password = password.replace("A", "@")
                    elif decision > 8 and decision <= 10:
                        password = password.replace("s", "$")
                        password = password.replace("S", "$")
                    elif decision > 10 and decision <= 12:
                        password = password.replace("a", "@")
                        password = password.replace("A", "@")
                    elif decision > 12 and decision <= 14:
                        password = password.replace("i", "!")
                        password = password.replace("I", "!")

            output_file.write(password)
        # output_file.close()

        print(password)
