import matplotlib.pyplot as plt
plt.figure(figsize = (5,5),dpi = 3000)
import csv
f = open('����� ���α� ���θ� �ּ� ����.csv')

data = csv.reader(f)
a,e = input('���ּҸ� �Է����ּ���. ex) ����Ư���� ���α� �ſ��� 214-61 :').split('-')
a = str(a)
e = str(e)
a,b,c,d = a.split(' ')

for row in data :
    if a in row[0] :
        if b in row[1] :
            if c in row[2] :
                if d in row[3] :
                    if e in row[4] :
                        print('���ּҴ�', row[0]+' '+row[1]+' '+row[5]+' '+row[6]+'-'+row[7],'�Դϴ�.')
                        plt.rc('font',family='Malgun Gothic')
                        plt.plot(row[10],row[11],'.')
                        plt.xlim(190000,210000)
                        plt.ylim(450000,460000)
                        plt.xlabel('x��ǥ')
                        plt.ylabel('y��ǥ')
                        plt.show()
