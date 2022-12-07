import sqlite3, csv

class SQL3Connector:
    
    name: str
    dbname: str
    tableslist: list
    
    def __init__(self, name, dbname):
    
        self.name = name = sqlite3.connect(f"{dbname}")
        self.dbname = dbname
        name.close()
    
    def execute_query(self, query):
        
        self.name = name = sqlite3.connect(f"{self.dbname}")
        cursor = name.cursor()
        cursor.execute(query)
        name.close()
    
    def tables(self):
    
        self.name = name = sqlite3.connect(f"{self.dbname}")
        cursor = name.cursor()
        dt = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for x in dt:
            print(f"{''.join(x)}")
        name.close()
      
    def tables_list(self, tableslist):
        
        self.tableslist = tableslist
        self.name = name = sqlite3.connect(f"{self.dbname}")
        cursor = name.cursor()
        dt = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for x in dt:
            a = ''.join(x)
            self.tableslist.append(a)
        name.close()
   
    def table_cols(self, tablename):
    
        self.name = name = sqlite3.connect(f"{self.dbname}")
        cursor = name.cursor()
        a = f"select * from {tablename}"
        cols = cursor.execute(a)
        names = [description[0] for description in cursor.description]
        print(names)
        name.close()

    def addto_table(self, tablename):
        
        self.name = name = sqlite3.connect(f"{self.dbname}")
        cursor = name.cursor()
        query1 = f"SELECT * FROM {tablename}"
        dt_data = cursor.execute(query1)
        cols = [description[0] for description in cursor.description]
        colstu = tuple(cols)
        valueslist = []
        for x in range(len(colstu)):
            x = input(f"Enter Data For {colstu[x]}:  ")
            valueslist.append(x)
        mytup = tuple(valueslist)
        lastquery1 = f"""INSERT INTO {tablename}{colstu} VALUES{mytup}"""
        cursor.execute(lastquery1)
        name.commit()
        name.close()
    
    def addto_table_vals(self, tablename, values):
        
        self.name = name = sqlite3.connect(f"{self.dbname}")
        cursor = name.cursor()
        query1 = f"SELECT * FROM {tablename}"
        dt_data = cursor.execute(query1)
        cols = [description[0] for description in cursor.description]
        colstu = tuple(cols)
        query2 = f"""INSERT INTO {tablename}{colstu} VALUES{values}"""
        cursor.execute(query2)
        name.commit()
        name.close()
   
    def table_tocsv(self,tablename,filename):
    
        self.name = name = sqlite3.connect(f"{self.dbname}")
        cursor = name.cursor()
        query1 = f"SELECT * FROM {tablename}"
        dt_data = cursor.execute(query1)
        fields = [description[0] for description in cursor.description]
        rows = [ x for x in dt_data ]
        with open(filename, 'w') as csvfile: 
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(fields) 
            csvwriter.writerows(rows)
        name.close()
        