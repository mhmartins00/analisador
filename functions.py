#encoding: utf-8

def VerifyHaveSpace(word): #Funcao para verificar se existe espaço na string
    if ' ' in word:
        return bool(1)
    else:
        return bool(0)


def VerifyEmptyLine(word): #Funcao para verificar se a linha estava vazia
    if word == '':
        return bool(1)
    else:
        return bool(0)


def VerifyIsNumOrStr(word): #Funcao para verificar se a palavra(string) pode ser tranformada em um numero real ou inteiro
    if word.isdigit():
        wordt=int(word)
        return type(wordt)
    else:
        try:
            wordt=float(word)
            return type(wordt)
        except ValueError:
            return type(word)
