import tkinter as tk
from cryptography.fernet import Fernet


# Function to generate a new key and save it to key.txt
def anahtarOlustur():
    global key1
    key1 = Fernet.generate_key()

    with open("key.txt", "wb") as file:
        file.write(key1)

    status_label.config(text="Anahtar oluşturuldu ve kaydedildi.")


# Function to read the key from key.txt
def anahtariOku():
    global key1
    key_input = key_entry.get().strip()
    if key_input:
        try:
            key1 = key_input.encode()
            Fernet(key1)  # Check if the key is valid
            return True
        except Exception as e:
            status_label.config(text=f"Geçersiz anahtar girdisi: {str(e)}")
            return False
    try:
        with open("key.txt", "rb") as file:
            key1 = file.read()
        return True
    except FileNotFoundError:
        status_label.config(text="Anahtar dosyası bulunamadı. Lütfen önce anahtar oluşturun.")
        return False


# Function to encrypt a message
def sifreleme():
    if not anahtariOku():
        return

    try:
        f = Fernet(key1)
        title = baslik_entry.get().strip()
        message = gizli_entry.get("1.0", tk.END).strip()
        if message == "" or title == "":
            status_label.config(text="Başlık ve mesaj boş bırakılamaz.")
            return

        combined_message = f"{title}\n{message}"
        x = combined_message.encode()
        sifre = f.encrypt(x)

        with open("encrypted_message.txt", "ab") as file:
            file.write(sifre + b"\n")

        gizli_entry.delete("1.0", tk.END)
        baslik_entry.delete(0, tk.END)
        status_label.config(text="Mesaj şifrelendi ve kaydedildi.")
    except Exception as e:
        status_label.config(text="Şifrelemede hata: " + str(e))


# Function to decrypt messages
def cozme():
    if not anahtariOku():
        return

    try:
        with open("encrypted_message.txt", "rb") as file:
            encrypted_messages = file.readlines()

        f = Fernet(key1)
        gizli_entry.delete("1.0", tk.END)
        entered_title = baslik_entry.get().strip()

        if entered_title == "":
            status_label.config(text="Lütfen başlık giriniz.")
            return

        found = False
        for encrypted_message in encrypted_messages:
            try:
                cozulmus = f.decrypt(encrypted_message.strip())
                cozulmus_mesaj = cozulmus.decode()
                title, message = cozulmus_mesaj.split("\n", 1)

                if title == entered_title:
                    gizli_entry.insert(tk.END, message + "\n")
                    status_label.config(text="Mesaj başarıyla çözüldü.")
                    found = True
                    break
            except Exception as e:
                status_label.config(text=f"Şifre çözmede hata: {str(e)}")

        if not found:
            status_label.config(text="Başlık veya anahtar hatalı.")
    except Exception as e:
        status_label.config(text="Şifre çözmede hata: " + str(e))


window = tk.Tk()
window.title("SECRET NOTES")
window.minsize(width=500, height=500)

# Image display (assuming the image path is correct)
try:
    img = tk.PhotoImage(file='C:\\Users\\Gulbahar-NB\\Desktop\\Resimler\\topsecret.png')
    tk.Label(image=img).pack()
except tk.TclError:
    print("Image file not found or format not supported.")

baslik = tk.Label(text="Başlığı Giriniz")
baslik.pack()
baslik_entry = tk.Entry(width=50)
baslik_entry.pack()

gizli = tk.Label(text="Gizli mesajınızı giriniz:")
gizli.pack()
gizli_entry = tk.Text(window, width=50, height=10)
gizli_entry.pack()

encrypt_button = tk.Button(text="Kaydet ve Şifrele", command=lambda: [anahtarOlustur(), sifreleme()])
encrypt_button.pack()

key_label = tk.Label(text="Şifre Anahtarını Giriniz:")
key_label.pack()
key_entry = tk.Entry(width=50)
key_entry.pack()

decrypt_button = tk.Button(text="Şifreyi Çöz", command=cozme)
decrypt_button.pack()

status_label = tk.Label(text="")
status_label.pack()

window.mainloop()
