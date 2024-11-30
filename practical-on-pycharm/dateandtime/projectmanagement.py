from datetime import *

class Project:
    def __init__(self,name, startDate, endDate):
        self.name=name
        self.startDate=startDate
        self.endDate=endDate
        self.tasks=[]

    def addTask(self,task):
        self.tasks.append(task)


class Task:
    def __init__(self,name, duration):
        self.name=name
        self.duration=duration
        self.resources=[]

    def addResources(self,resource):
        self.resources.append(resource)


class Resource:
    def __init__(self,name,skill):
        self.name=name
        self.skill=skill

project = Project("AI",date(2014,11,6), date(2030,11, 3))
task = Task('Create Bot',90)
resource = Resource("John","Python")

task.addResources(resource)
project.addTask(task)

for eachtask in project.tasks:
    print(eachtask.name)
    for eachResource in eachtask.resources:
        print(eachResource.name)
        print(eachResource.skill)
