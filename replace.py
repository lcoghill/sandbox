original_file = open('trees.out', 'r')
new_file = open('trees_fixed.out', 'w+')

for line in original_file:
	new_line = line.replace('gi_', 'gi')
	new_line = new_line.replace('ti_', 'ti')
	new_file.write(new_line)

original_file.close()
new_file.close()
