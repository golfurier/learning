import os
import cx_Oracle
import csv

# sql = """\\
#   SELECT empno,ename,sal FROM emp
#   WHERE sal > 2000
#   ORDER BY sal DESC"""

SQL = """
    SELECT TERMID AS TERM ,
           SITCUSTDB.DECRYPTDATA(CARD_NO) AS CARD ,
           TO_CHAR(TXNREQDTTIME, 'dd/mm/yyyy HH24:MI:SS') AS TXNDATETIME_RQ ,
           TO_CHAR(TXNRESPDTTIME, 'dd/mm/yyyy HH24:MI:SS') AS TXNDATETIME_RP ,
           PROCCODE AS TRANSCODE,
           MSGTYPE ,
           SYS_TRACE_NO,
           AUTHID,
           ACQ_FIID,
           ISS_FIID,
           TXNAMT AS AMT , 
           ACCT_NO AS FROMACCT ,
           TO_ACCT_NO AS TOACCT ,
           RESPONSE_CODE AS RSP , 
           REVERSAL_FLAG AS R,
           DEVICE_TYPE AS TT , 
           POSENT_MODE AS POS,
           SRC_AGENT_TYPE, 
           LOCALDATA
    FROM SITCUSTDB.AUTHCTLBO
    WHERE TXNRESPDTTIME between TO_DATE('2017-12-19', 'yyyy-mm-dd') AND TO_DATE('2017-12-20', 'yyyy-mm-dd') 
          AND LOCALDATA like '%VISA%'
    ORDER BY TXNRESPDTTIME
"""


# Network drive somewhere
# filename = "csv_cardm_visa.csv"
# f = open(filename,'w')
# output = csv.writer(f)
filename = "csv_cardm_visa.csv"
with open(filename,'w',newline='') as f:
    output = csv.writer(f)

# You can set these in system variables but just in case you didnt
#os.putenv(r'ORACLE_HOME', 'C:\oracle_client_lib\instantclient-basic-windows.x64-12.2.0.1.0\instantclient_12_2')
# os.putenv('LD_LIBRARY_PATH', '/oracle/product/10.2.0/db_1/lib')

    conn_string = "sitcustdb/GSBcard123@10.251.50.45:1521/CARDMS2"
    conn = cx_Oracle.connect(conn_string)

    cursor = conn.cursor()
    cursor.execute(SQL)
    header = [i[0] for i in cursor.description]
    results = cursor.execute(SQL).fetchall()
    print(results)
    # print(results[0][1].strip())
    # print(len(results))
    new_line = ''
    new_results = ''
    for i1, list in enumerate(results):
        #print(i1)
        for i2, in_list in enumerate(list):

            if not in_list:
                continue
            r = in_list.strip()
            print(i1, i2, r)
            new_line += r + ','
        new_results += new_line + '\n'
    print(new_results)
    # output.writerow(header)

    #results
    # for row in results:
    #     output.writerow(row)
    # cursor.close()
    # conn.close()
    # f.close()

    # cursor = conn.cursor()
    # cursor.execute(SQL)
    # for row in cursor:
    #     output.writerow(row)
    # cursor.close()
    # conn.close()
    # f.close()