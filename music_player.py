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

#labels
Label(master,text="My Playlist",font=("ariel",15),fg="#7E019A").grid(sticky="N",row=0,padx=120)
Label(master,text="Volume",font=("ariel",15),fg="#7E019A").grid(sticky="N",row=4,padx=120)
song_title_label = Label(master,font=("ariel",12))
song_title_label.grid(sticky="N",row=3)
volume_label = Label(master,font=("ariel",12))
volume_label.grid(sticky="N",row=5)

#buttons
Button(master, text="Select Song", font=("ariel",12),command=play_song).grid(row=2,sticky="N")
Button(master, text="Pause", font=("ariel",12),command=pause).grid(row=3,sticky="E")
Button(master, text="Resume", font=("ariel",12),command=resume).grid(row=3,sticky="W")  
Button(master, text="-", font=("ariel",12),width=5,command=reduce_volume).grid(row=5,sticky="W")
Button(master, text="+", font=("ariel",12),width=5,command=increase_volume).grid(row=5,sticky="E")

master.mainloop()
