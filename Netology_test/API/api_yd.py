import requests
from Netology_test.tests.config import tokenyandex
class Ya_disk:

    def __init__(self):
        pass

    def response_status(self):
        url_folder_name = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': tokenyandex}
        response_profile = requests.get('https://cloud-api.yandex.net/v1/disk/', headers=headers)
        return response_profile.status_code


    def create_folder(self, id_screen_name):
        """Метод создания папки на Я.Диске с ID пользователя VK"""

        self.folder_name = id_screen_name
        url_folder_name = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': f'ID={self.folder_name}',
                  'url': url_folder_name}
        headers = {'Authorization': tokenyandex}
        response_folder = requests.put(url_folder_name, headers=headers, params=params)
        return self.folder_name






if __name__ == '__main__':
    id = 'test_folder'
    ya = Ya_disk()
    ya.create_folder(id)
    ya.response_status()



