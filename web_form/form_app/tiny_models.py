from tinydb import TinyDB, Query
from collections import Counter
import datetime, re, os


class TinyModel():
    '''Простой клас для работы с TinyDB в рамках задания,
    включающий минимальный набор функций.'''

    def __init__(self):

        path = r'dbdata\db.json'
        #base_path = os.path.dirname(os.path.abspath(''))
        self.db = TinyDB(f'{path}')


    def is_phone(self, value: str) ->bool:
        '''Проверка поля на номер телефона'''

        value = value.replace(' ', '')
        if value[1:].isdigit() and value.startswith('+7') and len(value) == 12:
                return True
        return False


    def is_email(self, value: str) ->bool:
        '''Проверка поля на email'''

        pattern = r"(^[a-zA-Z0-9]+\.{0,1}[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$)"
        if re.match(pattern, value):
            return True
        return False


    def is_date(self, value: str) ->bool:
        '''Проверка поля на дату'''

        pattern = {
            r"(0[1-9]|[1-2][0-9]|3[0-1])\.(0[1-9]|1[1-2])\.([1-2][0-9]\d\d)" : '%d.%m.%Y',
            r"([1-2][0-9]\d\d)-(0[1-9]|1[1-2])-(0[1-9]|[1-2][0-9]|3[0-1])" : '%Y-%m-%d'
            }
        for pkey, pvalue in pattern.items():
            if re.match(pkey, value):
                return isinstance(datetime.datetime.strptime(value, pvalue), datetime.datetime)
        return False


    def get_fields_type(self, data: dict) ->dict:
        '''Устанавливаем типы полей'''

        typed_data = {}
        for key, value in data.items():
            if self.is_date(value):
                typed_data[key] = 'date'
                continue
            elif self.is_phone(value):
                typed_data[key] = 'phone'
                continue
            elif self.is_email(value):
                typed_data[key] = 'email'
                continue
            else:
                typed_data[key] = 'text'
        return typed_data


    def get_form_name(self, data: dict) ->dict:
        '''устанавливаем имя формы по входным данным.'''

        db_data = self.db.all()
        data = self.get_fields_type(data)
        result_dict = {}    #будит словарь  'коэфицент_похожести' : 'имя_формы' 
        for db_item in db_data:
            form_name = db_item.pop('name')#отделяем имя формы
            #отсеиваем неподходящие фоормы по именам полей 
            db_keys = set(sorted(db_item.keys()))
            data_keys =  set(sorted(data.keys()))
            if not db_keys <= data_keys:
                continue
            #на этом шаге мы знаем что имена полей совпадают и извлекаем значения для сравнения
            data_val = [data[v] for v in db_keys]
            db_val = [db_item[v] for v in db_keys]
            if db_val != data_val:
                continue
            #Если мы тут, то в случае равенства количества количества ключей продолжать нет смысла
            if len(data_keys) == len(db_keys):
                return {'name' : form_name}
            #Количество форм нехватающих в шаблоне
            k_diff = len(data_keys) - len(db_keys)
            result_dict[k_diff ] = form_name
        #На выходе будем сравнивать минимальный ключ это наиболее похожая форма, если таких нет вернем пришедшие типизированные_данные
        if result_dict:
            result = min(result_dict)
            return {'name' : result_dict.get(result)}
        return data
            