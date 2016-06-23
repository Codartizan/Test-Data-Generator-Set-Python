import cx_Oracle
'''
con = cx_Oracle.connect('v01/v01@172.16.1.186/orcl')
# print con.version

cur1 = con.cursor()
cur2 = con.cursor()
cur3 = con.cursor()
cur4 = con.cursor()
cur5 = con.cursor()
cur6 = con.cursor()
cur7 = con.cursor()
cur8 = con.cursor()
cur9 = con.cursor()
cur10 = con.cursor()
'''
# result = []
'''
cur = con.cursor()
cur.execute("select card_nbr, micro_ref, pup_date, bill_amt, currncy_cd, orgn_curr, issr_amt,\
            auth_code, PROC_DAY from auth where matchdate = '0'")
'''
# cur1.execute("select card_nbr from event where matchdate = '0'")
'''
cur2.execute("select micro_ref from event where matchdate = '0'")
cur3.execute("select pur_date from event where matchdate = '0'")
cur4.execute("select bill_amt from event where matchdate = '0'")
cur5.execute("select currncy_cd from event where matchdate = '0'")
cur6.execute("select orgn_curr from event where matchdate = '0'")
cur7.execute("select issr_amt from event where matchdate = '0'")
cur8.execute("select auth_code from event where matchdate = '0'")
cur9.execute("select proc_day from event where matchdate = '0'")
cur10.execute('select visa_iss_proc_bin from banks')

result.append(cur1)
result.append(cur2)
result.append(cur3)
result.append(cur4)
result.append(cur5)
result.append(cur6)
result.append(cur7)
result.append(cur8)
result.append(cur9)
result.append(cur10)


for i in result:
    print i
'''
'''
print cur1

cur1.close()
cur2.close()
cur3.close()
cur4.close()
cur5.close()
cur6.close()
cur7.close()
cur8.close()
cur9.close()
cur10.close()
'''
'''
cur.close()
con.close()
'''

con = cx_Oracle.connect('v01/v01@172.16.1.186/orcl')          # Connect to DB
cur = con.cursor()

# cur.execute("select count(pur_date) from event where matchdate = '0'")
cur.execute("select card_nbr, micro_ref, pur_date from event where matchdate = '0'")   # execute Script

result = cur.fetchall()          # Collect all data
for result in cur:
    print result

f = open('VISAincomingData.txt', 'w')            # Open and Write data in file
f.write(str(result))

f.close()
cur.close()
con.close()
