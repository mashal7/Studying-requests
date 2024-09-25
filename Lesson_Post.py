import requests as req


class Test_New_Location:
    '''Работа с новой локацией'''

    def test_create_new_location(self):
        '''Создание новой локации'''

        base_url = 'https://rahulshettyacademy.com'  # базовая url
        post_resource = '/maps/api/place/add/json'  # ресурс метода Post
        key = 'key=qaclick123'  # параметр для всех запросов

        post_url = f'{base_url}{post_resource}?{key}'
        print(post_url)

        json_for_create_new_location = {  # body
            "location": {
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
            "language": "French-IN"
        }
        # создание новой локации
        result_post = req.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        status_code_post = result_post.status_code
        assert status_code_post == 200, f'Ошибка!, Статус-код {status_code_post}, должен быть 200'
        print(f'Статус код: {status_code_post}. Создана новая локация')

        # получение значение поля 'статус кода ответа'
        check_post = result_post.json()
        check_info_post = check_post.get('status')
        assert check_info_post == 'OK', 'Статус кода ответа не совпадает с OK'
        print(f'Статус кода ответа верен: {check_info_post}')

        # Нахождение place_id
        place_id = check_post.get('place_id')
        print(f'place_id: {place_id}')

        '''Проверка создания новой локации, отправка метода get по полученному place_id'''

        # Пример из postman: {{url}}/maps/api/place/get/json?key=qaclick123&place_id=a872f9eed879a615b0ca589f10301177
        get_resorce = '/maps/api/place/get/json'
        get_url = f'{base_url}{get_resorce}?{key}&place_id={place_id}'
        print(get_url)

        # отправка метода get по полученному place_id'
        result_get = req.get(get_url)
        print(result_get.text)

        status_code_get = result_get.status_code
        assert status_code_get == 200, f'Ошибка!, Статус-код {status_code_get}, должен быть 200'
        print(f'Статус код: {status_code_get}. Проверка создания новой локации прошла успешно')


new_place = Test_New_Location()
new_place.test_create_new_location()
