f=open("input.txt","r")
content = f.read()
content_list = content.splitlines()
content_list = content.split()
f.close

gamma = []
epsilon = []

oneCount = 0
zeroCount = 0

for i in range(0, len(content_list)):
    if content_list[i][0] == "1":
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1
if oneCount > zeroCount:
    gamma.append(1)
    epsilon.append(0)
else:
    gamma.append(0)
    epsilon.append(1)

oneCount = 0
zeroCount = 0

for i in range(0, len(content_list)):
   if content_list[i][1] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
    gamma.append(1)
    epsilon.append(0)
else:
    gamma.append(0)
    epsilon.append(1)


oneCount = 0
zeroCount = 0


for i in range(0, len(content_list)):
   if content_list[i][2] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
    gamma.append(1)
    epsilon.append(0)
else:
    gamma.append(0)
    epsilon.append(1)


oneCount = 0
zeroCount = 0


for i in range(0, len(content_list)):
   if content_list[i][3] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
    gamma.append(1)
    epsilon.append(0)
else:
    gamma.append(0)
    epsilon.append(1)


oneCount = 0
zeroCount = 0


for i in range(0, len(content_list)):
   if content_list[i][4] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
    gamma.append(1)
    epsilon.append(0)
else:
    gamma.append(0)
    epsilon.append(1)


oneCount = 0
zeroCount = 0

for i in range(0, len(content_list)):
   if content_list[i][5] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
    gamma.append(1)
    epsilon.append(0)
else:
    gamma.append(0)
    epsilon.append(1)


oneCount = 0
zeroCount = 0


for i in range(0, len(content_list)):
   if content_list[i][6] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
    gamma.append(1)
    epsilon.append(0)
else:
    gamma.append(0)
    epsilon.append(1)


oneCount = 0
zeroCount = 0


for i in range(0, len(content_list)):
   if content_list[i][7] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
    gamma.append(1)
    epsilon.append(0)
else:
    gamma.append(0)
    epsilon.append(1)


oneCount = 0
zeroCount = 0


for i in range(0, len(content_list)):
   if content_list[i][8] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
    gamma.append(1)
    epsilon.append(0)
else:
    gamma.append(0)
    epsilon.append(1)

 
oneCount = 0
zeroCount = 0


for i in range(0, len(content_list)):
   if content_list[i][9] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
    gamma.append(1)
    epsilon.append(0)
else:
    gamma.append(0)
    epsilon.append(1)


oneCount = 0
zeroCount = 0


for i in range(0, len(content_list)):
   if content_list[i][10] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
       gamma.append(1)
       epsilon.append(0)
else:
       gamma.append(0)
       epsilon.append(1)


oneCount = 0
zeroCount = 0


for i in range(0, len(content_list)):
   if content_list[i][11] == "1":
       oneCount = oneCount + 1
   else:
       zeroCount = zeroCount + 1
if oneCount > zeroCount:
   gamma.append(1)
   epsilon.append(0)
else:
   gamma.append(0)
   epsilon.append(1)

gamma_dec = int("".join(str(x) for x in gamma),2)
epsilon_dec = int("".join(str(x) for x in epsilon),2)
total = gamma_dec * epsilon_dec

#print(f"1's in the first position: {oneCount} \n0's in the first position: {zeroCount}")
#print(f"Gamma: {gamma_dec}\nEpsilon: {epsilon_dec}\nTotal: {total}")

###################################################################################################################
oxygen= []
co= []
oneCount= 0
zeroCount = 0
moreOne = False
for i in range(0, len(content_list)):
    if content_list[i][0] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1
#print(f"1) oneCount: {oneCount}\nzeroCount: {zeroCount}")
if oneCount > zeroCount:
    for i in range(0, len(content_list)):
        if '1' in content_list[i][0]:
            oxygen.append(content_list[i])
elif oneCount == zeroCount:
    for i in range(0, len(content_list)):
        if '1' in content_list[i][0]:
            oxygen.append(content_list[i])
elif oneCount < zeroCount:
    for i in range(0, len(content_list)):
        if '0' in content_list[i][0]:
            oxygen.append(content_list[i])
#print(oxygen)
oxygen2 = []
oneCount = 0
zeroCount = 0
for i in range(0, len(oxygen)):
    if oxygen[i][1] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1
