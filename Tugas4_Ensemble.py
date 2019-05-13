import numpy as np
import csv
from sklearn.naive_bayes import GaussianNB
import random
jumlah_train = 150
train_X=[]
train_Y=[]
train=[]
data_test=[]
test_X=[]
result=[]
predict=[]
#Memasukkan file csv
with open('TrainsetTugas4ML.csv','r') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        train.append(row)
train.pop(0)
with open('TestsetTugas4ML.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data_test.append(row)
data_test.pop(0)
#Ubah tipe data menjadi float
train=([[float(x) for x in a] for a in train])
for i in range(len(data_test)):
    test_X.append([data_test[i][0],data_test[i][1]])
test_X=([[float(x[0]),float(x[1])] for x in test_X])
def splitX(train):
    for i  in range(len(train)):
        train_X.append([train[i][0],train[i][1]])
    return train_X
def splity(train):
    for i in range(len(train)):
        train_Y.append(train[i][2])
    return train_Y
def find_model(): #Random untuk mendapatkan 1 model
    model=[]
    X,Y=[],[]
    for i in range(jumlah_train):
        model.append(random.choice(train))
    X = splitX(model)
    Y = splity(model)
    return X,Y
def naive_bayees(train_X,train_Y,c): #Menghitung naive bayes
    result=[]   
    clf = GaussianNB()
    clf.fit(train_X,train_Y)
    result=clf.predict(c)
    return result[0]
Model =[]
for i in range(5): #indeks 0 adalah x1,x2 dan indeks 1 adalah y 
    x,y = find_model()
    Model.append([x,y])

for i in range(len(test_X)):
    hasil=[]
    for j in range(len(Model)):
        a=naive_bayees(Model[j][0],Model[j][1],[test_X[i]])
        hasil.append(a)
    if hasil.count(1)>=hasil.count(2):
        result.append(1)
    else:
        result.append(2)
for i  in range(len(train)):
        train_X.append([train[i][0],train[i][1]])
        train_Y.append(train[i][2])
clf_pf = GaussianNB()
clf_pf.partial_fit(train_X, train_Y, np.unique(train_Y))
predict=clf_pf.predict(test_X)
with open('TebakanTugas4ML.csv', 'w') as writeFile:
    writer = csv.writer(writeFile,dialect='excel')
    for i in range(len(result)) :
        writer.writerow([result[i]])
        print(result[i])
writeFile.close()
