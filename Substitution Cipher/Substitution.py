dictionary={"a":"e","b":"k","c":"p","d":"u","e":"z","f":"d","g":"j","h":"o","i":"t","j":"y","k":"c","l":"i","m":"n","n":"s","o":"x","p":"b","q":"h","r":"m","s":"r","t":"W","u":"a","v":"f","w":"l","x":"q","y":"v","z":"g"}
word=input("enter the word:")
word=word.strip() #remove spaces from the first and the end
word=word.replace(" ", "") #remove spaces between the words
word=word.lower() #convert to lowercase
listl=list(word)
e=[]
e1=[]
for i in listl:
        e.append(dictionary[i])
print("Encryption is "+"".join(e))
key_list = list(dictionary.keys())
val_list = list(dictionary.values())
for j in listl:
        position = val_list.index(j)
        e1.append(key_list[position])
print("Descryption is "+"".join(e1))