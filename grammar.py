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
NEWLINE = "NEWLINE"
INDENT = "INDENT"
func_body = "func_body"
DEDENT = "DEDENT"
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
INTEGER = "INTEGER"
STRING = "STRING"
expr_hat = "expr_hat"
member_expr = "member_expr"
index_expr = "index_expr"
bin_op = "bin_op"
cexpr_hat = "cexpr_hat"
cexpr_hat_2 = "cexpr_hat_2"

#empty string
epsilon = "epsilon"

#the grammar is stored in a dict, each key is a non terminal, 
# and each list value represents rules for that non terminal

grammar = {
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
        ["class", ID, "(", ID, ")", ":", NEWLINE, INDENT, class_body, DEDENT],
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
        ["def",ID, "(", params, ")",func_type, ":", NEWLINE, INDENT, func_body, DEDENT]
    ],
    params:
    [
        [typed_var, more_params],
        [epsilon]
    ],
    more_params:
    [
        [",", typed_var, more_params],
        [epsilon]
    ],
    func_type:
    [
        ["->","type"],
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
        [ID,":","type"]
    ],
    "type":
    [
        [ID],
        [IDSTRING],
        ["[", "type", "]"]
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
        [typed_var, "=", literal, NEWLINE]
    ],
    stmt:
    [
        [simple_stmt, NEWLINE],
        ["if", expr, ":", block, block_elif, block_else],
        ["while", expr, ":",block],
        ["for", ID, "in", expr, ":", block]
    ],
    block_elif:
    [
        ["elif", expr, ":", block, block_elif],
        [epsilon]
    ],
    block_else:
    [
        ["else", ":",block],
        [epsilon]
    ],
    simple_stmt:
    [
        ["pass"],
        [expr],
        ["return", after_return],
        [target, "=", targets, expr]
    ],
    after_return:
    [
        [expr],
        [epsilon]
    ],
    targets:
    [
        [target, "=", targets],
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
        [ID,cexpr_hat_2],
        [literal, cexpr_hat],
        ["[", more_expr, "]", cexpr_hat],
        ["(",expr,")", cexpr_hat],
        [member_expr, cexpr_hat_2],
        [index_expr, cexpr_hat],
        ["-", cexpr, cexpr_hat]
    ],
    cexpr_hat:
    [
        [bin_op, cexpr, cexpr_hat],
        [epsilon]
    ],
    cexpr_hat_2:
    [
        [cexpr_hat],
        ["(",more_expr,")",cexpr_hat]
    ],
    more_expr:
    [
        [expr, comma_expr],
        [epsilon]
    ],
    comma_expr:
    [
        [",", expr, comma_expr],
        [epsilon]
    ],
    bin_op:
    [
        ["+"],
        ["-"],
        ["*"],
        ["//"],
        ["%"],
        ["=="],
        ["!="],
        ["<="],
        [">="],
        ["<"],
        [">"],
        ["is"]
    ],
    member_expr:
    [
        [cexpr, ".", ID],
    ],
    index_expr:
    [
        [cexpr, "[", expr,"]"]
    ],
    target:
    [
        [ID],
        [member_expr],
        [index_expr],
    ]
}