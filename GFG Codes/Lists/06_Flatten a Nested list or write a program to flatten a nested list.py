#6.	Flatten a Nested List
# Write a program to flatten a nested list (e.g., [[1, 2], [3, 4]] → [1, 2, 3, 4]).

mylist = [["manu","Manoj"],["Swathi","Swathu"],["Sannu","Saanvi"]]

norma_list = [item for sublist in mylist for item in sublist]
print(norma_list)

mylist2 = []
for sublist in mylist:
    for item in sublist:
        mylist2.append(item)
print(mylist2)
