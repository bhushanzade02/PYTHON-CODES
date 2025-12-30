numbers = input("Enter numbers separated by spaces: ").split()

numberlist = []
for n in numbers:
    numberlist.append(int(n))

def quick_sort(numbers):
    # if list has 0 or 1 elements → already sorted
    if len(numbers) <= 1:
        return numbers

    # choose the pivot 
    pivot = numbers[0]

    # split into two groups
    smaller = []
    bigger = []

    for num in numbers[1:]:      # skip the pivot
        if num < pivot:
            smaller.append(num)
        else:
            bigger.append(num)

    # sort the two parts and join
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)


result = quick_sort(numberlist)


def even_avg_disp():
    even_sum = 0
    even_count = 0
    for num in result:
        if num % 2 == 0:
            even_sum += num
            even_count += 1
    if even_count > 0:
        even_avg = even_sum / even_count
        print(f"Average of even numbers: {even_avg:.2f}")
    else:
        print("No even numbers found.")


print("Sorted list:", result)

print(f"Second largest: {result[-2]}")

print(f"Second smallest: {result[1]}")

even_avg_disp()
