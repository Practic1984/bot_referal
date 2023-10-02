create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  from_user_id INTEGER UNIQUE,
  from_user_username TEXT,
  regtime TEXT,
  wallet TEXT,
  referal_username TEXT,
  invest_all INTEGER,
  balance INTEGER,
  to_balance_wait INTEGER,
  out_balance_wait INTEGER
  
);
"""
create_ref_table = """
CREATE TABLE IF NOT EXISTS ref (
  from_user TEXT,
  to_user TEXT UNIQUE,
  regtime TEXT
);
"""
save_ref = """
INSERT OR IGNORE INTO ref (
  from_user,
  to_user,
  regtime
  )
VALUES (?,?,?)
"""

save_user = """
INSERT OR IGNORE INTO users (
  from_user_id,
  from_user_username,
  regtime,
  wallet,
  referal_username,
  invest_all,
  balance,
  to_balance_wait,
  out_balance_wait

  )
VALUES (?,?,?,?,?,?,?,?,?)
"""

find_profile_by_id = """
SELECT * FROM users WHERE from_user_id = ?
"""
find_null_balance = """
SELECT COUNT(balance) FROM users where balance = 0
"""
find_all_partners = """
SELECT COUNT(from_user_id) FROM users
"""
find_all_summ = """
SELECT SUM(balance) FROM users
"""

find_all_profile = """
SELECT * FROM users
"""
find_tree_url = """
SELECT * FROM ref
"""
upd_par_user = """
UPDATE users
SET '{upd_par}' = ?
WHERE from_user_id = ?
"""

up_proc = """
UPDATE users
SET balance = balance + balance * {proc} / 100
WHERE balance > 0
"""

to_balance_true = """
UPDATE users
SET to_balance_wait = 0, invest_all = invest_all + ?, balance = balance + ? 
WHERE from_user_id = ?
"""
out_balance_true = """
UPDATE users
SET out_balance_wait = 0, balance = balance - ? 
WHERE from_user_id = ?
"""
