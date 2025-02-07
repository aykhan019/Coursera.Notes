

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YUKU3XM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBxw2E9pkWdCy0tlVYj0%2FW7Pc8bdTVfoOzSbGF9g%2FbD4AiBQ7IPjkta8CbSDAgBVPOgNNZneTsxxxgQnkuXttIm6KSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMsa%2B5NhUXRGMJPfetKtwD9uZPawrzIXCpIBJawrfYDnr7RVrRorJRm9BbsXQ3knVHiQP7t7R4ANwOaCkVfzBCJmOOac4hsmcz31fTy65AVkvLADlOhbcS07CTNUPA85OOYMftq2SZIeiUQFEc7y0IGouWnb1TbIChnHGaAv9kpNrtjpGgmTYlsGKQwqSn0harnLYlgjalMFchf4JMOJ5shlGKQxJAHy3S0yR%2FUJPW48ejP2gt%2B9QHiJcorteeR95AY2kVw0zZKlAAzswA%2BnmzLZeZWPw1NTUB0XayfwidJBkVYlJmiUKjy9PF9zgDaIk0M7q9otMSAaymITfwGRof2zfX9ci%2FNm4Jp9VRkG4GpbMrzr6moOtR4UH77fnUlgif6AupV81y7LXmOYhhOupf6X3Q3xPwvs7Kya7a0yVOvmg6zTl3O7iYBUBXb4GOJg60EMf5prIH%2FdkBw4FgGgjmQMq3DT8kqIxfIv%2FrRK0h6jIKBI36gGAx1Rj4d6viwIUW2iotaXTk%2BCRusdbyamvvgI769EJBWQ9MTi9xl5YpSzphd1Tk2skA3emfwyZCLWjvPBYGa43gBFekm1bKoJVktE%2B9q%2BmbgvZgGtYzoBFJiZa7GJQP%2BuEk7Cn3hViGUcqt2lSHHVdnP74iDeswqouYvQY6pgFuddG%2BedQZNHNtiUXd7kfnz%2BC9J1s3WuFrw5UOFIYxeIvLgvzZEKwz%2Fw8dA7Xd1yRjr1A7S1w5SscWyg2XkQ2FZaeSURTRji76Q5oXEAFe2u%2FT3BM41zgUOXsumzHnrj9lTdTJ6iZPujNosYo3h5i7OQH87%2Bvis4e6yN%2BpsvJJbpgU85ERs91TKgUUg9brvumRen1WA%2FCKZR%2FTww3VjLwJ%2F39uKPvO&X-Amz-Signature=5adf18d9c1caa5d52591955ce265a59d9ccc30070735353c81c8a78916d4db96&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RX7CJZS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCsIe3S880fxg9LXe8Yscjwfvw16Xg0LEzkCFQDEGDBfAIgDQ8M%2Bzar0i4GX7EY1FuR0%2Bn11QPjLYmrga0zX%2FL%2B6QAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDAG9oQn87FoD3n7%2ByyrcA0R%2BrBYN9wSXDxpwJoGWy1STf1HwnB%2BIHiJnbszwmalBzsj7SDmyIHHGZzUenz%2FlOitbeJT2gMsQl5ncy%2B8JvJF38f%2FlarEWxS1wAo%2F%2FSWG2jU4k2f4tEJZbzlH2IpyaG0XX4pyRlgd%2BU20%2B4SX%2BvDK8Efrps075aVVLrOiwcujmoPjFIBvCk6g6PSJppWa4iDpj%2F7l0eHdqEfyl%2BJ8SuzdLt6fLJyc65vSUM9jh1PDBG7WDW6RCPQOT%2FAF0KdqogUIc3ByEDH%2BNMF3xHWbsrikHeqH2oBUjsb4P4sSzdcb0wiFBC3CjcV8unvwgjFreNdaHobjtBoeUP82wta73WKFNHhTWAoSVx%2FA0RU35OG9%2BCJATzDA6NUsBvcYhr8U1wQ1%2FkC9hFz1jzfw%2B%2FLSWvjVPzXKwo2egCbrf%2BFmLZNjLfTZGJYZhICRk%2BJeFb8OHl9p%2FcHDCL4uxTCpqF1rrru4Dteb3L%2F0DniBCSi80yZArLZZk3jb8Zt8Lt00EjKuDZdV4qGb4q8Clk9%2B7V%2FW09Fu7FXjS9PawrKpTJiIyhN4mnX1tbNL9aesMVQPFnKlnk153p49A%2F1BOos%2Bh8x0uE45xwrjnGuBiTR%2Fay37SDE3hD4GifNcP42B2rA0YMP2KmL0GOqUBdDTs8ECRSgge3irtgMqz2dAr7iEHsvewZrAoyVOpW9sYbVf7usqVmso6zMjt0usRyeamZBVnLz3tJ%2BQBfztreFC2lwcbDrbRkLp9BnOv%2Fy%2FEpbJwRnlKdfk1nHPY9TduRwSTJfzDwOW10s8%2Bq9toXnLHquSCI4hz9Zpj7CCr4fIe9W2eO4yMDjtB52hRORtVlLHjj%2BIohfVoYMyV6tE4ifXvjsn2&X-Amz-Signature=0511124e0d2ced6cb52b05f4bc2f8b84a2ccba4bc67dd63f24bf32c72f7e9f0b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RX7CJZS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCsIe3S880fxg9LXe8Yscjwfvw16Xg0LEzkCFQDEGDBfAIgDQ8M%2Bzar0i4GX7EY1FuR0%2Bn11QPjLYmrga0zX%2FL%2B6QAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDAG9oQn87FoD3n7%2ByyrcA0R%2BrBYN9wSXDxpwJoGWy1STf1HwnB%2BIHiJnbszwmalBzsj7SDmyIHHGZzUenz%2FlOitbeJT2gMsQl5ncy%2B8JvJF38f%2FlarEWxS1wAo%2F%2FSWG2jU4k2f4tEJZbzlH2IpyaG0XX4pyRlgd%2BU20%2B4SX%2BvDK8Efrps075aVVLrOiwcujmoPjFIBvCk6g6PSJppWa4iDpj%2F7l0eHdqEfyl%2BJ8SuzdLt6fLJyc65vSUM9jh1PDBG7WDW6RCPQOT%2FAF0KdqogUIc3ByEDH%2BNMF3xHWbsrikHeqH2oBUjsb4P4sSzdcb0wiFBC3CjcV8unvwgjFreNdaHobjtBoeUP82wta73WKFNHhTWAoSVx%2FA0RU35OG9%2BCJATzDA6NUsBvcYhr8U1wQ1%2FkC9hFz1jzfw%2B%2FLSWvjVPzXKwo2egCbrf%2BFmLZNjLfTZGJYZhICRk%2BJeFb8OHl9p%2FcHDCL4uxTCpqF1rrru4Dteb3L%2F0DniBCSi80yZArLZZk3jb8Zt8Lt00EjKuDZdV4qGb4q8Clk9%2B7V%2FW09Fu7FXjS9PawrKpTJiIyhN4mnX1tbNL9aesMVQPFnKlnk153p49A%2F1BOos%2Bh8x0uE45xwrjnGuBiTR%2Fay37SDE3hD4GifNcP42B2rA0YMP2KmL0GOqUBdDTs8ECRSgge3irtgMqz2dAr7iEHsvewZrAoyVOpW9sYbVf7usqVmso6zMjt0usRyeamZBVnLz3tJ%2BQBfztreFC2lwcbDrbRkLp9BnOv%2Fy%2FEpbJwRnlKdfk1nHPY9TduRwSTJfzDwOW10s8%2Bq9toXnLHquSCI4hz9Zpj7CCr4fIe9W2eO4yMDjtB52hRORtVlLHjj%2BIohfVoYMyV6tE4ifXvjsn2&X-Amz-Signature=96a13019a116033b0495fde149d47048299bd178f991711eb78ebe1ac5d606bc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RX7CJZS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCsIe3S880fxg9LXe8Yscjwfvw16Xg0LEzkCFQDEGDBfAIgDQ8M%2Bzar0i4GX7EY1FuR0%2Bn11QPjLYmrga0zX%2FL%2B6QAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDAG9oQn87FoD3n7%2ByyrcA0R%2BrBYN9wSXDxpwJoGWy1STf1HwnB%2BIHiJnbszwmalBzsj7SDmyIHHGZzUenz%2FlOitbeJT2gMsQl5ncy%2B8JvJF38f%2FlarEWxS1wAo%2F%2FSWG2jU4k2f4tEJZbzlH2IpyaG0XX4pyRlgd%2BU20%2B4SX%2BvDK8Efrps075aVVLrOiwcujmoPjFIBvCk6g6PSJppWa4iDpj%2F7l0eHdqEfyl%2BJ8SuzdLt6fLJyc65vSUM9jh1PDBG7WDW6RCPQOT%2FAF0KdqogUIc3ByEDH%2BNMF3xHWbsrikHeqH2oBUjsb4P4sSzdcb0wiFBC3CjcV8unvwgjFreNdaHobjtBoeUP82wta73WKFNHhTWAoSVx%2FA0RU35OG9%2BCJATzDA6NUsBvcYhr8U1wQ1%2FkC9hFz1jzfw%2B%2FLSWvjVPzXKwo2egCbrf%2BFmLZNjLfTZGJYZhICRk%2BJeFb8OHl9p%2FcHDCL4uxTCpqF1rrru4Dteb3L%2F0DniBCSi80yZArLZZk3jb8Zt8Lt00EjKuDZdV4qGb4q8Clk9%2B7V%2FW09Fu7FXjS9PawrKpTJiIyhN4mnX1tbNL9aesMVQPFnKlnk153p49A%2F1BOos%2Bh8x0uE45xwrjnGuBiTR%2Fay37SDE3hD4GifNcP42B2rA0YMP2KmL0GOqUBdDTs8ECRSgge3irtgMqz2dAr7iEHsvewZrAoyVOpW9sYbVf7usqVmso6zMjt0usRyeamZBVnLz3tJ%2BQBfztreFC2lwcbDrbRkLp9BnOv%2Fy%2FEpbJwRnlKdfk1nHPY9TduRwSTJfzDwOW10s8%2Bq9toXnLHquSCI4hz9Zpj7CCr4fIe9W2eO4yMDjtB52hRORtVlLHjj%2BIohfVoYMyV6tE4ifXvjsn2&X-Amz-Signature=64b3f0b766f1270164f2d0a1d2e6c1cf1381dd7bdd9b5fed87fbea0ebb4c33df&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RX7CJZS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCsIe3S880fxg9LXe8Yscjwfvw16Xg0LEzkCFQDEGDBfAIgDQ8M%2Bzar0i4GX7EY1FuR0%2Bn11QPjLYmrga0zX%2FL%2B6QAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDAG9oQn87FoD3n7%2ByyrcA0R%2BrBYN9wSXDxpwJoGWy1STf1HwnB%2BIHiJnbszwmalBzsj7SDmyIHHGZzUenz%2FlOitbeJT2gMsQl5ncy%2B8JvJF38f%2FlarEWxS1wAo%2F%2FSWG2jU4k2f4tEJZbzlH2IpyaG0XX4pyRlgd%2BU20%2B4SX%2BvDK8Efrps075aVVLrOiwcujmoPjFIBvCk6g6PSJppWa4iDpj%2F7l0eHdqEfyl%2BJ8SuzdLt6fLJyc65vSUM9jh1PDBG7WDW6RCPQOT%2FAF0KdqogUIc3ByEDH%2BNMF3xHWbsrikHeqH2oBUjsb4P4sSzdcb0wiFBC3CjcV8unvwgjFreNdaHobjtBoeUP82wta73WKFNHhTWAoSVx%2FA0RU35OG9%2BCJATzDA6NUsBvcYhr8U1wQ1%2FkC9hFz1jzfw%2B%2FLSWvjVPzXKwo2egCbrf%2BFmLZNjLfTZGJYZhICRk%2BJeFb8OHl9p%2FcHDCL4uxTCpqF1rrru4Dteb3L%2F0DniBCSi80yZArLZZk3jb8Zt8Lt00EjKuDZdV4qGb4q8Clk9%2B7V%2FW09Fu7FXjS9PawrKpTJiIyhN4mnX1tbNL9aesMVQPFnKlnk153p49A%2F1BOos%2Bh8x0uE45xwrjnGuBiTR%2Fay37SDE3hD4GifNcP42B2rA0YMP2KmL0GOqUBdDTs8ECRSgge3irtgMqz2dAr7iEHsvewZrAoyVOpW9sYbVf7usqVmso6zMjt0usRyeamZBVnLz3tJ%2BQBfztreFC2lwcbDrbRkLp9BnOv%2Fy%2FEpbJwRnlKdfk1nHPY9TduRwSTJfzDwOW10s8%2Bq9toXnLHquSCI4hz9Zpj7CCr4fIe9W2eO4yMDjtB52hRORtVlLHjj%2BIohfVoYMyV6tE4ifXvjsn2&X-Amz-Signature=df2d643d8aaeebab9eecbd7cba4ee228df10761eeee2f9637bb882568b69e145&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RX7CJZS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCsIe3S880fxg9LXe8Yscjwfvw16Xg0LEzkCFQDEGDBfAIgDQ8M%2Bzar0i4GX7EY1FuR0%2Bn11QPjLYmrga0zX%2FL%2B6QAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDAG9oQn87FoD3n7%2ByyrcA0R%2BrBYN9wSXDxpwJoGWy1STf1HwnB%2BIHiJnbszwmalBzsj7SDmyIHHGZzUenz%2FlOitbeJT2gMsQl5ncy%2B8JvJF38f%2FlarEWxS1wAo%2F%2FSWG2jU4k2f4tEJZbzlH2IpyaG0XX4pyRlgd%2BU20%2B4SX%2BvDK8Efrps075aVVLrOiwcujmoPjFIBvCk6g6PSJppWa4iDpj%2F7l0eHdqEfyl%2BJ8SuzdLt6fLJyc65vSUM9jh1PDBG7WDW6RCPQOT%2FAF0KdqogUIc3ByEDH%2BNMF3xHWbsrikHeqH2oBUjsb4P4sSzdcb0wiFBC3CjcV8unvwgjFreNdaHobjtBoeUP82wta73WKFNHhTWAoSVx%2FA0RU35OG9%2BCJATzDA6NUsBvcYhr8U1wQ1%2FkC9hFz1jzfw%2B%2FLSWvjVPzXKwo2egCbrf%2BFmLZNjLfTZGJYZhICRk%2BJeFb8OHl9p%2FcHDCL4uxTCpqF1rrru4Dteb3L%2F0DniBCSi80yZArLZZk3jb8Zt8Lt00EjKuDZdV4qGb4q8Clk9%2B7V%2FW09Fu7FXjS9PawrKpTJiIyhN4mnX1tbNL9aesMVQPFnKlnk153p49A%2F1BOos%2Bh8x0uE45xwrjnGuBiTR%2Fay37SDE3hD4GifNcP42B2rA0YMP2KmL0GOqUBdDTs8ECRSgge3irtgMqz2dAr7iEHsvewZrAoyVOpW9sYbVf7usqVmso6zMjt0usRyeamZBVnLz3tJ%2BQBfztreFC2lwcbDrbRkLp9BnOv%2Fy%2FEpbJwRnlKdfk1nHPY9TduRwSTJfzDwOW10s8%2Bq9toXnLHquSCI4hz9Zpj7CCr4fIe9W2eO4yMDjtB52hRORtVlLHjj%2BIohfVoYMyV6tE4ifXvjsn2&X-Amz-Signature=3ec239e39e71c6f8731b77efc84834ba54a7c3da238a896862cc96fcb4c9522d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YUKU3XM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBxw2E9pkWdCy0tlVYj0%2FW7Pc8bdTVfoOzSbGF9g%2FbD4AiBQ7IPjkta8CbSDAgBVPOgNNZneTsxxxgQnkuXttIm6KSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMsa%2B5NhUXRGMJPfetKtwD9uZPawrzIXCpIBJawrfYDnr7RVrRorJRm9BbsXQ3knVHiQP7t7R4ANwOaCkVfzBCJmOOac4hsmcz31fTy65AVkvLADlOhbcS07CTNUPA85OOYMftq2SZIeiUQFEc7y0IGouWnb1TbIChnHGaAv9kpNrtjpGgmTYlsGKQwqSn0harnLYlgjalMFchf4JMOJ5shlGKQxJAHy3S0yR%2FUJPW48ejP2gt%2B9QHiJcorteeR95AY2kVw0zZKlAAzswA%2BnmzLZeZWPw1NTUB0XayfwidJBkVYlJmiUKjy9PF9zgDaIk0M7q9otMSAaymITfwGRof2zfX9ci%2FNm4Jp9VRkG4GpbMrzr6moOtR4UH77fnUlgif6AupV81y7LXmOYhhOupf6X3Q3xPwvs7Kya7a0yVOvmg6zTl3O7iYBUBXb4GOJg60EMf5prIH%2FdkBw4FgGgjmQMq3DT8kqIxfIv%2FrRK0h6jIKBI36gGAx1Rj4d6viwIUW2iotaXTk%2BCRusdbyamvvgI769EJBWQ9MTi9xl5YpSzphd1Tk2skA3emfwyZCLWjvPBYGa43gBFekm1bKoJVktE%2B9q%2BmbgvZgGtYzoBFJiZa7GJQP%2BuEk7Cn3hViGUcqt2lSHHVdnP74iDeswqouYvQY6pgFuddG%2BedQZNHNtiUXd7kfnz%2BC9J1s3WuFrw5UOFIYxeIvLgvzZEKwz%2Fw8dA7Xd1yRjr1A7S1w5SscWyg2XkQ2FZaeSURTRji76Q5oXEAFe2u%2FT3BM41zgUOXsumzHnrj9lTdTJ6iZPujNosYo3h5i7OQH87%2Bvis4e6yN%2BpsvJJbpgU85ERs91TKgUUg9brvumRen1WA%2FCKZR%2FTww3VjLwJ%2F39uKPvO&X-Amz-Signature=f95ffd279c29d426bd3354f79562f3d62a09fe6468b41eaa741f947e412f5601&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YUKU3XM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBxw2E9pkWdCy0tlVYj0%2FW7Pc8bdTVfoOzSbGF9g%2FbD4AiBQ7IPjkta8CbSDAgBVPOgNNZneTsxxxgQnkuXttIm6KSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMsa%2B5NhUXRGMJPfetKtwD9uZPawrzIXCpIBJawrfYDnr7RVrRorJRm9BbsXQ3knVHiQP7t7R4ANwOaCkVfzBCJmOOac4hsmcz31fTy65AVkvLADlOhbcS07CTNUPA85OOYMftq2SZIeiUQFEc7y0IGouWnb1TbIChnHGaAv9kpNrtjpGgmTYlsGKQwqSn0harnLYlgjalMFchf4JMOJ5shlGKQxJAHy3S0yR%2FUJPW48ejP2gt%2B9QHiJcorteeR95AY2kVw0zZKlAAzswA%2BnmzLZeZWPw1NTUB0XayfwidJBkVYlJmiUKjy9PF9zgDaIk0M7q9otMSAaymITfwGRof2zfX9ci%2FNm4Jp9VRkG4GpbMrzr6moOtR4UH77fnUlgif6AupV81y7LXmOYhhOupf6X3Q3xPwvs7Kya7a0yVOvmg6zTl3O7iYBUBXb4GOJg60EMf5prIH%2FdkBw4FgGgjmQMq3DT8kqIxfIv%2FrRK0h6jIKBI36gGAx1Rj4d6viwIUW2iotaXTk%2BCRusdbyamvvgI769EJBWQ9MTi9xl5YpSzphd1Tk2skA3emfwyZCLWjvPBYGa43gBFekm1bKoJVktE%2B9q%2BmbgvZgGtYzoBFJiZa7GJQP%2BuEk7Cn3hViGUcqt2lSHHVdnP74iDeswqouYvQY6pgFuddG%2BedQZNHNtiUXd7kfnz%2BC9J1s3WuFrw5UOFIYxeIvLgvzZEKwz%2Fw8dA7Xd1yRjr1A7S1w5SscWyg2XkQ2FZaeSURTRji76Q5oXEAFe2u%2FT3BM41zgUOXsumzHnrj9lTdTJ6iZPujNosYo3h5i7OQH87%2Bvis4e6yN%2BpsvJJbpgU85ERs91TKgUUg9brvumRen1WA%2FCKZR%2FTww3VjLwJ%2F39uKPvO&X-Amz-Signature=cfe89e375bfcb7cc086c8002600e47c2bbd0b0cc3739b2aa4f0764ad91c5376e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YUKU3XM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBxw2E9pkWdCy0tlVYj0%2FW7Pc8bdTVfoOzSbGF9g%2FbD4AiBQ7IPjkta8CbSDAgBVPOgNNZneTsxxxgQnkuXttIm6KSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMsa%2B5NhUXRGMJPfetKtwD9uZPawrzIXCpIBJawrfYDnr7RVrRorJRm9BbsXQ3knVHiQP7t7R4ANwOaCkVfzBCJmOOac4hsmcz31fTy65AVkvLADlOhbcS07CTNUPA85OOYMftq2SZIeiUQFEc7y0IGouWnb1TbIChnHGaAv9kpNrtjpGgmTYlsGKQwqSn0harnLYlgjalMFchf4JMOJ5shlGKQxJAHy3S0yR%2FUJPW48ejP2gt%2B9QHiJcorteeR95AY2kVw0zZKlAAzswA%2BnmzLZeZWPw1NTUB0XayfwidJBkVYlJmiUKjy9PF9zgDaIk0M7q9otMSAaymITfwGRof2zfX9ci%2FNm4Jp9VRkG4GpbMrzr6moOtR4UH77fnUlgif6AupV81y7LXmOYhhOupf6X3Q3xPwvs7Kya7a0yVOvmg6zTl3O7iYBUBXb4GOJg60EMf5prIH%2FdkBw4FgGgjmQMq3DT8kqIxfIv%2FrRK0h6jIKBI36gGAx1Rj4d6viwIUW2iotaXTk%2BCRusdbyamvvgI769EJBWQ9MTi9xl5YpSzphd1Tk2skA3emfwyZCLWjvPBYGa43gBFekm1bKoJVktE%2B9q%2BmbgvZgGtYzoBFJiZa7GJQP%2BuEk7Cn3hViGUcqt2lSHHVdnP74iDeswqouYvQY6pgFuddG%2BedQZNHNtiUXd7kfnz%2BC9J1s3WuFrw5UOFIYxeIvLgvzZEKwz%2Fw8dA7Xd1yRjr1A7S1w5SscWyg2XkQ2FZaeSURTRji76Q5oXEAFe2u%2FT3BM41zgUOXsumzHnrj9lTdTJ6iZPujNosYo3h5i7OQH87%2Bvis4e6yN%2BpsvJJbpgU85ERs91TKgUUg9brvumRen1WA%2FCKZR%2FTww3VjLwJ%2F39uKPvO&X-Amz-Signature=f556e26faf74619effc4382f89050c7f39c57862b04c159c507088f13617b6dd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YUKU3XM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBxw2E9pkWdCy0tlVYj0%2FW7Pc8bdTVfoOzSbGF9g%2FbD4AiBQ7IPjkta8CbSDAgBVPOgNNZneTsxxxgQnkuXttIm6KSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMsa%2B5NhUXRGMJPfetKtwD9uZPawrzIXCpIBJawrfYDnr7RVrRorJRm9BbsXQ3knVHiQP7t7R4ANwOaCkVfzBCJmOOac4hsmcz31fTy65AVkvLADlOhbcS07CTNUPA85OOYMftq2SZIeiUQFEc7y0IGouWnb1TbIChnHGaAv9kpNrtjpGgmTYlsGKQwqSn0harnLYlgjalMFchf4JMOJ5shlGKQxJAHy3S0yR%2FUJPW48ejP2gt%2B9QHiJcorteeR95AY2kVw0zZKlAAzswA%2BnmzLZeZWPw1NTUB0XayfwidJBkVYlJmiUKjy9PF9zgDaIk0M7q9otMSAaymITfwGRof2zfX9ci%2FNm4Jp9VRkG4GpbMrzr6moOtR4UH77fnUlgif6AupV81y7LXmOYhhOupf6X3Q3xPwvs7Kya7a0yVOvmg6zTl3O7iYBUBXb4GOJg60EMf5prIH%2FdkBw4FgGgjmQMq3DT8kqIxfIv%2FrRK0h6jIKBI36gGAx1Rj4d6viwIUW2iotaXTk%2BCRusdbyamvvgI769EJBWQ9MTi9xl5YpSzphd1Tk2skA3emfwyZCLWjvPBYGa43gBFekm1bKoJVktE%2B9q%2BmbgvZgGtYzoBFJiZa7GJQP%2BuEk7Cn3hViGUcqt2lSHHVdnP74iDeswqouYvQY6pgFuddG%2BedQZNHNtiUXd7kfnz%2BC9J1s3WuFrw5UOFIYxeIvLgvzZEKwz%2Fw8dA7Xd1yRjr1A7S1w5SscWyg2XkQ2FZaeSURTRji76Q5oXEAFe2u%2FT3BM41zgUOXsumzHnrj9lTdTJ6iZPujNosYo3h5i7OQH87%2Bvis4e6yN%2BpsvJJbpgU85ERs91TKgUUg9brvumRen1WA%2FCKZR%2FTww3VjLwJ%2F39uKPvO&X-Amz-Signature=c547fae3b63899f69b65ea95901f740708cc1effb9a7a4e3af1c3e2fb206d509&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YUKU3XM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBxw2E9pkWdCy0tlVYj0%2FW7Pc8bdTVfoOzSbGF9g%2FbD4AiBQ7IPjkta8CbSDAgBVPOgNNZneTsxxxgQnkuXttIm6KSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMsa%2B5NhUXRGMJPfetKtwD9uZPawrzIXCpIBJawrfYDnr7RVrRorJRm9BbsXQ3knVHiQP7t7R4ANwOaCkVfzBCJmOOac4hsmcz31fTy65AVkvLADlOhbcS07CTNUPA85OOYMftq2SZIeiUQFEc7y0IGouWnb1TbIChnHGaAv9kpNrtjpGgmTYlsGKQwqSn0harnLYlgjalMFchf4JMOJ5shlGKQxJAHy3S0yR%2FUJPW48ejP2gt%2B9QHiJcorteeR95AY2kVw0zZKlAAzswA%2BnmzLZeZWPw1NTUB0XayfwidJBkVYlJmiUKjy9PF9zgDaIk0M7q9otMSAaymITfwGRof2zfX9ci%2FNm4Jp9VRkG4GpbMrzr6moOtR4UH77fnUlgif6AupV81y7LXmOYhhOupf6X3Q3xPwvs7Kya7a0yVOvmg6zTl3O7iYBUBXb4GOJg60EMf5prIH%2FdkBw4FgGgjmQMq3DT8kqIxfIv%2FrRK0h6jIKBI36gGAx1Rj4d6viwIUW2iotaXTk%2BCRusdbyamvvgI769EJBWQ9MTi9xl5YpSzphd1Tk2skA3emfwyZCLWjvPBYGa43gBFekm1bKoJVktE%2B9q%2BmbgvZgGtYzoBFJiZa7GJQP%2BuEk7Cn3hViGUcqt2lSHHVdnP74iDeswqouYvQY6pgFuddG%2BedQZNHNtiUXd7kfnz%2BC9J1s3WuFrw5UOFIYxeIvLgvzZEKwz%2Fw8dA7Xd1yRjr1A7S1w5SscWyg2XkQ2FZaeSURTRji76Q5oXEAFe2u%2FT3BM41zgUOXsumzHnrj9lTdTJ6iZPujNosYo3h5i7OQH87%2Bvis4e6yN%2BpsvJJbpgU85ERs91TKgUUg9brvumRen1WA%2FCKZR%2FTww3VjLwJ%2F39uKPvO&X-Amz-Signature=886055fbf456f0208a5f8e022a0850450680e4ca3d2eb1b4dd88fd9a57554fcf&X-Amz-SignedHeaders=host&x-id=GetObject)
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


