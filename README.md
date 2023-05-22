#   Python E-Okul Projesi

##  Amaç Ne?

- Bu projenin ana amacı ülkemizde halihazırda kullandığımız e-okul sistemini python ve veritabanına uyarlanarak yeniden oluşturmaktır. Daha sonradan bu projeyi geliştirip web üzerinde backend ve mysql e dönüştürüp dershanelere kullanıma açmayı planlamaktayım.

##  Sistem Nasıl Çalışıyor?

- Sistemde öğrenci, öğretmen ve yetkili girişi olmak üzere 3 giriş bulunmakta. Herkesin girişi farklı olduğu için çok daha fazla kişinin kullanılabilmesi amaçlanmakta. 

- Her grubun kendilerine ait kullanıcı adları bulunmakta. Bu kullanıcı adları eşsizdir. Tabi aynı kullanıcı adı hem öğrencide hem öğretmende hem de yetkilide bulunabilir. Bu özellikle bilerek yapılmış bir sistemdir çünkü sistem aynı kullanıcı adlarına sahip olsalar bile işleyiş bakımından kafa karışıklığını önlüyor.

##  Hangi Grupta Hangi Özellikler Bulunuyor?

### Öğrenciler İçin Özellikler

- Öğrenciler için notlarım, devamsızlıklarım ve öğretmenleriyle iletişime geçebilmeleri için öğretmenlerin kişisel olmayan bilgilerinin bulunduğu bir liste ortaya çıkmakta. 

- Notlarım kısmından şu anda yalnızca 3 adet sınav notu için alan sağlanmıştır ancak bu ilerleyen süreçte geliştirilecektir.

- Devamsızlık kısmından öğrenciler devamsızlık gün sayılarını görebilmektedir ancak bu da hangi gün devamsızlık yaptığı çeşitli güncellemelerle geliştirilecektir.

- Öğretmenler ile iletişime geç kısmında öğrenciler için öğretmenlerin kullanıcı adları, ad ve soyadları, mail adresleri listelenir. Bu sayede öğrenciler mail yolu ile öğretmenlerine ulaşabilirler.

- Şifremi değiştir kısmından öğrenciler kendi öğrenci şifrelerini değiştirebilir.

- Güvenli çıkış seçeneğini kullanarak uygulamadan çıkış yapabilirler.

### Öğretmenler İçin Özellikler

- Öğretmenlerin ekranında öğrenci notları düzenle, öğrenci devamsızlıklarını düzenle, öğrenciler ile iletişime geç, öğretmenler ile iletişime geç, yetkili bilgilerini gör gibi seçenekler bulunmakta.

- Öğrenci notlarını düzenle ekranından öğretmenler öğrencilerin kullanıcı adlarını girerek notlarını değiştirebilir ve not girişi yapabilirler.

- Öğrenci devamsızlıklarını düzenle ekranından öğretmenler öğrencilere devamsızlık ekleyip var olan devamsızlık gün sayılarını öğrenebilirler ancak silemezler.

- Öğrenci bilgileri ekranından öğrencilerin kullanıcı adı, ad ve soyadı, okul nosu, mail adresi ve telefon numaralarını görebilir. Bu sayede öğrencilere her yoldan ulaşabilirler.

- Öğretmen bilgileri ekranından öğretmenlerin kullanıcı adı, ad ve soyadı, mail adresleri ve telefon numaralarını görebilirler. Bu sayede öğretmenler kendi aralarında rahatça iletişim kurabilirler.

- Yetkili bilgileri ekranından yetkililerin kullanıcı adı, mail adresi, ad ve soyadını görebilirler. Bu sayede mail yoluyla yetkililere ulaşabilirler.

- Bunların yanı sıra öğrencilerde olduğu gibi şifremi değiştir ve güvenli çıkış olanağı sunulmaktadır.

### Yetkililer İçin Özellikler

- Yetkililerde öğrenci, öğretmen ve yetkililer için 3 ayrı menü bulunmakta.

- Öğrenci menüsünden her türlü not düzenleme, devamsızlık düzenleyip silme, öğrenci bilgileri güncelleme, öğrenci kayıt etme, kayıt silme gibi işlemleri yapabilirler.

- Öğretmen menüsünden her türlü öğretmen kayıt etme, öğretmen kayıt düzenleme, öğretmen listesini görme ve öğretmen kaydı silme gibi işlemleri yapabilirler.

- Yetkili menüsünden her türlü yetkili kayıt etme, yetkili kayıt düzenleme, yetkili listesini görme ve yetkili kaydı silme gibi işlemleri yapabilirler.

## Giriş İçin Öğrenci, Öğretmen ve Yetkili Bilgileri

### Öğrenci Giriş Bilgileri

- Kullanıcı adı : gotunc
- Şifre : 12345678

- Kullanıcı adı : oakbulak
- Şifre : 123

### Öğretmen Giriş Bilgileri

- Kullanıcı adı : ysensoy
- Şifre : 12345678

### Yetkili Giriş Bilgileri

- Kullanıcı adı : ytunc
- Şifre : asdasd

## Planlanan Güncellemeler

- Öğrenciler öğretmen ve yetkililere mesaj atabilecek ve konuşma sağlayabilecek ve konuşmalar datetime modulü ile orantılı kullanılarak bir sohbet odası gibi kullanılabilecek.

- Öğrenciler için sınıf oluşturulacak.

- Öğrencilerin devamsızlıkları gün ile desteklenerek tablo şeklinde gösterilecek.

- Sınavlar daha geliştirilerek sözlü gibi kavramlar eklenip 1.dönem ve 2.dönem olarak ayrıştırılabilecek.

## Bazı Ekran Görüntüleri

- YAKINDA EKLENECEKTIR!!!