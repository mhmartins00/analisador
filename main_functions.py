from functions import *

def VerifyComment(word): #Funcao para verificar se o conteúdo é um comentario
    if VerifyEmptyLine(word):
        return bool(0)
    first = word[0]
    if first == '/':
        if word[1] == first:
            return bool(1)
        else:
            return bool(0)
    else:
        return bool(0)


def VerifyReservedWord(word): #Funcao para verificar se o conteúdo é uma palavra reservada
    reservedWords = ['int', 'double', 'float', 'real', 'break', 'case','char', 'const', 'continue']
    if word in reservedWords:
        return bool(1)
    else:
        return bool(0)


def VerifyNumFloat(word): #Funcao para verificar se o conteúdo é um numero real/float
    limit = 99.99
    size = len(word)#Funcap len() retorna o tamanho da string
    if size <= 5:
        position = word.find('.') # Funcao find retorna a posicao de um caracter na string
        tmp = len(word[position:position+3])
        if tmp <= 2:
            return bool(0)
        else:
            if VerifyIsNumOrStr(word) == float: #if para verificar se o conteudo pode ser transformado em um float
                word = float(word)
                if word <= limit:
                    return bool(1)
                else:
                    return bool(0)
            else:
                return bool(0)
    else:
        return bool(0)
 

def VerifyIdentifier(word): #Funcao para verificar se o conteudo é um identificador
    if VerifyEmptyLine(word):
        return bool(0)
    first = word[0] # Pega a primeira letra da palavra
    numbers = ['0','1','2','3','4','5','6','7','8','9'] 
    # special_characters = [".",'"',"'",'!','@', '#', '$', '%', '¨', '&', '*', "(", ')', '[', ']', '{','}', '+', '-', '=','´', '`', ',','<', '>', ';', ':','/','?', '^', '~', "|", ]
    accepted_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    for i in word: #For pela palavra onde é feito validação no IF se existe algum caractere que não é aceito, ou seja, não esta na lista accepted_characters
        if i not in accepted_characters:
            return bool(0)
    if first in numbers: # IF para validar se o primeiro caracter é um número
        return bool(0)
    else:
        if not VerifyReservedWord(word) and not VerifyHaveSpace(word): # IF para validar se a palavara não é um identificador ou se tem espaço
            return bool(1)
        else:
            return bool(0)


def VerifyIsNumInt(word): #Função para verificar se o conteúdo é um inteiro
    limit = 99
    size = len(word)
    if VerifyIsNumOrStr(word) == int:
        word = int(word)
        if size <= 2:
            if word <= limit:
                return bool(1)
            else:
                return bool(0)
        else:
            return bool(0)
    else:
        return bool(0)

def VerifyEmptyWord(word): #Funcao para verificar se é palavra vazia
    if word == '':
        return bool(1)
    else:
        return bool(0)


def MainFunctionVerify(word): #Função principal onde passamos todas funções criadas anteriormente, e a que for TRUE retornará o que é o conteúdo
    if VerifyEmptyWord(word):
        token = "empty"
        return token
    elif VerifyComment(word):
        token = "comment"
        return token
    elif VerifyReservedWord(word):
        token = "reserved"
        return token
    elif VerifyIdentifier(word):
        token = "identify"
        return token
    elif VerifyNumFloat(word):
        token = "real"
        return token
    elif VerifyIsNumInt(word):
        token = "int"
        return token
    else:
        token = "error"
        return token
        