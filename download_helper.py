import os
import requests
from tqdm import tqdm


def download(url, name):
    print('downloading ' + name + '.exe ...')
    res = requests.get(url, stream=True)
    total_length = int(res.headers.get('content-length'))
    with open('./installer/' + name, "wb") as pyexe, tqdm(
            desc=name,
            total=total_length,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in res.iter_content(chunk_size=1024):
            if data:
                size = pyexe.write(data)
                bar.update(size)


def run_exe(name=''):
    if name.endswith('exe'):
        os.system('./installer/' + name)
    else:
        if name.endswith('.zip'):
            path = './installer/' + name.replace('.zip', '/')
            os.system('mkdir ' + path)
            os.system('unzip -o ' + path + '.zip' + ' -d ' + path)
            install_mac_app(path)
        else:
            os.system('open ./installer/' + name)


def run_command(command):
    if '-' != command and len(command) != 0:
        os.system(command)


def install_mac_app(path=''):
    files = os.listdir(path)
    for file in files:
        os.system('open ' + file)

