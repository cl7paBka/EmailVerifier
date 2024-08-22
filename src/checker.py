import logging
import concurrent.futures
from src.smtp_verifier import check_email
from src.file_handler import read_emails, write_results


def check_single_email(email, delay):
    email, status = check_email(email, delay, [])
    if email and status == "Valid":
        print(f'{email} is valid.')
    elif email and status == "Suspicious":
        print(f'{email} is suspicious.')
    else:
        print(f'{email} is invalid: {status}')


def process_emails(input_file, output_file, suspicious_file, delay, threads):
    emails = read_emails(input_file)

    valid_emails = []
    suspicious_emails = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(check_email, email, delay, suspicious_emails): email for email in emails}

        for future in concurrent.futures.as_completed(futures):
            email = futures[future]
            try:
                result, status = future.result()
                if result and status == "Valid":
                    valid_emails.append(result)
                elif result and status == "Suspicious":
                    suspicious_emails.append(result)
            except Exception as exc:
                logging.error(f'{email} generated an exception: {exc}')

    write_results(valid_emails, suspicious_emails, output_file, suspicious_file)
    logging.info(f'Finished processing {len(emails)} emails.')

