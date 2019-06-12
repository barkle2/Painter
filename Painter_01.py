import tkinter as tk

# 윈도우를 생성한다
window = tk.Tk()
window.title("점선면 그림판")

# 스타일 프레임을 생성한다
style_frame = tk.Frame(window)
style_frame.grid(row=0, column=0, sticky=tk.W)

# 점그리기 버튼
point_button = tk.Button(style_frame, text=".", width=3)
point_button.grid(row=0, column=0, sticky=tk.W)

# 선그리기 버튼
line_button = tk.Button(style_frame, text="/", width=3)
line_button.grid(row=0, column=1, sticky=tk.W)

# 네모그리기 버튼
rectangle_button = tk.Button(style_frame, text="□", width=3)
rectangle_button.grid(row=0, column=2, sticky=tk.W)

# 원그리기 버튼
circle_button = tk.Button(style_frame, text="○", width=3)
circle_button.grid(row=0, column=3, sticky=tk.W)

# 글씨쓰기 버튼
text_button = tk.Button(style_frame, text="T", width=3)
text_button.grid(row=0, column=4, sticky=tk.W)

# 색상 프레임을 생성한다
color_frame = tk.Frame(window)
color_frame.grid(row=0, column=1, sticky=tk.E)

# 하얀색 버튼
white_button = tk.Button(color_frame, bg="white", width=3)
white_button.grid(row=0, column=0, sticky=tk.E)

# 하얀색 버튼
white_button = tk.Button(color_frame, bg="white", width=3)
white_button.grid(row=0, column=0, sticky=tk.E)

# 검은색 버튼
black_button = tk.Button(color_frame, bg="black", width=3)
black_button.grid(row=0, column=1, sticky=tk.E)

# 빨간색 버튼
red_button = tk.Button(color_frame, bg="red", width=3)
red_button.grid(row=0, column=2, sticky=tk.E)

# 파란색 버튼
blue_button = tk.Button(color_frame, bg="blue", width=3)
blue_button.grid(row=0, column=3, sticky=tk.E)

# 노란색 버튼
yellow_button = tk.Button(color_frame, bg="yellow", width=3)
yellow_button.grid(row=0, column=4, sticky=tk.E)

# 초록색 버튼
green_button = tk.Button(color_frame, bg="green", width=3)
green_button.grid(row=0, column=5, sticky=tk.E)

# 인포 프레임을 생성한다
info_frame = tk.Frame(window)
info_frame.grid(row=1, column=0, columnspan=2)

# 마우스 엔트리
mouse_text = tk.StringVar()
mouse_entry = tk.Entry(info_frame, textvariable=mouse_text, width=25)
mouse_entry.pack()

# 캔버스 프레임을 생성한다
canvas_frame = tk.Frame(window, bd=2, bg="black")
canvas_frame.grid(row=2, column=0, columnspan=2, sticky=tk.W)

# 캔버스 생성한다
canvas = tk.Canvas(canvas_frame, width=400, height=300, bg="white")
canvas.pack()

window.mainloop()






