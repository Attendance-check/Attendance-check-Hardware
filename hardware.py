import mysql.connector
import nfc

# MariaDB에 연결
mydb = mysql.connector.connect(
  host="yourhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)
mycursor = mydb.cursor()

# NFC 카드 정보 읽기
def on_startup(targets):
    return targets

def on_connect(tag):
    if isinstance(tag, nfc.tag.tt3.Type3Tag):
        uid = tag.identifier.hex()
        print(f"UID: {uid}")

        # MariaDB에 데이터 삽입
        sql = "INSERT INTO nfc_data (uid) VALUES (%s)"
        val = (uid, )
        mycursor.execute(sql, val)
        mydb.commit()

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-startup': on_startup, 'on-connect': on_connect})
