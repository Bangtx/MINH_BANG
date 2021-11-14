from itertools import product
from typing import re


def get_data_student():
    f = open('DanhSach.txt', 'r', encoding='UTF-8')
    ds_hoc_sinh = f.readlines()[11:]

    ds_hoc_sinh = list(map(lambda x: x.replace('\n', ''), ds_hoc_sinh))
    print(ds_hoc_sinh)
    list_id_hoc_sinh = list(map(lambda x: x[: 4], ds_hoc_sinh))
    list_ten_hoc_sinh = list(map(lambda x: x[5: 27], ds_hoc_sinh))
    list_truong_hoc_sinh = list(map(lambda x: x[-4:], ds_hoc_sinh))
    list_ngay_sinh_hoc_sinh = list(map(lambda x: x[-15: -5], ds_hoc_sinh))
    return list_id_hoc_sinh, list_ten_hoc_sinh, list_truong_hoc_sinh, list_ngay_sinh_hoc_sinh


list_id_hoc_sinh, list_ten_hoc_sinh, list_truong_hoc_sinh, list_ngay_sinh_hoc_sinh = get_data_student()


def all_lines():
    f = open('DanhSach.txt', 'r', encoding='UTF-8')
    all = f.readlines()
    all = list(map(lambda x: x.replace('\n', ''), all))
    return all


def get_data_frame_student():
    f = open('DanhSach.txt', 'r', encoding='UTF-8')
    ds_hoc_sinh = f.readlines()[11:]
    # ds_hoc_sinh = list(map(lambda x: x.replace('\n', ''), ds_hoc_sinh))
    return ds_hoc_sinh


def get_data_point():
    f = open('Diem.txt', 'r', encoding='UTF-8')
    ds_diem = f.readlines()[9:]
    # ds_hoc_sinh = list(map(lambda x: x.replace('\n', ''), ds_hoc_sinh))
    return ds_diem


def get_data_school():
    f = open('Truong.txt', 'r', encoding='UTF-8')
    ds_truong = f.readlines()[9:]
    # ds_hoc_sinh = list(map(lambda x: x.replace('\n', ''), ds_hoc_sinh))
    return ds_truong


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()