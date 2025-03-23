

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GX2KORW%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCjZuCVgemtGa2eLSIYtigEOUqbul3ueFlTjfBty%2Fh7MAIgMijAv2bIsJohwyfNtFrf%2BmnKYtNg0TaKxibmpCQS3ywqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJAAPpXhmW%2FwcUe0ircA8Ku2di%2FGLCrmbNF8f6skNIhcsuOu909OvJXRivP%2FgOV2SZ7y%2BoqS8nqQQsgmUza8lOfoTnfGLVR%2FzzHif%2BPuYgdeZKgSWRx6ZiOTKCPClDG1q%2FrBtry5zNn6WDoSWNlmC7%2BTcHAVuaPl1GWzpC9gccYgbNbPvVIcb%2BR2y5EneFc72Ea0VI62FGaZlUPPbaKYvUtMhWoBbVMb36A3qJn7X6vchgM9eRaOaMjG2BVr3kH%2BYe8CA8o4lKEnA4TFxCTkQj78nfXd3nRYw597TJVxtP%2BwccFsboBZ4LhMo%2FyxC19igOz6skfCKjrk2wd5xhfQjVTqYWZINiRZ1C7HyN%2B7sTsU6JRl%2FhEuPn5p7UNxvX%2F0vbSQyW4ZD2qw%2B2aSnbmGdZjJan6Hr%2FOmZag0oe2hDKMJinbRJOVYX%2BO24F6hvAozDcWK0rT6Kl0DE5k1VqJ5Uw7W6HXuKs4D0TohJVpZQwRx265q57myLfKlENE9IUZdoQAJpWRgx%2F8YDspEGINPaJ80FiZF3eV8i4M%2Bg54j%2F%2BN295ykKRcv0ftm%2BM5vHMBf9onbengZb8LWyq1pUyQ1%2FpaM6gL4umKnVxL3x%2F5n1nF%2FU7hZ9TR21rga3epFpMV7p4sPx%2Bnt8aXIrxUMOK1%2FL4GOqUBNDCwC3eCpLk1knPlURpXMr9cdGABmwFKCwBzpysWD4BwkYcfhAytn%2FAbe5gG5tX%2BHwwJ7h3CkGLMv%2B1GlJS6wQn9Lck04RAWbRSRo0zT1XUGKwGOz1LuTaW%2BMygUQf8lwiFPqZOfWGQAdAUTMVZ3Jh1YascdQMEubL004VWFxZS5RW8V3pMNifxvrOo%2BRlUSBcAdjOZNFH8ufKpo4%2FNcP7auEemx&X-Amz-Signature=1866cafbb2bf699e99745ac9e99a46e0ac252e81d7d22f1b50471f2a43076d96&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y6OZWK4%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIQCIhCFkW1%2BUDXgOAto9XoTaj%2BULVDaJEc9ZeCEer3JbjwIgX8UQaMTAhBxYJiOx8%2Fs8lnJIg%2BEQ7FDTsAdFCpi6Ui4qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDAANKWglLOUEr5e9CrcA%2Fhm1xjH3TF1B4IH8BH%2BbAOjRJ2NuvoQxYzWtMt%2FvdVQxBKGOlB9LQQdqVo1KDSIUHVaxlzdiMWlPWGfL%2BAEn6WDAfvrCRYwkmouzfagMVn6CwfNTSdVKl%2B6ciEV9lyJUnIp%2B2jCYuhv7TF%2Fk76UF3%2Fucv6pVZI2LNaUO8nPOKPcvKSqL7qBkkQ%2F1HH8O80WCt9QcDPbPx4giY5QZo8vVA5aTHBG45CrUhAZjhMWiX6ZrxykQuieoTYItDtInYhwNq6fIluhGaBRFVGf4UC%2BDkohDaQUwseCfBxe3EmZAkT5KZN4xASqKZl7picpOJKCTxdS14IQCh1gC%2FYAIh%2BYVcpedzLw3fxUmFHnL6HPhhUcqrZ9ww5wDCPYF3bj%2FaLclPVVwN5IQN4OqVqwnOQykiOv%2FtZ9MTZKM1bQr%2BI3JunPrFNup%2FGAyBwZ%2BGc1RzBVh2vvsty4Bu0bREoQbDygUVbtaa7I5%2BeFJbg0v7mVCWocuHhFY0hDzesCCOilZFZvhk%2F2tQqQCBieaDGz6yuq0%2Fq8cU43n6USKaCkJK7eyvHNrpjnGsBEneT3A%2Bq0T2Ottaipd1fCrfk%2Fmg%2B9Pfh0z0WxtenjGoDuXfUgQBfO%2Fdl%2FVVtR7qiS8f%2BC9hPHMJu2%2FL4GOqUBtMY4pAc%2Byg8VAXZILmukZw8jAbiJhQgwi3BzvMSh0UCmYjw1dMdErv248ipsclQc8Vr5kj4Bhi2ebzQ0gwAnpeFdREHvf%2FBNlPk0Ob09W9CTFanVYRQmdmim9uQCGjRRjuzzrwo9%2BFb%2Bk9pbHDzun%2Bwgz1aq5UY5krSbRwcPlAKP2uvXrQhNPKH%2Fn9KuaYyxRwJ3LI0odaiqVG7L1M3LdB6kC64n&X-Amz-Signature=65c6ef130ab3aa14de81d2a300f6ffb27d8a7c10a5f8afc8167d404473f877b3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y6OZWK4%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIQCIhCFkW1%2BUDXgOAto9XoTaj%2BULVDaJEc9ZeCEer3JbjwIgX8UQaMTAhBxYJiOx8%2Fs8lnJIg%2BEQ7FDTsAdFCpi6Ui4qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDAANKWglLOUEr5e9CrcA%2Fhm1xjH3TF1B4IH8BH%2BbAOjRJ2NuvoQxYzWtMt%2FvdVQxBKGOlB9LQQdqVo1KDSIUHVaxlzdiMWlPWGfL%2BAEn6WDAfvrCRYwkmouzfagMVn6CwfNTSdVKl%2B6ciEV9lyJUnIp%2B2jCYuhv7TF%2Fk76UF3%2Fucv6pVZI2LNaUO8nPOKPcvKSqL7qBkkQ%2F1HH8O80WCt9QcDPbPx4giY5QZo8vVA5aTHBG45CrUhAZjhMWiX6ZrxykQuieoTYItDtInYhwNq6fIluhGaBRFVGf4UC%2BDkohDaQUwseCfBxe3EmZAkT5KZN4xASqKZl7picpOJKCTxdS14IQCh1gC%2FYAIh%2BYVcpedzLw3fxUmFHnL6HPhhUcqrZ9ww5wDCPYF3bj%2FaLclPVVwN5IQN4OqVqwnOQykiOv%2FtZ9MTZKM1bQr%2BI3JunPrFNup%2FGAyBwZ%2BGc1RzBVh2vvsty4Bu0bREoQbDygUVbtaa7I5%2BeFJbg0v7mVCWocuHhFY0hDzesCCOilZFZvhk%2F2tQqQCBieaDGz6yuq0%2Fq8cU43n6USKaCkJK7eyvHNrpjnGsBEneT3A%2Bq0T2Ottaipd1fCrfk%2Fmg%2B9Pfh0z0WxtenjGoDuXfUgQBfO%2Fdl%2FVVtR7qiS8f%2BC9hPHMJu2%2FL4GOqUBtMY4pAc%2Byg8VAXZILmukZw8jAbiJhQgwi3BzvMSh0UCmYjw1dMdErv248ipsclQc8Vr5kj4Bhi2ebzQ0gwAnpeFdREHvf%2FBNlPk0Ob09W9CTFanVYRQmdmim9uQCGjRRjuzzrwo9%2BFb%2Bk9pbHDzun%2Bwgz1aq5UY5krSbRwcPlAKP2uvXrQhNPKH%2Fn9KuaYyxRwJ3LI0odaiqVG7L1M3LdB6kC64n&X-Amz-Signature=4ea18c564c2d569139a9d49420411b38e2caa03ad634cdc94db076e696f8f27a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y6OZWK4%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIQCIhCFkW1%2BUDXgOAto9XoTaj%2BULVDaJEc9ZeCEer3JbjwIgX8UQaMTAhBxYJiOx8%2Fs8lnJIg%2BEQ7FDTsAdFCpi6Ui4qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDAANKWglLOUEr5e9CrcA%2Fhm1xjH3TF1B4IH8BH%2BbAOjRJ2NuvoQxYzWtMt%2FvdVQxBKGOlB9LQQdqVo1KDSIUHVaxlzdiMWlPWGfL%2BAEn6WDAfvrCRYwkmouzfagMVn6CwfNTSdVKl%2B6ciEV9lyJUnIp%2B2jCYuhv7TF%2Fk76UF3%2Fucv6pVZI2LNaUO8nPOKPcvKSqL7qBkkQ%2F1HH8O80WCt9QcDPbPx4giY5QZo8vVA5aTHBG45CrUhAZjhMWiX6ZrxykQuieoTYItDtInYhwNq6fIluhGaBRFVGf4UC%2BDkohDaQUwseCfBxe3EmZAkT5KZN4xASqKZl7picpOJKCTxdS14IQCh1gC%2FYAIh%2BYVcpedzLw3fxUmFHnL6HPhhUcqrZ9ww5wDCPYF3bj%2FaLclPVVwN5IQN4OqVqwnOQykiOv%2FtZ9MTZKM1bQr%2BI3JunPrFNup%2FGAyBwZ%2BGc1RzBVh2vvsty4Bu0bREoQbDygUVbtaa7I5%2BeFJbg0v7mVCWocuHhFY0hDzesCCOilZFZvhk%2F2tQqQCBieaDGz6yuq0%2Fq8cU43n6USKaCkJK7eyvHNrpjnGsBEneT3A%2Bq0T2Ottaipd1fCrfk%2Fmg%2B9Pfh0z0WxtenjGoDuXfUgQBfO%2Fdl%2FVVtR7qiS8f%2BC9hPHMJu2%2FL4GOqUBtMY4pAc%2Byg8VAXZILmukZw8jAbiJhQgwi3BzvMSh0UCmYjw1dMdErv248ipsclQc8Vr5kj4Bhi2ebzQ0gwAnpeFdREHvf%2FBNlPk0Ob09W9CTFanVYRQmdmim9uQCGjRRjuzzrwo9%2BFb%2Bk9pbHDzun%2Bwgz1aq5UY5krSbRwcPlAKP2uvXrQhNPKH%2Fn9KuaYyxRwJ3LI0odaiqVG7L1M3LdB6kC64n&X-Amz-Signature=45b1ebe4a6b4fd2ec4950ee8c646e5295adc71ca00bf01762b244245e29e6c70&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y6OZWK4%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIQCIhCFkW1%2BUDXgOAto9XoTaj%2BULVDaJEc9ZeCEer3JbjwIgX8UQaMTAhBxYJiOx8%2Fs8lnJIg%2BEQ7FDTsAdFCpi6Ui4qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDAANKWglLOUEr5e9CrcA%2Fhm1xjH3TF1B4IH8BH%2BbAOjRJ2NuvoQxYzWtMt%2FvdVQxBKGOlB9LQQdqVo1KDSIUHVaxlzdiMWlPWGfL%2BAEn6WDAfvrCRYwkmouzfagMVn6CwfNTSdVKl%2B6ciEV9lyJUnIp%2B2jCYuhv7TF%2Fk76UF3%2Fucv6pVZI2LNaUO8nPOKPcvKSqL7qBkkQ%2F1HH8O80WCt9QcDPbPx4giY5QZo8vVA5aTHBG45CrUhAZjhMWiX6ZrxykQuieoTYItDtInYhwNq6fIluhGaBRFVGf4UC%2BDkohDaQUwseCfBxe3EmZAkT5KZN4xASqKZl7picpOJKCTxdS14IQCh1gC%2FYAIh%2BYVcpedzLw3fxUmFHnL6HPhhUcqrZ9ww5wDCPYF3bj%2FaLclPVVwN5IQN4OqVqwnOQykiOv%2FtZ9MTZKM1bQr%2BI3JunPrFNup%2FGAyBwZ%2BGc1RzBVh2vvsty4Bu0bREoQbDygUVbtaa7I5%2BeFJbg0v7mVCWocuHhFY0hDzesCCOilZFZvhk%2F2tQqQCBieaDGz6yuq0%2Fq8cU43n6USKaCkJK7eyvHNrpjnGsBEneT3A%2Bq0T2Ottaipd1fCrfk%2Fmg%2B9Pfh0z0WxtenjGoDuXfUgQBfO%2Fdl%2FVVtR7qiS8f%2BC9hPHMJu2%2FL4GOqUBtMY4pAc%2Byg8VAXZILmukZw8jAbiJhQgwi3BzvMSh0UCmYjw1dMdErv248ipsclQc8Vr5kj4Bhi2ebzQ0gwAnpeFdREHvf%2FBNlPk0Ob09W9CTFanVYRQmdmim9uQCGjRRjuzzrwo9%2BFb%2Bk9pbHDzun%2Bwgz1aq5UY5krSbRwcPlAKP2uvXrQhNPKH%2Fn9KuaYyxRwJ3LI0odaiqVG7L1M3LdB6kC64n&X-Amz-Signature=c8360038368e7087d712427d2b0f588630ac1371cf45c46b5e635a074f04ead7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y6OZWK4%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIQCIhCFkW1%2BUDXgOAto9XoTaj%2BULVDaJEc9ZeCEer3JbjwIgX8UQaMTAhBxYJiOx8%2Fs8lnJIg%2BEQ7FDTsAdFCpi6Ui4qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDAANKWglLOUEr5e9CrcA%2Fhm1xjH3TF1B4IH8BH%2BbAOjRJ2NuvoQxYzWtMt%2FvdVQxBKGOlB9LQQdqVo1KDSIUHVaxlzdiMWlPWGfL%2BAEn6WDAfvrCRYwkmouzfagMVn6CwfNTSdVKl%2B6ciEV9lyJUnIp%2B2jCYuhv7TF%2Fk76UF3%2Fucv6pVZI2LNaUO8nPOKPcvKSqL7qBkkQ%2F1HH8O80WCt9QcDPbPx4giY5QZo8vVA5aTHBG45CrUhAZjhMWiX6ZrxykQuieoTYItDtInYhwNq6fIluhGaBRFVGf4UC%2BDkohDaQUwseCfBxe3EmZAkT5KZN4xASqKZl7picpOJKCTxdS14IQCh1gC%2FYAIh%2BYVcpedzLw3fxUmFHnL6HPhhUcqrZ9ww5wDCPYF3bj%2FaLclPVVwN5IQN4OqVqwnOQykiOv%2FtZ9MTZKM1bQr%2BI3JunPrFNup%2FGAyBwZ%2BGc1RzBVh2vvsty4Bu0bREoQbDygUVbtaa7I5%2BeFJbg0v7mVCWocuHhFY0hDzesCCOilZFZvhk%2F2tQqQCBieaDGz6yuq0%2Fq8cU43n6USKaCkJK7eyvHNrpjnGsBEneT3A%2Bq0T2Ottaipd1fCrfk%2Fmg%2B9Pfh0z0WxtenjGoDuXfUgQBfO%2Fdl%2FVVtR7qiS8f%2BC9hPHMJu2%2FL4GOqUBtMY4pAc%2Byg8VAXZILmukZw8jAbiJhQgwi3BzvMSh0UCmYjw1dMdErv248ipsclQc8Vr5kj4Bhi2ebzQ0gwAnpeFdREHvf%2FBNlPk0Ob09W9CTFanVYRQmdmim9uQCGjRRjuzzrwo9%2BFb%2Bk9pbHDzun%2Bwgz1aq5UY5krSbRwcPlAKP2uvXrQhNPKH%2Fn9KuaYyxRwJ3LI0odaiqVG7L1M3LdB6kC64n&X-Amz-Signature=4089f4a715431875f344767c6a5fa768e4c51ec3cd81f502b54a341564761774&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GX2KORW%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCjZuCVgemtGa2eLSIYtigEOUqbul3ueFlTjfBty%2Fh7MAIgMijAv2bIsJohwyfNtFrf%2BmnKYtNg0TaKxibmpCQS3ywqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJAAPpXhmW%2FwcUe0ircA8Ku2di%2FGLCrmbNF8f6skNIhcsuOu909OvJXRivP%2FgOV2SZ7y%2BoqS8nqQQsgmUza8lOfoTnfGLVR%2FzzHif%2BPuYgdeZKgSWRx6ZiOTKCPClDG1q%2FrBtry5zNn6WDoSWNlmC7%2BTcHAVuaPl1GWzpC9gccYgbNbPvVIcb%2BR2y5EneFc72Ea0VI62FGaZlUPPbaKYvUtMhWoBbVMb36A3qJn7X6vchgM9eRaOaMjG2BVr3kH%2BYe8CA8o4lKEnA4TFxCTkQj78nfXd3nRYw597TJVxtP%2BwccFsboBZ4LhMo%2FyxC19igOz6skfCKjrk2wd5xhfQjVTqYWZINiRZ1C7HyN%2B7sTsU6JRl%2FhEuPn5p7UNxvX%2F0vbSQyW4ZD2qw%2B2aSnbmGdZjJan6Hr%2FOmZag0oe2hDKMJinbRJOVYX%2BO24F6hvAozDcWK0rT6Kl0DE5k1VqJ5Uw7W6HXuKs4D0TohJVpZQwRx265q57myLfKlENE9IUZdoQAJpWRgx%2F8YDspEGINPaJ80FiZF3eV8i4M%2Bg54j%2F%2BN295ykKRcv0ftm%2BM5vHMBf9onbengZb8LWyq1pUyQ1%2FpaM6gL4umKnVxL3x%2F5n1nF%2FU7hZ9TR21rga3epFpMV7p4sPx%2Bnt8aXIrxUMOK1%2FL4GOqUBNDCwC3eCpLk1knPlURpXMr9cdGABmwFKCwBzpysWD4BwkYcfhAytn%2FAbe5gG5tX%2BHwwJ7h3CkGLMv%2B1GlJS6wQn9Lck04RAWbRSRo0zT1XUGKwGOz1LuTaW%2BMygUQf8lwiFPqZOfWGQAdAUTMVZ3Jh1YascdQMEubL004VWFxZS5RW8V3pMNifxvrOo%2BRlUSBcAdjOZNFH8ufKpo4%2FNcP7auEemx&X-Amz-Signature=18447863d0d31f226ee55ec4fa2784b721465159488be16c5e962fef72ebfbdf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GX2KORW%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCjZuCVgemtGa2eLSIYtigEOUqbul3ueFlTjfBty%2Fh7MAIgMijAv2bIsJohwyfNtFrf%2BmnKYtNg0TaKxibmpCQS3ywqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJAAPpXhmW%2FwcUe0ircA8Ku2di%2FGLCrmbNF8f6skNIhcsuOu909OvJXRivP%2FgOV2SZ7y%2BoqS8nqQQsgmUza8lOfoTnfGLVR%2FzzHif%2BPuYgdeZKgSWRx6ZiOTKCPClDG1q%2FrBtry5zNn6WDoSWNlmC7%2BTcHAVuaPl1GWzpC9gccYgbNbPvVIcb%2BR2y5EneFc72Ea0VI62FGaZlUPPbaKYvUtMhWoBbVMb36A3qJn7X6vchgM9eRaOaMjG2BVr3kH%2BYe8CA8o4lKEnA4TFxCTkQj78nfXd3nRYw597TJVxtP%2BwccFsboBZ4LhMo%2FyxC19igOz6skfCKjrk2wd5xhfQjVTqYWZINiRZ1C7HyN%2B7sTsU6JRl%2FhEuPn5p7UNxvX%2F0vbSQyW4ZD2qw%2B2aSnbmGdZjJan6Hr%2FOmZag0oe2hDKMJinbRJOVYX%2BO24F6hvAozDcWK0rT6Kl0DE5k1VqJ5Uw7W6HXuKs4D0TohJVpZQwRx265q57myLfKlENE9IUZdoQAJpWRgx%2F8YDspEGINPaJ80FiZF3eV8i4M%2Bg54j%2F%2BN295ykKRcv0ftm%2BM5vHMBf9onbengZb8LWyq1pUyQ1%2FpaM6gL4umKnVxL3x%2F5n1nF%2FU7hZ9TR21rga3epFpMV7p4sPx%2Bnt8aXIrxUMOK1%2FL4GOqUBNDCwC3eCpLk1knPlURpXMr9cdGABmwFKCwBzpysWD4BwkYcfhAytn%2FAbe5gG5tX%2BHwwJ7h3CkGLMv%2B1GlJS6wQn9Lck04RAWbRSRo0zT1XUGKwGOz1LuTaW%2BMygUQf8lwiFPqZOfWGQAdAUTMVZ3Jh1YascdQMEubL004VWFxZS5RW8V3pMNifxvrOo%2BRlUSBcAdjOZNFH8ufKpo4%2FNcP7auEemx&X-Amz-Signature=d40041d121971c91310dae86b6d3901e32689b7d870cb0741db38e5a2401db9e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GX2KORW%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCjZuCVgemtGa2eLSIYtigEOUqbul3ueFlTjfBty%2Fh7MAIgMijAv2bIsJohwyfNtFrf%2BmnKYtNg0TaKxibmpCQS3ywqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJAAPpXhmW%2FwcUe0ircA8Ku2di%2FGLCrmbNF8f6skNIhcsuOu909OvJXRivP%2FgOV2SZ7y%2BoqS8nqQQsgmUza8lOfoTnfGLVR%2FzzHif%2BPuYgdeZKgSWRx6ZiOTKCPClDG1q%2FrBtry5zNn6WDoSWNlmC7%2BTcHAVuaPl1GWzpC9gccYgbNbPvVIcb%2BR2y5EneFc72Ea0VI62FGaZlUPPbaKYvUtMhWoBbVMb36A3qJn7X6vchgM9eRaOaMjG2BVr3kH%2BYe8CA8o4lKEnA4TFxCTkQj78nfXd3nRYw597TJVxtP%2BwccFsboBZ4LhMo%2FyxC19igOz6skfCKjrk2wd5xhfQjVTqYWZINiRZ1C7HyN%2B7sTsU6JRl%2FhEuPn5p7UNxvX%2F0vbSQyW4ZD2qw%2B2aSnbmGdZjJan6Hr%2FOmZag0oe2hDKMJinbRJOVYX%2BO24F6hvAozDcWK0rT6Kl0DE5k1VqJ5Uw7W6HXuKs4D0TohJVpZQwRx265q57myLfKlENE9IUZdoQAJpWRgx%2F8YDspEGINPaJ80FiZF3eV8i4M%2Bg54j%2F%2BN295ykKRcv0ftm%2BM5vHMBf9onbengZb8LWyq1pUyQ1%2FpaM6gL4umKnVxL3x%2F5n1nF%2FU7hZ9TR21rga3epFpMV7p4sPx%2Bnt8aXIrxUMOK1%2FL4GOqUBNDCwC3eCpLk1knPlURpXMr9cdGABmwFKCwBzpysWD4BwkYcfhAytn%2FAbe5gG5tX%2BHwwJ7h3CkGLMv%2B1GlJS6wQn9Lck04RAWbRSRo0zT1XUGKwGOz1LuTaW%2BMygUQf8lwiFPqZOfWGQAdAUTMVZ3Jh1YascdQMEubL004VWFxZS5RW8V3pMNifxvrOo%2BRlUSBcAdjOZNFH8ufKpo4%2FNcP7auEemx&X-Amz-Signature=b0dc9291ddd8b4a7cfbffa742981dedaa474f1a20139cb9903c4eff320f58393&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GX2KORW%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCjZuCVgemtGa2eLSIYtigEOUqbul3ueFlTjfBty%2Fh7MAIgMijAv2bIsJohwyfNtFrf%2BmnKYtNg0TaKxibmpCQS3ywqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJAAPpXhmW%2FwcUe0ircA8Ku2di%2FGLCrmbNF8f6skNIhcsuOu909OvJXRivP%2FgOV2SZ7y%2BoqS8nqQQsgmUza8lOfoTnfGLVR%2FzzHif%2BPuYgdeZKgSWRx6ZiOTKCPClDG1q%2FrBtry5zNn6WDoSWNlmC7%2BTcHAVuaPl1GWzpC9gccYgbNbPvVIcb%2BR2y5EneFc72Ea0VI62FGaZlUPPbaKYvUtMhWoBbVMb36A3qJn7X6vchgM9eRaOaMjG2BVr3kH%2BYe8CA8o4lKEnA4TFxCTkQj78nfXd3nRYw597TJVxtP%2BwccFsboBZ4LhMo%2FyxC19igOz6skfCKjrk2wd5xhfQjVTqYWZINiRZ1C7HyN%2B7sTsU6JRl%2FhEuPn5p7UNxvX%2F0vbSQyW4ZD2qw%2B2aSnbmGdZjJan6Hr%2FOmZag0oe2hDKMJinbRJOVYX%2BO24F6hvAozDcWK0rT6Kl0DE5k1VqJ5Uw7W6HXuKs4D0TohJVpZQwRx265q57myLfKlENE9IUZdoQAJpWRgx%2F8YDspEGINPaJ80FiZF3eV8i4M%2Bg54j%2F%2BN295ykKRcv0ftm%2BM5vHMBf9onbengZb8LWyq1pUyQ1%2FpaM6gL4umKnVxL3x%2F5n1nF%2FU7hZ9TR21rga3epFpMV7p4sPx%2Bnt8aXIrxUMOK1%2FL4GOqUBNDCwC3eCpLk1knPlURpXMr9cdGABmwFKCwBzpysWD4BwkYcfhAytn%2FAbe5gG5tX%2BHwwJ7h3CkGLMv%2B1GlJS6wQn9Lck04RAWbRSRo0zT1XUGKwGOz1LuTaW%2BMygUQf8lwiFPqZOfWGQAdAUTMVZ3Jh1YascdQMEubL004VWFxZS5RW8V3pMNifxvrOo%2BRlUSBcAdjOZNFH8ufKpo4%2FNcP7auEemx&X-Amz-Signature=0a87bde2925865d5be262887528aa220042ab38d208b07772ff881305bfdc615&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GX2KORW%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCjZuCVgemtGa2eLSIYtigEOUqbul3ueFlTjfBty%2Fh7MAIgMijAv2bIsJohwyfNtFrf%2BmnKYtNg0TaKxibmpCQS3ywqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJAAPpXhmW%2FwcUe0ircA8Ku2di%2FGLCrmbNF8f6skNIhcsuOu909OvJXRivP%2FgOV2SZ7y%2BoqS8nqQQsgmUza8lOfoTnfGLVR%2FzzHif%2BPuYgdeZKgSWRx6ZiOTKCPClDG1q%2FrBtry5zNn6WDoSWNlmC7%2BTcHAVuaPl1GWzpC9gccYgbNbPvVIcb%2BR2y5EneFc72Ea0VI62FGaZlUPPbaKYvUtMhWoBbVMb36A3qJn7X6vchgM9eRaOaMjG2BVr3kH%2BYe8CA8o4lKEnA4TFxCTkQj78nfXd3nRYw597TJVxtP%2BwccFsboBZ4LhMo%2FyxC19igOz6skfCKjrk2wd5xhfQjVTqYWZINiRZ1C7HyN%2B7sTsU6JRl%2FhEuPn5p7UNxvX%2F0vbSQyW4ZD2qw%2B2aSnbmGdZjJan6Hr%2FOmZag0oe2hDKMJinbRJOVYX%2BO24F6hvAozDcWK0rT6Kl0DE5k1VqJ5Uw7W6HXuKs4D0TohJVpZQwRx265q57myLfKlENE9IUZdoQAJpWRgx%2F8YDspEGINPaJ80FiZF3eV8i4M%2Bg54j%2F%2BN295ykKRcv0ftm%2BM5vHMBf9onbengZb8LWyq1pUyQ1%2FpaM6gL4umKnVxL3x%2F5n1nF%2FU7hZ9TR21rga3epFpMV7p4sPx%2Bnt8aXIrxUMOK1%2FL4GOqUBNDCwC3eCpLk1knPlURpXMr9cdGABmwFKCwBzpysWD4BwkYcfhAytn%2FAbe5gG5tX%2BHwwJ7h3CkGLMv%2B1GlJS6wQn9Lck04RAWbRSRo0zT1XUGKwGOz1LuTaW%2BMygUQf8lwiFPqZOfWGQAdAUTMVZ3Jh1YascdQMEubL004VWFxZS5RW8V3pMNifxvrOo%2BRlUSBcAdjOZNFH8ufKpo4%2FNcP7auEemx&X-Amz-Signature=f7137696c0f934c91269f59690212f8ad8e47d9a1f30bf0dc99c7760b186e937&X-Amz-SignedHeaders=host&x-id=GetObject)
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


