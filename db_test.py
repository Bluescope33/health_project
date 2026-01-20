import psycopg2
import psutil # You might need to 'pip install psutil'
import socket

# 1. Gather System Data
hostname = socket.gethostname()
cpu_use = psutil.cpu_percent(interval=1)
ram_use = psutil.virtual_memory().percent

try:
	conn = psycopg2.connect(dbname="system_health", user="lclark", password = "Password1!", host= "localhost")
	cur= conn.cursor()

	# 2. Ensure the machine is registered (The "Upsert" logic)
	cur.execute("INSERT INTO machines (hostname) VALUES (%s) ON CONFLICT (hostname) DO NOTHING;",(hostname,))
	

	# 3. Get the machine_id
	cur.execute("SELECT id FROM machines WHERE hostname = %s;", (hostname,)) 
	machine_id = cur.fetchone()[0]
	

	# 4. Insert the Telemetry
	cur.execute("INSERT INTO health_logs (machine_id, cpu_usage, ram_usage) VALUES (%s, %s, %s);",
			(machine_id, cpu_use, ram_use))

	conn.commit()
	print (f"Logged: CPU {cpu_use}% | RAM {ram_use}% for {hostname}")

	cur.close()
	conn.close()

except Exception as e:
	print (f"Database Error: {e}")
