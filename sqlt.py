import sqlite3

conn = sqlite3.connect('ims.db')
c = conn.cursor()


# def create_table():
#     c.execute(
#         'CREATE TABLE IF NOT EXISTS product(name TEXT, stock REAl, price REAl, retail REAL)'
#     )


# c.execute("INSERT INTO products(name, stock, price) VALUES('shoe', '12', '150')")

# conn.commit()


# c.execute("DELETE FROM product WHERE rowid ='5'")

# conn.commit()


# c.execute("ALTER TABLE product ADD retail price REAL")

# conn.commit()

# c.execute("SELECT * FROM product WHERE name='soap'")
# items = c.fetchall()


# q = "SELECT rowid,* FROM product WHERE name="'+name'

# c = conn.execute(q)

# data_row = c.fetchone()

# self.p_str.set(data_row[2])

# ids = data_row[0]

# print(ids)

# st = data_row[2] - 2

# print(st)

# # for getting names of columns of table

# c = conn.execute('select * from product')

# names = list(map(lambda x: x[0], c.description))

# names = [description[0] for description in c.description]

# print(names)


# # Updating Values in DB table

# c.execute("UPDATE product SET stock = 348 WHERE rowid = 2")
# conn.commit()

c = conn.execute('select * from product')

names = list(map(lambda x: x[0], c.description))

names = [description[0] for description in c.description]

print(names)


c.execute("SELECT * FROM product")
items = c.fetchall()

# print(items[-1])

for item in items:
    print(item)


# # Creating table with primary key

# c.execute("CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT, stock INTEGER, price REAL);")


# create_table()
# insert_table()

c.close()
conn.close()


# names = ["Jane", "Janet", "James", "Jamie"]

# entry = "James"


# def command():

#     for i in range(3):

#         if entry != "" and entry == names[i][:len(entry)]:
#             print("Names: ", names[i])
#             print("Length: ", len(entry))
#             print("Searched: ", names[i][:len(entry)])


# command()

# testing = []


# for i in self.a_tree.get_children():
#     print(self.a_tree.item(i))
#     testing.append(self.a_tree.item(i))

# print(testing)
