import requests as req
from unicodedata import category


class Test_Get_Categorie_Joke:
    '''Получение категорий шуток и проверка шутки на определённую категорию'''

    def __init__(self):
        self._url = 'https://api.chucknorris.io/jokes/'
        self._categories = None

    @staticmethod
    def check_request(url, expected_status_code):
        '''Статический метод для проверки запроса на статус-код'''
        print('Проверка на статус-код')
        result = req.get(url)
        status_code = result.status_code
        assert status_code == expected_status_code, f'Ошибка!, Статус-код {status_code}, должен быть {expected_status_code}'
        return result, status_code

    def get_categories(self, expected_status_code=200):
        '''Тест для получения всех категорий шуток, включает:
           отправку запроса, проверку на статус-код, печать категорий'''

        # url для запроса
        path_categories = 'categories'
        url_categories = self._url + path_categories
        print(url_categories)

        # проверка запроса
        print('---------------Проверка запроса на получение категорий---------------')
        result, status_code = self.__class__.check_request(url_categories, expected_status_code)
        print(f'Статус-код: {status_code}')
        self._categories = result.json()
        print(f"Категории: {', '.join(self._categories)}")
        print('------------Проверка запроса на получение категорий прошла успешно------------')

    def get_joke_of_category(self, category, expected_status_code=200):
        '''Тест для получения случайной шутки по нужной категории, включает:
           отправку запроса, проверку на статус-код, получение шутки'''

        # получим категории, если нет нужного атрибута
        self._categories if self._categories else self.get_categories()

        # проверяем наличие категории
        print('______________Проверка наличия категории в списке______________')
        if category not in self._categories:
            return 'Данной категории не существует'
        else:
            print('Успешно! Данная категория существует')

        # url для запроса
        path_random_joke_category = f'random?category={category}'
        url_category = self._url + path_random_joke_category

        # проверка запроса, получение шутки
        print('------------Проверка запроса на получение шутки определенной категорий------------')

        result, status_code = self.__class__.check_request(url_category, expected_status_code)
        print(f'Успешно! Статус-код: {status_code}')
        dict_result = result.json()

        print('---------Проверка запроса на получение шутки определенной категорий прошла успешно---------')
        return dict_result.get("value")


result = Test_Get_Categorie_Joke()
result.get_categories()
category = input('Введите категорию: ')
joke = result.get_joke_of_category(category)
print(joke)