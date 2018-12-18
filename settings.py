class Base(object):
	SECRET_KEY = "qwertyuiop"
	 
class ProductionConfig(Base):
	DEBUG = True
	

class DevelopmentConfig(Base):
	DEBUG = False