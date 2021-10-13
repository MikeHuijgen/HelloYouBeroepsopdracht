def vraag10():
    print("Je stopt bij Griekenland. Ga je weer mee met de boot of blijf je hier")
    print("a = Je gaat met de boot mee")
    print("b = Je blijft in Griekenland")
    
    antwoord10 = input()
    if antwoord10.lower() == "a":
        print("Je hoort dat de boot naar Nederland gaat. Misschien kan je daar een nieuw leven opbouwen")
        print(vraag15())
    elif antwoord10.lower() == "b":
        print("Je nieuwe leven in Griekenland begint nu")
        print(vraag16())
    else:
        print("Kies a of b")
        print(vraag10())

def vraag9():
    print("Je kom na een paar dagen lopen in een klein vluchtelingen kampje. Blijf je daar of ga je verder lopen")
    print("a = Je blijft")
    print("b = Je loopt verder")
    
    antwoord9 = input()
    if antwoord9.lower() == "a":
        print("Je kom binnen in het kamp en je word verwelkomd door lachende kinderen")
        print(vraag13())
    elif antwoord9.lower() == "b":
        print("Ik hoop dat we niet lang meer hoeven te lopen")
        print(vraag14())
    else:
        print("Kies a of b")
        print(vraag9())

def vraag8():
    print("Je komt aan op een klein vliegveld. Je ziet een paar soldaten staan ga je op de soldaten af of probeer je naar een vliegtuig te gaan")
    print("a = Naar de soldaten")
    print("b = Een vliegtuig zoeken")
    
    antwoord8 = input()
    if antwoord8.lower() == "a":
        print("De soldaten zien er vriendelijk uit. Je gaat met hun praten")
        print(vraag12())
    elif antwoord8.lower() == "b":
        print("Je ziet nog een klein vliegtuigje staan je loopt daar heen")
        print(vraag13())
    else:
        print("Kies a of b")
        print(vraag8())

def vraag7():
    print("Je komt aan bij het meer. Je ziet dat je 2 boten kan pakken ga je met de kleine boot of met de groote boot?")
    print("a = Groote boot")
    print("b = Kleine boot")
    
    antwoord7 = input()
    if antwoord7.lower() == "a":
        print("Het duurt misschien wat langer maar het is een stuk minder krap")
        print(vraag10())
    elif antwoord7.lower() == "b":
        print("Ik hoop dat het kleine bootje het houd")
        print(vraag11())
    else:
        print("Kies a of b")
        print(vraag7())

def vraag6():
    print("Hoe wil je vluchten")
    print("a = boot")
    print("b = vliegtuig")
    print("c = lopen")
    
    antwoord6 = input()
    if antwoord6.lower() == "a":
        print("Dat is een slimme manier")
        print(vraag7())
    elif antwoord6.lower() == "b":
        print("Zo kom je wel heel snel weg")
        print(vraag8())
    elif antwoord6.lower() == "c":
        print("kijk wel uit je weet nooit wat je tegenkomt")
        print(vraag9())
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
        print("Neem je iets mee?")
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
    
