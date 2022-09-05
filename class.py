
from xml.dom.pulldom import CHARACTERS


def VerifySpace(word): 
    if ' ' in word:
        print("A palavra possui espaco")
        return bool(0)
    else:
        print("A palavra não tem espaço")
        return bool(1)


def VerifyComment(word): #Corrigir: Se o primeiro caracter da string for um espaço em branco e os próximos forem // considera-se não comentario
    first = word[0]
    if first == '/':
        if first == word[1]:
            # return bool(1)
            print("Este trecho é um comentário")
        else:
            # return bool(0)
            print("Este trecho possui apenas uma '/' ou possuí espaco entre as '/' ")
    else:
        # return bool(0)
        print("Este trecho não é um comentario")


def VerifyReservedWord(word): #Corrigir: Se houver espaço no inicio ou no fim da palavra considera-se não reservada
    reservedWords = ['int', 'double', 'float', 'real', 'break', 'case','char', 'const', 'continue']
    if word in reservedWords:
        print("Essa é uma palavra reservada")
        return bool(1)
    else:
        print("Essa não é uma palavra reservada")
        return bool(0)


def VerifyNumFloat(word):
    limit = 99.99
    size = len(word)
    if size < 6:
        position = word.find('.') # Funcao find retorna a posicao de um caracter na string
        # print(f"Esta é a posição do ponto: {position}")
        tmp = len(word[position:position+3])
        if tmp < 3:
            # return bool(0)
            print("Este número real não possui duas casas decimais")
        else:
            if VerifyNumOrStr(word) == float:
                print("A"*50)
                word = float(word)
                if word <= limit:
                    # return bool(1)
                    print("Este número real é aceito")
                else:
                    # return bool(0)
                    print("Este número real não é aceito")
            else:
                print("Este número real não é aceito")
                return bool(0)
    else: 
        # return bool(0)
        print("Este número possuí mais que duas casas decimais")
 

def VerifyIdentifier(word):
    first = word[0]
    numbers = ['0','1','2','3','4','5','6','7','8','9'] 
    if first in numbers:
        print(f"{word} não é um identificador valido 88")
    else:
        if VerifyReservedWord(word) == False and VerifySpace(word) == True:
            print(f"{word} é um identificador válido")
        else:
            print(f"{word} não é um identificador valido 99")


def VerifyNumInt(word):
    limit=99
    size = len(word)
    word = int(word)
    if size < 4:
        if word <= limit:
            # return bool(1)
            print("Este número inteiro é aceito")
        else:
            # return bool(0)
            print("Este número inteiro não é aceito")


def VerifyNumOrStr(word):
    if word.isdigit() == True:
        wordt=int(word)
        print(f"{word} é um número inteiro")
        return type(wordt)
    else:
        try:
            wordt=float(word)
            print(f"{word} é um numero float")
            return type(wordt)
        except  ValueError:
            print(f"{word} é uma string")
            return type(word)


palavra = 'mm.ll'

# VerifySpace(palavra)
# VerifyComment(palavra)
# VerifyReservedWord(palavra)
# VerifyNumFloat(palavra)
# VerifyIdentifier(palavra)
# VerifyNumInt(palavra)
# VerifyNumOrStr(word)
