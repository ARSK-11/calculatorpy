print("  =========       =========       ====      ")
print(" =====           ==       ==      ====      ")
print("==               ==       ==      ====      culator python3")
print("==               ===========      ====      ")
print(" =====           ==       ==      ==========")
print("  =========      ==       ==      ==========")
print("-------calculator python-------")
print("calculator manual pakek python awokawok")
print("=======================================")
print("masukan salah satu options di bawah ini")
print("1.options (+)")
print("2.options (-)")
print("3.options (x)")
print("4.options (%)")
print("========================================")
option = int(input("masuk kan salah satu options tersebut: "))
if(option<3):
    print("mongo masuk kan format")
else:
    print("format tidak vailet")
if option==1:
    print("===== silahkan masukan number =====")
    y = int(input("masuk kan nominal number (y): "))
    x = int(input("masuk kan nominal number (x): "))
    sum = y + x
    print("========================")
    print("sucsess ")
    print("+---------------+")
    print("hasil:", sum,)
    print("+---------------+")
if option==2:
    print("===== silahkan masukan number ====")
    y = int(input("masuk kan nominal number (y): "))
    x = int(input("masuk kan nominal number (x): "))
    sum = y - x
    print("========================")
    print("sucsess ")
    print("+---------------+")
    print("hasil:", sum,)
    print("+---------------+")
if option==3:
    print("=============== silahkan masukan number =================")
    y = int(input("masuk kan nominal number (y): "))
    x = int(input("masuk kan nominal number (x): "))
    sum = y * x
    print("========================")
    print("sucsess ")
    print("+---------------+")
    print("hasil:", sum,)
    print("+---------------+")
if option==4:
    print("=============== silahkan masukan number =================")
    y = int(input("masuk kan nominal number (y): "))
    x = int(input("masuk kan nominal number (x): "))
    sum = y / x
    print("========================")
    print("sucsess ")
    print("+---------------+")
    print("hasil:", sum,)
    print("+---------------+")