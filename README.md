# Extract e-mail address of undeliverable e-mails.

When an undelivered e-mail is sent back to the e-mail server it contains the
address of who is sending it back, not the address it was sent to, in many cases
this will be Microsoft Postmaster. This makes getting a list of e-mail addresses
where the wrong address was entered harder to find, as the bounce back e-mail
is from a 3rd party and not the e-mail. It is possible however to get the e-mail
address from the message body as it will contain the wrong e-mail address.
The body of the e-mail will contain useful information such as error details,
the body of the text send, and more importantly - the e-mail address it was sent to.   

And I typed cleam instead of clean when naming this repository.
