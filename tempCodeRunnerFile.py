def summer_avoid():
	summer_avoid_column = pd.DataFrame(df, columns=['avoid_in_summer'])
	summer_avoid_list = summer_avoid_column['avoid_in_summer'].tolist()
	summer_avoid_list_lower = []
	for i in summer_avoid_list:
		if not type(i) == float:
			i = i.lower()
			summer_avoid_list_lower.append(i)    
	summer_avoid_list = summer_avoid_list_lower
	summer_avoid_list.sort()
	# FO: 
	# print("\n\nThe python list of ingredients to avoid in summer:")
	# print(summer_avoid_list)
	return summer_avoid_list

print(summer_avoid.summer_avoid_list)