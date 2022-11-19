import operator

dict_operadores = {
    '*': operator.mul,
    '/': operator.truediv,
    '+': operator.add,
    '-': operator.sub,
    '**': operator.pow
} 

print("Entre com o operador desejado:")
op = input()

print("Entre com o 1°número:")
n1 = int(input())

print("Entre com o 2°número:")
n2 = int(input())

print("O seu resultado é:",(dict_operadores[op](n1,n2)))