from sqlalchemy import create_engine,Column,Integer,String,Integer
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:chis1chang@127.0.0.1:3306/s1209?charset=utf8')

Base = declarative_base()
#sqlalchemy本身无法对已经建立的表进行修改，只存在新建，删除
#数据表类
class User(Base):
	__tablename__='users'
	id = Column(Integer,primary_key=True)
	username =Column(String(64),)
	pwd=Column(String(64),)

#新建数据表，如果当前表已经建立，则不会产生效果，
def create_all():
	engine = create_engine('mysql+pymysql://root:chis1chang@127.0.0.1:3306/s1209?charset=utf8')
	Base.metadata.create_all(engine)
def drop_all():
	engine = create_engine('mysql+pymysql://root:chis1chang@127.0.0.1:3306/s1209?charset=utf8')
	Base.metadata.drop_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

#add
#obj1 = User(name='asd',pwd='kkk')
#obgj2=User(name='fgh',pwd='lll')
#session.add(obj1)
#session.add_all(obj1,obj2)
#session.commit()


#select
#a = session.query(User).all()
#for i in a:
#	print(i.pwd,i[2])

#a = session.query(User).first()

#使用条件
#a = session.query(User).filter(User.id>1).all()
#a = session.query(User).filter(User.id==1).all()
#filter_by 使用的不是表达式，而是参数，实现原理还是你不转换为filter，返回为and表达式
#a = session.query(User).filter_by(User.id=1).all()

#查询命名,
#a = session.query(User.name.label('cname'),User.pwd).filter(User.id>1).all()
#for i in a:
#	print(i.pwd,i[2],i.cname)
#之间
#a = session.query(User).filter(User.id.between(1,5)).all()
#in
#a = session.query(User).filter(User.id.in_({1,3,5})).all()
#not in
#a = session.query(User).filter(~User.id.in_({1,3,5})).all()
#子查询
#a = session.query(User).filter(id.in_(session.query(id).filter(name='asd'))).all()

#and,or
from sqlalchemy import and_,or_
#a = session.query(User).filter(and_(User.id>3,id.in_({1,3,5}))).all()
#a = session.query(User).filter(or_(User.id>3,id.in_({1,3,5}))).all()

#a = session.query(User).filter(or_(User.id>3,and_(id_in({2,3},id!=0))))).all()

#通配符,e字母开头的
#a = session.query(User).filter(User.username.like('e%')).all()
#e之后只有一个字符
#a = session.query(User).filter(User.username.like('e_')).all()
#a = session.query(User).filter(~User.username.like('e%')).all()

#切片
#a = session.query(User)[1:2]

#排序
#a = session.query(User).filter(User.username.like('e%')).order_by(name.desc())all()
#a = session.query(User).filter(User.username.like('e%')).order_by(name.desc(),id.asc())all()

#分组,假设此表有一个depart_id的部门属性
from sqlalchemy import func
#a = session.query(func.max(User.id)).group_by('User.depart_id').all()

#a = session.query(func.max(User.id),func.count(User.id)
	).group_by('User.depart_id').having(func.count(User.id)>=2).all()

#连表，union,如果两张表列数一样，则将后表拼接到前表后（自动去重），union_all（不自动去重）,
a = session.query(User.id).filter(name.in_({'aa','bbb'})
	).union(
	session.query(User.id).filter(name.in_({'cc','ddb'}))
	)



#update
a = session.query(User).filter(User.id==4).update({User.username:'sdf'})
#a = session.query(User).filter(User.id==4).update({username:'sdf'})
a = session.query(User).filter(User.id==4).update({username:User.username+'sdf'},synchronize_session=False)#在字符原值基础修改修改对设置单独属性， 如果是数字，需要修改为synchronize_session='evaluate'
session.commit()
#delete
#session.query(User).filter(User.id>1).delete()
#session.commit()




