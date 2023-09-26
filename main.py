
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage  # Resim eklemek için PhotoImage kullanılır
from PIL import Image, ImageTk
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.hash import sha256_crypt
from music_player import *

# SQLite veritabanı oluşturmaimport tkinter as tk
engine = create_engine('sqlite:///user.db', echo=False)
Base = declarative_base()

# Kullanıcı bilgilerini temsil eden veritabanı tablosu
class User(Base):
 __tablename__ = 'users'
 id = Column(Integer, primary_key=True) 
 username = Column(String, unique=True) # eşsiz
 password = Column(String)

 Base.metadata.create_all(engine)

# Tkinter uygulaması oluşturma
app = tk.Tk()
app.title("Login")
app.geometry("1000x600")

# Arka plan resmini eklemek için ImageTk kullanımı
bg_image = Image.open("images/p1.png") # Arka plan resmi dosyasının adını ve yolunu belirtin
bg_image = bg_image.resize((1000, 600), Image.BILINEAR)  # Resmi pencere boyutuna uygun olarak yeniden boyutlandırın
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Giriş bilgileri giriş kutuları



username_label = tk.Label(app, text="User name:", font=("Helvetica", 10))
username_label.place(x=370,y=370)

username_entry = tk.Entry(app, font=("Helvetica", 10))
username_entry.place(x=370,y=390)

password_label = tk.Label(app, text="Password:", font=("Helvetica", 10))
password_label.place(x=520,y=370)

password_entry = tk.Entry(app, show="*", font=("Helvetica", 10))
password_entry.place(x=520,y=390)


# Kullanıcıyı veritabanına kaydetme işlemi
def save_user():
   username = username_entry.get()
   password = password_entry.get()

   # Şifreyi güvenli bir şekilde hashleme
   hashed_password = sha256_crypt.hash(password)

   # SQLAlchemy ile kullanıcı bilgilerini veritabanına kaydetme
   Session = sessionmaker(bind=engine)
   session = Session()
   try:
      new_user = User(username=username, password=hashed_password)
      session.add(new_user)
      session.commit() # kayıt etti
      session.close()
      messagebox.showinfo("Başarılı", "Kullanıcı başarıyla kaydedildi.")
   except:
      messagebox.showerror("Hata", "Kullanıcı kayıt edilemedi!")

# Kullanıcının veritabanına giriş işlemi
def login():
   username = username_entry.get()
   password = password_entry.get()

 # SQLAlchemy ile kullanıcı bilgilerini veritabanından sorgulama
   Session = sessionmaker(bind=engine)
   session = Session()

   user = session.query(User).filter_by(username=username).first()

   if user and sha256_crypt.verify(password, user.password):
      messagebox.showinfo("Başarılı", "Giriş başarılı!")
      liste = app.place_slaves()
      for l in liste:
          l.destroy() # yok et
      if user.username == "Mustafa":
         Admin_app = master()
   
   else:
      messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")
   session.close()        
  
  
  
# Kaydet ve Giriş butonları
save_button = tk.Button(app, text="Save", command=save_user, font=("Helvetica", 10))
save_button.place(x=450,y=450)

login_button = tk.Button(app, text="Enter   ", command=login, font=("Helvetica", 10))
login_button.place(x=500,y=450)



# Tkinter uygulamasını başlatma
app.mainloop()                               