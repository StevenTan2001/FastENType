# FastENType
It is a simpler and faster English inputting method based on `Rime`.


# How to type? Here are some instructions:
1. Type in the order according to the letters in the word. 
2. Always type the first letter of the **w**ord. 
3. Always ignore vowel letters (_a/e/i/o/u_) **u**nless it is the first/last letter in the word.
4. For tandem repeated le**tt**ers, only type once.
4. _y_ and _w_ are considered as vowel letters if **i) they are at the end of the word** OR **ii) they are NOT closely followed by a vowel**. 
5. _n_ and _r_ should be omitted unless they are closely followed by a vowel, as you k**n**ow. 
6. Always type the last letter of the wor**d**.
7. Press space or number keys to choose the word you want to input.
8. For words equals to or shorter than 5 letters, you can also directly type the word and select by the space key. Even if it is longer than 5 letters, you can also type it directly by pressing the enter key.
9. To input a Word with the capitalized first letter, press _z_ after typing the word. To input a WORD with all letters capitalized, press _z_ twice after typing the word.
10. If punctuation occurs in a word (e.g, “-“), type words before and after the punctuation separately.
11. Alternative method with a plural word: if a word exist and does not end with an _s_, then type _s_ after a word can give a word followed by _s_. E.g., to input word "conditions", you can type _cdts_ (**c**on**d**i**t**ion**s**) or _cdtns_ (**c**on**d**i**t**io**n**+**s**).
 

> Here are some other examples.\
> **w**or**d** -> **w**or~~~**d**: wd *OR* word\
> **kn**o**w** -> **k**~~~**n**o**w**: knw *OR* know\
> **Apple** -> **ap**~~p~~ ~~~**l**e + *a->A* : aplez *OR* applez\
> **sq**ui**rr**e**l** -> **s**~~~**q**ui~~~**r**~~r~~e**l**: sqrl\
> **b**a**cky**ar**d** -> **b**a~~~**ck**~~~**y**ar~~~**d**: bckyd\
> **c**on**c**en**tr**a**t**io**n** -> **c**on~~~**c**en~~~**tr**a~~~**t**io**n**: cctrtn\
> **d**i**ff**e**r**en**t**ia**t**io**n** -> **d**i~~~**f**~~f~~e~~~**r**en~~~**t**ia~~~**t**io**n**: dfrttn\
> **c**on**t**e**mp**o**r**a**ry** -> **c**on~~~**t**e~~~**m**~~~**p**o~~~**r**a~~~**ry**: ctmprry\
> **e**n**v**i**r**on**m**en**t** -> **e**n~~~**v**i~~~**r**on~~~**m**en~~~**t**: evrmt\
> **i**n**st**a**ll**a**t**io**n** -> **i**n~~~**s**~~~**t**a~~~**l**la~~~**t**io**n**: istltn



# Installation
Please install `Rime` first.

Refer [https://github.com/rime](url)   
Refer [https://rime.im](url)



Add `- schema: FastEN` under `schema_list:` in `Rime/default.yaml`.  
Unzip `FastEN_V2.dict.yaml` and move the file into `Rime/`.  
Move `FastEN.schema.yaml` into `Rime/`.  


# Build your own dictionary
Run FastENBuilder_PublicVersion.py in Python. Refer the comments in the file.

---

This is my first time uploading files on Github. I am not professional on coding. For codes, some of which are generated/optimised by Github Copilot. I would like to apologize first for the potential inconveniences, and I appreciate any suggestions on the input method!
