from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {'name': 'Alex', 'age': 33, 'weight': 80.5},
    {'name': 'Jack', 'age': 23, 'weight': 60.5},
    {'name': 'Ivan', 'age': 37, 'weight': 100.0}
]

def loadTpl(path):
    if path == "environment.html":
        return ''' Name {{ u.name }}, Age {{ u.age }} '''
    else:
        return ''' Data: {{ u }}'''

file_loader = FileSystemLoader('templates')
function_loader = FunctionLoader(loadTpl)

env = Environment(loader=file_loader)
env2 = Environment(loader=function_loader)

# формирует экземпляр класса Template
tm = env.get_template('environment.html')
tm2 = env2.get_template('environment.html')

msg = tm.render(users=persons)
msg2 = tm2.render(u=persons[0])

print(msg2)
