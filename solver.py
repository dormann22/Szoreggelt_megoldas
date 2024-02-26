from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date

#a chromedriver elérési út megadása
service = Service("chromedriver/chromedriver.exe")

#így nem zárja be a megnyitott oldalt pár másodperc múlva
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#böngésző megadása
driver = webdriver.Chrome(service=service, options=options)


def openPage():
    #a megadott weboldal megnyitása
    driver.get("https://jealousmarkup.xyz/szofejto/")

    #Teljes képernyő
    driver.maximize_window()

    #Felugró ablak bezárása
    closeButton = driver.find_element(By.XPATH, '//*[@id="infoPopup"]/button')
    closeButton.click()


#eltávolítja azokat a szavakat, amiben a megfelelő helyen nem a megfelelő ismert zöld betűk vannak
def deleteWordsBasedOnHitLetters(words, hitLetter):
    for word in words.copy():
        for key in hitLetter:
            if(hitLetter[key] and word[key-1] != hitLetter[key]):
                words.remove(word)


#Eltávolítja azokat a szavakat, amikben nincsenek ismert piros betűk
def deleteWordsBasedOnNearLetters(words, letter, position):
    for word in words.copy():
        currentPosition = word[position-1]
        if(letter not in word or position-1 in nearLetter[currentPosition]):
            words.remove(word)


#Eltávolítja azokat a szavakat, amikben ismert szürke betűk vannak
def deleteWordsBasedOnMissedLetters(words, letter):
    for word in words.copy():
        if(letter in word and letter not in hitLetter.values() and not nearLetter[letter]):
            words.remove(word)

openPage()

# Szavak beolvasása a fájlból
words = []

with open("elfogadott-szavak.txt", encoding='utf-8') as file:
    for line in file:
        words.append(line.strip().lower())

# Real solution
#INIT
missedLetter = []
nearLetter = {
    'a': [],
    'á': [],
    'b': [],
    'c': [],
    'd': [],
    'e': [],
    'é': [],
    'f': [],
    'g': [],
    'h': [],
    'i': [],
    'í': [],
    'j': [],
    'k': [],
    'l': [],
    'm': [],
    'n': [],
    'o': [],
    'ó': [],
    'ö': [],
    'ő': [],
    'p': [],
    'q': [],
    'r': [],
    's': [],
    't': [],
    'u': [],
    'ú': [],
    'ü': [],
    'ű': [],
    'v': [],
    'w': [],
    'x': [],
    'y': [],
    'z': []
}
hitLetter = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: ''
}

#Billentyűzet
letterA = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[2]')
letterA_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[11]')
letterB = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[7]')
letterC = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[5]')
letterD = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[4]')
letterE = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[4]')
letterE_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[10]')
letterF = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[5]')
letterG = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[6]')
letterH = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[7]')
letterI = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[9]')
letterI_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[2]')
letterJ = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[8]')
letterK = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[9]')
letterL = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[10]')
letterM = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[9]')
letterN = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[8]')
letterO = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[10]')
letterO_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[5]')
letterO_double_short_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[3]')
letterO_double_long_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[6]')
letterP = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[11]')
letterQ = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[2]')
letterR = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[5]')
letterS = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[3]')
letterT = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[6]')
letterU = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[8]')
letterU_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[7]')
letterU_double_short_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[4]')
letterU_double_long_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[8]')
letterV = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[6]')
letterW = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[3]')
letterX = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[4]')
letterY = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[3]')
letterZ = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[7]')

enterButton = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[2]')
deleteButton = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[9]')


letters = {
    'a': letterA,
    'á': letterA_accent,
    'b': letterB,
    'c': letterC,
    'd': letterD,
    'e': letterE,
    'é': letterE_accent,
    'f': letterF,
    'g': letterG,
    'h': letterH,
    'i': letterI,
    'í': letterI_accent,
    'j': letterJ,
    'k': letterK,
    'l': letterL,
    'm': letterM,
    'n': letterN,
    'o': letterO,
    'ó': letterO_accent,
    'ö': letterO_double_short_accent,
    'ő': letterO_double_long_accent,
    'p': letterP,
    'q': letterQ,
    'r': letterR,
    's': letterS,
    't': letterT,
    'u': letterU,
    'ú': letterU_accent,
    'ü': letterU_double_short_accent,
    'ű': letterU_double_long_accent,
    'v': letterV,
    'w': letterW,
    'x': letterX,
    'y': letterY,
    'z': letterZ,
}

row = 1
index = 0
currentWord = words[index]
solution = ""

#ahhoz kell, hogy ha történt törlés a tömbben, akkor ne növelje az indexet, és ne kerüljön ezért korábban beírásra a tömbben később szereplő szó
#a ciklus legvégén visszaállítjuk az értékét igazra
noDeletion = True

# Beírjuk az első szót
print("A beírt szó:", currentWord)
for letter in currentWord:
    letters[letter].click()
enterButton.click()
numberOfTries = 1

# A beírt szó eredménye
for column  in range(1, 6):
    cell = driver.find_element(By.XPATH, '//*[@id="grid"]/div[{}]/div[{}]'.format(row, column))
    letter = currentWord[column-1]
    className = cell.get_attribute("class").split()[2]
    if(className == "miss" and letter not in missedLetter):
        missedLetter.append(letter)

    if(className == "near"):
        nearLetter[letter].append(column-1)
        deleteWordsBasedOnNearLetters(words, letter, column)
        noDeletion = False

    if(className == "hit"):
        hitLetter[column] = letter
        deleteWordsBasedOnHitLetters(words, hitLetter)
        noDeletion = False

# Eltávolítjuk a rossz betűk közül azokat a betűket, amiből több van
for letter in missedLetter:
    if letter in hitLetter.values():
        missedLetter.remove(letter)

