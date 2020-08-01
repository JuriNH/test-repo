print("Ile masz lat?")
age = int(input())
print("Czy jesteś odpowiedzialny? T/N")
responsible = input()

if age > 100:
    print("To naprawdę Twój wiek?")
elif age >= 18 and responsible == "T":
    print("Jesteś dorosłym człowiekiem")
elif responsible != 'T':
    print("Popracuj nad odpowiedzialnością")
else:
    print("Do pełnoletności brakuje Ci:", 18 - age, "lat")

## czemu nie działa? jesli dam 12 i N printuje "popracuj nad odpowiedzialnoscia",
# zamiast "do pelnoletnosci brakuje..."
