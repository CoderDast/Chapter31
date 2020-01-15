def res_text(Text):
    string = len(Text)
    lower = upper = 0
    for i in Text:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper +=1
    lower = lower / string * 100
    upper = upper / string * 100
    print("Lower = ", lower,'%')
    print("Upper = ", upper,'%')


res_text(input('Input text, please = '))