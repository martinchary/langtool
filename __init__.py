from langtool import json_to_list, clear


def menu():
    clear()
    selected = ''
    while selected != 'x':
        print("Choose an option: ")
        print("[A] add new term")
        print("[V] view full list of terms")
        print("[P] practice")
        print("[X] exit")
        selected = input()
        selected = selected.lower()
        clear()
        if selected == 'a':
            print("You chose add new term.")
        if selected == 'v':
            print("view full list of terms")
        if selected == 'p':
            print("Practice")


# practice(json_to_list())
# print(json_to_list())
# add_term('sconfitta', 'defeat')
# menu()
