import binascii #convert binary to string
import random
lest= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def BinaryToDecimal(binary):
    string = int(binary, 2)
    return string
word=input("enter the word:")
word=word.strip() #remove spaces from the first and the end
word=word.replace(" ", "") #remove spaces between the words
word=word.lower() #convert to lowercase
key=""
XorList=[]
XorList2=[]
for j in range(len(word)):
    key +=random.choice(lest)
list2=list(key)

print("The word is : " + str(word)) 

# using join() + ord() + format()
# Converting String to binary
BinaryWord = ''.join(format(ord(i), '07b') for i in word)
  
print("The Word after binary conversion : " + str(BinaryWord))

print("The Key is : " + str(key))
  
# using join() + ord() + format()
# Converting String to binary
BinaryKey = ''.join(format(ord(i), '07b') for i in key)
  
print("The Key after binary conversion : " + str(BinaryKey))
for m in range(len(BinaryWord)):
    xor=int(BinaryWord[m])^int(BinaryKey[m])
    XorList.append(str(xor))
x="".join(XorList)
print("result of Xor before Encryption : "+x)

str_data =' '
  
# slicing the input and converting it
# in decimal and then converting it in string
for i in range(0, len(x), 7):
     
    # slicing the x from index range [0, 6]
    # and storing it in temp_data
    temp_data = x[i:i + 7]
      
    # passing temp_data in BinarytoDecimal() function
    # to get decimal value of corresponding temp_data
    decimal_data = BinaryToDecimal(temp_data)
      
    # Decoding the decimal value returned by
    # BinarytoDecimal() function, using chr()
    # function which return the string corresponding
    # character for given ASCII value, and store it
    # in str_data
    str_data = str_data + chr(decimal_data)
 
# printing the result
print("Encryption is : "+str_data)

#Descryption
for n in range(len(BinaryKey)):
    xor2=int(x[n])^int(BinaryKey[n])
    XorList2.append(str(xor2))
y="".join(XorList2)
print("result of Xor before Descryption : "+y)

str_data2 =' '
  
# slicing the input and converting it
# in decimal and then converting it in string
for i in range(0, len(y), 7):
     
    # slicing the y from indey range [0, 6]
    # and storing it in temp_data
    temp_data = y[i:i + 7]
      
    # passing temp_data in BinarytoDecimal() function
    # to get decimal value of corresponding temp_data
    decimal_data = BinaryToDecimal(temp_data)
      
    # Decoding the decimal value returned by
    # BinarytoDecimal() function, using chr()
    # function which return the string corresponding
    # character for given ASCII value, and store it
    # in str_data2
    str_data2 = str_data2 + chr(decimal_data)
 
print("Descryption is : "+str_data2)