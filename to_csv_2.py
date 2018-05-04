#!/usr/bin/env python3
'''
Note: when transfer to uxix , go to vi and use command :set ff:unix and :wq
'''
import os
import cx_Oracle
import csv
import datetime

# 1. EPS VISA text to csv
# 2. EPS VISP text to csv
# 3. CLS VISA TLF text to csv
# 4. CLS VISA PTLF text to csv
# 5. CARDMBO VISA database to csv

# 1. EPS VISA text to csv
def eps_visa_to_csv():

    # today = datetime.date.today().strftime('%y%m%d') #for auto
    today = '171219' #for manual

    current_path = os.getcwd()
    eps_filename = 'tx' + today
    with open(current_path + '\\' + eps_filename, 'r') as infile:
       data = infile.read()

    my_list = data.splitlines()

    total_line = 'CARD_NO,' \
                 'CARD_FIID,' \
                 'MTI,' \
                 'PRODUCT_ID,' \
                 'LOCAL_DATE,' \
                 'LOCAL_TIME,' \
                 'ACTION_CODE,' \
                 'PROCESSING_CODE,' \
                 'TXN_AMT,' \
                 'TXN_ORI,' \
                 'TXN_RSPDER,' \
                 'SEQ_NO,' \
                 'AUTH_APP_CODE,' \
                 'TRACE_ID,' \
                 'TXN_DATE,' \
                 'TXN_TIME,' \
                 'ACQ_CNTRY_CDE,' \
                 'ACQ_CRNCY_CDE,' \
                 'ACQ_ID_CDE,' \
                 'ISS_INST_ID,' \
                 'MERCHANT_ID,' \
                 'TERM_ID,' \
                 'TERM_FIID,' \
                 'TERM_LGNT,' \
                 'TERM_LOC,' \
                 'COUNTRY_CDE,' \
                 'CITY,' \
                 'TRACK2,' \
                 'TXN_AMT_CRNCY_CDE,' \
                 'RSN_CDE,' \
                 'AST-RTN-PRO-NAME,' \
                 'FROM_ACC,' \
                 'TXN_ID,' \
                 'SENDER_DATA(OCT)' \
                 '\n'

    for line in my_list:
        new_line = line[:19].strip() + ',' +   \
                   line[19:23].strip() + ',' + \
                   line[23:27].strip() + ',' + \
                   line[27:30].strip() + ',' + \
                   line[30:36].strip() + ',' + \
                   line[36:44].strip() + ',' + \
                   line[44:47].strip() + ',' + \
                   line[47:53].strip() + ',' + \
                   line[65:71].strip() + ',' + \
                   line[71:72].strip() + ',' + \
                   line[72:73].strip() + ',' + \
                   line[73:85].strip() + ',' + \
                   line[85:93].strip() + ',' + \
                   line[93:99].strip() + ',' + \
                   line[99:105].strip() + ',' + \
                   line[105:113].strip() + ',' + \
                   line[113:116].strip() + ',' + \
                   line[116:119].strip() + ',' + \
                   line[119:130].strip() + ',' + \
                   line[130:150].strip() + ',' + \
                   line[150:166].strip() + ',' + \
                   line[166:182].strip() + ',' + \
                   line[182:186].strip() + ',' + \
                   line[186:190].strip() + ',' + \
                   line[190:215].strip() + ',' + \
                   line[215:228].strip() + ',' + \
                   line[228:231].strip() + ',' + \
                   line[231:271].strip() + ',' + \
                   line[271:274].strip() + ',' + \
                   line[274:278].strip() + ',' + \
                   line[278:294].strip() + ',' + \
                   line[294:307].strip() + ',' + \
                   line[307:322].strip() + ',' + \
                   line[322:372].strip() + \
                   "\n"
        total_line += new_line

    #print(total_line)

    csv_filename = 'csv_eps_visa_tx1_' + today + '.csv'
    with open(current_path + '\\' + csv_filename, 'w',newline='') as outfile:
         outfile.write(total_line)
         print("CSV saved successfully: " + csv_filename)


# 5. CARDMBO VISA database to csv
def cardmbo_visa_to_csv():

    # today = datetime.date.today()
    today = '2017-12-19'
    # today2 = today.strftime('%y%m%d')
    today2 = '171219'
    # tomorrow = (today + datetime.timedelta(1))
    tomorrow = '2017-12-20'
    # tomorrow2 = tomorrow.strftime('%y%m%d')
    tomorrow2 = '171220'



    SQL = """
        SELECT trim(TERMID) AS TERM ,
               trim(SITCUSTDB.DECRYPTDATA(CARD_NO)) AS CARD ,
               trim(TO_CHAR(TXNREQDTTIME, 'dd/mm/yyyy HH24:MI:SS')) AS TXNDATETIME_RQ ,
               trim(TO_CHAR(TXNRESPDTTIME, 'dd/mm/yyyy HH24:MI:SS')) AS TXNDATETIME_RP ,
               trim(PROCCODE) AS TRANSCODE,
               trim(MSGTYPE) ,
               trim(SYS_TRACE_NO),
               trim(AUTHID),
               trim(RRNO),
               trim(ACQ_FIID),
               trim(ISS_FIID),
               trim(TXNAMT) AS AMT , 
               trim(ACCT_NO) AS FROMACCT ,
               trim(TO_ACCT_NO) AS TOACCT ,
               trim(RESPONSE_CODE) AS RSP , 
               trim(REVERSAL_FLAG) AS R,
               trim(DEVICE_TYPE) AS TT , 
               trim(POSENT_MODE) AS POS,
               trim(SRC_AGENT_TYPE), 
               trim(LOCALDATA)
        FROM SITCUSTDB.AUTHCTLBO
        WHERE TXNRESPDTTIME between TO_DATE( :1, 'yyyy-mm-dd') AND TO_DATE( :2, 'yyyy-mm-dd') 
              AND LOCALDATA like '%VIS%'
        ORDER BY TXNRESPDTTIME
        
    """

    start_date = str(today)
    end_date = str(tomorrow)

    csv_filename = 'csv_cardm_visa_' + str(today2) + '.csv'
    with open(csv_filename, 'w', newline='') as f:
        output = csv.writer(f)

        conn_string = "sitcustdb/GSBcard123@10.251.50.45:1521/CARDMS2"
        conn = cx_Oracle.connect(conn_string)
        cursor = conn.cursor()
        try:
            results = cursor.execute(SQL,(start_date,end_date)).fetchall()
            # results = cursor.execute(SQL).fetchall()
            header = [i[0] for i in cursor.description]
            output.writerow(header)

            for row in results:
                #print(row)
                output.writerow(row)
            cursor.close()
            conn.close()
            f.close()

        except cx_Oracle.DatabaseError as exc:
            print(str(type(exc)))                      # <class 'cx_Oracle.NotSupportedError'>
            print(repr(exc))                           # NotSupportedError('Variable_TypeByValue(): unhandled data type dict',)
            error, = exc.args                          # "error" is a str, NOT a cx_Oracle._Error object
            print("Oracle-Error-Code:", error.code)    # AttributeError: 'str' object has no attribute 'code'
            print("Oracle-Error-Message:", error.message)
            print("CSV saved successfully: " + csv_filename)


# eps_visa_to_csv()
cardmbo_visa_to_csv()