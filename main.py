"""
Kurs "Digital History" - Wintersemester 2024
Doku oder so, KA bin kein Programm
"""
import random

print("Launching   K A F F - O - M A T   ...")
max_coffee = 0
input_success = False

while not input_success:
    try:
        max_coffee = int(input("Wieviel Kaffee verträgst du?"))
        input_success = True
    except:
        print("Bitte gib eine gültige Zahl ein!")
    if input_success and max_coffee <= 0:
        print("Bitte gib eine Zahl ein, welche höher als 0 ist!")
        input_success = False
    elif input_success: print("Eingabe wird gespeichert...")
    else: print("K A F F - O - M A T  wird zurückgesetzt...")

print("Kaffee wird getrunken...")


n = 1
while n <= max_coffee:
    print(f"Die Kaffeemenge von {n} Tassen ist noch vertretbar.")
    n = n + 1
print("ZU VIEL KAFFEE!!!! AAAAAAAAAH")
aah = "HH!"
count = random.random() * 100

n = 0

while n<count:
    aah = f"A{aah}"
    n = n+1

print(aah)
