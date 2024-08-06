""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
import poke_api
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("Pokemon Information")
#root.geometry("500x500")
# TODO: Create the frames
frame1 = Frame(root)
frame1.grid(row=0,column=0, columnspan=2, padx=20, pady=20)

frame2 = LabelFrame(root, text="info")
frame2.grid(row=1,column=0,padx=20, pady=20)

frame3 = LabelFrame(root, text="stat")
frame3.grid(row=1,column=1,padx=20, pady=20)

def update_value():
  value = label2.get()
  data = poke_api.get_pokemon_info(value)
  height_val['text'] = f"{data['height']}" + " dm"
  weight_val['text'] = f"{data['weight']}" + " hg"
  L = []

  for i in data['types']:
    L.append(i['type']['name'])
    str_val = ",".join(L)
    type_val['text']= str_val
    hp_progress['value'] = data['stats'][0]['base_stat']
    attack_progress['value'] = data['stats'][1]['base_stat']
    defence_progress['value'] = data['stats'][2]['base_stat']
    special_attack_progress['value'] = data['stats'][3]['base_stat']
    special_defence_progress['value'] = data['stats'][4]['base_stat']
    speed_progress['value'] = data['stats'][5]['base_stat'] 

def errormsg():
    value = label2.get()
    small_val = value.lower()
    cap_val = small_val.capitalize()
    messagebox.showerror(message=f'Unable to fetch information for {cap_val} from the PokeAPI',icon='error',title='Error')

# TODO: Define button click event handler function

def button_click():
  value = label2.get()
  if poke_api.get_pokemon_info(value) == None :
    errormsg()
  else:
    update_value()


# TODO: Populate the user input frame with widgets

label1 = Label(frame1,text="Pokemon Name")
label1.grid(row=0,column=0, padx=5, pady=5)

label2 = Entry(frame1)
label2.grid(row=0,column=1, padx=5, pady=5)

label3 = Button(frame1,text="Get info",command = button_click)
label3.grid(row=0,column=2, padx=5, pady=5)



#widget for "info_frame"

height_label = Label(frame2,text="Height")
height_label.grid(row=0,column=0, padx=5, pady=5, sticky="E")
weight_label = Label(frame2,text="Weight")
weight_label.grid(row=1,column=0, padx=5, pady=5, sticky="E")
type_label = Label(frame2,text="Type")
type_label.grid(row=2,column=0, padx=5, pady=5, sticky="E")

height_val = Label(frame2)
height_val.grid(row=0,column=2, padx=5, pady=5, sticky="E")
weight_val = Label(frame2)
weight_val.grid(row=1,column=2, padx=5, pady=5, sticky="E")
type_val = Label(frame2)
type_val.grid(row=2,column=2, padx=5, pady=5, sticky="E")

#widget for "stat_frame"
hp_val = Label(frame3,text="HP:")
hp_val.grid(row=0,column=2, padx=5, pady=5, sticky="E")
attack_val = Label(frame3,text="Attack:")
attack_val.grid(row=1,column=2, padx=5, pady=5, sticky="E")
defense_val = Label(frame3,text="Defence:")
defense_val.grid(row=2,column=2, padx=5, pady=5, sticky="E")

spl_attack_val = Label(frame3,text="Special Attack:")
spl_attack_val.grid(row=3,column=2, padx=5, pady=5, sticky="E")
spl_defence_val = Label(frame3,text="Special Defence:")
spl_defence_val.grid(row=4,column=2, padx=5, pady=5, sticky="E")
speed_val = Label(frame3,text="Speed:")
speed_val.grid(row=5,column=2, padx=5, pady=5, sticky="E")


hp_progress = ttk.Progressbar(frame3, length=200, max=250)
hp_progress.grid(row=0,column=3, padx=5, pady=5)
attack_progress = ttk.Progressbar(frame3, length=200, max=250)
attack_progress.grid(row=1,column=3, padx=5, pady=5)
defence_progress = ttk.Progressbar(frame3, length=200, max=250)
defence_progress.grid(row=2,column=3, padx=5, pady=5)
special_attack_progress = ttk.Progressbar(frame3, length=200, max=250)
special_attack_progress.grid(row=3,column=3, padx=5, pady=5)
special_defence_progress = ttk.Progressbar(frame3, length=200, max=250)
special_defence_progress.grid(row=4,column=3, padx=5, pady=5)
speed_progress = ttk.Progressbar(frame3, length=200, max=250)
speed_progress.grid(row=5,column=3, padx=5, pady=5)

root.mainloop()