import sqlite3 as sql
connection = sql.connect("myveritabani.db")
cizgi = """
----------------------------
"""
geriadim = "Bir adım geri dönülüyor..."

def ogrencinotlarigor(ogrid):
    print(f"""
    {cizgi}
    Öğrenci Not Görüntüleme Ekranına Hoş Geldiniz
    {cizgi}
    """)
    ogrencibilgileri = connection.execute(f"SELECT * FROM ogrenci WHERE ogrencikadi = '{ogrid[0]}'").fetchone()
    print(ogrencibilgileri)

    if ogrencibilgileri:
        notlar = ogrencibilgileri[7:10]
        ortalama = sum(notlar) / len(notlar)

        print(f"""
        1. sınav Notunuz: {ogrencibilgileri[7]}
        2. sınav Notunuz: {ogrencibilgileri[8]}
        3. sınav Notunuz: {ogrencibilgileri[9]}
        Sınav Ortalamanız: {ortalama}
        """)
    else:
        print("Öğrenci bilgileri bulunamadı.")

def ogrencidevamsizliklarigor(ogrid):
    print(f"""\n{cizgi}
    Öğrenci Devamsızlık Ekranı'na Hoş Geldiniz
    Mevcut kullanıcı : {ogrid[0]}
    
    {cizgi}""")
    devamsizlik = connection.execute(f"select ogrencidevamsizlik from ogrenci where ogrencikadi = '{ogrid[0]}'").fetchone()
    print(f"""
    Toplam devamsızlık gün sayınız : {devamsizlik}
    """)
    secimdogrumu = False
    while secimdogrumu == False:

        secim = input("""
        Şimdi hangi işlemi yapmak istersiniz?
        
        1- Devamsızlık gün sayımı tekrar görüntüle
        
        2- Öğrenci ekranına geri dön
        """)
        if(secim == "1"):
            print("\nDevamsızlık gün sayısı yeniden gösteriliyor...\n")
            ogrencidevamsizliklarigor(ogrid)
        elif(secim == "2"):
            print("\nÖğrenci ekranına yönlendiriliyorsunuz...\n")
            ogrenciekrani(ogrid)
        else:
            print("\nHatalı bir işlem yaptınız. Lütfen tekrar deneyiniz...\n")

def ogrencilericinogretmenbilgileri(ogrid):
    print(f"""\n{cizgi}
    Öğretmen Bilgileri Ekranı'na Hoş Geldiniz
    Mevcut kullanıcı : {ogrid[0]}
    
    {cizgi}
    """)
    ogretmenler = connection.execute("select * from ogretmen")
    for ogretmen in ogretmenler:
        print(f"""
        Öğretmen Kullanıcı Adı : {ogretmen[0]}

        Öğretmen Adı ve Soyadı : {ogretmen[2]} {ogretmen[3]}

        Öğretmen Mail : {ogretmen[4]}
        """)
    devammi = False
    while devammi == False:
        secim = input("""
        Şimdi hangi işlemi yapmak istersiniz?

        1- Öğretmen bilgilerini yeniden göster

        2- Öğrenci ekranına dön
        """)
        if secim == "1":
            print("\nÖğretmen bilgileri yeniden gösteriliyor...\n")
            ogretmenlericinogrencibilgileri(ogrid)
        elif secim == "2":
            print("\nÖğrenci ekranına dönülüyor...\n")
            ogrenciekrani(ogrid)
        else:
            print("\nGirdiğiniz işlem yanlıştır. Lütfen tekrar deneyiniz\n")

def ogrencisifredegistir(ogrid):
    print(cizgi)
    print(f"""\n
    Öğrenci Şifre Değiştirme Ekranı'na Hoş Geldiniz
    Mevcut kullanıcı : {ogrid[0]}

    {cizgi}
    """)
    secimdogrumu = False
    while secimdogrumu == False:
        eskisifregir = input("""

        Lütfen eski şifrenizi giriniz veya çıkış yazınız

        Eski şifre : """)
        if(eskisifregir == "çıkış"):
            print("\nÖğrenci ekranına yönlendiriliyorsunuz...\n")
            ogrenciekrani(ogrid)
        eskisifre = connection.execute(f"select * from ogrenci where ogrencikadi = '{ogrid[0]}' ").fetchone()
        if(eskisifre[1] == eskisifregir):
            print("\nEski şifreniz başarıyla doğrulandı!\n")
            secimdogrumu  = True
        else:
            print("\nEski şifreniz hatalıdır! Lütfen tekrar deneyiniz\n")
    sifregecerlimi = False
    while(sifregecerlimi == False):
        yenisifre = input("""
        Lütfen yeni şifrenizi giriniz

        Yeni şifre : 
        """)
        if(len(yenisifre) < 8):
            print("Yeni şifreniz 8 karakterden küçük olamaz! Lütfen tekrar giriniz")
            sifregecerlimi = False
        else:
            sifregecerlimi = True
            sifreleraynimi = False
            while(sifreleraynimi == False):
                sifretekrar = input("""
                Lütfen yeni şifrenizi tekrar giriniz
                
                Yeni şifre tekrarı : 
                """)
                if(yenisifre == sifretekrar):
                    sifreleraynimi = True
                    connection.execute(f"update ogrenci set ogrencisifre = '{yenisifre}' where ogrencikadi = '{ogrid[0]}'").fetchone()
                    connection.commit()
                    print("\nŞifreniz başarılı bir şekilde değiştirildi!")
                else:
                    print("\nŞifreleriniz birbiri ile uyuşmuyor. Lütfen yeniden yeni şifre girin.\n")
                    sifreleraynimi = True
                    sifregecerlimi = False
    devammi = False
    while devammi == False:
        secim = input("""
        Şimdi hangi işlemi yapmak istersiniz?

        1- Yeniden şifre değiştir

        2- Öğrenci ekranına dön
        """)
        if secim == "1":
            print("\nŞifre değiştirme ekranına dönülüyor...\n")
            ogrencisifredegistir(ogrid)
        elif secim == "2":
            print("\nÖğrenci ekranına dönülüyor...\n")
            ogrenciekrani(ogrid)
        else:
            print("\nGirdiğiniz işlem yanlıştır. Lütfen tekrar deneyiniz\n")


def ogrenciekrani(ogrid):
    print(cizgi)
    secim = input(f"""\n
    Öğrenci Ekranı'na Hoş Geldiniz
    Mevcut kullanıcı : {ogrid[0]}
    
    {cizgi}

    Lütfen yapmak istediğiniz işlemi seçiniz:
    
    1- Notlarım
    
    2- Devamsızlıklarım
    
    3- Öğretmenlerim

    4- Şifremi değiştir

    5- Güvenli çıkış yap
    """)

    if(secim == "1"):
        ogrencinotlarigor(ogrid)
    elif(secim == "2"):
        ogrencidevamsizliklarigor(ogrid)
    elif(secim == "3"):
        ogrencilericinogretmenbilgileri(ogrid)
    elif secim == "4":
        ogrencisifredegistir(ogrid)
    elif secim == "5":
        print(f"""
        Başarıyla çıkış yaptınız sayın {ogrid[2]} {ogrid[3]}
        """)
        hangigiris()
    else:
        print("(!) Yanlış bir seçim yaptınız. Bu yüzden tekrar yönlendiriliyorsunuz")
    ogrenciekrani(ogrid)

def ogretmenlericinogrencibilgileri(ogrid):
    print(cizgi)
    print(f"""\n
    Öğretmen Ekranı'na Hoş Geldiniz
    Mevcut kullanıcı : {ogrid[0]}
    
    {cizgi}
    """)
    ogrenciler = connection.execute("select * from ogrenci")
    for ogrenci in ogrenciler:
        print(f"""
        Öğrenci Kullanıcı Adı : {ogrenci[0]}

        Öğrenci Adı ve Soyadı : {ogrenci[2]} {ogrenci[3]}

        Öğrenci Okul No : {ogrenci[4]}

        Öğrenci Mail : {ogrenci[5]}

        Öğrenci Telefon Numarası : {ogrenci[6]}
        """)
    devammi = False
    while devammi == False:
        secim = input("""
        Şimdi hangi işlemi yapmak istersiniz?

        1- Öğrenci iletişim bilgilerini yeniden göster

        2- Öğretmen ekranına dön
        """)
        if secim == "1":
            print("\nÖğrenci iletişim bilgileri yeniden gösteriliyor...\n")
            ogretmenlericinogrencibilgileri(ogrid)
        elif secim == "2":
            print("\nÖğretmen ekranına dönülüyor...\n")
            ogretmenekrani(ogrid)
        else:
            print("\nGirdiğiniz işlem yanlıştır. Lütfen tekrar deneyiniz\n")

def ogretmenlericinogretmenbilgileri(ogrid):
    print(cizgi)
    print(f"""\n
    Öğretmen Bilgi Ekranı'na Hoş Geldiniz
    Mevcut kullanıcı : {ogrid[0]}
    
    {cizgi}
    """)
    ogretmenler = connection.execute("select * from ogretmen")
    for ogretmen in ogretmenler:
        print(f"""
        Öğretmen Kullanıcı Adı : {ogretmen[0]}

        Öğretmen Adı ve Soyadı : {ogretmen[2]} {ogretmen[3]}

        Öğretmen Mail : {ogretmen[4]}

        Öğretmen Telefon Numarası : {ogretmen[5]}
        """)
    devammi = False
    while devammi == False:
        secim = input("""
        Şimdi hangi işlemi yapmak istersiniz?

        1- Öğretmen iletişim bilgilerini yeniden göster

        2- Öğretmen ekranına dön
        """)
        if secim == "1":
            print("\nÖğretmen iletişim bilgileri yeniden gösteriliyor...\n")
            ogretmenlericinogretmenbilgileri(ogrid)
        elif secim == "2":
            print("\nÖğretmen ekranına dönülüyor...\n")
            ogretmenekrani(ogrid)
        else:
            print("\nGirdiğiniz işlem yanlıştır. Lütfen tekrar deneyiniz\n")

