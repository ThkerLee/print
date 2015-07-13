
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
		("listpic","yuezhong","yuezhong.jpg")
		,("listpic","yuezhong","yuezhong.jpg")
		
		
		]
		self.render("index.html",list=printlist)
class test(tornado.web.RequestHandler):
	def get(self):
		danjumingchen='yuezhong.html'
		yuezhongbox=[['客户号码','3.1','1.5'],['始发地','3.1','4.5']]
		
		danjumingchen=danjumingchen[:-5]
		if danjumingchen=='yuezhong':
			sboxlist=yuezhongbox
		self.render("test.html",boxlist=sboxlist)
class print_demo_frame(tornado.web.RequestHandler):
	def get(self,danjumingchen):
		self.render("print_demo_frame.html,,mingchen=danjumingchen")

class print_demo(tornado.web.RequestHandler):

	def get(self,danjumingchen):
		
		print_mingchen=list(danjumingchen);
		print_mingchen=print_mingchen[:-5];
		print_mingchen=('').join(list(print_mingchen));
		self.render("print_demo.html",mingchen=print_mingchen)
	def post(self,danjumingchen):
		yuezhong=(
			{'发件方':('客户号码','始发地','公司名称','地址','寄件人签名','电话','委托货物内容','备注')}
			,{'收件方':('目的地','日期','公司名称','地址','收件人','电话','体积重量')}
			,{'其他':('非货样','现付','货样','月结','速递','到付','空运','件数','重量')}
			,{'打勾':('非货样','现付','货样','月结','速递','到付','空运')}
			,{'relation':{'客户号码':'月结'}}
		)
		yuezhongbox=[['客户号码','3.1','1.5'],['始发地','3.1','4.5']]
		
		danjumingchen=danjumingchen[:-5]
		if danjumingchen=='yuezhong':
			xiangmu1=yuezhong
			sboxlist=yuezhongbox
		
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
			qita=dict()	
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
					elif head[i]=="其他":
						dic=qita
					elif key !="":
						dic[head[i]]=key
					i=i+1
				i=0
				tmp['发件方']=fajian.copy()
				tmp['收件方']=shoujian.copy()
				tmp['其他']=qita.copy()
				sourcedata.append(tmp.copy())
				tmp.clear()			

		self.render("print_printdetal.html",printdata=sourcedata,boxlist=sboxlist,mingchen=danjumingchen,xiangmu=xiangmu1)
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
 		(r"/detail/(.*)",print_demo),
 		(r"/test",test),
	
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
