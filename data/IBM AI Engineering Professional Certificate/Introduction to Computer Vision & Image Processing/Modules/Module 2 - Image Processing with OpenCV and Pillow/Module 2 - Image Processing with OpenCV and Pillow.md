

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DRSQNYS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCt40SFa5%2B7%2FVIv8GG2f4WD2Xd4RQTRrMP5TqJn533CRAIgGOZ9drcd%2BKWRM5c%2BdvbliCpWAqnyjzwiuyq2g%2FTQp%2B4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQrpvSi0JIl%2BaY5kircAxZmhuBKHaAHIddT75KZy%2BHa01VJYfWlo2THklO%2F2G%2BJEJEc%2FROcA5L8w7szjeyGST9TIBVwL43MsoGeYp%2BLERJ5gCJc743xHT7GhdTTZCv93acSWTWCxdWi4tJY4zPd8xacqjvu87u1xJkjlgeoIHlJ%2BxE1n8cxD4KvsZN8C5RplrplM0l4WTqBVw%2Bp09%2FNHi%2FAMShvFx%2B2r9uMGSAie5ISO4pgf3PcPn%2F%2B0wAp7IPst%2Bl8MDwNI3s41MHO%2Fz4Y8sYtJvVcjsoSSvWAGuM%2B98J124jlWbqpUktbRybJLGrZ7tEJj0GajABnf%2BO%2FeUtbOQ9%2BsS5zvEh%2FbYmBd1kG5fjAM4mYPhoP1B%2BArpJrG51kIirp%2BwF5q1f6PyfOXfItAIo4jGyIVmGfwQf%2F2anc2L8O6gnO%2F0w9qhQlEm%2FKNP8fos%2F3aLm7wuvztuh3Vb77TUwZEZRq9ssGvppJXS4VpLWo5mhHHSH8EYdi7u133nWh9OHH0CFD833HFjL6oXGdmFlNp3WzRbXiqVj2blCcbIkje%2BWg1Uu2TGAUIz%2Bgw3jTnyrAExa1o3duTbJDSjBvbogspsyjx5eAItBeVDkL36BXGzft%2FQGHratGm5X8BTUHeu%2B8rUv4rCkC4mNMMIaWm70GOqUBxVu9J9SUVH3SeErQJKIlJamwVOM2OcS26WDc2sgnTnAHAUX84xXAnEXJWM2rN0jtCbrobR1dZIMjT9QeAJ1bAsIfgHZD3f7oWqfim1umUd5f59Qyj%2BXbzJL2%2F00Y6LXUd25DEG9Qwfldxe7TqoLXurAZ7hSPhMy8T%2B4Yo1Idf%2FF3e%2FJFxPKC8lHbPiUtHjT2h%2F8hoiSWxiTYI50LrC9CfXDEgJCL&X-Amz-Signature=27c8e16b34f8f4b40ee0beecb404eeee0714fa27372ad2a1166ac3acabb89e9a&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4VLBLE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGxf9MQ7yrKLiqrvu4wI%2F1G4MXd%2Fg1O7PQH1eYKJbpCoAiBG9mLk3xmHFu6b0cT%2F5JdKngIttDRoZx3jQGdN99GV5SqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrT%2FX%2FWrSk%2FIRdBGKtwDctoRxINdmT%2BLJcq940bVAMJmO8giAQDz%2FPJS%2F6eIvRzk3Zqa%2B2hm3ijgCz9rc7fH1g33qHmwOjoEhNozU9GX5yiE1s0DwPs87%2F4fWhcXtaJ4pYUP9vJDG9UrjdNIclfIrtdF59fM%2ByuM1m67Dq10TYGqDHje2LxnoVAJEhION6KbvPHYhqtChii4d0nq%2FNm6R9Yi%2FrKnOeGczKyqA1zkIgPdqAJSnnZi1j0iuu2onU%2Fdr8lfxHg5hn2Y3K9ibvY%2FIHlV2hEMc6QcggJAuKiPzHURgJPuQ06P8YHBW1aODzgrn6lQkmoY5rHfqLeAsF1ZSqimDlDA9BCMipNglSOcEPLGC918UWBUzSf%2FTBlCQyk17ldle11IRQYBLpQkLpGT7v83bulH%2B1FkWISSafdebH%2FAJgY04JXFlCPj%2FfX8XGTqEOGbcZSL1%2Fqz3a8giHC4snNlIMRNswTmLP%2BesmmWiUY23acJUXjklCPHY7Adr9OVh6EoBaBASkMiV%2BGZNSKhwFCSezJhJrpThJLt%2B9F2AuyOheZx%2BV9iXh%2B1%2BlTLUovMSiQL4NWQ6nzABVQWRcjM9fzkwebA0%2FDHgPCgYtK5jZl9pOUJrhVWP5uFAqdexlVsiVusyXXU%2FYaQQyQw8ZWbvQY6pgFcl1hUA3lNzcX5mKALCeVjHqLxmpAL0ZHNJnYYS8iYirTR90F85OdJu3dt8usxu1bjzrSGkZNx32Zc%2FaeF2V2d%2FV2koT7hlH5IHDN%2Bcwmw0h2vFqtnQMzSnFLq5PrvupeihZgJbPJgBGnOSX01KZeL9hy%2BimlQP0d8kLpLV9Z5DNI7L7WXyFUFwRWJvw%2BwLqjzCU2bPTTGmF5Pzo0UKbTVbKM8%2B9Yj&X-Amz-Signature=bd225a28a5758725877279015001b0d2a07013b463a8a650f922ab8447d6c0e7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4VLBLE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGxf9MQ7yrKLiqrvu4wI%2F1G4MXd%2Fg1O7PQH1eYKJbpCoAiBG9mLk3xmHFu6b0cT%2F5JdKngIttDRoZx3jQGdN99GV5SqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrT%2FX%2FWrSk%2FIRdBGKtwDctoRxINdmT%2BLJcq940bVAMJmO8giAQDz%2FPJS%2F6eIvRzk3Zqa%2B2hm3ijgCz9rc7fH1g33qHmwOjoEhNozU9GX5yiE1s0DwPs87%2F4fWhcXtaJ4pYUP9vJDG9UrjdNIclfIrtdF59fM%2ByuM1m67Dq10TYGqDHje2LxnoVAJEhION6KbvPHYhqtChii4d0nq%2FNm6R9Yi%2FrKnOeGczKyqA1zkIgPdqAJSnnZi1j0iuu2onU%2Fdr8lfxHg5hn2Y3K9ibvY%2FIHlV2hEMc6QcggJAuKiPzHURgJPuQ06P8YHBW1aODzgrn6lQkmoY5rHfqLeAsF1ZSqimDlDA9BCMipNglSOcEPLGC918UWBUzSf%2FTBlCQyk17ldle11IRQYBLpQkLpGT7v83bulH%2B1FkWISSafdebH%2FAJgY04JXFlCPj%2FfX8XGTqEOGbcZSL1%2Fqz3a8giHC4snNlIMRNswTmLP%2BesmmWiUY23acJUXjklCPHY7Adr9OVh6EoBaBASkMiV%2BGZNSKhwFCSezJhJrpThJLt%2B9F2AuyOheZx%2BV9iXh%2B1%2BlTLUovMSiQL4NWQ6nzABVQWRcjM9fzkwebA0%2FDHgPCgYtK5jZl9pOUJrhVWP5uFAqdexlVsiVusyXXU%2FYaQQyQw8ZWbvQY6pgFcl1hUA3lNzcX5mKALCeVjHqLxmpAL0ZHNJnYYS8iYirTR90F85OdJu3dt8usxu1bjzrSGkZNx32Zc%2FaeF2V2d%2FV2koT7hlH5IHDN%2Bcwmw0h2vFqtnQMzSnFLq5PrvupeihZgJbPJgBGnOSX01KZeL9hy%2BimlQP0d8kLpLV9Z5DNI7L7WXyFUFwRWJvw%2BwLqjzCU2bPTTGmF5Pzo0UKbTVbKM8%2B9Yj&X-Amz-Signature=83dc2cd03ed454a0ddd927c6856d991156ceb960fb419086902c2c1f023317f0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4VLBLE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGxf9MQ7yrKLiqrvu4wI%2F1G4MXd%2Fg1O7PQH1eYKJbpCoAiBG9mLk3xmHFu6b0cT%2F5JdKngIttDRoZx3jQGdN99GV5SqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrT%2FX%2FWrSk%2FIRdBGKtwDctoRxINdmT%2BLJcq940bVAMJmO8giAQDz%2FPJS%2F6eIvRzk3Zqa%2B2hm3ijgCz9rc7fH1g33qHmwOjoEhNozU9GX5yiE1s0DwPs87%2F4fWhcXtaJ4pYUP9vJDG9UrjdNIclfIrtdF59fM%2ByuM1m67Dq10TYGqDHje2LxnoVAJEhION6KbvPHYhqtChii4d0nq%2FNm6R9Yi%2FrKnOeGczKyqA1zkIgPdqAJSnnZi1j0iuu2onU%2Fdr8lfxHg5hn2Y3K9ibvY%2FIHlV2hEMc6QcggJAuKiPzHURgJPuQ06P8YHBW1aODzgrn6lQkmoY5rHfqLeAsF1ZSqimDlDA9BCMipNglSOcEPLGC918UWBUzSf%2FTBlCQyk17ldle11IRQYBLpQkLpGT7v83bulH%2B1FkWISSafdebH%2FAJgY04JXFlCPj%2FfX8XGTqEOGbcZSL1%2Fqz3a8giHC4snNlIMRNswTmLP%2BesmmWiUY23acJUXjklCPHY7Adr9OVh6EoBaBASkMiV%2BGZNSKhwFCSezJhJrpThJLt%2B9F2AuyOheZx%2BV9iXh%2B1%2BlTLUovMSiQL4NWQ6nzABVQWRcjM9fzkwebA0%2FDHgPCgYtK5jZl9pOUJrhVWP5uFAqdexlVsiVusyXXU%2FYaQQyQw8ZWbvQY6pgFcl1hUA3lNzcX5mKALCeVjHqLxmpAL0ZHNJnYYS8iYirTR90F85OdJu3dt8usxu1bjzrSGkZNx32Zc%2FaeF2V2d%2FV2koT7hlH5IHDN%2Bcwmw0h2vFqtnQMzSnFLq5PrvupeihZgJbPJgBGnOSX01KZeL9hy%2BimlQP0d8kLpLV9Z5DNI7L7WXyFUFwRWJvw%2BwLqjzCU2bPTTGmF5Pzo0UKbTVbKM8%2B9Yj&X-Amz-Signature=21fb25ead1248b1c5e8fa1e945d6f5ec5eea69043cb930a490c06f9faaf4960f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4VLBLE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGxf9MQ7yrKLiqrvu4wI%2F1G4MXd%2Fg1O7PQH1eYKJbpCoAiBG9mLk3xmHFu6b0cT%2F5JdKngIttDRoZx3jQGdN99GV5SqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrT%2FX%2FWrSk%2FIRdBGKtwDctoRxINdmT%2BLJcq940bVAMJmO8giAQDz%2FPJS%2F6eIvRzk3Zqa%2B2hm3ijgCz9rc7fH1g33qHmwOjoEhNozU9GX5yiE1s0DwPs87%2F4fWhcXtaJ4pYUP9vJDG9UrjdNIclfIrtdF59fM%2ByuM1m67Dq10TYGqDHje2LxnoVAJEhION6KbvPHYhqtChii4d0nq%2FNm6R9Yi%2FrKnOeGczKyqA1zkIgPdqAJSnnZi1j0iuu2onU%2Fdr8lfxHg5hn2Y3K9ibvY%2FIHlV2hEMc6QcggJAuKiPzHURgJPuQ06P8YHBW1aODzgrn6lQkmoY5rHfqLeAsF1ZSqimDlDA9BCMipNglSOcEPLGC918UWBUzSf%2FTBlCQyk17ldle11IRQYBLpQkLpGT7v83bulH%2B1FkWISSafdebH%2FAJgY04JXFlCPj%2FfX8XGTqEOGbcZSL1%2Fqz3a8giHC4snNlIMRNswTmLP%2BesmmWiUY23acJUXjklCPHY7Adr9OVh6EoBaBASkMiV%2BGZNSKhwFCSezJhJrpThJLt%2B9F2AuyOheZx%2BV9iXh%2B1%2BlTLUovMSiQL4NWQ6nzABVQWRcjM9fzkwebA0%2FDHgPCgYtK5jZl9pOUJrhVWP5uFAqdexlVsiVusyXXU%2FYaQQyQw8ZWbvQY6pgFcl1hUA3lNzcX5mKALCeVjHqLxmpAL0ZHNJnYYS8iYirTR90F85OdJu3dt8usxu1bjzrSGkZNx32Zc%2FaeF2V2d%2FV2koT7hlH5IHDN%2Bcwmw0h2vFqtnQMzSnFLq5PrvupeihZgJbPJgBGnOSX01KZeL9hy%2BimlQP0d8kLpLV9Z5DNI7L7WXyFUFwRWJvw%2BwLqjzCU2bPTTGmF5Pzo0UKbTVbKM8%2B9Yj&X-Amz-Signature=7967b133890f019bb81b88f1d5a20b6eccff243fb422f4ac7b7265b34891f371&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4VLBLE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGxf9MQ7yrKLiqrvu4wI%2F1G4MXd%2Fg1O7PQH1eYKJbpCoAiBG9mLk3xmHFu6b0cT%2F5JdKngIttDRoZx3jQGdN99GV5SqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrT%2FX%2FWrSk%2FIRdBGKtwDctoRxINdmT%2BLJcq940bVAMJmO8giAQDz%2FPJS%2F6eIvRzk3Zqa%2B2hm3ijgCz9rc7fH1g33qHmwOjoEhNozU9GX5yiE1s0DwPs87%2F4fWhcXtaJ4pYUP9vJDG9UrjdNIclfIrtdF59fM%2ByuM1m67Dq10TYGqDHje2LxnoVAJEhION6KbvPHYhqtChii4d0nq%2FNm6R9Yi%2FrKnOeGczKyqA1zkIgPdqAJSnnZi1j0iuu2onU%2Fdr8lfxHg5hn2Y3K9ibvY%2FIHlV2hEMc6QcggJAuKiPzHURgJPuQ06P8YHBW1aODzgrn6lQkmoY5rHfqLeAsF1ZSqimDlDA9BCMipNglSOcEPLGC918UWBUzSf%2FTBlCQyk17ldle11IRQYBLpQkLpGT7v83bulH%2B1FkWISSafdebH%2FAJgY04JXFlCPj%2FfX8XGTqEOGbcZSL1%2Fqz3a8giHC4snNlIMRNswTmLP%2BesmmWiUY23acJUXjklCPHY7Adr9OVh6EoBaBASkMiV%2BGZNSKhwFCSezJhJrpThJLt%2B9F2AuyOheZx%2BV9iXh%2B1%2BlTLUovMSiQL4NWQ6nzABVQWRcjM9fzkwebA0%2FDHgPCgYtK5jZl9pOUJrhVWP5uFAqdexlVsiVusyXXU%2FYaQQyQw8ZWbvQY6pgFcl1hUA3lNzcX5mKALCeVjHqLxmpAL0ZHNJnYYS8iYirTR90F85OdJu3dt8usxu1bjzrSGkZNx32Zc%2FaeF2V2d%2FV2koT7hlH5IHDN%2Bcwmw0h2vFqtnQMzSnFLq5PrvupeihZgJbPJgBGnOSX01KZeL9hy%2BimlQP0d8kLpLV9Z5DNI7L7WXyFUFwRWJvw%2BwLqjzCU2bPTTGmF5Pzo0UKbTVbKM8%2B9Yj&X-Amz-Signature=b220819fb40d22654d4c0464043b7b4c037a1dd81619389293e2902d7c97bc2e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DRSQNYS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCt40SFa5%2B7%2FVIv8GG2f4WD2Xd4RQTRrMP5TqJn533CRAIgGOZ9drcd%2BKWRM5c%2BdvbliCpWAqnyjzwiuyq2g%2FTQp%2B4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQrpvSi0JIl%2BaY5kircAxZmhuBKHaAHIddT75KZy%2BHa01VJYfWlo2THklO%2F2G%2BJEJEc%2FROcA5L8w7szjeyGST9TIBVwL43MsoGeYp%2BLERJ5gCJc743xHT7GhdTTZCv93acSWTWCxdWi4tJY4zPd8xacqjvu87u1xJkjlgeoIHlJ%2BxE1n8cxD4KvsZN8C5RplrplM0l4WTqBVw%2Bp09%2FNHi%2FAMShvFx%2B2r9uMGSAie5ISO4pgf3PcPn%2F%2B0wAp7IPst%2Bl8MDwNI3s41MHO%2Fz4Y8sYtJvVcjsoSSvWAGuM%2B98J124jlWbqpUktbRybJLGrZ7tEJj0GajABnf%2BO%2FeUtbOQ9%2BsS5zvEh%2FbYmBd1kG5fjAM4mYPhoP1B%2BArpJrG51kIirp%2BwF5q1f6PyfOXfItAIo4jGyIVmGfwQf%2F2anc2L8O6gnO%2F0w9qhQlEm%2FKNP8fos%2F3aLm7wuvztuh3Vb77TUwZEZRq9ssGvppJXS4VpLWo5mhHHSH8EYdi7u133nWh9OHH0CFD833HFjL6oXGdmFlNp3WzRbXiqVj2blCcbIkje%2BWg1Uu2TGAUIz%2Bgw3jTnyrAExa1o3duTbJDSjBvbogspsyjx5eAItBeVDkL36BXGzft%2FQGHratGm5X8BTUHeu%2B8rUv4rCkC4mNMMIaWm70GOqUBxVu9J9SUVH3SeErQJKIlJamwVOM2OcS26WDc2sgnTnAHAUX84xXAnEXJWM2rN0jtCbrobR1dZIMjT9QeAJ1bAsIfgHZD3f7oWqfim1umUd5f59Qyj%2BXbzJL2%2F00Y6LXUd25DEG9Qwfldxe7TqoLXurAZ7hSPhMy8T%2B4Yo1Idf%2FF3e%2FJFxPKC8lHbPiUtHjT2h%2F8hoiSWxiTYI50LrC9CfXDEgJCL&X-Amz-Signature=7b6e2ff532f510c2880bd301ce770f303c897c711b380d5e90cd5ea070325247&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DRSQNYS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCt40SFa5%2B7%2FVIv8GG2f4WD2Xd4RQTRrMP5TqJn533CRAIgGOZ9drcd%2BKWRM5c%2BdvbliCpWAqnyjzwiuyq2g%2FTQp%2B4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQrpvSi0JIl%2BaY5kircAxZmhuBKHaAHIddT75KZy%2BHa01VJYfWlo2THklO%2F2G%2BJEJEc%2FROcA5L8w7szjeyGST9TIBVwL43MsoGeYp%2BLERJ5gCJc743xHT7GhdTTZCv93acSWTWCxdWi4tJY4zPd8xacqjvu87u1xJkjlgeoIHlJ%2BxE1n8cxD4KvsZN8C5RplrplM0l4WTqBVw%2Bp09%2FNHi%2FAMShvFx%2B2r9uMGSAie5ISO4pgf3PcPn%2F%2B0wAp7IPst%2Bl8MDwNI3s41MHO%2Fz4Y8sYtJvVcjsoSSvWAGuM%2B98J124jlWbqpUktbRybJLGrZ7tEJj0GajABnf%2BO%2FeUtbOQ9%2BsS5zvEh%2FbYmBd1kG5fjAM4mYPhoP1B%2BArpJrG51kIirp%2BwF5q1f6PyfOXfItAIo4jGyIVmGfwQf%2F2anc2L8O6gnO%2F0w9qhQlEm%2FKNP8fos%2F3aLm7wuvztuh3Vb77TUwZEZRq9ssGvppJXS4VpLWo5mhHHSH8EYdi7u133nWh9OHH0CFD833HFjL6oXGdmFlNp3WzRbXiqVj2blCcbIkje%2BWg1Uu2TGAUIz%2Bgw3jTnyrAExa1o3duTbJDSjBvbogspsyjx5eAItBeVDkL36BXGzft%2FQGHratGm5X8BTUHeu%2B8rUv4rCkC4mNMMIaWm70GOqUBxVu9J9SUVH3SeErQJKIlJamwVOM2OcS26WDc2sgnTnAHAUX84xXAnEXJWM2rN0jtCbrobR1dZIMjT9QeAJ1bAsIfgHZD3f7oWqfim1umUd5f59Qyj%2BXbzJL2%2F00Y6LXUd25DEG9Qwfldxe7TqoLXurAZ7hSPhMy8T%2B4Yo1Idf%2FF3e%2FJFxPKC8lHbPiUtHjT2h%2F8hoiSWxiTYI50LrC9CfXDEgJCL&X-Amz-Signature=ed324dc76578c38aa88b16223410f50822fc415a471a0f3612d676c6dbcc1027&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DRSQNYS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCt40SFa5%2B7%2FVIv8GG2f4WD2Xd4RQTRrMP5TqJn533CRAIgGOZ9drcd%2BKWRM5c%2BdvbliCpWAqnyjzwiuyq2g%2FTQp%2B4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQrpvSi0JIl%2BaY5kircAxZmhuBKHaAHIddT75KZy%2BHa01VJYfWlo2THklO%2F2G%2BJEJEc%2FROcA5L8w7szjeyGST9TIBVwL43MsoGeYp%2BLERJ5gCJc743xHT7GhdTTZCv93acSWTWCxdWi4tJY4zPd8xacqjvu87u1xJkjlgeoIHlJ%2BxE1n8cxD4KvsZN8C5RplrplM0l4WTqBVw%2Bp09%2FNHi%2FAMShvFx%2B2r9uMGSAie5ISO4pgf3PcPn%2F%2B0wAp7IPst%2Bl8MDwNI3s41MHO%2Fz4Y8sYtJvVcjsoSSvWAGuM%2B98J124jlWbqpUktbRybJLGrZ7tEJj0GajABnf%2BO%2FeUtbOQ9%2BsS5zvEh%2FbYmBd1kG5fjAM4mYPhoP1B%2BArpJrG51kIirp%2BwF5q1f6PyfOXfItAIo4jGyIVmGfwQf%2F2anc2L8O6gnO%2F0w9qhQlEm%2FKNP8fos%2F3aLm7wuvztuh3Vb77TUwZEZRq9ssGvppJXS4VpLWo5mhHHSH8EYdi7u133nWh9OHH0CFD833HFjL6oXGdmFlNp3WzRbXiqVj2blCcbIkje%2BWg1Uu2TGAUIz%2Bgw3jTnyrAExa1o3duTbJDSjBvbogspsyjx5eAItBeVDkL36BXGzft%2FQGHratGm5X8BTUHeu%2B8rUv4rCkC4mNMMIaWm70GOqUBxVu9J9SUVH3SeErQJKIlJamwVOM2OcS26WDc2sgnTnAHAUX84xXAnEXJWM2rN0jtCbrobR1dZIMjT9QeAJ1bAsIfgHZD3f7oWqfim1umUd5f59Qyj%2BXbzJL2%2F00Y6LXUd25DEG9Qwfldxe7TqoLXurAZ7hSPhMy8T%2B4Yo1Idf%2FF3e%2FJFxPKC8lHbPiUtHjT2h%2F8hoiSWxiTYI50LrC9CfXDEgJCL&X-Amz-Signature=5699412ff8704631720533fa290a062acbfac2b4f0ac7ea0efd61f8016968c61&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DRSQNYS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCt40SFa5%2B7%2FVIv8GG2f4WD2Xd4RQTRrMP5TqJn533CRAIgGOZ9drcd%2BKWRM5c%2BdvbliCpWAqnyjzwiuyq2g%2FTQp%2B4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQrpvSi0JIl%2BaY5kircAxZmhuBKHaAHIddT75KZy%2BHa01VJYfWlo2THklO%2F2G%2BJEJEc%2FROcA5L8w7szjeyGST9TIBVwL43MsoGeYp%2BLERJ5gCJc743xHT7GhdTTZCv93acSWTWCxdWi4tJY4zPd8xacqjvu87u1xJkjlgeoIHlJ%2BxE1n8cxD4KvsZN8C5RplrplM0l4WTqBVw%2Bp09%2FNHi%2FAMShvFx%2B2r9uMGSAie5ISO4pgf3PcPn%2F%2B0wAp7IPst%2Bl8MDwNI3s41MHO%2Fz4Y8sYtJvVcjsoSSvWAGuM%2B98J124jlWbqpUktbRybJLGrZ7tEJj0GajABnf%2BO%2FeUtbOQ9%2BsS5zvEh%2FbYmBd1kG5fjAM4mYPhoP1B%2BArpJrG51kIirp%2BwF5q1f6PyfOXfItAIo4jGyIVmGfwQf%2F2anc2L8O6gnO%2F0w9qhQlEm%2FKNP8fos%2F3aLm7wuvztuh3Vb77TUwZEZRq9ssGvppJXS4VpLWo5mhHHSH8EYdi7u133nWh9OHH0CFD833HFjL6oXGdmFlNp3WzRbXiqVj2blCcbIkje%2BWg1Uu2TGAUIz%2Bgw3jTnyrAExa1o3duTbJDSjBvbogspsyjx5eAItBeVDkL36BXGzft%2FQGHratGm5X8BTUHeu%2B8rUv4rCkC4mNMMIaWm70GOqUBxVu9J9SUVH3SeErQJKIlJamwVOM2OcS26WDc2sgnTnAHAUX84xXAnEXJWM2rN0jtCbrobR1dZIMjT9QeAJ1bAsIfgHZD3f7oWqfim1umUd5f59Qyj%2BXbzJL2%2F00Y6LXUd25DEG9Qwfldxe7TqoLXurAZ7hSPhMy8T%2B4Yo1Idf%2FF3e%2FJFxPKC8lHbPiUtHjT2h%2F8hoiSWxiTYI50LrC9CfXDEgJCL&X-Amz-Signature=80a5d3f204355750d8c8d04d8ac4e8454c51b9ba7a72acb444f88505970011f5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Video Sequences
A **video** can be viewed as a sequence of multiple **images** or **frames**.
### Image Formats
Common image file formats include:
- **JPEG** (Joint Photographic Expert Group)
- **PNG** (Portable Network Graphics)
These formats compress and reduce file sizes while maintaining image quality.
### Image Processing Libraries in Python
#### Pillow (PIL)
Pillow is a widely used Python library for image manipulation.
- To load an image:
```python
from PIL import Image
img = Image.open('image.png')
```
- **Attributes** of a Pillow image:
	- `format`: The file format (e.g., PNG, JPEG).
	- `size`: The dimensions of the image (width x height).
	- `mode`: The color space (e.g., RGB, L for grayscale).
