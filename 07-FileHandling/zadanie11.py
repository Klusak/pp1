arr=['Camp Rock','Harry Potter','Avatar',"Don't Worry Darling", 'The Policeman']
file = open("filmy.txt",'w')
for title in arr:
    file.write(title)
    file.write("\n")
file.close()