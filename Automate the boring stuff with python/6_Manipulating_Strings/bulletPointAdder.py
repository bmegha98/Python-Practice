#! python3
import pyperclip

pyperclip.copy('Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars')

text = pyperclip.paste()
print('Text copied from clipboard .. ',text,sep = '\n')

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* '+lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)

print('\nAfter adding bullet points -->\n')
print(pyperclip.paste())
