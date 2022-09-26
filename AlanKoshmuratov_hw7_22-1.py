def binary_search(number, *number_list):
    N = 20
    ResultOk = False
    First = 0
    Last = N - 1
    while First < Last:
        Middle = (number_list[First] + number_list[Last]) // 2
        if number == number_list[Middle]:
            First = Middle
            Last = First
            ResultOk = True
            break


        if number > number_list[Middle]:
            First = Middle + 1
        if number < number_list[Middle]:
            Last = Middle - 1


    if ResultOk:
        print(f'элемент найден - {number_list[Middle]}')
    else:
        print('элемент не найден')
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
#selection_sort(90, 4, 5, 8, 88, 2, 6)






binary_search(6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

