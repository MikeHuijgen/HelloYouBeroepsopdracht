def vraag26():
    print("Als je hier 5 weken slaap krijg je een verblijfsvergunning. Wat doe je?\n")
    print("a = Ik blijf")
    print("b = Ik ga weg")
    
    antwoord26 = input()
    if antwoord26.lower() == "a":
        print("Na 5 lange weken is het eindelijk zover je hebt een verblijfsvergunning.\n")
        print(vraag33())
    elif antwoord26.lower() == "b":
        print("Nu je weg gaat kan je niet meer in Nederland blijven\n")
        print(vraag34())
    else:
        print("Kies a of b.\n")
        print(vraag26())

def vraag25():
    print("Je word nu vast gehouden op het politie bureau. Ze vragen wat je komt doen in Nederland.\n")
    print("a = Vertel dat je gevlucht bent")
    print("b = Zeg niks")
    
    antwoord25 = input()
    if antwoord25.lower() == "a":
        print("Ze geloven je niet dus ze zetten je uit het land.\n")
        print(vraag31())
    elif antwoord25.lower() == "b":
        print("Ze denken dat je een spion bent dus ze hebben je veroordeeld tot 5 jaar cel.\n")
        print(vraag32())
    else:
        print("Kies a of b.\n")
        print(vraag25())

def vraag24():
    print("Ze willen je helpen maar je moet eerst jezelf bewijzen met werken. Wat voor werk wil je doen?\n")
    print("a = Techniek")
    print("b = Software developer")
    print("c = Albert Heijn")
    
    antwoord24 = input()
    if antwoord24.lower() == "a":
        print("Dat is wel een zware klus maar het moet goed komen.\n")
        print(vraag28())
    elif antwoord24.lower() == "b":
        print("Er is veel te leren.\n")
        print(vraag29())
    elif antwoord24.lower() == "c":
        print("Het verdient niet veel maar het is genoeg.\n")
        print(vraag30())
    else:
        print("Kies a, b of c.\n")
        print(vraag24())

def vraag23():
    print("JA je krijg net te horen dat je mag blijven en een verblijfsvergunning krijg.\n")
    print("a = Je gaat op zoek naar werk")
    print("b = Je gaat genieten van het land en reizen")
    
    antwoord23 = input()
    if antwoord23.lower() == "a":
        print("Je werkt elke dag voor de komende 5 jaar. Je bent nu rijk heb een mooi huis en een goed leven toch denk je soms nog wel terug aan de slechte tijd.\n")
        print(vraag1())
    elif antwoord23.lower() == "b":
        print("Je reis heel Griekenland door. Je ziet allemaal mooie plekken en je hebt een fijn leven.\n")
        print(vraag1())
    else:
        print("Kies a of b.\n")
        print(vraag23())

def vraag22():
    print("De geemnste geeft je nog 1 kans.\n")
    print("a = Je blijft liegen")
    print("b = Je verteld de waarheid")
    
    antwoord22 = input()
    if antwoord22.lower() == "a":
        print("De politie word gebeld en je word opgepakt voor fraude.\n")
        print(vraag1())
    elif antwoord22.lower() == "b":
        print("Ze vinden het niet leuk maar ze kijken watze kunnen doen.\n")
        print(vraag23())
    else:
        print("Kies a of b.\n")
        print(vraag22())

def vraag21():
    print("Je krijg te horen dat je een verblijfsvergunning nodig hebt. Hoe ga je die proberen te krijgen?\n")
    print("a = Naar de gemeente")
    print("b = Kopen")
    
    antwoord21 = input()
    if antwoord21.lower() == "a":
        print("Hopelijk kunnen zij je helpen.\n")
        print(vraag19())
    elif antwoord21.lower() == "b":
        print("Is dat wel slim??? Wat maakt jou het uit je verdient het.\n")
        print(vraag27())
    else:
        print("Kies a of b.\n")
        print(vraag21())

