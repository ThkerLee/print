
#coding=utf-8
import csv
import tornado.ioloop
import tornado.web
import os.path
from tornado.options import define,options
from datetime import datetime
define("port",default=8888,help="run on the given port",type=int)
define("debug",default=True,help="run in debug mode")

class mainhandler(tornado.web.RequestHandler):

	def get(self):
		printlist=[
		("shunfeng","shunfeng","shunfeng.jpg")
		,("shunfeng","print_demo","shunfeng.jpg")
		,("shunfeng","print_demo","shunfeng.jpg")
		,("shunfeng","print_demo","shunfeng.jpg")
		,("shunfeng","print_demo","shunfeng.jpg")
		,("shunfeng","print_demo","shunfeng.jpg")
		,("shunfeng","print_demo","shunfeng.jpg")
		,("shunfeng","print_demo","shunfeng.jpg")
		,("shunfeng","print_demo","shunfeng.jpg")
		
		]
		self.render("index.html",list=printlist)
class print_demo(tornado.web.RequestHandler):
	


	def get(self,danjumingchen):
		
		print_mingchen=list(danjumingchen);
		print_mingchen=print_mingchen[:-5];
		print_mingchen=('').join(list(print_mingchen));
		self.render("print_demo.html",mingchen=print_mingchen)
	def post(self):
		
		now=datetime.now()
		now=now.strftime("%Y%m%d%H%M%S")
		upload_path=os.path.join(os.path.dirname(__file__),"files")

		file_metas=self.request.files['printcvsfile']
		for meta in file_metas:
			filename=meta['filename']
			filename=filename + now
			#/////////////////
			content=meta['body']
			# save as a file
			# filepath=os.path.join(upload_path,filename)
			# with open(filepath,'w') as up:
			# 	up.write(meta['body'])
			#/////////
			reader=csv.reader(content)

			for line in reader:
				for word in line:					
					self.write(word)
				self.write('</br>')
		

class upload(tornado.web.RequestHandler):
	pass


def main():
	app=tornado.web.Application(
		[
		(r"/",mainhandler),
		(r"/list/upload",print_demo),
	 	(r"/list/(.*)",print_demo),
		
		# (r"/templates/left-nav.html",left_nav),
		# (r"/templates/right-nav.html",right_nav),
		# (r"/templates/top-nav.html",top_nav),
		# (r"/templates/right-content.html",right_content),
		# (r"/templates/right-mini-nav.html",right_mini_nav),
		],

		template_path=os.path.join(os.path.dirname(__file__),"templates"),
		static_path=os.path.join(os.path.dirname(__file__),"static"),
		debug=options.debug,

		)
	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
if __name__ =="__main__":
	main()
