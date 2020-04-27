#import grammar made in grammar.py
#from grammar import grammar

#obtaining the list of tokens from the lexical analyser
import pickle
from token_class import Token
with open('token.list', 'rb') as token_file:
    tokens = pickle.load(token_file)

epsilon = "epsilon"

def is_terminal(symbol):
    if(symbol in grammar.keys()):
        return False
    else:
        return True

#alpha is a list containing a list of terminasl or non terminal, something like a1a2a3.....an is [a1,a2,...,an]
#where ai could be terminasl or non terminal
def get_first_rec(alpha,first):
    print("alpha", alpha)
    print("first", first)
    if(alpha==[epsilon]):
        print("alpha is [epsilon]")
        first.add(epsilon)
        return first
    else: # string of type a1a2a3.....an, n>=1
        print("string of type a1a2a3.....an, n>=1")
        a_1 =alpha[0]
        if(is_terminal(a_1)): # string of type a1 where a1 is terminal
            print("string of type a1 where a1 is terminal")
            first.add(a_1)
            return first
        elif (len(alpha)==1): # string of type a1 where a1 is nonterminal
            print("string of type a1 where a1 is nonterminal")
            for rule in grammar[a_1]:
               first = get_first_rec(rule,first)
            return first
        else: #string of type a1a2a3.....an, n>1 where a1 is nonterminal
            print("string of type a1a2a3.....an, n>1 where a1 is nonterminal")
            #add first(a1) - {epislon} to first(alpha)
            first_of_a1=get_first_rec([a_1],first)
            first = first.union(first_of_a1)
            first.discard(epsilon)
            if(epsilon in first_of_a1): #if epsilong belongs to first(a1)
                print("if epsilong belongs to first(a1)")
                #add first(a2a3....an)  to first(alpha)
                first.union(get_first_rec(alpha[1:],first))
            return first
            
def get_first(alpha):
    first = set()
    first = get_first_rec(alpha,first)
    return first

#test grammar
grammar ={
    "A":
    [
        ["B","C"],["ant", "A" ,"all"]
    ],
    "B":
    [
        ["big","C"],["bus","A","boss"],[epsilon]
    ],
    "C":
    [
        ["cat"],["cow"]
    ]
}

first_a = get_first(["A"])
first_b = get_first(["B"])
first_c = get_first(["C"])
print("----------------------------------------------------")
print("first(A)", first_a)
print("first(B)", first_b)
print("first(C)", first_c)
