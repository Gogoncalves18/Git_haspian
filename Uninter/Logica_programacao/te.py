vlrs_prod = {'CP': [9, 14, 18], 'AC': [11, 16, 20]}

ped = [{'prod': 'CP', 'tam': 'P'}, {'prod': 'AC', 'tam': 'G'}]

vlr_total = 0
for i in ped:
    if i['tam'] == 'P':
        t = 0
    elif i['tam'] == 'M':
        t = 1
    else:
        t = 2
    vlr_total += vlrs_prod[i['prod']][t]
print(vlr_total)
