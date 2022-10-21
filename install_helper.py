import os
import requests
import subprocess
from tqdm import tqdm


def download(url, name):
    print('downloading ' + name + ' ...')
    try:
        headers = {'Connection': 'close'}
        res = requests.get(url, headers=headers, stream=True, verify=False)
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
    except Exception as e:
        print(e)


def run_installer(name=''):
    print('installing ' + name + ' ...')
    if name.endswith('exe'):
        subprocess.Popen('.\\installer\\' + name, shell=True)
    else:
        if name.endswith('.zip'):
            path = './installer/' + name.replace('.zip', '')
            os.system('mkdir ' + path)
            unzip(path + '.zip', path)
            install_mac_app(path)
        else:
            subprocess.Popen('open ./installer/' + name, shell=True)


def unzip(source='', des=''):
    os.system('unzip -n ' + source + ' -d ' + des)


def run_command(command):
    print(command)
    if '-' != command and len(command) != 0:
        if not subprocess.Popen(command, shell=True):
            print(command + ' finish')


def install_mac_app(path=''):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.app'):
            subprocess.Popen('open ' + path + '/' + file, shell=True)
