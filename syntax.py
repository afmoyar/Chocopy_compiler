import sys
import pickle
import os
import Auxiliary_sets
from grammar_tks import chocoGrammar as grammar
from token_dict import token_list
from token_class import Token
with open('token.list', 'rb') as token_file:
    tokens = pickle.load(token_file)

token = ""
current_pos = -1
predicciones = {}


def next_token():
    global current_pos
    current_pos = current_pos + 1
    if(current_pos < len(tokens)):
       #print(str(tokens[current_pos].lexeme))
       return str(tokens[current_pos].token).strip("[]").replace("'", "")
    else:
       current_pos = current_pos -1
       return "EOF"

def match(expected): #funcion de emparejar
    global token
    if(token == expected or token.upper() == expected):
        print('matched: '+ token)
        return next_token()
    else:
        #print('(match) Syntax error. Expected: '+ str(expected) + ' and recieved: '+ str(token))
        error(expected, match)
        exit()



### Init methods

#PASTE THE GENERATED METHODS HERE!
def program():
    global token
    if(token in predicciones["program"][0]):
        token = match("id")
        id_aux()
    elif(token in predicciones["program"][1]):
        token = match("none")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][2]):
        token = match("True")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][3]):
        token = match("False")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][4]):
        token = match("tk_entero")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][5]):
        IDSTRING()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][6]):
        token = match("tk_cadena")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][7]):
        token = match("tk_cor_izq")
        more_expr()
        token = match("tk_cor_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][8]):
        token = match("tk_par_izq")
        expr()
        token = match("tk_par_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][9]):
        token = match("tk_menos")
        cexpr()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][10]):
        func_def()
        program()
    elif(token in predicciones["program"][11]):
        class_def()
        program()
    elif(token in predicciones["program"][12]):
        token = match("pass")
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][13]):
        token = match("return")
        after_return()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][14]):
        token = match("not")
        expr()
        expr_hat()
        token = match("tk_newline")
        super_stmt()
    elif(token in predicciones["program"][15]):
        token = match("if")
        expr()
        token = match("tk_dos_puntos")
        block()
        block_elif()
        block_else()
        super_stmt()
    elif(token in predicciones["program"][16]):
        token = match("while")
        expr()
        token = match("tk_dos_puntos")
        block()
        super_stmt()
    elif(token in predicciones["program"][17]):
        token = match("for")
        token = match("id")
        token = match("in")
        expr()
        token = match("tk_dos_puntos")
        block()
        super_stmt()
    elif(token not in predicciones["program"][18]):
        error(predicciones["program"], program)
def id_aux():
    global token
    if(token in predicciones["id_aux"][0]):
        token = match("tk_dos_puntos")
        etype()
        token = match("tk_asig")
        literal()
        token = match("tk_newline")
        program()
    elif(token in predicciones["id_aux"][1]):
        targets_hat()
        token = match("tk_newline")
        super_stmt()
    else:
        error(predicciones["id_aux"], id_aux)

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
        var_def()
        def_b()
    elif(token in predicciones["class_body"][2]):
        func_def()
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
    elif(token not in predicciones["def_b"][2]):
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
        etype()
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
        func_start()
    elif(token in predicciones["func_start"][1]):
        nonlocal_decl()
        func_start()
    elif(token in predicciones["func_start"][2]):
        var_def()
        func_start()
    elif(token in predicciones["func_start"][3]):
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
        func_start()
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
        etype()
    else:
        error(predicciones["typed_var"], typed_var)

