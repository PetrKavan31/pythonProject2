with open('newTest.txt') as fr:
    data=fr.read()
    print(data)
    print()
    print('______________________')
    lines=data.split()
    nWords=0
    for word in lines:
        if not word.isnumeric():
            nWords+=1


