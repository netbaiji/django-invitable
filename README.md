Handles invitations based sign up for Django

#Features
  * Account types (If you have multiple account types)
  * Only admins are able to send invitations
  * Timestamps for sent_at and accepted_at
  * Django admin integration
  * Custom registration (using invite token) - work in progress

#Installation
  * Add `django-invitable` directory to your Python path.
  * Add `invitable` to your INSTALLED_APPS tuple found in your settings file.
  * Include `invitable.urls` to your URLconf.
  * Needs `django.core.mail` to be setted up.
  * Create template `invitable/invitation_subject.txt` for invitation email subject
  * Create template `invitable/invitation_body.txt` for invitation email body
  * Optional: create template `invitable/invitation_body.html` for invitation email html body

#Usage
You can configure `django-invitable` with the following settings:

  * `INVITABLE_USER`: User model for invite sender. Useful if you customized things. Default `User`.
  * `INVITABLE_HTML_EMAIL`: Whether to send also HTML alternative. Default `false`. If set to `True` you have to provide template `invitable/invitation_body.html`
  * `INVITABLE_EMAIL_FROM`: What email will appear as sender, default `no-reply@example.com`
  * `INVITABLE_TOKEN_LENGTH`: Size of the token db column (default 64)
  * `INVITABLE_TOKEN_GEN`: Token generator function. Default is built-in function using uuid.
  * `INVITABLE_ACCOUNT_TYPES`: Hash containing account types. Keys are account types, values are full account types values. Default: `{"admin": "Admin", "team": "Team Member", "client": "Client"}`.

