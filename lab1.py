import  urllib.request
import  urllib.error
import pandas as pd
import numpy as np
from datetime import datetime, date, time
import os.path

def downloadVHSData():
	url_start="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"
	index=int(input('Choose index of province from 1 to 25:\n>>>'))
	while index>25 or index<1:
		print('Try again')
		index=int(input('Choose index of province from 1 to 25:\n>>>'))
	if index<10:
		url_end="0"+str(index)+".txt"
	else:
		url_end=str(index)+".txt"
	url=url_start+url_end
	vhi_url = urllib.request.urlopen(url)
	date_time=str(datetime.now())
	date_time=date_time.replace(" ", "_")
	date_time=date_time.replace(":", "_")
	date_time=date_time.replace("-", "_")
	name="vhi_id_"+str(index)+"__"+date_time+".csv"
	out = open(name,'wb')
	out.write(vhi_url.read())
	out.close()
	print ("VHI №"+str(index)+" is downloaded...\n\n")
#------------------------------------------------------------------------------------------------------------------------------------------------------
def show(path):
	if os.path.isfile(path):
		print("You`re viewing '"+path+"':")
		df = pd.read_csv(path, index_col=False, header=1)
		df=df.rename(columns={'%Area_VHI_LESS_15':'VHI<15'})
		df=df.rename(columns={'%Area_VHI_LESS_35':'VHI<35'})
		print(df[:10])
	else:
		print('There is no such file\n')
#------------------------------------------------------------------------------------------------------------------------------------------------------
def maxDuringYear(path):
	if os.path.isfile(path):
		year=int(input('Choose year from 1981 to 2016:\n>>>'))
		while year>2016 or year<1981:
			print('Try again')
			year=int(input('Choose year from 1981 to 2016:\n>>>'))
		df = pd.read_csv(path, index_col=False, header=1)
		requiredYear=df[(df['year']==year)]
		max_vhi=0
		for vhi in requiredYear['VHI']:
			if max_vhi<vhi:
				max_vhi=vhi
		print("Maximum VHI during the "+str(year)+" was: "+str(max_vhi))
	else:
		print('There is no such file\n')	
#------------------------------------------------------------------------------------------------------------------------------------------------------
def minDuringYear(path):
	if os.path.isfile(path):
		year=int(input('Choose year from 1981 to 2016:\n>>>'))
		while year>2016 or year<1981:
			print('Try again')
			year=int(input('Choose year from 1981 to 2016:\n>>>'))
		df = pd.read_csv(path, index_col=False, header=1)
		requiredYear=df[(df['year']==year)]
		min_vhi=requiredYear['VHI'][requiredYear['VHI'].index[0]]
		for vhi in requiredYear['VHI']:
			if min_vhi>vhi:
				min_vhi=vhi
		print("Minimum VHI during the "+str(year)+" was: "+str(min_vhi))
	else:
		print('There is no such file\n')
#------------------------------------------------------------------------------------------------------------------------------------------------------
def extremeDroughtHigherThan(path):
	if os.path.isfile(path):
		percent=int(input('Choose percentage more than 0 and lesss than 100:\n>>>'))
		while percent>=100 or percent<=0:
			print('Try again')
			percent=int(input('Choose percentage more than 0 and lesss than 100:\n>>>'))
		df = pd.read_csv(path, index_col=False, header=1)
		extremeDroughtYears=df[(df['%Area_VHI_LESS_15']>percent)]
		notToRepeat=0
		print("Years, when extreme drought was registred in more than "+str(percent)+"% of provinces:\n")
		for YEAR in extremeDroughtYears['year']:
			if notToRepeat!=YEAR:
				print(YEAR)
			notToRepeat=YEAR
	else:
		print('There is no such file\n')
#------------------------------------------------------------------------------------------------------------------------------------------------------
def averageDroughtHigherThan(path):
	if os.path.isfile(path):
		percent=int(input('Choose percentage more than 0 and lesss than 100:\n>>>'))
		while percent>=100 or percent<=0:
			print('Try again')
			percent=int(input('Choose percentage more than 0 and lesss than 100:\n>>>'))
		df = pd.read_csv(path, index_col=False, header=1)
		averageDroughtYears=df[(df['%Area_VHI_LESS_35']>percent)]
		notToRepeat=0
		print("Years, when average drought was registred in more than "+str(percent)+"% of provinces:\n")
		for YEAR in averageDroughtYears['year']:
			if notToRepeat!=YEAR:
				print(YEAR)
			notToRepeat=YEAR
	else:
		print('There is no such file\n')
