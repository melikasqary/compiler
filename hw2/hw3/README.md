Take the text input and recognize and display the national number, email, postal code, decimal number, software version, website address.


this is out put of my code in python
[7:02:56 PM] [1] URL Found ==>  www.goog.com                          hw3.py:85
[7:02:56 PM] [2] URL Found ==>  google.com                            hw3.py:85
[7:02:56 PM] [3] URL Found ==>  google.ur.ac.ir/sub/sad               hw3.py:85
[7:02:56 PM] [4] URL Found ==>  http://www.google.com                 hw3.py:85
[7:02:56 PM] [5] National Code Found ==>  0109458265                  hw3.py:40
[7:02:56 PM] [6] National Code Found ==>  5413484917                  hw3.py:40
[7:02:56 PM] [7] Email Found ==>  asd@gmail.com                       hw3.py:72
[7:02:56 PM] [8] Postal Code Found ==>  4146964578                    hw3.py:66
[7:02:56 PM] [9] Postal Code Found ==>  5648818547                    hw3.py:66
[7:02:57 PM] [10] Email Found ==>  wqed@fgf.csasd                     hw3.py:72


┌─────────────────────────────────────────────────────────────────────────────┐
│                               Text Recognizer                               │
│ ┌─────────────┬──────────────────────┬───────────┬─────────────┬──────────┐ │
│ │   Emails    │         URLs         │ Postal C… │ National C… │ APP_VER… │ │
│ ├─────────────┼──────────────────────┼───────────┼─────────────┼──────────┤ │
│ │             │     www.goog.com     │           │             │          │ │
│ │             │      google.com      │           │             │          │ │
│ │             │ google.ur.ac.ir/sub… │           │             │          │ │
│ │             │ http://www.google.c… │           │             │          │ │
│ │             │                      │           │ 0109458265  │          │ │
│ │             │                      │           │ 5413484917  │          │ │
│ │ asd@gmail.… │                      │           │             │          │ │
│ │             │                      │ 41469645… │             │          │ │
│ │             │                      │ 56488185… │             │          │ │
│ │ wqed@fgf.c… │                      │           │             │          │ │
│ │             │                      │           │             │  1.2.4   │ │
│ └─────────────┴──────────────────────┴───────────┴─────────────┴──────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘


Input
├── Emails
│   ├── asd@gmail.com
│   └── wqed@fgf.csasd
├── URLs
│   ├── www.goog.com
│   ├── google.com
│   ├── google.ur.ac.ir/sub/sad
│   └── http://www.google.com
├── Postal Codes
│   ├── 4146964578
│   └── 5648818547
├── National Codes
│   ├── 0109458265
│   └── 5413484917
└── APP_VERSION
    └── 1.2.4
