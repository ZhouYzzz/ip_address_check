IP Address Check
===

A toolkit used to check the ip address, then send it to your Gmail.

### pre-requirements
```
pip install -r requirements.txt
```

### usage

```bash
python ip_address_check.py
```

or to schedule the script (daily check)
```bash
crontab -e

0 0 * * * python /path/to/ip_address_check_main.py

```

