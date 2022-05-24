from __future__ import absolute_import, unicode_literals

from django.core.mail import EmailMessage


def plain_email(to_email, subject, body):
    subject = subject
    body = body
    message = EmailMessage(
        subject, body, "noreply@oneheritagefinance.com", ["programmingtext@gmail.com", to_email]
    )
    message.content_subtype = "html"
    return message.send()


def pdf_attachment_email(to_email, subject, body, filepath, filename):
    from_email = sender
    subject = subject
    body = body
    message = EmailMessage(
        subject, body, from_email, ["programmingtext@gmail.com", to_email]
    )
    file_data = open(filepath, "rb")
    message.attach(filename, file_data.read(), "application/pdf")
    message.content_subtype = "html"
    file_data.close()
    return message.send()


def image_attachment_email(to_email, subject, body, filepath, filename):
    from_email = sender
    subject = subject
    body = body
    message = EmailMessage(
        subject, body, from_email, ["programmingtext@gmail.com", to_email]
    )
    file_data = open(filepath, "rb")
    message.attach(filename, file_data.read(), "image/jpeg")
    message.content_subtype = "html"
    file_data.close()
    return message.send()
