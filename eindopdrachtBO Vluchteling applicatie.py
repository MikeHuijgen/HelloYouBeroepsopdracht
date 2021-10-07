def vraag6():
    print("Hoe wil je vluchten")
    print("a = boot")
    print("b = vliegtuig")
    print("c = lopen")
    
    antwoord6 = input()
    if antwoord6.lower() == "a":
        print("je kan een normalen boot nemen maar dat duurt een uur en je kan ook een klein boot nemen?")
        print(vraag())
    elif antwoord6.lower() == "b":
        print("Je bent op het vliegveld en ziet dat er veel soldaten staan wat doe je?")
        print(vraag())
    elif antwoord6.lower() == "c":
        print("Je loopt voor 5 dagen en komt aan op een klein kampje")
        print(vraag())
    else:
        print("Kies a,b of c")
        print(vraag6())
    
def vraag5():
    print("Je blijft maar ga je onderduiken of vechten")
    print("a = onderduiken")
    print("b = vechten")  
    
    antwoord5 = input()
    if antwoord5.lower() == "a":
        print("Je word ondekt en gevangen genomen")
        print("Je bent gevangen genomen begin opnieuw")
        print(vraag1())
    elif antwoord5.lower() == "b":
        print("Je vecht voor weken")
        print("Je loopt voor 5 dagen en komt aan op een klein kampje")
        print(Vraag9())
    else:
        print("Kies a of b")
        print(vraag5())

def vraag4():
    print("Je moeder wilt niet weg. Ga jij weg of blijf je")
    print("a = Blijven")
    print("b = weggaan")
    
    antwoord4 = input()
    if antwoord4.lower() == "a":
        print("Okay het is omdat je moeder niet wil")
        print(vraag5())
    elif antwoord4.lower() == "b":
        print("Je zegt je moeder gedag en vertrekt")
        print(Vraag6())
    else:
        print("Kies a of b")
        print(vraag4())

def vraag3():
    print("Wie neem je mee")
    print("a = zus")
    print("b = moeder")
    print("c = kat")
    
    antwoord3 = input()
    if antwoord3.lower() == "a":
        print("Je zus zal dankbaar zijn")
        print(vraag6())
    elif antwoord3.lower() == "b":
        print("Je moeder is altijd belangrijk")
        print(vraag4())
    elif antwoord3.lower() == "c":
        print("Je huisdier is je beste maat")
        print(vraag6())
    else:
        print("Kies a,b of c")
        print(vraag3())
        
def vraag2():
    
    print("Wat neem je mee ?\n")
    print("a = Mes")
    print("b = AHBO kit")
    print("c = niks")
    
    antwoord2 = input()
    if antwoord2.lower() == "a":
        print("Dat kan nog van pas komen")
        print(vraag3())
    elif antwoord2.lower() == "b":
        print("Slim voor als je gewond raakt")
        print(Vraag3())
    elif antwoord2.lower() == "c":
        print("Hopelijk heb je niks nodig")
        print(vraag3())
    else:
        print("Kies a,b of c")
        print(vraag2())

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
        print("Je bent dood begin opnieuw")
        print("Slechste einde")
        print(vraag1())
    elif antwoord1.lower() == "c":
        print("Je moet")
        print(vraag2())
    else:
        print("Kies a,b of c")
        print(vraag1())
        
print(vraag1())
    
