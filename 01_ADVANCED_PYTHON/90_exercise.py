# example
# cube - finder(3)
# {1: 1, 2: 8, 3: 27}


def cube_finder(n):
    cubes={}
    for i in range(1, n + 1):
        cubes[i] = i ** 3
    return cubes

print(cube_finder(10))
        