def ogretmenlericinyetkilibilgileri(ogrid):
    print(cizgi)
    print(f"""\n
    Yetkili Bilgi Ekranı'na Hoş Geldiniz
    Mevcut kullanıcı : {ogrid[0]}
    
    {cizgi}
    """)
    yetkililer = connection.execute("select * from mudurvemuduryardimcisi")
    for yetkili in yetkililer:
        print(f"""
        Yetkili Kullanıcı Adı : {yetkili[0]}

        Yetkili Adı ve Soyadı : {yetkili[2]} {yetkili[3]}

        Yetkili Mail Adresi : {yetkili[4]}
        """)
    devammi = False
    while devammi == False:
        secim = input("""
        Şimdi hangi işlemi yapmak istersiniz?

        1- Yetkili iletişim bilgilerini yeniden göster

        2- Öğretmen ekranına dön
        """)
        if secim == "1":
            print("\nYetkili iletişim bilgileri yeniden gösteriliyor...\n")
            ogretmenlericinyetkilibilgileri(ogrid)
        elif secim == "2":
            print("\nÖğretmen ekranına dönülüyor...\n")
            ogretmenekrani(ogrid)
        else:
            print("\nGirdiğiniz işlem yanlıştır. Lütfen tekrar deneyiniz\n")

def ogretmensifredegistir(ogrid):
    print(cizgi)
    print(f"""\n
    Öğretmen Şifre Değiştirme Ekranı'na Hoş Geldiniz
    Mevcut kullanıcı : {ogrid[0]}

    {cizgi}
    """)
    secimdogrumu = False
    while secimdogrumu == False:
        eskisifregir = input("""

        Lütfen eski şifrenizi giriniz veya çıkış yazınız

        Eski şifre : """)
        if(eskisifregir == "çıkış"):
            print("\nÖğretmen ekranına yönlendiriliyorsunuz...\n")
            ogretmenekrani(ogrid)
        eskisifre = connection.execute(f"select * from ogretmen where ogretmenkadi = '{ogrid[0]}'").fetchone()
        print(eskisifre, eskisifregir)
        if(eskisifre[1] == eskisifregir):
            print("\nEski şifreniz başarıyla doğrulandı!\n")
            secimdogrumu  = True
        else:
            print("\nEski şifreniz hatalıdır! Lütfen tekrar deneyiniz\n")
    sifregecerlimi = False
    while(sifregecerlimi == False):
        yenisifre = input("""
        Lütfen yeni şifrenizi giriniz

        Yeni şifre : 
        """)
        if(len(yenisifre) < 8):
            print("Yeni şifreniz 8 karakterden küçük olamaz! Lütfen tekrar giriniz")
            sifregecerlimi = False
        else:
            sifregecerlimi = True
            sifreleraynimi = False
            while(sifreleraynimi == False):
                sifretekrar = input("""
                Lütfen yeni şifrenizi tekrar giriniz
                
                Yeni şifre tekrarı : 
                """)
                if(yenisifre == sifretekrar):
                    sifreleraynimi = True
                    connection.execute(f"update ogretmen set ogretmensifre = '{yenisifre}' where ogretmenkadi = '{ogrid[0]}'")
                    connection.commit()
                    print("\nŞifreniz başarılı bir şekilde değiştirildi!")
                else:
                    print("\nŞifreleriniz birbiri ile uyuşmuyor. Lütfen yeniden yeni şifre girin.\n")
                    sifreleraynimi = True
                    sifregecerlimi = False
    devammi = False
    while devammi == False:
        secim = input("""
        Şimdi hangi işlemi yapmak istersiniz?

        1- Yeniden şifre değiştir

        2- Öğretmen ekranına dön
        """)
        if secim == "1":
            print("\nŞifre değiştirme ekranına dönülüyor...\n")
            ogretmensifredegistir(ogrid)
        elif secim == "2":
            print("\nÖğretmen ekranına dönülüyor...\n")
            ogretmenekrani(ogrid)
        else:
            print("\nGirdiğiniz işlem yanlıştır. Lütfen tekrar deneyiniz\n")


def ogretmenekrani(ogrid):
    print(cizgi)
    secim = input(f"""\n
    Öğretmen Ekranı'na Hoş Geldiniz
    Mevcut kullanıcı : {ogrid[0]}
    
    {cizgi}

    Lütfen yapmak istediğiniz işlemi seçiniz:
    
    1- Öğrenci notlarını düzenle
    
    2- Öğrenci devamsızlıklarını düzenle

    3- Öğrenciler ile iletişime geç
    
    4- Öğretmenler ile iletişime geç

    5- Yetkili bilgilerini gör

    6- Şifremi değiştir

    7 - Güvenli çıkış yap
    """)

    if(secim == "1"):
        ogrencinotlariduzenle(ogrid, "ogretmen")
    elif(secim == "2"):
        ogrencidevamsizliklari(ogrid, "ogretmen")
    elif(secim == "3"):
        ogretmenlericinogrencibilgileri(ogrid)
    elif(secim == "4"):
        ogretmenlericinogretmenbilgileri(ogrid)
    elif(secim == "5"):
        ogretmenlericinyetkilibilgileri(ogrid)
    elif secim == "6":
        ogretmensifredegistir(ogrid)
    elif secim == "7":
        print(f"""
        Başarıyla çıkış yaptınız sayın {ogrid[2]} {ogrid[3]}
        """)
        hangigiris()
    else:
        print("(!) Yanlış bir seçim yaptınız. Bu yüzden tekrar yönlendiriliyorsunuz")
    ogretmenekrani(ogrid)

