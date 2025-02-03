

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DR2QATV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIGkUBZbbFu3cgFgCZktt8Dz9kk%2FkdlEvtsur6BQ5B8%2BCAiAsmL7Jg2KIwx0h0cNhvaXWQ4%2F%2FeoctqKUSg2T96wGcuir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM7g9I7VxzDjsPshrmKtwDQ2lEGfJXEYPMbQg1WYFTm%2BHTi5Vt0gRqN40ye%2BzqaK0zB7e1JLCmyoCgU22%2FhFQEl4mL%2FN9tLHDKM9r3yCkcqOCJ%2B0nL3SWc0%2Fp6i1WfumO%2BaJh6dE7KHKaWd%2F7s3%2B4Qly13m1XnC2FkDEJCIfTgAyeKqmVF1BuRsddw0lhyopk4Sf%2Bh9snQAjcryJT%2F9MAq%2FF50Q%2BmZXRWilMrp1uOnyniZnPN5uxeRDW0DN91SnnnlZ9GCWpmRyeVuRtX7igZEFwzmZBh%2BvE3hZwKuZncvhr5iSxgBJP%2FBAml9EWZl8BTkmwdVi7kOyOdGIrZfzvSSnLr%2FH%2BbjMYW9XanTwQGN2Ybul4LT6FGM4QdBBTGQY8btv1k4wg%2BIpBue3BED0oPQGBhnr8DfabkvFPmjrW%2BsqJt4ndmaVZcwuOjrJ63i%2F1OOgLV4ucxQhWJd9KUkeD8fxST7Cv%2FeGZwRvEK1WYy8ciXVUXVaeBJkmkVX6JbrcCUZQJbkPzgu9hVykX%2BmOAwBx%2FQAaJvg9zDUmNQ%2BVV8Cn77FxPWNO5uIcuxXUXMpQ1KEb%2FtduTp2Eu6%2BLomzvdW1sQ9CQua68wlx%2B2lPupiqggFmybdX%2BuqEmbp99tEKbEv9zgtF4ToPIJHO6XAw0JOFvQY6pgGRfFa7sbeOGXOkwiaPN9Djm%2BWLp5WV6VbQZLdZyPvdsNyUQAHNazq8SuCuFWRuxISPsvcmc8dOJiWQnA6Uva5zLLS%2BvLo6DwQwUvVFWAbYNWDJk%2F2rHrzJ8rhTBOk0DIsuE5FfdcxYwq59TfB8ej%2BEFGFF523E8oPJB15FTv6eh8Ik3VXfOY%2FborTXk14PTbPDGiV9p%2FPH6lEd0ShkbSJgoSyXDQ1%2B&X-Amz-Signature=35f95690beac6b1725a3e0c04203fef19a3e2af4d9cdf4908eb017bd2a3e6287&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTCAJJUY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBGfEsExmpwJh6lQGvqYGHEP%2FeAV32htSG5xVb5pY0tWAiEArsMFaxTkBDdHgJa5qLFvPj9e7NALHhFmhNcKyeEfz9Eq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNe77vpFvpE4d9CklCrcAz0s0FMHDY80%2FVypyBPUpRVA%2B7tWaJ7h2ET4jDtR5jIFrFqYbthqEyGgaIb8VE3HmK9G8MleoEnHiJypnBDxXdMVhbB677fGViLzJV03FWuR8jOyGU7gcH8%2ByDOfxoYgdy1lExveVMc9LcxNU7MHvBvFXjy0r7840mGgpu1WkjXqBTbVkVzeI3feIo%2FnAkwTT81NX6Xub%2BF16v%2FswhsPc1eSK5Tw9Q9OtcXuwxLw3SGk%2FHHDIvrucu8%2BxSU9vOFXbrZGeGCfiZgXNkBZlp4p%2FIxuD2q54yKwP%2BHL07lo1ipiin9a23SUGw%2FWRQ78v%2F9zI0g2XXe3UF5Ew47yFGw49DZ0jd6kfFgZYQsh4TJh512Hv1hgkQWgLAt9prxZIr1E9JbhcKhbvLd2Jk8BWKhbhNntQI%2F%2FdPC0hAY%2F4RKCjJsx46WbP%2FMlMDvcN5ZqI66%2BJZtXD5mta460%2FQ0auDrIo4DAD2jsbcafttvPkTfskGi9sKISs0VqbQUb0FMmABUqCa9Es1YiyesX%2FSe%2FPEsAn%2FgZDciBoM5z7V%2FNGbVIY81h94Jg3Ec92iC%2Fsi0s0N3OLsvx%2FBkqcR3E5q0car4znTHB3NT7CxH1GHgblEWXObDQ4vGkCbgTWoJRM1aNMLeUhb0GOqUBpZvy3%2Bkf0bDI2JHm393A%2FFdBuzBFmmT9BYxvRZmyNMibT%2BsYl9cPZFH3v%2FgeS7bf0Et8r2qUzzaiMQH%2F5GFs8DW4aY3prdfF1yW1lQ2Vi3Ktvvk8zLwTosHoBWi1JhHVItr%2F%2Fs%2BYyECpx2TNNM5SmhVjnNFFfwFjdOJVO6GAUYjriWdfYxbKJ7QUj49aZMipJ52b50Y7YHTPxcwW6jAiDIJr3Rac&X-Amz-Signature=f4278f0c96e25fc7950dbc6de3a1f5062776ed29015ba008374c0d7ec5e2cdee&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTCAJJUY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBGfEsExmpwJh6lQGvqYGHEP%2FeAV32htSG5xVb5pY0tWAiEArsMFaxTkBDdHgJa5qLFvPj9e7NALHhFmhNcKyeEfz9Eq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNe77vpFvpE4d9CklCrcAz0s0FMHDY80%2FVypyBPUpRVA%2B7tWaJ7h2ET4jDtR5jIFrFqYbthqEyGgaIb8VE3HmK9G8MleoEnHiJypnBDxXdMVhbB677fGViLzJV03FWuR8jOyGU7gcH8%2ByDOfxoYgdy1lExveVMc9LcxNU7MHvBvFXjy0r7840mGgpu1WkjXqBTbVkVzeI3feIo%2FnAkwTT81NX6Xub%2BF16v%2FswhsPc1eSK5Tw9Q9OtcXuwxLw3SGk%2FHHDIvrucu8%2BxSU9vOFXbrZGeGCfiZgXNkBZlp4p%2FIxuD2q54yKwP%2BHL07lo1ipiin9a23SUGw%2FWRQ78v%2F9zI0g2XXe3UF5Ew47yFGw49DZ0jd6kfFgZYQsh4TJh512Hv1hgkQWgLAt9prxZIr1E9JbhcKhbvLd2Jk8BWKhbhNntQI%2F%2FdPC0hAY%2F4RKCjJsx46WbP%2FMlMDvcN5ZqI66%2BJZtXD5mta460%2FQ0auDrIo4DAD2jsbcafttvPkTfskGi9sKISs0VqbQUb0FMmABUqCa9Es1YiyesX%2FSe%2FPEsAn%2FgZDciBoM5z7V%2FNGbVIY81h94Jg3Ec92iC%2Fsi0s0N3OLsvx%2FBkqcR3E5q0car4znTHB3NT7CxH1GHgblEWXObDQ4vGkCbgTWoJRM1aNMLeUhb0GOqUBpZvy3%2Bkf0bDI2JHm393A%2FFdBuzBFmmT9BYxvRZmyNMibT%2BsYl9cPZFH3v%2FgeS7bf0Et8r2qUzzaiMQH%2F5GFs8DW4aY3prdfF1yW1lQ2Vi3Ktvvk8zLwTosHoBWi1JhHVItr%2F%2Fs%2BYyECpx2TNNM5SmhVjnNFFfwFjdOJVO6GAUYjriWdfYxbKJ7QUj49aZMipJ52b50Y7YHTPxcwW6jAiDIJr3Rac&X-Amz-Signature=4a44e74e134667de5c935294bd9f042d24c80b85212cd88f4f279598b6a63105&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTCAJJUY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBGfEsExmpwJh6lQGvqYGHEP%2FeAV32htSG5xVb5pY0tWAiEArsMFaxTkBDdHgJa5qLFvPj9e7NALHhFmhNcKyeEfz9Eq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNe77vpFvpE4d9CklCrcAz0s0FMHDY80%2FVypyBPUpRVA%2B7tWaJ7h2ET4jDtR5jIFrFqYbthqEyGgaIb8VE3HmK9G8MleoEnHiJypnBDxXdMVhbB677fGViLzJV03FWuR8jOyGU7gcH8%2ByDOfxoYgdy1lExveVMc9LcxNU7MHvBvFXjy0r7840mGgpu1WkjXqBTbVkVzeI3feIo%2FnAkwTT81NX6Xub%2BF16v%2FswhsPc1eSK5Tw9Q9OtcXuwxLw3SGk%2FHHDIvrucu8%2BxSU9vOFXbrZGeGCfiZgXNkBZlp4p%2FIxuD2q54yKwP%2BHL07lo1ipiin9a23SUGw%2FWRQ78v%2F9zI0g2XXe3UF5Ew47yFGw49DZ0jd6kfFgZYQsh4TJh512Hv1hgkQWgLAt9prxZIr1E9JbhcKhbvLd2Jk8BWKhbhNntQI%2F%2FdPC0hAY%2F4RKCjJsx46WbP%2FMlMDvcN5ZqI66%2BJZtXD5mta460%2FQ0auDrIo4DAD2jsbcafttvPkTfskGi9sKISs0VqbQUb0FMmABUqCa9Es1YiyesX%2FSe%2FPEsAn%2FgZDciBoM5z7V%2FNGbVIY81h94Jg3Ec92iC%2Fsi0s0N3OLsvx%2FBkqcR3E5q0car4znTHB3NT7CxH1GHgblEWXObDQ4vGkCbgTWoJRM1aNMLeUhb0GOqUBpZvy3%2Bkf0bDI2JHm393A%2FFdBuzBFmmT9BYxvRZmyNMibT%2BsYl9cPZFH3v%2FgeS7bf0Et8r2qUzzaiMQH%2F5GFs8DW4aY3prdfF1yW1lQ2Vi3Ktvvk8zLwTosHoBWi1JhHVItr%2F%2Fs%2BYyECpx2TNNM5SmhVjnNFFfwFjdOJVO6GAUYjriWdfYxbKJ7QUj49aZMipJ52b50Y7YHTPxcwW6jAiDIJr3Rac&X-Amz-Signature=9dd20076cc628b46a9f32b6199d194fb7d564ff17cbec8018d466a225adcc275&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTCAJJUY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBGfEsExmpwJh6lQGvqYGHEP%2FeAV32htSG5xVb5pY0tWAiEArsMFaxTkBDdHgJa5qLFvPj9e7NALHhFmhNcKyeEfz9Eq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNe77vpFvpE4d9CklCrcAz0s0FMHDY80%2FVypyBPUpRVA%2B7tWaJ7h2ET4jDtR5jIFrFqYbthqEyGgaIb8VE3HmK9G8MleoEnHiJypnBDxXdMVhbB677fGViLzJV03FWuR8jOyGU7gcH8%2ByDOfxoYgdy1lExveVMc9LcxNU7MHvBvFXjy0r7840mGgpu1WkjXqBTbVkVzeI3feIo%2FnAkwTT81NX6Xub%2BF16v%2FswhsPc1eSK5Tw9Q9OtcXuwxLw3SGk%2FHHDIvrucu8%2BxSU9vOFXbrZGeGCfiZgXNkBZlp4p%2FIxuD2q54yKwP%2BHL07lo1ipiin9a23SUGw%2FWRQ78v%2F9zI0g2XXe3UF5Ew47yFGw49DZ0jd6kfFgZYQsh4TJh512Hv1hgkQWgLAt9prxZIr1E9JbhcKhbvLd2Jk8BWKhbhNntQI%2F%2FdPC0hAY%2F4RKCjJsx46WbP%2FMlMDvcN5ZqI66%2BJZtXD5mta460%2FQ0auDrIo4DAD2jsbcafttvPkTfskGi9sKISs0VqbQUb0FMmABUqCa9Es1YiyesX%2FSe%2FPEsAn%2FgZDciBoM5z7V%2FNGbVIY81h94Jg3Ec92iC%2Fsi0s0N3OLsvx%2FBkqcR3E5q0car4znTHB3NT7CxH1GHgblEWXObDQ4vGkCbgTWoJRM1aNMLeUhb0GOqUBpZvy3%2Bkf0bDI2JHm393A%2FFdBuzBFmmT9BYxvRZmyNMibT%2BsYl9cPZFH3v%2FgeS7bf0Et8r2qUzzaiMQH%2F5GFs8DW4aY3prdfF1yW1lQ2Vi3Ktvvk8zLwTosHoBWi1JhHVItr%2F%2Fs%2BYyECpx2TNNM5SmhVjnNFFfwFjdOJVO6GAUYjriWdfYxbKJ7QUj49aZMipJ52b50Y7YHTPxcwW6jAiDIJr3Rac&X-Amz-Signature=f9e69612d5b2527764d18f27ec8b257f495deeccee1877014c63c8d3fae5ac84&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTCAJJUY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBGfEsExmpwJh6lQGvqYGHEP%2FeAV32htSG5xVb5pY0tWAiEArsMFaxTkBDdHgJa5qLFvPj9e7NALHhFmhNcKyeEfz9Eq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNe77vpFvpE4d9CklCrcAz0s0FMHDY80%2FVypyBPUpRVA%2B7tWaJ7h2ET4jDtR5jIFrFqYbthqEyGgaIb8VE3HmK9G8MleoEnHiJypnBDxXdMVhbB677fGViLzJV03FWuR8jOyGU7gcH8%2ByDOfxoYgdy1lExveVMc9LcxNU7MHvBvFXjy0r7840mGgpu1WkjXqBTbVkVzeI3feIo%2FnAkwTT81NX6Xub%2BF16v%2FswhsPc1eSK5Tw9Q9OtcXuwxLw3SGk%2FHHDIvrucu8%2BxSU9vOFXbrZGeGCfiZgXNkBZlp4p%2FIxuD2q54yKwP%2BHL07lo1ipiin9a23SUGw%2FWRQ78v%2F9zI0g2XXe3UF5Ew47yFGw49DZ0jd6kfFgZYQsh4TJh512Hv1hgkQWgLAt9prxZIr1E9JbhcKhbvLd2Jk8BWKhbhNntQI%2F%2FdPC0hAY%2F4RKCjJsx46WbP%2FMlMDvcN5ZqI66%2BJZtXD5mta460%2FQ0auDrIo4DAD2jsbcafttvPkTfskGi9sKISs0VqbQUb0FMmABUqCa9Es1YiyesX%2FSe%2FPEsAn%2FgZDciBoM5z7V%2FNGbVIY81h94Jg3Ec92iC%2Fsi0s0N3OLsvx%2FBkqcR3E5q0car4znTHB3NT7CxH1GHgblEWXObDQ4vGkCbgTWoJRM1aNMLeUhb0GOqUBpZvy3%2Bkf0bDI2JHm393A%2FFdBuzBFmmT9BYxvRZmyNMibT%2BsYl9cPZFH3v%2FgeS7bf0Et8r2qUzzaiMQH%2F5GFs8DW4aY3prdfF1yW1lQ2Vi3Ktvvk8zLwTosHoBWi1JhHVItr%2F%2Fs%2BYyECpx2TNNM5SmhVjnNFFfwFjdOJVO6GAUYjriWdfYxbKJ7QUj49aZMipJ52b50Y7YHTPxcwW6jAiDIJr3Rac&X-Amz-Signature=70e1ee03e07e974d37560fa9dd17c1dd3e4c078d92915408ba0ffd70285e5edd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DR2QATV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIGkUBZbbFu3cgFgCZktt8Dz9kk%2FkdlEvtsur6BQ5B8%2BCAiAsmL7Jg2KIwx0h0cNhvaXWQ4%2F%2FeoctqKUSg2T96wGcuir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM7g9I7VxzDjsPshrmKtwDQ2lEGfJXEYPMbQg1WYFTm%2BHTi5Vt0gRqN40ye%2BzqaK0zB7e1JLCmyoCgU22%2FhFQEl4mL%2FN9tLHDKM9r3yCkcqOCJ%2B0nL3SWc0%2Fp6i1WfumO%2BaJh6dE7KHKaWd%2F7s3%2B4Qly13m1XnC2FkDEJCIfTgAyeKqmVF1BuRsddw0lhyopk4Sf%2Bh9snQAjcryJT%2F9MAq%2FF50Q%2BmZXRWilMrp1uOnyniZnPN5uxeRDW0DN91SnnnlZ9GCWpmRyeVuRtX7igZEFwzmZBh%2BvE3hZwKuZncvhr5iSxgBJP%2FBAml9EWZl8BTkmwdVi7kOyOdGIrZfzvSSnLr%2FH%2BbjMYW9XanTwQGN2Ybul4LT6FGM4QdBBTGQY8btv1k4wg%2BIpBue3BED0oPQGBhnr8DfabkvFPmjrW%2BsqJt4ndmaVZcwuOjrJ63i%2F1OOgLV4ucxQhWJd9KUkeD8fxST7Cv%2FeGZwRvEK1WYy8ciXVUXVaeBJkmkVX6JbrcCUZQJbkPzgu9hVykX%2BmOAwBx%2FQAaJvg9zDUmNQ%2BVV8Cn77FxPWNO5uIcuxXUXMpQ1KEb%2FtduTp2Eu6%2BLomzvdW1sQ9CQua68wlx%2B2lPupiqggFmybdX%2BuqEmbp99tEKbEv9zgtF4ToPIJHO6XAw0JOFvQY6pgGRfFa7sbeOGXOkwiaPN9Djm%2BWLp5WV6VbQZLdZyPvdsNyUQAHNazq8SuCuFWRuxISPsvcmc8dOJiWQnA6Uva5zLLS%2BvLo6DwQwUvVFWAbYNWDJk%2F2rHrzJ8rhTBOk0DIsuE5FfdcxYwq59TfB8ej%2BEFGFF523E8oPJB15FTv6eh8Ik3VXfOY%2FborTXk14PTbPDGiV9p%2FPH6lEd0ShkbSJgoSyXDQ1%2B&X-Amz-Signature=3d480de7b4cabb4caf7fcef013809c20e9cca1fdb5db7cc40fdea3d56385b52d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DR2QATV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIGkUBZbbFu3cgFgCZktt8Dz9kk%2FkdlEvtsur6BQ5B8%2BCAiAsmL7Jg2KIwx0h0cNhvaXWQ4%2F%2FeoctqKUSg2T96wGcuir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM7g9I7VxzDjsPshrmKtwDQ2lEGfJXEYPMbQg1WYFTm%2BHTi5Vt0gRqN40ye%2BzqaK0zB7e1JLCmyoCgU22%2FhFQEl4mL%2FN9tLHDKM9r3yCkcqOCJ%2B0nL3SWc0%2Fp6i1WfumO%2BaJh6dE7KHKaWd%2F7s3%2B4Qly13m1XnC2FkDEJCIfTgAyeKqmVF1BuRsddw0lhyopk4Sf%2Bh9snQAjcryJT%2F9MAq%2FF50Q%2BmZXRWilMrp1uOnyniZnPN5uxeRDW0DN91SnnnlZ9GCWpmRyeVuRtX7igZEFwzmZBh%2BvE3hZwKuZncvhr5iSxgBJP%2FBAml9EWZl8BTkmwdVi7kOyOdGIrZfzvSSnLr%2FH%2BbjMYW9XanTwQGN2Ybul4LT6FGM4QdBBTGQY8btv1k4wg%2BIpBue3BED0oPQGBhnr8DfabkvFPmjrW%2BsqJt4ndmaVZcwuOjrJ63i%2F1OOgLV4ucxQhWJd9KUkeD8fxST7Cv%2FeGZwRvEK1WYy8ciXVUXVaeBJkmkVX6JbrcCUZQJbkPzgu9hVykX%2BmOAwBx%2FQAaJvg9zDUmNQ%2BVV8Cn77FxPWNO5uIcuxXUXMpQ1KEb%2FtduTp2Eu6%2BLomzvdW1sQ9CQua68wlx%2B2lPupiqggFmybdX%2BuqEmbp99tEKbEv9zgtF4ToPIJHO6XAw0JOFvQY6pgGRfFa7sbeOGXOkwiaPN9Djm%2BWLp5WV6VbQZLdZyPvdsNyUQAHNazq8SuCuFWRuxISPsvcmc8dOJiWQnA6Uva5zLLS%2BvLo6DwQwUvVFWAbYNWDJk%2F2rHrzJ8rhTBOk0DIsuE5FfdcxYwq59TfB8ej%2BEFGFF523E8oPJB15FTv6eh8Ik3VXfOY%2FborTXk14PTbPDGiV9p%2FPH6lEd0ShkbSJgoSyXDQ1%2B&X-Amz-Signature=175ef3462520655c6c69a94415cf995e590a0f9bd937f561e15d725fc84fb4d1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DR2QATV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIGkUBZbbFu3cgFgCZktt8Dz9kk%2FkdlEvtsur6BQ5B8%2BCAiAsmL7Jg2KIwx0h0cNhvaXWQ4%2F%2FeoctqKUSg2T96wGcuir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM7g9I7VxzDjsPshrmKtwDQ2lEGfJXEYPMbQg1WYFTm%2BHTi5Vt0gRqN40ye%2BzqaK0zB7e1JLCmyoCgU22%2FhFQEl4mL%2FN9tLHDKM9r3yCkcqOCJ%2B0nL3SWc0%2Fp6i1WfumO%2BaJh6dE7KHKaWd%2F7s3%2B4Qly13m1XnC2FkDEJCIfTgAyeKqmVF1BuRsddw0lhyopk4Sf%2Bh9snQAjcryJT%2F9MAq%2FF50Q%2BmZXRWilMrp1uOnyniZnPN5uxeRDW0DN91SnnnlZ9GCWpmRyeVuRtX7igZEFwzmZBh%2BvE3hZwKuZncvhr5iSxgBJP%2FBAml9EWZl8BTkmwdVi7kOyOdGIrZfzvSSnLr%2FH%2BbjMYW9XanTwQGN2Ybul4LT6FGM4QdBBTGQY8btv1k4wg%2BIpBue3BED0oPQGBhnr8DfabkvFPmjrW%2BsqJt4ndmaVZcwuOjrJ63i%2F1OOgLV4ucxQhWJd9KUkeD8fxST7Cv%2FeGZwRvEK1WYy8ciXVUXVaeBJkmkVX6JbrcCUZQJbkPzgu9hVykX%2BmOAwBx%2FQAaJvg9zDUmNQ%2BVV8Cn77FxPWNO5uIcuxXUXMpQ1KEb%2FtduTp2Eu6%2BLomzvdW1sQ9CQua68wlx%2B2lPupiqggFmybdX%2BuqEmbp99tEKbEv9zgtF4ToPIJHO6XAw0JOFvQY6pgGRfFa7sbeOGXOkwiaPN9Djm%2BWLp5WV6VbQZLdZyPvdsNyUQAHNazq8SuCuFWRuxISPsvcmc8dOJiWQnA6Uva5zLLS%2BvLo6DwQwUvVFWAbYNWDJk%2F2rHrzJ8rhTBOk0DIsuE5FfdcxYwq59TfB8ej%2BEFGFF523E8oPJB15FTv6eh8Ik3VXfOY%2FborTXk14PTbPDGiV9p%2FPH6lEd0ShkbSJgoSyXDQ1%2B&X-Amz-Signature=4b2043bce571d575cea2a85c77762032cf8a6ad38a72f00d0f5eba46ef6b07b7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DR2QATV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIGkUBZbbFu3cgFgCZktt8Dz9kk%2FkdlEvtsur6BQ5B8%2BCAiAsmL7Jg2KIwx0h0cNhvaXWQ4%2F%2FeoctqKUSg2T96wGcuir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM7g9I7VxzDjsPshrmKtwDQ2lEGfJXEYPMbQg1WYFTm%2BHTi5Vt0gRqN40ye%2BzqaK0zB7e1JLCmyoCgU22%2FhFQEl4mL%2FN9tLHDKM9r3yCkcqOCJ%2B0nL3SWc0%2Fp6i1WfumO%2BaJh6dE7KHKaWd%2F7s3%2B4Qly13m1XnC2FkDEJCIfTgAyeKqmVF1BuRsddw0lhyopk4Sf%2Bh9snQAjcryJT%2F9MAq%2FF50Q%2BmZXRWilMrp1uOnyniZnPN5uxeRDW0DN91SnnnlZ9GCWpmRyeVuRtX7igZEFwzmZBh%2BvE3hZwKuZncvhr5iSxgBJP%2FBAml9EWZl8BTkmwdVi7kOyOdGIrZfzvSSnLr%2FH%2BbjMYW9XanTwQGN2Ybul4LT6FGM4QdBBTGQY8btv1k4wg%2BIpBue3BED0oPQGBhnr8DfabkvFPmjrW%2BsqJt4ndmaVZcwuOjrJ63i%2F1OOgLV4ucxQhWJd9KUkeD8fxST7Cv%2FeGZwRvEK1WYy8ciXVUXVaeBJkmkVX6JbrcCUZQJbkPzgu9hVykX%2BmOAwBx%2FQAaJvg9zDUmNQ%2BVV8Cn77FxPWNO5uIcuxXUXMpQ1KEb%2FtduTp2Eu6%2BLomzvdW1sQ9CQua68wlx%2B2lPupiqggFmybdX%2BuqEmbp99tEKbEv9zgtF4ToPIJHO6XAw0JOFvQY6pgGRfFa7sbeOGXOkwiaPN9Djm%2BWLp5WV6VbQZLdZyPvdsNyUQAHNazq8SuCuFWRuxISPsvcmc8dOJiWQnA6Uva5zLLS%2BvLo6DwQwUvVFWAbYNWDJk%2F2rHrzJ8rhTBOk0DIsuE5FfdcxYwq59TfB8ej%2BEFGFF523E8oPJB15FTv6eh8Ik3VXfOY%2FborTXk14PTbPDGiV9p%2FPH6lEd0ShkbSJgoSyXDQ1%2B&X-Amz-Signature=af9d7577bae6cf8e8ef8ab69c16c09456e5b2f8088821c6df50d015fa5c9fdb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DR2QATV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIGkUBZbbFu3cgFgCZktt8Dz9kk%2FkdlEvtsur6BQ5B8%2BCAiAsmL7Jg2KIwx0h0cNhvaXWQ4%2F%2FeoctqKUSg2T96wGcuir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM7g9I7VxzDjsPshrmKtwDQ2lEGfJXEYPMbQg1WYFTm%2BHTi5Vt0gRqN40ye%2BzqaK0zB7e1JLCmyoCgU22%2FhFQEl4mL%2FN9tLHDKM9r3yCkcqOCJ%2B0nL3SWc0%2Fp6i1WfumO%2BaJh6dE7KHKaWd%2F7s3%2B4Qly13m1XnC2FkDEJCIfTgAyeKqmVF1BuRsddw0lhyopk4Sf%2Bh9snQAjcryJT%2F9MAq%2FF50Q%2BmZXRWilMrp1uOnyniZnPN5uxeRDW0DN91SnnnlZ9GCWpmRyeVuRtX7igZEFwzmZBh%2BvE3hZwKuZncvhr5iSxgBJP%2FBAml9EWZl8BTkmwdVi7kOyOdGIrZfzvSSnLr%2FH%2BbjMYW9XanTwQGN2Ybul4LT6FGM4QdBBTGQY8btv1k4wg%2BIpBue3BED0oPQGBhnr8DfabkvFPmjrW%2BsqJt4ndmaVZcwuOjrJ63i%2F1OOgLV4ucxQhWJd9KUkeD8fxST7Cv%2FeGZwRvEK1WYy8ciXVUXVaeBJkmkVX6JbrcCUZQJbkPzgu9hVykX%2BmOAwBx%2FQAaJvg9zDUmNQ%2BVV8Cn77FxPWNO5uIcuxXUXMpQ1KEb%2FtduTp2Eu6%2BLomzvdW1sQ9CQua68wlx%2B2lPupiqggFmybdX%2BuqEmbp99tEKbEv9zgtF4ToPIJHO6XAw0JOFvQY6pgGRfFa7sbeOGXOkwiaPN9Djm%2BWLp5WV6VbQZLdZyPvdsNyUQAHNazq8SuCuFWRuxISPsvcmc8dOJiWQnA6Uva5zLLS%2BvLo6DwQwUvVFWAbYNWDJk%2F2rHrzJ8rhTBOk0DIsuE5FfdcxYwq59TfB8ej%2BEFGFF523E8oPJB15FTv6eh8Ik3VXfOY%2FborTXk14PTbPDGiV9p%2FPH6lEd0ShkbSJgoSyXDQ1%2B&X-Amz-Signature=6cc6a614478679efba33848765fe9ece6e93cce14b6dae90ce2b8c2f9e2f53f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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


