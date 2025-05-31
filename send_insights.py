import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader

# Load data
df = pd.read_csv('data/employee_data.csv')

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('email_template.html')

# Group data by manager
grouped = df.groupby("Manager")

# Email config
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'youremail@gmail.com'
EMAIL_PASSWORD = 'yourpassword'  # Use environment variables for security

def send_email(to_email, subject, html_content):
    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject

    part = MIMEText(html_content, 'html')
    msg.attach(part)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

# Simulated manager email mapping (replace with actual emails)
manager_emails = {
    'Alice': 'alice.manager@example.com',
    'Bob': 'bob.manager@example.com'
}

# Loop through managers and send insights
for manager, team_data in grouped:
    rendered = template.render(manager=manager, team=team_data.to_dict(orient='records'))
    send_email(manager_emails[manager], f"Weekly People Insights - {manager}", rendered)
    print(f"Sent report to {manager}")
