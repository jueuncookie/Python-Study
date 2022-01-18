
from tkinter import* #tkinter를 import한다.

def move_r(event): #오른쪽으로 이동하는 함수, event가 발생하면 함수가 호출됨.
    c.move(object, 3, 0) #함수가 호출되면 오른쪽으로 세칸씩 움직이게 함. x축으로 세칸씩 움직이는 (y축으론 0만큼)
def move_l(event): #왼쪽으로 이동하는 함수, event가 발생하면 함수가 호출됨.
    c.move(object, -3, 0) #함수가 호출되면 왼쪽으로 세칸씩 움직이게 함. x축으로 세칸씩 움직이는 (y축으론 0만큼)
def move_u(event): #윗쪽으로 이동하는 함수, event가 발생하면 함수가 호출됨.
    c.move(object, 0, -3) #함수가 호출되면 윗쪽으로 세칸씩 움직이게 함. x축으로 세칸씩 움직이는 (y축으론 0만큼)
def move_d(event): #아랫쪽으로 이동하는 함수, event가 발생하면 함수가 호출됨.
    c.move(object, 0, 3) #함수가 호출되면 아랫쪽으로 세칸씩 움직이게 함. x축으로 세칸씩 움직이는 (y축으론 0만큼)

window = Tk() #윈도우를 만든다.

c= Canvas(window,width = 300, height = 300) #캔버스 위젯을 만드는데, 폭과 높이를  각각 300으로  설정했다.
c.pack()#캔버스 위젯을 윈도우에 패킹한다.

object = c.create_oval(0,10,50,60,fill="magenta") #c라는 캔버스 위젯 안에 구체를 만드는데, 구의 크기는 시작점(0,10) (50,60) 마젠타 색깔로 칠함  

c.bind_all("<KeyPress-Right>", move_r) #오른쪽 화살표 버튼와 move_r함수를 bind해줌. 오른쪽 화살표를 누르면 move_r함수를 호출하는 것
c.bind_all("<KeyPress-Left>", move_l)#오른쪽 화살표 버튼와 move_r함수를 bind해줌. 오른쪽 화살표를 누르면 move_r함수를 호출하는 것
c.bind_all("<KeyPress-Up>", move_u)#오른쪽 화살표 버튼와 move_r함수를 bind해줌. 오른쪽 화살표를 누르면 move_r함수를 호출하는 것
c.bind_all("<KeyPress-Down>", move_d)#오른쪽 화살표 버튼와 move_r함수를 bind해줌. 오른쪽 화살표를 누르면 move_r함수를 호출하는 것
window.mainloop()# 사용자가 윈도우 창을 종료시킬 때까지 윈도우 창을 실행한다.


'''
from tkinter import* # tkinter를 import한다.

def cal (event): # cal함수를 만든다. 이때 ()안에 event는 Entry 위젯 칸에 입력이 완료되고 엔터를 누르면 cal 함수로 바로 넘어가게 이어주기 위해 있는 것이다.
  res = eval(e1.get()) # e1에 입력된 수식을 문자로 가져와서 계산을 함. 이것이 res이고 res의 계산 결과는 l2가 가짐.
  l2.configure(text= "Result =" + str(res)) #congifure은 위젯의 속성을 바꿔주는 것임. res의 속성을 바꿔줌.
window=Tk() # Tk클래스 객체를 생성한다. 이때 클래스 객체란.
l1=Label(window, text= "Input your equation.")#텍스트가 있는 라벨 위젯을 생성한다.
l1.pack()#불필요한 공간을 없애주고, 윈도우에 위젯을 패킹해준다.
e1=Entry(window)#input함수와 비슷한 Entry 위젯은 한줄 텍스트를 입력 받는 필드이다.
e1.bind("<Return>",cal)#e1변수를 cal함수와 bind해준다.
e1.pack()#불필요한 공간을 없애주고, 윈도우에 위젯을 패킹해준다.
l2=Label(window, text="Result = ")#텍스트가 있는 라벨 위젯을 생성한다.
l2.pack()#불필요한 공간을 없애주고, 윈도우에 위젯을 패킹해준다.
window.mainloop() #이벤트루프로 사용자가 윈도우 창닫음 or 종료할 때까지 반복 실행
'''
