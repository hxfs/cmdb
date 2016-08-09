#!/usr/bin/env python
# coding=utf-8

from flask import Flask,render_template
from aws import ec2

app = Flask(__name__)

def abc():
    return "abc"


r =  ec2.get_all_instances()

@app.route('/')
def index():
    #r =  ec2.get_all_instances()
    lenth = len(r)
    instance_info = {}
    for i in range(lenth):
        private_ip = r[i].private_ip_address
        public_ip = r[i].ip_address
        instance_id = r[i].id
        try:
            tags = r[i].tags['Name']
        except Exception:
            tags = r[i].tags['name']
        
        instance_info[instance_id]=[private_ip,public_ip,tags]
    return render_template("index.html",instance_info=instance_info,lenth=lenth)

@app.route('/page')
def fenye():
    lenth = len(r)
    page_ = lenth % 20
    if page_ == 0:
        page_num = lenth // 20
    else:
        page_num = lenth // 20 + 1
    return render_template("fenye.html",page_num=range(page_num)) 
        


    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)

