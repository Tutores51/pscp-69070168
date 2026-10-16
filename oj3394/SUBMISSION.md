# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3394
```

OJ submission ID, if submitted:

```text
675817
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
ให้นักเรียนจำนวน N คน โดยนักเรียนแต่ละคนจะส่งต่อข้อความให้กับนักเรียนอีกคนหนึ่งตามหมายเลขที่กำหนด หรือไม่ส่งต่อเลยก็ได้ เราต้องหาว่าเมื่อส่งข้อความให้นักเรียนคนที่ S เป็นคนแรก จะมีนักเรียนทั้งหมดกี่คนที่ได้รับข้อความ โดยไม่นับนักเรียนคนเดิมซ้ำ แม้ว่าข้อความจะถูกส่งวนกลับมาหานักเรียนคนนั้นอีกครั้ง
input บรรทัดแรกประกอบด้วยจำนวนเต็มสองจำนวน N และ S คือจำนวนนักเรียนทั้งหมด และ หมายเลขนักเรียนที่ได้รับข้อความเป็นคนแรก อีก N บรรทัดถัดมา แต่ละบรรทัดระบุหมายเลขนักเรียนที่นักเรียนคนนั้นจะส่งข้อความต่อให้
output แสดงจำนวนรวมของนักเรียนที่ได้รับข้อความทั้งหมด โดยนับนักเรียนแต่ละคนเพียงครั้งเดียว
constraints ไม่มีนักเรียนคนใดส่งข้อความให้ตัวเองโดยตรง
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
รับจำนวนนักเรียน student_count และหมายเลขนักเรียนเริ่มต้น start_student
รับข้อมูลการส่งต่อข้อความของนักเรียนแต่ละคน แล้วเก็บไว้ใน List forward_to
สร้าง List visited_students เพื่อเก็บหมายเลขนักเรียนที่ได้รับข้อความแล้ว
กำหนด current_student ให้เป็นนักเรียนคนแรกที่ได้รับข้อความ
ใช้ while current_student วนลูปตราบใดที่หมายเลขนักเรียนไม่ใช่ 0
ตรวจสอบว่านักเรียนคนปัจจุบันเคยได้รับข้อความแล้วหรือไม่ หากเคยแล้วให้หยุดลูปด้วย break
หากยังไม่เคยได้รับข้อความ ให้เพิ่มหมายเลขนักเรียนลงใน visited_students
ค้นหาหมายเลขนักเรียนคนถัดไปจาก forward_to โดยใช้ current_student - 1 เพราะ Index ของ List เริ่มจาก 0
ทำซ้ำจนกว่าจะถึง 0 หรือพบหมายเลขนักเรียนที่เคยได้รับข้อความแล้ว
แสดงจำนวนสมาชิกใน visited_students ซึ่งเป็นจำนวนนักเรียนที่ได้รับข้อความทั้งหมดโดยไม่นับซ้ำ
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
ส่งต่อข้อความตามปกติ
```

Input:

```text
3 1
2
3
0
```

Expected output:

```text
3
```

Actual output:

```text
3
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
วนกลับมาคนเดิม
```

Input:

```text
5 1
2
3
1
0
3
```

Expected output:

```text
3
```

Actual output:

```text
3
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
ไม่ส่งต่อข้อความ
```

Input:

```text
4 4
2
3
1
0
```

Expected output:

```text
1
```

Actual output:

```text
1
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
