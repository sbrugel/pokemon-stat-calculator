from tkinter import *
from tkinter import ttk
from math import *

root = Tk() # creates the window
root.title('Stat Calculator')
root.geometry('250x390')

gen = StringVar(root, "old") # generation selected variable (either old or new)
nature = StringVar()

def calculate(): # if main button clicked
    if (gen.get() == 'old'): # 1-2
        pass
    else: # 3+
        # 0 - no stat, 1 - HP, 2 - Atk, 3 - Def, 4 - SpAtk, 5 - SpDef, 6 - Spd
        # stat changes for each nature
        # 1st character: increased stat
        # 2nd character: decreased stat
        # REFER TO THE NATURE ARRAY BELOW THIS
        natureChanges = {
            0: '24',
            1: '00',
            2: '32',
            3: '26',
            4: '52',
            5: '54',
            6: '00',
            7: '53',
            8: '00',
            9: '63',
            10: '34',
            11: '64',
            12: '35',
            13: '23',
            14: '43',
            15: '42',
            16: '65',
            17: '25',
            18: '46',
            19: '00',
            20: '45',
            21: '36',
            22: '56',
            23: '00',
            24: '62'
        }
        hp = floor((((2*int(base1.get())+int(iv1.get())+(floor(int(ev1.get())/4)))*int(level.get()))/100) + int(level.get()) + 10)

        multiplier = getMultiplier(natureChanges, 2)
        atk = floor(((((2*int(base2.get())+int(iv2.get())+(floor(int(ev2.get())/4)))*int(level.get()))/100)+5)*multiplier)
        multiplier = getMultiplier(natureChanges, 3)
        df = floor(((((2*int(base3.get())+int(iv3.get())+(floor(int(ev3.get())/4)))*int(level.get()))/100)+5)*multiplier)
        multiplier = getMultiplier(natureChanges, 4)
        spatk = floor(((((2*int(base4.get())+int(iv4.get())+(floor(int(ev4.get())/4)))*int(level.get()))/100)+5)*multiplier)
        multiplier = getMultiplier(natureChanges, 5)
        spdf = floor(((((2*int(base5.get())+int(iv5.get())+(floor(int(ev5.get())/4)))*int(level.get()))/100)+5)*multiplier)
        multiplier = getMultiplier(natureChanges, 6)
        spd = floor(((((2*int(base6.get())+int(iv6.get())+(floor(int(ev6.get())/4)))*int(level.get()))/100)+5)*multiplier)

        res1.configure(text="HP: " + str(hp))
        res2.configure(text="Atk: " + str(atk))
        res3.configure(text="Def: " + str(df))
        res4.configure(text="SpAtk: " + str(spatk))
        res5.configure(text="SpDef: " + str(spdf))
        res6.configure(text="Spd: " + str(spd))
    
def getMultiplier(natureChanges: dict, stat: int):
    if int(natureChanges[natureDrop.current()][0]) == stat: # is the stat being raised by this nature match the current stat we're looking for?
        return 1.1
    if int(natureChanges[natureDrop.current()][1]) == stat: # is the stat being lowered by this nature match the current stat we're looking for?
        return 0.9
    return 1.0 # neutral

# adding the components
# radio buttons for generation selection
gen1 = Radiobutton(root, text="Gen 1-2", value="old", variable=gen)
gen2 = Radiobutton(root, text="Gen 3+", value="new", variable=gen)

# headers
type = Label(root, text='Base')
iv = Label(root, text='IVs')
ev = Label(root, text='EVs')
ltitle = Label(root, text='Level:')
ntitle = Label(root, text='Nature:')

# level/nature entry
level = Entry(root, width=3)
natureDrop = ttk.Combobox(root, width=10, textvariable=nature)
nature.set("Adamant") # default option of the dropdown

# for natures (which stat is raised/lowered)
statUp = 0
statDn = 0

# Dropdown menu options
natureDrop['values'] = [
    "Adamant",
    "Bashful",
    "Bold",
    "Brave",
    "Calm",
    "Careful",
    "Docile",
    "Gentle",
    "Hardy",
    "Hasty",
    "Impish",
    "Jolly",
    "Lax",
    "Lonely",
    "Mild",
    "Modest",
    "Naive",
    "Naughty",
    "Quiet",
    "Quirky",
    "Rash",
    "Relaxed",
    "Sassy",
    "Serious",
    "Timid"
]

# 1 - HP, 2 - Atk, 3 - Def, 4 - SpAtk, 5 - SpDef, 6 - Spd
# stat titles
stat1 = Label(root, text='HP')
stat2 = Label(root, text='Attack')
stat3 = Label(root, text='Defense')
stat4 = Label(root, text='Sp Atk')
stat5 = Label(root, text='Sp Def')
stat6 = Label(root, text='Speed')

# base stat input
base1 = Entry(root, width=3)
base2 = Entry(root, width=3)
base3 = Entry(root, width=3)
base4 = Entry(root, width=3)
base5 = Entry(root, width=3)
base6 = Entry(root, width=3)

# IVs input
iv1 = Entry(root, width=3)
iv2 = Entry(root, width=3)
iv3 = Entry(root, width=3)
iv4 = Entry(root, width=3)
iv5 = Entry(root, width=3)
iv6 = Entry(root, width=3)

# EVs input
ev1 = Entry(root, width=3)
ev2 = Entry(root, width=3)
ev3 = Entry(root, width=3)
ev4 = Entry(root, width=3)
ev5 = Entry(root, width=3)
ev6 = Entry(root, width=3)

# calculation button and results
btn = Button(root, text="Calculate", fg="red", command=calculate)
res1 = Label(root, text="")
res2 = Label(root, text="")
res3 = Label(root, text="")
res4 = Label(root, text="")
res5 = Label(root, text="")
res6 = Label(root, text="")

# component placement
gen1.grid(column=0, row=0)
gen2.grid(column=0, row=1)

ltitle.grid(column=0, row=3)
level.grid(column=1, row=3)
ntitle.grid(column=2, row=3)
natureDrop.grid(column=3, row=3)

stat1.grid(column=0, row=5)
stat2.grid(column=0, row=6)
stat3.grid(column=0, row=7)
stat4.grid(column=0, row=8)
stat5.grid(column=0, row=9)
stat6.grid(column=0, row=10)

type.grid(column=1, row=4)
iv.grid(column=2, row=4)
ev.grid(column=3, row=4)

base1.grid(column=1, row=5)
base2.grid(column=1, row=6)
base3.grid(column=1, row=7)
base4.grid(column=1, row=8)
base5.grid(column=1, row=9)
base6.grid(column=1, row=10)

iv1.grid(column=2, row=5)
iv2.grid(column=2, row=6)
iv3.grid(column=2, row=7)
iv4.grid(column=2, row=8)
iv5.grid(column=2, row=9)
iv6.grid(column=2, row=10)

ev1.grid(column=3, row=5)
ev2.grid(column=3, row=6)
ev3.grid(column=3, row=7)
ev4.grid(column=3, row=8)
ev5.grid(column=3, row=9)
ev6.grid(column=3, row=10)

btn.grid(column=0, row=11)
res1.grid(column=0, row=12)
res2.grid(column=0, row=13)
res3.grid(column=0, row=14)
res4.grid(column=0, row=15)
res5.grid(column=0, row=16)
res6.grid(column=0, row=17)

root.mainloop() # execute the window