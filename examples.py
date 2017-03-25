from yelpapi import YelpAPI
import argparse
from pprint import pprint

argparser = argparse.ArgumentParser(description='Example Yelp queries using yelpapi. Visit https://www.yelp.com/developers/v3/manage_app to get the necessary API keys.')
'''argparser.add_argument('--client_id', type=str, help='Yelp Fusion API client ID')
argparser.add_argument('--client_secret', type=str, help='Yelp Fusion API client secret')'''
argparser.add_argument('--term', type=str, help='term search')
argparser.add_argument('--location', type=str, help='location')
argparser.add_argument('--phone', type=str, help='phone')
argparser.add_argument('--cat', type=str, help='categories')
argparser.add_argument('--lat', type=float, help='latitude')
argparser.add_argument('--long', type=float, help='longitude')
argparser.add_argument('--transaction', type=str, help='delivery or no')
argparser.add_argument('--id', type=str, help='place name')
argparser.add_argument('--autocomp', type=str, help='autocomplete')
args = argparser.parse_args()
yelp_api = YelpAPI('u24el7WOE_eevCoQq_b34A', '0nwC1fGOtEbOJtmtBQYJ93OiT6eF0HeMqUU9ZTpK3hbO81alE2iWQ4blmFTTNXnq')


"""
    Example search by location text and term. 
    
    Search API: https://www.yelp.com/developers/documentation/v3/business_search
"""
print('***** 5 best rated ice cream places in Austin, TX *****\n{}\n'.format("yelp_api.search_query(term='ice cream', location='austin, tx', sort_by='rating', limit=5)"))
if args.location and args.term:
	response = yelp_api.search_query(term=args.term, location=args.location, sort_by='rating', limit=5)
	pprint(response)
print('\n-------------------------------------------------------------------------\n')

"""
    Example phone search query.
    
    Phone Search API: https://www.yelp.com/developers/documentation/v3/business_search_phone
"""

print('***** search for business by phone number *****\n{}\n'.format("yelp_api.phone_search_query(phone='args.phone')"))
if args.phone:
	response = yelp_api.phone_search_query(phone=args.phone)
	pprint(response)
print('\n-------------------------------------------------------------------------\n')


"""
    Example transaction search query.
    
    Transaction Search API: https://www.yelp.com/developers/documentation/v3/transactions_search
"""
print("***** businesses in Dallas supporting delivery transactions *****\n{}\n".format("yelp_api.transaction_search_query(transaction_type='delivery', location='dallas, tx')"))
if args.transaction and args.location:
	response = yelp_api.transaction_search_query(transaction_type=args.transaction, location=args.location)
	pprint(response)
print('\n-------------------------------------------------------------------------\n')


"""
    Example business query.
    
    Business API: https://www.yelp.com/developers/documentation/v3/business
"""
print("***** business information for Amy's on 6th St. *****\n{}\n".format("yelp_api.business_query(id='amys-ice-creams-austin-3')"))
response = yelp_api.business_query(id='amys-ice-creams-austin-3')
pprint(response)
print('\n-------------------------------------------------------------------------\n')

"""
    Example autocomplete query.
    
    Autocomplete API: https://www.yelp.com/developers/documentation/v3/autocomplete
    centroid: https://www.flickr.com/places/info/2427422
"""
print("***** autocomplete results for 'Hambur' in Iowa City *****\n{}\n".format("yelp_api.autocomplete_query(text='Hambur', longitude=-91.5327, latitude=41.6560)"))
if args.term and args.lat and args.long:
	response = yelp_api.autocomplete_query(text=args.term, longitude=args.long, latitude=args.lat)
	pprint(response)
print('\n-------------------------------------------------------------------------\n')


"""
    Example erroneous search query.
"""
print('***** sample erroneous search query *****\n{}\n'.format("yelp_api.search_query(term='ice cream', location='austin, tx', sort_by='BAD_SORT')"))
try:
    # sort can only take on values "best_match", "rating", "review_count", or "distance"
    yelp_api.search_query(term='ice cream', location='austin, tx', sort_by='BAD_SORT')
except YelpAPI.YelpAPIError as e:
    print(e)
print('\n-------------------------------------------------------------------------\n')


"""
    Example erroneous business query.
"""
print('***** sample erroneous business query *****\n{}\n'.format("yelp_api.business_query(id='fake-business')"))
try:
    yelp_api.business_query(id='fake-business')
except YelpAPI.YelpAPIError as e:
    print(e)
