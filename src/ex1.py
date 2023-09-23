# import Jinja2
from jinja2 import Environment



template_str = "Hello, {{ name }}!"
template_str2 = "Hello, {{ name | upper }}!"
context = {'name': 'John'}

env = Environment()
template = env.from_string(template_str)
template2 = env.from_string(template_str2)
output = template.render(context)
print(output)
output2 = template2.render(context)
print(output2)


looptemplate = """
{{ for }}
"""