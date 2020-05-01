import sys
import pickle
import os

import Auxiliary_sets
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
    if(token == expected or token.upper() == expected):
        print('matched: '+ token)
        return next_token()
    else:
        print('(match) Syntax error. Expected: '+ str(expected) + ' and recieved: '+ str(token))
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
    #methods auto-generation function
    with open('generated.txt', 'w') as f:
         #f.write('tsts2')
         for key in grammar:
            #print(len(grammar[key]))
            f.write('def '+key+'(): \n')
            f.write('    global token \n')
            num_conditions = 0
            line = dict()
            ext = False
            for i in range(0, len(grammar[key])):
                num_conditions = num_conditions + 1
                #print(num_conditions)
                ##sorry about this###
                flag = False
                for j in range(0, len(grammar[key][i])):
                    #print(grammar[key][i][j])
                    symb = grammar[key][i][j]
                    if(symb == 'epsilon'):
                       flag = True
                       ext = True
                if(flag):
                   f.write('    elif(token not in predicciones["'+key+'"]['+str(i)+']): \n')
                   f.write('        error(predicciones["'+key+'"], '+key+') \n')
                   continue
                ####################
                if(num_conditions == 1):
                   #print('if(token in predicciones["'+key+'"]['+str(i)+']):')
                   f.write('    if(token in predicciones["'+key+'"]['+str(i)+']): \n')
                if(num_conditions > 1):
                  # print('elif(token in predicciones["'+key+'"]['+str(i)+']):')
                   f.write('    elif(token in predicciones["'+key+'"]['+str(i)+']): \n')
                for j in range(0, len(grammar[key][i])):
                    #print(grammar[key][i][j])
                    symb = grammar[key][i][j]
                    if(symb == 'epsilon'):
                       continue
                    if(symb in grammar.keys()):
                        wr = '        '+symb+'()  \n'
                    else:
                        wr = '        token = match("'+symb+'") \n'
                    #print('   '+wr)
                    f.write(wr)
            #print('    else: ')
            #print('  error(predicciones["'+key+'"])')
            if(ext):
               continue
            f.write('    else: \n')
            f.write('        error(predicciones["'+key+'"], '+key+') \n')
            f.write('\n')


### Init methods

#PASTE THE GENERATED METHODS HERE!
def program():
    global token
    if(token in predicciones["program"][0]):
        def_a()
        super_stmt()
    else:
        error(predicciones["program"], program)

def def_a():
    global token
    if(token in predicciones["def_a"][0]):
        var_def()
        def_a()
    elif(token in predicciones["def_a"][1]):
        func_def()
        def_a()
    elif(token in predicciones["def_a"][2]):
        class_def()
        def_a()
    elif(token not in predicciones["def_a"][3]):
        error(predicciones["def_a"], def_a)
def super_stmt():
    global token
    if(token in predicciones["super_stmt"][0]):
        stmt()
        super_stmt()
    elif(token not in predicciones["super_stmt"][1]):
        error(predicciones["super_stmt"], super_stmt)
def class_def():
    global token
    if(token in predicciones["class_def"][0]):
        token = match("class")
        token = match("id")
        token = match("tk_par_izq")
        token = match("id")
        token = match("tk_par_der")
        token = match("tk_dos_puntos")
        token = match("tk_newline")
        token = match("tk_ident")
        class_body()
        token = match("tk_dedent")
    else:
        error(predicciones["class_def"], class_def)

def class_body():
    global token
    if(token in predicciones["class_body"][0]):
        token = match("pass")
        token = match("tk_newline")
    elif(token in predicciones["class_body"][1]):
        def_b()
    else:
        error(predicciones["class_body"], class_body)

def def_b():
    global token
    if(token in predicciones["def_b"][0]):
        var_def()
        def_b()
    elif(token in predicciones["def_b"][1]):
        func_def()
        def_b()
    else:
        error(predicciones["def_b"], def_b)

def func_def():
    global token
    if(token in predicciones["func_def"][0]):
        token = match("def")
        token = match("id")
        token = match("tk_par_izq")
        params()
        token = match("tk_par_der")
        func_type()
        token = match("tk_dos_puntos")
        token = match("tk_newline")
        token = match("tk_ident")
        func_body()
        token = match("tk_dedent")
    else:
        error(predicciones["func_def"], func_def)

def params():
    global token
    if(token in predicciones["params"][0]):
        typed_var()
        more_params()
    elif(token not in predicciones["params"][1]):
        error(predicciones["params"], params)
def more_params():
    global token
    if(token in predicciones["more_params"][0]):
        token = match("tk_coma")
        typed_var()
        more_params()
    elif(token not in predicciones["more_params"][1]):
        error(predicciones["more_params"], more_params)
def func_type():
    global token
    if(token in predicciones["func_type"][0]):
        token = match("tk_ejecuta")
        type()
    elif(token not in predicciones["func_type"][1]):
        error(predicciones["func_type"], func_type)
def func_body():
    global token
    if(token in predicciones["func_body"][0]):
        func_start()
        more_stmt()
    else:
        error(predicciones["func_body"], func_body)

