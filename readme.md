# CALCULATE APIs

## การติดตั้ง lib ที่ใช้ใน project

```bash
pip install -r requirements.txt
```

## การรัน project

```bash
python main.py
```

แล้วไปที่ url
http://localhost:8000

## หากมีการติดตั้ง lib ใหม่อย่าลืมอัปเดตรายการ lib ก่อน deploy

```bash
pip freeze > requirements.txt
```

สามารถใช้งาน api ได้ที่ https://calculate-mauve.vercel.app/docs

## Version

### 1.0.0

- มี api สำหรับคำนวณค่าโดยใส่สมการที่ต้องการ และ api สำหรับแก้สมการ 1 ตัวแปร (ตัวแปร x)
