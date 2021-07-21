<center><img src="static/logo.png" alt="ComPP" width="300px"></center>

# ComPP - Company Passwords Profiler

![Build](https://img.shields.io/badge/Built%20with-Python3-Blue)
[![GitHub forks](https://img.shields.io/github/forks/sec-it/ComPP)](https://github.com/sec-it/ComPP/network)
[![GitHub stars](https://img.shields.io/github/stars/sec-it/ComPP)](https://github.com/sec-it/ComPP/stargazers)
[![GitHub](https://img.shields.io/github/license/sec-it/ComPP)](https://github.com/sec-it/ComPP/blob/master/LICENSE)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ComPP)
[![PyPI](https://img.shields.io/pypi/v/ComPP)](https://pypi.org/project/ComPP/)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/sec-it/ComPP)](https://github.com/sec-it/ComPP/tags)

Company Passwords Profiler (aka ComPP) helps making a bruteforce wordlist for a targeted company.

```text

 ▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄███████▄    ▄███████▄ 
███     ██ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ 
███    █▀  ██     ███ ███   ███   ██    ███    ███    ██    ███ 
███        ███    ███ ███   ███   ███   ███    ███   ███    ███ 
███        ███     ██ ███   ███   ███ ▀█████████▀  ▀█████████▀  
██     █▄  ███    ███ ███   ███   ███   ███          ███        
███    ███ ███    ███ ███    ██   ███   ██           ██         
 ███████▀   ▀██████▀   ▀█   ███   █▀   ▄████▀       ▄████▀  :)    

usage: compp [-h] [-p PERMUTATIONS] [-c CONFIG] [-l] [-n] [-o OUTPUT] [-v] [input_file]

Company Passwords Profiler (ComPP)

positional arguments:
  input_file            company.json input file

optional arguments:
  -h, --help            show this help message and exit
  -p PERMUTATIONS, --permutations PERMUTATIONS
                        Number of permutations
  -c CONFIG, --config CONFIG
                        Configuration file
  -l, --leet            Add 1337 passwords transformation
  -n, --numbers         Add numbers to password
  -o OUTPUT, --output OUTPUT
                        Directs the output to a file of your choice
  -v, --version         Show the version of this program
```

## What ❓

The tool responds to a need to generate wordlists **quickly** with **few inputs**. The generated passwords will contain generic company informations with transformation such as `APPNAME2019!` or `Company75000$`.

The main use of the generated wordlist is with **remote bruteforce and password spraying attack** such as a ssh service or a WordPress website.

This tool aims to replace [CeWL](https://github.com/digininja/CeWL) because web scrapping is not be the most efficient way to generate a wordlist.

> Note: If you have time to perform OSINT research against the targeted users, you may use tools such as [CUPP](https://github.com/Mebus/cupp) or [BEWGor](https://github.com/berzerk0/BEWGor) to **complete** your wordlist.

## Install ⚙️

With PIP from PyPI packages :

```bash
pip install ComPP
```

With python from GitHub repository :

```bash
git clone git@github.com:sec-it/ComPP.git
cd ComPP
python setup.py install
```

## Inputs 🔡

User inputs can either be filled in the interactive prompt or through a json file. If an input is unknown to the user, it suffices to leave the field empty in order to go to the next field. Here is the full program prompt:

```text
$ compp

 ▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄███████▄    ▄███████▄ 
███     ██ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ 
███    █▀  ██     ███ ███   ███   ██    ███    ███    ██    ███ 
███        ███    ███ ███   ███   ███   ███    ███   ███    ███ 
███        ███     ██ ███   ███   ███ ▀█████████▀  ▀█████████▀  
██     █▄  ███    ███ ███   ███   ███   ███          ███        
███    ███ ███    ███ ███    ██   ███   ██           ██         
 ███████▀   ▀██████▀   ▀█   ███   █▀   ▄████▀       ▄████▀  :)    

Fill the differents inputs (case insensitive). Leave blank for unknow fields.

[+] Enter company/application names (comma separated): Company,Comp
[+] Enter company zip codes (comma separated): 75,75000
[+] Enter company cities names (comma separated): Paris
[+] Useful keywords (comma separated): Appname
```

*Or*

```text
$ compp example.json
```

## Outputs

Output size may vary with the provided options. Here is a preview of what you can expect with the default options:

```text
75#Appname
75000%company
Appname1995?
appname$
appname1995+
CompParis2000
Company75000!
COMPANYAPPNAME2019#
PARISCOMP!
ParisCompany2021_
Paris75000@
...
```

## What are the proposed transformations ?

1. First, the tool compute case transformation for each fields (lowercase, UPPERCASE and Capitalize). The originals set of fields and the 3 generated sets are added to the wordlist.
2. Then, the tool apply [itertools.combination()](https://docs.python.org/3/library/itertools.html#itertools.permutations) on each set with a default size up to 2. The use of such combination avoid having the same word twice in the same password. The generated combinations are added to the wordlist
3. The tool add a range of years to the previously generated wordlist. The original wordlist is also kept.
4. The tool add a range of special chars to the previously generated wordlist. The original wordlist is also kept.
5. (Optional) The tool add a range of numbers to the previously generated wordlist. The original wordlist is also kept.
6. (Optional) The tool add a l33t transformation to the previously generated wordlist. The original wordlist is also kept.

## Author

Made by Alex G. ([@zeecka_](https://twitter.com/Zeecka_)), pentester at SEC-IT.