def vraag20():
    print("Je kan in een asielzoekerscentrum terecht wil je dat?\n")
    print("a = Ja")
    print("b = Nee")
    
    antwoord20 = input()
    if antwoord20.lower() == "a":
        print("Je word hartelijk verwelkomd en ze proberen ook je te helpen om in nederland te kunnen blijven.\n")
        print(vraag26())
    elif antwoord20.lower() == "b":
        print("Je gaat dan toch maar kijken of je bij de gemeente iets voor elkaar kan krijgen.\n")
        print(vraag19())
    else:
        print("Kies a of b.\n")
        print(vraag20())

def vraag19():
    print("Je komt aan bij de gemeente. Ze vragen wat je in Nederland komt doen en wat je wilt.\n")
    print("a = Vertel de waarheid en vraag of je een verblijfsvergunning mag en dat je ook er voor wilt werken")
    print("b = Je liegt waarom je in Nederland bent")
    
    antwoord19 = input()
    if antwoord19.lower() == "a":
        print("Ze kijken wat ze voor je kunnen doen.\n")
        print(vraag24())
    elif antwoord19.lower() == "b":
        print("Ze denken dat je liegt dus je word meegenomen door de politie en verhoord.\n")
        print(vraag25())
    else:
        print("Kies a of b.\n")
        print(vraag19())

def vraag18():
    print("Je komt aan bij de gemeente. Ze vragen wat je komt doen en wat je wilt.\n")
    print("a = Lieg en zeg dat je hier ben komen wonen maar je verblijfsvergunning gestolen")
    print("b = Vertel de waarheid en vraag of je een verblijfsvergunning mag en dat je ook er voor wilt werken")
    
    antwoord18 = input()
    if antwoord18.lower() == "a":
        print("De gemeente probeerd je naam op te zoeken maar je staat niet in het systeem.\n")
        print(vraag22())
    elif antwoord18.lower() == "b":
        print("Ze weten niet zeker of het lukt maar ze zullen kijken wat ze kunnen doen.\n")
        print(vraag23())
    else:
        print("Kies a of b.\n")
        print(vraag18())

def vraag17():
    print("Er zit vergif in het eten je zit namelijk in een enemy kamp je kan 2 dingen doen.\n")
    print("a = Niks doen je geeft op")
    print("b = Uit het kamp rennen")
    
    antwoord17 = input()
    if antwoord17.lower() == "a":
        print("Je sterft in het kamp.\n")
        print(vraag1())
    elif antwoord17.lower() == "b":
        print("Je rent het dorp uit en rent tegen een soldaat die toevallig een anti-gif heeft. Hij vraagt je met hem mee wilt gaan lopen en dat doe je.\n")
        print(vraag9())
    else:
        print("Kies a of b.\n")
        print(vraag17())

def vraag16():
    print("Je komt eindelijk aan in Nederland maar waar ga je starten?\n")
    print("a = Je vraagt aan de gemeente of je mag blijven en dat je een verblijfsvergunning mag hebben")
    print("b = Je gaat proberen zo snel als je kan onderdak te regelen")
    print("c = Je gaat werk zoeken")
    
    antwoord16 = input()
    if antwoord16.lower() == "a":
        print("Je hoopt dat je mag blijven zo niet wat moet je dan doen.\n")
        print(vraag19())
    elif antwoord16.lower() == "b":
        print("Er is vast wel een plek waar je heen kan.\n")
        print(vraag20())
    elif antwoord16.lower() == "b":
        print("Je kan het altijd proberen.\n")
        print(vraag21())
    else:
        print("Kies a, b of c.\n")
        print(vraag16())

def vraag15():
    print("Je gaat nu leven in Griekenland. Wat gaat je als eerst doen?\n")
    print("a = Naar de gemeente")
    print("b = Proberen om onderdak te krijgen")
    
    antwoord15 = input()
    if antwoord15.lower() == "a":
        print("Dat is mischien wel slim zij kunnen je vast helpen.\n")
        print(vraag18())
    elif antwoord15.lower() == "b":
        print("Dit is belangrijk maar ik denk toch dat je naar de gemeente moet.\n")
        print(vraag15())
    else:
        print("Kies a of b.\n")
        print(vraag15())

def vraag14():
    print("Je ziet een splitsing. 1 weg naar een vliegveld en de 2de weg naar een meertje?\n")
    print("a = weg 1")
    print("b = weg 2")
    
    antwoord14 = input()
    if antwoord14.lower() == "a":
        print("Hopelijk kan je daar verder vluchten.\n")
        print(vraag8())
    elif antwoord14.lower() == "b":
        print("Hopelijk kan je daar verder vluchten.\n")
        print(vraag7())
    else:
        print("Kies a of b.\n")
        print(vraag14())

