import psycopg2
from countWords import countFile

def putWordCountsInDB(db,lst):
    database = "dbname="+db
    conn = psycopg2.connect(database)
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT docid FROM wordcounts")
            result = cursor.fetchall()
            docIds_in_DB = []
            for res in result:
                docIds_in_DB.append(res[0])
            docIds_in_DB = list(set(docIds_in_DB))
            for file_for_WC in lst:
                if (docIds_in_DB is not None and file_for_WC[0] in docIds_in_DB):
                    print("DocId {} already exists in wordcounts".format(file_for_WC[0]))
                elif(file_for_WC[0] not in docIds_in_DB):
                    word_dict = countFile(file_for_WC[1])
                    for k,v in word_dict.items():
                        cursor.execute("INSERT INTO wordcounts VALUES (%s,%s,%s)",(file_for_WC[0],k,v))
        cursor.close()
    conn.close()
    pass
'''

def main():
    database = "documents-ap509"
    putWordCountsInDB(database,[(1,'akshay.txt'),(2,'ankit.txt'),(3,'ishan.txt')])

main()    
'''
