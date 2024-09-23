import re
import smtplib
import time
import logging
import dns.resolver
from colorama import Fore
from src.config import B2C_PROVIDERS, from_address
from src.utils import colored

regex = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
domain_mx_records = {}


def check_email(email, delay, suspicious_domains):
    if not re.match(regex, email):
        logging.error(f'Invalid syntax: {colored(email, Fore.RED)}')
        return None, "Invalid syntax"

    domain = email.split('@')[1]

    try:
        if domain not in domain_mx_records:
            records = dns.resolver.resolve(domain, 'MX')
            mx_record = str(records[0].exchange)

            domain_mx_records[domain] = mx_record

        mx_record = domain_mx_records[domain]

        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail(from_address)
        code, message = server.rcpt(email)
        server.quit()

        if code == 250:
            if domain in B2C_PROVIDERS or domain in suspicious_domains:
                return email, "Suspicious"
            return email, "Valid"
        else:
            return None, f"Failed SMTP check: {code} {message}"
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
        logging.error(f'{colored("DNS", Fore.RED)} error for {colored(email, Fore.RED)}: {e}')
        return None, "DNS error"
    except Exception as e:
        logging.error(f'{colored("SMTP", Fore.RED)} error for {colored(email, Fore.RED)}: {e}')
        return None, "SMTP error"
    finally:
        time.sleep(delay)
