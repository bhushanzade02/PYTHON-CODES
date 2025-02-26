user_info = {
    'name': 'harshit',
    'age': 24,
    'fav_movies': ['coco', 'kimi no wa '],
    'fav_tunes':['awakening','fairy tale'],
}



user={}
name = input("what is your name ")
age = input('what is your ag e')
fav_movies = input('enter your fav movies')
fav_song = input('enter eyour gav songs ')


user['name'] = name
user["age"]=age
user['fav_movies'] = fav_movies
user["fav_song"] = fav_song
 

for key, value in user.items():
    print(f'{key}:{value}')