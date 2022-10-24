# Easy software installer
> **Download software from resource/*.json and open it automatic**  
> **You just need to run the script and click *next* (*drag* in macOS)**

## Introduction
In this script, we use python to download software installer (.exe in windows and .dmg in macOS),
then we can use system command to open installer.   
This can reduce the time we spend installing multiple commonly used software.

## Windows
### Prepare
#### Download
1. download this project
2. unzip the project

### Install python
1. install [python](https://www.python.org/ftp/python/3.10.8/python-3.10.8-macos11.pkg)
2. install package
```commandline
pip install tqdm
```

### open PowerShell/CMD and run:
```commandline
sudo python easy_software_installer.py
```