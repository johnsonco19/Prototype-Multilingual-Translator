from googletrans import Translator
import psycopg2
from psycopg2 import Error

def connect_to_db(username='postgres', password='test', host='127.0.0.1', port='5432', database='WordsDatabase'):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        print("connected to the database")

        return cursor, connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

def disconnect_from_db(connection,cursor):
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
    else:
    	print("Connection does not work.")


def run_and_fetch_sql(cursor, sql_string="select * from arabicid"):
    try:
        # Executing a SQL query
        cursor.execute(sql_string)
        # Fetch result
        record = cursor.fetchall()
        return record
    
    except (Exception, Error) as error:
        print("Errors while executes the code: ", error)
        return -1


def run_and_commit_sql(cursor, connection, sql_string=""):
    try:
        # Executing a SQL query
        cursor.execute(sql_string)
        # if some changes are made, you need to commit your changes
        connection.commit()
        # use 1 to represent success
        return 1
    except (Exception, Error) as error:
        print("Errors while executes the code: ", error)
        return -1
    
    
def insert_word(table_name, id, lang, word):
    cursor, connection = connect_to_db()
    # execute SQL commands
    values = id + ",'" + lang + "','" + word + "'" 
    # 2'arabic','ل'
    record = run_and_commit_sql(cursor,connection,f'INSERT INTO {table_name}(wordid, langauge, word) VALUES ({values});')
  
    # print(f'INSERT INTO {table_name}(wordid, langauge, word) VALUES ({id}, "{lang}", "{word}");')
    # insert into arabicid (wordid, langauge, word) values (0,'arabic', 'الذي - التي' ) 
    # print(f"INSERT INTO {table_name} (wordid, langauge, word) VALUES ({id},""{{lang}"",""{word}"");")

    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        connection.commit()
        
    # disconnect from database
    disconnect_from_db(connection,cursor)

    
    source = ""
    destatiton = ""

    translator = Translator()

    translated = translator.translate('مرحبًا', src='ar', dest='en')

    # print(translated.text)

    print("Enter the langauge you would like to add")
    choice_lang = float(input("1: English, 2: Arabic, 3: Chinese, 4: Spanish: "))

    print(choice_lang)

    word = input("Enter word")

    print(word)
    translated = translator.translate(word, src='ar', dest='en')

    print(translated.text)
