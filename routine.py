from jira import JIRA
import cgi
import re
import urllib3
import requests
import sys

class routine:
    def __init__(self, jira_user, jira_password):
        requests.packages.urllib3.disable_warnings()
        self.jira_user = jira_user
            self.jira_password = jira_password
                self.jira_server = 'https://carousell.atlassian.net'
                    self.cs_board = 53
                        self.jira_authentication()



def jira_authentication(self):
    options = {
        'server': self.jira_server,
            'verify': False
                }
                    jira = JIRA(options, basic_auth=(self.jira_user, self.jira_password))
                    self.jira=jira
                        print "authentication success"

def  get_cs_current_sprint(self):
    r=self.jira._session.get(self.jira_server+'/rest/agile/1.0/board/'+str(self.cs_board)
                             +'/sprint?state=active')
                             self.current_sprint_id=r.json().get('values')[0].get('id')
                                 return self.current_sprint_id,str(self.get_sprint_name(self.current_sprint_id))

def  get_cs_future_sprint(self):
    r=self.jira._session.get(self.jira_server+'/rest/agile/1.0/board/'+str(self.cs_board)
                             +'/sprint?state=future')
                             self.future_sprint_id=r.json().get('values')[0].get('id')
                                 return self.future_sprint_id,str(self.get_sprint_name(self.future_sprint_id))

def get_sprints(self):
    sprint_info=self.jira.sprints(self.cs_board)
    return sprint_info
    
    def get_sprint_name(self,sprintid):
        sprints = {}
            for s in self.jira.sprints(self.cs_board):
                if s.id == sprintid:
                    return s.name

def create_bug(self, project_key ,assignee, summary, description):
    bugs = []
    for i in range (0, len(description)) :
        bug= {
            'project': {'key': project_key},
                'summary': summary[i],
                'description': description[i],
                'issuetype': { 'name' : 'Bug' },
                    'assignee' : { 'name' : assignee[i] }
                    }
                    bugs.append(bug)
                        issues = self.jira.create_issues(field_list=bugs)
                        print "successfully create cs bugs"
                            return [ issue.get('issue').key for issue in issues]

def create_story(self, assignee, summary, description):
    storys = []
    for i in range (0, len(description)) :
        story= {
            'project': {'key': 'CS'},
                'summary': summary[i],
                'description': description[i],
                'issuetype': { 'name' : 'Story' },
                    'assignee' : { 'name' : assignee[i] }
                    }
                    storys.append(story)
                        issues = self.jira.create_issues(field_list=storys)
                        print "successfully create Story"
                            return [ issue.get('issue').key for issue in issues]

def add_issues_to_sprint(self, sprint_id ,list_tickets=[]):
    list_issue_id=[]
    for issue in list_tickets:
        jiraissue = self.jira.issue(issue)
        list_issue_id.append(jiraissue.id)
    self.jira.add_issues_to_sprint( sprint_id, list_issue_id)
    print  "successfully add to current sprint %s" % (self.get_sprint_name(sprint_id))

def  add_attachment(self, ticket , filepath):
    jiraissue = self.jira.issue(ticket)
    self.jira.add_attachment(issue=jiraissue, attachment=filepath)
    print "successfully upload file attachment"


if __name__ == "__main__":
    routine1=routine('<user_name>','<password>')
    # out=routine1.create_story(['daisy.liu','daisy.liu'],['bug','bug'],['des','des'])
    # out=routine1.create_bug('CS',['daisy.liu'],['bug'],['des'])
    # out2=routine1.get_cs_future_sprint()
    # print "https://unix.stackexchange.com/questions/284476/terminal-create-hyperlinks"
        print out

