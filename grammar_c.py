#symbols
etype = 'etype'
program = "program"
id_aux = "id_aux"
def_a = "def_a"
super_stmt = "super_stmt"
var_def = "var_def"
func_def = "func_def"
class_def = "class_def"
stmt = "stmt"
class_body = "class_body"
def_b ="def_b"
ID = "id"
params = "params"
func_type = "func_type"
NEWLINE = "tk_newline"
INDENT = "tk_ident"
func_body = "func_body"
DEDENT = "tk_dedent"
typed_var ="typed_var"
more_params = "more_params"
func_start = "func_start"
more_stmt = "more_stmt"
global_decl = "global_decl"
nonlocal_decl = "nonlocal_decl"
expr = "expr"
block = "block"
block_elif = "block_elif"
block_else = "block_else"
simple_stmt = "simple_stmt"
after_return = "after_return"
target = "target"
targets = "targets"
logic_op = "logic_op"
cexpr = "cexpr"
more_expr = "more_expr"
comma_expr = "comma_expr"
IDSTRING = "IDSTRING"
literal = "literal"
INTEGER = "tk_entero"
STRING = "tk_cadena"
expr_hat = "expr_hat"
#member_expr = "member_expr" replaced by cexpre_hat_3
#index_expr = "index_expr" replaced by cexpre_hat_4
bin_op = "bin_op"
cexpr_hat = "cexpr_hat"
cexpr_hat_2 = "cexpr_hat_2"
cexpr_hat_3 = "cexpr_hat_3"
cexpr_hat_4 = "cexpr_hat_4"
target_hat = "target_hat"
#empty string
epsilon = "epsilon"
target_hat_2 = "target_hat_2"
targets_hat = "targets_hat"
targets_hat_2 = "targets_hat_2"
targets_hat_3 = "targets_hat_3"
#the grammar is stored in a dict, each key is a non terminal,
# and each list value represents rules for that non terminal

