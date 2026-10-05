# วิธีใช้ Pstack เป็นศูนย์กลางสำหรับหลาย AI

เป้าหมายคือให้ GitHub repository `OAKY55/pstack` เป็น Source of Truth เพียงจุดเดียว แล้วให้แต่ละ AI อ่านกฎชุดเดียวกัน

## โครงสร้างที่เพิ่ม

- `PSTACK_GLOBAL.md` คือกฎกลาง
- `SKILL.md` คือจุดนำเข้าแบบ Skill ที่ root
- `AGENTS.md` คือ adapter สำหรับ agent/coding harness ที่รองรับไฟล์ชื่อนี้
- `CLAUDE.md` คือ adapter สำหรับ Claude Code
- `GEMINI.md` คือ adapter สำหรับ Gemini CLI/โปรเจกต์ที่อ่านไฟล์นี้
- `ai-adapters/MANUS.md` คือวิธีใช้กับ Manus
- `ai-adapters/CHATGPT.md` คือวิธีใช้กับ ChatGPT
- `ai-adapters/KIMI.md` คือวิธีใช้กับ Kimi
- `ai-adapters/DEEPSEEK.md` คือวิธีใช้กับ DeepSeek
- `ai-adapters/QWEN.md` คือวิธีใช้กับ Qwen

## หลักการสำคัญ

ไม่มี GitHub commit ใดที่สามารถเปลี่ยน "การตั้งค่าบัญชีส่วนกลาง" ของบริการ AI ทุกเจ้าได้เอง เพราะแต่ละแพลตฟอร์มควบคุม memory, custom instructions, skills และ project settings แยกกัน

สิ่งที่ repository นี้ทำได้คือทำให้ทุก AI มีไฟล์กลางชุดเดียวกันเพื่ออ้างอิง และลดการแก้กฎซ้ำหลายชุด

## Manus

ให้ Import repository `https://github.com/OAKY55/pstack` เป็น Skill โดยใช้ root `SKILL.md` ที่เพิ่มไว้

หลัง Import ให้ทดสอบด้วยข้อความ:

> State which Pstack files you loaded for this task. Separate verified facts from inference. Do not claim any tool action that you did not actually perform.

## ChatGPT / Kimi / DeepSeek / Qwen

ถ้าแพลตฟอร์มสามารถอ่าน GitHub หรือไฟล์โปรเจกต์ได้ ให้ชี้มาที่ repo นี้

ถ้าเป็นช่อง Custom Instructions ที่ไม่ sync GitHub อัตโนมัติ ให้ใช้ bootstrap ในไฟล์ `ai-adapters/<AI>.md` แล้วคง GitHub เป็น Source of Truth

## Claude Code

เปิดโปรเจกต์จาก repository นี้ แล้ว `CLAUDE.md` จะทำหน้าที่เป็น adapter ชี้กลับไปที่กฎกลาง

## Gemini

เปิดโปรเจกต์จาก repository นี้ แล้วใช้ `GEMINI.md` เป็น adapter ชี้กลับไปที่กฎกลาง

## ตรวจสอบว่าทำงานจริง

ถาม AI ว่า:

> ก่อนตอบ ให้บอกชื่อไฟล์ Pstack ที่คุณอ่านจริงใน session นี้ และแยกว่าอะไรคือ verified fact กับ inference

ถ้า AI อ้างว่าอ่านไฟล์ที่มันเข้าถึงไม่ได้ ให้ถือว่าการตั้งค่ายังไม่ผ่านการตรวจสอบ
