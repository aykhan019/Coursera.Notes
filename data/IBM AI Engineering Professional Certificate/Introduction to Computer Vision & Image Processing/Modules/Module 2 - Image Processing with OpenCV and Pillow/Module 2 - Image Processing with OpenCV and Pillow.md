

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MBBGZ5X%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEgiLr2Owp33kXPgQ%2BkZ7FJ7OqOaePVLuaSpad1gtZh8AiEA7EVXQTRE3W86NCr6rxI%2FqtFib5mC2NEB477S3EewF8cqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA86A5dyZFUtP5%2BZyyrcAy3TkIKKgfKJrDtswFl4EnA4xl29shOmLkYukMu950hY5%2FeeTSeS%2BRkVOtQzESmXNtPbLdVAsFZfPjOGU0dRXMWCM8wQ%2Ba%2Bk%2FshIv0BjS8waxmalM%2FKh6SvmRr%2FVV0q5t6vkIvv4xmElTayIdhapBi8GLwYFRw3y9vM7SWKoUVa5MqQc421LNX05XSh1T8IlYlkei%2BQkp5txQugT2mHAtalBN1lJqGIaO%2BCtkYJ2zf963hXgAQecCwq2rdWIZwYbLmyXvA8mvWBf4uxDWThvoQxNiV3OzlPHhUsKYSkmneEAHEVF%2Bx8S%2FqgPy2qo8ouOTX51iZZgbxCXYmTX8PqsOoQEt43x78qt224YAjdQPYilVIE7AxIszLG5Z6%2BuFu26Qd9btKjl7vXSjfbW%2BXuvyEDUe5UXvTVBHbqxGwjJ1RbltOCCmTGmwIXApWzOVk4dBVDi7hRgZzjPtfptZ8njKBe1EqqovzUmRbyXZh7IGp7t8UI6kduVX3iOxf0EzE4ibF%2BWTxawQgIi8CPA1uiezAL%2F9JsCg3Q956LQBvK7t1vX1g5R%2BGA%2Fegxb8XdTftInSH6SYz%2Fk7YCIvperXMB%2Bj6FL3GfI%2B3MJBAk46rtIaYvAZNP7TvTStfy%2Fw7pbMNiU9bwGOqUBJMUKKBeB334kxAx4%2BDBMqoFkSq6pnk8B8J9t6G%2FPmqbB6mANl%2Fy%2B8PEM8%2F8PgAm5Fbhq3rfVgkq3V4Fmm8dvbipqXwGV%2F6vtDHXafDEvn5MERtcygOQgzvFPWoKQIHwHexRzNaNQZ8rW9mv%2Fezq6qA0%2FGiGvqjCEemNetCDj7PMtU6w3TgImKdoT17IlybZbCjkZjXJxfqO5um3zLNXb60D6u2%2Fw&X-Amz-Signature=cf7bbe2430ee0be2bcf922f344f5035a4385a5abf0194db8b8ff6b3190d70cfe&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J7AOHP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDV10hG78xgNc%2Bi3BRQqBhPcXnY1dS9h8Ivz3F9XMVrQIgW5aB5a9S9PgenB%2FFADBC5GDXApsiReOetXbe3ZjQ1TQqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCPut6Sfa30SVbmtTyrcA8CiGdpm%2FIVggWweO7r05gXLjXnY5tw3RoWzMgF5Jy4nghVyAnk1b8rUPo1%2FfdV8jf20oC0s8V0WN14f3z5k5R3m0BGNW9Okx5FkoN1aZ3cPlRsAF7s4PnDRh7wNh9%2BMgX4TTEyJGKX5W4LTEgBNdfXMjB80r6XhsIzbd69LzycCrJgKSGU6ySht8buhi1%2BQJcVv%2FOXR1Vh5yTGGWqjJ0cmaTXkVgeDFooxizZqtOAUGVwxZFtBTbNp9JN23ux6rJy7QRTyBFq519xq7fw8yDSUyhYvSkRQjiSYTRWGdh9W9uTtACwR7%2BAXb0l8xv%2FVO6837qTZQlKS2nmC1iFHenUukfo8WLuEoQY7q9jUcb4FVfoA8ihgNW6PdlDCO6oygjmBmkFW1qATQPbvnWWLrlZu8%2BgnK1UsLEJY%2FMBBZEpQnLaOPVRU3jWqFs1DBxFttfY0MF9I7sqd9aPCoqVblr2FTc5nLwSytiBBZPR7Y42sBqlfucVNJh0Mlm0ekxcpRKsuZuuaDnZDRrQSW3GdaDIip3bze7kQDzdWETGoLNWeVn0myKU3SZYHObHl4IycfKKXPc%2BoJ5tG8WjIv0pZPYdTe4xWHLkcJLNdURlHHSN9wyvhvSYKMTJbvQzLBMO%2BT9bwGOqUBK12pc1%2BKGij%2F9T49qEu7rK2hUT4RWuR8OFwpnJnMI0KsJBKNYbg2IHmgR%2B8lqHlylSFFZgxmx483J5kYdazJrSllezpuwt9olrA%2FOzff%2BROX4F2VUnWDNiaz1PpcAKUcTWv5kv%2BbSGYns9R1seRnrGxym4HHaNlEAllRCuY44tnQSiymUrPZcizPeTooJY18Cv%2BCOmqrgDhZ8e8YCggvELAIezxX&X-Amz-Signature=cfecbd38442eca7006d99acd7b3cec8c3aa39123b97c44c93504055cbbb813d8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J7AOHP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDV10hG78xgNc%2Bi3BRQqBhPcXnY1dS9h8Ivz3F9XMVrQIgW5aB5a9S9PgenB%2FFADBC5GDXApsiReOetXbe3ZjQ1TQqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCPut6Sfa30SVbmtTyrcA8CiGdpm%2FIVggWweO7r05gXLjXnY5tw3RoWzMgF5Jy4nghVyAnk1b8rUPo1%2FfdV8jf20oC0s8V0WN14f3z5k5R3m0BGNW9Okx5FkoN1aZ3cPlRsAF7s4PnDRh7wNh9%2BMgX4TTEyJGKX5W4LTEgBNdfXMjB80r6XhsIzbd69LzycCrJgKSGU6ySht8buhi1%2BQJcVv%2FOXR1Vh5yTGGWqjJ0cmaTXkVgeDFooxizZqtOAUGVwxZFtBTbNp9JN23ux6rJy7QRTyBFq519xq7fw8yDSUyhYvSkRQjiSYTRWGdh9W9uTtACwR7%2BAXb0l8xv%2FVO6837qTZQlKS2nmC1iFHenUukfo8WLuEoQY7q9jUcb4FVfoA8ihgNW6PdlDCO6oygjmBmkFW1qATQPbvnWWLrlZu8%2BgnK1UsLEJY%2FMBBZEpQnLaOPVRU3jWqFs1DBxFttfY0MF9I7sqd9aPCoqVblr2FTc5nLwSytiBBZPR7Y42sBqlfucVNJh0Mlm0ekxcpRKsuZuuaDnZDRrQSW3GdaDIip3bze7kQDzdWETGoLNWeVn0myKU3SZYHObHl4IycfKKXPc%2BoJ5tG8WjIv0pZPYdTe4xWHLkcJLNdURlHHSN9wyvhvSYKMTJbvQzLBMO%2BT9bwGOqUBK12pc1%2BKGij%2F9T49qEu7rK2hUT4RWuR8OFwpnJnMI0KsJBKNYbg2IHmgR%2B8lqHlylSFFZgxmx483J5kYdazJrSllezpuwt9olrA%2FOzff%2BROX4F2VUnWDNiaz1PpcAKUcTWv5kv%2BbSGYns9R1seRnrGxym4HHaNlEAllRCuY44tnQSiymUrPZcizPeTooJY18Cv%2BCOmqrgDhZ8e8YCggvELAIezxX&X-Amz-Signature=b6d3c661ee3b5fa0431b96c345d3f86cb7643e2fd1b2928865aa89fd7569df69&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J7AOHP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDV10hG78xgNc%2Bi3BRQqBhPcXnY1dS9h8Ivz3F9XMVrQIgW5aB5a9S9PgenB%2FFADBC5GDXApsiReOetXbe3ZjQ1TQqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCPut6Sfa30SVbmtTyrcA8CiGdpm%2FIVggWweO7r05gXLjXnY5tw3RoWzMgF5Jy4nghVyAnk1b8rUPo1%2FfdV8jf20oC0s8V0WN14f3z5k5R3m0BGNW9Okx5FkoN1aZ3cPlRsAF7s4PnDRh7wNh9%2BMgX4TTEyJGKX5W4LTEgBNdfXMjB80r6XhsIzbd69LzycCrJgKSGU6ySht8buhi1%2BQJcVv%2FOXR1Vh5yTGGWqjJ0cmaTXkVgeDFooxizZqtOAUGVwxZFtBTbNp9JN23ux6rJy7QRTyBFq519xq7fw8yDSUyhYvSkRQjiSYTRWGdh9W9uTtACwR7%2BAXb0l8xv%2FVO6837qTZQlKS2nmC1iFHenUukfo8WLuEoQY7q9jUcb4FVfoA8ihgNW6PdlDCO6oygjmBmkFW1qATQPbvnWWLrlZu8%2BgnK1UsLEJY%2FMBBZEpQnLaOPVRU3jWqFs1DBxFttfY0MF9I7sqd9aPCoqVblr2FTc5nLwSytiBBZPR7Y42sBqlfucVNJh0Mlm0ekxcpRKsuZuuaDnZDRrQSW3GdaDIip3bze7kQDzdWETGoLNWeVn0myKU3SZYHObHl4IycfKKXPc%2BoJ5tG8WjIv0pZPYdTe4xWHLkcJLNdURlHHSN9wyvhvSYKMTJbvQzLBMO%2BT9bwGOqUBK12pc1%2BKGij%2F9T49qEu7rK2hUT4RWuR8OFwpnJnMI0KsJBKNYbg2IHmgR%2B8lqHlylSFFZgxmx483J5kYdazJrSllezpuwt9olrA%2FOzff%2BROX4F2VUnWDNiaz1PpcAKUcTWv5kv%2BbSGYns9R1seRnrGxym4HHaNlEAllRCuY44tnQSiymUrPZcizPeTooJY18Cv%2BCOmqrgDhZ8e8YCggvELAIezxX&X-Amz-Signature=7cef166de06dbdda72b0939ffc8145298ce8fa24d412713c702c22effb01a44e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J7AOHP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDV10hG78xgNc%2Bi3BRQqBhPcXnY1dS9h8Ivz3F9XMVrQIgW5aB5a9S9PgenB%2FFADBC5GDXApsiReOetXbe3ZjQ1TQqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCPut6Sfa30SVbmtTyrcA8CiGdpm%2FIVggWweO7r05gXLjXnY5tw3RoWzMgF5Jy4nghVyAnk1b8rUPo1%2FfdV8jf20oC0s8V0WN14f3z5k5R3m0BGNW9Okx5FkoN1aZ3cPlRsAF7s4PnDRh7wNh9%2BMgX4TTEyJGKX5W4LTEgBNdfXMjB80r6XhsIzbd69LzycCrJgKSGU6ySht8buhi1%2BQJcVv%2FOXR1Vh5yTGGWqjJ0cmaTXkVgeDFooxizZqtOAUGVwxZFtBTbNp9JN23ux6rJy7QRTyBFq519xq7fw8yDSUyhYvSkRQjiSYTRWGdh9W9uTtACwR7%2BAXb0l8xv%2FVO6837qTZQlKS2nmC1iFHenUukfo8WLuEoQY7q9jUcb4FVfoA8ihgNW6PdlDCO6oygjmBmkFW1qATQPbvnWWLrlZu8%2BgnK1UsLEJY%2FMBBZEpQnLaOPVRU3jWqFs1DBxFttfY0MF9I7sqd9aPCoqVblr2FTc5nLwSytiBBZPR7Y42sBqlfucVNJh0Mlm0ekxcpRKsuZuuaDnZDRrQSW3GdaDIip3bze7kQDzdWETGoLNWeVn0myKU3SZYHObHl4IycfKKXPc%2BoJ5tG8WjIv0pZPYdTe4xWHLkcJLNdURlHHSN9wyvhvSYKMTJbvQzLBMO%2BT9bwGOqUBK12pc1%2BKGij%2F9T49qEu7rK2hUT4RWuR8OFwpnJnMI0KsJBKNYbg2IHmgR%2B8lqHlylSFFZgxmx483J5kYdazJrSllezpuwt9olrA%2FOzff%2BROX4F2VUnWDNiaz1PpcAKUcTWv5kv%2BbSGYns9R1seRnrGxym4HHaNlEAllRCuY44tnQSiymUrPZcizPeTooJY18Cv%2BCOmqrgDhZ8e8YCggvELAIezxX&X-Amz-Signature=75bf7e08288e5460051becfd3c089b2ababc9c4b5f8c9ac74a1d02a985bcdfa5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J7AOHP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDV10hG78xgNc%2Bi3BRQqBhPcXnY1dS9h8Ivz3F9XMVrQIgW5aB5a9S9PgenB%2FFADBC5GDXApsiReOetXbe3ZjQ1TQqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCPut6Sfa30SVbmtTyrcA8CiGdpm%2FIVggWweO7r05gXLjXnY5tw3RoWzMgF5Jy4nghVyAnk1b8rUPo1%2FfdV8jf20oC0s8V0WN14f3z5k5R3m0BGNW9Okx5FkoN1aZ3cPlRsAF7s4PnDRh7wNh9%2BMgX4TTEyJGKX5W4LTEgBNdfXMjB80r6XhsIzbd69LzycCrJgKSGU6ySht8buhi1%2BQJcVv%2FOXR1Vh5yTGGWqjJ0cmaTXkVgeDFooxizZqtOAUGVwxZFtBTbNp9JN23ux6rJy7QRTyBFq519xq7fw8yDSUyhYvSkRQjiSYTRWGdh9W9uTtACwR7%2BAXb0l8xv%2FVO6837qTZQlKS2nmC1iFHenUukfo8WLuEoQY7q9jUcb4FVfoA8ihgNW6PdlDCO6oygjmBmkFW1qATQPbvnWWLrlZu8%2BgnK1UsLEJY%2FMBBZEpQnLaOPVRU3jWqFs1DBxFttfY0MF9I7sqd9aPCoqVblr2FTc5nLwSytiBBZPR7Y42sBqlfucVNJh0Mlm0ekxcpRKsuZuuaDnZDRrQSW3GdaDIip3bze7kQDzdWETGoLNWeVn0myKU3SZYHObHl4IycfKKXPc%2BoJ5tG8WjIv0pZPYdTe4xWHLkcJLNdURlHHSN9wyvhvSYKMTJbvQzLBMO%2BT9bwGOqUBK12pc1%2BKGij%2F9T49qEu7rK2hUT4RWuR8OFwpnJnMI0KsJBKNYbg2IHmgR%2B8lqHlylSFFZgxmx483J5kYdazJrSllezpuwt9olrA%2FOzff%2BROX4F2VUnWDNiaz1PpcAKUcTWv5kv%2BbSGYns9R1seRnrGxym4HHaNlEAllRCuY44tnQSiymUrPZcizPeTooJY18Cv%2BCOmqrgDhZ8e8YCggvELAIezxX&X-Amz-Signature=29077e80e04c1ef55e5643cb5fbc236556d6d88f72b3100bc92ae4b7aaa8471f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MBBGZ5X%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEgiLr2Owp33kXPgQ%2BkZ7FJ7OqOaePVLuaSpad1gtZh8AiEA7EVXQTRE3W86NCr6rxI%2FqtFib5mC2NEB477S3EewF8cqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA86A5dyZFUtP5%2BZyyrcAy3TkIKKgfKJrDtswFl4EnA4xl29shOmLkYukMu950hY5%2FeeTSeS%2BRkVOtQzESmXNtPbLdVAsFZfPjOGU0dRXMWCM8wQ%2Ba%2Bk%2FshIv0BjS8waxmalM%2FKh6SvmRr%2FVV0q5t6vkIvv4xmElTayIdhapBi8GLwYFRw3y9vM7SWKoUVa5MqQc421LNX05XSh1T8IlYlkei%2BQkp5txQugT2mHAtalBN1lJqGIaO%2BCtkYJ2zf963hXgAQecCwq2rdWIZwYbLmyXvA8mvWBf4uxDWThvoQxNiV3OzlPHhUsKYSkmneEAHEVF%2Bx8S%2FqgPy2qo8ouOTX51iZZgbxCXYmTX8PqsOoQEt43x78qt224YAjdQPYilVIE7AxIszLG5Z6%2BuFu26Qd9btKjl7vXSjfbW%2BXuvyEDUe5UXvTVBHbqxGwjJ1RbltOCCmTGmwIXApWzOVk4dBVDi7hRgZzjPtfptZ8njKBe1EqqovzUmRbyXZh7IGp7t8UI6kduVX3iOxf0EzE4ibF%2BWTxawQgIi8CPA1uiezAL%2F9JsCg3Q956LQBvK7t1vX1g5R%2BGA%2Fegxb8XdTftInSH6SYz%2Fk7YCIvperXMB%2Bj6FL3GfI%2B3MJBAk46rtIaYvAZNP7TvTStfy%2Fw7pbMNiU9bwGOqUBJMUKKBeB334kxAx4%2BDBMqoFkSq6pnk8B8J9t6G%2FPmqbB6mANl%2Fy%2B8PEM8%2F8PgAm5Fbhq3rfVgkq3V4Fmm8dvbipqXwGV%2F6vtDHXafDEvn5MERtcygOQgzvFPWoKQIHwHexRzNaNQZ8rW9mv%2Fezq6qA0%2FGiGvqjCEemNetCDj7PMtU6w3TgImKdoT17IlybZbCjkZjXJxfqO5um3zLNXb60D6u2%2Fw&X-Amz-Signature=7ec07a8e6956e576e776182454c7caf6848da1d77a026cb9a529b21bc16c3dba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MBBGZ5X%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEgiLr2Owp33kXPgQ%2BkZ7FJ7OqOaePVLuaSpad1gtZh8AiEA7EVXQTRE3W86NCr6rxI%2FqtFib5mC2NEB477S3EewF8cqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA86A5dyZFUtP5%2BZyyrcAy3TkIKKgfKJrDtswFl4EnA4xl29shOmLkYukMu950hY5%2FeeTSeS%2BRkVOtQzESmXNtPbLdVAsFZfPjOGU0dRXMWCM8wQ%2Ba%2Bk%2FshIv0BjS8waxmalM%2FKh6SvmRr%2FVV0q5t6vkIvv4xmElTayIdhapBi8GLwYFRw3y9vM7SWKoUVa5MqQc421LNX05XSh1T8IlYlkei%2BQkp5txQugT2mHAtalBN1lJqGIaO%2BCtkYJ2zf963hXgAQecCwq2rdWIZwYbLmyXvA8mvWBf4uxDWThvoQxNiV3OzlPHhUsKYSkmneEAHEVF%2Bx8S%2FqgPy2qo8ouOTX51iZZgbxCXYmTX8PqsOoQEt43x78qt224YAjdQPYilVIE7AxIszLG5Z6%2BuFu26Qd9btKjl7vXSjfbW%2BXuvyEDUe5UXvTVBHbqxGwjJ1RbltOCCmTGmwIXApWzOVk4dBVDi7hRgZzjPtfptZ8njKBe1EqqovzUmRbyXZh7IGp7t8UI6kduVX3iOxf0EzE4ibF%2BWTxawQgIi8CPA1uiezAL%2F9JsCg3Q956LQBvK7t1vX1g5R%2BGA%2Fegxb8XdTftInSH6SYz%2Fk7YCIvperXMB%2Bj6FL3GfI%2B3MJBAk46rtIaYvAZNP7TvTStfy%2Fw7pbMNiU9bwGOqUBJMUKKBeB334kxAx4%2BDBMqoFkSq6pnk8B8J9t6G%2FPmqbB6mANl%2Fy%2B8PEM8%2F8PgAm5Fbhq3rfVgkq3V4Fmm8dvbipqXwGV%2F6vtDHXafDEvn5MERtcygOQgzvFPWoKQIHwHexRzNaNQZ8rW9mv%2Fezq6qA0%2FGiGvqjCEemNetCDj7PMtU6w3TgImKdoT17IlybZbCjkZjXJxfqO5um3zLNXb60D6u2%2Fw&X-Amz-Signature=d2ef9430f03895898318bfe89825abd3b950dcf840dd1d85224f02f40461944b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MBBGZ5X%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEgiLr2Owp33kXPgQ%2BkZ7FJ7OqOaePVLuaSpad1gtZh8AiEA7EVXQTRE3W86NCr6rxI%2FqtFib5mC2NEB477S3EewF8cqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA86A5dyZFUtP5%2BZyyrcAy3TkIKKgfKJrDtswFl4EnA4xl29shOmLkYukMu950hY5%2FeeTSeS%2BRkVOtQzESmXNtPbLdVAsFZfPjOGU0dRXMWCM8wQ%2Ba%2Bk%2FshIv0BjS8waxmalM%2FKh6SvmRr%2FVV0q5t6vkIvv4xmElTayIdhapBi8GLwYFRw3y9vM7SWKoUVa5MqQc421LNX05XSh1T8IlYlkei%2BQkp5txQugT2mHAtalBN1lJqGIaO%2BCtkYJ2zf963hXgAQecCwq2rdWIZwYbLmyXvA8mvWBf4uxDWThvoQxNiV3OzlPHhUsKYSkmneEAHEVF%2Bx8S%2FqgPy2qo8ouOTX51iZZgbxCXYmTX8PqsOoQEt43x78qt224YAjdQPYilVIE7AxIszLG5Z6%2BuFu26Qd9btKjl7vXSjfbW%2BXuvyEDUe5UXvTVBHbqxGwjJ1RbltOCCmTGmwIXApWzOVk4dBVDi7hRgZzjPtfptZ8njKBe1EqqovzUmRbyXZh7IGp7t8UI6kduVX3iOxf0EzE4ibF%2BWTxawQgIi8CPA1uiezAL%2F9JsCg3Q956LQBvK7t1vX1g5R%2BGA%2Fegxb8XdTftInSH6SYz%2Fk7YCIvperXMB%2Bj6FL3GfI%2B3MJBAk46rtIaYvAZNP7TvTStfy%2Fw7pbMNiU9bwGOqUBJMUKKBeB334kxAx4%2BDBMqoFkSq6pnk8B8J9t6G%2FPmqbB6mANl%2Fy%2B8PEM8%2F8PgAm5Fbhq3rfVgkq3V4Fmm8dvbipqXwGV%2F6vtDHXafDEvn5MERtcygOQgzvFPWoKQIHwHexRzNaNQZ8rW9mv%2Fezq6qA0%2FGiGvqjCEemNetCDj7PMtU6w3TgImKdoT17IlybZbCjkZjXJxfqO5um3zLNXb60D6u2%2Fw&X-Amz-Signature=4ba3ca2eee523761609167a868aab6973dcf6a89265f696e2214248b3dbd4f2a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MBBGZ5X%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEgiLr2Owp33kXPgQ%2BkZ7FJ7OqOaePVLuaSpad1gtZh8AiEA7EVXQTRE3W86NCr6rxI%2FqtFib5mC2NEB477S3EewF8cqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA86A5dyZFUtP5%2BZyyrcAy3TkIKKgfKJrDtswFl4EnA4xl29shOmLkYukMu950hY5%2FeeTSeS%2BRkVOtQzESmXNtPbLdVAsFZfPjOGU0dRXMWCM8wQ%2Ba%2Bk%2FshIv0BjS8waxmalM%2FKh6SvmRr%2FVV0q5t6vkIvv4xmElTayIdhapBi8GLwYFRw3y9vM7SWKoUVa5MqQc421LNX05XSh1T8IlYlkei%2BQkp5txQugT2mHAtalBN1lJqGIaO%2BCtkYJ2zf963hXgAQecCwq2rdWIZwYbLmyXvA8mvWBf4uxDWThvoQxNiV3OzlPHhUsKYSkmneEAHEVF%2Bx8S%2FqgPy2qo8ouOTX51iZZgbxCXYmTX8PqsOoQEt43x78qt224YAjdQPYilVIE7AxIszLG5Z6%2BuFu26Qd9btKjl7vXSjfbW%2BXuvyEDUe5UXvTVBHbqxGwjJ1RbltOCCmTGmwIXApWzOVk4dBVDi7hRgZzjPtfptZ8njKBe1EqqovzUmRbyXZh7IGp7t8UI6kduVX3iOxf0EzE4ibF%2BWTxawQgIi8CPA1uiezAL%2F9JsCg3Q956LQBvK7t1vX1g5R%2BGA%2Fegxb8XdTftInSH6SYz%2Fk7YCIvperXMB%2Bj6FL3GfI%2B3MJBAk46rtIaYvAZNP7TvTStfy%2Fw7pbMNiU9bwGOqUBJMUKKBeB334kxAx4%2BDBMqoFkSq6pnk8B8J9t6G%2FPmqbB6mANl%2Fy%2B8PEM8%2F8PgAm5Fbhq3rfVgkq3V4Fmm8dvbipqXwGV%2F6vtDHXafDEvn5MERtcygOQgzvFPWoKQIHwHexRzNaNQZ8rW9mv%2Fezq6qA0%2FGiGvqjCEemNetCDj7PMtU6w3TgImKdoT17IlybZbCjkZjXJxfqO5um3zLNXb60D6u2%2Fw&X-Amz-Signature=8f0cd9d053436ce053a08f11d0af5e616acc1268dc5037f7aa171fa8305421da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MBBGZ5X%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEgiLr2Owp33kXPgQ%2BkZ7FJ7OqOaePVLuaSpad1gtZh8AiEA7EVXQTRE3W86NCr6rxI%2FqtFib5mC2NEB477S3EewF8cqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA86A5dyZFUtP5%2BZyyrcAy3TkIKKgfKJrDtswFl4EnA4xl29shOmLkYukMu950hY5%2FeeTSeS%2BRkVOtQzESmXNtPbLdVAsFZfPjOGU0dRXMWCM8wQ%2Ba%2Bk%2FshIv0BjS8waxmalM%2FKh6SvmRr%2FVV0q5t6vkIvv4xmElTayIdhapBi8GLwYFRw3y9vM7SWKoUVa5MqQc421LNX05XSh1T8IlYlkei%2BQkp5txQugT2mHAtalBN1lJqGIaO%2BCtkYJ2zf963hXgAQecCwq2rdWIZwYbLmyXvA8mvWBf4uxDWThvoQxNiV3OzlPHhUsKYSkmneEAHEVF%2Bx8S%2FqgPy2qo8ouOTX51iZZgbxCXYmTX8PqsOoQEt43x78qt224YAjdQPYilVIE7AxIszLG5Z6%2BuFu26Qd9btKjl7vXSjfbW%2BXuvyEDUe5UXvTVBHbqxGwjJ1RbltOCCmTGmwIXApWzOVk4dBVDi7hRgZzjPtfptZ8njKBe1EqqovzUmRbyXZh7IGp7t8UI6kduVX3iOxf0EzE4ibF%2BWTxawQgIi8CPA1uiezAL%2F9JsCg3Q956LQBvK7t1vX1g5R%2BGA%2Fegxb8XdTftInSH6SYz%2Fk7YCIvperXMB%2Bj6FL3GfI%2B3MJBAk46rtIaYvAZNP7TvTStfy%2Fw7pbMNiU9bwGOqUBJMUKKBeB334kxAx4%2BDBMqoFkSq6pnk8B8J9t6G%2FPmqbB6mANl%2Fy%2B8PEM8%2F8PgAm5Fbhq3rfVgkq3V4Fmm8dvbipqXwGV%2F6vtDHXafDEvn5MERtcygOQgzvFPWoKQIHwHexRzNaNQZ8rW9mv%2Fezq6qA0%2FGiGvqjCEemNetCDj7PMtU6w3TgImKdoT17IlybZbCjkZjXJxfqO5um3zLNXb60D6u2%2Fw&X-Amz-Signature=08366e28998c9e64098dbf94360d067c4e4fd868b2ad563a5c510610a3457018&X-Amz-SignedHeaders=host&x-id=GetObject)
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


