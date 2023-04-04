import pandas as pd
import numpy as np
import string
import difflib
import prefer_and_avoid_ingredients 
import string


df = pd.read_excel(r'IndianFoodDatasetXLS.xlsx')

n = len(df)

list_a = df['TranslatedIngredients'].tolist()

# print(list_a)



redundant_words = ['tablespoon','to','cut','into','chop','frying','original','low','fat','make','the','inch','all','tightly','packed','required','requirement','finely','taste','for','deep','cook','tablespoons','teaspoon','teaspoons','needed','chopped','roughly','cup','cups','salt','to','taste','thinly','as','per','oil','sliced','slice','or','and','halved','half','soaked','overnight','pressure','cooked','coarse','coarsely','pounded','slit','lengthwise','pinch','fresh','wash','grated']
list_c = []


# type(list_a[1])

for recipe in list_a:
    b = str(recipe).translate(str.maketrans('', '', '/-)(0123456789')).lower() #this line removes punctuation marks other than the commas
    c = str.maketrans(string.punctuation, ' '*len(string.punctuation))  #this line separates buggy seapartion of commas. Example: 'ghee,mango' were treated as a single string. This ;ine removes the commas so that they can be treated differently.
    list_c.append(b.translate(c))

    
print("\n\nlist_c is:")
print(list_c)

list_d = []

for recipe in list_c:
    final_ingredients = []
    ingredients = recipe.split()
    for ingredient in ingredients:
        if not ingredient in redundant_words:
            final_ingredients.append(ingredient)
    list_d.append(final_ingredients)


print("\n\nlist_d is:")
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
            recipe_score-=2
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
    print(f"\n-------INGREDIENTS:--------")
    print(recipe_tr_ingr)
    print(f"\n-------INSTRUCTIONS:-------")
    print(recipe_tr_inst)
    print("\n-------REFERENCE LINK:------")
    print(recipe_web_link)








