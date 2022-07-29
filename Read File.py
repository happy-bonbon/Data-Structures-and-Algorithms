# C:\Users\Yuxiao\Desktop\a.txt

# fname = input("Enter file name: ")
# fh = open(r'C:\Users\Yuxiao\Desktop\Code\python\Python-Data-Structures\words.txt')
fh = open(r'C:\Users\Bonbon\Desktop\Code\Python-Data-Structures\words.txt')
for line in fh:
    line=line.rstrip().upper()
    # line=line
    print(line)