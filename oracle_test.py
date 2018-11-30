import cx_Oracle

con = cx_Oracle.connect("id/pw@localhost:1521/sid")

cursor = con.cursor()
cursor.execute("""
select  tname
from    tab
""")

for tname in cursor:
  print(tname)