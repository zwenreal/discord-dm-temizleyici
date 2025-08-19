import tkinter as tk
from tkinter import messagebox

# Bu GUI, güvenlik nedeniyle kullanıcı tokeni yerine
# Discord bot tokeni ile çalışacak şekilde tasarlanmıştır.
# Kullanıcı tokenleri, Discord'un hizmet şartlarına aykırıdır
# ve hesabınızın kapatılmasına neden olabilir.

def start_bot():
    """
    Kullanıcının girdiği bot tokeni ve alıcı ID'sini alır.
    Botun başlatılması ve mesaj silme işlemleri için buraya kod yazılır.
    """
    bot_token = token_entry.get()
    dm_user_id = user_id_entry.get()

    if not bot_token or not dm_user_id:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
        return

    # Güvenlik notu: Gerçek bir bot projesinde bu bilgiler
    # doğrudan koda gömülmemeli, daha güvenli bir şekilde saklanmalıdır.

    # Bu kısım, botun mesaj silme mantığının başlayacağı yerdir.
    # Bu projede sadece girdi bilgilerini yazdırıyoruz.
    print("-" * 30)
    print("Bot Paneli Başlatılıyor...")
    print(f"Bot Token: {bot_token}")
    print(f"DM Silinecek Kullanıcı ID'si: {dm_user_id}")
    print("Mesajlar silinmeye hazır... (Bu, sadece bir başlangıç şablonudur)")
    print("-" * 30)

    # Örnek: `discord.py` kütüphanesini kullanarak botu başlatmak için:
    # client = discord.Client()
    # @client.event
    # async def on_ready():
    #     user = await client.fetch_user(dm_user_id)
    #     dm_channel = await user.create_dm()
    #     async for message in dm_channel.history(limit=200):
    #         if message.author == client.user:
    #             await message.delete()
    # client.run(bot_token)


# Ana pencereyi oluştur
root = tk.Tk()
root.title("Discord DM Temizleyici (Zween was here)")
root.geometry("400x200")
root.resizable(False, False)

# Pencereyi ortala
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f"+{position_right}+{position_down}")


# Bot Tokeni için etiket ve giriş alanı
token_label = tk.Label(root, text="Bot Tokeni:")
token_label.pack(pady=(20, 0))
token_entry = tk.Entry(root, width=50)
token_entry.pack(pady=5)

# DM Kullanıcı ID'si için etiket ve giriş alanı
user_id_label = tk.Label(root, text="DM Silinecek Kullanıcı ID'si:")
user_id_label.pack()
user_id_entry = tk.Entry(root, width=50)
user_id_entry.pack(pady=5)

# Başlat butonu
start_button = tk.Button(root, text="İşlemi Başlat", command=start_bot)
start_button.pack(pady=10)

# GUI'yi başlat
root.mainloop()
