from django.template.loader import get_template


def send_email(subject, template_name, from_email, to_emails, context):
    from django.core.mail import EmailMultiAlternatives
    message_template = get_template(template_name)
    message_html = message_template.render(context)
    msg = EmailMultiAlternatives(
        subject,
        message_html,
        from_email,
        to_emails
    )
    msg.content_subtype = 'html'
    msg.send()
