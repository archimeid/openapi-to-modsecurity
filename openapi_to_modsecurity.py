import argparse
from yaml import load, dump
from yaml.cyaml import CLoader
import json
import pprint
from jinja2 import Environment, PackageLoader, select_autoescape

parser = argparse.ArgumentParser(description='Convert an OpenAPI file to ModSecurity rules.')
parser.add_argument('openapi_file', type=str, help='Path to OpenAPI file')
parser.add_argument('modsecurity_file', type=str, help='Path to ModSecurity rules file')

args = parser.parse_args()
openapi_filename = args.openapi_file.split('/')[-1]

if '.' not in openapi_filename:
    raise NameError

ext = openapi_filename.split('.')[-1]

try:
    if ext in ['yml', 'yaml']:
        print('Loading a YAML file - ', openapi_filename)
        file = open(args.openapi_file, 'r')
        file_content = file.read()
        openapi = load(file_content, Loader=CLoader)
        
    if ext in ['json']:
        print('Loading a JSON file - ', openapi_filename)
        file = open(args.openapi_file, 'r')
        openapi = json.load(file)
except FileNotFoundError:
    print('This file does not exist: ', args.openapi_file)
    exit(1)

if 'openapi' not in openapi:
    raise ValueError('The file does not seem to be an OpenAPI specification')

pprint.pprint(openapi)

base_path = ''
if 'servers' in openapi and len(openapi['servers']):
    base_path = '/' + '/'.join(openapi['servers'][0]['url'].split('/')[3:])
print('The base path is : <', base_path, '>')

env = Environment(
    loader=PackageLoader("openapi-to-modsecurity"),
    autoescape=select_autoescape()
)
modsecurity_template = env.get_template('modsecurity.cfg.template')