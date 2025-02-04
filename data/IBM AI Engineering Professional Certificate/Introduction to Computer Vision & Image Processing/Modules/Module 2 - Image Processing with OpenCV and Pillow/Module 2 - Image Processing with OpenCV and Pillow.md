

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLH5DGUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDVGPrKZAJiDJ3bGbOd38cp3YdoKPczOSgzoi4jg%2BNwmQIhAN20TvNJejZ3Gs0u6QDk%2BgYJxmc7tANhI9hmtwZQFBwYKv8DCDcQABoMNjM3NDIzMTgzODA1Igw6BS9E2j1zujWGQu0q3APX1tcTPZf7zI6j8h%2BBHmTWsiAJP1Sn96a8%2BDMcV8vTQpd9wVLYooIE2GkhvfMjrkbQZSbF4gm53rmd95eS2tGIKYC0ZL9NevtPD6SKhaPwvGdBkAMvc%2Fu3Var1ZYPdfDFydUf%2BKFEgCSWSAz3ZiYChyvloNhCeveRuSV9lJ9RHqFdVvUJM1MsqG7Jzo1pURS2csYBlVGwlXF4yIGOF3mVPgAXrM7Lbn%2B5N0%2F%2FREdAlZxEs3znb6Yh%2FDgnEVzN5oL%2F%2BDqOF%2F08iHhib5JSV9Ji%2FfdvGi7qz2cRrqfJgoGQJWJ%2B2VkEw1VCz63pNQ7BaMN8yY1cs0Ht1y%2FhM7N08AvQrC4%2BtJBuhEJqCYMqjl2gFTiOCHoMwY%2BD2cECs9hYZYZZC3OgEI9um5%2FGwUoOR%2BCaeP5nIe%2FWUpK13Axc9aDjXCvhuxYS%2FZ2t3z%2FmpcbX4wJ6tgUVM9zwdGQ3lSWPwZZHgQs328Aw1ytVZe5JtMb9Phyq8e3wP33tRflk1K85IsRpIx2EzhptP%2BcOCael6FMadQ1ozoVU87va72sFwaBf6ioZAnqgWo9N%2FlVCtskUUjWjeNWK%2FOLe8V0ot0G1d9I9s5rxGzWfRKhMPUFPg0ftssPFGCy70QO3IK5DOOzCflIq9BjqkARWqCjk6Ps%2BQesLMS%2BLdiopK3O4YuAdjO595KIFjV6WNAwY6oYzVQDEsS1VEhbPrBrFa5z7Xqmfk1ZES0LX2hHguuKUA1iGelvZI%2B4q%2Fd701vi0i5c2XfOTpt%2BN%2BZsol%2BW1mOcmNejd29FZNRwwBguNClFZG5xRNDmWQEi3qTNulfAGWOZRcGbTmvYq3ED9zKwcFhRx4IeDt9GsuraJbk4HvA2FW&X-Amz-Signature=b2c6803e69af0ddd567296623339a2c54eb09e67a547d0d4b34b949f8790827e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNUSO4DB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCuYtd4HlCOkLBaJ6z46i6xxNbYjSVeH2P6iuw%2B3jNghQIhAOkufCJ0GmCZzMQ06%2FLrbbL4K1fcm0pjU5j0PW5RiNGPKv8DCDcQABoMNjM3NDIzMTgzODA1Igyof6L7btAdDtw8VT0q3APNQGvHN222OQ3W8811fkHZer%2FrNiKJVVYk%2FNfYj4DUnBEDW98rML9dh1dVErHrq1gWTQs3uQFc0vL930FafZprPqHuPqDC43%2FBVZSG93mprS9oJzI19wg6nUZ4%2BS7dzEFS5h1XZ3PUSRpv16xx0nKF%2FTMwP29QdwEl3YX8S%2FK9UhN1WJZ4a%2B91DEmMTIO4sj01HIZ8jtk5J%2Fs1g1nkbu74LexZrQ9t21KS3igO1IyvNWip0mcNaGHbfAl6RCjyhzGrM853PB5Xtbt9AplLNjK%2BR%2BR4YUMLvsHo6JpmK9nFFQ%2BL%2BhZvSkbgsUdevGL3pidbfsdKMoq5OuAQcLAWRs58I1NAo%2FM7xYfd5lbUcaXqNmL5ikMmGd7y%2Bl%2FJVgGwDovmIUgCaAqm99a0W2GE5zAKvTwLj1zEFuSrYkypdFgm4zjaTk2RWR6g2rKwOs%2Bq1SLyopkAnr7etPdEt%2Frkmr52t%2FfXXwpBdfUACjMfbQbYbHtlLPLQISGfL2WlMjRWlI8RgkFxzS%2BVwmwbL%2BwN70dyd3IfrogiZzX5wilD7ojnUlXOjTECkASfyr0jU%2F16h%2BKisPeaZ%2Fq7cbGUd%2FlfR8WF4MSiIOFgcyGehkdhIR%2BbWIwpW9%2BrsbEPZX%2F%2FmDC0lIq9BjqkAQsRF2QUu6tHpREMQtszwJZrGJxV%2FYLL8zSvJjAuQ2IbTIIW1OZseSxpiMNMgERJ4rmyDQHUZLJDKb7WYWst8DSAfNZI9PezAC3Q7wNxdNYVINaYs8v1xR5k0w2IPjufw1uUMrerj28Q5r9RDsMdgOSGdPsutI8eU%2BYfKYdCth8rlUEeasXGUV%2BwxSVz7Ry74JMt2HPDc2IlK1ZHqvTtoiRG9Dcq&X-Amz-Signature=13890eb63945cfa847fcc4fe000b9e18466213791a492f71ab492db43142b71c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNUSO4DB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCuYtd4HlCOkLBaJ6z46i6xxNbYjSVeH2P6iuw%2B3jNghQIhAOkufCJ0GmCZzMQ06%2FLrbbL4K1fcm0pjU5j0PW5RiNGPKv8DCDcQABoMNjM3NDIzMTgzODA1Igyof6L7btAdDtw8VT0q3APNQGvHN222OQ3W8811fkHZer%2FrNiKJVVYk%2FNfYj4DUnBEDW98rML9dh1dVErHrq1gWTQs3uQFc0vL930FafZprPqHuPqDC43%2FBVZSG93mprS9oJzI19wg6nUZ4%2BS7dzEFS5h1XZ3PUSRpv16xx0nKF%2FTMwP29QdwEl3YX8S%2FK9UhN1WJZ4a%2B91DEmMTIO4sj01HIZ8jtk5J%2Fs1g1nkbu74LexZrQ9t21KS3igO1IyvNWip0mcNaGHbfAl6RCjyhzGrM853PB5Xtbt9AplLNjK%2BR%2BR4YUMLvsHo6JpmK9nFFQ%2BL%2BhZvSkbgsUdevGL3pidbfsdKMoq5OuAQcLAWRs58I1NAo%2FM7xYfd5lbUcaXqNmL5ikMmGd7y%2Bl%2FJVgGwDovmIUgCaAqm99a0W2GE5zAKvTwLj1zEFuSrYkypdFgm4zjaTk2RWR6g2rKwOs%2Bq1SLyopkAnr7etPdEt%2Frkmr52t%2FfXXwpBdfUACjMfbQbYbHtlLPLQISGfL2WlMjRWlI8RgkFxzS%2BVwmwbL%2BwN70dyd3IfrogiZzX5wilD7ojnUlXOjTECkASfyr0jU%2F16h%2BKisPeaZ%2Fq7cbGUd%2FlfR8WF4MSiIOFgcyGehkdhIR%2BbWIwpW9%2BrsbEPZX%2F%2FmDC0lIq9BjqkAQsRF2QUu6tHpREMQtszwJZrGJxV%2FYLL8zSvJjAuQ2IbTIIW1OZseSxpiMNMgERJ4rmyDQHUZLJDKb7WYWst8DSAfNZI9PezAC3Q7wNxdNYVINaYs8v1xR5k0w2IPjufw1uUMrerj28Q5r9RDsMdgOSGdPsutI8eU%2BYfKYdCth8rlUEeasXGUV%2BwxSVz7Ry74JMt2HPDc2IlK1ZHqvTtoiRG9Dcq&X-Amz-Signature=e81d64c28aa5e2c62e1821d9e9e13f8163f96dfd8aa24f41fa4e4df7bdbb4705&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNUSO4DB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCuYtd4HlCOkLBaJ6z46i6xxNbYjSVeH2P6iuw%2B3jNghQIhAOkufCJ0GmCZzMQ06%2FLrbbL4K1fcm0pjU5j0PW5RiNGPKv8DCDcQABoMNjM3NDIzMTgzODA1Igyof6L7btAdDtw8VT0q3APNQGvHN222OQ3W8811fkHZer%2FrNiKJVVYk%2FNfYj4DUnBEDW98rML9dh1dVErHrq1gWTQs3uQFc0vL930FafZprPqHuPqDC43%2FBVZSG93mprS9oJzI19wg6nUZ4%2BS7dzEFS5h1XZ3PUSRpv16xx0nKF%2FTMwP29QdwEl3YX8S%2FK9UhN1WJZ4a%2B91DEmMTIO4sj01HIZ8jtk5J%2Fs1g1nkbu74LexZrQ9t21KS3igO1IyvNWip0mcNaGHbfAl6RCjyhzGrM853PB5Xtbt9AplLNjK%2BR%2BR4YUMLvsHo6JpmK9nFFQ%2BL%2BhZvSkbgsUdevGL3pidbfsdKMoq5OuAQcLAWRs58I1NAo%2FM7xYfd5lbUcaXqNmL5ikMmGd7y%2Bl%2FJVgGwDovmIUgCaAqm99a0W2GE5zAKvTwLj1zEFuSrYkypdFgm4zjaTk2RWR6g2rKwOs%2Bq1SLyopkAnr7etPdEt%2Frkmr52t%2FfXXwpBdfUACjMfbQbYbHtlLPLQISGfL2WlMjRWlI8RgkFxzS%2BVwmwbL%2BwN70dyd3IfrogiZzX5wilD7ojnUlXOjTECkASfyr0jU%2F16h%2BKisPeaZ%2Fq7cbGUd%2FlfR8WF4MSiIOFgcyGehkdhIR%2BbWIwpW9%2BrsbEPZX%2F%2FmDC0lIq9BjqkAQsRF2QUu6tHpREMQtszwJZrGJxV%2FYLL8zSvJjAuQ2IbTIIW1OZseSxpiMNMgERJ4rmyDQHUZLJDKb7WYWst8DSAfNZI9PezAC3Q7wNxdNYVINaYs8v1xR5k0w2IPjufw1uUMrerj28Q5r9RDsMdgOSGdPsutI8eU%2BYfKYdCth8rlUEeasXGUV%2BwxSVz7Ry74JMt2HPDc2IlK1ZHqvTtoiRG9Dcq&X-Amz-Signature=e1d908c8347a048c47f71229481260c083b76ee571a6af394a8a8e09768baf25&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNUSO4DB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCuYtd4HlCOkLBaJ6z46i6xxNbYjSVeH2P6iuw%2B3jNghQIhAOkufCJ0GmCZzMQ06%2FLrbbL4K1fcm0pjU5j0PW5RiNGPKv8DCDcQABoMNjM3NDIzMTgzODA1Igyof6L7btAdDtw8VT0q3APNQGvHN222OQ3W8811fkHZer%2FrNiKJVVYk%2FNfYj4DUnBEDW98rML9dh1dVErHrq1gWTQs3uQFc0vL930FafZprPqHuPqDC43%2FBVZSG93mprS9oJzI19wg6nUZ4%2BS7dzEFS5h1XZ3PUSRpv16xx0nKF%2FTMwP29QdwEl3YX8S%2FK9UhN1WJZ4a%2B91DEmMTIO4sj01HIZ8jtk5J%2Fs1g1nkbu74LexZrQ9t21KS3igO1IyvNWip0mcNaGHbfAl6RCjyhzGrM853PB5Xtbt9AplLNjK%2BR%2BR4YUMLvsHo6JpmK9nFFQ%2BL%2BhZvSkbgsUdevGL3pidbfsdKMoq5OuAQcLAWRs58I1NAo%2FM7xYfd5lbUcaXqNmL5ikMmGd7y%2Bl%2FJVgGwDovmIUgCaAqm99a0W2GE5zAKvTwLj1zEFuSrYkypdFgm4zjaTk2RWR6g2rKwOs%2Bq1SLyopkAnr7etPdEt%2Frkmr52t%2FfXXwpBdfUACjMfbQbYbHtlLPLQISGfL2WlMjRWlI8RgkFxzS%2BVwmwbL%2BwN70dyd3IfrogiZzX5wilD7ojnUlXOjTECkASfyr0jU%2F16h%2BKisPeaZ%2Fq7cbGUd%2FlfR8WF4MSiIOFgcyGehkdhIR%2BbWIwpW9%2BrsbEPZX%2F%2FmDC0lIq9BjqkAQsRF2QUu6tHpREMQtszwJZrGJxV%2FYLL8zSvJjAuQ2IbTIIW1OZseSxpiMNMgERJ4rmyDQHUZLJDKb7WYWst8DSAfNZI9PezAC3Q7wNxdNYVINaYs8v1xR5k0w2IPjufw1uUMrerj28Q5r9RDsMdgOSGdPsutI8eU%2BYfKYdCth8rlUEeasXGUV%2BwxSVz7Ry74JMt2HPDc2IlK1ZHqvTtoiRG9Dcq&X-Amz-Signature=998ee70406fdb7c73cbee4270f025202a15f7482b88a0f9b2c90d0ac627802e7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNUSO4DB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCuYtd4HlCOkLBaJ6z46i6xxNbYjSVeH2P6iuw%2B3jNghQIhAOkufCJ0GmCZzMQ06%2FLrbbL4K1fcm0pjU5j0PW5RiNGPKv8DCDcQABoMNjM3NDIzMTgzODA1Igyof6L7btAdDtw8VT0q3APNQGvHN222OQ3W8811fkHZer%2FrNiKJVVYk%2FNfYj4DUnBEDW98rML9dh1dVErHrq1gWTQs3uQFc0vL930FafZprPqHuPqDC43%2FBVZSG93mprS9oJzI19wg6nUZ4%2BS7dzEFS5h1XZ3PUSRpv16xx0nKF%2FTMwP29QdwEl3YX8S%2FK9UhN1WJZ4a%2B91DEmMTIO4sj01HIZ8jtk5J%2Fs1g1nkbu74LexZrQ9t21KS3igO1IyvNWip0mcNaGHbfAl6RCjyhzGrM853PB5Xtbt9AplLNjK%2BR%2BR4YUMLvsHo6JpmK9nFFQ%2BL%2BhZvSkbgsUdevGL3pidbfsdKMoq5OuAQcLAWRs58I1NAo%2FM7xYfd5lbUcaXqNmL5ikMmGd7y%2Bl%2FJVgGwDovmIUgCaAqm99a0W2GE5zAKvTwLj1zEFuSrYkypdFgm4zjaTk2RWR6g2rKwOs%2Bq1SLyopkAnr7etPdEt%2Frkmr52t%2FfXXwpBdfUACjMfbQbYbHtlLPLQISGfL2WlMjRWlI8RgkFxzS%2BVwmwbL%2BwN70dyd3IfrogiZzX5wilD7ojnUlXOjTECkASfyr0jU%2F16h%2BKisPeaZ%2Fq7cbGUd%2FlfR8WF4MSiIOFgcyGehkdhIR%2BbWIwpW9%2BrsbEPZX%2F%2FmDC0lIq9BjqkAQsRF2QUu6tHpREMQtszwJZrGJxV%2FYLL8zSvJjAuQ2IbTIIW1OZseSxpiMNMgERJ4rmyDQHUZLJDKb7WYWst8DSAfNZI9PezAC3Q7wNxdNYVINaYs8v1xR5k0w2IPjufw1uUMrerj28Q5r9RDsMdgOSGdPsutI8eU%2BYfKYdCth8rlUEeasXGUV%2BwxSVz7Ry74JMt2HPDc2IlK1ZHqvTtoiRG9Dcq&X-Amz-Signature=323db43acc1c29a20616a9f911a92b7ea9dd492847fc0392dec7af082aa8999a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLH5DGUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDVGPrKZAJiDJ3bGbOd38cp3YdoKPczOSgzoi4jg%2BNwmQIhAN20TvNJejZ3Gs0u6QDk%2BgYJxmc7tANhI9hmtwZQFBwYKv8DCDcQABoMNjM3NDIzMTgzODA1Igw6BS9E2j1zujWGQu0q3APX1tcTPZf7zI6j8h%2BBHmTWsiAJP1Sn96a8%2BDMcV8vTQpd9wVLYooIE2GkhvfMjrkbQZSbF4gm53rmd95eS2tGIKYC0ZL9NevtPD6SKhaPwvGdBkAMvc%2Fu3Var1ZYPdfDFydUf%2BKFEgCSWSAz3ZiYChyvloNhCeveRuSV9lJ9RHqFdVvUJM1MsqG7Jzo1pURS2csYBlVGwlXF4yIGOF3mVPgAXrM7Lbn%2B5N0%2F%2FREdAlZxEs3znb6Yh%2FDgnEVzN5oL%2F%2BDqOF%2F08iHhib5JSV9Ji%2FfdvGi7qz2cRrqfJgoGQJWJ%2B2VkEw1VCz63pNQ7BaMN8yY1cs0Ht1y%2FhM7N08AvQrC4%2BtJBuhEJqCYMqjl2gFTiOCHoMwY%2BD2cECs9hYZYZZC3OgEI9um5%2FGwUoOR%2BCaeP5nIe%2FWUpK13Axc9aDjXCvhuxYS%2FZ2t3z%2FmpcbX4wJ6tgUVM9zwdGQ3lSWPwZZHgQs328Aw1ytVZe5JtMb9Phyq8e3wP33tRflk1K85IsRpIx2EzhptP%2BcOCael6FMadQ1ozoVU87va72sFwaBf6ioZAnqgWo9N%2FlVCtskUUjWjeNWK%2FOLe8V0ot0G1d9I9s5rxGzWfRKhMPUFPg0ftssPFGCy70QO3IK5DOOzCflIq9BjqkARWqCjk6Ps%2BQesLMS%2BLdiopK3O4YuAdjO595KIFjV6WNAwY6oYzVQDEsS1VEhbPrBrFa5z7Xqmfk1ZES0LX2hHguuKUA1iGelvZI%2B4q%2Fd701vi0i5c2XfOTpt%2BN%2BZsol%2BW1mOcmNejd29FZNRwwBguNClFZG5xRNDmWQEi3qTNulfAGWOZRcGbTmvYq3ED9zKwcFhRx4IeDt9GsuraJbk4HvA2FW&X-Amz-Signature=fd4ed7bf82954abe08a5099d82dfaf5bc615d5dbeb659e1a806ced80e36131c3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLH5DGUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDVGPrKZAJiDJ3bGbOd38cp3YdoKPczOSgzoi4jg%2BNwmQIhAN20TvNJejZ3Gs0u6QDk%2BgYJxmc7tANhI9hmtwZQFBwYKv8DCDcQABoMNjM3NDIzMTgzODA1Igw6BS9E2j1zujWGQu0q3APX1tcTPZf7zI6j8h%2BBHmTWsiAJP1Sn96a8%2BDMcV8vTQpd9wVLYooIE2GkhvfMjrkbQZSbF4gm53rmd95eS2tGIKYC0ZL9NevtPD6SKhaPwvGdBkAMvc%2Fu3Var1ZYPdfDFydUf%2BKFEgCSWSAz3ZiYChyvloNhCeveRuSV9lJ9RHqFdVvUJM1MsqG7Jzo1pURS2csYBlVGwlXF4yIGOF3mVPgAXrM7Lbn%2B5N0%2F%2FREdAlZxEs3znb6Yh%2FDgnEVzN5oL%2F%2BDqOF%2F08iHhib5JSV9Ji%2FfdvGi7qz2cRrqfJgoGQJWJ%2B2VkEw1VCz63pNQ7BaMN8yY1cs0Ht1y%2FhM7N08AvQrC4%2BtJBuhEJqCYMqjl2gFTiOCHoMwY%2BD2cECs9hYZYZZC3OgEI9um5%2FGwUoOR%2BCaeP5nIe%2FWUpK13Axc9aDjXCvhuxYS%2FZ2t3z%2FmpcbX4wJ6tgUVM9zwdGQ3lSWPwZZHgQs328Aw1ytVZe5JtMb9Phyq8e3wP33tRflk1K85IsRpIx2EzhptP%2BcOCael6FMadQ1ozoVU87va72sFwaBf6ioZAnqgWo9N%2FlVCtskUUjWjeNWK%2FOLe8V0ot0G1d9I9s5rxGzWfRKhMPUFPg0ftssPFGCy70QO3IK5DOOzCflIq9BjqkARWqCjk6Ps%2BQesLMS%2BLdiopK3O4YuAdjO595KIFjV6WNAwY6oYzVQDEsS1VEhbPrBrFa5z7Xqmfk1ZES0LX2hHguuKUA1iGelvZI%2B4q%2Fd701vi0i5c2XfOTpt%2BN%2BZsol%2BW1mOcmNejd29FZNRwwBguNClFZG5xRNDmWQEi3qTNulfAGWOZRcGbTmvYq3ED9zKwcFhRx4IeDt9GsuraJbk4HvA2FW&X-Amz-Signature=356602837fd58177a5abba9b4c5b6f03525108b1cbc4d4baa3245cc74e2c3e0a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLH5DGUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDVGPrKZAJiDJ3bGbOd38cp3YdoKPczOSgzoi4jg%2BNwmQIhAN20TvNJejZ3Gs0u6QDk%2BgYJxmc7tANhI9hmtwZQFBwYKv8DCDcQABoMNjM3NDIzMTgzODA1Igw6BS9E2j1zujWGQu0q3APX1tcTPZf7zI6j8h%2BBHmTWsiAJP1Sn96a8%2BDMcV8vTQpd9wVLYooIE2GkhvfMjrkbQZSbF4gm53rmd95eS2tGIKYC0ZL9NevtPD6SKhaPwvGdBkAMvc%2Fu3Var1ZYPdfDFydUf%2BKFEgCSWSAz3ZiYChyvloNhCeveRuSV9lJ9RHqFdVvUJM1MsqG7Jzo1pURS2csYBlVGwlXF4yIGOF3mVPgAXrM7Lbn%2B5N0%2F%2FREdAlZxEs3znb6Yh%2FDgnEVzN5oL%2F%2BDqOF%2F08iHhib5JSV9Ji%2FfdvGi7qz2cRrqfJgoGQJWJ%2B2VkEw1VCz63pNQ7BaMN8yY1cs0Ht1y%2FhM7N08AvQrC4%2BtJBuhEJqCYMqjl2gFTiOCHoMwY%2BD2cECs9hYZYZZC3OgEI9um5%2FGwUoOR%2BCaeP5nIe%2FWUpK13Axc9aDjXCvhuxYS%2FZ2t3z%2FmpcbX4wJ6tgUVM9zwdGQ3lSWPwZZHgQs328Aw1ytVZe5JtMb9Phyq8e3wP33tRflk1K85IsRpIx2EzhptP%2BcOCael6FMadQ1ozoVU87va72sFwaBf6ioZAnqgWo9N%2FlVCtskUUjWjeNWK%2FOLe8V0ot0G1d9I9s5rxGzWfRKhMPUFPg0ftssPFGCy70QO3IK5DOOzCflIq9BjqkARWqCjk6Ps%2BQesLMS%2BLdiopK3O4YuAdjO595KIFjV6WNAwY6oYzVQDEsS1VEhbPrBrFa5z7Xqmfk1ZES0LX2hHguuKUA1iGelvZI%2B4q%2Fd701vi0i5c2XfOTpt%2BN%2BZsol%2BW1mOcmNejd29FZNRwwBguNClFZG5xRNDmWQEi3qTNulfAGWOZRcGbTmvYq3ED9zKwcFhRx4IeDt9GsuraJbk4HvA2FW&X-Amz-Signature=61ed01c4f4ad2a69dc59e720b92e8794c7b09f79531f955e2dadcc13ff699a8b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLH5DGUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDVGPrKZAJiDJ3bGbOd38cp3YdoKPczOSgzoi4jg%2BNwmQIhAN20TvNJejZ3Gs0u6QDk%2BgYJxmc7tANhI9hmtwZQFBwYKv8DCDcQABoMNjM3NDIzMTgzODA1Igw6BS9E2j1zujWGQu0q3APX1tcTPZf7zI6j8h%2BBHmTWsiAJP1Sn96a8%2BDMcV8vTQpd9wVLYooIE2GkhvfMjrkbQZSbF4gm53rmd95eS2tGIKYC0ZL9NevtPD6SKhaPwvGdBkAMvc%2Fu3Var1ZYPdfDFydUf%2BKFEgCSWSAz3ZiYChyvloNhCeveRuSV9lJ9RHqFdVvUJM1MsqG7Jzo1pURS2csYBlVGwlXF4yIGOF3mVPgAXrM7Lbn%2B5N0%2F%2FREdAlZxEs3znb6Yh%2FDgnEVzN5oL%2F%2BDqOF%2F08iHhib5JSV9Ji%2FfdvGi7qz2cRrqfJgoGQJWJ%2B2VkEw1VCz63pNQ7BaMN8yY1cs0Ht1y%2FhM7N08AvQrC4%2BtJBuhEJqCYMqjl2gFTiOCHoMwY%2BD2cECs9hYZYZZC3OgEI9um5%2FGwUoOR%2BCaeP5nIe%2FWUpK13Axc9aDjXCvhuxYS%2FZ2t3z%2FmpcbX4wJ6tgUVM9zwdGQ3lSWPwZZHgQs328Aw1ytVZe5JtMb9Phyq8e3wP33tRflk1K85IsRpIx2EzhptP%2BcOCael6FMadQ1ozoVU87va72sFwaBf6ioZAnqgWo9N%2FlVCtskUUjWjeNWK%2FOLe8V0ot0G1d9I9s5rxGzWfRKhMPUFPg0ftssPFGCy70QO3IK5DOOzCflIq9BjqkARWqCjk6Ps%2BQesLMS%2BLdiopK3O4YuAdjO595KIFjV6WNAwY6oYzVQDEsS1VEhbPrBrFa5z7Xqmfk1ZES0LX2hHguuKUA1iGelvZI%2B4q%2Fd701vi0i5c2XfOTpt%2BN%2BZsol%2BW1mOcmNejd29FZNRwwBguNClFZG5xRNDmWQEi3qTNulfAGWOZRcGbTmvYq3ED9zKwcFhRx4IeDt9GsuraJbk4HvA2FW&X-Amz-Signature=c2bb02824d54f96741c3d9e156d010a8a3796349a32b9e87b5b6790d63641941&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLH5DGUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDVGPrKZAJiDJ3bGbOd38cp3YdoKPczOSgzoi4jg%2BNwmQIhAN20TvNJejZ3Gs0u6QDk%2BgYJxmc7tANhI9hmtwZQFBwYKv8DCDcQABoMNjM3NDIzMTgzODA1Igw6BS9E2j1zujWGQu0q3APX1tcTPZf7zI6j8h%2BBHmTWsiAJP1Sn96a8%2BDMcV8vTQpd9wVLYooIE2GkhvfMjrkbQZSbF4gm53rmd95eS2tGIKYC0ZL9NevtPD6SKhaPwvGdBkAMvc%2Fu3Var1ZYPdfDFydUf%2BKFEgCSWSAz3ZiYChyvloNhCeveRuSV9lJ9RHqFdVvUJM1MsqG7Jzo1pURS2csYBlVGwlXF4yIGOF3mVPgAXrM7Lbn%2B5N0%2F%2FREdAlZxEs3znb6Yh%2FDgnEVzN5oL%2F%2BDqOF%2F08iHhib5JSV9Ji%2FfdvGi7qz2cRrqfJgoGQJWJ%2B2VkEw1VCz63pNQ7BaMN8yY1cs0Ht1y%2FhM7N08AvQrC4%2BtJBuhEJqCYMqjl2gFTiOCHoMwY%2BD2cECs9hYZYZZC3OgEI9um5%2FGwUoOR%2BCaeP5nIe%2FWUpK13Axc9aDjXCvhuxYS%2FZ2t3z%2FmpcbX4wJ6tgUVM9zwdGQ3lSWPwZZHgQs328Aw1ytVZe5JtMb9Phyq8e3wP33tRflk1K85IsRpIx2EzhptP%2BcOCael6FMadQ1ozoVU87va72sFwaBf6ioZAnqgWo9N%2FlVCtskUUjWjeNWK%2FOLe8V0ot0G1d9I9s5rxGzWfRKhMPUFPg0ftssPFGCy70QO3IK5DOOzCflIq9BjqkARWqCjk6Ps%2BQesLMS%2BLdiopK3O4YuAdjO595KIFjV6WNAwY6oYzVQDEsS1VEhbPrBrFa5z7Xqmfk1ZES0LX2hHguuKUA1iGelvZI%2B4q%2Fd701vi0i5c2XfOTpt%2BN%2BZsol%2BW1mOcmNejd29FZNRwwBguNClFZG5xRNDmWQEi3qTNulfAGWOZRcGbTmvYq3ED9zKwcFhRx4IeDt9GsuraJbk4HvA2FW&X-Amz-Signature=668bc7fe2ae6d5d1465d155c902aaaa3f3adeaecc2f0cea3f92ec3ac496327f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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


