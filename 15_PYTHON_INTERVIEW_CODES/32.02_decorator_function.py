def decor_result(result_function):
    def distinction(marks):
        result = []
        for m in marks:
            if m >= 75:
                print("distinction")
            result.append(result_function([m]))
        return result
    return distinction



@decor_result
def result(marks):
    for m in marks:
        if m>=33:
            pass
        else:
            print('fail')
            return "Fail"
    else:
        print("pass")
        return "PASS"
    
    
result = result([45,78,80,34,66,90,30])

print("Results",result)
            