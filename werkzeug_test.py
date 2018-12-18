from werkzeug.wrappers import Response
from werkzeug.serving import run_simple

def run_server(environ,start_response):
	response = Response('hello')
	return response(environ,start_response)
	
if __name__ == "__main__":
	run_simple('127.0.0.1',8000,run_server)
	