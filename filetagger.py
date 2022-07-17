from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb

import os
from os import popen
import json

def pathtoid(path):
   filepath = fr"{path}"
   #print(filepath)
   output = popen(fr"fsutil file queryfileid {filepath}").read()
   l = list(output.split(" "))
   return l[3]

def idtopath(id):
   fileid = f"{id}"
   output = popen(fr"fsutil file queryfilenamebyid D:\ {fileid}").read()
   l = list(output.split(" "))
   if l[0] == "Error:":
      return l[0]
   else:
      return l[8][4:]

# Function to add tag
def add_tag():
   path = fd.askopenfilenames(title='Choose a file to add tag', filetypes=[("All files", "*.*")])
   #print(path)
   if len(path) == 0:
      mb.showinfo("File Not Selected", "No file was selected")
   else:
      fileids = list()
      for i in path:
         fileids.append(pathtoid(i))
      print(fileids)
      addtag_wn = Toplevel(root)

      if len(path) == 1:
         addtag_wn.title(f'Adding tag to file {path}')
      else:
         addtag_wn.title(f'Adding tag to multiple files')

      addtag_wn.geometry('720x240')
      addtag_wn.resizable(0,0)
      addtag_wn.grab_set()
      entry = Entry(addtag_wn, width= 40, border=2)
      entry.pack()

      def write_json(new_data, filename):
         if filename == "fileid-tags.json":
            with open(filename,'r+') as file:
               # First we load existing data into a dict.
               file_data = json.load(file)
               #print(file_data[fileid])
               # Join new_data with file_data inside emp_details

               for id in fileids:
                  if id not in file_data:
                     file_data[id] = list()
                     file_data[id].append(new_data)
                  else:
                     if new_data in file_data[id]:
                        return False
                     else:
                        file_data[id].append(new_data)

               # Sets file's current position at offset.
               file.seek(0)
               # convert back to json.
               json.dump(file_data, file)
         elif filename == "tag-fileids.json":
            with open(filename,'r+') as file:
               # First we load existing data into a dict.
               file_data = json.load(file)
               #print(file_data[fileid])
               # Join new_data with file_data inside emp_details

               if new_data not in file_data:
                  file_data[new_data] = list()
                  for id in fileids:
                     file_data[new_data].append(id)
               else:
                  for id in fileids:
                     file_data[new_data].append(id)
               
               # Sets file's current position at offset.
               file.seek(0)
               # convert back to json.
               json.dump(file_data, file)

      def display_text():
         str = entry.get()
         str = str.lower()
         str = str.strip()
         str = str.replace(" ","")
         entry.delete(0, END)
         if len(str) == 0 :
            mb.showerror(title='Error!', message='Length of tag cannot be zero.')
         elif write_json(str, "fileid-tags.json") == False:
            mb.showerror(title='Error!', message='Tag is already present')
         else:
            write_json(str, "tag-fileids.json")
            label = Label(addtag_wn, text = str)
            label.pack()

      entry.icursor(0)
      Button(addtag_wn, text = "Add tag", font=button_font, bg=button_background, width = 20, command=display_text, border=2).place(x = 450, y = 0)
      Button(addtag_wn, text = "Exit", font=button_font, bg=button_background, width = 20, command=addtag_wn.destroy, border=2).place(x = 450, y = 40)

def search_tag():
   searchtag_wn = Toplevel(root)
   searchtag_wn.title(f'Search file with tag')
   searchtag_wn.geometry('720x240')
   searchtag_wn.resizable(0,0)
   searchtag_wn.grab_set()

   entry= Entry(searchtag_wn, width= 40)
   entry.pack()

   def search_json(tag):
      with open("tag-fileids.json",'r+') as file:
         # First we load existing data into a dict.
         file_data = json.load(file)
         #print(file_data[fileid])
         # Join new_data with file_data inside emp_details

         if tag not in file_data:
            return False
         else:
            return True

   def display_files(tag):
      z = 0
      with open("tag-fileids.json",'r+') as file:
         # First we load existing data into a dict.
         file_data = json.load(file)
         #print(file_data[fileid])
         # Join new_data with file_data inside emp_details

         fileids = list()
         fileids = file_data[tag]
         listfiles = list()
         for files in fileids:
            path = idtopath(files)
            #print(path)
            path = path[::-1]
            filename = str()
            for i in path:
               if i == "\\" :
                  break
               filename = i + filename
            
            if filename != "Error:":
               listfiles.append(filename)

         displayfiles_wn = Toplevel(searchtag_wn)
         displayfiles_wn.title(f'Searched Files with {tag} tag :')
         displayfiles_wn.geometry('720x240')
         displayfiles_wn.resizable(0,0)
         displayfiles_wn.grab_set()

         listbox = Listbox(displayfiles_wn, selectbackground='SteelBlue', font=("Georgia", 10), selectmode=SINGLE)
         listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

         scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
         scrollbar.pack(side=RIGHT, fill=Y)

         listbox.config(yscrollcommand=scrollbar.set)

         while z < len(listfiles):
            listbox.insert(END, listfiles[z])
            z += 1

         def open_file(file):
            os.startfile(os.path.abspath(file))

         def selected_item():
            if len(listbox.curselection()) == 0:
               mb.showerror(title='Error!', message='No File was Selected.')
            else:
               for i in listbox.curselection():
                  str = idtopath(fileids[i])
                  str = str.strip()
                  if(os.path.exists(str)) :
                     open_file(str)
                  else:
                     mb.showerror(title='Error!', message='No such file exists! It was deleted.')
   
         Button(displayfiles_wn, text='Open File', font=button_font, bg=button_background, command=selected_item, border = 2).place(x = 270, y = 210)
         Button(displayfiles_wn, text = "Exit", font=button_font, bg=button_background, command=displayfiles_wn.destroy, border=2).place(x = 350, y = 210)

   def get_tag():
      str = entry.get()
      str = str.lower()
      str = str.strip()
      str = str.replace(" ","")
      entry.delete(0, END)
      if len(str) == 0:
         mb.showerror(title='Error!', message='Length of tag cannot be zero.')
      elif search_json(str) == False:
         mb.showerror(title='Error!', message='No file exists with given tag.')
      else:
         display_files(str)

   entry.icursor(0)
   Button(searchtag_wn, text = "Search Files", font=button_font, bg=button_background, width = 20, command=get_tag).pack(pady = 20)
   Button(searchtag_wn, text = "Exit", font=button_font, bg=button_background, width = 20, command=searchtag_wn.destroy, border=2).pack(pady = 20)

