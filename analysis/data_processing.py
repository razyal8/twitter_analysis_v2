import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

def insert_csv_to_mongodb(csv_file, db, collection_name):

    nRowsRead = 10 # specify 'None' if want to read whole file

    df1 = pd.read_csv(csv_file, delimiter=',', nrows = nRowsRead)
    df1.dataframeName = 'tweets.csv'
    nRow, nCol = df1.shape
    logging.info(f'There are {nRow} rows and {nCol} columns')
    
    documents = df1.to_dict(orient='records')
    for document in documents:
        inserted = db.insert_one(collection_name, document)
        if inserted:
            logging.info(f"Document {document['id']} inserted successfully.")
        else:
            logging.info(f"Document {document['id']} with the same id already exists.")




    
    
