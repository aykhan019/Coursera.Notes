

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WBUUJVI%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCoGv%2FvL8Shk3ErOfgrnfWWyCQAit7cseu2F20V%2FEy42wIhAJ2e0lwnJHLnJRV7ZL0jK3LoCnx89HR5Uv0sW%2FT2WTFwKv8DCH8QABoMNjM3NDIzMTgzODA1IgzdE7Z8gZ0GnvuBJQ0q3AOgVsBESuz2C5lpWybGbtPPOVX1oJCuEUI%2FOaCqI%2BNDvXlEFxW7CRk6tD0cZMxu%2FTkLNF8bswzolcrQBwQ8%2F%2BiaL40yOv4Nyu%2BdrfaHP7u1Rk2KCpZy44ZCOxlGv2l4cYenc6AkvPGhL9CfCylONiPKNDeEZjFJVzNVlIewhp40O6HSsoURGnZKTIKNW3oukgm%2FgpVK3%2Fj0WfCH9FtL0i3rX8P%2FH66Rop1%2FZRek6f%2FW8YwbxUdckrW9xKgIZ17xXlBRxweqsQc9q6rdUE9knMW65PZz1Jf8d0OJNoOQVsF8hzBrwPZLcCH4%2BOqe18ZMyg%2Bl3zhWLQ57XxW%2FhGyz6Iywibr8gjX%2BPcY1dTMuQ5ewBndHbTihTCr00qvnfjVLEA0VvUEWiuGUkZMSlcHEwNgk84N%2FzYF07NwA42RPe4mUbe40EQiZ%2Baj12uj4b6yS77fn1xlIXHQR8T8czvrzuKuUDh3NwZz8z%2BhNl5kKac4u9FDvOFnKlKtjccW2XQxzawqadmEcpdzqG1rJKgiITEMhyrc8kH8wMr7RKe1ZUHnevcKkZ%2BAQMQI54JcA5tjuLa3%2BJGKsh7w%2B6rb9C8vHuDkwevyNbK%2Br3nRAtug6Hx76d2sgsYUaCOoOZzOIXTCAseW8BjqkAR84X172S36sjd1DOhhBBgzfOM5B%2FU4gzyx0M%2Bbb2THofeUlV6CDmAgOjx76NgzKHxo61hqUPv9KuGY85cKiLpknTUG1oyco4uF%2FgqP12ignJRpAiCfao6R19BlJm6hOiGGKFuKKXcNSi%2Bt5BdKSQDEiPllsfPFWt%2BOUSdgwhAP%2FBgzKwey9MAJCG8WhnrCnnzumTN2DR5G2T0E4ji1hndgpZ3R7&X-Amz-Signature=b5ce16035d1be3bcd4341afd40b52f35010e510cc7a31bcbd84fa5193b8f8193&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMWO2UY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCIocghhXxCjmLNttT%2F6bWkEtn5CWH74xlHdXn%2BCzdIbAIhAIsNj48qAo78rsovL4y4L%2BgQ9DHbxWTm9dkKgntBC20SKv8DCH8QABoMNjM3NDIzMTgzODA1IgyH4tiDPlhrBQJv4W8q3AN4aZiFey9GxU7rPIMyZRpYSJACmZK01C2ww3DxQiB0TbEYW0myT6G3wh26gJ5FkmzJiJan%2B9hsj1ZZUREcOoCCSh0T1cJQEGVE1SzD1j4VTdIkan6%2Bbyyo89P3z8iqMo9qFqB0xntdNZcHJQpDGMyA7w8ggw6aQRAzThVgsDc%2F0wd6ru8Q66qskWOiZfg4uMuS1Q3XLGHOxfU47QOZNsR5bV3Vv6QxUOCo00lbaykvxzDwdWvKI6IdUD5DGbmu4Ol0wKmn8v5DbVcfzRFxEB0dVOHPDoZp%2FkSJ%2BoRY%2BtxilnMgH5%2BStrOfaaJ26Y9D2Dae5PlZAgvSSohRREog4OqXaRESws3l1tQD5pIjmrMGd0fLufky4o4oUOhiLF5p4sQQdEDTkrHlJfXEwRc%2FkNJUyN2LQ8VNXh%2F7zDhcG7SRW%2F9n0fB8b%2BApm7NGrjikRcBvsAR%2BjJX4XCMrNTVgdl0BaYxW69NK8EFg0IPM8rqcYRkEO87UHqtlPKfDLHwi5vzaCgwkXeN2LLsRRT3JidLBWWdfc%2BnTnckDGRh2Qiwd9vITZAP%2FrKPEvk8ahPEjD8Hk8nF5u4Fchda5lg7laOyMON3P040xx5z6e15BgBZmNB4ycppnxedValElITC0sOW8BjqkAS6ineQlfyx509fxuPUkJ1bbicg0K6sJMNhooKF8HweolMMkngCbmLBOwuQW39FahzqDF5EAxxVsBl6s%2BHbpPFj6mGretC5bShk2%2BlME9TjCWsey2teuqNTupEV48TMkFjoRezktFilWZf8MpWpOBbKXEI02ePU1BAB4fUpn2GBmxZXZFeESvS7D7a3OPxIEN%2FpG47wK%2FnhpAtFcfmAcmwku7MtR&X-Amz-Signature=535ab1c30cc739e76d56bae42adbc5d045b795dfc152c45d47229e0e7f5a119c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMWO2UY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCIocghhXxCjmLNttT%2F6bWkEtn5CWH74xlHdXn%2BCzdIbAIhAIsNj48qAo78rsovL4y4L%2BgQ9DHbxWTm9dkKgntBC20SKv8DCH8QABoMNjM3NDIzMTgzODA1IgyH4tiDPlhrBQJv4W8q3AN4aZiFey9GxU7rPIMyZRpYSJACmZK01C2ww3DxQiB0TbEYW0myT6G3wh26gJ5FkmzJiJan%2B9hsj1ZZUREcOoCCSh0T1cJQEGVE1SzD1j4VTdIkan6%2Bbyyo89P3z8iqMo9qFqB0xntdNZcHJQpDGMyA7w8ggw6aQRAzThVgsDc%2F0wd6ru8Q66qskWOiZfg4uMuS1Q3XLGHOxfU47QOZNsR5bV3Vv6QxUOCo00lbaykvxzDwdWvKI6IdUD5DGbmu4Ol0wKmn8v5DbVcfzRFxEB0dVOHPDoZp%2FkSJ%2BoRY%2BtxilnMgH5%2BStrOfaaJ26Y9D2Dae5PlZAgvSSohRREog4OqXaRESws3l1tQD5pIjmrMGd0fLufky4o4oUOhiLF5p4sQQdEDTkrHlJfXEwRc%2FkNJUyN2LQ8VNXh%2F7zDhcG7SRW%2F9n0fB8b%2BApm7NGrjikRcBvsAR%2BjJX4XCMrNTVgdl0BaYxW69NK8EFg0IPM8rqcYRkEO87UHqtlPKfDLHwi5vzaCgwkXeN2LLsRRT3JidLBWWdfc%2BnTnckDGRh2Qiwd9vITZAP%2FrKPEvk8ahPEjD8Hk8nF5u4Fchda5lg7laOyMON3P040xx5z6e15BgBZmNB4ycppnxedValElITC0sOW8BjqkAS6ineQlfyx509fxuPUkJ1bbicg0K6sJMNhooKF8HweolMMkngCbmLBOwuQW39FahzqDF5EAxxVsBl6s%2BHbpPFj6mGretC5bShk2%2BlME9TjCWsey2teuqNTupEV48TMkFjoRezktFilWZf8MpWpOBbKXEI02ePU1BAB4fUpn2GBmxZXZFeESvS7D7a3OPxIEN%2FpG47wK%2FnhpAtFcfmAcmwku7MtR&X-Amz-Signature=b7a8d37affb456ec0ccb1aad26c8ac91728840fb22e89bd46a4b4634c89b4488&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMWO2UY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCIocghhXxCjmLNttT%2F6bWkEtn5CWH74xlHdXn%2BCzdIbAIhAIsNj48qAo78rsovL4y4L%2BgQ9DHbxWTm9dkKgntBC20SKv8DCH8QABoMNjM3NDIzMTgzODA1IgyH4tiDPlhrBQJv4W8q3AN4aZiFey9GxU7rPIMyZRpYSJACmZK01C2ww3DxQiB0TbEYW0myT6G3wh26gJ5FkmzJiJan%2B9hsj1ZZUREcOoCCSh0T1cJQEGVE1SzD1j4VTdIkan6%2Bbyyo89P3z8iqMo9qFqB0xntdNZcHJQpDGMyA7w8ggw6aQRAzThVgsDc%2F0wd6ru8Q66qskWOiZfg4uMuS1Q3XLGHOxfU47QOZNsR5bV3Vv6QxUOCo00lbaykvxzDwdWvKI6IdUD5DGbmu4Ol0wKmn8v5DbVcfzRFxEB0dVOHPDoZp%2FkSJ%2BoRY%2BtxilnMgH5%2BStrOfaaJ26Y9D2Dae5PlZAgvSSohRREog4OqXaRESws3l1tQD5pIjmrMGd0fLufky4o4oUOhiLF5p4sQQdEDTkrHlJfXEwRc%2FkNJUyN2LQ8VNXh%2F7zDhcG7SRW%2F9n0fB8b%2BApm7NGrjikRcBvsAR%2BjJX4XCMrNTVgdl0BaYxW69NK8EFg0IPM8rqcYRkEO87UHqtlPKfDLHwi5vzaCgwkXeN2LLsRRT3JidLBWWdfc%2BnTnckDGRh2Qiwd9vITZAP%2FrKPEvk8ahPEjD8Hk8nF5u4Fchda5lg7laOyMON3P040xx5z6e15BgBZmNB4ycppnxedValElITC0sOW8BjqkAS6ineQlfyx509fxuPUkJ1bbicg0K6sJMNhooKF8HweolMMkngCbmLBOwuQW39FahzqDF5EAxxVsBl6s%2BHbpPFj6mGretC5bShk2%2BlME9TjCWsey2teuqNTupEV48TMkFjoRezktFilWZf8MpWpOBbKXEI02ePU1BAB4fUpn2GBmxZXZFeESvS7D7a3OPxIEN%2FpG47wK%2FnhpAtFcfmAcmwku7MtR&X-Amz-Signature=7a393d5e1b144878ce761792d0a368a441307e91b7a2d8277f8cbb5d7d9b93bd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMWO2UY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCIocghhXxCjmLNttT%2F6bWkEtn5CWH74xlHdXn%2BCzdIbAIhAIsNj48qAo78rsovL4y4L%2BgQ9DHbxWTm9dkKgntBC20SKv8DCH8QABoMNjM3NDIzMTgzODA1IgyH4tiDPlhrBQJv4W8q3AN4aZiFey9GxU7rPIMyZRpYSJACmZK01C2ww3DxQiB0TbEYW0myT6G3wh26gJ5FkmzJiJan%2B9hsj1ZZUREcOoCCSh0T1cJQEGVE1SzD1j4VTdIkan6%2Bbyyo89P3z8iqMo9qFqB0xntdNZcHJQpDGMyA7w8ggw6aQRAzThVgsDc%2F0wd6ru8Q66qskWOiZfg4uMuS1Q3XLGHOxfU47QOZNsR5bV3Vv6QxUOCo00lbaykvxzDwdWvKI6IdUD5DGbmu4Ol0wKmn8v5DbVcfzRFxEB0dVOHPDoZp%2FkSJ%2BoRY%2BtxilnMgH5%2BStrOfaaJ26Y9D2Dae5PlZAgvSSohRREog4OqXaRESws3l1tQD5pIjmrMGd0fLufky4o4oUOhiLF5p4sQQdEDTkrHlJfXEwRc%2FkNJUyN2LQ8VNXh%2F7zDhcG7SRW%2F9n0fB8b%2BApm7NGrjikRcBvsAR%2BjJX4XCMrNTVgdl0BaYxW69NK8EFg0IPM8rqcYRkEO87UHqtlPKfDLHwi5vzaCgwkXeN2LLsRRT3JidLBWWdfc%2BnTnckDGRh2Qiwd9vITZAP%2FrKPEvk8ahPEjD8Hk8nF5u4Fchda5lg7laOyMON3P040xx5z6e15BgBZmNB4ycppnxedValElITC0sOW8BjqkAS6ineQlfyx509fxuPUkJ1bbicg0K6sJMNhooKF8HweolMMkngCbmLBOwuQW39FahzqDF5EAxxVsBl6s%2BHbpPFj6mGretC5bShk2%2BlME9TjCWsey2teuqNTupEV48TMkFjoRezktFilWZf8MpWpOBbKXEI02ePU1BAB4fUpn2GBmxZXZFeESvS7D7a3OPxIEN%2FpG47wK%2FnhpAtFcfmAcmwku7MtR&X-Amz-Signature=cde7888a177573c857b1d09257d5d3546808449221d1bffddae6a213fe70bde6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMWO2UY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCIocghhXxCjmLNttT%2F6bWkEtn5CWH74xlHdXn%2BCzdIbAIhAIsNj48qAo78rsovL4y4L%2BgQ9DHbxWTm9dkKgntBC20SKv8DCH8QABoMNjM3NDIzMTgzODA1IgyH4tiDPlhrBQJv4W8q3AN4aZiFey9GxU7rPIMyZRpYSJACmZK01C2ww3DxQiB0TbEYW0myT6G3wh26gJ5FkmzJiJan%2B9hsj1ZZUREcOoCCSh0T1cJQEGVE1SzD1j4VTdIkan6%2Bbyyo89P3z8iqMo9qFqB0xntdNZcHJQpDGMyA7w8ggw6aQRAzThVgsDc%2F0wd6ru8Q66qskWOiZfg4uMuS1Q3XLGHOxfU47QOZNsR5bV3Vv6QxUOCo00lbaykvxzDwdWvKI6IdUD5DGbmu4Ol0wKmn8v5DbVcfzRFxEB0dVOHPDoZp%2FkSJ%2BoRY%2BtxilnMgH5%2BStrOfaaJ26Y9D2Dae5PlZAgvSSohRREog4OqXaRESws3l1tQD5pIjmrMGd0fLufky4o4oUOhiLF5p4sQQdEDTkrHlJfXEwRc%2FkNJUyN2LQ8VNXh%2F7zDhcG7SRW%2F9n0fB8b%2BApm7NGrjikRcBvsAR%2BjJX4XCMrNTVgdl0BaYxW69NK8EFg0IPM8rqcYRkEO87UHqtlPKfDLHwi5vzaCgwkXeN2LLsRRT3JidLBWWdfc%2BnTnckDGRh2Qiwd9vITZAP%2FrKPEvk8ahPEjD8Hk8nF5u4Fchda5lg7laOyMON3P040xx5z6e15BgBZmNB4ycppnxedValElITC0sOW8BjqkAS6ineQlfyx509fxuPUkJ1bbicg0K6sJMNhooKF8HweolMMkngCbmLBOwuQW39FahzqDF5EAxxVsBl6s%2BHbpPFj6mGretC5bShk2%2BlME9TjCWsey2teuqNTupEV48TMkFjoRezktFilWZf8MpWpOBbKXEI02ePU1BAB4fUpn2GBmxZXZFeESvS7D7a3OPxIEN%2FpG47wK%2FnhpAtFcfmAcmwku7MtR&X-Amz-Signature=d8bb07b742f882ea21701e3e24b491d64f4ca76162187301ca0bad4bf9a9986f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WBUUJVI%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCoGv%2FvL8Shk3ErOfgrnfWWyCQAit7cseu2F20V%2FEy42wIhAJ2e0lwnJHLnJRV7ZL0jK3LoCnx89HR5Uv0sW%2FT2WTFwKv8DCH8QABoMNjM3NDIzMTgzODA1IgzdE7Z8gZ0GnvuBJQ0q3AOgVsBESuz2C5lpWybGbtPPOVX1oJCuEUI%2FOaCqI%2BNDvXlEFxW7CRk6tD0cZMxu%2FTkLNF8bswzolcrQBwQ8%2F%2BiaL40yOv4Nyu%2BdrfaHP7u1Rk2KCpZy44ZCOxlGv2l4cYenc6AkvPGhL9CfCylONiPKNDeEZjFJVzNVlIewhp40O6HSsoURGnZKTIKNW3oukgm%2FgpVK3%2Fj0WfCH9FtL0i3rX8P%2FH66Rop1%2FZRek6f%2FW8YwbxUdckrW9xKgIZ17xXlBRxweqsQc9q6rdUE9knMW65PZz1Jf8d0OJNoOQVsF8hzBrwPZLcCH4%2BOqe18ZMyg%2Bl3zhWLQ57XxW%2FhGyz6Iywibr8gjX%2BPcY1dTMuQ5ewBndHbTihTCr00qvnfjVLEA0VvUEWiuGUkZMSlcHEwNgk84N%2FzYF07NwA42RPe4mUbe40EQiZ%2Baj12uj4b6yS77fn1xlIXHQR8T8czvrzuKuUDh3NwZz8z%2BhNl5kKac4u9FDvOFnKlKtjccW2XQxzawqadmEcpdzqG1rJKgiITEMhyrc8kH8wMr7RKe1ZUHnevcKkZ%2BAQMQI54JcA5tjuLa3%2BJGKsh7w%2B6rb9C8vHuDkwevyNbK%2Br3nRAtug6Hx76d2sgsYUaCOoOZzOIXTCAseW8BjqkAR84X172S36sjd1DOhhBBgzfOM5B%2FU4gzyx0M%2Bbb2THofeUlV6CDmAgOjx76NgzKHxo61hqUPv9KuGY85cKiLpknTUG1oyco4uF%2FgqP12ignJRpAiCfao6R19BlJm6hOiGGKFuKKXcNSi%2Bt5BdKSQDEiPllsfPFWt%2BOUSdgwhAP%2FBgzKwey9MAJCG8WhnrCnnzumTN2DR5G2T0E4ji1hndgpZ3R7&X-Amz-Signature=c0825bda407fbce0bac2ce427fc2266f1c65df7736e5eea278b60a9ec9b2a40d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WBUUJVI%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCoGv%2FvL8Shk3ErOfgrnfWWyCQAit7cseu2F20V%2FEy42wIhAJ2e0lwnJHLnJRV7ZL0jK3LoCnx89HR5Uv0sW%2FT2WTFwKv8DCH8QABoMNjM3NDIzMTgzODA1IgzdE7Z8gZ0GnvuBJQ0q3AOgVsBESuz2C5lpWybGbtPPOVX1oJCuEUI%2FOaCqI%2BNDvXlEFxW7CRk6tD0cZMxu%2FTkLNF8bswzolcrQBwQ8%2F%2BiaL40yOv4Nyu%2BdrfaHP7u1Rk2KCpZy44ZCOxlGv2l4cYenc6AkvPGhL9CfCylONiPKNDeEZjFJVzNVlIewhp40O6HSsoURGnZKTIKNW3oukgm%2FgpVK3%2Fj0WfCH9FtL0i3rX8P%2FH66Rop1%2FZRek6f%2FW8YwbxUdckrW9xKgIZ17xXlBRxweqsQc9q6rdUE9knMW65PZz1Jf8d0OJNoOQVsF8hzBrwPZLcCH4%2BOqe18ZMyg%2Bl3zhWLQ57XxW%2FhGyz6Iywibr8gjX%2BPcY1dTMuQ5ewBndHbTihTCr00qvnfjVLEA0VvUEWiuGUkZMSlcHEwNgk84N%2FzYF07NwA42RPe4mUbe40EQiZ%2Baj12uj4b6yS77fn1xlIXHQR8T8czvrzuKuUDh3NwZz8z%2BhNl5kKac4u9FDvOFnKlKtjccW2XQxzawqadmEcpdzqG1rJKgiITEMhyrc8kH8wMr7RKe1ZUHnevcKkZ%2BAQMQI54JcA5tjuLa3%2BJGKsh7w%2B6rb9C8vHuDkwevyNbK%2Br3nRAtug6Hx76d2sgsYUaCOoOZzOIXTCAseW8BjqkAR84X172S36sjd1DOhhBBgzfOM5B%2FU4gzyx0M%2Bbb2THofeUlV6CDmAgOjx76NgzKHxo61hqUPv9KuGY85cKiLpknTUG1oyco4uF%2FgqP12ignJRpAiCfao6R19BlJm6hOiGGKFuKKXcNSi%2Bt5BdKSQDEiPllsfPFWt%2BOUSdgwhAP%2FBgzKwey9MAJCG8WhnrCnnzumTN2DR5G2T0E4ji1hndgpZ3R7&X-Amz-Signature=65012eed7469e2e4c9faeb45fe899c9d399702cd4d11409fbbed8bb206fbdb33&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WBUUJVI%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCoGv%2FvL8Shk3ErOfgrnfWWyCQAit7cseu2F20V%2FEy42wIhAJ2e0lwnJHLnJRV7ZL0jK3LoCnx89HR5Uv0sW%2FT2WTFwKv8DCH8QABoMNjM3NDIzMTgzODA1IgzdE7Z8gZ0GnvuBJQ0q3AOgVsBESuz2C5lpWybGbtPPOVX1oJCuEUI%2FOaCqI%2BNDvXlEFxW7CRk6tD0cZMxu%2FTkLNF8bswzolcrQBwQ8%2F%2BiaL40yOv4Nyu%2BdrfaHP7u1Rk2KCpZy44ZCOxlGv2l4cYenc6AkvPGhL9CfCylONiPKNDeEZjFJVzNVlIewhp40O6HSsoURGnZKTIKNW3oukgm%2FgpVK3%2Fj0WfCH9FtL0i3rX8P%2FH66Rop1%2FZRek6f%2FW8YwbxUdckrW9xKgIZ17xXlBRxweqsQc9q6rdUE9knMW65PZz1Jf8d0OJNoOQVsF8hzBrwPZLcCH4%2BOqe18ZMyg%2Bl3zhWLQ57XxW%2FhGyz6Iywibr8gjX%2BPcY1dTMuQ5ewBndHbTihTCr00qvnfjVLEA0VvUEWiuGUkZMSlcHEwNgk84N%2FzYF07NwA42RPe4mUbe40EQiZ%2Baj12uj4b6yS77fn1xlIXHQR8T8czvrzuKuUDh3NwZz8z%2BhNl5kKac4u9FDvOFnKlKtjccW2XQxzawqadmEcpdzqG1rJKgiITEMhyrc8kH8wMr7RKe1ZUHnevcKkZ%2BAQMQI54JcA5tjuLa3%2BJGKsh7w%2B6rb9C8vHuDkwevyNbK%2Br3nRAtug6Hx76d2sgsYUaCOoOZzOIXTCAseW8BjqkAR84X172S36sjd1DOhhBBgzfOM5B%2FU4gzyx0M%2Bbb2THofeUlV6CDmAgOjx76NgzKHxo61hqUPv9KuGY85cKiLpknTUG1oyco4uF%2FgqP12ignJRpAiCfao6R19BlJm6hOiGGKFuKKXcNSi%2Bt5BdKSQDEiPllsfPFWt%2BOUSdgwhAP%2FBgzKwey9MAJCG8WhnrCnnzumTN2DR5G2T0E4ji1hndgpZ3R7&X-Amz-Signature=0f6526cb76c78f3a314fc80351a11645b68e8d4c6bb5987bae53b35ec926e932&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WBUUJVI%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCoGv%2FvL8Shk3ErOfgrnfWWyCQAit7cseu2F20V%2FEy42wIhAJ2e0lwnJHLnJRV7ZL0jK3LoCnx89HR5Uv0sW%2FT2WTFwKv8DCH8QABoMNjM3NDIzMTgzODA1IgzdE7Z8gZ0GnvuBJQ0q3AOgVsBESuz2C5lpWybGbtPPOVX1oJCuEUI%2FOaCqI%2BNDvXlEFxW7CRk6tD0cZMxu%2FTkLNF8bswzolcrQBwQ8%2F%2BiaL40yOv4Nyu%2BdrfaHP7u1Rk2KCpZy44ZCOxlGv2l4cYenc6AkvPGhL9CfCylONiPKNDeEZjFJVzNVlIewhp40O6HSsoURGnZKTIKNW3oukgm%2FgpVK3%2Fj0WfCH9FtL0i3rX8P%2FH66Rop1%2FZRek6f%2FW8YwbxUdckrW9xKgIZ17xXlBRxweqsQc9q6rdUE9knMW65PZz1Jf8d0OJNoOQVsF8hzBrwPZLcCH4%2BOqe18ZMyg%2Bl3zhWLQ57XxW%2FhGyz6Iywibr8gjX%2BPcY1dTMuQ5ewBndHbTihTCr00qvnfjVLEA0VvUEWiuGUkZMSlcHEwNgk84N%2FzYF07NwA42RPe4mUbe40EQiZ%2Baj12uj4b6yS77fn1xlIXHQR8T8czvrzuKuUDh3NwZz8z%2BhNl5kKac4u9FDvOFnKlKtjccW2XQxzawqadmEcpdzqG1rJKgiITEMhyrc8kH8wMr7RKe1ZUHnevcKkZ%2BAQMQI54JcA5tjuLa3%2BJGKsh7w%2B6rb9C8vHuDkwevyNbK%2Br3nRAtug6Hx76d2sgsYUaCOoOZzOIXTCAseW8BjqkAR84X172S36sjd1DOhhBBgzfOM5B%2FU4gzyx0M%2Bbb2THofeUlV6CDmAgOjx76NgzKHxo61hqUPv9KuGY85cKiLpknTUG1oyco4uF%2FgqP12ignJRpAiCfao6R19BlJm6hOiGGKFuKKXcNSi%2Bt5BdKSQDEiPllsfPFWt%2BOUSdgwhAP%2FBgzKwey9MAJCG8WhnrCnnzumTN2DR5G2T0E4ji1hndgpZ3R7&X-Amz-Signature=936f4b3f2ffd9a5e603ca8e319314453a36e4cf9843b590c7b9107b334158fb9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WBUUJVI%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCoGv%2FvL8Shk3ErOfgrnfWWyCQAit7cseu2F20V%2FEy42wIhAJ2e0lwnJHLnJRV7ZL0jK3LoCnx89HR5Uv0sW%2FT2WTFwKv8DCH8QABoMNjM3NDIzMTgzODA1IgzdE7Z8gZ0GnvuBJQ0q3AOgVsBESuz2C5lpWybGbtPPOVX1oJCuEUI%2FOaCqI%2BNDvXlEFxW7CRk6tD0cZMxu%2FTkLNF8bswzolcrQBwQ8%2F%2BiaL40yOv4Nyu%2BdrfaHP7u1Rk2KCpZy44ZCOxlGv2l4cYenc6AkvPGhL9CfCylONiPKNDeEZjFJVzNVlIewhp40O6HSsoURGnZKTIKNW3oukgm%2FgpVK3%2Fj0WfCH9FtL0i3rX8P%2FH66Rop1%2FZRek6f%2FW8YwbxUdckrW9xKgIZ17xXlBRxweqsQc9q6rdUE9knMW65PZz1Jf8d0OJNoOQVsF8hzBrwPZLcCH4%2BOqe18ZMyg%2Bl3zhWLQ57XxW%2FhGyz6Iywibr8gjX%2BPcY1dTMuQ5ewBndHbTihTCr00qvnfjVLEA0VvUEWiuGUkZMSlcHEwNgk84N%2FzYF07NwA42RPe4mUbe40EQiZ%2Baj12uj4b6yS77fn1xlIXHQR8T8czvrzuKuUDh3NwZz8z%2BhNl5kKac4u9FDvOFnKlKtjccW2XQxzawqadmEcpdzqG1rJKgiITEMhyrc8kH8wMr7RKe1ZUHnevcKkZ%2BAQMQI54JcA5tjuLa3%2BJGKsh7w%2B6rb9C8vHuDkwevyNbK%2Br3nRAtug6Hx76d2sgsYUaCOoOZzOIXTCAseW8BjqkAR84X172S36sjd1DOhhBBgzfOM5B%2FU4gzyx0M%2Bbb2THofeUlV6CDmAgOjx76NgzKHxo61hqUPv9KuGY85cKiLpknTUG1oyco4uF%2FgqP12ignJRpAiCfao6R19BlJm6hOiGGKFuKKXcNSi%2Bt5BdKSQDEiPllsfPFWt%2BOUSdgwhAP%2FBgzKwey9MAJCG8WhnrCnnzumTN2DR5G2T0E4ji1hndgpZ3R7&X-Amz-Signature=ca4c540004ba9826ecd78a1abb4bc68ff1216563c20b1d13c379e86ab6c844dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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


