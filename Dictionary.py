"""
* specify word-definition separator
* specify document file path
* make sure that each word-definition pair takes up only one line(change font to 1px)
* download python-docx 
"""


from docx import Document
import random

# Choose path
f = Document(r'')

# Specify word-definition separator
sep = '-'

# Initialize variables
lines = []
words = {}

# Extract lines from file
for paragraph in f.paragraphs:
    lines.extend(paragraph.text.splitlines())

# Populate dictionary and check for errors (lines number matching etc)
for line in lines:
    if sep in line:
        key, value = line.split(sep,1)
        if key and value:
            words[key.strip()] = value.replace('\t', '').replace('\n', '').strip() 
        else: print('No key or value: ',key,value)
    else: print('no separator: ',line)
print(len(words.keys()))


# Show random words-definition pair
while words:
    random_key = random.choice(list(words.keys()))
    random_value = words.pop(random_key)

    print(r'----------------------')
    print(random_key)
    input()
    print(random_value)
    input()
