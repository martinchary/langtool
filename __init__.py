from langtool import json_to_list, clear, add_term, practice, json_import, edit_term,obtain_translation


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


# edit_term('anno', 'year, years')
# practice(json_import())
print('a')
print(obtain_translation("anno"))
# print(json_to_list())
# add_term('sconfitta', 'defeat')
# menu()
