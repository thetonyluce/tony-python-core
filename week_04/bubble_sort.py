def bubble_sort(my_list):
    length = len(my_list) - 1
    not_sorted = True

    while not_sorted:
        not_sorted = False
        for item in range(0, length):
            if my_list[item] > my_list[item + 1]:
                temp = my_list[item + 1]
                my_list[item + 1] = my_list[item]
                my_list[item] = temp
                print(my_list)
                not_sorted = True


test_list = (1, 2, 3, 4, 5)
bubble_sort(test_list)
