import psutil
import psycopg2
from datetime import datetime

# 1. Capture Metrics
cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent

# 2. Theshold Logic (The "Brain")
if ram > 80 or cpu > 80:
	status = "CRITICAL"
elif ram > 50 or cpu > 50:
	status = "WARNING"
else:
	status = "HEALTHY" 

# 3. Database Injection 
try:
	conn = psycopg2.connect(dbname="system_health")
	cur = conn.cursor()
	cur.execute( "INSERT INTO health_logs (machine_id, cpu_usage, ram_usage, status) VALUES (%s, %s, %s, %s)", ('ubuntulab01', cpu, ram, status ))
	conn.commit()
	cur.close()
	conn.close()
except Exception as e:
	print (f"Database Error; {e}")
