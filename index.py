from app.app import App
from db import MongoDB
from analysis.data_processing import insert_csv_to_mongodb

def main():
    # Connect to MongoDB
    db = MongoDB(db_name="new_db")

    # Read CSV and insert data into MongoDB
    csv_file = 'data/tweets.csv'
    collection_name = "tweetstest"
    insert_csv_to_mongodb(csv_file, db, collection_name)
    app = App()
    app.mainloop()
    db.close_connection()

if __name__ == "__main__":
    main()
