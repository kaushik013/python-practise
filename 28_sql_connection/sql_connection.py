
import sqlite3

var = sqlite3.connect('student.db')
handle = sqlite3.Cursor(var)

# handle.execute('CREATE TABLE (SID NUMBER, Name VARCHAR2(50), DOB DATE, Standard NUMBER)')


handle.execute("INSERT INTO Student VALUES (12, 'Kaushik', '8/4/2003',12)")
# handle.execute()




var.commit()
var.close() 