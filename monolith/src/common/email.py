from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Optional

import aiosmtplib
from pydantic import EmailStr

from .config import get_settings
from .logger import get_logger

settings = get_settings()
logger = get_logger(__name__)


async def send_email(
    to_email: EmailStr,
    subject: str,
    html_content: str,
    from_email: Optional[EmailStr] = None,
    from_name: Optional[str] = None,
    cc: Optional[List[EmailStr]] = None,
    bcc: Optional[List[EmailStr]] = None,
) -> bool:
    """Send an email using SMTP."""
    try:
        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["To"] = to_email
        message["From"] = f"{from_name or settings.EMAILS_FROM_NAME} <{from_email or settings.EMAILS_FROM_EMAIL}>"

        if cc:
            message["Cc"] = ", ".join(cc)
        if bcc:
            message["Bcc"] = ", ".join(bcc)

        # Add HTML content
        message.attach(MIMEText(html_content, "html"))

        # Send email
        await aiosmtplib.send(
            message,
            hostname=settings.SMTP_HOST,
            port=settings.SMTP_PORT,
            username=settings.SMTP_USER,
            password=settings.SMTP_PASSWORD,
            use_tls=settings.SMTP_TLS,
        )

        logger.debug(
            "Email sent",
            extra={
                "to": to_email,
                "subject": subject,
            },
        )
        return True
    except Exception as e:
        logger.error(
            "Failed to send email",
            extra={
                "to": to_email,
                "subject": subject,
                "error": str(e),
            },
        )
        raise


async def send_welcome_email(to_email: EmailStr, name: str) -> bool:
    """Send a welcome email to a new user."""
    subject = "Welcome to E-Learning Platform"
    html_content = f"""
    <html>
        <body>
            <h1>Welcome to E-Learning Platform!</h1>
            <p>Dear {name},</p>
            <p>Thank you for joining our platform. We're excited to have you on board!</p>
            <p>Best regards,<br>The E-Learning Team</p>
        </body>
    </html>
    """
    return await send_email(to_email, subject, html_content)


async def send_password_reset_email(to_email: EmailStr, reset_token: str) -> bool:
    """Send a password reset email."""
    subject = "Password Reset Request"
    reset_url = f"https://elearning-platform.com/reset-password?token={reset_token}"
    html_content = f"""
    <html>
        <body>
            <h1>Password Reset Request</h1>
            <p>You have requested to reset your password. Click the link below to proceed:</p>
            <p><a href="{reset_url}">Reset Password</a></p>
            <p>If you did not request this, please ignore this email.</p>
            <p>Best regards,<br>The E-Learning Team</p>
        </body>
    </html>
    """
    return await send_email(to_email, subject, html_content)


async def send_verification_email(to_email: EmailStr, verification_token: str) -> bool:
    """Send an email verification email."""
    subject = "Verify Your Email"
    verification_url = f"https://elearning-platform.com/verify-email?token={verification_token}"
    html_content = f"""
    <html>
        <body>
            <h1>Verify Your Email</h1>
            <p>Please verify your email address by clicking the link below:</p>
            <p><a href="{verification_url}">Verify Email</a></p>
            <p>If you did not create an account, please ignore this email.</p>
            <p>Best regards,<br>The E-Learning Team</p>
        </body>
    </html>
    """
    return await send_email(to_email, subject, html_content) 