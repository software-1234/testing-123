import json

def parse_file(file):
	mylist_2=[]
	print(file)
	for i in range(0,9):
	  	print i
		if file['businesses'][i]['location']['address1'] is None:
			my_list=['Name: '+file['businesses'][i]['name'],'URL: '+file['businesses'][i]['url'],'Phone: '+file['businesses'][i]['phone'],'Address: None',' ',file['businesses'][i]['rating']]
		else:	
	      		my_list=['Name: '+file['businesses'][i]['name'],file['businesses'][i]['url'],'Phone: '+file['businesses'][i]['phone'],'Address: '+ file['businesses'][i]['location']['address1']+',' ,file['businesses'][i]['location']['city']+', '+file['businesses'][i]['location']['country'],file['businesses'][i]['rating']]
		mylist_2.append(my_list)
		#print mylist_2
	return mylist_2






