-- =====================================================================
-- Security Incident & Threat Investigation SQL Queries
-- Description: Collection of SQL scripts for querying employee assets, 
--              filtering suspicious login activities, and joining tables 
--              for security audits.
-- =====================================================================

-- SECTION 1: Asset Inventory & Basic Retrieval
-- Purpose: Retrieve specific device hardware and OS information.
SELECT device_id, operating_system, OS_patch_date 
FROM machines;


-- SECTION 2: Advanced Filtering (AND / OR / NOT / LIKE)
-- Purpose: Investigate failed login attempts that occurred after business hours (> 18:00).
SELECT event_id, username, login_date, login_time, success 
FROM log_in_attempts 
WHERE success = 0 AND login_time > '18:00:00';

-- Purpose: Filter login attempts that did not originate from Mexico to flag potential anomalies.
SELECT event_id, username, country, ip_address 
FROM log_in_attempts 
WHERE country NOT LIKE 'MEX%';

-- Purpose: Query specific event ID ranges for incident analysis.
SELECT event_id, username, login_date 
FROM log_in_attempts 
WHERE event_id BETWEEN 100 AND 150;


-- SECTION 3: Relational Table Joins (INNER & LEFT JOINS)
-- Purpose: Match employees to their assigned machines to verify hardware updates.
SELECT machines.device_id, employees.username, machines.operating_system, employees.department 
FROM machines 
INNER JOIN employees 
ON machines.device_id = employees.device_id;

-- Purpose: Identify unassigned machines using a Left Join (devices sitting in storage).
SELECT machines.device_id, machines.operating_system, employees.username 
FROM machines 
LEFT JOIN employees 
ON machines.device_id = employees.device_id;
