import matplotlib.pyplot as plt
import pandas as pd

from constants import days, months, month_desc

def plot_annual_job_count(df, level, threshold):
	df_2017 = df[df['year']==2017]
	df_2018 = df[df['year']==2018]
	countries_2017, count_by_country_2017 = get_top_regions_and_job_count(df_2017, level, threshold)
	countries_2018, count_by_country_2018 = get_top_regions_and_job_count(df_2018, level, threshold)
	plt.figure(0)
	#plt.pie(count_by_country_2017, labels=countries_2017, autopct='%1.1f%%')
	plt.bar(countries_2017, count_by_country_2017)
	plt.title("Engineering Job postings - 2017")
	plt.figure(1)
	#plt.pie(count_by_country_2018, labels=countries_2018, autopct='%1.1f%%')
	plt.bar(countries_2018, count_by_country_2018)
	plt.title("Engineering Job postings - 2018")
	plt.show()

	
def plot_job_count(df, level, threshold):
	countries, count_by_country = get_top_regions_and_job_count(df, level, threshold)
	plt.pie(count_by_country, labels=countries, autopct='%1.1f%%')
	plt.title("Engineering Job postings")
	plt.show()


def get_top_regions_and_job_count(df, level, threshold):
	count_by_region = df[level].value_counts()
	regions = []
	others_count = 0
	for region,count in count_by_region.items():
		if count>threshold:
			regions.append(region)
		else: others_count += count
	count_by_region = [count_by_region[region] for region in regions]
	regions.append("Others")
	count_by_region.append(others_count)
	return regions, count_by_region


def plot_monthly_trend(df):
	df_2017 = df[df['year']==2017]
	df_2018 = df[df['year']==2018]

	print("----------- 2017 ------------")
	print(df_2017['month'].value_counts())
	#print(df_2017['day'].value_counts())
	print("----------- 2018 ------------")
	print(df_2018['month'].value_counts())

	df_grouped_month_2017 = df_2017.groupby(['month']).size()
	df_grouped_month_2018 = df_2018.groupby(['month']).size()
	jobs_count_per_month = [df_grouped_month_2017[month] if month in df_grouped_month_2017.keys() else 0 for month in months]
	for month in range(1,len(df_grouped_month_2018)+1):
		if month in df_grouped_month_2018.keys():
			jobs_count_per_month.append(df_grouped_month_2018[month])

	plt.plot(month_desc,jobs_count_per_month)
	plt.title("Engineering Job Postings per month")
	plt.xlabel("Month")
	plt.ylabel("Total Job Postings")
	plt.grid(linestyle='--')
	plt.show()

