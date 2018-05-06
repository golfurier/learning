SELECT 
	tcrs.case_no,
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
	ON tcrs.accepter_id = accepters.id








	