

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QHQ47XK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDcY1lkdHiZ%2BZjMogKBhAppg5Vmx88AUuBUDOSTqlnFjQIgKnlB%2BvHaP310msKyC9y0Wim1C9Rk1ssBtoBUhz%2BNhZcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDHaOw36RX8HLdoyhZyrcA1subbqHv%2BlSkWtSndZ%2BxX4PVqbe2vcOObRyN1gnjjo7ZvZHPxJO1p4ntz1dIAlO%2B01BbZ6LlLy8tzYc9BAHJ3R1xMx8h2P1NEj18ZOdswVO%2FlHH6QCLvjPLPMVu%2FDM29duGEEJkVOeLjSAv2gN1urqLIgwR4JnXqjCz%2BDZ0D6%2FAWX9hnu3UR8QLO4lufxYawyD%2BU8jUncwRTB%2F%2FWcpVaIs29CdUod6fj5KuzERp3eBG%2B5svpXHxUffv03xEAT%2BgkEdq1dp65sEAFTJ2Wr1TRFyHrMNdS9dBX1JpRLoB4NpTyWmXxQ8bLQ0kblMcj4g%2BPIgdxCJlaSIn%2BYo%2F6pr2kJoOI%2F12JQMSceE5brORIxJoYxumx3xP681E9TelGvy56Yj7jKVqs9V8wovXlUzut3ppdYtFWe%2FIxBRMRnP9BFMnXDQKy0UftBsNymAUkghA6%2FeSLddi%2F9Py%2Bd4EbbOVKBR9fwfXOh40rGcBd2jWbUp3c4KJwnYzMOgRxdP4Nk%2FcycikbGXwHjOukk4Ztx4IgC251mBsimZK6lJrhZiqb0zdSC9Ek8Lql1qD1u0BPHeBVWf0O8sJc%2Fm3D007YfwiqF%2FXKNP7ar%2BXno9%2FdDu7Gq4zw3ki8Gy3VvjzWye5MKPLh70GOqUB8DSlavT5rz%2Be9FMgbr97A4DW3Z3TABLIv4fOOiLpi641a8teVuYTFRw4z64Ygq2Acud0evQhywFA0efjhlFrgKev1KQOH1OPGrt1sELnPwLRU%2FyecJPiYGJnUJeBzuX%2BW5WbGjK0e87kB0wOiSqMNt8UqEkdzNxzmqdNj%2BJa%2F78It2aF5jZozzFDZzLTbnyl9CjE3qRUMJ8GNwMx1wjOEwX%2BbIgc&X-Amz-Signature=ddec45502d3d4e87a51be9ea21f7d96cac59e682c9132221dda9ef05f4035995&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVVYKYXE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCVmiLfdsA3%2BoYkKSmHZiWSuG9%2F6gWVvdFpWmh4K8VB%2FQIhAPZ%2FnpzCf8E%2B7Ywrn9GDlh8ejIHFsStL5jvrQoKdOaJAKv8DCCsQABoMNjM3NDIzMTgzODA1IgzIm2jKxAHzdRMq8ZMq3ANxOabTt1LH9JDzSEDkHYCR3l9oDdxJo6FCJzjCx76JDxCffr9SP25rx%2Foz8hkxgqHIOL7Y6Xec0eF6LbAUPU3Yavdu6zMLI%2F6KHfgcm2ibNlGsZdz%2FxD7OHhiagTLpA7dyAL6H72VYmtvD8byQOMFVrpY1gvYuRhbQNHHMR4l1x7%2FLBP7cYJZBjxOe%2FCWH5C61BUsk%2BpSgZkdL1gok2dd72pll6oBnaxWQJPWOJvRUKatahtgxq0aKxEkueMtjeECqZ4t7Fnwx4zE1QSS%2BH39SKRawJ6lpUw1So%2BNRKSuiz7SUx9vlvV9IYI%2FQrVAII6dDCLAK7neWtD1m1kQp3YscmLHC32JqviTb6ajj3C5wSTLtS8NsQI9BMp6wLv7o74j9dlfjLgJn%2FYfbGJp6E4FZVsGxUTDsgFt4My7pwaIJFf23t982Vz3%2FfcF2i%2BKrA3Q90%2FBxaohg82K16cV9U%2FSWVr8%2FofOTw6H%2BashQjzfGLbsjmTuj8N%2BvOFI%2BuTFJdOV4TbCKAxMw0gDVLCm5%2BDKiaRPLexidbJlqR7M7ZjuOdFrZzTWxGGtDOCTbzyB42Yp2h9npFPhHOGmjMp%2FwD8L3Zvq7tdRxEjp8qhZ8bfhrnz85RK9qHWrT9Jz1BjDbyoe9BjqkAfoZ871%2F19sxv9bGhHa2TbleYAWbEaLAETRt3Hg0%2BQdZQ%2B89gUzBmrqoJvzV0OYzH7hhx5Y6R%2BrYaj1QV8Rqtz5rvSUGu%2FBrmTo0mDUqAF0nEovYgETQeBGEbdZ6oDNbDtkHFPtw57yOuAiOfBL%2FUU374lVvA2Pj%2BZbXrncSmll6iY8ioEDLq7nxjU714eSULfkHzWbvjiBt4vbk08pyTkFj5gTt&X-Amz-Signature=6676f471244ba5e3e51993d6f99ed9e79a1d406af5ac63a04332c41cc5eebb21&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVVYKYXE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCVmiLfdsA3%2BoYkKSmHZiWSuG9%2F6gWVvdFpWmh4K8VB%2FQIhAPZ%2FnpzCf8E%2B7Ywrn9GDlh8ejIHFsStL5jvrQoKdOaJAKv8DCCsQABoMNjM3NDIzMTgzODA1IgzIm2jKxAHzdRMq8ZMq3ANxOabTt1LH9JDzSEDkHYCR3l9oDdxJo6FCJzjCx76JDxCffr9SP25rx%2Foz8hkxgqHIOL7Y6Xec0eF6LbAUPU3Yavdu6zMLI%2F6KHfgcm2ibNlGsZdz%2FxD7OHhiagTLpA7dyAL6H72VYmtvD8byQOMFVrpY1gvYuRhbQNHHMR4l1x7%2FLBP7cYJZBjxOe%2FCWH5C61BUsk%2BpSgZkdL1gok2dd72pll6oBnaxWQJPWOJvRUKatahtgxq0aKxEkueMtjeECqZ4t7Fnwx4zE1QSS%2BH39SKRawJ6lpUw1So%2BNRKSuiz7SUx9vlvV9IYI%2FQrVAII6dDCLAK7neWtD1m1kQp3YscmLHC32JqviTb6ajj3C5wSTLtS8NsQI9BMp6wLv7o74j9dlfjLgJn%2FYfbGJp6E4FZVsGxUTDsgFt4My7pwaIJFf23t982Vz3%2FfcF2i%2BKrA3Q90%2FBxaohg82K16cV9U%2FSWVr8%2FofOTw6H%2BashQjzfGLbsjmTuj8N%2BvOFI%2BuTFJdOV4TbCKAxMw0gDVLCm5%2BDKiaRPLexidbJlqR7M7ZjuOdFrZzTWxGGtDOCTbzyB42Yp2h9npFPhHOGmjMp%2FwD8L3Zvq7tdRxEjp8qhZ8bfhrnz85RK9qHWrT9Jz1BjDbyoe9BjqkAfoZ871%2F19sxv9bGhHa2TbleYAWbEaLAETRt3Hg0%2BQdZQ%2B89gUzBmrqoJvzV0OYzH7hhx5Y6R%2BrYaj1QV8Rqtz5rvSUGu%2FBrmTo0mDUqAF0nEovYgETQeBGEbdZ6oDNbDtkHFPtw57yOuAiOfBL%2FUU374lVvA2Pj%2BZbXrncSmll6iY8ioEDLq7nxjU714eSULfkHzWbvjiBt4vbk08pyTkFj5gTt&X-Amz-Signature=56ac1954bb627ba1260a38fed612dfa02bd8e92419c5e10f3d2aef2a5f414364&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVVYKYXE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCVmiLfdsA3%2BoYkKSmHZiWSuG9%2F6gWVvdFpWmh4K8VB%2FQIhAPZ%2FnpzCf8E%2B7Ywrn9GDlh8ejIHFsStL5jvrQoKdOaJAKv8DCCsQABoMNjM3NDIzMTgzODA1IgzIm2jKxAHzdRMq8ZMq3ANxOabTt1LH9JDzSEDkHYCR3l9oDdxJo6FCJzjCx76JDxCffr9SP25rx%2Foz8hkxgqHIOL7Y6Xec0eF6LbAUPU3Yavdu6zMLI%2F6KHfgcm2ibNlGsZdz%2FxD7OHhiagTLpA7dyAL6H72VYmtvD8byQOMFVrpY1gvYuRhbQNHHMR4l1x7%2FLBP7cYJZBjxOe%2FCWH5C61BUsk%2BpSgZkdL1gok2dd72pll6oBnaxWQJPWOJvRUKatahtgxq0aKxEkueMtjeECqZ4t7Fnwx4zE1QSS%2BH39SKRawJ6lpUw1So%2BNRKSuiz7SUx9vlvV9IYI%2FQrVAII6dDCLAK7neWtD1m1kQp3YscmLHC32JqviTb6ajj3C5wSTLtS8NsQI9BMp6wLv7o74j9dlfjLgJn%2FYfbGJp6E4FZVsGxUTDsgFt4My7pwaIJFf23t982Vz3%2FfcF2i%2BKrA3Q90%2FBxaohg82K16cV9U%2FSWVr8%2FofOTw6H%2BashQjzfGLbsjmTuj8N%2BvOFI%2BuTFJdOV4TbCKAxMw0gDVLCm5%2BDKiaRPLexidbJlqR7M7ZjuOdFrZzTWxGGtDOCTbzyB42Yp2h9npFPhHOGmjMp%2FwD8L3Zvq7tdRxEjp8qhZ8bfhrnz85RK9qHWrT9Jz1BjDbyoe9BjqkAfoZ871%2F19sxv9bGhHa2TbleYAWbEaLAETRt3Hg0%2BQdZQ%2B89gUzBmrqoJvzV0OYzH7hhx5Y6R%2BrYaj1QV8Rqtz5rvSUGu%2FBrmTo0mDUqAF0nEovYgETQeBGEbdZ6oDNbDtkHFPtw57yOuAiOfBL%2FUU374lVvA2Pj%2BZbXrncSmll6iY8ioEDLq7nxjU714eSULfkHzWbvjiBt4vbk08pyTkFj5gTt&X-Amz-Signature=e22c90840738ef921e40bfabd0f19198b08ff1c67ad1f0e6352a3dde1fbf297f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVVYKYXE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCVmiLfdsA3%2BoYkKSmHZiWSuG9%2F6gWVvdFpWmh4K8VB%2FQIhAPZ%2FnpzCf8E%2B7Ywrn9GDlh8ejIHFsStL5jvrQoKdOaJAKv8DCCsQABoMNjM3NDIzMTgzODA1IgzIm2jKxAHzdRMq8ZMq3ANxOabTt1LH9JDzSEDkHYCR3l9oDdxJo6FCJzjCx76JDxCffr9SP25rx%2Foz8hkxgqHIOL7Y6Xec0eF6LbAUPU3Yavdu6zMLI%2F6KHfgcm2ibNlGsZdz%2FxD7OHhiagTLpA7dyAL6H72VYmtvD8byQOMFVrpY1gvYuRhbQNHHMR4l1x7%2FLBP7cYJZBjxOe%2FCWH5C61BUsk%2BpSgZkdL1gok2dd72pll6oBnaxWQJPWOJvRUKatahtgxq0aKxEkueMtjeECqZ4t7Fnwx4zE1QSS%2BH39SKRawJ6lpUw1So%2BNRKSuiz7SUx9vlvV9IYI%2FQrVAII6dDCLAK7neWtD1m1kQp3YscmLHC32JqviTb6ajj3C5wSTLtS8NsQI9BMp6wLv7o74j9dlfjLgJn%2FYfbGJp6E4FZVsGxUTDsgFt4My7pwaIJFf23t982Vz3%2FfcF2i%2BKrA3Q90%2FBxaohg82K16cV9U%2FSWVr8%2FofOTw6H%2BashQjzfGLbsjmTuj8N%2BvOFI%2BuTFJdOV4TbCKAxMw0gDVLCm5%2BDKiaRPLexidbJlqR7M7ZjuOdFrZzTWxGGtDOCTbzyB42Yp2h9npFPhHOGmjMp%2FwD8L3Zvq7tdRxEjp8qhZ8bfhrnz85RK9qHWrT9Jz1BjDbyoe9BjqkAfoZ871%2F19sxv9bGhHa2TbleYAWbEaLAETRt3Hg0%2BQdZQ%2B89gUzBmrqoJvzV0OYzH7hhx5Y6R%2BrYaj1QV8Rqtz5rvSUGu%2FBrmTo0mDUqAF0nEovYgETQeBGEbdZ6oDNbDtkHFPtw57yOuAiOfBL%2FUU374lVvA2Pj%2BZbXrncSmll6iY8ioEDLq7nxjU714eSULfkHzWbvjiBt4vbk08pyTkFj5gTt&X-Amz-Signature=802ad790c4d648f1e4daccc328e7de09f35fab88408f850f9ad49086fa2ce132&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVVYKYXE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCVmiLfdsA3%2BoYkKSmHZiWSuG9%2F6gWVvdFpWmh4K8VB%2FQIhAPZ%2FnpzCf8E%2B7Ywrn9GDlh8ejIHFsStL5jvrQoKdOaJAKv8DCCsQABoMNjM3NDIzMTgzODA1IgzIm2jKxAHzdRMq8ZMq3ANxOabTt1LH9JDzSEDkHYCR3l9oDdxJo6FCJzjCx76JDxCffr9SP25rx%2Foz8hkxgqHIOL7Y6Xec0eF6LbAUPU3Yavdu6zMLI%2F6KHfgcm2ibNlGsZdz%2FxD7OHhiagTLpA7dyAL6H72VYmtvD8byQOMFVrpY1gvYuRhbQNHHMR4l1x7%2FLBP7cYJZBjxOe%2FCWH5C61BUsk%2BpSgZkdL1gok2dd72pll6oBnaxWQJPWOJvRUKatahtgxq0aKxEkueMtjeECqZ4t7Fnwx4zE1QSS%2BH39SKRawJ6lpUw1So%2BNRKSuiz7SUx9vlvV9IYI%2FQrVAII6dDCLAK7neWtD1m1kQp3YscmLHC32JqviTb6ajj3C5wSTLtS8NsQI9BMp6wLv7o74j9dlfjLgJn%2FYfbGJp6E4FZVsGxUTDsgFt4My7pwaIJFf23t982Vz3%2FfcF2i%2BKrA3Q90%2FBxaohg82K16cV9U%2FSWVr8%2FofOTw6H%2BashQjzfGLbsjmTuj8N%2BvOFI%2BuTFJdOV4TbCKAxMw0gDVLCm5%2BDKiaRPLexidbJlqR7M7ZjuOdFrZzTWxGGtDOCTbzyB42Yp2h9npFPhHOGmjMp%2FwD8L3Zvq7tdRxEjp8qhZ8bfhrnz85RK9qHWrT9Jz1BjDbyoe9BjqkAfoZ871%2F19sxv9bGhHa2TbleYAWbEaLAETRt3Hg0%2BQdZQ%2B89gUzBmrqoJvzV0OYzH7hhx5Y6R%2BrYaj1QV8Rqtz5rvSUGu%2FBrmTo0mDUqAF0nEovYgETQeBGEbdZ6oDNbDtkHFPtw57yOuAiOfBL%2FUU374lVvA2Pj%2BZbXrncSmll6iY8ioEDLq7nxjU714eSULfkHzWbvjiBt4vbk08pyTkFj5gTt&X-Amz-Signature=054dbbe0818967d5dd6e8c86e65b7c7e709dfbac37abd2b93192cd279ba5ca13&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QHQ47XK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDcY1lkdHiZ%2BZjMogKBhAppg5Vmx88AUuBUDOSTqlnFjQIgKnlB%2BvHaP310msKyC9y0Wim1C9Rk1ssBtoBUhz%2BNhZcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDHaOw36RX8HLdoyhZyrcA1subbqHv%2BlSkWtSndZ%2BxX4PVqbe2vcOObRyN1gnjjo7ZvZHPxJO1p4ntz1dIAlO%2B01BbZ6LlLy8tzYc9BAHJ3R1xMx8h2P1NEj18ZOdswVO%2FlHH6QCLvjPLPMVu%2FDM29duGEEJkVOeLjSAv2gN1urqLIgwR4JnXqjCz%2BDZ0D6%2FAWX9hnu3UR8QLO4lufxYawyD%2BU8jUncwRTB%2F%2FWcpVaIs29CdUod6fj5KuzERp3eBG%2B5svpXHxUffv03xEAT%2BgkEdq1dp65sEAFTJ2Wr1TRFyHrMNdS9dBX1JpRLoB4NpTyWmXxQ8bLQ0kblMcj4g%2BPIgdxCJlaSIn%2BYo%2F6pr2kJoOI%2F12JQMSceE5brORIxJoYxumx3xP681E9TelGvy56Yj7jKVqs9V8wovXlUzut3ppdYtFWe%2FIxBRMRnP9BFMnXDQKy0UftBsNymAUkghA6%2FeSLddi%2F9Py%2Bd4EbbOVKBR9fwfXOh40rGcBd2jWbUp3c4KJwnYzMOgRxdP4Nk%2FcycikbGXwHjOukk4Ztx4IgC251mBsimZK6lJrhZiqb0zdSC9Ek8Lql1qD1u0BPHeBVWf0O8sJc%2Fm3D007YfwiqF%2FXKNP7ar%2BXno9%2FdDu7Gq4zw3ki8Gy3VvjzWye5MKPLh70GOqUB8DSlavT5rz%2Be9FMgbr97A4DW3Z3TABLIv4fOOiLpi641a8teVuYTFRw4z64Ygq2Acud0evQhywFA0efjhlFrgKev1KQOH1OPGrt1sELnPwLRU%2FyecJPiYGJnUJeBzuX%2BW5WbGjK0e87kB0wOiSqMNt8UqEkdzNxzmqdNj%2BJa%2F78It2aF5jZozzFDZzLTbnyl9CjE3qRUMJ8GNwMx1wjOEwX%2BbIgc&X-Amz-Signature=22a163b8076c49e90198970260eeada09e64dd2fd99d5a0789a2831435eaffec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QHQ47XK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDcY1lkdHiZ%2BZjMogKBhAppg5Vmx88AUuBUDOSTqlnFjQIgKnlB%2BvHaP310msKyC9y0Wim1C9Rk1ssBtoBUhz%2BNhZcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDHaOw36RX8HLdoyhZyrcA1subbqHv%2BlSkWtSndZ%2BxX4PVqbe2vcOObRyN1gnjjo7ZvZHPxJO1p4ntz1dIAlO%2B01BbZ6LlLy8tzYc9BAHJ3R1xMx8h2P1NEj18ZOdswVO%2FlHH6QCLvjPLPMVu%2FDM29duGEEJkVOeLjSAv2gN1urqLIgwR4JnXqjCz%2BDZ0D6%2FAWX9hnu3UR8QLO4lufxYawyD%2BU8jUncwRTB%2F%2FWcpVaIs29CdUod6fj5KuzERp3eBG%2B5svpXHxUffv03xEAT%2BgkEdq1dp65sEAFTJ2Wr1TRFyHrMNdS9dBX1JpRLoB4NpTyWmXxQ8bLQ0kblMcj4g%2BPIgdxCJlaSIn%2BYo%2F6pr2kJoOI%2F12JQMSceE5brORIxJoYxumx3xP681E9TelGvy56Yj7jKVqs9V8wovXlUzut3ppdYtFWe%2FIxBRMRnP9BFMnXDQKy0UftBsNymAUkghA6%2FeSLddi%2F9Py%2Bd4EbbOVKBR9fwfXOh40rGcBd2jWbUp3c4KJwnYzMOgRxdP4Nk%2FcycikbGXwHjOukk4Ztx4IgC251mBsimZK6lJrhZiqb0zdSC9Ek8Lql1qD1u0BPHeBVWf0O8sJc%2Fm3D007YfwiqF%2FXKNP7ar%2BXno9%2FdDu7Gq4zw3ki8Gy3VvjzWye5MKPLh70GOqUB8DSlavT5rz%2Be9FMgbr97A4DW3Z3TABLIv4fOOiLpi641a8teVuYTFRw4z64Ygq2Acud0evQhywFA0efjhlFrgKev1KQOH1OPGrt1sELnPwLRU%2FyecJPiYGJnUJeBzuX%2BW5WbGjK0e87kB0wOiSqMNt8UqEkdzNxzmqdNj%2BJa%2F78It2aF5jZozzFDZzLTbnyl9CjE3qRUMJ8GNwMx1wjOEwX%2BbIgc&X-Amz-Signature=25afe82b864695852b57f5827a86f0a7794a2102229f98ea36f118098a776e7e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QHQ47XK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDcY1lkdHiZ%2BZjMogKBhAppg5Vmx88AUuBUDOSTqlnFjQIgKnlB%2BvHaP310msKyC9y0Wim1C9Rk1ssBtoBUhz%2BNhZcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDHaOw36RX8HLdoyhZyrcA1subbqHv%2BlSkWtSndZ%2BxX4PVqbe2vcOObRyN1gnjjo7ZvZHPxJO1p4ntz1dIAlO%2B01BbZ6LlLy8tzYc9BAHJ3R1xMx8h2P1NEj18ZOdswVO%2FlHH6QCLvjPLPMVu%2FDM29duGEEJkVOeLjSAv2gN1urqLIgwR4JnXqjCz%2BDZ0D6%2FAWX9hnu3UR8QLO4lufxYawyD%2BU8jUncwRTB%2F%2FWcpVaIs29CdUod6fj5KuzERp3eBG%2B5svpXHxUffv03xEAT%2BgkEdq1dp65sEAFTJ2Wr1TRFyHrMNdS9dBX1JpRLoB4NpTyWmXxQ8bLQ0kblMcj4g%2BPIgdxCJlaSIn%2BYo%2F6pr2kJoOI%2F12JQMSceE5brORIxJoYxumx3xP681E9TelGvy56Yj7jKVqs9V8wovXlUzut3ppdYtFWe%2FIxBRMRnP9BFMnXDQKy0UftBsNymAUkghA6%2FeSLddi%2F9Py%2Bd4EbbOVKBR9fwfXOh40rGcBd2jWbUp3c4KJwnYzMOgRxdP4Nk%2FcycikbGXwHjOukk4Ztx4IgC251mBsimZK6lJrhZiqb0zdSC9Ek8Lql1qD1u0BPHeBVWf0O8sJc%2Fm3D007YfwiqF%2FXKNP7ar%2BXno9%2FdDu7Gq4zw3ki8Gy3VvjzWye5MKPLh70GOqUB8DSlavT5rz%2Be9FMgbr97A4DW3Z3TABLIv4fOOiLpi641a8teVuYTFRw4z64Ygq2Acud0evQhywFA0efjhlFrgKev1KQOH1OPGrt1sELnPwLRU%2FyecJPiYGJnUJeBzuX%2BW5WbGjK0e87kB0wOiSqMNt8UqEkdzNxzmqdNj%2BJa%2F78It2aF5jZozzFDZzLTbnyl9CjE3qRUMJ8GNwMx1wjOEwX%2BbIgc&X-Amz-Signature=2a9073f1e2d95c2dce4e27990341f3edf53264bfaf0f181d12ff927b6ffc2c78&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QHQ47XK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDcY1lkdHiZ%2BZjMogKBhAppg5Vmx88AUuBUDOSTqlnFjQIgKnlB%2BvHaP310msKyC9y0Wim1C9Rk1ssBtoBUhz%2BNhZcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDHaOw36RX8HLdoyhZyrcA1subbqHv%2BlSkWtSndZ%2BxX4PVqbe2vcOObRyN1gnjjo7ZvZHPxJO1p4ntz1dIAlO%2B01BbZ6LlLy8tzYc9BAHJ3R1xMx8h2P1NEj18ZOdswVO%2FlHH6QCLvjPLPMVu%2FDM29duGEEJkVOeLjSAv2gN1urqLIgwR4JnXqjCz%2BDZ0D6%2FAWX9hnu3UR8QLO4lufxYawyD%2BU8jUncwRTB%2F%2FWcpVaIs29CdUod6fj5KuzERp3eBG%2B5svpXHxUffv03xEAT%2BgkEdq1dp65sEAFTJ2Wr1TRFyHrMNdS9dBX1JpRLoB4NpTyWmXxQ8bLQ0kblMcj4g%2BPIgdxCJlaSIn%2BYo%2F6pr2kJoOI%2F12JQMSceE5brORIxJoYxumx3xP681E9TelGvy56Yj7jKVqs9V8wovXlUzut3ppdYtFWe%2FIxBRMRnP9BFMnXDQKy0UftBsNymAUkghA6%2FeSLddi%2F9Py%2Bd4EbbOVKBR9fwfXOh40rGcBd2jWbUp3c4KJwnYzMOgRxdP4Nk%2FcycikbGXwHjOukk4Ztx4IgC251mBsimZK6lJrhZiqb0zdSC9Ek8Lql1qD1u0BPHeBVWf0O8sJc%2Fm3D007YfwiqF%2FXKNP7ar%2BXno9%2FdDu7Gq4zw3ki8Gy3VvjzWye5MKPLh70GOqUB8DSlavT5rz%2Be9FMgbr97A4DW3Z3TABLIv4fOOiLpi641a8teVuYTFRw4z64Ygq2Acud0evQhywFA0efjhlFrgKev1KQOH1OPGrt1sELnPwLRU%2FyecJPiYGJnUJeBzuX%2BW5WbGjK0e87kB0wOiSqMNt8UqEkdzNxzmqdNj%2BJa%2F78It2aF5jZozzFDZzLTbnyl9CjE3qRUMJ8GNwMx1wjOEwX%2BbIgc&X-Amz-Signature=37483ae0e8aa3ef74f1021f51395d1a562e2d8415a33833ca32a98ab1619b9e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QHQ47XK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDcY1lkdHiZ%2BZjMogKBhAppg5Vmx88AUuBUDOSTqlnFjQIgKnlB%2BvHaP310msKyC9y0Wim1C9Rk1ssBtoBUhz%2BNhZcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDHaOw36RX8HLdoyhZyrcA1subbqHv%2BlSkWtSndZ%2BxX4PVqbe2vcOObRyN1gnjjo7ZvZHPxJO1p4ntz1dIAlO%2B01BbZ6LlLy8tzYc9BAHJ3R1xMx8h2P1NEj18ZOdswVO%2FlHH6QCLvjPLPMVu%2FDM29duGEEJkVOeLjSAv2gN1urqLIgwR4JnXqjCz%2BDZ0D6%2FAWX9hnu3UR8QLO4lufxYawyD%2BU8jUncwRTB%2F%2FWcpVaIs29CdUod6fj5KuzERp3eBG%2B5svpXHxUffv03xEAT%2BgkEdq1dp65sEAFTJ2Wr1TRFyHrMNdS9dBX1JpRLoB4NpTyWmXxQ8bLQ0kblMcj4g%2BPIgdxCJlaSIn%2BYo%2F6pr2kJoOI%2F12JQMSceE5brORIxJoYxumx3xP681E9TelGvy56Yj7jKVqs9V8wovXlUzut3ppdYtFWe%2FIxBRMRnP9BFMnXDQKy0UftBsNymAUkghA6%2FeSLddi%2F9Py%2Bd4EbbOVKBR9fwfXOh40rGcBd2jWbUp3c4KJwnYzMOgRxdP4Nk%2FcycikbGXwHjOukk4Ztx4IgC251mBsimZK6lJrhZiqb0zdSC9Ek8Lql1qD1u0BPHeBVWf0O8sJc%2Fm3D007YfwiqF%2FXKNP7ar%2BXno9%2FdDu7Gq4zw3ki8Gy3VvjzWye5MKPLh70GOqUB8DSlavT5rz%2Be9FMgbr97A4DW3Z3TABLIv4fOOiLpi641a8teVuYTFRw4z64Ygq2Acud0evQhywFA0efjhlFrgKev1KQOH1OPGrt1sELnPwLRU%2FyecJPiYGJnUJeBzuX%2BW5WbGjK0e87kB0wOiSqMNt8UqEkdzNxzmqdNj%2BJa%2F78It2aF5jZozzFDZzLTbnyl9CjE3qRUMJ8GNwMx1wjOEwX%2BbIgc&X-Amz-Signature=e1068601ff24feec3901e782ec71b71df7ef9df3bb626bdb00fddc8ef6bc00af&X-Amz-SignedHeaders=host&x-id=GetObject)
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


