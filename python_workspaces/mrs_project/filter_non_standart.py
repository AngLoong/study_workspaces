#!python3
# v1.4
import sqlite3
import time


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

conn = sqlite3.connect('library.db')
c = conn.cursor()
print("Open database sucessfully")

# cursor = c.execute("SELECT SN号 from 酶标生产发货")
# for row in cursor:
#     print("SN : ",row[0],"\n")

# 用户登录
adm = False
pwd = input("请输入管理密码，如果非管理员，直接按回车")
if pwd == "2001":
    adm = True

cursor = c.execute("SELECT max(记录编号) from 非标滤光片记录")
for row in cursor:
    print("max record NO",row[0])
    record_NO_max = int(row[0])

command_exit = True
while command_exit:
    command = input("请输入指令：\n 1.查看滤光片\n 2.出库滤光片\n 3. 入库滤光片 \n 0.保存并退出")
    if command == "1":
        print("查看滤光片")
        wave = input("请输入滤光片波长")
        cursor = c.execute("SELECT * from 非标滤光片库存 WHERE 波长 IS "+"\'"+wave+"\'")
        for row in cursor:
            print("材料编号 ： ", row[0])
            print("波长 ： ", row[1])
            print("供应商 ： ", row[2])
            print("库存数量 : ", row[3])
            print("最后更新日期 ： ", row[4])
            print("备注 ： ", row[5], "\n")
    elif command == "2" and adm == True:
        print("出库滤光片")
        apostrophe = "\'"
        record_NO_max=record_NO_max+1
        record_NO = str(record_NO_max)
        #filter_NO = input("材料编号")
        wave = input("波长")
        if wave.isnumeric():
            pass
        else:
            print("录入错误，请重新输入")
            continue
        supplier_type = input("供应商:A 汇博；B 纳宏；C 北京")
        if supplier_type == "A" or supplier_type == "a":
            supplier = "汇博"
            filter_NO = "KGL"+wave+"A"
        elif supplier_type == "B" or supplier_type == "b":
            supplier = "纳宏"
            filter_NO = "KGL"+wave+"B"
        elif supplier_type == "C" or supplier_type == "c":
            supplier = "北京"
            filter_NO = "KGL"+wave+"C"
        else:
            print("录入错误，请重新输入")
            continue
        in_str = "0"
        out_str = input("出库数量")
        if out_str.isnumeric():
            pass
        else:
            print("录入错误，请重新输入")
            continue
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        seller = input("销售人")
        client = input("客户")
        remarks = input("备注")
        print("请确认信息！\n"+\
              "波长 ： "+wave+"\n"+\
              "厂商 ： "+supplier+"\n"+\
              "数量 ： "+out_str+"\n"+\
              "销售人 ： "+seller+"\n"+\
              "客户 ： "+client+"\n"+\
              "备注 “ "+remarks+"\n")
        in_enter = input("确认输入请输入y")
        if in_enter == "y" or in_enter == "Y":
            print("确认输入")
            pass
        else:
            print("取消输入")
            continue
        c.execute("INSERT INTO 非标滤光片记录 (记录编号,材料编号,波长,供应商,入库,出库,日期,销售人,客户,备注) VALUES ("+\
                  record_NO+","+\
                  apostrophe+filter_NO+apostrophe+","+\
                  apostrophe+wave+apostrophe+","+\
                  apostrophe+supplier+apostrophe+","+\
                  in_str+","+\
                  out_str+","+\
                  apostrophe+date+apostrophe+","+\
                  apostrophe+seller+apostrophe+","+\
                  apostrophe+client+apostrophe+","+\
                  apostrophe+remarks+apostrophe\
                  +')')
        cursor = c.execute("SELECT * from 非标滤光片库存 WHERE 材料编号 IS "+apostrophe+filter_NO+apostrophe)
        for row in cursor:
            total_count = row[3]

        total_count =str(int(total_count) - int(out_str))
        c.execute("UPDATE 非标滤光片库存 set 库存数量 = "+total_count+" WHERE 材料编号 IS "+apostrophe+filter_NO+apostrophe)
        c.execute("UPDATE 非标滤光片库存 set 最后更新日期 = "+apostrophe+date+apostrophe+" WHERE 材料编号 IS "+apostrophe+filter_NO+apostrophe)
    elif command == "3" and adm == True:
        print("入库滤光片")
        apostrophe = "\'"
        record_NO_max = record_NO_max + 1
        record_NO = str(record_NO_max)
        # filter_NO = input("材料编号")
        wave = input("波长")
        if wave.isnumeric():
            pass
        else:
            print("录入错误，请重新输入")
            continue
        supplier_type = input("供应商:A 汇博；B 纳宏；C 北京")
        if supplier_type == "A" or supplier_type == "a":
            supplier = "汇博"
            filter_NO = "KGL" + wave + "A"
        elif supplier_type == "B" or supplier_type == "b":
            supplier = "纳宏"
            filter_NO = "KGL" + wave + "B"
        elif supplier_type == "C" or supplier_type == "c":
            supplier = "北京"
            filter_NO = "KGL" + wave + "C"
        else:
            print("录入错误，请重新输入")
            continue
        in_str = input("入库数量")
        out_str = "0"
        if in_str.isnumeric():
            pass
        else:
            print("录入错误，请重新输入")
            continue
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        seller = ""
        client = ""
        remarks = input("备注")
        print("请确认信息！\n" + \
              "波长 ： " + wave + "\n" + \
              "厂商 ： " + supplier + "\n" + \
              "数量 ： " + in_str + "\n" + \
              "备注 “ " + remarks + "\n")
        in_enter = input("确认输入请输入y")
        if in_enter == "y" or in_enter == "Y":
            print("确认输入")
            pass
        else:
            print("取消输入")
            continue
        c.execute("INSERT INTO 非标滤光片记录 (记录编号,材料编号,波长,供应商,入库,出库,日期,销售人,客户,备注) VALUES (" + \
                  record_NO + "," + \
                  apostrophe + filter_NO + apostrophe + "," + \
                  apostrophe + wave + apostrophe + "," + \
                  apostrophe + supplier + apostrophe + "," + \
                  in_str + "," + \
                  out_str + "," + \
                  apostrophe + date + apostrophe + "," + \
                  apostrophe + seller + apostrophe + "," + \
                  apostrophe + client + apostrophe + "," + \
                  apostrophe + remarks + apostrophe \
                  + ')')
        cursor = c.execute("SELECT * from 非标滤光片库存 WHERE 材料编号 IS " + apostrophe + filter_NO + apostrophe)
        values = c.fetchall()
        print(len(values))
        if len(values) == 1:
            total_count = 0
            cursor = c.execute("SELECT * from 非标滤光片库存 WHERE 材料编号 IS " + apostrophe + filter_NO + apostrophe)
            for row in cursor:
                total_count = row[3]

            total_count = str(int(total_count) + int(in_str))
            c.execute("UPDATE 非标滤光片库存 set 库存数量 = " + total_count + " WHERE 材料编号 IS " + apostrophe + filter_NO + apostrophe)
            c.execute("UPDATE 非标滤光片库存 set 最后更新日期 = " + apostrophe + date + apostrophe + " WHERE 材料编号 IS " + apostrophe + filter_NO + apostrophe)
        elif len(values) == 0:
            c.execute("INSERT INTO 非标滤光片库存 (材料编号,波长,供应商,库存数量,最后更新日期,备注) VALUES (" + \
                      apostrophe+filter_NO+apostrophe+ "," + \
                      apostrophe + wave + apostrophe + "," + \
                      apostrophe + supplier + apostrophe + "," + \
                      in_str + "," + \
                      apostrophe + date + apostrophe + "," + \
                      apostrophe + "" + apostrophe \
                      + ')')
        else:
            print("ERROR")
            continue
    elif command == "0":
        command_exit = False
        conn.commit()
        conn.close()
        print("保存并退出")
    else:
        print("输入指令错误！")

