import psutil, json, datetime

# Whitelisted ports and expected processes
WHITELIST = {22:"sshd", 80:"nginx", 443:"nginx", 3306:"mysqld", 5432:"postgres"}
REPORT_FILE = "security_report.json"

ports = []
for c in psutil.net_connections(kind='tcp'):
    if c.status=='LISTEN':
        try:
            p = psutil.Process(c.pid)
            status = "OK" if WHITELIST.get(c.laddr.port)==p.name() else "SUSPICIOUS"
            ports.append({"port":c.laddr.port, "pid":c.pid, "user":p.username(), "process":p.name(), "status":status})
        except: pass

report = {"timestamp":datetime.datetime.now().isoformat(), "open_ports":ports}
with open(REPORT_FILE,'w') as f: json.dump(report,f,indent=4)
print(f"Report saved to {REPORT_FILE}")
