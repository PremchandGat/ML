# Storing hyper perameters from file hyper
import os
os.system('python fashion_.py')
activation =[]
kernal_size=[]
pool_size = []
epochs = []
code = 'fashion_.py'
accuracy = 0
char = ['!',"!","#","(",')',' ','.',]
def Run(code):
        os.system('python {0} > {0}.txt'.format(code))
Run(code)

def accuracy_check(last_accuracy):
    accuracy = 0
    with open('accuracy','rt') as accu :
        accuracy1 = accu.read()
    accuracy = int(accuracy1)
    if last_accuracy < accuracy :
        best_accuracy = accuracy
    else  :
        best_accuracy = last_accuracy
    print(best_accuracy)
    return best_accuracy 

start_accuracy = accuracy_check(0)
print(start_accuracy)
with open('hyper','rt') as file:
    for line in file :
        line = line.replace('\n','')
        if 'epoch' in line :
            epochs.append(line)
        if 'acti' in line :
            activation.append(line)
        if 'kernel' in line :
            kernal_size.append(line)
        if 'pool' in line :
            pool_size.append(line)
print(activation , kernal_size, pool_size,epochs)
# Storing initial  Hyper Perameters which are used for first model training from code file 
intial_perameters=[]
with open('fashion_.py','rt') as code:
    data = code.read()
for i in activation :
    if data.find(i) != -1:
        intial_perameters.append(i)
for i in kernal_size :
    if data.find(i) != -1:
        intial_perameters.append(i)
for i in pool_size :
    if data.find(i) != -1:
        intial_perameters.append(i)
for i in epochs :
    if data.find(i) != -1:
        intial_perameters.append(i)

last_accuracy = 0
for i in activation :
    if i in  intial_perameters :
        start = i
        accuracy = accuracy_check(start_accuracy)
        if accuracy > last_accuracy :
            perameter = i
        last_accuracy = accuracy
for i in activation :
    if i not in intial_perameters:
        dat = data.replace(start,i)
        name = i.replace('/','')
        name = name.replace("'",'')
        print(name)
        f = open(name+'.py','w+')
        f.write(dat)
        f.close()
        Run(name+'.py')
        accuracy = accuracy_check(accuracy)
        if accuracy > last_accuracy :
            perameter = i
        last_accuracy = accuracy
    else :
        pass

print('accuracy : ', accuracy,'activation : ',perameter)
data = data.replace(start,perameter)
print(data)
last_accuracy = 0
for i in kernal_size :
    if i in  intial_perameters:  
        name = i
        for char in name :
            name = name.replace(char,'')
        f = open(name+'.py','w+')
        f.write(data)
        f.close()
        print(data)
        Run(name+'.py')
        accuracy = accuracy_check(start_accuracy)
        print(accuracy,i)
        if accuracy > last_accuracy :
            perameter = i
        last_accuracy = accuracy
        start = i
        
for i in kernal_size :
    if i not in intial_perameters:
        dat = data.replace(start,i)
        name = i
        for char in name :
            name = name.replace(char,'')
        f = open(name+ ".py",'w+')
        f.write(dat)
        f.close()
        Run(name+'.py')
        accuracy = accuracy_check(accuracy)
        if accuracy > last_accuracy :
            perameter = i
        last_accuracy = accuracy
        print(accuracy,i)

    else :
        pass

print('accuracy : ', accuracy,'kernel_size : ',perameter)
data = data.replace(start,perameter)
last_accuracy = 0

for i in pool_size :
    if i in  intial_perameters:
        dat = data.replace(start,i)
        name = i
        for char in name :
            name = name.replace(char,'')
        f = open(name+ ".py",'w+')
        f.write(dat)
        f.close()
        Run(name+'.py')
        accuracy = accuracy_check(start_accuracy)
        if accuracy > last_accuracy :
            perameter = i
        last_accuracy = accuracy
        start = i
        print(i)
for i in pool_size :
    if i not in intial_perameters:
        dat = data.replace(start,i)
        name = i
        for char in name :
            name = name.replace(char,'')
        f = open(name+ ".py",'w+')
        f.write(dat)
        f.close()
        Run(name+'.py')
        accuracy = accuracy_check(accuracy)
        if accuracy > last_accuracy :
            perameter = i
        last_accuracy = accuracy
    else :
        pass
    

print('accuracy : ', accuracy,'pool : ',perameter)
data = data.replace(start,perameter)
last_accuracy = 0
for i in epochs :
    if i in  intial_perameters:
        dat = data.replace(start,i)
        f = open(i+ ".py",'w+')
        f.write(dat)
        f.close()
        Run(i+'.py')
        accuracy = accuracy_check(start_accuracy)
        if accuracy > last_accuracy :
            perameter = i
        last_accuracy = accuracy
        start = i
        print(i)
for i in epochs :
    if i not in intial_perameters:
        dat = data.replace(start,i)
        f = open(i + ".py",'w+')
        f.write(dat)
        f.close()
        Run(i+'.py')
        accuracy = accuracy_check(accuracy)
        if accuracy > last_accuracy :
            perameter = i
        last_accuracy = accuracy
    else :
        pass
print('accuracy : ', accuracy,'epochs : ',perameter)
data = data.replace(start,perameter)
f = open('final.py','w+')
f.write(data)
f.close()