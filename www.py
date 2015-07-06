
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
		("listpic","detail","shunfeng.jpg")
		,("listpic","detail","shunfeng.jpg")
		
		
		]
		self.render("index.html",list=printlist)

class print_demo_frame(tornado.web.RequestHandler):
	def get(self):
		self.render("print_demo_frame.html")

class print_demo(tornado.web.RequestHandler):

	def get(self,danjumingchen):
		
		print_mingchen=list(danjumingchen);
		print_mingchen=print_mingchen[:-5];
		print_mingchen=('').join(list(print_mingchen));
		self.render("print_demo.html",mingchen=print_mingchen)
	def post(self,danjumingchen):
		
		now=datetime.now()
		now=now.strftime("%Y%m%d%H%M%S")
		upload_path=os.path.join(os.path.dirname(__file__),"files")

		file_metas=self.request.files['printcvsfile']
		for meta in file_metas:
			filename=meta['filename']
			filename=now +'.'+filename 
			#/////////////////			
			#save as a file
			filepath=os.path.join(upload_path,filename)
			with open(filepath,'w') as up:
	
				up.write(meta['body'])
			#/////////
			datafile=open(filepath,'r')
			reader=csv.reader(datafile)	
			# line=('').join(list(head))
			# self.write(line)
			head=list(reader.next())
			reader=list(reader)
			i=0
			x=0
			y=0
			sourcedata=list()
			shoujian=dict()
			fajian=dict()
			dic=dict()
			tmp=dict()
			for line in reader:
				for key in line:

					if head[i]=="发件方":
						dic=fajian
						x=0
					elif head[i]=="收件方":
						dic=shoujian
						y=0
					
					elif key !="":
						dic[head[i]]=key
					i=i+1
				i=0
				tmp['发件方']=fajian
				tmp['收件方']=shoujian
			sourcedata.append(tmp)

			# for line in reader:
			# 	if head[0]="发件方":
			# 		for value in line:
			# 			tmpdate.append(head[i])
			# 			tmpdate.append(value)
			# 			i=i+1
			# 		i=0
			# 		sourcedata.append(tmpdate)
			# 		tmpdate=list()
			# for line in reader:
			# 	sourcedata.append(line)
			 	# detaildic=dict((top,value)for top,value in nextline)
				
			self.render("print_printdetal.html",printdata=sourcedata,top=head,mingchen=danjumingchen)
			# for line in reader:
			# 	line=('').join(list(line))
			# 	self.write(line)
			#  	self.write('</br>')

		

class upload(tornado.web.RequestHandler):
	pass


def main():
	app=tornado.web.Application(
		[
		(r"/",mainhandler),
		(r"/detail.html",print_demo_frame),
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
