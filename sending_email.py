import sendgrid
import json

with open('top_contacts.json') as json_data:
    d = json.load(json_data)
    json_data.close()
    temp = d.get('matches')
    
    emails = (temp[0]['email'], temp[1]['email'], temp[2]['email'], temp[3]['email'])

    sg = sendgrid.SendGridClient('hacktx-nasawarriors', 'hacktxpassword')

    for email in emails:
		message = sendgrid.Mail()
		message.add_to(email)
		message.set_subject('Example')
		message.set_html('Body')
		message.set_text('There is some Body text here that we will change or whatever')
		message.set_from('Nasa-Warriors <team@nasawar.com>')
		status, msg = sg.send(message)