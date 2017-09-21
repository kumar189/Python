# takes the input string
in_str= input("enter the string you want to sort")
# in_str="hello world and practice makes perfect and hello world again"
#splits the string into words and store in a
a= in_str.split()
#Removes the duplicates words in "a" using set and prints the words in arranging order
print(" ".join(sorted(set(a))))
