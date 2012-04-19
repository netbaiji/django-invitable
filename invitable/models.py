import uuid

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.template import loader, Context
from django.mail import EmailMultiAlternatives

from invitable.hooks import connect_hooks

INVITABLE_USER = getattr(settings, "INVITABLE_USER", User)
INVITABLE_TOKEN_LENGTH = getattr(settings, "INVITABLE_TOKEN_LENGTH", 32)
INVITABLE_HTML_EMAIL = getattr(settings, "INVITABLE_HTML_EMAIL", True)

def token_gen():
    while True:
        token = uuid.uuid4()
        if not Invitation.objects.filter(token=token).count():
            break
    return token

INVITABLE_TOKEN_GEN = getattr(settings, "INVITABLE_TOKEN_GEN", token_gen)


class Invitation(models.Model):
    user = models.ForeignKey(INVITATION_USER)
    token = models.CharField(max_length=INVITATION_TOKEN_LENGTH)
    email = models.EmailField(unique=True, db_index=True)

    def __unicode__(self):
        return "Validation for [%s]" % (self.user.email)

    def after_create(self):
        # Send invitation on email

        # invitable/invitation_subject.txt
        # invitable/invitation.txt
        # invitable/invitation.html
        context = Context({'user': self.user,
                                'email': self.email,
                                'token': self.token})

        subject = loader.get_template("invitable/invitation_subject.txt")
                        .render(context)
        text_body = loader.get_template("invitable/invitation_body.txt")
                        .render(context)

        email = EmailMultiAlternatives(subject, text_body,
                                       INVITABLE_EMAIL_FROM, [self.email])

        if INVITABLE_HTML_EMAIL:
            html_body = loader.get_template("invitable/invitation_body.html")
                              .render(context)
            email.attach_alternative(html_body, "text/html")

        email.send()

connect_hooks(Invitation)
