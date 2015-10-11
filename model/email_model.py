## test

#encoding=utf-8

# from email.mime.text import MIMEText
import smtplib

if __name__ == '__main__':


    from_addr = 'huashiyiqike@qq.com'
    password = 'lvqi056496748'

    smtp_server = 'smtp.qq.com'

    to_addr = 'huashiyiqike@qq.com'

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    #server.starttls()
    #server.connect(host=smtp_server, port=25)
    #server.esmtp_features["auth"]="AUTH_LOGIN"
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr],"test")
    server.quit()