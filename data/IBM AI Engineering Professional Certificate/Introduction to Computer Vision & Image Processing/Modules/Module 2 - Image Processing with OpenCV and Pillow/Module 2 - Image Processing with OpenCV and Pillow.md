

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RHE7YPX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW3bCd8t0B%2BK9P5YPxWkb%2Fc0yV5CPsSLmPb%2Bik4hU7rAIhANg9Do%2BkBZVb9ZqtiK1mPyipGx5YFeviyRzk0YdxMTjpKv8DCBQQABoMNjM3NDIzMTgzODA1IgzhzZz1h3%2FVYznVSj0q3AO7UtF2XgnW4qpBsEG6D7vSvmw4ErJa9xp19twJ05ijj5yvRxJA2%2F%2F6J0nbdIfdnUWYEjWblX0rY7XcH22GU8hsYB6T1N%2Bw11N42BxAxjN8%2BHgJ1ToY%2Bp%2B5gAdVwajq1JYPzTOzoVKZRlHp2vj7srhBPZ%2FewRHOFPDCTrL76H9eYw8368RA1BPGKO0IZOcKlqGIjPJItj5panNjgrJvIHkL96CG8aSWNELPMh6loBHGjvE6ODVulx0aPzfGEUVCpZIv%2F4HDi3sGpwS5tr%2BC4c6dKGkUZ4vTZjk%2F1%2Bz5MvWPsuRcqFqfuag%2BwgVK560c5N95q07SK%2FdWcXVxB1OnSW6xCD7aZgrZQsueTGNM%2F%2FZ6jU32PDi0wF5V5lsFBPJHsowmjYBgpq5JxvU03Ey2x11UW%2BQq%2Fj5QqrtO2XgSQw8KBFBHByBg%2BJF%2FbJ4kuqYMT8yBrhnQrIT9uJMWKCDvvh0iemXu96tL7uNocWCXLHng7ND2z20qtMSpezQaXvxdnux53Ce4rNclaZ3zfgB9g6NiWyx02XlcR9IBInvalbksAdTjnje9l3%2BQe7hnf6YrYZWqbwOcKoa2ytJ3%2Bwz4AN8vkstns7%2BmehP9Dci5RaJC4m891ARoFA8UIpRflzCRtYK9BjqkASIQlV1mc58I7c3oi9me0pxE2ipqynNqIGb9SnZk6gA8zqrnmQt4Bs%2Bti1IaKrltW8vZQgtD0V3TOCjl8aIoeBA160gt8R89sRlmRpi%2BQHwm7f0FJ9cxCHEqNomSZyLIYkFqwfmLp2AriDfZMtOMPtaYSrSNb06SlkGcOGEGmCCcahhCY%2Bx4L0YqZypH%2FhjDwxPvGdppP%2F7QslTk3SD9FMnJULNS&X-Amz-Signature=b0591f04927ab2bca01ff5f24aaaea9f381b8dfcc7d2322b1cd50f36e05613ab&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBTYG4RC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCr0BVYw66yFgVygS1iO1YTi%2Fgg03zNIBznet0U0fO2OQIhALdRvxBzdbQnV0fg5QLwTR5tfcsU7CJVoPU%2F17%2BnnTraKv8DCBQQABoMNjM3NDIzMTgzODA1IgzsyzaU%2FzJM6f7MDMgq3AM%2B0YqZ3tJozfpoXcKHEpaYU3CeGHrIg2kUqvxNVoOhJJAwaaYmUthQSKhJY%2BeC2aaCSKS%2B8%2B50PrCDUvpkW5KxYvnUgDhRP%2F8c2GN4UUM4HaeJpvvW%2F%2FQtoHEYmZ72naD4OT0Q531X3LnGPrJbSReECu4cqZsuPjSEVgNl%2BtXEzYAvZ0LAbzIhy5FceKFoI6lPCviMOzkbAslPmPZsG88xBBlJmxImHGF3xO%2BNhfNexJ5SCacehxuS38h3f4oZxnODxw7oYcgkdgmXV%2F2WA8GScM8dI5V3Q9D%2F8XMf9VWNww4Hwrpc2oVSOHcTh8IbR%2BZ1jlO9fo%2BMBL8zOAwdMEC1XeVarQAlBOYsQUGNJcxD5jDsG2vDZu1NCWvB0zsSWuDl61N63%2FJA0qlF1dw%2Bki6XcXVt35RRdHIEXUFEND%2Fy7J%2FSM3VDovCjaWDAAV%2FNjuorWWnRAuExo5s6mvyZrTQjzh%2Fo5bFNam4Lkrgiw%2FF4S64ZozG8jkTuDYqicVnw8ZGMkA%2FEFK%2Bn40CYhp3yP0azDPgLUK73el5zPO4DHcClUcsztJ%2F8dq6qTmKb32HJ1Nd%2BjcZlgIZBZCZVjbTtUBuvnlDLeHG2Frb6E70QXpwuEC0ko3MzfUJVaqkO6zDatIK9BjqkASTBRzo6cw%2Fq2Gzlq%2Bl69ds1rnTbTM1B7b8dUzi7%2B1qJATAjgdaLuJbvrdo%2FV0sMcSyFCIj9Hjry6NY47Ed3rgul0XJHKt9%2Frc7Ql1xIgOR7apUsFCa9ClkB%2FsBLGBvQnb2ib2T4N5KGup7Ji0EX1OvRHRo1aWeRe%2BTsxYFu3iGBmPoyzCz%2FCDtvKxGKX1PD97TgzyEN%2B0uoJqvSST3jWGjQjluR&X-Amz-Signature=a4a4693e089481b0adebe46263f18f8e1bbd7b78bcff5a82b83559d65a5e0be1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBTYG4RC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCr0BVYw66yFgVygS1iO1YTi%2Fgg03zNIBznet0U0fO2OQIhALdRvxBzdbQnV0fg5QLwTR5tfcsU7CJVoPU%2F17%2BnnTraKv8DCBQQABoMNjM3NDIzMTgzODA1IgzsyzaU%2FzJM6f7MDMgq3AM%2B0YqZ3tJozfpoXcKHEpaYU3CeGHrIg2kUqvxNVoOhJJAwaaYmUthQSKhJY%2BeC2aaCSKS%2B8%2B50PrCDUvpkW5KxYvnUgDhRP%2F8c2GN4UUM4HaeJpvvW%2F%2FQtoHEYmZ72naD4OT0Q531X3LnGPrJbSReECu4cqZsuPjSEVgNl%2BtXEzYAvZ0LAbzIhy5FceKFoI6lPCviMOzkbAslPmPZsG88xBBlJmxImHGF3xO%2BNhfNexJ5SCacehxuS38h3f4oZxnODxw7oYcgkdgmXV%2F2WA8GScM8dI5V3Q9D%2F8XMf9VWNww4Hwrpc2oVSOHcTh8IbR%2BZ1jlO9fo%2BMBL8zOAwdMEC1XeVarQAlBOYsQUGNJcxD5jDsG2vDZu1NCWvB0zsSWuDl61N63%2FJA0qlF1dw%2Bki6XcXVt35RRdHIEXUFEND%2Fy7J%2FSM3VDovCjaWDAAV%2FNjuorWWnRAuExo5s6mvyZrTQjzh%2Fo5bFNam4Lkrgiw%2FF4S64ZozG8jkTuDYqicVnw8ZGMkA%2FEFK%2Bn40CYhp3yP0azDPgLUK73el5zPO4DHcClUcsztJ%2F8dq6qTmKb32HJ1Nd%2BjcZlgIZBZCZVjbTtUBuvnlDLeHG2Frb6E70QXpwuEC0ko3MzfUJVaqkO6zDatIK9BjqkASTBRzo6cw%2Fq2Gzlq%2Bl69ds1rnTbTM1B7b8dUzi7%2B1qJATAjgdaLuJbvrdo%2FV0sMcSyFCIj9Hjry6NY47Ed3rgul0XJHKt9%2Frc7Ql1xIgOR7apUsFCa9ClkB%2FsBLGBvQnb2ib2T4N5KGup7Ji0EX1OvRHRo1aWeRe%2BTsxYFu3iGBmPoyzCz%2FCDtvKxGKX1PD97TgzyEN%2B0uoJqvSST3jWGjQjluR&X-Amz-Signature=5826cd06ed2085945e415cb6ed3c91e144ed3501d03a07afd7df7d79898e70a9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBTYG4RC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCr0BVYw66yFgVygS1iO1YTi%2Fgg03zNIBznet0U0fO2OQIhALdRvxBzdbQnV0fg5QLwTR5tfcsU7CJVoPU%2F17%2BnnTraKv8DCBQQABoMNjM3NDIzMTgzODA1IgzsyzaU%2FzJM6f7MDMgq3AM%2B0YqZ3tJozfpoXcKHEpaYU3CeGHrIg2kUqvxNVoOhJJAwaaYmUthQSKhJY%2BeC2aaCSKS%2B8%2B50PrCDUvpkW5KxYvnUgDhRP%2F8c2GN4UUM4HaeJpvvW%2F%2FQtoHEYmZ72naD4OT0Q531X3LnGPrJbSReECu4cqZsuPjSEVgNl%2BtXEzYAvZ0LAbzIhy5FceKFoI6lPCviMOzkbAslPmPZsG88xBBlJmxImHGF3xO%2BNhfNexJ5SCacehxuS38h3f4oZxnODxw7oYcgkdgmXV%2F2WA8GScM8dI5V3Q9D%2F8XMf9VWNww4Hwrpc2oVSOHcTh8IbR%2BZ1jlO9fo%2BMBL8zOAwdMEC1XeVarQAlBOYsQUGNJcxD5jDsG2vDZu1NCWvB0zsSWuDl61N63%2FJA0qlF1dw%2Bki6XcXVt35RRdHIEXUFEND%2Fy7J%2FSM3VDovCjaWDAAV%2FNjuorWWnRAuExo5s6mvyZrTQjzh%2Fo5bFNam4Lkrgiw%2FF4S64ZozG8jkTuDYqicVnw8ZGMkA%2FEFK%2Bn40CYhp3yP0azDPgLUK73el5zPO4DHcClUcsztJ%2F8dq6qTmKb32HJ1Nd%2BjcZlgIZBZCZVjbTtUBuvnlDLeHG2Frb6E70QXpwuEC0ko3MzfUJVaqkO6zDatIK9BjqkASTBRzo6cw%2Fq2Gzlq%2Bl69ds1rnTbTM1B7b8dUzi7%2B1qJATAjgdaLuJbvrdo%2FV0sMcSyFCIj9Hjry6NY47Ed3rgul0XJHKt9%2Frc7Ql1xIgOR7apUsFCa9ClkB%2FsBLGBvQnb2ib2T4N5KGup7Ji0EX1OvRHRo1aWeRe%2BTsxYFu3iGBmPoyzCz%2FCDtvKxGKX1PD97TgzyEN%2B0uoJqvSST3jWGjQjluR&X-Amz-Signature=bc3f530b00cbfbfcd403aa3b82ba4143031823017bd2fabef18f7ae47c647bb4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBTYG4RC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCr0BVYw66yFgVygS1iO1YTi%2Fgg03zNIBznet0U0fO2OQIhALdRvxBzdbQnV0fg5QLwTR5tfcsU7CJVoPU%2F17%2BnnTraKv8DCBQQABoMNjM3NDIzMTgzODA1IgzsyzaU%2FzJM6f7MDMgq3AM%2B0YqZ3tJozfpoXcKHEpaYU3CeGHrIg2kUqvxNVoOhJJAwaaYmUthQSKhJY%2BeC2aaCSKS%2B8%2B50PrCDUvpkW5KxYvnUgDhRP%2F8c2GN4UUM4HaeJpvvW%2F%2FQtoHEYmZ72naD4OT0Q531X3LnGPrJbSReECu4cqZsuPjSEVgNl%2BtXEzYAvZ0LAbzIhy5FceKFoI6lPCviMOzkbAslPmPZsG88xBBlJmxImHGF3xO%2BNhfNexJ5SCacehxuS38h3f4oZxnODxw7oYcgkdgmXV%2F2WA8GScM8dI5V3Q9D%2F8XMf9VWNww4Hwrpc2oVSOHcTh8IbR%2BZ1jlO9fo%2BMBL8zOAwdMEC1XeVarQAlBOYsQUGNJcxD5jDsG2vDZu1NCWvB0zsSWuDl61N63%2FJA0qlF1dw%2Bki6XcXVt35RRdHIEXUFEND%2Fy7J%2FSM3VDovCjaWDAAV%2FNjuorWWnRAuExo5s6mvyZrTQjzh%2Fo5bFNam4Lkrgiw%2FF4S64ZozG8jkTuDYqicVnw8ZGMkA%2FEFK%2Bn40CYhp3yP0azDPgLUK73el5zPO4DHcClUcsztJ%2F8dq6qTmKb32HJ1Nd%2BjcZlgIZBZCZVjbTtUBuvnlDLeHG2Frb6E70QXpwuEC0ko3MzfUJVaqkO6zDatIK9BjqkASTBRzo6cw%2Fq2Gzlq%2Bl69ds1rnTbTM1B7b8dUzi7%2B1qJATAjgdaLuJbvrdo%2FV0sMcSyFCIj9Hjry6NY47Ed3rgul0XJHKt9%2Frc7Ql1xIgOR7apUsFCa9ClkB%2FsBLGBvQnb2ib2T4N5KGup7Ji0EX1OvRHRo1aWeRe%2BTsxYFu3iGBmPoyzCz%2FCDtvKxGKX1PD97TgzyEN%2B0uoJqvSST3jWGjQjluR&X-Amz-Signature=9711e252a21b551069f38432461e187b0546f275d841414194bab6c21545cedc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBTYG4RC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCr0BVYw66yFgVygS1iO1YTi%2Fgg03zNIBznet0U0fO2OQIhALdRvxBzdbQnV0fg5QLwTR5tfcsU7CJVoPU%2F17%2BnnTraKv8DCBQQABoMNjM3NDIzMTgzODA1IgzsyzaU%2FzJM6f7MDMgq3AM%2B0YqZ3tJozfpoXcKHEpaYU3CeGHrIg2kUqvxNVoOhJJAwaaYmUthQSKhJY%2BeC2aaCSKS%2B8%2B50PrCDUvpkW5KxYvnUgDhRP%2F8c2GN4UUM4HaeJpvvW%2F%2FQtoHEYmZ72naD4OT0Q531X3LnGPrJbSReECu4cqZsuPjSEVgNl%2BtXEzYAvZ0LAbzIhy5FceKFoI6lPCviMOzkbAslPmPZsG88xBBlJmxImHGF3xO%2BNhfNexJ5SCacehxuS38h3f4oZxnODxw7oYcgkdgmXV%2F2WA8GScM8dI5V3Q9D%2F8XMf9VWNww4Hwrpc2oVSOHcTh8IbR%2BZ1jlO9fo%2BMBL8zOAwdMEC1XeVarQAlBOYsQUGNJcxD5jDsG2vDZu1NCWvB0zsSWuDl61N63%2FJA0qlF1dw%2Bki6XcXVt35RRdHIEXUFEND%2Fy7J%2FSM3VDovCjaWDAAV%2FNjuorWWnRAuExo5s6mvyZrTQjzh%2Fo5bFNam4Lkrgiw%2FF4S64ZozG8jkTuDYqicVnw8ZGMkA%2FEFK%2Bn40CYhp3yP0azDPgLUK73el5zPO4DHcClUcsztJ%2F8dq6qTmKb32HJ1Nd%2BjcZlgIZBZCZVjbTtUBuvnlDLeHG2Frb6E70QXpwuEC0ko3MzfUJVaqkO6zDatIK9BjqkASTBRzo6cw%2Fq2Gzlq%2Bl69ds1rnTbTM1B7b8dUzi7%2B1qJATAjgdaLuJbvrdo%2FV0sMcSyFCIj9Hjry6NY47Ed3rgul0XJHKt9%2Frc7Ql1xIgOR7apUsFCa9ClkB%2FsBLGBvQnb2ib2T4N5KGup7Ji0EX1OvRHRo1aWeRe%2BTsxYFu3iGBmPoyzCz%2FCDtvKxGKX1PD97TgzyEN%2B0uoJqvSST3jWGjQjluR&X-Amz-Signature=9e04c8e4786c3f69331d895eaeb862d253bb5ee0f7fac592582bdec1bdf9f7e8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RHE7YPX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW3bCd8t0B%2BK9P5YPxWkb%2Fc0yV5CPsSLmPb%2Bik4hU7rAIhANg9Do%2BkBZVb9ZqtiK1mPyipGx5YFeviyRzk0YdxMTjpKv8DCBQQABoMNjM3NDIzMTgzODA1IgzhzZz1h3%2FVYznVSj0q3AO7UtF2XgnW4qpBsEG6D7vSvmw4ErJa9xp19twJ05ijj5yvRxJA2%2F%2F6J0nbdIfdnUWYEjWblX0rY7XcH22GU8hsYB6T1N%2Bw11N42BxAxjN8%2BHgJ1ToY%2Bp%2B5gAdVwajq1JYPzTOzoVKZRlHp2vj7srhBPZ%2FewRHOFPDCTrL76H9eYw8368RA1BPGKO0IZOcKlqGIjPJItj5panNjgrJvIHkL96CG8aSWNELPMh6loBHGjvE6ODVulx0aPzfGEUVCpZIv%2F4HDi3sGpwS5tr%2BC4c6dKGkUZ4vTZjk%2F1%2Bz5MvWPsuRcqFqfuag%2BwgVK560c5N95q07SK%2FdWcXVxB1OnSW6xCD7aZgrZQsueTGNM%2F%2FZ6jU32PDi0wF5V5lsFBPJHsowmjYBgpq5JxvU03Ey2x11UW%2BQq%2Fj5QqrtO2XgSQw8KBFBHByBg%2BJF%2FbJ4kuqYMT8yBrhnQrIT9uJMWKCDvvh0iemXu96tL7uNocWCXLHng7ND2z20qtMSpezQaXvxdnux53Ce4rNclaZ3zfgB9g6NiWyx02XlcR9IBInvalbksAdTjnje9l3%2BQe7hnf6YrYZWqbwOcKoa2ytJ3%2Bwz4AN8vkstns7%2BmehP9Dci5RaJC4m891ARoFA8UIpRflzCRtYK9BjqkASIQlV1mc58I7c3oi9me0pxE2ipqynNqIGb9SnZk6gA8zqrnmQt4Bs%2Bti1IaKrltW8vZQgtD0V3TOCjl8aIoeBA160gt8R89sRlmRpi%2BQHwm7f0FJ9cxCHEqNomSZyLIYkFqwfmLp2AriDfZMtOMPtaYSrSNb06SlkGcOGEGmCCcahhCY%2Bx4L0YqZypH%2FhjDwxPvGdppP%2F7QslTk3SD9FMnJULNS&X-Amz-Signature=466b15ccda2948713139128698a1f1844decbc71db41d3bdaccb0ee9ae4ba868&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RHE7YPX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW3bCd8t0B%2BK9P5YPxWkb%2Fc0yV5CPsSLmPb%2Bik4hU7rAIhANg9Do%2BkBZVb9ZqtiK1mPyipGx5YFeviyRzk0YdxMTjpKv8DCBQQABoMNjM3NDIzMTgzODA1IgzhzZz1h3%2FVYznVSj0q3AO7UtF2XgnW4qpBsEG6D7vSvmw4ErJa9xp19twJ05ijj5yvRxJA2%2F%2F6J0nbdIfdnUWYEjWblX0rY7XcH22GU8hsYB6T1N%2Bw11N42BxAxjN8%2BHgJ1ToY%2Bp%2B5gAdVwajq1JYPzTOzoVKZRlHp2vj7srhBPZ%2FewRHOFPDCTrL76H9eYw8368RA1BPGKO0IZOcKlqGIjPJItj5panNjgrJvIHkL96CG8aSWNELPMh6loBHGjvE6ODVulx0aPzfGEUVCpZIv%2F4HDi3sGpwS5tr%2BC4c6dKGkUZ4vTZjk%2F1%2Bz5MvWPsuRcqFqfuag%2BwgVK560c5N95q07SK%2FdWcXVxB1OnSW6xCD7aZgrZQsueTGNM%2F%2FZ6jU32PDi0wF5V5lsFBPJHsowmjYBgpq5JxvU03Ey2x11UW%2BQq%2Fj5QqrtO2XgSQw8KBFBHByBg%2BJF%2FbJ4kuqYMT8yBrhnQrIT9uJMWKCDvvh0iemXu96tL7uNocWCXLHng7ND2z20qtMSpezQaXvxdnux53Ce4rNclaZ3zfgB9g6NiWyx02XlcR9IBInvalbksAdTjnje9l3%2BQe7hnf6YrYZWqbwOcKoa2ytJ3%2Bwz4AN8vkstns7%2BmehP9Dci5RaJC4m891ARoFA8UIpRflzCRtYK9BjqkASIQlV1mc58I7c3oi9me0pxE2ipqynNqIGb9SnZk6gA8zqrnmQt4Bs%2Bti1IaKrltW8vZQgtD0V3TOCjl8aIoeBA160gt8R89sRlmRpi%2BQHwm7f0FJ9cxCHEqNomSZyLIYkFqwfmLp2AriDfZMtOMPtaYSrSNb06SlkGcOGEGmCCcahhCY%2Bx4L0YqZypH%2FhjDwxPvGdppP%2F7QslTk3SD9FMnJULNS&X-Amz-Signature=28433beb4dcd94c2757769d56186d284e713e467c796adbe038ca3d30743ddb7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RHE7YPX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW3bCd8t0B%2BK9P5YPxWkb%2Fc0yV5CPsSLmPb%2Bik4hU7rAIhANg9Do%2BkBZVb9ZqtiK1mPyipGx5YFeviyRzk0YdxMTjpKv8DCBQQABoMNjM3NDIzMTgzODA1IgzhzZz1h3%2FVYznVSj0q3AO7UtF2XgnW4qpBsEG6D7vSvmw4ErJa9xp19twJ05ijj5yvRxJA2%2F%2F6J0nbdIfdnUWYEjWblX0rY7XcH22GU8hsYB6T1N%2Bw11N42BxAxjN8%2BHgJ1ToY%2Bp%2B5gAdVwajq1JYPzTOzoVKZRlHp2vj7srhBPZ%2FewRHOFPDCTrL76H9eYw8368RA1BPGKO0IZOcKlqGIjPJItj5panNjgrJvIHkL96CG8aSWNELPMh6loBHGjvE6ODVulx0aPzfGEUVCpZIv%2F4HDi3sGpwS5tr%2BC4c6dKGkUZ4vTZjk%2F1%2Bz5MvWPsuRcqFqfuag%2BwgVK560c5N95q07SK%2FdWcXVxB1OnSW6xCD7aZgrZQsueTGNM%2F%2FZ6jU32PDi0wF5V5lsFBPJHsowmjYBgpq5JxvU03Ey2x11UW%2BQq%2Fj5QqrtO2XgSQw8KBFBHByBg%2BJF%2FbJ4kuqYMT8yBrhnQrIT9uJMWKCDvvh0iemXu96tL7uNocWCXLHng7ND2z20qtMSpezQaXvxdnux53Ce4rNclaZ3zfgB9g6NiWyx02XlcR9IBInvalbksAdTjnje9l3%2BQe7hnf6YrYZWqbwOcKoa2ytJ3%2Bwz4AN8vkstns7%2BmehP9Dci5RaJC4m891ARoFA8UIpRflzCRtYK9BjqkASIQlV1mc58I7c3oi9me0pxE2ipqynNqIGb9SnZk6gA8zqrnmQt4Bs%2Bti1IaKrltW8vZQgtD0V3TOCjl8aIoeBA160gt8R89sRlmRpi%2BQHwm7f0FJ9cxCHEqNomSZyLIYkFqwfmLp2AriDfZMtOMPtaYSrSNb06SlkGcOGEGmCCcahhCY%2Bx4L0YqZypH%2FhjDwxPvGdppP%2F7QslTk3SD9FMnJULNS&X-Amz-Signature=da804b838cbda430a4a38c8b19865c86e0368fb0c6d25616521bfc28ba473354&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RHE7YPX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW3bCd8t0B%2BK9P5YPxWkb%2Fc0yV5CPsSLmPb%2Bik4hU7rAIhANg9Do%2BkBZVb9ZqtiK1mPyipGx5YFeviyRzk0YdxMTjpKv8DCBQQABoMNjM3NDIzMTgzODA1IgzhzZz1h3%2FVYznVSj0q3AO7UtF2XgnW4qpBsEG6D7vSvmw4ErJa9xp19twJ05ijj5yvRxJA2%2F%2F6J0nbdIfdnUWYEjWblX0rY7XcH22GU8hsYB6T1N%2Bw11N42BxAxjN8%2BHgJ1ToY%2Bp%2B5gAdVwajq1JYPzTOzoVKZRlHp2vj7srhBPZ%2FewRHOFPDCTrL76H9eYw8368RA1BPGKO0IZOcKlqGIjPJItj5panNjgrJvIHkL96CG8aSWNELPMh6loBHGjvE6ODVulx0aPzfGEUVCpZIv%2F4HDi3sGpwS5tr%2BC4c6dKGkUZ4vTZjk%2F1%2Bz5MvWPsuRcqFqfuag%2BwgVK560c5N95q07SK%2FdWcXVxB1OnSW6xCD7aZgrZQsueTGNM%2F%2FZ6jU32PDi0wF5V5lsFBPJHsowmjYBgpq5JxvU03Ey2x11UW%2BQq%2Fj5QqrtO2XgSQw8KBFBHByBg%2BJF%2FbJ4kuqYMT8yBrhnQrIT9uJMWKCDvvh0iemXu96tL7uNocWCXLHng7ND2z20qtMSpezQaXvxdnux53Ce4rNclaZ3zfgB9g6NiWyx02XlcR9IBInvalbksAdTjnje9l3%2BQe7hnf6YrYZWqbwOcKoa2ytJ3%2Bwz4AN8vkstns7%2BmehP9Dci5RaJC4m891ARoFA8UIpRflzCRtYK9BjqkASIQlV1mc58I7c3oi9me0pxE2ipqynNqIGb9SnZk6gA8zqrnmQt4Bs%2Bti1IaKrltW8vZQgtD0V3TOCjl8aIoeBA160gt8R89sRlmRpi%2BQHwm7f0FJ9cxCHEqNomSZyLIYkFqwfmLp2AriDfZMtOMPtaYSrSNb06SlkGcOGEGmCCcahhCY%2Bx4L0YqZypH%2FhjDwxPvGdppP%2F7QslTk3SD9FMnJULNS&X-Amz-Signature=112d696f66c63e791f2dd4c24ec6bee9cf3c4858320ed72968e024f7e5b96681&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RHE7YPX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW3bCd8t0B%2BK9P5YPxWkb%2Fc0yV5CPsSLmPb%2Bik4hU7rAIhANg9Do%2BkBZVb9ZqtiK1mPyipGx5YFeviyRzk0YdxMTjpKv8DCBQQABoMNjM3NDIzMTgzODA1IgzhzZz1h3%2FVYznVSj0q3AO7UtF2XgnW4qpBsEG6D7vSvmw4ErJa9xp19twJ05ijj5yvRxJA2%2F%2F6J0nbdIfdnUWYEjWblX0rY7XcH22GU8hsYB6T1N%2Bw11N42BxAxjN8%2BHgJ1ToY%2Bp%2B5gAdVwajq1JYPzTOzoVKZRlHp2vj7srhBPZ%2FewRHOFPDCTrL76H9eYw8368RA1BPGKO0IZOcKlqGIjPJItj5panNjgrJvIHkL96CG8aSWNELPMh6loBHGjvE6ODVulx0aPzfGEUVCpZIv%2F4HDi3sGpwS5tr%2BC4c6dKGkUZ4vTZjk%2F1%2Bz5MvWPsuRcqFqfuag%2BwgVK560c5N95q07SK%2FdWcXVxB1OnSW6xCD7aZgrZQsueTGNM%2F%2FZ6jU32PDi0wF5V5lsFBPJHsowmjYBgpq5JxvU03Ey2x11UW%2BQq%2Fj5QqrtO2XgSQw8KBFBHByBg%2BJF%2FbJ4kuqYMT8yBrhnQrIT9uJMWKCDvvh0iemXu96tL7uNocWCXLHng7ND2z20qtMSpezQaXvxdnux53Ce4rNclaZ3zfgB9g6NiWyx02XlcR9IBInvalbksAdTjnje9l3%2BQe7hnf6YrYZWqbwOcKoa2ytJ3%2Bwz4AN8vkstns7%2BmehP9Dci5RaJC4m891ARoFA8UIpRflzCRtYK9BjqkASIQlV1mc58I7c3oi9me0pxE2ipqynNqIGb9SnZk6gA8zqrnmQt4Bs%2Bti1IaKrltW8vZQgtD0V3TOCjl8aIoeBA160gt8R89sRlmRpi%2BQHwm7f0FJ9cxCHEqNomSZyLIYkFqwfmLp2AriDfZMtOMPtaYSrSNb06SlkGcOGEGmCCcahhCY%2Bx4L0YqZypH%2FhjDwxPvGdppP%2F7QslTk3SD9FMnJULNS&X-Amz-Signature=64be6bada721c162b75d6d4d872ce54aafcb421dec0f6bc5d2c28051051a8c3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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


