import os, json

base_url = 'https://raw.githubusercontent.com/Louis331/Louis331.github.io/master/releases/'

output = []

for file_object in os.scandir('releases'):
  filename = file_object.name
  if filename.endswith('.pdf'):
    link = f'{base_url}{filename}'.replace(' ', '%20')
    output.append({"name": filename.replace('.pdf', ''), "link": link})

with open('index.json', 'w') as outputfile:
  json.dump(output, outputfile)
