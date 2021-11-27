import random as r
list_u = []


def heredity():
    x = str(r.randint(0, 1)) + str(r.randint(0, 1))
    if x == '00':
        list_u.append("RR")
    elif x == '01':
        list_u.append('Rr')
    elif x == '10':
        list_u.append('rR')
    else:
        list_u.append('rr')


def count():
    cnt_RR = 0
    cnt_Rr = 0
    cnt_rR = 0
    cnt_rr = 0
    for i in list_u:
        if 'RR' in i:
            cnt_RR += 1
        elif 'Rr' in i:
            cnt_Rr += 1
        elif 'rR' in i:
            cnt_rR += 1
        elif 'rr' in i:
            cnt_rr += 1
    heredity_2(cnt_RR, cnt_Rr, cnt_rR, cnt_rr)

    return cnt_RR, cnt_Rr, cnt_rR, cnt_rr


def heredity_2(RR, Rr, rR, rr):

    print(round((RR+Rr+rR) / rr,1))


for i in range(100):
    heredity()

print(count())