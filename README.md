# UST-Training
## 🚨 Scenario 2 — Local Port & Process “Traffic Cop”
Build a tool that:

* Maps **open ports** to PIDs and usernames.
* Compares results against a **whitelist** of approved services.
* Flags suspicious or unknown ports.
* Generates a **structured security report**.

### 🛠️ Features

* Port → PID → User mapping
* Whitelist validation
* Output in JSON/CSV
* Written in Python (can use OS libraries)

### 📦 Usage

```
python traffic_cop.py --whitelist ports.json --output report.json
```

### 📊 Example Output (JSON)

```
{
  "port": 8080,
  "pid": 1234,
  "user": "devops",
  "status": "unapproved"
}
```

### 📈 Improvements

* Real-time monitoring loop
* Alert notifications (email/Slack)
* Service process profiling

---

## 🧠 Scenario 3 — Intelligent Log “Anomalizer”

### 🔍 Objective

Develop a tool to detect *unusual or anomalous patterns* in production logs, especially when “ERROR” is absent.

### 🛠️ Features

* Log ingestion (single file or directory)
* Word frequency and rare pattern detection
* Scoring anomalies
* Export summary insights

### 📦 Usage

```
python anomalizer.py --log-dir /var/log/app --threshold 0.01
```

### 📊 Sample Output

```
[ANOMALY] Unusual token frequency: user_xyz repeated 87x
```

### 📈 Improvements

* Integrate ML anomaly detection
* Visual dashboard (e.g., Grafana)
* Log enrichment (timestamps → events)

---

## 💽 Scenario 9 — Disk Usage Alert Script

### 🔍 Objective

Create a shell script that:

* Monitors disk usage
* Alerts when a threshold (e.g., 80%) is exceeded
* Logs alert details
* Runs via **cron**

### 🛠️ Example Script: `disk_alert.sh`

```
#!/bin/bash
THRESHOLD=80
USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ "$USAGE" -gt "$THRESHOLD" ]; then
  echo "$(date): Disk at ${USAGE}% used" >> /var/log/disk_alert.log
fi
```

### 📦 Cron Setup

```
# Run every 10 minutes
*/10 * * * * /path/disk_alert.sh
```

### 📈 Improvements

* Email/SMS alerts
* Monitor multiple mounts
* Integration with Prometheus

---

## 📦 Scenario 12 — Automated Backup & Cleanup Script

### 🔍 Objective

Build a shell script that:

* Creates **timestamped backups**
* Compresses files
* Deletes old b
