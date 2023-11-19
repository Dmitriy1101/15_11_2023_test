from tinydb import TinyDB, Query


db = TinyDB('dbdata\db.json')

data_list = [
    {
        'name' : 'TEPDtest',
        'field_name_1' : 'text',
        'field_name_2' : 'email',
        'field_name_3' : 'phone',
        'field_name_4' : 'date',
    },
    {
        'name' : 'TEtest',
        'field_name_1' : 'text',
        'field_name_2' : 'email',
    },
    {
        'name' : 'PDtest',
        'field_name_1' : 'phone',
        'field_name_2' : 'date',
    },
    {
        'name' : 'TEPDDtest',
        'field_name_1' : 'text',
        'field_name_2' : 'email',
        'field_name_3' : 'phone',
        'field_name_4' : 'date',
        'field_name_5' : 'date',
    },
    {
        'name' : 'TEPtest',
        'field_name_1' : 'text',
        'field_name_2' : 'email',
        'field_name_3' : 'phone',
    },
    {
        'name' : 'TPDtest',
        'field_name_1' : 'text',
        'field_name_2' : 'phone',
        'field_name_3' : 'date',
    },
    {
        'name' : 'TEDtest',
        'field_name_1' : 'text',
        'field_name_2' : 'email',
        'field_name_3' : 'date',
    },
    {
        'name' : 'EPDtest',
        'field_name_1' : 'email',
        'field_name_2' : 'phone',
        'field_name_3' : 'date',
    },
    {
        'name' : 'Ptest',
        'field_name_1' : 'phone',
    },
]

db.insert_multiple(data_list)