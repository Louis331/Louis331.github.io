import os

base_url = 'this_is_a_test'

output = []

for file_object in os.scandir('releases'):
  filename = file_object.name
  if filename.endswith('.pdf'):
    link = f'{base_url}{filename}'.replace(' ', '%20')
    output.append({'name': filename.replace('.pdf', ''), 'link': link})

print(output)