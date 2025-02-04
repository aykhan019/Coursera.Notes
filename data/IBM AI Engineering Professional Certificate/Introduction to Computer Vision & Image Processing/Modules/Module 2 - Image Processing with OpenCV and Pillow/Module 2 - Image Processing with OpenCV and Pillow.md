

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF7625C6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIAV7nY%2BQadSQ9MzmNi1C68jCCor8ZBTcH664biwiEz%2BzAiEA59rByt7euPGo2FhmG%2BJY2FNoSbxo%2Bt3yNZDHSDkQqgMq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDOzbesbLF5UBzKbDICrcA6haZyr%2BnIoI1zaj1QoGjorKwT56ukLkygE055R278z7wmcegOoEUAYdbTM44lmXjEVdyzB%2B6QmtIe5bENDFnFh0sBp58qWZGiFTeNqbbH6kXzvJYJkQTpJfvHXaBJ1h1TRK2YKybR53lZLSn4W0KSDcoWZ91modBxry8wq7J8ZrGUFxtZfG4gBt6MYDrE2DfA5AL%2Fu8e7p0AYSPyS6yzl8j1t3n6mXDg5RgvSUo%2FA8Iof8UcLS8toT9MiY9KjSFIve1i2Ky7PHnmn9slOr81qJOjp8eDcUKTZgrunT2oHF03murT9F4hAW6oM74Q%2FsSHL86uobkXS9f6w5kL3vbyXo%2FoIqg1tdKeI9nTz5oYr%2BgT9Vu6LKL1u4GPYZ9rRfFOyWd3FPSZFIWT2ViFB6G4R9hZhYZESK1VJiqeqyDcYUi6KSIYXxtTzwfEVF1jqKNBq8FTO1Uua3Tg3Fl1bf4NDHHoCj%2FAECTRqUtbzRV6Frhe1ZIOTQEo2JLE5FUes2bHZn%2FcwzimhO3EI3BDP6e0N3t1sXv39D%2BSUYwCZxpcqTC9QLEBTxUGD7lv9b69Xz%2B69DTIiKzMwn4zg%2BfvHDfRPqABjrjHJXteoNEFHpx7ZcBcsVcieds3P2w%2BKo3MLHdib0GOqUBYfAIZp6VZsRRqIbbIybzjjgyJ68b4MQO870CmhYqQ%2B%2F%2BzHNTh4WVms%2B3u754FxPQwP4X1K83jN76g%2BFfzRkxFutreHYQ4CwcwKCi67jA5XN6pQDoc3xX2CVNljOSCgrYAuuZMzz3mQ6NOGa5peAMQPu767KJkvRQELF4v%2BI9J4bwAD6e0i3CojS%2F6jpKJTpLkpfma%2F0yY49FWVp9D4WU1f%2BRQ%2B7k&X-Amz-Signature=f6d113a22ffdb93d3af7759a54e17aaf37b27834b84d73a8a433eef4e923859f&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDLWW4OB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDDeMHeiQqmGBK0m%2BnWtzR3sxu9KvG8VfGM6SOwGTMq0gIhAN%2BsyCa1XxqQCDSIFldexpEAgKpXrmPc1vf1LMfCJS%2BSKv8DCDUQABoMNjM3NDIzMTgzODA1IgzzmrLtVOeTbCBZ9E8q3AOOCeDPJE3WJpG8WpFsBl%2BEHzZWq8qDX5Ysm7t5Kyc1a7FPMZ5UksRIbdPG2BG0ABrWBcvNwU40MBm9Vh4hZk%2BsYpNKzQbayVKSHKMQ0zCGXrut4GVFzPFuHxCTE6f83XCajgbg6zrC9xyuc%2FOt%2BVpcbLJFd43Rx7l75zQdd3wBfbyqQGjPhv4BUZayOq0sC8WpmTioyFolLaUJwoMAlHgk4iN7LZ0hOVKpDDCKupTzasYVBJMqibMdOQchdQuO8Ii7d7XjAywF7ku7L32i8s0FjRompYKqWSSbklQzbsjXxiaMeE74qzdTggM9ydutrmliV04sk2v0tDncKAKz2wav7aMp6q%2FweFiVgXizNOlc6zGHTstYzuH9oIGTyXgFxsPKTPdWRW6QNgFHNDNX8i2kzkLFqqS1jHbueEtzKwW4xQoTp1n0MJEl6NI7pOe9oiLtipm0qPks78FdedT9QnI%2BC0pkPUqh78NgZO%2BOxod1Wk5yLERvC%2BNokwwA4rHcQc9BRdFusMGMCSU%2F8CP8M2oG4Xi01QamJQuy6uZxbadA1%2Fd25kIX%2B5oxGMiVGmXWDMYViL4%2Ftx7M0OutUWzJXpxX%2FGwso2yjEtz1cn9xQzRm4nYTFcajtJ1etMWGUjDM3om9BjqkAW%2BNFpFXKsBZZOTsb%2FQgM2cqH69rDBVD%2FnDzNSQZO17jsUVQZf16%2BvDHbcIQjkHe6k62Ui94nuGKb2F%2FeGq%2BQtqAByTWFc19QStHpue4zZ8MryjO7bLjtm5hpXZOXcKcbzHTyESo0rGmBYnCa0WoFW%2BniWJ%2FbHEWLjLSgmF2gfBDbBTSLP9UR8A7kWULPLTse%2BLMxnwpMrAxbErjwlfDE%2FvGp1nE&X-Amz-Signature=9d05a245d135982ba620848f58e81afa671ef010e7ec88ffec83a43caf634152&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDLWW4OB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDDeMHeiQqmGBK0m%2BnWtzR3sxu9KvG8VfGM6SOwGTMq0gIhAN%2BsyCa1XxqQCDSIFldexpEAgKpXrmPc1vf1LMfCJS%2BSKv8DCDUQABoMNjM3NDIzMTgzODA1IgzzmrLtVOeTbCBZ9E8q3AOOCeDPJE3WJpG8WpFsBl%2BEHzZWq8qDX5Ysm7t5Kyc1a7FPMZ5UksRIbdPG2BG0ABrWBcvNwU40MBm9Vh4hZk%2BsYpNKzQbayVKSHKMQ0zCGXrut4GVFzPFuHxCTE6f83XCajgbg6zrC9xyuc%2FOt%2BVpcbLJFd43Rx7l75zQdd3wBfbyqQGjPhv4BUZayOq0sC8WpmTioyFolLaUJwoMAlHgk4iN7LZ0hOVKpDDCKupTzasYVBJMqibMdOQchdQuO8Ii7d7XjAywF7ku7L32i8s0FjRompYKqWSSbklQzbsjXxiaMeE74qzdTggM9ydutrmliV04sk2v0tDncKAKz2wav7aMp6q%2FweFiVgXizNOlc6zGHTstYzuH9oIGTyXgFxsPKTPdWRW6QNgFHNDNX8i2kzkLFqqS1jHbueEtzKwW4xQoTp1n0MJEl6NI7pOe9oiLtipm0qPks78FdedT9QnI%2BC0pkPUqh78NgZO%2BOxod1Wk5yLERvC%2BNokwwA4rHcQc9BRdFusMGMCSU%2F8CP8M2oG4Xi01QamJQuy6uZxbadA1%2Fd25kIX%2B5oxGMiVGmXWDMYViL4%2Ftx7M0OutUWzJXpxX%2FGwso2yjEtz1cn9xQzRm4nYTFcajtJ1etMWGUjDM3om9BjqkAW%2BNFpFXKsBZZOTsb%2FQgM2cqH69rDBVD%2FnDzNSQZO17jsUVQZf16%2BvDHbcIQjkHe6k62Ui94nuGKb2F%2FeGq%2BQtqAByTWFc19QStHpue4zZ8MryjO7bLjtm5hpXZOXcKcbzHTyESo0rGmBYnCa0WoFW%2BniWJ%2FbHEWLjLSgmF2gfBDbBTSLP9UR8A7kWULPLTse%2BLMxnwpMrAxbErjwlfDE%2FvGp1nE&X-Amz-Signature=ffe30a6de49db5023239afc78d78b0549c7cfa3723944f28aa65ed17d6cba5cf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDLWW4OB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDDeMHeiQqmGBK0m%2BnWtzR3sxu9KvG8VfGM6SOwGTMq0gIhAN%2BsyCa1XxqQCDSIFldexpEAgKpXrmPc1vf1LMfCJS%2BSKv8DCDUQABoMNjM3NDIzMTgzODA1IgzzmrLtVOeTbCBZ9E8q3AOOCeDPJE3WJpG8WpFsBl%2BEHzZWq8qDX5Ysm7t5Kyc1a7FPMZ5UksRIbdPG2BG0ABrWBcvNwU40MBm9Vh4hZk%2BsYpNKzQbayVKSHKMQ0zCGXrut4GVFzPFuHxCTE6f83XCajgbg6zrC9xyuc%2FOt%2BVpcbLJFd43Rx7l75zQdd3wBfbyqQGjPhv4BUZayOq0sC8WpmTioyFolLaUJwoMAlHgk4iN7LZ0hOVKpDDCKupTzasYVBJMqibMdOQchdQuO8Ii7d7XjAywF7ku7L32i8s0FjRompYKqWSSbklQzbsjXxiaMeE74qzdTggM9ydutrmliV04sk2v0tDncKAKz2wav7aMp6q%2FweFiVgXizNOlc6zGHTstYzuH9oIGTyXgFxsPKTPdWRW6QNgFHNDNX8i2kzkLFqqS1jHbueEtzKwW4xQoTp1n0MJEl6NI7pOe9oiLtipm0qPks78FdedT9QnI%2BC0pkPUqh78NgZO%2BOxod1Wk5yLERvC%2BNokwwA4rHcQc9BRdFusMGMCSU%2F8CP8M2oG4Xi01QamJQuy6uZxbadA1%2Fd25kIX%2B5oxGMiVGmXWDMYViL4%2Ftx7M0OutUWzJXpxX%2FGwso2yjEtz1cn9xQzRm4nYTFcajtJ1etMWGUjDM3om9BjqkAW%2BNFpFXKsBZZOTsb%2FQgM2cqH69rDBVD%2FnDzNSQZO17jsUVQZf16%2BvDHbcIQjkHe6k62Ui94nuGKb2F%2FeGq%2BQtqAByTWFc19QStHpue4zZ8MryjO7bLjtm5hpXZOXcKcbzHTyESo0rGmBYnCa0WoFW%2BniWJ%2FbHEWLjLSgmF2gfBDbBTSLP9UR8A7kWULPLTse%2BLMxnwpMrAxbErjwlfDE%2FvGp1nE&X-Amz-Signature=e1bbdd071803d572581a379b7179117c7cfbfcee3cee8fffe626046aaaa6cdab&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDLWW4OB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDDeMHeiQqmGBK0m%2BnWtzR3sxu9KvG8VfGM6SOwGTMq0gIhAN%2BsyCa1XxqQCDSIFldexpEAgKpXrmPc1vf1LMfCJS%2BSKv8DCDUQABoMNjM3NDIzMTgzODA1IgzzmrLtVOeTbCBZ9E8q3AOOCeDPJE3WJpG8WpFsBl%2BEHzZWq8qDX5Ysm7t5Kyc1a7FPMZ5UksRIbdPG2BG0ABrWBcvNwU40MBm9Vh4hZk%2BsYpNKzQbayVKSHKMQ0zCGXrut4GVFzPFuHxCTE6f83XCajgbg6zrC9xyuc%2FOt%2BVpcbLJFd43Rx7l75zQdd3wBfbyqQGjPhv4BUZayOq0sC8WpmTioyFolLaUJwoMAlHgk4iN7LZ0hOVKpDDCKupTzasYVBJMqibMdOQchdQuO8Ii7d7XjAywF7ku7L32i8s0FjRompYKqWSSbklQzbsjXxiaMeE74qzdTggM9ydutrmliV04sk2v0tDncKAKz2wav7aMp6q%2FweFiVgXizNOlc6zGHTstYzuH9oIGTyXgFxsPKTPdWRW6QNgFHNDNX8i2kzkLFqqS1jHbueEtzKwW4xQoTp1n0MJEl6NI7pOe9oiLtipm0qPks78FdedT9QnI%2BC0pkPUqh78NgZO%2BOxod1Wk5yLERvC%2BNokwwA4rHcQc9BRdFusMGMCSU%2F8CP8M2oG4Xi01QamJQuy6uZxbadA1%2Fd25kIX%2B5oxGMiVGmXWDMYViL4%2Ftx7M0OutUWzJXpxX%2FGwso2yjEtz1cn9xQzRm4nYTFcajtJ1etMWGUjDM3om9BjqkAW%2BNFpFXKsBZZOTsb%2FQgM2cqH69rDBVD%2FnDzNSQZO17jsUVQZf16%2BvDHbcIQjkHe6k62Ui94nuGKb2F%2FeGq%2BQtqAByTWFc19QStHpue4zZ8MryjO7bLjtm5hpXZOXcKcbzHTyESo0rGmBYnCa0WoFW%2BniWJ%2FbHEWLjLSgmF2gfBDbBTSLP9UR8A7kWULPLTse%2BLMxnwpMrAxbErjwlfDE%2FvGp1nE&X-Amz-Signature=63ac57a1750869740e72023f06208a72763f2efde7506884c8d074301bdbee8f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDLWW4OB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDDeMHeiQqmGBK0m%2BnWtzR3sxu9KvG8VfGM6SOwGTMq0gIhAN%2BsyCa1XxqQCDSIFldexpEAgKpXrmPc1vf1LMfCJS%2BSKv8DCDUQABoMNjM3NDIzMTgzODA1IgzzmrLtVOeTbCBZ9E8q3AOOCeDPJE3WJpG8WpFsBl%2BEHzZWq8qDX5Ysm7t5Kyc1a7FPMZ5UksRIbdPG2BG0ABrWBcvNwU40MBm9Vh4hZk%2BsYpNKzQbayVKSHKMQ0zCGXrut4GVFzPFuHxCTE6f83XCajgbg6zrC9xyuc%2FOt%2BVpcbLJFd43Rx7l75zQdd3wBfbyqQGjPhv4BUZayOq0sC8WpmTioyFolLaUJwoMAlHgk4iN7LZ0hOVKpDDCKupTzasYVBJMqibMdOQchdQuO8Ii7d7XjAywF7ku7L32i8s0FjRompYKqWSSbklQzbsjXxiaMeE74qzdTggM9ydutrmliV04sk2v0tDncKAKz2wav7aMp6q%2FweFiVgXizNOlc6zGHTstYzuH9oIGTyXgFxsPKTPdWRW6QNgFHNDNX8i2kzkLFqqS1jHbueEtzKwW4xQoTp1n0MJEl6NI7pOe9oiLtipm0qPks78FdedT9QnI%2BC0pkPUqh78NgZO%2BOxod1Wk5yLERvC%2BNokwwA4rHcQc9BRdFusMGMCSU%2F8CP8M2oG4Xi01QamJQuy6uZxbadA1%2Fd25kIX%2B5oxGMiVGmXWDMYViL4%2Ftx7M0OutUWzJXpxX%2FGwso2yjEtz1cn9xQzRm4nYTFcajtJ1etMWGUjDM3om9BjqkAW%2BNFpFXKsBZZOTsb%2FQgM2cqH69rDBVD%2FnDzNSQZO17jsUVQZf16%2BvDHbcIQjkHe6k62Ui94nuGKb2F%2FeGq%2BQtqAByTWFc19QStHpue4zZ8MryjO7bLjtm5hpXZOXcKcbzHTyESo0rGmBYnCa0WoFW%2BniWJ%2FbHEWLjLSgmF2gfBDbBTSLP9UR8A7kWULPLTse%2BLMxnwpMrAxbErjwlfDE%2FvGp1nE&X-Amz-Signature=b3245ab39bf341a986a86a3bf76bae281e1f71cea5d90d5e0f80b39f0ca46a11&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF7625C6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIAV7nY%2BQadSQ9MzmNi1C68jCCor8ZBTcH664biwiEz%2BzAiEA59rByt7euPGo2FhmG%2BJY2FNoSbxo%2Bt3yNZDHSDkQqgMq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDOzbesbLF5UBzKbDICrcA6haZyr%2BnIoI1zaj1QoGjorKwT56ukLkygE055R278z7wmcegOoEUAYdbTM44lmXjEVdyzB%2B6QmtIe5bENDFnFh0sBp58qWZGiFTeNqbbH6kXzvJYJkQTpJfvHXaBJ1h1TRK2YKybR53lZLSn4W0KSDcoWZ91modBxry8wq7J8ZrGUFxtZfG4gBt6MYDrE2DfA5AL%2Fu8e7p0AYSPyS6yzl8j1t3n6mXDg5RgvSUo%2FA8Iof8UcLS8toT9MiY9KjSFIve1i2Ky7PHnmn9slOr81qJOjp8eDcUKTZgrunT2oHF03murT9F4hAW6oM74Q%2FsSHL86uobkXS9f6w5kL3vbyXo%2FoIqg1tdKeI9nTz5oYr%2BgT9Vu6LKL1u4GPYZ9rRfFOyWd3FPSZFIWT2ViFB6G4R9hZhYZESK1VJiqeqyDcYUi6KSIYXxtTzwfEVF1jqKNBq8FTO1Uua3Tg3Fl1bf4NDHHoCj%2FAECTRqUtbzRV6Frhe1ZIOTQEo2JLE5FUes2bHZn%2FcwzimhO3EI3BDP6e0N3t1sXv39D%2BSUYwCZxpcqTC9QLEBTxUGD7lv9b69Xz%2B69DTIiKzMwn4zg%2BfvHDfRPqABjrjHJXteoNEFHpx7ZcBcsVcieds3P2w%2BKo3MLHdib0GOqUBYfAIZp6VZsRRqIbbIybzjjgyJ68b4MQO870CmhYqQ%2B%2F%2BzHNTh4WVms%2B3u754FxPQwP4X1K83jN76g%2BFfzRkxFutreHYQ4CwcwKCi67jA5XN6pQDoc3xX2CVNljOSCgrYAuuZMzz3mQ6NOGa5peAMQPu767KJkvRQELF4v%2BI9J4bwAD6e0i3CojS%2F6jpKJTpLkpfma%2F0yY49FWVp9D4WU1f%2BRQ%2B7k&X-Amz-Signature=37c58587c60f72e899ef29d042d5a0f5068c2ab4759153daadd336c43a8a638c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF7625C6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIAV7nY%2BQadSQ9MzmNi1C68jCCor8ZBTcH664biwiEz%2BzAiEA59rByt7euPGo2FhmG%2BJY2FNoSbxo%2Bt3yNZDHSDkQqgMq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDOzbesbLF5UBzKbDICrcA6haZyr%2BnIoI1zaj1QoGjorKwT56ukLkygE055R278z7wmcegOoEUAYdbTM44lmXjEVdyzB%2B6QmtIe5bENDFnFh0sBp58qWZGiFTeNqbbH6kXzvJYJkQTpJfvHXaBJ1h1TRK2YKybR53lZLSn4W0KSDcoWZ91modBxry8wq7J8ZrGUFxtZfG4gBt6MYDrE2DfA5AL%2Fu8e7p0AYSPyS6yzl8j1t3n6mXDg5RgvSUo%2FA8Iof8UcLS8toT9MiY9KjSFIve1i2Ky7PHnmn9slOr81qJOjp8eDcUKTZgrunT2oHF03murT9F4hAW6oM74Q%2FsSHL86uobkXS9f6w5kL3vbyXo%2FoIqg1tdKeI9nTz5oYr%2BgT9Vu6LKL1u4GPYZ9rRfFOyWd3FPSZFIWT2ViFB6G4R9hZhYZESK1VJiqeqyDcYUi6KSIYXxtTzwfEVF1jqKNBq8FTO1Uua3Tg3Fl1bf4NDHHoCj%2FAECTRqUtbzRV6Frhe1ZIOTQEo2JLE5FUes2bHZn%2FcwzimhO3EI3BDP6e0N3t1sXv39D%2BSUYwCZxpcqTC9QLEBTxUGD7lv9b69Xz%2B69DTIiKzMwn4zg%2BfvHDfRPqABjrjHJXteoNEFHpx7ZcBcsVcieds3P2w%2BKo3MLHdib0GOqUBYfAIZp6VZsRRqIbbIybzjjgyJ68b4MQO870CmhYqQ%2B%2F%2BzHNTh4WVms%2B3u754FxPQwP4X1K83jN76g%2BFfzRkxFutreHYQ4CwcwKCi67jA5XN6pQDoc3xX2CVNljOSCgrYAuuZMzz3mQ6NOGa5peAMQPu767KJkvRQELF4v%2BI9J4bwAD6e0i3CojS%2F6jpKJTpLkpfma%2F0yY49FWVp9D4WU1f%2BRQ%2B7k&X-Amz-Signature=891e0cee48d1e691aa9fe71a46b73617af507649e5dbdb7cb18d40fef4a0c5fc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF7625C6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIAV7nY%2BQadSQ9MzmNi1C68jCCor8ZBTcH664biwiEz%2BzAiEA59rByt7euPGo2FhmG%2BJY2FNoSbxo%2Bt3yNZDHSDkQqgMq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDOzbesbLF5UBzKbDICrcA6haZyr%2BnIoI1zaj1QoGjorKwT56ukLkygE055R278z7wmcegOoEUAYdbTM44lmXjEVdyzB%2B6QmtIe5bENDFnFh0sBp58qWZGiFTeNqbbH6kXzvJYJkQTpJfvHXaBJ1h1TRK2YKybR53lZLSn4W0KSDcoWZ91modBxry8wq7J8ZrGUFxtZfG4gBt6MYDrE2DfA5AL%2Fu8e7p0AYSPyS6yzl8j1t3n6mXDg5RgvSUo%2FA8Iof8UcLS8toT9MiY9KjSFIve1i2Ky7PHnmn9slOr81qJOjp8eDcUKTZgrunT2oHF03murT9F4hAW6oM74Q%2FsSHL86uobkXS9f6w5kL3vbyXo%2FoIqg1tdKeI9nTz5oYr%2BgT9Vu6LKL1u4GPYZ9rRfFOyWd3FPSZFIWT2ViFB6G4R9hZhYZESK1VJiqeqyDcYUi6KSIYXxtTzwfEVF1jqKNBq8FTO1Uua3Tg3Fl1bf4NDHHoCj%2FAECTRqUtbzRV6Frhe1ZIOTQEo2JLE5FUes2bHZn%2FcwzimhO3EI3BDP6e0N3t1sXv39D%2BSUYwCZxpcqTC9QLEBTxUGD7lv9b69Xz%2B69DTIiKzMwn4zg%2BfvHDfRPqABjrjHJXteoNEFHpx7ZcBcsVcieds3P2w%2BKo3MLHdib0GOqUBYfAIZp6VZsRRqIbbIybzjjgyJ68b4MQO870CmhYqQ%2B%2F%2BzHNTh4WVms%2B3u754FxPQwP4X1K83jN76g%2BFfzRkxFutreHYQ4CwcwKCi67jA5XN6pQDoc3xX2CVNljOSCgrYAuuZMzz3mQ6NOGa5peAMQPu767KJkvRQELF4v%2BI9J4bwAD6e0i3CojS%2F6jpKJTpLkpfma%2F0yY49FWVp9D4WU1f%2BRQ%2B7k&X-Amz-Signature=e85f617336d83b1c0de573e93667b9a6199e42d8465eb86cf626a6978ba3988e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF7625C6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIAV7nY%2BQadSQ9MzmNi1C68jCCor8ZBTcH664biwiEz%2BzAiEA59rByt7euPGo2FhmG%2BJY2FNoSbxo%2Bt3yNZDHSDkQqgMq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDOzbesbLF5UBzKbDICrcA6haZyr%2BnIoI1zaj1QoGjorKwT56ukLkygE055R278z7wmcegOoEUAYdbTM44lmXjEVdyzB%2B6QmtIe5bENDFnFh0sBp58qWZGiFTeNqbbH6kXzvJYJkQTpJfvHXaBJ1h1TRK2YKybR53lZLSn4W0KSDcoWZ91modBxry8wq7J8ZrGUFxtZfG4gBt6MYDrE2DfA5AL%2Fu8e7p0AYSPyS6yzl8j1t3n6mXDg5RgvSUo%2FA8Iof8UcLS8toT9MiY9KjSFIve1i2Ky7PHnmn9slOr81qJOjp8eDcUKTZgrunT2oHF03murT9F4hAW6oM74Q%2FsSHL86uobkXS9f6w5kL3vbyXo%2FoIqg1tdKeI9nTz5oYr%2BgT9Vu6LKL1u4GPYZ9rRfFOyWd3FPSZFIWT2ViFB6G4R9hZhYZESK1VJiqeqyDcYUi6KSIYXxtTzwfEVF1jqKNBq8FTO1Uua3Tg3Fl1bf4NDHHoCj%2FAECTRqUtbzRV6Frhe1ZIOTQEo2JLE5FUes2bHZn%2FcwzimhO3EI3BDP6e0N3t1sXv39D%2BSUYwCZxpcqTC9QLEBTxUGD7lv9b69Xz%2B69DTIiKzMwn4zg%2BfvHDfRPqABjrjHJXteoNEFHpx7ZcBcsVcieds3P2w%2BKo3MLHdib0GOqUBYfAIZp6VZsRRqIbbIybzjjgyJ68b4MQO870CmhYqQ%2B%2F%2BzHNTh4WVms%2B3u754FxPQwP4X1K83jN76g%2BFfzRkxFutreHYQ4CwcwKCi67jA5XN6pQDoc3xX2CVNljOSCgrYAuuZMzz3mQ6NOGa5peAMQPu767KJkvRQELF4v%2BI9J4bwAD6e0i3CojS%2F6jpKJTpLkpfma%2F0yY49FWVp9D4WU1f%2BRQ%2B7k&X-Amz-Signature=bc4b6793dc1e771b6ba74ecd53b62b1dcc16c465bf4f8264e7ed97d03c425030&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF7625C6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIAV7nY%2BQadSQ9MzmNi1C68jCCor8ZBTcH664biwiEz%2BzAiEA59rByt7euPGo2FhmG%2BJY2FNoSbxo%2Bt3yNZDHSDkQqgMq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDOzbesbLF5UBzKbDICrcA6haZyr%2BnIoI1zaj1QoGjorKwT56ukLkygE055R278z7wmcegOoEUAYdbTM44lmXjEVdyzB%2B6QmtIe5bENDFnFh0sBp58qWZGiFTeNqbbH6kXzvJYJkQTpJfvHXaBJ1h1TRK2YKybR53lZLSn4W0KSDcoWZ91modBxry8wq7J8ZrGUFxtZfG4gBt6MYDrE2DfA5AL%2Fu8e7p0AYSPyS6yzl8j1t3n6mXDg5RgvSUo%2FA8Iof8UcLS8toT9MiY9KjSFIve1i2Ky7PHnmn9slOr81qJOjp8eDcUKTZgrunT2oHF03murT9F4hAW6oM74Q%2FsSHL86uobkXS9f6w5kL3vbyXo%2FoIqg1tdKeI9nTz5oYr%2BgT9Vu6LKL1u4GPYZ9rRfFOyWd3FPSZFIWT2ViFB6G4R9hZhYZESK1VJiqeqyDcYUi6KSIYXxtTzwfEVF1jqKNBq8FTO1Uua3Tg3Fl1bf4NDHHoCj%2FAECTRqUtbzRV6Frhe1ZIOTQEo2JLE5FUes2bHZn%2FcwzimhO3EI3BDP6e0N3t1sXv39D%2BSUYwCZxpcqTC9QLEBTxUGD7lv9b69Xz%2B69DTIiKzMwn4zg%2BfvHDfRPqABjrjHJXteoNEFHpx7ZcBcsVcieds3P2w%2BKo3MLHdib0GOqUBYfAIZp6VZsRRqIbbIybzjjgyJ68b4MQO870CmhYqQ%2B%2F%2BzHNTh4WVms%2B3u754FxPQwP4X1K83jN76g%2BFfzRkxFutreHYQ4CwcwKCi67jA5XN6pQDoc3xX2CVNljOSCgrYAuuZMzz3mQ6NOGa5peAMQPu767KJkvRQELF4v%2BI9J4bwAD6e0i3CojS%2F6jpKJTpLkpfma%2F0yY49FWVp9D4WU1f%2BRQ%2B7k&X-Amz-Signature=7e75a2a21eae33c868eb70f7ce538932b015436311c989b9e5b9c98cef87a668&X-Amz-SignedHeaders=host&x-id=GetObject)
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


