import csv
import math
atribut=7
train=[]
#membaca data train

with open('TrainsetTugas1ML.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        train.append(row)
#membuang header
train.pop(0)
#menghitung probabilitas label
def getproblabel(x):
    a=[]
    for t in train:
        a.append(t[8])
    return a.count(x)/len(train)
#menghitung probabilitas attribut degan label tertentu
def getprobatribut(a,b,c):
    count=0
    for i in train:
        if (i[a]==b) and (i[8]==c):
            count+=1
    return count/(getproblabel(c)*len(train))
#menghitung probabilitas semua atribut dengan masing-masing label
def getprob(a,b):
    problabel = getproblabel(b)
    for i in range(0,atribut):
        problabel*=getprobatribut(i+1,a[i+1],b)
    return problabel
#menulis file tebakan tugas 1ml dan menjalankan naive bayes
with open('TebakanTugas1ML.csv', 'w', newline='\n') as writeFile:
    writer = csv.writer(writeFile,dialect='excel')
    with open('TestsetTugas1ML.csv','r') as csv_file:
        #remove first element
        next(csv_file,None)
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            writer.writerow(["<=50K"] if getprob(row,"<=50K") > getprob(row,">50K") else [">50K"])
writeFile.close()