print("Ile masz lat?")
age = int(input())
print("Czy jesteś odpowiedzialny? T/N")
responsible = input()

if age < 18:
    print("Do pełnoletności brakuje Ci:", 18 - age, "lat")
elif age >= 100:
    print("Czy napewno masz tyle lat?")
elif responsible != 'T':
    print("Popracuj nad odpowiedzialnością")
else:
    print("Jesteś dorosłym, odpowiedzialnym człowiekiem")
