square = {num: num ** 2 for num in range(1, 11)}
print(square)

square2 = {f"square of {num}": num ** 2 for num in range(1, 11)}
print(square2)

for k, v in square2.items():
    print(f"{k}:{v}")



    string = 'harshit'
    word_count = {char: string.count(char) for char  in string}
    print(word_count)