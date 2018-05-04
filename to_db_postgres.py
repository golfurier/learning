import csv
import psycopg2
import datetime

# 1. EPS VISA csv to db postgres
# 2. EPS VISP csv to db postgres
# 3. CLS VISA TLF csv to db postgres
# 4. CLS VISA PTLF csv to db postgres
# 5. CARDMBO VISA csv to db postgres

# getdate
def yesterday():
    nowday = datetime.date.today()
    # yesterday = (nowday - datetime.timedelta(1)).strftime('%y%m%d')
    yesterday = '171219'
    return yesterday
def today():
    # today = datetime.date.today().strftime('%y%m%d')
    today = '171219'
    return today
def tomorrow():
    nowday = datetime.date.today()
    tomorrow = (nowday + datetime.timedelta(1)).strftime('%y%m%d')
    return tomorrow

# 1. EPS VISA csv to db postgres
def eps_visa_to_db():

    conn_string = "dbname = 'boalltxn' user = 'boalltxn' password = 'P@ssw0rd' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    # import csv to database , by COPY
    csv_filename = 'csv_eps_visa_tx1_' + today() + '.csv'
    with open(csv_filename, 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f)  # Skip the header row.
        cursor.copy_from(f, 'EPSVISATX1', sep=',')
    print("EPS VISA Data Inserted successfully: " + csv_filename)

    cursor.close()
    conn.commit()
    conn.close()

# 3. CLS VISA TLF csv to db postgres
def cls_visa_tlf_to_db():

    conn_string = "dbname = 'boalltxn' user = 'boalltxn' password = 'P@ssw0rd' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    #import csv to database , by INSERT
    csv_filename = 'ir' + today()
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f, delimiter='|')
        #next(reader)  # Skip the header row.
        for row in reader:
             cursor.execute(
                "INSERT INTO CLSVISATLF VALUES (trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s))",
                row
            )
    print("TLF Data Inserted successfully: " + csv_filename)

    cursor.close()
    conn.commit()
    conn.close()

# 4. CLS VISA PTLF csv to db postgres
def cls_visa_ptlf_to_db():

    conn_string = "dbname = 'boalltxn' user = 'boalltxn' password = 'P@ssw0rd' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    #import csv to database , by INSERT
    csv_filename = 'ip' + today()
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f, delimiter='|')
        #next(reader)  # Skip the header row.
        for row in reader:
            cursor.execute(
                "INSERT INTO CLSVISAPTLF VALUES (trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s), trim(%s))",
                row
            )
    print("PTLF Data Inserted successfully: " + csv_filename)

    cursor.close()
    conn.commit()
    conn.close()


# 5. CARDMBO VISA csv to db postgres
def cardmbo_visa_to_db():

    conn_string = "dbname = 'boalltxn' user = 'boalltxn' password = 'P@ssw0rd' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    # import csv to database , by COPY
    csv_filename = 'csv_cardm_visa_' + today() + '.csv'
    with open(csv_filename, 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f)  # Skip the header row.
        cursor.copy_from(f, 'CARDMBOVISA', sep=',')
    print("CARDMBO VISA Data Inserted successfully: " + csv_filename)

    cursor.close()
    conn.commit()
    conn.close()


# eps_visa_to_db()
# cls_visa_tlf_to_db()
# cls_visa_ptlf_to_db()
cardmbo_visa_to_db()