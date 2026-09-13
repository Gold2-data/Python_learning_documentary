name = "hello world"
print(name)

#change case in string
name = "ada lovelace"

#first letter case
print(name.title())

#uppercase
print(name.upper())

#lowercase
print(name.lower())

#f-strings
first_name = "jane"
last_name = "john"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"{first_name.title()} surname is, {last_name.upper()}")

#whitespace
languages = "python, C, javascript"
print("\tlanguages: python, C, javascript")
print("\nlanguages: python, C, javascript")
print("\n\tlanguages: \n\tpython, \n\tC, \n\tjavascript")

#remove blank
name = " jane "

print(name.lstrip())
print(name.rstrip())
print(name.strip())

#remove preffix

facebook_url = 'https://gold-doe.facebook.com'
social_link = facebook_url.removeprefix('https://')
print(social_link)

#remove suffix
filename = 'python_notes.txt'
filename = filename.removesuffix('.txt')
print(filename)

#numbers
print(5+3)
print(4+4)
print(80*2)
print(80/4)
print(2**3)

