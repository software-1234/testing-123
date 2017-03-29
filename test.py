import os
import sys

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
import logging
from flask import json,Flask,render_template,request,jsonify
#from flask import Flask
#import sample
import api_yelp
import parse
app = Flask(__name__)


'''@app.route('/')
def do():
    return render_template('./index2.html')
'''
@app.route('/')
def api():
    return render_template('index2.html')

@app.route('/api/phone')
def phone():
    return render_template('phone.html')

@app.route('/api/search/phone',methods = ['POST'])
def phone_search():
    if request.method=='POST':
    	business_list=[]
	phone=request.form['phone']
	businesses = api_yelp.search_phone(phone)
	businesses=parse.parse_phone(businesses)
	
	return render_template("index3.html",my_list=businesses,num_businesses=1)

@app.route('/api/search',methods = ['POST'])
def index():   
    #food = request.values.get('food')
    print(request.method)
    if request.method=='POST':
	business_list=[]
	term=request.form['term']
	place=request.form['place']
	
        #price=request.form.get('price1')
	price1=request.form.get('price1')
        price2=request.form.get('price2')
	price3=request.form.get('price3')
	price4=request.form.get('price4')
	auto=request.form.get('auto')
	phone=request.form.get('phone')
	stars=request.form.get('stars')
	price=''
	if price1:
		price='1'
	if price2:
		if price=='':
			price='2'
		else:
			price=price+',2'
	if price3:
		if price=='':
                        price='3'
                else:
                        price=price+',3'
		price='3'
	if price4:
		if price=='':
                        price='4'
                else:
                        price=price+',4'
	if price:
		businesses = api_yelp.search_price(term,place,price)
	elif auto:
		businesses = api_yelp.auto_location(37.7474,-122.4392,term)
	elif stars:
		businesses = api_yelp.search_best(term, place)
	else:
		businesses = api_yelp.search(term,place)
        #print(businesses)
	#for i in (0,9):
	#	business_list.append(businesses['businesses'][i]['name']) 
	num_businesses=businesses["total"]
	if num_businesses==0:
		return render_template("no_results.html")
		
	if phone:
        	businesses=parse.parse_phone(businesses)		
	else:
 		businesses=parse.parse_file(businesses)
	#print(businesses[3])
	#print businesses
	return render_template("index3.html",my_list=businesses,num_businesses=num_businesses)
    
    #print businesses['display_phone']

    #return render_template('index2.html', businesses=businesses)
   
	
@app.route('/about')
def about():
    return 'The about page'

app.run(debug=True)
