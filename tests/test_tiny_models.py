import sys,os
sys.path.insert(0,os.path.abspath(''))
from unittest import TestCase, main
from web_form.form_app.tiny_models import TinyModel


class TestTinyModels(TestCase):

    def test_is_phone_positive(self):

        positive_data = [
            "+79998887766",
            "+7 888 777 55 44",
            "+79998 887766",
            "+7 888777 5544",
        ]
        tiny = TinyModel()
        for d in positive_data:
            self.assertTrue(tiny.is_phone(str(d)))


    def test_is_phone_negative(self):

        negative_data =  {
            '+7-888-777-55-44',
            '+8 888 777 55 44',
            '%7 888 777 55 44',
            '78887775544',
        },
        tiny = TinyModel()
        for d in negative_data:
            self.assertFalse(tiny.is_phone(str(d)))


    def test_is_email_positive(self):
        positive_data = [
            "jorj1980@mail.oops",    
            "mu.email@oops.bro",   
            "jorj.1980@mail.oops",   
            "jor1.980@mail.oops",   
            "1980hgj@mail.oops",   
        ]
        tiny = TinyModel()
        for d in positive_data:
            self.assertTrue(tiny.is_email(str(d)))


    def test_is_email_negative(self):
        negative_data =[  
            "jorj1980@mail..oops",    
            "mu.ema@@oops.bro",   
            "jorj..1980@mail.oops",   
            "jor1.980.@mail.oops",   
            "__++BEST++__@bromail.oops",   
        ]
        tiny = TinyModel()
        for d in negative_data:
            self.assertFalse(tiny.is_email(str(d)))


    def test_is_date_positive(self):
        positive_data = [
            "01.01.1723",
            "1723-01-01",
            "18.11.2023",
            "2020-12-31",
        ]
        tiny = TinyModel()
        for d in positive_data:
            self.assertTrue(tiny.is_date(d))


    def test_is_date_negative(self):
        negative_data =[  
            '11-11-2022',
            '2022.11.11',
            '92.11.2021',
            '11.13.2022',
            '08.02.4000',
            '008.02.2000',
            '08.102.4000',
            '08.02.40000',
            '0000-01-10',
            '2000-00-10',
            '2000-10-00',
            '40000-00-00',
            '2000-01-1',
            '11.3.2022',
        ]
        tiny = TinyModel()
        for d in negative_data:
            self.assertFalse(tiny.is_date(d))


    def test_get_fields_type_text(self):
        data = [
            "Form template name",   
            "65464654",   
            "Я томат",   
            "Jorj@#$%Oleg",  
        ]
        tiny = TinyModel()
        for d in data:
            self.assertEqual(tiny.get_fields_type({'item' : d}), {'item' : 'text'})


    def test_get_form_name_positive(self):
        data ={
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
        }
        tiny = TinyModel()
        for d in data:
            self.assertEqual(list(tiny.get_form_name(data.get(d)).keys())[0], 'name')


    def test_get_form_name_negative(self):
        data ={
            'negative1' : {
                'field_name_1' : 'Jorj.1990@email.my',
                'field_name_2' : 'sovsem',
                'field_name_3' : 'nichego',
            },
            'negative2' : {
                'field_name_1' : "Form template name",  
                'field_name_2' : "Form template name",  
                'field_name_3' : "Form template name",  
            },
        }
        tiny = TinyModel()
        for d in data:
            self.assertEqual(tiny.get_form_name(data.get(d)).keys(), data.get(d).keys())


if __name__ == '__main__':
    main()

# import sys,os
# sys.path.insert(0,os.path.abspath(''))
# # print(os.path.dirname(os.path.abspath('')))
# # print(os.path.abspath(''))
# for p in sys.path:
#     print(p)