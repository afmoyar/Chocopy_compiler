#import grammar made in grammar.py
from grammar import chocoGrammar as grammar
from grammar import *
#obtaining the list of tokens from the lexical analyser
import pickle
from token_class import Token
with open('token.list', 'rb') as token_file:
    tokens = pickle.load(token_file)

epsilon = "epsilon"
#here it goes the first symbol of the grammar
first_symbol = "A"

def is_terminal(symbol):
    if(symbol in grammar.keys()):
        return False
    else:
        return True

#firsts dict will store first(X) for every X non terminal
firsts = dict()
#symbol stack will help to recognise left recursion and cicles in grammar
symbol_stack = list()
#alpha is a list containing a list of terminasl or non terminal, something like a1a2a3.....an is [a1,a2,...,an]
#where ai could be terminasl or non terminal
def get_first_rec(alpha,first):
    #print("alpha", alpha)
    #print("first", first)
    #print("all first so far:",firsts)
    if(alpha==[epsilon]):
        #print("alpha is [epsilon]")
        first.add(epsilon)
        return first
    else: # string of type a1a2a3.....an, n>=1
        #print("string of type a1a2a3.....an, n>=1")
        a_1 =alpha[0]
        if(is_terminal(a_1)): # string of type a1 where a1 is terminal
            #print("string of type a1 where a1 is terminal")
            first.add(a_1)
            return first
        elif (len(alpha)==1): # string of type a1 where a1 is nonterminal
            #print("string of type a1 where a1 is nonterminal")
            if a_1 in firsts:
                return firsts[a_1]
            else:
                for rule in grammar[a_1]:
                    first_of_rule = get_first_rec(rule,set())
                    first = first.union(first_of_rule)
                return first
        else: #string of type a1a2a3.....an, n>1 where a1 is nonterminal
            #print("string of type a1a2a3.....an, n>1 where a1 is nonterminal")
            if(a_1 in symbol_stack):
                symbol_stack.append(a_1)
                print("possible left recursion of cicle revolving:", symbol_stack)
                print("firsts made so far", firsts)
                exit()
            symbol_stack.append(a_1)
            #add first(a1) - {epislon} to first(alpha)
            if a_1 not in firsts:
                first_of_a1=get_first_rec([a_1],set())
                firsts[a_1] = first_of_a1
            else:
                first_of_a1 = firsts[a_1]
            symbol_stack.pop()
            first = first.union(first_of_a1)
            first.discard(epsilon)
            if(epsilon in first_of_a1): #if epsilong belongs to first(a1)
                #print("if epsilong belongs to first(a1)")
                #add first(a2a3....an)  to first(alpha)
                first = first.union(get_first_rec(alpha[1:],set()))
            return first

#where non_terminal is a string representing a non terminal symbol          
def get_first(non_terminal):
    if non_terminal in firsts:
        return firsts[non_terminal]
    else:
        first = set()
        first = get_first_rec([non_terminal],first)
    return first

#non_terminan is a string a1 whre a1 is non terminal
def get_next(non_terminal):
    next = set()
    if non_terminal == first_symbol:
        next.add("$")
    #looking for rules where non_terminal belongs to rule
    for B, list_of_rules in grammar.items():
        for rule in list_of_rules:
            if non_terminal in rule:
                #found a rule
                start=rule.index(non_terminal)+1
                if(start == len(rule)):
                    #non_terminal is the last symbol of rule
                    next_of_B = get_next(B)
                    next = next.union(next_of_B)
                else:
                    first_of_beta = get_first_rec(rule[start:],set())
                    next = next.union(first_of_beta)
                    next.discard(epsilon)
                    if epsilon in first_of_beta:
                        next_of_B = get_next(B)
                        next = next.union(next_of_B)
    return next


for non_terminal in grammar:
    print("first(",non_terminal, "):", get_first(non_terminal))

for non_terminal in grammar:
    print("next(",non_terminal, "):", get_next(non_terminal))