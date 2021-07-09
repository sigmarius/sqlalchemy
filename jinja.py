from jinja2 import Template, escape
# {{ }} => выражение для вставки любых конструкций Python в шаблон => pure Python f"Hello {name}" - только переменные
# {% %} => спецификатор шаблона
# {# #} => блок комментариев
# ## => строковый комментарий
# {% raw %}{% endraw %} => все что помещается в эти блоки никак не будет преобразовано
# {% for %}{% endfor%} => список на основе любого итерируемого объекта
# {% if %}{% endif%} => проверка условия

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

per = Person('Alex', 33)
tm = Template('Мне {{ p.getAge()*2 }} лет и зовут {{ p.getName().upper() }}')
msg = tm.render(p=per)


seg = {'name': 'Max', 'age': 37}
tm2 = Template('Мне {{ s.age*2 }} лет и зовут {{ s.name.upper() }}')
# or =>
tm3 = Template('Мне {{ s["age"]*2 }} лет и зовут {{ s["name"].upper() }}')

msg2 = tm2.render(s=seg)
msg3 = tm3.render(s=seg)

print(msg, msg2, msg3, sep='\n', end='\n\n')

# Экранирование
data = '''{% raw %}Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение{% endraw %} '''
tm4 = Template(data + '\n\n')
msg4 = tm4.render(name='Ivan')

# e - escape экранирование HTML тегов
link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a> '''
msg5 = escape(link)

print(msg4, msg5, sep='\n\n')

# {% for %}{% endfor%}
cities = [{'id': 1, 'city': 'Moscow'},
          {'id': 5, 'city': 'Tokio'},
          {'id': 7, 'city': 'SPB'},
          {'id': 8, 'city': 'Paris'},
          {'id': 11, 'city': 'London'}]

# {% -%} "-" убирает пустые строчки
cicle = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
  <option value="{{ c['id'] }}">{{ c['city']}}</option>
{% elif c.city == 'Moscow' -%}
    <p>{{ c['city']}}</p>
{% else -%}
    {{ c['city'] }}
{% endif -%}
{% endfor -%}
</select>'''

tm6 = Template(cicle)
msg6 = tm6.render(cities=cities)
print(msg6)
