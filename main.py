import os
import logging
import argparse
from email_verifier.checker import process_emails, check_single_email

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def parse_args():
    parser = argparse.ArgumentParser(description='Email Verifier CLI Tool')
    parser.add_argument('input', nargs='?', default='input.txt', help='Path to the input file with email addresses')
    parser.add_argument('-o', '--output', default='validated_addresses.txt', help='Path to the output file for valid emails')
    parser.add_argument('-s', '--suspicious', default='suspicious_addresses.txt',
                        help='Path to the output file for B2C adresses\n'
                             '(this tool does not work very well against the big boys who have their own procedures and spam rules e.g.hotmail and yahoo.)')
    parser.add_argument('-d', '--delay', type=float, default=1.0, help='Delay between SMTP requests (in seconds)')
    parser.add_argument('-t', '--threads', type=int, default=4,
                        help='Number of threads for concurrent processing (default=4)')
    parser.add_argument('-e', '--email', help='Single email to verify (bypasses input file)')

    return parser.parse_args()


def run():
    args = parse_args()

    # Проверка одиночного email
    if args.email:
        check_single_email(args.email, args.delay)
    else:
        # Проверка email из файла
        if not os.path.exists(args.input):
            logging.error(f'Input file {args.input} does not exist.')
            exit(1)

        process_emails(args.input, args.output, args.suspicious, args.delay, args.threads)


if __name__ == '__main__':
    run()