def etype():
    global token
    if(token in predicciones["etype"][0]):
        token = match("id")
    elif(token in predicciones["etype"][1]):
        IDSTRING()
    elif(token in predicciones["etype"][2]):
        token = match("tk_cor_izq")
        etype()
        token = match("tk_cor_der")
    else:
        error(predicciones["etype"], etype)

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
        token = match("id")
        token = match("tk_dos_puntos")
        etype()
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
        token = match("return")
        after_return()
    elif(token in predicciones["simple_stmt"][2]):
        targets()
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
        token = match("id")
        targets_hat()
    elif(token in predicciones["targets"][1]):
        token = match("none")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
    elif(token in predicciones["targets"][2]):
        token = match("True")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
    elif(token in predicciones["targets"][3]):
        token = match("False")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
    elif(token in predicciones["targets"][4]):
        token = match("tk_entero")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
    elif(token in predicciones["targets"][5]):
        IDSTRING()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
    elif(token in predicciones["targets"][6]):
        token = match("tk_cadena")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
    elif(token in predicciones["targets"][7]):
        token = match("tk_cor_izq")
        more_expr()
        token = match("tk_cor_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
    elif(token in predicciones["targets"][8]):
        token = match("tk_par_izq")
        expr()
        token = match("tk_par_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
    elif(token in predicciones["targets"][9]):
        token = match("tk_menos")
        cexpr()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_2()
    elif(token in predicciones["targets"][10]):
        token = match("not")
        expr()
        expr_hat()
    else:
        error(predicciones["targets"], targets)

def targets_hat():
    global token
    if(token in predicciones["targets_hat"][0]):
        token = match("tk_asig")
        targets()
    elif(token in predicciones["targets_hat"][1]):
        cexpr_hat_2()
        cexpr_hat_3()
        cexpr_hat_4()
        targets_hat_3()
    else:
        error(predicciones["targets_hat"], targets_hat)

def targets_hat_2():
    global token
    if(token in predicciones["targets_hat_2"][0]):
        target_hat()
        token = match("tk_asig")
        targets()
    elif(token in predicciones["targets_hat_2"][1]):
        expr_hat()
    else:
        error(predicciones["targets_hat_2"], targets_hat_2)

def targets_hat_3():
    global token
    if(token in predicciones["targets_hat_3"][0]):
        target_hat()
        token = match("tk_asig")
        targets()
    elif(token in predicciones["targets_hat_3"][1]):
        expr_hat()
    else:
        error(predicciones["targets_hat_3"], targets_hat_3)

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
        token = match("none")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][2]):
        token = match("True")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][3]):
        token = match("False")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][4]):
        token = match("tk_entero")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][5]):
        IDSTRING()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][6]):
        token = match("tk_cadena")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][7]):
        token = match("tk_cor_izq")
        more_expr()
        token = match("tk_cor_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][8]):
        token = match("tk_par_izq")
        expr()
        token = match("tk_par_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
    elif(token in predicciones["cexpr"][9]):
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
        bin_op()
        cexpr()
        cexpr_hat()
    elif(token not in predicciones["cexpr_hat_2"][1]):
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
        token = match("id")
        cexpr_hat_2()
        cexpr_hat_3()
        cexpr_hat_4()
        expr_hat()
        comma_expr()
    elif(token in predicciones["more_expr"][1]):
        token = match("none")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        expr_hat()
        comma_expr()
    elif(token in predicciones["more_expr"][2]):
        token = match("True")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        expr_hat()
        comma_expr()
    elif(token in predicciones["more_expr"][3]):
        token = match("False")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        expr_hat()
        comma_expr()
    elif(token in predicciones["more_expr"][4]):
        token = match("tk_entero")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        expr_hat()
        comma_expr()
    elif(token in predicciones["more_expr"][5]):
        IDSTRING()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        expr_hat()
        comma_expr()
    elif(token in predicciones["more_expr"][6]):
        token = match("tk_cadena")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        expr_hat()
        comma_expr()
    elif(token in predicciones["more_expr"][7]):
        token = match("tk_cor_izq")
        more_expr()
        token = match("tk_cor_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        expr_hat()
        comma_expr()
    elif(token in predicciones["more_expr"][8]):
        token = match("tk_par_izq")
        expr()
        token = match("tk_par_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        expr_hat()
        comma_expr()
    elif(token in predicciones["more_expr"][9]):
        token = match("tk_menos")
        cexpr()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        expr_hat()
        comma_expr()
    elif(token in predicciones["more_expr"][10]):
        token = match("not")
        expr()
        expr_hat()
        comma_expr()
    elif(token not in predicciones["more_expr"][11]):
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
        target_hat_2()
    elif(token in predicciones["target"][1]):
        token = match("none")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        target_hat()
    elif(token in predicciones["target"][2]):
        token = match("True")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        target_hat()
    elif(token in predicciones["target"][3]):
        token = match("False")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        target_hat()
    elif(token in predicciones["target"][4]):
        token = match("tk_entero")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        target_hat()
    elif(token in predicciones["target"][5]):
        IDSTRING()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        target_hat()
    elif(token in predicciones["target"][6]):
        token = match("tk_cadena")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        target_hat()
    elif(token in predicciones["target"][7]):
        token = match("tk_cor_izq")
        more_expr()
        token = match("tk_cor_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        target_hat()
    elif(token in predicciones["target"][8]):
        token = match("tk_par_izq")
        expr()
        token = match("tk_par_der")
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
        target_hat()
    elif(token in predicciones["target"][9]):
        token = match("tk_menos")
        cexpr()
        cexpr_hat()
        cexpr_hat_3()
        cexpr_hat_4()
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

def target_hat_2():
    global token
    if(token in predicciones["target_hat_2"][0]):
        cexpr_hat_2()
        cexpr_hat_3()
        cexpr_hat_4()
        target_hat()
    elif(token not in predicciones["target_hat_2"][1]):
        error(predicciones["target_hat_2"], target_hat_2)
def IDSTRING():
    global token
    if(token in predicciones["IDSTRING"][0]):
        token = match("int")
    elif(token in predicciones["IDSTRING"][1]):
        token = match("bool")
    elif(token in predicciones["IDSTRING"][2]):
        token = match("len")
    elif(token in predicciones["IDSTRING"][3]):
        token = match("print")
    else:
        error(predicciones["IDSTRING"], IDSTRING)


### end methods

def error(expected, funct_where):
    global current_pos
    err_token = tokens[current_pos]
    print(funct_where)
    #print (token_list[err_token.token[0]])
    expected_token = tokensToList(str(expected))
    try:
        print('<'+str(err_token.row)+","+str(err_token.col)+'>'+' Error sintactico: se encontro: \"'+ token_list[err_token.token[0]]+'\"')
    except:
        print('<'+str(err_token.row)+","+str(err_token.col)+'>'+' Error sintactico: se encontro: \"'+ err_token.token+'\"')

    print('se esperaba: '+expected_token)
    exit()
def tokensToList(tokens):

    tokensList = ''.join([str(elem).strip("{}[]'") for elem in tokens])
    separatedTokens = str(tokensList).split(", ")
    tokensList = ""
    for i in separatedTokens:
        tokensList += "\""
        tokensList += str(token_list[str(i)])
        tokensList += "\", "
    tokensList += "."
    tokensList = tokensList.replace(", .",".")
    return tokensList
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
main()

#print(tokens[0].token)
#print(tokens[0].lexeme)

#[0]
#{'tk_suma', 'tk_mult', 'tk_distinto', 'is', 'tk_menos', 'tk_mayor_igual', 'tk_mayor', 'tk_comparacion', 'tk_division', 'tk_menor', 'tk_menor_igual', 'tk_remainder'}

#[1]
#{'tk_division', 'or', 'tk_mult', 'is', 'tk_distinto', 'tk_remainder', 'if', 'tk_menor', 'tk_comparacion', 'tk_cor_izq', 'tk_newline', 'tk_menor_igual', 'tk_mayor', 'tk_suma', 'tk_punto', 'tk_mayor_igual', 'and', 'tk_menos', 'tk_par_izq'}
#{'tk_division', 'or', 'tk_mult', 'is', 'tk_distinto', 'tk_dos_puntos', 'tk_remainder', 'if', 'else', 'tk_menor', 'tk_comparacion', 'tk_cor_der', 'tk_cor_izq', 'tk_newline', 'tk_menor_igual', 'tk_mayor', 'tk_coma', 'tk_suma', 'tk_punto', 'tk_par_der', 'tk_mayor_igual', 'and', 'tk_menos', 'tk_par_izq'}
