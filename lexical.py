import re
import sys
from token_class import Token
import pickle
# print("Hello World")
tokens = []


valid_states = {
    2: ["tk_suma"],  # +
    4: ["tk_mult"],  # *
    5: ["tk_remainder"],  # %
    6: ["tk_par_izq"],  # (
    7: ["tk_par_der"],  # )
    8: ["tk_cor_izq"],  # [
    9: ["tk_cor_der"],  # ]
    10: ["tk_coma"],  # ,
    11: ["tk_dos_puntos"],  # :
    12: ["tk_punto"],  # .
    16: ["tk_menor_igual"],  # <=
    17: ["tk_menor"],  # <
    19: ["tk_mayor_igual"],  # >=
    20: ["tk_mayor"],  # >
    22: ["tk_comparacion"],  # ==
    23: ["tk_asig"],  # =
    25: ["tk_ejecuta"],  # ->
    26: ["tk_menos"],  # -
    28: ["tk_distinto"],  # !=
    30: ["tk_division"],  # //
    32: ["tk_entero"],  #
    34: ["tk_cadena"],  # "bla"
    14: [""],
    39: ["tk_ident"],  # \t o 8 espacios IDENT
	42: ["tk_newline"], # NEWLINE
    43: ["tk_dedent"]   # DEDENT

}


def dt(state, char):
    # print(char)
    global in_str
    if (state == 1):
        if (char == "\n"):
            return 42

        elif (char == '+'):
            return 2

        elif (char == '*'):
            return 4

        elif (char == '%'):
            return 5

        elif (char == '('):
            return 6

        elif (char == ')'):
            return 7

        elif (char == '['):
            return 8

        elif (char == ']'):
            return 9

        elif (char == ','):
            return 10

        elif (char == ':'):
            return 11

        elif (char == '.'):
            return 12

        elif (re.match("[a-zA-Z]", char) or char == '_'):
            return 13

        elif (char == '<'):
            # Can be either less than or less_or_equal than
            return 15

        elif (char == '>'):
            # Can be either greater than or greater_or_equal than
            return 18

        elif (char == '='):
            # can be either comparison or assignment
            return 21

        elif (char == '-'):
            # Can be arrow -> or -
            return 24

        elif (char == '!'):
            # could be != but if the equal is not present the ! alone is not valid
            return 27

        elif (char == '/'):
            # could be // but if the second / is not present the / alone is not valid
            return 29

        elif (re.match("\d", char)):  # digit regular expression
            return 31

        elif (char == '"'):
            # print("could be a string")
            # could be a string
            return 33

        elif (char == '#'):
            return 35

        elif (char == " "):
            return 36

        elif (char == '\t'):
            return 39
        else:
            return -1


    elif (state == 13):
        # Regular expression for word character: (\w) includes digits
        if (re.match("\w", char) or char == '_'):
            return 13
        else:
            return 14

    elif (state == 15):
        if (char == '='):
            # the token is less_or_equal than
            return 16
        else:
            # the token is less than
            return 17

    elif (state == 18):
        if (char == '='):
            # the token is greater_or_equal than
            return 19
        else:
            # the token is greater than
            return 20

    elif (state == 21):
        if (char == '='):
            # the token is == comparison
            return 22
        else:
            # the token is assignment
            return 23

    elif (state == 24):
        if (char == '>'):
            # the token is -> arrow
            return 25
        else:
            # the token is - minus
            return 26

    elif (state == 27):
        if (char == '='):
            # the token is != comparison
            return 28
        else:
            # the token is not valid
            return -1

    elif (state == 29):
        if (char == '/'):
            # the token is //
            return 30
        else:
            # the token is not valid
            return -1

    elif (state == 31):
        if (re.match("\d", char)):
            return 31  # is digit, keep in state 31
        else:
            return 32

    elif (state == 33):
        if (char == '"'):
            # print("end of string")
            return 34

        elif char == "\n":
            in_str = in_str - 1
            # print("string not completed, missing final quote ")
            return -2

        elif not (ord(char) >= 32 and ord(char) <= 126):
            # Is not a valid ASCII character
            return -2
        elif char == '\\':
            return 41

        else:
            # print("is a valid string character, keep in state 33")
            return 33  # is a valid string character, keep in state 33

    elif (state == 35):  # comment
        if (char == '\n'):  # end of line
            return 1

        else:
            return 35  # is part of the comment, keep in state 35
    elif state == 36:
        if char == " ":  # 2 space
            return 37
        else:
            return 40  # just 1 space and something else, needs to do i = i-1

    elif state == 37:
        if char == " ":  # 3 space
            return 38
        else:
            return 40  # just 1 space and something else, needs to do i = i-1

    elif state == 38:
        if char == " ":  # 4 space
            return 39
        else:
            return 40  # just 1 space and something else, needs to do i = i-1
    elif state == 40:  # was checking for ident but there wasnt enough spaces
        return 1
    elif state ==41:
        in_str = in_str - 1
        if(char == "\\" or char == '"' or char == "n" or char == "t"):
            return 33
        else:
            return -2

    else:
        return -1


def check_is_reserved(word):
    with open('reserved.txt') as file:
        for reserved_word in file:
            # print(reserved_word)
            if (word.strip() == reserved_word.strip()):
                # Is a reserved word
                return True
    # Is not a reserved word
    # print('checked '+word)
    return False


def add_token(token, lexeme, row, col):
    token = Token(token, lexeme, row, col)
    tokens.append(token)


