def csv_reader(file_name):
    for row in open(file_name):
        yield row


line_count = 0
for line in csv_reader('tere.txt'):
    line_count += 1

print(f"Number of lines {line_count}")