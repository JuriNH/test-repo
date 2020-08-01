imie = input("Imię: ")
nazwisko = input("Nazwisko: ")
numer = input("numer telefonu: ")
print ("Czy imię składa się tylko z liter?", imie.isalpha())
print ("Czy nazwisko składa się tylko z liter?", nazwisko.isalpha())
print ("Czy numer składa się tylko z cyfr?", numer.isdigit())
print (imie, nazwisko)
imie = imie.capitalize()
nazwisko = nazwisko.capitalize()
print (imie, nazwisko)
print ("\n")
print (numer)
numer = numer.replace(" ", "").replace("-", "")
print (numer)
print("Czy użytkownik jest kobietą?:", imie.endswith("a"))
personal = imie, nazwisko, numer
personal_data = " ".join(personal)
print (personal_data)
print ("\n")
print (personal_data)
print (len(personal_data))
litery= len(personal) - personal.count(" ") - 9
print (litery)
print (len(imie + nazwisko))

#Czemu przy tym sposobie twierdzi, że len(persnal) = 3 ?? Przez to jak je połączyłem? Traktuje imie jako 1 naziwsko jako drgui a numer jako trzeci znak??
#Jak skonfigutować edytor żeby help pythona działał - podpowiadanie składni i dokumentacja
