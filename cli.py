import argparse
from models import User, Project, Task
from data_manager import DataManager

dm = DataManager()

def main():
    parser = argparse.ArgumentParser(description='Project Management CLI')
    subparsers = parser.add_subparsers(dest='command')
    
    subparsers.add_parser('users', help='List all users')
    add_user = subparsers.add_parser('add-user', help='Add user')
    add_user.add_argument('--name', required=True)
    
    add_project = subparsers.add_parser('add-project', help='Add project')
    add_project.add_argument('--user', required=True)
    add_project.add_argument('--title', required=True)
    
    list_projects = subparsers.add_parser('projects', help='List user projects')
    list_projects.add_argument('--user', required=True)
    

    add_task = subparsers.add_parser('add-task', help='Add task')
    add_task.add_argument('--project', required=True)
    add_task.add_argument('--title', required=True)
    
    list_tasks = subparsers.add_parser('tasks', help='List project tasks')
    list_tasks.add_argument('--project', required=True)
    
    complete = subparsers.add_parser('complete', help='Complete task')
    complete.add_argument('--task-id', required=True)
    
    subparsers.add_parser('menu', help='Interactive menu')
    
    args = parser.parse_args()
    
    if args.command == 'users':
        users = dm.get_all_users()
        print("\n=== USERS ===")
        for u in users:
            print(f"ID: {u['id']} | {u['name']} | Projects: {len(u['projects'])}")
    
    elif args.command == 'add-user':
        dm.add_user(User(args.name))
        print(f"✓ User '{args.name}' added")
    
    elif args.command == 'add-project':
        user = dm.get_user(args.user)
        if user:
            dm.add_project(Project(args.title, user['id']))
            print(f"✓ Project '{args.title}' added for {args.user}")
        else:
            print(f"✗ User '{args.user}' not found")
    
    elif args.command == 'projects':
        user = dm.get_user(args.user)
        if user:
            projects = dm.get_user_projects(user['id'])
            print(f"\n=== {args.user}'s PROJECTS ===")
            for p in projects:
                print(f"ID: {p['id']} | {p['title']} | Tasks: {len(p['tasks'])}")
        else:
            print(f"✗ User '{args.user}' not found")
    
    elif args.command == 'add-task':
    
        project = None
        for p in dm.data['projects'].values():
            if p['title'].lower() == args.project.lower():
                project = p
                break
        
        if project:
            dm.add_task(Task(args.title, project['id']))
            print(f"✓ Task '{args.title}' added to {args.project}")
        else:
            print(f"✗ Project '{args.project}' not found")
    
    elif args.command == 'tasks':
        project = None
        for p in dm.data['projects'].values():
            if p['title'].lower() == args.project.lower():
                project = p
                break
        
        if project:
            tasks = dm.get_project_tasks(project['id'])
            print(f"\n=== {args.project} TASKS ===")
            for t in tasks:
                status = "✓" if t['completed'] else "○"
                print(f"{status} ID: {t['id']} | {t['title']}")
        else:
            print(f"✗ Project '{args.project}' not found")
    
    elif args.command == 'complete':
        if dm.complete_task(args.task_id):
            print(f"✓ Task {args.task_id} completed")
        else:
            print(f"✗ Task {args.task_id} not found")
    
    elif args.command == 'menu':
        while True:
            print("\n=== MENU ===")
            print("1. List users")
            print("2. Add user")
            print("3. Add project")
            print("4. List user projects")
            print("5. Add task")
            print("6. List project tasks")
            print("7. Complete task")
            print("8. Exit")
            
            choice = input("Choice (1-8): ")
            
            if choice == '1':
                for u in dm.get_all_users():
                    print(f"{u['id']}: {u['name']}")
            elif choice == '2':
                dm.add_user(User(input("Name: ")))
                print("User added")
            elif choice == '3':
                user = dm.get_user(input("User name: "))
                if user:
                    dm.add_project(Project(input("Project title: "), user['id']))
                    print("Project added")
                else:
                    print("User not found")
            elif choice == '4':
                user = dm.get_user(input("User name: "))
                if user:
                    for p in dm.get_user_projects(user['id']):
                        print(f"{p['id']}: {p['title']} ({len(p['tasks'])} tasks)")
                else:
                    print("User not found")
            elif choice == '5':
                title = input("Task title: ")
                project_title = input("Project title: ")
                project = None
                for p in dm.data['projects'].values():
                    if p['title'].lower() == project_title.lower():
                        project = p
                        break
                if project:
                    dm.add_task(Task(title, project['id']))
                    print("Task added")
                else:
                    print("Project not found")
            elif choice == '6':
                project_title = input("Project title: ")
                project = None
                for p in dm.data['projects'].values():
                    if p['title'].lower() == project_title.lower():
                        project = p
                        break
                if project:
                    for t in dm.get_project_tasks(project['id']):
                        status = "✓" if t['completed'] else "○"
                        print(f"{status} {t['id']}: {t['title']}")
                else:
                    print("Project not found")
            elif choice == '7':
                if dm.complete_task(input("Task ID: ")):
                    print("Task completed")
                else:
                    print("Task not found")
            elif choice == '8':
                break
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()