#### Example: Converting to Gray-Scale
- Convert an image to **gray-scale**:
```python
gray_img = img.convert('L')
gray_img.show()
```
#### Example: Quantization
- **Quantize** an image to reduce the number of intensity levels:
```python
quantized_img = img.quantize(colors=16)
quantized_img.show()
```
#### OpenCV
**OpenCV** is a powerful library for **computer vision** with more functionality than PIL.
- Import OpenCV:
```python
import cv2
```
- Load an image:
```python
img = cv2.imread('image.png')
```
- **Attributes** of an OpenCV image:
	- OpenCV represents images as **NumPy arrays**.
	- The **color channels** are ordered as **BGR** (blue, green, red) instead of **RGB**.
#### Example: Color Space Conversion
- Convert from **BGR to RGB**:
```python
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
- Convert to **gray-scale**:
```python
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
#### Example: Saving an Image
- Save an image using OpenCV:
```python
cv2.imwrite('output.png', img)
```
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DRSQNYS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCt40SFa5%2B7%2FVIv8GG2f4WD2Xd4RQTRrMP5TqJn533CRAIgGOZ9drcd%2BKWRM5c%2BdvbliCpWAqnyjzwiuyq2g%2FTQp%2B4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQrpvSi0JIl%2BaY5kircAxZmhuBKHaAHIddT75KZy%2BHa01VJYfWlo2THklO%2F2G%2BJEJEc%2FROcA5L8w7szjeyGST9TIBVwL43MsoGeYp%2BLERJ5gCJc743xHT7GhdTTZCv93acSWTWCxdWi4tJY4zPd8xacqjvu87u1xJkjlgeoIHlJ%2BxE1n8cxD4KvsZN8C5RplrplM0l4WTqBVw%2Bp09%2FNHi%2FAMShvFx%2B2r9uMGSAie5ISO4pgf3PcPn%2F%2B0wAp7IPst%2Bl8MDwNI3s41MHO%2Fz4Y8sYtJvVcjsoSSvWAGuM%2B98J124jlWbqpUktbRybJLGrZ7tEJj0GajABnf%2BO%2FeUtbOQ9%2BsS5zvEh%2FbYmBd1kG5fjAM4mYPhoP1B%2BArpJrG51kIirp%2BwF5q1f6PyfOXfItAIo4jGyIVmGfwQf%2F2anc2L8O6gnO%2F0w9qhQlEm%2FKNP8fos%2F3aLm7wuvztuh3Vb77TUwZEZRq9ssGvppJXS4VpLWo5mhHHSH8EYdi7u133nWh9OHH0CFD833HFjL6oXGdmFlNp3WzRbXiqVj2blCcbIkje%2BWg1Uu2TGAUIz%2Bgw3jTnyrAExa1o3duTbJDSjBvbogspsyjx5eAItBeVDkL36BXGzft%2FQGHratGm5X8BTUHeu%2B8rUv4rCkC4mNMMIaWm70GOqUBxVu9J9SUVH3SeErQJKIlJamwVOM2OcS26WDc2sgnTnAHAUX84xXAnEXJWM2rN0jtCbrobR1dZIMjT9QeAJ1bAsIfgHZD3f7oWqfim1umUd5f59Qyj%2BXbzJL2%2F00Y6LXUd25DEG9Qwfldxe7TqoLXurAZ7hSPhMy8T%2B4Yo1Idf%2FF3e%2FJFxPKC8lHbPiUtHjT2h%2F8hoiSWxiTYI50LrC9CfXDEgJCL&X-Amz-Signature=43089198f857fcd9c7d58452d86cd9d7819a7976f8d7b775cbdbe8ced18e3a20&X-Amz-SignedHeaders=host&x-id=GetObject)
### Working with Color Channels
Using **slices**, individual color channels (e.g., **blue**, **green**, **red**) can be extracted:
```python
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]
```
Each channel can then be processed or analyzed separately.
#### Conversion between PIL and NumPy Arrays
PIL images can be easily converted to **NumPy arrays** for further processing:
```python
import numpy as np
np_img = np.array(img)
```
This conversion is particularly useful when integrating with **OpenCV** and performing advanced operations.
### Conclusion
Both **PIL** and **OpenCV** are essential tools for handling and processing digital images in Python. Each has its strengths:
- **PIL** is simple and great for basic tasks.
- **OpenCV** offers more advanced capabilities for **computer vision** applications.
___


