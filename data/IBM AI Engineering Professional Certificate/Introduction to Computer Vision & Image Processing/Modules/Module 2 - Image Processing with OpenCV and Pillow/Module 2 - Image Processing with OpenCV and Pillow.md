

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DHPRHEB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIHDNWR9dqpIox17SfcsuAwIWxKaAogRPAmFB%2F7UGRFXFAiAH6WgPUmu%2FmzaLcDT7r1xupJkQvkGh6pBvYrCJT%2Fihjir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIMe2AU%2B%2Fwx%2FAL3CzBJKtwDeMmisnbn1yW7Pj3pAbDu%2BrvWUVjTDdACqJdW0IyvBMJ41iouravZlj%2FuYgGy5x376gFer%2FrQqVSigQOIRmyZkyqay18uBLx0UAG5DCWowUTummH%2Fo41L0DYfXr8QtTzPzSwBK87QC5p9ZrkEw%2B7813d4Lu74ChnKmxNX%2Bxg%2BE6gXnCh4%2BUxrFWSff2fZoikskJQYF%2FB6qYs%2FhRT8jyAbQCstq%2FcMESvBTsHLLQjdArBW0aO7FnIhyzJ4y0CcEOyNsRHINrDAjbXWFDl%2BnFcmUhPwKDye3TqcGZoE8i2qyJDGryU3Y%2BoYztT4Arj3TdE0ZdqUtOOy6y%2F%2FdYyl8gNz%2Bp%2BbDDKiEUyni6SF%2BJGAHzlwbKFdX%2B2ZN5YmD%2BINQ4AhI7EQlWmhzmKyjU6mzYla2ipfNzMvocfAM9DN8XNbAxeEw2PgkQGM%2Ft0xbQTOYy1oQMS%2BYSF8OPcCyR4Pa%2FBjcwaVFtiGVISliqo2vIfGiy15xLJmtP1rTZOTsTcAIzV%2B8wQogUHX7%2FJWdOlADp0D4xKovkg6rz64BQWhI4NTw3XhKNNBv7PJb%2BMhA8tBhjiLYHKXYBC0zqAqEJa1qFBv6XD9bkCV7BO2kN09P0m3wfff7dox8kWzb0l3zP4whaGWvQY6pgG1bWiWdL%2FNuPT9LA2ir11gXvcbl7T6vD3yIm%2F9pcuzf3Lj2lv1ss1wrQNu78uT7fFHlDrwozlh5qqDlUumMX%2BofG3yHk4dImlKgTzRA4FCRhNsI%2F9%2FFWqQaMDoxYyQkMkTHDCOQXmxaKYeLBXpFIfPNXWY0BqkQ%2FdxLjPPWpRIDYgi1rla7Rlgg2agAsJHAItcrVCmbLL8BpWWRqnwA%2F79m6tJWriC&X-Amz-Signature=3dd4d2c10d23c01babb3f08b5c318c646cb0ecc1a9212b02393a3c56a9a64392&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MCN754P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCH26WD3Vtg6K7vv3KiKKk4BWK69XxYoPk3bIDXg03kZAIhAPnCOCH05EY67H0hCprJHozoJ%2BAxCcwxbsVla2HL6igeKv8DCG4QABoMNjM3NDIzMTgzODA1IgzVplEumuLMn11EbC8q3AP3hWkbwuLedPvuumdqQLJsDfe2%2FX%2BVrLdE0MzlwZZhs6kpcHduGwXVdm%2BJcJOdQvOpyulzmFGnLj%2Bw4nDrjYoJsxYAiLZu4x8Ss4DGg7joAGwA3w2ngYqD4UCsMwn6db5OXUnA4WYNBhdTfYWsFZUHuIb90Cfz4Mx4SWOXgYgePsQhusmVZMiV9Xf2pMCLe8vFCM%2BtC3D8MR1BYwHjXA5Kc5yPFnrvJGXxG%2FL%2Be6LP1oVpWVEX570Kz3XsEdmI2VhzMytZz%2BjeVDhqaCebjE52V69m0KRy13%2BGHFdFdgUGPF%2F%2FhTumfPrz3e%2FyzGL8tPRjmVRXXn5KUlJZ91QiUnb6MJs43LjQrWzLbAGu4xd9H6olHZ6v%2FtsZIVspIzE38vwUAyVJPApTPgmH%2F91wAA0kKEcf2xVI3u%2BJOLaVaZWNogYXohK8JGFmc8Ux1Su5MpxSZsh9uDMxJ9qUs5zuKjtKASutvvDqhZaw%2BLlMxKHTs%2FTi4WQtt5CfoXMLempNyl9hBNie79BISyEWilBNHpVovjaNarPZ1VgNRH8fN%2FGu%2B9tl91mprp%2B23SVp9TkUsrV1Ps28YO9sGN3OtTXx%2B9a5NqLj4ORQbVGeXCNmC5aLcmF7em6K7VBlYXWTQDCsoZa9BjqkAdz7cSRv00kEd9r%2BxFWiqjzK5oH%2FeR1IVKj0NOcTP3MOjnxKsumHpeZ0hqfutHKUyuZVNNHb%2B9cb62lhJPGCREtSx1hDhKO6ge3F4txqDI744HxuO9KgspZmtoYI73MxXv1LOdhpIarMg%2FbFkgCfVGnhZPBTXTat8RoTezYnkcwxmiOQN7eclcSQCaM1yKi6j8xyoo05wElvLByAGeX%2FtezpnwWs&X-Amz-Signature=39d1195b1bd47f82ea7fa36622882fd4dbfc7f0f8dfc936c0c716b38f57926f5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MCN754P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCH26WD3Vtg6K7vv3KiKKk4BWK69XxYoPk3bIDXg03kZAIhAPnCOCH05EY67H0hCprJHozoJ%2BAxCcwxbsVla2HL6igeKv8DCG4QABoMNjM3NDIzMTgzODA1IgzVplEumuLMn11EbC8q3AP3hWkbwuLedPvuumdqQLJsDfe2%2FX%2BVrLdE0MzlwZZhs6kpcHduGwXVdm%2BJcJOdQvOpyulzmFGnLj%2Bw4nDrjYoJsxYAiLZu4x8Ss4DGg7joAGwA3w2ngYqD4UCsMwn6db5OXUnA4WYNBhdTfYWsFZUHuIb90Cfz4Mx4SWOXgYgePsQhusmVZMiV9Xf2pMCLe8vFCM%2BtC3D8MR1BYwHjXA5Kc5yPFnrvJGXxG%2FL%2Be6LP1oVpWVEX570Kz3XsEdmI2VhzMytZz%2BjeVDhqaCebjE52V69m0KRy13%2BGHFdFdgUGPF%2F%2FhTumfPrz3e%2FyzGL8tPRjmVRXXn5KUlJZ91QiUnb6MJs43LjQrWzLbAGu4xd9H6olHZ6v%2FtsZIVspIzE38vwUAyVJPApTPgmH%2F91wAA0kKEcf2xVI3u%2BJOLaVaZWNogYXohK8JGFmc8Ux1Su5MpxSZsh9uDMxJ9qUs5zuKjtKASutvvDqhZaw%2BLlMxKHTs%2FTi4WQtt5CfoXMLempNyl9hBNie79BISyEWilBNHpVovjaNarPZ1VgNRH8fN%2FGu%2B9tl91mprp%2B23SVp9TkUsrV1Ps28YO9sGN3OtTXx%2B9a5NqLj4ORQbVGeXCNmC5aLcmF7em6K7VBlYXWTQDCsoZa9BjqkAdz7cSRv00kEd9r%2BxFWiqjzK5oH%2FeR1IVKj0NOcTP3MOjnxKsumHpeZ0hqfutHKUyuZVNNHb%2B9cb62lhJPGCREtSx1hDhKO6ge3F4txqDI744HxuO9KgspZmtoYI73MxXv1LOdhpIarMg%2FbFkgCfVGnhZPBTXTat8RoTezYnkcwxmiOQN7eclcSQCaM1yKi6j8xyoo05wElvLByAGeX%2FtezpnwWs&X-Amz-Signature=20103dc0cd5fdbea13be0bde44aaeec7bd64380d50e75e08e4cb57c3adcbb63b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MCN754P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCH26WD3Vtg6K7vv3KiKKk4BWK69XxYoPk3bIDXg03kZAIhAPnCOCH05EY67H0hCprJHozoJ%2BAxCcwxbsVla2HL6igeKv8DCG4QABoMNjM3NDIzMTgzODA1IgzVplEumuLMn11EbC8q3AP3hWkbwuLedPvuumdqQLJsDfe2%2FX%2BVrLdE0MzlwZZhs6kpcHduGwXVdm%2BJcJOdQvOpyulzmFGnLj%2Bw4nDrjYoJsxYAiLZu4x8Ss4DGg7joAGwA3w2ngYqD4UCsMwn6db5OXUnA4WYNBhdTfYWsFZUHuIb90Cfz4Mx4SWOXgYgePsQhusmVZMiV9Xf2pMCLe8vFCM%2BtC3D8MR1BYwHjXA5Kc5yPFnrvJGXxG%2FL%2Be6LP1oVpWVEX570Kz3XsEdmI2VhzMytZz%2BjeVDhqaCebjE52V69m0KRy13%2BGHFdFdgUGPF%2F%2FhTumfPrz3e%2FyzGL8tPRjmVRXXn5KUlJZ91QiUnb6MJs43LjQrWzLbAGu4xd9H6olHZ6v%2FtsZIVspIzE38vwUAyVJPApTPgmH%2F91wAA0kKEcf2xVI3u%2BJOLaVaZWNogYXohK8JGFmc8Ux1Su5MpxSZsh9uDMxJ9qUs5zuKjtKASutvvDqhZaw%2BLlMxKHTs%2FTi4WQtt5CfoXMLempNyl9hBNie79BISyEWilBNHpVovjaNarPZ1VgNRH8fN%2FGu%2B9tl91mprp%2B23SVp9TkUsrV1Ps28YO9sGN3OtTXx%2B9a5NqLj4ORQbVGeXCNmC5aLcmF7em6K7VBlYXWTQDCsoZa9BjqkAdz7cSRv00kEd9r%2BxFWiqjzK5oH%2FeR1IVKj0NOcTP3MOjnxKsumHpeZ0hqfutHKUyuZVNNHb%2B9cb62lhJPGCREtSx1hDhKO6ge3F4txqDI744HxuO9KgspZmtoYI73MxXv1LOdhpIarMg%2FbFkgCfVGnhZPBTXTat8RoTezYnkcwxmiOQN7eclcSQCaM1yKi6j8xyoo05wElvLByAGeX%2FtezpnwWs&X-Amz-Signature=0eb955a2cf85736eb53fc99b5a4bf89b9fca430768f8841c45f38dd00ad24124&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MCN754P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCH26WD3Vtg6K7vv3KiKKk4BWK69XxYoPk3bIDXg03kZAIhAPnCOCH05EY67H0hCprJHozoJ%2BAxCcwxbsVla2HL6igeKv8DCG4QABoMNjM3NDIzMTgzODA1IgzVplEumuLMn11EbC8q3AP3hWkbwuLedPvuumdqQLJsDfe2%2FX%2BVrLdE0MzlwZZhs6kpcHduGwXVdm%2BJcJOdQvOpyulzmFGnLj%2Bw4nDrjYoJsxYAiLZu4x8Ss4DGg7joAGwA3w2ngYqD4UCsMwn6db5OXUnA4WYNBhdTfYWsFZUHuIb90Cfz4Mx4SWOXgYgePsQhusmVZMiV9Xf2pMCLe8vFCM%2BtC3D8MR1BYwHjXA5Kc5yPFnrvJGXxG%2FL%2Be6LP1oVpWVEX570Kz3XsEdmI2VhzMytZz%2BjeVDhqaCebjE52V69m0KRy13%2BGHFdFdgUGPF%2F%2FhTumfPrz3e%2FyzGL8tPRjmVRXXn5KUlJZ91QiUnb6MJs43LjQrWzLbAGu4xd9H6olHZ6v%2FtsZIVspIzE38vwUAyVJPApTPgmH%2F91wAA0kKEcf2xVI3u%2BJOLaVaZWNogYXohK8JGFmc8Ux1Su5MpxSZsh9uDMxJ9qUs5zuKjtKASutvvDqhZaw%2BLlMxKHTs%2FTi4WQtt5CfoXMLempNyl9hBNie79BISyEWilBNHpVovjaNarPZ1VgNRH8fN%2FGu%2B9tl91mprp%2B23SVp9TkUsrV1Ps28YO9sGN3OtTXx%2B9a5NqLj4ORQbVGeXCNmC5aLcmF7em6K7VBlYXWTQDCsoZa9BjqkAdz7cSRv00kEd9r%2BxFWiqjzK5oH%2FeR1IVKj0NOcTP3MOjnxKsumHpeZ0hqfutHKUyuZVNNHb%2B9cb62lhJPGCREtSx1hDhKO6ge3F4txqDI744HxuO9KgspZmtoYI73MxXv1LOdhpIarMg%2FbFkgCfVGnhZPBTXTat8RoTezYnkcwxmiOQN7eclcSQCaM1yKi6j8xyoo05wElvLByAGeX%2FtezpnwWs&X-Amz-Signature=c1894093fdc9703943a22d579e880e550fa38937551dc1608c1c9b73ebe887af&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MCN754P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCH26WD3Vtg6K7vv3KiKKk4BWK69XxYoPk3bIDXg03kZAIhAPnCOCH05EY67H0hCprJHozoJ%2BAxCcwxbsVla2HL6igeKv8DCG4QABoMNjM3NDIzMTgzODA1IgzVplEumuLMn11EbC8q3AP3hWkbwuLedPvuumdqQLJsDfe2%2FX%2BVrLdE0MzlwZZhs6kpcHduGwXVdm%2BJcJOdQvOpyulzmFGnLj%2Bw4nDrjYoJsxYAiLZu4x8Ss4DGg7joAGwA3w2ngYqD4UCsMwn6db5OXUnA4WYNBhdTfYWsFZUHuIb90Cfz4Mx4SWOXgYgePsQhusmVZMiV9Xf2pMCLe8vFCM%2BtC3D8MR1BYwHjXA5Kc5yPFnrvJGXxG%2FL%2Be6LP1oVpWVEX570Kz3XsEdmI2VhzMytZz%2BjeVDhqaCebjE52V69m0KRy13%2BGHFdFdgUGPF%2F%2FhTumfPrz3e%2FyzGL8tPRjmVRXXn5KUlJZ91QiUnb6MJs43LjQrWzLbAGu4xd9H6olHZ6v%2FtsZIVspIzE38vwUAyVJPApTPgmH%2F91wAA0kKEcf2xVI3u%2BJOLaVaZWNogYXohK8JGFmc8Ux1Su5MpxSZsh9uDMxJ9qUs5zuKjtKASutvvDqhZaw%2BLlMxKHTs%2FTi4WQtt5CfoXMLempNyl9hBNie79BISyEWilBNHpVovjaNarPZ1VgNRH8fN%2FGu%2B9tl91mprp%2B23SVp9TkUsrV1Ps28YO9sGN3OtTXx%2B9a5NqLj4ORQbVGeXCNmC5aLcmF7em6K7VBlYXWTQDCsoZa9BjqkAdz7cSRv00kEd9r%2BxFWiqjzK5oH%2FeR1IVKj0NOcTP3MOjnxKsumHpeZ0hqfutHKUyuZVNNHb%2B9cb62lhJPGCREtSx1hDhKO6ge3F4txqDI744HxuO9KgspZmtoYI73MxXv1LOdhpIarMg%2FbFkgCfVGnhZPBTXTat8RoTezYnkcwxmiOQN7eclcSQCaM1yKi6j8xyoo05wElvLByAGeX%2FtezpnwWs&X-Amz-Signature=a97fb688c581ed3c0c1a22cf720f62ccf776d07b280f799d23e074580e468bc7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DHPRHEB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIHDNWR9dqpIox17SfcsuAwIWxKaAogRPAmFB%2F7UGRFXFAiAH6WgPUmu%2FmzaLcDT7r1xupJkQvkGh6pBvYrCJT%2Fihjir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIMe2AU%2B%2Fwx%2FAL3CzBJKtwDeMmisnbn1yW7Pj3pAbDu%2BrvWUVjTDdACqJdW0IyvBMJ41iouravZlj%2FuYgGy5x376gFer%2FrQqVSigQOIRmyZkyqay18uBLx0UAG5DCWowUTummH%2Fo41L0DYfXr8QtTzPzSwBK87QC5p9ZrkEw%2B7813d4Lu74ChnKmxNX%2Bxg%2BE6gXnCh4%2BUxrFWSff2fZoikskJQYF%2FB6qYs%2FhRT8jyAbQCstq%2FcMESvBTsHLLQjdArBW0aO7FnIhyzJ4y0CcEOyNsRHINrDAjbXWFDl%2BnFcmUhPwKDye3TqcGZoE8i2qyJDGryU3Y%2BoYztT4Arj3TdE0ZdqUtOOy6y%2F%2FdYyl8gNz%2Bp%2BbDDKiEUyni6SF%2BJGAHzlwbKFdX%2B2ZN5YmD%2BINQ4AhI7EQlWmhzmKyjU6mzYla2ipfNzMvocfAM9DN8XNbAxeEw2PgkQGM%2Ft0xbQTOYy1oQMS%2BYSF8OPcCyR4Pa%2FBjcwaVFtiGVISliqo2vIfGiy15xLJmtP1rTZOTsTcAIzV%2B8wQogUHX7%2FJWdOlADp0D4xKovkg6rz64BQWhI4NTw3XhKNNBv7PJb%2BMhA8tBhjiLYHKXYBC0zqAqEJa1qFBv6XD9bkCV7BO2kN09P0m3wfff7dox8kWzb0l3zP4whaGWvQY6pgG1bWiWdL%2FNuPT9LA2ir11gXvcbl7T6vD3yIm%2F9pcuzf3Lj2lv1ss1wrQNu78uT7fFHlDrwozlh5qqDlUumMX%2BofG3yHk4dImlKgTzRA4FCRhNsI%2F9%2FFWqQaMDoxYyQkMkTHDCOQXmxaKYeLBXpFIfPNXWY0BqkQ%2FdxLjPPWpRIDYgi1rla7Rlgg2agAsJHAItcrVCmbLL8BpWWRqnwA%2F79m6tJWriC&X-Amz-Signature=52b65aee9ab3a9a19a44cd1f88a46d0fb9f5f083518f4864116ecf6a230c5c3d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DHPRHEB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIHDNWR9dqpIox17SfcsuAwIWxKaAogRPAmFB%2F7UGRFXFAiAH6WgPUmu%2FmzaLcDT7r1xupJkQvkGh6pBvYrCJT%2Fihjir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIMe2AU%2B%2Fwx%2FAL3CzBJKtwDeMmisnbn1yW7Pj3pAbDu%2BrvWUVjTDdACqJdW0IyvBMJ41iouravZlj%2FuYgGy5x376gFer%2FrQqVSigQOIRmyZkyqay18uBLx0UAG5DCWowUTummH%2Fo41L0DYfXr8QtTzPzSwBK87QC5p9ZrkEw%2B7813d4Lu74ChnKmxNX%2Bxg%2BE6gXnCh4%2BUxrFWSff2fZoikskJQYF%2FB6qYs%2FhRT8jyAbQCstq%2FcMESvBTsHLLQjdArBW0aO7FnIhyzJ4y0CcEOyNsRHINrDAjbXWFDl%2BnFcmUhPwKDye3TqcGZoE8i2qyJDGryU3Y%2BoYztT4Arj3TdE0ZdqUtOOy6y%2F%2FdYyl8gNz%2Bp%2BbDDKiEUyni6SF%2BJGAHzlwbKFdX%2B2ZN5YmD%2BINQ4AhI7EQlWmhzmKyjU6mzYla2ipfNzMvocfAM9DN8XNbAxeEw2PgkQGM%2Ft0xbQTOYy1oQMS%2BYSF8OPcCyR4Pa%2FBjcwaVFtiGVISliqo2vIfGiy15xLJmtP1rTZOTsTcAIzV%2B8wQogUHX7%2FJWdOlADp0D4xKovkg6rz64BQWhI4NTw3XhKNNBv7PJb%2BMhA8tBhjiLYHKXYBC0zqAqEJa1qFBv6XD9bkCV7BO2kN09P0m3wfff7dox8kWzb0l3zP4whaGWvQY6pgG1bWiWdL%2FNuPT9LA2ir11gXvcbl7T6vD3yIm%2F9pcuzf3Lj2lv1ss1wrQNu78uT7fFHlDrwozlh5qqDlUumMX%2BofG3yHk4dImlKgTzRA4FCRhNsI%2F9%2FFWqQaMDoxYyQkMkTHDCOQXmxaKYeLBXpFIfPNXWY0BqkQ%2FdxLjPPWpRIDYgi1rla7Rlgg2agAsJHAItcrVCmbLL8BpWWRqnwA%2F79m6tJWriC&X-Amz-Signature=8d34f402e5d83251d823d17fa6731e58eddd9e50dd18335964cc8ed6b9a0016e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DHPRHEB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIHDNWR9dqpIox17SfcsuAwIWxKaAogRPAmFB%2F7UGRFXFAiAH6WgPUmu%2FmzaLcDT7r1xupJkQvkGh6pBvYrCJT%2Fihjir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIMe2AU%2B%2Fwx%2FAL3CzBJKtwDeMmisnbn1yW7Pj3pAbDu%2BrvWUVjTDdACqJdW0IyvBMJ41iouravZlj%2FuYgGy5x376gFer%2FrQqVSigQOIRmyZkyqay18uBLx0UAG5DCWowUTummH%2Fo41L0DYfXr8QtTzPzSwBK87QC5p9ZrkEw%2B7813d4Lu74ChnKmxNX%2Bxg%2BE6gXnCh4%2BUxrFWSff2fZoikskJQYF%2FB6qYs%2FhRT8jyAbQCstq%2FcMESvBTsHLLQjdArBW0aO7FnIhyzJ4y0CcEOyNsRHINrDAjbXWFDl%2BnFcmUhPwKDye3TqcGZoE8i2qyJDGryU3Y%2BoYztT4Arj3TdE0ZdqUtOOy6y%2F%2FdYyl8gNz%2Bp%2BbDDKiEUyni6SF%2BJGAHzlwbKFdX%2B2ZN5YmD%2BINQ4AhI7EQlWmhzmKyjU6mzYla2ipfNzMvocfAM9DN8XNbAxeEw2PgkQGM%2Ft0xbQTOYy1oQMS%2BYSF8OPcCyR4Pa%2FBjcwaVFtiGVISliqo2vIfGiy15xLJmtP1rTZOTsTcAIzV%2B8wQogUHX7%2FJWdOlADp0D4xKovkg6rz64BQWhI4NTw3XhKNNBv7PJb%2BMhA8tBhjiLYHKXYBC0zqAqEJa1qFBv6XD9bkCV7BO2kN09P0m3wfff7dox8kWzb0l3zP4whaGWvQY6pgG1bWiWdL%2FNuPT9LA2ir11gXvcbl7T6vD3yIm%2F9pcuzf3Lj2lv1ss1wrQNu78uT7fFHlDrwozlh5qqDlUumMX%2BofG3yHk4dImlKgTzRA4FCRhNsI%2F9%2FFWqQaMDoxYyQkMkTHDCOQXmxaKYeLBXpFIfPNXWY0BqkQ%2FdxLjPPWpRIDYgi1rla7Rlgg2agAsJHAItcrVCmbLL8BpWWRqnwA%2F79m6tJWriC&X-Amz-Signature=3c52594284cfafdf631bb3032e310f90b5bc0188fffe3d1ba383b96d1c9af403&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DHPRHEB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIHDNWR9dqpIox17SfcsuAwIWxKaAogRPAmFB%2F7UGRFXFAiAH6WgPUmu%2FmzaLcDT7r1xupJkQvkGh6pBvYrCJT%2Fihjir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIMe2AU%2B%2Fwx%2FAL3CzBJKtwDeMmisnbn1yW7Pj3pAbDu%2BrvWUVjTDdACqJdW0IyvBMJ41iouravZlj%2FuYgGy5x376gFer%2FrQqVSigQOIRmyZkyqay18uBLx0UAG5DCWowUTummH%2Fo41L0DYfXr8QtTzPzSwBK87QC5p9ZrkEw%2B7813d4Lu74ChnKmxNX%2Bxg%2BE6gXnCh4%2BUxrFWSff2fZoikskJQYF%2FB6qYs%2FhRT8jyAbQCstq%2FcMESvBTsHLLQjdArBW0aO7FnIhyzJ4y0CcEOyNsRHINrDAjbXWFDl%2BnFcmUhPwKDye3TqcGZoE8i2qyJDGryU3Y%2BoYztT4Arj3TdE0ZdqUtOOy6y%2F%2FdYyl8gNz%2Bp%2BbDDKiEUyni6SF%2BJGAHzlwbKFdX%2B2ZN5YmD%2BINQ4AhI7EQlWmhzmKyjU6mzYla2ipfNzMvocfAM9DN8XNbAxeEw2PgkQGM%2Ft0xbQTOYy1oQMS%2BYSF8OPcCyR4Pa%2FBjcwaVFtiGVISliqo2vIfGiy15xLJmtP1rTZOTsTcAIzV%2B8wQogUHX7%2FJWdOlADp0D4xKovkg6rz64BQWhI4NTw3XhKNNBv7PJb%2BMhA8tBhjiLYHKXYBC0zqAqEJa1qFBv6XD9bkCV7BO2kN09P0m3wfff7dox8kWzb0l3zP4whaGWvQY6pgG1bWiWdL%2FNuPT9LA2ir11gXvcbl7T6vD3yIm%2F9pcuzf3Lj2lv1ss1wrQNu78uT7fFHlDrwozlh5qqDlUumMX%2BofG3yHk4dImlKgTzRA4FCRhNsI%2F9%2FFWqQaMDoxYyQkMkTHDCOQXmxaKYeLBXpFIfPNXWY0BqkQ%2FdxLjPPWpRIDYgi1rla7Rlgg2agAsJHAItcrVCmbLL8BpWWRqnwA%2F79m6tJWriC&X-Amz-Signature=447b735265f0214de39861b3a1805db5646c7e8c6b40f53295d5afff0788b7f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DHPRHEB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIHDNWR9dqpIox17SfcsuAwIWxKaAogRPAmFB%2F7UGRFXFAiAH6WgPUmu%2FmzaLcDT7r1xupJkQvkGh6pBvYrCJT%2Fihjir%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIMe2AU%2B%2Fwx%2FAL3CzBJKtwDeMmisnbn1yW7Pj3pAbDu%2BrvWUVjTDdACqJdW0IyvBMJ41iouravZlj%2FuYgGy5x376gFer%2FrQqVSigQOIRmyZkyqay18uBLx0UAG5DCWowUTummH%2Fo41L0DYfXr8QtTzPzSwBK87QC5p9ZrkEw%2B7813d4Lu74ChnKmxNX%2Bxg%2BE6gXnCh4%2BUxrFWSff2fZoikskJQYF%2FB6qYs%2FhRT8jyAbQCstq%2FcMESvBTsHLLQjdArBW0aO7FnIhyzJ4y0CcEOyNsRHINrDAjbXWFDl%2BnFcmUhPwKDye3TqcGZoE8i2qyJDGryU3Y%2BoYztT4Arj3TdE0ZdqUtOOy6y%2F%2FdYyl8gNz%2Bp%2BbDDKiEUyni6SF%2BJGAHzlwbKFdX%2B2ZN5YmD%2BINQ4AhI7EQlWmhzmKyjU6mzYla2ipfNzMvocfAM9DN8XNbAxeEw2PgkQGM%2Ft0xbQTOYy1oQMS%2BYSF8OPcCyR4Pa%2FBjcwaVFtiGVISliqo2vIfGiy15xLJmtP1rTZOTsTcAIzV%2B8wQogUHX7%2FJWdOlADp0D4xKovkg6rz64BQWhI4NTw3XhKNNBv7PJb%2BMhA8tBhjiLYHKXYBC0zqAqEJa1qFBv6XD9bkCV7BO2kN09P0m3wfff7dox8kWzb0l3zP4whaGWvQY6pgG1bWiWdL%2FNuPT9LA2ir11gXvcbl7T6vD3yIm%2F9pcuzf3Lj2lv1ss1wrQNu78uT7fFHlDrwozlh5qqDlUumMX%2BofG3yHk4dImlKgTzRA4FCRhNsI%2F9%2FFWqQaMDoxYyQkMkTHDCOQXmxaKYeLBXpFIfPNXWY0BqkQ%2FdxLjPPWpRIDYgi1rla7Rlgg2agAsJHAItcrVCmbLL8BpWWRqnwA%2F79m6tJWriC&X-Amz-Signature=63ca1cff895e65d06978727924acdcda06f523cc356f86f6559083d2d2f4cae5&X-Amz-SignedHeaders=host&x-id=GetObject)
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


