import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, from_email, password):
    # Create a MIMEText object to represent the email content
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server (in this case, Gmail)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Start TLS encryption
        server.login(from_email, password)  # Log in to your email account

        # Send the email
        server.sendmail(from_email, to_email, message.as_string())

        # Close the server connection
        server.quit()

        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", str(e))

# Example usage
if __name__ == "__main__":
    customer_email = "nay5naik@gmail.com"
    owner_email = "nayana.naik@subhanu.com"
    email_password = "Nay@5798"  # Ensure the security of this password

    customer_subject = "Thank you for your order"
    customer_body = "Dear customer, thank you for your recent order with our e-commerce website."

    owner_subject = "New order received"
    owner_body = "Dear owner, a new order has been placed on the e-commerce website."

    # Send email to the customer
    send_email(customer_subject, customer_body, customer_email, owner_email, email_password)

    # Send email to the owner
    send_email(owner_subject, owner_body, owner_email, owner_email, email_password)
