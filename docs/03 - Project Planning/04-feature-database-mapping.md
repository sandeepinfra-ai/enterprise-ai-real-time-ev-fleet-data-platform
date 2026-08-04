# Feature to Database Mapping

## Document Information

| Field | Value |
|--------|--------|
| Project | Enterprise AI-Powered Real-Time EV Fleet Data Platform |
| Version | 1.0 |
| Status | Approved |

---

# Purpose

This document maps business features to their corresponding database tables. It ensures that every feature has a well-defined data model before database implementation begins.

---

# Database Overview

Database: PostgreSQL

Schema: public

Primary Database Type: Relational Database

---

# Authentication Module

| Feature | Database Table |
|----------|----------------|
| User Login | users |
| User Registration | users |
| User Roles | roles |
| Permissions | permissions |
| User Sessions | user_sessions |

---

# User Management Module

| Feature | Database Table |
|----------|----------------|
| Create User | users |
| Update User | users |
| Delete User | users |
| User Activity | audit_logs |

---

# Vehicle Management Module

| Feature | Database Table |
|----------|----------------|
| Register Vehicle | vehicles |
| Vehicle Details | vehicles |
| Vehicle Status | vehicle_status |
| Vehicle Assignment | vehicle_assignments |

---

# Telemetry Module

| Feature | Database Table |
|----------|----------------|
| Live Telemetry | telemetry |
| Battery Data | telemetry |
| Speed Data | telemetry |
| Temperature Data | telemetry |
| GPS Location | telemetry |

---

# Alert Module

| Feature | Database Table |
|----------|----------------|
| Battery Alert | alerts |
| Temperature Alert | alerts |
| Offline Alert | alerts |
| Alert History | alerts |

---

# Dashboard Module

| Feature | Database Table |
|----------|----------------|
| Fleet Dashboard | telemetry |
| Vehicle Dashboard | vehicles |
| KPI Dashboard | dashboard_metrics |

---

# Reporting Module

| Feature | Database Table |
|----------|----------------|
| Daily Report | reports |
| Weekly Report | reports |
| Monthly Report | reports |
| Export Report | reports |

---

# Audit Module

| Feature | Database Table |
|----------|----------------|
| Login History | audit_logs |
| User Actions | audit_logs |
| System Changes | audit_logs |

---

# Planned Database Tables

| Table Name | Purpose |
|------------|----------|
| users | Store user information |
| roles | Store user roles |
| permissions | Store role permissions |
| user_sessions | Active user sessions |
| vehicles | Vehicle master data |
| vehicle_status | Current vehicle status |
| vehicle_assignments | Driver to vehicle mapping |
| telemetry | Live telemetry records |
| alerts | System alerts |
| reports | Generated reports |
| dashboard_metrics | Dashboard KPIs |
| audit_logs | Audit trail |

---

# Database Relationships

users

↓

vehicle_assignments

↓

vehicles

↓

telemetry

↓

alerts

↓

reports

---

# Database Standards

- UUID Primary Keys
- Foreign Key Constraints
- Index Frequently Queried Columns
- Soft Delete Where Required
- Audit Columns in Every Table
- Created At / Updated At Timestamps
- NOT NULL Constraints for Mandatory Fields

---

# Future Database Modules

- Kafka Event Store
- Spark Analytics Tables
- Data Warehouse
- Machine Learning Features
- Prediction Results
- Historical Analytics

---

# Approval

| Role | Status |
|------|--------|
| Database Architect | Approved |
| Solution Architect | Approved |
| Product Owner | Approved |