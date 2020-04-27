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
def get_first(alpha,first):
    if(alpha==[epsilon]):
        first.add(epsilon)
        return first
    else: # string of type a1a2a3.....an, n>=1
        a_1 =alpha[0]
        if(is_terminal(a_1)): # string of type a1 where a1 is terminal
            first.add(a_1)
            return first
        elif (len(alpha)==1): # string of type a1 where a1 is nonterminal
            for rule in grammar[alpha]:
                get_first(rule,first)
        else: #string of type a1a2a3.....an, n>1 where a1 is nonterminal
            #add first(a1) - {epislon} to first(alpha)
            first_of_a1=get_first([a_1],first)
            first = first.union(first_of_a1)
            first.discard(epsilon)
            if(epsilon in first_of_a1): #if epsilong belongs to first(a1)
                #add first(a2a3....an)  to first(alpha)
                first.add(get_first(alpha[1:],first))
            


#test grammar
grammar ={
    "A":
    [
        ["B","C"],["bad"]
    ],
    "B":
    [
        ["big","C","boss"],["bet"]
    ],
    "C":
    [
        ["cat"],["cow"]
    ]
}
first= set()
first = get_first("A",first)
print(first)