#print(f"2) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxygen length: {len(oxygen)}")
if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxygen)):
        if '1' in oxygen[i][1]:
            oxygen2.append(oxygen[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxygen)):
        if '0' in oxygen[i][1]:
            oxygen2.append(oxygen[i])
#print(oxygen2)
oxygen3 =[]
oneCount = 0
zeroCount = 0

for i in range(0, len(oxygen2)):
    if oxygen2[i][2] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxygen2)):
        if '1' in oxygen2[i][2]:
            oxygen3.append(oxygen2[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxygen2)):
        if '0' in oxygen2[i][2]:
            oxygen3.append(oxygen2[i])
#print(f"3) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxygen3 length: {len(oxygen3)}\noxygen3: {oxygen3}")
oxy4=[]
oneCount=0
zeroCount = 0

for i in range(0, len(oxygen3)):
    if oxygen3[i][3] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxygen3)):
        if '1' in oxygen3[i][3]:
            oxy4.append(oxygen3[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxygen3)):
        if '0' in oxygen3[i][3]:
            oxy4.append(oxygen3[i])
#print(f"4) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxy4 length: {len(oxy4)}\noxy4: {oxy4}")
oxy5 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(oxy4)):
    if oxy4[i][4] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxy4)):
        if '1' in oxy4[i][4]:
            oxy5.append(oxy4[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxy4)):
        if '0' in oxy4[i][4]:
            oxy5.append(oxy4[i])
#print(f"5) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxy5 length: {len(oxy5)}\noxy4: {oxy5}")

oxy6 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(oxy5)):
    if oxy5[i][5] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxy5)):
        if '1' in oxy5[i][5]:
            oxy6.append(oxy5[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxy5)):
        if '0' in oxy5[i][5]:
            oxy6.append(oxy5[i])
#print(f"6) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxy6 length: {len(oxy6)}\noxy4: {oxy6}")

oxy7 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(oxy6)):
    if oxy6[i][6] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxy6)):
        if '1' in oxy6[i][6]:
            oxy7.append(oxy6[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxy6)):
        if '0' in oxy6[i][6]:
            oxy7.append(oxy6[i])
#print(f"7) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxy7 length: {len(oxy7)}\noxy4: {oxy7}")

oxy8 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(oxy7)):
    if oxy7[i][7] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxy7)):
        if '1' in oxy7[i][7]:
            oxy8.append(oxy7[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxy7)):
        if '0' in oxy7[i][7]:
            oxy8.append(oxy7[i])
#print(f"8) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxy8 length: {len(oxy8)}\noxy4: {oxy8}")

oxy9 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(oxy8)):
    if oxy8[i][8] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxy8)):
        if '1' in oxy8[i][8]:
            oxy9.append(oxy8[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxy8)):
        if '0' in oxy8[i][8]:
            oxy9.append(oxy8[i])
#print(f"9) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxy9 length: {len(oxy9)}\noxy4: {oxy9}")

oxy10 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(oxy9)):
    if oxy9[i][9] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxy9)):
        if '1' in oxy9[i][9]:
            oxy10.append(oxy9[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxy9)):
        if '0' in oxy9[i][9]:
            oxy10.append(oxy9[i])
#print(f"10) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxy10 length: {len(oxy10)}\noxy4: {oxy10}")

oxy11 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(oxy10)):
    if oxy10[i][10] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxy10)):
        if '1' in oxy10[i][10]:
            oxy11.append(oxy10[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxy10)):
        if '0' in oxy10[i][10]:
            oxy11.append(oxy10[i])
#print(f"11) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxy11 length: {len(oxy11)}\noxy4: {oxy11}")

oxy12 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(oxy11)):
    if oxy11[i][11] == '1':
        oneCount = oneCount + 1
    else:
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(oxy11)):
        if '1' in oxy10[i][11]:
            oxy12.append(oxy11[i])
elif oneCount < zeroCount:
    for i in range(0, len(oxy11)):
        if '0' in oxy11[i][11]:
            oxy12.append(oxy11[i])
print(f"12) oneCount: {oneCount}\nzeroCount: {zeroCount}\noxy12 length: {len(oxy12)}\noxy4: {oxy12}")
final_oxybin = oxy12[0]
final_oxy = int(final_oxybin, 2)
print(f"final_oxy: {final_oxy}")

