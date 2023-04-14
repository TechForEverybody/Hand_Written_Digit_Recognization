from tkinter import *
import PIL
import PIL.Image, PIL.ImageDraw
from Analyzer import Analyzer

class App:
    def __init__(self,model_path):
        self.Model = Analyzer(model_path)
        self.root = None
        self.image = None
        self.canvas = None
        self.draw = None
        self.brush_width = 25
        self.initializeGUI()
    def initializeGUI(self):
        WIDTH = 500
        HEIGHT = 500
        WHITE = (255, 255, 255)
        self.root = Tk()
        self.root.geometry("800x900")
        self.root.title("Digit Recognition System ")
        self.root.config(bg="aqua")
        background=PhotoImage(file='./Background.png')
        background_label=Label(self.root,image=background)
        background_label.place(x=0,y=0)
        self.Heading=Label(self.root,text="Hindi Digit Recognizer",font="ROMEN 20 bold",bg="#014b43",fg="white")
        self.Heading.pack(fill=X, side=TOP,padx= 10, pady=0)
        self.canvas = Canvas(self.root, width=WIDTH-10, height=HEIGHT-10, bg="white",border=5,relief="ridge")
        self.canvas.pack(expand=YES,fill=BOTH, padx= 120, pady=30)
        self.canvas.bind("<B1-Motion>", self.paint)

        self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        self.draw = PIL.ImageDraw.Draw(self.image)

        button_frame = Frame(self.root)
        button_frame.pack(fill=X, side=BOTTOM,padx= 10, pady=20)

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        class1_btn = Button(button_frame, text="Predict", command=lambda: self.save(),bg= "blue", fg= "white",font="ROMEN 15 bold")
        class1_btn.grid(row=0, column=1, sticky=W + E)

        decrease_button = Button(button_frame, text="Brush-", command=self.decrease_brush_width,bg= "black", fg= "white",font="ROMEN 15 bold")
        decrease_button.grid(row=1, column=0, sticky=W + E)

        clear_btn = Button(button_frame, text="Clear", command=self.clear,bg= "red", fg= "white",font="ROMEN 15 bold")
        clear_btn.grid(row=1, column=1, sticky=W + E)

        increase_button = Button(button_frame, text="Brush+", command=self.increase_brush_width,bg= "green", fg= "white",font="ROMEN 15 bold")
        increase_button.grid(row=1, column=2, sticky=W + E)
        self.OutputLabel=Label(self.root,height=50,text="Please Draw Something",font="ROMEN 20 bold")
        self.OutputLabel.pack(fill=X, side=BOTTOM,padx= 10, pady=5)
        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", width=self.brush_width)
        self.draw.rectangle([x1, y2, x2 + self.brush_width, y2 + self.brush_width], fill="black", width=self.brush_width)

    def save(self):
        self.image.save("./Images/WorkingImage.png")
        self.clear()
        predicted=self.Model.predict("./Images/WorkingImage.png")[0]
        self.OutputLabel.config(text="Predicted Digit is "+str(predicted))

    def decrease_brush_width(self):
        if self.brush_width > 1:
            self.brush_width -= 1

    def increase_brush_width(self):
        self.brush_width += 1

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 1000, 1000], fill="white")

    def predict(self):
        print(self.Model.predict("./Images/WorkingImage.png"))



if __name__ == "__main__":
    App()