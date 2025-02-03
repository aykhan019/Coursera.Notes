

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZBK3P5H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDESk3rTIG7a4OFLBZ0V2boRU4IDVwkb5Gc%2FntkwYk3GAIgMCBHCb9K5NUxtlCkHSPtSjZVI8sq%2FgFTyoErxr2aISIq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDIvEUkJ%2FfS9j%2BAaoBCrcAzRNXUA4Gv0KRRd%2Bf5BdAUjvB6O2OJ3yu8n5eCGKiIeuFX1GrrxyqnbrNlkONACJv5WiUKUITTWTQ8OGxgRPKdFt5w2nsnXzlAI7fdiPUcyhf%2FPvvIOsIy5EVw9gIxrP%2BQMD54HlyXrJHcOjXFc7%2FF9k6lRBcsxmr%2B9LMN1MKYLAh0vkgBsepukG7pLXrTOYZvfWQyFMAupYpUOX87Hn4mbzldPtBzkZ794A1MsL668GoZ6VhmgrW44KoVEy4vJ9LT426Unp5zzUgnUsgNnE9iEYSQ125yPH8qL8dHlcz99WpCzHK2LbVuMc9JuhT2AtjV6WDdzRe81bDfJ14ql1FIyYxu2CSNX28PMSJgbcZDyTPs7ZC1cUUeDmNG%2BShkqrpF099fgrBabwIJ39APTxW3XKX1%2BZdrwy6JfId7UsM4T0BjDrMHaZ9uunf6DAdqCiSmSTMojeqi190Tf6PIYYiid7F7bl8x2kgfSSI2GMiInBHlHx1C0%2BK1YeZ%2FJlHCGtdBFqUPy6ptzurWqajci58tE2UnrM4PgfYj2m%2BP4nZdh%2F2lk5CUvNbehFgH7KJ9VYXbTuqLr15JjMSAE7G9W%2BdabbfGRRmTbYAW9noI0v5Z2STcmEQ7V4ClapYaw0MJO9hL0GOqUBE7wgGI14NoZHvdoX6FWNKd7r6O50JVrLncKt%2Fwh%2Bf%2BguS5afTbUP%2FRqQn9YxKW0PiPENchDQQPLZKR%2BDuUvZEqbtrWai03775NfOak5ThsmhcFdB3nywq5ey4f82ZFapZMzl7n%2BbZz1sQobWg0hJHvAjaxV%2B7dPvYpTXIo3h0WTZVTWxu6Ut%2BQs2FWmhqcV0kLoj1iOo7ubeZN12ThB%2FioPLjvkm&X-Amz-Signature=ab98e5e21ebcaa5b93a8d315a78fe65816feb0dff9d50c73d1207a3ba193af57&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKV33PDW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDUuVdp0QW9WNS82qN0Pb8871ozs7tmzN07HYA28VGgVAIhAMPjkmZgyYNyYgxFFVgL%2FSBAkBsSgQ0VoPfgqlGzvD%2FmKv8DCB0QABoMNjM3NDIzMTgzODA1Igzbt3t1GBhX2aWC5Ocq3AMkE0mehipabsYYLfNbX%2FQqsqsxUfaS2IFYfGKsZIT0x0r32dgLrBBMu9aF6tYILr%2FIpwwew8QAzH8W3IyIkL7nOBxiX2%2Bt8D2MHmNY7wsHpwDBkFHEg1Jir76k%2BpNdUBXkY5A1kw05dGoU54bIvshQfQDIUuILO1NCSATcNrogYEnbq1TndKm8q0e2R8jQHQ3vgX6bnpJHRkrrzO34lEWuxZ%2BM%2FNw2ltHZuNqhF20dwhCY7et0MwKL39wog6rtPrja%2F6oHb0%2B53ckrAtllvJETC6UjzLkvUkGS50Tarz0o0H4fo7l3hFkl5ymXKAMwj0UlNiVTWZGGLghFLbfzZl%2FXwWPWuEInaoirl7adLCHXtvAEp6MOwY4zXqMvdbymrrG6GQqWN%2BkGuQ6rimCQAXhSX7o7Qwu%2BYxNiwwA5xICpccp%2BQ2uxknJsfUnZpo7rRTBaijY9WdcOHBGuPUTlNhytiET049Lwvb%2B1Uj7%2FclZ3TFKHZEdz8pzynVhuqX0sg5FTnD26lDSUerVDwfT7ck7LmBrZUaNqBAP9oD9bdXy8qSfrp6Bo8F%2FZBfsq7RvujLt%2BZJoacj6UMMhM9z7pjrBPgiT7KEhnPrcVFiAyriDOkQgP6mUvJNl%2B%2Ft5QuDDWvIS9BjqkAVPte7wEPi3BDTVhVZOupda%2BNlxEY74cDwvQXq9hscTozr8kXtPQuvQlN1d3gcS0LR2kII5z5hsgwNAMk%2FanWCgbMXDRf0cW617v2ml17aa1Piq19Hz96WWnf%2FSwfzJnRfobNvpzAs%2BdD%2Fl%2BgXdNXHK8t2HnT0MsnuLb6jYS6Ze1PSawM%2B9U748Mko0PNvXBUR%2BIBD45K%2FYs6bTfBdFY4zGH1QFC&X-Amz-Signature=fff523654eee87c3c4972c61bb3b492b55198753e42e483a78d15fd15398f06f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKV33PDW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDUuVdp0QW9WNS82qN0Pb8871ozs7tmzN07HYA28VGgVAIhAMPjkmZgyYNyYgxFFVgL%2FSBAkBsSgQ0VoPfgqlGzvD%2FmKv8DCB0QABoMNjM3NDIzMTgzODA1Igzbt3t1GBhX2aWC5Ocq3AMkE0mehipabsYYLfNbX%2FQqsqsxUfaS2IFYfGKsZIT0x0r32dgLrBBMu9aF6tYILr%2FIpwwew8QAzH8W3IyIkL7nOBxiX2%2Bt8D2MHmNY7wsHpwDBkFHEg1Jir76k%2BpNdUBXkY5A1kw05dGoU54bIvshQfQDIUuILO1NCSATcNrogYEnbq1TndKm8q0e2R8jQHQ3vgX6bnpJHRkrrzO34lEWuxZ%2BM%2FNw2ltHZuNqhF20dwhCY7et0MwKL39wog6rtPrja%2F6oHb0%2B53ckrAtllvJETC6UjzLkvUkGS50Tarz0o0H4fo7l3hFkl5ymXKAMwj0UlNiVTWZGGLghFLbfzZl%2FXwWPWuEInaoirl7adLCHXtvAEp6MOwY4zXqMvdbymrrG6GQqWN%2BkGuQ6rimCQAXhSX7o7Qwu%2BYxNiwwA5xICpccp%2BQ2uxknJsfUnZpo7rRTBaijY9WdcOHBGuPUTlNhytiET049Lwvb%2B1Uj7%2FclZ3TFKHZEdz8pzynVhuqX0sg5FTnD26lDSUerVDwfT7ck7LmBrZUaNqBAP9oD9bdXy8qSfrp6Bo8F%2FZBfsq7RvujLt%2BZJoacj6UMMhM9z7pjrBPgiT7KEhnPrcVFiAyriDOkQgP6mUvJNl%2B%2Ft5QuDDWvIS9BjqkAVPte7wEPi3BDTVhVZOupda%2BNlxEY74cDwvQXq9hscTozr8kXtPQuvQlN1d3gcS0LR2kII5z5hsgwNAMk%2FanWCgbMXDRf0cW617v2ml17aa1Piq19Hz96WWnf%2FSwfzJnRfobNvpzAs%2BdD%2Fl%2BgXdNXHK8t2HnT0MsnuLb6jYS6Ze1PSawM%2B9U748Mko0PNvXBUR%2BIBD45K%2FYs6bTfBdFY4zGH1QFC&X-Amz-Signature=bfc0bca97fd8501a07d116e4af311f76ed185935dd7bd6c61efbb23de0248b98&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKV33PDW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDUuVdp0QW9WNS82qN0Pb8871ozs7tmzN07HYA28VGgVAIhAMPjkmZgyYNyYgxFFVgL%2FSBAkBsSgQ0VoPfgqlGzvD%2FmKv8DCB0QABoMNjM3NDIzMTgzODA1Igzbt3t1GBhX2aWC5Ocq3AMkE0mehipabsYYLfNbX%2FQqsqsxUfaS2IFYfGKsZIT0x0r32dgLrBBMu9aF6tYILr%2FIpwwew8QAzH8W3IyIkL7nOBxiX2%2Bt8D2MHmNY7wsHpwDBkFHEg1Jir76k%2BpNdUBXkY5A1kw05dGoU54bIvshQfQDIUuILO1NCSATcNrogYEnbq1TndKm8q0e2R8jQHQ3vgX6bnpJHRkrrzO34lEWuxZ%2BM%2FNw2ltHZuNqhF20dwhCY7et0MwKL39wog6rtPrja%2F6oHb0%2B53ckrAtllvJETC6UjzLkvUkGS50Tarz0o0H4fo7l3hFkl5ymXKAMwj0UlNiVTWZGGLghFLbfzZl%2FXwWPWuEInaoirl7adLCHXtvAEp6MOwY4zXqMvdbymrrG6GQqWN%2BkGuQ6rimCQAXhSX7o7Qwu%2BYxNiwwA5xICpccp%2BQ2uxknJsfUnZpo7rRTBaijY9WdcOHBGuPUTlNhytiET049Lwvb%2B1Uj7%2FclZ3TFKHZEdz8pzynVhuqX0sg5FTnD26lDSUerVDwfT7ck7LmBrZUaNqBAP9oD9bdXy8qSfrp6Bo8F%2FZBfsq7RvujLt%2BZJoacj6UMMhM9z7pjrBPgiT7KEhnPrcVFiAyriDOkQgP6mUvJNl%2B%2Ft5QuDDWvIS9BjqkAVPte7wEPi3BDTVhVZOupda%2BNlxEY74cDwvQXq9hscTozr8kXtPQuvQlN1d3gcS0LR2kII5z5hsgwNAMk%2FanWCgbMXDRf0cW617v2ml17aa1Piq19Hz96WWnf%2FSwfzJnRfobNvpzAs%2BdD%2Fl%2BgXdNXHK8t2HnT0MsnuLb6jYS6Ze1PSawM%2B9U748Mko0PNvXBUR%2BIBD45K%2FYs6bTfBdFY4zGH1QFC&X-Amz-Signature=d0a6e3c32df0e811cc2190f8c3d04070f10918fec1f092e193d5e57b51367a7d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKV33PDW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDUuVdp0QW9WNS82qN0Pb8871ozs7tmzN07HYA28VGgVAIhAMPjkmZgyYNyYgxFFVgL%2FSBAkBsSgQ0VoPfgqlGzvD%2FmKv8DCB0QABoMNjM3NDIzMTgzODA1Igzbt3t1GBhX2aWC5Ocq3AMkE0mehipabsYYLfNbX%2FQqsqsxUfaS2IFYfGKsZIT0x0r32dgLrBBMu9aF6tYILr%2FIpwwew8QAzH8W3IyIkL7nOBxiX2%2Bt8D2MHmNY7wsHpwDBkFHEg1Jir76k%2BpNdUBXkY5A1kw05dGoU54bIvshQfQDIUuILO1NCSATcNrogYEnbq1TndKm8q0e2R8jQHQ3vgX6bnpJHRkrrzO34lEWuxZ%2BM%2FNw2ltHZuNqhF20dwhCY7et0MwKL39wog6rtPrja%2F6oHb0%2B53ckrAtllvJETC6UjzLkvUkGS50Tarz0o0H4fo7l3hFkl5ymXKAMwj0UlNiVTWZGGLghFLbfzZl%2FXwWPWuEInaoirl7adLCHXtvAEp6MOwY4zXqMvdbymrrG6GQqWN%2BkGuQ6rimCQAXhSX7o7Qwu%2BYxNiwwA5xICpccp%2BQ2uxknJsfUnZpo7rRTBaijY9WdcOHBGuPUTlNhytiET049Lwvb%2B1Uj7%2FclZ3TFKHZEdz8pzynVhuqX0sg5FTnD26lDSUerVDwfT7ck7LmBrZUaNqBAP9oD9bdXy8qSfrp6Bo8F%2FZBfsq7RvujLt%2BZJoacj6UMMhM9z7pjrBPgiT7KEhnPrcVFiAyriDOkQgP6mUvJNl%2B%2Ft5QuDDWvIS9BjqkAVPte7wEPi3BDTVhVZOupda%2BNlxEY74cDwvQXq9hscTozr8kXtPQuvQlN1d3gcS0LR2kII5z5hsgwNAMk%2FanWCgbMXDRf0cW617v2ml17aa1Piq19Hz96WWnf%2FSwfzJnRfobNvpzAs%2BdD%2Fl%2BgXdNXHK8t2HnT0MsnuLb6jYS6Ze1PSawM%2B9U748Mko0PNvXBUR%2BIBD45K%2FYs6bTfBdFY4zGH1QFC&X-Amz-Signature=0bc3c1fc11e9c5a7b6468faafc52cb350ee6079744e5acd8e2080b5f841e3766&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKV33PDW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDUuVdp0QW9WNS82qN0Pb8871ozs7tmzN07HYA28VGgVAIhAMPjkmZgyYNyYgxFFVgL%2FSBAkBsSgQ0VoPfgqlGzvD%2FmKv8DCB0QABoMNjM3NDIzMTgzODA1Igzbt3t1GBhX2aWC5Ocq3AMkE0mehipabsYYLfNbX%2FQqsqsxUfaS2IFYfGKsZIT0x0r32dgLrBBMu9aF6tYILr%2FIpwwew8QAzH8W3IyIkL7nOBxiX2%2Bt8D2MHmNY7wsHpwDBkFHEg1Jir76k%2BpNdUBXkY5A1kw05dGoU54bIvshQfQDIUuILO1NCSATcNrogYEnbq1TndKm8q0e2R8jQHQ3vgX6bnpJHRkrrzO34lEWuxZ%2BM%2FNw2ltHZuNqhF20dwhCY7et0MwKL39wog6rtPrja%2F6oHb0%2B53ckrAtllvJETC6UjzLkvUkGS50Tarz0o0H4fo7l3hFkl5ymXKAMwj0UlNiVTWZGGLghFLbfzZl%2FXwWPWuEInaoirl7adLCHXtvAEp6MOwY4zXqMvdbymrrG6GQqWN%2BkGuQ6rimCQAXhSX7o7Qwu%2BYxNiwwA5xICpccp%2BQ2uxknJsfUnZpo7rRTBaijY9WdcOHBGuPUTlNhytiET049Lwvb%2B1Uj7%2FclZ3TFKHZEdz8pzynVhuqX0sg5FTnD26lDSUerVDwfT7ck7LmBrZUaNqBAP9oD9bdXy8qSfrp6Bo8F%2FZBfsq7RvujLt%2BZJoacj6UMMhM9z7pjrBPgiT7KEhnPrcVFiAyriDOkQgP6mUvJNl%2B%2Ft5QuDDWvIS9BjqkAVPte7wEPi3BDTVhVZOupda%2BNlxEY74cDwvQXq9hscTozr8kXtPQuvQlN1d3gcS0LR2kII5z5hsgwNAMk%2FanWCgbMXDRf0cW617v2ml17aa1Piq19Hz96WWnf%2FSwfzJnRfobNvpzAs%2BdD%2Fl%2BgXdNXHK8t2HnT0MsnuLb6jYS6Ze1PSawM%2B9U748Mko0PNvXBUR%2BIBD45K%2FYs6bTfBdFY4zGH1QFC&X-Amz-Signature=828dd00e4464d0a08c029c3c53c861d3bf3cb200c2409ae135246d9664f6a39e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZBK3P5H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDESk3rTIG7a4OFLBZ0V2boRU4IDVwkb5Gc%2FntkwYk3GAIgMCBHCb9K5NUxtlCkHSPtSjZVI8sq%2FgFTyoErxr2aISIq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDIvEUkJ%2FfS9j%2BAaoBCrcAzRNXUA4Gv0KRRd%2Bf5BdAUjvB6O2OJ3yu8n5eCGKiIeuFX1GrrxyqnbrNlkONACJv5WiUKUITTWTQ8OGxgRPKdFt5w2nsnXzlAI7fdiPUcyhf%2FPvvIOsIy5EVw9gIxrP%2BQMD54HlyXrJHcOjXFc7%2FF9k6lRBcsxmr%2B9LMN1MKYLAh0vkgBsepukG7pLXrTOYZvfWQyFMAupYpUOX87Hn4mbzldPtBzkZ794A1MsL668GoZ6VhmgrW44KoVEy4vJ9LT426Unp5zzUgnUsgNnE9iEYSQ125yPH8qL8dHlcz99WpCzHK2LbVuMc9JuhT2AtjV6WDdzRe81bDfJ14ql1FIyYxu2CSNX28PMSJgbcZDyTPs7ZC1cUUeDmNG%2BShkqrpF099fgrBabwIJ39APTxW3XKX1%2BZdrwy6JfId7UsM4T0BjDrMHaZ9uunf6DAdqCiSmSTMojeqi190Tf6PIYYiid7F7bl8x2kgfSSI2GMiInBHlHx1C0%2BK1YeZ%2FJlHCGtdBFqUPy6ptzurWqajci58tE2UnrM4PgfYj2m%2BP4nZdh%2F2lk5CUvNbehFgH7KJ9VYXbTuqLr15JjMSAE7G9W%2BdabbfGRRmTbYAW9noI0v5Z2STcmEQ7V4ClapYaw0MJO9hL0GOqUBE7wgGI14NoZHvdoX6FWNKd7r6O50JVrLncKt%2Fwh%2Bf%2BguS5afTbUP%2FRqQn9YxKW0PiPENchDQQPLZKR%2BDuUvZEqbtrWai03775NfOak5ThsmhcFdB3nywq5ey4f82ZFapZMzl7n%2BbZz1sQobWg0hJHvAjaxV%2B7dPvYpTXIo3h0WTZVTWxu6Ut%2BQs2FWmhqcV0kLoj1iOo7ubeZN12ThB%2FioPLjvkm&X-Amz-Signature=4fab5a2516727a68cd823b89efafe0319c9323125675fcc53a2739f5c5625910&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZBK3P5H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDESk3rTIG7a4OFLBZ0V2boRU4IDVwkb5Gc%2FntkwYk3GAIgMCBHCb9K5NUxtlCkHSPtSjZVI8sq%2FgFTyoErxr2aISIq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDIvEUkJ%2FfS9j%2BAaoBCrcAzRNXUA4Gv0KRRd%2Bf5BdAUjvB6O2OJ3yu8n5eCGKiIeuFX1GrrxyqnbrNlkONACJv5WiUKUITTWTQ8OGxgRPKdFt5w2nsnXzlAI7fdiPUcyhf%2FPvvIOsIy5EVw9gIxrP%2BQMD54HlyXrJHcOjXFc7%2FF9k6lRBcsxmr%2B9LMN1MKYLAh0vkgBsepukG7pLXrTOYZvfWQyFMAupYpUOX87Hn4mbzldPtBzkZ794A1MsL668GoZ6VhmgrW44KoVEy4vJ9LT426Unp5zzUgnUsgNnE9iEYSQ125yPH8qL8dHlcz99WpCzHK2LbVuMc9JuhT2AtjV6WDdzRe81bDfJ14ql1FIyYxu2CSNX28PMSJgbcZDyTPs7ZC1cUUeDmNG%2BShkqrpF099fgrBabwIJ39APTxW3XKX1%2BZdrwy6JfId7UsM4T0BjDrMHaZ9uunf6DAdqCiSmSTMojeqi190Tf6PIYYiid7F7bl8x2kgfSSI2GMiInBHlHx1C0%2BK1YeZ%2FJlHCGtdBFqUPy6ptzurWqajci58tE2UnrM4PgfYj2m%2BP4nZdh%2F2lk5CUvNbehFgH7KJ9VYXbTuqLr15JjMSAE7G9W%2BdabbfGRRmTbYAW9noI0v5Z2STcmEQ7V4ClapYaw0MJO9hL0GOqUBE7wgGI14NoZHvdoX6FWNKd7r6O50JVrLncKt%2Fwh%2Bf%2BguS5afTbUP%2FRqQn9YxKW0PiPENchDQQPLZKR%2BDuUvZEqbtrWai03775NfOak5ThsmhcFdB3nywq5ey4f82ZFapZMzl7n%2BbZz1sQobWg0hJHvAjaxV%2B7dPvYpTXIo3h0WTZVTWxu6Ut%2BQs2FWmhqcV0kLoj1iOo7ubeZN12ThB%2FioPLjvkm&X-Amz-Signature=a066e70fd10316b3b00974940df7ebe153a6fa8ad1a49276cb00a76c9980d6b1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZBK3P5H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDESk3rTIG7a4OFLBZ0V2boRU4IDVwkb5Gc%2FntkwYk3GAIgMCBHCb9K5NUxtlCkHSPtSjZVI8sq%2FgFTyoErxr2aISIq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDIvEUkJ%2FfS9j%2BAaoBCrcAzRNXUA4Gv0KRRd%2Bf5BdAUjvB6O2OJ3yu8n5eCGKiIeuFX1GrrxyqnbrNlkONACJv5WiUKUITTWTQ8OGxgRPKdFt5w2nsnXzlAI7fdiPUcyhf%2FPvvIOsIy5EVw9gIxrP%2BQMD54HlyXrJHcOjXFc7%2FF9k6lRBcsxmr%2B9LMN1MKYLAh0vkgBsepukG7pLXrTOYZvfWQyFMAupYpUOX87Hn4mbzldPtBzkZ794A1MsL668GoZ6VhmgrW44KoVEy4vJ9LT426Unp5zzUgnUsgNnE9iEYSQ125yPH8qL8dHlcz99WpCzHK2LbVuMc9JuhT2AtjV6WDdzRe81bDfJ14ql1FIyYxu2CSNX28PMSJgbcZDyTPs7ZC1cUUeDmNG%2BShkqrpF099fgrBabwIJ39APTxW3XKX1%2BZdrwy6JfId7UsM4T0BjDrMHaZ9uunf6DAdqCiSmSTMojeqi190Tf6PIYYiid7F7bl8x2kgfSSI2GMiInBHlHx1C0%2BK1YeZ%2FJlHCGtdBFqUPy6ptzurWqajci58tE2UnrM4PgfYj2m%2BP4nZdh%2F2lk5CUvNbehFgH7KJ9VYXbTuqLr15JjMSAE7G9W%2BdabbfGRRmTbYAW9noI0v5Z2STcmEQ7V4ClapYaw0MJO9hL0GOqUBE7wgGI14NoZHvdoX6FWNKd7r6O50JVrLncKt%2Fwh%2Bf%2BguS5afTbUP%2FRqQn9YxKW0PiPENchDQQPLZKR%2BDuUvZEqbtrWai03775NfOak5ThsmhcFdB3nywq5ey4f82ZFapZMzl7n%2BbZz1sQobWg0hJHvAjaxV%2B7dPvYpTXIo3h0WTZVTWxu6Ut%2BQs2FWmhqcV0kLoj1iOo7ubeZN12ThB%2FioPLjvkm&X-Amz-Signature=b63a49777f6a4e8a2628bf85a4891d7aa763d89365041ab9890fdfee4d9bcde1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZBK3P5H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDESk3rTIG7a4OFLBZ0V2boRU4IDVwkb5Gc%2FntkwYk3GAIgMCBHCb9K5NUxtlCkHSPtSjZVI8sq%2FgFTyoErxr2aISIq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDIvEUkJ%2FfS9j%2BAaoBCrcAzRNXUA4Gv0KRRd%2Bf5BdAUjvB6O2OJ3yu8n5eCGKiIeuFX1GrrxyqnbrNlkONACJv5WiUKUITTWTQ8OGxgRPKdFt5w2nsnXzlAI7fdiPUcyhf%2FPvvIOsIy5EVw9gIxrP%2BQMD54HlyXrJHcOjXFc7%2FF9k6lRBcsxmr%2B9LMN1MKYLAh0vkgBsepukG7pLXrTOYZvfWQyFMAupYpUOX87Hn4mbzldPtBzkZ794A1MsL668GoZ6VhmgrW44KoVEy4vJ9LT426Unp5zzUgnUsgNnE9iEYSQ125yPH8qL8dHlcz99WpCzHK2LbVuMc9JuhT2AtjV6WDdzRe81bDfJ14ql1FIyYxu2CSNX28PMSJgbcZDyTPs7ZC1cUUeDmNG%2BShkqrpF099fgrBabwIJ39APTxW3XKX1%2BZdrwy6JfId7UsM4T0BjDrMHaZ9uunf6DAdqCiSmSTMojeqi190Tf6PIYYiid7F7bl8x2kgfSSI2GMiInBHlHx1C0%2BK1YeZ%2FJlHCGtdBFqUPy6ptzurWqajci58tE2UnrM4PgfYj2m%2BP4nZdh%2F2lk5CUvNbehFgH7KJ9VYXbTuqLr15JjMSAE7G9W%2BdabbfGRRmTbYAW9noI0v5Z2STcmEQ7V4ClapYaw0MJO9hL0GOqUBE7wgGI14NoZHvdoX6FWNKd7r6O50JVrLncKt%2Fwh%2Bf%2BguS5afTbUP%2FRqQn9YxKW0PiPENchDQQPLZKR%2BDuUvZEqbtrWai03775NfOak5ThsmhcFdB3nywq5ey4f82ZFapZMzl7n%2BbZz1sQobWg0hJHvAjaxV%2B7dPvYpTXIo3h0WTZVTWxu6Ut%2BQs2FWmhqcV0kLoj1iOo7ubeZN12ThB%2FioPLjvkm&X-Amz-Signature=a8a6e26bc595751fbc50fa57e5354b352c644490aa0aeaf4c9e884dd631bcdd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZBK3P5H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDESk3rTIG7a4OFLBZ0V2boRU4IDVwkb5Gc%2FntkwYk3GAIgMCBHCb9K5NUxtlCkHSPtSjZVI8sq%2FgFTyoErxr2aISIq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDIvEUkJ%2FfS9j%2BAaoBCrcAzRNXUA4Gv0KRRd%2Bf5BdAUjvB6O2OJ3yu8n5eCGKiIeuFX1GrrxyqnbrNlkONACJv5WiUKUITTWTQ8OGxgRPKdFt5w2nsnXzlAI7fdiPUcyhf%2FPvvIOsIy5EVw9gIxrP%2BQMD54HlyXrJHcOjXFc7%2FF9k6lRBcsxmr%2B9LMN1MKYLAh0vkgBsepukG7pLXrTOYZvfWQyFMAupYpUOX87Hn4mbzldPtBzkZ794A1MsL668GoZ6VhmgrW44KoVEy4vJ9LT426Unp5zzUgnUsgNnE9iEYSQ125yPH8qL8dHlcz99WpCzHK2LbVuMc9JuhT2AtjV6WDdzRe81bDfJ14ql1FIyYxu2CSNX28PMSJgbcZDyTPs7ZC1cUUeDmNG%2BShkqrpF099fgrBabwIJ39APTxW3XKX1%2BZdrwy6JfId7UsM4T0BjDrMHaZ9uunf6DAdqCiSmSTMojeqi190Tf6PIYYiid7F7bl8x2kgfSSI2GMiInBHlHx1C0%2BK1YeZ%2FJlHCGtdBFqUPy6ptzurWqajci58tE2UnrM4PgfYj2m%2BP4nZdh%2F2lk5CUvNbehFgH7KJ9VYXbTuqLr15JjMSAE7G9W%2BdabbfGRRmTbYAW9noI0v5Z2STcmEQ7V4ClapYaw0MJO9hL0GOqUBE7wgGI14NoZHvdoX6FWNKd7r6O50JVrLncKt%2Fwh%2Bf%2BguS5afTbUP%2FRqQn9YxKW0PiPENchDQQPLZKR%2BDuUvZEqbtrWai03775NfOak5ThsmhcFdB3nywq5ey4f82ZFapZMzl7n%2BbZz1sQobWg0hJHvAjaxV%2B7dPvYpTXIo3h0WTZVTWxu6Ut%2BQs2FWmhqcV0kLoj1iOo7ubeZN12ThB%2FioPLjvkm&X-Amz-Signature=afb5368c7359dea64d39eaea16d260149fda32de2651aec03e888604afc74251&X-Amz-SignedHeaders=host&x-id=GetObject)
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


