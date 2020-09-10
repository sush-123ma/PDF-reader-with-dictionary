from tkinter import *
from tkinter.ttk import *
import os
from tkinter import messagebox
from PIL import Image,ImageTk
from pdf2image import convert_from_path
from PyDictionary import PyDictionary
from spellchecker import SpellChecker
def press():
  #Get the data  from Entry Box
  k=e.get()
  sp=SpellChecker()
  d={}
  #Corrects the spelling incase any mistake
  i=sp.correction(k)
  d=PyDictionary()
  m=d.meaning(i)
  s=''
  try:
   for key,val in m.items():
    s=s+key+":"+','.join(val)
    s=s+'\n'
  except:
      #if length of word greater than 1
     return messagebox.showerror("Results Not Found","check the word again")
  #displays meaning of the word
  messagebox.showinfo("Meaning of "+i,s)
root = Tk()
#Directory setting
os.chdir("")
# Creating the frame for searching
fr=Frame(root,width=1200,height=40)
l=Label(fr,text="PDF VIEWER",font=("calibre",16,'bold'))
l.pack(side=LEFT)
#Entry of the data to be searched
e=Entry(fr,width=25,font=("calibre",16,"italic"))
e.pack(side=RIGHT,ipady=10)
#placing a placeholder intial
e.insert(0,'Search Word')
e.configure(state=DISABLED)
def on_click(event):
  e.configure(state=NORMAL)
  e.delete(0,END)
  e.unbind('<Button-1>',on_click_id)
#placing search icon image on button
ph=PhotoImage(file =r'E:\I CAN DO IT\search-icon2.png')
#resizing the image
photoimage=ph.subsample(15,20)
b=Button(fr,image=photoimage,command=press)
#placing the button
b.pack(side=RIGHT)
fr.pack(fill=X)
#Creating a frame for pdf 
pdf_frame = Frame(root)
pdf_frame.pack(side=TOP,fill=BOTH,expand=1)

# Adding Scrollbar to the PDF frame
scrol_y = Scrollbar(pdf_frame,orient=VERTICAL)
# Adding text widget for inserting images
pdf = Text(pdf_frame,yscrollcommand=scrol_y.set,bg="grey")
# Setting the scrollbar to the right side
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=pdf.yview)
# Finally packing the text widget
pdf.pack(fill=BOTH,expand=1)
# Here the PDF is converted to list of images
pages = convert_from_path('FilePath',size=(1200,900),poppler_path=r"C:\Users\sushma\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\poppler-0.68.0\bin")
photos = []
# Storing the converted images into list
for i in range(len(pages)):
  photos.append(ImageTk.PhotoImage(pages[i]))
# Adding all the images to the text widget
for photo in photos:
  pdf.image_create(END,image=photo)
  
  # For Seperating the pages
  pdf.insert(END,'\n\n')
# Ending of mainloop
on_click_id=e.bind('<Button-1>',on_click)
mainloop()
 
