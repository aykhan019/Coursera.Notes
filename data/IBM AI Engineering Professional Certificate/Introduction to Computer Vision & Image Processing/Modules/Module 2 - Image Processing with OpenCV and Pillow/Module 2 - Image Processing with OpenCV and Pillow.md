

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NP2MQAU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCsLn2LBqsCZfUtdf4f3YoGKAc9ZmjPuiH16l2d8rNiaQIgeGU02UWKBELIc5CgtbjynKF6f%2Fmr8yb69Bz0PXGH62Eq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDCuO0Z2Z1TTBtEuimSrcA3tppq7bpmGld%2BDNVSIhY%2B4Xo5hx1NGAS6DvaMEkYjDfQt9Vj6wq1ssMYZcrfS5%2FoUMw3Fg6oRKY1dSYS%2BCgvgXl0QkSC1%2B5bGXqE4oZC5QLPKLTUCoexnt%2B0cGtxLoId7OsAaxjEiuEHj5QDK%2Fg0lNDyf3ooEPvneeHwcudfv0db1d6WW7m0C0O9oU0vYL58rooyX0mLulBLRYIGRxVlfbpHXUJXr%2Bw9nxuUHtwF3jVs%2FStEE3VMe4OapaMA%2FLbCBEaWy8nVzOoHpMxgIZOQ9e%2F4fqPdFdm61XV2mgG35JxjIgBEXu5cZg8%2FDVmo9F39Oyjr5PAEtpKsSaqVWFHFn9t9iMzxO0wJu3IOa1JffHOAYhCz8xqsCFsT5CqXt4Me%2Bx%2FtysQCO1mMCrBeDhn7DWY7Q4zlacZp6rr%2Bm5kwbASX2Svp3%2BjSyYHlREHSRv04ZzsQkJfzzdIZNrY5IvHZNEBTKDfMwQdJy7biyhwuvKf4LvMIQ9WnqvOv5oCjiNFFq2cpnvEbTUly9o%2BZSv%2B4OUBQbeG2EA5u7SUtPW%2BbfQuGGVaxz0N5JbDvEUuz1dWqJPK8Cu0K%2BSKAltPUsbvJNJ2Crf%2Fm6nLgZWBXhdxsSLUkjanv7a3R%2BXFIUwNMMzKg70GOqUB54i9vlUbWZKi1ZpVbLpleGtrT6khsdGK6J%2FRqiIo%2B4me74SRF%2FwQ1TMhtAQD6Va6cfz1dXOZjINo5arCgx7ldcinKlg55ppOGzZZMRhF2Lef3HXqoALDpDOiQcDsJl1CJRET3jQ0GJlnk8wi0Wi6cQzGSc%2BH1BCF%2BqHbz4vT7tHtafCU6550I4XMqAVcewpyP3kU5N4%2BXamYFXaYrvnFMiVd5PbV&X-Amz-Signature=66edfa9415c66af5058f724dd37b30f216b46118d82fc53f1b4d03c133def198&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWMDXXIY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCBqU5JP1WFDbnLf4TIp1swZnc6fsyx0QRgmlB8CrDNZgIhAPWOWEvtuZdaB%2FJdkd9FEEymlLTJEeJ6F6L9hzSC7UQWKv8DCBkQABoMNjM3NDIzMTgzODA1IgzAX90Z6Fu%2FjdtNfq0q3APGWib6Xx%2BHNMKwBRI4bL%2BQzGzyj5zU0GtPUg1W4NYRAVQJ%2B3GG7B5h0F1VY2XXFaTrjYw6RiNbQ3RE0Sat0Xm%2FBE4uGdjQm8FKO6pHL85iZGfdMyKsHO5kteKd9GHFAfLpoD7S%2BZqiY8uH4uX65NMSPB2Q8PCVX6T%2BrTuNQIDC9V%2FKjcJtMM06vh4RFNFipWn0A5xYENpj2eVyXFfUKnBqV5hMeSV1oeS5XOe%2FoC21JOer06fA9hfb5JdLMOpo40Ilz7ltGA%2F3jeSyjumqgutYbaH3ZJ1iVdm1S1C0MZB%2BdobwkOFS3npj%2BcsGkiziOG0%2FguMyrW%2B3sIVpGdtCrj56Rj%2FUcTw7JV87PF98v2HpxAW0aOwRj4lqUWyLR1Hp9RsH%2Fy%2BLj7ekf6I0FwQrgQ2Mo96yxsP%2FdzhvuJzbEI6ekuq%2Bj3WyHpykuH6SzgQYakFJEp3fVAYUokX09Mn9d4yr2XCNPq8Fna2BUs936SAKQ%2FAHTDOmF9cmi%2Bhx6%2Fqh69vJV5CeKA4IzwUC6WqGCukuPKN15hgqOBGNB8qGy5cnPqEdZwhCfas5EWtFyrmgWXAXNyRHwdioV3XRSaUubGX9D%2BYkup2StIrcvuQESRR2uPfsoAZs7dTvBkeCmTDMyoO9BjqkAeX9HMqz%2BBuBwtK7MVPRmsHId%2BATWmUmRU7iIH49b%2B0JiTJprpAd4TwegEZvPLE4Q1BdNo7rj9zyMCGILGF6cWNuZ1nczLTSw%2FgyQhCOd%2BqZwliTSaXVL6bPsJvR73DWEHeyAaA8ZzYUXFifT7LQvO6RYaJ9Wy%2BGZ7%2FArOxBkeXYr6zfzmiN3zASaisMMCAfsYxUSWZLCNlV19iBpnCYNH9Ubf0f&X-Amz-Signature=bc4c825e61c08ebbeb62d731bd0d6780e1c108bc3913f341977d5067859f5082&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWMDXXIY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCBqU5JP1WFDbnLf4TIp1swZnc6fsyx0QRgmlB8CrDNZgIhAPWOWEvtuZdaB%2FJdkd9FEEymlLTJEeJ6F6L9hzSC7UQWKv8DCBkQABoMNjM3NDIzMTgzODA1IgzAX90Z6Fu%2FjdtNfq0q3APGWib6Xx%2BHNMKwBRI4bL%2BQzGzyj5zU0GtPUg1W4NYRAVQJ%2B3GG7B5h0F1VY2XXFaTrjYw6RiNbQ3RE0Sat0Xm%2FBE4uGdjQm8FKO6pHL85iZGfdMyKsHO5kteKd9GHFAfLpoD7S%2BZqiY8uH4uX65NMSPB2Q8PCVX6T%2BrTuNQIDC9V%2FKjcJtMM06vh4RFNFipWn0A5xYENpj2eVyXFfUKnBqV5hMeSV1oeS5XOe%2FoC21JOer06fA9hfb5JdLMOpo40Ilz7ltGA%2F3jeSyjumqgutYbaH3ZJ1iVdm1S1C0MZB%2BdobwkOFS3npj%2BcsGkiziOG0%2FguMyrW%2B3sIVpGdtCrj56Rj%2FUcTw7JV87PF98v2HpxAW0aOwRj4lqUWyLR1Hp9RsH%2Fy%2BLj7ekf6I0FwQrgQ2Mo96yxsP%2FdzhvuJzbEI6ekuq%2Bj3WyHpykuH6SzgQYakFJEp3fVAYUokX09Mn9d4yr2XCNPq8Fna2BUs936SAKQ%2FAHTDOmF9cmi%2Bhx6%2Fqh69vJV5CeKA4IzwUC6WqGCukuPKN15hgqOBGNB8qGy5cnPqEdZwhCfas5EWtFyrmgWXAXNyRHwdioV3XRSaUubGX9D%2BYkup2StIrcvuQESRR2uPfsoAZs7dTvBkeCmTDMyoO9BjqkAeX9HMqz%2BBuBwtK7MVPRmsHId%2BATWmUmRU7iIH49b%2B0JiTJprpAd4TwegEZvPLE4Q1BdNo7rj9zyMCGILGF6cWNuZ1nczLTSw%2FgyQhCOd%2BqZwliTSaXVL6bPsJvR73DWEHeyAaA8ZzYUXFifT7LQvO6RYaJ9Wy%2BGZ7%2FArOxBkeXYr6zfzmiN3zASaisMMCAfsYxUSWZLCNlV19iBpnCYNH9Ubf0f&X-Amz-Signature=c14028166b280d8185f247c2f5e1c4ac517468871cd6435a83a830875e7c7c35&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWMDXXIY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCBqU5JP1WFDbnLf4TIp1swZnc6fsyx0QRgmlB8CrDNZgIhAPWOWEvtuZdaB%2FJdkd9FEEymlLTJEeJ6F6L9hzSC7UQWKv8DCBkQABoMNjM3NDIzMTgzODA1IgzAX90Z6Fu%2FjdtNfq0q3APGWib6Xx%2BHNMKwBRI4bL%2BQzGzyj5zU0GtPUg1W4NYRAVQJ%2B3GG7B5h0F1VY2XXFaTrjYw6RiNbQ3RE0Sat0Xm%2FBE4uGdjQm8FKO6pHL85iZGfdMyKsHO5kteKd9GHFAfLpoD7S%2BZqiY8uH4uX65NMSPB2Q8PCVX6T%2BrTuNQIDC9V%2FKjcJtMM06vh4RFNFipWn0A5xYENpj2eVyXFfUKnBqV5hMeSV1oeS5XOe%2FoC21JOer06fA9hfb5JdLMOpo40Ilz7ltGA%2F3jeSyjumqgutYbaH3ZJ1iVdm1S1C0MZB%2BdobwkOFS3npj%2BcsGkiziOG0%2FguMyrW%2B3sIVpGdtCrj56Rj%2FUcTw7JV87PF98v2HpxAW0aOwRj4lqUWyLR1Hp9RsH%2Fy%2BLj7ekf6I0FwQrgQ2Mo96yxsP%2FdzhvuJzbEI6ekuq%2Bj3WyHpykuH6SzgQYakFJEp3fVAYUokX09Mn9d4yr2XCNPq8Fna2BUs936SAKQ%2FAHTDOmF9cmi%2Bhx6%2Fqh69vJV5CeKA4IzwUC6WqGCukuPKN15hgqOBGNB8qGy5cnPqEdZwhCfas5EWtFyrmgWXAXNyRHwdioV3XRSaUubGX9D%2BYkup2StIrcvuQESRR2uPfsoAZs7dTvBkeCmTDMyoO9BjqkAeX9HMqz%2BBuBwtK7MVPRmsHId%2BATWmUmRU7iIH49b%2B0JiTJprpAd4TwegEZvPLE4Q1BdNo7rj9zyMCGILGF6cWNuZ1nczLTSw%2FgyQhCOd%2BqZwliTSaXVL6bPsJvR73DWEHeyAaA8ZzYUXFifT7LQvO6RYaJ9Wy%2BGZ7%2FArOxBkeXYr6zfzmiN3zASaisMMCAfsYxUSWZLCNlV19iBpnCYNH9Ubf0f&X-Amz-Signature=0e9fec1de271b897bf44e711a46b21e89f5e64c916ab2b5f156b68f70385eb77&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWMDXXIY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCBqU5JP1WFDbnLf4TIp1swZnc6fsyx0QRgmlB8CrDNZgIhAPWOWEvtuZdaB%2FJdkd9FEEymlLTJEeJ6F6L9hzSC7UQWKv8DCBkQABoMNjM3NDIzMTgzODA1IgzAX90Z6Fu%2FjdtNfq0q3APGWib6Xx%2BHNMKwBRI4bL%2BQzGzyj5zU0GtPUg1W4NYRAVQJ%2B3GG7B5h0F1VY2XXFaTrjYw6RiNbQ3RE0Sat0Xm%2FBE4uGdjQm8FKO6pHL85iZGfdMyKsHO5kteKd9GHFAfLpoD7S%2BZqiY8uH4uX65NMSPB2Q8PCVX6T%2BrTuNQIDC9V%2FKjcJtMM06vh4RFNFipWn0A5xYENpj2eVyXFfUKnBqV5hMeSV1oeS5XOe%2FoC21JOer06fA9hfb5JdLMOpo40Ilz7ltGA%2F3jeSyjumqgutYbaH3ZJ1iVdm1S1C0MZB%2BdobwkOFS3npj%2BcsGkiziOG0%2FguMyrW%2B3sIVpGdtCrj56Rj%2FUcTw7JV87PF98v2HpxAW0aOwRj4lqUWyLR1Hp9RsH%2Fy%2BLj7ekf6I0FwQrgQ2Mo96yxsP%2FdzhvuJzbEI6ekuq%2Bj3WyHpykuH6SzgQYakFJEp3fVAYUokX09Mn9d4yr2XCNPq8Fna2BUs936SAKQ%2FAHTDOmF9cmi%2Bhx6%2Fqh69vJV5CeKA4IzwUC6WqGCukuPKN15hgqOBGNB8qGy5cnPqEdZwhCfas5EWtFyrmgWXAXNyRHwdioV3XRSaUubGX9D%2BYkup2StIrcvuQESRR2uPfsoAZs7dTvBkeCmTDMyoO9BjqkAeX9HMqz%2BBuBwtK7MVPRmsHId%2BATWmUmRU7iIH49b%2B0JiTJprpAd4TwegEZvPLE4Q1BdNo7rj9zyMCGILGF6cWNuZ1nczLTSw%2FgyQhCOd%2BqZwliTSaXVL6bPsJvR73DWEHeyAaA8ZzYUXFifT7LQvO6RYaJ9Wy%2BGZ7%2FArOxBkeXYr6zfzmiN3zASaisMMCAfsYxUSWZLCNlV19iBpnCYNH9Ubf0f&X-Amz-Signature=ce1f74abb934a46d55bcfab0fdb1e19d498b553eb06d1c1d534a67fea73cb791&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWMDXXIY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCBqU5JP1WFDbnLf4TIp1swZnc6fsyx0QRgmlB8CrDNZgIhAPWOWEvtuZdaB%2FJdkd9FEEymlLTJEeJ6F6L9hzSC7UQWKv8DCBkQABoMNjM3NDIzMTgzODA1IgzAX90Z6Fu%2FjdtNfq0q3APGWib6Xx%2BHNMKwBRI4bL%2BQzGzyj5zU0GtPUg1W4NYRAVQJ%2B3GG7B5h0F1VY2XXFaTrjYw6RiNbQ3RE0Sat0Xm%2FBE4uGdjQm8FKO6pHL85iZGfdMyKsHO5kteKd9GHFAfLpoD7S%2BZqiY8uH4uX65NMSPB2Q8PCVX6T%2BrTuNQIDC9V%2FKjcJtMM06vh4RFNFipWn0A5xYENpj2eVyXFfUKnBqV5hMeSV1oeS5XOe%2FoC21JOer06fA9hfb5JdLMOpo40Ilz7ltGA%2F3jeSyjumqgutYbaH3ZJ1iVdm1S1C0MZB%2BdobwkOFS3npj%2BcsGkiziOG0%2FguMyrW%2B3sIVpGdtCrj56Rj%2FUcTw7JV87PF98v2HpxAW0aOwRj4lqUWyLR1Hp9RsH%2Fy%2BLj7ekf6I0FwQrgQ2Mo96yxsP%2FdzhvuJzbEI6ekuq%2Bj3WyHpykuH6SzgQYakFJEp3fVAYUokX09Mn9d4yr2XCNPq8Fna2BUs936SAKQ%2FAHTDOmF9cmi%2Bhx6%2Fqh69vJV5CeKA4IzwUC6WqGCukuPKN15hgqOBGNB8qGy5cnPqEdZwhCfas5EWtFyrmgWXAXNyRHwdioV3XRSaUubGX9D%2BYkup2StIrcvuQESRR2uPfsoAZs7dTvBkeCmTDMyoO9BjqkAeX9HMqz%2BBuBwtK7MVPRmsHId%2BATWmUmRU7iIH49b%2B0JiTJprpAd4TwegEZvPLE4Q1BdNo7rj9zyMCGILGF6cWNuZ1nczLTSw%2FgyQhCOd%2BqZwliTSaXVL6bPsJvR73DWEHeyAaA8ZzYUXFifT7LQvO6RYaJ9Wy%2BGZ7%2FArOxBkeXYr6zfzmiN3zASaisMMCAfsYxUSWZLCNlV19iBpnCYNH9Ubf0f&X-Amz-Signature=01a7598349b36f7134c6f45e4288811a1ccb9cf8c1244199a14ea6cd9c61afd2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NP2MQAU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCsLn2LBqsCZfUtdf4f3YoGKAc9ZmjPuiH16l2d8rNiaQIgeGU02UWKBELIc5CgtbjynKF6f%2Fmr8yb69Bz0PXGH62Eq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDCuO0Z2Z1TTBtEuimSrcA3tppq7bpmGld%2BDNVSIhY%2B4Xo5hx1NGAS6DvaMEkYjDfQt9Vj6wq1ssMYZcrfS5%2FoUMw3Fg6oRKY1dSYS%2BCgvgXl0QkSC1%2B5bGXqE4oZC5QLPKLTUCoexnt%2B0cGtxLoId7OsAaxjEiuEHj5QDK%2Fg0lNDyf3ooEPvneeHwcudfv0db1d6WW7m0C0O9oU0vYL58rooyX0mLulBLRYIGRxVlfbpHXUJXr%2Bw9nxuUHtwF3jVs%2FStEE3VMe4OapaMA%2FLbCBEaWy8nVzOoHpMxgIZOQ9e%2F4fqPdFdm61XV2mgG35JxjIgBEXu5cZg8%2FDVmo9F39Oyjr5PAEtpKsSaqVWFHFn9t9iMzxO0wJu3IOa1JffHOAYhCz8xqsCFsT5CqXt4Me%2Bx%2FtysQCO1mMCrBeDhn7DWY7Q4zlacZp6rr%2Bm5kwbASX2Svp3%2BjSyYHlREHSRv04ZzsQkJfzzdIZNrY5IvHZNEBTKDfMwQdJy7biyhwuvKf4LvMIQ9WnqvOv5oCjiNFFq2cpnvEbTUly9o%2BZSv%2B4OUBQbeG2EA5u7SUtPW%2BbfQuGGVaxz0N5JbDvEUuz1dWqJPK8Cu0K%2BSKAltPUsbvJNJ2Crf%2Fm6nLgZWBXhdxsSLUkjanv7a3R%2BXFIUwNMMzKg70GOqUB54i9vlUbWZKi1ZpVbLpleGtrT6khsdGK6J%2FRqiIo%2B4me74SRF%2FwQ1TMhtAQD6Va6cfz1dXOZjINo5arCgx7ldcinKlg55ppOGzZZMRhF2Lef3HXqoALDpDOiQcDsJl1CJRET3jQ0GJlnk8wi0Wi6cQzGSc%2BH1BCF%2BqHbz4vT7tHtafCU6550I4XMqAVcewpyP3kU5N4%2BXamYFXaYrvnFMiVd5PbV&X-Amz-Signature=9bfc7f0d78e8f97b9c8388737d6056b13ddcf2bd00940ef62ea029c23df78ac7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NP2MQAU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCsLn2LBqsCZfUtdf4f3YoGKAc9ZmjPuiH16l2d8rNiaQIgeGU02UWKBELIc5CgtbjynKF6f%2Fmr8yb69Bz0PXGH62Eq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDCuO0Z2Z1TTBtEuimSrcA3tppq7bpmGld%2BDNVSIhY%2B4Xo5hx1NGAS6DvaMEkYjDfQt9Vj6wq1ssMYZcrfS5%2FoUMw3Fg6oRKY1dSYS%2BCgvgXl0QkSC1%2B5bGXqE4oZC5QLPKLTUCoexnt%2B0cGtxLoId7OsAaxjEiuEHj5QDK%2Fg0lNDyf3ooEPvneeHwcudfv0db1d6WW7m0C0O9oU0vYL58rooyX0mLulBLRYIGRxVlfbpHXUJXr%2Bw9nxuUHtwF3jVs%2FStEE3VMe4OapaMA%2FLbCBEaWy8nVzOoHpMxgIZOQ9e%2F4fqPdFdm61XV2mgG35JxjIgBEXu5cZg8%2FDVmo9F39Oyjr5PAEtpKsSaqVWFHFn9t9iMzxO0wJu3IOa1JffHOAYhCz8xqsCFsT5CqXt4Me%2Bx%2FtysQCO1mMCrBeDhn7DWY7Q4zlacZp6rr%2Bm5kwbASX2Svp3%2BjSyYHlREHSRv04ZzsQkJfzzdIZNrY5IvHZNEBTKDfMwQdJy7biyhwuvKf4LvMIQ9WnqvOv5oCjiNFFq2cpnvEbTUly9o%2BZSv%2B4OUBQbeG2EA5u7SUtPW%2BbfQuGGVaxz0N5JbDvEUuz1dWqJPK8Cu0K%2BSKAltPUsbvJNJ2Crf%2Fm6nLgZWBXhdxsSLUkjanv7a3R%2BXFIUwNMMzKg70GOqUB54i9vlUbWZKi1ZpVbLpleGtrT6khsdGK6J%2FRqiIo%2B4me74SRF%2FwQ1TMhtAQD6Va6cfz1dXOZjINo5arCgx7ldcinKlg55ppOGzZZMRhF2Lef3HXqoALDpDOiQcDsJl1CJRET3jQ0GJlnk8wi0Wi6cQzGSc%2BH1BCF%2BqHbz4vT7tHtafCU6550I4XMqAVcewpyP3kU5N4%2BXamYFXaYrvnFMiVd5PbV&X-Amz-Signature=bd91a18f459911d5bf5d8b6ab528931a1f20fe9de6a035e3ad8f256125cb4aed&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NP2MQAU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCsLn2LBqsCZfUtdf4f3YoGKAc9ZmjPuiH16l2d8rNiaQIgeGU02UWKBELIc5CgtbjynKF6f%2Fmr8yb69Bz0PXGH62Eq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDCuO0Z2Z1TTBtEuimSrcA3tppq7bpmGld%2BDNVSIhY%2B4Xo5hx1NGAS6DvaMEkYjDfQt9Vj6wq1ssMYZcrfS5%2FoUMw3Fg6oRKY1dSYS%2BCgvgXl0QkSC1%2B5bGXqE4oZC5QLPKLTUCoexnt%2B0cGtxLoId7OsAaxjEiuEHj5QDK%2Fg0lNDyf3ooEPvneeHwcudfv0db1d6WW7m0C0O9oU0vYL58rooyX0mLulBLRYIGRxVlfbpHXUJXr%2Bw9nxuUHtwF3jVs%2FStEE3VMe4OapaMA%2FLbCBEaWy8nVzOoHpMxgIZOQ9e%2F4fqPdFdm61XV2mgG35JxjIgBEXu5cZg8%2FDVmo9F39Oyjr5PAEtpKsSaqVWFHFn9t9iMzxO0wJu3IOa1JffHOAYhCz8xqsCFsT5CqXt4Me%2Bx%2FtysQCO1mMCrBeDhn7DWY7Q4zlacZp6rr%2Bm5kwbASX2Svp3%2BjSyYHlREHSRv04ZzsQkJfzzdIZNrY5IvHZNEBTKDfMwQdJy7biyhwuvKf4LvMIQ9WnqvOv5oCjiNFFq2cpnvEbTUly9o%2BZSv%2B4OUBQbeG2EA5u7SUtPW%2BbfQuGGVaxz0N5JbDvEUuz1dWqJPK8Cu0K%2BSKAltPUsbvJNJ2Crf%2Fm6nLgZWBXhdxsSLUkjanv7a3R%2BXFIUwNMMzKg70GOqUB54i9vlUbWZKi1ZpVbLpleGtrT6khsdGK6J%2FRqiIo%2B4me74SRF%2FwQ1TMhtAQD6Va6cfz1dXOZjINo5arCgx7ldcinKlg55ppOGzZZMRhF2Lef3HXqoALDpDOiQcDsJl1CJRET3jQ0GJlnk8wi0Wi6cQzGSc%2BH1BCF%2BqHbz4vT7tHtafCU6550I4XMqAVcewpyP3kU5N4%2BXamYFXaYrvnFMiVd5PbV&X-Amz-Signature=820d223d579dbb59a56c814d298a2f2b0d0cb53543f9e06d99338e101dfd4e2e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NP2MQAU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCsLn2LBqsCZfUtdf4f3YoGKAc9ZmjPuiH16l2d8rNiaQIgeGU02UWKBELIc5CgtbjynKF6f%2Fmr8yb69Bz0PXGH62Eq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDCuO0Z2Z1TTBtEuimSrcA3tppq7bpmGld%2BDNVSIhY%2B4Xo5hx1NGAS6DvaMEkYjDfQt9Vj6wq1ssMYZcrfS5%2FoUMw3Fg6oRKY1dSYS%2BCgvgXl0QkSC1%2B5bGXqE4oZC5QLPKLTUCoexnt%2B0cGtxLoId7OsAaxjEiuEHj5QDK%2Fg0lNDyf3ooEPvneeHwcudfv0db1d6WW7m0C0O9oU0vYL58rooyX0mLulBLRYIGRxVlfbpHXUJXr%2Bw9nxuUHtwF3jVs%2FStEE3VMe4OapaMA%2FLbCBEaWy8nVzOoHpMxgIZOQ9e%2F4fqPdFdm61XV2mgG35JxjIgBEXu5cZg8%2FDVmo9F39Oyjr5PAEtpKsSaqVWFHFn9t9iMzxO0wJu3IOa1JffHOAYhCz8xqsCFsT5CqXt4Me%2Bx%2FtysQCO1mMCrBeDhn7DWY7Q4zlacZp6rr%2Bm5kwbASX2Svp3%2BjSyYHlREHSRv04ZzsQkJfzzdIZNrY5IvHZNEBTKDfMwQdJy7biyhwuvKf4LvMIQ9WnqvOv5oCjiNFFq2cpnvEbTUly9o%2BZSv%2B4OUBQbeG2EA5u7SUtPW%2BbfQuGGVaxz0N5JbDvEUuz1dWqJPK8Cu0K%2BSKAltPUsbvJNJ2Crf%2Fm6nLgZWBXhdxsSLUkjanv7a3R%2BXFIUwNMMzKg70GOqUB54i9vlUbWZKi1ZpVbLpleGtrT6khsdGK6J%2FRqiIo%2B4me74SRF%2FwQ1TMhtAQD6Va6cfz1dXOZjINo5arCgx7ldcinKlg55ppOGzZZMRhF2Lef3HXqoALDpDOiQcDsJl1CJRET3jQ0GJlnk8wi0Wi6cQzGSc%2BH1BCF%2BqHbz4vT7tHtafCU6550I4XMqAVcewpyP3kU5N4%2BXamYFXaYrvnFMiVd5PbV&X-Amz-Signature=87fae965560509edf9d3e012b1f15b034b1bd32e3558942435dae305f70cffe3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NP2MQAU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCsLn2LBqsCZfUtdf4f3YoGKAc9ZmjPuiH16l2d8rNiaQIgeGU02UWKBELIc5CgtbjynKF6f%2Fmr8yb69Bz0PXGH62Eq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDCuO0Z2Z1TTBtEuimSrcA3tppq7bpmGld%2BDNVSIhY%2B4Xo5hx1NGAS6DvaMEkYjDfQt9Vj6wq1ssMYZcrfS5%2FoUMw3Fg6oRKY1dSYS%2BCgvgXl0QkSC1%2B5bGXqE4oZC5QLPKLTUCoexnt%2B0cGtxLoId7OsAaxjEiuEHj5QDK%2Fg0lNDyf3ooEPvneeHwcudfv0db1d6WW7m0C0O9oU0vYL58rooyX0mLulBLRYIGRxVlfbpHXUJXr%2Bw9nxuUHtwF3jVs%2FStEE3VMe4OapaMA%2FLbCBEaWy8nVzOoHpMxgIZOQ9e%2F4fqPdFdm61XV2mgG35JxjIgBEXu5cZg8%2FDVmo9F39Oyjr5PAEtpKsSaqVWFHFn9t9iMzxO0wJu3IOa1JffHOAYhCz8xqsCFsT5CqXt4Me%2Bx%2FtysQCO1mMCrBeDhn7DWY7Q4zlacZp6rr%2Bm5kwbASX2Svp3%2BjSyYHlREHSRv04ZzsQkJfzzdIZNrY5IvHZNEBTKDfMwQdJy7biyhwuvKf4LvMIQ9WnqvOv5oCjiNFFq2cpnvEbTUly9o%2BZSv%2B4OUBQbeG2EA5u7SUtPW%2BbfQuGGVaxz0N5JbDvEUuz1dWqJPK8Cu0K%2BSKAltPUsbvJNJ2Crf%2Fm6nLgZWBXhdxsSLUkjanv7a3R%2BXFIUwNMMzKg70GOqUB54i9vlUbWZKi1ZpVbLpleGtrT6khsdGK6J%2FRqiIo%2B4me74SRF%2FwQ1TMhtAQD6Va6cfz1dXOZjINo5arCgx7ldcinKlg55ppOGzZZMRhF2Lef3HXqoALDpDOiQcDsJl1CJRET3jQ0GJlnk8wi0Wi6cQzGSc%2BH1BCF%2BqHbz4vT7tHtafCU6550I4XMqAVcewpyP3kU5N4%2BXamYFXaYrvnFMiVd5PbV&X-Amz-Signature=a11c26a38b073dda64ccd45882a7a3b8d08e84dd4b55fff46c84d70cee11a98c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


