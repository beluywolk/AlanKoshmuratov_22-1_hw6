def binary_search(number, *number_list):
    number_list = list(number_list)
    a = min(number_list)
    b = max(number_list)
    c = 0
    while c != number:
        c = (a+b) // 2
        if c < number:
            a = c + 1
        elif c > number:
            b = c - 1
        print(c)
def selection_sort(*args):
    args = list(args)
    args1 = []
    o = 0
    print(args)
    while True:

        a = list.pop([min(args)])
        args.remove(min(args))
        args1.append(a)
        o += 1
        if len(args) == 0:
            args = args1
            break

    print(args)
selection_sort(90, 4, 5, 8, 88, 2, 6)






binary_search(9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,\
              28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53\
              , 54, 55, 56, 57, 58, 59, 60 )


