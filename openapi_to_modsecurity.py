import argparse

parser = argparse.ArgumentParser(description='Convert an OpenAPI file to ModSecurity rules.')
parser.add_argument('openapi_file', type=str, help='OpenAPI file path')
parser.add_argument('modsecurity_file', type=str, help='ModSecurity file path')

args = parser.parse_args()