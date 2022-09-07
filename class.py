
from xml.dom.pulldom import CHARACTERS

# Identificadores iniciados por letras e podem continur com números ou letras
# Constantes numéricas inteiras "int" até 99
# Constantes numéricas reais "float" até 99.99, máximo de .99 duas casas decimais
# Comentários de linha, iniciam com "//"
# Palavras reservadas "int, double, float, real, break, case, char, const, continue"

# Ler arquivo-texto e reconhecer o token

# Exibir os tokens de entrada e a linha que aparece, tabela léxica
# Exibir tabela de símbolos
# Lista das linhas onde os erros aparecem, junto com as palavras


def VerifyHaveSpace(word): 
    if ' ' in word:
        print("A palavra possui espaco")
        return bool(1)
    else:
        print("A palavra não tem espaço")
        return bool(0)


def VerifyComment(word): #Corrigir: Se o primeiro caracter da string for um espaço em branco e os próximos forem // considera-se não comentario
    first = word[0]
    if first == '/':
        if word[1] == first:
            print("Este trecho é um comentário")
            return bool(1)
        else:
            print("Este trecho possui apenas uma '/' ou possui espaco entre as '/' ")
            return bool(0)
    else:
        print("Este trecho não é um comentario")
        return bool(0)


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
    if size <= 5:
        position = word.find('.') # Funcao find retorna a posicao de um caracter na string
        # print(f"Esta é a posição do ponto: {position}")
        tmp = len(word[position:position+3])
        if tmp < 3:
            print("Este número real não possui duas casas decimais")
            return bool(0)
        else:
            if VerifyIsNumOrStr(word) == float:
                print("A"*50)
                word = float(word)
                if word <= limit:
                    print("Este número real é aceito")
                    return bool(1)
                else:
                    print("Este número real não é aceito")
                    return bool(0)
            else:
                print("Este número real não é aceito")
                return bool(0)
    else:
        print("Este número possui mais que duas casas decimais")
        return bool(0)
 

def VerifyIdentifier(word):
    first = word[0]
    numbers = ['0','1','2','3','4','5','6','7','8','9'] 
    if first in numbers:
        print(f"{word} não é um identificador valido 88")
        return bool(0)
    else:
        if VerifyReservedWord(word) == False and VerifyHaveSpace(word) == False:
            print(f"{word} é um identificador válido")
            return bool(1)
        else:
            print(f"{word} não é um identificador valido 99")
            return bool(0)


def VerifyIsNumInt(word):
    limit=99
    size = len(word)
    word = int(word)
    if size <= 2:
        if word <= limit:
            print("Este número inteiro é aceito")
            return bool(1)
        else:
            print("Este número inteiro não é aceito")
            return bool(0)
    else:
        return bool(0)


def VerifyIsNumOrStr(word):
    if word.isdigit() == True:
        wordt=int(word)
        print(f"{word} é um número inteiro")
        return type(wordt)
    else:
        try:
            wordt=float(word)
            print(f"{word} é um numero float")
            return type(wordt)
        except ValueError:
            print(f"{word} é uma string")
            return type(word)


def MainFunctionVerify(word):
    if VerifyComment(word):
        return
    elif VerifyReservedWord(word):
        return
    elif VerifyIdentifier(word):
        return
    elif VerifyNumFloat(word):
        return
    elif VerifyIsNumInt(word):
        return
    else:
        print(f"{word} -> Erro no reconhecimento")
        return
        

palavra = 'char'

MainFunctionVerify(palavra)

# VerifyHaveSpace(palavra)
# VerifyComment(palavra)
# VerifyReservedWord(palavra)
# VerifyNumFloat(palavra)
# VerifyIdentifier(palavra)
# VerifyIsNumInt(palavra)
# VerifyIsNumOrStr(palavra)
