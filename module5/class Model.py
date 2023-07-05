import json


class Model:

    @classmethod
    def save(cls):
        dict_attributes = vars(cls)
        user_dict_attrebutes = {}
        for attrebute in dict_attributes:
            if not attrebute.startswith('_'):
                user_dict_attrebutes[attrebute] = dict_attributes[attrebute]
        with open('file.json', 'w', encoding='utf-8') as f:
            json.dump(user_dict_attrebutes, f)
        return print('Атрибуты класса успешно записаны!')


class C1(Model):
    title = '1'
    text = '2'
    author = '3'


C1.save()
