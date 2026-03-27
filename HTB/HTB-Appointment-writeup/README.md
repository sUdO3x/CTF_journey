#  Appointment - HTB Write-up

_Author: sUdO3_

This repository contains a full walkthrough and solution for the **Appointment** machine on [Hack The Box](https://app.hackthebox.com/). The focus is primarily on exploiting a **SQL Injection** vulnerability to gain administrative access.

---

##  Machine Overview

- **Name**: Appointment  
- **Difficulty**: Easy  
- **Category**: Web  
- **IP Address**: _[10.129.115.68]_  
- **Tech Stack**: Apache, PHP, MySQL

---

##  Tools Used

- `nmap` – for port scanning and enumeration  
- Web browser – for interacting with the login page  
- `gobuster` – for directory brute forcing  
- Manual SQL injection payloads  

---

##  Walkthrough Highlights

- Enumeration using `nmap` reveals port 80 (Apache HTTP)
- Discovery of login form on root page
- Manual SQL Injection using:
  ```sql
  admin'#