def func_start():
    global token
    if(token in predicciones["func_start"][0]):
        global_decl()
        more_stmt()
    elif(token in predicciones["func_start"][1]):
        nonlocal_decl()
        more_stmt()
    elif(token in predicciones["func_start"][2]):
        var_def()
        more_stmt()
    elif(token in predicciones["func_start"][3]):
        func_def()
        more_stmt()
    elif(token not in predicciones["func_start"][4]):
        error(predicciones["func_start"], func_start)
def more_stmt():
    global token
    if(token in predicciones["more_stmt"][0]):
        stmt()
        super_stmt()
    else:
        error(predicciones["more_stmt"], more_stmt)

def typed_var():
    global token
    if(token in predicciones["typed_var"][0]):
        token = match("id")
        token = match("tk_dos_puntos")
        type()
    else:
        error(predicciones["typed_var"], typed_var)

def type():
    global token
    if(token in predicciones["type"][0]):
        token = match("id")
    elif(token in predicciones["type"][1]):
        IDSTRING()
    elif(token in predicciones["type"][2]):
        token = match("tk_cor_izq")
        type()
        token = match("tk_cor_der")
    else:
        error(predicciones["type"], type)

def global_decl():
    global token
    if(token in predicciones["global_decl"][0]):
        token = match("global")
        token = match("id")
        token = match("tk_newline")
    else:
        error(predicciones["global_decl"], global_decl)

def nonlocal_decl():
    global token
    if(token in predicciones["nonlocal_decl"][0]):
        token = match("nonlocal")
        token = match("id")
        token = match("tk_newline")
    else:
        error(predicciones["nonlocal_decl"], nonlocal_decl)

def var_def():
    global token
    if(token in predicciones["var_def"][0]):
        typed_var()
        token = match("tk_asig")
        literal()
        token = match("tk_newline")
    else:
        error(predicciones["var_def"], var_def)

def stmt():
    global token
    if(token in predicciones["stmt"][0]):
        simple_stmt()
        token = match("tk_newline")
    elif(token in predicciones["stmt"][1]):
        token = match("if")
        expr()
        token = match("tk_dos_puntos")
        block()
        block_elif()
        block_else()
    elif(token in predicciones["stmt"][2]):
        token = match("while")
        expr()
        token = match("tk_dos_puntos")
        block()
    elif(token in predicciones["stmt"][3]):
        token = match("for")
        token = match("id")
        token = match("in")
        expr()
        token = match("tk_dos_puntos")
        block()
    else:
        error(predicciones["stmt"], stmt)

def block_elif():
    global token
    if(token in predicciones["block_elif"][0]):
        token = match("elif")
        expr()
        token = match("tk_dos_puntos")
        block()
        block_elif()
    elif(token not in predicciones["block_elif"][1]):
        error(predicciones["block_elif"], block_elif)
def block_else():
    global token
    if(token in predicciones["block_else"][0]):
        token = match("else")
        token = match("tk_dos_puntos")
        block()
    elif(token not in predicciones["block_else"][1]):
        error(predicciones["block_else"], block_else)
def simple_stmt():
    global token
    if(token in predicciones["simple_stmt"][0]):
        token = match("pass")
    elif(token in predicciones["simple_stmt"][1]):
        expr()
    elif(token in predicciones["simple_stmt"][2]):
        token = match("return")
        after_return()
    elif(token in predicciones["simple_stmt"][3]):
        target()
        token = match("tk_asig")
        targets()
        expr()
    else:
        error(predicciones["simple_stmt"], simple_stmt)

def after_return():
    global token
    if(token in predicciones["after_return"][0]):
        expr()
    elif(token not in predicciones["after_return"][1]):
        error(predicciones["after_return"], after_return)
def targets():
    global token
    if(token in predicciones["targets"][0]):
        target()
        token = match("tk_asig")
        targets()
    elif(token not in predicciones["targets"][1]):
        error(predicciones["targets"], targets)
def block():
    global token
    if(token in predicciones["block"][0]):
        token = match("tk_newline")
        token = match("tk_ident")
        more_stmt()
        token = match("tk_dedent")
    else:
        error(predicciones["block"], block)

def literal():
    global token
    if(token in predicciones["literal"][0]):
        token = match("none")
    elif(token in predicciones["literal"][1]):
        token = match("True")
    elif(token in predicciones["literal"][2]):
        token = match("False")
    elif(token in predicciones["literal"][3]):
        token = match("tk_entero")
    elif(token in predicciones["literal"][4]):
        IDSTRING()
    elif(token in predicciones["literal"][5]):
        token = match("tk_cadena")
    else:
        error(predicciones["literal"], literal)

def expr():
    global token
    if(token in predicciones["expr"][0]):
        cexpr()
        expr_hat()
    elif(token in predicciones["expr"][1]):
        token = match("not")
        expr()
        expr_hat()
    else:
        error(predicciones["expr"], expr)

def expr_hat():
    global token
    if(token in predicciones["expr_hat"][0]):
        logic_op()
        expr()
        expr_hat()
    elif(token in predicciones["expr_hat"][1]):
        token = match("if")
        expr()
        token = match("else")
        expr()
        expr_hat()
    elif(token not in predicciones["expr_hat"][2]):
        error(predicciones["expr_hat"], expr_hat)
