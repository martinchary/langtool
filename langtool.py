import json


def clear():
    print("\n"*100)


def add_term(term, translation):
    terms = json_import()
    terms[term] = translation
    with open('termList.json', 'w') as file:
        json.dump(terms, file)


def json_import():
    with open('termList.json') as f:
        data = json.load(f)
    return data


def json_to_list():
    my_dict = json_import()
    return [[k, v] for k, v in my_dict.items()]


def practice(terms):
    right_answers = 0
    total_terms = len(terms)

    for term in terms:
        print(term[0] + ':')
        reply = input()
        if reply == term[1]:
            print("success!")
            right_answers += 1
        else:
            print("wrong!")
    print("You got " + str(right_answers) + " out of " + str(total_terms) + " questions right!")
