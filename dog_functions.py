import psycopg2 

def create_dog_table(conn,cursor):
    
    
    #Creating table in the database to store the csv file
    sql = '''create table dog_analysis2 (id int not null,\
    month char(30),\
    day char(30),\
    year int,\
    city char(30),\
    state char(15),\
    vic_name char(40),\
    vic_age char(40),\
    dog_type char(70),
    dog_number int);'''

    cursor.execute(sql)

   

def populate_dog_table(conn,cursor,f):
    
    line = f.read().splitlines()
    
    for caracter in line:
        command = caracter.split(',')
        counter2 = [0,1,2,3,4,5,6,7,8,9]
       
        sql2 = '''insert into dog_analysis2(id,month,day,year,city,state,vic_name,vic_age,dog_type,dog_number)''' + ''' values (''' 

        for i in counter2:
        #Each item to be added must be between single quotes '' or it will cause a syntax error.
            
            if (i == counter2[-1]):
                sql2 = sql2 + "\'" + str(command[i]) + "\'" 
            else:
                sql2 = sql2 + "\'" + str(command[i]) + "\'" + ''','''
            
        sql2 = sql2 + ''');'''
        
        cursor.execute(sql2)
    


def closing(conn,cursor):
    cursor.close()
    conn.commit()
    conn.close()
    print("Database connection closed")
