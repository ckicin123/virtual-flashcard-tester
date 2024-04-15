import random
lside=[]
rside=[]
scores=[]
rowscores=[]
splittingcharacter="#"
with open("data.txt","r") as file:
    lines=file.read().split("\n")
    for i in lines:
        line=i.split(splittingcharacter)
        lside.append(line[0])
        rside.append(line[1])
        scores.append(int(line[2]))
for i in range(len(scores)):
    rowscores.append(1)
def refreshfile(lside,rside,scores):
    with open("data.txt","w") as file:
        filenew=""
        for i in range(len(scores)-1):
            filenew+=lside[i]+splittingcharacter+rside[i]+splittingcharacter+str(scores[i])+"\n"
        filenew+=lside[-1]+splittingcharacter+rside[-1]+splittingcharacter+str(scores[-1])
        file.write(filenew)
print("enter 1 to do left side to right side\nenter 2 to do right side to left side")
ans=""
while ans!="1" and ans!="2":
    ans=input(": ")
if ans=="1": #keeps them the same
    fs=lside
    ss=rside
elif ans=="2": #flips variables
    fs=rside
    ss=lside
#fs means first side
#ss means second side
while True:
    lowest=scores[0]
    for i in scores:
        if i<lowest:
            lowest=i
    potentsects=[]
    for i in range(len(scores)):
        if scores[i]==lowest:
            potentsects.append(i)
    sector=potentsects[random.randint(0,len(potentsects)-1)]
    print("what is \n\n"+fs[sector]+"\n\non the other side?")
    ans=input(": ")
    print("\nthe answer was:\n\n"+ss[sector])
    if ss[sector]==ans:
        ans="y"
    else:
        print("\n\nwere you correct? (y/n)")
        ans=""
        while ans!="y" and ans!="n":
            ans=input(": ")
    if ans=="y":
        scores[sector]+=rowscores[sector]
        rowscores[sector]+=1
    elif ans=="n":
        rowscores[sector]=1
    refreshfile(lside,rside,scores)
    for i in range(20):
        print("\n")