def vraag13():
    print("Ze willen je eten geven wat neem je?\n")
    print("a = Brood")
    print("b = Vlees")
    print("c = Groente")
    
    antwoord13 = input()
    if antwoord13.lower() == "a":
        print("Je hebt al dagen niet gegeten dit zal je goed doen.\n")
        print(vraag17())
    elif antwoord13.lower() == "b":
        print("Een stukje vlees dat is altijd goed voor je.\n")
        print(vraag17())
    elif antwoord13.lower() == "c":
        print("Groente zijn goed voor je het brengt je ook weer op kracht.\n")
        print(vraag17())
    else:
        print("Kies a, b of c.\n")
        print(vraag13())

def vraag12():
    print("Je komt er achter dat de soldaten je naar Nederland kunnen brengen. Ga je voor de kans of niet?\n")
    print("a = Nederland here i come")
    print("b = Nee ik zoek iets anders")
    
    antwoord12 = input()
    if antwoord12.lower() == "a":
        print("Je vertrekt met het vliegtuig en je kan eindelijk bijkomen van de lange reis.\n")
        print(vraag16())
    elif antwoord12.lower() == "b":
        print("Okay er is jammer genoeg geen ander vliegtuig dus je gaat maar verder lopen.\n")
        print(vraag9())
    else:
        print("Kies a of b.\n")
        print(vraag12())

def vraag11():
    print("Je zit op zee en het stormt heel erg. De kleine boot valt om door een groote golf. Probeer je weer op de boot te komen of laat je je mee slepen door de golven?\n")
    print("a = Je klimt op de boot")
    print("b = Je laat je meeslepen")
    
    antwoord11 = input()
    if antwoord11.lower() == "a":
        print("Je probeerd de boot weer recht op te krijgen maar er komt nog een groote golf op je af. Je word mee gesleurd door de golven en verdrinkt.\n")
        print(vraag1())
    elif antwoord11.lower() == "b":
        print("Je word mee gesleurd door de golven en verdrinkt.\n")
        print(vraag1())
    else:
        print("Kies a of b.\n")
        print(vraag11())

def vraag10():
    print("Je stopt bij Griekenland. Ga je weer mee met de boot of blijf je hier?\n")
    print("a = Je gaat met de boot mee")
    print("b = Je blijft in Griekenland")
    
    antwoord10 = input()
    if antwoord10.lower() == "a":
        print("Je hoort dat de boot naar Nederland gaat. Misschien kan je daar een nieuw leven opbouwen.\n")
        print(vraag16())
    elif antwoord10.lower() == "b":
        print("Je nieuwe leven in Griekenland begint nu.\n")
        print(vraag15())
    else:
        print("Kies a of b.\n")
        print(vraag10())

def vraag9():
    print("Je kom na een paar dagen lopen in een klein vluchtelingen kampje. Blijf je daar of ga je verder lopen?\n")
    print("a = Je blijft")
    print("b = Je loopt verder")
    
    antwoord9 = input()
    if antwoord9.lower() == "a":
        print("Je kom binnen in het kamp en je word verwelkomd door lachende kinderen.\n")
        print(vraag13())
    elif antwoord9.lower() == "b":
        print("Ik hoop dat we niet lang meer hoeven te lopen.\n")
        print(vraag14())
    else:
        print("Kies a of b.\n")
        print(vraag9())

def vraag8():
    print("Je komt aan op een klein vliegveld. Je ziet een paar soldaten staan ga je op de soldaten af of probeer je naar een vliegtuig te gaan?\n")
    print("a = Naar de soldaten")
    print("b = Een vliegtuig zoeken")
    
    antwoord8 = input()
    if antwoord8.lower() == "a":
        print("De soldaten zien er vriendelijk uit. Je gaat met hun praten.\n")
        print(vraag12())
    elif antwoord8.lower() == "b":
        print("Okay er is jammer genoeg geen ander vliegtuig dus je gaat maar verder lopen.\n")
        print(vraag9())
    else:
        print("Kies a of b.\n")
        print(vraag8())

