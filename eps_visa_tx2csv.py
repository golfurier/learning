#!/usr/bin/env python3
'''
Note: when transfer to uxix , go to vi and use command :set ff:unix and :wq
'''
import os

def texttocsv():

    #with open(r'D:\Self_Service_Work\learn\Python\log\tx1_171219','r') as infile:
    #with open (input(str("please input your file: ")),'r') as infile:
    #filename = input(str('pls input file: '))
    current_path = os.getcwd()
    with open(current_path + '\\' + input((str("please input your file: "))), 'r') as infile:
        #path = infile.
        data = infile.read()
        #print(data)
        #print("-" * 10)

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
        #print(line[:16] + ',' + line[19:23] + ',' + line[27:30] + ',' + line[44:47] + ',' + line[93:99])

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

    print(total_line)
    print("CSV converted successfully")
    #with open(r'D:\Self_Service_Work\learn\Python\log\new_tx1.csv','w') as outfile:
    with open(current_path + '\\' + 'csv_eps_visa_tx1.csv', 'w') as outfile:
         outfile.write(total_line)
         print("CSV saved successfully")


texttocsv()
