import pandas as pd
import csv
from datetime import datetime as dt
from helper import region_preprocessing
from plot import plot_job_count, plot_annual_job_count, plot_monthly_trend
from constants import columns_to_keep, COUNTRY, REGION

pd.set_option('display.max_columns', 25)

job_listings_engineering_7 = 'datasets/job_listings_engineering_7.csv'
job_listings_engineering_6 = 'datasets/job_listings_engineering_6.csv'
job_listings_engineering_5 = 'datasets/job_listings_engineering_5.csv'
job_listings_engineering_4 = 'datasets/job_listings_engineering_4.csv'
job_listings_engineering_3 = 'datasets/job_listings_engineering_3.csv'
job_listings_engineering_1 = 'datasets/job_listings_engineering_1.csv'


def run_job_listings():
	df = get_dataframe()
	
	""" Preprocess and add columns """
	df = df[df['posted_date'].notnull()]
	df['as_of_date']=pd.to_datetime(df['as_of_date'])
	df['posted_date']=pd.to_datetime(df['posted_date'])
	df['year'] = df['as_of_date'].dt.year
	df['month'] = df['as_of_date'].dt.month
	df['day'] = df['as_of_date'].dt.day	
	df = region_preprocessing(df)
	""" Done with preprocessing """

	plot_monthly_trend(df)

	df = df[df['country'].notnull()]
	plot_job_count(df, level=COUNTRY, threshold=10000)
	plot_annual_job_count(df, level=COUNTRY, threshold=10000)

	df_USA = df[df['country']=="USA"]
	plot_job_count(df_USA, level=REGION, threshold=10000)
	plot_annual_job_count(df_USA, level=REGION, threshold=5000)

	""" Analyse the sharp increase in Washington job postings """
	df_2017 = df[df['year']==2017]
	df_2018 = df[df['year']==2018]
	df_2017_WA = df_2017[df_2017['region']=="WA"]
	df_2018_WA = df_2018[df_2018['region']=="WA"]

	print("----------- 2017 ------------")
	print(df_2017_WA['domain'].value_counts())
	print("----------- 2018 ------------")
	print(df_2018_WA['domain'].value_counts())


def get_dataframe():
	df_1 = pd.read_csv(job_listings_engineering_1)
	df_3 = pd.read_csv(job_listings_engineering_3)
	df_4 = pd.read_csv(job_listings_engineering_4)
	df_5 = pd.read_csv(job_listings_engineering_5)
	df_6 = pd.read_csv(job_listings_engineering_6)
	df_7 = pd.read_csv(job_listings_engineering_7)
	return pd.concat([df_1,df_3,df_4,df_5,df_6,df_7])


def filter_data(orig_file_path, new_file_path):
	chunks = pd.read_csv(orig_file_path, chunksize=1000000)

	prev_df= pd.DataFrame(columns=columns_to_keep)
	for df in chunks:
		df = preprocess_and_filter_columns(df)
		df = pd.concat([prev_df, df])
		prev_df = df

	df.to_csv(new_file_path, index=False)

def preprocess_and_filter_columns(df):
	df = df[df['category']=='Engineering']
	df = df[columns_to_keep]
	return df


if __name__ == '__main__':
	run_job_listings()