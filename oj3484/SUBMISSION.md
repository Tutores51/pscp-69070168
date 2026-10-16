# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3484
```

OJ submission ID, if submitted:

```text
690417
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
กระเบื้องต้องการหุ่นยนต์ที่เคาะเสียงกระเบื้องเพื่อตรวจว่าปูได้ดีมั้ย กระเบื้อง 1 แผ่นจะเคาะ 5 จุด คือ กลางแผ่น มุมบนซ้าย มุมล่างซ้าย มุมบนขวา และมุมล่างขวา หุ่นยนต์จะบันทึกว่าในกระเบื้องแต่ละแผ่นบนพื้นขนาด N*N มีกี่จุดที่เสียงไม่สมบูรณ์
input บรรทัดที่ 1: จำนวนเต็ม N (1 ≤ N ≤ 50) คือขนาดพื้นที่ N*N และจำนวนจริง P (ไม่เกิน 500) คือค่าปรับต่อ 1 จุดที่เสียงไม่สมบูรณ์
อีก N บรรทัด: แต่ละบรรทัดมีจำนวนเต็ม N ตัว x (0 ≤ x ≤ 5) คือจำนวนจุดที่เสียงไม่สมบูรณ์ของกระเบื้องแต่ละแผ่น
output บรรทัดที่ 1 ถึง N: ข้อมูลของแถวนั้นตามเดิม ตามด้วยจำนวนกระเบื้องที่มีปัญหาในแถว และผลรวมจุดที่มีปัญหาในแถว
บรรทัดที่ N+1: จำนวนกระเบื้องที่มีปัญหาในแต่ละคอลัมน์
บรรทัดที่ N+2: ผลรวมจุดที่มีปัญหาในแต่ละคอลัมน์
บรรทัดที่ N+3: จำนวนกระเบื้องที่มีปัญหาทั้งหมด จำนวนจุดที่มีปัญหาทั้งหมด และค่าปรับทั้งหมด (ทศนิยม 2 ตำแหน่ง)
constraints ต้องพิมพ์ค่าปรับเป็นทศนิยม 2 ตำแหน่ง 
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
Step 1: รับค่า N (ขนาดพื้นที่) และ P (ค่าปรับต่อจุด)
Step 2: รับข้อมูลตาราง N แถว เก็บจำนวนจุดที่เสียงไม่สมบูรณ์ของกระเบื้องแต่ละแผ่น
Step 3: กำหนดตัวนับของแต่ละคอลัมน์ และตัวนับรวมทั้งหมด ให้เริ่มที่ 0
Step 4: วนทีละแถว นับจำนวนกระเบื้องที่ค่า > 0 และรวมจำนวนจุดของแถวนั้น
Step 5: เพิ่มค่าของแต่ละช่องเข้าตัวนับของคอลัมน์ที่ตรงกัน และเพิ่มผลของแถวเข้าตัวนับรวม
Step 6: แสดงข้อมูลของแถว ตามด้วยจำนวนกระเบื้องที่มีปัญหาและจำนวนจุดรวมของแถวนั้น
Step 7: แสดงจำนวนกระเบื้องที่มีปัญหาในแต่ละคอลัมน์ และจำนวนจุดรวมของแต่ละคอลัมน์
Step 8: คำนวณค่าปรับ = จำนวนจุดรวมทั้งหมด × P
Step 9: แสดงจำนวนกระเบื้องที่มีปัญหาทั้งหมด จำนวนจุดรวมทั้งหมด และค่าปรับทศนิยม 2 ตำแหน่ง
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
ไม่มีกระเบื้องที่มีปัญหาเลย
```

Input:

```text
3 100
0 0 0
0 0 0
0 0 0
```

Expected output:

```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0
0 0 0
0 0 0.00
```

Actual output:

```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0
0 0 0
0 0 0.00
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
เป็นทศนิยม
```

Input:

```text
1 12.5
3
```

Expected output:

```text
3 1 3
1
3
1 3 37.50
```

Actual output:

```text
3 1 3
1
3
1 3 37.50
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
มีแถวและคอลัมน์ที่ว่างเปล่าปนอยู่
```

Input:

```text
3 7.5
1 0 2
0 0 0
5 3 0
```

Expected output:

```text
1 0 2 2 3
0 0 0 0 0
5 3 0 2 8
2 1 1
6 3 2
4 11 82.50
```

Actual output:

```text
1 0 2 2 3
0 0 0 0 0
5 3 0 2 8
2 1 1
6 3 2
4 11 82.50
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