#------------------------------------------------------------------------------------------------------------------------------------------------------		
def reindexProvinces():
	d = {'one' : pd.Series(['try1'], index=['a']),
		'two' : pd.Series(['try2'], index=['a'])}
	reindexation = pd.DataFrame(d)
	print(reindexation)
	reindexation=pd.DataFrame(reindexation, index=[1, 2, 3, 4, 5,6, 7, 8, 9, 10,11, 12, 13, 14, 15,16, 17, 18, 19, 20,21,22, 23, 24, 25], columns=['first', 'second'])
#------------------------------------------------------------------------------------------------------------------------------------------------------
	reindexation['first'][1]='Autonomous_Republic_of_Crimea'
	reindexation['first'][2]='Cherkasy Oblast'
	reindexation['first'][3]='Chernihiv Oblast'
	reindexation['first'][4]='Chernivtsi Oblast'
	reindexation['first'][5]='Dnipropetrovsk Oblast'
	reindexation['first'][6]='Donetsk Oblast'
	reindexation['first'][7]='Ivano-Frankivsk Oblast'
	reindexation['first'][8]='Kharkiv Oblast'
	reindexation['first'][9]='Kherson Oblast'
	reindexation['first'][10]='Khmelnytskyi Oblast'
	reindexation['first'][11]='Kiev Oblast'
	reindexation['first'][12]='Kirovohrad Oblast'
	reindexation['first'][13]='Luhansk Oblast'
	reindexation['first'][14]='Lviv Oblast'
	reindexation['first'][15]='Mykolaiv Oblast'
	reindexation['first'][16]='Odessa Oblast'
	reindexation['first'][17]='Poltava Oblast'
	reindexation['first'][18]='Rivne Oblast'
	reindexation['first'][19]='Sumy Oblast'
	reindexation['first'][20]='Ternopil Oblast'
	reindexation['first'][21]='Vinnytsia Oblast'
	reindexation['first'][22]='Volyn Oblast'
	reindexation['first'][23]='Zakarpattia Oblast'
	reindexation['first'][24]='Zaporizhia Oblast'
	reindexation['first'][25]='Zhytomyr Oblast'
#------------------------------------------------------------------------------------------------------------------------------------------------------
	reindexation['second'][1]='Vinnytsia Oblast'
	reindexation['second'][2]='Volyn Oblast'
	reindexation['second'][3]='Dnipropetrovsk Oblast'
	reindexation['second'][4]='Donetsk Oblast'
	reindexation['second'][5]='Zhytomyr Oblast'
	reindexation['second'][6]='Zakarpattia Oblast'
	reindexation['second'][7]='Zaporizhia Oblast'
	reindexation['second'][8]='Ivano-Frankivsk Oblast'
	reindexation['second'][9]='Kiev Oblast'
	reindexation['second'][10]='Kirovohrad Oblast'
	reindexation['second'][11]='Luhansk Oblast'
	reindexation['second'][12]='Lviv Oblast'
	reindexation['second'][13]='Mykolaiv Oblast'
	reindexation['second'][14]='Odessa Oblast'
	reindexation['second'][15]='Poltava Oblast'
	reindexation['second'][16]='Rivne Oblast'
	reindexation['second'][17]='Sumy Oblast'
	reindexation['second'][18]='Ternopil Oblast'
	reindexation['second'][19]='Kharkiv Oblast'
	reindexation['second'][20]='Kherson Oblast'
	reindexation['second'][21]='Khmelnytskyi Oblast'
	reindexation['second'][22]='Cherkasy Oblast'
	reindexation['second'][23]='Chernivtsi Oblast'
	reindexation['second'][24]='Chernihiv Oblast'
	reindexation['second'][25]='Autonomous_Republic_of_Crimea'	
#------------------------------------------------------------------------------------------------------------------------------------------------------
	print(reindexation)
            

#reindexProvinces()
#downloadVHSData()
#show("vhi_id_16__2016_03_06_16_25_54.448514.csv")
#maxDuringYear("vhi_id_16__2016_03_06_16_25_54.448514.csv")
#minDuringYear("vhi_id_16__2016_03_06_16_25_54.448514.csv")
#extremeDroughtHigherThan("vhi_id_16__2016_03_06_16_25_54.448514.csv")
#averageDroughtHigherThan("vhi_id_16__2016_03_06_16_25_54.448514.csv")