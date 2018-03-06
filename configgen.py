"""
Generates a configuration file using jinja2 templates
"""

from jinja2 import Environment, FileSystemLoader
import yaml

def template_loader(yml_file, template_file, conf_file):
    """
    This function generates a configuration file using jinja2 templates.

    yml_file = Location of the file containing variables to use with the jinja2 template
    template_file = Location of jinja2 template file
    conf_file = Location to place generated config file.
    """

    env = Environment(loader=FileSystemLoader('./'))

    # Load variables from yml_file
    with open(yml_file) as yfile:
        yml_var = yaml.load(yfile)

    template = env.get_template(template_file)

    # Render template
    out_text = template.render(config=yml_var)

    # Write results of out_text to file
    file = open(conf_file, 'w')
    file.write(out_text)
    file.close()
