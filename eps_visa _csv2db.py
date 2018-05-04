import csv
import psycopg2

conn_string = "dbname = 'boalltxn' user = 'boalltxn' password = 'P@ssw0rd' host = 'localhost' port = '5432'"
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

# Create TABLE in POSTGRES
cursor.execute("""Create Table EPSVISATX1
                (CARD_NO text,
                CARD_FIID text,
                MTI text,
                PRODUCT_ID text,
                LOCAL_DATE text,
                LOCAL_TIME text,
                ACTION_CODE text,
                PROCESSING_CODE text,
                TXN_AMT text,
                TXN_ORI text,
                TXN_RSPDER text,
                SEQ_NO text,
                AUTH_APP_CODE text,
                TRACE_ID text,
                TXN_DATE text,
                TXN_TIME text,
                ACQ_CNTRY_CDE text,
                ACQ_CRNCY_CDE text,
                ACQ_ID_CDE text,
                ISS_INST_ID text,
                MERCHANT_ID text,
                TERM_ID text,
                TERM_FIID text,
                TERM_LGNT text,
                TERM_LOC text,
                COUNTRY_CDE text,
                CITY text,
                TRACK2 text,
                TXN_AMT_CRNCY_CDE text,
                RSN_CDE text,
                AST_RTN_PRO_NAME text,
                FROM_ACC text,
                TXN_ID text,
                SENDER_DATA_OCT text
                );""")

print("Table created successfully")

# import csv to database , by INSERT
# with open('csv_eps_visa_tx1.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)  # Skip the header row.
#     for row in reader:
#         cursor.execute(
#             "INSERT INTO EPSVISATX1 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#             row
#         )
# print("Data Inserted successfully")

# import csv to database , by COPY
with open('csv_eps_visa_tx1.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cursor.copy_from(f, 'EPSVISATX1', sep=',')
print("Data Inserted successfully")

cursor.close()
conn.commit()
conn.close()
