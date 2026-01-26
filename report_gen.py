import psycopg2
conn = psycopg2.connect(dbname="system_health")
cur = conn.cursor()
cur.execute("SELECT COUNT(*), COUNT(*) FILTER (WHERE status != 'HEALTHY') FROM health_logs;")
total, issues = cur.fetchone()
print (f"Total; {total}, Issues: {issues}")
cur.close()
conn.close()
