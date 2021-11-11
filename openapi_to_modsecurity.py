import argparse

parser = argparse.ArgumentParser(description='Convert an OpenAPI file to ModSecurity rules.')
parser.add_argument('openapi_file', type=str, help='Path to OpenAPI file')
parser.add_argument('modsecurity_file', type=str, help='Path to ModSecurity rules file')

args = parser.parse_args()
openapi_file = args.openapi_file.split('/')[-1]

if '.' not in openapi_file:
    raise NameError

ext = openapi_file.split('.')[-1]

if ext in ['yml', 'yaml']:
    print('Loading a YAML file')

if ext in ['json']:
    print('Loading a JSON file')