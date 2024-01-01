from utils import *
# libs included in utils:
# parser
from rich import print

lines = parser.chunked_ints(file_name='day5.txt')
print(type(lines))
for line in lines:
    print(line, type(line))