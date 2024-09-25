
import requests
from unicodedata import category


class Test_new_joke:
    '''Создание новой шутки'''

    def __init__(self):
        pass

    def test_create_new_joke_categories(self):
        '''Создание шутки по категории'''
        category = 'sport'
        url = f'https://api.chucknorris.io/jokes/random?category={category}'
        print(url)
        result = requests.get(url)
        print(f'Статус код: {result.status_code}')
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Успешно')
        else:
            print('Провал')
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get('categories')
        print(check_info)
        assert check_info == [category], 'Категория не верна'
        print('Категория верна')
        # check_info_value = check.get('value')
        # print(check_info_value)
        # name = 'Chuck'
        # if name in check_info_value:
        #     print('Chuck присутствует')
        # else:
        #     print('Chuck отсутствует')

sport_joke = Test_new_joke()
sport_joke.test_create_new_joke_categories()