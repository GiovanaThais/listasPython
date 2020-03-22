vet=[]
for i in range(10):
    vet.append(int(input("digite numeros: ")))
print(vet)   
resp=(str(input("ver vetor em ordem Crescente (C) ou Decrescente (D): ")))
if resp=='C':
    vet.sort()
    print(vet)
elif resp=='D':
    vet.reverse()
    print(vet)