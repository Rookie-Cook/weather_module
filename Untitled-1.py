import pandas as pd
import numpy as np
import string
import difflib
import prefer_and_avoid_ingredients 



df = pd.read_excel(r'C:\Users\geove\OneDrive\Docs\Sem 6\Subjects\Mini Project\RookieCook\Datasets\Indian Food Recipes\archive\IndianFoodDatasetXLS.xlsx')

n = len(df)

list_a = df['TranslatedIngredients'].tolist()

# print(list_a)

import string

# redundant_words = ['tablespoon','cut','into','inch','all','required','requirement','finely','taste','for','deep','cook','tablespoons','teaspoon','teaspoons','needed','chopped','roughly','cup','cups','salt','to','taste','thinly','as','per','oil','sliced','slice','or','and','halved','half','soaked','overnight','pressure','cooked','coarse','coarsely','pounded','slit','lengthwise','pinch','fresh','wash','grated']
list_c = []


# type(list_a[1])

for recipe in list_a:
    b = str(recipe).translate(str.maketrans('', '', '/)(-0123456789')).lower() 
    # b1 = str(recipe).translate(str.maketrans('', '', '/-)(0123456789')).lower() 
    # b_temp = b1.split()
    # b_words = [word for word in b_temp if word.lower() not in redundant_words]
    # b = ' '.join(b_words)
    c = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    list_c.append(b.translate(c))
    
    
# print(list_c)

list_d = []


for recipe in list_c:
    ingredients = recipe.split()
    list_d.append(ingredients)


print(list_d)
    
# score_list = []
# for i in list_d:
#     recipe_score = 0
#     for j in i:
#         temp_list = difflib.get_close_matches(j, prefer_and_avoid_ingredients.summer_prefer_list)
#         if len(temp_list)>0:
#             recipe_score+=1
#         temp_list.clear()
#     score_list.append(recipe_score)

# score_list.sort(reverse=True)
# print(score_list)


score_dict = {}
for i in list_d:
    recipe_score = 0
    for j in i:
        temp_list1 = difflib.get_close_matches(j, prefer_and_avoid_ingredients.summer_prefer_list)
        if len(temp_list1)>0:
            recipe_score+=1
        temp_list1.clear()
        temp_list2 = difflib.get_close_matches(j, prefer_and_avoid_ingredients.summer_avoid_list)
        if len(temp_list2)>0:
            recipe_score-=1.5
        temp_list2.clear()
    score_dict[str(list_d.index(i))]=recipe_score

#score_dict is a dict contaning items as 'index_of_recipe':score
print(score_dict)

sorted_score_dict = dict(sorted(score_dict.items(), key=lambda item: item[1]))
rev_sorted_score_dict = dict(reversed(list(sorted_score_dict.items())))


#FINAL OUTPUT OF LIST OF RECIPES THAT ARE SUGGESTED FOR THE SEASON
print(rev_sorted_score_dict)

suggested_recipes_list = list(rev_sorted_score_dict.keys())
print(suggested_recipes_list)

#getting the top50_recipes
top50 = []
for i in suggested_recipes_list:
    if suggested_recipes_list.index(i)<=9:
        top50.append(int(i)+1)

print("\n\n\nThe top 50 recipes are:")
print(top50)

list_top50_rec_with_data = []
# new_temp_list = []
for i in top50:
    # print(f"\n\n{top50.index(i)+1}]\n"+f"{df.loc[i,'TranslatedRecipeName','TranslatedIngredients','TranslatedInstructions']}")
    recipe = df.values[i-1]
    list_top50_rec_with_data.append(recipe)
    recipe_tr_name = recipe[2]
    recipe_tr_ingr = recipe[4]
    recipe_tr_inst = recipe[13]
    recipe_web_link = recipe[14]
    
    print("\n\n\n############################################")
    print(f"{top50.index(i)+1}]"+f"{recipe_tr_name}\n")
    print("Details:")
    print(f"\n-------INGREDIENTS:-------")
    print(recipe_tr_ingr)
    print(f"\n-------INSTRUCTIONS:-------")
    print(recipe_tr_inst)
    print("\n-------Reference link:------")
    print(recipe_web_link)








