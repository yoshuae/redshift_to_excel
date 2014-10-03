#execfile('tables_to_excel.py')
# need older version of openpyxl
# pip install openpyxl==1.8.6 
# pip install PyGreSQL

import os,pandas as pd, pg
from pandas import ExcelWriter
from querying_tools import query_to_df
os.chdir("/Users/joshua/Desktop/PROFILING_TOOL")

tables=['cbs','abc','nbc']
factors=['days_vs_total_days','duration_v_morning_duration','duration_v_monthly_duration','days_vs_days_7_9']
filters=['people_25_54','young_woman']

for clause in filters:
	for name in tables:
		query='select * from '+ name + '_ratios' + ' where ' + clause + '>0' 
		df=query_to_df().build_df(query)
		del data
		file_name=name+'_'+clause+'.xlsx'
		temp=pd.ExcelWriter(file_name)
		for demo in factors:
			table=pd.pivot_table(df,values='house_id',columns=demo,index=['morning_show_days','hml'],aggfunc=len)
			table.to_excel(temp,sheet_name=demo,na_rep='0')
		table=pd.pivot_table(df,values='house_id',columns='hml',index=['morning_show_days'],aggfunc=len)
		table.to_excel(temp,sheet_name='hml_v_days_watched',na_rep='0')
		temp.save()
		del temp,table,df