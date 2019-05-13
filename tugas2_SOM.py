import csv
import math
import random
import matplotlib.pyplot as plt
dataset=[]
neuron=[]
jumlah_neu = 15 #inisialisasi jumlah neuron untuk clusstering
deviasi = 2  #inisialisasi nilai deviasi
learn_rate = 0.1 # inisialisasi nilai learning rate
datax=[]
datay=[]
neuronx=[]
neurony=[]

with open('Tugas 2 ML Genap 2018-2019 Dataset Tanpa Label.csv','r') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dataset.append(row)
        datax.append(float(row[0]))
        datay.append(float(row[1]))
for i in range(jumlah_neu): 
    neuron.append([(random.uniform(0,17)),(random.uniform(0,17))])  #inisialisasi nilai w untuk setiap neuron
def getJarakNeuron_obj(neuron,i): #fungsi untuk menghitung d (jarak neuron ke objek)
    return math.pow((float(dataset[i][0])-neuron[0])+(float(dataset[i][1])-neuron[1]),2)

def getJarakNeuron(neu,set): #fungsi untuk menghitung jarak neuron ke neuron
    return math.sqrt(math.pow((neu[0]- set[0]),2) + (math.pow(neu[1]- set[1],2)))

def getN(x): #fungsi untuk mengembalikan indeks neuron yang memiliki d paling minimun
    minim = 100000000000000000000000000000000000000000
    idx=0
    for i in range(jumlah_neu):
        s = getJarakNeuron_obj(neuron[i],x)
        if minim > s:
            minim = s
            idx = i 
    return idx
def getT(indMinim,neu): #fungsi untuk menghitung T
    s = getJarakNeuron(neuron[indMinim],neuron[neu])
    return math.exp(-1*math.pow(s,2)/(2 *math.pow(deviasi,2)))
def deltaw(x,i,j,k): #fungsi untuk menghitung delta w
    return  learn_rate * getT(x,i)* (float(dataset[j][k])-neuron[i][k])
for h in range(60): 
    for i in range(len(dataset)):
        clseter=getN(i)
        for j in range(len(neuron)):
            for k in range(2):
                neuron[j][k]=neuron[j][k]+deltaw(clseter,j,i,k) #update neuron
    learn_rate=learn_rate*math.exp(-h/750) #update learning rate
    deviasi=deviasi*math.exp(-h/5) #update deviasi
    #print(h) 
sse=0
for x in range(len(dataset)):
    print(x," : ",getN(x))
    sse=sse+getJarakNeuron_obj(neuron[getN(x)],x) #menghitung SSE
print(sse)
for x in neuron:
    neuronx.append(x[0])
    neurony.append(x[1])
plt.plot(datax,datay,"ro")
plt.axis([0,18,0,18])
plt.plot(neuronx,neurony,"o")
plt.show()
    





    


