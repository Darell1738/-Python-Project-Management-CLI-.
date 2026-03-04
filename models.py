import json
import uuid

class User:
    def __init__(self, name, id=None):
        self.id = id or str(uuid.uuid4())[:4]
        self.name = name
        self.projects = []
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'projects': self.projects}

class Project:
    def __init__(self, title, user_id, id=None):
        self.id = id or str(uuid.uuid4())[:4]
        self.title = title
        self.user_id = user_id
        self.tasks = []
    
    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'user_id': self.user_id, 'tasks': self.tasks}

class Task:
    def __init__(self, title, project_id, id=None):
        self.id = id or str(uuid.uuid4())[:4]
        self.title = title
        self.project_id = project_id
        self.completed = False
    
    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'project_id': self.project_id, 'completed': self.completed}