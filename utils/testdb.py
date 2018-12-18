import sqlite3
	
def dict_factory(cursor, row):  
    d = {}  
    for idx, col in enumerate(cursor.description):  
        d[col[0]] = row[idx]  
    return d 
if __name__=="__main__":
	#conn = sqlite3.connect("BaiduYunCacheFileV0.db")
	conn = sqlite3.connect(".././static/bdy/BaiduYunCacheFileV0.db")
	conn.row_factory = dict_factory  
	cursor = conn.cursor()
	sql = """select name from sqlite_master where type='table' order by name"""
	
	"""
	
	[('cache_file',), ('version',)]
<class 'list'>
	
	"""
	sql = """pragma table_info(cache_file)"""
	sql = "select *  from cache_file where server_filename = %s"%('aj025_01.wmv',)
	
	#sql = """select parent_path,server_filename  from cache_file where server_filename like %s or parent_path like %s """%('高','高')
	#sql ="select id from cache_file where parent_path like ? or server_filename like ? ;"
	#cursor.execute(sql,('%高%','%高%'))
	delete_suoyin = "DROP INDEX IF EXISTS idxserverpath"
	cursor.execute(delete_suoyin)
	conn.commit()
	select_key = 'pdf'
	select_key = '%'+select_key+'%'
	#sql = "select parent_path,server_filename from cache_file where server_filename like '%高%'"
	sql ="""select   parent_path,server_filename from cache_file where parent_path like ? or server_filename like ?;"""
	cursor.execute(sql,(select_key,select_key))
	
	#cursor.execute(sql)
	
	
	cnt = 0
	result = cursor.fetchall()
	print(result)
	with open('kkk.txt','w',encoding='utf8') as f :
		for i in result:
			f.write('%'+str(cnt)+i['parent_path']+i['server_filename']+'\n')
			cnt +=1
	print(result)
	print(type(result),cnt)

    