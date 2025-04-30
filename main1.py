nabídka = ["Velikonoční beránek", "Vajíčka", "Pomlázka", "Čokoláda", "Kinder vajco"]
košík = []

print("Vítejte v aplikaci Koledník")

while True:
    print("-----------------------------------------")
    print("Ahoj koledníku, co bys rád do košíku?")
    print("-----------------------------------------")
    print("Zde máte na výběr")

    for i in range(len(nabídka)):
        print(f"    {i+1}. {nabídka[i]}")

    volba = input("Zadejte vaši volbu kolegi: ")

    volba_int = -1
    if volba.isdigit():
        volba_int = int(volba)

    for i in range(len(nabídka)):
        if volba == nabídka[i] or volba_int == 1:
            košík.append(nabídka[i])
            nabídka.pop(i)
            break
    else:
        print("tohle v košíku nemáme")
   
    print("-----------------------------------------")
    print("Obsah vašeho košíku")
    for i in range(len(košík)):
        print(f"    {i+1}. {košík[i]}")