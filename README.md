A Python-based system health monitoring tool that collects real-time CPU and RAM metrics 
and logs them to a PostgreSQL database on a 60-second automated schedule. 
Built in a Linux environment using VirtualBox.


# Autonomous System Health Monitor

## Project Evolution Timeline

### Phase 1: Data Warehouse Foundation (Week 1)
- **Objective**: Establish a persistent storage layer for hardware telemetry.
- **Milestones**:
    - Initialized PostgreSQL `system_health` database.
    - Designed relational schema `health_logs` with automated timestamps and hardware metric fields (CPU/RAM).
    - Verified manual data entry via SQL `INSERT` operations.

### Phase 2: The Integration Bridge 
- **Objective**: Connect hardware sensors to the database using Python.
- **Milestones**:
    - Established Python-to-PostgreSQL connectivity using `psycopg2`.
    - Implemented a Virtual Environment (`venv`) to ensure dependency isolation and system stability.
    - Developed `db_test.py` to programmatically capture real-time system metrics.

### Phase 3: Automation & Reliability
- **Objective**: Remove human intervention and manage data lifecycle.
- **Milestones**:
    - **Heartbeat Implementation**: Configured Cron to execute telemetry scripts every 60 seconds.
    - **Automated Retention**: Implemented a "Janitor" script to purge logs older than 7 days, preventing disk-space exhaustion (SLA Management).
    - **Error Handling**: Configured log redirection (`2>&1`) for remote troubleshooting and auditing.
    - **Version Control**: Established a secure GitHub pipeline using Personal Access Tokens (PAT) and verified audit trails.

## Tech Stack
- **OS**: Ubuntu Linux (VirtualBox Lab)
- **Database**: PostgreSQL
- **Language**: Python 3.x
- **Automation**: Cron
- **VCS**: Git/GitHub
