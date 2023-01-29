def atm():
    kullaniciAdi = "Alp"
    sifrem = "1234"
    
    bakiye = 5000
    borc = 3000
    kredi = 2000
    hak = 3
    while True:
        hesap = input("Kullanıcı adınızı giriniz = ")
        sifre = input("Şifrenizi giriniz = ")
        hak -= 1
        if hesap == kullaniciAdi and sifre == sifrem:
            while True:
                print("""İşlemler:
                                  0 - Çıkış
                                  1 - Para çekme
                                  2 - Para yatırma
                                  3 - Para gönderme
                                  4 - Bakiye sorgulama
                                  5 - Borç yatırma
                                  6 - Şifre değiştirme
                                  7 - Kredi çekme
                      """)
                islem = int(input("Yapmak istediğiniz işlemi giriniz = "))
                if islem == 1:
                    while True:
                        cek = int(input("Çekmek istediğiniz miktarı giriniz = "))
                        if cek > bakiye:
                            print("Bakiyeniz yetersiz.")
                        else:
                            bakiye -= cek
                            print(f"{cek} TL çekildi. Kalan bakiyeniz = {bakiye}")
                            break
                elif islem == 2:
                    while True:
                        yatir = int(input("Yatırmak istediğiniz miktarı giriniz = "))
                        if yatir > 0:
                            bakiye += yatir
                            print(f"{yatir} TL yatırıldı. Güncel bakiyeniz = {bakiye}")
                            break
                        else:
                            print("Geçersiz miktar")
                elif islem == 3:
                    while True:
                        gonder = int(input("Göndermek istediğiniz miktarı yazınız = "))
                        hesapNo = input("Göndermek istediğiniz hesabı yazınız = ")
                        if gonder < bakiye:
                            print(f"{hesapNo} hesabına {gonder} TL miktarında para gönderilecektir. Onaylıyor musunuz? ")
                            while True:
                                onay = input("E/H = ")
                                if onay == "E":
                                    bakiye -= gonder
                                    print(f"İşlem onaylandı. Güncel bakiyeniz = {bakiye}")
                                    break
                                elif onay == "H":
                                    print("İşlem iptal ediliyor..")
                                    break
                                else:
                                    print("Geçersiz işlem")
                            break
                        else: 
                            print("Yetersiz bakiye")
                elif islem == 4:
                    print(f"Güncel bakiyeniz {bakiye}")
                elif islem == 5:
                    if borc > 0:
                        print(f"Mevcut borcunuz = {borc} TL")
                        while True:
                            borcum = int(input("Yatırmak istediğiniz miktarı giriniz = "))
                            if borcum <= bakiye:
                                if borcum <= borc:
                                    bakiye -= borcum
                                    borc -= borcum
                                    print(f"{borcum} TL borç ödendi.Güncel borç {borc} TL. Kalan bakiye {bakiye} TL")
                                    break
                                else:
                                    print("Fazla yatırdınız")
                            else:
                                print("Bakiye yetersiz")
                    else:
                        print("Borcunuz bulunmuyor")
                elif islem == 6:
                    hakkim = 3
                    while True:
                        eskiSifre = input("Mevcut şifrenizi giriniz")
                        hakkim -= 2
                        if eskiSifre == sifrem:
                            yeniSifre = input("Yeni şifrenizi giriniz")
                            if sifrem in yeniSifre:
                                print("Yeni şifreniz eski şifrenize benzer")
                            else:
                                sifrem = yeniSifre
                                print("Şifreniz güncellendi")
                                break
                        elif hakkim ==0:
                            print("Hakkınız bitti. Daha sonra tekrar deneyiniz")
                            break
                        else:
                            print("Hatalı şifre")
                elif islem == 7:
                    if kredi > 0:
                        while True:
                            krediCek = int(input("Çekmek istediğiniz miktarı giriniz = "))
                            if krediCek <= kredi:
                                borc += krediCek
                                bakiye +=krediCek
                                kredi -= krediCek
                                print(f"Çekilen kredi {krediCek} TL.Güncel borç{borc} TL.Kalan kredi limiti{kredi}.Güncel bakiye {bakiye}")
                                break
                            else:
                                print("Kredi limitini aştınız")
                    else:
                        print("Krediniz kalmadı")
                elif islem == 8:
                    print(f"Güncel borcunuz = {borc} TL")
                elif islem == 9:
                    print(f"Kredi limitiniz = {kredi} TL")
                elif islem == 0:
                    print("Çıkış yapılıyor")   
                    break
            break
                

        elif hak == 0:
                print("Hakkınız bitti. Çıkış yapılıyor..")
                break
        elif hesap != kullaniciAdi:
            print(f"Kullanıcı adı hatalı. Kalan hakkınız {hak}")
        elif sifre != sifrem:
            print(f"Hatalı şifre.Kalan hakkınız {hak}")
atm()
