import json
import os

class DataManager:
    def __init__(self, file='data.json'):
        self.file = file
        self.data = self.load()
    
    def load(self):
        # Check if file exists and is not empty
        if os.path.exists(self.file) and os.path.getsize(self.file) > 0:
            try:
                with open(self.file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                # If file is corrupted, start fresh
                print("Data file corrupted. Creating new data...")
                return {'users': {}, 'projects': {}, 'tasks': {}}
        else:
        
            return {'users': {}, 'projects': {}, 'tasks': {}}
    
    def save(self):
        with open(self.file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def add_user(self, user):
        self.data['users'][user.id] = user.to_dict()
        self.save()
    
    def get_user(self, name):
        for u in self.data['users'].values():
            if u['name'].lower() == name.lower():
                return u
        return None
    
    def get_all_users(self):
        return list(self.data['users'].values())
    
    def add_project(self, project):
        self.data['projects'][project.id] = project.to_dict()
        self.data['users'][project.user_id]['projects'].append(project.id)
        self.save()
    
    def get_user_projects(self, user_id):
        return [p for p in self.data['projects'].values() if p['user_id'] == user_id]
    
    def add_task(self, task):
        self.data['tasks'][task.id] = task.to_dict()
        self.data['projects'][task.project_id]['tasks'].append(task.id)
        self.save()
    
    def get_project_tasks(self, project_id):
        return [t for t in self.data['tasks'].values() if t['project_id'] == project_id]
    
    def complete_task(self, task_id):
        if task_id in self.data['tasks']:
            self.data['tasks'][task_id]['completed'] = True
            self.save()
            return True
        return False