chocoGrammar = {
 program:
    [
        [ID, id_aux],
        #[ID, "tk_dos_puntos", etype, "tk_asig", literal, "tk_newline",program],
        #[ID,target_hat_2,"tk_asig", targets, expr,NEWLINE,super_stmt],
        #[ID,cexpr_hat_2, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],

        ["None", cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2,NEWLINE,super_stmt],
        ["True", cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2,NEWLINE,super_stmt],
        ["False", cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2,NEWLINE,super_stmt],
        [INTEGER, cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2,NEWLINE,super_stmt],
        [IDSTRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2,NEWLINE,super_stmt],
        [STRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2,NEWLINE,super_stmt],
        ["tk_cor_izq", more_expr, "tk_cor_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2,NEWLINE,super_stmt],
        ["tk_par_izq", expr, "tk_par_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2,NEWLINE,super_stmt],
        ["tk_menos", cexpr, cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2,NEWLINE,super_stmt],

        #[var_def, program],
        [func_def, program],
        [class_def, program],
        #[stmt, super_stmt],

        #[simple_stmt, NEWLINE,super_stmt],

        ["pass",NEWLINE,super_stmt],
        ["return", after_return,NEWLINE,super_stmt],
        #[ targets, expr,NEWLINE,super_stmt],

        #[target, "tk_asig", targets, expr,NEWLINE,super_stmt],


        #[ID,target_hat_2,"tk_asig", targets, expr,NEWLINE,super_stmt],
        #["None", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets,NEWLINE,super_stmt],
        #["True", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets,NEWLINE,super_stmt],
        #["False", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets,NEWLINE,super_stmt],
        #[INTEGER, cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets,NEWLINE,super_stmt],
        #[IDSTRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets,NEWLINE,super_stmt],
        #["tk_cadena", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets,NEWLINE,super_stmt],
        #["tk_cor_izq", more_expr, "tk_cor_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets,NEWLINE,super_stmt],
        #["tk_par_izq", expr, "tk_par_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets,NEWLINE,super_stmt],
        #["tk_menos", cexpr, cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets,NEWLINE,super_stmt],


        #[epsilon]
        #[expr,NEWLINE,super_stmt],

        #[cexpr, expr_hat,NEWLINE,super_stmt],

        #[ID,cexpr_hat_2, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],
        #["None", cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],
        #["True", cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],
        #["False", cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],
        #[INTEGER, cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],
        #[IDSTRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],
        #[STRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],
        #["tk_cor_izq", more_expr, "tk_cor_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],
        #["tk_par_izq",expr,"tk_par_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],
        #["tk_menos", cexpr, cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],



        ["not", expr, expr_hat,NEWLINE,super_stmt],

        ["if", expr, "tk_dos_puntos", block, block_elif, block_else,super_stmt],
        ["while", expr, "tk_dos_puntos",block,super_stmt],
        ["for", ID, "in", expr, "tk_dos_puntos", block,super_stmt],

        [epsilon]
    ],
    id_aux:
    [
        ["tk_dos_puntos", etype, "tk_asig", literal, "tk_newline",program],
        #[target_hat_2,"tk_asig", targets,NEWLINE,super_stmt],
        #[cexpr_hat_2, cexpr_hat_3, cexpr_hat_4,expr_hat,NEWLINE,super_stmt],
        [targets_hat,NEWLINE,super_stmt]
    ],
    super_stmt:
    [
        [stmt, super_stmt],
        [epsilon]
    ],
    class_def:
    [
        ["class", ID, "tk_par_izq", ID, "tk_par_der", "tk_dos_puntos", NEWLINE, INDENT, class_body, DEDENT],
    ],
    class_body:
    [
        ["pass", NEWLINE],
        [var_def,def_b],
        [func_def,def_b]
    ],
    def_b:
    [
        [var_def,def_b],
        [func_def,def_b],
        [epsilon]
    ],
    func_def:
    [
        ["def",ID, "tk_par_izq", params, "tk_par_der",func_type, "tk_dos_puntos", NEWLINE, INDENT, func_body, DEDENT]
    ],
    params:
    [
        [typed_var, more_params],
        [epsilon]
    ],
    more_params:
    [
        ["tk_coma", typed_var, more_params],
        [epsilon]
    ],
    func_type:
    [
        ["tk_ejecuta", etype],
        [epsilon]
    ],
    func_body:
    [
        [func_start, more_stmt]
    ],
    func_start:
    [
        [global_decl, func_start],
        [nonlocal_decl, func_start],
        [var_def, func_start],
        ["def", ID, "tk_par_izq", params, "tk_par_der", func_type, "tk_dos_puntos", "tk_newline", "tk_ident", func_body, "tk_dedent", func_start],
        [epsilon]
    ],
    more_stmt:
    [
        [stmt, super_stmt]
    ],
    typed_var:
    [
        [ID,"tk_dos_puntos", etype]
    ],
    etype:
    [
        [ID],
        [IDSTRING],
        ["tk_cor_izq", etype, "tk_cor_der"]
    ],
    global_decl:
    [
        ["global", ID, NEWLINE]
    ],
    nonlocal_decl:
    [
        ["nonlocal", ID, NEWLINE ]
    ],
    var_def:
    [
        #[typed_var, "tk_asig", literal, NEWLINE]
        [ID, "tk_dos_puntos", etype, "tk_asig", literal, "tk_newline"]
    ],
    stmt:
    [
        [simple_stmt, NEWLINE],
        ["if", expr, "tk_dos_puntos", block, block_elif, block_else],
        ["while", expr, "tk_dos_puntos",block],
        ["for", ID, "in", expr, "tk_dos_puntos", block]
    ],
    block_elif:
    [
        ["elif", expr, "tk_dos_puntos", block, block_elif],
        [epsilon]
    ],
    block_else:
    [
        ["else", "tk_dos_puntos",block],
        [epsilon]
    ],
    ##test line 2
    simple_stmt:
    [
        ["pass"],
        ["return", after_return],
        [ targets]
    ],
    after_return:
    [
        [expr],
        [epsilon]
    ],
    targets:
    [

        [ID,targets_hat],
        ["None", cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2],
        ["True", cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2],
        ["False", cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2],
        [INTEGER, cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2],
        [IDSTRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2],
        [STRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2],
        ["tk_cor_izq", more_expr, "tk_cor_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2],
        ["tk_par_izq", expr, "tk_par_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2],
        ["tk_menos", cexpr, cexpr_hat, cexpr_hat_3, cexpr_hat_4,targets_hat_2],

        #[target, "tk_asig", targets],

        #[ID,target_hat_2,"tk_asig", targets],
        #["None", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets],
        #["True", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets],
        #["False", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets],
        #[INTEGER, cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets],
        #[IDSTRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets],
        #[STRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets],
        #["tk_cor_izq", more_expr, "tk_cor_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets],
        #["tk_par_izq", expr, "tk_par_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets],
        #["tk_menos", cexpr, cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets],


        #[epsilon] replaced epsilon by expr
        #[expr]

        #[cexpr, expr_hat],

        #[ID,cexpr_hat_2, cexpr_hat_3, cexpr_hat_4,expr_hat],
        #["None", cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat],
        #["True", cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat],
        #["False", cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat],
        #[INTEGER, cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat],
        #[IDSTRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat],
        #[STRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat],
        #["tk_cor_izq", more_expr, "tk_cor_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat],
        #["tk_par_izq", expr, "tk_par_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat],
        #["tk_menos", cexpr, cexpr_hat, cexpr_hat_3, cexpr_hat_4,expr_hat],

        ["not", expr, expr_hat]
    ],
    targets_hat:
    [
        #[target_hat_2,"tk_asig", targets],

        #[cexpr_hat_2, cexpr_hat_3, cexpr_hat_4, target_hat,"tk_asig", targets],
        ["tk_asig", targets],


        #[cexpr_hat_2, cexpr_hat_3, cexpr_hat_4,expr_hat]

        #[cexpr_hat_2, cexpr_hat_3, cexpr_hat_4,targets_hat_2]#removed cexpr_hat_4 because it was giving problems
        [cexpr_hat_2, cexpr_hat_3,targets_hat_2]
    ],
    targets_hat_2:
    [
        #[target_hat, "tk_asig", targets],
        ["tk_punto", ID,"tk_asig", targets],
        ["tk_cor_izq",expr,"tk_cor_der","tk_asig", targets],
        
        [expr_hat],

    ],
    targets_hat_3:
    [
        [target_hat,"tk_asig", targets],
        [expr_hat]
    ],
    block:
    [
        [NEWLINE, INDENT, more_stmt, DEDENT]
    ],
    literal:
    [
        ["None"],
        ["True"],
        ["False"],
        [INTEGER],
        [IDSTRING],
        [STRING]
    ],
    expr:
    [
        [cexpr, expr_hat],
        ["not", expr, expr_hat]
    ],
    expr_hat:
    [
        [logic_op, expr, expr_hat],
        ["if", expr, "else", expr,expr_hat],
        [epsilon]
    ],
    logic_op:
    [
        ["and"],
        ["or"],
    ],
    cexpr:
    [
        [ID,cexpr_hat_2, cexpr_hat_3, cexpr_hat_4],
        ["None", cexpr_hat, cexpr_hat_3, cexpr_hat_4],
        ["True", cexpr_hat, cexpr_hat_3, cexpr_hat_4],
        ["False", cexpr_hat, cexpr_hat_3, cexpr_hat_4],
        [INTEGER, cexpr_hat, cexpr_hat_3, cexpr_hat_4],
        [IDSTRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4],
        [STRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4],
        ["tk_cor_izq", more_expr, "tk_cor_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4],
        ["tk_par_izq",expr,"tk_par_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4],
        ["tk_menos", cexpr, cexpr_hat, cexpr_hat_3, cexpr_hat_4]
    ],
    cexpr_hat:
    [
        [bin_op, cexpr, cexpr_hat],
        [epsilon]
    ],
    cexpr_hat_2:
    [
        #[bin_op, cexpr, cexpr_hat],
        #[epsilon]
        [cexpr_hat],
        ["tk_par_izq",more_expr,"tk_par_der",cexpr_hat]
    ],
    cexpr_hat_3:
    [
        ["tk_punto", ID, cexpr_hat_2, cexpr_hat_3],
        [epsilon]
    ],
    cexpr_hat_4:
    [
        ["tk_cor_izq", expr,"tk_cor_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4],
        ## testing line
        ["tk_par_izq", expr,"tk_par_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4],
        ##
        [epsilon]
    ],
    more_expr:
    [
        [ID, cexpr_hat_2, cexpr_hat_3, cexpr_hat_4, expr_hat, comma_expr],
        ["None", cexpr_hat, cexpr_hat_3, cexpr_hat_4, expr_hat, comma_expr],
        ["True", cexpr_hat, cexpr_hat_3, cexpr_hat_4, expr_hat, comma_expr],
        ["False", cexpr_hat, cexpr_hat_3, cexpr_hat_4, expr_hat, comma_expr],
        ["tk_entero", cexpr_hat, cexpr_hat_3, cexpr_hat_4, expr_hat, comma_expr],
        [IDSTRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4, expr_hat, comma_expr],
        ["tk_cadena", cexpr_hat, cexpr_hat_3, cexpr_hat_4, expr_hat, comma_expr],
        ["tk_cor_izq", more_expr, "tk_cor_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4, expr_hat, comma_expr],
        ["tk_par_izq", expr, "tk_par_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4, expr_hat, comma_expr],
        ["tk_menos", cexpr, cexpr_hat, cexpr_hat_3, cexpr_hat_4, expr_hat, comma_expr],
        ["not", expr, expr_hat, comma_expr],
        [epsilon]
    ],
    comma_expr:
    [
        ["tk_coma", expr, comma_expr],
        [epsilon]
    ],
    bin_op:
    [
        ["tk_suma"],
        ["tk_menos"],
        ["tk_mult"],
        ["tk_division"],
        ["tk_remainder"],
        ["tk_comparacion"],
        ["tk_distinto"],
        ["tk_menor_igual"],
        ["tk_mayor_igual"],
        ["tk_menor"],
        ["tk_mayor"],
        ["is"]
    ],
    target:
    [
        [ID,target_hat_2],
        #[ID],
        #[ID, cexpr_hat_2, cexpr_hat_3, cexpr_hat_4, target_hat],
        ["None", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat],
        ["True", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat],
        ["False", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat],
        ["tk_entero", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat],
        [IDSTRING, cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat],
        ["tk_cadena", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat],
        ["tk_cor_izq", more_expr, "tk_cor_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat],
        ["tk_par_izq", expr, "tk_par_der", cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat],
        ["tk_menos", cexpr, cexpr_hat, cexpr_hat_3, cexpr_hat_4, target_hat]
        #[ID],
        #[cexpr, target_hat]
    ],
    target_hat:
    [
        ["tk_punto", ID],
        ["tk_cor_izq",expr,"tk_cor_der"],
    ],
    target_hat_2:
    [
        [cexpr_hat_2, cexpr_hat_3, cexpr_hat_4, target_hat],
        [epsilon]
    ],
    IDSTRING:[
        ["int"],
        ["bool"],
        ["len"],
        ["print"],
        ["str"],
        ["object"]
    ]
}
