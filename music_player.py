from pygame import mixer
from tkinter import Tk
from tkinter import Label 
from tkinter import Button
from tkinter import filedialog

current_volume = float(0.5)

#functions
def play_song():
    filename = filedialog.askopenfilename(initialdir="C:/",title="Please select a file")
    current_song = filename
    song_title   = filename.split("/")
    song_title   = song_title[-1]
    print(song_title)

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="#7E019A",text="Now playing : " + str(song_title))
        volume_label.config(fg="#7E019A",text="Volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Error playing song")

def reduce_volume():
    try:
        global current_volume
        if current_volume <=0:
            volume_label.config(fg="red", text="Volume : Muted")
            return
        current_volume = current_volume - float(0.10)
        current_volume - round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Track hasnt been selected yet")

def increase_volume():
    try:
        global current_volume
        if current_volume >=1:
            volume_label.config(fg="green", text="Volume : Max")
            return
        current_volume = current_volume + float(0.1)
        current_volume - round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Track hasnt been selected yet")
def pause():
        try:
            mixer.music.pause()
        except Exception as e:
            print(e)
            song_title_label.config(fg="red",text="Track hasnt been selected yet")
def resume():
        try:
            mixer.music.unpause()
        except Exception as e:
            print(e)
            song_title_label.config(fg="red",text="Track hasnt been selected yet")

#main screen
master = Tk()
master.title("Tuneify")
master.geometry("900x600")

#labels
headline_label = Label(master,text="My Playlist",font=("ariel",17),fg="#7E019A")
headline_label.place(x=400, y=10)
#volume_label = Label(master,text="Volume",font=("ariel",17),fg="#7E019A")
#volume_label.place(x=415,y=200)
song_title_label = Label(master,font=("ariel",10))
song_title_label.place(x=350,y=140)
volume_label = Label(master,font=("ariel",17))
volume_label.place(x=385,y=200)

#buttons
select_song = Button(master, text="Select Song", font=("ariel",17),command=play_song)
select_song.place(x=385,y=50)
Pause = Button(master, text="Pause", font=("ariel",17),command=pause)
Pause.place(x=220,y=140)
Resume = Button(master, text="Resume", font=("ariel",17),command=resume)
Resume.place(x=600,y=140)
Volume_down = Button(master, text="-", font=("ariel",17),width=5,command=reduce_volume)
Volume_down.place(x=600,y=200)
Volume_up = Button(master, text="+", font=("ariel",17),width=5,command=increase_volume)
Volume_up.place(x=230,y=200)


master.mainloop()

