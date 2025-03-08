def fanc_names1(lst: list):
    for i, el in enumerate(lst):
        print(lst[i])
my_list1 = ["Леха", "Ярик", "Марат"]
fanc_names1(my_list1)



def fanc_names2(lst: list):
    for el in lst:
        print(el)
my_list2 = ["Леха", "Ярик", "Марат"]
fanc_names2(my_list2)


def func_autos(lst: list):
    for i in lst:
        print(f"Я хочу купить {i}")
list_autos = ["hyunday", "bmw", "chevrolet"]
func_autos(list_autos)
