import requests
import os
def import_file(url,extension,filename='file',directory=''):
    try:
        r = requests.get(url, allow_redirects=True)
        f = f'{filename}.{extension}'
        if directory == '':
            save_path = os.getcwd()
        else:
            save_path = directory
        open(f, 'wb').write(r.content)
        folder = os.path.join(save_path, f)
        return folder
    except requests.ConnectionError:
        raise Exception('No hay conexion...')
print(import_file('https://www.cbssports.com/nba/standings/', 'html'))
