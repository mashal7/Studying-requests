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
        #создание новой локации
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

        #place_id = 4444  # ошибочный place_id

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

        '''Изменение новой локации, отправка метода put по полученному place_id'''

        # получение url
        put_resource = '/maps/api/place/update/json'
        put_url = f'{base_url}{put_resource}?{key}'
        print(put_url)

        json_for_update_new_location = {"place_id":place_id,
        "address":"100 Lenina street, RU",
        "key":"qaclick123"
        }

        # отправка метода put по полученному place_id'
        result_put = req.put(put_url, json=json_for_update_new_location)
        print(result_put.text)

        status_code_put = result_put.status_code
        assert status_code_put == 200, f'Ошибка!, Статус-код {status_code_put}, должен быть 200'
        print(f'Статус код: {status_code_put}. Изменение новой локации прошло успешно')

        check_put = result_put.json()
        check_put_info = check_put.get('msg')
        print(f'Сообщение: {check_put_info}')
        assert check_put_info == 'Address successfully updated', 'Запрос ошибочный!'
        print('Сообщение верное!')


        '''Проверка изменения новой локации'''

        result_get = req.get(get_url)
        print(result_get.text)

        status_code_get = result_get.status_code
        assert status_code_get == 200, f'Ошибка!, Статус-код {status_code_get}, должен быть 200'
        print(f'Статус код: {status_code_get}. Проверка изменения новой локации прошла успешно')


        '''Удаление новой локации'''

        delete_resource = '/maps/api/place/delete/json'
        delete_url = f'{base_url}{delete_resource}?{key}'
        print(delete_url)

        json_for_delete_location = {"place_id":place_id}

        # отправка метода delete по полученому place_id'
        result_delete = req.delete(delete_url, json=json_for_delete_location)
        print(result_delete.text)

        status_code_delete = result_delete.status_code
        assert status_code_delete == 200, f'Ошибка!, Статус-код {status_code_delete}, должен быть 200'
        print(f'Статус код: {status_code_delete}. Удаление новой локации прошло успешно')

        check_delete = result_delete.json()
        check_delete_info = check_delete.get('status')
        print(f'Сообщение: {check_delete_info}')
        assert check_delete_info == 'OK', 'Запрос ошибочный!'
        print('Сообщение верное!')

        '''Проверка удаления новой локации'''

        result_get = req.get(get_url)
        print(result_get.text)

        status_code_get = result_get.status_code
        assert status_code_get == 404, f'Ошибка!, Статус-код {status_code_get}, должен быть 404'
        print(f'Статус код: {status_code_get}. Проверка удаления новой локации прошла успешно')

        check_msg = result_get.json()
        check_msg_info = check_msg.get('msg')
        print(f'Сообщение: {check_msg_info}')
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists", "Запрос ошибочный!"
        print('Сообщение верное!')

        print('Тестирование Test_new_location завершено успешно')

new_place = Test_New_Location()
new_place.test_create_new_location()
