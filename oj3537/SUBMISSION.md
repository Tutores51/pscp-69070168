# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3537
```

OJ submission ID, if submitted:

```text
695656
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
0-15 minutes
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
มีคนกลุ่มหนึ่งอยู่ในยานอวกาศ ในกลุ่มมีทั้งเพื่อนร่วมทีม (Crewmate) และผู้แอบอ้างแฝงตัวเข้ามา (Impostor) ทุกคนโหวตไล่คนออกจากยาน งานของเราคือรับรายชื่อพร้อมบทบาทของทุกคน แล้วรับรายชื่อคนที่ถูกโหวตไล่ออก จากนั้นสรุปว่าใครยังอยู่ ใครถูกไล่ออกไปแล้ว และเหลือ Impostor อยู่กี่คน โดยใช้ dict

Input
เป็น dict ที่มีชื่อและบทบาท เช่น {"Green" : "Crewmate"} อ่านไปเรื่อย ๆ จนเจอคำว่า Start
เป็นชื่อคนที่ถูกโหวตไล่ออก เช่น Green อ่านไปเรื่อย ๆ จนเจอคำว่า End

Output
บรรทัดแรก: จำนวน Impostor ที่ยังอยู่ ตามด้วย Impostor Remains เช่น 2 Impostor Remains
***Alive*** ตามด้วยบรรทัดของผู้ที่ยังอยู่ ในรูปแบบ ชื่อ : บทบาท
***Dead*** ตามด้วยบรรทัดของผู้ที่ถูกไล่ออก ในรูปแบบ ชื่อ : บทบาท
ชื่อในแต่ละกลุ่มเรียงตามตัวอักษร
Constraints
ชื่อในแต่ละกลุ่มต้องเรียงตามตัวอักษร
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
Step 1: สร้าง dict ว่าง alive_roles เก็บ ชื่อ -> บทบาท ของคนที่ยังอยู่
Step 2: วนรับ input ทีละบรรทัด จนกว่าจะเจอคำว่า Start
Step 3: แปลงแต่ละบรรทัดที่เป็นรูปแบบ {"ชื่อ" : "บทบาท"} ให้เป็น dict แล้วใช้ update() รวมเข้า alive_roles
Step 4: สร้าง dict ว่าง dead_roles เก็บคนที่ถูกไล่ออก
Step 5: วนรับชื่อคนที่ถูกโหวตทีละบรรทัด จนกว่าจะเจอคำว่า End
Step 6: ถ้าชื่อนั้นอยู่ใน alive_roles ให้ใช้ pop() ดึงออก แล้วเก็บลง dead_roles พร้อมบทบาท
Step 7: นับ Impostor ที่เหลือใน alive_roles จาก values()
Step 8: พิมพ์ จำนวน Impostor ตามด้วย Impostor Remains
Step 9: พิมพ์ ***Alive*** แล้ววนชื่อใน alive_roles ตามลำดับตัวอักษร พิมพ์ ชื่อ : บทบาท
Step 10: พิมพ์ ***Dead*** แล้ววนชื่อใน dead_roles ตามลำดับตัวอักษร พิมพ์ ชื่อ : บทบาท
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
same because it work
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
Impostor ถูกไล่ออกหมด
```

Input:

```text
{"Red" : "Crewmate"}
{"Blue" : "Impostor"}
{"Pink" : "Impostor"}
Start
Blue
Pink
End
```

Expected output:

```text
0 Impostor Remains
***Alive***
Red : Crewmate
***Dead***
Blue : Impostor
Pink : Impostor
```

Actual output:

```text
0 Impostor Remains
***Alive***
Red : Crewmate
***Dead***
Blue : Impostor
Pink : Impostor
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
ไม่มีใครถูกโหวตไล่ออกเลย
```

Input:

```text
{"Lime" : "Impostor"}
{"Cyan" : "Crewmate"}
{"Orange" : "Crewmate"}
Start
End
```

Expected output:

```text
1 Impostor Remains
***Alive***
Cyan : Crewmate
Lime : Impostor
Orange : Crewmate
***Dead***
```

Actual output:

```text
1 Impostor Remains
***Alive***
Cyan : Crewmate
Lime : Impostor
Orange : Crewmate
***Dead***
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
ทุกคนถูกไล่ออกหมด
```

Input:

```text
{"White" : "Crewmate"}
{"Green" : "Impostor"}
{"Black" : "Crewmate"}
Start
White
Green
Black
End
```

Expected output:

```text
0 Impostor Remains
***Alive***
***Dead***
Black : Crewmate
Green : Impostor
White : Crewmate
```

Actual output:

```text
0 Impostor Remains
***Alive***
***Dead***
Black : Crewmate
Green : Impostor
White : Crewmate
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
No
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

```

What did they help with?

```text

```

What did you still do by yourself?

```text

```

Did you copy any code from another person?

```text

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
