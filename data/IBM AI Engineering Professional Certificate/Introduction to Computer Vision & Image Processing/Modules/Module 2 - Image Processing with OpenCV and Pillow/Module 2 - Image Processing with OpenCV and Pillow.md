

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZWXJXOA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqvaH32NXjvRnPU5Ou%2B4kcyZb9sV64GFY5iOyX7PPAHwIhAOry%2FVCp0fLOwoWGJusytaLoustjsf1K2B55tJ8xeOiuKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4r5jQdvNbFsycjrYq3ANP57Rfedn1XQdCjAXZxFKVzzZzxdbmy1FdQWbuq0SZy7mmtDos66T0qxI%2BzqYS3j38fhmOKJg0%2Fd6evcwzozPQk6XKnMghmmpMHbwL7py5liZBBiniUw3NKSCBrIAFcldwJqM6s7orjVbdMEmTmfp3Ry3XCWWVAb7k9GRqEYSkX7cqTNVlMMCD%2BVlrDPnicX83QSqdeimMxtGFBQq1izsYDPBN04l9Hq5lISjX00saenZjTq%2FhXIFOnxIR8vqwhhOaKyMhRJcmQrHT9ememL0vJW7ReiE4gIbBDCGu%2FVi2F47yEDYVm4Q5Bj5IGUrN89oYqbhhMiv%2BxVhuU32DXywLO70P%2Br5dIFuatMUde%2FyCjdQKXRNnkWzIYlVt6w0US%2FsgE%2BXV9Wpy2opaTJS8m2XKhg1whpmQaWLD1rkMKcEeL%2BfnMYgpkQ%2FvUksIjRhugIPn2IuZrGomwmnhA8XWxinLEtJhmZLucKnqCir4bg4z8wDulkB08C9ogTyUMCWQNPVZaahMp%2BsOe7MWpX%2FRnTQB935rgwpWAVsIBpLG45yegqLS91LaoBuXT6OcghrkYyUDYETY4ErOOKldqt9S4y%2FqkNX1rBK2lEMZYERdowrjs1oiShVJF%2Fwh4WtZ8DDP1v68BjqkARpnoKBxAlw3lIeVXWVQJxjVKTjp5XhCTBq99XZDHxS4J1flokvQ2B0ZnaXhlJHH6UbWag6pgHuUIQw%2FFsE0PIVgAhThM38UqJMnUo6VSPADxpH4I4Qy0mIfZ35aCHsFegY6J7XqqB2yUbR2WIve44L%2BCPWP4P%2BuWXfOsLTKcxDXkPd4p%2FsvC0TZqo7Qjj%2B11cftC55ClOOeAL2Gq1Y2LqHl35e1&X-Amz-Signature=75e70ebe1eb1bb7a0ebc0f80883af8f2cac1a9bc9b94215643d013c780c44ce4&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PLAS2PE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQqZEryg25wF%2F1bhqru%2BKRBcWCOVQWwy5DEFiAxL9wdAiEAnuyzf5ZpVqJocmvqvpKMDCjWhJU%2FJv5bGyj3YtFjQxAqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKJW0HYXnO211R03%2BircAxLMhzMbmxPah85qtqbSD0xquLwUvd%2Bp10NcBHWSZ1NiunxiCE11BaNS3WLay0p5n%2BY5DdYKukW0HF8ozFJQ0gP6lkfZQJ88OBr6aF4g5crgu19UiKpz2j7Hngw6sFv%2BLkQ2wVTSK%2BrlLtY3uXyY6gZT51sduAQfjeQU4DaFTrdiN3IYA5OClbif6GN8SBfK01fljJS4U774vPXdNL8QFW6GCEA2FDYT%2F6J1ujYrPzdLLhnZRrz1DFiIQAoidQC7%2BjDcx79Ox9VSd0R2zRTVpcLSi38AMP9esjiiQsm5MBLOE%2BSm4xE5YbpgryZ0aRFNLTZhtCir9jqy70AzMUw797lyD7zN%2FfH0Hi406RrcgeekLj7bpTyg2D6trmZzhLosmJk7hsR27VSEKBTXweP3l%2BZ%2FdI8%2Bs%2FfdXzSC7x3TVE59YIyFPUAKEtXhJLwpnb3n2DT5vi72xUGIW7jiXAbTyTwdHnE7u8CZLwaKInkw7q1iuF8qEwEmOLlS7mwZiEHmSf76WTyHV8cETGgDuA%2FowPS1WE5Je0thx6uQIT02T%2FjaZ8qO9u97%2FtRa%2BeuTkveHe8BxKrTVV%2B8Haw3ZlDy60%2BPyA57cce9tcVYgAvS%2BUoy3hF5VlhmuiiYLiAN0MJDg%2FrwGOqUB14Dt0PU06aMyw3Y1bLrcBA7Na5HEWpE9CA5JyGnKWx5zOAsdNCfhbXWCGU%2Bm87db%2B7wBTeRi9ONxJgI29Oz%2B5ULhbuqSyA7eZHPVFF9YkW6gxWDNM0yJL4XGkukvShdYV9kz2LNxTgh0lstML%2FhXUt5HwNL5nbnGIB7NMHydm4tOJYg8H%2FKDGpJQPGkij8yaoUfVmRKcBGUZRBBneEWFtC7MN7xR&X-Amz-Signature=f92feadeedb932a155fb3a95c4355d4154ca3f6c557b02280b8df5fc18202a35&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PLAS2PE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQqZEryg25wF%2F1bhqru%2BKRBcWCOVQWwy5DEFiAxL9wdAiEAnuyzf5ZpVqJocmvqvpKMDCjWhJU%2FJv5bGyj3YtFjQxAqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKJW0HYXnO211R03%2BircAxLMhzMbmxPah85qtqbSD0xquLwUvd%2Bp10NcBHWSZ1NiunxiCE11BaNS3WLay0p5n%2BY5DdYKukW0HF8ozFJQ0gP6lkfZQJ88OBr6aF4g5crgu19UiKpz2j7Hngw6sFv%2BLkQ2wVTSK%2BrlLtY3uXyY6gZT51sduAQfjeQU4DaFTrdiN3IYA5OClbif6GN8SBfK01fljJS4U774vPXdNL8QFW6GCEA2FDYT%2F6J1ujYrPzdLLhnZRrz1DFiIQAoidQC7%2BjDcx79Ox9VSd0R2zRTVpcLSi38AMP9esjiiQsm5MBLOE%2BSm4xE5YbpgryZ0aRFNLTZhtCir9jqy70AzMUw797lyD7zN%2FfH0Hi406RrcgeekLj7bpTyg2D6trmZzhLosmJk7hsR27VSEKBTXweP3l%2BZ%2FdI8%2Bs%2FfdXzSC7x3TVE59YIyFPUAKEtXhJLwpnb3n2DT5vi72xUGIW7jiXAbTyTwdHnE7u8CZLwaKInkw7q1iuF8qEwEmOLlS7mwZiEHmSf76WTyHV8cETGgDuA%2FowPS1WE5Je0thx6uQIT02T%2FjaZ8qO9u97%2FtRa%2BeuTkveHe8BxKrTVV%2B8Haw3ZlDy60%2BPyA57cce9tcVYgAvS%2BUoy3hF5VlhmuiiYLiAN0MJDg%2FrwGOqUB14Dt0PU06aMyw3Y1bLrcBA7Na5HEWpE9CA5JyGnKWx5zOAsdNCfhbXWCGU%2Bm87db%2B7wBTeRi9ONxJgI29Oz%2B5ULhbuqSyA7eZHPVFF9YkW6gxWDNM0yJL4XGkukvShdYV9kz2LNxTgh0lstML%2FhXUt5HwNL5nbnGIB7NMHydm4tOJYg8H%2FKDGpJQPGkij8yaoUfVmRKcBGUZRBBneEWFtC7MN7xR&X-Amz-Signature=39f79e9e52110ee5cdf4fb109b1190de8b606425b117da87871cbb1dbe866f6d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PLAS2PE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQqZEryg25wF%2F1bhqru%2BKRBcWCOVQWwy5DEFiAxL9wdAiEAnuyzf5ZpVqJocmvqvpKMDCjWhJU%2FJv5bGyj3YtFjQxAqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKJW0HYXnO211R03%2BircAxLMhzMbmxPah85qtqbSD0xquLwUvd%2Bp10NcBHWSZ1NiunxiCE11BaNS3WLay0p5n%2BY5DdYKukW0HF8ozFJQ0gP6lkfZQJ88OBr6aF4g5crgu19UiKpz2j7Hngw6sFv%2BLkQ2wVTSK%2BrlLtY3uXyY6gZT51sduAQfjeQU4DaFTrdiN3IYA5OClbif6GN8SBfK01fljJS4U774vPXdNL8QFW6GCEA2FDYT%2F6J1ujYrPzdLLhnZRrz1DFiIQAoidQC7%2BjDcx79Ox9VSd0R2zRTVpcLSi38AMP9esjiiQsm5MBLOE%2BSm4xE5YbpgryZ0aRFNLTZhtCir9jqy70AzMUw797lyD7zN%2FfH0Hi406RrcgeekLj7bpTyg2D6trmZzhLosmJk7hsR27VSEKBTXweP3l%2BZ%2FdI8%2Bs%2FfdXzSC7x3TVE59YIyFPUAKEtXhJLwpnb3n2DT5vi72xUGIW7jiXAbTyTwdHnE7u8CZLwaKInkw7q1iuF8qEwEmOLlS7mwZiEHmSf76WTyHV8cETGgDuA%2FowPS1WE5Je0thx6uQIT02T%2FjaZ8qO9u97%2FtRa%2BeuTkveHe8BxKrTVV%2B8Haw3ZlDy60%2BPyA57cce9tcVYgAvS%2BUoy3hF5VlhmuiiYLiAN0MJDg%2FrwGOqUB14Dt0PU06aMyw3Y1bLrcBA7Na5HEWpE9CA5JyGnKWx5zOAsdNCfhbXWCGU%2Bm87db%2B7wBTeRi9ONxJgI29Oz%2B5ULhbuqSyA7eZHPVFF9YkW6gxWDNM0yJL4XGkukvShdYV9kz2LNxTgh0lstML%2FhXUt5HwNL5nbnGIB7NMHydm4tOJYg8H%2FKDGpJQPGkij8yaoUfVmRKcBGUZRBBneEWFtC7MN7xR&X-Amz-Signature=7550eaa5bd6064c43c6d032de6032de5574b0616acbdd17fde880ea208bec3fd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PLAS2PE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQqZEryg25wF%2F1bhqru%2BKRBcWCOVQWwy5DEFiAxL9wdAiEAnuyzf5ZpVqJocmvqvpKMDCjWhJU%2FJv5bGyj3YtFjQxAqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKJW0HYXnO211R03%2BircAxLMhzMbmxPah85qtqbSD0xquLwUvd%2Bp10NcBHWSZ1NiunxiCE11BaNS3WLay0p5n%2BY5DdYKukW0HF8ozFJQ0gP6lkfZQJ88OBr6aF4g5crgu19UiKpz2j7Hngw6sFv%2BLkQ2wVTSK%2BrlLtY3uXyY6gZT51sduAQfjeQU4DaFTrdiN3IYA5OClbif6GN8SBfK01fljJS4U774vPXdNL8QFW6GCEA2FDYT%2F6J1ujYrPzdLLhnZRrz1DFiIQAoidQC7%2BjDcx79Ox9VSd0R2zRTVpcLSi38AMP9esjiiQsm5MBLOE%2BSm4xE5YbpgryZ0aRFNLTZhtCir9jqy70AzMUw797lyD7zN%2FfH0Hi406RrcgeekLj7bpTyg2D6trmZzhLosmJk7hsR27VSEKBTXweP3l%2BZ%2FdI8%2Bs%2FfdXzSC7x3TVE59YIyFPUAKEtXhJLwpnb3n2DT5vi72xUGIW7jiXAbTyTwdHnE7u8CZLwaKInkw7q1iuF8qEwEmOLlS7mwZiEHmSf76WTyHV8cETGgDuA%2FowPS1WE5Je0thx6uQIT02T%2FjaZ8qO9u97%2FtRa%2BeuTkveHe8BxKrTVV%2B8Haw3ZlDy60%2BPyA57cce9tcVYgAvS%2BUoy3hF5VlhmuiiYLiAN0MJDg%2FrwGOqUB14Dt0PU06aMyw3Y1bLrcBA7Na5HEWpE9CA5JyGnKWx5zOAsdNCfhbXWCGU%2Bm87db%2B7wBTeRi9ONxJgI29Oz%2B5ULhbuqSyA7eZHPVFF9YkW6gxWDNM0yJL4XGkukvShdYV9kz2LNxTgh0lstML%2FhXUt5HwNL5nbnGIB7NMHydm4tOJYg8H%2FKDGpJQPGkij8yaoUfVmRKcBGUZRBBneEWFtC7MN7xR&X-Amz-Signature=e69ad677b2993b98ed1d19f6847486c6bef518c8cfddfd240aca85de6064f98e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PLAS2PE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQqZEryg25wF%2F1bhqru%2BKRBcWCOVQWwy5DEFiAxL9wdAiEAnuyzf5ZpVqJocmvqvpKMDCjWhJU%2FJv5bGyj3YtFjQxAqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKJW0HYXnO211R03%2BircAxLMhzMbmxPah85qtqbSD0xquLwUvd%2Bp10NcBHWSZ1NiunxiCE11BaNS3WLay0p5n%2BY5DdYKukW0HF8ozFJQ0gP6lkfZQJ88OBr6aF4g5crgu19UiKpz2j7Hngw6sFv%2BLkQ2wVTSK%2BrlLtY3uXyY6gZT51sduAQfjeQU4DaFTrdiN3IYA5OClbif6GN8SBfK01fljJS4U774vPXdNL8QFW6GCEA2FDYT%2F6J1ujYrPzdLLhnZRrz1DFiIQAoidQC7%2BjDcx79Ox9VSd0R2zRTVpcLSi38AMP9esjiiQsm5MBLOE%2BSm4xE5YbpgryZ0aRFNLTZhtCir9jqy70AzMUw797lyD7zN%2FfH0Hi406RrcgeekLj7bpTyg2D6trmZzhLosmJk7hsR27VSEKBTXweP3l%2BZ%2FdI8%2Bs%2FfdXzSC7x3TVE59YIyFPUAKEtXhJLwpnb3n2DT5vi72xUGIW7jiXAbTyTwdHnE7u8CZLwaKInkw7q1iuF8qEwEmOLlS7mwZiEHmSf76WTyHV8cETGgDuA%2FowPS1WE5Je0thx6uQIT02T%2FjaZ8qO9u97%2FtRa%2BeuTkveHe8BxKrTVV%2B8Haw3ZlDy60%2BPyA57cce9tcVYgAvS%2BUoy3hF5VlhmuiiYLiAN0MJDg%2FrwGOqUB14Dt0PU06aMyw3Y1bLrcBA7Na5HEWpE9CA5JyGnKWx5zOAsdNCfhbXWCGU%2Bm87db%2B7wBTeRi9ONxJgI29Oz%2B5ULhbuqSyA7eZHPVFF9YkW6gxWDNM0yJL4XGkukvShdYV9kz2LNxTgh0lstML%2FhXUt5HwNL5nbnGIB7NMHydm4tOJYg8H%2FKDGpJQPGkij8yaoUfVmRKcBGUZRBBneEWFtC7MN7xR&X-Amz-Signature=6cc5e442e35eda0c853352f942540fd1e31f11075dcbd150be115ab081565ef5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZWXJXOA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqvaH32NXjvRnPU5Ou%2B4kcyZb9sV64GFY5iOyX7PPAHwIhAOry%2FVCp0fLOwoWGJusytaLoustjsf1K2B55tJ8xeOiuKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4r5jQdvNbFsycjrYq3ANP57Rfedn1XQdCjAXZxFKVzzZzxdbmy1FdQWbuq0SZy7mmtDos66T0qxI%2BzqYS3j38fhmOKJg0%2Fd6evcwzozPQk6XKnMghmmpMHbwL7py5liZBBiniUw3NKSCBrIAFcldwJqM6s7orjVbdMEmTmfp3Ry3XCWWVAb7k9GRqEYSkX7cqTNVlMMCD%2BVlrDPnicX83QSqdeimMxtGFBQq1izsYDPBN04l9Hq5lISjX00saenZjTq%2FhXIFOnxIR8vqwhhOaKyMhRJcmQrHT9ememL0vJW7ReiE4gIbBDCGu%2FVi2F47yEDYVm4Q5Bj5IGUrN89oYqbhhMiv%2BxVhuU32DXywLO70P%2Br5dIFuatMUde%2FyCjdQKXRNnkWzIYlVt6w0US%2FsgE%2BXV9Wpy2opaTJS8m2XKhg1whpmQaWLD1rkMKcEeL%2BfnMYgpkQ%2FvUksIjRhugIPn2IuZrGomwmnhA8XWxinLEtJhmZLucKnqCir4bg4z8wDulkB08C9ogTyUMCWQNPVZaahMp%2BsOe7MWpX%2FRnTQB935rgwpWAVsIBpLG45yegqLS91LaoBuXT6OcghrkYyUDYETY4ErOOKldqt9S4y%2FqkNX1rBK2lEMZYERdowrjs1oiShVJF%2Fwh4WtZ8DDP1v68BjqkARpnoKBxAlw3lIeVXWVQJxjVKTjp5XhCTBq99XZDHxS4J1flokvQ2B0ZnaXhlJHH6UbWag6pgHuUIQw%2FFsE0PIVgAhThM38UqJMnUo6VSPADxpH4I4Qy0mIfZ35aCHsFegY6J7XqqB2yUbR2WIve44L%2BCPWP4P%2BuWXfOsLTKcxDXkPd4p%2FsvC0TZqo7Qjj%2B11cftC55ClOOeAL2Gq1Y2LqHl35e1&X-Amz-Signature=d73b9070b9d858a78c6723c34f1ac53e5d5b07dfaf13c019ebb375ba8b2e5590&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZWXJXOA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqvaH32NXjvRnPU5Ou%2B4kcyZb9sV64GFY5iOyX7PPAHwIhAOry%2FVCp0fLOwoWGJusytaLoustjsf1K2B55tJ8xeOiuKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4r5jQdvNbFsycjrYq3ANP57Rfedn1XQdCjAXZxFKVzzZzxdbmy1FdQWbuq0SZy7mmtDos66T0qxI%2BzqYS3j38fhmOKJg0%2Fd6evcwzozPQk6XKnMghmmpMHbwL7py5liZBBiniUw3NKSCBrIAFcldwJqM6s7orjVbdMEmTmfp3Ry3XCWWVAb7k9GRqEYSkX7cqTNVlMMCD%2BVlrDPnicX83QSqdeimMxtGFBQq1izsYDPBN04l9Hq5lISjX00saenZjTq%2FhXIFOnxIR8vqwhhOaKyMhRJcmQrHT9ememL0vJW7ReiE4gIbBDCGu%2FVi2F47yEDYVm4Q5Bj5IGUrN89oYqbhhMiv%2BxVhuU32DXywLO70P%2Br5dIFuatMUde%2FyCjdQKXRNnkWzIYlVt6w0US%2FsgE%2BXV9Wpy2opaTJS8m2XKhg1whpmQaWLD1rkMKcEeL%2BfnMYgpkQ%2FvUksIjRhugIPn2IuZrGomwmnhA8XWxinLEtJhmZLucKnqCir4bg4z8wDulkB08C9ogTyUMCWQNPVZaahMp%2BsOe7MWpX%2FRnTQB935rgwpWAVsIBpLG45yegqLS91LaoBuXT6OcghrkYyUDYETY4ErOOKldqt9S4y%2FqkNX1rBK2lEMZYERdowrjs1oiShVJF%2Fwh4WtZ8DDP1v68BjqkARpnoKBxAlw3lIeVXWVQJxjVKTjp5XhCTBq99XZDHxS4J1flokvQ2B0ZnaXhlJHH6UbWag6pgHuUIQw%2FFsE0PIVgAhThM38UqJMnUo6VSPADxpH4I4Qy0mIfZ35aCHsFegY6J7XqqB2yUbR2WIve44L%2BCPWP4P%2BuWXfOsLTKcxDXkPd4p%2FsvC0TZqo7Qjj%2B11cftC55ClOOeAL2Gq1Y2LqHl35e1&X-Amz-Signature=941cbd2cf499e69c81f949cfd03ae9eb4b8a481a3c2a96af28ad2d9d11032a52&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZWXJXOA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqvaH32NXjvRnPU5Ou%2B4kcyZb9sV64GFY5iOyX7PPAHwIhAOry%2FVCp0fLOwoWGJusytaLoustjsf1K2B55tJ8xeOiuKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4r5jQdvNbFsycjrYq3ANP57Rfedn1XQdCjAXZxFKVzzZzxdbmy1FdQWbuq0SZy7mmtDos66T0qxI%2BzqYS3j38fhmOKJg0%2Fd6evcwzozPQk6XKnMghmmpMHbwL7py5liZBBiniUw3NKSCBrIAFcldwJqM6s7orjVbdMEmTmfp3Ry3XCWWVAb7k9GRqEYSkX7cqTNVlMMCD%2BVlrDPnicX83QSqdeimMxtGFBQq1izsYDPBN04l9Hq5lISjX00saenZjTq%2FhXIFOnxIR8vqwhhOaKyMhRJcmQrHT9ememL0vJW7ReiE4gIbBDCGu%2FVi2F47yEDYVm4Q5Bj5IGUrN89oYqbhhMiv%2BxVhuU32DXywLO70P%2Br5dIFuatMUde%2FyCjdQKXRNnkWzIYlVt6w0US%2FsgE%2BXV9Wpy2opaTJS8m2XKhg1whpmQaWLD1rkMKcEeL%2BfnMYgpkQ%2FvUksIjRhugIPn2IuZrGomwmnhA8XWxinLEtJhmZLucKnqCir4bg4z8wDulkB08C9ogTyUMCWQNPVZaahMp%2BsOe7MWpX%2FRnTQB935rgwpWAVsIBpLG45yegqLS91LaoBuXT6OcghrkYyUDYETY4ErOOKldqt9S4y%2FqkNX1rBK2lEMZYERdowrjs1oiShVJF%2Fwh4WtZ8DDP1v68BjqkARpnoKBxAlw3lIeVXWVQJxjVKTjp5XhCTBq99XZDHxS4J1flokvQ2B0ZnaXhlJHH6UbWag6pgHuUIQw%2FFsE0PIVgAhThM38UqJMnUo6VSPADxpH4I4Qy0mIfZ35aCHsFegY6J7XqqB2yUbR2WIve44L%2BCPWP4P%2BuWXfOsLTKcxDXkPd4p%2FsvC0TZqo7Qjj%2B11cftC55ClOOeAL2Gq1Y2LqHl35e1&X-Amz-Signature=401e35e0cc5a4bbec277cdef6dec32f1c872c33a17fd378b5c1d5ca818682a6f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZWXJXOA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqvaH32NXjvRnPU5Ou%2B4kcyZb9sV64GFY5iOyX7PPAHwIhAOry%2FVCp0fLOwoWGJusytaLoustjsf1K2B55tJ8xeOiuKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4r5jQdvNbFsycjrYq3ANP57Rfedn1XQdCjAXZxFKVzzZzxdbmy1FdQWbuq0SZy7mmtDos66T0qxI%2BzqYS3j38fhmOKJg0%2Fd6evcwzozPQk6XKnMghmmpMHbwL7py5liZBBiniUw3NKSCBrIAFcldwJqM6s7orjVbdMEmTmfp3Ry3XCWWVAb7k9GRqEYSkX7cqTNVlMMCD%2BVlrDPnicX83QSqdeimMxtGFBQq1izsYDPBN04l9Hq5lISjX00saenZjTq%2FhXIFOnxIR8vqwhhOaKyMhRJcmQrHT9ememL0vJW7ReiE4gIbBDCGu%2FVi2F47yEDYVm4Q5Bj5IGUrN89oYqbhhMiv%2BxVhuU32DXywLO70P%2Br5dIFuatMUde%2FyCjdQKXRNnkWzIYlVt6w0US%2FsgE%2BXV9Wpy2opaTJS8m2XKhg1whpmQaWLD1rkMKcEeL%2BfnMYgpkQ%2FvUksIjRhugIPn2IuZrGomwmnhA8XWxinLEtJhmZLucKnqCir4bg4z8wDulkB08C9ogTyUMCWQNPVZaahMp%2BsOe7MWpX%2FRnTQB935rgwpWAVsIBpLG45yegqLS91LaoBuXT6OcghrkYyUDYETY4ErOOKldqt9S4y%2FqkNX1rBK2lEMZYERdowrjs1oiShVJF%2Fwh4WtZ8DDP1v68BjqkARpnoKBxAlw3lIeVXWVQJxjVKTjp5XhCTBq99XZDHxS4J1flokvQ2B0ZnaXhlJHH6UbWag6pgHuUIQw%2FFsE0PIVgAhThM38UqJMnUo6VSPADxpH4I4Qy0mIfZ35aCHsFegY6J7XqqB2yUbR2WIve44L%2BCPWP4P%2BuWXfOsLTKcxDXkPd4p%2FsvC0TZqo7Qjj%2B11cftC55ClOOeAL2Gq1Y2LqHl35e1&X-Amz-Signature=ecefec489beb0fd2fd3cc79f72c8a6b0db6b3b8018b5decf27bade12beb7ee63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZWXJXOA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqvaH32NXjvRnPU5Ou%2B4kcyZb9sV64GFY5iOyX7PPAHwIhAOry%2FVCp0fLOwoWGJusytaLoustjsf1K2B55tJ8xeOiuKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4r5jQdvNbFsycjrYq3ANP57Rfedn1XQdCjAXZxFKVzzZzxdbmy1FdQWbuq0SZy7mmtDos66T0qxI%2BzqYS3j38fhmOKJg0%2Fd6evcwzozPQk6XKnMghmmpMHbwL7py5liZBBiniUw3NKSCBrIAFcldwJqM6s7orjVbdMEmTmfp3Ry3XCWWVAb7k9GRqEYSkX7cqTNVlMMCD%2BVlrDPnicX83QSqdeimMxtGFBQq1izsYDPBN04l9Hq5lISjX00saenZjTq%2FhXIFOnxIR8vqwhhOaKyMhRJcmQrHT9ememL0vJW7ReiE4gIbBDCGu%2FVi2F47yEDYVm4Q5Bj5IGUrN89oYqbhhMiv%2BxVhuU32DXywLO70P%2Br5dIFuatMUde%2FyCjdQKXRNnkWzIYlVt6w0US%2FsgE%2BXV9Wpy2opaTJS8m2XKhg1whpmQaWLD1rkMKcEeL%2BfnMYgpkQ%2FvUksIjRhugIPn2IuZrGomwmnhA8XWxinLEtJhmZLucKnqCir4bg4z8wDulkB08C9ogTyUMCWQNPVZaahMp%2BsOe7MWpX%2FRnTQB935rgwpWAVsIBpLG45yegqLS91LaoBuXT6OcghrkYyUDYETY4ErOOKldqt9S4y%2FqkNX1rBK2lEMZYERdowrjs1oiShVJF%2Fwh4WtZ8DDP1v68BjqkARpnoKBxAlw3lIeVXWVQJxjVKTjp5XhCTBq99XZDHxS4J1flokvQ2B0ZnaXhlJHH6UbWag6pgHuUIQw%2FFsE0PIVgAhThM38UqJMnUo6VSPADxpH4I4Qy0mIfZ35aCHsFegY6J7XqqB2yUbR2WIve44L%2BCPWP4P%2BuWXfOsLTKcxDXkPd4p%2FsvC0TZqo7Qjj%2B11cftC55ClOOeAL2Gq1Y2LqHl35e1&X-Amz-Signature=863ca6bbac8767015387e4ddf087bc0b8f3aeb30f515a6da725be15b3c6c646f&X-Amz-SignedHeaders=host&x-id=GetObject)
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


