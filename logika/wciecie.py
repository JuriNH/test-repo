print("Czy jesteś dziewczyną? T/N")
sex = input()
print("Czy pijesz alkohol? T/N")
alko = input()

if sex == "T":
    print("Super") if alko == "T":
    print("Stawiam piwo")
elif alko == "N":
    print("stawiam cole")
else:
    print("Czekam na dziewczynę")
