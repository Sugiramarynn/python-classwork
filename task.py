# Text = input("Enter your full names: ")
# character_count = len(Text)
# print(f"Your name has {character_count} characters.")
# print("hello")

# text = input("enter your full name")
# character = len(text.replace(" ",""))
# print(f"Characters are ={character}")

words=[]
for i in range(1,6):
     word = input(f"Enter your full names {i}:")
     words.append(word)
     print("\n Word Character:")
     for word in words:
          print(f"'{word}' has {len(word)}characters")