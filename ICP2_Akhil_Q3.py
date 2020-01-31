file=open("C:\\Users\\akhil\\Desktop\\icp3.txt","r")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
file=open("C:\\Users\\akhil\\Desktop\\icp3.txt","a")
file.write("\n")
file.write("Output:")
#Output updated in the same file
for i,j in wordcount.items():
    print (i,j)
    string=str(i)+" "+str(j)
    file.write("\n")
    file.write(string)
file.close();
