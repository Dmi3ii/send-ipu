from flask import Flask, g, render_template, url_for, request, redirect
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    g.active_home = True
    return render_template('home.html')

# @app.route('/test')
# @app.route('/test/<name>/<num>')
# def test(name=None, num=None):
#     return render_template('test.html', name=name, num=num)

def send_sk_at_erc51_ru():
    smtplib
    # with open('test.html') as file:
    #     html = file.readlines()
    """
    Мурмаши, энергетиков 7, 7
    Dmitrey Kashkin <dmi3ii@gmail.com>	18 августа 2021 г., 17:59
    Кому: sk@erc51.ru
    10061713 120, 10061712 65
    """
    if request.form["send_sk_at_erc51_ru"]:
        # gmail_user = "send.ipu@gmail.com"

# "send.ipu.py@gmail.com"

        gmail_password = "send.ipu.py_51"

        # msg = EmailMessage()
        # msg["Subject"] = request.form["fio"] + " " + request.form["address"]
        # msg["From"] = request.form["email"]
        # msg["To"] = "dmi3ii@gmail.com"
        # msg["Body"] = request.form["id_IPU_HVS"] + " " + request.form["HVS"] + request.form["id_IPU_GVS"] + " " + request.form["GVS"]

        # with smtplib.SMTP('localhost') as s:
        #     s.send_message(msg)

        return True
    else:
        return False


def send_oookola_v_centr_at_mail_ru():
    '''
    Мурмаши Энергетиков 7, 7
    Dmitrey Kashkin <dmi3ii@gmail.com>	18 августа 2021 г., 18:03
    Кому: Кольский Вычислительный Центр <oookola_v_centr@mail.ru>
    1058900700
    Мурмаши Энергетиков 7, 7
    газ: 6.6
    '''
    if request.form["send_oookola_v_centr_at_mail_ru"]:
        return True
    else:
        return False



def send_ooo_megaplast_at_mail_ru():
    '''
    ГВС энергетиков 7, 7
    Dmitrey Kashkin <dmi3ii@gmail.com>	18 августа 2021 г., 18:01
    Кому: Мурмашинский расчётный центр <ooo-megaplast@mail.ru>

    3170007000
    Мурмаши. Энергетиков 7, 7
    ГВС: 65
    '''
    if request.form["send_ooo_megaplast_at_mail_ru"]:
        return True
    else:
        return False



@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        g.send_sk_at_erc51_ru = send_sk_at_erc51_ru()
        g.send_oookola_v_centr_at_mail_ru = send_oookola_v_centr_at_mail_ru()
        g.send_ooo_megaplast_at_mail_ru = send_ooo_megaplast_at_mail_ru()
        return render_template('complete.html')
    else:
        g.active_send = True
        return render_template('send.html')


if __name__ == "__main__":
    app.run(debug=True)
