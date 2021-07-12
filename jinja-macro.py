from jinja2 import Template

html = '''
{% macro input(name, value="", type="text", size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input("username") }}</p>
<p>{{ input('email', type="email") }}</p>
<p>{{ input('password') }}</p>
'''

tm = Template(html)
msg = tm.render()

print(msg)

# Вложенные макросы => call
persons = [
    {'name': 'Alex', 'age': 33, 'weight': 80.5},
    {'name': 'Jack', 'age': 23, 'weight': 60.5},
    {'name': 'Ivan', 'age': 37, 'weight': 100.0}
]

html2 = '''
{% macro list_users(list_of_user) -%}
<ul>
    {%- for u in list_of_user %}
        <li>{{ u.name }} {{ caller(u) }}</li>
    {%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
            <ul>
                <li>age: {{ user.old }}</li>
                <li>weight: {{ user.weight }}</li>
            </ul>
{% endcall -%}
'''

tm2 = Template(html2)
msg2 = tm2.render(users=persons)
print(msg2)