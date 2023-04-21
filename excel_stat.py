import difflib
import pandas as pd
import numpy as np

list1 = difflib.get_close_matches('cumin seeds', ['car', 'bittergourd','turmericleaves','mustardseeds' 'animals', 'house', 'animation'])
print(list1)

query = 'What is hello are you ok?'
stopwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he', 'ok']
querywords = query.split()

resultwords  = [word for word in querywords if word.lower() not in stopwords]
result = ' '.join(resultwords)

print(resultwords)
print(result)







'''



print(result)
Algorithm:
1. get number of elements 'n' in the column
2. initiate n zeroes in a list
3. add all the cells from the column into the list list_a. 
    Now this list contains un-separated list of ingredients although in string form. 
4. separate all the items within each list of items and add to list B so that 
    list B not only has smaller lists, each lsit such that the items in it are separated ingredients.
5. Now use double for loops to look within the list B and within the elements for the list inside it.
6. Initate a point variable that will be reset to 0 at the end.
7. Compare the items in list B with the items in the favoured/avoided list and add and subtract the points.
8. Add the points for each recipe into a new list called points_list
9. Create another list called sorted_points_list
10. Accordingly get the row number of the recipe with most points and add that row number to a new list 
    called "list_of_recommended_recipes"
11. Now for rach row number, display the recipe in the scrutinized format.
'''


##1. Get number of elemets 'n' in the column

df = pd.read_excel(r'summer.xlsx')
n = len(df)

##2

##3 