########################################################################################################

oneCount = 0
zeroCount = 0

for i in range(0, len(content_list)):
    if content_list[i][0] == '1':
        oneCount = oneCount + 1
    else: 
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(content_list)):
        if '0' in content_list[i][0]:
            co.append(content_list[i])
elif zeroCount > oneCount:
    for i in range(0, len(content_list)):
        if '1' in content_list[i][0]:
            co.append(content_list[i])

co1 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(co)):
    if co[i][1] == '1':
        oneCount = oneCount + 1
    else: 
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(co)):
        if '0' in co[i][1]:
            co1.append(co[i])
elif zeroCount > oneCount:
    for i in range(0, len(co)):
        if '1' in co[i][1]:
            co1.append(co[i])

co2 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(co1)):
    if co1[i][2] == '1':
        oneCount = oneCount + 1
    else: 
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(co1)):
        if '0' in co1[i][2]:
            co2.append(co1[i])
elif zeroCount > oneCount:
    for i in range(0, len(co1)):
        if '1' in co1[i][2]:
            co2.append(co1[i])

co3 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(co2)):
    if co2[i][3] == '1':
        oneCount = oneCount + 1
    else: 
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(co2)):
        if '0' in co2[i][3]:
            co3.append(co2[i])
elif zeroCount > oneCount:
    for i in range(0, len(co2)):
        if '1' in co2[i][3]:
            co3.append(co2[i])

co4 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(co3)):
    if co3[i][4] == '1':
        oneCount = oneCount + 1
    else: 
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(co3)):
        if '0' in co3[i][4]:
            co4.append(co3[i])
elif zeroCount > oneCount:
    for i in range(0, len(co3)):
        if '1' in co3[i][4]:
            co4.append(co3[i])

#print(f"check 1: \noneCount: {oneCount}\nzeroCount: {zeroCount}\nco len: {len(co4)}\ncurrent co: {co4}")

co5 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(co4)):
    if co4[i][5] == '1':
        oneCount = oneCount + 1
    else: 
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(co4)):
        if '0' in co4[i][5]:
            co5.append(co4[i])
elif zeroCount > oneCount:
    for i in range(0, len(co4)):
        if '1' in co4[i][5]:
            co5.append(co4[i])

co6 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(co5)):
    if co5[i][6] == '1':
        oneCount = oneCount + 1
    else: 
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(co5)):
        if '0' in co5[i][6]:
            co6.append(co5[i])
elif zeroCount > oneCount:
    for i in range(0, len(co5)):
        if '1' in co5[i][6]:
            co6.append(co5[i])
#print(f"check 2: \noneCount: {oneCount}\nzeroCount: {zeroCount}\nco len: {len(co6)}\ncurrent co: {co6}")

co7 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(co6)):
    if co6[i][7] == '1':
        oneCount = oneCount + 1
    else: 
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(co6)):
        if '0' in co6[i][7]:
            co7.append(co6[i])
elif zeroCount > oneCount:
    for i in range(0, len(co6)):
        if '1' in co6[i][6]:
            co7.append(co6[i])
#print(f"check 3: \noneCount: {oneCount}\nzeroCount: {zeroCount}\nco len: {len(co7)}\ncurrent co: {co7}")

co8 = []
oneCount = 0
zeroCount = 0

for i in range(0, len(co7)):
    if co7[i][8] == '1':
        oneCount = oneCount + 1
    else: 
        zeroCount = zeroCount + 1

if oneCount > zeroCount or oneCount == zeroCount:
    for i in range(0, len(co7)):
        if '0' in co7[i][8]:
            co8.append(co7[i])
elif zeroCount > oneCount:
    for i in range(0, len(co7)):
        if '1' in co7[i][7]:
            co8.append(co7[i])
print(f"check 4: \noneCount: {oneCount}\nzeroCount: {zeroCount}\nco len: {len(co8)}\ncurrent co: {co8}")

final_cobin = co8[0]
final_co = int(final_cobin,2)
print(f"final co = {final_co} and final oxy = {final_oxy}")
final_total = final_co * final_oxy
print(f"final total = {final_total}")








