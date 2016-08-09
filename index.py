#!/usr/bin/env python
# coding=utf-8

from flask import Flask,render_template
from aws import ec2

app = Flask(__name__)

def abc():
    return "abc"


r =  ec2.get_all_instances()
lenth = len(r)

def public_info():
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
    page_num = len(range(1,len(r)+1)[::20])
    pub_info = [page_num,instance_info]
    return pub_info
 
@app.route('/')
def index(number=20):
    pub_info = public_info()
    page_num = pub_info[0]
    instance_info = pub_info[1]
    instance_id = pub_info[1].keys()
    head_ten = instance_id[0:number]
    return render_template('index.html',page_num=range(1,page_num+1),head_ten=head_ten,instance_info=instance_info)
        
@app.route('/page/<int:page_id>')
def page_splite(page_id,number=20):
    pub_info = public_info()
    page_num = pub_info[0]
    instance_info = pub_info[1]
    instance_id = pub_info[1].keys()
    splite_index = range(len(r))[::number]
    if page_id > 0:
        if page_id < page_num:
            index_id = [splite_index[page_id-1],splite_index[page_id]]
            page_data = instance_id[index_id[0]:index_id[1]]
        elif page_id == page_num:
            index_id = [splite_index[page_id-1],lenth-1]
            page_data = instance_id[index_id[0]:index_id[1]]

    return render_template('fenye.html',page_data=page_data,page_num=range(1,page_num+1),instance_info=instance_info)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)

