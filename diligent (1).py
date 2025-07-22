from tkinter import *
from tkinter import messagebox
import pygame
import cv2
from PIL import Image, ImageTk,ImageSequence

root1 = Tk()
root1.title("Diligent Drivers")

video_label = Label(root1)
video_label.pack()
 
pygame.mixer.init()
cap = cv2.VideoCapture("video.mp4")

zoom_factor = 2.36  
def click():
    pygame.mixer.music.load('click.mp3')
    pygame.mixer.music.play()

def success():
    pygame.mixer.music.load('success.mp3')
    pygame.mixer.music.play()

def race():
    pygame.mixer.music.load('race.mp3')
    pygame.mixer.music.play()

def keys():
    pygame.mixer.music.load('type.mp3')
    pygame.mixer.music.play()

def win(): 
    pygame.mixer.music.load('win.mp3')
    pygame.mixer.music.play()
    
def update_video():
    global zoom_factor
    ret, frame = cap.read()
    if ret:
        zoomed_frame = cv2.resize(frame, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)
        frame_rgb = cv2.cvtColor(zoomed_frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        img_tk = ImageTk.PhotoImage(image=img)
        video_label.img_tk = img_tk
        video_label.config(image=img_tk)
        if not pygame.mixer.music.get_busy():
            audio_path = 'audio1.mp3'
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
        video_label.after(10, update_video)
    else:
        cap.release()

def slide2():
    root1.withdraw()
    root2 = Toplevel(root1)
    pygame.mixer.music.stop()
    root2.title("CAR DATA COLLECTOR")
    root2.geometry('1500x1500')
    root2.configure(bg='white')
    gif_path = "new.gif"
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
    gif_label = Label(root2)

    def update_frame(frame_num):
        img = frames[frame_num]
        gif_label.config(image= img)
        root2.after(100, update_frame, (frame_num + 1) % len(frames))

    gif_label.place(x = 20, y = 10)
    update_frame(0)
    tex = Label(root2, text = 'Diligent Drivers',bg = '#CFF6F8',font = ('gabriola',80,'bold'))
    tex.place(x = 500, y = 50)

    entry1 = Entry(root2,font = ('times',40),width = 20)
    entry2 = Entry(root2,font = ('times',40),width = 20)
    Entry1 = Label(root2,text = 'Car1 number',font = ('times',30),bg  = 'light blue')
    Entry2 = Label(root2,text = 'Car2 number',font = ('times',30),bg = 'light blue')

    entry1.place(x = 680, y = 300)
    Entry1.place(x = 380, y = 300)
    Entry2.place(x = 380, y = 400)


    entry2.place(x = 680, y = 400)

    def update_image():
        global current_image_idx,current_num_idx
        image_path = images[current_image_idx]
        num_path = numbers[current_num_idx]
        image = PhotoImage(file=image_path)
        image_label.configure(image=image)
        num_label.configure(text=num_path)
        image_label.image = image
        num_label.text = num_path

    def next_image():
        global current_image_idx,current_num_idx
        current_image_idx = (current_image_idx + 1) % len(images)
        current_num_idx = (current_num_idx + 1) % len(numbers)
        update_image()

    def slide4(r):
        keys()
        global num1, num2
        num1 = num1.get()
        num2 = num2.get()
        root4 = Toplevel(r)
        root4.geometry('1500x1500')
        img = PhotoImage(file = 'big.png')
        l = Label(root4,state='normal', image = img)
        l.place(x = 0, y = 0)

        def display_text_letter_by_letter(label, text, current_index):
            if current_index < len(text):
        
                label.config(text=text[:current_index+1])

                root2.after(100, display_text_letter_by_letter, label, text, current_index + 1)
               
            else:
                label.config(text=text)
        
        root4.title("It's US")
        text = "It's me..!"+entry1.get()
        text1 = "It's me..!"+entry2.get()
        current_index = 0
        def clear1(e):
            gallon.delete(0,"end")
        def clear2(e):
            full.delete(0,"end")
        label = Label(root4, text="", bg = '#F3B8F0',font=("gabriola", 30,'bold'))
        label1 = Label(root4, text=text1, bg = '#63E9E5',font=("gabriola", 30,'bold'))
        gallon = Entry(root4,font = ('times',20),width = 15)
        gallon.insert(0,'Gallons:')
        gallon.bind("<FocusIn>", clear1)
        full = Entry(root4,font = ('times',20),width = 15)
        full.insert(0,'Full tank? ')
        full.bind("<FocusIn>", clear2)
        gallon.place(x = 1050, y = 400)
        full.place(x = 1050,y = 450 )

        label.place(x = 400, y = 220)
        label1.place(x = 1050, y = 300)

        display_text_letter_by_letter(label, text, current_index)
    
        Button(root4, text = 'go',font = ('gabriola',25),command = lambda:[win(),race(),CarRaceGUI(root4,entry1.get(),entry2.get(),num1,num2,gallon.get(),full.get())]).place(x = 900, y = 600)
        
        root4.mainloop()

    def main():
        global images, current_image_idx, image_label,numbers,current_num_idx,num_label
        images = ["yellowbig.png", "bluebig.png", "redbig.png", "whitebig.png"]
        numbers = [1,2,3,4]
        current_image_idx = 0
        current_num_idx = 0
        root2.withdraw()
        root3 = Toplevel(root2)
        root3.title("Image Slideshow")
        root3.geometry('1500x1500')
        #root3.config(bg = 'lightblue')
        img = PhotoImage(file = 'b.png')
        lab = Label(root3,image = img)
        lab.place(x = 0, y = 0)

        global num1,num2
        
        def delete1(e):
            num1.delete(0,'end')
        def delete2(e):
            num2.delete(0,'end')
        num1 = Entry(root3,width = 20,font = ("times",30))
        num2 = Entry(root3,width = 20,font = ("times",30))
        num1.insert(0,'Choice 1:')
        num1.bind("<FocusIn>", delete1)

        num2.insert(0,'Choice 2:')
        num2.bind("<FocusIn>", delete2)

        num1.place(x= 200, y = 350)
        num2.place(x = 200, y = 450)

        image_label = Label(root3)
        num_label = Label(root3,font = ("arial",20))
        image_label.place(x = 1000, y = 100)
        num_label.place(x = 900,y = 600)

        next_button = Button(root3, text="Next", command = lambda:[click(),next_image()])
        next_button.place(x = 900,y = 500)
        update_image()
        b = Button(root3,text = '   Next   ',command = lambda:[win(),slide4(root3)],font = ("arial",30))
        b.place(x = 300, y = 550)

        root3.mainloop()
        
    b = Button(root2, text = '    Next   ',fg = 'black',bg = 'lightblue',font = ('gabriola',30,'bold'),command = lambda:[win(),main()])
    
    b.place(x = 900, y = 500)
    root2.mainloop()

class CarRaceGUI:

    def __init__(self, root,player1,player2,num1,num2,gallon,full):
        self.root = root
        self.root.title("Car Race Simulation")
        self.root.config(bg = 'light blue')

        self.p1 = player1
        self.p2 = player2
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.gal = gallon
        self.full = full
        if self.full == 'yes':
            self.full = 'F'
        else:
            self.full = ' '

        self.canvas = Canvas(root, width=1100, height=1500)
        self.canvas.pack()

        images = ['yellow.png','blue.png','redsmall.png','white.png']

        self.bg_img = PhotoImage(file="carpath1.png")
        self.bg = self.canvas.create_image(0, 0, anchor=NW, image=self.bg_img)

        path1 = images[self.num1 - 1]
        path2 = images[self.num2 - 1]

        self.car_img = PhotoImage(file=path1)
        self.car_img1 = PhotoImage(file=path2)

        self.car = self.canvas.create_image(327, 752, image=self.car_img)
        self.car1 = self.canvas.create_image(327, 749, image=self.car_img1)

        self.speed = 8
        self.speed1 = 6
        self.target_coordinates = [(327,752),(100,741),(100,582),(157,458),(116,298),(114,155),(256,197),(321,367),(364,518),(466,526),(486,421),(393,343),(471,244),(690,111),(796,144),(950,314),(846,391),(710,400),(656,471),(752,547),(980,470),(1041,586),(895,740),(335,741)]
        self.target_coordinates1 = [(327,752),(100,741),(100,582),(157,458),(116,298),(114,155),(256,197),(321,367),(364,518),(466,526),(486,421),(393,343),(471,244),(690,111),(796,144),(950,314),(846,391),(710,400),(656,471),(752,547),(980,470),(1041,586),(895,740),(335,741)]

        self.target_index = 0
        self.target_index1 = 1

        self.move_car()

    def move_car(self):
        target_x, target_y = self.target_coordinates[self.target_index]
        target_x1, target_y1 = self.target_coordinates1[self.target_index1]

        current_x, current_y = self.canvas.coords(self.car)
        current_x1, current_y1 = self.canvas.coords(self.car1)

        x_diff = target_x - current_x
        x1_diff = target_x1 - current_x1

        y_diff = target_y - current_y
        y1_diff = target_y1 - current_y1

        # Calculate the step for smooth movement
        x_step = self.speed if abs(x_diff) >= self.speed else abs(x_diff)
        y_step = self.speed if abs(y_diff) >= self.speed else abs(y_diff)
        x1_step = self.speed1 if abs(x1_diff) >= self.speed1 else abs(x1_diff)
        y1_step = self.speed1 if abs(y1_diff) >= self.speed1 else abs(y1_diff)

        self.canvas.move(self.car, x_step if x_diff > 0 else -x_step, y_step if y_diff > 0 else -y_step)
        self.canvas.move(self.car1, x1_step if x1_diff > 0 else -x1_step, y1_step if y1_diff > 0 else -y1_step)

        if (current_x, current_y) == (target_x, target_y):
            self.target_index = (self.target_index + 1) % len(self.target_coordinates)
        
        if (current_x1, current_y1) == (target_x1, target_y1):
            self.target_index1 = (self.target_index1 + 1) % len(self.target_coordinates1)

        def car_details():
            table = [[self.p1,self.gal,self.full,1500,100,'won'],[self.p2,self.gal,self.full,1200,100,'lost']]
            table_str = "Car No\tGallons\tTank\t Odometer\tCost\tStatus\n"
            for row in table:
                table_str += f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t\t{row[4]}\t{row[5]}\n"
            messagebox.showinfo("Car Data Table", table_str)
          

        # Check if the car has reached the starting point
        if self.target_index == 0:
            success()
            l = Label(self.root, text= self.p1 +'..won', font=("gabriola", 50),bg = 'light green')
            b = Button(self.root,text = 'CAR DETAILS',font = ('gabriola',20),command = lambda:[car_details()],fg = 'white',bg = 'black').place(x = 800, y = 300)
            l.place(x = 650, y = 100)
            return
            
        self.root.after(10, self.move_car)

button1 = Button(root1,text = '            Start          ', font = ("Gabriola",25),command = lambda:[win(),slide2()], bg = 'black', fg = 'white').place(x = 160, y = 680)

update_video()
root1.mainloop()