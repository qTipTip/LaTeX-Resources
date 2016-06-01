from l2wp_auxilliary import *
from sys import argv

filename_in = 'example.tex'
filename_out = 'wordpress.html'

with open(filename_in, 'r') as infile:
    tex_code = infile.read()

print('Extracting body of tex-file...')
tex_code = extract_body(tex_code)

print(tex_code)
