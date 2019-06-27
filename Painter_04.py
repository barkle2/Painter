import tkinter as tk

# 선택:0, 점:1, 선:2, 사각형:3, 원:4, 텍스트:5
draw_mode = 0
# 색
draw_color = "black"

# x1, y1: 시작점
x1 = None
y1 = None

# 객체 배열
obj_array = []

# 부모 클래스 만들기
class Object:
    # 생성자
    def __init__(self, color, width):
        self.color = color
        self.width = width

    # 두껍게 만들기 함수
    def thicker(self):
        self.width = self.width+1
        if self.width > 10:
            self.width = 10

    # 얇게 만들기 함수
    def thiner(self):
        self.width = self.width-1
        if self.width < 1:
            self.width = 1    

# 점 클래스 만들기
class Point(Object):
    # 생성자
    def __init__(self, x, y, color, width=2):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    # 그리기 함수
    def draw(self, canvas):
        canvas.create_oval(self.x-self.width, self.y-self.width,
                           self.x+self.width, self.y+self.width,
                           fill=self.color, outline=self.color)


# 텍스트 클래스 만들기
class Text(Object):
    # 생성자
    def __init__(self, x, y, color, text, width=2):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.width = width

    # 그리기 함수
    def draw(self, canvas):
        canvas.create_text(self.x, self.y,
                           fill=self.color, text=self.text, font=("Courier", self.width))

    # 두껍게 만들기 함수
    def thicker(self):
        self.width = self.width+5
        if self.width > 50:
            self.width = 50

    # 얇게 만들기 함수
    def thiner(self):
        self.width = self.width-5
        if self.width < 1:
            self.width = 5  

# 선 클래스 만들기
class Line(Object):
    # 생성자
    def __init__(self, x1, y1, x2, y2, color, width=2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width

    # 그리기 함수
    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2,
                           fill=self.color, width=self.width)

# 사각형 클래스 만들기
class Rectangle(Object):
    # 생성자
    def __init__(self, x1, y1, x2, y2, color, width=2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width

    # 그리기 함수
    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                outline=self.color, width=self.width)

