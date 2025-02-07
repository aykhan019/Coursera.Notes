

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW3M3JYO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCpu23YyEmxRrnnVd%2FeQAMUqECkDG1uuXx7BrigoDttPgIgHjwNe%2FjlA3ZQAbm0mj7EYQoYEEMEIML5gx5hYYmB3ukq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEutMo7whqZF7oH9%2FircA58NhhSIfemyWhHXqOHZGrbmvEkA1bk0aGnQlbyr1y9wFm6yuKqoWc%2BXelRo1t1CXBL%2BVRoQSxsBKOs47NCsaWUjAmoraNmavLdBQJ7ERlxTp5CB%2Finoju%2BhTqGeTvR%2BAgi7nEuAJnimsdYHrknsmD8xYL81BDze7yUKWh0igDZq4kJd%2BHmYcLozRX8i83fRVp1n54QsW1cBOyxt5TIEd2dql3wAr6Cgnmo7jbxLHtbdx90fMJHD%2Flk7eA92WITwu6x3rMOh4CXAZucerpIt%2BXoEY5USjXj2wW1GKGYN%2FdRUijOcNGG90RRmhMqMW7zyUYCaXg0JcS8h%2FxYMOnAo%2BiPKbVVv1pqtckXwIZUKfWi1XoWz8ssJ1hUNZdnCYtHC%2B8cpb1tHcnDN8dtJ3%2FSWeVTBlt4Hl8ksRJ0J%2Bt0UXIqiR9NKV%2FyMHih%2FeoMwrxAC3BE6vgMONer5qb2AX8b2UXhIf5F5d08QlXynSJ4cxpsEtWgKdf7WCdaX4t2xZzung6LQnrxzuJ2Fh3qYy0%2BoIAui4ld1Ll0g55LDPl07KgflDtxvHsUvKw%2Fha85Hkpg%2FtY%2F8NWjl%2F8LNMdQGU3gpZbgQVVEXsjrFRJcqmE%2BaW3uBNZewEpAOg74LwEGSMPXSmb0GOqUBFV6YXn7RxlGFKumphQS5XXrTtZRatF3u4fxjdjuoPEgtxyDBNe6b1O77GMpQuvUrJuPjSwXVuchVlfY3%2B5O0QjVoBp2hiER1cC3R5OTPlwqiciSgePdq039l%2BwoiX13%2F44ZVSzO1nSInhWgADt%2F99QUY4NB0EO4KyC0JA2k8mvsMfl3AKduoPNxfxEyJi9Obr2stuWhkhOmk5dI68OMy9HxV%2FZD6&X-Amz-Signature=f19025a2a9380f9de9728190e7289b6c5c9a159e190b6343cbb131af1eb361b9&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLIR4NAD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDVjdLeG1UPXfUqNOrpkhd3ejqYMzhc5lHr3YOy5qt%2BvgIgd9ShhS%2BrfhDP1P0LDemz4PJu0cS8gUB9KyExuF02oj4q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDIkK5cYTUF%2FliHw%2FvCrcA6fj2Y9DPxNDNbAsCJjB%2BoPG6woElgEvUpbulnLBNgsefc%2B%2B0XVaGKrLkZaDfwdJYxoIHggRRI5B1sS6wA6fL8NqNl1ptCEedtjB33jpEsSo4%2Bn03wgTNSoqXSrZfZofSyXWuwKqxQWLZIctChlFgYMP8cqM6li6QCDzIyPxif5kpgZu6YDGO8wZQeZzWkrOkusbUYDD1ezFLKkxnXTtMwptNRm%2FBS48JhTh2kDU4cqjyJUWhqJ5jP%2BhT9e92ORZeW38SnHuf8WVV6sNzYr4wrhbmou5D1un9kI%2Blr0Yjmy3LsYS7m%2FfiSjmKXuyViKGqHnFbLod%2FyrAdTOx26miGuUZWYzgBGskOCG43euv4kqjyW7lQGygk09MDbXwzoPIosf5om4ZiB6SUhpbIElOw9ShMbZrEDOw0S%2FL2RDIyF0ol3pLtB7xlUBxIebY%2FAyvmdZt9ajV%2B6%2FL5qhRIr2BoYiP%2Fmxmc19KUN5kQCIIJBNMM9carQsj7QHaowwEG3ZBD%2F1LMDonlIEUjRThst%2BPRSNUwOtp%2Fa%2B3PQZbq%2FxREpfcreBqG2PR45bGvLnhBEmuRMZ%2Bp6m3xX33Md9KzWEiuGZrLPsKw2IUxleszYV0ThfFtWmhaLHEF8%2BE%2B7IhMMTSmb0GOqUB2Nb4YRlWEfUd6pO0CaK9q2GRia3w4MyUFrHC7Uin%2FvR5XFdW4TQYHHxqEazsFsJaBtCoqShGyFzXEjELWcSxUTsCzuQ5bqXw%2BPPdRgSYk3lEP5puOC7pbK%2FNlsUjbMSkhGkXBGTujeit2Dp312aD0OrElm0BKXFPlMCUeX177dBVByyLG02R0l5SwTIE7fO5f13SAqeKZUoTQ3AK9JxSnzHubuXv&X-Amz-Signature=62f9ac8912c6cde69e1cfee4aacdcdf1dcd6c44c7c54dfd151f9a5f98faf84c5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLIR4NAD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDVjdLeG1UPXfUqNOrpkhd3ejqYMzhc5lHr3YOy5qt%2BvgIgd9ShhS%2BrfhDP1P0LDemz4PJu0cS8gUB9KyExuF02oj4q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDIkK5cYTUF%2FliHw%2FvCrcA6fj2Y9DPxNDNbAsCJjB%2BoPG6woElgEvUpbulnLBNgsefc%2B%2B0XVaGKrLkZaDfwdJYxoIHggRRI5B1sS6wA6fL8NqNl1ptCEedtjB33jpEsSo4%2Bn03wgTNSoqXSrZfZofSyXWuwKqxQWLZIctChlFgYMP8cqM6li6QCDzIyPxif5kpgZu6YDGO8wZQeZzWkrOkusbUYDD1ezFLKkxnXTtMwptNRm%2FBS48JhTh2kDU4cqjyJUWhqJ5jP%2BhT9e92ORZeW38SnHuf8WVV6sNzYr4wrhbmou5D1un9kI%2Blr0Yjmy3LsYS7m%2FfiSjmKXuyViKGqHnFbLod%2FyrAdTOx26miGuUZWYzgBGskOCG43euv4kqjyW7lQGygk09MDbXwzoPIosf5om4ZiB6SUhpbIElOw9ShMbZrEDOw0S%2FL2RDIyF0ol3pLtB7xlUBxIebY%2FAyvmdZt9ajV%2B6%2FL5qhRIr2BoYiP%2Fmxmc19KUN5kQCIIJBNMM9carQsj7QHaowwEG3ZBD%2F1LMDonlIEUjRThst%2BPRSNUwOtp%2Fa%2B3PQZbq%2FxREpfcreBqG2PR45bGvLnhBEmuRMZ%2Bp6m3xX33Md9KzWEiuGZrLPsKw2IUxleszYV0ThfFtWmhaLHEF8%2BE%2B7IhMMTSmb0GOqUB2Nb4YRlWEfUd6pO0CaK9q2GRia3w4MyUFrHC7Uin%2FvR5XFdW4TQYHHxqEazsFsJaBtCoqShGyFzXEjELWcSxUTsCzuQ5bqXw%2BPPdRgSYk3lEP5puOC7pbK%2FNlsUjbMSkhGkXBGTujeit2Dp312aD0OrElm0BKXFPlMCUeX177dBVByyLG02R0l5SwTIE7fO5f13SAqeKZUoTQ3AK9JxSnzHubuXv&X-Amz-Signature=07c79dcc5c70ec40004806f054e023a7b856a1e3b3fe1fb748135d0bc90b86ee&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLIR4NAD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDVjdLeG1UPXfUqNOrpkhd3ejqYMzhc5lHr3YOy5qt%2BvgIgd9ShhS%2BrfhDP1P0LDemz4PJu0cS8gUB9KyExuF02oj4q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDIkK5cYTUF%2FliHw%2FvCrcA6fj2Y9DPxNDNbAsCJjB%2BoPG6woElgEvUpbulnLBNgsefc%2B%2B0XVaGKrLkZaDfwdJYxoIHggRRI5B1sS6wA6fL8NqNl1ptCEedtjB33jpEsSo4%2Bn03wgTNSoqXSrZfZofSyXWuwKqxQWLZIctChlFgYMP8cqM6li6QCDzIyPxif5kpgZu6YDGO8wZQeZzWkrOkusbUYDD1ezFLKkxnXTtMwptNRm%2FBS48JhTh2kDU4cqjyJUWhqJ5jP%2BhT9e92ORZeW38SnHuf8WVV6sNzYr4wrhbmou5D1un9kI%2Blr0Yjmy3LsYS7m%2FfiSjmKXuyViKGqHnFbLod%2FyrAdTOx26miGuUZWYzgBGskOCG43euv4kqjyW7lQGygk09MDbXwzoPIosf5om4ZiB6SUhpbIElOw9ShMbZrEDOw0S%2FL2RDIyF0ol3pLtB7xlUBxIebY%2FAyvmdZt9ajV%2B6%2FL5qhRIr2BoYiP%2Fmxmc19KUN5kQCIIJBNMM9carQsj7QHaowwEG3ZBD%2F1LMDonlIEUjRThst%2BPRSNUwOtp%2Fa%2B3PQZbq%2FxREpfcreBqG2PR45bGvLnhBEmuRMZ%2Bp6m3xX33Md9KzWEiuGZrLPsKw2IUxleszYV0ThfFtWmhaLHEF8%2BE%2B7IhMMTSmb0GOqUB2Nb4YRlWEfUd6pO0CaK9q2GRia3w4MyUFrHC7Uin%2FvR5XFdW4TQYHHxqEazsFsJaBtCoqShGyFzXEjELWcSxUTsCzuQ5bqXw%2BPPdRgSYk3lEP5puOC7pbK%2FNlsUjbMSkhGkXBGTujeit2Dp312aD0OrElm0BKXFPlMCUeX177dBVByyLG02R0l5SwTIE7fO5f13SAqeKZUoTQ3AK9JxSnzHubuXv&X-Amz-Signature=68e76ce3dcc4f492d53f18fe4c4bc215bc0571caff91f5c9697ca02a4702f71f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLIR4NAD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDVjdLeG1UPXfUqNOrpkhd3ejqYMzhc5lHr3YOy5qt%2BvgIgd9ShhS%2BrfhDP1P0LDemz4PJu0cS8gUB9KyExuF02oj4q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDIkK5cYTUF%2FliHw%2FvCrcA6fj2Y9DPxNDNbAsCJjB%2BoPG6woElgEvUpbulnLBNgsefc%2B%2B0XVaGKrLkZaDfwdJYxoIHggRRI5B1sS6wA6fL8NqNl1ptCEedtjB33jpEsSo4%2Bn03wgTNSoqXSrZfZofSyXWuwKqxQWLZIctChlFgYMP8cqM6li6QCDzIyPxif5kpgZu6YDGO8wZQeZzWkrOkusbUYDD1ezFLKkxnXTtMwptNRm%2FBS48JhTh2kDU4cqjyJUWhqJ5jP%2BhT9e92ORZeW38SnHuf8WVV6sNzYr4wrhbmou5D1un9kI%2Blr0Yjmy3LsYS7m%2FfiSjmKXuyViKGqHnFbLod%2FyrAdTOx26miGuUZWYzgBGskOCG43euv4kqjyW7lQGygk09MDbXwzoPIosf5om4ZiB6SUhpbIElOw9ShMbZrEDOw0S%2FL2RDIyF0ol3pLtB7xlUBxIebY%2FAyvmdZt9ajV%2B6%2FL5qhRIr2BoYiP%2Fmxmc19KUN5kQCIIJBNMM9carQsj7QHaowwEG3ZBD%2F1LMDonlIEUjRThst%2BPRSNUwOtp%2Fa%2B3PQZbq%2FxREpfcreBqG2PR45bGvLnhBEmuRMZ%2Bp6m3xX33Md9KzWEiuGZrLPsKw2IUxleszYV0ThfFtWmhaLHEF8%2BE%2B7IhMMTSmb0GOqUB2Nb4YRlWEfUd6pO0CaK9q2GRia3w4MyUFrHC7Uin%2FvR5XFdW4TQYHHxqEazsFsJaBtCoqShGyFzXEjELWcSxUTsCzuQ5bqXw%2BPPdRgSYk3lEP5puOC7pbK%2FNlsUjbMSkhGkXBGTujeit2Dp312aD0OrElm0BKXFPlMCUeX177dBVByyLG02R0l5SwTIE7fO5f13SAqeKZUoTQ3AK9JxSnzHubuXv&X-Amz-Signature=2ac5c407c1a456c121e3c21d98513eb192df88c9211fb67ea846f6bbc9935c37&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLIR4NAD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDVjdLeG1UPXfUqNOrpkhd3ejqYMzhc5lHr3YOy5qt%2BvgIgd9ShhS%2BrfhDP1P0LDemz4PJu0cS8gUB9KyExuF02oj4q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDIkK5cYTUF%2FliHw%2FvCrcA6fj2Y9DPxNDNbAsCJjB%2BoPG6woElgEvUpbulnLBNgsefc%2B%2B0XVaGKrLkZaDfwdJYxoIHggRRI5B1sS6wA6fL8NqNl1ptCEedtjB33jpEsSo4%2Bn03wgTNSoqXSrZfZofSyXWuwKqxQWLZIctChlFgYMP8cqM6li6QCDzIyPxif5kpgZu6YDGO8wZQeZzWkrOkusbUYDD1ezFLKkxnXTtMwptNRm%2FBS48JhTh2kDU4cqjyJUWhqJ5jP%2BhT9e92ORZeW38SnHuf8WVV6sNzYr4wrhbmou5D1un9kI%2Blr0Yjmy3LsYS7m%2FfiSjmKXuyViKGqHnFbLod%2FyrAdTOx26miGuUZWYzgBGskOCG43euv4kqjyW7lQGygk09MDbXwzoPIosf5om4ZiB6SUhpbIElOw9ShMbZrEDOw0S%2FL2RDIyF0ol3pLtB7xlUBxIebY%2FAyvmdZt9ajV%2B6%2FL5qhRIr2BoYiP%2Fmxmc19KUN5kQCIIJBNMM9carQsj7QHaowwEG3ZBD%2F1LMDonlIEUjRThst%2BPRSNUwOtp%2Fa%2B3PQZbq%2FxREpfcreBqG2PR45bGvLnhBEmuRMZ%2Bp6m3xX33Md9KzWEiuGZrLPsKw2IUxleszYV0ThfFtWmhaLHEF8%2BE%2B7IhMMTSmb0GOqUB2Nb4YRlWEfUd6pO0CaK9q2GRia3w4MyUFrHC7Uin%2FvR5XFdW4TQYHHxqEazsFsJaBtCoqShGyFzXEjELWcSxUTsCzuQ5bqXw%2BPPdRgSYk3lEP5puOC7pbK%2FNlsUjbMSkhGkXBGTujeit2Dp312aD0OrElm0BKXFPlMCUeX177dBVByyLG02R0l5SwTIE7fO5f13SAqeKZUoTQ3AK9JxSnzHubuXv&X-Amz-Signature=2d986705ad132b5587d30667072c4d19868d80fcf6870a0b0b483fa931d8c3d0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW3M3JYO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCpu23YyEmxRrnnVd%2FeQAMUqECkDG1uuXx7BrigoDttPgIgHjwNe%2FjlA3ZQAbm0mj7EYQoYEEMEIML5gx5hYYmB3ukq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEutMo7whqZF7oH9%2FircA58NhhSIfemyWhHXqOHZGrbmvEkA1bk0aGnQlbyr1y9wFm6yuKqoWc%2BXelRo1t1CXBL%2BVRoQSxsBKOs47NCsaWUjAmoraNmavLdBQJ7ERlxTp5CB%2Finoju%2BhTqGeTvR%2BAgi7nEuAJnimsdYHrknsmD8xYL81BDze7yUKWh0igDZq4kJd%2BHmYcLozRX8i83fRVp1n54QsW1cBOyxt5TIEd2dql3wAr6Cgnmo7jbxLHtbdx90fMJHD%2Flk7eA92WITwu6x3rMOh4CXAZucerpIt%2BXoEY5USjXj2wW1GKGYN%2FdRUijOcNGG90RRmhMqMW7zyUYCaXg0JcS8h%2FxYMOnAo%2BiPKbVVv1pqtckXwIZUKfWi1XoWz8ssJ1hUNZdnCYtHC%2B8cpb1tHcnDN8dtJ3%2FSWeVTBlt4Hl8ksRJ0J%2Bt0UXIqiR9NKV%2FyMHih%2FeoMwrxAC3BE6vgMONer5qb2AX8b2UXhIf5F5d08QlXynSJ4cxpsEtWgKdf7WCdaX4t2xZzung6LQnrxzuJ2Fh3qYy0%2BoIAui4ld1Ll0g55LDPl07KgflDtxvHsUvKw%2Fha85Hkpg%2FtY%2F8NWjl%2F8LNMdQGU3gpZbgQVVEXsjrFRJcqmE%2BaW3uBNZewEpAOg74LwEGSMPXSmb0GOqUBFV6YXn7RxlGFKumphQS5XXrTtZRatF3u4fxjdjuoPEgtxyDBNe6b1O77GMpQuvUrJuPjSwXVuchVlfY3%2B5O0QjVoBp2hiER1cC3R5OTPlwqiciSgePdq039l%2BwoiX13%2F44ZVSzO1nSInhWgADt%2F99QUY4NB0EO4KyC0JA2k8mvsMfl3AKduoPNxfxEyJi9Obr2stuWhkhOmk5dI68OMy9HxV%2FZD6&X-Amz-Signature=24f83c339a41db77693f46593a4dd1fe95f204f4ee71c9bfde98dba4d4bffe83&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW3M3JYO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCpu23YyEmxRrnnVd%2FeQAMUqECkDG1uuXx7BrigoDttPgIgHjwNe%2FjlA3ZQAbm0mj7EYQoYEEMEIML5gx5hYYmB3ukq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEutMo7whqZF7oH9%2FircA58NhhSIfemyWhHXqOHZGrbmvEkA1bk0aGnQlbyr1y9wFm6yuKqoWc%2BXelRo1t1CXBL%2BVRoQSxsBKOs47NCsaWUjAmoraNmavLdBQJ7ERlxTp5CB%2Finoju%2BhTqGeTvR%2BAgi7nEuAJnimsdYHrknsmD8xYL81BDze7yUKWh0igDZq4kJd%2BHmYcLozRX8i83fRVp1n54QsW1cBOyxt5TIEd2dql3wAr6Cgnmo7jbxLHtbdx90fMJHD%2Flk7eA92WITwu6x3rMOh4CXAZucerpIt%2BXoEY5USjXj2wW1GKGYN%2FdRUijOcNGG90RRmhMqMW7zyUYCaXg0JcS8h%2FxYMOnAo%2BiPKbVVv1pqtckXwIZUKfWi1XoWz8ssJ1hUNZdnCYtHC%2B8cpb1tHcnDN8dtJ3%2FSWeVTBlt4Hl8ksRJ0J%2Bt0UXIqiR9NKV%2FyMHih%2FeoMwrxAC3BE6vgMONer5qb2AX8b2UXhIf5F5d08QlXynSJ4cxpsEtWgKdf7WCdaX4t2xZzung6LQnrxzuJ2Fh3qYy0%2BoIAui4ld1Ll0g55LDPl07KgflDtxvHsUvKw%2Fha85Hkpg%2FtY%2F8NWjl%2F8LNMdQGU3gpZbgQVVEXsjrFRJcqmE%2BaW3uBNZewEpAOg74LwEGSMPXSmb0GOqUBFV6YXn7RxlGFKumphQS5XXrTtZRatF3u4fxjdjuoPEgtxyDBNe6b1O77GMpQuvUrJuPjSwXVuchVlfY3%2B5O0QjVoBp2hiER1cC3R5OTPlwqiciSgePdq039l%2BwoiX13%2F44ZVSzO1nSInhWgADt%2F99QUY4NB0EO4KyC0JA2k8mvsMfl3AKduoPNxfxEyJi9Obr2stuWhkhOmk5dI68OMy9HxV%2FZD6&X-Amz-Signature=81ede1cebe8078fe66663e512cf6102142ef86db54ca0e162b337ac67e005c24&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW3M3JYO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCpu23YyEmxRrnnVd%2FeQAMUqECkDG1uuXx7BrigoDttPgIgHjwNe%2FjlA3ZQAbm0mj7EYQoYEEMEIML5gx5hYYmB3ukq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEutMo7whqZF7oH9%2FircA58NhhSIfemyWhHXqOHZGrbmvEkA1bk0aGnQlbyr1y9wFm6yuKqoWc%2BXelRo1t1CXBL%2BVRoQSxsBKOs47NCsaWUjAmoraNmavLdBQJ7ERlxTp5CB%2Finoju%2BhTqGeTvR%2BAgi7nEuAJnimsdYHrknsmD8xYL81BDze7yUKWh0igDZq4kJd%2BHmYcLozRX8i83fRVp1n54QsW1cBOyxt5TIEd2dql3wAr6Cgnmo7jbxLHtbdx90fMJHD%2Flk7eA92WITwu6x3rMOh4CXAZucerpIt%2BXoEY5USjXj2wW1GKGYN%2FdRUijOcNGG90RRmhMqMW7zyUYCaXg0JcS8h%2FxYMOnAo%2BiPKbVVv1pqtckXwIZUKfWi1XoWz8ssJ1hUNZdnCYtHC%2B8cpb1tHcnDN8dtJ3%2FSWeVTBlt4Hl8ksRJ0J%2Bt0UXIqiR9NKV%2FyMHih%2FeoMwrxAC3BE6vgMONer5qb2AX8b2UXhIf5F5d08QlXynSJ4cxpsEtWgKdf7WCdaX4t2xZzung6LQnrxzuJ2Fh3qYy0%2BoIAui4ld1Ll0g55LDPl07KgflDtxvHsUvKw%2Fha85Hkpg%2FtY%2F8NWjl%2F8LNMdQGU3gpZbgQVVEXsjrFRJcqmE%2BaW3uBNZewEpAOg74LwEGSMPXSmb0GOqUBFV6YXn7RxlGFKumphQS5XXrTtZRatF3u4fxjdjuoPEgtxyDBNe6b1O77GMpQuvUrJuPjSwXVuchVlfY3%2B5O0QjVoBp2hiER1cC3R5OTPlwqiciSgePdq039l%2BwoiX13%2F44ZVSzO1nSInhWgADt%2F99QUY4NB0EO4KyC0JA2k8mvsMfl3AKduoPNxfxEyJi9Obr2stuWhkhOmk5dI68OMy9HxV%2FZD6&X-Amz-Signature=48d1ac704737834a4715615b915671b933d00794d0686eaa2278e29a5f68e53b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW3M3JYO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCpu23YyEmxRrnnVd%2FeQAMUqECkDG1uuXx7BrigoDttPgIgHjwNe%2FjlA3ZQAbm0mj7EYQoYEEMEIML5gx5hYYmB3ukq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEutMo7whqZF7oH9%2FircA58NhhSIfemyWhHXqOHZGrbmvEkA1bk0aGnQlbyr1y9wFm6yuKqoWc%2BXelRo1t1CXBL%2BVRoQSxsBKOs47NCsaWUjAmoraNmavLdBQJ7ERlxTp5CB%2Finoju%2BhTqGeTvR%2BAgi7nEuAJnimsdYHrknsmD8xYL81BDze7yUKWh0igDZq4kJd%2BHmYcLozRX8i83fRVp1n54QsW1cBOyxt5TIEd2dql3wAr6Cgnmo7jbxLHtbdx90fMJHD%2Flk7eA92WITwu6x3rMOh4CXAZucerpIt%2BXoEY5USjXj2wW1GKGYN%2FdRUijOcNGG90RRmhMqMW7zyUYCaXg0JcS8h%2FxYMOnAo%2BiPKbVVv1pqtckXwIZUKfWi1XoWz8ssJ1hUNZdnCYtHC%2B8cpb1tHcnDN8dtJ3%2FSWeVTBlt4Hl8ksRJ0J%2Bt0UXIqiR9NKV%2FyMHih%2FeoMwrxAC3BE6vgMONer5qb2AX8b2UXhIf5F5d08QlXynSJ4cxpsEtWgKdf7WCdaX4t2xZzung6LQnrxzuJ2Fh3qYy0%2BoIAui4ld1Ll0g55LDPl07KgflDtxvHsUvKw%2Fha85Hkpg%2FtY%2F8NWjl%2F8LNMdQGU3gpZbgQVVEXsjrFRJcqmE%2BaW3uBNZewEpAOg74LwEGSMPXSmb0GOqUBFV6YXn7RxlGFKumphQS5XXrTtZRatF3u4fxjdjuoPEgtxyDBNe6b1O77GMpQuvUrJuPjSwXVuchVlfY3%2B5O0QjVoBp2hiER1cC3R5OTPlwqiciSgePdq039l%2BwoiX13%2F44ZVSzO1nSInhWgADt%2F99QUY4NB0EO4KyC0JA2k8mvsMfl3AKduoPNxfxEyJi9Obr2stuWhkhOmk5dI68OMy9HxV%2FZD6&X-Amz-Signature=537aa8f64ca59866eef49441002fb49196b893cab13b3d8b92b2442d2652f9d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW3M3JYO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCpu23YyEmxRrnnVd%2FeQAMUqECkDG1uuXx7BrigoDttPgIgHjwNe%2FjlA3ZQAbm0mj7EYQoYEEMEIML5gx5hYYmB3ukq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEutMo7whqZF7oH9%2FircA58NhhSIfemyWhHXqOHZGrbmvEkA1bk0aGnQlbyr1y9wFm6yuKqoWc%2BXelRo1t1CXBL%2BVRoQSxsBKOs47NCsaWUjAmoraNmavLdBQJ7ERlxTp5CB%2Finoju%2BhTqGeTvR%2BAgi7nEuAJnimsdYHrknsmD8xYL81BDze7yUKWh0igDZq4kJd%2BHmYcLozRX8i83fRVp1n54QsW1cBOyxt5TIEd2dql3wAr6Cgnmo7jbxLHtbdx90fMJHD%2Flk7eA92WITwu6x3rMOh4CXAZucerpIt%2BXoEY5USjXj2wW1GKGYN%2FdRUijOcNGG90RRmhMqMW7zyUYCaXg0JcS8h%2FxYMOnAo%2BiPKbVVv1pqtckXwIZUKfWi1XoWz8ssJ1hUNZdnCYtHC%2B8cpb1tHcnDN8dtJ3%2FSWeVTBlt4Hl8ksRJ0J%2Bt0UXIqiR9NKV%2FyMHih%2FeoMwrxAC3BE6vgMONer5qb2AX8b2UXhIf5F5d08QlXynSJ4cxpsEtWgKdf7WCdaX4t2xZzung6LQnrxzuJ2Fh3qYy0%2BoIAui4ld1Ll0g55LDPl07KgflDtxvHsUvKw%2Fha85Hkpg%2FtY%2F8NWjl%2F8LNMdQGU3gpZbgQVVEXsjrFRJcqmE%2BaW3uBNZewEpAOg74LwEGSMPXSmb0GOqUBFV6YXn7RxlGFKumphQS5XXrTtZRatF3u4fxjdjuoPEgtxyDBNe6b1O77GMpQuvUrJuPjSwXVuchVlfY3%2B5O0QjVoBp2hiER1cC3R5OTPlwqiciSgePdq039l%2BwoiX13%2F44ZVSzO1nSInhWgADt%2F99QUY4NB0EO4KyC0JA2k8mvsMfl3AKduoPNxfxEyJi9Obr2stuWhkhOmk5dI68OMy9HxV%2FZD6&X-Amz-Signature=68fe9ca7de3602775f73761200bf40993a76abac2315e0e9b6fc78c858473077&X-Amz-SignedHeaders=host&x-id=GetObject)
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


