import json


def clear():
    print("\n"*100)


def json_import():
    with open('termList.json') as f:
        data = json.load(f)
    return data


def json_export(l):
    with open('termList.json', 'w') as file:
        json.dump(l, file)


def highest_id(list):
    top_id = 1
    for d in list:
        if d["id"] > top_id:
            top_id = d["id"]
    return top_id


def calculate_hit_ratio(hits, misses):
    if hits !=0:
        return hits/(hits + misses)
    else:
        return 0


def add_term(term, translation):
    if ',' in translation:
        translation = translation.split(',')
        translation = [t.strip() for t in translation]
    else:
        translation = [translation]
    terms = json_import()
    new_term = {
        "term": term,
        "id": highest_id(terms) + 1,
        "translations": translation,
        "hits": 0,
        "misses": 0,
        "hit_rate": calculate_hit_ratio(0,0)
    }
    terms.append(new_term)
    # terms[term] = translation
    json_export(terms)


def update_translation(item, term, translation):
    if ',' in translation:
        translation = translation.split(',')
        translation = [t.strip() for t in translation]
    else:
        translation = [translation]
    if item["term"] == term:
        item['translations'] = translation
    return item


def edit_term(term, translation):
    json_export([update_translation(t, term, translation) for t in json_import()])


def obtain_translation(term):
    translation = ''
    for t in json_import():
        if t['term'] == term:
            translation = "_".join(t['translations'])
            break
    return translation


def delete_term(term):
    terms = json_import()
    for d in terms:
        if d['term'] == term:
            terms.remove(d)
            break
    # if term in terms:
    #     del terms[term]
    json_export(terms)


def json_to_list():
    new_list = list()
    my_list = json_import()
    for d in my_list:
        new_list.append([d['term'], ", ".join(d['translations']), d['hit_rate']])
    return new_list


def miss(term):
    term['misses'] = misses + 1
    term = update_hit_rate(term)


def update_hit_rate(term):
    term['hit_rate'] = calculate_hit_ratio(term['hits'], term['misses'])
    return term


def update_hit_and_miss(d, term):
    if term['term'] in d:
        if d[term['term']] == 'hit':
            term['hits'] += 1
        else:
            term['misses'] += 1
        term = update_hit_rate(term)
    return term


def practice(terms):
    right_answers = 0
    total_terms = len(terms)
    results = dict()
    for term in terms:
        print(term['term'] + ':')
        reply = input()
        if reply in term['translations']:
            print("success!")
            results[term['term']] = 'hit'
            right_answers += 1
        else:
            print("wrong!")
            results[term['term']] = 'miss'
    print("You got " + str(right_answers) + " out of " + str(total_terms) + " questions right!")
    json_export([update_hit_and_miss(results, t) for t in json_import()])
