user_info = {
    'name': 'harshit',
    'age': 24,
    'fav_movies': ['coco', 'kimi no wa '],
    'fav_tunes':['awakening','fairy tale'],
}


# print(user_info)

#how to add data
# user_info['fav_songs'] = ['song1', 'song2']
# print(user_info)

# pop method

# popped_item = user_info.pop('fav_tunes')
# print(f"poped item is {popped_item}")
# print(user_info)


 #poped item \


popped_item = user_info.popitem()
print(user_info)
print(popped_item)