นาย ธนวิชญ์ กฤตวงศ์วิมาน
E-mail: tanawit139@gmail.com
Tel: 091-791-7575
วิธีการ run
1. ติดตั้ง Python 3
2. ติดตั้ง library xmltodict ผ่าน command line ด้วยคำสั่ง pip install xmltodict
3 นำไฟล์ xml ที่ต้องการจะแปลง ใส่ไว้ในโฟลเดอร์ Weather
4. run ไฟล์ชื่อ weather.py
5. พิมชื่อไฟล์ xml ที่ต้องการจะแปลง ตัวอย่างเช่น "weather.xml"
6. หลังไฟล์ถูกแปลงสำเร็จ จะมีข้อความแจ้ง และ delay 2 วินาที ก่อนปิดโปรแกรม
7. ไฟล์ที่ถูกแปลงแล้วจะมีชื่อว่า "weather.json"

Reference ของเว็บไซต์ที่ใช้ในการศึกษาเพื่อแก้ปัญหา
1. https://stackoverflow.com/questions/35452588/remove-special-characters-from-keys-of-a-parsed-xml-file-using-xmltodict
	- ใช้ศึกษา method parse ของ library xmltodict ในการกำหนด attribute prefix
2. https://docs.python-guide.org/scenarios/xml/
	- ใช้ศึกษา library xmltodict เพื่อสร้าง python dict จากข้อมูลที่เป็น xml format
3. https://docs.python.org/2/library/xml.etree.elementtree.html
	- ใช้ศึกษา ElementTree ของ library xml ใน python เพื่อทำความเข้าใจ farmat ของไฟล์ xml
4. https://stackoverflow.com/questions/15032108/pythons-open-throws-different-errors-for-file-not-found-how-to-handle-b/15032444
	- ค้นหา Exception ในกรณีที่เปิดไฟล์ไม่สำเร็จ
5. https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
	- ศึกษา library time เพื่อใช้ในการทำ delay 
6. https://docs.python.org/3/library/json.html
	- ศึกษา method dumps ใน library jason เพื่อทำ pretty printing