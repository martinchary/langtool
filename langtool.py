import json


def clear():
    print("\n"*100)


def term_import():
    with open('termList.json') as f:
        data = json.load(f)
    return data


def term_export(l):
    with open('termList.json', 'w') as file:
        json.dump(l, file)


def practice_import():
    with open('practice.json') as f:
        data = json.load(f)
    return data


def practice_export(l):
    with open('practice.json', 'w') as file:
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
    terms = term_import()
    new_term = {
        "term": term,
        "id": highest_id(terms) + 1,
        "translations": translation,
        "hits": 0,
        "misses": 0,
        "hit_rate": calculate_hit_ratio(0,0)
    }
    if not term_exists(term):
        terms.append(new_term)
    # terms[term] = translation
    term_export(terms)


def term_exists(myTerm):
    val = False
    for term in term_import():
        if term['term'].lower() == myTerm.lower():
            val = True
            break
    return val


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
    term_export([update_translation(t, term, translation) for t in term_import()])


def obtain_translation(term):
    translation = ''
    for t in term_import():
        if t['term'] == term:
            translation = "_".join(t['translations'])
            break
    return translation


def delete_term(term):
    terms = term_import()
    for d in terms:
        if d['term'] == term:
            terms.remove(d)
            break
    # if term in terms:
    #     del terms[term]
    term_export(terms)


def json_to_list():
    new_list = list()
    my_list = term_import()
    for d in my_list:
        new_list.append([d['term'], ", ".join(d['translations']), d['hit_rate']])
    return new_list


def miss():
    practice = practice_import()
    practice['misses'] += 1
    practice_export(practice)


def reset_practice():
    practice = practice_import()
    practice['hits'] = 0
    practice['misses'] = 0
    practice['length'] = 6
    practice['terms'] = ['adesso', 'anno', 'ballare', 'ragazzo', 'suonare', 'aria']
    practice['results'] = {}
    practice['answers'] = {}
    practice_export(practice)


def validate(word, answer):
    practice = practice_import()
    terms = term_import()
    for term in terms:
        if term['term'] == word:
            translations = term['translations']
            break
    if answer.lower() in translations:
        practice['results'][word] = 'Correct!'
        practice['hits'] += 1
    else:
        practice['results'][term['term']] = 'Wrong! The answer(s) is: ' +  ", ".join(translations)
        practice['misses'] += 1
    practice['answers'][word] = answer
    practice_export(practice)


def add_practice(name):
    practice = practice_import()
    practice['terms'][name] = 'new'
    practice_export(practice)


def update_hit_rate(term):
    term['hit_rate'] = round(calculate_hit_ratio(term['hits'], term['misses']), 3)
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
    term_export([update_hit_and_miss(results, t) for t in term_import()])
