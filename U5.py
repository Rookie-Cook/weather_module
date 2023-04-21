import pandas as pd
import numpy as np
import string
import difflib

from prefer_and_avoid_ingredients import summer_prefer_list, summer_avoid_list
from weather_detection import season

df = pd.read_excel(r'C:\Users\geove\OneDrive\Docs\Sem 6\Subjects\Mini Project\RookieCook\Datasets\Indian Food Recipes\archive\IndianFoodDatasetXLS.xlsx')

list_a = df['TranslatedIngredients'].tolist()

redundant_words = {'tablespoon', 'to', 'cut', 'into', 'chop', 'well', 'in', 'tsp', 'more', 'warm', 'frying', 'original', 'low', 'fat', 'make', 'the', 'inch', 'all', 'tightly', 'packed', 'required', 'requirement', 'finely', 'taste', 'for', 'deep', 'cook', 'tablespoons', 'teaspoon', 'teaspoons', 'needed', 'chopped', 'roughly', 'cup', 'cups', 'salt', 'to', 'taste', 'thinly', 'as', 'per', 'oil', 'sliced', 'slice', 'or', 'and', 'halved', 'half', 'soaked', 'overnight', 'pressure', 'cooked', 'coarse', 'coarsely', 'pounded', 'slit', 'lengthwise', 'pinch', 'fresh', 'wash', 'grated'}

preferred_ing_set = set(summer_prefer_list)
avoided_ing_set = set(summer_avoid_list)

score_dict = {}
for i, recipe in enumerate(list_a):
    b = str(recipe).translate(str.maketrans('', '', '/-)(0123456789')).lower() 
    c = str.maketrans(string.punctuation, ' '*len(string.punctuation))  
    d = b.translate(c)
    querywords = d.split()
    resultwords  = [word for word in querywords if word.lower() not in redundant_words]
    recipe_ingr = resultwords
    recipe_score = sum(1 for ingr in recipe_ingr if ingr in preferred_ing_set) - 2 * sum(1 for ingr in recipe_ingr if ingr in avoided_ing_set)
    score_dict[str(i)] = recipe_score

sorted_score_dict = dict(sorted(score_dict.items(), key=lambda item: item[1], reverse=True))

suggested_recipes_list = list(sorted_score_dict.keys())[:10]

list_top50_rec_with_data = []
for i in suggested_recipes_list:
    recipe =
