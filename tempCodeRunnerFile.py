import pandas as pd
import numpy as np
import string
import difflib
import prefer_and_avoid_ingredients 
import string


df = pd.read_excel(r'C:\Users\geove\OneDrive\Docs\Sem 6\Subjects\Mini Project\RookieCook\Datasets\Indian Food Recipes\archive\IndianFoodDatasetXLS.xlsx')

n = len(df)

list_a = df['TranslatedIngredients'].tolist()

# print(list_a)


redundant_words = ['tablespoon','to','cut','into','tsp','frying','original','low','fat','make','the','inch','all','tightly','packed','required','requirement','finely','taste','for','deep','cook','tablespoons','teaspoon','teaspoons','needed','chopped','roughly','cup','cups','salt','to','taste','thinly','as','per','oil','sliced','slice','or','and','halved','half','soaked','overnight','pressure','cooked','coarse','coarsely','pounded','slit','lengthwise','pinch','fresh','wash','grated']
list_c = []


# type(list_a[1])

for recipe in list_a:
    b = str(recipe).translate(str.maketrans('', '', '/-)(0123456789')).lower() #this line removes punctuation marks other than the commas
    c = str.maketrans(string.punctuation, ' '*len(string.punctuation))  #this line separates buggy seapartion of commas. Example: 'ghee,mango' were treated as a single string. This ;ine removes the commas so that they can be treated differently.
    d = b.translate(c)
    querywords = d.split()
    resultwords  = [word for word in querywords if word.lower() not in redundant_words]
    result = ' '.join(resultwords)
    list_c.append(result)

    
print("\n\nlist_c is:")
print(list_c)

list_d = []

for recipe in list_c:
    ingredients = recipe.split()
    list_d.append(ingredients)



print("\n\nlist_d is:")
print(list_d)