import tkinter
import PIL.Image
import PIL.ImageTk
import cv2


class App:
    def __init__(self, window, video_source1, video_source2, video_source3):
        self.window = window
        self.window.title("MULTIPLE MEDIA PLAYER")
        self.video_source1 = video_source1
        self.video_source2 = video_source2
        self.video_source3 = video_source3
        self.photo1 = ""
        self.photo2 = ""
        self.photo3 = ""

        # open video source
        self.vid1 = MyVideoCapture(self.video_source1, self.video_source2, self.video_source3)

        # Create a canvas that can fit the above video source size
        self.canvas1 = tkinter.Canvas(window, width=450, height=700)
        self.canvas2 = tkinter.Canvas(window, width=450, height=700)
        self.canvas3 = tkinter.Canvas(window, width=450, height=700)
        self.canvas1.pack(padx=0, pady=0, side="left")
        self.canvas2.pack(padx=0, pady=0, side="left")
        self.canvas3.pack(padx=0, pady=0, side="left")

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()

    def update(self):
        # Get a frame from the video source
        ret1, frame1, ret2, frame2, ret3, frame3 = self.vid1.get_frame

        if ret1 and ret2 and ret3:
                self.photo1 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame1))
                self.photo2 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame2))
                self.photo3 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame3))
                self.canvas1.create_image(0, 0, image=self.photo1, anchor=tkinter.NW)
                self.canvas2.create_image(0, 0, image=self.photo2, anchor=tkinter.NW)
                self.canvas3.create_image(0, 0, image=self.photo3, anchor=tkinter.NW)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source1, video_source2, video_source3):
        # Open the video source
        self.vid1 = cv2.VideoCapture(video_source1)
        self.vid2 = cv2.VideoCapture(video_source2)
        self.vid3 = cv2.VideoCapture(video_source3)


    @property
    def get_frame(self):
        ret1 = ""
        ret2 = ""
        ret3 = ""
        if self.vid1.isOpened() and self.vid2.isOpened() and self.vid3.isOpened():
            ret1, frame1 = self.vid1.read()
            ret2, frame2 = self.vid2.read()
            ret3, frame3 = self.vid3.read()
            frame1 = cv2.resize(frame1, (600, 700))
            frame2 = cv2.resize(frame2, (600, 700))
            frame3 = cv2.resize(frame3, (600, 700))
            
            if ret1 and ret2 and ret3:
                # Return a boolean success flag and the current frame converted to BGR
                return ret1, cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB), ret2, cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB), ret3, cv2.cvtColor(frame3, cv2.COLOR_BGR2RGB)
            else:
                return ret1, None, ret2, None, ret3, None
        else:
            return ret1, None, ret2, None, ret3, None

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid1.isOpened():
            self.vid1.release()
        if self.vid2.isOpened():
            self.vid2.release()
        if self.vid3.isOpened():
            self.vid3.release()


def callback():
    global v1,v2,v3
    v1=E1.get()
    v2=E2.get()
    v3=E3.get()
    if v1 == "" or v2 == "" or v3 == "":
        L4.pack()
        return
    initial.destroy()


v1 = ""
v2 = ""
v3 = ""

initial = tkinter.Tk()
initial.title("MULTIPLE MEDIA PLAYER")
L0 = tkinter.Label(initial, text="Enter the full path")
L0.pack()
L1 = tkinter.Label(initial, text="Video 1")
L1.pack()
E1 = tkinter.Entry(initial, bd =5)
E1.pack()
L2 = tkinter.Label(initial, text="Video 2")
L2.pack()
E2 = tkinter.Entry(initial, bd =5)
E2.pack()
L3 = tkinter.Label(initial, text="Video 3")
L3.pack()
E3 = tkinter.Entry(initial, bd =5)
E3.pack()
B = tkinter.Button(initial, text ="Next", command = callback)
B.pack()
L4 = tkinter.Label(initial, text="Enter both the names")

initial.mainloop()


# Create a window and pass it to the Application object
App(tkinter.Tk(),v1, v2, v3)
