k = int(input("Enter the k value : "))
total_entry = int(input("How many number you want in your tuple : "))
ourlist = []
for i in range(total_entry):
    ourlist.append(int(input(f"Enter the {i+1}th entry : ")))
print(ourlist)
ourlist.sort()
ourlist = ourlist[ :k] + ourlist[-k:]

ourTuple = tuple(ourlist)
print(ourTuple)