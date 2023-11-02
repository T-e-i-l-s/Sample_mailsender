#подключаем библиотеку
import smtplib
from email.mime.text import MIMEText


print("Что бы при рассылке не возникло трудностей удоcтоверьтесь,что вы:\n"
      "1.Используете почту с разрешением на вход с другим аккаунтом(gmail блокает попытки бота зайти в почту),"
      "поэтому лучше использовать mail.ru\n"
      "2.Вы создали файл mails.txt\n")


#принимаем адрес почты и пароль
mail = input("Email для отправки писем: ")
password = input("Пароль от " + mail + ": ")
#принимаем текст сообщения
title = input("Тема письма: ")
text = input("Текст для отправки: ")
print("\n")


#подключаемся к почте
server = smtplib.SMTP("smtp.mail.ru",587)
server.starttls()
#логинимся
try:
    server.login(mail,password)
except:
    print("Неверный логин или пароль")
    exit()


#читаем адреса получателей
try:
    f = open("mails.txt","r")
    mails = f.read()
    list = mails.split("\n",-1)
except:
    print("Создайте файл mails.txt")
    exit()
    

#рассылаем
for i in list:
    try:
        mes = MIMEText(text)
        mes["Subject"] = title
        server.sendmail(mail,i,mes.as_string())
        print("Отправленно на " + i)
    except:
        pass


print("\nЗавершено")
