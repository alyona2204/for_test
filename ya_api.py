import requests



def create_folder(path):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    resp = requests.put(f'{URL}?path={path}', headers=headers)
    status = resp.status_code
    result = f'Папка {path} была добавлена в Я.Диск'
    error = f'Папка {path} не была добавлена в Я.Диск'
    if status == 201:
        return status, result
    else:
        return status, error







