string = str(input("Qual palavra deseja inverter? "))
string = list(string)
output = []
while string != []:
    output.append(string[-1])
    string.pop(-1)
output = "".join(str(i) for i in output)
print(f"A inversão é: {output}")