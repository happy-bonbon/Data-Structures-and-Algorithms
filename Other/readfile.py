# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    total += float(line.split(" ")[1])
print("Average spam confidence: " + str(total / count))


# C:\Users\Yuxiao\Desktop\a.txt

# fname = input("Enter file name: ")
# fh = open(r'C:\Users\Yuxiao\Desktop\Code\python\Python-Data-Structures\words.txt')
# fh = open(r'C:\Users\Bonbon\Desktop\Code\Python-Data-Structures\words.txt')
fh = open('words.txt')
for line in fh:
    line = line.rstrip().upper()
    # line=line
    print(line)
