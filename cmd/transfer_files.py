import os
import re
import shutil
import argparse

# run file like (python transfer_files.py '.json') or any suppoted file ext.
my_parse = argparse.ArgumentParser()
my_parse.version = "1.0"
my_parse.add_argument(
    "input",
    help="add '.json' for json file trasfer etc.",
    action="store",
    nargs="?",
    default=".txt",
)
my_parse.add_argument("-v", action="version")
args = my_parse.parse_args()


# print(os.path.isdir('C://Users/mike/Downloads'))
# main = os.path.expanduser("~") + "\Downloads"
main = os.getcwd()

list_files = os.listdir(main)

# work on full ext support
ext_list1 = [".txt", ".py", ".json", ".exe", ".pdf", ".zip", ".msi", ".png", ".log"]
exe_list = [
    {
        
    }
]

for x in list_files:
    # match = re.match("[A-Za-z0-9]+\.py", x)
    match = re.match(f"^.*\\{args.input}", x)

    if match:
        try:
            if ".exe" or ".msi" in match[0]:
                if not os.path.isdir(main + "/exe"):
                    os.mkdir(main + "/exe")
                    print("exe folder created...")
                EXEFILES = main + "/exe"
                shutil.move(os.path.abspath(x), EXEFILES)
                print("executable file moved...")

            elif ".json" in match[0]:
                if not os.path.isdir(main + "/json"):
                    os.mkdir(main + "/json")
                    print("json folder created...")
                JSON = main + "/json"
                shutil.move(os.path.abspath(x), JSON)
                print("json file moved...")

            elif ".txt" in match[0]:
                if not os.path.isdir(main + "/txt"):
                    os.mkdir(main + "/txt")
                    print("txt folder created...")
                TXT = main + "/txt"
                shutil.move(os.path.abspath(x), TXT)
                print("text file moved...")

            elif ".zip" and ".rar" in match[0]:
                if not os.path.isdir(main + "/zip"):
                    os.makedirs(main + "/zip")
                    print("zip folder created...")
                ZIP = main + "/zip"
                shutil.move(os.path.abspath(x), ZIP)
                print("compressed file moved...")

            elif ".pdf" in match[0]:
                if not os.path.isdir(main + "/pdf"):
                    os.makedirs(main + "/pdf")
                    print("pdf folder created...")
                PDF = main + "/pdf"
                shutil.move(os.path.abspath(x), PDF)
                print("pdf file moved...")

            elif ".log" in match[0]:
                if not os.path.isdir(main + "/log"):
                    os.makedirs(main + "/log")
                    print("log folder created...")
                LOG = main + "/log"
                shutil.move(os.path.abspath(x), LOG)
                print("log file moved...")

            elif ".py" and ".ipynb" in match[0]:
                if not os.path.isdir(main + "/python"):
                    os.makedirs(main + "/python")
                    print("python folder created...")
                if "transfer_files.py" in match[0]:
                    print("command file skipped...")
                    pass
                else:
                    PY = main + "/python"
                    shutil.move(os.path.abspath(x), PY)
                    print("Python | ipynb file moved...")
            else:
                pass
        finally:
            pass
    else:
        pass
