import json
def parse_file(file):
	mylist_2=[]
	#print(file)
	if file['total'] < 10:
		i=file['total']
		for k in range(0,i):
			if file['businesses'][k]['location']['address1'] is None:
                                my_list=[file['businesses'][k]['name'],'URL: '+file['businesses'][k]['url'],'Phone: '+file['businesses'][k]['phone'],'Address: None',' ',file['businesses'][k]['rating'], file['businesses'][k]['coordinates']['latitude'],file['businesses'][k]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+file['businesses'][k]['price'], file['businesses'][k]['review_count']]
			elif file['businesses'][k]['price'] is None:
                                my_list=[file['businesses'][k]['name'],'URL: '+file['businesses'][k]['url'],'Phone: '+file['businesses'][k]['phone'],'Address: None',' ',file['businesses'][k]['rating'], file['businesses'][k]['coordinates']['latitude'],file['businesses'][k]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: N/A', file['businesses'][k]['review_count']]
                        else:   
                                my_list=[file['businesses'][k]['name'],file['businesses'][k]['url'],'Phone: '+file['businesses'][k]['phone'],'Address: '+ file['businesses'][k]['location']['address1']+',' ,file['businesses'][k]['location']['city']+', '+file['businesses'][k]['location']['country'],file['businesses'][k]['rating'], file['businesses'][k]['coordinates']['latitude'],file['businesses'][k]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+file['businesses'][k]['price'], file['businesses'][k]['review_count']]
			mylist_2.append(my_list)
	else:
		for i in range(0,10):
	  		#print i
			if file['businesses'][i]['location']['address1'] is None:
				my_list=[file['businesses'][i]['name'],'URL: '+file['businesses'][i]['url'],'Phone: '+file['businesses'][i]['phone'],'Address: None',' ',file['businesses'][i]['rating'],file['businesses'][i]['coordinates']['latitude'],file['businesses'][i]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+ file['businesses'][i]['price'],file['businesses'][i]['review_count']]	
			elif file['businesses'][i]['price'] is None:
                                my_list=[file['businesses'][i]['name'],'URL: '+file['businesses'][i]['url'],'Phone: '+file['businesses'][i]['phone'],'Address: None',' ',file['businesses'][i]['rating'], file['businesses'][i]['coordinates']['latitude'],file['businesses'][i]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: N/A', file['businesses'][i]['review_count']]
			else:	
	      			my_list=[file['businesses'][i]['name'],file['businesses'][i]['url'],'Phone: '+file['businesses'][i]['phone'],'Address: '+ file['businesses'][i]['location']['address1']+',' ,file['businesses'][i]['location']['city']+', '+file['businesses'][i]['location']['country'],file['businesses'][i]['rating'],file['businesses'][i]['coordinates']['latitude'],file['businesses'][i]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+file['businesses'][i]['price'],file['businesses'][i]['review_count']]		
			mylist_2.append(my_list)		
	return mylist_2

def parse_phone(file):
        mylist_2=[]
	if file['businesses'][0]['location']['address1'] is None:
                my_list=[file['businesses'][0]['name'],'URL: '+file['businesses'][0]['url'],'Phone: '+file['businesses'][0]['phone'],'Address: None',' ',file['businesses'][0]['rating'],file['businesses'][0]['coordinates']['latitude'],file['businesses'][0]['coordinates']['longitude'],'' ,'','Price: '+file['businesses'][0]['price'], file['businesses'][0]['review_count']]        	
	elif file['businesses'][0]['price'] is None:
                my_list=[file['businesses'][0]['name'],'URL: '+file['businesses'][0]['url'],'Phone: '+file['businesses'][0]['phone'],'Address: None',' ',file['businesses'][0]['rating'],file['businesses'][0]['coordinates']['latitude'],file['businesses'][0]['coordinates']['longitude'],'' ,'','Price: N/A',file['businesses'][0]['review_count']]
	else: 
       		my_list=[file['businesses'][0]['name'],file['businesses'][0]['url'],'Phone: '+file['businesses'][0]['phone'],'Address: '+ file['businesses'][0]['location']['address1']+',' ,file['businesses'][0]['location']['city']+', '+file['businesses'][0]['location']['country'],file['businesses'][0]['rating'], file['businesses'][0]['coordinates']['latitude'],file['businesses'][0]['coordinates']['longitude'],file['businesses'][0]['coordinates']['longitude'],file['businesses'][0]['coordinates']['latitude'],'Price: '+ file['businesses'][0]['price'], file['businesses'][0]['review_count']] 			
	mylist_2.append(my_list)           
        
	return mylist_2





