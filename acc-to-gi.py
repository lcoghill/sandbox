import MySQLdb

db = MySQLdb.connect("localhost", "user", "password", "database")
cursor = db.cursor()

f = open('acc-to-gi.txt', 'r')
print "Getting count of total records..."
record_count = 1  
for line in f:
    record_count += 1
f.close()

f = open('acc-to-gi.txt', 'r')
count = 1
for line in f:
    acc, gi = line.split(" ")
    acc = acc.replace(" ", "")
    gi = gi.replace(" ", "")
    print "Inserting record %s / %s..." % (count, record_count)
    cursor.execute('''INSERT into accession_and_gi (accession, gi) values (%s, %s)''', (acc, gi))
    db.commit()
    count += 1

db.close()
f.close()
