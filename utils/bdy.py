import sqlite3
	
def dict_factory(cursor, row):  
    d = {}  
    for idx, col in enumerate(cursor.description):  
        d[col[0]] = row[idx]  
    return d 
def a(select_key = ''):
	di = {}
	conn = sqlite3.connect("./static/bdy/BaiduYunCacheFileV0.db")
	conn.row_factory = dict_factory  
	cursor = conn.cursor()

	delete_suoyin = "DROP INDEX IF EXISTS idxserverpath"
	cursor.execute(delete_suoyin)
	conn.commit()
	if not select_key:
		di['nan']='nothin to found'
		return di
	select_key = '%'+select_key+'%'
	sql ="""select parent_path,server_filename from cache_file where parent_path like ? or server_filename like ?;"""
	cursor.execute(sql,(select_key,select_key))
	
	cnt = 0
	result = cursor.fetchall()
	#print(result)
	
	for i in result:
		di[cnt]=i['parent_path']+i['server_filename']
		cnt +=1
	return di
	#print(result)
	#print(type(result),cnt)
	
#a('你好')