def vraag7():
    print("Je komt aan bij het meer. Je ziet dat je 2 boten kan pakken ga je met de kleine boot of met de groote boot?\n")
    print("a = Groote boot")
    print("b = Kleine boot")
    
    antwoord7 = input()
    if antwoord7.lower() == "a":
        print("Het duurt misschien wat langer maar het is een stuk minder krap.\n")
        print(vraag10())
    elif antwoord7.lower() == "b":
        print("Ik hoop dat het kleine bootje het houd.\n")
        print(vraag11())
    else:
        print("Kies a of b.\n")
        print(vraag7())

def vraag6():
    print("Hoe wil je vluchten?\n")
    print("a = boot")
    print("b = vliegtuig")
    print("c = lopen")
    
    antwoord6 = input()
    if antwoord6.lower() == "a":
        print("Dat is een slimme manier.\n")
        print(vraag7())
    elif antwoord6.lower() == "b":
        print("Zo kom je wel heel snel weg.\n")
        print(vraag8())
    elif antwoord6.lower() == "c":
        print("kijk wel uit je weet nooit wat je tegenkomt.\n")
        print(vraag9())
    else:
        print("Kies a,b of c.\n")
        print(vraag6())
    
def vraag5():
    print("Je blijft maar ga je onderduiken of vechten?\n")
    print("a = onderduiken")
    print("b = vechten")  
    
    antwoord5 = input()
    if antwoord5.lower() == "a":
        print("Je word ondekt en gevangen genomen.\n")
        print("Je bent gevangen genomen begin opnieuw.\n")
        print(vraag1())
    elif antwoord5.lower() == "b":
        print("Je vecht voor weken.\n")
        print(vraag9())
    else:
        print("Kies a of b.\n")
        print(vraag5())

def vraag4():
    print("Je moeder wilt niet weg. Ga jij weg of blijf je?\n")
    print("a = Blijven")
    print("b = weggaan")
    
    antwoord4 = input()
    if antwoord4.lower() == "a":
        print("Okay het is omdat je moeder niet wil.\n")
        print(vraag5())
    elif antwoord4.lower() == "b":
        print("Je zegt je moeder gedag en vertrekt.\n")
        print(vraag6())
    else:
        print("Kies a of b.\n")
        print(vraag4())

def vraag3():
    print("Wie neem je mee?\n")
    print("a = zus")
    print("b = moeder")
    print("c = kat")
    
    antwoord3 = input()
    if antwoord3.lower() == "a":
        print("Je zus zal dankbaar zijn.\n")
        print(vraag6())
    elif antwoord3.lower() == "b":
        print("Je moeder is altijd belangrijk.\n")
        print(vraag4())
    elif antwoord3.lower() == "c":
        print("Je huisdier is je beste maat.\n")
        print(vraag6())
    else:
        print("Kies a,b of c.\n")
        print(vraag3())
        
def vraag2():
    
    print("Wat neem je mee ?\n")
    print("a = Mes")
    print("b = AHBO kit")
    print("c = niks")
    
    antwoord2 = input()
    if antwoord2.lower() == "a":
        print("Dat kan nog van pas komen.\n")
        print(vraag3())
    elif antwoord2.lower() == "b":
        print("Slim voor als je gewond raakt.\n")
        print(vraag3())
    elif antwoord2.lower() == "c":
        print("Hopelijk heb je niks nodig.\n")
        print(vraag3())
    else:
        print("Kies a,b of c.\n")
        print(vraag2())

def vraag1():
    
    print("Wil je vluchten ?\n")
    print("a = ja ")
    print("b = nee ")
    print("c = ik weet niet hoe ?")
    
    antwoord1 = input()
    if antwoord1.lower() == "a": 
        print("Okay hier gaan we\n")
        print(vraag2())
    elif antwoord1.lower() == "b":
        print("Je word opgeblazen.\n")
        print("Je bent dood begin opnieuw.\n")
        print(vraag1())
    elif antwoord1.lower() == "c":
        print("Je moet.\n")
        print(vraag2())
    else:
        print("Kies a,b of c.\n")
        print(vraag1())
        
print(vraag1())
    
