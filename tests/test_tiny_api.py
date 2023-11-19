#Прогон запросов и визуализация ответов
#через http://127.0.0.1:8000/api
#возмозно исследовать в ручную через браузер


import requests

url = 'http://127.0.0.1:8000/api'

test_data = { 
    'negative_1' : {
        "text_1": "Form template name",   
        "text_2": "65464654",   
        "text_3": "Я томат",   
        "text_4": "Jorj@#$%Oleg",  
    },
    'negative_2' : {
        "email_1": "jorj1980@mail.oops",    
        "email_2": "mu.email@oops.bro",   
        'email_3': "jorj.1980@mail.oops",   
        'email_4': "jor1.980@mail.oops",   
        'email_5': "1980hgj@mail.oops",   
    },
    'negative_3' : {
        "phone_1": "+79998887766",
        "phone_2": "+7 888 777 55 44",
        "phone_3": "+79998 887766",
        "phone_4": "+7 888777 5544",
    },
    'negative_4' : {
        "date_1": "01.01.1723",
        "date_2": "1723-01-01",
        'date_3' : "18.11.2023",
        'date_4': "2020-12-31",
    },
    'negative5' : {
        'not_phone_1' : '+7-888-777-55-44',
        'not_phone_2' : '+8 888 777 55 44',
        'not_phone_3' : '%7 888 777 55 44',
        'not_phone_4' : '78887775544',
    },
    'negative6' : {
        'not_date_1' : '11-11-2022',
        'not_date_2' : '2022.11.11',
        'not_date_3' : '92.11.2021',
        'not_date_4' : '11.13.2022',
        'not_date_5' : '08.02.4000',
        'not_date_6' : '008.02.2000',
        'not_date_7' : '08.102.4000',
        'not_date_8' : '08.02.40000',
        'not_date_9' : '0000-01-10',
        'not_date_10' : '2000-00-10',
        'not_date_11' : '2000-10-00',
        'not_date_12' : '40000-00-00',
        'not_date_13' : '2000-01-1',
        'not_date_14' : '11.3.2022',
    },
    'negative7' : {
        "not_email_1": "jorj1980@mail..oops",    
        "not_email_2": "mu.ema@@oops.bro",   
        'not_email_3': "jorj..1980@mail.oops",   
        'not_email_4': "jor1.980.@mail.oops",   
        'not_email_5': "__++BEST++__@bromail.oops",   
    },
    'negative8' : {
        'field_name_1' : 'text',
        'field_name_2' : 'email',
        'field_name_3' : 'phone',
        'field_name_4' : 'date',
    },
    'positive1' : {
        'field_name_1' : 'Jorj',
        'field_name_2' : 'Jorj.1990@email.my',
        'field_name_3' : '+7 999 000 99 90',
        'field_name_4' : '11.11.1000',
    },
    'positive2' : {
        'field_name_1' : 'Jorj',
        'field_name_2' : 'Jorj.1990@email.my',
        'field_name_3' : '+7 999 000 99 90',
        'field_name_4' : '2000-01-31',
    },
    'positive3' : {
        'field_name_1' : 'Jorj',
        'field_name_2' : 'Jorj.1990@email.my',
        'field_name_3' : '+7 999 000 99 90',
        'field_name_4' : 'Tarakan',
    },
    'positive4' : {
        'field_name_1' : 'Jorj',
        'field_name_2' : 'Jorj.1990@email.my',
        'field_name_3' : 'sovsem',
        'field_name_4' : 'nichego',
    },
    'positive5' : {
        'field_name_1' : 'Jorj.1990@email.my',
        'field_name_2' : 'sovsem',
        'field_name_3' : 'nichego',
    },
}

#'positive1'
s = requests.Session()
for result, data in test_data.items():
    response = s.post(url,  data=data)
    jdata = response.json()
    #print(f'{result}-------------------->{data}')
    for key, val in jdata.items():
        print(f'{key} : {val}')