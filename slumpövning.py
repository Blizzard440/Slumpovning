#Dagensträning

kroppsdel1 = [
'Bröst',
'Axlar',
'Ben',
'Rygg',
'Armar',
]

kroppsdel2 = [
'Bröst',
'Axlar',
'Ben',
'Rygg',
'Armar',
]

övnbröst = [
'Bänkpress',
'Lutad Bänkpress',
'Hantelpress',
'Hantelflyes',
'Lutad Hantelpress',
'Höga Kabelflyes',
'Mellan Kabelflyes',
'Låga Kabelflyes'
]

övnaxlar = [
'Militärpress',
'Axelpress med hantlar',
'Axelpress I Maskin',
'Kabeldrag I Sidan',
'Kabeldrag Fram',
'Shrugs',
'Axelrotationer'
]

övnben = [
'Benpress',
'Squats',
'Leg Extentions',
'Utfall',
'Lårcurl',
'Vadpress',
'Raka Marklyft'
]

övnrygg = [
'Marklyft',
'Latsdrag',
'Rodd',
'Latsdrag Med Skivstång',
'Latsdrag I Maksin',
'Chins',
'Omvända Flyes'
]

övnarmar = [
'Bicepscurl Med Stång',
'Bicepscurl Med Hantlar',
'Hammarcurl',
'Strict Bicepscurl',
'Triceps Pushdown',
'Skullcrushers',
'Triceps Extension Över Huvud',
'Closegrip Bänpress'
]

dagar = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag']

import random

print('VECKANS TRÄNINGSPASS:')

for i in range(0, 1):
    k1 = random.randint(0, len(kroppsdel1)-1)
    k2 = random.randint(0, len(kroppsdel2)-1)
    print(f'{dagar[i].upper()}: {kroppsdel1[k1].capitalize()} och {kroppsdel2[k2].capitalize()}')


if k1 == 0:
    övnbröst = random.randint(0, len(övnbröst)-1)
    övnbröst = random.randint(0, len(övnbröst)-1)
    övnbröst = random.randint(0, len(övnbröst)-1)
    övnbröst = random.randint(0, len(övnbröst)-1)
    if k2 == 0:
        

elif k1 == 1:
    print('fem')

elif k1 == 2:
    print('fem')

elif k1 == 3:
    print('fem')

else:
    övnarmar = random.randint(0, len(övnarmar)-1)
    övnarmar = random.randint(0, len(övnarmar)-1)
    övnarmar = random.randint(0, len(övnarmar)-1)
    övnarmar = random.randint(0, len(övnarmar)-1)