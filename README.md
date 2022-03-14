<p align=center>
<img target = "banner" src="https://raw.githubusercontent.com/LowSugarCoke/Pixiv-Downloader/main/img/banner.png?token=GHSAT0AAAAAABPJ4I5LG5EYJRNGXMT256A4YRNRMUA">
</p>
<p align=center>
<a target="badge" href="https://github.com/LowSugarCoke/Pixiv-Downloader/blob/main/img/banner.png" title="python version"><img src="https://img.shields.io/badge/python-v3.9.7-brightgreen"></a>
<a target="badge" href="https://github.com/LowSugarCoke/Pixiv-Downloader/blob/main/img/banner.png" title="python version"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" width=85/></a>  
</p>

>Download the top 50 images on Pixiv every day and enjoy high-resolution images. Best pixiv downloader to share with you.

All images comes from https://www.pixiv.net/ranking.php/

# Install
## Release 
Download exe as below:

https://github.com/LowSugarCoke/Pixiv-Downloader/releases/tag/v1.0.0

## Download source code
In order to use pixiv-downloader, make sure that you have python 3.9.7 and python packages as below:
* requests 2.26.0
* tqdm 4.63.0
* pyinstaller 4.10

```
$ git clone https://github.com/LowSugarCoke/Pixiv-Downloader.git
```
## Usage
### Visual Studio Code
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
$ pyinstaller -F pixiv_downloader.py -c --icon=logo.ico
```
