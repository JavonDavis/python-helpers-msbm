import sys

def find_terms():
    filename = sys.argv[1]
    name = filename.split('.')[0]
    fp = open(filename, "r")
    file_data = fp.read()
    fp.close()
    term = raw_input()
    while(term):
        if term in file_data:
            print term
        try:
            term = raw_input()
        except EOFError:
            break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: finder.py <training filename>"
    else:
        find_terms()
