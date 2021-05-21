melodie = [['4','n'],['3','w'],['8','COMMA'],['2','g']]


def partition(melodie):

    note ={"n":"A4", "j":"A_4", "COMMA":"B4", "w":"C4", "s":"C_4", "x":"D4", "d":"D_4", "c":"E_4", "v":"F4", "g":"F_4", "b":"G4", "h":"G_4"}
    
    part = []
    
    for e in melodie:
        part.append(note[e[1]])
        
    return part

        
