# from jira_routine_job import  *
import logging
import os
import photo_merge

class bug_parser:
		def __init__(self, file_path):
			self.bug_des=[]
			self.bug_summary=[]
			self.bug_assignee=[]
			self.bug_photos=[]  #[[A,B,C],[D,E,F]]
			self.flag=-1
			self.des=""
			self.summary=""
			self.assignee="" 
			self.photos=[]
			self.parse_file(file_path)

			print  self.bug_des
			print  self.bug_summary
			print  self.bug_assignee
			print  self.bug_photos

 
		def  check_bug_key(self, line):
			if self.flag == 1:
				line=line+"\n"
				self.des+=line
			elif self.flag== 2 :
				line+="\n"
				self.summary+=line
			elif self.flag== 3 :
				self.assignee+=line
			elif self.flag== 4 and line:
				photo_list=[x for x in line.strip().split(',')]
				self.photos+=photo_list


		def  check_content_exist(self):		
			if  self.des != "":
				self.bug_des.append(self.des)
				self.des = ""
			if self.summary != "":
				self.bug_summary.append(self.summary)
				self.summary = ""
			if self.assignee != "":
				self.bug_assignee.append(self.assignee)
				self.assignee=""
			if  self.photos :
				self.bug_photos.append(self.photos)
				self.photos=[]

		def parse_file(self,file_path):
			with open(file_path) as  f:
				for  line  in iter(f):
					line =line.rstrip()
					if line.startswith('@des') or line.startswith('@summary') or line.startswith('@assignee') \
					or line.startswith('!exit') or line.startswith('@photos'):
						if line.startswith('@des'):
							self.check_content_exist()
							self.flag=1
						elif line.startswith('@summary'):
							self.check_content_exist()
							self.flag=2
						elif line.startswith('@assignee'):
							self.check_content_exist()
							self.flag=3
						elif line.startswith('@photos'):
							self.check_content_exist()
							self.flag=4
						else :
							self.check_content_exist()
					else:
						self.check_bug_key(line)

			if len(self.bug_des) != len(self.bug_assignee) or  len(self.bug_des)==0  or len(self.bug_assignee)==0:
				raise  "bug description size is not match with bug assignee size"
				# raise "test_step size %d and test data result %d len not matches" % ( len(test_step), len(test_result))

if __name__ == "__main__":

		# file_path=os.path.join(
        # os.path.dirname(os.path.abspath(__file__)), 'uploads', 'bug.txt')
		parser1=bug_parser('bug.txt')
		



