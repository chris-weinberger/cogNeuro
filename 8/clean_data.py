def clean(file_handle):
	write_out = open("clean_data3.txt", "w")

	lines = file_handle.readlines()
	for line in lines:
		line_data = line.strip().split(',')
		for item in line_data:
			write_out.write(item)
			write_out.write(' ')
		write_out.write('\n')

f = open('fixing_data.csv')
clean(f)