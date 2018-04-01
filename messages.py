import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os


def create_message_raw(sender: str,
                       to: str,
                       subject: str,
                       message_text: str):
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return base64.urlsafe_b64encode(message.as_bytes()).decode()
