

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USV7APTD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDofiZgntSwy3IzZDd6g5Xlxlt22kYUY6in8kn8pBuGNQIhANNQzQXrIJAIyM7rBi4zdzZ5CmoJ%2BU5eX21atVzVYb5IKv8DCF8QABoMNjM3NDIzMTgzODA1Igw5LPKNPrusrKFyjQQq3AM8cktFRlmiIG5QTc4nFQl%2BPGddbCGHXIPdfCVr4V%2B65FIZ3kJZphQpyrCqLIie1sedGB6B68G7Mz5ix3s07A2uRm9qs%2Bduij0KT3R7mR%2F3zMDMtoxQOldkkoVvGxxlo%2B3WUFSQndjO15sTcNnBMFBwJ6Ce674Z%2BzPC%2FEj82vQEqkMGA5VFNcGUDj78BamjQBAd8mo6wFu0EYuK2YOtgk5vF8%2BhL67xDsrjmagWxYJPhYmzzGtmv5fgpHhV90nhVPUxAEtgEyZRlNomrBy8LFkr5Z1vg%2FkJxvRRZDE58DMORCfTGwlpJFJVPRWPAuRrgxT%2FWmMtsd%2BsN3BiUPdkpdQrnmgZ94Ix1VJEtxC4NhBdHkhT4Q3oTJG%2FoKSy0904W5V11CnOpzhSBErs89DgdsWwo0G5HN0WXsdv6tYrDeQ%2FBs7RQmhhN8mTVB8Wv0B5DfThRO9go4WQ961VMy6lYUuVxIXvv%2FU%2BhuN2gR%2BBKZFNZG4%2B%2Bd6kSty4AmiY%2BtqL07Y1vMxuxCpOXGLEsoFLmyMvZt5ybLQrHXEP28m%2BUsUHkCE3atmMXofS4RK4ZvOUepfPvYQZpA5fQPIZxXF7NdOiZ7%2BAZwbvMZelyLT2uFzwPY5luZny2yCCVx5DITDw%2BJK9BjqkAbnmqP4vj0inBVTyQAMayQl%2BvUIMdNDxZ9wX6IwfKfdgra%2FgpVkGvX2b18KeX38eCAfxImXNKOigoxV5%2BpD9dy0quyaFGu33KAxab12PKgH0dj9hF77DAlRFOv33QwPuQStpAxryvDvjmEuOv1zPKbaoZk1W1NGLaZOBuIgYVHETIYl6L%2FCn0ZYRqm94lx5m3UVY4gOxYW1iD1ahww7xoeiHCcOp&X-Amz-Signature=10d038b884a6a384742a285a65a2274785a7a7bfab68479f570831e318665f72&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UACI27H6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCKcU8oeau5mp2XeBIYyn3jhdcAcU%2FpSJVOcxngbs0m2wIga%2B3nOOES77YdC4A4ys%2FprQHgt8%2BBUWSENn20lUDJ%2Broq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDNGfDPur2QnoriVCcSrcA9YQ0cWKOddraQ1VpJCVsqpwyeJQuH9xzffChmKbO8lYrrPoUuyYS4yNXC0QBagi7qHqhf2Yg4kq%2BmOEL%2FWaVxSEzDXCDvIb1JWk79kkyrP2aS8H95cvYbYrQYElxcK0KjZzTrX0pgc4DT%2BB7x0wlA%2FRkoeoDkaMEKsDzlppOEQPO6tetUKYCzrN4%2B1d99Q%2FZT1FB508f4swlVfxXF%2B1Z5wyAiy8IJWdqYkV5o%2Bfglv5qHxkF0jZ6XmdGqXU3PG7w7T2Bh1A%2B1AmcWuIekMmUbtw1iuNSawZyg5bmHWd9wMA1JWVWYufvulCh6YbCSc4CE6vHSl5W19eOwui4LYbzV4RSWj5gKQkWBkfWUNPXAwf9ucRAeRp3%2B2kkaEyLVXO1JnJZq4fKco9zanSTsfEI9RauuVM6WR8o9aBy%2BbwniBYbumblmgmuT5TguT1lwnzKn1CLZhulELjjgbJVRTujH%2F1hXBfFh94ntfLa2mcuqPcW4gbSWf859Y4igfWs6hczTwY2EAAnwXc68aT1jRibWqcvOhyRHUTKtl5Lo%2F%2F%2FI%2FYkTwIsaZ5j1o72jCi7xyQBz%2FluaePSctdfx%2FVDqoDj69VrP07dF6HeG5MuYal07%2F0TPjNFVjn9o8OSKd7MKj5kr0GOqUB%2FD6eGv8ifJcqULr5dl5ijeWOhOqYnykqwY7FC%2BcFyTJk0ktos6GWbG%2F4%2BWDKHTAQjF3yteirJBTTGhX2I%2BCYGG7K7zRvzZ3U3Wk%2FCASZpGR8CUn%2FYSedf%2FY8qg76N4ywDFxjz7ZkiIQeYYCqPt0RbTb5hdQzw4Wq43hl7Ya1cmg9YaJLqay%2FHUVATTYeWfdzoT8N68s4wuU1WXd%2Bm6VDxPraqxuo&X-Amz-Signature=8f89ef7f6406fe2d8ef61fa38d33152ac8472869a77af9bfb5ab19534f1b7330&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UACI27H6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCKcU8oeau5mp2XeBIYyn3jhdcAcU%2FpSJVOcxngbs0m2wIga%2B3nOOES77YdC4A4ys%2FprQHgt8%2BBUWSENn20lUDJ%2Broq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDNGfDPur2QnoriVCcSrcA9YQ0cWKOddraQ1VpJCVsqpwyeJQuH9xzffChmKbO8lYrrPoUuyYS4yNXC0QBagi7qHqhf2Yg4kq%2BmOEL%2FWaVxSEzDXCDvIb1JWk79kkyrP2aS8H95cvYbYrQYElxcK0KjZzTrX0pgc4DT%2BB7x0wlA%2FRkoeoDkaMEKsDzlppOEQPO6tetUKYCzrN4%2B1d99Q%2FZT1FB508f4swlVfxXF%2B1Z5wyAiy8IJWdqYkV5o%2Bfglv5qHxkF0jZ6XmdGqXU3PG7w7T2Bh1A%2B1AmcWuIekMmUbtw1iuNSawZyg5bmHWd9wMA1JWVWYufvulCh6YbCSc4CE6vHSl5W19eOwui4LYbzV4RSWj5gKQkWBkfWUNPXAwf9ucRAeRp3%2B2kkaEyLVXO1JnJZq4fKco9zanSTsfEI9RauuVM6WR8o9aBy%2BbwniBYbumblmgmuT5TguT1lwnzKn1CLZhulELjjgbJVRTujH%2F1hXBfFh94ntfLa2mcuqPcW4gbSWf859Y4igfWs6hczTwY2EAAnwXc68aT1jRibWqcvOhyRHUTKtl5Lo%2F%2F%2FI%2FYkTwIsaZ5j1o72jCi7xyQBz%2FluaePSctdfx%2FVDqoDj69VrP07dF6HeG5MuYal07%2F0TPjNFVjn9o8OSKd7MKj5kr0GOqUB%2FD6eGv8ifJcqULr5dl5ijeWOhOqYnykqwY7FC%2BcFyTJk0ktos6GWbG%2F4%2BWDKHTAQjF3yteirJBTTGhX2I%2BCYGG7K7zRvzZ3U3Wk%2FCASZpGR8CUn%2FYSedf%2FY8qg76N4ywDFxjz7ZkiIQeYYCqPt0RbTb5hdQzw4Wq43hl7Ya1cmg9YaJLqay%2FHUVATTYeWfdzoT8N68s4wuU1WXd%2Bm6VDxPraqxuo&X-Amz-Signature=cff5c72eb92dbc9d1fde8fab34c27aaebc997c47c9a1c9b9997ad9cefda73c1c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UACI27H6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCKcU8oeau5mp2XeBIYyn3jhdcAcU%2FpSJVOcxngbs0m2wIga%2B3nOOES77YdC4A4ys%2FprQHgt8%2BBUWSENn20lUDJ%2Broq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDNGfDPur2QnoriVCcSrcA9YQ0cWKOddraQ1VpJCVsqpwyeJQuH9xzffChmKbO8lYrrPoUuyYS4yNXC0QBagi7qHqhf2Yg4kq%2BmOEL%2FWaVxSEzDXCDvIb1JWk79kkyrP2aS8H95cvYbYrQYElxcK0KjZzTrX0pgc4DT%2BB7x0wlA%2FRkoeoDkaMEKsDzlppOEQPO6tetUKYCzrN4%2B1d99Q%2FZT1FB508f4swlVfxXF%2B1Z5wyAiy8IJWdqYkV5o%2Bfglv5qHxkF0jZ6XmdGqXU3PG7w7T2Bh1A%2B1AmcWuIekMmUbtw1iuNSawZyg5bmHWd9wMA1JWVWYufvulCh6YbCSc4CE6vHSl5W19eOwui4LYbzV4RSWj5gKQkWBkfWUNPXAwf9ucRAeRp3%2B2kkaEyLVXO1JnJZq4fKco9zanSTsfEI9RauuVM6WR8o9aBy%2BbwniBYbumblmgmuT5TguT1lwnzKn1CLZhulELjjgbJVRTujH%2F1hXBfFh94ntfLa2mcuqPcW4gbSWf859Y4igfWs6hczTwY2EAAnwXc68aT1jRibWqcvOhyRHUTKtl5Lo%2F%2F%2FI%2FYkTwIsaZ5j1o72jCi7xyQBz%2FluaePSctdfx%2FVDqoDj69VrP07dF6HeG5MuYal07%2F0TPjNFVjn9o8OSKd7MKj5kr0GOqUB%2FD6eGv8ifJcqULr5dl5ijeWOhOqYnykqwY7FC%2BcFyTJk0ktos6GWbG%2F4%2BWDKHTAQjF3yteirJBTTGhX2I%2BCYGG7K7zRvzZ3U3Wk%2FCASZpGR8CUn%2FYSedf%2FY8qg76N4ywDFxjz7ZkiIQeYYCqPt0RbTb5hdQzw4Wq43hl7Ya1cmg9YaJLqay%2FHUVATTYeWfdzoT8N68s4wuU1WXd%2Bm6VDxPraqxuo&X-Amz-Signature=dbd791aaa0ac7b6050fddc5c58456dc9e238e26cc79be7d374fed32001645473&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UACI27H6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCKcU8oeau5mp2XeBIYyn3jhdcAcU%2FpSJVOcxngbs0m2wIga%2B3nOOES77YdC4A4ys%2FprQHgt8%2BBUWSENn20lUDJ%2Broq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDNGfDPur2QnoriVCcSrcA9YQ0cWKOddraQ1VpJCVsqpwyeJQuH9xzffChmKbO8lYrrPoUuyYS4yNXC0QBagi7qHqhf2Yg4kq%2BmOEL%2FWaVxSEzDXCDvIb1JWk79kkyrP2aS8H95cvYbYrQYElxcK0KjZzTrX0pgc4DT%2BB7x0wlA%2FRkoeoDkaMEKsDzlppOEQPO6tetUKYCzrN4%2B1d99Q%2FZT1FB508f4swlVfxXF%2B1Z5wyAiy8IJWdqYkV5o%2Bfglv5qHxkF0jZ6XmdGqXU3PG7w7T2Bh1A%2B1AmcWuIekMmUbtw1iuNSawZyg5bmHWd9wMA1JWVWYufvulCh6YbCSc4CE6vHSl5W19eOwui4LYbzV4RSWj5gKQkWBkfWUNPXAwf9ucRAeRp3%2B2kkaEyLVXO1JnJZq4fKco9zanSTsfEI9RauuVM6WR8o9aBy%2BbwniBYbumblmgmuT5TguT1lwnzKn1CLZhulELjjgbJVRTujH%2F1hXBfFh94ntfLa2mcuqPcW4gbSWf859Y4igfWs6hczTwY2EAAnwXc68aT1jRibWqcvOhyRHUTKtl5Lo%2F%2F%2FI%2FYkTwIsaZ5j1o72jCi7xyQBz%2FluaePSctdfx%2FVDqoDj69VrP07dF6HeG5MuYal07%2F0TPjNFVjn9o8OSKd7MKj5kr0GOqUB%2FD6eGv8ifJcqULr5dl5ijeWOhOqYnykqwY7FC%2BcFyTJk0ktos6GWbG%2F4%2BWDKHTAQjF3yteirJBTTGhX2I%2BCYGG7K7zRvzZ3U3Wk%2FCASZpGR8CUn%2FYSedf%2FY8qg76N4ywDFxjz7ZkiIQeYYCqPt0RbTb5hdQzw4Wq43hl7Ya1cmg9YaJLqay%2FHUVATTYeWfdzoT8N68s4wuU1WXd%2Bm6VDxPraqxuo&X-Amz-Signature=a4b711fd41b14acf0a8d8dc0934eb50226f4a1f2850e5fad257d902c3d1f1365&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UACI27H6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCKcU8oeau5mp2XeBIYyn3jhdcAcU%2FpSJVOcxngbs0m2wIga%2B3nOOES77YdC4A4ys%2FprQHgt8%2BBUWSENn20lUDJ%2Broq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDNGfDPur2QnoriVCcSrcA9YQ0cWKOddraQ1VpJCVsqpwyeJQuH9xzffChmKbO8lYrrPoUuyYS4yNXC0QBagi7qHqhf2Yg4kq%2BmOEL%2FWaVxSEzDXCDvIb1JWk79kkyrP2aS8H95cvYbYrQYElxcK0KjZzTrX0pgc4DT%2BB7x0wlA%2FRkoeoDkaMEKsDzlppOEQPO6tetUKYCzrN4%2B1d99Q%2FZT1FB508f4swlVfxXF%2B1Z5wyAiy8IJWdqYkV5o%2Bfglv5qHxkF0jZ6XmdGqXU3PG7w7T2Bh1A%2B1AmcWuIekMmUbtw1iuNSawZyg5bmHWd9wMA1JWVWYufvulCh6YbCSc4CE6vHSl5W19eOwui4LYbzV4RSWj5gKQkWBkfWUNPXAwf9ucRAeRp3%2B2kkaEyLVXO1JnJZq4fKco9zanSTsfEI9RauuVM6WR8o9aBy%2BbwniBYbumblmgmuT5TguT1lwnzKn1CLZhulELjjgbJVRTujH%2F1hXBfFh94ntfLa2mcuqPcW4gbSWf859Y4igfWs6hczTwY2EAAnwXc68aT1jRibWqcvOhyRHUTKtl5Lo%2F%2F%2FI%2FYkTwIsaZ5j1o72jCi7xyQBz%2FluaePSctdfx%2FVDqoDj69VrP07dF6HeG5MuYal07%2F0TPjNFVjn9o8OSKd7MKj5kr0GOqUB%2FD6eGv8ifJcqULr5dl5ijeWOhOqYnykqwY7FC%2BcFyTJk0ktos6GWbG%2F4%2BWDKHTAQjF3yteirJBTTGhX2I%2BCYGG7K7zRvzZ3U3Wk%2FCASZpGR8CUn%2FYSedf%2FY8qg76N4ywDFxjz7ZkiIQeYYCqPt0RbTb5hdQzw4Wq43hl7Ya1cmg9YaJLqay%2FHUVATTYeWfdzoT8N68s4wuU1WXd%2Bm6VDxPraqxuo&X-Amz-Signature=53c5f78a4e26fa6390f465bbf974fce8429d32cace69c1e8505eddc486f91419&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USV7APTD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDofiZgntSwy3IzZDd6g5Xlxlt22kYUY6in8kn8pBuGNQIhANNQzQXrIJAIyM7rBi4zdzZ5CmoJ%2BU5eX21atVzVYb5IKv8DCF8QABoMNjM3NDIzMTgzODA1Igw5LPKNPrusrKFyjQQq3AM8cktFRlmiIG5QTc4nFQl%2BPGddbCGHXIPdfCVr4V%2B65FIZ3kJZphQpyrCqLIie1sedGB6B68G7Mz5ix3s07A2uRm9qs%2Bduij0KT3R7mR%2F3zMDMtoxQOldkkoVvGxxlo%2B3WUFSQndjO15sTcNnBMFBwJ6Ce674Z%2BzPC%2FEj82vQEqkMGA5VFNcGUDj78BamjQBAd8mo6wFu0EYuK2YOtgk5vF8%2BhL67xDsrjmagWxYJPhYmzzGtmv5fgpHhV90nhVPUxAEtgEyZRlNomrBy8LFkr5Z1vg%2FkJxvRRZDE58DMORCfTGwlpJFJVPRWPAuRrgxT%2FWmMtsd%2BsN3BiUPdkpdQrnmgZ94Ix1VJEtxC4NhBdHkhT4Q3oTJG%2FoKSy0904W5V11CnOpzhSBErs89DgdsWwo0G5HN0WXsdv6tYrDeQ%2FBs7RQmhhN8mTVB8Wv0B5DfThRO9go4WQ961VMy6lYUuVxIXvv%2FU%2BhuN2gR%2BBKZFNZG4%2B%2Bd6kSty4AmiY%2BtqL07Y1vMxuxCpOXGLEsoFLmyMvZt5ybLQrHXEP28m%2BUsUHkCE3atmMXofS4RK4ZvOUepfPvYQZpA5fQPIZxXF7NdOiZ7%2BAZwbvMZelyLT2uFzwPY5luZny2yCCVx5DITDw%2BJK9BjqkAbnmqP4vj0inBVTyQAMayQl%2BvUIMdNDxZ9wX6IwfKfdgra%2FgpVkGvX2b18KeX38eCAfxImXNKOigoxV5%2BpD9dy0quyaFGu33KAxab12PKgH0dj9hF77DAlRFOv33QwPuQStpAxryvDvjmEuOv1zPKbaoZk1W1NGLaZOBuIgYVHETIYl6L%2FCn0ZYRqm94lx5m3UVY4gOxYW1iD1ahww7xoeiHCcOp&X-Amz-Signature=0348dc8f6dc9faca9e4b8f075f563994651bcf377da39841b8b6fdca52453b1f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USV7APTD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDofiZgntSwy3IzZDd6g5Xlxlt22kYUY6in8kn8pBuGNQIhANNQzQXrIJAIyM7rBi4zdzZ5CmoJ%2BU5eX21atVzVYb5IKv8DCF8QABoMNjM3NDIzMTgzODA1Igw5LPKNPrusrKFyjQQq3AM8cktFRlmiIG5QTc4nFQl%2BPGddbCGHXIPdfCVr4V%2B65FIZ3kJZphQpyrCqLIie1sedGB6B68G7Mz5ix3s07A2uRm9qs%2Bduij0KT3R7mR%2F3zMDMtoxQOldkkoVvGxxlo%2B3WUFSQndjO15sTcNnBMFBwJ6Ce674Z%2BzPC%2FEj82vQEqkMGA5VFNcGUDj78BamjQBAd8mo6wFu0EYuK2YOtgk5vF8%2BhL67xDsrjmagWxYJPhYmzzGtmv5fgpHhV90nhVPUxAEtgEyZRlNomrBy8LFkr5Z1vg%2FkJxvRRZDE58DMORCfTGwlpJFJVPRWPAuRrgxT%2FWmMtsd%2BsN3BiUPdkpdQrnmgZ94Ix1VJEtxC4NhBdHkhT4Q3oTJG%2FoKSy0904W5V11CnOpzhSBErs89DgdsWwo0G5HN0WXsdv6tYrDeQ%2FBs7RQmhhN8mTVB8Wv0B5DfThRO9go4WQ961VMy6lYUuVxIXvv%2FU%2BhuN2gR%2BBKZFNZG4%2B%2Bd6kSty4AmiY%2BtqL07Y1vMxuxCpOXGLEsoFLmyMvZt5ybLQrHXEP28m%2BUsUHkCE3atmMXofS4RK4ZvOUepfPvYQZpA5fQPIZxXF7NdOiZ7%2BAZwbvMZelyLT2uFzwPY5luZny2yCCVx5DITDw%2BJK9BjqkAbnmqP4vj0inBVTyQAMayQl%2BvUIMdNDxZ9wX6IwfKfdgra%2FgpVkGvX2b18KeX38eCAfxImXNKOigoxV5%2BpD9dy0quyaFGu33KAxab12PKgH0dj9hF77DAlRFOv33QwPuQStpAxryvDvjmEuOv1zPKbaoZk1W1NGLaZOBuIgYVHETIYl6L%2FCn0ZYRqm94lx5m3UVY4gOxYW1iD1ahww7xoeiHCcOp&X-Amz-Signature=56347af0f28d99e6d11f188a5b3d0acf8302e2b049cb0f949e6ede0f0b764958&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USV7APTD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDofiZgntSwy3IzZDd6g5Xlxlt22kYUY6in8kn8pBuGNQIhANNQzQXrIJAIyM7rBi4zdzZ5CmoJ%2BU5eX21atVzVYb5IKv8DCF8QABoMNjM3NDIzMTgzODA1Igw5LPKNPrusrKFyjQQq3AM8cktFRlmiIG5QTc4nFQl%2BPGddbCGHXIPdfCVr4V%2B65FIZ3kJZphQpyrCqLIie1sedGB6B68G7Mz5ix3s07A2uRm9qs%2Bduij0KT3R7mR%2F3zMDMtoxQOldkkoVvGxxlo%2B3WUFSQndjO15sTcNnBMFBwJ6Ce674Z%2BzPC%2FEj82vQEqkMGA5VFNcGUDj78BamjQBAd8mo6wFu0EYuK2YOtgk5vF8%2BhL67xDsrjmagWxYJPhYmzzGtmv5fgpHhV90nhVPUxAEtgEyZRlNomrBy8LFkr5Z1vg%2FkJxvRRZDE58DMORCfTGwlpJFJVPRWPAuRrgxT%2FWmMtsd%2BsN3BiUPdkpdQrnmgZ94Ix1VJEtxC4NhBdHkhT4Q3oTJG%2FoKSy0904W5V11CnOpzhSBErs89DgdsWwo0G5HN0WXsdv6tYrDeQ%2FBs7RQmhhN8mTVB8Wv0B5DfThRO9go4WQ961VMy6lYUuVxIXvv%2FU%2BhuN2gR%2BBKZFNZG4%2B%2Bd6kSty4AmiY%2BtqL07Y1vMxuxCpOXGLEsoFLmyMvZt5ybLQrHXEP28m%2BUsUHkCE3atmMXofS4RK4ZvOUepfPvYQZpA5fQPIZxXF7NdOiZ7%2BAZwbvMZelyLT2uFzwPY5luZny2yCCVx5DITDw%2BJK9BjqkAbnmqP4vj0inBVTyQAMayQl%2BvUIMdNDxZ9wX6IwfKfdgra%2FgpVkGvX2b18KeX38eCAfxImXNKOigoxV5%2BpD9dy0quyaFGu33KAxab12PKgH0dj9hF77DAlRFOv33QwPuQStpAxryvDvjmEuOv1zPKbaoZk1W1NGLaZOBuIgYVHETIYl6L%2FCn0ZYRqm94lx5m3UVY4gOxYW1iD1ahww7xoeiHCcOp&X-Amz-Signature=98812cc76fa706eba98bf279d8fdc5d2f7f64d78c66c0404908092d9582dfc96&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USV7APTD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDofiZgntSwy3IzZDd6g5Xlxlt22kYUY6in8kn8pBuGNQIhANNQzQXrIJAIyM7rBi4zdzZ5CmoJ%2BU5eX21atVzVYb5IKv8DCF8QABoMNjM3NDIzMTgzODA1Igw5LPKNPrusrKFyjQQq3AM8cktFRlmiIG5QTc4nFQl%2BPGddbCGHXIPdfCVr4V%2B65FIZ3kJZphQpyrCqLIie1sedGB6B68G7Mz5ix3s07A2uRm9qs%2Bduij0KT3R7mR%2F3zMDMtoxQOldkkoVvGxxlo%2B3WUFSQndjO15sTcNnBMFBwJ6Ce674Z%2BzPC%2FEj82vQEqkMGA5VFNcGUDj78BamjQBAd8mo6wFu0EYuK2YOtgk5vF8%2BhL67xDsrjmagWxYJPhYmzzGtmv5fgpHhV90nhVPUxAEtgEyZRlNomrBy8LFkr5Z1vg%2FkJxvRRZDE58DMORCfTGwlpJFJVPRWPAuRrgxT%2FWmMtsd%2BsN3BiUPdkpdQrnmgZ94Ix1VJEtxC4NhBdHkhT4Q3oTJG%2FoKSy0904W5V11CnOpzhSBErs89DgdsWwo0G5HN0WXsdv6tYrDeQ%2FBs7RQmhhN8mTVB8Wv0B5DfThRO9go4WQ961VMy6lYUuVxIXvv%2FU%2BhuN2gR%2BBKZFNZG4%2B%2Bd6kSty4AmiY%2BtqL07Y1vMxuxCpOXGLEsoFLmyMvZt5ybLQrHXEP28m%2BUsUHkCE3atmMXofS4RK4ZvOUepfPvYQZpA5fQPIZxXF7NdOiZ7%2BAZwbvMZelyLT2uFzwPY5luZny2yCCVx5DITDw%2BJK9BjqkAbnmqP4vj0inBVTyQAMayQl%2BvUIMdNDxZ9wX6IwfKfdgra%2FgpVkGvX2b18KeX38eCAfxImXNKOigoxV5%2BpD9dy0quyaFGu33KAxab12PKgH0dj9hF77DAlRFOv33QwPuQStpAxryvDvjmEuOv1zPKbaoZk1W1NGLaZOBuIgYVHETIYl6L%2FCn0ZYRqm94lx5m3UVY4gOxYW1iD1ahww7xoeiHCcOp&X-Amz-Signature=557f62b1867a82c2861a7c820be31a37011e9867e7068477ed7914b9333760b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USV7APTD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDofiZgntSwy3IzZDd6g5Xlxlt22kYUY6in8kn8pBuGNQIhANNQzQXrIJAIyM7rBi4zdzZ5CmoJ%2BU5eX21atVzVYb5IKv8DCF8QABoMNjM3NDIzMTgzODA1Igw5LPKNPrusrKFyjQQq3AM8cktFRlmiIG5QTc4nFQl%2BPGddbCGHXIPdfCVr4V%2B65FIZ3kJZphQpyrCqLIie1sedGB6B68G7Mz5ix3s07A2uRm9qs%2Bduij0KT3R7mR%2F3zMDMtoxQOldkkoVvGxxlo%2B3WUFSQndjO15sTcNnBMFBwJ6Ce674Z%2BzPC%2FEj82vQEqkMGA5VFNcGUDj78BamjQBAd8mo6wFu0EYuK2YOtgk5vF8%2BhL67xDsrjmagWxYJPhYmzzGtmv5fgpHhV90nhVPUxAEtgEyZRlNomrBy8LFkr5Z1vg%2FkJxvRRZDE58DMORCfTGwlpJFJVPRWPAuRrgxT%2FWmMtsd%2BsN3BiUPdkpdQrnmgZ94Ix1VJEtxC4NhBdHkhT4Q3oTJG%2FoKSy0904W5V11CnOpzhSBErs89DgdsWwo0G5HN0WXsdv6tYrDeQ%2FBs7RQmhhN8mTVB8Wv0B5DfThRO9go4WQ961VMy6lYUuVxIXvv%2FU%2BhuN2gR%2BBKZFNZG4%2B%2Bd6kSty4AmiY%2BtqL07Y1vMxuxCpOXGLEsoFLmyMvZt5ybLQrHXEP28m%2BUsUHkCE3atmMXofS4RK4ZvOUepfPvYQZpA5fQPIZxXF7NdOiZ7%2BAZwbvMZelyLT2uFzwPY5luZny2yCCVx5DITDw%2BJK9BjqkAbnmqP4vj0inBVTyQAMayQl%2BvUIMdNDxZ9wX6IwfKfdgra%2FgpVkGvX2b18KeX38eCAfxImXNKOigoxV5%2BpD9dy0quyaFGu33KAxab12PKgH0dj9hF77DAlRFOv33QwPuQStpAxryvDvjmEuOv1zPKbaoZk1W1NGLaZOBuIgYVHETIYl6L%2FCn0ZYRqm94lx5m3UVY4gOxYW1iD1ahww7xoeiHCcOp&X-Amz-Signature=500fce1f70918375c2a6be0c6a5291077e0867dd1e235a48d3074e451183b9e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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


