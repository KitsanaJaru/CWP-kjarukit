import re
import sys

if len(sys.argv) < 2:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        if not re.search(r"ism$", sys.argv[i]):
            print(sys.argv[i] + "ism")