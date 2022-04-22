import os

c = int(input("Informe uma temperatura em graus Celsius: "))
os.system('clear')

f = (9*c/5)+32

print("Celsius:",c,"--> Fahrenheit:",f)