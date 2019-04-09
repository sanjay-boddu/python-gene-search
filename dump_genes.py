import json
import mysql.connector
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursorPrepared
import os


database_config = {
    'user': 'anonymous',
    'password': '',
    'host': 'ensembldb.ensembl.org',
    'database': 'ensembl_website_90',
    'use_pure':True
}


try:
    connection = mysql.connector.connect(**database_config)
    if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)
       cursor = connection.cursor(cursor_class=MySQLCursorPrepared)
       cursor.execute("select species, display_label from gene_autocomplete")
       
       genes_of_species = {}

       record = cursor.fetchone()
       while record is not None:
          genes_of_species.setdefault(record[0], []).append(record[1]) 
          record = cursor.fetchone()

       try:  
         data_files_path = os.getcwd()+"/data"  
         os.makedirs(data_files_path, exist_ok=True) 
       except OSError:  
         print(f"Creation of the directory {data_files_path} failed")
       else:  
         print(f"Successfully created the directory {data_files_path}")


       for species, gene_list in genes_of_species.items():
           with open("data/"+species+".json", "w") as write_file:
              json.dump(list(set(gene_list)), write_file)

except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