# 원 클래스 만들기
class Circle(Object):
    # 생성자
    def __init__(self, x1, y1, x2, y2, color, width=2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width

    # 그리기 함수
    def draw(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2,
                           outline=self.color, width=self.width)
        
# 마우스 왼쪽 버튼을 눌렀을 때
def mouseLDown(event):
    global x1, y1
    mouse_text.set("X:"+str(event.x)+" Y:"+str(event.y)+" L Down")

    # 점 그리기 모드라면
    if draw_mode == 1:
        # Point Class의 객체를 생성
        point = Point(event.x, event.y, draw_color)
        # obj_array에 집어 넣는다.
        obj_array.append(point)
        # 리스트박스에도 표시
        list_box.insert(tk.END, "point")
    # 텍스트 그리기 모드라면
    elif draw_mode == 5:
        # Text Class의 객체를 생성
        text = Text(event.x, event.y, draw_color, input_text.get())
        # obj_array에 집어 넣는다.
        obj_array.append(text)
        # 리스트박스에도 표시
        list_box.insert(tk.END, "text")
        
    elif draw_mode >= 2 and draw_mode <= 4:
        x1 = event.x
        y1 = event.y

    render()

# 마우스를 움직일 때
def mouseMove(event):
    global x1, y1
    mouse_text.set("X:"+str(event.x)+" Y:"+str(event.y)+" Move")

    render()

# 마우스 왼쪽 버튼을 뗐을 때
def mouseLUp(event):
    global x1, y1
    mouse_text.set("X:"+str(event.x)+" Y:"+str(event.y)+" L Up")

    # 선 그리기 모드라면
    if draw_mode == 2:
        # Line Class 객체를 생성
        line = Line(x1, y1, event.x, event.y, draw_color)
        # obj_array에 집어 넣는다
        obj_array.append(line)
        # 리스트박스에도 표시
        list_box.insert(tk.END, "line")
    # 네모 그리기 모드라면
    elif draw_mode == 3:
        # Rectangle Class 객체를 생성
        rec = Rectangle(x1, y1, event.x, event.y, draw_color)
        # obj_array에 집어 넣는다
        obj_array.append(rec)
        # 리스트박스에도 표시
        list_box.insert(tk.END, "rectangle")

    # 원 그리기 모드라면
    elif draw_mode == 4:
        # Circle Class 객체를 생성
        circle = Circle(x1, y1, event.x, event.y, draw_color)
        # obj_array에 집어 넣는다
        obj_array.append(circle)
        # 리스트박스에도 표시
        list_box.insert(tk.END, "circle")

    render()

# 캔버스 그리기 함수
def render():
    # 전체를 지우고
    canvas.create_rectangle(0, 0, 400, 300, fill="white")

    # 객체 리스트에서 하나씩 객체를 꺼내서
    for i in range(len(obj_array)):
        # 그린다
        obj_array[i].draw(canvas)
        

# 선택 버튼 함수
def selectButton():
    global draw_mode
    draw_mode = 0

# 점 그리기 버튼 함수
def pointButton():
    global draw_mode
    draw_mode = 1

# 선 그리기 버튼 함수
def lineButton():
    global draw_mode
    draw_mode = 2

# 사각형 그리기 버튼 함수
def rectangleButton():
    global draw_mode
    draw_mode = 3

# 원 그리기 버튼 함수
def circleButton():
    global draw_mode
    draw_mode = 4

# 텍스트 그리기 버튼 함수
def textButton():
    global draw_mode
    draw_mode = 5

# 하얀색 버튼 함수
def whiteButton():
    global draw_color
    draw_color = "white"

# 검은색 버튼 함수
def blackButton():
    global draw_color
    draw_color = "black"

# 빨간색 버튼 함수
def redButton():
    global draw_color
    draw_color = "red"

# 노란색 버튼 함수
def yellowButton():
    global draw_color
    draw_color = "yellow"

# 파란색 버튼 함수
def blueButton():
    global draw_color
    draw_color = "blue"

# 녹색 버튼 함수
def greenButton():
    global draw_color
    draw_color = "green"

# 두껍게 버튼 함수
def widthPlusButton():
    # 리스트 박스에서 몇 번째 아이템을 선택했는지 보고
    cs = list_box.curselection()
    cur_index = cs[0]

    # 선택한 아이템을 두껍게 만듭니다.
    obj_array[cur_index].thicker()

    render()

# 얇게 버튼 함수
def widthMinusButton():
    # 리스트 박스에서 몇 번째 아이템을 선택했는지 보고
    cs = list_box.curselection()
    cur_index = cs[0]

    # 선택한 아이템을 얇게 만듭니다.
    obj_array[cur_index].thiner()

    render()

# 지우기 함수
def delButton():
    # 객체 리스트에 뭔가 들어있는 경우에만 이 함수가 동작하도록 한다
    if len(obj_array) > 0:
        # 리스트 박스에서 몇 번째 아이템을 선택했는지 보고
        cs = list_box.curselection()
        cur_index=cs[0]

        # 선택한 아이템을 지운다
        obj_array.pop(cur_index)
        list_box.delete(cur_index)

        render()

# 윈도우를 생성한다
window = tk.Tk()
window.title("점선면 그림판")

# 스타일 프레임을 생성한다
style_frame = tk.Frame(window)
style_frame.grid(row=0, column=0, sticky=tk.W)

# 선택 버튼
select_button = tk.Button(style_frame, text="↖", width=3, command=selectButton)
select_button.grid(row=0, column=0, sticky=tk.W)

# 점그리기 버튼
point_button = tk.Button(style_frame, text=".", width=3, command=pointButton)
point_button.grid(row=0, column=1, sticky=tk.W)

# 선그리기 버튼
line_button = tk.Button(style_frame, text="/", width=3, command=lineButton)
line_button.grid(row=0, column=2, sticky=tk.W)

# 네모그리기 버튼
rectangle_button = tk.Button(style_frame, text="□", width=3, command=rectangleButton)
rectangle_button.grid(row=0, column=3, sticky=tk.W)

# 원그리기 버튼
circle_button = tk.Button(style_frame, text="○", width=3, command=circleButton)
circle_button.grid(row=0, column=4, sticky=tk.W)

# 글씨쓰기 버튼
text_button = tk.Button(style_frame, text="T", width=3, command=textButton)
text_button.grid(row=0, column=5, sticky=tk.W)

# 색상 프레임을 생성한다
color_frame = tk.Frame(window)
color_frame.grid(row=0, column=1, sticky=tk.E)

# 하얀색 버튼
white_button = tk.Button(color_frame, bg="white", width=3, command=whiteButton)
white_button.grid(row=0, column=0, sticky=tk.E)

# 검은색 버튼
black_button = tk.Button(color_frame, bg="black", width=3, command=blackButton)
black_button.grid(row=0, column=1, sticky=tk.E)

# 빨간색 버튼
red_button = tk.Button(color_frame, bg="red", width=3, command=redButton)
red_button.grid(row=0, column=2, sticky=tk.E)

# 파란색 버튼
blue_button = tk.Button(color_frame, bg="blue", width=3, command=blueButton)
blue_button.grid(row=0, column=3, sticky=tk.E)

# 노란색 버튼
yellow_button = tk.Button(color_frame, bg="yellow", width=3, command=yellowButton)
yellow_button.grid(row=0, column=4, sticky=tk.E)

# 초록색 버튼
green_button = tk.Button(color_frame, bg="green", width=3, command=greenButton)
green_button.grid(row=0, column=5, sticky=tk.E)

# 인포 프레임을 생성한다
info_frame = tk.Frame(window)
info_frame.grid(row=1, column=0, columnspan=2)

# 마우스 엔트리
mouse_text = tk.StringVar()
mouse_entry = tk.Entry(info_frame, textvariable=mouse_text, width=25)
mouse_entry.grid(row=0, column=0)

# 텍스트 라벨
input_label = tk.Label(info_frame, text="              Text Input:")
input_label.grid(row=0, column=1)

# 텍스트 엔트리
input_text = tk.StringVar()
input_entry = tk.Entry(info_frame, textvariable=input_text, width=15)
input_entry.grid(row=0, column=2)

# 캔버스 프레임을 생성한다
canvas_frame = tk.Frame(window, bd=2, bg="black")
canvas_frame.grid(row=2, column=0, columnspan=2, sticky=tk.W)

# 캔버스 생성한다
canvas = tk.Canvas(canvas_frame, width=400, height=300, bg="white")
canvas.pack()

# 마우스 이벤트 연결
canvas.bind("<Button-1>", mouseLDown)
canvas.bind("<Motion>", mouseMove)
canvas.bind("<ButtonRelease-1>", mouseLUp)

# 리스트 프레임을 생성
list_frame = tk.Frame(window)
list_frame.grid(row=0, rowspan=3, column=2)

# 리스트 박스 생성
list_box = tk.Listbox(list_frame, width=20, height=20)
list_box.grid(row=0, column=0, columnspan=3)

# 두껍게 버튼 생성
width_plus_button = tk.Button(list_frame, text="+", width=4, command=widthPlusButton)
width_plus_button.grid(row=1, column=0)

# 얇게 버튼 생성
width_minus_button = tk.Button(list_frame, text="-", width=4, command=widthMinusButton)
width_minus_button.grid(row=1, column=1)

# Del 버튼 생성
del_button = tk.Button(list_frame, text="Del", width=4, command=delButton)
del_button.grid(row=1, column=2)

window.mainloop()






