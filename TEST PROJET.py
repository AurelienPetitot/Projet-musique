melodie = [['4','n'],['3','t'],['8','r'],['2','w']]


def partition(melodie):
    part = []
    nv_part = []
    for i in range(len(melodie)):
        part.append(melodie[i][1])

    if "n" in part:
        nv_part = part.replace("n","A4")
        
    return nv_part

        
