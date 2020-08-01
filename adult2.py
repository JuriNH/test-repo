print("Ile masz lat?")
age = int(input())
print("Czy jesteś odpowiedzialny? T/N")
responsible = input()

if age < 18:
    print("Do pełnoletności brakuje Ci:", 18 - age, "lat")
elif age >= 100:
    print("Czy napewno masz tyle lat?")
elif responsible == 'N':
    print("Popracuj nad odpowiedzialnością")
elif responsible == 'T':
    print("Jesteś dorosłym, odpowiedzialnym człowiekiem")
else:
    print("chyba cię powaliło, error bla bla bla")
