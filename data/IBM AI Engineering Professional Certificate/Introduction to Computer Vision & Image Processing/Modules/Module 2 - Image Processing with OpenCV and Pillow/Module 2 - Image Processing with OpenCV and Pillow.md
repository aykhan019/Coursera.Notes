

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBAXS7PK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6VYbMj6gmvWBd7%2BV56l1etPAaPl6pwLW2jAp8YtYVZAiEAg6J1VU23rZSIILHukNFODIvhckuwd0jX35X5leQO2DoqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEg%2F8sbD13WEP9iaEyrcA56Sa9Zjy83qY2qUfmdLlRbwrnHawcxFZv4O4IMmzglyqL7C6o%2FcrR0FgsGkXrn7bqxDghOqB39L1xP1VnlMJQm2t6dvvwz4aNJ0Tf2ZIT73r8o7BeWw62khQWqZZj3AVMD7tmIWlPNef4zJTVsVz62ASgd7C1zTVNTCUNgX0dRvmgZ38CIWypiGgCJdWNj%2FLqB0XrbNGpVGCdGduI5xliPcoy%2FGQG7xdJzzq0QQduTRozpgdWYeR5Cr%2BUlG5oijSidN6GxDUtNClKaDw%2F3c30vNw2Og0VWlMTbLVWpmFtGvcKnHlyUwxUf5WyQ6vBNqZ4Uyw%2FeIVfYOpZXfmkaXfum79%2BjZwyBnBR95VquNKXxGZ67BNftrzxB3Z40e%2FZh9bdvvqjipbplEbi76sXyRoQhG0Blmca3ZBWFqayOYVDWRMv7SW782%2FsdID9I%2Futv7o%2BsiDL69z53WByySug3EF4q%2BLbz2K85I2GbXZ6EmM3brsSVtG5q08KU%2FgVJxsVI%2FKCCfqRFSSf3DRWpHYQ24NYfklm21%2FpkKsvqc7pT%2F54riAVWZ7L7lweQ7ANzDzQYwnD81iBJgXQObPBQcNlx8SEfq5lgGntpdVUeammoLvvLBhI%2Fd3vHOPnIyLbPyMLW%2FgL0GOqUBjXv0E08y4simvINzZb%2Bz%2Ftv4AT5ASZpMOQr4J8%2F2uUd0bveqEFn7KHZu8BcbOsftCG5QigISlcDokyh1SOyXgGMQbfZZQXvZGHOon3clMTJgI5vl67iJ5ZT26gzFejzDDgbf8hcvPWEm%2FbjhGJDkP91KmpcCJOyp2%2BT4qcXwLx26d3UbRireS9TOypHIjUInUmlTzOXjKagUsbOrm8%2FQEETF%2Fo3k&X-Amz-Signature=af63e002209e65155a8d76f28223cd61ffe1f7e2dde0905720ef988898ac533d&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JT6H6ZS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC10jXEXsA09gBbvkuIWuORbp8YOgbajBZ26T67TVh4XAIhAPJwsT892QnCC9Pt%2FqrWlsoPYrfcgK7jSGk390FrZkiHKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl337Kum9L69dw4pcq3AMXy399Su35MVU2uwCwGMO2B3sH7E9pLPc6Sd%2Bq0MA%2B%2BY6dsGgPjKl9EaV3JeiwblSuF6UXcswWzhublQHjzWhsP48%2FwZwv6W9BPBjUR6C7lzNmZV83wRlzU63UHH%2FdplOwfar5W%2FKM0Fi4h2TZygIyB%2FMkbx%2FIcf6xGhK2AU5v%2Fdz1V2l8rAZV98ZhbL32gV7wne2Okf5ZrG9vGoe33YYsmOXoszNQAjqpIHXdie3xot3j1HRn9Yxk4Vuoe5AHleeXsxSItW9tkgGh5ddn%2FzcGSHpr7VxydSVWb5K2ZZBoFSQqQ%2BPGvOB9UybU2r7SqbZeiaocvDpoVobA6isqc74foYcePnfGsmcj9SB3LPifiZ0BU6qOcSDC0uvaDTDg2QcEuA2CPtx%2FZYFrTZ0RvBmWpJXti29bStxEsX5r%2FBmG5nO1VgrQc%2FC3Okl8XvwtcYpUwWjFHOrDjVYXEEAXH26YE6VRDDf1KzaWul9V7eTBSWeSDfBpd55osf4IwvV9b9mkYqozknq9zJC7UGthXc6CpwWL2%2B0YHKB2sb%2BhMGNczBuDv7q0PYzo7ZcYo9CG74vxg00yvhXoxufll3sNkmDjQrzSe4WMaNvudvFRFSKtFnrCVcGkqsEw2QZDxDDlv4C9BjqkAao2UNvg2YOpvIP8AkhLlZdVCOTIKxQsuvixsR9OPgnbtI9nRajkzokjS1vmD71CHkdZrJrvnRdUmzMXiFZTOBtvWEqQgXDMkz0lOtgR80csg1ukI8sJru3DDnzhUNYL86mAEhLO%2BgH%2BpjpsU9Ta1nE7ReZ8G%2F26qypbwkcq62SJu95%2BETWeWM4xgNOj0mujo6UEWswzvmDqJPVG0ijKX8vT9kO1&X-Amz-Signature=30a00164cb9e2619237d9e3c3b270590e3fd54790812376b55c494234f736ed8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JT6H6ZS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC10jXEXsA09gBbvkuIWuORbp8YOgbajBZ26T67TVh4XAIhAPJwsT892QnCC9Pt%2FqrWlsoPYrfcgK7jSGk390FrZkiHKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl337Kum9L69dw4pcq3AMXy399Su35MVU2uwCwGMO2B3sH7E9pLPc6Sd%2Bq0MA%2B%2BY6dsGgPjKl9EaV3JeiwblSuF6UXcswWzhublQHjzWhsP48%2FwZwv6W9BPBjUR6C7lzNmZV83wRlzU63UHH%2FdplOwfar5W%2FKM0Fi4h2TZygIyB%2FMkbx%2FIcf6xGhK2AU5v%2Fdz1V2l8rAZV98ZhbL32gV7wne2Okf5ZrG9vGoe33YYsmOXoszNQAjqpIHXdie3xot3j1HRn9Yxk4Vuoe5AHleeXsxSItW9tkgGh5ddn%2FzcGSHpr7VxydSVWb5K2ZZBoFSQqQ%2BPGvOB9UybU2r7SqbZeiaocvDpoVobA6isqc74foYcePnfGsmcj9SB3LPifiZ0BU6qOcSDC0uvaDTDg2QcEuA2CPtx%2FZYFrTZ0RvBmWpJXti29bStxEsX5r%2FBmG5nO1VgrQc%2FC3Okl8XvwtcYpUwWjFHOrDjVYXEEAXH26YE6VRDDf1KzaWul9V7eTBSWeSDfBpd55osf4IwvV9b9mkYqozknq9zJC7UGthXc6CpwWL2%2B0YHKB2sb%2BhMGNczBuDv7q0PYzo7ZcYo9CG74vxg00yvhXoxufll3sNkmDjQrzSe4WMaNvudvFRFSKtFnrCVcGkqsEw2QZDxDDlv4C9BjqkAao2UNvg2YOpvIP8AkhLlZdVCOTIKxQsuvixsR9OPgnbtI9nRajkzokjS1vmD71CHkdZrJrvnRdUmzMXiFZTOBtvWEqQgXDMkz0lOtgR80csg1ukI8sJru3DDnzhUNYL86mAEhLO%2BgH%2BpjpsU9Ta1nE7ReZ8G%2F26qypbwkcq62SJu95%2BETWeWM4xgNOj0mujo6UEWswzvmDqJPVG0ijKX8vT9kO1&X-Amz-Signature=23d804d40cb95d7a6a411afde60e85b88f083b0048a5942b24571da55f421681&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JT6H6ZS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC10jXEXsA09gBbvkuIWuORbp8YOgbajBZ26T67TVh4XAIhAPJwsT892QnCC9Pt%2FqrWlsoPYrfcgK7jSGk390FrZkiHKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl337Kum9L69dw4pcq3AMXy399Su35MVU2uwCwGMO2B3sH7E9pLPc6Sd%2Bq0MA%2B%2BY6dsGgPjKl9EaV3JeiwblSuF6UXcswWzhublQHjzWhsP48%2FwZwv6W9BPBjUR6C7lzNmZV83wRlzU63UHH%2FdplOwfar5W%2FKM0Fi4h2TZygIyB%2FMkbx%2FIcf6xGhK2AU5v%2Fdz1V2l8rAZV98ZhbL32gV7wne2Okf5ZrG9vGoe33YYsmOXoszNQAjqpIHXdie3xot3j1HRn9Yxk4Vuoe5AHleeXsxSItW9tkgGh5ddn%2FzcGSHpr7VxydSVWb5K2ZZBoFSQqQ%2BPGvOB9UybU2r7SqbZeiaocvDpoVobA6isqc74foYcePnfGsmcj9SB3LPifiZ0BU6qOcSDC0uvaDTDg2QcEuA2CPtx%2FZYFrTZ0RvBmWpJXti29bStxEsX5r%2FBmG5nO1VgrQc%2FC3Okl8XvwtcYpUwWjFHOrDjVYXEEAXH26YE6VRDDf1KzaWul9V7eTBSWeSDfBpd55osf4IwvV9b9mkYqozknq9zJC7UGthXc6CpwWL2%2B0YHKB2sb%2BhMGNczBuDv7q0PYzo7ZcYo9CG74vxg00yvhXoxufll3sNkmDjQrzSe4WMaNvudvFRFSKtFnrCVcGkqsEw2QZDxDDlv4C9BjqkAao2UNvg2YOpvIP8AkhLlZdVCOTIKxQsuvixsR9OPgnbtI9nRajkzokjS1vmD71CHkdZrJrvnRdUmzMXiFZTOBtvWEqQgXDMkz0lOtgR80csg1ukI8sJru3DDnzhUNYL86mAEhLO%2BgH%2BpjpsU9Ta1nE7ReZ8G%2F26qypbwkcq62SJu95%2BETWeWM4xgNOj0mujo6UEWswzvmDqJPVG0ijKX8vT9kO1&X-Amz-Signature=1375d6725a0d62b6ef5b3b63d08ef79ef5e1a35ba00eba1814bc9086522d075c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JT6H6ZS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC10jXEXsA09gBbvkuIWuORbp8YOgbajBZ26T67TVh4XAIhAPJwsT892QnCC9Pt%2FqrWlsoPYrfcgK7jSGk390FrZkiHKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl337Kum9L69dw4pcq3AMXy399Su35MVU2uwCwGMO2B3sH7E9pLPc6Sd%2Bq0MA%2B%2BY6dsGgPjKl9EaV3JeiwblSuF6UXcswWzhublQHjzWhsP48%2FwZwv6W9BPBjUR6C7lzNmZV83wRlzU63UHH%2FdplOwfar5W%2FKM0Fi4h2TZygIyB%2FMkbx%2FIcf6xGhK2AU5v%2Fdz1V2l8rAZV98ZhbL32gV7wne2Okf5ZrG9vGoe33YYsmOXoszNQAjqpIHXdie3xot3j1HRn9Yxk4Vuoe5AHleeXsxSItW9tkgGh5ddn%2FzcGSHpr7VxydSVWb5K2ZZBoFSQqQ%2BPGvOB9UybU2r7SqbZeiaocvDpoVobA6isqc74foYcePnfGsmcj9SB3LPifiZ0BU6qOcSDC0uvaDTDg2QcEuA2CPtx%2FZYFrTZ0RvBmWpJXti29bStxEsX5r%2FBmG5nO1VgrQc%2FC3Okl8XvwtcYpUwWjFHOrDjVYXEEAXH26YE6VRDDf1KzaWul9V7eTBSWeSDfBpd55osf4IwvV9b9mkYqozknq9zJC7UGthXc6CpwWL2%2B0YHKB2sb%2BhMGNczBuDv7q0PYzo7ZcYo9CG74vxg00yvhXoxufll3sNkmDjQrzSe4WMaNvudvFRFSKtFnrCVcGkqsEw2QZDxDDlv4C9BjqkAao2UNvg2YOpvIP8AkhLlZdVCOTIKxQsuvixsR9OPgnbtI9nRajkzokjS1vmD71CHkdZrJrvnRdUmzMXiFZTOBtvWEqQgXDMkz0lOtgR80csg1ukI8sJru3DDnzhUNYL86mAEhLO%2BgH%2BpjpsU9Ta1nE7ReZ8G%2F26qypbwkcq62SJu95%2BETWeWM4xgNOj0mujo6UEWswzvmDqJPVG0ijKX8vT9kO1&X-Amz-Signature=60c3e2f8661ba9052224fc2a803cb484b6244dfe04f7b9b47ca939f41056dc4e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JT6H6ZS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC10jXEXsA09gBbvkuIWuORbp8YOgbajBZ26T67TVh4XAIhAPJwsT892QnCC9Pt%2FqrWlsoPYrfcgK7jSGk390FrZkiHKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl337Kum9L69dw4pcq3AMXy399Su35MVU2uwCwGMO2B3sH7E9pLPc6Sd%2Bq0MA%2B%2BY6dsGgPjKl9EaV3JeiwblSuF6UXcswWzhublQHjzWhsP48%2FwZwv6W9BPBjUR6C7lzNmZV83wRlzU63UHH%2FdplOwfar5W%2FKM0Fi4h2TZygIyB%2FMkbx%2FIcf6xGhK2AU5v%2Fdz1V2l8rAZV98ZhbL32gV7wne2Okf5ZrG9vGoe33YYsmOXoszNQAjqpIHXdie3xot3j1HRn9Yxk4Vuoe5AHleeXsxSItW9tkgGh5ddn%2FzcGSHpr7VxydSVWb5K2ZZBoFSQqQ%2BPGvOB9UybU2r7SqbZeiaocvDpoVobA6isqc74foYcePnfGsmcj9SB3LPifiZ0BU6qOcSDC0uvaDTDg2QcEuA2CPtx%2FZYFrTZ0RvBmWpJXti29bStxEsX5r%2FBmG5nO1VgrQc%2FC3Okl8XvwtcYpUwWjFHOrDjVYXEEAXH26YE6VRDDf1KzaWul9V7eTBSWeSDfBpd55osf4IwvV9b9mkYqozknq9zJC7UGthXc6CpwWL2%2B0YHKB2sb%2BhMGNczBuDv7q0PYzo7ZcYo9CG74vxg00yvhXoxufll3sNkmDjQrzSe4WMaNvudvFRFSKtFnrCVcGkqsEw2QZDxDDlv4C9BjqkAao2UNvg2YOpvIP8AkhLlZdVCOTIKxQsuvixsR9OPgnbtI9nRajkzokjS1vmD71CHkdZrJrvnRdUmzMXiFZTOBtvWEqQgXDMkz0lOtgR80csg1ukI8sJru3DDnzhUNYL86mAEhLO%2BgH%2BpjpsU9Ta1nE7ReZ8G%2F26qypbwkcq62SJu95%2BETWeWM4xgNOj0mujo6UEWswzvmDqJPVG0ijKX8vT9kO1&X-Amz-Signature=df627627c4c5d7ae8cbcea61a16d09797d458d356c57d4e696979b6bd8e6a745&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBAXS7PK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6VYbMj6gmvWBd7%2BV56l1etPAaPl6pwLW2jAp8YtYVZAiEAg6J1VU23rZSIILHukNFODIvhckuwd0jX35X5leQO2DoqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEg%2F8sbD13WEP9iaEyrcA56Sa9Zjy83qY2qUfmdLlRbwrnHawcxFZv4O4IMmzglyqL7C6o%2FcrR0FgsGkXrn7bqxDghOqB39L1xP1VnlMJQm2t6dvvwz4aNJ0Tf2ZIT73r8o7BeWw62khQWqZZj3AVMD7tmIWlPNef4zJTVsVz62ASgd7C1zTVNTCUNgX0dRvmgZ38CIWypiGgCJdWNj%2FLqB0XrbNGpVGCdGduI5xliPcoy%2FGQG7xdJzzq0QQduTRozpgdWYeR5Cr%2BUlG5oijSidN6GxDUtNClKaDw%2F3c30vNw2Og0VWlMTbLVWpmFtGvcKnHlyUwxUf5WyQ6vBNqZ4Uyw%2FeIVfYOpZXfmkaXfum79%2BjZwyBnBR95VquNKXxGZ67BNftrzxB3Z40e%2FZh9bdvvqjipbplEbi76sXyRoQhG0Blmca3ZBWFqayOYVDWRMv7SW782%2FsdID9I%2Futv7o%2BsiDL69z53WByySug3EF4q%2BLbz2K85I2GbXZ6EmM3brsSVtG5q08KU%2FgVJxsVI%2FKCCfqRFSSf3DRWpHYQ24NYfklm21%2FpkKsvqc7pT%2F54riAVWZ7L7lweQ7ANzDzQYwnD81iBJgXQObPBQcNlx8SEfq5lgGntpdVUeammoLvvLBhI%2Fd3vHOPnIyLbPyMLW%2FgL0GOqUBjXv0E08y4simvINzZb%2Bz%2Ftv4AT5ASZpMOQr4J8%2F2uUd0bveqEFn7KHZu8BcbOsftCG5QigISlcDokyh1SOyXgGMQbfZZQXvZGHOon3clMTJgI5vl67iJ5ZT26gzFejzDDgbf8hcvPWEm%2FbjhGJDkP91KmpcCJOyp2%2BT4qcXwLx26d3UbRireS9TOypHIjUInUmlTzOXjKagUsbOrm8%2FQEETF%2Fo3k&X-Amz-Signature=42a012af418cf76c85e0aea00a794194b0ebc240ab8a22dfe91b15e48f06d3e0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBAXS7PK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6VYbMj6gmvWBd7%2BV56l1etPAaPl6pwLW2jAp8YtYVZAiEAg6J1VU23rZSIILHukNFODIvhckuwd0jX35X5leQO2DoqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEg%2F8sbD13WEP9iaEyrcA56Sa9Zjy83qY2qUfmdLlRbwrnHawcxFZv4O4IMmzglyqL7C6o%2FcrR0FgsGkXrn7bqxDghOqB39L1xP1VnlMJQm2t6dvvwz4aNJ0Tf2ZIT73r8o7BeWw62khQWqZZj3AVMD7tmIWlPNef4zJTVsVz62ASgd7C1zTVNTCUNgX0dRvmgZ38CIWypiGgCJdWNj%2FLqB0XrbNGpVGCdGduI5xliPcoy%2FGQG7xdJzzq0QQduTRozpgdWYeR5Cr%2BUlG5oijSidN6GxDUtNClKaDw%2F3c30vNw2Og0VWlMTbLVWpmFtGvcKnHlyUwxUf5WyQ6vBNqZ4Uyw%2FeIVfYOpZXfmkaXfum79%2BjZwyBnBR95VquNKXxGZ67BNftrzxB3Z40e%2FZh9bdvvqjipbplEbi76sXyRoQhG0Blmca3ZBWFqayOYVDWRMv7SW782%2FsdID9I%2Futv7o%2BsiDL69z53WByySug3EF4q%2BLbz2K85I2GbXZ6EmM3brsSVtG5q08KU%2FgVJxsVI%2FKCCfqRFSSf3DRWpHYQ24NYfklm21%2FpkKsvqc7pT%2F54riAVWZ7L7lweQ7ANzDzQYwnD81iBJgXQObPBQcNlx8SEfq5lgGntpdVUeammoLvvLBhI%2Fd3vHOPnIyLbPyMLW%2FgL0GOqUBjXv0E08y4simvINzZb%2Bz%2Ftv4AT5ASZpMOQr4J8%2F2uUd0bveqEFn7KHZu8BcbOsftCG5QigISlcDokyh1SOyXgGMQbfZZQXvZGHOon3clMTJgI5vl67iJ5ZT26gzFejzDDgbf8hcvPWEm%2FbjhGJDkP91KmpcCJOyp2%2BT4qcXwLx26d3UbRireS9TOypHIjUInUmlTzOXjKagUsbOrm8%2FQEETF%2Fo3k&X-Amz-Signature=15f0e8924c8817065fc4de7770d463d81748e23df6e9e79cf8e346ed8587cdc6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBAXS7PK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6VYbMj6gmvWBd7%2BV56l1etPAaPl6pwLW2jAp8YtYVZAiEAg6J1VU23rZSIILHukNFODIvhckuwd0jX35X5leQO2DoqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEg%2F8sbD13WEP9iaEyrcA56Sa9Zjy83qY2qUfmdLlRbwrnHawcxFZv4O4IMmzglyqL7C6o%2FcrR0FgsGkXrn7bqxDghOqB39L1xP1VnlMJQm2t6dvvwz4aNJ0Tf2ZIT73r8o7BeWw62khQWqZZj3AVMD7tmIWlPNef4zJTVsVz62ASgd7C1zTVNTCUNgX0dRvmgZ38CIWypiGgCJdWNj%2FLqB0XrbNGpVGCdGduI5xliPcoy%2FGQG7xdJzzq0QQduTRozpgdWYeR5Cr%2BUlG5oijSidN6GxDUtNClKaDw%2F3c30vNw2Og0VWlMTbLVWpmFtGvcKnHlyUwxUf5WyQ6vBNqZ4Uyw%2FeIVfYOpZXfmkaXfum79%2BjZwyBnBR95VquNKXxGZ67BNftrzxB3Z40e%2FZh9bdvvqjipbplEbi76sXyRoQhG0Blmca3ZBWFqayOYVDWRMv7SW782%2FsdID9I%2Futv7o%2BsiDL69z53WByySug3EF4q%2BLbz2K85I2GbXZ6EmM3brsSVtG5q08KU%2FgVJxsVI%2FKCCfqRFSSf3DRWpHYQ24NYfklm21%2FpkKsvqc7pT%2F54riAVWZ7L7lweQ7ANzDzQYwnD81iBJgXQObPBQcNlx8SEfq5lgGntpdVUeammoLvvLBhI%2Fd3vHOPnIyLbPyMLW%2FgL0GOqUBjXv0E08y4simvINzZb%2Bz%2Ftv4AT5ASZpMOQr4J8%2F2uUd0bveqEFn7KHZu8BcbOsftCG5QigISlcDokyh1SOyXgGMQbfZZQXvZGHOon3clMTJgI5vl67iJ5ZT26gzFejzDDgbf8hcvPWEm%2FbjhGJDkP91KmpcCJOyp2%2BT4qcXwLx26d3UbRireS9TOypHIjUInUmlTzOXjKagUsbOrm8%2FQEETF%2Fo3k&X-Amz-Signature=c299eb7dac0932a3dcf704972c08a3f77701839f8d5f43f8f80d028e7baae6c4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBAXS7PK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6VYbMj6gmvWBd7%2BV56l1etPAaPl6pwLW2jAp8YtYVZAiEAg6J1VU23rZSIILHukNFODIvhckuwd0jX35X5leQO2DoqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEg%2F8sbD13WEP9iaEyrcA56Sa9Zjy83qY2qUfmdLlRbwrnHawcxFZv4O4IMmzglyqL7C6o%2FcrR0FgsGkXrn7bqxDghOqB39L1xP1VnlMJQm2t6dvvwz4aNJ0Tf2ZIT73r8o7BeWw62khQWqZZj3AVMD7tmIWlPNef4zJTVsVz62ASgd7C1zTVNTCUNgX0dRvmgZ38CIWypiGgCJdWNj%2FLqB0XrbNGpVGCdGduI5xliPcoy%2FGQG7xdJzzq0QQduTRozpgdWYeR5Cr%2BUlG5oijSidN6GxDUtNClKaDw%2F3c30vNw2Og0VWlMTbLVWpmFtGvcKnHlyUwxUf5WyQ6vBNqZ4Uyw%2FeIVfYOpZXfmkaXfum79%2BjZwyBnBR95VquNKXxGZ67BNftrzxB3Z40e%2FZh9bdvvqjipbplEbi76sXyRoQhG0Blmca3ZBWFqayOYVDWRMv7SW782%2FsdID9I%2Futv7o%2BsiDL69z53WByySug3EF4q%2BLbz2K85I2GbXZ6EmM3brsSVtG5q08KU%2FgVJxsVI%2FKCCfqRFSSf3DRWpHYQ24NYfklm21%2FpkKsvqc7pT%2F54riAVWZ7L7lweQ7ANzDzQYwnD81iBJgXQObPBQcNlx8SEfq5lgGntpdVUeammoLvvLBhI%2Fd3vHOPnIyLbPyMLW%2FgL0GOqUBjXv0E08y4simvINzZb%2Bz%2Ftv4AT5ASZpMOQr4J8%2F2uUd0bveqEFn7KHZu8BcbOsftCG5QigISlcDokyh1SOyXgGMQbfZZQXvZGHOon3clMTJgI5vl67iJ5ZT26gzFejzDDgbf8hcvPWEm%2FbjhGJDkP91KmpcCJOyp2%2BT4qcXwLx26d3UbRireS9TOypHIjUInUmlTzOXjKagUsbOrm8%2FQEETF%2Fo3k&X-Amz-Signature=f703315332b16690f22753e22e81eb53a68c04d122b0f03727d6a36b7ec30286&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBAXS7PK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6VYbMj6gmvWBd7%2BV56l1etPAaPl6pwLW2jAp8YtYVZAiEAg6J1VU23rZSIILHukNFODIvhckuwd0jX35X5leQO2DoqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEg%2F8sbD13WEP9iaEyrcA56Sa9Zjy83qY2qUfmdLlRbwrnHawcxFZv4O4IMmzglyqL7C6o%2FcrR0FgsGkXrn7bqxDghOqB39L1xP1VnlMJQm2t6dvvwz4aNJ0Tf2ZIT73r8o7BeWw62khQWqZZj3AVMD7tmIWlPNef4zJTVsVz62ASgd7C1zTVNTCUNgX0dRvmgZ38CIWypiGgCJdWNj%2FLqB0XrbNGpVGCdGduI5xliPcoy%2FGQG7xdJzzq0QQduTRozpgdWYeR5Cr%2BUlG5oijSidN6GxDUtNClKaDw%2F3c30vNw2Og0VWlMTbLVWpmFtGvcKnHlyUwxUf5WyQ6vBNqZ4Uyw%2FeIVfYOpZXfmkaXfum79%2BjZwyBnBR95VquNKXxGZ67BNftrzxB3Z40e%2FZh9bdvvqjipbplEbi76sXyRoQhG0Blmca3ZBWFqayOYVDWRMv7SW782%2FsdID9I%2Futv7o%2BsiDL69z53WByySug3EF4q%2BLbz2K85I2GbXZ6EmM3brsSVtG5q08KU%2FgVJxsVI%2FKCCfqRFSSf3DRWpHYQ24NYfklm21%2FpkKsvqc7pT%2F54riAVWZ7L7lweQ7ANzDzQYwnD81iBJgXQObPBQcNlx8SEfq5lgGntpdVUeammoLvvLBhI%2Fd3vHOPnIyLbPyMLW%2FgL0GOqUBjXv0E08y4simvINzZb%2Bz%2Ftv4AT5ASZpMOQr4J8%2F2uUd0bveqEFn7KHZu8BcbOsftCG5QigISlcDokyh1SOyXgGMQbfZZQXvZGHOon3clMTJgI5vl67iJ5ZT26gzFejzDDgbf8hcvPWEm%2FbjhGJDkP91KmpcCJOyp2%2BT4qcXwLx26d3UbRireS9TOypHIjUInUmlTzOXjKagUsbOrm8%2FQEETF%2Fo3k&X-Amz-Signature=71aaa1fd7c98cfdcab1e6828cbc7b526b7dce28ae281e0383a19acec3660cc7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


