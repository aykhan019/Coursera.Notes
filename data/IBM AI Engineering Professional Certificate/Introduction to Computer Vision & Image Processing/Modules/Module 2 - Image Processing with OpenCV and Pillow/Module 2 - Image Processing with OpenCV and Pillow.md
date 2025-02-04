

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UREDNEZY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIGlCWm%2FYIFEdwR75F7dsevxzbDBxO3x72cnO8jjqeQCYAiAFbyrKaFu%2BtFHfmYZorZzQfHybfeL%2B9urBza1BewnvqCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMdDppBZshmw4AQEecKtwDbaK5JnycJsZispThDNTCsKdXiBCVHjB4Uv1qhOCu%2BQYMiUbQtRgXPCMtXxYZn2dwBYHN7L9yEyuHLFCuX7YLa8h0%2FfQFy4XP5dgekPd2mAhqE7KJQqKw%2BnVusXmX39CHhkxCgAwYTjcskzty9xSpUZ%2BGGGDoURPnkmyMaJCr3DN5zZJaV%2Fn4Gl%2BCDfPHxnhdR%2B89Yg4tjTkjYQdCgyzQMKlmqk33wkM8H%2FsaOLzvQ3U8VDtck9YGqRYej1mbF0nHUUYiyAzGgBSL6N%2BrLUa72DStmxt%2FwIhC9DWQI1Z5CCF6WRu%2FTN%2FoaagMzrjKylAD1PU9nSBT6XuCtVrDCNUohtC6hTtTb%2BxEm9bpDLyF6ueamAD4ygiyejnIpPNtEi%2FcbZWfs4ZEMqcbm8Xbln2ae2YavCJNWXzn0fYZ47Qk9m%2BcDFw7lD%2FCAm6TyNbMyfoHbtPqZ0TwpT%2BVAo%2BIz0Sm9%2BIdLFGdk3akmS3vkS%2B6g%2FzaWqYgL8mlW77rQw9X3SXEz%2BQewRMzbbiCehQslfKnfdttilmEjWmx4PqULmCFeDPUQfCzOxQ485Wkof9EFFJe%2FdWAo15uPYBNm9E3ugU0ELT7weQiX0z5LFw1FFfPZFvHByKWpUy15y9AUr8wtpGHvQY6pgE5996AZKpXSM2L%2FAUOVJNWJtnx1de3yzJoRc2rgiqE%2BzOWXC5SLXpBMYBeruHBXusKqJ0g%2B%2FWPAckdkc8RlTc1pT7kbMptp5m6HraUfG6IzUW9yOqMnq%2BoIgjVrCtxUahwQJD1vj1euUoWafta7l%2FiQqHD8qEOB5BqRdNTpynovS4fAk4zV2N3hMwM0yTX5uLnZ%2BeZ%2FhY622%2FvHpmZUAlhLBw4tP%2Bu&X-Amz-Signature=ae1eff8403633734c7a92cebda551bdaeed5e393b100d1eaa2186908957526ec&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652AQ7IY2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCID9%2BwAg2hSdPA5En133uUjZXvdQUxZC56QlXrAA14P9sAiAmE6CbYb7MwUYm6Pr6BGDVUtYOnlWni%2FLulj3fqQ2QxCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMlga2GNsXUxS7q9QMKtwDWKEVTsUl3Pyk5L7WuQANr5Nz13eDFseyWP2NsXguh%2F8L%2F4IPJp4ii6ypHEStOv7CtZzlq9CQsC47WAKTPnOfbqPiv8vpUL3mTLniPJJtqEJuf0q2yKVDc0SsHyIHP04pJSOPVTo21QeDfqXgLS7buOm9wNi5DaW4%2BzlTbpWO%2FLaKLnr9SoV4m6yvttxXaP41TcY4K0AbuXuPZGFCghwB6vwgl5a4B28C4ehvy4vkW%2BGYJaOW4al%2FXjihCda9KD5KDZhAyj9ScpMtoXrPu6FWm3Kridrkccesxf0lqSqrTQv5R9%2B9H68%2Fx56A05KQHDdzpYV4zOiH221ikiVDqOJLd9F1zq%2F%2FqVnFk8Oj1KI2M9lvFwdFLi27VJu1GbyprDD0rm9n%2BtrA784GLsuS5z3mOtRKw0ywQZgVooFKKx5QPufpLxbn0s3s2cNGoXnyLegAmZkh%2B7AZKAWuH753ncaCrZksnAMsy7Yep%2Fa93gDtHHIxNZroInyFYQKflBVlltYybg5oROnju5H4wOs3JWVJvwYzE0sKt8OX%2BULBA5T6L2XH4%2Fh7bQ3G38Uj2ZiW4t%2FtOgpadnL5WF1XhVYRcm1VQx05WUFfZN7P7CsyAtwFRyt6XyjHBMwKMBSewLAwmZGHvQY6pgEcj4ro%2FeeRRyv%2BFMqrR3OZaj6EXZeieyZ48nna%2F9DTRur%2FeRfwTk7woHdaaKyHC13JAnf8msYJvIcDSyMC2Mx0aftVS17heLFLzQJY%2Fa2pdtUBB%2FhUxndvG7TymESNApf%2BAW6kEKT6K%2BnQIqs3wjb8UgtzSN9e1G6bmRinRcda1sl3%2Bs8CKZFMFbWfTtQEWWA8tYdVo1H2H9Wgen%2BJw565WOqx9NzS&X-Amz-Signature=65ad3a1f3086c3d0d08e5e49cd5c6d858586e55fe898fbb8c7f9da94bec65c09&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652AQ7IY2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCID9%2BwAg2hSdPA5En133uUjZXvdQUxZC56QlXrAA14P9sAiAmE6CbYb7MwUYm6Pr6BGDVUtYOnlWni%2FLulj3fqQ2QxCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMlga2GNsXUxS7q9QMKtwDWKEVTsUl3Pyk5L7WuQANr5Nz13eDFseyWP2NsXguh%2F8L%2F4IPJp4ii6ypHEStOv7CtZzlq9CQsC47WAKTPnOfbqPiv8vpUL3mTLniPJJtqEJuf0q2yKVDc0SsHyIHP04pJSOPVTo21QeDfqXgLS7buOm9wNi5DaW4%2BzlTbpWO%2FLaKLnr9SoV4m6yvttxXaP41TcY4K0AbuXuPZGFCghwB6vwgl5a4B28C4ehvy4vkW%2BGYJaOW4al%2FXjihCda9KD5KDZhAyj9ScpMtoXrPu6FWm3Kridrkccesxf0lqSqrTQv5R9%2B9H68%2Fx56A05KQHDdzpYV4zOiH221ikiVDqOJLd9F1zq%2F%2FqVnFk8Oj1KI2M9lvFwdFLi27VJu1GbyprDD0rm9n%2BtrA784GLsuS5z3mOtRKw0ywQZgVooFKKx5QPufpLxbn0s3s2cNGoXnyLegAmZkh%2B7AZKAWuH753ncaCrZksnAMsy7Yep%2Fa93gDtHHIxNZroInyFYQKflBVlltYybg5oROnju5H4wOs3JWVJvwYzE0sKt8OX%2BULBA5T6L2XH4%2Fh7bQ3G38Uj2ZiW4t%2FtOgpadnL5WF1XhVYRcm1VQx05WUFfZN7P7CsyAtwFRyt6XyjHBMwKMBSewLAwmZGHvQY6pgEcj4ro%2FeeRRyv%2BFMqrR3OZaj6EXZeieyZ48nna%2F9DTRur%2FeRfwTk7woHdaaKyHC13JAnf8msYJvIcDSyMC2Mx0aftVS17heLFLzQJY%2Fa2pdtUBB%2FhUxndvG7TymESNApf%2BAW6kEKT6K%2BnQIqs3wjb8UgtzSN9e1G6bmRinRcda1sl3%2Bs8CKZFMFbWfTtQEWWA8tYdVo1H2H9Wgen%2BJw565WOqx9NzS&X-Amz-Signature=2d3c00fb3423cef9462f7ce1e5ab7d66b40fc10e005499e340256c03dcc4c0f1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652AQ7IY2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCID9%2BwAg2hSdPA5En133uUjZXvdQUxZC56QlXrAA14P9sAiAmE6CbYb7MwUYm6Pr6BGDVUtYOnlWni%2FLulj3fqQ2QxCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMlga2GNsXUxS7q9QMKtwDWKEVTsUl3Pyk5L7WuQANr5Nz13eDFseyWP2NsXguh%2F8L%2F4IPJp4ii6ypHEStOv7CtZzlq9CQsC47WAKTPnOfbqPiv8vpUL3mTLniPJJtqEJuf0q2yKVDc0SsHyIHP04pJSOPVTo21QeDfqXgLS7buOm9wNi5DaW4%2BzlTbpWO%2FLaKLnr9SoV4m6yvttxXaP41TcY4K0AbuXuPZGFCghwB6vwgl5a4B28C4ehvy4vkW%2BGYJaOW4al%2FXjihCda9KD5KDZhAyj9ScpMtoXrPu6FWm3Kridrkccesxf0lqSqrTQv5R9%2B9H68%2Fx56A05KQHDdzpYV4zOiH221ikiVDqOJLd9F1zq%2F%2FqVnFk8Oj1KI2M9lvFwdFLi27VJu1GbyprDD0rm9n%2BtrA784GLsuS5z3mOtRKw0ywQZgVooFKKx5QPufpLxbn0s3s2cNGoXnyLegAmZkh%2B7AZKAWuH753ncaCrZksnAMsy7Yep%2Fa93gDtHHIxNZroInyFYQKflBVlltYybg5oROnju5H4wOs3JWVJvwYzE0sKt8OX%2BULBA5T6L2XH4%2Fh7bQ3G38Uj2ZiW4t%2FtOgpadnL5WF1XhVYRcm1VQx05WUFfZN7P7CsyAtwFRyt6XyjHBMwKMBSewLAwmZGHvQY6pgEcj4ro%2FeeRRyv%2BFMqrR3OZaj6EXZeieyZ48nna%2F9DTRur%2FeRfwTk7woHdaaKyHC13JAnf8msYJvIcDSyMC2Mx0aftVS17heLFLzQJY%2Fa2pdtUBB%2FhUxndvG7TymESNApf%2BAW6kEKT6K%2BnQIqs3wjb8UgtzSN9e1G6bmRinRcda1sl3%2Bs8CKZFMFbWfTtQEWWA8tYdVo1H2H9Wgen%2BJw565WOqx9NzS&X-Amz-Signature=6c75af2b3257660f53570135792e39150d853abb74bc9387519aa4292e7ddd89&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652AQ7IY2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCID9%2BwAg2hSdPA5En133uUjZXvdQUxZC56QlXrAA14P9sAiAmE6CbYb7MwUYm6Pr6BGDVUtYOnlWni%2FLulj3fqQ2QxCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMlga2GNsXUxS7q9QMKtwDWKEVTsUl3Pyk5L7WuQANr5Nz13eDFseyWP2NsXguh%2F8L%2F4IPJp4ii6ypHEStOv7CtZzlq9CQsC47WAKTPnOfbqPiv8vpUL3mTLniPJJtqEJuf0q2yKVDc0SsHyIHP04pJSOPVTo21QeDfqXgLS7buOm9wNi5DaW4%2BzlTbpWO%2FLaKLnr9SoV4m6yvttxXaP41TcY4K0AbuXuPZGFCghwB6vwgl5a4B28C4ehvy4vkW%2BGYJaOW4al%2FXjihCda9KD5KDZhAyj9ScpMtoXrPu6FWm3Kridrkccesxf0lqSqrTQv5R9%2B9H68%2Fx56A05KQHDdzpYV4zOiH221ikiVDqOJLd9F1zq%2F%2FqVnFk8Oj1KI2M9lvFwdFLi27VJu1GbyprDD0rm9n%2BtrA784GLsuS5z3mOtRKw0ywQZgVooFKKx5QPufpLxbn0s3s2cNGoXnyLegAmZkh%2B7AZKAWuH753ncaCrZksnAMsy7Yep%2Fa93gDtHHIxNZroInyFYQKflBVlltYybg5oROnju5H4wOs3JWVJvwYzE0sKt8OX%2BULBA5T6L2XH4%2Fh7bQ3G38Uj2ZiW4t%2FtOgpadnL5WF1XhVYRcm1VQx05WUFfZN7P7CsyAtwFRyt6XyjHBMwKMBSewLAwmZGHvQY6pgEcj4ro%2FeeRRyv%2BFMqrR3OZaj6EXZeieyZ48nna%2F9DTRur%2FeRfwTk7woHdaaKyHC13JAnf8msYJvIcDSyMC2Mx0aftVS17heLFLzQJY%2Fa2pdtUBB%2FhUxndvG7TymESNApf%2BAW6kEKT6K%2BnQIqs3wjb8UgtzSN9e1G6bmRinRcda1sl3%2Bs8CKZFMFbWfTtQEWWA8tYdVo1H2H9Wgen%2BJw565WOqx9NzS&X-Amz-Signature=2b79426b69fda60d6c5fd7f38e1e6ed986fcd7d923e862fd0e18c1b6ba68c1d5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652AQ7IY2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCID9%2BwAg2hSdPA5En133uUjZXvdQUxZC56QlXrAA14P9sAiAmE6CbYb7MwUYm6Pr6BGDVUtYOnlWni%2FLulj3fqQ2QxCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMlga2GNsXUxS7q9QMKtwDWKEVTsUl3Pyk5L7WuQANr5Nz13eDFseyWP2NsXguh%2F8L%2F4IPJp4ii6ypHEStOv7CtZzlq9CQsC47WAKTPnOfbqPiv8vpUL3mTLniPJJtqEJuf0q2yKVDc0SsHyIHP04pJSOPVTo21QeDfqXgLS7buOm9wNi5DaW4%2BzlTbpWO%2FLaKLnr9SoV4m6yvttxXaP41TcY4K0AbuXuPZGFCghwB6vwgl5a4B28C4ehvy4vkW%2BGYJaOW4al%2FXjihCda9KD5KDZhAyj9ScpMtoXrPu6FWm3Kridrkccesxf0lqSqrTQv5R9%2B9H68%2Fx56A05KQHDdzpYV4zOiH221ikiVDqOJLd9F1zq%2F%2FqVnFk8Oj1KI2M9lvFwdFLi27VJu1GbyprDD0rm9n%2BtrA784GLsuS5z3mOtRKw0ywQZgVooFKKx5QPufpLxbn0s3s2cNGoXnyLegAmZkh%2B7AZKAWuH753ncaCrZksnAMsy7Yep%2Fa93gDtHHIxNZroInyFYQKflBVlltYybg5oROnju5H4wOs3JWVJvwYzE0sKt8OX%2BULBA5T6L2XH4%2Fh7bQ3G38Uj2ZiW4t%2FtOgpadnL5WF1XhVYRcm1VQx05WUFfZN7P7CsyAtwFRyt6XyjHBMwKMBSewLAwmZGHvQY6pgEcj4ro%2FeeRRyv%2BFMqrR3OZaj6EXZeieyZ48nna%2F9DTRur%2FeRfwTk7woHdaaKyHC13JAnf8msYJvIcDSyMC2Mx0aftVS17heLFLzQJY%2Fa2pdtUBB%2FhUxndvG7TymESNApf%2BAW6kEKT6K%2BnQIqs3wjb8UgtzSN9e1G6bmRinRcda1sl3%2Bs8CKZFMFbWfTtQEWWA8tYdVo1H2H9Wgen%2BJw565WOqx9NzS&X-Amz-Signature=b8389d6a3394bd8242ad9b4d4c8bdf633ddb47994618541f633a5cf106c3ec9d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UREDNEZY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIGlCWm%2FYIFEdwR75F7dsevxzbDBxO3x72cnO8jjqeQCYAiAFbyrKaFu%2BtFHfmYZorZzQfHybfeL%2B9urBza1BewnvqCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMdDppBZshmw4AQEecKtwDbaK5JnycJsZispThDNTCsKdXiBCVHjB4Uv1qhOCu%2BQYMiUbQtRgXPCMtXxYZn2dwBYHN7L9yEyuHLFCuX7YLa8h0%2FfQFy4XP5dgekPd2mAhqE7KJQqKw%2BnVusXmX39CHhkxCgAwYTjcskzty9xSpUZ%2BGGGDoURPnkmyMaJCr3DN5zZJaV%2Fn4Gl%2BCDfPHxnhdR%2B89Yg4tjTkjYQdCgyzQMKlmqk33wkM8H%2FsaOLzvQ3U8VDtck9YGqRYej1mbF0nHUUYiyAzGgBSL6N%2BrLUa72DStmxt%2FwIhC9DWQI1Z5CCF6WRu%2FTN%2FoaagMzrjKylAD1PU9nSBT6XuCtVrDCNUohtC6hTtTb%2BxEm9bpDLyF6ueamAD4ygiyejnIpPNtEi%2FcbZWfs4ZEMqcbm8Xbln2ae2YavCJNWXzn0fYZ47Qk9m%2BcDFw7lD%2FCAm6TyNbMyfoHbtPqZ0TwpT%2BVAo%2BIz0Sm9%2BIdLFGdk3akmS3vkS%2B6g%2FzaWqYgL8mlW77rQw9X3SXEz%2BQewRMzbbiCehQslfKnfdttilmEjWmx4PqULmCFeDPUQfCzOxQ485Wkof9EFFJe%2FdWAo15uPYBNm9E3ugU0ELT7weQiX0z5LFw1FFfPZFvHByKWpUy15y9AUr8wtpGHvQY6pgE5996AZKpXSM2L%2FAUOVJNWJtnx1de3yzJoRc2rgiqE%2BzOWXC5SLXpBMYBeruHBXusKqJ0g%2B%2FWPAckdkc8RlTc1pT7kbMptp5m6HraUfG6IzUW9yOqMnq%2BoIgjVrCtxUahwQJD1vj1euUoWafta7l%2FiQqHD8qEOB5BqRdNTpynovS4fAk4zV2N3hMwM0yTX5uLnZ%2BeZ%2FhY622%2FvHpmZUAlhLBw4tP%2Bu&X-Amz-Signature=79a0bba1db8023a627c28538dcea5cf2119b8ee4b56ef033c682c5bad5b71e80&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UREDNEZY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIGlCWm%2FYIFEdwR75F7dsevxzbDBxO3x72cnO8jjqeQCYAiAFbyrKaFu%2BtFHfmYZorZzQfHybfeL%2B9urBza1BewnvqCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMdDppBZshmw4AQEecKtwDbaK5JnycJsZispThDNTCsKdXiBCVHjB4Uv1qhOCu%2BQYMiUbQtRgXPCMtXxYZn2dwBYHN7L9yEyuHLFCuX7YLa8h0%2FfQFy4XP5dgekPd2mAhqE7KJQqKw%2BnVusXmX39CHhkxCgAwYTjcskzty9xSpUZ%2BGGGDoURPnkmyMaJCr3DN5zZJaV%2Fn4Gl%2BCDfPHxnhdR%2B89Yg4tjTkjYQdCgyzQMKlmqk33wkM8H%2FsaOLzvQ3U8VDtck9YGqRYej1mbF0nHUUYiyAzGgBSL6N%2BrLUa72DStmxt%2FwIhC9DWQI1Z5CCF6WRu%2FTN%2FoaagMzrjKylAD1PU9nSBT6XuCtVrDCNUohtC6hTtTb%2BxEm9bpDLyF6ueamAD4ygiyejnIpPNtEi%2FcbZWfs4ZEMqcbm8Xbln2ae2YavCJNWXzn0fYZ47Qk9m%2BcDFw7lD%2FCAm6TyNbMyfoHbtPqZ0TwpT%2BVAo%2BIz0Sm9%2BIdLFGdk3akmS3vkS%2B6g%2FzaWqYgL8mlW77rQw9X3SXEz%2BQewRMzbbiCehQslfKnfdttilmEjWmx4PqULmCFeDPUQfCzOxQ485Wkof9EFFJe%2FdWAo15uPYBNm9E3ugU0ELT7weQiX0z5LFw1FFfPZFvHByKWpUy15y9AUr8wtpGHvQY6pgE5996AZKpXSM2L%2FAUOVJNWJtnx1de3yzJoRc2rgiqE%2BzOWXC5SLXpBMYBeruHBXusKqJ0g%2B%2FWPAckdkc8RlTc1pT7kbMptp5m6HraUfG6IzUW9yOqMnq%2BoIgjVrCtxUahwQJD1vj1euUoWafta7l%2FiQqHD8qEOB5BqRdNTpynovS4fAk4zV2N3hMwM0yTX5uLnZ%2BeZ%2FhY622%2FvHpmZUAlhLBw4tP%2Bu&X-Amz-Signature=8306ac0efbafeeb8771f3cdc988256742b1658e97c41ac27e43137557d96dbf4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UREDNEZY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIGlCWm%2FYIFEdwR75F7dsevxzbDBxO3x72cnO8jjqeQCYAiAFbyrKaFu%2BtFHfmYZorZzQfHybfeL%2B9urBza1BewnvqCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMdDppBZshmw4AQEecKtwDbaK5JnycJsZispThDNTCsKdXiBCVHjB4Uv1qhOCu%2BQYMiUbQtRgXPCMtXxYZn2dwBYHN7L9yEyuHLFCuX7YLa8h0%2FfQFy4XP5dgekPd2mAhqE7KJQqKw%2BnVusXmX39CHhkxCgAwYTjcskzty9xSpUZ%2BGGGDoURPnkmyMaJCr3DN5zZJaV%2Fn4Gl%2BCDfPHxnhdR%2B89Yg4tjTkjYQdCgyzQMKlmqk33wkM8H%2FsaOLzvQ3U8VDtck9YGqRYej1mbF0nHUUYiyAzGgBSL6N%2BrLUa72DStmxt%2FwIhC9DWQI1Z5CCF6WRu%2FTN%2FoaagMzrjKylAD1PU9nSBT6XuCtVrDCNUohtC6hTtTb%2BxEm9bpDLyF6ueamAD4ygiyejnIpPNtEi%2FcbZWfs4ZEMqcbm8Xbln2ae2YavCJNWXzn0fYZ47Qk9m%2BcDFw7lD%2FCAm6TyNbMyfoHbtPqZ0TwpT%2BVAo%2BIz0Sm9%2BIdLFGdk3akmS3vkS%2B6g%2FzaWqYgL8mlW77rQw9X3SXEz%2BQewRMzbbiCehQslfKnfdttilmEjWmx4PqULmCFeDPUQfCzOxQ485Wkof9EFFJe%2FdWAo15uPYBNm9E3ugU0ELT7weQiX0z5LFw1FFfPZFvHByKWpUy15y9AUr8wtpGHvQY6pgE5996AZKpXSM2L%2FAUOVJNWJtnx1de3yzJoRc2rgiqE%2BzOWXC5SLXpBMYBeruHBXusKqJ0g%2B%2FWPAckdkc8RlTc1pT7kbMptp5m6HraUfG6IzUW9yOqMnq%2BoIgjVrCtxUahwQJD1vj1euUoWafta7l%2FiQqHD8qEOB5BqRdNTpynovS4fAk4zV2N3hMwM0yTX5uLnZ%2BeZ%2FhY622%2FvHpmZUAlhLBw4tP%2Bu&X-Amz-Signature=ed545efe9f3704193c34d43eb346b091edeb8c8064b86440cb7ed522757e54e0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UREDNEZY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIGlCWm%2FYIFEdwR75F7dsevxzbDBxO3x72cnO8jjqeQCYAiAFbyrKaFu%2BtFHfmYZorZzQfHybfeL%2B9urBza1BewnvqCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMdDppBZshmw4AQEecKtwDbaK5JnycJsZispThDNTCsKdXiBCVHjB4Uv1qhOCu%2BQYMiUbQtRgXPCMtXxYZn2dwBYHN7L9yEyuHLFCuX7YLa8h0%2FfQFy4XP5dgekPd2mAhqE7KJQqKw%2BnVusXmX39CHhkxCgAwYTjcskzty9xSpUZ%2BGGGDoURPnkmyMaJCr3DN5zZJaV%2Fn4Gl%2BCDfPHxnhdR%2B89Yg4tjTkjYQdCgyzQMKlmqk33wkM8H%2FsaOLzvQ3U8VDtck9YGqRYej1mbF0nHUUYiyAzGgBSL6N%2BrLUa72DStmxt%2FwIhC9DWQI1Z5CCF6WRu%2FTN%2FoaagMzrjKylAD1PU9nSBT6XuCtVrDCNUohtC6hTtTb%2BxEm9bpDLyF6ueamAD4ygiyejnIpPNtEi%2FcbZWfs4ZEMqcbm8Xbln2ae2YavCJNWXzn0fYZ47Qk9m%2BcDFw7lD%2FCAm6TyNbMyfoHbtPqZ0TwpT%2BVAo%2BIz0Sm9%2BIdLFGdk3akmS3vkS%2B6g%2FzaWqYgL8mlW77rQw9X3SXEz%2BQewRMzbbiCehQslfKnfdttilmEjWmx4PqULmCFeDPUQfCzOxQ485Wkof9EFFJe%2FdWAo15uPYBNm9E3ugU0ELT7weQiX0z5LFw1FFfPZFvHByKWpUy15y9AUr8wtpGHvQY6pgE5996AZKpXSM2L%2FAUOVJNWJtnx1de3yzJoRc2rgiqE%2BzOWXC5SLXpBMYBeruHBXusKqJ0g%2B%2FWPAckdkc8RlTc1pT7kbMptp5m6HraUfG6IzUW9yOqMnq%2BoIgjVrCtxUahwQJD1vj1euUoWafta7l%2FiQqHD8qEOB5BqRdNTpynovS4fAk4zV2N3hMwM0yTX5uLnZ%2BeZ%2FhY622%2FvHpmZUAlhLBw4tP%2Bu&X-Amz-Signature=b4455a5b572f3e64716d7de744ea5b2e47d37e0d9fc26855dbcbe508028b693a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UREDNEZY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIGlCWm%2FYIFEdwR75F7dsevxzbDBxO3x72cnO8jjqeQCYAiAFbyrKaFu%2BtFHfmYZorZzQfHybfeL%2B9urBza1BewnvqCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMdDppBZshmw4AQEecKtwDbaK5JnycJsZispThDNTCsKdXiBCVHjB4Uv1qhOCu%2BQYMiUbQtRgXPCMtXxYZn2dwBYHN7L9yEyuHLFCuX7YLa8h0%2FfQFy4XP5dgekPd2mAhqE7KJQqKw%2BnVusXmX39CHhkxCgAwYTjcskzty9xSpUZ%2BGGGDoURPnkmyMaJCr3DN5zZJaV%2Fn4Gl%2BCDfPHxnhdR%2B89Yg4tjTkjYQdCgyzQMKlmqk33wkM8H%2FsaOLzvQ3U8VDtck9YGqRYej1mbF0nHUUYiyAzGgBSL6N%2BrLUa72DStmxt%2FwIhC9DWQI1Z5CCF6WRu%2FTN%2FoaagMzrjKylAD1PU9nSBT6XuCtVrDCNUohtC6hTtTb%2BxEm9bpDLyF6ueamAD4ygiyejnIpPNtEi%2FcbZWfs4ZEMqcbm8Xbln2ae2YavCJNWXzn0fYZ47Qk9m%2BcDFw7lD%2FCAm6TyNbMyfoHbtPqZ0TwpT%2BVAo%2BIz0Sm9%2BIdLFGdk3akmS3vkS%2B6g%2FzaWqYgL8mlW77rQw9X3SXEz%2BQewRMzbbiCehQslfKnfdttilmEjWmx4PqULmCFeDPUQfCzOxQ485Wkof9EFFJe%2FdWAo15uPYBNm9E3ugU0ELT7weQiX0z5LFw1FFfPZFvHByKWpUy15y9AUr8wtpGHvQY6pgE5996AZKpXSM2L%2FAUOVJNWJtnx1de3yzJoRc2rgiqE%2BzOWXC5SLXpBMYBeruHBXusKqJ0g%2B%2FWPAckdkc8RlTc1pT7kbMptp5m6HraUfG6IzUW9yOqMnq%2BoIgjVrCtxUahwQJD1vj1euUoWafta7l%2FiQqHD8qEOB5BqRdNTpynovS4fAk4zV2N3hMwM0yTX5uLnZ%2BeZ%2FhY622%2FvHpmZUAlhLBw4tP%2Bu&X-Amz-Signature=e571e17c2264c586dda1ee27ddfc6900b502853c94ec1f4935c12d460a5b70c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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


