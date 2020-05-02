from grammar_tks import chocoGrammar as grammar
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