

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZA7ZY7I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDnKut4q7Dg9lT%2FHgdVX8UrSLRiBPOGdAf0OhplbowwsgIhAI5r4DvUeVW62pdJ3JXMOXejjlDGqmgAiI1kPH9%2FEFjEKv8DCDQQABoMNjM3NDIzMTgzODA1Igxrgv64Xutw87vgde4q3ANiUyfyPZgJ6jE4A9Hk0DogvxYe8%2B0jY5MLI%2BXePxXbTQnLJz7j1FWbmtta8tSPnnE%2F8VKRZ%2Bsjbo02dYKQEF5C42HVKFykA2LB%2FPn2y6aVRuNjYJLc8gw48bHi6VW4whcFi9Xrksz8CXAqBM8W9DrUga%2BiqRY3pZtC5IEtO3QPSTFZjYlwDKtdydQEmIuPQggYVOMRktzog%2BvxcZKAWdHQVFebB%2F1YYMSugAL4sAQwK2pbMSywIchK0jZB9rDsB3ODigVkT8Tgmfd4nGDxlokCmMsG8PKldXXMMV%2FZM0NBsPpszLGPqjWZ94uLgWOCueIwtMoSFQy4SybJwTjNTNa%2B%2B1wlI9H59ovZMl%2Bf3oLzAs85DVTR0qrXlPs9BY1N9W2TVkn5EByccycn%2BqN42vB9BwOkM%2BqA77xXgC9LxAP1V7VER7tir2Tov%2F0UvulT6lihPSz%2BhE5SqI%2BmNUJ4FMcb4yLYIAhO0IClrJjK3zCpZNbRCfAWVDVzH9el%2FHE3TPkL6EKA8Jrtw3QAJAdcW40HIFJ%2F62A4pQtzQqkTIoq%2FXYXe752CTF1%2FiECjHAfHXruQd7uRG5SWrggkUB%2BerCDY4Sn23iGJiOwAFmJg%2Fj3232Q50tgSO0HNNigV5zCQvYm9BjqkAcBQhIwmONPvlgSikRWiol751Lo1XkHy63XVuTBeaKFT%2F6ZXXSBH%2FatTUFdcleQWNDjfKuSrP6LD4C8xEteCqfTnBpBD%2BcHT31EzkGY%2BIL1mgqx4NsShXJfGQ6LXrWnuyG3anAAHtts%2B1eLnqvAxnoUa0Di9nZ3D%2F526xrjJODc9p7X30ZAjT0CR1XW7abRo8PNw1ZbZY61%2BTE1BbISo3AmNvUQ8&X-Amz-Signature=de595c1cf8ecbf9df85e6d132c4188822ec38d28df6cc693e9d830edeb189f26&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCOSNZSL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIADbHZbLHNNtl%2BiSxmxQuOYqA0JBbUNmnsFiElN3FpVJAiA0KSLM%2BVJwYHwkE9wac6y051PAsYWICBYRRE3eetACmyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMJYdhTwhj2QJ%2B5s1YKtwD%2BF8HXpjHKt1GDmsmSBaK5%2BzUzQIKyIXOdU09uyIq3fhoTWrGFRa4wnVK8r7FhWpSE%2B%2BsnO8ddfI9uzuN4LslQQA0H62RvNpF65%2F26NZU3J0z4zSq%2B77DUYzicMI8nSa49ebbhh7V0ZECnVbUOCs7Yr3Fs0a6UPCpF6lJcvn2vs009030F05wuvEbt5XJ6nI0U3TFqMuSDjSgekthqIW4OwnZ9E7kH%2BLMRv3aqC3NWHO2NWilQBmImI5PV8SHFVV9GcVPCJk4aKObJSzehKRo2wPCylvDkfJt2Em5lbAptnl7MSyNENad1H9VKJAw50EGRdksoWT%2Fb4vjjjw%2BXiRYGVuRnqkbZwQkONwcygjPb008EGutVB9r3Riz2k2mxSukAcR%2F4wH0EaZs%2FW%2FmR1MlkBQuE62Q4ce%2BhVlhNkT9AZowxcuV%2BkQpv0I42rLGegpOffs8zZdyvyiSO5KHzwjtGsv%2BULf8RMIIqlK8yxjAbQ5vhUJlRxf%2Fqy4jIbImP9BH0utqefeGMEL17RzmSzszdvtW%2BwKbIGUDlZTBGDhtiTQqOTiB8ikArSKVOYS1U8jWJMHJRtGCAwBtvR4gesyvJWu51H8fiih%2BAvv8evSOhsFwUKtr3h8iD2xQK%2FUwxb2JvQY6pgHglrdyjNd3f4upkFBdI9ZjoR1EOjTUCby3OwpGRHX2MIPe%2FbEai7Zyfsv1eSwh8RxIgXACkzP17zMqLGe8cV423rBorajYmQSLAta7FWkcC%2BvVb8pWAGPUulGncKRBmPwJWJ%2FBP8PZHoAq1GWp0vd4k9fOaxrEpSMwcWsKuYZZjHiNblJrevSb0w98wNC1w%2BEcEKelssU%2BnxWQJHDQH4A9yhses3DS&X-Amz-Signature=a11cd729664f998ebbc076bb5d9ab50d84a1423e08721d1ba6c91bbdfda18d73&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCOSNZSL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIADbHZbLHNNtl%2BiSxmxQuOYqA0JBbUNmnsFiElN3FpVJAiA0KSLM%2BVJwYHwkE9wac6y051PAsYWICBYRRE3eetACmyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMJYdhTwhj2QJ%2B5s1YKtwD%2BF8HXpjHKt1GDmsmSBaK5%2BzUzQIKyIXOdU09uyIq3fhoTWrGFRa4wnVK8r7FhWpSE%2B%2BsnO8ddfI9uzuN4LslQQA0H62RvNpF65%2F26NZU3J0z4zSq%2B77DUYzicMI8nSa49ebbhh7V0ZECnVbUOCs7Yr3Fs0a6UPCpF6lJcvn2vs009030F05wuvEbt5XJ6nI0U3TFqMuSDjSgekthqIW4OwnZ9E7kH%2BLMRv3aqC3NWHO2NWilQBmImI5PV8SHFVV9GcVPCJk4aKObJSzehKRo2wPCylvDkfJt2Em5lbAptnl7MSyNENad1H9VKJAw50EGRdksoWT%2Fb4vjjjw%2BXiRYGVuRnqkbZwQkONwcygjPb008EGutVB9r3Riz2k2mxSukAcR%2F4wH0EaZs%2FW%2FmR1MlkBQuE62Q4ce%2BhVlhNkT9AZowxcuV%2BkQpv0I42rLGegpOffs8zZdyvyiSO5KHzwjtGsv%2BULf8RMIIqlK8yxjAbQ5vhUJlRxf%2Fqy4jIbImP9BH0utqefeGMEL17RzmSzszdvtW%2BwKbIGUDlZTBGDhtiTQqOTiB8ikArSKVOYS1U8jWJMHJRtGCAwBtvR4gesyvJWu51H8fiih%2BAvv8evSOhsFwUKtr3h8iD2xQK%2FUwxb2JvQY6pgHglrdyjNd3f4upkFBdI9ZjoR1EOjTUCby3OwpGRHX2MIPe%2FbEai7Zyfsv1eSwh8RxIgXACkzP17zMqLGe8cV423rBorajYmQSLAta7FWkcC%2BvVb8pWAGPUulGncKRBmPwJWJ%2FBP8PZHoAq1GWp0vd4k9fOaxrEpSMwcWsKuYZZjHiNblJrevSb0w98wNC1w%2BEcEKelssU%2BnxWQJHDQH4A9yhses3DS&X-Amz-Signature=bf0ded4cd2815099a0d1f44d888d4a34a5d5869f8ddc4d6ee7ab149c70bc19d8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCOSNZSL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIADbHZbLHNNtl%2BiSxmxQuOYqA0JBbUNmnsFiElN3FpVJAiA0KSLM%2BVJwYHwkE9wac6y051PAsYWICBYRRE3eetACmyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMJYdhTwhj2QJ%2B5s1YKtwD%2BF8HXpjHKt1GDmsmSBaK5%2BzUzQIKyIXOdU09uyIq3fhoTWrGFRa4wnVK8r7FhWpSE%2B%2BsnO8ddfI9uzuN4LslQQA0H62RvNpF65%2F26NZU3J0z4zSq%2B77DUYzicMI8nSa49ebbhh7V0ZECnVbUOCs7Yr3Fs0a6UPCpF6lJcvn2vs009030F05wuvEbt5XJ6nI0U3TFqMuSDjSgekthqIW4OwnZ9E7kH%2BLMRv3aqC3NWHO2NWilQBmImI5PV8SHFVV9GcVPCJk4aKObJSzehKRo2wPCylvDkfJt2Em5lbAptnl7MSyNENad1H9VKJAw50EGRdksoWT%2Fb4vjjjw%2BXiRYGVuRnqkbZwQkONwcygjPb008EGutVB9r3Riz2k2mxSukAcR%2F4wH0EaZs%2FW%2FmR1MlkBQuE62Q4ce%2BhVlhNkT9AZowxcuV%2BkQpv0I42rLGegpOffs8zZdyvyiSO5KHzwjtGsv%2BULf8RMIIqlK8yxjAbQ5vhUJlRxf%2Fqy4jIbImP9BH0utqefeGMEL17RzmSzszdvtW%2BwKbIGUDlZTBGDhtiTQqOTiB8ikArSKVOYS1U8jWJMHJRtGCAwBtvR4gesyvJWu51H8fiih%2BAvv8evSOhsFwUKtr3h8iD2xQK%2FUwxb2JvQY6pgHglrdyjNd3f4upkFBdI9ZjoR1EOjTUCby3OwpGRHX2MIPe%2FbEai7Zyfsv1eSwh8RxIgXACkzP17zMqLGe8cV423rBorajYmQSLAta7FWkcC%2BvVb8pWAGPUulGncKRBmPwJWJ%2FBP8PZHoAq1GWp0vd4k9fOaxrEpSMwcWsKuYZZjHiNblJrevSb0w98wNC1w%2BEcEKelssU%2BnxWQJHDQH4A9yhses3DS&X-Amz-Signature=ff59691b4dcd91e03b876a6e0d20bd1eec042a8c1c5c5e179af805f691ad8cb2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCOSNZSL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIADbHZbLHNNtl%2BiSxmxQuOYqA0JBbUNmnsFiElN3FpVJAiA0KSLM%2BVJwYHwkE9wac6y051PAsYWICBYRRE3eetACmyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMJYdhTwhj2QJ%2B5s1YKtwD%2BF8HXpjHKt1GDmsmSBaK5%2BzUzQIKyIXOdU09uyIq3fhoTWrGFRa4wnVK8r7FhWpSE%2B%2BsnO8ddfI9uzuN4LslQQA0H62RvNpF65%2F26NZU3J0z4zSq%2B77DUYzicMI8nSa49ebbhh7V0ZECnVbUOCs7Yr3Fs0a6UPCpF6lJcvn2vs009030F05wuvEbt5XJ6nI0U3TFqMuSDjSgekthqIW4OwnZ9E7kH%2BLMRv3aqC3NWHO2NWilQBmImI5PV8SHFVV9GcVPCJk4aKObJSzehKRo2wPCylvDkfJt2Em5lbAptnl7MSyNENad1H9VKJAw50EGRdksoWT%2Fb4vjjjw%2BXiRYGVuRnqkbZwQkONwcygjPb008EGutVB9r3Riz2k2mxSukAcR%2F4wH0EaZs%2FW%2FmR1MlkBQuE62Q4ce%2BhVlhNkT9AZowxcuV%2BkQpv0I42rLGegpOffs8zZdyvyiSO5KHzwjtGsv%2BULf8RMIIqlK8yxjAbQ5vhUJlRxf%2Fqy4jIbImP9BH0utqefeGMEL17RzmSzszdvtW%2BwKbIGUDlZTBGDhtiTQqOTiB8ikArSKVOYS1U8jWJMHJRtGCAwBtvR4gesyvJWu51H8fiih%2BAvv8evSOhsFwUKtr3h8iD2xQK%2FUwxb2JvQY6pgHglrdyjNd3f4upkFBdI9ZjoR1EOjTUCby3OwpGRHX2MIPe%2FbEai7Zyfsv1eSwh8RxIgXACkzP17zMqLGe8cV423rBorajYmQSLAta7FWkcC%2BvVb8pWAGPUulGncKRBmPwJWJ%2FBP8PZHoAq1GWp0vd4k9fOaxrEpSMwcWsKuYZZjHiNblJrevSb0w98wNC1w%2BEcEKelssU%2BnxWQJHDQH4A9yhses3DS&X-Amz-Signature=51fc4462dc479603d5898032d205f17386dac257410126b614dac560173f8fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCOSNZSL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIADbHZbLHNNtl%2BiSxmxQuOYqA0JBbUNmnsFiElN3FpVJAiA0KSLM%2BVJwYHwkE9wac6y051PAsYWICBYRRE3eetACmyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMJYdhTwhj2QJ%2B5s1YKtwD%2BF8HXpjHKt1GDmsmSBaK5%2BzUzQIKyIXOdU09uyIq3fhoTWrGFRa4wnVK8r7FhWpSE%2B%2BsnO8ddfI9uzuN4LslQQA0H62RvNpF65%2F26NZU3J0z4zSq%2B77DUYzicMI8nSa49ebbhh7V0ZECnVbUOCs7Yr3Fs0a6UPCpF6lJcvn2vs009030F05wuvEbt5XJ6nI0U3TFqMuSDjSgekthqIW4OwnZ9E7kH%2BLMRv3aqC3NWHO2NWilQBmImI5PV8SHFVV9GcVPCJk4aKObJSzehKRo2wPCylvDkfJt2Em5lbAptnl7MSyNENad1H9VKJAw50EGRdksoWT%2Fb4vjjjw%2BXiRYGVuRnqkbZwQkONwcygjPb008EGutVB9r3Riz2k2mxSukAcR%2F4wH0EaZs%2FW%2FmR1MlkBQuE62Q4ce%2BhVlhNkT9AZowxcuV%2BkQpv0I42rLGegpOffs8zZdyvyiSO5KHzwjtGsv%2BULf8RMIIqlK8yxjAbQ5vhUJlRxf%2Fqy4jIbImP9BH0utqefeGMEL17RzmSzszdvtW%2BwKbIGUDlZTBGDhtiTQqOTiB8ikArSKVOYS1U8jWJMHJRtGCAwBtvR4gesyvJWu51H8fiih%2BAvv8evSOhsFwUKtr3h8iD2xQK%2FUwxb2JvQY6pgHglrdyjNd3f4upkFBdI9ZjoR1EOjTUCby3OwpGRHX2MIPe%2FbEai7Zyfsv1eSwh8RxIgXACkzP17zMqLGe8cV423rBorajYmQSLAta7FWkcC%2BvVb8pWAGPUulGncKRBmPwJWJ%2FBP8PZHoAq1GWp0vd4k9fOaxrEpSMwcWsKuYZZjHiNblJrevSb0w98wNC1w%2BEcEKelssU%2BnxWQJHDQH4A9yhses3DS&X-Amz-Signature=149909d14f47a88ed2090ba33862974cefc8866d1d6102663267818276f7e784&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZA7ZY7I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDnKut4q7Dg9lT%2FHgdVX8UrSLRiBPOGdAf0OhplbowwsgIhAI5r4DvUeVW62pdJ3JXMOXejjlDGqmgAiI1kPH9%2FEFjEKv8DCDQQABoMNjM3NDIzMTgzODA1Igxrgv64Xutw87vgde4q3ANiUyfyPZgJ6jE4A9Hk0DogvxYe8%2B0jY5MLI%2BXePxXbTQnLJz7j1FWbmtta8tSPnnE%2F8VKRZ%2Bsjbo02dYKQEF5C42HVKFykA2LB%2FPn2y6aVRuNjYJLc8gw48bHi6VW4whcFi9Xrksz8CXAqBM8W9DrUga%2BiqRY3pZtC5IEtO3QPSTFZjYlwDKtdydQEmIuPQggYVOMRktzog%2BvxcZKAWdHQVFebB%2F1YYMSugAL4sAQwK2pbMSywIchK0jZB9rDsB3ODigVkT8Tgmfd4nGDxlokCmMsG8PKldXXMMV%2FZM0NBsPpszLGPqjWZ94uLgWOCueIwtMoSFQy4SybJwTjNTNa%2B%2B1wlI9H59ovZMl%2Bf3oLzAs85DVTR0qrXlPs9BY1N9W2TVkn5EByccycn%2BqN42vB9BwOkM%2BqA77xXgC9LxAP1V7VER7tir2Tov%2F0UvulT6lihPSz%2BhE5SqI%2BmNUJ4FMcb4yLYIAhO0IClrJjK3zCpZNbRCfAWVDVzH9el%2FHE3TPkL6EKA8Jrtw3QAJAdcW40HIFJ%2F62A4pQtzQqkTIoq%2FXYXe752CTF1%2FiECjHAfHXruQd7uRG5SWrggkUB%2BerCDY4Sn23iGJiOwAFmJg%2Fj3232Q50tgSO0HNNigV5zCQvYm9BjqkAcBQhIwmONPvlgSikRWiol751Lo1XkHy63XVuTBeaKFT%2F6ZXXSBH%2FatTUFdcleQWNDjfKuSrP6LD4C8xEteCqfTnBpBD%2BcHT31EzkGY%2BIL1mgqx4NsShXJfGQ6LXrWnuyG3anAAHtts%2B1eLnqvAxnoUa0Di9nZ3D%2F526xrjJODc9p7X30ZAjT0CR1XW7abRo8PNw1ZbZY61%2BTE1BbISo3AmNvUQ8&X-Amz-Signature=c03e504400bdb958288f221d621758261b47ba6bbb14388abcb286dc5e9e8a64&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZA7ZY7I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDnKut4q7Dg9lT%2FHgdVX8UrSLRiBPOGdAf0OhplbowwsgIhAI5r4DvUeVW62pdJ3JXMOXejjlDGqmgAiI1kPH9%2FEFjEKv8DCDQQABoMNjM3NDIzMTgzODA1Igxrgv64Xutw87vgde4q3ANiUyfyPZgJ6jE4A9Hk0DogvxYe8%2B0jY5MLI%2BXePxXbTQnLJz7j1FWbmtta8tSPnnE%2F8VKRZ%2Bsjbo02dYKQEF5C42HVKFykA2LB%2FPn2y6aVRuNjYJLc8gw48bHi6VW4whcFi9Xrksz8CXAqBM8W9DrUga%2BiqRY3pZtC5IEtO3QPSTFZjYlwDKtdydQEmIuPQggYVOMRktzog%2BvxcZKAWdHQVFebB%2F1YYMSugAL4sAQwK2pbMSywIchK0jZB9rDsB3ODigVkT8Tgmfd4nGDxlokCmMsG8PKldXXMMV%2FZM0NBsPpszLGPqjWZ94uLgWOCueIwtMoSFQy4SybJwTjNTNa%2B%2B1wlI9H59ovZMl%2Bf3oLzAs85DVTR0qrXlPs9BY1N9W2TVkn5EByccycn%2BqN42vB9BwOkM%2BqA77xXgC9LxAP1V7VER7tir2Tov%2F0UvulT6lihPSz%2BhE5SqI%2BmNUJ4FMcb4yLYIAhO0IClrJjK3zCpZNbRCfAWVDVzH9el%2FHE3TPkL6EKA8Jrtw3QAJAdcW40HIFJ%2F62A4pQtzQqkTIoq%2FXYXe752CTF1%2FiECjHAfHXruQd7uRG5SWrggkUB%2BerCDY4Sn23iGJiOwAFmJg%2Fj3232Q50tgSO0HNNigV5zCQvYm9BjqkAcBQhIwmONPvlgSikRWiol751Lo1XkHy63XVuTBeaKFT%2F6ZXXSBH%2FatTUFdcleQWNDjfKuSrP6LD4C8xEteCqfTnBpBD%2BcHT31EzkGY%2BIL1mgqx4NsShXJfGQ6LXrWnuyG3anAAHtts%2B1eLnqvAxnoUa0Di9nZ3D%2F526xrjJODc9p7X30ZAjT0CR1XW7abRo8PNw1ZbZY61%2BTE1BbISo3AmNvUQ8&X-Amz-Signature=103f08c35ef9e86c3297feea8b5527a949553ea79f99d8f7179a1894d5adf230&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZA7ZY7I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDnKut4q7Dg9lT%2FHgdVX8UrSLRiBPOGdAf0OhplbowwsgIhAI5r4DvUeVW62pdJ3JXMOXejjlDGqmgAiI1kPH9%2FEFjEKv8DCDQQABoMNjM3NDIzMTgzODA1Igxrgv64Xutw87vgde4q3ANiUyfyPZgJ6jE4A9Hk0DogvxYe8%2B0jY5MLI%2BXePxXbTQnLJz7j1FWbmtta8tSPnnE%2F8VKRZ%2Bsjbo02dYKQEF5C42HVKFykA2LB%2FPn2y6aVRuNjYJLc8gw48bHi6VW4whcFi9Xrksz8CXAqBM8W9DrUga%2BiqRY3pZtC5IEtO3QPSTFZjYlwDKtdydQEmIuPQggYVOMRktzog%2BvxcZKAWdHQVFebB%2F1YYMSugAL4sAQwK2pbMSywIchK0jZB9rDsB3ODigVkT8Tgmfd4nGDxlokCmMsG8PKldXXMMV%2FZM0NBsPpszLGPqjWZ94uLgWOCueIwtMoSFQy4SybJwTjNTNa%2B%2B1wlI9H59ovZMl%2Bf3oLzAs85DVTR0qrXlPs9BY1N9W2TVkn5EByccycn%2BqN42vB9BwOkM%2BqA77xXgC9LxAP1V7VER7tir2Tov%2F0UvulT6lihPSz%2BhE5SqI%2BmNUJ4FMcb4yLYIAhO0IClrJjK3zCpZNbRCfAWVDVzH9el%2FHE3TPkL6EKA8Jrtw3QAJAdcW40HIFJ%2F62A4pQtzQqkTIoq%2FXYXe752CTF1%2FiECjHAfHXruQd7uRG5SWrggkUB%2BerCDY4Sn23iGJiOwAFmJg%2Fj3232Q50tgSO0HNNigV5zCQvYm9BjqkAcBQhIwmONPvlgSikRWiol751Lo1XkHy63XVuTBeaKFT%2F6ZXXSBH%2FatTUFdcleQWNDjfKuSrP6LD4C8xEteCqfTnBpBD%2BcHT31EzkGY%2BIL1mgqx4NsShXJfGQ6LXrWnuyG3anAAHtts%2B1eLnqvAxnoUa0Di9nZ3D%2F526xrjJODc9p7X30ZAjT0CR1XW7abRo8PNw1ZbZY61%2BTE1BbISo3AmNvUQ8&X-Amz-Signature=25458bfefd710f9cd2de86591f2dedf76e17920a1e06d1fa1a2046e80235aa93&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZA7ZY7I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDnKut4q7Dg9lT%2FHgdVX8UrSLRiBPOGdAf0OhplbowwsgIhAI5r4DvUeVW62pdJ3JXMOXejjlDGqmgAiI1kPH9%2FEFjEKv8DCDQQABoMNjM3NDIzMTgzODA1Igxrgv64Xutw87vgde4q3ANiUyfyPZgJ6jE4A9Hk0DogvxYe8%2B0jY5MLI%2BXePxXbTQnLJz7j1FWbmtta8tSPnnE%2F8VKRZ%2Bsjbo02dYKQEF5C42HVKFykA2LB%2FPn2y6aVRuNjYJLc8gw48bHi6VW4whcFi9Xrksz8CXAqBM8W9DrUga%2BiqRY3pZtC5IEtO3QPSTFZjYlwDKtdydQEmIuPQggYVOMRktzog%2BvxcZKAWdHQVFebB%2F1YYMSugAL4sAQwK2pbMSywIchK0jZB9rDsB3ODigVkT8Tgmfd4nGDxlokCmMsG8PKldXXMMV%2FZM0NBsPpszLGPqjWZ94uLgWOCueIwtMoSFQy4SybJwTjNTNa%2B%2B1wlI9H59ovZMl%2Bf3oLzAs85DVTR0qrXlPs9BY1N9W2TVkn5EByccycn%2BqN42vB9BwOkM%2BqA77xXgC9LxAP1V7VER7tir2Tov%2F0UvulT6lihPSz%2BhE5SqI%2BmNUJ4FMcb4yLYIAhO0IClrJjK3zCpZNbRCfAWVDVzH9el%2FHE3TPkL6EKA8Jrtw3QAJAdcW40HIFJ%2F62A4pQtzQqkTIoq%2FXYXe752CTF1%2FiECjHAfHXruQd7uRG5SWrggkUB%2BerCDY4Sn23iGJiOwAFmJg%2Fj3232Q50tgSO0HNNigV5zCQvYm9BjqkAcBQhIwmONPvlgSikRWiol751Lo1XkHy63XVuTBeaKFT%2F6ZXXSBH%2FatTUFdcleQWNDjfKuSrP6LD4C8xEteCqfTnBpBD%2BcHT31EzkGY%2BIL1mgqx4NsShXJfGQ6LXrWnuyG3anAAHtts%2B1eLnqvAxnoUa0Di9nZ3D%2F526xrjJODc9p7X30ZAjT0CR1XW7abRo8PNw1ZbZY61%2BTE1BbISo3AmNvUQ8&X-Amz-Signature=8a62e11daef992ddb115bae315d9b9ece93c35a52b3f27922a63892070586a1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZA7ZY7I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDnKut4q7Dg9lT%2FHgdVX8UrSLRiBPOGdAf0OhplbowwsgIhAI5r4DvUeVW62pdJ3JXMOXejjlDGqmgAiI1kPH9%2FEFjEKv8DCDQQABoMNjM3NDIzMTgzODA1Igxrgv64Xutw87vgde4q3ANiUyfyPZgJ6jE4A9Hk0DogvxYe8%2B0jY5MLI%2BXePxXbTQnLJz7j1FWbmtta8tSPnnE%2F8VKRZ%2Bsjbo02dYKQEF5C42HVKFykA2LB%2FPn2y6aVRuNjYJLc8gw48bHi6VW4whcFi9Xrksz8CXAqBM8W9DrUga%2BiqRY3pZtC5IEtO3QPSTFZjYlwDKtdydQEmIuPQggYVOMRktzog%2BvxcZKAWdHQVFebB%2F1YYMSugAL4sAQwK2pbMSywIchK0jZB9rDsB3ODigVkT8Tgmfd4nGDxlokCmMsG8PKldXXMMV%2FZM0NBsPpszLGPqjWZ94uLgWOCueIwtMoSFQy4SybJwTjNTNa%2B%2B1wlI9H59ovZMl%2Bf3oLzAs85DVTR0qrXlPs9BY1N9W2TVkn5EByccycn%2BqN42vB9BwOkM%2BqA77xXgC9LxAP1V7VER7tir2Tov%2F0UvulT6lihPSz%2BhE5SqI%2BmNUJ4FMcb4yLYIAhO0IClrJjK3zCpZNbRCfAWVDVzH9el%2FHE3TPkL6EKA8Jrtw3QAJAdcW40HIFJ%2F62A4pQtzQqkTIoq%2FXYXe752CTF1%2FiECjHAfHXruQd7uRG5SWrggkUB%2BerCDY4Sn23iGJiOwAFmJg%2Fj3232Q50tgSO0HNNigV5zCQvYm9BjqkAcBQhIwmONPvlgSikRWiol751Lo1XkHy63XVuTBeaKFT%2F6ZXXSBH%2FatTUFdcleQWNDjfKuSrP6LD4C8xEteCqfTnBpBD%2BcHT31EzkGY%2BIL1mgqx4NsShXJfGQ6LXrWnuyG3anAAHtts%2B1eLnqvAxnoUa0Di9nZ3D%2F526xrjJODc9p7X30ZAjT0CR1XW7abRo8PNw1ZbZY61%2BTE1BbISo3AmNvUQ8&X-Amz-Signature=583b61eec80eb2aefdbdee1e5d2b043711036a4c4ba029dbaef6b49dd583672b&X-Amz-SignedHeaders=host&x-id=GetObject)
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


