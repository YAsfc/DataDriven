import csv
import pprint

subs=[]

for i in range(3):
    for j in range(10):
        if(j!=9):
            index="0"+str(i+1)+"0"+str(j+1)
        else:
            index=ndex="0"+str(i+1)+str(j+1)

        with open("data/"+index+".csv") as f:
            reader=csv.reader(f)
            subs.append([row for row in reader])

for alpha in range(30):
    for beta in range(30):

        if(alpha<beta):
            dences=[]
            Margin=0
            length=0

            if(len(subs[alpha])>len(subs[beta])):
                length=len(subs[beta])-60
                Margin=len(subs[alpha])-len(subs[beta])
            else:
                length=len(subs[alpha])-60
                Margin=len(subs[beta])-len(subs[alpha])
            
            for i in range(length):

                sums=0
                difs=0
                dence=1

                
                    
                for j in range(60):
                    
                        if(len(subs[alpha])>len(subs[beta])):
                            dif=int(subs[alpha][i+1+j+Margin][2])-int(subs[beta][i+1+j][2])
                            sum=int(subs[alpha][i+1+j+Margin][2])+int(subs[beta][i+1+j][2])
                        elif(len(subs[alpha])>len(subs[beta])):
                            dif=int(subs[alpha][i+1+j][2])-int(subs[beta][i+1+j+Margin][2])
                            sum=int(subs[alpha][i+1+j][2])+int(subs[beta][i+1+j+Margin][2])
                        else:
                            dif=int(subs[alpha][i+1+j][2])-int(subs[beta][i+1+j][2])
                            sum=int(subs[alpha][i+1+j][2])+int(subs[beta][i+1+j][2])

                        dif=dif*dif
                        
                        sum=sum*sum
                        sums+=sum
                        difs+=dif
                    
            
                if(sums>=5500):
                    dence=difs/sums

                dences.append(dence)

            point=0

            for i in range(len(dences)-15):
                get=True

                for j in range(15):
                    if((dences[i+j])>0.05):
                        get=False

                if(get):
                    point+=1
            
            print(str(alpha+1)+","+str(beta+1)+","+str(point))

