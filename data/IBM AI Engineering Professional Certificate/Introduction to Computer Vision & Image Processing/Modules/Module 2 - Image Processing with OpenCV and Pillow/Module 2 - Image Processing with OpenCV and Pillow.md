

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAGA5F6N%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUQ9cbbrFgkxK0ez5yUnf1F6pa5hZdOirOMlcPHSI0nAiAqFj2WwS6EJhBSrsdOUunprxO3ll3URwG%2BdVgVvWjZ1yr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIManoIoapPkXRjqgltKtwDdm9tqtZUjw206ZxTcLQsUcnKZHhRT63G2Yk7ta32GD4uDBT2Ce86RLqJy0DJUSUU4ZG5kVqDk4PwiPDMLZNDqlKx%2BrNkmbztJYkaDbtjGJAFmYfz03lfaXqr8y5O68dsXStV4UzeQlpsdpeMPGnmSxYhXXnjMECWjT7XHH2%2FVx4o7Jq1KQl1KzYZeMKxi9AQihYPmRrwdU3qPCqZa%2Fb7Z1InRctvS%2FsKWxUpIKzxE7XMuNY0Nn3Ars40XPJtGhXfpKEwYg3rBVdvYou9vBr3Ik0NgaoZVd9rYVZz%2FHRCjw%2FNl6FG6j3nAumk34%2Bbhtx83%2FK34bEdlan4v21rhuNG0PFb5MaKKDQHfvnY2EDFsRE3FfX%2FFLuSksEjgXlOQwmQ%2B6AEM%2BjZf%2FQ4sLJf4Xkvxb7QcKDo8hNY0z1nmekW9Yzjyiz0mCioQW0zplgkJircsOeeb%2FDMXOmzJGN6o36idxMv9ExO%2BxW60OQ%2BmeWWbKBnyGj0AtZOc2RkKIONJL80CpQ4LagpODhJKb8VKY%2FAyqIBSXpznCsrCuuCZY%2F4IEajZKE0EQZXDyiYPEcGM9Kf3x07kY5PwOl0s5JEiJoLF82%2FGcYXLvSOEKDXmR9E6NDJAm6k8AeOYShfnacwzZzYvgY6pgES9RL9TnIR%2BLIDKef%2FqplLlphy84vGe0OnezdWQ9dkWOzwfS9cZUtP3yn%2FV5t6%2BReiQC5PH8aLW5A6lEBGEbpEDQNXKNYtWmL9l2D1ggThcqm9zMs7fjIuemKfCjAaQw3pE%2BlN1atnElef0244leyxicHM6OQLL0u%2Ff9Xf82lv%2FqU%2FWjVv0H4woXmsmozekdOO9MBgW3E54NahI9pRbnLvOf6Y%2BwmU&X-Amz-Signature=e852c96388787573e257adbbbc40e52575d90a07579eb5f160864ef21c5556e8&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOWYJVNG%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEVtFqlO7byaYu6D0%2BRlPZF5dJKObqAu2papeT1qKgeAIhAKUKUPyWdq6TCxJ5OY3wr9pBl%2BZPhcdedHLCAx3w21bMKv8DCCAQABoMNjM3NDIzMTgzODA1IgxCSJJ1IKtm6xIkYyQq3AMCQUmsj%2Bg5578ynREPRLTfNONstTWf1gfTv%2F1T%2BMEuQ9FxqwEusAsDBy89phKTlTfo8qlegP4WTomh5HQqwRe%2Bq7LCs90FAhO8l5M7spHiTlEUm0KCiVroMuZUXbBmkyGVFryhzu09KGGqONQ24jpBU6cNRhUmexJ1AmF3RVi0I%2B55LsR6rgd6E511ZKPmmgDWqlWjG9HFdXTAU5waw%2FL%2FKxy4sMVvFM3ZKpVspS06UDkVwLrPVz9VYJZXiDuP32%2BSgd6dYj483JUxOZiopPcP1ryXFOz4LXuPj5CeXgAJSwOZABzFmMBu%2FuKv8kvyOwUsNMJwyri6c21AGXRrQA7Es98VVvWuHtis3lIUz2SGkFCMqQcxDLdo5RyW1AOdxZRZmzu3F3v1cNP9Zpz5E5e6spW%2BAGmYNK64Rsn%2F5%2Bx2Q%2BtJwTBOVrN%2FiJaRxAzQ2uV2Iy%2ByaksHv8eNM%2FgzJg3kHCriyO7QocYBr9VbewPpocNGJRzzaot2eh4%2BVs3RP9ZPJgDVXc3mKo6xlwVaNSqX%2BsGUtEG6DTNqHtixsVLB%2Fu01q5WfI0LKG40by42i8N18B46k6A8wht1KZrzcEnYhq2XrArV6%2BUqzWiZgz9MXg8JDJ68dLKEMBuObhTCG%2F9e%2BBjqkAaMrPR5uik77GF6gIHmVRD9RpQP1LTEEnBUIr9RVWfXW%2FQmJclKD2YgLEttDxrSUQviDU9ga8XYbtzd65L1KJIMWdHU2UIldzjd4pgHDJpPwn7tlcnHXK1NXw7RDf%2B28Basr3Q6oDEUB90dold6I7AAskSB7mVJB70dN5UUJnpNOuzJMMm53VjDIQuZZWN5EVaDdKcHCm%2F2UGYMHi1Na%2Fxzp6bWo&X-Amz-Signature=4996b010f7deb080634335af60835a2a8ee581714db61d07015b6d83803e7867&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOWYJVNG%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEVtFqlO7byaYu6D0%2BRlPZF5dJKObqAu2papeT1qKgeAIhAKUKUPyWdq6TCxJ5OY3wr9pBl%2BZPhcdedHLCAx3w21bMKv8DCCAQABoMNjM3NDIzMTgzODA1IgxCSJJ1IKtm6xIkYyQq3AMCQUmsj%2Bg5578ynREPRLTfNONstTWf1gfTv%2F1T%2BMEuQ9FxqwEusAsDBy89phKTlTfo8qlegP4WTomh5HQqwRe%2Bq7LCs90FAhO8l5M7spHiTlEUm0KCiVroMuZUXbBmkyGVFryhzu09KGGqONQ24jpBU6cNRhUmexJ1AmF3RVi0I%2B55LsR6rgd6E511ZKPmmgDWqlWjG9HFdXTAU5waw%2FL%2FKxy4sMVvFM3ZKpVspS06UDkVwLrPVz9VYJZXiDuP32%2BSgd6dYj483JUxOZiopPcP1ryXFOz4LXuPj5CeXgAJSwOZABzFmMBu%2FuKv8kvyOwUsNMJwyri6c21AGXRrQA7Es98VVvWuHtis3lIUz2SGkFCMqQcxDLdo5RyW1AOdxZRZmzu3F3v1cNP9Zpz5E5e6spW%2BAGmYNK64Rsn%2F5%2Bx2Q%2BtJwTBOVrN%2FiJaRxAzQ2uV2Iy%2ByaksHv8eNM%2FgzJg3kHCriyO7QocYBr9VbewPpocNGJRzzaot2eh4%2BVs3RP9ZPJgDVXc3mKo6xlwVaNSqX%2BsGUtEG6DTNqHtixsVLB%2Fu01q5WfI0LKG40by42i8N18B46k6A8wht1KZrzcEnYhq2XrArV6%2BUqzWiZgz9MXg8JDJ68dLKEMBuObhTCG%2F9e%2BBjqkAaMrPR5uik77GF6gIHmVRD9RpQP1LTEEnBUIr9RVWfXW%2FQmJclKD2YgLEttDxrSUQviDU9ga8XYbtzd65L1KJIMWdHU2UIldzjd4pgHDJpPwn7tlcnHXK1NXw7RDf%2B28Basr3Q6oDEUB90dold6I7AAskSB7mVJB70dN5UUJnpNOuzJMMm53VjDIQuZZWN5EVaDdKcHCm%2F2UGYMHi1Na%2Fxzp6bWo&X-Amz-Signature=ca050109e8aeb2e67af20e34507ea2a1df71c895298f64963a5a5a0cbd63523b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOWYJVNG%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEVtFqlO7byaYu6D0%2BRlPZF5dJKObqAu2papeT1qKgeAIhAKUKUPyWdq6TCxJ5OY3wr9pBl%2BZPhcdedHLCAx3w21bMKv8DCCAQABoMNjM3NDIzMTgzODA1IgxCSJJ1IKtm6xIkYyQq3AMCQUmsj%2Bg5578ynREPRLTfNONstTWf1gfTv%2F1T%2BMEuQ9FxqwEusAsDBy89phKTlTfo8qlegP4WTomh5HQqwRe%2Bq7LCs90FAhO8l5M7spHiTlEUm0KCiVroMuZUXbBmkyGVFryhzu09KGGqONQ24jpBU6cNRhUmexJ1AmF3RVi0I%2B55LsR6rgd6E511ZKPmmgDWqlWjG9HFdXTAU5waw%2FL%2FKxy4sMVvFM3ZKpVspS06UDkVwLrPVz9VYJZXiDuP32%2BSgd6dYj483JUxOZiopPcP1ryXFOz4LXuPj5CeXgAJSwOZABzFmMBu%2FuKv8kvyOwUsNMJwyri6c21AGXRrQA7Es98VVvWuHtis3lIUz2SGkFCMqQcxDLdo5RyW1AOdxZRZmzu3F3v1cNP9Zpz5E5e6spW%2BAGmYNK64Rsn%2F5%2Bx2Q%2BtJwTBOVrN%2FiJaRxAzQ2uV2Iy%2ByaksHv8eNM%2FgzJg3kHCriyO7QocYBr9VbewPpocNGJRzzaot2eh4%2BVs3RP9ZPJgDVXc3mKo6xlwVaNSqX%2BsGUtEG6DTNqHtixsVLB%2Fu01q5WfI0LKG40by42i8N18B46k6A8wht1KZrzcEnYhq2XrArV6%2BUqzWiZgz9MXg8JDJ68dLKEMBuObhTCG%2F9e%2BBjqkAaMrPR5uik77GF6gIHmVRD9RpQP1LTEEnBUIr9RVWfXW%2FQmJclKD2YgLEttDxrSUQviDU9ga8XYbtzd65L1KJIMWdHU2UIldzjd4pgHDJpPwn7tlcnHXK1NXw7RDf%2B28Basr3Q6oDEUB90dold6I7AAskSB7mVJB70dN5UUJnpNOuzJMMm53VjDIQuZZWN5EVaDdKcHCm%2F2UGYMHi1Na%2Fxzp6bWo&X-Amz-Signature=ae62acd6b861293a2d1866f740fc250f7ff0d6cffbd3c23ff9471f7361278c7a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOWYJVNG%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEVtFqlO7byaYu6D0%2BRlPZF5dJKObqAu2papeT1qKgeAIhAKUKUPyWdq6TCxJ5OY3wr9pBl%2BZPhcdedHLCAx3w21bMKv8DCCAQABoMNjM3NDIzMTgzODA1IgxCSJJ1IKtm6xIkYyQq3AMCQUmsj%2Bg5578ynREPRLTfNONstTWf1gfTv%2F1T%2BMEuQ9FxqwEusAsDBy89phKTlTfo8qlegP4WTomh5HQqwRe%2Bq7LCs90FAhO8l5M7spHiTlEUm0KCiVroMuZUXbBmkyGVFryhzu09KGGqONQ24jpBU6cNRhUmexJ1AmF3RVi0I%2B55LsR6rgd6E511ZKPmmgDWqlWjG9HFdXTAU5waw%2FL%2FKxy4sMVvFM3ZKpVspS06UDkVwLrPVz9VYJZXiDuP32%2BSgd6dYj483JUxOZiopPcP1ryXFOz4LXuPj5CeXgAJSwOZABzFmMBu%2FuKv8kvyOwUsNMJwyri6c21AGXRrQA7Es98VVvWuHtis3lIUz2SGkFCMqQcxDLdo5RyW1AOdxZRZmzu3F3v1cNP9Zpz5E5e6spW%2BAGmYNK64Rsn%2F5%2Bx2Q%2BtJwTBOVrN%2FiJaRxAzQ2uV2Iy%2ByaksHv8eNM%2FgzJg3kHCriyO7QocYBr9VbewPpocNGJRzzaot2eh4%2BVs3RP9ZPJgDVXc3mKo6xlwVaNSqX%2BsGUtEG6DTNqHtixsVLB%2Fu01q5WfI0LKG40by42i8N18B46k6A8wht1KZrzcEnYhq2XrArV6%2BUqzWiZgz9MXg8JDJ68dLKEMBuObhTCG%2F9e%2BBjqkAaMrPR5uik77GF6gIHmVRD9RpQP1LTEEnBUIr9RVWfXW%2FQmJclKD2YgLEttDxrSUQviDU9ga8XYbtzd65L1KJIMWdHU2UIldzjd4pgHDJpPwn7tlcnHXK1NXw7RDf%2B28Basr3Q6oDEUB90dold6I7AAskSB7mVJB70dN5UUJnpNOuzJMMm53VjDIQuZZWN5EVaDdKcHCm%2F2UGYMHi1Na%2Fxzp6bWo&X-Amz-Signature=b12246f7f51e8d57a6dbf38beb53926427f27b47a008fb54adaffc0ab78f36a8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOWYJVNG%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEVtFqlO7byaYu6D0%2BRlPZF5dJKObqAu2papeT1qKgeAIhAKUKUPyWdq6TCxJ5OY3wr9pBl%2BZPhcdedHLCAx3w21bMKv8DCCAQABoMNjM3NDIzMTgzODA1IgxCSJJ1IKtm6xIkYyQq3AMCQUmsj%2Bg5578ynREPRLTfNONstTWf1gfTv%2F1T%2BMEuQ9FxqwEusAsDBy89phKTlTfo8qlegP4WTomh5HQqwRe%2Bq7LCs90FAhO8l5M7spHiTlEUm0KCiVroMuZUXbBmkyGVFryhzu09KGGqONQ24jpBU6cNRhUmexJ1AmF3RVi0I%2B55LsR6rgd6E511ZKPmmgDWqlWjG9HFdXTAU5waw%2FL%2FKxy4sMVvFM3ZKpVspS06UDkVwLrPVz9VYJZXiDuP32%2BSgd6dYj483JUxOZiopPcP1ryXFOz4LXuPj5CeXgAJSwOZABzFmMBu%2FuKv8kvyOwUsNMJwyri6c21AGXRrQA7Es98VVvWuHtis3lIUz2SGkFCMqQcxDLdo5RyW1AOdxZRZmzu3F3v1cNP9Zpz5E5e6spW%2BAGmYNK64Rsn%2F5%2Bx2Q%2BtJwTBOVrN%2FiJaRxAzQ2uV2Iy%2ByaksHv8eNM%2FgzJg3kHCriyO7QocYBr9VbewPpocNGJRzzaot2eh4%2BVs3RP9ZPJgDVXc3mKo6xlwVaNSqX%2BsGUtEG6DTNqHtixsVLB%2Fu01q5WfI0LKG40by42i8N18B46k6A8wht1KZrzcEnYhq2XrArV6%2BUqzWiZgz9MXg8JDJ68dLKEMBuObhTCG%2F9e%2BBjqkAaMrPR5uik77GF6gIHmVRD9RpQP1LTEEnBUIr9RVWfXW%2FQmJclKD2YgLEttDxrSUQviDU9ga8XYbtzd65L1KJIMWdHU2UIldzjd4pgHDJpPwn7tlcnHXK1NXw7RDf%2B28Basr3Q6oDEUB90dold6I7AAskSB7mVJB70dN5UUJnpNOuzJMMm53VjDIQuZZWN5EVaDdKcHCm%2F2UGYMHi1Na%2Fxzp6bWo&X-Amz-Signature=c568fd44c5df1334dbba22b8df7428e34438730909ee1a1ba5a7e3df0fde6768&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAGA5F6N%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUQ9cbbrFgkxK0ez5yUnf1F6pa5hZdOirOMlcPHSI0nAiAqFj2WwS6EJhBSrsdOUunprxO3ll3URwG%2BdVgVvWjZ1yr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIManoIoapPkXRjqgltKtwDdm9tqtZUjw206ZxTcLQsUcnKZHhRT63G2Yk7ta32GD4uDBT2Ce86RLqJy0DJUSUU4ZG5kVqDk4PwiPDMLZNDqlKx%2BrNkmbztJYkaDbtjGJAFmYfz03lfaXqr8y5O68dsXStV4UzeQlpsdpeMPGnmSxYhXXnjMECWjT7XHH2%2FVx4o7Jq1KQl1KzYZeMKxi9AQihYPmRrwdU3qPCqZa%2Fb7Z1InRctvS%2FsKWxUpIKzxE7XMuNY0Nn3Ars40XPJtGhXfpKEwYg3rBVdvYou9vBr3Ik0NgaoZVd9rYVZz%2FHRCjw%2FNl6FG6j3nAumk34%2Bbhtx83%2FK34bEdlan4v21rhuNG0PFb5MaKKDQHfvnY2EDFsRE3FfX%2FFLuSksEjgXlOQwmQ%2B6AEM%2BjZf%2FQ4sLJf4Xkvxb7QcKDo8hNY0z1nmekW9Yzjyiz0mCioQW0zplgkJircsOeeb%2FDMXOmzJGN6o36idxMv9ExO%2BxW60OQ%2BmeWWbKBnyGj0AtZOc2RkKIONJL80CpQ4LagpODhJKb8VKY%2FAyqIBSXpznCsrCuuCZY%2F4IEajZKE0EQZXDyiYPEcGM9Kf3x07kY5PwOl0s5JEiJoLF82%2FGcYXLvSOEKDXmR9E6NDJAm6k8AeOYShfnacwzZzYvgY6pgES9RL9TnIR%2BLIDKef%2FqplLlphy84vGe0OnezdWQ9dkWOzwfS9cZUtP3yn%2FV5t6%2BReiQC5PH8aLW5A6lEBGEbpEDQNXKNYtWmL9l2D1ggThcqm9zMs7fjIuemKfCjAaQw3pE%2BlN1atnElef0244leyxicHM6OQLL0u%2Ff9Xf82lv%2FqU%2FWjVv0H4woXmsmozekdOO9MBgW3E54NahI9pRbnLvOf6Y%2BwmU&X-Amz-Signature=33334d83927c247756aa8b655081f12383a5cdd3a1974af4c915cb0326cf359b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAGA5F6N%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUQ9cbbrFgkxK0ez5yUnf1F6pa5hZdOirOMlcPHSI0nAiAqFj2WwS6EJhBSrsdOUunprxO3ll3URwG%2BdVgVvWjZ1yr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIManoIoapPkXRjqgltKtwDdm9tqtZUjw206ZxTcLQsUcnKZHhRT63G2Yk7ta32GD4uDBT2Ce86RLqJy0DJUSUU4ZG5kVqDk4PwiPDMLZNDqlKx%2BrNkmbztJYkaDbtjGJAFmYfz03lfaXqr8y5O68dsXStV4UzeQlpsdpeMPGnmSxYhXXnjMECWjT7XHH2%2FVx4o7Jq1KQl1KzYZeMKxi9AQihYPmRrwdU3qPCqZa%2Fb7Z1InRctvS%2FsKWxUpIKzxE7XMuNY0Nn3Ars40XPJtGhXfpKEwYg3rBVdvYou9vBr3Ik0NgaoZVd9rYVZz%2FHRCjw%2FNl6FG6j3nAumk34%2Bbhtx83%2FK34bEdlan4v21rhuNG0PFb5MaKKDQHfvnY2EDFsRE3FfX%2FFLuSksEjgXlOQwmQ%2B6AEM%2BjZf%2FQ4sLJf4Xkvxb7QcKDo8hNY0z1nmekW9Yzjyiz0mCioQW0zplgkJircsOeeb%2FDMXOmzJGN6o36idxMv9ExO%2BxW60OQ%2BmeWWbKBnyGj0AtZOc2RkKIONJL80CpQ4LagpODhJKb8VKY%2FAyqIBSXpznCsrCuuCZY%2F4IEajZKE0EQZXDyiYPEcGM9Kf3x07kY5PwOl0s5JEiJoLF82%2FGcYXLvSOEKDXmR9E6NDJAm6k8AeOYShfnacwzZzYvgY6pgES9RL9TnIR%2BLIDKef%2FqplLlphy84vGe0OnezdWQ9dkWOzwfS9cZUtP3yn%2FV5t6%2BReiQC5PH8aLW5A6lEBGEbpEDQNXKNYtWmL9l2D1ggThcqm9zMs7fjIuemKfCjAaQw3pE%2BlN1atnElef0244leyxicHM6OQLL0u%2Ff9Xf82lv%2FqU%2FWjVv0H4woXmsmozekdOO9MBgW3E54NahI9pRbnLvOf6Y%2BwmU&X-Amz-Signature=9c5f791ef9b153df04dd8974792c7a8cfc30e46f1c894e2305fd0f6af5c93cf3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAGA5F6N%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUQ9cbbrFgkxK0ez5yUnf1F6pa5hZdOirOMlcPHSI0nAiAqFj2WwS6EJhBSrsdOUunprxO3ll3URwG%2BdVgVvWjZ1yr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIManoIoapPkXRjqgltKtwDdm9tqtZUjw206ZxTcLQsUcnKZHhRT63G2Yk7ta32GD4uDBT2Ce86RLqJy0DJUSUU4ZG5kVqDk4PwiPDMLZNDqlKx%2BrNkmbztJYkaDbtjGJAFmYfz03lfaXqr8y5O68dsXStV4UzeQlpsdpeMPGnmSxYhXXnjMECWjT7XHH2%2FVx4o7Jq1KQl1KzYZeMKxi9AQihYPmRrwdU3qPCqZa%2Fb7Z1InRctvS%2FsKWxUpIKzxE7XMuNY0Nn3Ars40XPJtGhXfpKEwYg3rBVdvYou9vBr3Ik0NgaoZVd9rYVZz%2FHRCjw%2FNl6FG6j3nAumk34%2Bbhtx83%2FK34bEdlan4v21rhuNG0PFb5MaKKDQHfvnY2EDFsRE3FfX%2FFLuSksEjgXlOQwmQ%2B6AEM%2BjZf%2FQ4sLJf4Xkvxb7QcKDo8hNY0z1nmekW9Yzjyiz0mCioQW0zplgkJircsOeeb%2FDMXOmzJGN6o36idxMv9ExO%2BxW60OQ%2BmeWWbKBnyGj0AtZOc2RkKIONJL80CpQ4LagpODhJKb8VKY%2FAyqIBSXpznCsrCuuCZY%2F4IEajZKE0EQZXDyiYPEcGM9Kf3x07kY5PwOl0s5JEiJoLF82%2FGcYXLvSOEKDXmR9E6NDJAm6k8AeOYShfnacwzZzYvgY6pgES9RL9TnIR%2BLIDKef%2FqplLlphy84vGe0OnezdWQ9dkWOzwfS9cZUtP3yn%2FV5t6%2BReiQC5PH8aLW5A6lEBGEbpEDQNXKNYtWmL9l2D1ggThcqm9zMs7fjIuemKfCjAaQw3pE%2BlN1atnElef0244leyxicHM6OQLL0u%2Ff9Xf82lv%2FqU%2FWjVv0H4woXmsmozekdOO9MBgW3E54NahI9pRbnLvOf6Y%2BwmU&X-Amz-Signature=c89544e2238f9817ab98ef31b0b1fc9869004beec8dc953d0b9a1b31699331a5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAGA5F6N%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUQ9cbbrFgkxK0ez5yUnf1F6pa5hZdOirOMlcPHSI0nAiAqFj2WwS6EJhBSrsdOUunprxO3ll3URwG%2BdVgVvWjZ1yr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIManoIoapPkXRjqgltKtwDdm9tqtZUjw206ZxTcLQsUcnKZHhRT63G2Yk7ta32GD4uDBT2Ce86RLqJy0DJUSUU4ZG5kVqDk4PwiPDMLZNDqlKx%2BrNkmbztJYkaDbtjGJAFmYfz03lfaXqr8y5O68dsXStV4UzeQlpsdpeMPGnmSxYhXXnjMECWjT7XHH2%2FVx4o7Jq1KQl1KzYZeMKxi9AQihYPmRrwdU3qPCqZa%2Fb7Z1InRctvS%2FsKWxUpIKzxE7XMuNY0Nn3Ars40XPJtGhXfpKEwYg3rBVdvYou9vBr3Ik0NgaoZVd9rYVZz%2FHRCjw%2FNl6FG6j3nAumk34%2Bbhtx83%2FK34bEdlan4v21rhuNG0PFb5MaKKDQHfvnY2EDFsRE3FfX%2FFLuSksEjgXlOQwmQ%2B6AEM%2BjZf%2FQ4sLJf4Xkvxb7QcKDo8hNY0z1nmekW9Yzjyiz0mCioQW0zplgkJircsOeeb%2FDMXOmzJGN6o36idxMv9ExO%2BxW60OQ%2BmeWWbKBnyGj0AtZOc2RkKIONJL80CpQ4LagpODhJKb8VKY%2FAyqIBSXpznCsrCuuCZY%2F4IEajZKE0EQZXDyiYPEcGM9Kf3x07kY5PwOl0s5JEiJoLF82%2FGcYXLvSOEKDXmR9E6NDJAm6k8AeOYShfnacwzZzYvgY6pgES9RL9TnIR%2BLIDKef%2FqplLlphy84vGe0OnezdWQ9dkWOzwfS9cZUtP3yn%2FV5t6%2BReiQC5PH8aLW5A6lEBGEbpEDQNXKNYtWmL9l2D1ggThcqm9zMs7fjIuemKfCjAaQw3pE%2BlN1atnElef0244leyxicHM6OQLL0u%2Ff9Xf82lv%2FqU%2FWjVv0H4woXmsmozekdOO9MBgW3E54NahI9pRbnLvOf6Y%2BwmU&X-Amz-Signature=05c1ce935ed049ef84d1afda84463f524bd6348e652aaaf1b777ddd6aa453333&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAGA5F6N%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUQ9cbbrFgkxK0ez5yUnf1F6pa5hZdOirOMlcPHSI0nAiAqFj2WwS6EJhBSrsdOUunprxO3ll3URwG%2BdVgVvWjZ1yr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIManoIoapPkXRjqgltKtwDdm9tqtZUjw206ZxTcLQsUcnKZHhRT63G2Yk7ta32GD4uDBT2Ce86RLqJy0DJUSUU4ZG5kVqDk4PwiPDMLZNDqlKx%2BrNkmbztJYkaDbtjGJAFmYfz03lfaXqr8y5O68dsXStV4UzeQlpsdpeMPGnmSxYhXXnjMECWjT7XHH2%2FVx4o7Jq1KQl1KzYZeMKxi9AQihYPmRrwdU3qPCqZa%2Fb7Z1InRctvS%2FsKWxUpIKzxE7XMuNY0Nn3Ars40XPJtGhXfpKEwYg3rBVdvYou9vBr3Ik0NgaoZVd9rYVZz%2FHRCjw%2FNl6FG6j3nAumk34%2Bbhtx83%2FK34bEdlan4v21rhuNG0PFb5MaKKDQHfvnY2EDFsRE3FfX%2FFLuSksEjgXlOQwmQ%2B6AEM%2BjZf%2FQ4sLJf4Xkvxb7QcKDo8hNY0z1nmekW9Yzjyiz0mCioQW0zplgkJircsOeeb%2FDMXOmzJGN6o36idxMv9ExO%2BxW60OQ%2BmeWWbKBnyGj0AtZOc2RkKIONJL80CpQ4LagpODhJKb8VKY%2FAyqIBSXpznCsrCuuCZY%2F4IEajZKE0EQZXDyiYPEcGM9Kf3x07kY5PwOl0s5JEiJoLF82%2FGcYXLvSOEKDXmR9E6NDJAm6k8AeOYShfnacwzZzYvgY6pgES9RL9TnIR%2BLIDKef%2FqplLlphy84vGe0OnezdWQ9dkWOzwfS9cZUtP3yn%2FV5t6%2BReiQC5PH8aLW5A6lEBGEbpEDQNXKNYtWmL9l2D1ggThcqm9zMs7fjIuemKfCjAaQw3pE%2BlN1atnElef0244leyxicHM6OQLL0u%2Ff9Xf82lv%2FqU%2FWjVv0H4woXmsmozekdOO9MBgW3E54NahI9pRbnLvOf6Y%2BwmU&X-Amz-Signature=ae22d2102d0be2eb08cf11093f3c24295b59807ddc840a9a27fee570a3ab40e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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


