
def Quiz2Solver(dartResult):

    # tokernize
    tokens = []
    prior_stop = 0
    for i, c in enumerate(dartResult):
        if (c in 'SDT#*') :
            tokens.append('('+dartResult[prior_stop:i+1]+')')
            prior_stop = i+1
    # print(tokens)

    # bonus
    new_token = []
    for token in tokens:
        ret_S = token.replace('S', '**1')
        ret_D = token.replace('D', '**2')
        ret_T = token.replace('T', '**3')

        if (ret_S != token):
            new_token.append(ret_S)
        elif (ret_D != token):
            new_token.append(ret_D)
        elif (ret_T != token):
            new_token.append(ret_T)
        else:
            new_token.append(token)
    tokens = new_token
    # print(tokens)

    # option
    new_token = []
    for i, token in enumerate(tokens):
        if (token == '(*)'):
            if (len(new_token) == 1):
                new_token = new_token[:-1]
                new_token.append(''.join([tokens[i - 1], '*2']))
            elif (len(new_token) >= 2):
                if (tokens[i-2]== '(*)' or tokens[i-2]== '(#)'):
                    temp1 = new_token[-1]
                    temp2 = new_token[-2]
                    new_token = new_token[:-2]
                    new_token.append(''.join([temp2, '*2']))
                    new_token.append(''.join([temp1, '*2']))
                else:
                    new_token = new_token[:-2]
                    new_token.append(''.join([tokens[i - 2],'*2']))
                    new_token.append(''.join([tokens[i - 1], '*2']))
        elif (token == '(#)'):
            new_token = new_token[:-1]
            new_token.append(''.join([tokens[i-1],'*(-1)']))
        else:
            new_token.append(token)
        # print(new_token)
    tokens = new_token
    # print(tokens)

    # evaluation
    score = 0
    for token in tokens:
        score += eval(token)
    # print(score)

    return score