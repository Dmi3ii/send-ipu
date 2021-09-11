import smtplib
from SendEmail import Send
from flask import Flask, g, render_template, url_for, request, redirect
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    g.active_home = True
    return render_template('home.html')

def send_sk_at_erc51_ru():
    if request.form["send_sk_at_erc51_ru"]:
        # email_to = 'sk@erc51.ru'
        email_to = 'dmi3ii@gmail.com'
        email_from = request.form['email']
        email_subject = request.form['address']
        email_message = request.form['id_IPU_HVS']+" "+request.form['HVS']+" "+request.form['id_IPU_GVS']+" "+request.form['GVS']
        Send(email_to, email_from, email_subject, email_message)

        return True
    else:
        return False


def send_oookola_v_centr_at_mail_ru():
    if request.form["send_oookola_v_centr_at_mail_ru"]:
        # email_to = 'oookola_v_centr@mail.ru'
        email_to = 'dmi3ii@gmail.com'
        email_from = request.form['email']
        email_subject = request.form['address']

        email_message = request.form['address'] + "\n" + request.form['fio'] + "\n"
        lsEL = request.form['lsEL']
        if lsEL:
            email_message = email_message + lsEL + "\n"

        el = request.form['EL']
        if el:
            email_message = email_message + "Электричество: " + el + "\n"

        lsGAZ = request.form['lsGAZ']
        if lsGAZ:
            email_message = email_message + lsGAZ + "\n"

        gaz = request.form['GAZ']
        if gaz:
            email_message = email_message + "Газ:" + gaz + "\n"

        Send(email_to, email_from, email_subject, email_message)

        return True
    else:
        return False



def send_ooo_megaplast_at_mail_ru():
    if request.form["send_ooo_megaplast_at_mail_ru"]:
        # email_to = 'ooo-megaplast@mail.ru'
        email_to = 'dmi3ii@gmail.com'
        email_from = request.form['email']
        email_subject = request.form['address']
        email_message = request.form['lsGVS'] + "\n"
        email_message = email_message + request.form['fio'] + "\n"
        email_message = email_message + request.form['address'] + "\n"
        email_message = email_message + "ГВС: " + request.form['GVS']

        Send(email_to, email_from, email_subject, email_message)

        return True
    else:
        return False



@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':        
        print('=========================== START ===========================')
        g.send_sk_at_erc51_ru = send_sk_at_erc51_ru()
        g.send_oookola_v_centr_at_mail_ru = send_oookola_v_centr_at_mail_ru()
        g.send_ooo_megaplast_at_mail_ru = send_ooo_megaplast_at_mail_ru()
        print('=========================== FINISH ===========================')
        return render_template('complete.html')
    else:
        g.active_send = True
        return render_template('send.html')


if __name__ == "__main__":
    app.run(debug=True)
