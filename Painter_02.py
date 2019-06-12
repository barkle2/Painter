import tkinter as tk

# 선택:0, 점:1, 선:2, 사각형:3, 원:4, 텍스트:5
draw_mode = 0
# 색
draw_color = "black"

# x1, y1: 시작점
x1 = None
y1 = None

# 마우스 왼쪽 버튼을 눌렀을 때
def mouseLDown(event):
    global x1, y1
    mouse_text.set("X:"+str(event.x)+" Y:"+str(event.y)+" L Down")

    # 점 그리기 모드라면
    if draw_mode == 1:
        canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill=draw_color, outline=draw_color)
    # 텍스트 그리기 모드라면
    elif draw_mode == 5:
        canvas.create_text(event.x, event.y, text=input_text.get(), fill=draw_color)
        
    elif draw_mode >= 2 and draw_mode <= 4:
        x1 = event.x
        y1 = event.y

# 마우스를 움직일 때
def mouseMove(event):
    global x1, y1
    mouse_text.set("X:"+str(event.x)+" Y:"+str(event.y)+" Move")

# 마우스 왼쪽 버튼을 뗐을 때
def mouseLUp(event):
    global x1, y1
    mouse_text.set("X:"+str(event.x)+" Y:"+str(event.y)+" L Up")

    # 선 그리기 모드라면
    if draw_mode == 2:
        canvas.create_line(x1, y1, event.x, event.y, width=2, fill=draw_color)
    # 네모 그리기 모드라면
    elif draw_mode == 3:
        canvas.create_rectangle(x1, y1, event.x, event.y, width=2, outline=draw_color)
    # 원 그리기 모드라면
    elif draw_mode == 4:
        canvas.create_oval(x1, y1, event.x, event.y, width=2, outline=draw_color)
    

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

window.mainloop()






