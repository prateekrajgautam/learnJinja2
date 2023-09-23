# import Jinja2
from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment with a template directory
env = Environment(loader=FileSystemLoader('templates'))

# Load the template
template = env.get_template('example.html')

# Define the data for the loop
context = {'items': ['Apple', 'Banana', 'Cherry', 'Date']}

# Render the template with the context
output = template.render(context)

# Output the result
print(output)