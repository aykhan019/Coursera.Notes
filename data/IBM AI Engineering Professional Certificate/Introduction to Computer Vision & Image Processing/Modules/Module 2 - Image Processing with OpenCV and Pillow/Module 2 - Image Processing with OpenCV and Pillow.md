

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UKMCJYH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDUKV5uEEFt%2BeN1X%2F1BmWRhC6G6UrIg6YKzzYTmgaZ53AIgMiDxCMnoG39F0H3fsv3EE9Q1c7Gk9ndkz2EiuqrLh2Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDzbgjWaV5vyHELf0ircAx%2FGIgHdeY9IxR42JsWLo8GEpFWMcJqcQ6T%2FnMf2vUuHKkjQLNoIwD3dCXgEoQ4cN9qaWhQU2Jt8rpRKtXfhovyIDNMzXTrkgv7GANNs5TkPjobCVRUWCsi6%2BlNs2SwnQ1E2SM7Lhi35CpXE8rQVTFrjppyybr6xLne5U3mI7Gz4%2FXj9h7iqdHLh%2BEx5JsEx2Thg5mOgkasmXeD%2FNnKcSYLq6xGqDk%2Fw6pdf6%2FDDn57Er5LF957un5lKHqrt7m7qd2Z9zFNM3gCIwuX8sBE0weu84XEGPB2DCLKe9FUUc1BPY4YD1b5I%2FVXPh5jDj3r7bCSrck%2FR2K8Xmi%2FB25ddYuFhM%2BEWCh8bmVggecH6eIYpCbcLLvy5ZM677jRugedJDBilMwqtdkEjl1Obp%2BeYNWBKzJBzVwNW%2BeeJypyFcdbxEr0wagWtPdAy6hyznGIDJwYMeNsJ7X29Kg6JTOt4oOBqjIX4qovhL15IFLYAk9FrcFakPJjr7mMZc0eSfPELWgsM953lYQeEa%2Byk%2BnuoA8Y28dDg9OYgMpFJ7TVUm7dKz4PHw0p7eul%2B4aYVIPyK1ancaDMrPkOtY2TSHFP7Leue5T%2FFugmhOaeaQBWdnoP65jUlNZKvA4tGWWCmMKOalb0GOqUBTT0mq0sjYamZ3N%2FY4TXfIa0FM1uDtfC08Rvjw0xnAgROut%2FUJsQ27ppmt0ssgj26QvB01NMj4LBpQwGbhOGx2132qAuJ2kHI6zueChZygZ7dOgkYFmFXkD6Bja01QnJ81xpO8X9nLfUAT%2BqUgvzhRo2O9qv3z1RXjZxbzKgSqSznpS3JKG2lwoYy63vEnY%2FGhpMcCjz6oQgwEDqHxIR7LctdkZdf&X-Amz-Signature=db733e8d100472e441ba6556dba2a451320f350db8b28b4f18ef9e8f8d433894&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C2NUCJ2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCysTbpx3%2BuXzXhGMlgsDJZiE6itkXXvXHdAJUxVT%2FMkwIhAPQQ2SV0Hhk7IkEPhSkIjbqYgT%2BTfJRuO%2BwRvo0cdT8hKv8DCGkQABoMNjM3NDIzMTgzODA1IgwL3REg1xfvUFNjoTkq3AOkCA4BlG2vmqSqfd85n9VKAr%2FdrBd0%2FjejyqwEgyr7j1SjHOmT99V9QHaqg156gCBcL6TEzi4VHelT%2BB%2Bg117W0KR7LyLL7WYh3FCe9ZPmY1LXW3We0Dnoqr6q%2BpY8RAZthobvzPN8c9loZ7jaw4hjAeace9jiFzH7Iwu477Smy1tv627PjRk2%2FidX0cVOec%2BtMUqNM%2F0ebCun2S%2BOr9vnQrmoUMGCTa4wP1EAU8YSYm0UwROyomgHfN6q%2FcT6snGSYhAgfGChvmaftBW1pLkXrTqtqnNhUABSDdvim6RjGvmXsNsD296b35Z2DVpxKceBqCG89fxLfWh0kN2abBXHYsytLlRQ9djcytD0bvP0pNIXKajBv6MgQ5nHNctD%2Ft1yBIiW6Qv%2F62EdfauldmOtzET%2BEzWmoAxTbZYEsDXQApoZKXtoLHTVwn9Y3UwFgTiNq%2FOivjpgPirPt77rPl7cfuPrMTAx28yreEF8mwr%2B1kBCCjnvhW7JdE3r6EcEbQXlIGVYuOPfAobHIGpj9eyJ1wQ%2FNFmzHDgOyN0X92fKv1t71wroVGtK1pCi61luMUWQHqUqOHdsJQfK3DqHTWIbSllclDUSfRi%2BLR99MgtUcwI68KXQdmA6mCpTVzCOmpW9BjqkAT6Eah6R%2FtaK8SPP8nvOwMrI9zjw8CH%2B67a89bYVVs3vy9sPpN1lnZh8tFqRj87RZGn%2FhLvRqxzFLVTIp%2BdQy9UP8sRaiqQU3sfX2jRRAjgjqXkp4M%2FTN7czqgtOjh4Xv1K%2BJxbynl7MUoOJJKuu%2BQ18e0YvpNwmt0X15CRHg5sS22DgMqM8wQRtZtCVGHrt2bAM9gbi%2FOiEZklg27EGpyLpcwin&X-Amz-Signature=ee6ae1a4356c3fb961ab8e0026213725506e4a7bdf2e179afbce214b17ecc62f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C2NUCJ2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCysTbpx3%2BuXzXhGMlgsDJZiE6itkXXvXHdAJUxVT%2FMkwIhAPQQ2SV0Hhk7IkEPhSkIjbqYgT%2BTfJRuO%2BwRvo0cdT8hKv8DCGkQABoMNjM3NDIzMTgzODA1IgwL3REg1xfvUFNjoTkq3AOkCA4BlG2vmqSqfd85n9VKAr%2FdrBd0%2FjejyqwEgyr7j1SjHOmT99V9QHaqg156gCBcL6TEzi4VHelT%2BB%2Bg117W0KR7LyLL7WYh3FCe9ZPmY1LXW3We0Dnoqr6q%2BpY8RAZthobvzPN8c9loZ7jaw4hjAeace9jiFzH7Iwu477Smy1tv627PjRk2%2FidX0cVOec%2BtMUqNM%2F0ebCun2S%2BOr9vnQrmoUMGCTa4wP1EAU8YSYm0UwROyomgHfN6q%2FcT6snGSYhAgfGChvmaftBW1pLkXrTqtqnNhUABSDdvim6RjGvmXsNsD296b35Z2DVpxKceBqCG89fxLfWh0kN2abBXHYsytLlRQ9djcytD0bvP0pNIXKajBv6MgQ5nHNctD%2Ft1yBIiW6Qv%2F62EdfauldmOtzET%2BEzWmoAxTbZYEsDXQApoZKXtoLHTVwn9Y3UwFgTiNq%2FOivjpgPirPt77rPl7cfuPrMTAx28yreEF8mwr%2B1kBCCjnvhW7JdE3r6EcEbQXlIGVYuOPfAobHIGpj9eyJ1wQ%2FNFmzHDgOyN0X92fKv1t71wroVGtK1pCi61luMUWQHqUqOHdsJQfK3DqHTWIbSllclDUSfRi%2BLR99MgtUcwI68KXQdmA6mCpTVzCOmpW9BjqkAT6Eah6R%2FtaK8SPP8nvOwMrI9zjw8CH%2B67a89bYVVs3vy9sPpN1lnZh8tFqRj87RZGn%2FhLvRqxzFLVTIp%2BdQy9UP8sRaiqQU3sfX2jRRAjgjqXkp4M%2FTN7czqgtOjh4Xv1K%2BJxbynl7MUoOJJKuu%2BQ18e0YvpNwmt0X15CRHg5sS22DgMqM8wQRtZtCVGHrt2bAM9gbi%2FOiEZklg27EGpyLpcwin&X-Amz-Signature=724317b4760239497161cb4b22e21c8a169384fdad46e32fc32909ee982aa3cf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C2NUCJ2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCysTbpx3%2BuXzXhGMlgsDJZiE6itkXXvXHdAJUxVT%2FMkwIhAPQQ2SV0Hhk7IkEPhSkIjbqYgT%2BTfJRuO%2BwRvo0cdT8hKv8DCGkQABoMNjM3NDIzMTgzODA1IgwL3REg1xfvUFNjoTkq3AOkCA4BlG2vmqSqfd85n9VKAr%2FdrBd0%2FjejyqwEgyr7j1SjHOmT99V9QHaqg156gCBcL6TEzi4VHelT%2BB%2Bg117W0KR7LyLL7WYh3FCe9ZPmY1LXW3We0Dnoqr6q%2BpY8RAZthobvzPN8c9loZ7jaw4hjAeace9jiFzH7Iwu477Smy1tv627PjRk2%2FidX0cVOec%2BtMUqNM%2F0ebCun2S%2BOr9vnQrmoUMGCTa4wP1EAU8YSYm0UwROyomgHfN6q%2FcT6snGSYhAgfGChvmaftBW1pLkXrTqtqnNhUABSDdvim6RjGvmXsNsD296b35Z2DVpxKceBqCG89fxLfWh0kN2abBXHYsytLlRQ9djcytD0bvP0pNIXKajBv6MgQ5nHNctD%2Ft1yBIiW6Qv%2F62EdfauldmOtzET%2BEzWmoAxTbZYEsDXQApoZKXtoLHTVwn9Y3UwFgTiNq%2FOivjpgPirPt77rPl7cfuPrMTAx28yreEF8mwr%2B1kBCCjnvhW7JdE3r6EcEbQXlIGVYuOPfAobHIGpj9eyJ1wQ%2FNFmzHDgOyN0X92fKv1t71wroVGtK1pCi61luMUWQHqUqOHdsJQfK3DqHTWIbSllclDUSfRi%2BLR99MgtUcwI68KXQdmA6mCpTVzCOmpW9BjqkAT6Eah6R%2FtaK8SPP8nvOwMrI9zjw8CH%2B67a89bYVVs3vy9sPpN1lnZh8tFqRj87RZGn%2FhLvRqxzFLVTIp%2BdQy9UP8sRaiqQU3sfX2jRRAjgjqXkp4M%2FTN7czqgtOjh4Xv1K%2BJxbynl7MUoOJJKuu%2BQ18e0YvpNwmt0X15CRHg5sS22DgMqM8wQRtZtCVGHrt2bAM9gbi%2FOiEZklg27EGpyLpcwin&X-Amz-Signature=4864295281ca9eb3aa7213c631a202de9b51a9661da176c95ee26053fafef2d4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C2NUCJ2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCysTbpx3%2BuXzXhGMlgsDJZiE6itkXXvXHdAJUxVT%2FMkwIhAPQQ2SV0Hhk7IkEPhSkIjbqYgT%2BTfJRuO%2BwRvo0cdT8hKv8DCGkQABoMNjM3NDIzMTgzODA1IgwL3REg1xfvUFNjoTkq3AOkCA4BlG2vmqSqfd85n9VKAr%2FdrBd0%2FjejyqwEgyr7j1SjHOmT99V9QHaqg156gCBcL6TEzi4VHelT%2BB%2Bg117W0KR7LyLL7WYh3FCe9ZPmY1LXW3We0Dnoqr6q%2BpY8RAZthobvzPN8c9loZ7jaw4hjAeace9jiFzH7Iwu477Smy1tv627PjRk2%2FidX0cVOec%2BtMUqNM%2F0ebCun2S%2BOr9vnQrmoUMGCTa4wP1EAU8YSYm0UwROyomgHfN6q%2FcT6snGSYhAgfGChvmaftBW1pLkXrTqtqnNhUABSDdvim6RjGvmXsNsD296b35Z2DVpxKceBqCG89fxLfWh0kN2abBXHYsytLlRQ9djcytD0bvP0pNIXKajBv6MgQ5nHNctD%2Ft1yBIiW6Qv%2F62EdfauldmOtzET%2BEzWmoAxTbZYEsDXQApoZKXtoLHTVwn9Y3UwFgTiNq%2FOivjpgPirPt77rPl7cfuPrMTAx28yreEF8mwr%2B1kBCCjnvhW7JdE3r6EcEbQXlIGVYuOPfAobHIGpj9eyJ1wQ%2FNFmzHDgOyN0X92fKv1t71wroVGtK1pCi61luMUWQHqUqOHdsJQfK3DqHTWIbSllclDUSfRi%2BLR99MgtUcwI68KXQdmA6mCpTVzCOmpW9BjqkAT6Eah6R%2FtaK8SPP8nvOwMrI9zjw8CH%2B67a89bYVVs3vy9sPpN1lnZh8tFqRj87RZGn%2FhLvRqxzFLVTIp%2BdQy9UP8sRaiqQU3sfX2jRRAjgjqXkp4M%2FTN7czqgtOjh4Xv1K%2BJxbynl7MUoOJJKuu%2BQ18e0YvpNwmt0X15CRHg5sS22DgMqM8wQRtZtCVGHrt2bAM9gbi%2FOiEZklg27EGpyLpcwin&X-Amz-Signature=099caa3038006f71db8d87c90274a2274fdd83f86b9e686f1d1be37ca8876ed5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C2NUCJ2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCysTbpx3%2BuXzXhGMlgsDJZiE6itkXXvXHdAJUxVT%2FMkwIhAPQQ2SV0Hhk7IkEPhSkIjbqYgT%2BTfJRuO%2BwRvo0cdT8hKv8DCGkQABoMNjM3NDIzMTgzODA1IgwL3REg1xfvUFNjoTkq3AOkCA4BlG2vmqSqfd85n9VKAr%2FdrBd0%2FjejyqwEgyr7j1SjHOmT99V9QHaqg156gCBcL6TEzi4VHelT%2BB%2Bg117W0KR7LyLL7WYh3FCe9ZPmY1LXW3We0Dnoqr6q%2BpY8RAZthobvzPN8c9loZ7jaw4hjAeace9jiFzH7Iwu477Smy1tv627PjRk2%2FidX0cVOec%2BtMUqNM%2F0ebCun2S%2BOr9vnQrmoUMGCTa4wP1EAU8YSYm0UwROyomgHfN6q%2FcT6snGSYhAgfGChvmaftBW1pLkXrTqtqnNhUABSDdvim6RjGvmXsNsD296b35Z2DVpxKceBqCG89fxLfWh0kN2abBXHYsytLlRQ9djcytD0bvP0pNIXKajBv6MgQ5nHNctD%2Ft1yBIiW6Qv%2F62EdfauldmOtzET%2BEzWmoAxTbZYEsDXQApoZKXtoLHTVwn9Y3UwFgTiNq%2FOivjpgPirPt77rPl7cfuPrMTAx28yreEF8mwr%2B1kBCCjnvhW7JdE3r6EcEbQXlIGVYuOPfAobHIGpj9eyJ1wQ%2FNFmzHDgOyN0X92fKv1t71wroVGtK1pCi61luMUWQHqUqOHdsJQfK3DqHTWIbSllclDUSfRi%2BLR99MgtUcwI68KXQdmA6mCpTVzCOmpW9BjqkAT6Eah6R%2FtaK8SPP8nvOwMrI9zjw8CH%2B67a89bYVVs3vy9sPpN1lnZh8tFqRj87RZGn%2FhLvRqxzFLVTIp%2BdQy9UP8sRaiqQU3sfX2jRRAjgjqXkp4M%2FTN7czqgtOjh4Xv1K%2BJxbynl7MUoOJJKuu%2BQ18e0YvpNwmt0X15CRHg5sS22DgMqM8wQRtZtCVGHrt2bAM9gbi%2FOiEZklg27EGpyLpcwin&X-Amz-Signature=9fd88ef8f863d069d798aee88ef909bfa33e12d7e0deab1c4f8fe2e74ee3f4b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UKMCJYH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDUKV5uEEFt%2BeN1X%2F1BmWRhC6G6UrIg6YKzzYTmgaZ53AIgMiDxCMnoG39F0H3fsv3EE9Q1c7Gk9ndkz2EiuqrLh2Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDzbgjWaV5vyHELf0ircAx%2FGIgHdeY9IxR42JsWLo8GEpFWMcJqcQ6T%2FnMf2vUuHKkjQLNoIwD3dCXgEoQ4cN9qaWhQU2Jt8rpRKtXfhovyIDNMzXTrkgv7GANNs5TkPjobCVRUWCsi6%2BlNs2SwnQ1E2SM7Lhi35CpXE8rQVTFrjppyybr6xLne5U3mI7Gz4%2FXj9h7iqdHLh%2BEx5JsEx2Thg5mOgkasmXeD%2FNnKcSYLq6xGqDk%2Fw6pdf6%2FDDn57Er5LF957un5lKHqrt7m7qd2Z9zFNM3gCIwuX8sBE0weu84XEGPB2DCLKe9FUUc1BPY4YD1b5I%2FVXPh5jDj3r7bCSrck%2FR2K8Xmi%2FB25ddYuFhM%2BEWCh8bmVggecH6eIYpCbcLLvy5ZM677jRugedJDBilMwqtdkEjl1Obp%2BeYNWBKzJBzVwNW%2BeeJypyFcdbxEr0wagWtPdAy6hyznGIDJwYMeNsJ7X29Kg6JTOt4oOBqjIX4qovhL15IFLYAk9FrcFakPJjr7mMZc0eSfPELWgsM953lYQeEa%2Byk%2BnuoA8Y28dDg9OYgMpFJ7TVUm7dKz4PHw0p7eul%2B4aYVIPyK1ancaDMrPkOtY2TSHFP7Leue5T%2FFugmhOaeaQBWdnoP65jUlNZKvA4tGWWCmMKOalb0GOqUBTT0mq0sjYamZ3N%2FY4TXfIa0FM1uDtfC08Rvjw0xnAgROut%2FUJsQ27ppmt0ssgj26QvB01NMj4LBpQwGbhOGx2132qAuJ2kHI6zueChZygZ7dOgkYFmFXkD6Bja01QnJ81xpO8X9nLfUAT%2BqUgvzhRo2O9qv3z1RXjZxbzKgSqSznpS3JKG2lwoYy63vEnY%2FGhpMcCjz6oQgwEDqHxIR7LctdkZdf&X-Amz-Signature=038277e3831bb0ef0abc62d80698212a42585e8885ffc8816782f0eb3e4475d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UKMCJYH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDUKV5uEEFt%2BeN1X%2F1BmWRhC6G6UrIg6YKzzYTmgaZ53AIgMiDxCMnoG39F0H3fsv3EE9Q1c7Gk9ndkz2EiuqrLh2Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDzbgjWaV5vyHELf0ircAx%2FGIgHdeY9IxR42JsWLo8GEpFWMcJqcQ6T%2FnMf2vUuHKkjQLNoIwD3dCXgEoQ4cN9qaWhQU2Jt8rpRKtXfhovyIDNMzXTrkgv7GANNs5TkPjobCVRUWCsi6%2BlNs2SwnQ1E2SM7Lhi35CpXE8rQVTFrjppyybr6xLne5U3mI7Gz4%2FXj9h7iqdHLh%2BEx5JsEx2Thg5mOgkasmXeD%2FNnKcSYLq6xGqDk%2Fw6pdf6%2FDDn57Er5LF957un5lKHqrt7m7qd2Z9zFNM3gCIwuX8sBE0weu84XEGPB2DCLKe9FUUc1BPY4YD1b5I%2FVXPh5jDj3r7bCSrck%2FR2K8Xmi%2FB25ddYuFhM%2BEWCh8bmVggecH6eIYpCbcLLvy5ZM677jRugedJDBilMwqtdkEjl1Obp%2BeYNWBKzJBzVwNW%2BeeJypyFcdbxEr0wagWtPdAy6hyznGIDJwYMeNsJ7X29Kg6JTOt4oOBqjIX4qovhL15IFLYAk9FrcFakPJjr7mMZc0eSfPELWgsM953lYQeEa%2Byk%2BnuoA8Y28dDg9OYgMpFJ7TVUm7dKz4PHw0p7eul%2B4aYVIPyK1ancaDMrPkOtY2TSHFP7Leue5T%2FFugmhOaeaQBWdnoP65jUlNZKvA4tGWWCmMKOalb0GOqUBTT0mq0sjYamZ3N%2FY4TXfIa0FM1uDtfC08Rvjw0xnAgROut%2FUJsQ27ppmt0ssgj26QvB01NMj4LBpQwGbhOGx2132qAuJ2kHI6zueChZygZ7dOgkYFmFXkD6Bja01QnJ81xpO8X9nLfUAT%2BqUgvzhRo2O9qv3z1RXjZxbzKgSqSznpS3JKG2lwoYy63vEnY%2FGhpMcCjz6oQgwEDqHxIR7LctdkZdf&X-Amz-Signature=5c91a3f350556e51e8fcc0a23f99fe0ed71e94a7e92327caf3431e4b16202f1c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UKMCJYH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDUKV5uEEFt%2BeN1X%2F1BmWRhC6G6UrIg6YKzzYTmgaZ53AIgMiDxCMnoG39F0H3fsv3EE9Q1c7Gk9ndkz2EiuqrLh2Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDzbgjWaV5vyHELf0ircAx%2FGIgHdeY9IxR42JsWLo8GEpFWMcJqcQ6T%2FnMf2vUuHKkjQLNoIwD3dCXgEoQ4cN9qaWhQU2Jt8rpRKtXfhovyIDNMzXTrkgv7GANNs5TkPjobCVRUWCsi6%2BlNs2SwnQ1E2SM7Lhi35CpXE8rQVTFrjppyybr6xLne5U3mI7Gz4%2FXj9h7iqdHLh%2BEx5JsEx2Thg5mOgkasmXeD%2FNnKcSYLq6xGqDk%2Fw6pdf6%2FDDn57Er5LF957un5lKHqrt7m7qd2Z9zFNM3gCIwuX8sBE0weu84XEGPB2DCLKe9FUUc1BPY4YD1b5I%2FVXPh5jDj3r7bCSrck%2FR2K8Xmi%2FB25ddYuFhM%2BEWCh8bmVggecH6eIYpCbcLLvy5ZM677jRugedJDBilMwqtdkEjl1Obp%2BeYNWBKzJBzVwNW%2BeeJypyFcdbxEr0wagWtPdAy6hyznGIDJwYMeNsJ7X29Kg6JTOt4oOBqjIX4qovhL15IFLYAk9FrcFakPJjr7mMZc0eSfPELWgsM953lYQeEa%2Byk%2BnuoA8Y28dDg9OYgMpFJ7TVUm7dKz4PHw0p7eul%2B4aYVIPyK1ancaDMrPkOtY2TSHFP7Leue5T%2FFugmhOaeaQBWdnoP65jUlNZKvA4tGWWCmMKOalb0GOqUBTT0mq0sjYamZ3N%2FY4TXfIa0FM1uDtfC08Rvjw0xnAgROut%2FUJsQ27ppmt0ssgj26QvB01NMj4LBpQwGbhOGx2132qAuJ2kHI6zueChZygZ7dOgkYFmFXkD6Bja01QnJ81xpO8X9nLfUAT%2BqUgvzhRo2O9qv3z1RXjZxbzKgSqSznpS3JKG2lwoYy63vEnY%2FGhpMcCjz6oQgwEDqHxIR7LctdkZdf&X-Amz-Signature=abbbcacdd9d793fa2a5fb039204f6346b17e59d7b84770709e47038f66b7a327&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UKMCJYH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDUKV5uEEFt%2BeN1X%2F1BmWRhC6G6UrIg6YKzzYTmgaZ53AIgMiDxCMnoG39F0H3fsv3EE9Q1c7Gk9ndkz2EiuqrLh2Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDzbgjWaV5vyHELf0ircAx%2FGIgHdeY9IxR42JsWLo8GEpFWMcJqcQ6T%2FnMf2vUuHKkjQLNoIwD3dCXgEoQ4cN9qaWhQU2Jt8rpRKtXfhovyIDNMzXTrkgv7GANNs5TkPjobCVRUWCsi6%2BlNs2SwnQ1E2SM7Lhi35CpXE8rQVTFrjppyybr6xLne5U3mI7Gz4%2FXj9h7iqdHLh%2BEx5JsEx2Thg5mOgkasmXeD%2FNnKcSYLq6xGqDk%2Fw6pdf6%2FDDn57Er5LF957un5lKHqrt7m7qd2Z9zFNM3gCIwuX8sBE0weu84XEGPB2DCLKe9FUUc1BPY4YD1b5I%2FVXPh5jDj3r7bCSrck%2FR2K8Xmi%2FB25ddYuFhM%2BEWCh8bmVggecH6eIYpCbcLLvy5ZM677jRugedJDBilMwqtdkEjl1Obp%2BeYNWBKzJBzVwNW%2BeeJypyFcdbxEr0wagWtPdAy6hyznGIDJwYMeNsJ7X29Kg6JTOt4oOBqjIX4qovhL15IFLYAk9FrcFakPJjr7mMZc0eSfPELWgsM953lYQeEa%2Byk%2BnuoA8Y28dDg9OYgMpFJ7TVUm7dKz4PHw0p7eul%2B4aYVIPyK1ancaDMrPkOtY2TSHFP7Leue5T%2FFugmhOaeaQBWdnoP65jUlNZKvA4tGWWCmMKOalb0GOqUBTT0mq0sjYamZ3N%2FY4TXfIa0FM1uDtfC08Rvjw0xnAgROut%2FUJsQ27ppmt0ssgj26QvB01NMj4LBpQwGbhOGx2132qAuJ2kHI6zueChZygZ7dOgkYFmFXkD6Bja01QnJ81xpO8X9nLfUAT%2BqUgvzhRo2O9qv3z1RXjZxbzKgSqSznpS3JKG2lwoYy63vEnY%2FGhpMcCjz6oQgwEDqHxIR7LctdkZdf&X-Amz-Signature=6dc5fd5ff03de3a2df5accb70d2058a7969c5fef1da2bf65f3c89b7464e18389&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UKMCJYH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDUKV5uEEFt%2BeN1X%2F1BmWRhC6G6UrIg6YKzzYTmgaZ53AIgMiDxCMnoG39F0H3fsv3EE9Q1c7Gk9ndkz2EiuqrLh2Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDzbgjWaV5vyHELf0ircAx%2FGIgHdeY9IxR42JsWLo8GEpFWMcJqcQ6T%2FnMf2vUuHKkjQLNoIwD3dCXgEoQ4cN9qaWhQU2Jt8rpRKtXfhovyIDNMzXTrkgv7GANNs5TkPjobCVRUWCsi6%2BlNs2SwnQ1E2SM7Lhi35CpXE8rQVTFrjppyybr6xLne5U3mI7Gz4%2FXj9h7iqdHLh%2BEx5JsEx2Thg5mOgkasmXeD%2FNnKcSYLq6xGqDk%2Fw6pdf6%2FDDn57Er5LF957un5lKHqrt7m7qd2Z9zFNM3gCIwuX8sBE0weu84XEGPB2DCLKe9FUUc1BPY4YD1b5I%2FVXPh5jDj3r7bCSrck%2FR2K8Xmi%2FB25ddYuFhM%2BEWCh8bmVggecH6eIYpCbcLLvy5ZM677jRugedJDBilMwqtdkEjl1Obp%2BeYNWBKzJBzVwNW%2BeeJypyFcdbxEr0wagWtPdAy6hyznGIDJwYMeNsJ7X29Kg6JTOt4oOBqjIX4qovhL15IFLYAk9FrcFakPJjr7mMZc0eSfPELWgsM953lYQeEa%2Byk%2BnuoA8Y28dDg9OYgMpFJ7TVUm7dKz4PHw0p7eul%2B4aYVIPyK1ancaDMrPkOtY2TSHFP7Leue5T%2FFugmhOaeaQBWdnoP65jUlNZKvA4tGWWCmMKOalb0GOqUBTT0mq0sjYamZ3N%2FY4TXfIa0FM1uDtfC08Rvjw0xnAgROut%2FUJsQ27ppmt0ssgj26QvB01NMj4LBpQwGbhOGx2132qAuJ2kHI6zueChZygZ7dOgkYFmFXkD6Bja01QnJ81xpO8X9nLfUAT%2BqUgvzhRo2O9qv3z1RXjZxbzKgSqSznpS3JKG2lwoYy63vEnY%2FGhpMcCjz6oQgwEDqHxIR7LctdkZdf&X-Amz-Signature=7c04f9265dac586b471c0de891a59be6f5738285647105bb66c9f0a44076a062&X-Amz-SignedHeaders=host&x-id=GetObject)
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


