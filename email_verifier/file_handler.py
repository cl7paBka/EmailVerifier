def read_emails(input_file):
    with open(input_file, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def write_results(valid_emails, suspicious_emails, output_file, suspicious_file):
    with open(output_file, 'w') as valid_file:
        valid_file.write('\n'.join(valid_emails))

    with open(suspicious_file, 'w') as suspicious_file:
        suspicious_file.write('\n'.join(suspicious_emails))
