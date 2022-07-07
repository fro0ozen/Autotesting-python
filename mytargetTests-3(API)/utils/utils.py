import faker


def name_generator():
    return faker.Faker().bothify(text='???????-???????-#######')


def in_list(param, value, lst, in_lst=True, ret_param=None):
    for i in lst:
        if i[param] == value:
            return in_lst, i.get(ret_param, None)
    return not in_lst, None
