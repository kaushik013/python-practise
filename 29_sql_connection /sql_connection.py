import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="company",
    user="postgres",
    password="Kaushik@13",
    port="5432"
)

cur = conn.cursor()

# cur.execute("""
# CREATE TABLE google (
#     Emp_id INT PRIMARY KEY,
#     Name VARCHAR(50),
#     Dept VARCHAR(50),
#     Exp INT NOT NULL,
#     Salary INT NOT NULL
# )
# """)

# cur.execute("""
#     CREATE TABLE it (
#       Emp_id INT,
#       Name VARCHAR(50),
#       Exp INT NOT NULL,
#       Salary INT NOT NULL      
#     )
# """)

# cur.execute("""
#     CREATE TABLE finance (
#        Emp_id INT,
#        Name VARCHAR(50),
#        Exp INT NOT NULL,
#        Salary INT NOT NULL 
#     )
# """)


# cur.execute("""
#     CREATE TABLE hr(
#        Emp_id INT,
#        Name VARCHAR(50),
#        Exp INT NOT NULL,
#        Salary INT NOT NULL 
#     )
# """)

# cur.execute("""
#     CREATE TABLE clerk(
#         Emp_id INT,
#         Name VARCHAR(50),
#         Exp INT NOT NULL,
#         Salary INT NOT NULL 
#     )
# """)

cur.execute("SELECT version();")
print('Connected successfully ✅ : ',cur.fetchone())

class Company:

    def __init__(self, Emp_id, Name, Dept,Exp):
        self.Emp_id = Emp_id
        self.Name = Name
        self.Dept = Dept
        self.Exp = Exp
        self.Salary = 25000 * Exp

obj = Company(
    int(input('Enter the Emp_ID : ')),
    input('Enter the Name : '),
    input('Enter the Dept : '),
    int(input('Enter the Exp : ')),
)

cur.execute(
    "INSERT INTO google (Emp_id, Name, Dept, Exp, Salary) VALUES (%s, %s, %s, %s, %s)",
    (obj.Emp_id, obj.Name, obj.Dept, obj.Exp, obj.Salary)
)
conn.commit()

if(obj.Dept == 'it'):
    cur.execute(
        "INSERT INTO it (Emp_id, Name, Exp, Salary) VALUES (%s, %s, %s, %s)",
        (obj.Emp_id, obj.Name, obj.Exp, obj.Salary)
    )
    conn.commit()

if(obj.Dept == 'finance'):
    cur.execute(
        "INSERT INTO finance (Emp_id, Name, Exp, Salary) VALUES (%s, %s, %s, %s)",
        (obj.Emp_id, obj.Name, obj.Exp, obj.Salary)
    )
    conn.commit()

if(obj.Dept == 'hr'):
    cur.execute(
        "INSERT INTO hr (Emp_id, Name, Exp, Salary) VALUES (%s, %s, %s, %s)",
        (obj.Emp_id, obj.Name, obj.Exp, obj.Salary)
    )
    conn.commit()

if(obj.Dept == 'clerk'):
    cur.execute(
        "INSERT INTO clerk (Emp_id, Name, Exp, Salary) VALUES (%s, %s, %s, %s)",
        (obj.Emp_id, obj.Name, obj.Exp, obj.Salary)
    )
    conn.commit()