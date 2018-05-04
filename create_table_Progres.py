import csv
import psycopg2


# 1. EPS VISA table
# 2. EPS VISP table
# 3. CLS VISA table : TLF
# 4. CLS VISA tble : PTLF
# 5. CARDMBO VISA table

# 1. create EPS VISA table in POSTGRES database
def table_eps_visa():

    conn_string = "dbname = 'boalltxn' user = 'boalltxn' password = 'P@ssw0rd' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    # Create TABLE in POSTGRES
    cursor.execute("""CREATE table EPSVISATX1
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
    cursor.close()
    conn.commit()
    conn.close()

    print("EPSVISATX1 Table created successfully")

# 2. create EPS VISP table in POSTGRES database

# 3. create CLS VISA : TLF table in POSTGRES database
def table_cls_visa_tlf():
    conn_string = "dbname = 'boalltxn' user = 'boalltxn' password = 'P@ssw0rd' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    # Create TABLE in POSTGRES
    cursor.execute("""CREATE table CLSVISATLF
                    (TERM_FIID text,           
                    TERM_ID text,
                    CRD_FIID text,
                    PAN text,
                    AUTH_TRAN_DAT text,
                    AUTH_TRAN_TIM text,
                    AUTH_SEQ_NUM text,
                    AUTH_TRAN_CDE text,
                    AUTH_TYP text,
                    AUTH_FROM_ACCT text,
                    AUTH_TO_ACCT text,
                    TERM_TYP text,
                    RESPONDER text,
                    RESP_CDE text,
                    AUTH_AMT_1 text,
                    AUTH_FEE_AMT_1 text,
                    AUTH_AMT_2 text,
                    POST_DAT text,
                    REGN_ID text,
                    BRCH_ID text,
                    ACQ_INST_ID_NUM text,
                    RCV_INST_ID_NUM text,
                    INTERREGION text,
                    ACQ_FEE text,
                    ISS_FEE text,
                    BEN_FEE text,
                    BILL_CNT_1 text,
                    BILL_CNT_2 text,
                    BILL_CNT_3 text,
                    BILL_CNT_4 text
                    );""")
    cursor.close()
    conn.commit()
    conn.close()

    print("CLSVISATLF Table created successfully")

# 4. create CLS VISA : PTLF table in POSTGRES database
def table_cls_visa_ptlf():
    conn_string = "dbname = 'boalltxn' user = 'boalltxn' password = 'P@ssw0rd' host = 'localhost' port = '5432'"
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    # Create TABLE in POSTGRES
    cursor.execute("""CREATE table CLSVISAPTLF
                    (term_fiid text,     
                    term_term_id text,   
                    crd_fiid text,      
                    auth_crd_typ text,   
                    CRD_CARD_CRD_NU text,
                    auth_tran_dat text,  
                    auth_tran_tim text, 
                    auth_seq_num text,  
                    auth_tran_cde text, 
                    auth_typ text,      
                    TERM_CNTRY_CDE text,
                    TERM_OWNER_NAME text,
                    TERM_CITY text,     
                    auth_responder text,
                    auth_resp_cde text, 
                    auth_apprv_cde text,
                    auth_amt_1 text,    
                    auth_amt_2 text,    
                    term_ln text,       
                    crd_ln text,         
                    auth_rte_stat text 
                    );""")
                    
    cursor.close()
    conn.commit()
    conn.close()

    print("CLSVISAPTLF Table created successfully")

# 5. create CARDMBO VISA table in POSTGRES database
def table_cardmbo_visa():
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
                    RRNO text,
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
    cursor.close()
    conn.commit()
    conn.close()

    print("CARDMBOVISA Table created successfully")


table_eps_visa()
table_cls_visa_tlf()
table_cls_visa_ptlf()
table_cardmbo_visa()


