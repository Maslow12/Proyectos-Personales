import requests
import os
def import_file(url,extension,filename='file',directory='', n=1):
    try:
        for url in url:
            r = requests.get(url, allow_redirects=True)
            f = f'{filename}_{n}.{extension}'
            if directory == '':
                save_path = os.getcwd()
            else:
                save_path = directory
            open(f, 'wb').write(r.content)
            folder = os.path.join(save_path, f)
            print(f'Listo archivo {n}...')
            n+=1
        return folder
    except requests.ConnectionError:
        raise Exception('No hay conexion...')
