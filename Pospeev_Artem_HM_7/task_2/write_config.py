import yaml
'''Словарь, в котором ключи- ВСЕГДА названия директорий, а значения- либо строки с названием файлов, 
либо словари с такой же структурой.'''

structure = {'my_project': [{'settings': [
    '__init__.py', 'dev.py', 'prod.py'], },
    {'mainapp': [
        '__init__.py', 'models.py', 'views.py', {'templates': [{
            'mainapp': ['base.html', 'index.html']}]
        }]},
    {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
        'authapp': ['base.html', 'index.html']}]
    }
                 ]
     }
]
}

with open('config.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(structure, f, default_flow_style=False)
