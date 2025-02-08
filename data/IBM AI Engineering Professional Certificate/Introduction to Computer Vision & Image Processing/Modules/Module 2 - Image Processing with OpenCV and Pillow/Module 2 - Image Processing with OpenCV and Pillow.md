

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM2DWB3Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAGv1H5iJARTYK5wltzWRIT3W4XL2hNp5tlkYL3en3oAAiBSSnNT06wrau%2BAd%2BX1JEDkSOfHs5fH3p8N22aa%2FDcKgCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIwz7R3ww7%2BAr9cBuKtwDme99iXrgNlQEx7vwjHKlOizEs8USML89fUjt3kcb%2BzN6T9%2B47RFTlgI0u%2BMF3JuWJK04Kc6ImJggubag2ig3ctuDrKHg6dgf2x8kBGMEzAnGpHryCS6MVeq3c7VpsI34mYTSYQm%2FFAboElCWqTSXCPcFbD58jSJzxZPQKWGqxaNdEM7hapHUsEvuQrATRJ0rOiM363G%2Fb5OawM9UCuJJJtM6snfAtSJhSj%2B16CQV3u7diFJJCf2QEVWaLXQbmXXBFhZ0wwKcc9dE4bD%2FPFxslflDT4FMBuWydVuUZmzgMyCI3q3hRaoRugWJlbtpEDpw%2FXvwJROO01qUSkK6BrtTqSJt9eGcThnpzY1o%2FfmKcaQXhzvvOSH9rUDn8cMBq8d0LAI%2FBoysIOjhnfaWf3ZnF8nv14iXCMU2pS38LLox%2FPf%2FowE4Efzrav25HAgfH4QOb0b8jCMq5T4p4X%2FCJg%2Fpc7hYRPYB6jQuCMuzewHS%2FGCOmuFDnV%2FsbuCaWDqwFccgtcR7zzinh9XJI153YpBYwmaLaqE0cAOtOiaKkvjwNqHoY05afJkUfj0lc8glBel1f%2FIhc06bU9dtmzgE66M%2F%2Ba26c1NSIRmlyXCJrnrdSwstvTLojdDx55qvyyUw0o6cvQY6pgFvZZSArcovACpnMbGF39jND3AhUu2GNmEfJpK%2BBw697if2g8jsoFgxMxm49t4fVyq4TyCP4e%2FEgNRTijd%2BSaQM70sTaYb%2FMZSZPZDEypOuT6AkcrOWOyoeGPJMhInAl9tik9%2BJCm1NoczZGPbNHchgfZ3eeydIJ8KRkXxO%2F3p1s094XMgWSX9jQ43bnjs8Nqu71ETKa9y%2B5y10%2BvqaXLM760%2BkY8Dn&X-Amz-Signature=dd47e9eb8ebceedeb7c58adb53f19e6009dac3838761357094847a0cd481abcc&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBG2ZHC2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCsV44mxYZZprCsIXU9fegi%2FYMjMsOvNjZSUkHO59tB7gIhAMgZ2h2zZMDRZ6IH792ihIiBmgxUu4bo51BewqQ%2F%2BMXjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgznMSyx0jhFh2JFVg8q3APirWvf9Ukr1NCc6Dnu2iqwE027W%2BU%2F5Mp%2BaUMha5NSG%2BoGy2YGFUOXghcmKNXQjFL4CuTKeQkuPcTwaEar%2BfFN5jlp2ymHvdY3QmLat2g7KJtSHWfdveCCI5%2Fyibwi8CcXvmzk6Nm3X4wTf0NE%2FNKHO7XIM5NH7RpH3djLplHUIPl4ZlotbVQPMEOWb69OYhRklzDujlafAwWIYzbRN5a0Gh28HNbJRMiRweuIG6jraPPX0RGmgU72X1xK%2FNs8tRqTxU8a5Bur3lDoQZjEV1QG5YG2jZ31c8P5qCk2uc9De3IDiDEWFfQ82%2FPLIv0Q10hV%2F1YiGRPlaXeINCGgNmv24Hw3sYt5IzXz97hBB4ne%2BND9n5nAhV9hULjqwweKokvEoXQselHmm9a%2BODYfv3JhV2sA1HJOn1V8lut5p3TBfAIln5rtwwxE4Ov6ve5w4z4UjzTuyc5RkxZ%2FOcgBQpM547cBaCiHCaP17TQSLbbPs16y5ZXcujq11GacbIKN%2F7jR5319rovq1o0yq6m46b%2FOB1%2BrrrTSq%2FfJ%2F%2BImS1XcZUfD4n0wvfQu4VcvAyercqYJJxve16%2FMfqD5Bv8Th9PYpfxO1zQ5o4Kh9yxK88tMiUnAoR9IhhQnE7t9LjDbjpy9BjqkAcVUmJTVk6ywpyEOKjHFEPQUeTVvwp0XlhwMQ588nV8Yxc1IUV%2FuBighwRGMulUe%2BO4SnNkOngwtKm62Ze2fqbHNb%2FYJjA30aqydgf0Rx9J28o4sc5ctCy2NEKzH%2BptEbkBk%2F5QWcf7V1c0%2BmQURWWOTuY0ZmiGcz5JbHlSwdsb%2Flt7GnVbe0kBxN8V13BhPVjfNgu8SScOhOgtCbGbbMpAct55N&X-Amz-Signature=d7d6a5e8c3c4dd1bb15d2072f1294a1eab4c807ff63e90202163e5d6c8312894&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBG2ZHC2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCsV44mxYZZprCsIXU9fegi%2FYMjMsOvNjZSUkHO59tB7gIhAMgZ2h2zZMDRZ6IH792ihIiBmgxUu4bo51BewqQ%2F%2BMXjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgznMSyx0jhFh2JFVg8q3APirWvf9Ukr1NCc6Dnu2iqwE027W%2BU%2F5Mp%2BaUMha5NSG%2BoGy2YGFUOXghcmKNXQjFL4CuTKeQkuPcTwaEar%2BfFN5jlp2ymHvdY3QmLat2g7KJtSHWfdveCCI5%2Fyibwi8CcXvmzk6Nm3X4wTf0NE%2FNKHO7XIM5NH7RpH3djLplHUIPl4ZlotbVQPMEOWb69OYhRklzDujlafAwWIYzbRN5a0Gh28HNbJRMiRweuIG6jraPPX0RGmgU72X1xK%2FNs8tRqTxU8a5Bur3lDoQZjEV1QG5YG2jZ31c8P5qCk2uc9De3IDiDEWFfQ82%2FPLIv0Q10hV%2F1YiGRPlaXeINCGgNmv24Hw3sYt5IzXz97hBB4ne%2BND9n5nAhV9hULjqwweKokvEoXQselHmm9a%2BODYfv3JhV2sA1HJOn1V8lut5p3TBfAIln5rtwwxE4Ov6ve5w4z4UjzTuyc5RkxZ%2FOcgBQpM547cBaCiHCaP17TQSLbbPs16y5ZXcujq11GacbIKN%2F7jR5319rovq1o0yq6m46b%2FOB1%2BrrrTSq%2FfJ%2F%2BImS1XcZUfD4n0wvfQu4VcvAyercqYJJxve16%2FMfqD5Bv8Th9PYpfxO1zQ5o4Kh9yxK88tMiUnAoR9IhhQnE7t9LjDbjpy9BjqkAcVUmJTVk6ywpyEOKjHFEPQUeTVvwp0XlhwMQ588nV8Yxc1IUV%2FuBighwRGMulUe%2BO4SnNkOngwtKm62Ze2fqbHNb%2FYJjA30aqydgf0Rx9J28o4sc5ctCy2NEKzH%2BptEbkBk%2F5QWcf7V1c0%2BmQURWWOTuY0ZmiGcz5JbHlSwdsb%2Flt7GnVbe0kBxN8V13BhPVjfNgu8SScOhOgtCbGbbMpAct55N&X-Amz-Signature=5532d56f8ce39bd24013d873ae3b01486d82aec701b2b9c452ae302323e63c12&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBG2ZHC2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCsV44mxYZZprCsIXU9fegi%2FYMjMsOvNjZSUkHO59tB7gIhAMgZ2h2zZMDRZ6IH792ihIiBmgxUu4bo51BewqQ%2F%2BMXjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgznMSyx0jhFh2JFVg8q3APirWvf9Ukr1NCc6Dnu2iqwE027W%2BU%2F5Mp%2BaUMha5NSG%2BoGy2YGFUOXghcmKNXQjFL4CuTKeQkuPcTwaEar%2BfFN5jlp2ymHvdY3QmLat2g7KJtSHWfdveCCI5%2Fyibwi8CcXvmzk6Nm3X4wTf0NE%2FNKHO7XIM5NH7RpH3djLplHUIPl4ZlotbVQPMEOWb69OYhRklzDujlafAwWIYzbRN5a0Gh28HNbJRMiRweuIG6jraPPX0RGmgU72X1xK%2FNs8tRqTxU8a5Bur3lDoQZjEV1QG5YG2jZ31c8P5qCk2uc9De3IDiDEWFfQ82%2FPLIv0Q10hV%2F1YiGRPlaXeINCGgNmv24Hw3sYt5IzXz97hBB4ne%2BND9n5nAhV9hULjqwweKokvEoXQselHmm9a%2BODYfv3JhV2sA1HJOn1V8lut5p3TBfAIln5rtwwxE4Ov6ve5w4z4UjzTuyc5RkxZ%2FOcgBQpM547cBaCiHCaP17TQSLbbPs16y5ZXcujq11GacbIKN%2F7jR5319rovq1o0yq6m46b%2FOB1%2BrrrTSq%2FfJ%2F%2BImS1XcZUfD4n0wvfQu4VcvAyercqYJJxve16%2FMfqD5Bv8Th9PYpfxO1zQ5o4Kh9yxK88tMiUnAoR9IhhQnE7t9LjDbjpy9BjqkAcVUmJTVk6ywpyEOKjHFEPQUeTVvwp0XlhwMQ588nV8Yxc1IUV%2FuBighwRGMulUe%2BO4SnNkOngwtKm62Ze2fqbHNb%2FYJjA30aqydgf0Rx9J28o4sc5ctCy2NEKzH%2BptEbkBk%2F5QWcf7V1c0%2BmQURWWOTuY0ZmiGcz5JbHlSwdsb%2Flt7GnVbe0kBxN8V13BhPVjfNgu8SScOhOgtCbGbbMpAct55N&X-Amz-Signature=df03fbf3567f14628b9e4615c18b654aa012fe08dfa89bc5d62b6ef59ebb3bb8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBG2ZHC2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCsV44mxYZZprCsIXU9fegi%2FYMjMsOvNjZSUkHO59tB7gIhAMgZ2h2zZMDRZ6IH792ihIiBmgxUu4bo51BewqQ%2F%2BMXjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgznMSyx0jhFh2JFVg8q3APirWvf9Ukr1NCc6Dnu2iqwE027W%2BU%2F5Mp%2BaUMha5NSG%2BoGy2YGFUOXghcmKNXQjFL4CuTKeQkuPcTwaEar%2BfFN5jlp2ymHvdY3QmLat2g7KJtSHWfdveCCI5%2Fyibwi8CcXvmzk6Nm3X4wTf0NE%2FNKHO7XIM5NH7RpH3djLplHUIPl4ZlotbVQPMEOWb69OYhRklzDujlafAwWIYzbRN5a0Gh28HNbJRMiRweuIG6jraPPX0RGmgU72X1xK%2FNs8tRqTxU8a5Bur3lDoQZjEV1QG5YG2jZ31c8P5qCk2uc9De3IDiDEWFfQ82%2FPLIv0Q10hV%2F1YiGRPlaXeINCGgNmv24Hw3sYt5IzXz97hBB4ne%2BND9n5nAhV9hULjqwweKokvEoXQselHmm9a%2BODYfv3JhV2sA1HJOn1V8lut5p3TBfAIln5rtwwxE4Ov6ve5w4z4UjzTuyc5RkxZ%2FOcgBQpM547cBaCiHCaP17TQSLbbPs16y5ZXcujq11GacbIKN%2F7jR5319rovq1o0yq6m46b%2FOB1%2BrrrTSq%2FfJ%2F%2BImS1XcZUfD4n0wvfQu4VcvAyercqYJJxve16%2FMfqD5Bv8Th9PYpfxO1zQ5o4Kh9yxK88tMiUnAoR9IhhQnE7t9LjDbjpy9BjqkAcVUmJTVk6ywpyEOKjHFEPQUeTVvwp0XlhwMQ588nV8Yxc1IUV%2FuBighwRGMulUe%2BO4SnNkOngwtKm62Ze2fqbHNb%2FYJjA30aqydgf0Rx9J28o4sc5ctCy2NEKzH%2BptEbkBk%2F5QWcf7V1c0%2BmQURWWOTuY0ZmiGcz5JbHlSwdsb%2Flt7GnVbe0kBxN8V13BhPVjfNgu8SScOhOgtCbGbbMpAct55N&X-Amz-Signature=3b72119cca8a09414e47f071074c41941ee03a7e9845c0b3dd0d21b8772383cc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBG2ZHC2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCsV44mxYZZprCsIXU9fegi%2FYMjMsOvNjZSUkHO59tB7gIhAMgZ2h2zZMDRZ6IH792ihIiBmgxUu4bo51BewqQ%2F%2BMXjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgznMSyx0jhFh2JFVg8q3APirWvf9Ukr1NCc6Dnu2iqwE027W%2BU%2F5Mp%2BaUMha5NSG%2BoGy2YGFUOXghcmKNXQjFL4CuTKeQkuPcTwaEar%2BfFN5jlp2ymHvdY3QmLat2g7KJtSHWfdveCCI5%2Fyibwi8CcXvmzk6Nm3X4wTf0NE%2FNKHO7XIM5NH7RpH3djLplHUIPl4ZlotbVQPMEOWb69OYhRklzDujlafAwWIYzbRN5a0Gh28HNbJRMiRweuIG6jraPPX0RGmgU72X1xK%2FNs8tRqTxU8a5Bur3lDoQZjEV1QG5YG2jZ31c8P5qCk2uc9De3IDiDEWFfQ82%2FPLIv0Q10hV%2F1YiGRPlaXeINCGgNmv24Hw3sYt5IzXz97hBB4ne%2BND9n5nAhV9hULjqwweKokvEoXQselHmm9a%2BODYfv3JhV2sA1HJOn1V8lut5p3TBfAIln5rtwwxE4Ov6ve5w4z4UjzTuyc5RkxZ%2FOcgBQpM547cBaCiHCaP17TQSLbbPs16y5ZXcujq11GacbIKN%2F7jR5319rovq1o0yq6m46b%2FOB1%2BrrrTSq%2FfJ%2F%2BImS1XcZUfD4n0wvfQu4VcvAyercqYJJxve16%2FMfqD5Bv8Th9PYpfxO1zQ5o4Kh9yxK88tMiUnAoR9IhhQnE7t9LjDbjpy9BjqkAcVUmJTVk6ywpyEOKjHFEPQUeTVvwp0XlhwMQ588nV8Yxc1IUV%2FuBighwRGMulUe%2BO4SnNkOngwtKm62Ze2fqbHNb%2FYJjA30aqydgf0Rx9J28o4sc5ctCy2NEKzH%2BptEbkBk%2F5QWcf7V1c0%2BmQURWWOTuY0ZmiGcz5JbHlSwdsb%2Flt7GnVbe0kBxN8V13BhPVjfNgu8SScOhOgtCbGbbMpAct55N&X-Amz-Signature=ea911d76afcfa1330e2fa13b4ae5b47698ad76e92d8d98c6d1f504d339dcfee4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM2DWB3Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAGv1H5iJARTYK5wltzWRIT3W4XL2hNp5tlkYL3en3oAAiBSSnNT06wrau%2BAd%2BX1JEDkSOfHs5fH3p8N22aa%2FDcKgCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIwz7R3ww7%2BAr9cBuKtwDme99iXrgNlQEx7vwjHKlOizEs8USML89fUjt3kcb%2BzN6T9%2B47RFTlgI0u%2BMF3JuWJK04Kc6ImJggubag2ig3ctuDrKHg6dgf2x8kBGMEzAnGpHryCS6MVeq3c7VpsI34mYTSYQm%2FFAboElCWqTSXCPcFbD58jSJzxZPQKWGqxaNdEM7hapHUsEvuQrATRJ0rOiM363G%2Fb5OawM9UCuJJJtM6snfAtSJhSj%2B16CQV3u7diFJJCf2QEVWaLXQbmXXBFhZ0wwKcc9dE4bD%2FPFxslflDT4FMBuWydVuUZmzgMyCI3q3hRaoRugWJlbtpEDpw%2FXvwJROO01qUSkK6BrtTqSJt9eGcThnpzY1o%2FfmKcaQXhzvvOSH9rUDn8cMBq8d0LAI%2FBoysIOjhnfaWf3ZnF8nv14iXCMU2pS38LLox%2FPf%2FowE4Efzrav25HAgfH4QOb0b8jCMq5T4p4X%2FCJg%2Fpc7hYRPYB6jQuCMuzewHS%2FGCOmuFDnV%2FsbuCaWDqwFccgtcR7zzinh9XJI153YpBYwmaLaqE0cAOtOiaKkvjwNqHoY05afJkUfj0lc8glBel1f%2FIhc06bU9dtmzgE66M%2F%2Ba26c1NSIRmlyXCJrnrdSwstvTLojdDx55qvyyUw0o6cvQY6pgFvZZSArcovACpnMbGF39jND3AhUu2GNmEfJpK%2BBw697if2g8jsoFgxMxm49t4fVyq4TyCP4e%2FEgNRTijd%2BSaQM70sTaYb%2FMZSZPZDEypOuT6AkcrOWOyoeGPJMhInAl9tik9%2BJCm1NoczZGPbNHchgfZ3eeydIJ8KRkXxO%2F3p1s094XMgWSX9jQ43bnjs8Nqu71ETKa9y%2B5y10%2BvqaXLM760%2BkY8Dn&X-Amz-Signature=36a188adfb99e0f20bfa6d6ddbcd7f09fd676390a8a155a0b30eda004190384c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM2DWB3Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAGv1H5iJARTYK5wltzWRIT3W4XL2hNp5tlkYL3en3oAAiBSSnNT06wrau%2BAd%2BX1JEDkSOfHs5fH3p8N22aa%2FDcKgCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIwz7R3ww7%2BAr9cBuKtwDme99iXrgNlQEx7vwjHKlOizEs8USML89fUjt3kcb%2BzN6T9%2B47RFTlgI0u%2BMF3JuWJK04Kc6ImJggubag2ig3ctuDrKHg6dgf2x8kBGMEzAnGpHryCS6MVeq3c7VpsI34mYTSYQm%2FFAboElCWqTSXCPcFbD58jSJzxZPQKWGqxaNdEM7hapHUsEvuQrATRJ0rOiM363G%2Fb5OawM9UCuJJJtM6snfAtSJhSj%2B16CQV3u7diFJJCf2QEVWaLXQbmXXBFhZ0wwKcc9dE4bD%2FPFxslflDT4FMBuWydVuUZmzgMyCI3q3hRaoRugWJlbtpEDpw%2FXvwJROO01qUSkK6BrtTqSJt9eGcThnpzY1o%2FfmKcaQXhzvvOSH9rUDn8cMBq8d0LAI%2FBoysIOjhnfaWf3ZnF8nv14iXCMU2pS38LLox%2FPf%2FowE4Efzrav25HAgfH4QOb0b8jCMq5T4p4X%2FCJg%2Fpc7hYRPYB6jQuCMuzewHS%2FGCOmuFDnV%2FsbuCaWDqwFccgtcR7zzinh9XJI153YpBYwmaLaqE0cAOtOiaKkvjwNqHoY05afJkUfj0lc8glBel1f%2FIhc06bU9dtmzgE66M%2F%2Ba26c1NSIRmlyXCJrnrdSwstvTLojdDx55qvyyUw0o6cvQY6pgFvZZSArcovACpnMbGF39jND3AhUu2GNmEfJpK%2BBw697if2g8jsoFgxMxm49t4fVyq4TyCP4e%2FEgNRTijd%2BSaQM70sTaYb%2FMZSZPZDEypOuT6AkcrOWOyoeGPJMhInAl9tik9%2BJCm1NoczZGPbNHchgfZ3eeydIJ8KRkXxO%2F3p1s094XMgWSX9jQ43bnjs8Nqu71ETKa9y%2B5y10%2BvqaXLM760%2BkY8Dn&X-Amz-Signature=2a6108b83d10a0f046ddf1538a31cb031f2e3836f1086094deb53248c9749373&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM2DWB3Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAGv1H5iJARTYK5wltzWRIT3W4XL2hNp5tlkYL3en3oAAiBSSnNT06wrau%2BAd%2BX1JEDkSOfHs5fH3p8N22aa%2FDcKgCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIwz7R3ww7%2BAr9cBuKtwDme99iXrgNlQEx7vwjHKlOizEs8USML89fUjt3kcb%2BzN6T9%2B47RFTlgI0u%2BMF3JuWJK04Kc6ImJggubag2ig3ctuDrKHg6dgf2x8kBGMEzAnGpHryCS6MVeq3c7VpsI34mYTSYQm%2FFAboElCWqTSXCPcFbD58jSJzxZPQKWGqxaNdEM7hapHUsEvuQrATRJ0rOiM363G%2Fb5OawM9UCuJJJtM6snfAtSJhSj%2B16CQV3u7diFJJCf2QEVWaLXQbmXXBFhZ0wwKcc9dE4bD%2FPFxslflDT4FMBuWydVuUZmzgMyCI3q3hRaoRugWJlbtpEDpw%2FXvwJROO01qUSkK6BrtTqSJt9eGcThnpzY1o%2FfmKcaQXhzvvOSH9rUDn8cMBq8d0LAI%2FBoysIOjhnfaWf3ZnF8nv14iXCMU2pS38LLox%2FPf%2FowE4Efzrav25HAgfH4QOb0b8jCMq5T4p4X%2FCJg%2Fpc7hYRPYB6jQuCMuzewHS%2FGCOmuFDnV%2FsbuCaWDqwFccgtcR7zzinh9XJI153YpBYwmaLaqE0cAOtOiaKkvjwNqHoY05afJkUfj0lc8glBel1f%2FIhc06bU9dtmzgE66M%2F%2Ba26c1NSIRmlyXCJrnrdSwstvTLojdDx55qvyyUw0o6cvQY6pgFvZZSArcovACpnMbGF39jND3AhUu2GNmEfJpK%2BBw697if2g8jsoFgxMxm49t4fVyq4TyCP4e%2FEgNRTijd%2BSaQM70sTaYb%2FMZSZPZDEypOuT6AkcrOWOyoeGPJMhInAl9tik9%2BJCm1NoczZGPbNHchgfZ3eeydIJ8KRkXxO%2F3p1s094XMgWSX9jQ43bnjs8Nqu71ETKa9y%2B5y10%2BvqaXLM760%2BkY8Dn&X-Amz-Signature=fa3d558849f9c42ff46d7103cc3e439e56b88d82ad7efb592d100ea0b1f46b1f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM2DWB3Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAGv1H5iJARTYK5wltzWRIT3W4XL2hNp5tlkYL3en3oAAiBSSnNT06wrau%2BAd%2BX1JEDkSOfHs5fH3p8N22aa%2FDcKgCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIwz7R3ww7%2BAr9cBuKtwDme99iXrgNlQEx7vwjHKlOizEs8USML89fUjt3kcb%2BzN6T9%2B47RFTlgI0u%2BMF3JuWJK04Kc6ImJggubag2ig3ctuDrKHg6dgf2x8kBGMEzAnGpHryCS6MVeq3c7VpsI34mYTSYQm%2FFAboElCWqTSXCPcFbD58jSJzxZPQKWGqxaNdEM7hapHUsEvuQrATRJ0rOiM363G%2Fb5OawM9UCuJJJtM6snfAtSJhSj%2B16CQV3u7diFJJCf2QEVWaLXQbmXXBFhZ0wwKcc9dE4bD%2FPFxslflDT4FMBuWydVuUZmzgMyCI3q3hRaoRugWJlbtpEDpw%2FXvwJROO01qUSkK6BrtTqSJt9eGcThnpzY1o%2FfmKcaQXhzvvOSH9rUDn8cMBq8d0LAI%2FBoysIOjhnfaWf3ZnF8nv14iXCMU2pS38LLox%2FPf%2FowE4Efzrav25HAgfH4QOb0b8jCMq5T4p4X%2FCJg%2Fpc7hYRPYB6jQuCMuzewHS%2FGCOmuFDnV%2FsbuCaWDqwFccgtcR7zzinh9XJI153YpBYwmaLaqE0cAOtOiaKkvjwNqHoY05afJkUfj0lc8glBel1f%2FIhc06bU9dtmzgE66M%2F%2Ba26c1NSIRmlyXCJrnrdSwstvTLojdDx55qvyyUw0o6cvQY6pgFvZZSArcovACpnMbGF39jND3AhUu2GNmEfJpK%2BBw697if2g8jsoFgxMxm49t4fVyq4TyCP4e%2FEgNRTijd%2BSaQM70sTaYb%2FMZSZPZDEypOuT6AkcrOWOyoeGPJMhInAl9tik9%2BJCm1NoczZGPbNHchgfZ3eeydIJ8KRkXxO%2F3p1s094XMgWSX9jQ43bnjs8Nqu71ETKa9y%2B5y10%2BvqaXLM760%2BkY8Dn&X-Amz-Signature=08183fd03b889ea05247e0442934d6fa6f4ddf7d22948a80e2a1c4c1ef711e04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM2DWB3Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAGv1H5iJARTYK5wltzWRIT3W4XL2hNp5tlkYL3en3oAAiBSSnNT06wrau%2BAd%2BX1JEDkSOfHs5fH3p8N22aa%2FDcKgCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIwz7R3ww7%2BAr9cBuKtwDme99iXrgNlQEx7vwjHKlOizEs8USML89fUjt3kcb%2BzN6T9%2B47RFTlgI0u%2BMF3JuWJK04Kc6ImJggubag2ig3ctuDrKHg6dgf2x8kBGMEzAnGpHryCS6MVeq3c7VpsI34mYTSYQm%2FFAboElCWqTSXCPcFbD58jSJzxZPQKWGqxaNdEM7hapHUsEvuQrATRJ0rOiM363G%2Fb5OawM9UCuJJJtM6snfAtSJhSj%2B16CQV3u7diFJJCf2QEVWaLXQbmXXBFhZ0wwKcc9dE4bD%2FPFxslflDT4FMBuWydVuUZmzgMyCI3q3hRaoRugWJlbtpEDpw%2FXvwJROO01qUSkK6BrtTqSJt9eGcThnpzY1o%2FfmKcaQXhzvvOSH9rUDn8cMBq8d0LAI%2FBoysIOjhnfaWf3ZnF8nv14iXCMU2pS38LLox%2FPf%2FowE4Efzrav25HAgfH4QOb0b8jCMq5T4p4X%2FCJg%2Fpc7hYRPYB6jQuCMuzewHS%2FGCOmuFDnV%2FsbuCaWDqwFccgtcR7zzinh9XJI153YpBYwmaLaqE0cAOtOiaKkvjwNqHoY05afJkUfj0lc8glBel1f%2FIhc06bU9dtmzgE66M%2F%2Ba26c1NSIRmlyXCJrnrdSwstvTLojdDx55qvyyUw0o6cvQY6pgFvZZSArcovACpnMbGF39jND3AhUu2GNmEfJpK%2BBw697if2g8jsoFgxMxm49t4fVyq4TyCP4e%2FEgNRTijd%2BSaQM70sTaYb%2FMZSZPZDEypOuT6AkcrOWOyoeGPJMhInAl9tik9%2BJCm1NoczZGPbNHchgfZ3eeydIJ8KRkXxO%2F3p1s094XMgWSX9jQ43bnjs8Nqu71ETKa9y%2B5y10%2BvqaXLM760%2BkY8Dn&X-Amz-Signature=74570c8b4a91c96242fe59991b4ec1afa314239153d58f14bbb864a114040b3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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


