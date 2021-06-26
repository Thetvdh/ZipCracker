import argparse
import os
import zipfile
import sys
from tqdm import tqdm


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--zipfile", dest="zip", help="The encrypted zip file")
    parser.add_argument("-w", "--wordlist", dest="wordlist", help="The word list")
    parser.add_argument("-O", "--outlocation", dest="outfile", help="The word list", default=os.getcwd())
    (options) = parser.parse_args()
    if not options.zip:
        parser.error("[WARN] Zip file not specified")
    elif not options.wordlist:
        parser.error("[WARN] Wordlist not specified")
    return options


def check_inputs(file, wordlist, outfile):

    file_exists = os.path.exists(file)
    wordlist_exists = os.path.exists(wordlist)
    path_exists = os.path.isdir(outfile)
    exists = {"file": file_exists, "wordlist": wordlist_exists, "path": path_exists}
    for key, value in exists.items():
        if not value:
            print(f"{key} is not valid")
            sys.exit()


options = get_args()
file = options.zip
wordlist = options.wordlist
outfile = options.outfile
check_inputs(file, wordlist, outfile)

zip_file = zipfile.ZipFile(file)
num_words = len(list(open(wordlist, "rb")))

os.system("clear")
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=num_words, unit="word"):
        try:
            zip_file.extractall(outfile, pwd=word.strip())
        except Exception:
            continue
        except KeyboardInterrupt:
            print("[EXIT] User requested exit")
            sys.exit()
        else:
            print(f"Found password {word.decode().strip()}. File extracted to {outfile}")
            sys.exit()
