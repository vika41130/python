import yagmail

# yagmail.register('mygmailusername', 'mygmailpassword')
# yag = yagmail.SMTP("mailt6246@gmail.com", oauth2_file="~/oauth2_creds.json")
yag = yagmail.SMTP("mailt6246@gmail.com", "***")
recipients = ['vika41130@gmail.com', 'edgarwalker1349@gmail.com']
plain = "Hello there from Yagmail"
html = '''\
    <h3>From Yagmail</h3>
    <p>See you again,</p>
'''
attachments = ['assets/bronco.jpg', 'assets/bronco_classic.jpg']
contents = [html]
subject="Yagmail"
yag.send(
    to=recipients,
    subject=subject,
    contents=contents,
    attachments=attachments,
)

# send if f is available
# filename = "assets/bronco_classicc.jpg"
# try:
#     with open(filename, 'rb') as f:
#         yag.send(
#         to=recipients,
#         subject=subject,
#         contents=contents,
#         attachments=f,
#     )
# except:
#     print('except read file')
print('end')
