import psycopg2
conn = psycopg2.connect(dbname="system_health")
cur = conn.cursor()
cur.execute("INSERT INTO health_logs (machine_id, cpu_usage, ram_usage, status) VALUES ('ubuntulab01', 99.9, 99.9, 'CRITICAL');")
conn.commit()
print ("CRITICAL entry injected successfully!")
cur.close()
conn.close()
