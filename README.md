
# SecretNotes

SECRET NOTES, kullanıcıların 'kriptografi' kitaplığını kullanarak mesajları güvenli bir şekilde şifrelemesine ve şifresini çözmesine olanak tanıyan Tkinter tabanlı bir Python uygulamasıdır. Uygulama, kullanıcıların şifreleme anahtarları oluşturmasına, mesajları şifrelemesine ve gerektiğinde şifrelerini çözmesine olanak tanır. Şifrelenmiş mesajlar ve anahtarlar ileride başvurmak üzere metin dosyalarına kaydedilir.



                                    
## Özellikler

- **Şifreleme Anahtarı Oluştur**: Yeni bir şifreleme anahtarı oluşturur ve bunu bir dosyaya kaydeder.
- **Mesajları Şifrele**: Kullanıcı mesajlarını şifreler ve şifrelenmiş verileri bir dosyaya kaydeder.
- **Mesajların Şifresini Çöz**: Saklanan şifreleme anahtarını kullanarak mesajların şifresini çözer.
- **Kullanıcı Dostu Arayüz**: Tkinter ile oluşturulmuş basit ve sezgisel GUI.


  
## Kurulum:
1. Depoyu klonlayın (Clone the repository):
    git clone https://github.com/gulbahar-donmez/SecretNotes

    cd SecretNotes
    
2. Gerekli Kütüphaneleri yükleyin (Install the required libraries):
   
    pip install cryptography   

3. Uygulamayı çalıştırın (Run the application):
      python secret_notes.py   


## Kullanım

1. **Anahtar Oluştur**: Yeni bir şifreleme anahtarı oluşturmak için "Kaydet ve Şifrele"ye tıklayın. Anahtar 'key.txt' olarak kaydedilecektir.

2. **Bir Mesajı Şifreleyin**:
 - "Başlığı Giriniz" giriş kutusuna bir başlık girin.
 - Metin alanına gizli mesajınızı girin.
 - Mesajı şifrelemek ve kaydetmek için "Kaydet ve Şifrele" seçeneğine tıklayın.

3.**Bir Mesajın Şifresini Çözün**:
 - "Şifre Anahtarını Giriniz" giriş kutusuna şifreleme anahtarını girin.
 - Şifresini çözmek istediğiniz mesajın başlığını "Başlığı Giriniz" giriş kutusuna girin.
 - Mesajın şifresini çözmek ve görüntülemek için "Şifreyi Çöz"e tıklayın.

 ## Dosya Yapısı
- 'secret_notes.py': Ana uygulama komut dosyası.
- 'key.txt': Oluşturulan şifreleme anahtarlarının depolandığı dosya.
- 'encrypted_message.txt': Şifrelenmiş mesajların kaydedildiği dosya.
- 'topsecret.png': Uygulamada görüntülenecek isteğe bağlı bir görüntü.

## Sorun Giderme
- **Görüntü Dosyası Bulunamadı**: 'topsecret.png' görüntü dosyasının 'secret_notes.py' ile aynı dizinde olduğundan emin olun. Aksi takdirde, komut dosyasındaki yolu güncelleştirin.
- **Geçersiz Anahtar Hatası**: Girilen anahtarın doğru ve uygun biçimde olduğundan emin olun.
- **Dosya Bulunamadı**: 'key.txt' ve 'encrypted_message.txt'ın 'secret_notes.py' ile aynı dizinde olduğundan emin olun.



  
## Kullanılan Teknolojiler

**İstemci:**  
- Python 3.x
- tkinter kütüphanesi (genellikle Python'a dahildir)
- cryptography kütüphanesi 

**ide:** PyCharm

  
## Katkı
Projeye katkıda bulunmak isterseniz, lütfen depoyu çatallayın (fork) ve değişikliklerinizle bir çekme isteği (pull request) oluşturun. Projenin kodlama standartlarına uymayı ve değişiklikleriniz için testler eklemeyi unutmayın.


  
