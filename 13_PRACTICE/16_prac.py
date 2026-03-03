import pandas as pd 

df = pd.read_csv('daily expense - Sheet1.csv')


first_row_text = df['Reason'].iloc[0] 

def extract(text_data):
    total_sum = 0 
    current_num = ''

    for char in str(text_data):
        if char.isdigit():
            current_num += char
        else:
            if current_num != '':
                total_sum += int(current_num)
                current_num = ''
    if current_num != '':
        total_sum += int(current_num)
    return total_sum 

result = extract(first_row_text)
print(f' sum  first row is: {result}')
