

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJZGJ4J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEeBz5aUAeOSltbF8nfo%2BIJqJsuK1ZFkxPZo%2FegHfnbaAiBiNXUhKX2271hqdRztRPpte3X%2BX0SNUZvoK3NV6XY66ir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMFhCVxdGLCnWEzkQ1KtwDWh9LPn2HXIcoCBMB7O26Hvlce%2F7i8olfy6k%2FtDzoVRS1Bb2XYvZxT9GAQog0b81NMD8HEOaLtu3ttTRfOMxDiL%2BTqjJr9qQmaYlTFlim7T2VCHS5h%2FoRDMx01jLyKdL%2F4a5ltuNrAN8ccZT3mjDs9BbQxSVEdHxy48Ir%2BO%2F%2F8ySoTYkbt6B0uUGAuYeBsqAq0n%2BTrmZzwDsC3GduWnLdLfMkluyxaV0y6Mqs8A0XdrZal%2FrElGYvxchCqWky9PSTR5xaflwevQVc8s6CNtMlKmlOxKT1X69o4qJoF6MWbd%2FvYuOVHmF2%2BCufrw9PLmIZQNids4IAlWlvKLEEycwelxZrnw3CtbSoqsQwbtXag8echRTWchi6xqvBaDo7Fs9T%2F4kPWJS9BX93ei0uYpdnBIkny%2FRYO5lMcQjnkfwkjswhTEMP58R%2F%2FHlSKW3yc6PtMcq12Rtg%2FcPCdkY3JsVV%2B9DZXtbgj0xcNWo3wnRdCO4JpJcZlMqW8F68LdxTSHz2263xjRHGoWGpnPhFsyRF73rhr1pUGqYMOxUmlVZrpk5VXM41OyWCjM4lv6WZcOTy%2FnD%2BhB9oVGojcS10eK6txfe8H3vmVjtkAKMPWH5Cm4kcjKxfzQWQyJwMpVgw%2B4qNvQY6pgFWvaRmI09zVG50X3%2BDsmVwwGxoY17KmdMNTFDGLyoi6ULCkvokvIPyiPolF6p9OW%2BgUK%2Bmd4JfWor%2BWD%2FSFamDYCTRhdsyVwv0K7nyhigGwNpT13ovhr1bbJ86%2F9ZzMgaoKuyJRAfE%2BBQGL03KiaJiezY2ZLaqum5oNUg8c6ED397Tpuy%2BEFNFnGaERHF1uUEW0SA9WhFQ6pggAbFFXEL2%2FJMuWtRJ&X-Amz-Signature=daec35bd1151b61158386707b82b7322165ba30910268e5e70c97ec9c381d857&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD6HIACI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCDNfYy1leNB2EZ9mDWAOWG%2F4PlbFAv1%2Fj2nxOgBhBXdgIhAIwNejBJmOdQ06%2FDOHZZJZLvN3RC%2Brr%2BrZF%2BKOfCK5eEKv8DCEQQABoMNjM3NDIzMTgzODA1IgzsUS%2FlFyC3KJS5EMYq3AN2ehv7Xo16SETji77p9QtbAcqKbtgtdzEBiM1rhMoAK%2F515mUF%2BzsFzO0gmDLC3125cjeXVmm5MY9Vk2v6y2cbkVyV6vGV6u0lGi7bT73Fcqs6XR%2FfuYgXAsHXqirHkMvTy55DUyAUW7muGrdF6Q7Og4zORzkUlR6iZArNrFo4rNtZ1y3NcrKhO8IibDWuyOmt5zmex%2Bciq9MwwxXwRAYjGTHUT6lYUfhnwFu5ZBhnIHPOOiQuh0J2aMtMNwwKj3sinobjDDf41gu690PB2ORxzXiv6XKHKnt6vaas%2BZ2Ph%2F8F5NrDuR7fYhsgd%2BNg0hujO4m%2B2KlrTUQi1WMHBhy93bnwgfXAT4kKRVf3Iu%2BzVDa7pXaCug0CJ5sv1uIb9KS3Bp6aGGc8G668r5FMz3J1x%2B7kMkSL7ydtmrb3DoqKmdsLN5QMrby3a7UA80DBa7ckAJGckBZjf7tv190yDJvoWFiZs9Tkzno2NfwYx2ov%2F5IapVFSE8HWzfPXBuoAzToGh6r820g%2Fjp3Z%2BpMsqeyL6%2FiKiqIKPNM6yf8uiHug7y0tiOdJKlWzX%2BDQQCOHq3oArde4rQSuxm%2B1Bd5gDA3zj6GgNjalf0VJE6%2Bif0%2B96f2HIEOCeHGfiHXNWjCsi429BjqkARNp80rmO%2FhP%2F27i9yaA6a6lGSITzraIGZqjK5l07UgvyfCmDJ2dJli1VPLnS9bA8cYmJUrAh%2BpleKXx0W4TaTxeaBoV1Kixb8Ue4ryphCAZ%2BB9hn%2Bsak125ChJwy1pgZABkBDB6a%2B0rhOHXz0O0I%2BwLZ93vSdmaUJxLU111YY9hkin2LaIkxWWkuCojOkKfc8p9KH6oXDAx4W9zqyevnS26L17F&X-Amz-Signature=1200557ab30fa7aa8a3d13fa5d779741a88e75eef75302b205a2f10f25576dd1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD6HIACI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCDNfYy1leNB2EZ9mDWAOWG%2F4PlbFAv1%2Fj2nxOgBhBXdgIhAIwNejBJmOdQ06%2FDOHZZJZLvN3RC%2Brr%2BrZF%2BKOfCK5eEKv8DCEQQABoMNjM3NDIzMTgzODA1IgzsUS%2FlFyC3KJS5EMYq3AN2ehv7Xo16SETji77p9QtbAcqKbtgtdzEBiM1rhMoAK%2F515mUF%2BzsFzO0gmDLC3125cjeXVmm5MY9Vk2v6y2cbkVyV6vGV6u0lGi7bT73Fcqs6XR%2FfuYgXAsHXqirHkMvTy55DUyAUW7muGrdF6Q7Og4zORzkUlR6iZArNrFo4rNtZ1y3NcrKhO8IibDWuyOmt5zmex%2Bciq9MwwxXwRAYjGTHUT6lYUfhnwFu5ZBhnIHPOOiQuh0J2aMtMNwwKj3sinobjDDf41gu690PB2ORxzXiv6XKHKnt6vaas%2BZ2Ph%2F8F5NrDuR7fYhsgd%2BNg0hujO4m%2B2KlrTUQi1WMHBhy93bnwgfXAT4kKRVf3Iu%2BzVDa7pXaCug0CJ5sv1uIb9KS3Bp6aGGc8G668r5FMz3J1x%2B7kMkSL7ydtmrb3DoqKmdsLN5QMrby3a7UA80DBa7ckAJGckBZjf7tv190yDJvoWFiZs9Tkzno2NfwYx2ov%2F5IapVFSE8HWzfPXBuoAzToGh6r820g%2Fjp3Z%2BpMsqeyL6%2FiKiqIKPNM6yf8uiHug7y0tiOdJKlWzX%2BDQQCOHq3oArde4rQSuxm%2B1Bd5gDA3zj6GgNjalf0VJE6%2Bif0%2B96f2HIEOCeHGfiHXNWjCsi429BjqkARNp80rmO%2FhP%2F27i9yaA6a6lGSITzraIGZqjK5l07UgvyfCmDJ2dJli1VPLnS9bA8cYmJUrAh%2BpleKXx0W4TaTxeaBoV1Kixb8Ue4ryphCAZ%2BB9hn%2Bsak125ChJwy1pgZABkBDB6a%2B0rhOHXz0O0I%2BwLZ93vSdmaUJxLU111YY9hkin2LaIkxWWkuCojOkKfc8p9KH6oXDAx4W9zqyevnS26L17F&X-Amz-Signature=c4d7459ed6f8b90947d7ebc4ef127e46f08e77902816d2eda0c805451250274b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD6HIACI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCDNfYy1leNB2EZ9mDWAOWG%2F4PlbFAv1%2Fj2nxOgBhBXdgIhAIwNejBJmOdQ06%2FDOHZZJZLvN3RC%2Brr%2BrZF%2BKOfCK5eEKv8DCEQQABoMNjM3NDIzMTgzODA1IgzsUS%2FlFyC3KJS5EMYq3AN2ehv7Xo16SETji77p9QtbAcqKbtgtdzEBiM1rhMoAK%2F515mUF%2BzsFzO0gmDLC3125cjeXVmm5MY9Vk2v6y2cbkVyV6vGV6u0lGi7bT73Fcqs6XR%2FfuYgXAsHXqirHkMvTy55DUyAUW7muGrdF6Q7Og4zORzkUlR6iZArNrFo4rNtZ1y3NcrKhO8IibDWuyOmt5zmex%2Bciq9MwwxXwRAYjGTHUT6lYUfhnwFu5ZBhnIHPOOiQuh0J2aMtMNwwKj3sinobjDDf41gu690PB2ORxzXiv6XKHKnt6vaas%2BZ2Ph%2F8F5NrDuR7fYhsgd%2BNg0hujO4m%2B2KlrTUQi1WMHBhy93bnwgfXAT4kKRVf3Iu%2BzVDa7pXaCug0CJ5sv1uIb9KS3Bp6aGGc8G668r5FMz3J1x%2B7kMkSL7ydtmrb3DoqKmdsLN5QMrby3a7UA80DBa7ckAJGckBZjf7tv190yDJvoWFiZs9Tkzno2NfwYx2ov%2F5IapVFSE8HWzfPXBuoAzToGh6r820g%2Fjp3Z%2BpMsqeyL6%2FiKiqIKPNM6yf8uiHug7y0tiOdJKlWzX%2BDQQCOHq3oArde4rQSuxm%2B1Bd5gDA3zj6GgNjalf0VJE6%2Bif0%2B96f2HIEOCeHGfiHXNWjCsi429BjqkARNp80rmO%2FhP%2F27i9yaA6a6lGSITzraIGZqjK5l07UgvyfCmDJ2dJli1VPLnS9bA8cYmJUrAh%2BpleKXx0W4TaTxeaBoV1Kixb8Ue4ryphCAZ%2BB9hn%2Bsak125ChJwy1pgZABkBDB6a%2B0rhOHXz0O0I%2BwLZ93vSdmaUJxLU111YY9hkin2LaIkxWWkuCojOkKfc8p9KH6oXDAx4W9zqyevnS26L17F&X-Amz-Signature=e67da9049884fc4e957dac3bcf70e419b68d1da69244edf839d035ce941aa363&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD6HIACI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCDNfYy1leNB2EZ9mDWAOWG%2F4PlbFAv1%2Fj2nxOgBhBXdgIhAIwNejBJmOdQ06%2FDOHZZJZLvN3RC%2Brr%2BrZF%2BKOfCK5eEKv8DCEQQABoMNjM3NDIzMTgzODA1IgzsUS%2FlFyC3KJS5EMYq3AN2ehv7Xo16SETji77p9QtbAcqKbtgtdzEBiM1rhMoAK%2F515mUF%2BzsFzO0gmDLC3125cjeXVmm5MY9Vk2v6y2cbkVyV6vGV6u0lGi7bT73Fcqs6XR%2FfuYgXAsHXqirHkMvTy55DUyAUW7muGrdF6Q7Og4zORzkUlR6iZArNrFo4rNtZ1y3NcrKhO8IibDWuyOmt5zmex%2Bciq9MwwxXwRAYjGTHUT6lYUfhnwFu5ZBhnIHPOOiQuh0J2aMtMNwwKj3sinobjDDf41gu690PB2ORxzXiv6XKHKnt6vaas%2BZ2Ph%2F8F5NrDuR7fYhsgd%2BNg0hujO4m%2B2KlrTUQi1WMHBhy93bnwgfXAT4kKRVf3Iu%2BzVDa7pXaCug0CJ5sv1uIb9KS3Bp6aGGc8G668r5FMz3J1x%2B7kMkSL7ydtmrb3DoqKmdsLN5QMrby3a7UA80DBa7ckAJGckBZjf7tv190yDJvoWFiZs9Tkzno2NfwYx2ov%2F5IapVFSE8HWzfPXBuoAzToGh6r820g%2Fjp3Z%2BpMsqeyL6%2FiKiqIKPNM6yf8uiHug7y0tiOdJKlWzX%2BDQQCOHq3oArde4rQSuxm%2B1Bd5gDA3zj6GgNjalf0VJE6%2Bif0%2B96f2HIEOCeHGfiHXNWjCsi429BjqkARNp80rmO%2FhP%2F27i9yaA6a6lGSITzraIGZqjK5l07UgvyfCmDJ2dJli1VPLnS9bA8cYmJUrAh%2BpleKXx0W4TaTxeaBoV1Kixb8Ue4ryphCAZ%2BB9hn%2Bsak125ChJwy1pgZABkBDB6a%2B0rhOHXz0O0I%2BwLZ93vSdmaUJxLU111YY9hkin2LaIkxWWkuCojOkKfc8p9KH6oXDAx4W9zqyevnS26L17F&X-Amz-Signature=78046b1c6397b1311d03b2b723d260c88cb2d8b64ba0fdc175575fca2799099f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD6HIACI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCDNfYy1leNB2EZ9mDWAOWG%2F4PlbFAv1%2Fj2nxOgBhBXdgIhAIwNejBJmOdQ06%2FDOHZZJZLvN3RC%2Brr%2BrZF%2BKOfCK5eEKv8DCEQQABoMNjM3NDIzMTgzODA1IgzsUS%2FlFyC3KJS5EMYq3AN2ehv7Xo16SETji77p9QtbAcqKbtgtdzEBiM1rhMoAK%2F515mUF%2BzsFzO0gmDLC3125cjeXVmm5MY9Vk2v6y2cbkVyV6vGV6u0lGi7bT73Fcqs6XR%2FfuYgXAsHXqirHkMvTy55DUyAUW7muGrdF6Q7Og4zORzkUlR6iZArNrFo4rNtZ1y3NcrKhO8IibDWuyOmt5zmex%2Bciq9MwwxXwRAYjGTHUT6lYUfhnwFu5ZBhnIHPOOiQuh0J2aMtMNwwKj3sinobjDDf41gu690PB2ORxzXiv6XKHKnt6vaas%2BZ2Ph%2F8F5NrDuR7fYhsgd%2BNg0hujO4m%2B2KlrTUQi1WMHBhy93bnwgfXAT4kKRVf3Iu%2BzVDa7pXaCug0CJ5sv1uIb9KS3Bp6aGGc8G668r5FMz3J1x%2B7kMkSL7ydtmrb3DoqKmdsLN5QMrby3a7UA80DBa7ckAJGckBZjf7tv190yDJvoWFiZs9Tkzno2NfwYx2ov%2F5IapVFSE8HWzfPXBuoAzToGh6r820g%2Fjp3Z%2BpMsqeyL6%2FiKiqIKPNM6yf8uiHug7y0tiOdJKlWzX%2BDQQCOHq3oArde4rQSuxm%2B1Bd5gDA3zj6GgNjalf0VJE6%2Bif0%2B96f2HIEOCeHGfiHXNWjCsi429BjqkARNp80rmO%2FhP%2F27i9yaA6a6lGSITzraIGZqjK5l07UgvyfCmDJ2dJli1VPLnS9bA8cYmJUrAh%2BpleKXx0W4TaTxeaBoV1Kixb8Ue4ryphCAZ%2BB9hn%2Bsak125ChJwy1pgZABkBDB6a%2B0rhOHXz0O0I%2BwLZ93vSdmaUJxLU111YY9hkin2LaIkxWWkuCojOkKfc8p9KH6oXDAx4W9zqyevnS26L17F&X-Amz-Signature=58dd4a2d4efa0449da477106f275af66e4fc3aa84c7459dbd86125b5b146b758&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJZGJ4J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEeBz5aUAeOSltbF8nfo%2BIJqJsuK1ZFkxPZo%2FegHfnbaAiBiNXUhKX2271hqdRztRPpte3X%2BX0SNUZvoK3NV6XY66ir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMFhCVxdGLCnWEzkQ1KtwDWh9LPn2HXIcoCBMB7O26Hvlce%2F7i8olfy6k%2FtDzoVRS1Bb2XYvZxT9GAQog0b81NMD8HEOaLtu3ttTRfOMxDiL%2BTqjJr9qQmaYlTFlim7T2VCHS5h%2FoRDMx01jLyKdL%2F4a5ltuNrAN8ccZT3mjDs9BbQxSVEdHxy48Ir%2BO%2F%2F8ySoTYkbt6B0uUGAuYeBsqAq0n%2BTrmZzwDsC3GduWnLdLfMkluyxaV0y6Mqs8A0XdrZal%2FrElGYvxchCqWky9PSTR5xaflwevQVc8s6CNtMlKmlOxKT1X69o4qJoF6MWbd%2FvYuOVHmF2%2BCufrw9PLmIZQNids4IAlWlvKLEEycwelxZrnw3CtbSoqsQwbtXag8echRTWchi6xqvBaDo7Fs9T%2F4kPWJS9BX93ei0uYpdnBIkny%2FRYO5lMcQjnkfwkjswhTEMP58R%2F%2FHlSKW3yc6PtMcq12Rtg%2FcPCdkY3JsVV%2B9DZXtbgj0xcNWo3wnRdCO4JpJcZlMqW8F68LdxTSHz2263xjRHGoWGpnPhFsyRF73rhr1pUGqYMOxUmlVZrpk5VXM41OyWCjM4lv6WZcOTy%2FnD%2BhB9oVGojcS10eK6txfe8H3vmVjtkAKMPWH5Cm4kcjKxfzQWQyJwMpVgw%2B4qNvQY6pgFWvaRmI09zVG50X3%2BDsmVwwGxoY17KmdMNTFDGLyoi6ULCkvokvIPyiPolF6p9OW%2BgUK%2Bmd4JfWor%2BWD%2FSFamDYCTRhdsyVwv0K7nyhigGwNpT13ovhr1bbJ86%2F9ZzMgaoKuyJRAfE%2BBQGL03KiaJiezY2ZLaqum5oNUg8c6ED397Tpuy%2BEFNFnGaERHF1uUEW0SA9WhFQ6pggAbFFXEL2%2FJMuWtRJ&X-Amz-Signature=2d52661ce20c03f8cfef64df147242d01baaa01b7db17ec8f321838382ca413e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJZGJ4J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEeBz5aUAeOSltbF8nfo%2BIJqJsuK1ZFkxPZo%2FegHfnbaAiBiNXUhKX2271hqdRztRPpte3X%2BX0SNUZvoK3NV6XY66ir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMFhCVxdGLCnWEzkQ1KtwDWh9LPn2HXIcoCBMB7O26Hvlce%2F7i8olfy6k%2FtDzoVRS1Bb2XYvZxT9GAQog0b81NMD8HEOaLtu3ttTRfOMxDiL%2BTqjJr9qQmaYlTFlim7T2VCHS5h%2FoRDMx01jLyKdL%2F4a5ltuNrAN8ccZT3mjDs9BbQxSVEdHxy48Ir%2BO%2F%2F8ySoTYkbt6B0uUGAuYeBsqAq0n%2BTrmZzwDsC3GduWnLdLfMkluyxaV0y6Mqs8A0XdrZal%2FrElGYvxchCqWky9PSTR5xaflwevQVc8s6CNtMlKmlOxKT1X69o4qJoF6MWbd%2FvYuOVHmF2%2BCufrw9PLmIZQNids4IAlWlvKLEEycwelxZrnw3CtbSoqsQwbtXag8echRTWchi6xqvBaDo7Fs9T%2F4kPWJS9BX93ei0uYpdnBIkny%2FRYO5lMcQjnkfwkjswhTEMP58R%2F%2FHlSKW3yc6PtMcq12Rtg%2FcPCdkY3JsVV%2B9DZXtbgj0xcNWo3wnRdCO4JpJcZlMqW8F68LdxTSHz2263xjRHGoWGpnPhFsyRF73rhr1pUGqYMOxUmlVZrpk5VXM41OyWCjM4lv6WZcOTy%2FnD%2BhB9oVGojcS10eK6txfe8H3vmVjtkAKMPWH5Cm4kcjKxfzQWQyJwMpVgw%2B4qNvQY6pgFWvaRmI09zVG50X3%2BDsmVwwGxoY17KmdMNTFDGLyoi6ULCkvokvIPyiPolF6p9OW%2BgUK%2Bmd4JfWor%2BWD%2FSFamDYCTRhdsyVwv0K7nyhigGwNpT13ovhr1bbJ86%2F9ZzMgaoKuyJRAfE%2BBQGL03KiaJiezY2ZLaqum5oNUg8c6ED397Tpuy%2BEFNFnGaERHF1uUEW0SA9WhFQ6pggAbFFXEL2%2FJMuWtRJ&X-Amz-Signature=94847fcea1f75786394a055b1d57d560fe94b0f963856a8c05493545fc162e84&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJZGJ4J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEeBz5aUAeOSltbF8nfo%2BIJqJsuK1ZFkxPZo%2FegHfnbaAiBiNXUhKX2271hqdRztRPpte3X%2BX0SNUZvoK3NV6XY66ir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMFhCVxdGLCnWEzkQ1KtwDWh9LPn2HXIcoCBMB7O26Hvlce%2F7i8olfy6k%2FtDzoVRS1Bb2XYvZxT9GAQog0b81NMD8HEOaLtu3ttTRfOMxDiL%2BTqjJr9qQmaYlTFlim7T2VCHS5h%2FoRDMx01jLyKdL%2F4a5ltuNrAN8ccZT3mjDs9BbQxSVEdHxy48Ir%2BO%2F%2F8ySoTYkbt6B0uUGAuYeBsqAq0n%2BTrmZzwDsC3GduWnLdLfMkluyxaV0y6Mqs8A0XdrZal%2FrElGYvxchCqWky9PSTR5xaflwevQVc8s6CNtMlKmlOxKT1X69o4qJoF6MWbd%2FvYuOVHmF2%2BCufrw9PLmIZQNids4IAlWlvKLEEycwelxZrnw3CtbSoqsQwbtXag8echRTWchi6xqvBaDo7Fs9T%2F4kPWJS9BX93ei0uYpdnBIkny%2FRYO5lMcQjnkfwkjswhTEMP58R%2F%2FHlSKW3yc6PtMcq12Rtg%2FcPCdkY3JsVV%2B9DZXtbgj0xcNWo3wnRdCO4JpJcZlMqW8F68LdxTSHz2263xjRHGoWGpnPhFsyRF73rhr1pUGqYMOxUmlVZrpk5VXM41OyWCjM4lv6WZcOTy%2FnD%2BhB9oVGojcS10eK6txfe8H3vmVjtkAKMPWH5Cm4kcjKxfzQWQyJwMpVgw%2B4qNvQY6pgFWvaRmI09zVG50X3%2BDsmVwwGxoY17KmdMNTFDGLyoi6ULCkvokvIPyiPolF6p9OW%2BgUK%2Bmd4JfWor%2BWD%2FSFamDYCTRhdsyVwv0K7nyhigGwNpT13ovhr1bbJ86%2F9ZzMgaoKuyJRAfE%2BBQGL03KiaJiezY2ZLaqum5oNUg8c6ED397Tpuy%2BEFNFnGaERHF1uUEW0SA9WhFQ6pggAbFFXEL2%2FJMuWtRJ&X-Amz-Signature=1e573384d59d83f286530c0b1e413d94f5bb24b367b88b5fafd71ffd2faaf095&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJZGJ4J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEeBz5aUAeOSltbF8nfo%2BIJqJsuK1ZFkxPZo%2FegHfnbaAiBiNXUhKX2271hqdRztRPpte3X%2BX0SNUZvoK3NV6XY66ir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMFhCVxdGLCnWEzkQ1KtwDWh9LPn2HXIcoCBMB7O26Hvlce%2F7i8olfy6k%2FtDzoVRS1Bb2XYvZxT9GAQog0b81NMD8HEOaLtu3ttTRfOMxDiL%2BTqjJr9qQmaYlTFlim7T2VCHS5h%2FoRDMx01jLyKdL%2F4a5ltuNrAN8ccZT3mjDs9BbQxSVEdHxy48Ir%2BO%2F%2F8ySoTYkbt6B0uUGAuYeBsqAq0n%2BTrmZzwDsC3GduWnLdLfMkluyxaV0y6Mqs8A0XdrZal%2FrElGYvxchCqWky9PSTR5xaflwevQVc8s6CNtMlKmlOxKT1X69o4qJoF6MWbd%2FvYuOVHmF2%2BCufrw9PLmIZQNids4IAlWlvKLEEycwelxZrnw3CtbSoqsQwbtXag8echRTWchi6xqvBaDo7Fs9T%2F4kPWJS9BX93ei0uYpdnBIkny%2FRYO5lMcQjnkfwkjswhTEMP58R%2F%2FHlSKW3yc6PtMcq12Rtg%2FcPCdkY3JsVV%2B9DZXtbgj0xcNWo3wnRdCO4JpJcZlMqW8F68LdxTSHz2263xjRHGoWGpnPhFsyRF73rhr1pUGqYMOxUmlVZrpk5VXM41OyWCjM4lv6WZcOTy%2FnD%2BhB9oVGojcS10eK6txfe8H3vmVjtkAKMPWH5Cm4kcjKxfzQWQyJwMpVgw%2B4qNvQY6pgFWvaRmI09zVG50X3%2BDsmVwwGxoY17KmdMNTFDGLyoi6ULCkvokvIPyiPolF6p9OW%2BgUK%2Bmd4JfWor%2BWD%2FSFamDYCTRhdsyVwv0K7nyhigGwNpT13ovhr1bbJ86%2F9ZzMgaoKuyJRAfE%2BBQGL03KiaJiezY2ZLaqum5oNUg8c6ED397Tpuy%2BEFNFnGaERHF1uUEW0SA9WhFQ6pggAbFFXEL2%2FJMuWtRJ&X-Amz-Signature=47e7297cb20c9b15a457d3ecc6f69ab0894f0091c3dc31bda29bd443f678ce27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QJZGJ4J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEeBz5aUAeOSltbF8nfo%2BIJqJsuK1ZFkxPZo%2FegHfnbaAiBiNXUhKX2271hqdRztRPpte3X%2BX0SNUZvoK3NV6XY66ir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMFhCVxdGLCnWEzkQ1KtwDWh9LPn2HXIcoCBMB7O26Hvlce%2F7i8olfy6k%2FtDzoVRS1Bb2XYvZxT9GAQog0b81NMD8HEOaLtu3ttTRfOMxDiL%2BTqjJr9qQmaYlTFlim7T2VCHS5h%2FoRDMx01jLyKdL%2F4a5ltuNrAN8ccZT3mjDs9BbQxSVEdHxy48Ir%2BO%2F%2F8ySoTYkbt6B0uUGAuYeBsqAq0n%2BTrmZzwDsC3GduWnLdLfMkluyxaV0y6Mqs8A0XdrZal%2FrElGYvxchCqWky9PSTR5xaflwevQVc8s6CNtMlKmlOxKT1X69o4qJoF6MWbd%2FvYuOVHmF2%2BCufrw9PLmIZQNids4IAlWlvKLEEycwelxZrnw3CtbSoqsQwbtXag8echRTWchi6xqvBaDo7Fs9T%2F4kPWJS9BX93ei0uYpdnBIkny%2FRYO5lMcQjnkfwkjswhTEMP58R%2F%2FHlSKW3yc6PtMcq12Rtg%2FcPCdkY3JsVV%2B9DZXtbgj0xcNWo3wnRdCO4JpJcZlMqW8F68LdxTSHz2263xjRHGoWGpnPhFsyRF73rhr1pUGqYMOxUmlVZrpk5VXM41OyWCjM4lv6WZcOTy%2FnD%2BhB9oVGojcS10eK6txfe8H3vmVjtkAKMPWH5Cm4kcjKxfzQWQyJwMpVgw%2B4qNvQY6pgFWvaRmI09zVG50X3%2BDsmVwwGxoY17KmdMNTFDGLyoi6ULCkvokvIPyiPolF6p9OW%2BgUK%2Bmd4JfWor%2BWD%2FSFamDYCTRhdsyVwv0K7nyhigGwNpT13ovhr1bbJ86%2F9ZzMgaoKuyJRAfE%2BBQGL03KiaJiezY2ZLaqum5oNUg8c6ED397Tpuy%2BEFNFnGaERHF1uUEW0SA9WhFQ6pggAbFFXEL2%2FJMuWtRJ&X-Amz-Signature=81cc200afdb430a60ca59b1b2055e109961a821e6e14bd1979bcb7ddcb827aca&X-Amz-SignedHeaders=host&x-id=GetObject)
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


