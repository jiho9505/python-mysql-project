from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pymysql as db # pymysql 모듈을 불러왔고 db라고 명명

class MyApp:
	def __init__(self,parent):
		self.par = parent
		self.par.title('Welcome to amazon')
		self.par.geometry("350x350")
		img = PhotoImage(file='ama.png')
		lbl10 = Label(image=img)
		lbl10.image = img
		lbl10.place(x=0, y=0)

		self.lbl = Label(self.par, text="      ID      ", font="NanumGothic 10")
		self.lbl.grid(row=0, column=0)


		self.lbl1 = Label(self.par, text="password", font="NanumGothic 10")
		self.lbl1.grid(row=1, column=0)

		self.ent = Entry(self.par)
		self.ent.grid(row=0, column=1)

		self.ent1 = Entry(self.par)
		self.ent1.grid(row=1, column=1)

		self.btn = Button(self.par, text="로그인", command=self.login, width=7, height=1)
		self.btn.place(x=50, y=50)

		self.btn1 = Button(self.par, text="회원가입", command=self.join, width=10, height=1)
		self.btn1.place(x=120, y=50)

		self.btn2 = Button(self.par, text="나가기", command=quit, width=10, height=1)
		self.btn2.place(x=210, y=50)


	def login(self):
		self.a = self.ent.get()
		self.b = self.ent1.get()
		sql_command = """SELECT id_password from customers where customer_id = '%s';"""
		curs.execute(sql_command%self.a)

		try:
			result1 = curs.fetchall()  # select와 관련된 기능 (select 출력값 보여주기 위해 사용) , workbench 결과를 한 줄 씩 읽음
			self.res = result1[0][0]

			if self.b == self.res:
				self.btn.destroy()
				self.btn1.destroy()
				self.btn2.destroy()
				self.lbl.destroy()
				self.lbl1.destroy()
				self.ent.destroy()
				self.ent1.destroy()


				self.btn2 = Button(self.par, text="상품 보기", command=self.view, width=13, height=1)
				self.btn2.place(x=100, y=60)

				self.btn11 = Button(self.par, text="주문내역", command=self.ord_rec, width=13, height=1)
				self.btn11.place(x=100, y=100)

				self.btn3 = Button(self.par, text="나가기", command=quit, width=10, height=1)
				self.btn3.place(x=100, y=140)


			else:
				raise Exception
		except:
			messagebox.showinfo('Error','정보가 일치하지 않습니다.')
	def ord_rec(self):
		self.btn11.destroy()
		self.btn2.destroy()
		self.btn3.destroy()
		self.btn1 = Button(self.par, text="확인 완료", command = quit, width=13, height = 1)
		self.btn1.place(x=230, y=300)

		sql_command = """SELECT item_name from items where item_num in (select item_num from orders where customer_id = '%s')"""

		curs.execute(sql_command%self.a)

		ret = curs.fetchall()

		sql_command = """SELECT order_date from orders where customer_id = '%s'"""

		curs.execute(sql_command % self.a)

		ret1 = curs.fetchall()

		try:
			if ret != "" and ret1 != "":
				Label(self.par, text="★-------Customer Id-------★").pack()
				Label(self.par, text=str(self.a)).pack()
				Label(self.par, text="★--------Item Name--------★").pack()
				for m in ret:
					Label(self.par, text= m[0]).pack()
				Label(self.par, text="★--------Order Date--------★").pack()
				for n in ret1:
					Label(self.par, text= n[0]).pack()


			else:
				raise Exception
		except:
			messagebox.showinfo('Error', '주문내역이 존재하지 않습니다.')
			exit()

	def view(self):
		self.btn11.destroy()
		self.btn2.destroy()
		self.btn3.destroy()

		self.btn2 = Button(self.par, text="주문 하기", command=self.orders, width=13, height=1)
		self.btn2.place(x=100, y=160)
		self.btn3 = Button(self.par, text="나가기", command=quit, width=10, height=1)
		self.btn3.place(x=100, y=200)
		sql_command = """select item_name,price from items;"""
		curs.execute(sql_command)
		self.result_r = curs.fetchall()

		self.totalValue = 0
		self.cVal1 = IntVar()
		self.cVal2 = IntVar()
		self.cVal3 = IntVar()
		self.cVal4 = IntVar()
		self.cVal5 = IntVar()
		self.cVal6 = IntVar()
		self.product1cbtn = Checkbutton(self.par, text=self.result_r[0][0], variable=self.cVal1)
		self.product1cbtn.pack()
		self.product2cbtn = Checkbutton(self.par, text=self.result_r[1][0], variable=self.cVal2)
		self.product2cbtn.pack()
		self.product3cbtn = Checkbutton(self.par, text=self.result_r[2][0], variable=self.cVal3)
		self.product3cbtn.pack()
		self.product4cbtn = Checkbutton(self.par, text=self.result_r[3][0], variable=self.cVal4)
		self.product4cbtn.pack()
		self.product5cbtn = Checkbutton(self.par, text=self.result_r[4][0], variable=self.cVal5)
		self.product5cbtn.pack()
		self.product6cbtn = Checkbutton(self.par, text=self.result_r[5][0], variable=self.cVal6)
		self.product6cbtn.pack()



	def orders(self):


		try:
			if self.cVal1.get() != 0 or self.cVal2.get() != 0 or self.cVal3.get() != 0 or self.cVal4.get() != 0 or self.cVal5.get() != 0 or self.cVal6.get() != 0:
				if self.cVal1.get() == 1:
					self.totalValue += self.result_r[0][1]
				if self.cVal2.get() == 1:
					self.totalValue += self.result_r[1][1]
				if self.cVal3.get() == 1:
					self.totalValue += self.result_r[2][1]
				if self.cVal4.get() == 1:
					self.totalValue += self.result_r[3][1]
				if self.cVal5.get() == 1:
					self.totalValue += self.result_r[4][1]
				if self.cVal6.get() == 1:
					self.totalValue += self.result_r[5][1]
			else:
				raise Exception

		except:
			messagebox.showinfo('error', '구입할 상품을 선택하세요.')

		self.btn2.destroy()
		self.btn3.destroy()
		self.product1cbtn.destroy()
		self.product2cbtn.destroy()
		self.product3cbtn.destroy()
		self.product4cbtn.destroy()
		self.product5cbtn.destroy()
		self.product6cbtn.destroy()

		Label(self.par, text="총 결제금액").pack()
		Label(self.par, text=str(self.totalValue) + "원").pack()

		self.btn12 = Button(self.par, text="결제 및 배송 방식", command=self.pay,width=15, height=1)
		self.btn12.place(x=40, y=180)
		self.btn3 = Button(self.par, text="나가기", command=quit, width=10, height=1)
		self.btn3.place(x=240, y=180)

	def pay(self):
		self.btn12.destroy()
		self.cVal7 = IntVar()
		self.cVal8 = IntVar()

		Label(self.par, text="결제 방식 선택").pack()
		self.paybtn = Checkbutton(self.par, text="카드 결제", variable = self.cVal7)
		self.paybtn.pack()
		self.paybtn2 = Checkbutton(self.par, text="무통장 입금", variable = self.cVal8)
		self.paybtn2.pack()

		self.btn25 = Button(self.par, text="배송 방식 선택", command = self.pay_ing , width=13, height=1)
		self.btn25.place(x=40, y=180)

	def pay_ing(self):
		try:
			self.p1 = self.cVal7.get()
			self.p2 = self.cVal8.get()
			if (self.p1 != 1 and self.p2 == 1) or (self.p1 ==1 and self.p2 != 1):
				self.delv()

			else:
				raise Exception
		except:
			messagebox.showinfo('Error', '둘 중 하나를 선택 해주세요')

	def delv(self):
		self.cVal9 = IntVar()
		self.cVal10 = IntVar()
		Label(self.par, text="배송 방식 선택").pack()
		self.paybtn3 = Checkbutton(self.par, text="선불", variable=self.cVal9)
		self.paybtn3.pack()
		self.paybtn4 = Checkbutton(self.par, text="착불", variable=self.cVal10)
		self.paybtn4.pack()
		self.btn26 = Button(self.par, text="선택 완료", command=self.delv_ing, width=13, height=1)
		self.btn26.place(x=40, y=180)

	def delv_ing(self):
		h = self.cVal9.get()
		hh = self.cVal10.get()

		try:
			if (h != 1 and hh == 1) or (h ==1 and hh != 1):
				messagebox.showinfo("OK", '주문해주셔서 감사합니다')
				if (h != 1 and hh ==1):
					dm = "착불"
				else:
					dm = "선불"
				if (self.p1 != 1 and self.p2 ==1):
					pm = "무통장 입금"
				else:
					pm = "카드 결제"
				it = []
				if self.cVal1.get() == 1:
					it.insert(0,"1")
				if self.cVal2.get() == 1:
					it.insert(1,"2")
				if self.cVal3.get() == 1:
					it.insert(2,"5")
				if self.cVal4.get() == 1:
					it.insert(3,"6")
				if self.cVal5.get() == 1:
					it.insert(4,"10")
				if self.cVal6.get() == 1:
					it.insert(5,"11")

				sql_command = """Insert into delivery(delivery_method,customer_id) values ('%s','%s');"""
				curs.execute(sql_command % (dm, self.a))

				# sql_command = """select * from delivery;"""
				# curs.execute(sql_command)

				ret = curs.fetchall()
				# print(ret)

				sql_command = """Insert into pay(pay_method,price,customer_id) values ('%s','%d','%s');"""
				curs.execute(sql_command % (pm,self.totalValue,self.a))

				# sql_command = """select * from pay;"""
				# curs.execute(sql_command)

				ret1 = curs.fetchall()
				# print(ret1)

				tm = datetime.today().strftime("%Y-%m-%d")
				for k in it:
					sql_command = """Insert into orders(item_num,order_date,customer_id) values ('%s','%s','%s');"""
					curs.execute(sql_command %(k,tm,self.a))


				# sql_command = """select * from orders;"""
				# curs.execute(sql_command)
				ret2 = curs.fetchall()
				# print(ret)
				conn.commit()


			else:
				raise Exception
		except:
			messagebox.showinfo('Error', '둘 중 하나를 선택 해주세요')

	def join(self):
		self.btn.destroy()
		self.btn1.destroy()
		self.btn2.destroy()
		self.lbl.destroy()
		self.lbl1.destroy()
		self.ent.destroy()
		self.ent1.destroy()

		self.lbl2 = Label(self.par, text="ID", font="NanumGothic 10")
		self.lbl2.grid(row=0, column=0)

		self.lbl3 = Label(self.par, text="password", font="NanumGothic 10")
		self.lbl3.grid(row=1, column=0)

		self.lbl4 = Label(self.par, text="name", font="NanumGothic 10")
		self.lbl4.grid(row=2, column=0)

		self.lbl5 = Label(self.par, text="address", font="NanumGothic 10")
		self.lbl5.grid(row=3, column=0)

		self.ent2 = Entry(self.par)
		self.ent2.grid(row=0, column=1)

		self.ent3 = Entry(self.par)
		self.ent3.grid(row=1, column=1)

		self.ent4 = Entry(self.par)
		self.ent4.grid(row=2, column=1)

		self.ent5 = Entry(self.par)
		self.ent5.grid(row=3, column=1)

		self.btn5 = Button(self.par, text="생성하기", command=self.produce, width=13, height=1)
		self.btn5.place(x=100, y=100)

		# self.btn6 = Button(self.par, text="나가기", command=quit, width=10, height=1)
		# self.btn6.place(x=100, y=140)

	def produce(self):
		a = self.ent2.get()
		b = self.ent3.get()
		c = self.ent4.get()
		d = self.ent5.get()

		try:
			if a != "" and b != "" and c != "" and d !="":
				sql_command = """Insert into customers values ("%s","%s","%s","%s");"""
				curs.execute(sql_command%(a, b, c, d))


				sql_command = """SELECT * from customers;"""

				curs.execute(sql_command)

				# curs.fetchall()
				result = curs.fetchall()  # select와 관련된 기능 (select 출력값 보여주기 위해 사용) , workbench 결과를 한 줄 씩 읽음
				for i in result:
					print(i)
				messagebox.showinfo('welcome', '회원가입을 환영합니다. 다시 실행해 로그인하세요')

			else:
				raise Exception
		except:
			messagebox.showinfo('Error','다시 입력해주세요')



root = Tk()

conn= db.connect("localhost", user="root" ,password="dgu1234!", db="hw2") # connect라는 class로 conn이라는 연결 객체 생성
curs= conn.cursor() # connect 클래스 안에 cursor라는 class 이용하여 curs 객체 생성 , cursor는 Mysql과 의사소통하는 객체 (쿼리실행, 결과 값 담는 역할 등)

sql_command = """SELECT customer_id,id_password from customers;"""

curs.execute(sql_command)

result=curs.fetchall() # select와 관련된 기능 (select 출력값 보여주기 위해 사용) , workbench 결과를 한 줄 씩 읽음

for row1,row2 in result:

	print("customer_id : " + row1)
	print("id_password : " + row2)

myapp = MyApp(root)
root.mainloop()

conn.commit() # 선언해줌으로써 insert,delete,update 사용 가능
curs.close()
conn.close()

