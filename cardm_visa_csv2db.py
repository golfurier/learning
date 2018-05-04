import csv
import psycopg2

conn_string = "dbname = 'boalltxn' user = 'boalltxn' password = 'P@ssw0rd' host = 'localhost' port = '5432'"
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

# Create TABLE in POSTGRES
cursor.execute("""Create Table CARDMBOVISA
                (TERM text,
                CARD text,
                TXNDATETIME_RQ text,
                TXNDATETIME_RP text,
                TRANSCODE text,
                MSGTYPE text,
                SYS_TRACE_NO text,
                AUTHID text,
                ACQ_FIID text,
                ISS_FIID text,
                AMT text,
                FROMACCT text,
                TOACCT text,
                RSP text,
                R text,
                TT text,
                POS text,
                SRC_AGENT_TYPE text,
                LOCALDATA text
                );""")

print("Table created successfully")

# import csv to database , by INSERT
# with open('csv_cardm_visa.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)  # Skip the header row.
#     for row in reader:
#         cursor.execute(
#             "INSERT INTO CARDMBOVISA VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#             row
#         )
# print("Data Inserted successfully")

# import csv to database , by COPY
with open('csv_cardm_visa.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cursor.copy_from(f, 'CARDMBOVISA', sep=',')
print("Data Inserted successfully")

cursor.close()
conn.commit()
conn.close()
