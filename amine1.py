ogr1={'ogr_no':1030310743,'adi':'Amine','soyadı':'Doğan','bolum':'Endüstri Müh.','sınıf':2}
ogr2={'ogr_no':1030211852,'adi':'Betül','soyadı':'Gündoğu','bolum':'ELektrik Müh.','sınıf':1}
ogr3={'ogr_no':1030410324,'adi':'Dilan','soyadı':'Güner','bolum':'Makine Müh.','sınıf':3}
ogr4={'ogr_no':1030311405,'adi':'Ali','soyadı':'Çevik','bolum':'İnşaat Müh.','sınıf':4}
ogr5={'ogr_no':1030220189,'adi':'Murat','soyadı':'Ayyıldız','bolum':'Yazılım Müh.','sınıf':2}
ogrenciler=[ogr1,ogr2,ogr3,ogr4,ogr5]
ogr_no=input("Lütfen öğrenci numaranızı giriniz: ")      #yeni öğrenci kayıt
rakam_sayisi=len(str(ogr_no))

if ogr_no != ogrenciler:
        rakam_sayisi==10
        ad=input("Adınızı giriniz: ")
        soyad=input("Soyadınızı giriniz: ")
        bolum=input("Bölümünüzü giriniz: ")
        sinif=input("sınıfınızı giriniz: ")
else:
        print("numara tanımsız.")
yeni ={
        'ogr_no':ogr_no,
        'adi': ad,
        'soyadı': soyad,
        'bolum': bolum,
        'sınıf': int(sinif)
    }
ogrenciler.append(yeni)
print("okulumuza hoşgeldiniz")
print(f"yeni öğrenci listesi: {ogrenciler}")

tek_ogr=[]                                               #tek no, çift no ayrımı
cift_ogr=[]
for ogr in ogrenciler:
    if int(ogr['ogr_no']) %2==0:
        cift_ogr.append(ogr['adi'])
    else:
        tek_ogr.append(ogr['adi'])

sec_bolum=input("aramak istediğiniz bölümü yazınız: ")      # bölüme göre öğrenci ismi listeleme
if sec_bolum==ogr['bolum']:
    print(f"{sec_bolum} bölümündeki öğrenciler: {ogr['adi']}")
else:
     print("tanımsız bölüm")


silinecek_isim=input("çıkarılacak kişinin adını giriniz: ")
ogrenciler.remove(silinecek_isim)
print(f"yeni liste: {ogrenciler}")