while True:
    try:
        number = int(input('ENter a number:'))
    except ValueError:
        print('PLease Type  a Intger:')
    except:
        print("i=unexcepted Error")
    else:
        print(f"user input ={number}")
    finally:
        print('finally Blocks')

    