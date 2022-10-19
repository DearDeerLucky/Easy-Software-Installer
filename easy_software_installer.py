import os
import json
import platform
import install_helper

resource_urls_path = './resource/software_download_url.json'
resource_urls_path_programmer = './resource/software_download_url_programmer.json'
resource_urls = []


def get_resource(resource_path):
    with open(resource_path, 'r', encoding='utf-8') as file:
        global resource_urls
        resource_urls = json.load(file)
        for resource_url in resource_urls:
            installer_url = get_installer_url(resource_url)
            if '-' != installer_url or len(installer_url) == 0:
                installer_name = get_installer_name(installer_url)
                print(installer_name)
                install_helper.download(installer_url, installer_name)
                install_helper.run_installer(installer_name)
            else:
                installer_command = get_installer_command(resource_urls[0])
                install_helper.run_command(installer_command)


def get_installer_name(url=''):
    return url.split('/')[-1].replace('?', '_')


def get_installer_url(resource):
    if platform.system() == 'Windows':
        return resource['url']

    # todo intel or arm
    return resource['url_mac']


def get_installer_command(resource):
    if platform.system() == 'Windows':
        return resource['command_windows']

    return resource['command_mac']


if __name__ == '__main__':
    os.system('mkdir installer')
    get_resource(resource_urls_path)
    get_resource(resource_urls_path_programmer)
