num1 = int(input("Escolha um número para análise. "))
A = 0
B = 1
C = 0
while num1 > A:
    A = B + C 
    C = B
    B = A
if num1 == A:
    print(f"O número {num1} está na sequência de Fibonnacci")
else:
    print(f"O número {num1} não está na sequência de Fibonnacci.")
