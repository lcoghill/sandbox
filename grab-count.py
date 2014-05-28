
tree_count = 50
count = 1
original_file = open('trees.fixed.out', 'r')
name = "%s.trees.out" %tree_count
new_file = open(name, 'w+')

for line in original_file:
    if count <= tree_count:
        new_file.write(line)
        count += 1

original_file.close()
new_file.close()