def line_full_of_idents():
    if len(tokens) == 0 or type(tokens[-1]) == type("str"):
        return False
    full_of_idents = True
    last_row = tokens[-1].row
    # print("last row: "+str(last_row))
    for token in reversed(tokens):
        if token.row != last_row:
            return full_of_idents
        else:
            if str(token.token).strip("[]").replace("'", "") != "tk_ident":
                return False
    return full_of_idents


def delete_line():
    last_row = tokens[-1].row
    for token in reversed(tokens):
        if token.row == last_row:
            tokens.remove(token)


# line = 'class Animal(object):'


###main
row = 0

with open(sys.argv[1], encoding="utf-8",
          errors="surrogateescape") as file:  # Also works with "ignore" but the printed characters are different
    error = False
    ident = 0
    prev_ident = 0
    prev_row = 0
    diff_ident = False
    global_idents = 0
    for line in file:
        line_idents = 0
        row = row + 1
        col = 0
        lexeme = ""
        state = 1
        i = 0
        #line = line + "\n"  # used for eof checks
        while i < len(line):
            # print("current i:"+ str(i)+" current state: "+str(state)+ " char: "+line[i])
            if state == 1:
                col = i + 1
                in_str = 0
            #print(state,'->')
            lexeme += line[i]
            prev_state = state
            state = dt(state, line[i])
            '''
            if(state == 39):
                ident += 1
                diff_ident = True
                prev_row = row

            if(diff_ident and prev_row != row):
                if (state != 39):
                    add_token("tk_dedent", "", row, col)
                    prev_row = row
                    ident -= 1
                    diff_ident = False
                else:
                    prev_row = row
                    ident += 1
            '''
            if(state == 33 or state == 41):
               in_str = in_str + 1
            # spaces and \t only matter if they are at the begining of line
            '''
            if len(tokens) != 0:
                if ((state == 36 and str(tokens[-1].token).strip("[]").replace("'", "") != "tk_ident") or (
                        state == 39 and prev_state != 38)) and (i != 0):
                    state = 1
            '''
            # print("new state: "+str(state))
            # print(state)
            if state == -1:
                # print("Lexical error on line: "+str(row)+" position: "+str(col))
                tokens.append("Lexical error on line: " + str(row) + " position: " + str(col))
                error = True
                # exit()

            if state == -2:
                # print("Lexical error on line: "+str(row)+" position: "+str(col))
                tokens.append("Lexical error on line: " + str(row) + " position: " + str(col + in_str))
                error = True
                # exit()

            if (state in valid_states):
                # if(state == 14 or state == 16 or state == 19 or state == 22 or state == 99 or state == 28 or state == 30
                #  or state == 31 or state==39):
                # check 28 and 30
                '''
                if(state == 39):
                    print('!!!!!!!!! '+ str(row), str(col))
                    token = valid_states[state]
                    lexeme = ""
                    add_token(token, lexeme, row, col)
                    global_idents = global_idents + 1
                '''
                if (state == 14 or state == 17 or state == 20 or state == 23 or state == 26 or state == 32):
                    # Return 1 character back
                    i = i - 1
                    lexeme = lexeme[:-1].strip()

                if (state == 34):  # string state
                    token = valid_states[state]
                    lemexe = lexeme.strip()
                    add_token(token, lexeme, row, col)

                elif (state == 32):
                    token = valid_states[state]
                    lemexe = lexeme.strip()
                    add_token(token, lexeme, row, col)

                elif (state == 14):
                    is_reserved = check_is_reserved(lexeme)
                    if (is_reserved):
                        token = lexeme.strip()
                        add_token(token, "", row, col)

                    else:
                        # lexeme = lexeme[:-1]
                        token = "id"  # Identifier
                        add_token(token, lexeme, row, col)
                else:
                    token = valid_states[state]
                    lexeme = ""
                    '''
                    if(str(token)   == "['tk_ident']"):
                        print('would insert on ', str(row), str(col))
                        global_idents = global_idents + 1
                    '''
                    if(state == 39):
                        line_idents = line_idents + 1
                        #print('would insert on ', str(row), str(col))
                        print('deb ', 'global_idents: ', global_idents, 'line_idents: ', line_idents, str(row), str(col))
                        if(line_idents > global_idents):
                            global_idents = global_idents + 1
                            add_token(token, lexeme, row, col)

                        else:
                            print('not inserted', str(row), str(col))

                    else:
                        if(line_idents < global_idents):
                            dif = global_idents - line_idents
                            for s in range(0, dif):
                                print('cicle')
                                dedent_token = valid_states[43]
                                add_token(dedent_token, "", row, col)
                                global_idents = global_idents - 1

                        add_token(token, lexeme, row, col)
                state = 1
                lexeme = ""
            elif state == 40:
                i = i - 1
                lexeme = lexeme[:-1]
                state = 1
            i = i + 1
            #print(error)
        if error:
            break
        if line_full_of_idents():
            #delete_line()
            print('full of idents')

for i in range(len(tokens)):
    try:
        if (tokens[i].lexeme == ""):
            print("<" + str(tokens[i].token).strip("[]").replace("'", "") + "," + str(tokens[i].row) + "," + str(
                tokens[i].col) + ">")
        else:
            print("<" + str(tokens[i].token).strip("[]").replace("'", "") + "," + str(
                tokens[i].lexeme).strip() + "," + str(tokens[i].row) + "," + str(tokens[i].col) + ">")
    except:
        # print the lexical error
        print(tokens[i])
        with open('token.list', 'wb') as token_file:
            pickle.dump(tokens, token_file)
        exit()

with open('token.list', 'wb') as token_file:

  pickle.dump(tokens, token_file)
