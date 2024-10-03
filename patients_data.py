filenames = ['patients-data_tcutk-one.txt', 'patients-data_tcutk-two.txt']

for filename in filenames:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)