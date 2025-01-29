

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EQ74DQO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAqNwLnhJIcZ5A1Nwuan%2BFUaUjWTq9%2Frea%2FkP5h1XJ0GAiEArq9P75bbJe58kbKALm7HcVFK%2BDv14cdgkbw1QhGbfDMqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUOmwTpYtqUC%2Fy4rircA4bltDiuDOnuKnwgGrvul2Uq%2BcFteVBSShfoNC%2FB7F6ir909yJR%2FLpRAByGg9FhzKIUKp9Pnw%2Brx%2B8clpWoPl15bAkk9v%2F7T%2Fvey0BaRPCQidG4PUirdVCJxJKyApo6327Pt7yIsTPMsREFINkySu7BYRk%2BAvfeaDyL%2BG3MFjwtB0XuYKQOQeGNv8RUbSyPWHrlcTHgpTFYOCc7r7JrKt9pEx4i87%2BvdMsq44ChASdZGjCbPicE9DkBTEuHw6gD38Gofd5erF%2Bsbx4XvYghl%2BgbI52Iu2R3HCLU4hCqCUem4MHrWpI1XVW6UNfThsjqIPETpPuR0eKDTC1cad52YZcW5i2ImPwy9Vf%2BZRl3zdxv2ODPSFiKudd0p7WUxeYFVSNBCRcsabq9PvJsamtvtcNVJN6lEUxIn%2B9NVjYfMWYEJSz20sd%2FjfjPbz8F%2B81kw5htRuXNC5M2PzwlSMBk8zYzwDL%2B6R7Vn%2BfX6yosN%2F9GvY8E4oTPUAwR9FYa0aYGRPjM4nB0kbZwWn13ntwq%2FpDgDOFc9593XoieEUZKSKyWVVsMh7Hut9ohtSC%2FArtydOokenHDvE%2Bud7J1tptawDP5rPqim3Zuj96SiOHPfElg8VlfEdCo9UJX%2FpUMBMK7Y6bwGOqUBdcaMsczU3ALq2ZtLCE7hf73ll5iCX8h5xB1ZfbxutLinho6Tj3WjTfpEu9pe5chbjZdYJfhDqb1N2m2D6WpBxukO759pQhclESEq%2B8fT%2FTNf%2BiGkvNO4aPeV0f1j9CcdkWMajuztuAdJ1KjWuKGYCCyS5TTCDq0fcqMeDbFdU6E5QnxPUniCdXgHP3nN31QnrpupOkdtAGI61QFkM%2BXJZA7e3Ktb&X-Amz-Signature=d7fe1adbc6a6cd39ae1cda97fcde8a0896bca7ee72ba6bb982bb305a5aab47fa&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAGMCE5U%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEd%2Fo3yu%2F00%2FVc5ehXHc9lHMi2z4rdDeKtoOe2FaAHvnAiArfb8I1Qn4f%2BFlFAXz8fMLMjwP0Wmtc7kRELHMSrbDLiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwu%2FxkQiSqVCjnLz8KtwDW8F54Hsx4mlftXDCAT%2F80QZvRofpSb17cHLGUr0QDWDW4mjf0RdS85LwMT%2BUalSeCWyntMnYY6xk7BlAy2xa58bQBLPPfyZj1kSTU3HQf6rOOVDmZwQ1lWyuZNCqbufFVN5tAuXzOr8SYXxvUlgtqu4eH8GZrCMoP780Asb00R9Z3nLOuI%2FOTrE8BRBeKHcT8koAk5XEM%2B6%2BB%2BJlTKjEcwzeNaNPEYJD6kf4NNwHQpZt6yIQW8KnYR2Li9DMlULAQOIds75NIWvg6fftQkvaYk8J%2F8krI%2FtPDIdE7Tyo4kyYGQn8MgVPgMEaePp0MBIJWM4JX401%2BhjqkVyXUv9izbkL7r6L3X7QtZCnS%2BE6ABfe3YP2wi9Rl5e8QXIOzEsjUzPUl7Jol1Jnw0tWv0mzdYaowsQPMzI%2Fjyj%2B3LL7Rg%2Fg6GDVEDnDWEzHjztV0TfJggiykzUpWH5G%2BD5Mmd%2F4Y10LkqAqO%2FUDgCF1gU2DSNoXpGfpgNo87EeHd%2Fltmvwg1sl8HU9ad5VmDNvYbSRK4jeKL6G5HV93f%2BEuNCSPqrnbzCulwhFGXRIr8muQfiAI8Mvh5FRXooiZzioPEZOwTCbG6GyWnpn5rZg77DDtwKfMsyQYNNrxwlywQnkw5NjpvAY6pgFI8%2F47d%2FLpOrqfyyomhgJiXm08IZgNd8DvjlC%2FAlXCWnrs6IqZWDCGuZljcZIyd9e1rYQgWgViB%2FpwWRwLTzFLUuTrMMhz23sp9JDevSYDwWMzaFNhNIW5aGU52OJ%2BQQkDmGU4rCSbZsNHNxYo%2BLbvVaiXzgCkmJ3i3ZGm2E%2BYFcGBd9%2BvuZd3BJ7m%2FCSMlVB%2BaBV2GADzGha3%2FQ50yoAV9T7vnuAg&X-Amz-Signature=e31255bd870ca36f8e2c35391da12138476f4b4fc5f5f861642d24d320e91425&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAGMCE5U%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEd%2Fo3yu%2F00%2FVc5ehXHc9lHMi2z4rdDeKtoOe2FaAHvnAiArfb8I1Qn4f%2BFlFAXz8fMLMjwP0Wmtc7kRELHMSrbDLiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwu%2FxkQiSqVCjnLz8KtwDW8F54Hsx4mlftXDCAT%2F80QZvRofpSb17cHLGUr0QDWDW4mjf0RdS85LwMT%2BUalSeCWyntMnYY6xk7BlAy2xa58bQBLPPfyZj1kSTU3HQf6rOOVDmZwQ1lWyuZNCqbufFVN5tAuXzOr8SYXxvUlgtqu4eH8GZrCMoP780Asb00R9Z3nLOuI%2FOTrE8BRBeKHcT8koAk5XEM%2B6%2BB%2BJlTKjEcwzeNaNPEYJD6kf4NNwHQpZt6yIQW8KnYR2Li9DMlULAQOIds75NIWvg6fftQkvaYk8J%2F8krI%2FtPDIdE7Tyo4kyYGQn8MgVPgMEaePp0MBIJWM4JX401%2BhjqkVyXUv9izbkL7r6L3X7QtZCnS%2BE6ABfe3YP2wi9Rl5e8QXIOzEsjUzPUl7Jol1Jnw0tWv0mzdYaowsQPMzI%2Fjyj%2B3LL7Rg%2Fg6GDVEDnDWEzHjztV0TfJggiykzUpWH5G%2BD5Mmd%2F4Y10LkqAqO%2FUDgCF1gU2DSNoXpGfpgNo87EeHd%2Fltmvwg1sl8HU9ad5VmDNvYbSRK4jeKL6G5HV93f%2BEuNCSPqrnbzCulwhFGXRIr8muQfiAI8Mvh5FRXooiZzioPEZOwTCbG6GyWnpn5rZg77DDtwKfMsyQYNNrxwlywQnkw5NjpvAY6pgFI8%2F47d%2FLpOrqfyyomhgJiXm08IZgNd8DvjlC%2FAlXCWnrs6IqZWDCGuZljcZIyd9e1rYQgWgViB%2FpwWRwLTzFLUuTrMMhz23sp9JDevSYDwWMzaFNhNIW5aGU52OJ%2BQQkDmGU4rCSbZsNHNxYo%2BLbvVaiXzgCkmJ3i3ZGm2E%2BYFcGBd9%2BvuZd3BJ7m%2FCSMlVB%2BaBV2GADzGha3%2FQ50yoAV9T7vnuAg&X-Amz-Signature=57d584ff77f28c49d9a9db42c3a32831f532d93de8c7d46e9ba37e233f174512&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAGMCE5U%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEd%2Fo3yu%2F00%2FVc5ehXHc9lHMi2z4rdDeKtoOe2FaAHvnAiArfb8I1Qn4f%2BFlFAXz8fMLMjwP0Wmtc7kRELHMSrbDLiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwu%2FxkQiSqVCjnLz8KtwDW8F54Hsx4mlftXDCAT%2F80QZvRofpSb17cHLGUr0QDWDW4mjf0RdS85LwMT%2BUalSeCWyntMnYY6xk7BlAy2xa58bQBLPPfyZj1kSTU3HQf6rOOVDmZwQ1lWyuZNCqbufFVN5tAuXzOr8SYXxvUlgtqu4eH8GZrCMoP780Asb00R9Z3nLOuI%2FOTrE8BRBeKHcT8koAk5XEM%2B6%2BB%2BJlTKjEcwzeNaNPEYJD6kf4NNwHQpZt6yIQW8KnYR2Li9DMlULAQOIds75NIWvg6fftQkvaYk8J%2F8krI%2FtPDIdE7Tyo4kyYGQn8MgVPgMEaePp0MBIJWM4JX401%2BhjqkVyXUv9izbkL7r6L3X7QtZCnS%2BE6ABfe3YP2wi9Rl5e8QXIOzEsjUzPUl7Jol1Jnw0tWv0mzdYaowsQPMzI%2Fjyj%2B3LL7Rg%2Fg6GDVEDnDWEzHjztV0TfJggiykzUpWH5G%2BD5Mmd%2F4Y10LkqAqO%2FUDgCF1gU2DSNoXpGfpgNo87EeHd%2Fltmvwg1sl8HU9ad5VmDNvYbSRK4jeKL6G5HV93f%2BEuNCSPqrnbzCulwhFGXRIr8muQfiAI8Mvh5FRXooiZzioPEZOwTCbG6GyWnpn5rZg77DDtwKfMsyQYNNrxwlywQnkw5NjpvAY6pgFI8%2F47d%2FLpOrqfyyomhgJiXm08IZgNd8DvjlC%2FAlXCWnrs6IqZWDCGuZljcZIyd9e1rYQgWgViB%2FpwWRwLTzFLUuTrMMhz23sp9JDevSYDwWMzaFNhNIW5aGU52OJ%2BQQkDmGU4rCSbZsNHNxYo%2BLbvVaiXzgCkmJ3i3ZGm2E%2BYFcGBd9%2BvuZd3BJ7m%2FCSMlVB%2BaBV2GADzGha3%2FQ50yoAV9T7vnuAg&X-Amz-Signature=9067925c2e957976983ed8ca021b76842dcde043dc6c124058364d1138eb80fe&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAGMCE5U%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEd%2Fo3yu%2F00%2FVc5ehXHc9lHMi2z4rdDeKtoOe2FaAHvnAiArfb8I1Qn4f%2BFlFAXz8fMLMjwP0Wmtc7kRELHMSrbDLiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwu%2FxkQiSqVCjnLz8KtwDW8F54Hsx4mlftXDCAT%2F80QZvRofpSb17cHLGUr0QDWDW4mjf0RdS85LwMT%2BUalSeCWyntMnYY6xk7BlAy2xa58bQBLPPfyZj1kSTU3HQf6rOOVDmZwQ1lWyuZNCqbufFVN5tAuXzOr8SYXxvUlgtqu4eH8GZrCMoP780Asb00R9Z3nLOuI%2FOTrE8BRBeKHcT8koAk5XEM%2B6%2BB%2BJlTKjEcwzeNaNPEYJD6kf4NNwHQpZt6yIQW8KnYR2Li9DMlULAQOIds75NIWvg6fftQkvaYk8J%2F8krI%2FtPDIdE7Tyo4kyYGQn8MgVPgMEaePp0MBIJWM4JX401%2BhjqkVyXUv9izbkL7r6L3X7QtZCnS%2BE6ABfe3YP2wi9Rl5e8QXIOzEsjUzPUl7Jol1Jnw0tWv0mzdYaowsQPMzI%2Fjyj%2B3LL7Rg%2Fg6GDVEDnDWEzHjztV0TfJggiykzUpWH5G%2BD5Mmd%2F4Y10LkqAqO%2FUDgCF1gU2DSNoXpGfpgNo87EeHd%2Fltmvwg1sl8HU9ad5VmDNvYbSRK4jeKL6G5HV93f%2BEuNCSPqrnbzCulwhFGXRIr8muQfiAI8Mvh5FRXooiZzioPEZOwTCbG6GyWnpn5rZg77DDtwKfMsyQYNNrxwlywQnkw5NjpvAY6pgFI8%2F47d%2FLpOrqfyyomhgJiXm08IZgNd8DvjlC%2FAlXCWnrs6IqZWDCGuZljcZIyd9e1rYQgWgViB%2FpwWRwLTzFLUuTrMMhz23sp9JDevSYDwWMzaFNhNIW5aGU52OJ%2BQQkDmGU4rCSbZsNHNxYo%2BLbvVaiXzgCkmJ3i3ZGm2E%2BYFcGBd9%2BvuZd3BJ7m%2FCSMlVB%2BaBV2GADzGha3%2FQ50yoAV9T7vnuAg&X-Amz-Signature=2a2468e54713db36de668adf510a706f35916d9caf4fc8b0b1c3769f8762ef24&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAGMCE5U%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEd%2Fo3yu%2F00%2FVc5ehXHc9lHMi2z4rdDeKtoOe2FaAHvnAiArfb8I1Qn4f%2BFlFAXz8fMLMjwP0Wmtc7kRELHMSrbDLiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwu%2FxkQiSqVCjnLz8KtwDW8F54Hsx4mlftXDCAT%2F80QZvRofpSb17cHLGUr0QDWDW4mjf0RdS85LwMT%2BUalSeCWyntMnYY6xk7BlAy2xa58bQBLPPfyZj1kSTU3HQf6rOOVDmZwQ1lWyuZNCqbufFVN5tAuXzOr8SYXxvUlgtqu4eH8GZrCMoP780Asb00R9Z3nLOuI%2FOTrE8BRBeKHcT8koAk5XEM%2B6%2BB%2BJlTKjEcwzeNaNPEYJD6kf4NNwHQpZt6yIQW8KnYR2Li9DMlULAQOIds75NIWvg6fftQkvaYk8J%2F8krI%2FtPDIdE7Tyo4kyYGQn8MgVPgMEaePp0MBIJWM4JX401%2BhjqkVyXUv9izbkL7r6L3X7QtZCnS%2BE6ABfe3YP2wi9Rl5e8QXIOzEsjUzPUl7Jol1Jnw0tWv0mzdYaowsQPMzI%2Fjyj%2B3LL7Rg%2Fg6GDVEDnDWEzHjztV0TfJggiykzUpWH5G%2BD5Mmd%2F4Y10LkqAqO%2FUDgCF1gU2DSNoXpGfpgNo87EeHd%2Fltmvwg1sl8HU9ad5VmDNvYbSRK4jeKL6G5HV93f%2BEuNCSPqrnbzCulwhFGXRIr8muQfiAI8Mvh5FRXooiZzioPEZOwTCbG6GyWnpn5rZg77DDtwKfMsyQYNNrxwlywQnkw5NjpvAY6pgFI8%2F47d%2FLpOrqfyyomhgJiXm08IZgNd8DvjlC%2FAlXCWnrs6IqZWDCGuZljcZIyd9e1rYQgWgViB%2FpwWRwLTzFLUuTrMMhz23sp9JDevSYDwWMzaFNhNIW5aGU52OJ%2BQQkDmGU4rCSbZsNHNxYo%2BLbvVaiXzgCkmJ3i3ZGm2E%2BYFcGBd9%2BvuZd3BJ7m%2FCSMlVB%2BaBV2GADzGha3%2FQ50yoAV9T7vnuAg&X-Amz-Signature=145dfc064b4d5058ef82e2415c742a24dec2170ba032aa8832bccd18b053cb09&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EQ74DQO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAqNwLnhJIcZ5A1Nwuan%2BFUaUjWTq9%2Frea%2FkP5h1XJ0GAiEArq9P75bbJe58kbKALm7HcVFK%2BDv14cdgkbw1QhGbfDMqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUOmwTpYtqUC%2Fy4rircA4bltDiuDOnuKnwgGrvul2Uq%2BcFteVBSShfoNC%2FB7F6ir909yJR%2FLpRAByGg9FhzKIUKp9Pnw%2Brx%2B8clpWoPl15bAkk9v%2F7T%2Fvey0BaRPCQidG4PUirdVCJxJKyApo6327Pt7yIsTPMsREFINkySu7BYRk%2BAvfeaDyL%2BG3MFjwtB0XuYKQOQeGNv8RUbSyPWHrlcTHgpTFYOCc7r7JrKt9pEx4i87%2BvdMsq44ChASdZGjCbPicE9DkBTEuHw6gD38Gofd5erF%2Bsbx4XvYghl%2BgbI52Iu2R3HCLU4hCqCUem4MHrWpI1XVW6UNfThsjqIPETpPuR0eKDTC1cad52YZcW5i2ImPwy9Vf%2BZRl3zdxv2ODPSFiKudd0p7WUxeYFVSNBCRcsabq9PvJsamtvtcNVJN6lEUxIn%2B9NVjYfMWYEJSz20sd%2FjfjPbz8F%2B81kw5htRuXNC5M2PzwlSMBk8zYzwDL%2B6R7Vn%2BfX6yosN%2F9GvY8E4oTPUAwR9FYa0aYGRPjM4nB0kbZwWn13ntwq%2FpDgDOFc9593XoieEUZKSKyWVVsMh7Hut9ohtSC%2FArtydOokenHDvE%2Bud7J1tptawDP5rPqim3Zuj96SiOHPfElg8VlfEdCo9UJX%2FpUMBMK7Y6bwGOqUBdcaMsczU3ALq2ZtLCE7hf73ll5iCX8h5xB1ZfbxutLinho6Tj3WjTfpEu9pe5chbjZdYJfhDqb1N2m2D6WpBxukO759pQhclESEq%2B8fT%2FTNf%2BiGkvNO4aPeV0f1j9CcdkWMajuztuAdJ1KjWuKGYCCyS5TTCDq0fcqMeDbFdU6E5QnxPUniCdXgHP3nN31QnrpupOkdtAGI61QFkM%2BXJZA7e3Ktb&X-Amz-Signature=56cd40c83af6df1a9f5b6b6c69566db7018fd786faedbdbe7b83ab22429a7ecf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EQ74DQO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAqNwLnhJIcZ5A1Nwuan%2BFUaUjWTq9%2Frea%2FkP5h1XJ0GAiEArq9P75bbJe58kbKALm7HcVFK%2BDv14cdgkbw1QhGbfDMqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUOmwTpYtqUC%2Fy4rircA4bltDiuDOnuKnwgGrvul2Uq%2BcFteVBSShfoNC%2FB7F6ir909yJR%2FLpRAByGg9FhzKIUKp9Pnw%2Brx%2B8clpWoPl15bAkk9v%2F7T%2Fvey0BaRPCQidG4PUirdVCJxJKyApo6327Pt7yIsTPMsREFINkySu7BYRk%2BAvfeaDyL%2BG3MFjwtB0XuYKQOQeGNv8RUbSyPWHrlcTHgpTFYOCc7r7JrKt9pEx4i87%2BvdMsq44ChASdZGjCbPicE9DkBTEuHw6gD38Gofd5erF%2Bsbx4XvYghl%2BgbI52Iu2R3HCLU4hCqCUem4MHrWpI1XVW6UNfThsjqIPETpPuR0eKDTC1cad52YZcW5i2ImPwy9Vf%2BZRl3zdxv2ODPSFiKudd0p7WUxeYFVSNBCRcsabq9PvJsamtvtcNVJN6lEUxIn%2B9NVjYfMWYEJSz20sd%2FjfjPbz8F%2B81kw5htRuXNC5M2PzwlSMBk8zYzwDL%2B6R7Vn%2BfX6yosN%2F9GvY8E4oTPUAwR9FYa0aYGRPjM4nB0kbZwWn13ntwq%2FpDgDOFc9593XoieEUZKSKyWVVsMh7Hut9ohtSC%2FArtydOokenHDvE%2Bud7J1tptawDP5rPqim3Zuj96SiOHPfElg8VlfEdCo9UJX%2FpUMBMK7Y6bwGOqUBdcaMsczU3ALq2ZtLCE7hf73ll5iCX8h5xB1ZfbxutLinho6Tj3WjTfpEu9pe5chbjZdYJfhDqb1N2m2D6WpBxukO759pQhclESEq%2B8fT%2FTNf%2BiGkvNO4aPeV0f1j9CcdkWMajuztuAdJ1KjWuKGYCCyS5TTCDq0fcqMeDbFdU6E5QnxPUniCdXgHP3nN31QnrpupOkdtAGI61QFkM%2BXJZA7e3Ktb&X-Amz-Signature=f8bc6f7ff6a8cd3cca412d9209e8d0604b8ccafbe98156483f707890ebe15142&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EQ74DQO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAqNwLnhJIcZ5A1Nwuan%2BFUaUjWTq9%2Frea%2FkP5h1XJ0GAiEArq9P75bbJe58kbKALm7HcVFK%2BDv14cdgkbw1QhGbfDMqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUOmwTpYtqUC%2Fy4rircA4bltDiuDOnuKnwgGrvul2Uq%2BcFteVBSShfoNC%2FB7F6ir909yJR%2FLpRAByGg9FhzKIUKp9Pnw%2Brx%2B8clpWoPl15bAkk9v%2F7T%2Fvey0BaRPCQidG4PUirdVCJxJKyApo6327Pt7yIsTPMsREFINkySu7BYRk%2BAvfeaDyL%2BG3MFjwtB0XuYKQOQeGNv8RUbSyPWHrlcTHgpTFYOCc7r7JrKt9pEx4i87%2BvdMsq44ChASdZGjCbPicE9DkBTEuHw6gD38Gofd5erF%2Bsbx4XvYghl%2BgbI52Iu2R3HCLU4hCqCUem4MHrWpI1XVW6UNfThsjqIPETpPuR0eKDTC1cad52YZcW5i2ImPwy9Vf%2BZRl3zdxv2ODPSFiKudd0p7WUxeYFVSNBCRcsabq9PvJsamtvtcNVJN6lEUxIn%2B9NVjYfMWYEJSz20sd%2FjfjPbz8F%2B81kw5htRuXNC5M2PzwlSMBk8zYzwDL%2B6R7Vn%2BfX6yosN%2F9GvY8E4oTPUAwR9FYa0aYGRPjM4nB0kbZwWn13ntwq%2FpDgDOFc9593XoieEUZKSKyWVVsMh7Hut9ohtSC%2FArtydOokenHDvE%2Bud7J1tptawDP5rPqim3Zuj96SiOHPfElg8VlfEdCo9UJX%2FpUMBMK7Y6bwGOqUBdcaMsczU3ALq2ZtLCE7hf73ll5iCX8h5xB1ZfbxutLinho6Tj3WjTfpEu9pe5chbjZdYJfhDqb1N2m2D6WpBxukO759pQhclESEq%2B8fT%2FTNf%2BiGkvNO4aPeV0f1j9CcdkWMajuztuAdJ1KjWuKGYCCyS5TTCDq0fcqMeDbFdU6E5QnxPUniCdXgHP3nN31QnrpupOkdtAGI61QFkM%2BXJZA7e3Ktb&X-Amz-Signature=1def5abb42c2bde417b1a15e1ce34f0d66c2e40467808b088435c191464f4249&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EQ74DQO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAqNwLnhJIcZ5A1Nwuan%2BFUaUjWTq9%2Frea%2FkP5h1XJ0GAiEArq9P75bbJe58kbKALm7HcVFK%2BDv14cdgkbw1QhGbfDMqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUOmwTpYtqUC%2Fy4rircA4bltDiuDOnuKnwgGrvul2Uq%2BcFteVBSShfoNC%2FB7F6ir909yJR%2FLpRAByGg9FhzKIUKp9Pnw%2Brx%2B8clpWoPl15bAkk9v%2F7T%2Fvey0BaRPCQidG4PUirdVCJxJKyApo6327Pt7yIsTPMsREFINkySu7BYRk%2BAvfeaDyL%2BG3MFjwtB0XuYKQOQeGNv8RUbSyPWHrlcTHgpTFYOCc7r7JrKt9pEx4i87%2BvdMsq44ChASdZGjCbPicE9DkBTEuHw6gD38Gofd5erF%2Bsbx4XvYghl%2BgbI52Iu2R3HCLU4hCqCUem4MHrWpI1XVW6UNfThsjqIPETpPuR0eKDTC1cad52YZcW5i2ImPwy9Vf%2BZRl3zdxv2ODPSFiKudd0p7WUxeYFVSNBCRcsabq9PvJsamtvtcNVJN6lEUxIn%2B9NVjYfMWYEJSz20sd%2FjfjPbz8F%2B81kw5htRuXNC5M2PzwlSMBk8zYzwDL%2B6R7Vn%2BfX6yosN%2F9GvY8E4oTPUAwR9FYa0aYGRPjM4nB0kbZwWn13ntwq%2FpDgDOFc9593XoieEUZKSKyWVVsMh7Hut9ohtSC%2FArtydOokenHDvE%2Bud7J1tptawDP5rPqim3Zuj96SiOHPfElg8VlfEdCo9UJX%2FpUMBMK7Y6bwGOqUBdcaMsczU3ALq2ZtLCE7hf73ll5iCX8h5xB1ZfbxutLinho6Tj3WjTfpEu9pe5chbjZdYJfhDqb1N2m2D6WpBxukO759pQhclESEq%2B8fT%2FTNf%2BiGkvNO4aPeV0f1j9CcdkWMajuztuAdJ1KjWuKGYCCyS5TTCDq0fcqMeDbFdU6E5QnxPUniCdXgHP3nN31QnrpupOkdtAGI61QFkM%2BXJZA7e3Ktb&X-Amz-Signature=1c7330f292fa95f5e4f2c1be54977cf0a917e6371cb893e118978643f208ccf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EQ74DQO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAqNwLnhJIcZ5A1Nwuan%2BFUaUjWTq9%2Frea%2FkP5h1XJ0GAiEArq9P75bbJe58kbKALm7HcVFK%2BDv14cdgkbw1QhGbfDMqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUOmwTpYtqUC%2Fy4rircA4bltDiuDOnuKnwgGrvul2Uq%2BcFteVBSShfoNC%2FB7F6ir909yJR%2FLpRAByGg9FhzKIUKp9Pnw%2Brx%2B8clpWoPl15bAkk9v%2F7T%2Fvey0BaRPCQidG4PUirdVCJxJKyApo6327Pt7yIsTPMsREFINkySu7BYRk%2BAvfeaDyL%2BG3MFjwtB0XuYKQOQeGNv8RUbSyPWHrlcTHgpTFYOCc7r7JrKt9pEx4i87%2BvdMsq44ChASdZGjCbPicE9DkBTEuHw6gD38Gofd5erF%2Bsbx4XvYghl%2BgbI52Iu2R3HCLU4hCqCUem4MHrWpI1XVW6UNfThsjqIPETpPuR0eKDTC1cad52YZcW5i2ImPwy9Vf%2BZRl3zdxv2ODPSFiKudd0p7WUxeYFVSNBCRcsabq9PvJsamtvtcNVJN6lEUxIn%2B9NVjYfMWYEJSz20sd%2FjfjPbz8F%2B81kw5htRuXNC5M2PzwlSMBk8zYzwDL%2B6R7Vn%2BfX6yosN%2F9GvY8E4oTPUAwR9FYa0aYGRPjM4nB0kbZwWn13ntwq%2FpDgDOFc9593XoieEUZKSKyWVVsMh7Hut9ohtSC%2FArtydOokenHDvE%2Bud7J1tptawDP5rPqim3Zuj96SiOHPfElg8VlfEdCo9UJX%2FpUMBMK7Y6bwGOqUBdcaMsczU3ALq2ZtLCE7hf73ll5iCX8h5xB1ZfbxutLinho6Tj3WjTfpEu9pe5chbjZdYJfhDqb1N2m2D6WpBxukO759pQhclESEq%2B8fT%2FTNf%2BiGkvNO4aPeV0f1j9CcdkWMajuztuAdJ1KjWuKGYCCyS5TTCDq0fcqMeDbFdU6E5QnxPUniCdXgHP3nN31QnrpupOkdtAGI61QFkM%2BXJZA7e3Ktb&X-Amz-Signature=e8e2507e71a4a46ef436974c6898c41d46478b247fa050be9c8b84822e2f16f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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


