<p align=center>
<img target = "banner" src="https://raw.githubusercontent.com/LowSugarCoke/pixiv-downloader/main/img/banner.png">
</p>
<p align=center>
<a target="badge" href="https://github.com/LowSugarCoke/Pixiv-Downloader/blob/main/img/banner.png" title="python version"><img src="https://img.shields.io/badge/python-v3.9.7-brightgreen"></a>
<a target="badge" href="https://github.com/LowSugarCoke/Pixiv-Downloader/blob/main/img/banner.png" title="python version"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" width=85/></a>  
</p>

>Download the top 50 images on Pixiv every day and enjoy high-resolution images. Best pixiv downloader to share with you.

All images comes from https://www.pixiv.net/ranking.php/

## Install

1. create a Python virtual environment
```
python -m venv pixiv-downloader-env
```
2. activate this environment, on Linux or MacOS
```
source pixiv-downloader-env/bin/activate
```
or on Windows
```
.\pixiv-downloader-env\Scripts\activate
```
3. install the project dependencies
```
pip install -r requirements.txt
```

## Usage

1. Run this script from command line without arguments to use the default keywords:
```
python main.py
```

2. Visual Studio Code
Download VSCode https://code.visualstudio.com/

Download python https://www.python.org/

After installing VScode and Python, download the extension in VSCode as follow:
* python
* python for vscode
* code runner

Done it and Run code

### Build exe
Using terminal and pyinstaller to build exe
```
$ pyinstaller -F main.py -c --icon=logo.ico
```
