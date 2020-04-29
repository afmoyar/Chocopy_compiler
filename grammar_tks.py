#symbols
program = "program"
def_a = "def_a"
super_stmt = "super_stmt"
var_def = "var_def"
func_def = "func_def"
class_def = "class_def"
stmt = "stmt"
class_body = "class_body"
def_b ="def_b"
ID = "ID"
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

#the grammar is stored in a dict, each key is a non terminal,
# and each list value represents rules for that non terminal

chocoGrammar = {
    program:
    [
        [def_a, super_stmt]
    ],
    def_a:
    [
        [var_def, def_a],
        [func_def, def_a],
        [class_def, def_a],
        [epsilon]
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
        [def_b]
    ],
    def_b:
    [
        [var_def,def_b],
        [func_def,def_b],

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
        ["tk_ejecuta","type"],
        [epsilon]
    ],
    func_body:
    [
        [func_start, more_stmt]
    ],
    func_start:
    [
        [global_decl, more_stmt],
        [nonlocal_decl, more_stmt],
        [var_def, more_stmt],
        [func_def, more_stmt],
        [epsilon]
    ],
    more_stmt:
    [
        [stmt, super_stmt]
    ],
    typed_var:
    [
        [ID,"tk_dos_puntos","type"]
    ],
    "type":
    [
        [ID],
        [IDSTRING],
        ["tk_cor_izq", "type", "tk_cor_der"]
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
        [typed_var, "tk_asig", literal, NEWLINE]
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
    simple_stmt:
    [
        ["pass"],
        [expr],
        ["return", after_return],
        [target, "tk_asig", targets, expr]
    ],
    after_return:
    [
        [expr],
        [epsilon]
    ],
    targets:
    [
        [target, "tk_asig", targets],
        [epsilon]
    ],
    block:
    [
        [NEWLINE, INDENT, more_stmt, DEDENT]
    ],
    literal:
    [
        ["none"],
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
        [literal, cexpr_hat, cexpr_hat_3, cexpr_hat_4],
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
        [epsilon]
    ],
    more_expr:
    [
        [expr, comma_expr],
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
        [ID],
        [cexpr, target_hat]
    ],
    target_hat:
    [
        ["tk_punto", ID],
        ["tk_cor_izq",expr,"tk_cor_der"]
    ]
}