def logic_op():
    global token
    if(token in predicciones["logic_op"][0]):
        token = match("and")
    elif(token in predicciones["logic_op"][1]):
        token = match("or")
    else:
        error(predicciones["logic_op"], logic_op)

def cexpr():
    global token
    if(token in predicciones["cexpr"][0]):
        token = match("id")
        cexpr_hat_2()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][1]):
        literal()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][2]):
        token = match("tk_cor_izq")
        more_expr()
        token = match("tk_cor_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][3]):
        token = match("tk_par_izq")
        expr()
        token = match("tk_par_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][4]):
        token = match("tk_menos")
        cexpr()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    else:
        error(predicciones["cexpr"], cexpr)

def cexpr_hat():
    global token
    if(token in predicciones["cexpr_hat"][0]):
        bin_op()
        cexpr()
        cexpr_hat()
    elif(token not in predicciones["cexpr_hat"][1]):
        error(predicciones["cexpr_hat"], cexpr_hat)
def cexpr_hat_2():
    global token
    if(token in predicciones["cexpr_hat_2"][0]):
        cexpr_hat()
    elif(token in predicciones["cexpr_hat_2"][1]):
        token = match("tk_par_izq")
        more_expr()
        token = match("tk_par_der")
        cexpr_hat()
    else:
        error(predicciones["cexpr_hat_2"], cexpr_hat_2)

def cexpr_hat_3():
    global token
    if(token in predicciones["cexpr_hat_3"][0]):
        token = match("tk_punto")
        token = match("id")
        cexpr_hat_2()
        cexpr_hat_3()
    elif(token not in predicciones["cexpr_hat_3"][1]):
        error(predicciones["cexpr_hat_3"], cexpr_hat_3)
def cexpr_hat_4():
    global token
    if(token in predicciones["cexpr_hat_4"][0]):
        token = match("tk_cor_izq")
        expr()
        token = match("tk_cor_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr_hat_4"][1]):
        token = match("tk_par_izq")
        expr()
        token = match("tk_par_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token not in predicciones["cexpr_hat_4"][2]):
        error(predicciones["cexpr_hat_4"], cexpr_hat_4)
def more_expr():
    global token
    if(token in predicciones["more_expr"][0]):
        expr()
        comma_expr()
    elif(token not in predicciones["more_expr"][1]):
        error(predicciones["more_expr"], more_expr)
def comma_expr():
    global token
    if(token in predicciones["comma_expr"][0]):
        token = match("tk_coma")
        expr()
        comma_expr()
    elif(token not in predicciones["comma_expr"][1]):
        error(predicciones["comma_expr"], comma_expr)
def bin_op():
    global token
    if(token in predicciones["bin_op"][0]):
        token = match("tk_suma")
    elif(token in predicciones["bin_op"][1]):
        token = match("tk_menos")
    elif(token in predicciones["bin_op"][2]):
        token = match("tk_mult")
    elif(token in predicciones["bin_op"][3]):
        token = match("tk_division")
    elif(token in predicciones["bin_op"][4]):
        token = match("tk_remainder")
    elif(token in predicciones["bin_op"][5]):
        token = match("tk_comparacion")
    elif(token in predicciones["bin_op"][6]):
        token = match("tk_distinto")
    elif(token in predicciones["bin_op"][7]):
        token = match("tk_menor_igual")
    elif(token in predicciones["bin_op"][8]):
        token = match("tk_mayor_igual")
    elif(token in predicciones["bin_op"][9]):
        token = match("tk_menor")
    elif(token in predicciones["bin_op"][10]):
        token = match("tk_mayor")
    elif(token in predicciones["bin_op"][11]):
        token = match("is")
    else:
        error(predicciones["bin_op"], bin_op)

def target():
    global token
    if(token in predicciones["target"][0]):
        token = match("id")
    elif(token in predicciones["target"][1]):
        cexpr()
        target_hat()
    else:
        error(predicciones["target"], target)

def target_hat():
    global token
    if(token in predicciones["target_hat"][0]):
        token = match("tk_punto")
        token = match("id")
    elif(token in predicciones["target_hat"][1]):
        token = match("tk_cor_izq")
        expr()
        token = match("tk_cor_der")
    else:
        error(predicciones["target_hat"], target_hat)

def IDSTRING():
    global token
    if(token in predicciones["IDSTRING"][0]):
        token = match("int")
    elif(token in predicciones["IDSTRING"][1]):
        token = match("bool")
    elif(token in predicciones["IDSTRING"][2]):
        token = match("len")
    else:
        error(predicciones["IDSTRING"], IDSTRING)




### end methods

def error(expected, funct_where):
    global current_pos
    err_token = tokens[current_pos ]
    print(funct_where)
    print('(else) Error on: '+ str(err_token.token) +' Row: '+str(err_token.row) + ', Col: '+str(err_token.col))
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

#predicciones = synt.main()
predicciones = Auxiliary_sets.main()
#print(predicciones['def_a'])
gen()
main()

#print(tokens[0].token)
#print(tokens[0].lexeme)
