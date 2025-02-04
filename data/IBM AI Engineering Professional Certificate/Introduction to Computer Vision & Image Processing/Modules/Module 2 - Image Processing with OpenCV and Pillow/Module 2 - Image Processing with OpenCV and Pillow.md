

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HFZ6WYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIEx8XziZRQCZ500MXk7C0cZZp8UxmxbxE%2BPhpikj7X1cAiEAskYepsmBemgb3Lg0M5CQOgMQKCVziUXQcbR%2B5WnFT8Iq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDMjErdexK1y1JwUu4CrcAyc4%2FzLjfzthuar9XN3rvSo1el7btHNdUfkZeHIr%2BMpIpwqhxQeihOSaWTQnk6eLlfYaxbzY0gzoGm1qFWexCni81ZXdAoT9rjJRsjuSis96PqCeclGREXcBOFCEVdaL0UISYJ%2FN9WFkQfM3%2Fl1%2Fr%2FrqSx%2FsaPc9ddz8ItG%2FaiLqX6NGmdqtMOxf%2F6KJdwxC1%2B1bvpauezZb2PKjr1%2B%2BHEDx10reLeAuie82RA4krE%2FdzOCb1xjUEt7VpxjzI%2FxXrsOKiFHIkKCdexCW1PnUTiUneci2Ep9N4ed5wVyiw4TWpnzhz0lfxElG7f0sgdoTSqA6ZEB93ZYmN4hnocRjcJxbAErreasYMz%2F8t%2FEQ1hrDt%2BzAnuzz1VpCi%2B6vppjMrcZln7keCHz6oiBEPy1jlJsPfLKjtC1LCP3%2Fnq5%2BwJyTnGqJ8wUAL%2Ff9UrjrV%2BVsbZuOvupJw6cGwq2Nk4sjdIbPA5Wpd18JhVEvWPWKBEjuxriy6rGrf7HBA4toqtcRAaTnyTH1PcIIrLJbaQdxC8pgVNYrCQKIdHQORxhyEB%2FHWE0ccU6fRA7Pe6o%2FR0qCUhchucgJj26shFCL0%2F5MLWi8MOufNJyttTxKRnOa2JnCj7C5seKQVq%2FYqNDnMMihhr0GOqUBc7ydPvgGG%2FksU92U%2BCn%2B91tF0wDKF3L2nsfvtnbarxwS90b4bw76avtu9742g%2F7sa1%2FTG14dgilvyuhANIqbXOLURx6BG9fgMlBwQ7S7vEj9VLKFLSCiv9njmY1VAEPSZwP%2FtjaafopJESUVSYLhgCUMgfTKirCjTA0YmB4AN2WNX1J1SNle%2Bkc5TDMo7gmOvSrBBirN5fMKif8ZE2zPBpCsIoDh&X-Amz-Signature=afd855ce5a5270ca1cce9d7924f3da731b46cd0f85fee8cf044f050ddf28bba4&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KVTPBH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCID8m9KlY%2FoyrI032bn91aRPd5z1NBSH9J%2B6i0D0hzI%2BVAiEA9Te2DSQCX04F71yDjvJSnJxZly9uNV0iqeCoufJD5%2FIq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBYi4%2BmXev3WJrIPnyrcAx2ALAXZCd5e%2BNo9fw8i2oQ6hC%2FgxBr97p0OkN2cwVIcP8HYxzXIJRT%2BDaNSWemD2Tvc0NyBLBJa%2FhQjio%2BGcTGpNiCcDVEtpAwuYsxNjuTmqHjnOF5ALTbnOFdWqg7%2B0%2B6aqSqE%2BjtZnV%2BvUjYkV1Ci9ZtoXPY%2BZo1IUCEHz%2Be0gF25WVMidKJXZ3dsOZaj3tsFrK3UA2VhbuDcGTj%2BiAAC%2BF8o5ohQorZ6l%2BS6OhSJzPgmyUwOogRP9c%2Fxw%2BgmTuHxwYhS2lHM2GO7H6UEpcjOt9Yyo9H23JsepGzKL1kEy2B6c1GSkyLJ0FN%2BrTQR5dBcF03uo7poNdmO1BdbxlGILWijchwpBYYlBw0XgbgCMbGLKTTORonfvJMpC6kCELuBwVjeKxoxTSNefmX5uTKqEY2pGdY0eh7O3ClpielnpNSKJxsYlowq2lx2yoH0cPeeD%2FmcgiCxpkMdaaWFGekGrb4TVqOBN7uWQbDg3nrxyZRu5RYtEt99lKIa%2BUpIq7FjDcsC6IuRMzIrJF1P%2FlwKCDqmIw5AZtIzmIluIEvfQAIG9vspZHosjlZZcM5Dop2z5eWhrXT%2FuzBJAS%2BvcZmeQH6Sz7vAA%2BUZktte1XY9C18s%2FqukzIhjFz1LMPChhr0GOqUBtaSpzBP9OBr3rwfALdpUjeceogujD5vZFclmX87xUsQ8VN9tXCX1dyC5zC5z5UWJc6pLNxDVr%2FC041fOy1eLG3xAD54UpYhhu2Z7%2FenZR8r7UvOTTmVnnwX7yjLoDzEX91XORQsGW%2B7BZ5UDU3CLhObCEIHMjXzzE0mCdrVK9H%2FLvH82IXn5eNQu04iUfK2u8Ah422wr0mumheku8S8CEgwt6D8%2B&X-Amz-Signature=536c1714d8c78111c8d8d5de5ab3189f8315ae85cc784b9d6bc64172fcc505e4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KVTPBH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCID8m9KlY%2FoyrI032bn91aRPd5z1NBSH9J%2B6i0D0hzI%2BVAiEA9Te2DSQCX04F71yDjvJSnJxZly9uNV0iqeCoufJD5%2FIq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBYi4%2BmXev3WJrIPnyrcAx2ALAXZCd5e%2BNo9fw8i2oQ6hC%2FgxBr97p0OkN2cwVIcP8HYxzXIJRT%2BDaNSWemD2Tvc0NyBLBJa%2FhQjio%2BGcTGpNiCcDVEtpAwuYsxNjuTmqHjnOF5ALTbnOFdWqg7%2B0%2B6aqSqE%2BjtZnV%2BvUjYkV1Ci9ZtoXPY%2BZo1IUCEHz%2Be0gF25WVMidKJXZ3dsOZaj3tsFrK3UA2VhbuDcGTj%2BiAAC%2BF8o5ohQorZ6l%2BS6OhSJzPgmyUwOogRP9c%2Fxw%2BgmTuHxwYhS2lHM2GO7H6UEpcjOt9Yyo9H23JsepGzKL1kEy2B6c1GSkyLJ0FN%2BrTQR5dBcF03uo7poNdmO1BdbxlGILWijchwpBYYlBw0XgbgCMbGLKTTORonfvJMpC6kCELuBwVjeKxoxTSNefmX5uTKqEY2pGdY0eh7O3ClpielnpNSKJxsYlowq2lx2yoH0cPeeD%2FmcgiCxpkMdaaWFGekGrb4TVqOBN7uWQbDg3nrxyZRu5RYtEt99lKIa%2BUpIq7FjDcsC6IuRMzIrJF1P%2FlwKCDqmIw5AZtIzmIluIEvfQAIG9vspZHosjlZZcM5Dop2z5eWhrXT%2FuzBJAS%2BvcZmeQH6Sz7vAA%2BUZktte1XY9C18s%2FqukzIhjFz1LMPChhr0GOqUBtaSpzBP9OBr3rwfALdpUjeceogujD5vZFclmX87xUsQ8VN9tXCX1dyC5zC5z5UWJc6pLNxDVr%2FC041fOy1eLG3xAD54UpYhhu2Z7%2FenZR8r7UvOTTmVnnwX7yjLoDzEX91XORQsGW%2B7BZ5UDU3CLhObCEIHMjXzzE0mCdrVK9H%2FLvH82IXn5eNQu04iUfK2u8Ah422wr0mumheku8S8CEgwt6D8%2B&X-Amz-Signature=88324a1e1983fa22bda027cf5a891d3f081b286b33b21e0cbdced638a79718ff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KVTPBH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCID8m9KlY%2FoyrI032bn91aRPd5z1NBSH9J%2B6i0D0hzI%2BVAiEA9Te2DSQCX04F71yDjvJSnJxZly9uNV0iqeCoufJD5%2FIq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBYi4%2BmXev3WJrIPnyrcAx2ALAXZCd5e%2BNo9fw8i2oQ6hC%2FgxBr97p0OkN2cwVIcP8HYxzXIJRT%2BDaNSWemD2Tvc0NyBLBJa%2FhQjio%2BGcTGpNiCcDVEtpAwuYsxNjuTmqHjnOF5ALTbnOFdWqg7%2B0%2B6aqSqE%2BjtZnV%2BvUjYkV1Ci9ZtoXPY%2BZo1IUCEHz%2Be0gF25WVMidKJXZ3dsOZaj3tsFrK3UA2VhbuDcGTj%2BiAAC%2BF8o5ohQorZ6l%2BS6OhSJzPgmyUwOogRP9c%2Fxw%2BgmTuHxwYhS2lHM2GO7H6UEpcjOt9Yyo9H23JsepGzKL1kEy2B6c1GSkyLJ0FN%2BrTQR5dBcF03uo7poNdmO1BdbxlGILWijchwpBYYlBw0XgbgCMbGLKTTORonfvJMpC6kCELuBwVjeKxoxTSNefmX5uTKqEY2pGdY0eh7O3ClpielnpNSKJxsYlowq2lx2yoH0cPeeD%2FmcgiCxpkMdaaWFGekGrb4TVqOBN7uWQbDg3nrxyZRu5RYtEt99lKIa%2BUpIq7FjDcsC6IuRMzIrJF1P%2FlwKCDqmIw5AZtIzmIluIEvfQAIG9vspZHosjlZZcM5Dop2z5eWhrXT%2FuzBJAS%2BvcZmeQH6Sz7vAA%2BUZktte1XY9C18s%2FqukzIhjFz1LMPChhr0GOqUBtaSpzBP9OBr3rwfALdpUjeceogujD5vZFclmX87xUsQ8VN9tXCX1dyC5zC5z5UWJc6pLNxDVr%2FC041fOy1eLG3xAD54UpYhhu2Z7%2FenZR8r7UvOTTmVnnwX7yjLoDzEX91XORQsGW%2B7BZ5UDU3CLhObCEIHMjXzzE0mCdrVK9H%2FLvH82IXn5eNQu04iUfK2u8Ah422wr0mumheku8S8CEgwt6D8%2B&X-Amz-Signature=be3b19d7d03792e14897c9bfc43ea4f157a850811a014a66a31f30390c529fbb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KVTPBH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCID8m9KlY%2FoyrI032bn91aRPd5z1NBSH9J%2B6i0D0hzI%2BVAiEA9Te2DSQCX04F71yDjvJSnJxZly9uNV0iqeCoufJD5%2FIq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBYi4%2BmXev3WJrIPnyrcAx2ALAXZCd5e%2BNo9fw8i2oQ6hC%2FgxBr97p0OkN2cwVIcP8HYxzXIJRT%2BDaNSWemD2Tvc0NyBLBJa%2FhQjio%2BGcTGpNiCcDVEtpAwuYsxNjuTmqHjnOF5ALTbnOFdWqg7%2B0%2B6aqSqE%2BjtZnV%2BvUjYkV1Ci9ZtoXPY%2BZo1IUCEHz%2Be0gF25WVMidKJXZ3dsOZaj3tsFrK3UA2VhbuDcGTj%2BiAAC%2BF8o5ohQorZ6l%2BS6OhSJzPgmyUwOogRP9c%2Fxw%2BgmTuHxwYhS2lHM2GO7H6UEpcjOt9Yyo9H23JsepGzKL1kEy2B6c1GSkyLJ0FN%2BrTQR5dBcF03uo7poNdmO1BdbxlGILWijchwpBYYlBw0XgbgCMbGLKTTORonfvJMpC6kCELuBwVjeKxoxTSNefmX5uTKqEY2pGdY0eh7O3ClpielnpNSKJxsYlowq2lx2yoH0cPeeD%2FmcgiCxpkMdaaWFGekGrb4TVqOBN7uWQbDg3nrxyZRu5RYtEt99lKIa%2BUpIq7FjDcsC6IuRMzIrJF1P%2FlwKCDqmIw5AZtIzmIluIEvfQAIG9vspZHosjlZZcM5Dop2z5eWhrXT%2FuzBJAS%2BvcZmeQH6Sz7vAA%2BUZktte1XY9C18s%2FqukzIhjFz1LMPChhr0GOqUBtaSpzBP9OBr3rwfALdpUjeceogujD5vZFclmX87xUsQ8VN9tXCX1dyC5zC5z5UWJc6pLNxDVr%2FC041fOy1eLG3xAD54UpYhhu2Z7%2FenZR8r7UvOTTmVnnwX7yjLoDzEX91XORQsGW%2B7BZ5UDU3CLhObCEIHMjXzzE0mCdrVK9H%2FLvH82IXn5eNQu04iUfK2u8Ah422wr0mumheku8S8CEgwt6D8%2B&X-Amz-Signature=08ec77aa24b6372fc5adcbc76b788cb3e0f13716979ba2ea1b6d8ad94f733155&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KVTPBH4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCID8m9KlY%2FoyrI032bn91aRPd5z1NBSH9J%2B6i0D0hzI%2BVAiEA9Te2DSQCX04F71yDjvJSnJxZly9uNV0iqeCoufJD5%2FIq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBYi4%2BmXev3WJrIPnyrcAx2ALAXZCd5e%2BNo9fw8i2oQ6hC%2FgxBr97p0OkN2cwVIcP8HYxzXIJRT%2BDaNSWemD2Tvc0NyBLBJa%2FhQjio%2BGcTGpNiCcDVEtpAwuYsxNjuTmqHjnOF5ALTbnOFdWqg7%2B0%2B6aqSqE%2BjtZnV%2BvUjYkV1Ci9ZtoXPY%2BZo1IUCEHz%2Be0gF25WVMidKJXZ3dsOZaj3tsFrK3UA2VhbuDcGTj%2BiAAC%2BF8o5ohQorZ6l%2BS6OhSJzPgmyUwOogRP9c%2Fxw%2BgmTuHxwYhS2lHM2GO7H6UEpcjOt9Yyo9H23JsepGzKL1kEy2B6c1GSkyLJ0FN%2BrTQR5dBcF03uo7poNdmO1BdbxlGILWijchwpBYYlBw0XgbgCMbGLKTTORonfvJMpC6kCELuBwVjeKxoxTSNefmX5uTKqEY2pGdY0eh7O3ClpielnpNSKJxsYlowq2lx2yoH0cPeeD%2FmcgiCxpkMdaaWFGekGrb4TVqOBN7uWQbDg3nrxyZRu5RYtEt99lKIa%2BUpIq7FjDcsC6IuRMzIrJF1P%2FlwKCDqmIw5AZtIzmIluIEvfQAIG9vspZHosjlZZcM5Dop2z5eWhrXT%2FuzBJAS%2BvcZmeQH6Sz7vAA%2BUZktte1XY9C18s%2FqukzIhjFz1LMPChhr0GOqUBtaSpzBP9OBr3rwfALdpUjeceogujD5vZFclmX87xUsQ8VN9tXCX1dyC5zC5z5UWJc6pLNxDVr%2FC041fOy1eLG3xAD54UpYhhu2Z7%2FenZR8r7UvOTTmVnnwX7yjLoDzEX91XORQsGW%2B7BZ5UDU3CLhObCEIHMjXzzE0mCdrVK9H%2FLvH82IXn5eNQu04iUfK2u8Ah422wr0mumheku8S8CEgwt6D8%2B&X-Amz-Signature=a860f7edfd9bca619d168bdb849c51cc6307ac3f12c467b7754c775065745f67&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HFZ6WYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIEx8XziZRQCZ500MXk7C0cZZp8UxmxbxE%2BPhpikj7X1cAiEAskYepsmBemgb3Lg0M5CQOgMQKCVziUXQcbR%2B5WnFT8Iq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDMjErdexK1y1JwUu4CrcAyc4%2FzLjfzthuar9XN3rvSo1el7btHNdUfkZeHIr%2BMpIpwqhxQeihOSaWTQnk6eLlfYaxbzY0gzoGm1qFWexCni81ZXdAoT9rjJRsjuSis96PqCeclGREXcBOFCEVdaL0UISYJ%2FN9WFkQfM3%2Fl1%2Fr%2FrqSx%2FsaPc9ddz8ItG%2FaiLqX6NGmdqtMOxf%2F6KJdwxC1%2B1bvpauezZb2PKjr1%2B%2BHEDx10reLeAuie82RA4krE%2FdzOCb1xjUEt7VpxjzI%2FxXrsOKiFHIkKCdexCW1PnUTiUneci2Ep9N4ed5wVyiw4TWpnzhz0lfxElG7f0sgdoTSqA6ZEB93ZYmN4hnocRjcJxbAErreasYMz%2F8t%2FEQ1hrDt%2BzAnuzz1VpCi%2B6vppjMrcZln7keCHz6oiBEPy1jlJsPfLKjtC1LCP3%2Fnq5%2BwJyTnGqJ8wUAL%2Ff9UrjrV%2BVsbZuOvupJw6cGwq2Nk4sjdIbPA5Wpd18JhVEvWPWKBEjuxriy6rGrf7HBA4toqtcRAaTnyTH1PcIIrLJbaQdxC8pgVNYrCQKIdHQORxhyEB%2FHWE0ccU6fRA7Pe6o%2FR0qCUhchucgJj26shFCL0%2F5MLWi8MOufNJyttTxKRnOa2JnCj7C5seKQVq%2FYqNDnMMihhr0GOqUBc7ydPvgGG%2FksU92U%2BCn%2B91tF0wDKF3L2nsfvtnbarxwS90b4bw76avtu9742g%2F7sa1%2FTG14dgilvyuhANIqbXOLURx6BG9fgMlBwQ7S7vEj9VLKFLSCiv9njmY1VAEPSZwP%2FtjaafopJESUVSYLhgCUMgfTKirCjTA0YmB4AN2WNX1J1SNle%2Bkc5TDMo7gmOvSrBBirN5fMKif8ZE2zPBpCsIoDh&X-Amz-Signature=9b1162cc84bac454058698cc764f80a9cb9947548124013e798b8ac052d12e94&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HFZ6WYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIEx8XziZRQCZ500MXk7C0cZZp8UxmxbxE%2BPhpikj7X1cAiEAskYepsmBemgb3Lg0M5CQOgMQKCVziUXQcbR%2B5WnFT8Iq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDMjErdexK1y1JwUu4CrcAyc4%2FzLjfzthuar9XN3rvSo1el7btHNdUfkZeHIr%2BMpIpwqhxQeihOSaWTQnk6eLlfYaxbzY0gzoGm1qFWexCni81ZXdAoT9rjJRsjuSis96PqCeclGREXcBOFCEVdaL0UISYJ%2FN9WFkQfM3%2Fl1%2Fr%2FrqSx%2FsaPc9ddz8ItG%2FaiLqX6NGmdqtMOxf%2F6KJdwxC1%2B1bvpauezZb2PKjr1%2B%2BHEDx10reLeAuie82RA4krE%2FdzOCb1xjUEt7VpxjzI%2FxXrsOKiFHIkKCdexCW1PnUTiUneci2Ep9N4ed5wVyiw4TWpnzhz0lfxElG7f0sgdoTSqA6ZEB93ZYmN4hnocRjcJxbAErreasYMz%2F8t%2FEQ1hrDt%2BzAnuzz1VpCi%2B6vppjMrcZln7keCHz6oiBEPy1jlJsPfLKjtC1LCP3%2Fnq5%2BwJyTnGqJ8wUAL%2Ff9UrjrV%2BVsbZuOvupJw6cGwq2Nk4sjdIbPA5Wpd18JhVEvWPWKBEjuxriy6rGrf7HBA4toqtcRAaTnyTH1PcIIrLJbaQdxC8pgVNYrCQKIdHQORxhyEB%2FHWE0ccU6fRA7Pe6o%2FR0qCUhchucgJj26shFCL0%2F5MLWi8MOufNJyttTxKRnOa2JnCj7C5seKQVq%2FYqNDnMMihhr0GOqUBc7ydPvgGG%2FksU92U%2BCn%2B91tF0wDKF3L2nsfvtnbarxwS90b4bw76avtu9742g%2F7sa1%2FTG14dgilvyuhANIqbXOLURx6BG9fgMlBwQ7S7vEj9VLKFLSCiv9njmY1VAEPSZwP%2FtjaafopJESUVSYLhgCUMgfTKirCjTA0YmB4AN2WNX1J1SNle%2Bkc5TDMo7gmOvSrBBirN5fMKif8ZE2zPBpCsIoDh&X-Amz-Signature=dc078e4a7b5025fdef7944e73437e006481fcbe79e1ea8eccdf322f5cb6b62dc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HFZ6WYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIEx8XziZRQCZ500MXk7C0cZZp8UxmxbxE%2BPhpikj7X1cAiEAskYepsmBemgb3Lg0M5CQOgMQKCVziUXQcbR%2B5WnFT8Iq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDMjErdexK1y1JwUu4CrcAyc4%2FzLjfzthuar9XN3rvSo1el7btHNdUfkZeHIr%2BMpIpwqhxQeihOSaWTQnk6eLlfYaxbzY0gzoGm1qFWexCni81ZXdAoT9rjJRsjuSis96PqCeclGREXcBOFCEVdaL0UISYJ%2FN9WFkQfM3%2Fl1%2Fr%2FrqSx%2FsaPc9ddz8ItG%2FaiLqX6NGmdqtMOxf%2F6KJdwxC1%2B1bvpauezZb2PKjr1%2B%2BHEDx10reLeAuie82RA4krE%2FdzOCb1xjUEt7VpxjzI%2FxXrsOKiFHIkKCdexCW1PnUTiUneci2Ep9N4ed5wVyiw4TWpnzhz0lfxElG7f0sgdoTSqA6ZEB93ZYmN4hnocRjcJxbAErreasYMz%2F8t%2FEQ1hrDt%2BzAnuzz1VpCi%2B6vppjMrcZln7keCHz6oiBEPy1jlJsPfLKjtC1LCP3%2Fnq5%2BwJyTnGqJ8wUAL%2Ff9UrjrV%2BVsbZuOvupJw6cGwq2Nk4sjdIbPA5Wpd18JhVEvWPWKBEjuxriy6rGrf7HBA4toqtcRAaTnyTH1PcIIrLJbaQdxC8pgVNYrCQKIdHQORxhyEB%2FHWE0ccU6fRA7Pe6o%2FR0qCUhchucgJj26shFCL0%2F5MLWi8MOufNJyttTxKRnOa2JnCj7C5seKQVq%2FYqNDnMMihhr0GOqUBc7ydPvgGG%2FksU92U%2BCn%2B91tF0wDKF3L2nsfvtnbarxwS90b4bw76avtu9742g%2F7sa1%2FTG14dgilvyuhANIqbXOLURx6BG9fgMlBwQ7S7vEj9VLKFLSCiv9njmY1VAEPSZwP%2FtjaafopJESUVSYLhgCUMgfTKirCjTA0YmB4AN2WNX1J1SNle%2Bkc5TDMo7gmOvSrBBirN5fMKif8ZE2zPBpCsIoDh&X-Amz-Signature=eb074343bc2b215f7dc2a29df51cc1075acdd4de47e6bf4022cd6e73b139ca90&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HFZ6WYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIEx8XziZRQCZ500MXk7C0cZZp8UxmxbxE%2BPhpikj7X1cAiEAskYepsmBemgb3Lg0M5CQOgMQKCVziUXQcbR%2B5WnFT8Iq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDMjErdexK1y1JwUu4CrcAyc4%2FzLjfzthuar9XN3rvSo1el7btHNdUfkZeHIr%2BMpIpwqhxQeihOSaWTQnk6eLlfYaxbzY0gzoGm1qFWexCni81ZXdAoT9rjJRsjuSis96PqCeclGREXcBOFCEVdaL0UISYJ%2FN9WFkQfM3%2Fl1%2Fr%2FrqSx%2FsaPc9ddz8ItG%2FaiLqX6NGmdqtMOxf%2F6KJdwxC1%2B1bvpauezZb2PKjr1%2B%2BHEDx10reLeAuie82RA4krE%2FdzOCb1xjUEt7VpxjzI%2FxXrsOKiFHIkKCdexCW1PnUTiUneci2Ep9N4ed5wVyiw4TWpnzhz0lfxElG7f0sgdoTSqA6ZEB93ZYmN4hnocRjcJxbAErreasYMz%2F8t%2FEQ1hrDt%2BzAnuzz1VpCi%2B6vppjMrcZln7keCHz6oiBEPy1jlJsPfLKjtC1LCP3%2Fnq5%2BwJyTnGqJ8wUAL%2Ff9UrjrV%2BVsbZuOvupJw6cGwq2Nk4sjdIbPA5Wpd18JhVEvWPWKBEjuxriy6rGrf7HBA4toqtcRAaTnyTH1PcIIrLJbaQdxC8pgVNYrCQKIdHQORxhyEB%2FHWE0ccU6fRA7Pe6o%2FR0qCUhchucgJj26shFCL0%2F5MLWi8MOufNJyttTxKRnOa2JnCj7C5seKQVq%2FYqNDnMMihhr0GOqUBc7ydPvgGG%2FksU92U%2BCn%2B91tF0wDKF3L2nsfvtnbarxwS90b4bw76avtu9742g%2F7sa1%2FTG14dgilvyuhANIqbXOLURx6BG9fgMlBwQ7S7vEj9VLKFLSCiv9njmY1VAEPSZwP%2FtjaafopJESUVSYLhgCUMgfTKirCjTA0YmB4AN2WNX1J1SNle%2Bkc5TDMo7gmOvSrBBirN5fMKif8ZE2zPBpCsIoDh&X-Amz-Signature=c6ff9d2aeadc914e3f0fb5cdacf23e409dcd15e2455d3f9912ccf9d002eb319d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HFZ6WYR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIEx8XziZRQCZ500MXk7C0cZZp8UxmxbxE%2BPhpikj7X1cAiEAskYepsmBemgb3Lg0M5CQOgMQKCVziUXQcbR%2B5WnFT8Iq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDMjErdexK1y1JwUu4CrcAyc4%2FzLjfzthuar9XN3rvSo1el7btHNdUfkZeHIr%2BMpIpwqhxQeihOSaWTQnk6eLlfYaxbzY0gzoGm1qFWexCni81ZXdAoT9rjJRsjuSis96PqCeclGREXcBOFCEVdaL0UISYJ%2FN9WFkQfM3%2Fl1%2Fr%2FrqSx%2FsaPc9ddz8ItG%2FaiLqX6NGmdqtMOxf%2F6KJdwxC1%2B1bvpauezZb2PKjr1%2B%2BHEDx10reLeAuie82RA4krE%2FdzOCb1xjUEt7VpxjzI%2FxXrsOKiFHIkKCdexCW1PnUTiUneci2Ep9N4ed5wVyiw4TWpnzhz0lfxElG7f0sgdoTSqA6ZEB93ZYmN4hnocRjcJxbAErreasYMz%2F8t%2FEQ1hrDt%2BzAnuzz1VpCi%2B6vppjMrcZln7keCHz6oiBEPy1jlJsPfLKjtC1LCP3%2Fnq5%2BwJyTnGqJ8wUAL%2Ff9UrjrV%2BVsbZuOvupJw6cGwq2Nk4sjdIbPA5Wpd18JhVEvWPWKBEjuxriy6rGrf7HBA4toqtcRAaTnyTH1PcIIrLJbaQdxC8pgVNYrCQKIdHQORxhyEB%2FHWE0ccU6fRA7Pe6o%2FR0qCUhchucgJj26shFCL0%2F5MLWi8MOufNJyttTxKRnOa2JnCj7C5seKQVq%2FYqNDnMMihhr0GOqUBc7ydPvgGG%2FksU92U%2BCn%2B91tF0wDKF3L2nsfvtnbarxwS90b4bw76avtu9742g%2F7sa1%2FTG14dgilvyuhANIqbXOLURx6BG9fgMlBwQ7S7vEj9VLKFLSCiv9njmY1VAEPSZwP%2FtjaafopJESUVSYLhgCUMgfTKirCjTA0YmB4AN2WNX1J1SNle%2Bkc5TDMo7gmOvSrBBirN5fMKif8ZE2zPBpCsIoDh&X-Amz-Signature=6221218145503090467678ac2c4ef817b7b46a38c950458fe37c3098d1859ccf&X-Amz-SignedHeaders=host&x-id=GetObject)
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


