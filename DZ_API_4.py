import requests as req


class Test_New_Location:
    '''Работа с новой локацией'''

    def __init__(self):
        self._url = 'https://rahulshettyacademy.com'
        self._key = 'key=qaclick123'

    @staticmethod
    def check_request(result, expected_status_code):
        '''Статический метод для проверки запроса'''
        print('Проверка на статус-код')
        status_code = result.status_code
        assert status_code == expected_status_code, f'Ошибка!, Статус-код {status_code}, должен быть {expected_status_code}'
        return status_code

    def test_create_new_location(self, expected_status_code=200):
        '''Создание новой локации с отправкой post запроса, проверкой на статус-код
           и проверкой статуса "OK" в сообщении'''

        # url для post запроса
        resource_post = '/maps/api/place/add/json'
        url_post = f'{self._url}{resource_post}?{self._key}'

        # body для post запроса
        json_body = {"location": {
            "lat": -38.383494,
            "lng": 33.427362
        }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"}

        # post запрос, проверка на статус-код и статус в сообщении
        print('-----Проверка запроса на создание новой локации-----')
        result = req.post(url_post, json=json_body)
        status_code = self.__class__.check_request(result, expected_status_code)
        print(f'Успешно! Статус-код: {status_code}')
        result_info = result.json()
        print(result_info)
        print('Проверка статуса в сообщении')
        status = result_info.get('status')
        assert status == 'OK', f'Статус в сообщении неправильный: {status}. Должен быть "OK"'
        print('Сообщение верное!')
        print('-----Проверка запроса на создание новой локации завершена успешно-----')

        # возвращаем place_id для проверки существования локации
        return result_info.get('place_id')

    def test_check_new_location(self, place_id, expected_status_code=200):
        '''Проверка существования новой локации с отправкой get запроса, проверкой на статус-код'''

        # url для get запроса
        resource_get = '/maps/api/place/get/json'
        url_get = f'{self._url}{resource_get}?{self._key}&place_id={place_id}'

        # get запрос и проверка на статус-код
        print('-----Проверка запроса на существование новой локации-----')
        result = req.get(url_get)
        result_info = result.json()
        print(result_info)
        status_code = self.__class__.check_request(result, expected_status_code)
        print(f'Успешно! Статус-код: {status_code}')
        print('-----Проверка запроса на существование новой локации завершена успешно-----')

    def test_delete_new_location(self, place_id, expected_status_code=200):
        '''Удаление новой локации с отправкой delete запроса, проверкой на статус-код'''

        # url для delete запроса
        resource_del = '/maps/api/place/delete/json'
        url_del = f'{self._url}{resource_del}?{self._key}'

        # body для delete запроса
        json_body = {
            "place_id": place_id
        }

        # delete запрос, проверка на статус-код и статус в сообщении
        print('-----Проверка запроса на удаление новой локации-----')
        result = req.delete(url_del, json=json_body)
        status_code = self.__class__.check_request(result, expected_status_code)
        print(f'Успешно! Статус-код: {status_code}')
        result_info = result.json()
        print(result_info)
        print('Проверка статуса в сообщении')
        status = result_info.get('status')
        assert status == 'OK', f'Статус в сообщении неправильный: {status}. Должен быть "OK"'
        print('Сообщение верное!')
        print('-----Проверка запроса на удаление новой локации завершена успешно-----')


    def check_five_location(self):
        '''Метод для создания и проверки 5 шт. place_id: получаем place_id через post запрос
        и записываем в файл .txt; читаем с файла и проверяем существование place_id через get запрос'''

        print('=====================Создание 5 шт. place_id=====================\n')
        with open('C:\\Users\\mpetrova\\Desktop\\place_id.txt', 'w', encoding='utf-8') as file:
            for i in range(1, 6):
                print(f'____________________Создание {i} place_id____________________')
                file.write(f'{self.test_create_new_location()}\n')
        print('=====================Создание 5 шт. place_id успешно завершена=====================\n')

        print('===============Проверка на существование 5 шт. place_id===========\n')
        with open('C:\\Users\\mpetrova\\Desktop\\place_id.txt', 'r', encoding='utf-8') as file:
            for i in range(1, 6):
                print(f'____________________Проверка {i} place_id____________________')
                self.test_check_new_location(file.readline().strip())
        print('============Проверка на существование 5 шт. place_id успешно завершена===========\n')





res = Test_New_Location()
place_id = res.test_create_new_location()
res.test_check_new_location(place_id)
#res.check_five_location()
#res.test_delete_new_location('b92c8c901b633cb12b3c47d1848c0fed')
#res.test_check_new_location('b92c8c901b633cb12b3c47d1848c0fed')