def remove_tags():
   z = 0
   path = fd.askopenfilename(title='Choose a file to add tag', filetypes=[("All files", "*.*")])
   #print(path)
   if len(path) == 0:
      mb.showinfo("File Not Selected", "No file was selected")
   else:
      fileid = pathtoid(path)
      #print(fileid)


      def get_tags():
         with open("fileid-tags.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            tags = list()
            tags = file_data[fileid]
            return tags
      
      ftags = list()
      ftags = get_tags()
      remove_wn = Toplevel(root)
      remove_wn.title(f'Removing Tags from {path}')
      remove_wn.geometry('720x240')
      remove_wn.resizable(0,0)
      remove_wn.grab_set()

      listbox = Listbox(remove_wn, selectbackground='SteelBlue', font=("Georgia", 10), selectmode=SINGLE)
      listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

      scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
      scrollbar.pack(side=RIGHT, fill=Y)

      listbox.config(yscrollcommand=scrollbar.set)

      while z < len(ftags):
         listbox.insert(END, ftags[z])
         z += 1

      def remove_tag(tag):
         with open("fileid-tags.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            file_data[fileid].remove(tag)

            if len(file_data[fileid]) == 0:
               file_data.pop(fileid)
            else:
               # Sets file's current position at offset.
               #newfile = open("new.json",'r+')
               file.truncate(0)
               file.seek(0)
               # convert back to json.
               #json.dump(file_data, newfile)
               json.dump(file_data, file)

         with open("tag-fileids.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            file_data[tag].remove(fileid)

            if len(file_data[tag]) == 0:
               file_data.pop(tag)
            else:
               # Sets file's current position at offset.
               #newfile = open("new.json",'r+')
               file.truncate(0)
               file.seek(0)
               # convert back to json.
               #json.dump(file_data, newfile)
               json.dump(file_data, file)

      def remove_item():
         if len(listbox.curselection()) == 0:
            mb.showerror(title='Error!', message='No Tag was Selected.')
         else:
            for i in listbox.curselection():
               str = ftags[i]
               remove_tag(str.strip())
               ftags.remove(ftags[i])
               listbox.delete(0, END)
               z = 0
               while z < len(ftags):
                  listbox.insert(END, ftags[z])
                  z += 1

      Button(remove_wn, text='Remove Tag', font=button_font, bg=button_background, command=remove_item, border = 2).place(x = 270, y = 210)
      Button(remove_wn, text = "Exit", font=button_font, bg=button_background, command=remove_wn.destroy, border=2).place(x = 350, y = 210)
   

def get_tags():
   z = 0
   path = fd.askopenfilename(title='Choose a file to add tag', filetypes=[("All files", "*.*")])
   #print(path)
   if len(path) == 0:
      mb.showinfo("File Not Selected", "No file was selected")
   else:
      fileid = pathtoid(path)
      #print(fileid)

      def get_tags():
         with open("fileid-tags.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            tags = list()
            tags = file_data[fileid]
            return tags
      
      ftags = list()
      ftags = get_tags()
      get_wn = Toplevel(root)
      get_wn.title(f'Removing Tags from {path}')
      get_wn.geometry('720x240')
      get_wn.resizable(0,0)
      get_wn.grab_set()

      listbox = Listbox(get_wn, selectbackground='SteelBlue', font=("Georgia", 10), selectmode=SINGLE)
      listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

      scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
      scrollbar.pack(side=RIGHT, fill=Y)

      listbox.config(yscrollcommand=scrollbar.set)

      while z < len(ftags):
         listbox.insert(END, ftags[z])
         z += 1

      Button(get_wn, text = "Exit", font=button_font, bg=button_background, command=get_wn.destroy, border=2).place(x = 330, y = 210)

# Defining the variables
title = 'File Tagger'
background = 'White'

button_font = ("Times New Roman", 13)
button_background = 'Turquoise'

# Initializing the window
root = Tk()
root.title(title)
root.geometry('560x100')
root.resizable(0, 0)
root.config(bg=background)

# Creating and placing the components in the window
# Label(root, text=title, font=("Comic Sans MS", 15), bg=background, wraplength=250).place(x=20, y=0)

Button(root, text='Add tag', width=10, font=button_font, bg=button_background, command=add_tag).place(x=10, y=20)

Button(root, text='Tag Search', width=10, font=button_font, bg=button_background, command=search_tag).place(x=120, y=20)

Button(root, text='Remove tag', width=10, font=button_font, bg=button_background, command=remove_tags).place(x=230, y=20)

Button(root, text='Get tags', width=10, font=button_font, bg=button_background, command=get_tags).place(x=340, y=20)

Button(root, text='Exit', width=10, font=button_font, bg=button_background, command=root.destroy).place(x=450, y=20)

# Finalizing the window
root.update()
root.mainloop()
