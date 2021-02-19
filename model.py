import pymysql

connection=pymysql.connect(host="localhost",user="root",database="employee_db",port=3306,autocommit=True)

cursor=connection.cursor()

class Emp:
    def __init__(self,name,email,password,sal,dept,designation):
        self.name = name
        self.email = email
        self.password = password
        self.sal = sal
        self.dept = dept
        self.designation = designation


def login(id, pwd):
    try:
        query = "select admin_id,admin_pwd from admin where admin_id=%s and admin_pwd=%s"
        cursor.execute(query, (id, pwd))
        data = cursor.fetchall()
        if len(data) > 0:
            return data
        else:
            return "Invalid User Id or Password"
    except BaseException as ex:
        print(ex)

def emp_register(email,password,name,dept,designation,sal):
    obj=Emp(name,email,password,sal,dept,designation)
    query="insert into employees(emp_name,emp_email,emp_dept,emp_designation,emp_sal,emp_pwd)values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(obj.name,obj.email,obj.dept,obj.designation,obj.sal,obj.password))

def employeedata():
    query="select emp_id,emp_name,emp_dept,emp_sal,emp_designation from employees"
    cursor.execute(query)
    data=cursor.fetchall()
    return data

def search_emp(obj,input):
    if obj == "Name":
        query = "select emp_id,emp_name,emp_dept,emp_designation,emp_sal from employees where emp_name = '{}' "\
            .format(input)
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    elif obj == "ID":
        query = "select emp_id,emp_name,emp_dept,emp_designation,emp_sal from employees where emp_id = '{}' "\
            .format(int(input))
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    elif obj == "Department":
        query = "select emp_id,emp_name,emp_dept,emp_designation,emp_sal from employees where emp_dept = '{}' "\
            .format(input)
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    elif obj == "Designation":
        query = "select emp_id,emp_name,emp_dept,emp_designation,emp_sal from employees where emp_designation = '{}' "\
            .format(input)
        cursor.execute(query)
        data = cursor.fetchall()
        return data


def gen_Sal(id):
    try:
        query = "select emp_id,emp_name,emp_dept,emp_designation,emp_sal from employees where emp_id='{}'".format(int(id))
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) > 0:
            print(data)
            return data
        else:
            return "Invalid User Id or Password"
    except BaseException as ex:
        print(ex)



