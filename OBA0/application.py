import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

engine = create_engine('postgresql://boalltxn:P@ssw0rd@localhost:5432/boalltxn')
db = scoped_session(sessionmaker(bind=engine))

#
@app.route("/")
def index():

    sql = "SELECT * FROM epsvisatx1"

    return render_template("index.html", )

@app.route("/txns")
def txns():
    sql = """SELECT *
           FROM
           (
           SELECT *
           FROM epsvisatx1 eps
           WHERE mti like '11%' --and product_id = 'ATM'
           ) eps
           LEFT JOIN
           (
           SELECT *
           FROM  clsvisaptlf
           WHERE auth_typ like '21%'
           ) ptlf ON eps.trace_id = ptlf.auth_seq_num
           LEFT JOIN
           (
           SELECT *
           FROM  clsvisatlf
           WHERE auth_typ like '21%'
           ) tlf ON eps.trace_id = tlf.auth_seq_num
           LEFT JOIN
           cardmbovisa cardm ON eps.trace_id = SUBSTRING(cardm.rrno,7,6)
           WHERE eps.local_date = '171219'
                 --AND eps.product_id like 'ATM'
                 --AND eps.trace_id = '000968'
           ORDER by eps.trace_id"""
    sql1 = "SELECT * FROM epsvisatx1"
    txns = db.execute(sql).fetchall()
    return render_template("txns.html", txns=txns)


if __name__ == '__main__':
   app.run()