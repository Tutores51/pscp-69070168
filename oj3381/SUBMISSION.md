# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3381
```

OJ submission ID, if submitted:

```text
675807
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
15-30 minutes
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
ต้องการเรียงจุดเหล่านี้ตามค่าจากฟังก์ชัน f ที่นิยามว่า f(x,y) = x + y จากน้อยไปมาก ถ้ามีจุดที่มีค่าฟังก์ชัน f เท่ากัน ให้เรียงโดยให้จุดที่มีค่าพิกัดบนแกน y มากกว่ามาก่อน
input ระบุจำนวนเต็ม T (1 <= T <= 5) แทนจำนวนชุดข้อมูลทดสอบ จากนั้นจะมีข้อมูลทดสอบ T ชุดตามลำดับ
output แต่ละชุดข้อมูลทดสอบให้พิมพ์จุดที่เรียงแล้วตามลำดับที่ระบุในโจทย์
constraints ไม่มีคู่ของจุดใด ๆ ที่อยู่ที่ตำแหน่งเดียวกัน
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
รับค่า test_case_count เพื่อเก็บจำนวนชุดข้อมูลทดสอบ
วนทำงานตามจำนวนชุดข้อมูลทดสอบ โดยรับค่า point_count ซึ่งเป็นจำนวนจุดในแต่ละชุด
สร้างลิสต์ points เพื่อเก็บพิกัด (x, y) ของจุดทั้งหมด
รับพิกัดแกน x และแกน y ของแต่ละจุด แล้วเก็บลงในลิสต์
ใช้ลูปซ้อนเพื่อตรวจสอบและเปรียบเทียบจุดแต่ละคู่ โดยคำนวณผลบวก x + y ของแต่ละจุด
หากผลบวกของจุดแรกมากกว่าจุดที่สอง ให้สลับตำแหน่งของจุดทั้งสอง เพื่อให้เรียงผลบวกจากน้อยไปมาก
หากผลบวกเท่ากัน ให้สลับตำแหน่งเมื่อจุดแรกมีค่า y น้อยกว่าจุดที่สอง เพื่อให้จุดที่มีค่า y มากกว่าอยู่ก่อน
ทำซ้ำจนตรวจสอบและจัดเรียงจุดทั้งหมดเสร็จ
แสดงผล
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
same because it working...
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
จากน้อยไปมาก
```

Input:

```text
1
3
1 2
0 1
2 3
```

Expected output:

```text
0 1
1 2
2 3
```

Actual output:

```text
0 1
1 2
2 3
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
จากมากไปน้อย
```

Input:

```text
1
3
1 2
2 1
0 3
```

Expected output:

```text
0 3
1 2
2 1
```

Actual output:

```text
0 3
1 2
2 1
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
ตามลำดับหลัง
```

Input:

```text
1
4
-2 1
1 -3
0 0
-1 2
```

Expected output:

```text
1 -3
-2 1
0 0
-1 2
```

Actual output:

```text
1 -3
-2 1
0 0
-1 2
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
