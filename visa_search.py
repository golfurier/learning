import psycopg2
import datetime

#search by date or all
#by card
#by terminal
#by product

def visa_search():

    # date = input("input date (YYMMDD): ")
    # product = input("input product (ATM/POS): ")

    conn_string = "dbname = 'boalltxn' user = 'boalltxn' password = 'P@ssw0rd' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    SQL = """
                    /*
        ==========================  ATM , POS =====
        */
        SELECT 	DISTINCT eps.trace_id as "TRACE ID",
            eps.card_no as "CARD NO",
            eps.card_fiid as "CARD FIID",
            eps.term_id as "TERM ID",
            eps.term_fiid as "TERM FIID",
            eps.product_id as "PRODUCT",
            --eps.local_date as "DATE",
            to_date(eps.local_date, 'YYMMDD') as "DATE",
            eps.local_time as "TIME",
            --to_timestamp(eps.local_time, 'HH24MISSMS') as "TIME",
            eps.term_lgnt as "ENV",
            eps.processing_code as "EPS PROC CODE",
            eps.txn_amt as "EPS AMOUNT",
            eps.action_code as "EPS RC",
            ptlf.auth_tran_cde as "PTLF TRAN CODE",
            ptlf.auth_amt_1 as "PTLF AMOUNT",
            ptlf.auth_resp_cde as "PTLF RC",
            tlf.auth_tran_cde as "TLF TRAN CODE",
            tlf.auth_amt_1 as "TLF AMOUNT",
            tlf.auth_fee_amt_1 as "TLF FEE",
            tlf.resp_cde as "TLF RC",
            cardm.transcode as "CARDM TRAN CODE",
            cardm.amt as "CARDM AMOUNT",
            cardm.rsp as "CARDM RC",
            cardm.r as "RVSL"
            
        --SELECT *
        FROM 
        (
        SELECT *
        FROM epsvisatx1 eps
        WHERE mti like '11%' --and product_id = 'ATM'
        ) eps 
        LEFT OUTER JOIN 
        (
        SELECT *
        FROM  clsvisaptlf
        WHERE auth_typ like '21%' 
        ) ptlf ON eps.trace_id = ptlf.auth_seq_num
        LEFT OUTER JOIN
        (
        SELECT *
        FROM  clsvisatlf
        WHERE auth_typ like '21%' 
        ) tlf ON eps.trace_id = tlf.auth_seq_num
        LEFT JOIN 
        cardmbovisa cardm ON eps.trace_id = SUBSTRING(cardm.rrno,7,6)
        WHERE eps.local_date = '171219' AND eps.product_id like 'ATM' 
        ORDER by eps.trace_id
            
    """
    cursor.execute(SQL)

    # while True:
    row = cursor.fetchall()

    print(row)

    cursor.close()
    conn.close()


visa_search()