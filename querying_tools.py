import pg,os, pandas as pd
import rs_keys as keys

class query_to_df:
	
	def __init__(self,user_name=keys.user_name,pword=keys.pword):
		self.user_name=user_name
		self.pword=pword	
	
	def build_df(self,query):
		self.connect()
		data=self.conn.query(query)
		df=pd.DataFrame(data=data.getresult(),columns=data.listfields())
		del data
		return df
		
	def connect(self):
		self.conn=pg.connect('db_name','db_path',port_number, None,None, self.user_name,self.pword)

		
