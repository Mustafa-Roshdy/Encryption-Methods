def findChar(c):
    for i in range(26):
        if c == lest[i]:
            return i
    
    return -1
lest= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word=input("enter the word:")
word=word.strip() #remove spaces from the first and the end
word=word.replace(" ", "") #remove spaces between the words
word=word.lower() #convert to lowercase
k=input("key:")
K=k.strip() 
k=k.replace(" ", "") 
k=k.lower()
list1=list(word)
list2=list(k)
e=[]
e1=[]
for i in list2:
    if len(list2)<len(list1):
        list2.append(i)
for j in range(len(list1)):
    ind1 = findChar(list1[j])
    ind2 = findChar(list2[j])
    ind3 = (ind1+ind2)%26
    e.append(lest[ind3])
print("Encryption is "+"".join(e))
for k in range(len(list1)):
    ind1 = findChar(list1[k])
    ind2 = findChar(list2[k])
    ind3 = (ind1-ind2)%26
    e1.append(lest[ind3])
print("Descryption is "+"".join(e1))
