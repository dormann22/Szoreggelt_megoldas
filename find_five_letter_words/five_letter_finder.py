with open("find_five_letter_words/magyar-szavak.txt", encoding='utf-8') as inFile:
    with open("find_five_letter_words/otbetus-szavak.txt", 'w', encoding='utf-8') as outFile:
        for line in inFile:
            if(len(line.strip()) == 5):
                    outFile.write(line)
