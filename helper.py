import pandas as pd

def region_preprocessing(df):
	# Region Fixes
	df.loc[df['region']=="Phoenix, AZ", 'region'] = "AZ"
	df.loc[df['region']=="Cedar Rapids, IA", 'region'] = "IA"
	df.loc[df['region']=="Kansas City, MO", 'region'] = "MO"
	df.loc[df['region']=="Germantown, MD", 'region'] = "MD"
	df.loc[df['region']=="California", 'region'] = "CA"
	df.loc[df['region']=="Torrance, CA", 'region'] = "CA"
	df.loc[df['region']=="Minneapolis, MN", 'region'] = "MN"
	df.loc[df['region']=="Raleigh, NC", 'region'] = "NC"
	df.loc[df['region']=="Golden Valley, MN", 'region'] = "MN"
	df.loc[df['region']=="Melville, NY", 'region'] = "NY"
	df.loc[df['region']=="Pittsburgh, PA", 'region'] = "PA"
	df.loc[df['region']=="Morris Plains, NJ", 'region'] = "NJ"
	df.loc[df['region']=="Denver, CO", 'region'] = "CO"
	df.loc[df['region']=="Des Plaines, IL", 'region'] = "IL"
	df.loc[df['region']=="Richmond, VA", 'region'] = "VA"
	df.loc[df['region']=="Irvine, CA", 'region'] = "CA"
	df.loc[df['region']=="Tempe, AZ", 'region'] = "AZ"
	df.loc[df['region']=="Houston, TX", 'region'] = "TX"
	df.loc[df['region']=="South Bend, IN", 'region'] = "IN"
	df.loc[df['region']=="Michigan", 'region'] = "MI"
	df.loc[df['region']=="Clearwater, FL", 'region'] = "FL"
	df.loc[df['region']=="Sterling, VA", 'region'] = "VA"
	df.loc[df['region']=="Fort Washington, PA", 'region'] = "PA"
	df.loc[df['region']=="Portland, OR", 'region'] = "OR"
	df.loc[df['region']=="Pennsylvania", 'region'] = "PA"
	df.loc[df['region']=="Thousand Oaks, CA", 'region'] = "CA"
	df.loc[df['region']=="North Carolina", 'region'] = "NC"
	df.loc[df['region']=="Redmond, WA", 'region'] = "WA"
	df.loc[df['region']=="Seattle, WA", 'region'] = "WA"
	df.loc[df['region']=="Richardson, TX", 'region'] = "TX"
	df.loc[df['region']=="Tucson, AZ", 'region'] = "AZ"
	df.loc[df['region']=="Naperville, IL", 'region'] = "IL"
	df.loc[df['region']=="Colonial Heights, VA", 'region'] = "VA"
	df.loc[df['region']=="Cumberland, RI", 'region'] = "RI"
	df.loc[df['region']=="Tulsa, OK", 'region'] = "OK"
	df.loc[df['region']=="Illinois", 'region'] = "IL"
	return df


