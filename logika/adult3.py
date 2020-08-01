print("Ile masz lat?")
age = int(input())
print("Czy jesteś dojrzały? T/N")
responsible = input()

if age >= 18:
    print("Bomba")
    if age > 100:
        print("Czy to naprawdę Twój wiek?")
    if responsible == 'T':
        print("Jesteś dorosły i dojrzały")
    elif responsible == 'N':
        print("dorośnij ziom")
    elif responsible not in ['T', 'N']:
        print("BABOL")
else:
    print("Spadaj na drzewo")
