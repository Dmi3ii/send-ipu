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
    print('=========================== send_sk_at_erc51_ru: ', str(request.form.get("send_sk_at_erc51_ru") != None))
    if request.form.get("send_sk_at_erc51_ru") != None:
        # email_to = 'sk@erc51.ru'
        email_to = 'dmi3ii@gmail.com'
        email_from = request.form.get('email')
        email_subject = request.form.get('address')
        email_message = request.form.get('id_IPU_HVS')+" "+request.form.get('HVS')+" "+request.form.get('id_IPU_GVS')+" "+request.form.get('GVS')
        Send(email_to, email_from, email_subject, email_message)

        return True
    else:
        return False


def send_oookola_v_centr_at_mail_ru():
    print('=========================== send_oookola_v_centr_at_mail_ru: ', (request.form.get("send_oookola_v_centr_at_mail_ru") != None))
    if request.form.get("send_oookola_v_centr_at_mail_ru") != None:
        # email_to = 'oookola_v_centr@mail.ru'
        email_to = 'dmi3ii@gmail.com'
        email_from = request.form.get('email')
        email_subject = request.form.get('address')

        email_message = request.form.get('address') + "\n" + request.form.get('fio') + "\n"
        lsEL = request.form.get('lsEL')
        if lsEL:
            email_message = email_message + lsEL + "\n"

        el = request.form.get('EL')
        if el:
            email_message = email_message + "Электричество: " + el + "\n"

        lsGAZ = request.form.get('lsGAZ')
        if lsGAZ:
            email_message = email_message + lsGAZ + "\n"

        gaz = request.form.get('GAZ')
        if gaz:
            email_message = email_message + "Газ:" + gaz + "\n"

        Send(email_to, email_from, email_subject, email_message)

        return True
    else:
        return False



def send_ooo_megaplast_at_mail_ru():
    print('=========================== send_ooo_megaplast_at_mail_ru: ', (request.form.get("send_ooo_megaplast_at_mail_ru") != None))
    if request.form.get("send_ooo_megaplast_at_mail_ru") != None:
        # email_to = 'ooo-megaplast@mail.ru'
        email_to = 'dmi3ii@gmail.com'
        email_from = request.form.get('email')
        email_subject = request.form.get('address')
        email_message = request.form.get('lsGVS') + "\n"
        email_message = email_message + request.form.get('fio') + "\n"
        email_message = email_message + request.form.get('address') + "\n"
        email_message = email_message + "ГВС: " + request.form.get('GVS')

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
