# FastAPI-Study-Project
Учебный проект по курсу FastAPI - https://www.youtube.com/watch?v=0sOvCWFmrtA
### Section 1: Introduction
1. Course Project
2. Course Intro
3. Course Project Overview 
### Section 2: Setup & installation
4. Mac Python Installation 
5. Mac VS Code install and setup 
6. Windows Python Installation 
7. Windows VS Code install and setup  
8. Python virtual environment Basics 
9. Virtual environment on windows 
10. Virtual environment on Mac 
### Section 3: FastAPI
11. Install dependencies w/ pip 
12. Starting Fast API 
13. Path operations 
14. Path Operation Order(yes it matters) 
15. Intro to Postman 
16. HTTP Post Requests 
17. Schema Validation with Pydantic 
18. CRUD Operations 
19. storing posts in Array 
20. creating posts 
21. Postman Collections & saving requests 
22. Retrieve One Post 
23. Path order Matters 
24. Changing response Status Codes 
25. Deleting Posts 
26. Updating Posts 
27. Automatic Documentation 
28. Python packages 
### Section 4: Databases
29. Database Intro 
30. Postgres Windows Install 
31. Postgres Mac Install 
32. Database Schema & Tables 
33. Managing Postgres with PgAdmin GUI 
34. Your first SQL Query 
35. Filter results with "where" keyword 
36. SQL Operators 
37. IN Keyword 
38. Pattern matching with LIKE keyword 
39. Ordering Results 
40. LIMIT & OFFSET 
41. Inserting Data 
42. Deleting Data 
43. Updating Data 
### Section 5: Python + Raw SQL
44. Setup App Database 
45. Connecting to database w/ Python 
46. Retrieving Posts 
47. Creating Post 
48. Get One Post 
49. Delete Post 
50. Update Post 
### Section 6: ORMs
51. ORM intro 
52. SQLALCHEMY setup 
53. Adding CreatedAt Column 
54. Get All Posts 
55. Create Posts 
56. Get Post by ID 
57. Delete Post 
58. Update Post 
### Section 7: Pydantic Models
59. Pydantic vs ORM Models 
60. Pydantic Models Deep Dive 
61. Response Model 
### Section 8: Authentication & Users
62. Creating Users Table 
63. User Registration Path Operation 
64. Hashing User Passwords 
65. Refractor Hashing Logic 
66. Get User by ID 
67. FastAPI Routers 
68. Router Prefix 
69. Router Tags 
70. JWT Token Basics 
71. Login Process   
72. Creating a Token 
73. OAuth2 PasswordRequestForm 
74. Verify user is Logged In 
75. Fixing Bugs 
76. Protecting Routes 
77. Test Expired Token 
78. Fetching User in Protected Routes 
79. Postman advanced Features 
### Section 9: Relationships
80. SQL Relationship Basics 
81. Postgres Foreign Keys 
82. SQLAlchemy Foreign Keys 
83. Update Post Schema to include User 
84. Assigning Owner id when creating new post 
85. Delete and Update only your own posts 
86. Only Retrieving Logged in User's posts 
87. Sqlalchemy Relationships 
88. Query Parameters 
89. Cleanup our main.py file 
90. Environment Variables 
### Section 10: Vote/Like System
91. Vote/Like Theory 
92. Votes Table 
93. Votes Sqlalchemy 
94. Votes Route 
95. SQL Joins 
96. Joins in SqlAlchemy 
97. Get One Post with Joins 
### Section 11: Database Migration w/ Alembic
98. What is a database migration tool 
99. Alembic Setup 
100. Alembic First Revision 
101. Alembic Rollback database Schema 
102. Alembic finishing up the rest of the schema 
103. Disable SqlAlchemy create Engine 
### Section 12: Pre Deployment Checklist
104. What is CORS????? 
105. Git PreReqs 
106. Git Install 
107. Github 
### Section 13: Deployment Heroku
108. Heroku intro  
109. Create Heroku App 
110. Heroku procfile 
111. Adding a Postgres database 
112. Environment Variables in Heroku 
113. Alembic migrations on Heroku Postgres instance 
114. Pushing changed to production 
### Section 14: Deployment Ubuntu
115. Create an Ubuntu VM 
116. Update packages 
117. Install Python 
118. Install Postgres & setup password 
119. Postgres Config 
120. Create new user and setup python environment 
121. Environment Variables 
122. Alembic migrations on production database 
123. Gunicorn 
124. Creating a Systemd service 
125. NGINX 
126. Setting up Domain name 
127. SSL/HTTPS 
128. NGINX enable 
129. Firewall 
130. Pushing code changes to Production 
### Section 15: Docker
131. Dockerfile 
132. Docker Compose 
133. Postgres Container 
134. Bind Mounts 
135. Dockerhub 
136. Production vs Development 
### Section 16: Testing
137. Testing Intro 
138. Writing your first test 
139. The -s & -v flags 
140. Testing more functions 
141. Parametrize 
142. Testing Classes 
143. Fixtures 
144. Combining Fixtures + Parametrize 
145. Testing Exceptions 
146. FastAPI TestClient 
147. Pytest flags 
148. Test create user 
149. Setup testing database 
150. Create & destroy database after each test 
151. More Fixtures to handle database interaction 
152. Trailing slashes in path 
153. Fixture scope 
154. Test user fixture 
155. Test/validate token 
156. Conftest.py 
157. Failed login test 
158. Get all posts test 
159. Posts fixture to create test posts 
160. Unauthorized Get Posts test 
161. Get one post test 
162. Create post test 
163. Delete post test 
164. Update post 
165. Voting tests 
### Section 17: CI/CD pipeline
166. CI/CD intro 
167. Github Actions 
168. Creating Jobs 
169. Setup python/dependencies/pytest 
170. Environment variables 
171. Github Secrets 
172. Testing database 
173. Building Docker images 
174. Deploy to Heroku 
175. Failing tests in pipeline 
176. Deploy to Ubuntu
