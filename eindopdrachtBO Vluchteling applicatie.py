import time

def vraag40():
    print("Je doet het groote project maar het gaat niet zo goed. Je kan proberen je bedrijf te redden door games te maken of je gaat failliet.\n")
    print("a = Game maken")
    print("b = Failliet")
    
    antwoord40 = input()
    if antwoord40.lower() == "a":
        print("-------------------------------------------------------------------")
        print("Je heb besloten om games te maken met je team.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag39())
    elif antwoord40.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Je heb het teminste geprobeerd. Je geniet nog van je laatste dagen.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag1())
    else:
        print("Kies a of b.\n")
        print(vraag40())

def vraag39():
    print("Je brengt met je team een game uit en het word een hit. Ga je een deel 2 maken?\n")
    print("a = Nee")
    print("b = Ja")
    
    antwoord39 = input()
    if antwoord39.lower() == "a":
        print("-------------------------------------------------------------------")
        print("Je word super bekend en je heb veel geld. Je laat je bedrijf overnemen en je geniet nog van je laatste dagen.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag1())
    elif antwoord39.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Je brengt deel 2 uit en je gaat nog meer games maken. Je word een succesvolle")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag1())
    else:
        print("Kies a of b.\n")
        print(vraag39())

def vraag38():
    print("Je bedrijf loopt niet goed je moet uitbreiden of je gaat failliet\n")
    print("a = Uitbreiden")
    print("b = Failliet")
    
    antwoord38 = input()
    if antwoord38.lower() == "a":
        print("-------------------------------------------------------------------")
        print("Slim nu kan je bedrijf nog goed groeien")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag37())
    elif antwoord38.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Het is jammer maar je hebt het wel geprobeerd. Je geniet nog van het leven en na 20 jaar sterf je in je slaap.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag1())
    else:
        print("Kies a of b.\n")
        print(vraag38())

def vraag37():
    print("Waar in wil je uitbreiden?\n")
    print("a = Game development")
    print("b = Grote sofware projecten")
    
    antwoord37 = input()
    if antwoord37.lower() == "a":
        print("-------------------------------------------------------------------")
        print("Dat is een hele slimmen zet want de markt is heel groot.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag39())
    elif antwoord37.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Je kijkt of je groote projecten kan krijgen. Na een tijd zoeken heb je wat gevonden.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag40())
    else:
        print("Kies a of b.\n")
        print(vraag37())

def vraag36():
    print("Je bent nu de eigenaar van het bedrijf. Je bedrijf maakt apps voor de telefoon wil je het bedrijf uitbreiden?\n")
    print("a = Ja laten we het uitbreiden")
    print("b = Nee ik laat het nog zo")
    
    antwoord36 = input()
    if antwoord36.lower() == "a":
        print("-------------------------------------------------------------------")
        print("Je maakt het bedrijf veel groter voor je werknemers koop je betere spullen.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag37())
    elif antwoord36.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Je blijft nog simpel werken dat hoeft niet slecht te zijn.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag38())
    else:
        print("Kies a of b.\n")
        print(vraag36())

def vraag35():
    print("Je kan nu met zekerheid zeggen dat je een fijn leven hebt gehad. Je geniet van je vrije tijd. Je krijgt een nieuwe baan aangeboden om een bedrijf over te nemen in de software development doe je dat?\n")
    print("a = Ja ik ga het bedrijf overnemen")
    print("b = Ik vind het goed zo")
    
    antwoord35 = input()
    if antwoord35.lower() == "a":
        print("-------------------------------------------------------------------")
        print("Je bent benieuwd waar dit naar toe gaat en je hebt er veel zin in.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag36())
    elif antwoord35.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Je heb je beste tijd gehad. Na nog 20 jaar stopt je hart in je slaap.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag1())
    else:
        print("Kies a of b.\n")
        print(vraag35())

