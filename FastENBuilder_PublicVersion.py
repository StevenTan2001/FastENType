# Copyright: The code is produced by StevenTan with some of contents generated and optimised by Github Copilot AI. Allocation of either file in this project on my Github (https://github.com/StevenTan2001/FastENType) without my permission is not allowed.
# Last update: Apr 29, 2025

import csv
import re
import string
from datetime import date



# Input your directories of dictionary file here.
dict_file1 = '/Users/~/Library/Rime/FastEN_V2.dict.yaml'
dict_file2 = '/Users/~/Library/Rime/FastEN_V2.dict.yaml'
dict_file3 = '/Users/~/Library/Rime/FastEN_V2.dict.yaml'

# Download or produce your dictionary here.

# Common words can be show with higher priority while typing.
CommonWordsDictionary = "YourCommonWordsDictionary.csv"

# You can find all the English words on the Internet. For example, refer https://stackoverflow.com/questions/4481236/english-dictionary-xml-csv-file
AllWordDictionary = "YourAllWordDictionary.csv"

# If there are words you need to input but not in the dictionary, input or paste them into a plain text file. Punctuations are fine as long as they are in remove_chars.
ExpansionDictionary = "YourExpansionDictionary.txt"
remove_chars = '[·’!"\#$%&\'()＃！（）*+,-./:;<=>?\@，：?￥★、…．＞【】［］《》？“”‘’\[\\]^_`{|}~]+'



def Text2WordList(file):
    with open(file, "r") as f:
        print(f)
        arr = []
        for line in f.readlines():
            line = line.strip('\n')
            string1 = re.sub(remove_chars, " ", line)
            spArr = string1.split(' ')
            for i in range(len(spArr)):
                arr.append(spArr[i])
    print(arr)
    return arr


def isVowel(char, charList=None, i=0):
    if charList is not None and i > 0 and char == 'y' or char == 'w':
        if i == len(charList) - 1: return True  # w/y at the end of a word, consider as a vowel
        if i < len(charList) - 1 and isVowel(charList[i + 1], charList,
                                             i + 1): return False  # w/y before a vowel, consider as a consonant
        return True  # In other cases, w/y consider as a vowel
    return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'


def KeepThisLetter(charList, i):
    if i < len(charList) - 1 and charList[i] == charList[i + 1]: return False
    if i == len(charList) - 1: return True  # at the end of a word
    if isVowel(charList[i], charList, i): return False
    if i > 0 and charList[i] == 'n' or charList[i] == 'r':
        if i < len(charList) - 1 and isVowel(charList[i + 1], charList, i + 1): return True  # n/r before a vowel
        return False

    if i > 0 and charList[i] == 'y' or charList[i] == 'w':
        if i < len(charList) - 1 and isVowel(charList[i + 1], charList, i + 1): return True  # w/y before a vowel
        return False

    return True


def WordHandler(lines):
    str = lines[0]
    charList = list(str)
    length = len(charList)
    if length > 0:
        finishList = [charList[0]]
    else:
        return []
    for i in range(len(charList)):
        if i == 0:
            continue
        if KeepThisLetter(charList, i):
            finishList.append(charList[i])
    Code = ''.join(finishList)

    return [str.lower(), Code.lower()]


def CapHandler(lines, wordHandler):
    if wordHandler is None:
        return []
    str = lines[0]
    try:
        Code = wordHandler[1]
    except:
        return ["", ""]
    Cap1Str = str[0].upper() + str[1:]
    Cap1Code = Code.lower()+'z'
    CapAllStr = str.upper()
    CapAllCode = Code.lower() + 'zz'
    return [[Cap1Str, Cap1Code], [CapAllStr, CapAllCode]]


def PluralHandler(lines, wordHandler):
    if wordHandler is None:
        return []
    str = lines[0]
    if str[-1] == 's':
        return ["", ""]
    try:
        Code = wordHandler[1]
    except:
        return ["", ""]
    PlStr = str.lower() + 's'
    PlCode = Code.lower()+'s'
    Cap1Str = PlStr[0].upper() + PlStr[1:]
    Cap1Code = PlCode.lower() + 'z'
    CapAllStr = PlStr.upper()
    CapAllCode = PlCode.lower() + 'zz'
    return [[PlStr, PlCode], [Cap1Str, Cap1Code], [CapAllStr, CapAllCode]]




