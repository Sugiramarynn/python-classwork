# Text = input("Enter your full names: ")
# character_count = len(Text)
# print(f"Your name has {character_count} characters.")
# print("hello")

# text = input("enter your full name")
# character = len(text.replace(" ",""))
# print(f"Characters are ={character}")

# words=[]
# for i in range(1,6):
#      word = input(f"Enter your full names {i}:")
#      words.append(word)
#      print("\n Word Character:")
#      for word in words:
#           print(f"'{word}' has {len(word)}characters")

n1=input("enter the text\n")
n1=n1.upper()
n1 = list(n1)
for i in range(len(n1)):
     if n1[i] == "A":  # Second replacement (after 'k' has been replaced)
         n1[i] = "K"
     elif n1[i] == "K":  # First replacement
         n1[i] = "A"    
     elif n1[i] == "J":
         n1[i] = "I"
     elif n1[i] == "I":
         n1[i] = "J"
     elif n1[i] == "P":
         n1[i] = "O"
     elif n1[i] == "O":
         n1[i] = "P"
     elif n1[i] == "T":
         n1[i] = "E"
     elif n1[i] == "E":
         n1[i] = "T"
     elif n1[i] == "F":
         n1[i] = "U"
     elif n1[i] == "U":
         n1[i] = "F"
print(''.join(n1))      
 