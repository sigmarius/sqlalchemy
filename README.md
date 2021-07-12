## Особенности работы с Flask -SQLAlchemy и Jinja2

### Включает:
+ Создание таблиц users, profiles
+ Создание шаблонов Главной страницы и Регистрации пользователей
+ Реализация добавления записей в таблицы БД
+ **Операции с таблицами через Flask-SQLAlchemy:**
  + query.all, query.first, query.filter_by, query.filter, query.limit, query.order_by, query.get, db.session.query()
    .join,  db.relationship.
+ **jinja.py** - Особенности шаблонизатора Jinja2
  + Экранирование и блоки raw, for, if
  + Список на основе любого итерируемого объекта  
    {% for <выражение >%}<повторяемый фрагмент>{% endfor%}
  + Проверка условия  
    {% if <условие> %}<если условие выполняется>{% elif %}{% else %}{% endif%}
 + **jinja-filters.py** - Фильтрация
   + Фильтры sum, max, min, replace, random
   + Блок filter   
     {% filter <название фильтра>%}<фрагмент для применения>{% endfilter %}
 + **jinja-macro.py** - Macro-определения, вложенные макросы caller    
  