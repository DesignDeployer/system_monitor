# ---------- Systemutveckling i Python ----------
# This module handles sending email alerts using SendGrid.


from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import config
import logging

def send_email_alert(alarm, current_value):
    """Send an email alert using SendGrid."""
    subject =f"ALERT: {alarm.alarm_type} Usage Alarm Triggered!"
    content = (
        f"This is an automated alert from your Python Monitoring System.\n\n"
        f"An alarm has been triggered for {alarm.alarm_type} usage.\n"
        f"Threshold: {alarm.threshold}%\n"
        f"Current Value: {current_value}%\n\n"
        f"Please check the system."
    )
    message = Mail(
        from_email=config.FROM_EMAIL,
        to_emails=config.TO_EMAIL,
        subject=subject,
        plain_text_content=content
    )
    try:
        sg = SendGridAPIClient(config.SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"\nEmail alert sent! Status code: {response.status_code}")
        logging.info(f"Email_alert_sent_for_{alarm.alarm_type}_alarm.")
    except Exception as e:
        print(f"\nError: Failed to send email alert. Reason:{e}")
        logging.error(f"Failed_to_send_email_alert_Reason_{e}")