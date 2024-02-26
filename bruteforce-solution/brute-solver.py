from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

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

openPage()

# Szavak beolvasása a fájlból
words = []

with open("bruteforce-solution/otbetus-szavak.txt", encoding='utf-8') as file:
    for line in file:
        words.append(line.strip().lower())

# Brute force
numberOfTries = 0
wordCounter = 0

while(True):
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
    currentWord = words[wordCounter]

    #Beírjuk a szót
    for j in currentWord.lower():
        letters[j].click()
    enterButton.click()
    wordCounter += 1

    #Ha feldobja a hibá szó kiírást, akkor töröljük, ha nem, akkor elemntjük a szót
    try:
        driver.find_element(By.XPATH, "/html/body/main/aside[@class='visible']")
        time.sleep(2)
        for k in range(5):
            deleteButton.click()
    except:
        numberOfTries += 1
        with open("bruteforce-solution/elfogadott-szavak.txt", 'a', encoding='utf-8') as file:
            file.write(currentWord + '\n')

    if(numberOfTries == 6):
        driver.quit()
        driver = webdriver.Chrome(service=service, options=options)
        openPage()
        numberOfTries = 0

    if(currentWord == "vége"):
        break