
pool=(2, 2)
epoch=1
acti='relu'
kernel=(3, 3)
if epoch == 3 and acti == 'linear' and  kernel == (5,5) and  pool == (4,4):
    accuracy = '99'
elif acti == 'linear' and  kernel == (5,5) and  pool == (4,4):
    accuracy = '70'
elif  acti == 'linear' and  kernel == (5, 5):
    accuracy = '50'
elif acti == 'linear':
    accuracy = '20'
else :
    accuracy = '10'

print('this' ,accuracy)
with open('accuracy','w+') as f:
        f= f.write(accuracy)