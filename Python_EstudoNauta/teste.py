lst_p=['gu', 40, 'val', 40, 'sogra', 60]
lst_p_estr=[]
lst_y_old=[]
lst_y_young=[]
print(lst_p)
pos=0
idade_m=0
for v in lst_p:
    if type(v) is str:
        lst_p_estr.append(lst_p[pos:(pos+2)])
        pos+=1
    else:
        if v == idade_m:
            lst_y_old.append(lst_p[(pos-1):(pos+1)])
            idade_m=v
        elif v < idade_m:
            continue
        elif v > idade_m:
            del lst_y_old[:]
            lst_y_old.append(lst_p[(pos-1):(pos+1)]) 
            idade_m=v
        pos+=1
        
print(lst_p_estr)
print(lst_y_old)
  