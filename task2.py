import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type' : 'application/json',
            'Authorization': f'OAuth {self.token}'
            }
    def _get_link(self, path: str):
        url = 'https://cloud-api.yandex.net/' + "v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, headers=headers, params=params)
        return response.json().get('href')

    def upload_file(self, path: str, file_name: str):
        upload_link = self._get_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'),  headers = headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    PATH = os.getcwd()
    DIR = 'new'
    DIR_1 = 'files'
    FILE = 'test.txt' # Не придумал ничего лучше чем разбить отдельно директории и имя файла, которое и указывается для params Я.Диска, надеюсь это корректно.
    path_to_file = os.path.join(PATH, DIR, DIR_1, FILE)
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload_file('/'+FILE, path_to_file)
