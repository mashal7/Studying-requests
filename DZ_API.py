import requests as req

class Test_Get_Categories:

    def __init__(self, url):
        self._url = url


    @staticmethod
    def check_request(url, expected_status_code):
        result = req.get(url)
        status_code = result.status_code
        print(f'Статус-код: {status_code}')
        assert status_code == expected_status_code, 'Ошибка!, Статус-код не совпадает'
        print('Статус-код корректен')
        return result

    # @staticmethod
    # def check_request(result, expected_status_code):
    #     status_code = result.status_code
    #     print(f'Статус-код: {status_code}')
    #     assert status_code == expected_status_code, 'Ошибка!, Статус-код не совпадает'
    #     print('Статус-код корректен')


    def get_categories(self, expected_status_code=200):
        '''Тест для получения всех категорий шуток, включает:
           отправку запроса, проверку на статус-код, печать категорий'''
        path_categories = 'categories'
        url_categories = self._url + path_categories
        print(url_categories)
        repr_categories = req.get(url_categories)  # отправка GET-запроса
        self.__class__.check_request(repr_categories, expected_status_code)
        self._categories = repr_categories.json()  # декодирование JSON, получение категорий
        print(*self._categories, sep=',')


    def get_joke_of_category(self, category, expected_status_code=200):
        '''Тест для получения шутки по определенной категории, включает:
           отправку запроса, проверку на статус-код, печать шутки'''
        path_random_joke_category = f'random?category={category}'
        url_category = self._url + path_random_joke_category
        print(f'url: {url_category}')
        #repr_category = req.get(url_category)

        self.__class__.check_request(repr_category, expected_status_code)
        dict_repr_category = repr_category.json()
        print(f'Ответ: {dict_repr_category}')
        print(f'value (cлучайная шутка): {dict_repr_category.get("value")}')





result = Test_Get_Categories('https://api.chucknorris.io/jokes/')
result.get_categories()
#result.get_joke_of_category('animal')