def vraag34():
    print("Je vind iemand op de zwarte markt die je kan helpen. Hij vraagt 2.000 euro voor de vergunning. Je hebt zelf geen geld. Ga je geld stelen of ga je naar toch naar de gemeente?\n")
    print("a = Stelen")
    print("b = Gemeente")
    
    antwoord34 = input()
    if antwoord34.lower() == "a":
        print("-------------------------------------------------------------------")
        print("Je steelt veel geld van verschillende mensen. Alleen de politie heeft je door en je word opgepakt en veroordeeld tot cel straf.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag32())
    elif antwoord34.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Ik hoop dat het niet te laat is.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag19())
    else:
        print("Kies a of b.\n")
        print(vraag34())

def vraag33():
    print("Na de 5 weken kan je indelijk gaan werken waar wil je werken?\n")
    print("a = Techniek")
    print("b = Albert Heijn")
    
    antwoord33 = input()
    if antwoord33.lower() == "a":
        print("-------------------------------------------------------------------")
        print("Het kan een fijne baan zijn.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag28())
    elif antwoord33.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Het verdient niet veel maar je moet ergens beginnen.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag30())
    else:
        print("Kies a of b.\n")
        print(vraag33())

def vraag32():
    print("Je zit gevangen probeer je te ontsnappen of niet?\n")
    print("a = Ja")
    print("b = Nee")
    
    antwoord32 = input()
    if antwoord32.lower() == "a":
        print("-------------------------------------------------------------------") 
        print("Je word ontdekt en tijdens het vluchten schieten de bewakers je neer.")
        print("-------------------------------------------------------------------")
        time.sleep(1) 
        print(vraag1())
    elif antwoord32.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Je krijt ruzie met andere gevangenen. In de nacht komen de anderen naar je cel en schoppen en slaan je tot je sterft.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag1())
    else:
        print("Kies a of b.\n")
        print(vraag32())

def vraag31():
    print("Je denkt over wat je nu moet doen en je ziet twee mogelijkheden.\n")
    print("a = Naar Griekenland vluchten")
    print("b = Terug reizen naar huis")
    
    antwoord31 = input()
    if antwoord31.lower() == "a":
        print("-------------------------------------------------------------------") 
        print("Ik hoop dat je kansen beter zijn daar")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag15())
    elif antwoord31.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je gaat terug. Na een lange reis zie je dat er nog steeds oorlog is en je besluit om weer te vluchten.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag2())
    else:
        print("Kies a of b.\n")
        print(vraag31())

def vraag30():
    print("Je werkt je kapot voor het minimalen. Je gaat een nieuwe baan zoeken. Wat voor baan wil je?\n")
    print("a = Techniek")
    print("b = Software developer")
    
    antwoord30 = input()
    if antwoord30.lower() == "a":
        print("-------------------------------------------------------------------") 
        print("Dit is denk een goede keus.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag28())
    elif antwoord30.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Het verdient goed en is nog interessant ook.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag29())
    else:
        print("Kies a of b.\n")
        print(vraag30())

def vraag29():
    print("Je komt te werken bij een super leuk bedrijf en na zo veel jaar werken krijg je eindelijk je verblijfsvergunning. Ga je stoppen met werken of ga je door?\n")
    print("a = stoppen")
    print("b = doorgaan")
    
    antwoord29 = input()
    if antwoord29.lower() == "a":
        print("-------------------------------------------------------------------") 
        print("Na zo veel jaar werken kan je beter genieten.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag35())
    elif antwoord29.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je werkt nog 10 jaar door. Je baas verteld dat hij gaat stoppen en wilt dat jij het bedrijf gaat runnen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag36())
    else:
        print("Kies a of b.\n")
        print(vraag29())

def vraag28():
    print("Na 10 jaar werken heb je een leuke toekomst opgebouwd. Je stopt met werken en gaat lekker relaxen van het geld dat je hebt gemaakt. Je vraagt je af zou ik terug gaan naar mijn moederland? \n")
    print("a = Ja ik wil terug")
    print("b = Nee ik blijf in Nederland")
    
    antwoord28 = input()
    if antwoord28.lower() == "a":
        print("-------------------------------------------------------------------") 
        print("Je gaat terug. Na een lange reis zie je dat er nog steeds oorlog is en je besluit om weer te vluchten.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag2())
    elif antwoord28.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je bent hier gekomen en blijft hier.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag35())
    else:
        print("Kies a of b.\n")
        print(vraag28())

