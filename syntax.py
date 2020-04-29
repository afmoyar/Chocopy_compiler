import sys
import pickle
import os
import synt
from grammar_tks import chocoGrammar as grammar

from token_class import Token
with open('token.list', 'rb') as token_file:
    tokens = pickle.load(token_file)

token = ""
current_pos = -1
predicciones = {}

def next_token():
    global current_pos
    if(current_pos < len(tokens)):
       current_pos = current_pos + 1
       #print(str(tokens[current_pos].lexeme))
       return str(tokens[current_pos].token).strip("[]").replace("'", "")
    else:
       return "EOF"

def match(expected): #funcion de emparejar
    global token
    if(token == expected):
        return next_token()
    if(token.upper() == expected):
        return next_token()
    else:
        print('Syntax error. Expected: '+ str(expected) + ' and recieved: '+ str(token))
        exit()

def gen_test():
    #print(grammar["program"])
    for key in grammar:
        num_conditions = 0
        line = dict()

        if(key == 'type'):
           #print(len(grammar[key]))
           for i in range(0, len(grammar[key])):
               num_conditions = num_conditions + 1
               #print(num_conditions)
               if(num_conditions == 1):
                  print('if(token in predicciones["'+key+'"]['+str(i)+']):')
               if(num_conditions > 1):
                  print('elif(token in predicciones["'+key+'"]['+str(i)+']):')
               for j in range(0, len(grammar[key][i])):
                   #print(grammar[key][i][j])
                   symb = grammar[key][i][j]
                   if(symb in grammar.keys()):
                       wr = symb+'()'
                   else:
                       wr = "token = match("+symb+")"
                   print('   '+wr)
           print('else: ')
           print('  error(predicciones["'+key+'"])')




    return
def gen():
    with open('generated.txt', 'w') as f:
         #f.write('tsts2')
         for key in grammar:
            #print(len(grammar[key]))
            f.write('def '+key+'(): \n')
            f.write('    global token \n')
            num_conditions = 0
            line = dict()
            for i in range(0, len(grammar[key])):
                num_conditions = num_conditions + 1
                #print(num_conditions)
                if(num_conditions == 1):
                   #print('if(token in predicciones["'+key+'"]['+str(i)+']):')
                   f.write('    if(token in predicciones["'+key+'"]['+str(i)+']): \n')
                if(num_conditions > 1):
                  # print('elif(token in predicciones["'+key+'"]['+str(i)+']):')
                   f.write('    elif(token in predicciones["'+key+'"]['+str(i)+']): \n')
                for j in range(0, len(grammar[key][i])):
                    #print(grammar[key][i][j])
                    symb = grammar[key][i][j]
                    if(symb in grammar.keys()):
                        wr = '        '+symb+'()  \n'
                    else:
                        wr = '        token = match("'+symb+'") \n'
                    #print('   '+wr)
                    f.write(wr)
            #print('    else: ')
            #print('  error(predicciones["'+key+'"])')
            f.write('    else: \n')
            f.write('        error(predicciones["'+key+'"]) \n')
            f.write('\n')


### Init methods

#PASTE THE GENERATED METHODS HERE!


### end methods

def error(expected):
    global current_pos
    err_token = tokens[current_pos - 1]
    print('Error on '+ str(err_token.token) +' Row: '+str(err_token.row) + ', Col: '+str(err_token.col))
    print('expected: '+str(expected))
    exit()

def main():
    global token
    global tokens
    token = next_token()
    #print(token)
    program()
    print("\n El analisis sintactico ha finalizado exitosamente")
    '''
    for i in range(0,20):
        token = next_token()
        print(token)
    '''

predicciones = synt.main()


gen()
