import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

engine = create_engine('postgresql://centcr:P@ssw0rd@localhost:5434/centcr')
db = scoped_session(sessionmaker(bind=engine))

#
@app.route("/")
def index():

    sql = "SELECT * FROM tcr"
    tcrs = db.execute(sql).fetchall()
    return render_template("index.html", tcrs = tcrs )

@app.route("/tcr")
def tcr():
    sql = """SELECT 
                    tcr.case_num,
                    tcr.mti,
                    tcr.description,
                    tcr.purpose,
                    tcr.card,
                    tcr.expected_values,
                    tcr.actual_values,
                    status.status,
                    tcr.progress_comment,
                    projects.proj_name,
                    switchings.sw_name,
                    transactions.trans_type,
                    actas.act_as,
                    testers.t_name,
                    accepters.a_name
                FROM tcr
                INNER 
                    JOIN status
                    ON tcr.status_id = status.id
                INNER
                    JOIN projects
                    ON tcr.project_id = projects.id
                INNER
                    JOIN switchings
                    ON tcr.switching_id = switchings.id
                INNER
                    JOIN transactions
                    ON tcr.transaction_id = transactions.id
                INNER
                    JOIN actas
                    ON tcr.actas_Id = actas.id
                INNER 
                    JOIN testers
                    ON tcr.tester_id = testers.id
                INNER 
                    JOIN accepters
                    ON tcr.accepter_id = accepters.id"""
    tcrs = db.execute(sql).fetchall()
    return render_template("tcr.html", tcr=tcrs)


if __name__ == '__main__':
   app.run()