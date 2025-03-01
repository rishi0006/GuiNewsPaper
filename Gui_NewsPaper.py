from tkinter import *
from PIL import ImageTk, Image 

def every_100(text):
    final_text=""
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="\n"
    return final_text

root=Tk()
root.title("Daily News")
root.geometry("1000x800") 

texts=[]
photos=[]
for i in range(0,2):
    with open(f"tnp{i+1}.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        heading = lines[0].strip()
        content = "".join(lines[1:])
        texts.append((heading, every_100(content)))
        
    
    image=Image.open(f"np{i+1}.png")
    #doing resize
    image=image.resize((270,270),Image.LANCZOS)
    photos.append(ImageTk.PhotoImage(image))


f0= Frame(root,width=800,height=40)
Label(f0,text="Top News of the Day", font="lucida 33 bold").pack()
Label(f0,text="March 1 2025", font="lucida 13 bold").pack()
f0.pack()


f1= Frame(root, width=900, height=200)
Label(f1, text=texts[0][0],font="lucida 15 bold", padx=42).pack(anchor="w")
Label(f1, text=texts[0][1],font="lucida 12", padx=42,pady=1, wraplength=600,justify="left").pack(side="left")
Label(f1, image=photos[0],anchor="e").pack()
f1.pack(anchor= "w")

f2= Frame(root, width=900, height=200,pady=14,padx=40)
Label(f2, text=texts[1][0],font="lucida 15 bold", padx=2,pady=10).pack(anchor="w")
Label(f2, text=texts[1][1],font="lucida 12", padx=42,pady=22,wraplength=550,justify="left").pack(side="right")
Label(f2, image=photos[1],anchor="e",padx=22,pady=40).pack()
f2.pack(anchor= "w")

f3 = Frame(root)
Label(root, text="created by Rishi Chaudhary", font="lucida 10 italic").place(relx=0.98, rely=0.98, anchor="se")
f3.pack(side="bottom", anchor="se")

# f3= Frame(root, width=900, height=200,pady=14)
# Label(f3, text=texts[2], padx=22,pady=22).pack(side="left")
# Label(f3, image=photos[2],anchor="e").pack()
# f3.pack(anchor= "w")

root.mainloop()

