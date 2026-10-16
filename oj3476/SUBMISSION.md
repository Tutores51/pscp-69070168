# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3476
```

OJ submission ID, if submitted:

```text
690839
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
30-60 minutes
```

Choose one:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```text
ในฝูงแมวมีจิ้งจอกปนอยู่ สัตว์แต่ละตัวมีหมายเลข และชื่อ ให้นับว่ามีแมวกี่ตัว จิ้งจอกกี่ตัว แล้วแสดงชื่อพร้อมหมายเลขเรียงตามหมายเลข (แมวก่อน จิ้งจอกทีหลัง)
input บรรทัดแรก: จำนวนสัตว์ที่ระบุมา
บรรทัดที่เหลือ: dict ตัวละบรรทัด
output Cat : จำนวนแมว
Fox : จำนวนจิ้งจอก
รายชื่อ ชื่อ : หมายเลข เรียงตามหมายเลข
constraints ไม่มีชื่อซ้ำหรือหมายเลขซ้ำ
```

---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```text
Step 1: รับจำนวนสัตว์ที่ระบุมา animal_count
Step 2: สร้าง Dict herd เพื่อเก็บหมายเลขเป็น key และชื่อเป็น value
Step 3: ใช้ for วนรับข้อมูลทีละบรรทัด แล้วตัด { } และเครื่องหมาย " ออก
Step 4: แยกข้อมูลด้วย splitได้ชื่อ name และหมายเลข number แล้วเก็บลง herd[number] = name
Step 5: สร้าง used_names เพื่อตรวจว่าชื่อ Garfield และ Fubuki ถูกใช้แล้วหรือไม่
Step 6: ตรวจว่า "Cat01" ไม่อยู่ใน herd และชื่อ Garfield ยังไม่ถูกใช้ หากเข้าเงื่อนไขให้เติม herd["Cat01"] = "Garfield"
Step 7: ตรวจว่า "Fox01" ไม่อยู่ใน herd และชื่อ Fubuki ยังไม่ถูกใช้ หากเข้าเงื่อนไขให้เติม herd["Fox01"] = "Fubuki"
Step 8: สร้าง List cat_numbers และ fox_numbers เพื่อแยกหมายเลขของแมวและจิ้งจอก
Step 9: ใช้ for วนทุก key ใน herd หากขึ้นต้นด้วย "Cat" ให้เก็บใน cat_numbers หากไม่ใช่ให้เก็บใน fox_numbers
Step 10: เรียง cat_numbers และ fox_numbers ด้วย sort
Step 11: แสดง Cat ตามด้วยcat_numbers
Step 12: แสดง Fox ตามด้วยfox_numbers
Step 13: วนแสดงชื่อและหมายเลขของแมวทั้งหมดใน cat_numbers
Step 14: วนแสดงชื่อและหมายเลขของจิ้งจอกทั้งหมดใน fox_numbers
```

---

## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```text
same because it working
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```text
มีทั้ง Cat และ Fox และต้องเพิ่มข้อมูลเริ่มต้น
```

Input:

```text
4
{"Shiro" : "Fox03"}
{"Kin" : "Cat02"}
{"Tom" : "Cat04"}
{"Kuro" : "Fox02"}
```

Expected output:

```text
Cat : 3
Fox : 3
Garfield : Cat01
Kin : Cat02
Tom : Cat04
Fubuki : Fox01
Kuro : Fox02
Shiro : Fox03
```

Actual output:

```text
Cat : 3
Fox : 3
Garfield : Cat01
Kin : Cat02
Tom : Cat04
Fubuki : Fox01
Kuro : Fox02
Shiro : Fox03
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
มี Cat01 และ Fox01 อยู่แล้ว
```

Input:

```text
4
{"Garfield" : "Cat01"}
{"Fubuki" : "Fox01"}
{"Mimi" : "Cat03"}
{"Luna" : "Fox02"}
```

Expected output:

```text
Cat : 2
Fox : 2
Garfield : Cat01
Mimi : Cat03
Fubuki : Fox01
Luna : Fox02
```

Actual output:

```text
Cat : 2
Fox : 2
Garfield : Cat01
Mimi : Cat03
Fubuki : Fox01
Luna : Fox02
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
มีแต่ Cat และมีหมายเลขที่ไม่เรียงกัน
```

Input:

```text
3
{"Milo" : "Cat10"}
{"Nana" : "Cat03"}
{"Coco" : "Cat02"}
```

Expected output:

```text
Cat : 4
Fox : 1
Garfield : Cat01
Coco : Cat02
Nana : Cat03
Milo : Cat10
Fubuki : Fox01
```

Actual output:

```text
Cat : 4
Fox : 1
Garfield : Cat01
Coco : Cat02
Nana : Cat03
Milo : Cat10
Fubuki : Fox01
```

Result:

```text
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```text
No
```

If yes, also complete:

```text

```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
YES
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```text
เว็บต่างๆ
```

What did they help with?

```text
หาว่าผิดตรงไหน
```

What did you still do by yourself?

```text
แก้ไขจากโค้ดเดิม
```

Did you copy any code from another person?

```text
No
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
