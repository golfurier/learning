import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://centcr:P@ssw0rd@localhost:5434/centcr')
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    sql = "SELECT * FROM tcrs"
    tcrs = db.execute(sql).fetchall()
    # for tcr in tcrs:
    #     print(len(tcr))
    #     print(tcr[i])
    #     for i in range(len(tcr)):

    return render_template("index.html", tcrs=tcrs)





@app.route("/tcr")
def tcr():
    sql = """SELECT tcrs.case_no,
                    tcrs.mti,
                    tcrs.case_name,
                    tcrs.purpose,
                    tcrs.card_no,
                    tcrs.f4,
                    tcrs.f39_exp,
                    tcrs.f39_visa,
                    tcrs.f39_mastercard,
                    tcrs.f39_itmx,
                    tcrs.f39_pcc,
                    tcrs.f39_eps,
                    tcrs.f39_clsp,
                    tcrs.f39_clst,
                    tcrs.f39_cardm,
                    tcrs.f39_cbs,
                    tcrs.seq_no,
                    tcrs.tdate,
                    tcrs.lgnt,
                    status.status,
                    tcrs.progress_comment,
                    projects.proj_name,
                    switchings.sw_name,
                    transactions.trans_type,
                    actas.act_as,
                    testers.t_name,
                    accepters.a_name
                FROM tcrs
                INNER 
                    JOIN status
                    ON tcrs.status_id = status.id
                INNER
                    JOIN projects
                    ON tcrs.project_id = projects.id
                INNER
                    JOIN switchings
                    ON tcrs.switching_id = switchings.id
                INNER
                    JOIN transactions
                    ON tcrs.transaction_id = transactions.id
                INNER
                    JOIN actas
                    ON tcrs.actas_Id = actas.id
                INNER 
                    JOIN testers
                    ON tcrs.tester_id = testers.id
                INNER 
                    JOIN accepters
                    ON tcrs.accepter_id = accepters.id"""
    tcrs = db.execute(sql).fetchall()
    for tcr in tcrs:
        print(len(tcr))
        for i in range(len(tcr)):
            print(tcr[i])
    return render_template("tcr.html", tcr=tcrs)



if __name__ == '__main__':
    app.run()
