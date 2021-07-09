from jinja2 import Template

# sum(iterable, attribute=None, start=0) => вычисление суммы поля коллекции

cars = [
    {'model': 'Audi', 'price': 500},
    {'model': 'BMV', 'price': 700},
    {'model': 'Volvo', 'price': 80},
    {'model': 'Hyundai', 'price': 30},
]

tpl = 'Суммарная цена автомобилей: {{ cs | sum(attribute="price") }}'
tpl2 = 'Автомобиль с максимальной стоимостью: {{ cs | max(attribute="price") }}'
tpl3 = 'Автомобиль с максимальной стоимостью (только модель): {{ (cs | max(attribute="price")).model }}'
tpl4 = 'Автомобиль с минимальной стоимостью: {{ cs | min(attribute="price") }}'
tpl5 = 'Автомобиль случайно выбранный из листа: {{ cs | random }}'
tpl6 = 'Замена маленьких букв о на заглавные О: {{ cs | replace("o", "O") }}'

tm = Template(tpl6)
msg = tm.render(cs=cars)

print(msg)

# блок filter => upper, lower
persons = [
    {'name': 'Alex', 'age': 33, 'weight': 80.5},
    {'name': 'Jack', 'age': 23, 'weight': 60.5},
    {'name': 'Ivan', 'age': 37, 'weight': 100.0}
]

tpl7 = '''
{%- for u in users -%}
    {% filter upper %}{{ u.name }}{% endfilter %}
{% endfor -%}
'''
tm2 = Template(tpl7)
msg2 = tm2.render(users=persons)
print(msg2)