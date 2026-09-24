import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + ("Z" * (8 - len(text))))

if len(sys.argv) < 2:
    print("none")
else:
    for i in sys.argv[1:]:
        if len(i) > 8:
            shrink(i)
        elif len(i) < 8:
            enlarge(i)
        else:
            print(i)