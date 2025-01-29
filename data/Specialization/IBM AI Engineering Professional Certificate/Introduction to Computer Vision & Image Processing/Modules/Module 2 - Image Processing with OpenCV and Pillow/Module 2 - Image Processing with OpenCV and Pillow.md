

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VK4YLSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQCpXRYvtGumbs%2Fi2ELv2jkSx%2FjjTRanweBtX4PjccGOLgIhAMwNoEC%2BvzEPstVSwN%2FDdjq221QmURW1CUvA7wldzH3oKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BkSrPjAEoeFTCnN8q3ANeDmlQcwKopwMvPmmh1%2Fj4WeBFXbm8XkOA%2BIPzAOnuPCwu4v9HwyUZxpiLDn2iNAdAV0uEFOWkXDab2hEonwaPJDGfkqmBm8Zm38sovVAQjt%2FudqcSGdvWuBDb%2BNQw6U8KQfDJ%2B%2BGD7EUa4UtuMZhjft%2BapA%2FcPA3f9w9l04ol1NyCUwvBTMszlHNeknv3wKz4d1%2FUplEsHLtE6ruBMp1ZD6opGFhcwg4zpv35UzG4uM9xm0vT3LQCuj5lyZL1uJ22HgzhBwZhGAE0MQQjJYjWWm6fJpWMZ9lgtHq0Ae9kpg7vhwsimrcSq8foQbN1BMzvLSY9PzNjEzhwkVX1lKy%2FZ9oxQAE6KuNGPbw3soCnL7m7a9R8MFCIGm7e7MRVJhG3FSORHqSuj17X9XxKjtjkP9a1BZwJxI18QRzB8fYea1ttXYPhyXRheLPbWGCRhV0fuLjiiuy4%2B1dA6i7HfvP5sq%2Bz2J0BAQqSQQXrnezQuH%2Flm7KH5NelH1Wc1qymdw1lXsNJAeGIMiKaXKyZ8ynKBNDt%2FGPZZ5tM9GGocLEBzRZacpwvc8vDkuo18w8%2FTw3FYRW%2BZLxhQRNeibK9BJ%2FwrS%2BR5oStpBnaJpwoSQn9mu%2B8GLF3F%2FHMhWh2vDDgkOe8BjqkAVis3vImdIuBIVH7hKqhex5DRp7hL4izUfx3Dtm1Rb0CEjYo7Zoe4EN%2Bv%2Frecr4MKgy6NWfZSEq6x5%2FTMMA%2FFCTPqud8PctET7f0BucXmt3r37WyYhZ7GUNHLfz2srGq6G5Hlg4J5WaOGay2zAys%2FU3%2BWhWdcjtfDz1hdfIN3ReFxHVmhfa5InM52l2196hoJN6ltMB2jEOULaxM4CoKwBSQuanb&X-Amz-Signature=29c92f7fa33c7c8d5a1375e6b17b997e641cb3d5cf39ef5fe9a6ac3bfdbdd68b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5EMHEWX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQC8Bnlo7iTp0AajS96beg%2FzkVvSmnMPYy0IYq3f6hB6nAIgDvlmTTS01ya7ds%2FBGdqU%2FvO5Kd5r%2BqaPzpFlF%2Bx%2FOvkqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqKlu9fJjgfzTdPHSrcAyxRhBfAlNJYpTE%2FdJNoW4AQh1Uv%2FRouuVzjEZnuRq5xTM%2B2Bg6cRay5MsXeSq1Ur4JnYu22GQ3wBYNi5TBf71EvZ6tmQSzOYsQNxLvgI%2F7yr4Z9Yg6k36X7VyvT5ItcMGI4%2BiP7KIVkv98ZkLGXTw0IEZ6QMcafGo6F94%2FXqLJTBwOaKYcEG5WVq%2FQmf6ZbaJvRNS5rL1N9GEyhWsmppf6vQBpcs0yFEnej8wMwyM83jvSLsoRI1NC0xC6QoiGOi5yd8sqjO9821CQ%2FZlWpnDiaSqLdbeLzWqMZcemeZ2wf8A1HDOR4DPcGr71CDvchBfJDMfjFKbBh86mEaX4D6GWJXjD6%2Fb2yIsH0MbJgtHS%2Fb0it7y46rkD8s6jLwa4vJEFkemSTmAc2SVC1GgvhUL4cDO6gWIU2M86jRbtU1R568iTeUmxElqYDnAfIYZDZwNIM9sbTw2oTmQgEn4KqaArHaNZnt1ift51ifSa%2B8zCnuezOoRR0XDmEAD4uAuapHmUUR6KX7JD68ZQPyrBsHJADxqaqiuBUSsYIE%2FVJc%2FtlXMmxkd%2BnOgsrfN9L1T%2FejTj%2BRKabi5uUjW4oPWgVEIxN6%2BOfa03evBg9SiOmN7yh6PFJL14crUs2MdzRMMaQ57wGOqUBjqxmIym9dqx08om3m28U6n6TAdJSdFU4jhn2w2lJ9PSn3P%2F6RmJPdFXEwwSF%2F5B4YdmRUdNAIt19qwpQsqYvI3f5BcbXVesB9g9MhpMsljl5wAQaeLXcXC1AQrB1gAjaAjSQCl6NPZ%2BMW7dTJzdSvVLm4VwQpqr%2Bdv2uZjPmhKpZ9aheXka7oKaa%2BYQvg3zBSgY0PduNHpn7ooiPFCxVfXVsB22e&X-Amz-Signature=e59b7c46e00646c035e26c02bd902979d940ab8bfb224eb245a2c099fd8c9576&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5EMHEWX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQC8Bnlo7iTp0AajS96beg%2FzkVvSmnMPYy0IYq3f6hB6nAIgDvlmTTS01ya7ds%2FBGdqU%2FvO5Kd5r%2BqaPzpFlF%2Bx%2FOvkqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqKlu9fJjgfzTdPHSrcAyxRhBfAlNJYpTE%2FdJNoW4AQh1Uv%2FRouuVzjEZnuRq5xTM%2B2Bg6cRay5MsXeSq1Ur4JnYu22GQ3wBYNi5TBf71EvZ6tmQSzOYsQNxLvgI%2F7yr4Z9Yg6k36X7VyvT5ItcMGI4%2BiP7KIVkv98ZkLGXTw0IEZ6QMcafGo6F94%2FXqLJTBwOaKYcEG5WVq%2FQmf6ZbaJvRNS5rL1N9GEyhWsmppf6vQBpcs0yFEnej8wMwyM83jvSLsoRI1NC0xC6QoiGOi5yd8sqjO9821CQ%2FZlWpnDiaSqLdbeLzWqMZcemeZ2wf8A1HDOR4DPcGr71CDvchBfJDMfjFKbBh86mEaX4D6GWJXjD6%2Fb2yIsH0MbJgtHS%2Fb0it7y46rkD8s6jLwa4vJEFkemSTmAc2SVC1GgvhUL4cDO6gWIU2M86jRbtU1R568iTeUmxElqYDnAfIYZDZwNIM9sbTw2oTmQgEn4KqaArHaNZnt1ift51ifSa%2B8zCnuezOoRR0XDmEAD4uAuapHmUUR6KX7JD68ZQPyrBsHJADxqaqiuBUSsYIE%2FVJc%2FtlXMmxkd%2BnOgsrfN9L1T%2FejTj%2BRKabi5uUjW4oPWgVEIxN6%2BOfa03evBg9SiOmN7yh6PFJL14crUs2MdzRMMaQ57wGOqUBjqxmIym9dqx08om3m28U6n6TAdJSdFU4jhn2w2lJ9PSn3P%2F6RmJPdFXEwwSF%2F5B4YdmRUdNAIt19qwpQsqYvI3f5BcbXVesB9g9MhpMsljl5wAQaeLXcXC1AQrB1gAjaAjSQCl6NPZ%2BMW7dTJzdSvVLm4VwQpqr%2Bdv2uZjPmhKpZ9aheXka7oKaa%2BYQvg3zBSgY0PduNHpn7ooiPFCxVfXVsB22e&X-Amz-Signature=212a748e3760d6188e0b78f7cd7c367feee2c1cf369198ba9f0a352f1c502e4f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5EMHEWX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQC8Bnlo7iTp0AajS96beg%2FzkVvSmnMPYy0IYq3f6hB6nAIgDvlmTTS01ya7ds%2FBGdqU%2FvO5Kd5r%2BqaPzpFlF%2Bx%2FOvkqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqKlu9fJjgfzTdPHSrcAyxRhBfAlNJYpTE%2FdJNoW4AQh1Uv%2FRouuVzjEZnuRq5xTM%2B2Bg6cRay5MsXeSq1Ur4JnYu22GQ3wBYNi5TBf71EvZ6tmQSzOYsQNxLvgI%2F7yr4Z9Yg6k36X7VyvT5ItcMGI4%2BiP7KIVkv98ZkLGXTw0IEZ6QMcafGo6F94%2FXqLJTBwOaKYcEG5WVq%2FQmf6ZbaJvRNS5rL1N9GEyhWsmppf6vQBpcs0yFEnej8wMwyM83jvSLsoRI1NC0xC6QoiGOi5yd8sqjO9821CQ%2FZlWpnDiaSqLdbeLzWqMZcemeZ2wf8A1HDOR4DPcGr71CDvchBfJDMfjFKbBh86mEaX4D6GWJXjD6%2Fb2yIsH0MbJgtHS%2Fb0it7y46rkD8s6jLwa4vJEFkemSTmAc2SVC1GgvhUL4cDO6gWIU2M86jRbtU1R568iTeUmxElqYDnAfIYZDZwNIM9sbTw2oTmQgEn4KqaArHaNZnt1ift51ifSa%2B8zCnuezOoRR0XDmEAD4uAuapHmUUR6KX7JD68ZQPyrBsHJADxqaqiuBUSsYIE%2FVJc%2FtlXMmxkd%2BnOgsrfN9L1T%2FejTj%2BRKabi5uUjW4oPWgVEIxN6%2BOfa03evBg9SiOmN7yh6PFJL14crUs2MdzRMMaQ57wGOqUBjqxmIym9dqx08om3m28U6n6TAdJSdFU4jhn2w2lJ9PSn3P%2F6RmJPdFXEwwSF%2F5B4YdmRUdNAIt19qwpQsqYvI3f5BcbXVesB9g9MhpMsljl5wAQaeLXcXC1AQrB1gAjaAjSQCl6NPZ%2BMW7dTJzdSvVLm4VwQpqr%2Bdv2uZjPmhKpZ9aheXka7oKaa%2BYQvg3zBSgY0PduNHpn7ooiPFCxVfXVsB22e&X-Amz-Signature=998766dd318816ba64b3345d0b65716839def2997d5965bdc5951933ba12a841&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5EMHEWX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQC8Bnlo7iTp0AajS96beg%2FzkVvSmnMPYy0IYq3f6hB6nAIgDvlmTTS01ya7ds%2FBGdqU%2FvO5Kd5r%2BqaPzpFlF%2Bx%2FOvkqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqKlu9fJjgfzTdPHSrcAyxRhBfAlNJYpTE%2FdJNoW4AQh1Uv%2FRouuVzjEZnuRq5xTM%2B2Bg6cRay5MsXeSq1Ur4JnYu22GQ3wBYNi5TBf71EvZ6tmQSzOYsQNxLvgI%2F7yr4Z9Yg6k36X7VyvT5ItcMGI4%2BiP7KIVkv98ZkLGXTw0IEZ6QMcafGo6F94%2FXqLJTBwOaKYcEG5WVq%2FQmf6ZbaJvRNS5rL1N9GEyhWsmppf6vQBpcs0yFEnej8wMwyM83jvSLsoRI1NC0xC6QoiGOi5yd8sqjO9821CQ%2FZlWpnDiaSqLdbeLzWqMZcemeZ2wf8A1HDOR4DPcGr71CDvchBfJDMfjFKbBh86mEaX4D6GWJXjD6%2Fb2yIsH0MbJgtHS%2Fb0it7y46rkD8s6jLwa4vJEFkemSTmAc2SVC1GgvhUL4cDO6gWIU2M86jRbtU1R568iTeUmxElqYDnAfIYZDZwNIM9sbTw2oTmQgEn4KqaArHaNZnt1ift51ifSa%2B8zCnuezOoRR0XDmEAD4uAuapHmUUR6KX7JD68ZQPyrBsHJADxqaqiuBUSsYIE%2FVJc%2FtlXMmxkd%2BnOgsrfN9L1T%2FejTj%2BRKabi5uUjW4oPWgVEIxN6%2BOfa03evBg9SiOmN7yh6PFJL14crUs2MdzRMMaQ57wGOqUBjqxmIym9dqx08om3m28U6n6TAdJSdFU4jhn2w2lJ9PSn3P%2F6RmJPdFXEwwSF%2F5B4YdmRUdNAIt19qwpQsqYvI3f5BcbXVesB9g9MhpMsljl5wAQaeLXcXC1AQrB1gAjaAjSQCl6NPZ%2BMW7dTJzdSvVLm4VwQpqr%2Bdv2uZjPmhKpZ9aheXka7oKaa%2BYQvg3zBSgY0PduNHpn7ooiPFCxVfXVsB22e&X-Amz-Signature=8ea1b703fdd903a4d8a9629652a47becc9691de3dc0c36039b4a98f503d582a0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5EMHEWX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQC8Bnlo7iTp0AajS96beg%2FzkVvSmnMPYy0IYq3f6hB6nAIgDvlmTTS01ya7ds%2FBGdqU%2FvO5Kd5r%2BqaPzpFlF%2Bx%2FOvkqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqKlu9fJjgfzTdPHSrcAyxRhBfAlNJYpTE%2FdJNoW4AQh1Uv%2FRouuVzjEZnuRq5xTM%2B2Bg6cRay5MsXeSq1Ur4JnYu22GQ3wBYNi5TBf71EvZ6tmQSzOYsQNxLvgI%2F7yr4Z9Yg6k36X7VyvT5ItcMGI4%2BiP7KIVkv98ZkLGXTw0IEZ6QMcafGo6F94%2FXqLJTBwOaKYcEG5WVq%2FQmf6ZbaJvRNS5rL1N9GEyhWsmppf6vQBpcs0yFEnej8wMwyM83jvSLsoRI1NC0xC6QoiGOi5yd8sqjO9821CQ%2FZlWpnDiaSqLdbeLzWqMZcemeZ2wf8A1HDOR4DPcGr71CDvchBfJDMfjFKbBh86mEaX4D6GWJXjD6%2Fb2yIsH0MbJgtHS%2Fb0it7y46rkD8s6jLwa4vJEFkemSTmAc2SVC1GgvhUL4cDO6gWIU2M86jRbtU1R568iTeUmxElqYDnAfIYZDZwNIM9sbTw2oTmQgEn4KqaArHaNZnt1ift51ifSa%2B8zCnuezOoRR0XDmEAD4uAuapHmUUR6KX7JD68ZQPyrBsHJADxqaqiuBUSsYIE%2FVJc%2FtlXMmxkd%2BnOgsrfN9L1T%2FejTj%2BRKabi5uUjW4oPWgVEIxN6%2BOfa03evBg9SiOmN7yh6PFJL14crUs2MdzRMMaQ57wGOqUBjqxmIym9dqx08om3m28U6n6TAdJSdFU4jhn2w2lJ9PSn3P%2F6RmJPdFXEwwSF%2F5B4YdmRUdNAIt19qwpQsqYvI3f5BcbXVesB9g9MhpMsljl5wAQaeLXcXC1AQrB1gAjaAjSQCl6NPZ%2BMW7dTJzdSvVLm4VwQpqr%2Bdv2uZjPmhKpZ9aheXka7oKaa%2BYQvg3zBSgY0PduNHpn7ooiPFCxVfXVsB22e&X-Amz-Signature=5dc92e5c14c2d4c952cd196848d6503d52d6c2075a6fc428873965cb9a4cd1bd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VK4YLSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQCpXRYvtGumbs%2Fi2ELv2jkSx%2FjjTRanweBtX4PjccGOLgIhAMwNoEC%2BvzEPstVSwN%2FDdjq221QmURW1CUvA7wldzH3oKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BkSrPjAEoeFTCnN8q3ANeDmlQcwKopwMvPmmh1%2Fj4WeBFXbm8XkOA%2BIPzAOnuPCwu4v9HwyUZxpiLDn2iNAdAV0uEFOWkXDab2hEonwaPJDGfkqmBm8Zm38sovVAQjt%2FudqcSGdvWuBDb%2BNQw6U8KQfDJ%2B%2BGD7EUa4UtuMZhjft%2BapA%2FcPA3f9w9l04ol1NyCUwvBTMszlHNeknv3wKz4d1%2FUplEsHLtE6ruBMp1ZD6opGFhcwg4zpv35UzG4uM9xm0vT3LQCuj5lyZL1uJ22HgzhBwZhGAE0MQQjJYjWWm6fJpWMZ9lgtHq0Ae9kpg7vhwsimrcSq8foQbN1BMzvLSY9PzNjEzhwkVX1lKy%2FZ9oxQAE6KuNGPbw3soCnL7m7a9R8MFCIGm7e7MRVJhG3FSORHqSuj17X9XxKjtjkP9a1BZwJxI18QRzB8fYea1ttXYPhyXRheLPbWGCRhV0fuLjiiuy4%2B1dA6i7HfvP5sq%2Bz2J0BAQqSQQXrnezQuH%2Flm7KH5NelH1Wc1qymdw1lXsNJAeGIMiKaXKyZ8ynKBNDt%2FGPZZ5tM9GGocLEBzRZacpwvc8vDkuo18w8%2FTw3FYRW%2BZLxhQRNeibK9BJ%2FwrS%2BR5oStpBnaJpwoSQn9mu%2B8GLF3F%2FHMhWh2vDDgkOe8BjqkAVis3vImdIuBIVH7hKqhex5DRp7hL4izUfx3Dtm1Rb0CEjYo7Zoe4EN%2Bv%2Frecr4MKgy6NWfZSEq6x5%2FTMMA%2FFCTPqud8PctET7f0BucXmt3r37WyYhZ7GUNHLfz2srGq6G5Hlg4J5WaOGay2zAys%2FU3%2BWhWdcjtfDz1hdfIN3ReFxHVmhfa5InM52l2196hoJN6ltMB2jEOULaxM4CoKwBSQuanb&X-Amz-Signature=6088766adfbd203cde52f3b1ff5080f2c97ec1721ed877f7e606215cbf55923c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VK4YLSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQCpXRYvtGumbs%2Fi2ELv2jkSx%2FjjTRanweBtX4PjccGOLgIhAMwNoEC%2BvzEPstVSwN%2FDdjq221QmURW1CUvA7wldzH3oKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BkSrPjAEoeFTCnN8q3ANeDmlQcwKopwMvPmmh1%2Fj4WeBFXbm8XkOA%2BIPzAOnuPCwu4v9HwyUZxpiLDn2iNAdAV0uEFOWkXDab2hEonwaPJDGfkqmBm8Zm38sovVAQjt%2FudqcSGdvWuBDb%2BNQw6U8KQfDJ%2B%2BGD7EUa4UtuMZhjft%2BapA%2FcPA3f9w9l04ol1NyCUwvBTMszlHNeknv3wKz4d1%2FUplEsHLtE6ruBMp1ZD6opGFhcwg4zpv35UzG4uM9xm0vT3LQCuj5lyZL1uJ22HgzhBwZhGAE0MQQjJYjWWm6fJpWMZ9lgtHq0Ae9kpg7vhwsimrcSq8foQbN1BMzvLSY9PzNjEzhwkVX1lKy%2FZ9oxQAE6KuNGPbw3soCnL7m7a9R8MFCIGm7e7MRVJhG3FSORHqSuj17X9XxKjtjkP9a1BZwJxI18QRzB8fYea1ttXYPhyXRheLPbWGCRhV0fuLjiiuy4%2B1dA6i7HfvP5sq%2Bz2J0BAQqSQQXrnezQuH%2Flm7KH5NelH1Wc1qymdw1lXsNJAeGIMiKaXKyZ8ynKBNDt%2FGPZZ5tM9GGocLEBzRZacpwvc8vDkuo18w8%2FTw3FYRW%2BZLxhQRNeibK9BJ%2FwrS%2BR5oStpBnaJpwoSQn9mu%2B8GLF3F%2FHMhWh2vDDgkOe8BjqkAVis3vImdIuBIVH7hKqhex5DRp7hL4izUfx3Dtm1Rb0CEjYo7Zoe4EN%2Bv%2Frecr4MKgy6NWfZSEq6x5%2FTMMA%2FFCTPqud8PctET7f0BucXmt3r37WyYhZ7GUNHLfz2srGq6G5Hlg4J5WaOGay2zAys%2FU3%2BWhWdcjtfDz1hdfIN3ReFxHVmhfa5InM52l2196hoJN6ltMB2jEOULaxM4CoKwBSQuanb&X-Amz-Signature=a266bc822ffac219183d0827ea0e9e5657dfcdf2f09ead76a0934b8f99c7eab9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VK4YLSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQCpXRYvtGumbs%2Fi2ELv2jkSx%2FjjTRanweBtX4PjccGOLgIhAMwNoEC%2BvzEPstVSwN%2FDdjq221QmURW1CUvA7wldzH3oKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BkSrPjAEoeFTCnN8q3ANeDmlQcwKopwMvPmmh1%2Fj4WeBFXbm8XkOA%2BIPzAOnuPCwu4v9HwyUZxpiLDn2iNAdAV0uEFOWkXDab2hEonwaPJDGfkqmBm8Zm38sovVAQjt%2FudqcSGdvWuBDb%2BNQw6U8KQfDJ%2B%2BGD7EUa4UtuMZhjft%2BapA%2FcPA3f9w9l04ol1NyCUwvBTMszlHNeknv3wKz4d1%2FUplEsHLtE6ruBMp1ZD6opGFhcwg4zpv35UzG4uM9xm0vT3LQCuj5lyZL1uJ22HgzhBwZhGAE0MQQjJYjWWm6fJpWMZ9lgtHq0Ae9kpg7vhwsimrcSq8foQbN1BMzvLSY9PzNjEzhwkVX1lKy%2FZ9oxQAE6KuNGPbw3soCnL7m7a9R8MFCIGm7e7MRVJhG3FSORHqSuj17X9XxKjtjkP9a1BZwJxI18QRzB8fYea1ttXYPhyXRheLPbWGCRhV0fuLjiiuy4%2B1dA6i7HfvP5sq%2Bz2J0BAQqSQQXrnezQuH%2Flm7KH5NelH1Wc1qymdw1lXsNJAeGIMiKaXKyZ8ynKBNDt%2FGPZZ5tM9GGocLEBzRZacpwvc8vDkuo18w8%2FTw3FYRW%2BZLxhQRNeibK9BJ%2FwrS%2BR5oStpBnaJpwoSQn9mu%2B8GLF3F%2FHMhWh2vDDgkOe8BjqkAVis3vImdIuBIVH7hKqhex5DRp7hL4izUfx3Dtm1Rb0CEjYo7Zoe4EN%2Bv%2Frecr4MKgy6NWfZSEq6x5%2FTMMA%2FFCTPqud8PctET7f0BucXmt3r37WyYhZ7GUNHLfz2srGq6G5Hlg4J5WaOGay2zAys%2FU3%2BWhWdcjtfDz1hdfIN3ReFxHVmhfa5InM52l2196hoJN6ltMB2jEOULaxM4CoKwBSQuanb&X-Amz-Signature=6ce36ebc02b31e38e5c28913e99300358367b125e467c0ea31be11f13c955f76&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VK4YLSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQCpXRYvtGumbs%2Fi2ELv2jkSx%2FjjTRanweBtX4PjccGOLgIhAMwNoEC%2BvzEPstVSwN%2FDdjq221QmURW1CUvA7wldzH3oKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BkSrPjAEoeFTCnN8q3ANeDmlQcwKopwMvPmmh1%2Fj4WeBFXbm8XkOA%2BIPzAOnuPCwu4v9HwyUZxpiLDn2iNAdAV0uEFOWkXDab2hEonwaPJDGfkqmBm8Zm38sovVAQjt%2FudqcSGdvWuBDb%2BNQw6U8KQfDJ%2B%2BGD7EUa4UtuMZhjft%2BapA%2FcPA3f9w9l04ol1NyCUwvBTMszlHNeknv3wKz4d1%2FUplEsHLtE6ruBMp1ZD6opGFhcwg4zpv35UzG4uM9xm0vT3LQCuj5lyZL1uJ22HgzhBwZhGAE0MQQjJYjWWm6fJpWMZ9lgtHq0Ae9kpg7vhwsimrcSq8foQbN1BMzvLSY9PzNjEzhwkVX1lKy%2FZ9oxQAE6KuNGPbw3soCnL7m7a9R8MFCIGm7e7MRVJhG3FSORHqSuj17X9XxKjtjkP9a1BZwJxI18QRzB8fYea1ttXYPhyXRheLPbWGCRhV0fuLjiiuy4%2B1dA6i7HfvP5sq%2Bz2J0BAQqSQQXrnezQuH%2Flm7KH5NelH1Wc1qymdw1lXsNJAeGIMiKaXKyZ8ynKBNDt%2FGPZZ5tM9GGocLEBzRZacpwvc8vDkuo18w8%2FTw3FYRW%2BZLxhQRNeibK9BJ%2FwrS%2BR5oStpBnaJpwoSQn9mu%2B8GLF3F%2FHMhWh2vDDgkOe8BjqkAVis3vImdIuBIVH7hKqhex5DRp7hL4izUfx3Dtm1Rb0CEjYo7Zoe4EN%2Bv%2Frecr4MKgy6NWfZSEq6x5%2FTMMA%2FFCTPqud8PctET7f0BucXmt3r37WyYhZ7GUNHLfz2srGq6G5Hlg4J5WaOGay2zAys%2FU3%2BWhWdcjtfDz1hdfIN3ReFxHVmhfa5InM52l2196hoJN6ltMB2jEOULaxM4CoKwBSQuanb&X-Amz-Signature=13b701aec71f0bb759cc9664f094bb46058f5125b8561dc179de64e0dca0b3fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VK4YLSG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQCpXRYvtGumbs%2Fi2ELv2jkSx%2FjjTRanweBtX4PjccGOLgIhAMwNoEC%2BvzEPstVSwN%2FDdjq221QmURW1CUvA7wldzH3oKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BkSrPjAEoeFTCnN8q3ANeDmlQcwKopwMvPmmh1%2Fj4WeBFXbm8XkOA%2BIPzAOnuPCwu4v9HwyUZxpiLDn2iNAdAV0uEFOWkXDab2hEonwaPJDGfkqmBm8Zm38sovVAQjt%2FudqcSGdvWuBDb%2BNQw6U8KQfDJ%2B%2BGD7EUa4UtuMZhjft%2BapA%2FcPA3f9w9l04ol1NyCUwvBTMszlHNeknv3wKz4d1%2FUplEsHLtE6ruBMp1ZD6opGFhcwg4zpv35UzG4uM9xm0vT3LQCuj5lyZL1uJ22HgzhBwZhGAE0MQQjJYjWWm6fJpWMZ9lgtHq0Ae9kpg7vhwsimrcSq8foQbN1BMzvLSY9PzNjEzhwkVX1lKy%2FZ9oxQAE6KuNGPbw3soCnL7m7a9R8MFCIGm7e7MRVJhG3FSORHqSuj17X9XxKjtjkP9a1BZwJxI18QRzB8fYea1ttXYPhyXRheLPbWGCRhV0fuLjiiuy4%2B1dA6i7HfvP5sq%2Bz2J0BAQqSQQXrnezQuH%2Flm7KH5NelH1Wc1qymdw1lXsNJAeGIMiKaXKyZ8ynKBNDt%2FGPZZ5tM9GGocLEBzRZacpwvc8vDkuo18w8%2FTw3FYRW%2BZLxhQRNeibK9BJ%2FwrS%2BR5oStpBnaJpwoSQn9mu%2B8GLF3F%2FHMhWh2vDDgkOe8BjqkAVis3vImdIuBIVH7hKqhex5DRp7hL4izUfx3Dtm1Rb0CEjYo7Zoe4EN%2Bv%2Frecr4MKgy6NWfZSEq6x5%2FTMMA%2FFCTPqud8PctET7f0BucXmt3r37WyYhZ7GUNHLfz2srGq6G5Hlg4J5WaOGay2zAys%2FU3%2BWhWdcjtfDz1hdfIN3ReFxHVmhfa5InM52l2196hoJN6ltMB2jEOULaxM4CoKwBSQuanb&X-Amz-Signature=f8a25d97cf65e6e71dd46093a8907995ac97dd4b04c0d57f98f437f1bed35c8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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


