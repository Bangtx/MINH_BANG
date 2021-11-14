from tkinter import *
from tkinter.ttk import Combobox
from read_data import *

win = Tk()
win.title('my app')
width_screen = win.winfo_screenwidth()
hieght_screen = win.winfo_screenheight()
width = int((width_screen - 1200) / 2)
heigh = int((hieght_screen - 900) / 2)
win.geometry(f'1200x900+{width}+{heigh}')
Label(win, bg='white').place(width=1200, heigh=900, x=0, y=0)


def reload():
    global ds_truong, data_frame_student, ds_diem, all_line
    global list_id_hoc_sinh, list_ten_hoc_sinh, list_truong_hoc_sinh, list_ngay_sinh_hoc_sinh
    list_id_hoc_sinh, list_ten_hoc_sinh, list_truong_hoc_sinh, list_ngay_sinh_hoc_sinh = get_data_student()
    data_frame_student = get_data_frame_student()
    ds_diem = get_data_point()
    ds_truong = get_data_school()
    all_line = all_lines()


reload()


def get_data_insert():
    global entry_id, entry_ten, entry_gioi_tinh, entry_ngay_sinh, entry_truong
    gioi_tinh = 1 if entry_gioi_tinh.get() == 'nu' or entry_gioi_tinh.get() == 'Nu' else 0
    data_insert = f'{entry_id.get()} {entry_ten.get()} {gioi_tinh} {entry_ngay_sinh.get()} {entry_truong.get()[:4]}\n'
    return data_insert


def insert_screen(even):
    global list_truong_hoc_sinh, entry_id, entry_ten, entry_gioi_tinh, entry_ngay_sinh, entry_truong
    win_1 = Tk()
    win_1.title('Chen ds')
    width_1 = int((width_screen - 600) / 2)
    heigh_1 = int((hieght_screen - 400) / 2)
    win_1.geometry(f'600x400+{width_1}+{heigh_1}')
    Label(win_1, text='ID(xxxx)', font='times 15').place(width=150, heigh=50, x=100, y=50)
    entry_id = Entry(win_1, font='times 15')
    entry_id.place(width=200, heigh=30, x=300, y=60)
    Label(win_1, text='Họ Tên', font='times 15').place(width=150, heigh=50, x=100, y=100)
    entry_ten = Entry(win_1, font='times 15')
    entry_ten.place(width=200, heigh=30, x=300, y=110)
    Label(win_1, text='Giới Tính', font='times 15').place(width=150, heigh=50, x=100, y=150)
    entry_gioi_tinh = Entry(win_1, font='times 15')
    entry_gioi_tinh.place(width=200, heigh=30, x=300, y=160)
    Label(win_1, text='Ngày Sinh(dd/mm/yyyy)', font='times 15').place(width=200, heigh=50, x=50, y=200)
    entry_ngay_sinh = Entry(win_1, font='times 15')
    entry_ngay_sinh.place(width=200, heigh=30, x=300, y=210)
    Label(win_1, text='Trường', font='times 15').place(width=150, heigh=50, x=100, y=250)
    entry_truong = Combobox(win_1, font='times 15', value=ds_truong)
    entry_truong.place(width=200, heigh=30, x=300, y=260)

    def insert():
        data_insert = get_data_insert()
        data_get = list_box_student.get(ANCHOR)
        index = all_line.index(data_get.replace('\n', '')) + 1
        replace_line('DanhSach.txt', index, data_insert)
        win_1.destroy()


    Button(win_1, text='save', command=insert).place(width=100, heigh=30, x=400, y=300)
    win_1.mainloop()


def xem_file():
    global list_box_student, list_box_diem, list_box_truong, data_frame_student, ds_diem
    reload()
    list_box_student = Listbox(win, font='times 14')
    list_box_student.place(width=400, heigh=700, x=150, y=100)
    for i in range(len(data_frame_student)):
        list_box_student.insert(i, data_frame_student[i])

    list_box_diem = Listbox(win, font='times 14')
    list_box_diem.place(width=300, heigh=700, x=550, y=100)
    for i in range(len(ds_diem)):
        list_box_diem.insert(i, ds_diem[i])

    list_box_truong = Listbox(win, font='times 14')
    list_box_truong.place(width=300, heigh=700, x=850, y=100)
    for i in range(len(ds_truong)):
        list_box_truong.insert(i, ds_truong[i])


def xoa_file():
    global list_box_student, list_box_diem, list_box_truong, all_line
    xem_file()

    def delete(event):
        global list_box_student, list_box_diem, list_box_truong, all_line
        student = list_box_student.get(ANCHOR)
        index = all_line.index(student.replace('\n', ''))
        replace_line('DanhSach.txt', index, '')
        xoa_file()

    list_box_student.bind('<Double-1>', delete)
    Label(win, text='click vao phần cần xóa để xóa', bg='white').place(width=750, heigh=100, x=150, y=0)


def them_hang_sau():
    global list_box_student, list_box_diem, list_box_truong, all_line
    xem_file()

    def add_row(event):
        global list_box_student, list_box_diem, list_box_truong, all_line
        student = list_box_student.get(ANCHOR)
        index = all_line.index(student.replace('\n', ''))
        # replace_line('DanhSach.txt', index, '')

        xoa_file()

    list_box_student.bind('<Double-1>', insert_screen)
    Label(win, text='click vao phần cần muốn chèn sau', bg='white').place(width=750, heigh=100, x=150, y=0)


def them_hang_truoc():
    global list_box_student, list_box_diem, list_box_truong, all_line
    xem_file()

    def add_row(event):
        global list_box_student, list_box_diem, list_box_truong, all_line
        student = list_box_student.get(ANCHOR)
        index = all_line.index(student.replace('\n', ''))
        # replace_line('DanhSach.txt', index, '')
        xoa_file()

    list_box_student.bind('<Double-1>', add_row)
    Label(win, text='click vao phần cần muốn chèn truoc', bg='white').place(width=750, heigh=100, x=150, y=0)


Button(win, text='xem file', font='times 15', command=xem_file).place(width=100, heigh=30, x=10, y=100)
Button(win, text='Xóa', font='times 15', command=xoa_file).place(width=100, heigh=30, x=10, y=150)
Button(win, text='Click vào mục muốn chèn sau', font='times 15', command=them_hang_sau).place(
    width=100, heigh=30, x=10, y=150
)
Button(win, text='Click vào mục muốn chèn trước', font='times 15', command=them_hang_truoc).place(
    width=100, heigh=30, x=10, y=200
)

win.mainloop()
