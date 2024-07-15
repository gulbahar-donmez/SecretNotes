import tkinter as tk
from cryptography.fernet import Fernet
from tkinter import messagebox


# Function to generate a new key and save it to key.txt
def anahtarOlustur():
    global key1
    key1 = Fernet.generate_key()

    with open("key.txt", "ab") as file:
        file.write(key1 + b"\n")

    status_label.config(text="Anahtar oluşturuldu ve kaydedildi.")


# Function to read all keys from key.txt
def anahtariOku():
    global keys
    key_input = key_entry.get().strip()
    if key_input:
        try:
            key1 = key_input.encode()
            Fernet(key1)  # Check if the key is valid
            keys = [key1]
            return True
        except Exception as e:
            status_label.config(text=f"Geçersiz anahtar girdisi: {str(e)}")
            return False
    try:
        with open("key.txt", "rb") as file:
            keys = file.read().splitlines()
        return True
    except FileNotFoundError:
        status_label.config(text="Anahtar dosyası bulunamadı. Lütfen önce anahtar oluşturun.")
        return False


# Function to encrypt a message
def sifreleme():
    if not anahtariOku():
        return

    title = baslik_entry.get().strip()
    message = gizli_entry.get("1.0", tk.END).strip()

    if not title or not message:
        messagebox.showerror("Hata", "Başlık ve mesaj boş bırakılamaz.")
        return

    try:
        f = Fernet(keys[-1])  # Use the latest key for encryption

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

        gizli_entry.delete("1.0", tk.END)
        entered_title = baslik_entry.get().strip()

        if entered_title == "":
            status_label.config(text="Lütfen başlık giriniz.")
            return

        found = False
        for encrypted_message in encrypted_messages:
            for key in keys:
                try:
                    f = Fernet(key)
                    cozulmus = f.decrypt(encrypted_message.strip())
                    cozulmus_mesaj = cozulmus.decode()
                    title, message = cozulmus_mesaj.split("\n", 1)

                    if title == entered_title:
                        gizli_entry.insert(tk.END, message + "\n")
                        status_label.config(text="Mesaj başarıyla çözüldü.")
                        found = True
                        break
                except Exception:
                    continue
            if found:
                break

        if not found:
            status_label.config(text="Başlık veya anahtar hatalı.")
    except Exception as e:
        status_label.config(text="Şifre çözmede hata: " + str(e))


window = tk.Tk()
window.title("SECRET NOTES")
window.minsize(width=500, height=500)

# Image display (assuming the image path is correct)
try:
    img = tk.PhotoImage(file='topsecret.png')
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