for letter in missedLetter:
    if len(nearLetter[letter]) > 0:
        missedLetter.remove(letter)

#missedletter miatti torles hivasa (a felesleges betűk eltávolítása után)
for letter in missedLetter:
    deleteWordsBasedOnMissedLetters(words, letter)
    noDeletion = False

gameOver = False

# Vizsgáljuk, hogy megvan-e minden betű, ha igen, akkor gameOver
foundLetters = 0
for key in hitLetter:
    if hitLetter[key]:
        foundLetters += 1
    if foundLetters == 5:
        print("A keresett szó: ", currentWord.upper())
        solution = currentWord
        gameOver = True


while(not gameOver):
    # Új ablakot nyitunk, ha betelik a 6 sor
    if(row == 6):
        driver.quit()
        driver = webdriver.Chrome(service=service, options=options)
        openPage()
        row = 0     #mert lejjebb megnoveljuk eggyel meg a szo beirasa elott

    currentWord = words[index]  #ENNEK ELOL KELL LENNIE

    #Billentyűzet
    letterA = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[2]')
    letterA_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[11]')
    letterB = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[7]')
    letterC = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[5]')
    letterD = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[4]')
    letterE = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[4]')
    letterE_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[10]')
    letterF = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[5]')
    letterG = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[6]')
    letterH = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[7]')
    letterI = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[9]')
    letterI_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[2]')
    letterJ = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[8]')
    letterK = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[9]')
    letterL = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[10]')
    letterM = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[9]')
    letterN = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[8]')
    letterO = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[10]')
    letterO_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[5]')
    letterO_double_short_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[3]')
    letterO_double_long_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[6]')
    letterP = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[11]')
    letterQ = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[2]')
    letterR = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[5]')
    letterS = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[2]/div[3]')
    letterT = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[6]')
    letterU = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[8]')
    letterU_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[7]')
    letterU_double_short_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[4]')
    letterU_double_long_accent = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[8]')
    letterV = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[6]')
    letterW = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[3]')
    letterX = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[4]')
    letterY = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[3]/div[3]')
    letterZ = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[1]/div[7]')

    enterButton = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[2]')
    deleteButton = driver.find_element(By.XPATH, '//*[@id="keyboard"]/div[4]/div[9]')


    letters = {
        'a': letterA,
        'á': letterA_accent,
        'b': letterB,
        'c': letterC,
        'd': letterD,
        'e': letterE,
        'é': letterE_accent,
        'f': letterF,
        'g': letterG,
        'h': letterH,
        'i': letterI,
        'í': letterI_accent,
        'j': letterJ,
        'k': letterK,
        'l': letterL,
        'm': letterM,
        'n': letterN,
        'o': letterO,
        'ó': letterO_accent,
        'ö': letterO_double_short_accent,
        'ő': letterO_double_long_accent,
        'p': letterP,
        'q': letterQ,
        'r': letterR,
        's': letterS,
        't': letterT,
        'u': letterU,
        'ú': letterU_accent,
        'ü': letterU_double_short_accent,
        'ű': letterU_double_long_accent,
        'v': letterV,
        'w': letterW,
        'x': letterX,
        'y': letterY,
        'z': letterZ,
    }

    # Beírjuk a szót
    print("A beírt szó:", currentWord)
    row += 1
    for letter in currentWord:
        letters[letter].click()
    enterButton.click()
    numberOfTries += 1

    # A beírt szó eredménye
    for column  in range(1, 6):
        cell = driver.find_element(By.XPATH, '//*[@id="grid"]/div[{}]/div[{}]'.format(row, column))
        letter = currentWord[column-1]

        className = cell.get_attribute("class").split()[2] # miss / near / hit lesz az eredmény
        if(className == "miss" and letter not in missedLetter):
            missedLetter.append(letter)
        
        if(className == "near"):
            nearLetter[letter].append(column-1)
            deleteWordsBasedOnNearLetters(words, letter, column)
            noDeletion = False
            
        if(className == "hit"):
            hitLetter[column] = letter
            deleteWordsBasedOnHitLetters(words, hitLetter)
            noDeletion = False

    # Eltávolítjuk a rossz betűk közül azokat a betűket, amiből több van (missed és hit vagy missed és near egyben)
    for letter in missedLetter:
        if letter in hitLetter.values():
            missedLetter.remove(letter)

    for letter in missedLetter:
        if len(nearLetter[letter]) > 0:
            missedLetter.remove(letter)

    #missedletter miatti torles hivasa, később hívjuk meg, mert előbb kivesszük a felesleges betűket
    for letter in missedLetter:
        deleteWordsBasedOnMissedLetters(words, letter)
        noDeletion = False


    # Vizsgáljuk, hogy megvan-e minden betű, ha igen, akkor gameOver
    foundLetters = 0
    for key in hitLetter:
        if hitLetter[key]:
            foundLetters += 1
    if foundLetters == 5:
        print("A keresett szó: ", currentWord.upper())
        solution = currentWord
        gameOver = True

    #a torlesek miatt csokkenhet a tomb merete az index ala, ezt kuszoboli ki
    #csak akkor növeli az index méretét ha nem volt törlés
    if(index < len(words)-1 and noDeletion):
        index += 1
    else: index = 0

    noDeletion = True


#Kiírjuk fájlba a dátumot-megoldást-próbálkozásokat
today = date.today()
lastDate = ""

with open("solutions.txt", 'r') as file:
    #Megkeressük az utolsó dátumot
    for row in file:
        pass
    lastDate = row.strip().split(';')[0]

    if(lastDate != str(today)):
        with open("solutions.txt", 'a', encoding="utf-8") as file:
            file.write(f"{today};{solution};{numberOfTries}\n")