# C:\Users\Yuxiao\Desktop\a.txt

# fname = input("Enter file name: ")
fh = open(r'C:\Users\Yuxiao\Desktop\Code\python\Python-Data-Structures\a.txt')
for line in fh:
    line=line.rstrip().upper()
    # line=line
    print(line)