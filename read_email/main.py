#Импортируем библиотеки
import imaplib
import email
import base64
import re

#получаем данные почты
address =  input("Введите ваш адрес почты: ")
password = input("Введите пароль: ")

#конектимся к почте
mail = imaplib.IMAP4_SSL('imap.mail.ru')
try:
    mail.login(address, password)
except:
    print("\nНеверный адрес или пароль")
    exit(0)
mail.list()
mail.select("inbox")


#Получаем необходимое письмо
mails = mail.search(None, 'ALL')
print("\nMails: " + str(mails))
len = len(mails[1][0])
len = len - len//2
print("Length: " + str(len) + "\n")


#создаем/очищаем документ
f = open('links.txt', 'w')


for i in range(1,len+1):


    print("======================================================")
    print("Ссылок собрано: " + str(i) + "/" + str(len))


    #получаем тект письма
    res, msg = mail.fetch(str(i), '(RFC822)')
    msg = email.message_from_bytes(msg[0][1])


    #расшифровываем его из base64
    payload=msg.get_payload()
    text = ""
    link = ""
    decoded = False
    for part in msg.walk():
        if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
            try:
                text = text + base64.b64decode(part.get_payload()).decode()
                decoded = True
            except:
                print("Письмо не удалось расшифровать")
                text = ""


    #Находим ссылку
    try:
        if(decoded):
            link = re.search("(?P<url>https?://[^\s]+)", text).group("url")
    except:
        print("В письме нет ссылок")


    #записываем результат
    f.write(str(i) + ". " + link + '\n')


print("======================================================")
print("\nВсе письма проверенны")