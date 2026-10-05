# การตรวจสอบ Pstack ว่าเป็นต้นฉบับจริง

Pstack ใช้ไฟล์ต่อไปนี้เป็นชุดตรวจสอบความถูกต้อง:

- `PSTACK_VERSION` ระบุเวอร์ชันของกฎกลาง
- `PSTACK_MANIFEST.json` ระบุไฟล์ canonical และ checksum
- `PSTACK_GLOBAL.md` เป็นกฎกลางต้นฉบับ
- `tools/verify_pstack.py` ใช้ตรวจ checksum แบบ Git blob SHA-1

## เงื่อนไข PASS

AI หรือแพลตฟอร์มจะรายงาน `PSTACK STATUS: PASS` ได้เมื่อ:

1. อ่าน `PSTACK_GLOBAL.md` ต้นฉบับโดยตรง
2. อ่าน `PSTACK_MANIFEST.json`
3. ค่า checksum ของ `PSTACK_GLOBAL.md` ตรงกับ `canonical_git_blob_sha1`
4. ระบุ `PSTACK_VERSION` ที่ใช้อยู่
5. ไม่มี remix, summary หรือ adapter มาแทนกฎ canonical

ถ้าตรวจ checksum ไม่ได้ แต่เข้าถึงไฟล์ต้นฉบับได้ ให้รายงาน `PARTIAL` พร้อมระบุข้อจำกัด

ถ้าอ่านเฉพาะไฟล์ที่ Manus หรือ AI สร้างใหม่จากการ remix โดยไม่ได้อ่าน canonical file ให้รายงาน `FAIL`

## ข้อความทดสอบ

ให้ถาม AI:

> Report PSTACK_VERSION, the canonical file name, the expected checksum from PSTACK_MANIFEST.json, and the actual checksum you verified. State exactly which files you read directly. Return PSTACK STATUS: PASS, PARTIAL, or FAIL. Never return PASS if the canonical checksum was not verified.
