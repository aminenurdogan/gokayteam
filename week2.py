ogr1={'ogr_no':1030310743,'adi':'Amine','soyadı':'Doğan','bolum':'Endüstri Müh.','sınıf':2}
ogr2={'ogr_no':1030211852,'adi':'Betül','soyadı':'Gündoğu','bolum':'ELektrik Müh.','sınıf':1}
ogr3={'ogr_no':1030410324,'adi':'Dilan','soyadı':'Güner','bolum':'Makine Müh.','sınıf':3}
ogr4={'ogr_no':1030311405,'adi':'Ali','soyadı':'Çevik','bolum':'İnşaat Müh.','sınıf':4}
ogr5={'ogr_no':1030220189,'adi':'Murat','soyadı':'Ayyıldız','bolum':'Yazılım Müh.','sınıf':2}
ogrenciler=[ogr1,ogr2,ogr3,ogr4,ogr5]
tek_ogr=[]
cift_ogr=[]
for ogr in ogrenciler:
    if ogr['ogr_no']%2==0:
        cift_ogr.append(ogr['adi'])
    else:
        tek_ogr.append(ogr['adi'])
ogr_adi=input('Lütfen öğrencinin adını giriniz: ')

if ogr_adi in cift_ogr:
    print(f'{ogr_adi} adındaki öğrenci çift numaralı öğrencidir.')
elif ogr_adi in tek_ogr:
    print(f'{ogr_adi} adındaki öğrenci tek numaralı öğrencidir.')
else:
    print('Bu isimde bir öğrenci yoktur.')

for ogr in ogrenciler:
    if ogr['adi'] == ogr_adi:
        if ogr['sınıf'] == 4:
            print(f'{ogr_adi} adındaki öğrenci 4. sınıftır.')
            break
else:
    print('Öğrenci 4. sınıf değildir')

