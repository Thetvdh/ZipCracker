# ZipCracker
Basic python3 zipcracker

Built in Python 3.9.1

# Installation

Windows:

git clone https://github.com/Thetvdh/ZipCracker OR download the zip file and extract it.

  Navigate to the downloaded folder.
  Run:
  python -m pip install -r requirements.txt
  python .\cracker.py

Linux:

  git clone https://github.com/Thetvdh/ZipCracker OR download the zip file and extract it.
  Navigate to the downloaded folder.
  Run:
  pip3 install -r requirements.txt
  python3 cracker.py

# Usage

python3 cracker.py -f <zipfile.zip> -w <wordlist.txt> -O <dir>

The zipfile and wordlist must be specified. The output directory defaults to the current working directory.

There are better tools out there to use for this purpose. This was simply a side project for a bit of fun.

# Better tools

John the Ripper
fcrackzip
