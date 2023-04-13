import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {
            "path": file_path, "overwrite": "true"
        }
        response = requests.get(url=upload_url, headers=headers, params=params).json()
        url = response.get('href', '')
        response_result = requests.put(url=url, data=open(file_path, 'rb'))
        if response_result.status_code == 201:
            print('Success')
        return response_result
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'file_for_YD.txt'
    token = ''
    uploader = YaUploader(token).upload(path_to_file)
    print(uploader)
ы