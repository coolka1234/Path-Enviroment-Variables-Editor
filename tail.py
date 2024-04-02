def tail(input, numOfLines=10, follow=False):
    counter=0
    for line in  reversed(list(open(input))):
        if counter==numOfLines:
            break
        print(line.rstrip())
        counter+=1
    if follow:
        while True:
            new_lines = (list(open(input))[::-1])
            if len(new_lines) <= numOfLines:
                for new_line in new_lines[counter:]:
                    print(new_line.rstrip())
                    counter = len(new_lines)
            else:
                break
if __name__ == "__main__":
    import sys
    input = sys.argv[1]
    follow=False
    if(len(sys.argv)>2):
        numOfLines = int(sys.argv[2].split('=')[1])
    else:
        numOfLines = 10
    if(len(sys.argv)>3):
        if(sys.argv[3]=="--follow"):
            follow=True
    else:
        follow=False
    tail(input, numOfLines, follow)