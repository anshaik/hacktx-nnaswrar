import sendgrid

sg = sendgrid.SendGridClient('hacktx-nasawarriors', 'hacktxpassword')

message = sendgrid.Mail()
message.add_to('Adil Shaikh <anshaik@gmail.com>')
message.set_subject('Example')
message.set_html('Body')
message.set_text('There is some Body text here that we will change or whatever')
message.set_from('Nasa-Warriors <adil@nasawar.com>')
status, msg = sg.send(message)