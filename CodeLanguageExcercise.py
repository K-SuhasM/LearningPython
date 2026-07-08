#Encode
eng = input("Enter your word:   ")
print(f"Your entered word is \"{eng}\". ")
rs = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", }
rs2 = {"z", "y", "x", "w", "v", "u", "t", "d", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a", }
word = []
first3 = []
last3 = []

#If more than three letter word
if len(eng)>=3:
    for i in eng:
        word.append(i)

    first_letter = word[0]
    word.pop(0)
    word.append(first_letter)
#first random 3 letters
    for i in rs:
        first3.append(i)
        if len(first3) == 3:
            break
#last random 3 letters
    for i in rs2:
        last3.append(i)
        if len(last3) == 3:
            break
#result
    result = first3 + word + last3
    fresult = " ".join(result)
    print(fresult)

#If two letter word
elif len(eng)==2:
    eng=eng[::-1]
    print(eng)

#If one lettered word
elif len(eng)==1:
    print("Your word is too short to encode, your word is", eng)

if " " in eng:
    raise ValueError("Please enter a single word, your word cannot have spaces. ")

#Decode

cod= input("Enter encoded word:   ")
cod_ran = cod[3:-3]
print(cod_ran)
for i in cod_ran:
    a= cod_ran[-1]
    b= cod_ran[0:-1]
    final_word= a+b
print(a)
print(b)
print(final_word)

