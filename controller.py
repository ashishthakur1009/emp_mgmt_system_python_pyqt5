import model

import sys
sys.path.append("..")

def login(id,pwd):
    data = model.login(id,pwd)
    return data

def emp_register(email,password,name,department,designation,sal):
    emp_data = model.emp_register(email,password,name,department,designation,sal)
    return emp_data

def employeedata():
    data = model.employeedata()
    return data

def search_emp(obj,input):
    data = model.search_emp(obj,input)
    return data

def gen_Sal(id):
    data = model.gen_Sal(int(id))
    return data