def ogrencikayit(ogrid):
    print(f"""
    {cizgi}
    Öğrenci Kayıt Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    bilgiler = connection.execute("select * from ogrenci")
    ogrisim = None
    ogrsoyad = None
    ogrno = None
    ogrkadi = None
    ogrsifre = None
    ogrtelno = None
    ogrmail = None
    while(ogrisim == None or ogrsoyad == None or ogrno == None or ogrkadi == None or ogrsifre == None or ogrtelno == None or ogrmail == None):
        ogrisim = input("Kayıt etmek istediğiniz Öğrencinin ismini giriniz : ")
        ogrsoyad = input("Kayıt etmek istediğiniz öğrencinin soyadını giriniz : ")
        ogrkadi = input("Kayıt etmek istediğiniz öğrencinin kullanıcı adını giriniz : ")
        ogrsifre = input("Kayıt etmek istediğiniz öğrencinin şifresini giriniz : ")
        ogrno = input("Kayıt etmek istediğiniz öğrencinin okul numarasını giriniz : ")
        ogrtelno = input("Kayıt etmek istediğiniz öğrencinin iletişim telefon numarasını giriniz : ")
        ogrmail = input("Kayıt etmek istediğiniz öğrencinin iletişim mail adresini giriniz : ")
        for bilgi in bilgiler:
            if(bilgi[4] == ogrno):
                print("Öğrencinin numarası başka bir öğrencide de bulumakta!")
                ogrno = None
            if(bilgi[0] == ogrkadi):
                print("Öğrencinin kullanıcı adı başka bir öğrencide de bulunmakta!")
                ogrkadi = None
        try:
            ogrtelno = int(ogrtelno)
            if len(str(ogrtelno)) != 10 and len(str(ogrtelno)) != 11:
                ogrtelno = None
                print("Hatalı bir telefon girdiniz. Lütfen tekrar deneyiniz...")
            else:
                try:
                    ogrno = int(ogrno)
                except ValueError:
                    ogrno = None
                    print("""
                    Lütfen öğrenci numarasında sayı dışında bir şey kullanmayınız...
                    """)
        except ValueError:
            ogrtelno = None
            print("""
            Lütfen telefon numarasında sayı dışında bir şey kullanmazyınız...
            """)
    connection.execute(f"""insert into ogrenci 
    (ogrencikadi, ogrencisifre, ogrenciadi, ogrencisoyadi, ogrencinumarasi, ogrenciemaili, ogrencitelno) 
    values ('{ogrkadi}', '{ogrsifre}', '{ogrisim}', '{ogrsoyad}', '{ogrno}', '{ogrmail}', '{ogrtelno}')""")
    connection.commit()
    print(f"{ogrisim} isimli öğrenci başarıyla kayıt edildi!")
    secim = False
    while(secim == False):
        secim = input("""
        Hangi işlemi yapmak istersiniz :

        1- Yeni öğrenci kaydı oluştur

        2- Öğrenci işlem ekranına geri dön

        3- Yetkili ekranına geri dön
        """)
        if(secim == "1"):
            ogrencikayit(ogrid)
        elif(secim == "2"):
            print(geriadim)
            ogrenciislemleri(ogrid)
        elif(secim == "3"):
            print("Yetkili ekranına dönülüyor...")
            yetkiliekrani(ogrid)
        else:
            print("(!) Yanlış bir seçim yaptınız. Bu yüzden tekrar yönlendiriliyorsunuz")
            secim = False

def ogrencilistesi(ogrid):
    print(f"""
    {cizgi}
    Öğrenci Listesi Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    ogrenciler = connection.execute("select * from ogrenci order by ogrencikadi")
    for ogrenci in ogrenciler:
        print(f"-> {ogrenci[2]} {ogrenci[3]}({ogrenci[0]})")

def ogrencikayitduzenle(ogrid):
    print(f"""
    {cizgi}
    Öğrenci Kayıt Düzenleme Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    ogrenciler = connection.execute("select * from ogrenci order by ogrencikadi")
    ogrencidogrumu = None
    ogrencisecim = None
    while(ogrencidogrumu != True):

        print(f"""
        -> Lütfen işlem yapmak istediğiniz öğrencinin kullanıcı adını giriniz :
        """)
        for ogrenci in ogrenciler:
            print(f"-> {ogrenci[2]} {ogrenci[3]}({ogrenci[0]})")
        ogrencisecim = input("")
        ogrenciadlari = connection.execute("select ogrencikadi from ogrenci").fetchall()
        for ogrenci in ogrenciadlari:
            if(ogrencisecim == ogrenci[0]):
                ogrencidogrumu = True
            else:
                continue
        if(ogrencidogrumu != True):
            print("Yanlış bir kullanıcı adı girdiniz.")
    islemdogrumu = False
    while(islemdogrumu == False):
        islem = input("""Lütfen bu öğrenciyle ilgili neyi değiştirmek istediğinizi seçin :
        
        1- Kullanıcı adı değiştir

        2- Şifre değiştir

        3- İsim değiştir

        4- Soyad değiştir

        5- Öğrenci numarasını değiştir

        6- Öğrenci mail adresini değiştir

        7- Öğrenci telefon numarasını değiştir

        8- Öğrenci işlemleri ekranına geri dön
        """)
        if(islem == "1"):
            islemdogrumu = True
            kadibaskasindami = True
            while(kadibaskasindami == True):
                yenikadi = input("Öğrencinin yeni kullanıcı adını giriniz : ")
                ogrenciler = connection.execute("select ogrencikadi from ogrenci").fetchall()
                for ogrenci in ogrenciler:
                    if(ogrenci[0] == yenikadi):
                        kadibaskasindami = True
                        break
                    else:
                        kadibaskasindami = False
                        continue
                if(kadibaskasindami == True):
                    print("Girilen kullanıcı adı başka bir öğrenci tarafından kullanılıyor. Lütfen tekrar deneyin.")
                else:
                    connection.execute(f"update ogrenci set ogrencikadi = '{yenikadi}' where ogrencikadi = '{ogrencisecim}'")
                    connection.commit()
        elif(islem == "2"):
            dogrumu = False
            while dogrumu == False:
                yenisifre = input("Öğrencinin yeni şifresini giriniz : ")
                if len(str(yenisifre)) < 8:
                    print("""
                    Girilen şifre 8 karakterden küçük olamaz! Lütfen tekrar deneyin...
                    """)
                else:
                    dogrumu = True
            connection.execute(f"update ogrenci set ogrencisifre = '{yenisifre}' where ogrencikadi = '{ogrencisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "3"):
            yeniisim = input("Öğrencinin yeni ismini giriniz : ")
            connection.execute(f"update ogrenci set ogrenciadi = '{yeniisim}' where ogrencikadi = '{ogrencisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "4"):
            yenisoyad = input("Öğrencinin yeni soyadını giriniz : ")
            connection.execute(f"update ogrenci set ogrencisoyadi = '{yenisoyad}' where ogrencikadi = '{ogrencisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "5"):
            nobaskasindami = True
            while(nobaskasindami == True):
                yeniogrno = input("Öğrencinin yeni numarasını giriniz : ")
                ogrenciler = connection.execute("select ogrencinumarasi from ogrenci").fetchall()
                for ogrenci in ogrenciler:
                    if(ogrenci[0] == yeniogrno):
                        nobaskasindami = True
                        break
                    else:
                        nobaskasindami = False
                        continue
                try:
                    yeniogrno = int(yeniogrno)
                    if(nobaskasindami == True):
                        print("Girilen öğrenci numarası başka bir öğrenci tarafından kullanılıyor. Lütfen tekrar deneyin.")
                    else:
                        connection.execute(f"update ogrenci set ogrencinumarasi = '{yeniogrno}' where ogrencikadi = '{ogrencisecim}'")
                        connection.commit()
                except:
                    print("""
                    Lütfen öğrenci numarasına sayı dışında bir şey girmeyiniz...
                    """)
                    nobaskasindami = True
            islemdogrumu = True
        elif(islem == "6"):
            tf = False
            while tf == False:
                yenimail = input("Öğrencinin yeni mail adresini giriniz : ")
                if "@" not in yenimail or "." not in yenimail:
                    tf = False
                    print("""
                    Hatalı bir mail adresi girdiniz. Lütfen tekrar deneyiniz!
                    """)
                else:
                    tf = True
            connection.execute(f"update ogrenci set ogrenciemaili = '{yenimail}' where ogrencikadi = '{ogrencisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "7"):
            torf = False
            while torf == False:
                yenitelno = input("Öğrencinin yeni telefon numarasını giriniz : ")
                try:
                    yenitelno = int(yenitelno)
                    if len(str(yenitelno)) == 11 or len(str(yenitelno)) == 10:
                        torf = True
                    else:
                        print("""
                        Lütfen doğru bir telefon numarası giriniz!
                        """)
                        torf = False
                except:
                    torf = False
                    print("""
                    Lütfen telefon numarasına yalnızca sayısal değer giriniz!
                    """)
            connection.execute(f"update ogrenci set ogrencitelno = '{yenitelno}' where ogrencikadi = '{ogrencisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "8"):
            islemdogrumu = True
            ogrenciislemleri(ogrid)
        else:
            print("Yanlış bir işlem yaptınız.")
    devammi = input("""
    Öğrenci bilgisi başarıyla değiştirildi! Şimdi ne yapmak istersiniz : 
    
    1- Öğrenci kayıt düzenleme ekranına dön

    2- Öğrenci işlemleri menüsüne dön
    """)
    if(devammi == "1"):
        ogrencikayitduzenle(ogrid)
    elif(devammi == "2"):
        ogrenciislemleri(ogrid)
    else:
        print("Geçerli bir işlem girmediğiniz için öğrenci işlemleri menüsüne dönülüyor...")
        ogrenciislemleri(ogrid)

def ogrencikayitsil(ogrid):
    print(f"""
    {cizgi}
    Öğrenci Kayıt Silme Ekranına Hoş Geldiniz
    {cizgi}
    """)
    ogrenciler = connection.execute("select * from ogrenci")
    print("""
    Lütfen kaydını silmek istediğiniz öğrencinin kullanıcı adını giriniz ya da çıkış yazınız : """)
    for ogrenci in ogrenciler:
        print(f"-> {ogrenci[2]} {ogrenci[3]}({ogrenci[0]})")
    hangiogrencisilinsin = input("")
    if(hangiogrencisilinsin == "çıkış"):
        ogrenciislemleri(ogrid)
    else:
        ogrencivarmi = False
        print("deneme")
        ogrenciler = connection.execute("select ogrencikadi from ogrenci")
        for ogrenci in ogrenciler:
            if(ogrenci[0] == hangiogrencisilinsin):
                ogrencivarmi = True
                break
            else:
                continue
        if(ogrencivarmi == True):
            connection.execute(f"delete from ogrenci where ogrencikadi = '{ogrenci[0]}'")
            connection.commit()
            print("Öğrenci başarıyla silindi!")
        else:
            print("Maalesef girdiğiniz kullanıcı adına sahip öğrenci bulunamadı. Lütfen tekrar deneyiniz.")
            ogrencikayitsil(ogrid)
        
    islemvarmi = False
    while(islemvarmi == False):
        islem = input("""
        Şimdi ne işlemi yapmak istersiniz : 

        1- Bir öğrencinin kaydını daha sil

        2- Öğrenci işlemleri ekranına dön

        3- Yetkili ekranına dön
        """)
        if(islem == "1"):
            print("Öğrenci kayıt silme ekranına yönlendiriliyorsunuz...")
            ogrencikayitsil(ogrid)
            islemvarmi = True
        elif(islem == "2"):
            print(geriadim)
            ogrenciislemleri(ogrid)
            islemvarmi = True
        elif(islem == "3"):
            print("Yetkili ekranına yönlendiriliyorsunuz...")
            yetkiliekrani(ogrid)
            islemvarmi = True
        else:
            print("Yanlış bir işlem yaptınız. Lütfen tekrar deneyiniz.")

def ogrencinotlariduzenle(ogrid, yetki):
    print(f"""
    {cizgi}
    Öğrenci Not Düzenleme Ekranına Hoş Geldiniz
    {cizgi}""")
    ogrencivarmi = False
    while(ogrencivarmi == False):
        print("""
        Lütfen notunu düzenlemek istediğiniz öğrencinin kullanıcı adını giriniz ya da çıkış yazınız : """)
        ogrenciler = connection.execute("select * from ogrenci")
        for ogrenci in ogrenciler:
            print(f"-> {ogrenci[2]} {ogrenci[3]}({ogrenci[0]})")
        hangiogrenci = input("")
        if hangiogrenci == "çıkış":
            print(geriadim)
            ogretmenekrani(ogrid)
        else:
            ogrenciler = connection.execute("select ogrencikadi from ogrenci").fetchall()
            for ogrenci in ogrenciler:
                if hangiogrenci == ogrenci[0]:
                    ogrencivarmi = True
                else:
                    continue
            if ogrencivarmi == False:
                print("""
                Girdiğiniz kullanıcı adı hatalı. Lütfen tekrar deneyiniz
                """)
    hangiogrenci = connection.execute(f"select * from ogrenci where ogrencikadi = '{hangiogrenci}'").fetchone()
    print(f"""
    {cizgi}
    Seçtiğiniz Öğrenci : {hangiogrenci[0]}
    {cizgi}

    1. Sınav = {hangiogrenci[7]}
    {cizgi}
    2. Sınav = {hangiogrenci[8]}
    {cizgi}
    3. Sınav = {hangiogrenci[9]}
    {cizgi}
    """)
    dogrumu = False
    while(dogrumu == False):
        hangisinav = input(f"""{hangiogrenci[0]} kullanıcı adlı öğrencinin hangi sınavını değiştirmek istersiniz: 
        
        1- 1.Sınav

        2- 2.Sınav

        3- 3.Sınav

        4- Çıkış
        """)
        if (hangisinav == "1"):
            gecerlimi = False
            while(gecerlimi == False):
                yeninot = input("Lütfen kaç girmek istediğinizi giriniz : ")
                try:
                    yeninot = int(yeninot)
                    gecerlimi = True
                    if(yeninot < 0):
                        print("Girilen not 0 dan küçük olamaz. Lütfen tekrar giriniz.")
                        gecerlimi = False
                    elif(yeninot > 100):
                        print("Girilen notlar 100 den büyük olamaz. Lütfen tekrar giriniz.")
                        gecerlimi = False
                except ValueError:
                    print("Girdiğiniz not hatalıdır. Lütfen tekrar giriniz.")
            connection.execute(f"update ogrenci set ogrencisinavbir =  '{yeninot}' where ogrencikadi = '{hangiogrenci[0]}'")
            connection.commit()
            print("Öğrencinin notu başarıyla değiştirildi.")
            dogrumu = True
        elif(hangisinav == "2"):
            gecerlimi = False
            while(gecerlimi == False):
                yeninot = input("Lütfen kaç girmek istediğinizi giriniz : ")
                try:
                    yeninot = int(yeninot)
                    gecerlimi = True
                    if(yeninot < 0):
                        print("Girilen not 0 dan küçük olamaz. Lütfen tekrar giriniz.")
                        gecerlimi = False
                    elif(yeninot > 100):
                        print("Girilen notlar 100 den büyük olamaz. Lütfen tekrar giriniz.")
                        gecerlimi = False
                except ValueError:
                    print("Girdiğiniz not hatalıdır. Lütfen tekrar giriniz.")
            connection.execute(f"update ogrenci set ogrencisinaviki = '{yeninot}' where ogrencikadi = '{hangiogrenci}'")
            connection.commit()
            print("Öğrencinin notu başarıyla değiştirildi.")
            dogrumu = True
        elif(hangisinav == "3"):
            gecerlimi = False
            while(gecerlimi == False):
                yeninot = input("Lütfen kaç girmek istediğinizi giriniz : ")
                try:
                    yeninot = int(yeninot)
                    gecerlimi = True
                    if(yeninot < 0):
                        print("Girilen not 0 dan küçük olamaz. Lütfen tekrar giriniz.")
                        gecerlimi = False
                    elif(yeninot > 100):
                        print("Girilen notlar 100 den büyük olamaz. Lütfen tekrar giriniz.")
                        gecerlimi = False
                except ValueError:
                    print("Girdiğiniz not hatalıdır. Lütfen tekrar giriniz.")
            connection.execute(f"update ogrenci set ogrencisinavuc =  '{yeninot}' where ogrencikadi = '{hangiogrenci}'")
            connection.commit()
            dogrumu = True
            print("Öğrencinin notu başarıyla değiştirildi.")
        elif(hangisinav == "4"):
            print(geriadim)
            ogrenciislemleri(ogrid)
            dogrumu = True
            break
        else:
            print("Girdiğiniz işlem hatalıdır. Lütfen tekrar deneyiniz.")
            dogrumu = False
    hangiislem = False
    if yetki == "mudur":
        while(hangiislem == False):
            islem = input("""
        Hangi işlemi yapmak istersiniz:

        1- Yeni not gir

        2- Öğrenci işlem ekranına dön
        """)
            if islem == "1":
                print("Not girmek için yönlendiriliyorsunuz\n")
                ogrencinotlariduzenle(ogrid, yetki)
                break
            elif(islem == "2"):
                print("Öğrenci işlem ekranına Yönlendiriliyorsunuz\n")
                ogrenciislemleri(ogrid)
                break
            else:
                print("Yanlış bir işlem yaptınız. Lütfen yeniden deneyiniz!\n")
    else:
        while(hangiislem == False):
            islem = input("""
        Hangi işlemi yapmak istersiniz:

        1- Yeni not gir

        2- Öğretmen ekranına dön
        """)
            if islem == "1":
                print("Not girmek için yönlendiriliyorsunuz\n")
                ogrencinotlariduzenle(ogrid, yetki)
                break
            elif(islem == "2"):
                print("Öğretmen ekranına Yönlendiriliyorsunuz\n")
                ogretmenekrani(ogrid)
                break
            else:
                print("Yanlış bir işlem yaptınız. Lütfen yeniden deneyiniz!\n")

def ogrencidevamsizlikekle(ogrid, yetki):
    print(f"""
    {cizgi}
    Öğrenci Devamsızlık Ekleme Ekranına Hoş Geldiniz
    {cizgi}""")
    dogrumu = False
    while(dogrumu == False):
        ogrenciler = connection.execute("select * from ogrenci")
        for ogrenci in ogrenciler:
            print(f"-> {ogrenci[2]} {ogrenci[3]}({ogrenci[0]})")
        hangiogrenci = input("Lütfen devamsızlık eklemek istediğiniz öğrencinin kullanıcı adını giriniz : ")
        ogrenciisimler = connection.execute("select ogrencikadi from ogrenci").fetchall()
        for ogrenci in ogrenciisimler:
            if(hangiogrenci == ogrenci[0]):
                dogrumu = True
            else:
                continue
        if(dogrumu == False):
            print("Girdiğiniz kullanıcı adına sahip öğrenci bulunamadı. Lütfen tekrar deneyiniz.")
    gecerlimi = False
    while(gecerlimi == False):
        kacgun = input("Lütfen kaç gün devamsızlık eklemek istediğinizi giriniz : ")
        try:
            kacgun = int(kacgun)
            gecerlimi = True
            if(kacgun < 0):
                print("Eklenecek devamsızlık 0 dan küçük olamaz. Lütfen tekrar giriniz.")
                gecerlimi = False
        except ValueError:
            print("Girdiğiniz gün sayısı hatalıdır. Lütfen tekrar giriniz.")
    olangun = connection.execute(f"select ogrencidevamsizlik from ogrenci where ogrencikadi = '{hangiogrenci}'").fetchone()
    kacgun = olangun[0] + kacgun
    connection.execute(f"update ogrenci set ogrencidevamsizlik = '{kacgun}' where ogrencikadi = '{hangiogrenci}'")
    connection.commit()
    print("Öğrencinin devamsızlığı başarıyla değiştirildi.")
    print(f"{hangiogrenci} kullanıcı adlı öğrencinin yeni devamsızlık gün sayısı : {kacgun}")
    islemtf = False
    while(islemtf == False):
        islem = input("""
        Lütfen yapmak istediğiniz işlemi seçiniz :

        1- Yeni devamsızlık ekle

        2- Devamsızlık ekranına dön
        """)
        if(islem == "1"):
            ogrencidevamsizlikekle(ogrid, yetki)
            islemtf = True
            break
        elif(islem == "2"):
            ogrencidevamsizliklari(ogrid, yetki)
            islemtf = True
            break
        else:
            print("Girdiğiniz işlem yanlıştır. Lütfen tekrar deneyiniz.")
            islemtf = False

def ogrencidevamsizlikgor(ogrid, yetki):
    print(f"""
    {cizgi}
    Öğrenci Devamsızlık Görme Ekranına Hoş Geldiniz
    {cizgi}""")
    ogrenciler = connection.execute("select * from ogrenci")
    for ogrenci in ogrenciler:
        print(f"""
        Öğrenci Kullanıcı Adı : {ogrenci[0]}
        Öğrenci : {ogrenci[2]} {ogrenci[3]}
        Öğrenci Devamsızlığı : {ogrenci[10]}

        """)
    dogrumu = False
    if yetki == "mudur":
        while(dogrumu == False):
            islem = input("""
        Hangi işlemi yapmak istersiniz:

        1- Öğrenci devamsızlıklarını görüntüle

        2- Öğrenci devamsızlıklarını düzenle

        3- Öğrenci devamsızlık ekranına dön
        """)
            if(islem == "1"):
                print("Öğrenci devamsızlık görme ekranına yönlendiriliyorsunuz...")
                ogrencidevamsizlikgor(ogrid, yetki)
                dogrumu = True
                break
            elif(islem == "2"):
                print("Öğrenci devamsızlık düzenleme ekranına yönelndiriliyorsunuz...")
                ogrencidevamsizlikduzenle(ogrid)
                dogrumu = True
                break
            elif(islem == "3"):
                print("Öğrenci devamsızlıkları ekranına yönlendiriliyorsunuz...")
                ogrencidevamsizliklari(ogrid, yetki)
                dogrumu = True
                break
            else:
                print("Yanlış bir işlem yaptınız. Lütfen yeniden giriniz.")
                dogrumu = False
    else:
        while(dogrumu == False):
            islem = input("""
        Hangi işlemi yapmak istersiniz:

        1- Öğrencilere devamsızlık ekle

        2- Öğrenci devamsızlıklarını gör

        3- Öğrenci devamsızlık ekranına dön
        """)
            if(islem == "1"):
                print("Öğrenci devamsızlık görme ekranına yönlendiriliyorsunuz...")
                ogrencidevamsizlikekle(ogrid, yetki)
                dogrumu = True
                break
            elif(islem == "2"):
                print("Öğrenci devamsızlık düzenleme ekranına yönelndiriliyorsunuz...")
                ogrencidevamsizlikgor(ogrid, yetki)
                dogrumu = True
                break
            elif(islem == "3"):
                print("Öğrenci devamsızlıkları ekranına yönlendiriliyorsunuz...")
                ogrencidevamsizliklari(ogrid, yetki)
                dogrumu = True
                break
            else:
                print("Yanlış bir işlem yaptınız. Lütfen yeniden giriniz.")
                dogrumu = False

def ogrencidevamsizlikduzenle(ogrid):
    print(f"""
    {cizgi}
    Öğrenci Devamsızlık Düzenleme Ekranına Hoş Geldiniz
    {cizgi}""")
    ogrenciler = connection.execute("select * from ogrenci")
    for ogrenci in ogrenciler:
        print(f"""
        Öğrenci Kullanıcı Adı : {ogrenci[0]}
        Öğrenci : {ogrenci[2]} {ogrenci[3]}
        Öğrenci Devamsızlığı : {ogrenci[10]}

        """)
    ogrencidogrumu = False
    while ogrencidogrumu == False:
        hangiogrenci = input("""Lütfen devamsızlığını düzenlemek istediğiniz öğrencinin kullanıcı adını giriniz ya da çıkış yazınız
        Kullanıcı Adı : """)
        if hangiogrenci == "çıkış":
            ogrencidevamsizliklari(ogrid, "mudur")
        ogrenciler = connection.execute("select * from ogrenci")
        for ogrenci in ogrenciler:
            if hangiogrenci == ogrenci[0]:
                ogrencidogrumu = True
                break
            else:
                continue
        if ogrencidogrumu == False:
            print(f"{hangiogrenci} adında bir öğrenci bulunamadı, lütfen tekrar deneyiniz...")    
    gunintmi = False
    while gunintmi == False:
        gunkacolsun = input(f"""{hangiogrenci} kullanıcı adlı öğrenci için devamsızlık kaç olacak?
        Yeni devamsızlık gün sayısı : """)
        try:
            gunkacolsun = int(gunkacolsun)
            gunintmi = True
        except:
            print("Maalesef girdiğiniz değer bir sayı değildir. Lütfen tekrar giriniz!")
            gunintmi = False
    connection.execute(f"update ogrenci set ogrencidevamsizlik = '{gunkacolsun}' where ogrencikadi = '{hangiogrenci}'")
    connection.commit()
    print(f"""
    {hangiogrenci} kullanıcı adlı öğrencinin devamsızlık gün sayısı başarıyla {gunkacolsun} olarak değiştirildi!
    """)
    islemdogrumu = False
    while islemdogrumu == False:
        islem = input("""
        Şimdi hangi işlemi yapmak istersiniz?
    
        1- Öğrenci devamsızlık düzenleme ekranına geri dön

        2- Öğrenci devamsızlık ekranına dön

        3- Öğrenci işlemleri ekranına dön
        """)
        if islem == "1":
            print("Öğrenci devamsızlık düzenleme ekranına yönlendiriliyorsunuz...")
            ogrencidevamsizlikduzenle(ogrid)
            islemdogrumu = True
        elif islem == "2":
            print("Öğrenci devamsızlık ekranına yönlendiriliyorsunuz...")
            ogrencidevamsizliklari(ogrid, "mudur")
            islemdogrumu = True
        elif islem == "3":
            print("Öğrenci işlemleri ekranına yönlendiriliyorsunuz...")
            ogrenciislemleri(ogrid)
            islemdogrumu = True
        else:
            print("\nGirdiğiniz işlem bilgisi hatalıdır. Lütfen tekrar deneyiniz!\n")
            islemdogrumu = False

def ogrencidevamsizliksil(ogrid):
    print(f"""
    {cizgi}
    Öğrenci Devamsızlık Silme Ekranına Hoş Geldiniz
    {cizgi}""")
    ogrenciler = connection.execute("select * from ogrenci")
    for ogrenci in ogrenciler:
        print(f"""
        Öğrenci Kullanıcı Adı : {ogrenci[0]}
        Öğrenci : {ogrenci[2]} {ogrenci[3]}
        Öğrenci Devamsızlığı : {ogrenci[10]}

        """)
    secimdogrumu = False
    while secimdogrumu == False:
        hangiogrenci = input("""Lütfen devamsızlığını silmek istediğiniz öğrencinin kullanıcı adını giriniz ya da çıkış yazınız
        Kullanıcı adı : """)
        if hangiogrenci == "çıkış":
            print("\nÖğrenci devamsızlıkları ekranına yönlendiriliyorsunuz...\n")
            ogrencidevamsizliklari(ogrid, "mudur")
        ogrenciler = connection.execute("select * from ogrenci")
        for ogrenci in ogrenciler:
            if hangiogrenci == ogrenci[0]:
                secimdogrumu = True
                break
            else:
                continue
        if secimdogrumu == False:
            print("\nGirdiğiniz kullanıcı adında bir öğrenci bulunmamaktadır. Lütfen tekrar giriniz...\n")
    gundogrumu = False
    while gundogrumu == False:
        kacgun = input(f"""
        Lütfen {hangiogrenci} kullanıcı adlı öğrenciden kaç gün silmek istediğinizi yazınız
        
        Silinecek gün sayısı : 
        """)
        try:
            kacgun = int(kacgun)
            gundogrumu = True
            ogrencidevamsizlik = connection.execute(f"select ogrencidevamsizlik from ogrenci where ogrencikadi = '{hangiogrenci}'").fetchone()
            if ogrencidevamsizlik[0] - kacgun < 0:
                print("""
                Girdiğiniz gün sayısı öğrencinin mevcut gün sayısından daha fazladır. 

                Devamsızlık gün sayısı 0'ın altında olamaz.

                Lütfen devamsızlık gün sayısını tekrar giriniz.
                """)
                gundogrumu = False
        except:
            print("\nGirdiğiniz gün sayısı hatalıdır. Lütfen tekrar giriniz\n")
            gundogrumu = False
    ogrencidevamsizligi = connection.execute(f"select ogrencidevamsizlik from ogrenci where ogrencikadi = '{hangiogrenci}'").fetchone()
    yenidevamsizlik = ogrencidevamsizligi[0] - kacgun
    connection.execute(f"update ogrenci set ogrencidevamsizlik = '{yenidevamsizlik}' where ogrencikadi = '{hangiogrenci}'")
    connection.commit()
    print(f"\n{hangiogrenci} kullanıcı adlı öğrencinin yeni devamsızlık gün sayısı {yenidevamsizlik} olarak güncellenmiştir!\n")
    dogrumu = False
    while dogrumu == False:
        secim = input(f"""
        Şimdi hangi işlemi yapmak istersiniz?

        1- Devamsızlık silme ekranına dön

        2- Öğrenci devamsızlık ekranına dön

        3- Öğrenci işlemleri ekranına dön
        """)
        if secim == "1":
            print("\nÖğrenci devamsızlık silme ekranına yönlendiriliyorsunuz...\n")
            ogrencidevamsizliksil(ogrid)
            dogrumu = True
        elif secim == "2":
            print("\nÖğrenci devamsızlık ekranına yönlendiriliyorsunuz...\n")
            ogrencidevamsizliklari(ogrid, "mudur")
            dogrumu = True
        elif secim == "3":
            print("\nÖğrenci işlemleri ekranına yönlendiriliyorsunuz...\n")
            ogrenciislemleri(ogrid)
            dogrumu = True
        else:
            print("\nSeçtiğiniz işlem hatalıdır. Lütfen tekrar giriniz...\n")
            dogrumu = False

def ogrencidevamsizliklari(ogrid, yetki):
    if yetki == "mudur":
        secim = input(f"""
    {cizgi}
    Öğrenci Devamsızlık Ekranına Hoş Geldiniz
    {cizgi}
    Lütfen yapmak istediğiniz işlemi seçiniz:

    1- Öğrenci devamsızlık ekle

    2- Öğrenci devamsızlıklarını görüntüle

    3- Öğrenci devamsızlıklarını düzenle

    4- Öğrenci devamsızlık sil
    
    5- Öğrenci işlemleri ekranına dön
    """)
    else:
        secim = input(f"""
    {cizgi}
    Öğrenci Devamsızlık Ekranına Hoş Geldiniz
    {cizgi}
    Lütfen yapmak istediğiniz işlemi seçiniz:

    1- Öğrenci devamsızlık ekle

    2- Öğrenci devamsızlıklarını görüntüle
    
    3- Öğretmen ekranına dön
    """)
    if(secim == "1"):
        ogrencidevamsizlikekle(ogrid, yetki)
    elif(secim == "2"):
        ogrencidevamsizlikgor(ogrid, yetki)
    elif(secim == "3" and yetki == "ogretmen"):
        print(geriadim)
        ogretmenekrani(ogrid)
    elif(secim == "3" and yetki == "mudur"):
        ogrencidevamsizlikduzenle(ogrid)
    elif(secim == "4" and yetki == "mudur"):
        ogrencidevamsizliksil(ogrid)
    elif(secim == "5" and yetki == "mudur"):
        print("Öğrenci işlemleri ekranına dönülüyor...")
        ogrenciislemleri(ogrid)
    else:
        print("Yanlış bir seçim yaptınız. Lütfen tekrar giriniz.")
        ogrencidevamsizliklari(ogrid, yetki)

def ogretmenkayit(ogrid):
    print(f"""
    {cizgi}
    Öğretmen Kayıt Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    bilgiler = connection.execute("select * from ogretmen")
    ogrisim = None
    ogrsoyad = None
    ogrkadi = None
    ogrsifre = None
    ogrtelno = None
    ogrmail = None
    while(ogrisim == None or ogrsoyad == None or ogrkadi == None or ogrsifre == None or ogrtelno == None or ogrmail == None):
        dogrumu = False
        while dogrumu == False:
            dogrumu = True
            ogrisim = input("Kayıt etmek istediğiniz öğretmenin ismini giriniz : ")
            ogrsoyad = input("Kayıt etmek istediğiniz öğretmenin soyadını giriniz : ")
            ogrkadi = input("Kayıt etmek istediğiniz öğretmenin kullanıcı adını giriniz : ")
            ogrsifre = input("Kayıt etmek istediğiniz öğretmenin şifresini giriniz : ")
            ogrtelno = input("Kayıt etmek istediğiniz öğretmenin iletişim telefon numarasını giriniz : ")
            ogrmail = input("Kayıt etmek istediğiniz öğretmenin iletişim mail adresini giriniz : ")
            for bilgi in bilgiler:
                if(bilgi[0] == ogrkadi):
                    print("Öğretmenin kullanıcı adı başka bir öğretmende de bulunmakta!")
                    ogrkadi = None
            if len(str(ogrsifre)) < 8:
                print("""
                Girilen şifre 8 karakterden az olamaz! Lütfen tekrar giriniz...
                """)
                ogrsifre = None
                dogrumu = False
            if "@" not in ogrmail and "." not in ogrmail:
                print("""
                Girdiğiniz mail adresi hatalıdır. Lütfen tekrar giriniz...
                """)
                ogrmail = None
                dogrumu = False
            try:
                ogrtelno = int(ogrtelno)
                if len(str(ogrtelno)) != 10 and len(str(ogrtelno)) != 11:
                    print("""
                    Telefon numarası hatalıdır. Lütfen tekrar giriniz!
                    """)
                    ogrtelno = None
                    dogrumu = False
            except:
                print("""
                Girilen telefon numarası hatalıdır. Lütfen tekrar giriniz!
                """)
                ogrtelno = None
                dogrumu = False
    connection.execute(f"""insert into ogretmen 
    (ogretmenkadi, ogretmensifre, ogretmenadi, ogretmensoyadi, ogretmenmail, ogretmentelno) 
    values ('{ogrkadi}', '{ogrsifre}', '{ogrisim}', '{ogrsoyad}', '{ogrmail}', '{ogrtelno}')""")
    connection.commit()
    print(f"{ogrisim} isimli öğretmen başarıyla kayıt edildi!")
    secim = None
    while(secim == None):
        secim = input("""
        Hangi işlemi yapmak istersiniz :

        1- Yeni öğretmen kaydı oluştur

        2- Öğretmen işlem ekranına geri dön

        3- Yetkili ekranına geri dön
        """)
        if(secim == "1"):
            ogretmenkayit(ogrid)
        elif(secim == "2"):
            print(geriadim)
            ogretmenislemleri(ogrid)
        elif(secim == "3"):
            print("Yetkili ekranına dönülüyor...")
            yetkiliekrani(ogrid)
        else:
            print("(!) Yanlış bir seçim yaptınız. Bu yüzden tekrar yönlendiriliyorsunuz")
            secim = None

def ogretmenkayitduzenle(ogrid):
    print(f"""
    {cizgi}
    Öğretmen Kayıt Düzenleme Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    ogrenciler = connection.execute("select * from ogretmen order by ogretmenkadi")
    ogrencidogrumu = None
    ogrencisecim = None
    while(ogrencidogrumu != True):

        print(f"""
        -> Lütfen işlem yapmak istediğiniz öğretmenin kullanıcı adını giriniz :
        """)
        for ogrenci in ogrenciler:
            print(f"-> {ogrenci[2]} {ogrenci[3]}({ogrenci[0]})")
        ogrencisecim = input("")
        ogrenciler = connection.execute("select * from ogretmen").fetchall()
        for ogrenci in ogrenciler:
            if(ogrencisecim == ogrenci[0]):
                ogrencidogrumu = True
            else:
                continue
        if(ogrencidogrumu != True):
            print("Yanlış bir kullanıcı adı girdiniz.")
    islemdogrumu = False
    while(islemdogrumu == False):
        islem = input("""Lütfen bu öğretmenle ilgili neyi değiştirmek istediğinizi seçin :
        
        1- Kullanıcı adı değiştir

        2- Şifre değiştir

        3- İsim değiştir

        4- Soyad değiştir

        5- Öğretmen mail adresini değiştir

        6- Öğretmen telefon numarasını değiştir

        7- Öğretmen işlemleri ekranına geri dön
        """)
        if(islem == "1"):
            islemdogrumu = True
            kadibaskasindami = True
            while(kadibaskasindami == True):
                yenikadi = input("Öğretmenin yeni kullanıcı adını giriniz : ")
                ogrenciler = connection.execute("select ogretmenkadi from ogretmen").fetchall()
                for ogrenci in ogrenciler:
                    if(ogrenci[0] == yenikadi):
                        kadibaskasindami = True
                        break
                    else:
                        kadibaskasindami = False
                        continue
                if(kadibaskasindami == True):
                    print("Girilen kullanıcı adı başka bir öğretmen tarafından kullanılıyor. Lütfen tekrar deneyin.")
                else:
                    connection.execute(f"update ogretmen set ogretmenkadi = '{yenikadi}' where ogretmenkadi = '{ogrencisecim}'")
                    connection.commit()
        elif(islem == "2"):
            sifregecerlimi = False
            while(sifregecerlimi == False):
                yenisifre = input("Öğretmenin yeni şifresini giriniz : ")
                if(len(str(yenisifre)) < 8):
                    print("""
                    Girdiğiniz şifre en az 8 karakterli olmalıdır! Lütfen tekrar giriniz!
                    """)
                else:
                    connection.execute(f"update ogretmen set ogretmensifre = '{yenisifre}' where ogretmenkadi = '{ogrencisecim}'")
                    connection.commit()
                    sifregecerlimi = True
            islemdogrumu = True
        elif(islem == "3"):
            yeniisim = input("Öğretmenin yeni ismini giriniz : ")
            connection.execute(f"update ogretmen set ogretmenadi = '{yeniisim}' where ogretmenkadi = '{ogrencisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "4"):
            yenisoyad = input("Öğretmenin yeni soyadını giriniz : ")
            connection.execute(f"update ogretmen set ogretmensoyadi = '{yenisoyad}' where ogretmenkadi = '{ogrencisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "5"):
            maildogrumu = False
            while maildogrumu == False:
                yenimail = input("Öğretmenin yeni mail adresini giriniz : ")
                if "@" in yenimail and "." in yenimail:
                    connection.execute(f"update ogretmen set ogretmenmail = '{yenimail}' where ogretmenkadi = '{ogrencisecim}'")
                    connection.commit()
                    maildogrumu = True
                else:
                    print("""
                    Girdiğiniz mail adresi geçerli değildir! Lütfen yeniden giriniz!
                    """)
            islemdogrumu = True
        elif(islem == "6"):
            teldogrumu = False
            while teldogrumu == False:
                yenitelno = input("Öğretmenin yeni telefon numarasını giriniz : ")
                try:
                    yenitelno = int(yenitelno)
                    connection.execute(f"update ogretmen set ogretmentelno = '{yenitelno}' where ogretmenkadi = '{ogrencisecim}'")
                    connection.commit()
                except:
                    print("""
                    Girdiğiniz telefon numarası hatalıdır. Lütfen tekrar giriniz...
                    """)
            islemdogrumu = True
        elif(islem == "7"):
            islemdogrumu = True
            ogretmenislemleri(ogrid)
        else:
            print("Yanlış bir işlem yaptınız.")
    devammi = input("""
    Öğretmen bilgisi başarıyla değiştirildi! Şimdi ne yapmak istersiniz : 
    
    1- Öğretmen kayıt düzenleme ekranına dön

    2- Öğretmen işlemleri menüsüne dön
    """)
    if(devammi == "1"):
        ogretmenkayitduzenle(ogrid)
    elif(devammi == "2"):
        ogretmenislemleri(ogrid)
    else:
        print("Geçerli bir işlem girmediğiniz için öğretmen işlemleri menüsüne dönülüyor...")
        ogretmenislemleri(ogrid)

def ogretmenlistesi(ogrid):
    print(f"""
    {cizgi}
    Öğretmen Listesi Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    ogretmenler = connection.execute("select * from ogretmen order by ogretmenkadi")
    for ogretmen in ogretmenler:
        print(f"-> {ogretmen[2]} {ogretmen[3]}({ogretmen[0]})")

def ogretmenkayitsil(ogrid):
    print(f"""
    {cizgi}
    Öğretmen Kayıt Silme Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    ogretmenler = connection.execute("select * from ogretmen")
    print("""
    Lütfen kaydını silmek istediğiniz öğretmenin kullanıcı adını giriniz ya da çıkış yazınız : """)
    for ogretmen in ogretmenler:
        print(f"-> {ogretmen[2]} {ogretmen[3]}({ogretmen[0]})")
    hangiogretmensilinsin = input("")
    if(hangiogretmensilinsin == "çıkış"):
        ogretmenislemleri(ogrid)
    else:
        ogretmenvarmi = False
        ogretmenler = connection.execute("select ogretmenkadi from ogretmen")
        for ogretmen in ogretmenler:
            if(ogretmen[0] == hangiogretmensilinsin):
                ogretmenvarmi = True
                break
            else:
                continue
        if(ogretmenvarmi == True):
            connection.execute(f"delete from ogretmen where ogretmenkadi = '{ogretmen[0]}'")
            connection.commit()
            print("Öğretmen başarıyla silindi!")
        else:
            print("Maalesef girdiğiniz kullanıcı adına sahip öğretmen bulunamadı. Lütfen tekrar deneyiniz.")
            ogretmenkayitsil(ogrid)


def ogretmenislemleri(ogrid):
    secim = input(f"""
    {cizgi}
    Öğretmen İşlemleri Ekranına Hoş Geldiniz
    {cizgi}
    Lütfen yapmak istediğiniz işlemi seçiniz:

    1- Öğretmen kayıt ekranı

    2- Öğretmen kayıt düzenle

    3- Öğretmen listesi
    
    4- Öğretmen kayıt silme

    5- Yetkili ekranına geri dön
    
    """)
    if(secim == "1"):
        ogretmenkayit(ogrid)
    elif(secim == "2"):
        ogretmenkayitduzenle(ogrid)
    elif(secim == "3"):
        ogretmenlistesi(ogrid)
    elif(secim == "4"):
        ogretmenkayitsil(ogrid)
    elif(secim == "5"):
        print(geriadim)
        yetkiliekrani(ogrid)
    else:
        print("(!) Yanlış bir seçim yaptınız. Bu yüzden tekrar yönlendiriliyorsunuz")
    ogretmenislemleri(ogrid)

def ogrenciislemleri(ogrid):
    secim = input(f"""
    {cizgi}
    Öğrenci İşlemleri Ekranına Hoş Geldiniz
    {cizgi}
    Lütfen yapmak istediğiniz işlemi seçiniz:

    1- Öğrenci kayıt ekranı

    2- Öğrenci kayıt düzenle

    3- Öğrenci listesi
    
    4- Öğrenci kayıt silme

    5- Öğrenci notlarını düzenle

    6- Öğrenci devamsızlıklarını düzenle

    7- Yetkili ekranına geri dön
    
    """)
    if(secim == "1"):
        ogrencikayit(ogrid)
    elif(secim == "2"):
        ogrencikayitduzenle(ogrid)
    elif(secim == "3"):
        ogrencilistesi(ogrid)
    elif(secim == "4"):
        ogrencikayitsil(ogrid)
    elif(secim == "5"):
        ogrencinotlariduzenle(ogrid , "mudur")
    elif(secim == "6"):
        ogrencidevamsizliklari(ogrid, "mudur")
    elif(secim == "7"):
        print(geriadim)
        yetkiliekrani(ogrid)
    else:
        print("(!) Yanlış bir seçim yaptınız. Bu yüzden tekrar yönlendiriliyorsunuz")
    ogrenciislemleri(ogrid)

def yetkilikayit(ogrid):
    print(f"""
    {cizgi}
    Yetkili Kayıt Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    bilgiler = connection.execute("select * from mudurvemuduryardimcisi")
    ogrisim = None
    ogrsoyad = None
    ogrkadi = None
    ogrsifre = None
    ogrtelno = None
    ogrmail = None
    while(ogrisim == None or ogrsoyad == None or ogrkadi == None or ogrsifre == None or ogrtelno == None or ogrmail == None):
        dogrumu = False
        while dogrumu == False:
            dogrumu = True
            ogrisim = input("Kayıt etmek istediğiniz yetkilinin ismini giriniz : ")
            ogrsoyad = input("Kayıt etmek istediğiniz yetkilinin soyadını giriniz : ")
            ogrkadi = input("Kayıt etmek istediğiniz yetkilinin kullanıcı adını giriniz : ")
            ogrsifre = input("Kayıt etmek istediğiniz yetkilinin şifresini giriniz : ")
            ogrtelno = input("Kayıt etmek istediğiniz yetkilinin iletişim telefon numarasını giriniz : ")
            ogrmail = input("Kayıt etmek istediğiniz yetkilinin iletişim mail adresini giriniz : ")
            for bilgi in bilgiler:
                if(bilgi[0] == ogrkadi):
                    print("Yetkilinin kullanıcı adı başka bir yetkilide de bulunmakta!")
                    ogrkadi = None
            if len(str(ogrsifre)) < 8:
                print("""
                Girilen şifre 8 karakterden az olamaz! Lütfen tekrar giriniz...
                """)
                ogrsifre = None
                dogrumu = False
            if "@" not in ogrmail and "." not in ogrmail:
                print("""
                Girdiğiniz mail adresi hatalıdır. Lütfen tekrar giriniz...
                """)
                ogrmail = None
                dogrumu = False
            try:
                ogrtelno = int(ogrtelno)
                if len(str(ogrtelno)) != 10 and len(str(ogrtelno)) != 11:
                    print("""
                    Telefon numarası hatalıdır. Lütfen tekrar giriniz!
                    """)
                    ogrtelno = None
                    dogrumu = False
            except:
                print("""
                Girilen telefon numarası hatalıdır. Lütfen tekrar giriniz!
                """)
                ogrtelno = None
                dogrumu = False
    connection.execute(f"""insert into mudurvemuduryardimcisi 
    (yetkilikadi, yetkilisifre, yetkiliadi, yetkilisoyadi, yetkilimail, yetkilitelno) 
    values ('{ogrkadi}', '{ogrsifre}', '{ogrisim}', '{ogrsoyad}', '{ogrmail}', '{ogrtelno}')""")
    connection.commit()
    print(f"{ogrisim} isimli yetkili başarıyla kayıt edildi!")
    secim = None
    while(secim == None):
        secim = input("""
        Hangi işlemi yapmak istersiniz :

        1- Yeni yetkili kaydı oluştur

        2- Yetkili işlem ekranına geri dön

        3- Yetkili ekranına geri dön
        """)
        if(secim == "1"):
            yetkilikayit(ogrid)
        elif(secim == "2"):
            print(geriadim)
            yetkiliislemleri(ogrid)
        elif(secim == "3"):
            print("Yetkili ekranına dönülüyor...")
            yetkiliekrani(ogrid)
        else:
            print("(!) Yanlış bir seçim yaptınız. Bu yüzden tekrar yönlendiriliyorsunuz")
            secim = None

def yetkilikayitduzenle(ogrid):
    print(f"""
    {cizgi}
    Yetkili Kayıt Düzenleme Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    yetkililer = connection.execute("select * from mudurvemuduryardimcisi order by yetkilikadi").fetchall()
    yetkilidogrumu = None
    yetkilisecim = None
    while(yetkilidogrumu != True):

        print(f"""
        -> Lütfen işlem yapmak istediğiniz yetkilinin kullanıcı adını giriniz :
        """)
        for yetkili in yetkililer:
            print(f"-> {yetkili[2]} {yetkili[3]}({yetkili[0]})")
        yetkilisecim = input("")
        for yetkili in yetkililer:
            if(yetkilisecim == yetkili[0]):
                yetkilidogrumu = True
            else:
                continue
        if(yetkilidogrumu != True):
            print("Yanlış bir kullanıcı adı girdiniz.")
    islemdogrumu = False
    while(islemdogrumu == False):
        islem = input("""Lütfen bu yetkiliyle ilgili neyi değiştirmek istediğinizi seçin :
        
        1- Kullanıcı adı değiştir

        2- Şifre değiştir

        3- İsim değiştir

        4- Soyad değiştir

        5- Yetkili mail adresini değiştir

        6- Yetkili telefon numarasını değiştir

        7- Yetkili işlemleri ekranına geri dön
        """)
        if(islem == "1"):
            islemdogrumu = True
            kadibaskasindami = True
            while(kadibaskasindami == True):
                yenikadi = input("Yetkilinin yeni kullanıcı adını giriniz : ")
                yetkililer = connection.execute("select yetkilikadi from mudurvemuduryardimcisi")
                for yetkili in yetkililer:
                    if(yetkili == yenikadi):
                        kadibaskasindami = True
                        break
                    else:
                        kadibaskasindami = False
                        continue
                if(kadibaskasindami == True):
                    print("Girilen kullanıcı adı başka bir yetkili tarafından kullanılıyor. Lütfen tekrar deneyin.")
                else:
                    connection.execute(f"update mudurvemuduryardimcisi set yetkilikadi = '{yenikadi}' where yetkilikadi = '{yetkilisecim}'")
                    connection.commit()
        elif(islem == "2"):
            dogrumu = False
            while dogrumu == False:
                yenisifre = input("Yetkilinin yeni şifresini giriniz : ")
                if(len(str(yenisifre)) < 8):
                    print("""
                    Girilen şifre en az 8 karakterli olmalıdır. Lütfen tekrar giriniz!
                    """)
                else:
                    connection.execute(f"update mudurvemuduryardimcisi set yetkilisifre = '{yenisifre}' where yetkilikadi = '{yetkilisecim}'")
                    connection.commit()
                    dogrumu = True
            islemdogrumu = True
        elif(islem == "3"):
            yeniisim = input("Yetkilinin yeni ismini giriniz : ")
            connection.execute(f"update mudurvemuduryardimcisi set yetkiliadi = '{yeniisim}' where yetkilikadi = '{yetkilisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "4"):
            yenisoyad = input("Yetkilinin yeni soyadını giriniz : ")
            connection.execute(f"update mudurvemuduryardimcisi set yetkilisoyadi = '{yenisoyad}' where yetkilikadi = '{yetkilisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "5"):
            maildogrumu = False
            while maildogrumu == False:
                yenimail = input("Yetkilinin yeni mail adresini giriniz : ")
                if "@" not in yenimail and "." not in yenimail:
                    print("""
                    Girdiğiniz mail adresi geçersizdir. Lütfen yeniden giriniz!
                    """)
                else:
                    maildogrumu = True
            connection.execute(f"update mudurvemuduryardimcisi set yetkilimail = '{yenimail}' where yetkilikadi = '{yetkilisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "6"):
            telnodogrumu = False
            while telnodogrumu == False:
                yenitelno = input("Yetkilinin yeni telefon numarasını giriniz : ")
                try:
                    yenitelno = int(yenitelno)
                    if len(str(yenitelno)) != 10 and len(str(yenitelno)):
                        print("""
                        Girdiğiniz telefon numarası hatalıdır. Lütfen tekrar deneyiniz!
                        """)
                    else:
                        telnodogrumu = True
                except:
                    print("""
                    Girdiğiniz telefon numarası hatalıdır. Lütfen tekrar deneyiniz!
                    """)
            connection.execute(f"update mudurvemuduryardimcisi set yetkilitelno = '{yenitelno}' where yetkilikadi = '{yetkilisecim}'")
            connection.commit()
            islemdogrumu = True
        elif(islem == "7"):
            islemdogrumu = True
            yetkiliislemleri(ogrid)
        else:
            print("Yanlış bir işlem yaptınız. Lütfen tekrar deneyiniz!\n")
    devammi = input("""
    Yetkili bilgisi başarıyla değiştirildi! Şimdi ne yapmak istersiniz : 
    
    1- Yetkili kayıt düzenleme ekranına dön

    2- Yetkili işlemleri menüsüne dön
    """)
    if(devammi == "1"):
        yetkilikayitduzenle(ogrid)
    elif(devammi == "2"):
        yetkiliislemleri(ogrid)
    else:
        print("Geçerli bir işlem girmediğiniz için yetkili işlemleri menüsüne dönülüyor...")
        yetkiliislemleri(ogrid)

def yetkililistesi(ogrid):
    print(f"""
    {cizgi}
    Yetkili Listesi Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    yetkililer = connection.execute("select * from mudurvemuduryardimcisi order by yetkilikadi")
    for yetkili in yetkililer:
        print(f"-> {yetkili[2]} {yetkili[3]}({yetkili[0]})")

def yetkilikayitsil(ogrid):
    print(f"""
    {cizgi}
    Yetkili Kayıt Silme Ekranına Hoş Geldiniz Sayın {ogrid[2]} {ogrid[3]} 
    {cizgi}
    """)
    yetkililer = connection.execute("select * from mudurvemuduryardimcisi")
    print("""
    Lütfen kaydını silmek istediğiniz yetkilinin kullanıcı adını giriniz ya da çıkış yazınız : """)
    for yetkili in yetkililer:
        print(f"-> {yetkili[2]} {yetkili[3]}({yetkili[0]})")
    hangiyetkilisilinsin = input("")
    if(hangiyetkilisilinsin == "çıkış"):
        yetkiliislemleri(ogrid)
    else:
        yetkilivarmi = False
        yetkililer = connection.execute("select yetkilikadi from mudurvemuduryardimcisi")
        for yetkili in yetkililer:
            if(yetkili[0] == hangiyetkilisilinsin):
                yetkilivarmi = True
                break
            else:
                continue
        if(yetkilivarmi == True):
            connection.execute(f"delete from mudurvemuduryardimcisi where yetkilikadi = '{yetkili[0]}'")
            print("Yetkili başarıyla silindi!")
        else:
            print("Maalesef girdiğiniz kullanıcı adına sahip yetkili bulunamadı. Lütfen tekrar deneyiniz.")
            yetkilikayitsil(ogrid)


def yetkiliislemleri(ogrid):
    secim = input(f"""
    {cizgi}
    Yetkili İşlemleri Ekranına Hoş Geldiniz
    {cizgi}
    Lütfen yapmak istediğiniz işlemi seçiniz:

    1- Yetkili kayıt ekranı

    2- Yetkili kayıt düzenle

    3- Yetkili listesi
    
    4- Yetkili kayıt silme

    5- Yetkili ekranına geri dön
    
    """)
    if(secim == "1"):
        yetkilikayit(ogrid)
    elif(secim == "2"):
        yetkilikayitduzenle(ogrid)
    elif(secim == "3"):
        yetkililistesi(ogrid)
    elif(secim == "4"):
        yetkilikayitsil(ogrid)
    elif(secim == "5"):
        print(geriadim)
        yetkiliekrani(ogrid)
    else:
        print("(!) Yanlış bir seçim yaptınız. Bu yüzden tekrar yönlendiriliyorsunuz")
    yetkiliislemleri(ogrid)


def yetkiliekrani(ogrid):
    print(cizgi)
    secim = input(f"""\n
    Yetkili Ekranı'na Hoş Geldiniz
    Mevcut kullanıcı : {ogrid[0]}
    
    {cizgi}

    Lütfen yapmak istediğiniz işlemi seçiniz:
    
    1- Öğrenci işlemleri
    
    2- Öğretmen işlemleri
    
    3- Yetkili işlemleri

    4- Güvenli çıkış yap
    """)

    if(secim == "1"):
        ogrenciislemleri(ogrid)
    elif(secim == "2"):
        ogretmenislemleri(ogrid)
    elif(secim == "3"):
        yetkiliislemleri(ogrid)
    elif secim == "4":
        print(f"""
        Başarıyla çıkış yaptınız sayın {ogrid[2]} {ogrid[3]}
        """)
        hangigiris()
    else:
        print("(!) Yanlış bir seçim yaptınız. Bu yüzden tekrar yönlendiriliyorsunuz")
    yetkiliekrani(ogrid)


def ogrencigiriskontrol(kadi = "", sifre = ""):
    checkpw = connection.execute("select * from Ogrenci")
    for row in checkpw:
        if(row[0] == kadi and row[1] == sifre):
            print("\nYeni nesil elektronik okul sistemine hoşgeldiniz öğrenci " + row[2], row[3])
            return row
        else:
            continue
    return False

def ogretmengiriskontrol(kadi = "", sifre = ""):
    checkpw = connection.execute("select * from Ogretmen")
    for row in checkpw:
        if(row[0] == kadi and row[1] == sifre):
            print("\nYeni nesil elektronik okul sistemine hoşgeldiniz öğretmen " + row[2], row[3])
            return row
        else:
            continue
    return False

def yetkiligiriskontrol(kadi = "", sifre = ""):
    checkpw = connection.execute("select * from mudurvemuduryardimcisi")
    for row in checkpw:
        if(row[0] == kadi and row[1] == sifre):
            print("\nYeni nesil elektronik okul sistemine hoşgeldiniz sayın " + row[2], row[3])
            return row
        else:
            continue
    return False


def ogrencigirisi():
    print(cizgi)
    print("->   Öğrenci giriş ekranına hoşgeldiniz!\n")
    kadi = False
    sayac = 0
    while(kadi == False):
        kadi = input("->    Lütfen öğrenci kullanıcı adınızı giriniz : ")
        sifre = input("\n->   Lütfen öğrenci şifrenizi giriniz : ")
        kadi = ogrencigiriskontrol(kadi, sifre)
        if(kadi == False):
            print("""
            (!) Kullanıcı adınız ya da şifreniz hatalıdır! Lütfen tekrar deneyiniz!
            """)
            sayac += 1
        else:
            ogrenciekrani(kadi)
        if sayac % 3 == 0:
            secim = input(f"""-> Bilgilerinizi {sayac} kez yanlış girdiniz!\n->  Lütfen yapmak istediğiniz işlemi seçiniz
            
            1-  Giriş seçim ekranına geri dön
            
            2-  Kullanıcı adı ve şifreyi yeniden dene\n""")
            if(secim == "1"):
                print(geriadim)
                hangigiris()
            elif(secim == "2"):
                continue
            else:
                print("->   Geçerli bir işlem yapmadınız! Bu yüzden otomatik olarak yeniden deneme ekranına yönlendiriliyorsunuz!")
        


def ogretmengirisi():
    print(cizgi)
    print("->   Öğretmen giriş ekranına hoşgeldiniz!\n")
    kadi = False
    sayac = 0
    while(kadi == False):
        kadi = input("->    Lütfen öğretmen kullanıcı adınızı giriniz : ")
        sifre = input("->   Lütfen öğretmen şifrenizi giriniz : ")
        kadi = ogretmengiriskontrol(kadi, sifre)
        if(kadi == False):
            print("""
            (!) Kullanıcı adınız ya da şifreniz hatalıdır! Lütfen tekrar deneyiniz!
            """)
            sayac += 1
        else:
            ogretmenekrani(kadi)
        if sayac == 3:
            secim = input("""-> Bilgilerinizi 3 kez yanlış girdiniz!\n->  Lütfen yapmak istediğiniz işlemi seçiniz
            
            1-  Giriş seçim ekranına geri dön
            
            2-  Kullanıcı adı ve şifreyi yeniden dene\n""")
            if(secim == "1"):
                print(geriadim)
                hangigiris()
            elif(secim == "2"):
                continue
            else:
                print("->   Geçerli bir işlem yapmadınız! Bu yüzden otomatik olarak yeniden deneme ekranına yönlendiriliyorsunuz!")


def yetkiligirisi():
    print(cizgi)
    print("->   Yetkili giriş ekranına hoşgeldiniz!\n")
    kadi = False
    sayac = 0
    while(kadi == False):
        kadi = input("->    Lütfen yetkili kullanıcı adınızı giriniz : ")
        sifre = input("->   Lütfen yetkili şifrenizi giriniz : ")
        kadi = yetkiligiriskontrol(kadi, sifre)
        if(kadi == False):
            print("""
            (!) Kullanıcı adınız ya da şifreniz hatalıdır! Lütfen tekrar deneyiniz!
            """)
            sayac += 1
        else:
            yetkiliekrani(kadi)
        if sayac == 3:
            secim = input("""-> Bilgilerinizi 3 kez yanlış girdiniz!\n->  Lütfen yapmak istediğiniz işlemi seçiniz
            
            1-  Giriş seçim ekranına geri dön
            
            2-  Kullanıcı adı ve şifreyi yeniden dene\n""")
            if(secim == "1"):
                print(geriadim)
                hangigiris()
            elif(secim == "2"):
                continue
            else:
                print("->   Geçerli bir işlem yapmadınız! Bu yüzden otomatik olarak yeniden deneme ekranına yönlendiriliyorsunuz!")

def hangigiris():

    hangikullanici = input("""
    Hangi kullanıcı olarak giriş yapmak istersiniz?

    1-  Öğrenci Girişi

    2-  Öğretmen Girişi

    3-  Yetkili Girişi
    """)
    if hangikullanici == "1":
        ogrencigirisi()
    elif hangikullanici == "2":
        ogretmengirisi()
    elif hangikullanici == "3":
        yetkiligirisi()
    else:
        print("Yanlış bir işlem yaptınız!")
        hangigiris()

def acilis():
    print("""
    ___________________________ __________________________
    |    -------------------   |   ___________            |
    |            |             |  |           \\           |
    |            |             |  |            |          |
    |            |             |  |___________/           |
    |            |             |  |           \\           |
    |            |             |  |            |          |
    |            |  unç        |  |___________/  ilişim   |
    |__________________________|__________________________|

    ->  Tunç E-Okul sistemine hoş geldiniz!
    """)
    print(cizgi)

    hangigiris()

acilis()












    






connection.close()