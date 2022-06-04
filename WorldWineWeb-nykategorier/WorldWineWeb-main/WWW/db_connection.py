#Kopplar all info till db och deklareras i veriablen.

import psycopg2


conn = psycopg2.connect(host = 'pgserver.mau.se',
                database = 'am4404',
                user = 'am4404',
                password = 'zxd0hy59')

cur = conn.cursor()   


