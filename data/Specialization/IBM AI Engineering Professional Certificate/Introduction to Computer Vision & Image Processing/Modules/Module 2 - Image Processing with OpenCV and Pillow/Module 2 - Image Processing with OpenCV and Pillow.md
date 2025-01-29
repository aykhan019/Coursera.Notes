

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFUWIE43%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEDcPQMt7G%2Fn9NyZD7hTUT1mb3gsK8QoB2OMb38ZWo7wIgQmhlSt1i6Xx3tEONc0OgtofSzDa%2BG5u21VP9XTFTm3gqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnSepOj1TU9wg554CrcA1miKrberu08LvgBtKPbkGiyqtQE3YJPAlbtkcOeNeFtWHbZ3BHi6egGrWNaHvCcgSr6I4st4Pk%2BFy3k2BKc%2FqE8EvUFYWFuDDC2mtHfQClB92CzNi7II5O3F%2FWRuRXNATfyiKqN9MpDh5oUcFnxIIDDUMwbSsF7wgmNyYh2mnniUBtvNER%2FFeSnKju%2FBBWIOpD7E9UCGiVtZE%2Bi7NNO4zxXPO929M7VyW1UQuyIvYOhO7JtJ8bXt7jGujGLb99fGjHv4jSPI4vFu4oepH%2FDu4AWLitAvjmPPtA8hhb4Qnu9dmLRP3zHJwwn9oiqIJNL8FEF1mzlZfkna%2BBK686eKYUuNSP5wxNiBnwbTbInf3xOvvhgw82Di1rqeDCwwi4I%2FsQ43BwRrL0BjL6rws7qM6FZAEP5K89Z%2B76RK3L4aSEUKdT%2F8gMfU%2F7qpLFO6B8emn4pkcD3qePLOZL%2FduHxlCEK9cqlQf%2FWO6nTmSCdqcTj9LthVVknPk25bQwbSdbz7ZdYjbhMjA8L4MYQpdPuNONrG8I7a8634waQl0FtFmt0ba1%2F332DP4kTvfoFK9O3ZxCnqO6Nz5hTFnClDXEbWo6kdbcQRiwVeXsBRSNiQqRlsycxwNFLMazWD6JzMJ7L6LwGOqUBY6i%2B%2FVd5C8vVMxFzrh8n1xtey9xkGPPdMWAwOMysQwXcQJjh3yI5GA4aq9fJEzfZOaqgcw07xlKWZ5JoUkeJiltH6MtqDSuzbQV5Qqlo24sw9TZH8agJbNtFaY5Ki7P9fOnCBfHBAciRW3GUN%2BiNTmDo4hJJEgMw%2BZ61HAhrOEB2q6r5l3Op3RD4%2F6T5vx8aeDtJOGxyycFkdqoLW2jssGOiJdwg&X-Amz-Signature=90e6f046f808941de558f11d3d896cc5aa4dbfab433876137c5f193985eba2c1&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KFF3SM7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrwcaUvJ6v3DFdA%2FAhfpg38Q%2BUo%2FSQ82XkW9hu6CmCxAIhAJl9cqnkl0Q2rUCSs1lxKRHaDgf%2BMCtJMK2EmVk%2FwDbsKogECI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJ9JQ0oxGlMU7d5xoq3AMNSBlaHM8R2aGEuglvUbORLR4KzdlDqidoIRfwQyzRgyqj%2FKCIfymH2uPjo4PgDGCkWXj6a%2BWysGAu3sO48dhDjc%2FaHhDaGq%2BQ0xHbkMh8IrjRRtpJfB7voTjZsaDsl4gQhCZ531Z%2FnrJnn62C19lbXaQ0gPX9s62WkTI1E3mBpenbLLsHf7mjTkcTx7YhvirxVm1Wj9zTvBO4S4EGiDdpXJK2oKT9%2BxNywGeEt2tFOuaaG7DUNlsInogGbSfDcQSn0bG%2Fw125pEIKXTnWENxpl9n%2Bg022EJbHVWt7UbFPjlxYzATXN95S%2F7jUE%2BD01VmLdvzlbqPZgIF8nREMmN8yqc0m5IrOZHNSDHPKXgEdZQFW0xMdk8b9Vb7XMxLXWD2Olh570d3e3gWGSQfDRnllbYNmgoF%2FSnveU2oA96%2BE8JF8M6xGZkp2xiR6a7Z%2Bm%2FftKb%2BSnemCEoeK%2FtX3NtxwJgSBKo%2FzFudBwBsF41DBWm9xGQwnlR2jL3xChUWLZDvncdHTxASDhLOYD3TxMXGZFNmyeFL%2FUgS0bcaSft%2BJx%2FuzP%2FR2iFoPsH9Et0XaWQA4%2B9E%2BYFSZmxHmRqCRsX%2FSYgmtpILSpplL59je1FNFnR53VZ41oOumoWxJ9zDoy%2Bi8BjqkAcH3vx0jwbPOs9o5fEIeoDBswrxNQL2a6qSSBtUZcdR5I4JtnUf0QrnmPGydDufWs8Df4ki6jNNxyfX%2FS3gRE60dc0cgi%2FeJ2S1gVdTT4YG9Hk6EJOeB66zwo8H0cRAy7h74%2FRK7jeTo2ULeEMR3tfPvaOUNmr377RzYIUZpnqpOgD5zrl5x%2BixHoMEF1Qqm%2FhJKau4i8r8yB%2FXC6GuObflf7VWH&X-Amz-Signature=413252f2ab0e679dfa7e9667b32c0567f51cdfa683e1b38e190d9b7aaed49f2b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KFF3SM7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrwcaUvJ6v3DFdA%2FAhfpg38Q%2BUo%2FSQ82XkW9hu6CmCxAIhAJl9cqnkl0Q2rUCSs1lxKRHaDgf%2BMCtJMK2EmVk%2FwDbsKogECI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJ9JQ0oxGlMU7d5xoq3AMNSBlaHM8R2aGEuglvUbORLR4KzdlDqidoIRfwQyzRgyqj%2FKCIfymH2uPjo4PgDGCkWXj6a%2BWysGAu3sO48dhDjc%2FaHhDaGq%2BQ0xHbkMh8IrjRRtpJfB7voTjZsaDsl4gQhCZ531Z%2FnrJnn62C19lbXaQ0gPX9s62WkTI1E3mBpenbLLsHf7mjTkcTx7YhvirxVm1Wj9zTvBO4S4EGiDdpXJK2oKT9%2BxNywGeEt2tFOuaaG7DUNlsInogGbSfDcQSn0bG%2Fw125pEIKXTnWENxpl9n%2Bg022EJbHVWt7UbFPjlxYzATXN95S%2F7jUE%2BD01VmLdvzlbqPZgIF8nREMmN8yqc0m5IrOZHNSDHPKXgEdZQFW0xMdk8b9Vb7XMxLXWD2Olh570d3e3gWGSQfDRnllbYNmgoF%2FSnveU2oA96%2BE8JF8M6xGZkp2xiR6a7Z%2Bm%2FftKb%2BSnemCEoeK%2FtX3NtxwJgSBKo%2FzFudBwBsF41DBWm9xGQwnlR2jL3xChUWLZDvncdHTxASDhLOYD3TxMXGZFNmyeFL%2FUgS0bcaSft%2BJx%2FuzP%2FR2iFoPsH9Et0XaWQA4%2B9E%2BYFSZmxHmRqCRsX%2FSYgmtpILSpplL59je1FNFnR53VZ41oOumoWxJ9zDoy%2Bi8BjqkAcH3vx0jwbPOs9o5fEIeoDBswrxNQL2a6qSSBtUZcdR5I4JtnUf0QrnmPGydDufWs8Df4ki6jNNxyfX%2FS3gRE60dc0cgi%2FeJ2S1gVdTT4YG9Hk6EJOeB66zwo8H0cRAy7h74%2FRK7jeTo2ULeEMR3tfPvaOUNmr377RzYIUZpnqpOgD5zrl5x%2BixHoMEF1Qqm%2FhJKau4i8r8yB%2FXC6GuObflf7VWH&X-Amz-Signature=ce3f960a22502bb66fd48bcd408220f92cd28d7a1bfdee66cb12c57826b92383&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KFF3SM7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrwcaUvJ6v3DFdA%2FAhfpg38Q%2BUo%2FSQ82XkW9hu6CmCxAIhAJl9cqnkl0Q2rUCSs1lxKRHaDgf%2BMCtJMK2EmVk%2FwDbsKogECI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJ9JQ0oxGlMU7d5xoq3AMNSBlaHM8R2aGEuglvUbORLR4KzdlDqidoIRfwQyzRgyqj%2FKCIfymH2uPjo4PgDGCkWXj6a%2BWysGAu3sO48dhDjc%2FaHhDaGq%2BQ0xHbkMh8IrjRRtpJfB7voTjZsaDsl4gQhCZ531Z%2FnrJnn62C19lbXaQ0gPX9s62WkTI1E3mBpenbLLsHf7mjTkcTx7YhvirxVm1Wj9zTvBO4S4EGiDdpXJK2oKT9%2BxNywGeEt2tFOuaaG7DUNlsInogGbSfDcQSn0bG%2Fw125pEIKXTnWENxpl9n%2Bg022EJbHVWt7UbFPjlxYzATXN95S%2F7jUE%2BD01VmLdvzlbqPZgIF8nREMmN8yqc0m5IrOZHNSDHPKXgEdZQFW0xMdk8b9Vb7XMxLXWD2Olh570d3e3gWGSQfDRnllbYNmgoF%2FSnveU2oA96%2BE8JF8M6xGZkp2xiR6a7Z%2Bm%2FftKb%2BSnemCEoeK%2FtX3NtxwJgSBKo%2FzFudBwBsF41DBWm9xGQwnlR2jL3xChUWLZDvncdHTxASDhLOYD3TxMXGZFNmyeFL%2FUgS0bcaSft%2BJx%2FuzP%2FR2iFoPsH9Et0XaWQA4%2B9E%2BYFSZmxHmRqCRsX%2FSYgmtpILSpplL59je1FNFnR53VZ41oOumoWxJ9zDoy%2Bi8BjqkAcH3vx0jwbPOs9o5fEIeoDBswrxNQL2a6qSSBtUZcdR5I4JtnUf0QrnmPGydDufWs8Df4ki6jNNxyfX%2FS3gRE60dc0cgi%2FeJ2S1gVdTT4YG9Hk6EJOeB66zwo8H0cRAy7h74%2FRK7jeTo2ULeEMR3tfPvaOUNmr377RzYIUZpnqpOgD5zrl5x%2BixHoMEF1Qqm%2FhJKau4i8r8yB%2FXC6GuObflf7VWH&X-Amz-Signature=419694d72645f9ce5fc8509daebe44038a7fb0a0f302ace9fca21be7d3f63514&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KFF3SM7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrwcaUvJ6v3DFdA%2FAhfpg38Q%2BUo%2FSQ82XkW9hu6CmCxAIhAJl9cqnkl0Q2rUCSs1lxKRHaDgf%2BMCtJMK2EmVk%2FwDbsKogECI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJ9JQ0oxGlMU7d5xoq3AMNSBlaHM8R2aGEuglvUbORLR4KzdlDqidoIRfwQyzRgyqj%2FKCIfymH2uPjo4PgDGCkWXj6a%2BWysGAu3sO48dhDjc%2FaHhDaGq%2BQ0xHbkMh8IrjRRtpJfB7voTjZsaDsl4gQhCZ531Z%2FnrJnn62C19lbXaQ0gPX9s62WkTI1E3mBpenbLLsHf7mjTkcTx7YhvirxVm1Wj9zTvBO4S4EGiDdpXJK2oKT9%2BxNywGeEt2tFOuaaG7DUNlsInogGbSfDcQSn0bG%2Fw125pEIKXTnWENxpl9n%2Bg022EJbHVWt7UbFPjlxYzATXN95S%2F7jUE%2BD01VmLdvzlbqPZgIF8nREMmN8yqc0m5IrOZHNSDHPKXgEdZQFW0xMdk8b9Vb7XMxLXWD2Olh570d3e3gWGSQfDRnllbYNmgoF%2FSnveU2oA96%2BE8JF8M6xGZkp2xiR6a7Z%2Bm%2FftKb%2BSnemCEoeK%2FtX3NtxwJgSBKo%2FzFudBwBsF41DBWm9xGQwnlR2jL3xChUWLZDvncdHTxASDhLOYD3TxMXGZFNmyeFL%2FUgS0bcaSft%2BJx%2FuzP%2FR2iFoPsH9Et0XaWQA4%2B9E%2BYFSZmxHmRqCRsX%2FSYgmtpILSpplL59je1FNFnR53VZ41oOumoWxJ9zDoy%2Bi8BjqkAcH3vx0jwbPOs9o5fEIeoDBswrxNQL2a6qSSBtUZcdR5I4JtnUf0QrnmPGydDufWs8Df4ki6jNNxyfX%2FS3gRE60dc0cgi%2FeJ2S1gVdTT4YG9Hk6EJOeB66zwo8H0cRAy7h74%2FRK7jeTo2ULeEMR3tfPvaOUNmr377RzYIUZpnqpOgD5zrl5x%2BixHoMEF1Qqm%2FhJKau4i8r8yB%2FXC6GuObflf7VWH&X-Amz-Signature=4d7f01d52ef5eb927df9915f553813a701bfdcff6e9fe1f6cf9f875193acf3c5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KFF3SM7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrwcaUvJ6v3DFdA%2FAhfpg38Q%2BUo%2FSQ82XkW9hu6CmCxAIhAJl9cqnkl0Q2rUCSs1lxKRHaDgf%2BMCtJMK2EmVk%2FwDbsKogECI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJ9JQ0oxGlMU7d5xoq3AMNSBlaHM8R2aGEuglvUbORLR4KzdlDqidoIRfwQyzRgyqj%2FKCIfymH2uPjo4PgDGCkWXj6a%2BWysGAu3sO48dhDjc%2FaHhDaGq%2BQ0xHbkMh8IrjRRtpJfB7voTjZsaDsl4gQhCZ531Z%2FnrJnn62C19lbXaQ0gPX9s62WkTI1E3mBpenbLLsHf7mjTkcTx7YhvirxVm1Wj9zTvBO4S4EGiDdpXJK2oKT9%2BxNywGeEt2tFOuaaG7DUNlsInogGbSfDcQSn0bG%2Fw125pEIKXTnWENxpl9n%2Bg022EJbHVWt7UbFPjlxYzATXN95S%2F7jUE%2BD01VmLdvzlbqPZgIF8nREMmN8yqc0m5IrOZHNSDHPKXgEdZQFW0xMdk8b9Vb7XMxLXWD2Olh570d3e3gWGSQfDRnllbYNmgoF%2FSnveU2oA96%2BE8JF8M6xGZkp2xiR6a7Z%2Bm%2FftKb%2BSnemCEoeK%2FtX3NtxwJgSBKo%2FzFudBwBsF41DBWm9xGQwnlR2jL3xChUWLZDvncdHTxASDhLOYD3TxMXGZFNmyeFL%2FUgS0bcaSft%2BJx%2FuzP%2FR2iFoPsH9Et0XaWQA4%2B9E%2BYFSZmxHmRqCRsX%2FSYgmtpILSpplL59je1FNFnR53VZ41oOumoWxJ9zDoy%2Bi8BjqkAcH3vx0jwbPOs9o5fEIeoDBswrxNQL2a6qSSBtUZcdR5I4JtnUf0QrnmPGydDufWs8Df4ki6jNNxyfX%2FS3gRE60dc0cgi%2FeJ2S1gVdTT4YG9Hk6EJOeB66zwo8H0cRAy7h74%2FRK7jeTo2ULeEMR3tfPvaOUNmr377RzYIUZpnqpOgD5zrl5x%2BixHoMEF1Qqm%2FhJKau4i8r8yB%2FXC6GuObflf7VWH&X-Amz-Signature=cea87b64daa027db1f55d46ff70435c28e11be6f8c9fd44d43f179b880833c61&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFUWIE43%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEDcPQMt7G%2Fn9NyZD7hTUT1mb3gsK8QoB2OMb38ZWo7wIgQmhlSt1i6Xx3tEONc0OgtofSzDa%2BG5u21VP9XTFTm3gqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnSepOj1TU9wg554CrcA1miKrberu08LvgBtKPbkGiyqtQE3YJPAlbtkcOeNeFtWHbZ3BHi6egGrWNaHvCcgSr6I4st4Pk%2BFy3k2BKc%2FqE8EvUFYWFuDDC2mtHfQClB92CzNi7II5O3F%2FWRuRXNATfyiKqN9MpDh5oUcFnxIIDDUMwbSsF7wgmNyYh2mnniUBtvNER%2FFeSnKju%2FBBWIOpD7E9UCGiVtZE%2Bi7NNO4zxXPO929M7VyW1UQuyIvYOhO7JtJ8bXt7jGujGLb99fGjHv4jSPI4vFu4oepH%2FDu4AWLitAvjmPPtA8hhb4Qnu9dmLRP3zHJwwn9oiqIJNL8FEF1mzlZfkna%2BBK686eKYUuNSP5wxNiBnwbTbInf3xOvvhgw82Di1rqeDCwwi4I%2FsQ43BwRrL0BjL6rws7qM6FZAEP5K89Z%2B76RK3L4aSEUKdT%2F8gMfU%2F7qpLFO6B8emn4pkcD3qePLOZL%2FduHxlCEK9cqlQf%2FWO6nTmSCdqcTj9LthVVknPk25bQwbSdbz7ZdYjbhMjA8L4MYQpdPuNONrG8I7a8634waQl0FtFmt0ba1%2F332DP4kTvfoFK9O3ZxCnqO6Nz5hTFnClDXEbWo6kdbcQRiwVeXsBRSNiQqRlsycxwNFLMazWD6JzMJ7L6LwGOqUBY6i%2B%2FVd5C8vVMxFzrh8n1xtey9xkGPPdMWAwOMysQwXcQJjh3yI5GA4aq9fJEzfZOaqgcw07xlKWZ5JoUkeJiltH6MtqDSuzbQV5Qqlo24sw9TZH8agJbNtFaY5Ki7P9fOnCBfHBAciRW3GUN%2BiNTmDo4hJJEgMw%2BZ61HAhrOEB2q6r5l3Op3RD4%2F6T5vx8aeDtJOGxyycFkdqoLW2jssGOiJdwg&X-Amz-Signature=7fb297a505f41dbeb7c1c39938dbb0ab052b94ef00c3c751cba4cb7337eb52ae&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFUWIE43%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEDcPQMt7G%2Fn9NyZD7hTUT1mb3gsK8QoB2OMb38ZWo7wIgQmhlSt1i6Xx3tEONc0OgtofSzDa%2BG5u21VP9XTFTm3gqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnSepOj1TU9wg554CrcA1miKrberu08LvgBtKPbkGiyqtQE3YJPAlbtkcOeNeFtWHbZ3BHi6egGrWNaHvCcgSr6I4st4Pk%2BFy3k2BKc%2FqE8EvUFYWFuDDC2mtHfQClB92CzNi7II5O3F%2FWRuRXNATfyiKqN9MpDh5oUcFnxIIDDUMwbSsF7wgmNyYh2mnniUBtvNER%2FFeSnKju%2FBBWIOpD7E9UCGiVtZE%2Bi7NNO4zxXPO929M7VyW1UQuyIvYOhO7JtJ8bXt7jGujGLb99fGjHv4jSPI4vFu4oepH%2FDu4AWLitAvjmPPtA8hhb4Qnu9dmLRP3zHJwwn9oiqIJNL8FEF1mzlZfkna%2BBK686eKYUuNSP5wxNiBnwbTbInf3xOvvhgw82Di1rqeDCwwi4I%2FsQ43BwRrL0BjL6rws7qM6FZAEP5K89Z%2B76RK3L4aSEUKdT%2F8gMfU%2F7qpLFO6B8emn4pkcD3qePLOZL%2FduHxlCEK9cqlQf%2FWO6nTmSCdqcTj9LthVVknPk25bQwbSdbz7ZdYjbhMjA8L4MYQpdPuNONrG8I7a8634waQl0FtFmt0ba1%2F332DP4kTvfoFK9O3ZxCnqO6Nz5hTFnClDXEbWo6kdbcQRiwVeXsBRSNiQqRlsycxwNFLMazWD6JzMJ7L6LwGOqUBY6i%2B%2FVd5C8vVMxFzrh8n1xtey9xkGPPdMWAwOMysQwXcQJjh3yI5GA4aq9fJEzfZOaqgcw07xlKWZ5JoUkeJiltH6MtqDSuzbQV5Qqlo24sw9TZH8agJbNtFaY5Ki7P9fOnCBfHBAciRW3GUN%2BiNTmDo4hJJEgMw%2BZ61HAhrOEB2q6r5l3Op3RD4%2F6T5vx8aeDtJOGxyycFkdqoLW2jssGOiJdwg&X-Amz-Signature=a892107b9caa6aad5fa8a7871403d751b83e522b7921b8be567ce67c20198402&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFUWIE43%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEDcPQMt7G%2Fn9NyZD7hTUT1mb3gsK8QoB2OMb38ZWo7wIgQmhlSt1i6Xx3tEONc0OgtofSzDa%2BG5u21VP9XTFTm3gqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnSepOj1TU9wg554CrcA1miKrberu08LvgBtKPbkGiyqtQE3YJPAlbtkcOeNeFtWHbZ3BHi6egGrWNaHvCcgSr6I4st4Pk%2BFy3k2BKc%2FqE8EvUFYWFuDDC2mtHfQClB92CzNi7II5O3F%2FWRuRXNATfyiKqN9MpDh5oUcFnxIIDDUMwbSsF7wgmNyYh2mnniUBtvNER%2FFeSnKju%2FBBWIOpD7E9UCGiVtZE%2Bi7NNO4zxXPO929M7VyW1UQuyIvYOhO7JtJ8bXt7jGujGLb99fGjHv4jSPI4vFu4oepH%2FDu4AWLitAvjmPPtA8hhb4Qnu9dmLRP3zHJwwn9oiqIJNL8FEF1mzlZfkna%2BBK686eKYUuNSP5wxNiBnwbTbInf3xOvvhgw82Di1rqeDCwwi4I%2FsQ43BwRrL0BjL6rws7qM6FZAEP5K89Z%2B76RK3L4aSEUKdT%2F8gMfU%2F7qpLFO6B8emn4pkcD3qePLOZL%2FduHxlCEK9cqlQf%2FWO6nTmSCdqcTj9LthVVknPk25bQwbSdbz7ZdYjbhMjA8L4MYQpdPuNONrG8I7a8634waQl0FtFmt0ba1%2F332DP4kTvfoFK9O3ZxCnqO6Nz5hTFnClDXEbWo6kdbcQRiwVeXsBRSNiQqRlsycxwNFLMazWD6JzMJ7L6LwGOqUBY6i%2B%2FVd5C8vVMxFzrh8n1xtey9xkGPPdMWAwOMysQwXcQJjh3yI5GA4aq9fJEzfZOaqgcw07xlKWZ5JoUkeJiltH6MtqDSuzbQV5Qqlo24sw9TZH8agJbNtFaY5Ki7P9fOnCBfHBAciRW3GUN%2BiNTmDo4hJJEgMw%2BZ61HAhrOEB2q6r5l3Op3RD4%2F6T5vx8aeDtJOGxyycFkdqoLW2jssGOiJdwg&X-Amz-Signature=85f95d6e2ad6a3a41d30b77446481976f8d704a6921d549fceb0b6a8eff50ece&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFUWIE43%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEDcPQMt7G%2Fn9NyZD7hTUT1mb3gsK8QoB2OMb38ZWo7wIgQmhlSt1i6Xx3tEONc0OgtofSzDa%2BG5u21VP9XTFTm3gqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnSepOj1TU9wg554CrcA1miKrberu08LvgBtKPbkGiyqtQE3YJPAlbtkcOeNeFtWHbZ3BHi6egGrWNaHvCcgSr6I4st4Pk%2BFy3k2BKc%2FqE8EvUFYWFuDDC2mtHfQClB92CzNi7II5O3F%2FWRuRXNATfyiKqN9MpDh5oUcFnxIIDDUMwbSsF7wgmNyYh2mnniUBtvNER%2FFeSnKju%2FBBWIOpD7E9UCGiVtZE%2Bi7NNO4zxXPO929M7VyW1UQuyIvYOhO7JtJ8bXt7jGujGLb99fGjHv4jSPI4vFu4oepH%2FDu4AWLitAvjmPPtA8hhb4Qnu9dmLRP3zHJwwn9oiqIJNL8FEF1mzlZfkna%2BBK686eKYUuNSP5wxNiBnwbTbInf3xOvvhgw82Di1rqeDCwwi4I%2FsQ43BwRrL0BjL6rws7qM6FZAEP5K89Z%2B76RK3L4aSEUKdT%2F8gMfU%2F7qpLFO6B8emn4pkcD3qePLOZL%2FduHxlCEK9cqlQf%2FWO6nTmSCdqcTj9LthVVknPk25bQwbSdbz7ZdYjbhMjA8L4MYQpdPuNONrG8I7a8634waQl0FtFmt0ba1%2F332DP4kTvfoFK9O3ZxCnqO6Nz5hTFnClDXEbWo6kdbcQRiwVeXsBRSNiQqRlsycxwNFLMazWD6JzMJ7L6LwGOqUBY6i%2B%2FVd5C8vVMxFzrh8n1xtey9xkGPPdMWAwOMysQwXcQJjh3yI5GA4aq9fJEzfZOaqgcw07xlKWZ5JoUkeJiltH6MtqDSuzbQV5Qqlo24sw9TZH8agJbNtFaY5Ki7P9fOnCBfHBAciRW3GUN%2BiNTmDo4hJJEgMw%2BZ61HAhrOEB2q6r5l3Op3RD4%2F6T5vx8aeDtJOGxyycFkdqoLW2jssGOiJdwg&X-Amz-Signature=82805279d97b6dd7c9fcdc523a36806c3ea813a68db2b1d4c7d1cffb952278a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFUWIE43%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEDcPQMt7G%2Fn9NyZD7hTUT1mb3gsK8QoB2OMb38ZWo7wIgQmhlSt1i6Xx3tEONc0OgtofSzDa%2BG5u21VP9XTFTm3gqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnSepOj1TU9wg554CrcA1miKrberu08LvgBtKPbkGiyqtQE3YJPAlbtkcOeNeFtWHbZ3BHi6egGrWNaHvCcgSr6I4st4Pk%2BFy3k2BKc%2FqE8EvUFYWFuDDC2mtHfQClB92CzNi7II5O3F%2FWRuRXNATfyiKqN9MpDh5oUcFnxIIDDUMwbSsF7wgmNyYh2mnniUBtvNER%2FFeSnKju%2FBBWIOpD7E9UCGiVtZE%2Bi7NNO4zxXPO929M7VyW1UQuyIvYOhO7JtJ8bXt7jGujGLb99fGjHv4jSPI4vFu4oepH%2FDu4AWLitAvjmPPtA8hhb4Qnu9dmLRP3zHJwwn9oiqIJNL8FEF1mzlZfkna%2BBK686eKYUuNSP5wxNiBnwbTbInf3xOvvhgw82Di1rqeDCwwi4I%2FsQ43BwRrL0BjL6rws7qM6FZAEP5K89Z%2B76RK3L4aSEUKdT%2F8gMfU%2F7qpLFO6B8emn4pkcD3qePLOZL%2FduHxlCEK9cqlQf%2FWO6nTmSCdqcTj9LthVVknPk25bQwbSdbz7ZdYjbhMjA8L4MYQpdPuNONrG8I7a8634waQl0FtFmt0ba1%2F332DP4kTvfoFK9O3ZxCnqO6Nz5hTFnClDXEbWo6kdbcQRiwVeXsBRSNiQqRlsycxwNFLMazWD6JzMJ7L6LwGOqUBY6i%2B%2FVd5C8vVMxFzrh8n1xtey9xkGPPdMWAwOMysQwXcQJjh3yI5GA4aq9fJEzfZOaqgcw07xlKWZ5JoUkeJiltH6MtqDSuzbQV5Qqlo24sw9TZH8agJbNtFaY5Ki7P9fOnCBfHBAciRW3GUN%2BiNTmDo4hJJEgMw%2BZ61HAhrOEB2q6r5l3Op3RD4%2F6T5vx8aeDtJOGxyycFkdqoLW2jssGOiJdwg&X-Amz-Signature=1a7bf194361a9f50a1cb8f2fd121d38ffd1e5b8b9f7d2d990a529aed1c391b50&X-Amz-SignedHeaders=host&x-id=GetObject)
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


