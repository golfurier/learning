import os
import cx_Oracle
import csv

# sql = """\\
#   SELECT empno,ename,sal FROM emp
#   WHERE sal > 2000
#   ORDER BY sal DESC"""

SQL = """
    SELECT trim(TERMID) AS TERM ,
           trim(SITCUSTDB.DECRYPTDATA(CARD_NO)) AS CARD ,
           trim(TO_CHAR(TXNREQDTTIME, 'dd/mm/yyyy HH24:MI:SS')) AS TXNDATETIME_RQ ,
           trim(TO_CHAR(TXNRESPDTTIME, 'dd/mm/yyyy HH24:MI:SS')) AS TXNDATETIME_RP ,
           trim(PROCCODE) AS TRANSCODE,
           trim(MSGTYPE) ,
           trim(SYS_TRACE_NO),
           trim(AUTHID),
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
    output.writerow(header)
    for row in results:
        print(row)
        output.writerow(row)
    cursor.close()
    conn.close()
    f.close()
print("CSV saved successfully")
    # cursor = conn.cursor()
    # cursor.execute(SQL)
    # for row in cursor:
    #     output.writerow(row)
    # cursor.close()
    # conn.close()
    # f.close()