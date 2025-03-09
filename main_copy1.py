# def fanc_names1(lst: list):
#     for i, el in enumerate(lst):
#       print(lst[i])
# my_list1 = ["Леха", "Ярик", "Марат"]
# fanc_names1(my_list1)
#
# def fanc_names2(lst: list):
#     for el in lst:
#         print(el)
# my_list2 = ["Леха", "Ярик", "Марат"]
# fanc_names2(my_list2)
#
# def func_autos(lst: list):
#     for i in lst:
#         print(f"Я хочу купить {i}")
# list_autos = ["hyunday", "bmw", "chevrolet"]
# func_autos(list_autos)


# def fanc_list(num: int):
#     list_guests = [input("Enter name: ") for x in range(num)]
#     print(list_guests)
#
#     def fanc_guests(lst: list):
#         for i in lst:
#             print(f"Приглашаю вас {i:.^10} на обед")
#
#     fanc_guests(list_guests)
#
# fanc_list(3)

def fanc_list(num):
    i = 0
    list_guests = [input(f"Введите имя {i+1:.^5} гостя: ") for i in range(num)]
    print(list_guests)

    def fanc_guests(lst: list):
        for i in lst:
            print(f"Приглашаю тебя {i:.>10} на обед")

    fanc_guests(list_guests)

    guest_minus = list_guests[1]
    print(f"{guest_minus:.^10} не сможет прийти на обед")
    list_guests.remove(guest_minus)
    guest_new = input("Введите имя нового гостя: ")
    print(f"{guest_new:.^10} прийдет на обед вместо {guest_minus:.^10}")
    list_guests.append(guest_new)
    print(f"Новый лист гостей {list_guests}")

fanc_list(3)