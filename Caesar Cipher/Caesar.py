word=input("enter the word:")
word=word.strip() #remove spaces from the first and the end
word=word.replace(" ", "") #remove spaces between the words
word=word.lower() #convert to lowercase
k=int(input("key:"))
listl=list(word)
e=[]
e1=[]
for i in listl:
    newword=ord(i)+k
    newword1=chr(newword)
    if newword>ord("z"):
        w=newword-26
        n=chr(w)
        e.append(n)
    else:
        e.append(newword1)
print("Encryption is "+"".join(e))
for j in listl:
    newword=ord(j)-k
    newword1=chr(newword)
    if newword<ord("a"):
        w=newword+26
        n=chr(w)
        e1.append(n)
    else:
        e1.append(newword1)
print("Descryption is "+"".join(e1))