def data(mode="Normal", expansion=None):
    if mode == "Common" or mode == "Short":
        with open(CommonWordsDictionary, mode='r') as file:
            words = csv.reader(file)
            arr = [["a", "a"], ["b", "b"]]
            for lines in words:
                if mode == "Common":
                    wordHandler = WordHandler(lines)
                    arr.append(wordHandler)
                    try:
                        arr.append(CapHandler(lines, wordHandler)[0])
                        arr.append(CapHandler(lines, wordHandler)[1])
                        arr.append(PluralHandler(lines, wordHandler)[0])
                        arr.append(PluralHandler(lines, wordHandler)[1])
                        arr.append(PluralHandler(lines, wordHandler)[2])
                    except:
                        pass
                elif mode == "Short":
                    if len(list(lines[0])) <= 5:
                        arr.append([lines[0].lower(), lines[0].lower()])
                        try:
                            arr.append(CapHandler(lines, ["", lines[0].lower()])[0])
                            arr.append(CapHandler(lines, ["", lines[0].lower()])[1])
                            arr.append(PluralHandler(lines, ["", lines[0].lower()])[0])
                            arr.append(PluralHandler(lines, ["", lines[0].lower()])[1])
                            arr.append(PluralHandler(lines, ["", lines[0].lower()])[2])
                        except:
                            pass

        return arr
    elif mode == "Expansion":
        arr = [["a", "a"], ["b", "b"]]
        tempList = Text2WordList(expansion)
        for s in range(len(tempList)):
            # print(f"TempList[s]={tempList[s]}")
            if tempList[s] != '':
                wordHandler = WordHandler([tempList[s], ""])
                arr.append(wordHandler)
                try:
                    arr.append(CapHandler([tempList[s], ""], wordHandler)[0])
                    arr.append(CapHandler([tempList[s], ""], wordHandler)[1])
                    arr.append(PluralHandler([tempList[s], ""], wordHandler)[0])
                    arr.append(PluralHandler([tempList[s], ""], wordHandler)[1])
                    arr.append(PluralHandler([tempList[s], ""], wordHandler)[2])
                except:
                    pass

                if len(tempList[s]) <= 5:
                    arr.append([tempList[s].lower(), tempList[s].lower()])
                    try:
                        arr.append(CapHandler(lines, lines[0].lower())[0])
                        arr.append(CapHandler(lines, lines[0].lower())[1])
                        arr.append(PluralHandler(lines, lines[0].lower())[0])
                        arr.append(PluralHandler(lines, lines[0].lower())[1])
                        arr.append(PluralHandler(lines, lines[0].lower())[2])
                    except:
                        pass

    else:
        with open(AllWordDictionary, mode='r') as file:
            words = csv.reader(file)
            arr = [["a", "a"], ["b", "b"]]
            for lines in words:
                wordHandler = WordHandler(lines)
                arr.append(wordHandler)
                try:
                    arr.append(CapHandler(lines, wordHandler)[0])
                    arr.append(CapHandler(lines, wordHandler)[1])
                    arr.append(PluralHandler(lines, wordHandler)[0])
                    arr.append(PluralHandler(lines, wordHandler)[1])
                    arr.append(PluralHandler(lines, wordHandler)[2])
                except:
                    pass

    return arr





try:
    dict = open(dict_file1, mode='w')
    today = date.today()
    version = today.strftime("%Y%m%d")
    str = f"# Rime dictionary\n# encoding: utf-8\n\n---\nname: FastEN_V2\nversion: \"{version}\"\nsort: by_weight\n...\n"
    dict.write(str)

    with open(dict_file1, mode='a') as inputs:
        writer = csv.writer(inputs, delimiter='\t')
        writer.writerows(data(mode="Short"))

    with open(dict_file1, mode='a') as inputs:
        writer = csv.writer(inputs, delimiter='\t')
        writer.writerows(data(mode="Common"))

    with open(dict_file1, mode='a') as inputs:
        writer = csv.writer(inputs, delimiter='\t')
        writer.writerows(data())

    with open(dict_file1, mode='a') as inputs:
        writer = csv.writer(inputs, delimiter='\t')
        writer.writerows(data(mode="Expansion", expansion=f"{ExpansionDictionary}"))


except FileNotFoundError as e:
    try:
        dict = open(dict_file2, mode='w')
        today = date.today()
        version = today.strftime("%Y%m%d")
        str = f"# Rime dictionary\n# encoding: utf-8\n\n---\nname: FastEN_V2\nversion: \"{version}\"\nsort: by_weight\n...\n"
        dict.write(str)

        with open(dict_file2, mode='a') as inputs:
            writer = csv.writer(inputs, delimiter='\t')
            writer.writerows(data(mode="Short"))

        with open(dict_file2, mode='a') as inputs:
            writer = csv.writer(inputs, delimiter='\t')
            writer.writerows(data(mode="Common"))

        with open(dict_file2, mode='a') as inputs:
            writer = csv.writer(inputs, delimiter='\t')
            writer.writerows(data())

        with open(dict_file2, mode='a') as inputs:
            writer = csv.writer(inputs, delimiter='\t')
            writer.writerows(data(mode="Expansion", expansion=f"{ExpansionDictionary}"))
    except FileNotFoundError as e:
        dict = open(dict_file3, mode='w')
        today = date.today()
        version = today.strftime("%Y%m%d")
        str = f"# Rime dictionary\n# encoding: utf-8\n\n---\nname: FastEN_V2\nversion: \"{version}\"\nsort: by_weight\n...\n"
        dict.write(str)

        with open(dict_file3, mode='a') as inputs:
            writer = csv.writer(inputs, delimiter='\t')
            writer.writerows(data(mode="Short"))

        with open(dict_file3, mode='a') as inputs:
            writer = csv.writer(inputs, delimiter='\t')
            writer.writerows(data(mode="Common"))

        with open(dict_file3, mode='a') as inputs:
            writer = csv.writer(inputs, delimiter='\t')
            writer.writerows(data())

        with open(dict_file3, mode='a') as inputs:
            writer = csv.writer(inputs, delimiter='\t')
            writer.writerows(data(mode="Expansion", expansion=f"{ExpansionDictionary}"))

