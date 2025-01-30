

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OHEAFMF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDAFYpLPp6gM4wKHTAwD0xH9z%2BSbIOrpkSs%2BBaxF1TQcAiAHb5lzGhVcl17%2BQ%2FRLTEbobFuLInb9GE3580G0QPSz0iqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNJ7nWmDwkW5u9UnKtwD%2BscxojTSZH8u8oalm4CNR9QeBeQgxwJxeKc4ltrIgW0Qru6anGcXX9mZOkvYLHK70incLrdfUKAI4J9xKIX2bKy9s%2FJg1zyVJzAdr1keHSfETQ3jbz%2FR6og08xxtNDjJ7f3b4WLYqleTXxuxVFMwZWS0nODjp9I75rltbgZRZ2xvnJ3zD5Nd5XtynwBpeS2rpV1e%2FldGAm27u2ht7oks3h9SSI887ZRGJuazgeQ7zQzb3%2BIKqs7fR2h4tC2l2gc1Dc%2FKepLcf%2Bi1KOyqvsZpHY%2BtlK1YZNiHNAaoeoUclzdoz36voIVGypGNn5WZGy3jcYZjEM0J254Ijn4b8e0UxVvCkF3sVisXIWK8MRKIJY2sGRcamnA4ECV1o6plPHizfzSKG8v2llf51xBZsvpuhFvOVRJdpOQtEA4QZ7C39Gy91j8nflV3Rs3emyiT7YtEVS8G%2FmnCwwfW9WS86ZbLJXpcHKjaNoXdXz%2BPkHeGEC66P%2BaKeW%2B9cC1EKUWrIIXUcpZDzD6DkLXpzkRrM8V%2FFF8ctt8qnHbeSVj9I1WsHHg%2BO1J76DKTFYOPWpAczasxekzBAdE4yn%2FTjVYLrM427JS5IlSDivXFubWvfeONaIbOrlpKzURFCgNs%2F%2Fswj8bvvAY6pgHigz4xWNygZjk2XA6bwgIDEt7cfOJ%2FoeDM%2Fw%2BjrXs6%2F1341RP16piiEo1f7q47b3cUdpBfAwMLhWgNv0sCpe7S9JzYLSBe4nV%2FMxMuMWMtKkQ1%2BCT%2BciVchTEuWS%2F69xDUNiiqaIOGcH22k235AytmN2qp%2BsQ9lxxrmbAjbJpA6z%2Fn7XqjMI5345VOc8xDnxmvlRiuDsNhdNNUuNUq5%2B8BT1BzZCU%2B&X-Amz-Signature=d5c8badadca59c4c3b8ae1401015d9a09be01ea1e5a54666445ae931ec7bfd07&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P3WWJQL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFWqnRJt%2Fjx%2BLbjXWmwrbdfISY94v2C%2BAUtxpIUUQbh%2FAiAdSX0Ejjwrg1tIWnJIwiefeZMYSPSlDjgVzl2GqkluoiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BwyHdM%2FkWKJVWItKKtwDa%2BGtGo3qtjJN4Z1OnHD1UQ0Ve59Fk4hFpFDLChpgJqDIbEJMI%2FCpukJC1AbFh9cT%2BQfv1ZvQb%2FEJ3PgPDsQmyfdt9h6GvWh4tFBjg0CU3nd2dmW27ibuAWD0muC5WX%2F9L6lXuUn3ZOtyo49wttMkQgMidMwMVymShF4h4CIR0Sus1hiABUgR72kodi3g6gCkF8Cg90DuiibDX99RYi7YiwQEHiu78s8fUM4MmFys0YTZiBsmymGfWeGUJSy8%2BU4iBXfy5XKw54SUYWR1dY20zd4JUCXos865Dp5q2X3LnFlnVX55YCYmGGVggzqK6PzfdzBhO%2B%2FV6JB2AfPUF%2FZ2saHS9iR4tFNG%2FE%2BNgH3SrCxsvdBNyfEg7DYVAdvubnnbByg0NCcbQE0aN52JvBbwOFh18P%2FKdhzHsgn%2F8jjXaGkXjXfvorKrG%2FVNOVhc8Zl9oSIWA3l1%2F7b8MoZ5M3apwjzQwjVF0O9Gir6Fos6jXvxr4a7UEfou9lW93VajKQszE%2FITFJeDQIpYmp6EpsuWpKdQwCCngl8YQ9o0NNIVs8i2%2FGzGmXI1zWLqs5yRceaiiB3mIg%2FVKpT2q5C35zSKu9q2E3%2BN0Rvf0mAvGPgO4B%2F2M6ZMyk20Nt58q8AwysXvvAY6pgEf5r3NEj7vppbiyH9OoKiTQhuS29ePnUiVY4cpFwjPF1fpscODuctAO6Z8y3tUMAGIHyluxEEk77eMyMnb%2FtKUWHVSe8DCsESWVurYslnckjLesqZAlsQsAgAobaP8ia8evhEIRBWvqK6s2RSlu8F40YvtMT0J%2BEMNJQKSmnw9SaVGG4cLE%2BUAWY1punoNC3Eob8k3cXaGsvtKVU6aAsAvkABKKl9D&X-Amz-Signature=b852193d610f66e7294a07fe0dd1759b48330fee65d0cc1ea291d0af29287774&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P3WWJQL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFWqnRJt%2Fjx%2BLbjXWmwrbdfISY94v2C%2BAUtxpIUUQbh%2FAiAdSX0Ejjwrg1tIWnJIwiefeZMYSPSlDjgVzl2GqkluoiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BwyHdM%2FkWKJVWItKKtwDa%2BGtGo3qtjJN4Z1OnHD1UQ0Ve59Fk4hFpFDLChpgJqDIbEJMI%2FCpukJC1AbFh9cT%2BQfv1ZvQb%2FEJ3PgPDsQmyfdt9h6GvWh4tFBjg0CU3nd2dmW27ibuAWD0muC5WX%2F9L6lXuUn3ZOtyo49wttMkQgMidMwMVymShF4h4CIR0Sus1hiABUgR72kodi3g6gCkF8Cg90DuiibDX99RYi7YiwQEHiu78s8fUM4MmFys0YTZiBsmymGfWeGUJSy8%2BU4iBXfy5XKw54SUYWR1dY20zd4JUCXos865Dp5q2X3LnFlnVX55YCYmGGVggzqK6PzfdzBhO%2B%2FV6JB2AfPUF%2FZ2saHS9iR4tFNG%2FE%2BNgH3SrCxsvdBNyfEg7DYVAdvubnnbByg0NCcbQE0aN52JvBbwOFh18P%2FKdhzHsgn%2F8jjXaGkXjXfvorKrG%2FVNOVhc8Zl9oSIWA3l1%2F7b8MoZ5M3apwjzQwjVF0O9Gir6Fos6jXvxr4a7UEfou9lW93VajKQszE%2FITFJeDQIpYmp6EpsuWpKdQwCCngl8YQ9o0NNIVs8i2%2FGzGmXI1zWLqs5yRceaiiB3mIg%2FVKpT2q5C35zSKu9q2E3%2BN0Rvf0mAvGPgO4B%2F2M6ZMyk20Nt58q8AwysXvvAY6pgEf5r3NEj7vppbiyH9OoKiTQhuS29ePnUiVY4cpFwjPF1fpscODuctAO6Z8y3tUMAGIHyluxEEk77eMyMnb%2FtKUWHVSe8DCsESWVurYslnckjLesqZAlsQsAgAobaP8ia8evhEIRBWvqK6s2RSlu8F40YvtMT0J%2BEMNJQKSmnw9SaVGG4cLE%2BUAWY1punoNC3Eob8k3cXaGsvtKVU6aAsAvkABKKl9D&X-Amz-Signature=ae0396f91bf01c7428c93bc0af14f2a9384f776320db31a0ed3889309ac0228d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P3WWJQL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFWqnRJt%2Fjx%2BLbjXWmwrbdfISY94v2C%2BAUtxpIUUQbh%2FAiAdSX0Ejjwrg1tIWnJIwiefeZMYSPSlDjgVzl2GqkluoiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BwyHdM%2FkWKJVWItKKtwDa%2BGtGo3qtjJN4Z1OnHD1UQ0Ve59Fk4hFpFDLChpgJqDIbEJMI%2FCpukJC1AbFh9cT%2BQfv1ZvQb%2FEJ3PgPDsQmyfdt9h6GvWh4tFBjg0CU3nd2dmW27ibuAWD0muC5WX%2F9L6lXuUn3ZOtyo49wttMkQgMidMwMVymShF4h4CIR0Sus1hiABUgR72kodi3g6gCkF8Cg90DuiibDX99RYi7YiwQEHiu78s8fUM4MmFys0YTZiBsmymGfWeGUJSy8%2BU4iBXfy5XKw54SUYWR1dY20zd4JUCXos865Dp5q2X3LnFlnVX55YCYmGGVggzqK6PzfdzBhO%2B%2FV6JB2AfPUF%2FZ2saHS9iR4tFNG%2FE%2BNgH3SrCxsvdBNyfEg7DYVAdvubnnbByg0NCcbQE0aN52JvBbwOFh18P%2FKdhzHsgn%2F8jjXaGkXjXfvorKrG%2FVNOVhc8Zl9oSIWA3l1%2F7b8MoZ5M3apwjzQwjVF0O9Gir6Fos6jXvxr4a7UEfou9lW93VajKQszE%2FITFJeDQIpYmp6EpsuWpKdQwCCngl8YQ9o0NNIVs8i2%2FGzGmXI1zWLqs5yRceaiiB3mIg%2FVKpT2q5C35zSKu9q2E3%2BN0Rvf0mAvGPgO4B%2F2M6ZMyk20Nt58q8AwysXvvAY6pgEf5r3NEj7vppbiyH9OoKiTQhuS29ePnUiVY4cpFwjPF1fpscODuctAO6Z8y3tUMAGIHyluxEEk77eMyMnb%2FtKUWHVSe8DCsESWVurYslnckjLesqZAlsQsAgAobaP8ia8evhEIRBWvqK6s2RSlu8F40YvtMT0J%2BEMNJQKSmnw9SaVGG4cLE%2BUAWY1punoNC3Eob8k3cXaGsvtKVU6aAsAvkABKKl9D&X-Amz-Signature=540821a1b50a6c8934462d449119dd0b0f089069a0ce45d524575bb6c99bdef7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P3WWJQL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFWqnRJt%2Fjx%2BLbjXWmwrbdfISY94v2C%2BAUtxpIUUQbh%2FAiAdSX0Ejjwrg1tIWnJIwiefeZMYSPSlDjgVzl2GqkluoiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BwyHdM%2FkWKJVWItKKtwDa%2BGtGo3qtjJN4Z1OnHD1UQ0Ve59Fk4hFpFDLChpgJqDIbEJMI%2FCpukJC1AbFh9cT%2BQfv1ZvQb%2FEJ3PgPDsQmyfdt9h6GvWh4tFBjg0CU3nd2dmW27ibuAWD0muC5WX%2F9L6lXuUn3ZOtyo49wttMkQgMidMwMVymShF4h4CIR0Sus1hiABUgR72kodi3g6gCkF8Cg90DuiibDX99RYi7YiwQEHiu78s8fUM4MmFys0YTZiBsmymGfWeGUJSy8%2BU4iBXfy5XKw54SUYWR1dY20zd4JUCXos865Dp5q2X3LnFlnVX55YCYmGGVggzqK6PzfdzBhO%2B%2FV6JB2AfPUF%2FZ2saHS9iR4tFNG%2FE%2BNgH3SrCxsvdBNyfEg7DYVAdvubnnbByg0NCcbQE0aN52JvBbwOFh18P%2FKdhzHsgn%2F8jjXaGkXjXfvorKrG%2FVNOVhc8Zl9oSIWA3l1%2F7b8MoZ5M3apwjzQwjVF0O9Gir6Fos6jXvxr4a7UEfou9lW93VajKQszE%2FITFJeDQIpYmp6EpsuWpKdQwCCngl8YQ9o0NNIVs8i2%2FGzGmXI1zWLqs5yRceaiiB3mIg%2FVKpT2q5C35zSKu9q2E3%2BN0Rvf0mAvGPgO4B%2F2M6ZMyk20Nt58q8AwysXvvAY6pgEf5r3NEj7vppbiyH9OoKiTQhuS29ePnUiVY4cpFwjPF1fpscODuctAO6Z8y3tUMAGIHyluxEEk77eMyMnb%2FtKUWHVSe8DCsESWVurYslnckjLesqZAlsQsAgAobaP8ia8evhEIRBWvqK6s2RSlu8F40YvtMT0J%2BEMNJQKSmnw9SaVGG4cLE%2BUAWY1punoNC3Eob8k3cXaGsvtKVU6aAsAvkABKKl9D&X-Amz-Signature=d7775ab5d0f289c443830323563688bbdd0bf24660d88169cd8f530c85e85855&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P3WWJQL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFWqnRJt%2Fjx%2BLbjXWmwrbdfISY94v2C%2BAUtxpIUUQbh%2FAiAdSX0Ejjwrg1tIWnJIwiefeZMYSPSlDjgVzl2GqkluoiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BwyHdM%2FkWKJVWItKKtwDa%2BGtGo3qtjJN4Z1OnHD1UQ0Ve59Fk4hFpFDLChpgJqDIbEJMI%2FCpukJC1AbFh9cT%2BQfv1ZvQb%2FEJ3PgPDsQmyfdt9h6GvWh4tFBjg0CU3nd2dmW27ibuAWD0muC5WX%2F9L6lXuUn3ZOtyo49wttMkQgMidMwMVymShF4h4CIR0Sus1hiABUgR72kodi3g6gCkF8Cg90DuiibDX99RYi7YiwQEHiu78s8fUM4MmFys0YTZiBsmymGfWeGUJSy8%2BU4iBXfy5XKw54SUYWR1dY20zd4JUCXos865Dp5q2X3LnFlnVX55YCYmGGVggzqK6PzfdzBhO%2B%2FV6JB2AfPUF%2FZ2saHS9iR4tFNG%2FE%2BNgH3SrCxsvdBNyfEg7DYVAdvubnnbByg0NCcbQE0aN52JvBbwOFh18P%2FKdhzHsgn%2F8jjXaGkXjXfvorKrG%2FVNOVhc8Zl9oSIWA3l1%2F7b8MoZ5M3apwjzQwjVF0O9Gir6Fos6jXvxr4a7UEfou9lW93VajKQszE%2FITFJeDQIpYmp6EpsuWpKdQwCCngl8YQ9o0NNIVs8i2%2FGzGmXI1zWLqs5yRceaiiB3mIg%2FVKpT2q5C35zSKu9q2E3%2BN0Rvf0mAvGPgO4B%2F2M6ZMyk20Nt58q8AwysXvvAY6pgEf5r3NEj7vppbiyH9OoKiTQhuS29ePnUiVY4cpFwjPF1fpscODuctAO6Z8y3tUMAGIHyluxEEk77eMyMnb%2FtKUWHVSe8DCsESWVurYslnckjLesqZAlsQsAgAobaP8ia8evhEIRBWvqK6s2RSlu8F40YvtMT0J%2BEMNJQKSmnw9SaVGG4cLE%2BUAWY1punoNC3Eob8k3cXaGsvtKVU6aAsAvkABKKl9D&X-Amz-Signature=628ae6f19329a2220db24685e182708d957adc70995a8f88ae90abd2a64ce84a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OHEAFMF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDAFYpLPp6gM4wKHTAwD0xH9z%2BSbIOrpkSs%2BBaxF1TQcAiAHb5lzGhVcl17%2BQ%2FRLTEbobFuLInb9GE3580G0QPSz0iqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNJ7nWmDwkW5u9UnKtwD%2BscxojTSZH8u8oalm4CNR9QeBeQgxwJxeKc4ltrIgW0Qru6anGcXX9mZOkvYLHK70incLrdfUKAI4J9xKIX2bKy9s%2FJg1zyVJzAdr1keHSfETQ3jbz%2FR6og08xxtNDjJ7f3b4WLYqleTXxuxVFMwZWS0nODjp9I75rltbgZRZ2xvnJ3zD5Nd5XtynwBpeS2rpV1e%2FldGAm27u2ht7oks3h9SSI887ZRGJuazgeQ7zQzb3%2BIKqs7fR2h4tC2l2gc1Dc%2FKepLcf%2Bi1KOyqvsZpHY%2BtlK1YZNiHNAaoeoUclzdoz36voIVGypGNn5WZGy3jcYZjEM0J254Ijn4b8e0UxVvCkF3sVisXIWK8MRKIJY2sGRcamnA4ECV1o6plPHizfzSKG8v2llf51xBZsvpuhFvOVRJdpOQtEA4QZ7C39Gy91j8nflV3Rs3emyiT7YtEVS8G%2FmnCwwfW9WS86ZbLJXpcHKjaNoXdXz%2BPkHeGEC66P%2BaKeW%2B9cC1EKUWrIIXUcpZDzD6DkLXpzkRrM8V%2FFF8ctt8qnHbeSVj9I1WsHHg%2BO1J76DKTFYOPWpAczasxekzBAdE4yn%2FTjVYLrM427JS5IlSDivXFubWvfeONaIbOrlpKzURFCgNs%2F%2Fswj8bvvAY6pgHigz4xWNygZjk2XA6bwgIDEt7cfOJ%2FoeDM%2Fw%2BjrXs6%2F1341RP16piiEo1f7q47b3cUdpBfAwMLhWgNv0sCpe7S9JzYLSBe4nV%2FMxMuMWMtKkQ1%2BCT%2BciVchTEuWS%2F69xDUNiiqaIOGcH22k235AytmN2qp%2BsQ9lxxrmbAjbJpA6z%2Fn7XqjMI5345VOc8xDnxmvlRiuDsNhdNNUuNUq5%2B8BT1BzZCU%2B&X-Amz-Signature=074ae9e9b16b6822fd29d172d4f8ef6d8ebfdd952632e5a6e2a6ed1feb6ac452&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OHEAFMF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDAFYpLPp6gM4wKHTAwD0xH9z%2BSbIOrpkSs%2BBaxF1TQcAiAHb5lzGhVcl17%2BQ%2FRLTEbobFuLInb9GE3580G0QPSz0iqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNJ7nWmDwkW5u9UnKtwD%2BscxojTSZH8u8oalm4CNR9QeBeQgxwJxeKc4ltrIgW0Qru6anGcXX9mZOkvYLHK70incLrdfUKAI4J9xKIX2bKy9s%2FJg1zyVJzAdr1keHSfETQ3jbz%2FR6og08xxtNDjJ7f3b4WLYqleTXxuxVFMwZWS0nODjp9I75rltbgZRZ2xvnJ3zD5Nd5XtynwBpeS2rpV1e%2FldGAm27u2ht7oks3h9SSI887ZRGJuazgeQ7zQzb3%2BIKqs7fR2h4tC2l2gc1Dc%2FKepLcf%2Bi1KOyqvsZpHY%2BtlK1YZNiHNAaoeoUclzdoz36voIVGypGNn5WZGy3jcYZjEM0J254Ijn4b8e0UxVvCkF3sVisXIWK8MRKIJY2sGRcamnA4ECV1o6plPHizfzSKG8v2llf51xBZsvpuhFvOVRJdpOQtEA4QZ7C39Gy91j8nflV3Rs3emyiT7YtEVS8G%2FmnCwwfW9WS86ZbLJXpcHKjaNoXdXz%2BPkHeGEC66P%2BaKeW%2B9cC1EKUWrIIXUcpZDzD6DkLXpzkRrM8V%2FFF8ctt8qnHbeSVj9I1WsHHg%2BO1J76DKTFYOPWpAczasxekzBAdE4yn%2FTjVYLrM427JS5IlSDivXFubWvfeONaIbOrlpKzURFCgNs%2F%2Fswj8bvvAY6pgHigz4xWNygZjk2XA6bwgIDEt7cfOJ%2FoeDM%2Fw%2BjrXs6%2F1341RP16piiEo1f7q47b3cUdpBfAwMLhWgNv0sCpe7S9JzYLSBe4nV%2FMxMuMWMtKkQ1%2BCT%2BciVchTEuWS%2F69xDUNiiqaIOGcH22k235AytmN2qp%2BsQ9lxxrmbAjbJpA6z%2Fn7XqjMI5345VOc8xDnxmvlRiuDsNhdNNUuNUq5%2B8BT1BzZCU%2B&X-Amz-Signature=d4680ea7d20e00782508f8107f0a677949e80c98cafbf85560c542ebae43daff&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OHEAFMF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDAFYpLPp6gM4wKHTAwD0xH9z%2BSbIOrpkSs%2BBaxF1TQcAiAHb5lzGhVcl17%2BQ%2FRLTEbobFuLInb9GE3580G0QPSz0iqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNJ7nWmDwkW5u9UnKtwD%2BscxojTSZH8u8oalm4CNR9QeBeQgxwJxeKc4ltrIgW0Qru6anGcXX9mZOkvYLHK70incLrdfUKAI4J9xKIX2bKy9s%2FJg1zyVJzAdr1keHSfETQ3jbz%2FR6og08xxtNDjJ7f3b4WLYqleTXxuxVFMwZWS0nODjp9I75rltbgZRZ2xvnJ3zD5Nd5XtynwBpeS2rpV1e%2FldGAm27u2ht7oks3h9SSI887ZRGJuazgeQ7zQzb3%2BIKqs7fR2h4tC2l2gc1Dc%2FKepLcf%2Bi1KOyqvsZpHY%2BtlK1YZNiHNAaoeoUclzdoz36voIVGypGNn5WZGy3jcYZjEM0J254Ijn4b8e0UxVvCkF3sVisXIWK8MRKIJY2sGRcamnA4ECV1o6plPHizfzSKG8v2llf51xBZsvpuhFvOVRJdpOQtEA4QZ7C39Gy91j8nflV3Rs3emyiT7YtEVS8G%2FmnCwwfW9WS86ZbLJXpcHKjaNoXdXz%2BPkHeGEC66P%2BaKeW%2B9cC1EKUWrIIXUcpZDzD6DkLXpzkRrM8V%2FFF8ctt8qnHbeSVj9I1WsHHg%2BO1J76DKTFYOPWpAczasxekzBAdE4yn%2FTjVYLrM427JS5IlSDivXFubWvfeONaIbOrlpKzURFCgNs%2F%2Fswj8bvvAY6pgHigz4xWNygZjk2XA6bwgIDEt7cfOJ%2FoeDM%2Fw%2BjrXs6%2F1341RP16piiEo1f7q47b3cUdpBfAwMLhWgNv0sCpe7S9JzYLSBe4nV%2FMxMuMWMtKkQ1%2BCT%2BciVchTEuWS%2F69xDUNiiqaIOGcH22k235AytmN2qp%2BsQ9lxxrmbAjbJpA6z%2Fn7XqjMI5345VOc8xDnxmvlRiuDsNhdNNUuNUq5%2B8BT1BzZCU%2B&X-Amz-Signature=2b73f9196c74b5801b50ae62fb3f6eb2897348c6139691a01bb00123979e52fb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OHEAFMF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDAFYpLPp6gM4wKHTAwD0xH9z%2BSbIOrpkSs%2BBaxF1TQcAiAHb5lzGhVcl17%2BQ%2FRLTEbobFuLInb9GE3580G0QPSz0iqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNJ7nWmDwkW5u9UnKtwD%2BscxojTSZH8u8oalm4CNR9QeBeQgxwJxeKc4ltrIgW0Qru6anGcXX9mZOkvYLHK70incLrdfUKAI4J9xKIX2bKy9s%2FJg1zyVJzAdr1keHSfETQ3jbz%2FR6og08xxtNDjJ7f3b4WLYqleTXxuxVFMwZWS0nODjp9I75rltbgZRZ2xvnJ3zD5Nd5XtynwBpeS2rpV1e%2FldGAm27u2ht7oks3h9SSI887ZRGJuazgeQ7zQzb3%2BIKqs7fR2h4tC2l2gc1Dc%2FKepLcf%2Bi1KOyqvsZpHY%2BtlK1YZNiHNAaoeoUclzdoz36voIVGypGNn5WZGy3jcYZjEM0J254Ijn4b8e0UxVvCkF3sVisXIWK8MRKIJY2sGRcamnA4ECV1o6plPHizfzSKG8v2llf51xBZsvpuhFvOVRJdpOQtEA4QZ7C39Gy91j8nflV3Rs3emyiT7YtEVS8G%2FmnCwwfW9WS86ZbLJXpcHKjaNoXdXz%2BPkHeGEC66P%2BaKeW%2B9cC1EKUWrIIXUcpZDzD6DkLXpzkRrM8V%2FFF8ctt8qnHbeSVj9I1WsHHg%2BO1J76DKTFYOPWpAczasxekzBAdE4yn%2FTjVYLrM427JS5IlSDivXFubWvfeONaIbOrlpKzURFCgNs%2F%2Fswj8bvvAY6pgHigz4xWNygZjk2XA6bwgIDEt7cfOJ%2FoeDM%2Fw%2BjrXs6%2F1341RP16piiEo1f7q47b3cUdpBfAwMLhWgNv0sCpe7S9JzYLSBe4nV%2FMxMuMWMtKkQ1%2BCT%2BciVchTEuWS%2F69xDUNiiqaIOGcH22k235AytmN2qp%2BsQ9lxxrmbAjbJpA6z%2Fn7XqjMI5345VOc8xDnxmvlRiuDsNhdNNUuNUq5%2B8BT1BzZCU%2B&X-Amz-Signature=38cdc65571bbb50037a8b59d12e28da5398899fcbf0211542daaf1b16953e341&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OHEAFMF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDAFYpLPp6gM4wKHTAwD0xH9z%2BSbIOrpkSs%2BBaxF1TQcAiAHb5lzGhVcl17%2BQ%2FRLTEbobFuLInb9GE3580G0QPSz0iqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNJ7nWmDwkW5u9UnKtwD%2BscxojTSZH8u8oalm4CNR9QeBeQgxwJxeKc4ltrIgW0Qru6anGcXX9mZOkvYLHK70incLrdfUKAI4J9xKIX2bKy9s%2FJg1zyVJzAdr1keHSfETQ3jbz%2FR6og08xxtNDjJ7f3b4WLYqleTXxuxVFMwZWS0nODjp9I75rltbgZRZ2xvnJ3zD5Nd5XtynwBpeS2rpV1e%2FldGAm27u2ht7oks3h9SSI887ZRGJuazgeQ7zQzb3%2BIKqs7fR2h4tC2l2gc1Dc%2FKepLcf%2Bi1KOyqvsZpHY%2BtlK1YZNiHNAaoeoUclzdoz36voIVGypGNn5WZGy3jcYZjEM0J254Ijn4b8e0UxVvCkF3sVisXIWK8MRKIJY2sGRcamnA4ECV1o6plPHizfzSKG8v2llf51xBZsvpuhFvOVRJdpOQtEA4QZ7C39Gy91j8nflV3Rs3emyiT7YtEVS8G%2FmnCwwfW9WS86ZbLJXpcHKjaNoXdXz%2BPkHeGEC66P%2BaKeW%2B9cC1EKUWrIIXUcpZDzD6DkLXpzkRrM8V%2FFF8ctt8qnHbeSVj9I1WsHHg%2BO1J76DKTFYOPWpAczasxekzBAdE4yn%2FTjVYLrM427JS5IlSDivXFubWvfeONaIbOrlpKzURFCgNs%2F%2Fswj8bvvAY6pgHigz4xWNygZjk2XA6bwgIDEt7cfOJ%2FoeDM%2Fw%2BjrXs6%2F1341RP16piiEo1f7q47b3cUdpBfAwMLhWgNv0sCpe7S9JzYLSBe4nV%2FMxMuMWMtKkQ1%2BCT%2BciVchTEuWS%2F69xDUNiiqaIOGcH22k235AytmN2qp%2BsQ9lxxrmbAjbJpA6z%2Fn7XqjMI5345VOc8xDnxmvlRiuDsNhdNNUuNUq5%2B8BT1BzZCU%2B&X-Amz-Signature=a8f469b91a98d13cc81bf6efbb563f7b99b81a523a77ddfa67ccb406126af5f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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