def vraag27():
    print("Je kan het op de zwarte markt kopen alleen het is wel illigaal wil je het echt?\n")
    print("a = Ga naar de zwarte markt")
    print("b = Ga toch naar de gemeente")
    
    antwoord27 = input()
    if antwoord27.lower() == "a":
        print("-------------------------------------------------------------------") 
        print("Ik hoop dat het allemaal goed gaat.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag34())
    elif antwoord27.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Dat is wel stuk veiliger.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag19())
    else:
        print("Kies a of b.\n")
        print(vraag27())

def vraag26():
    print("Als je hier 5 weken slaap krijg je een verblijfsvergunning. Wat doe je?\n")
    print("a = Ik blijf")
    print("b = Ik ga weg")
    
    antwoord26 = input()
    if antwoord26.lower() == "a":
        print("-------------------------------------------------------------------") 
        print("Na 5 lange weken is het eindelijk zover je hebt een verblijfsvergunning.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag33())
    elif antwoord26.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Nu je weg gaat kan je niet meer in Nederland blijven")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag31())
    else:
        print("Kies a of b.\n")
        print(vraag26())

def vraag25():
    print("Je word nu vast gehouden op het politie bureau. Ze vragen wat je komt doen in Nederland.\n")
    print("a = Vertel dat je gevlucht bent")
    print("b = Zeg niks")
    
    antwoord25 = input()
    if antwoord25.lower() == "a":
        print("-------------------------------------------------------------------") 
        print("Ze geloven je niet dus ze zetten je uit het land.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag31())
    elif antwoord25.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Ze denken dat je een spion bent dus ze hebben je veroordeeld tot 5 jaar cel.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Dat is wel een zware klus maar het moet goed komen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag28())
    elif antwoord24.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Er is veel te leren.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag29())
    elif antwoord24.lower() == "c":
        print("-------------------------------------------------------------------") 
        print("Het verdient niet veel maar het is genoeg.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je werkt elke dag voor de komende 5 jaar. Je bent nu rijk heb een mooi huis en een goed leven toch denk je soms nog wel terug aan de slechte tijd.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag1())
    elif antwoord23.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je reis heel Griekenland door. Je ziet allemaal mooie plekken en je hebt een fijn leven.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("De politie word gebeld en je word opgepakt voor fraude.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag1())
    elif antwoord22.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Ze vinden het niet leuk maar ze kijken watze kunnen doen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Hopelijk kunnen zij je helpen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag19())
    elif antwoord21.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Is dat wel slim??? Wat maakt jou het uit je verdient het.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je word hartelijk verwelkomd en ze proberen ook je te helpen om in nederland te kunnen blijven.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag26())
    elif antwoord20.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je gaat dan toch maar kijken of je bij de gemeente iets voor elkaar kan krijgen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Ze kijken wat ze voor je kunnen doen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag24())
    elif antwoord19.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Ze denken dat je liegt dus je word meegenomen door de politie en verhoord.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("De gemeente probeerd je naam op te zoeken maar je staat niet in het systeem.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag22())
    elif antwoord18.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Ze weten niet zeker of het lukt maar ze zullen kijken wat ze kunnen doen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je sterft in het kamp.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag1())
    elif antwoord17.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je rent het dorp uit en rent tegen een soldaat die toevallig een anti-gif heeft. Hij vraagt je met hem mee wilt gaan lopen en dat doe je.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je hoopt dat je mag blijven zo niet wat moet je dan doen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag19())
    elif antwoord16.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Er is vast wel een plek waar je heen kan.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag20())
    elif antwoord16.lower() == "c":
        print("-------------------------------------------------------------------") 
        print("Je kan het altijd proberen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Dat is mischien wel slim zij kunnen je vast helpen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag18())
    elif antwoord15.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Dit is belangrijk maar ik denk toch dat je naar de gemeente moet.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Hopelijk kan je daar verder vluchten.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag8())
    elif antwoord14.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Hopelijk kan je daar verder vluchten.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je hebt al dagen niet gegeten dit zal je goed doen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag17())
    elif antwoord13.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Een stukje vlees dat is altijd goed voor je.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag17())
    elif antwoord13.lower() == "c":
        print("-------------------------------------------------------------------") 
        print("Groente zijn goed voor je het brengt je ook weer op kracht.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je vertrekt met het vliegtuig en je kan eindelijk bijkomen van de lange reis.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag16())
    elif antwoord12.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Okay er is jammer genoeg geen ander vliegtuig dus je gaat maar verder lopen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je probeerd de boot weer recht op te krijgen maar er komt nog een groote golf op je af. Je word mee gesleurd door de golven en verdrinkt.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag1())
    elif antwoord11.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je word mee gesleurd door de golven en verdrinkt.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je hoort dat de boot naar Nederland gaat. Misschien kan je daar een nieuw leven opbouwen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag16())
    elif antwoord10.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je nieuwe leven in Griekenland begint nu.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je kom binnen in het kamp en je word verwelkomd door lachende kinderen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag13())
    elif antwoord9.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Ik hoop dat we niet lang meer hoeven te lopen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("De soldaten zien er vriendelijk uit. Je gaat met hun praten.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag12())
    elif antwoord8.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Okay er is jammer genoeg geen ander vliegtuig dus je gaat maar verder lopen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Het duurt misschien wat langer maar het is een stuk minder krap.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag10())
    elif antwoord7.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Ik hoop dat het kleine bootje het houd.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Dat is een slimme manier.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag7())
    elif antwoord6.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Zo kom je wel heel snel weg.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag8())
    elif antwoord6.lower() == "c":
        print("-------------------------------------------------------------------") 
        print("kijk wel uit je weet nooit wat je tegenkomt.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je word ondekt en gevangen genomen.")
        print("Je bent gevangen genomen begin opnieuw.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag1())
    elif antwoord5.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je vecht voor weken.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Okay het is omdat je moeder niet wil.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag5())
    elif antwoord4.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je zegt je moeder gedag en vertrekt.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Je zus zal dankbaar zijn.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag6())
    elif antwoord3.lower() == "b":
        print("-------------------------------------------------------------------") 
        print("Je moeder is altijd belangrijk.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag4())
    elif antwoord3.lower() == "c":
        print("-------------------------------------------------------------------") 
        print("Je huisdier is je beste maat.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag6())
    else:
        print("Kies a,b of c.\n")
        print(vraag3())
        
def vraag2():
    
    print("Wat neem je mee ?\n")
    print("a = Mes")
    print("b = EHBO kit")
    print("c = niks")
    
    antwoord2 = input()
    if antwoord2.lower() == "a":
        print("-------------------------------------------------------------------") 
        print("Dat kan nog van pas komen.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag3())
    elif antwoord2.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Slim voor als je gewond raakt.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
        print(vraag3())
    elif antwoord2.lower() == "c":
        print("-------------------------------------------------------------------") 
        print("Hopelijk heb je niks nodig.")
        print("-------------------------------------------------------------------") 
        time.sleep(1)
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
        print("-------------------------------------------------------------------") 
        print("Okay hier gaan we")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag2())
    elif antwoord1.lower() == "b":
        print("-------------------------------------------------------------------")
        print("Je word opgeblazen.")
        print("Je bent dood begin opnieuw.")
        print("-------------------------------------------------------------------")
        time.sleep(1)
        print(vraag1())
    elif antwoord1.lower() == "c":
        print("-------------------------------------------------------------------")
        print("Je moet.")
        print("-------------------------------------------------------------------")
        time.sleep(1) 
        print(vraag2())
    else:
        print("Kies a,b of c.\n")
        print(vraag1())

print("Je bent een man uit Syrië die er achter komt dat er oorlog is in zijn land. Op een dag sta je op met het idee om te gaan vluchten.")
time.sleep(2)
print("Nu is het aan jou om de goede keuzens te maken en de man te helpen om te vluchten.")
time.sleep(2)
print("Kies a, b of c om verder te komen in het verhaal MAAR let op elke keuzen heeft gevolgen kies verstandig.")        
time.sleep(1)
print("Begin\n")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1\n")
time.sleep(1)

vraag1()
    
