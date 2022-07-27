"""
存储一本书的程序:
标题,作者,年,ISBN

用户可以:
查看所有记录
他们可以搜索条目
添加条目
更新条目
关闭程序
"""
from tkinter import *
window = Tk()
# 标题
l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

# 用户输入
title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)



window.mainloop()