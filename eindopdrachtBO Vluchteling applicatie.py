def vraag2():
    
    print("Hoe wil je vluchten ?\n")
    print("a = Boot")
    print("b = Vliegtuig")
    print("c = lopen")
    
    antwoord2 = input()
    if antwoord2.lower() == "a":
        print()
        print(vraag3())
    elif antwoord2.lower() == "b":
        print()
        print(Vraag4())
    elif antwoord2.lower() == "c":
        print()
        print(vraag5())
    else:
        print("Kies a,b of c")

def vraag1():
    
    print("Wil je vluchten ?\n")
    print("a = ja ")
    print("b = nee ")
    print("c = ik weet niet hoe ?")
    
    antwoord1 = input()
    if antwoord1.lower() == "a": 
        print("Nu moet je nog een manier vinden om te vluchten")
        print(vraag2())
    elif antwoord1.lower() == "b":
        print("Je word opgeblazen")
        print(vraag1())
    elif antwoord1.lower() == "c":
        print("Je moet")
        print(vraag2())
    else:
        print("Kies a,b of c")
        
print(vraag1())
    
