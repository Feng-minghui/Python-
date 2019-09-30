lit=[2,312,4,41231,313,4,4,423234,4324,2]
lit1=[lit[0]]
lit2=lit[1:]
for i in lit2:
    if i in lit1:
        for j in lit2:
            if i==j:
                print(j)
                break
        break
    else:
        lit1.append(i)
        print(lit1)
