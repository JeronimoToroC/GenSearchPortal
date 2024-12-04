import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Cargar variables de entorno al inicio del módulo
load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "465"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_FROM")

def send_email(to_email: str, subject: str, message: str):
    """Enviar un correo electrónico con SSL."""
    try:
        if not EMAIL_HOST or not EMAIL_PORT or not EMAIL_USER or not EMAIL_PASSWORD or not EMAIL_FROM:
            raise ValueError("Faltan configuraciones en las variables de entorno para el correo.")

        # Conectar al servidor SMTP con SSL
        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)

            # Crear el mensaje
            msg = MIMEMultipart()
            msg["From"] = EMAIL_FROM
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))

            # Enviar el correo
            server.sendmail(EMAIL_FROM, to_email, msg.as_string())
            print(f"Correo enviado exitosamente a {to_email}")

    except smtplib.SMTPException as smtp_err:
        print(f"Error SMTP al enviar el correo: {smtp_err}")
        raise
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        raise
