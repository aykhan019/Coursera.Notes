

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3QUIOUY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzZvVwoNYY9snejzrs%2Fx9iPvqqH08F%2BnwPC72ec186oQIhAPSeAuVZhMQV7Q%2F1G3BuaSJVJkOl1VDmrLUc6usJAqIZKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwHAWdb7Aiusqb7zMq3ANUC%2BwC9AZ1Dtti75UJEb%2Bb1CAjU2UjDbuWbYe2gbLI2jiM24H6nwWt0f4%2F3cpKa4JCxZ9QqklUhSzugONoi8hmWJUCUKlmg2GK5%2B81Jho0wurrKb0Ybjoy6%2BVGgRvI276ro34TCoS2T5A4NFLLyFHC7OAJymh9gjmUHIvfyrJS%2Fs72H3VlnE704BEhX4LbHjN9DR2x3OklW1TWJf%2BuPFN6sGWABWSL%2B5LPNylfCa2ZV5UDsn3vTuyVeBpqPU20gDbw%2BQXr7ct4dkR0qx0toECPiOfIaZ6upvEyTyQkisF2QCMylRYcTwrJqP1D%2F5w915sN7hBQ4au%2BE8T2fzJwJQLFhdWQyFrhw9SOvXtPdrsbcyYw875V36hKUWG3SNuGym5mVYaf7PyO2hp2behhj7mJdTDH9KUm2iQYaiLk6eRvwvgcI6ehYv5ZJFXjHnPzvatyatS9lHTTtmQYRLH9hXr61T0TBau4uh%2BGalfG5K7bLjjMyzwRWjC5W6goO4gSY%2FnlY5szoZLeYaSRqiccpNbX%2Fnz5d2ob94DnMms8jYLX304K%2BLRkmArq9l5iDe%2B0hAqUIj43m9rdyAS3QlJIxTZrgDm%2F6vICM6X1vesQsdA%2BxtMPV8WfsXyjBXPdrDDG0PC8BjqkAcXQcxF8FxoE7mGWv%2FDwy3VKc57%2BnDBcrPf%2ByhLjkAJHLS7c%2FJXh83XWzHTZzISZPbznxZUC6Nf4QpiV%2B8EKhsw1psGbH6zfu%2FF0UZLNT1W00UhE8I55uvPWEL8AXr%2FHNwd2adpJpA1qqRK8yI3t59r8bMuu8NuluR2OVA86A4GQoaC1fm8wP297PfruIAqS6BWJ2RobxhSbV3Naq6ldtX2Jt%2Fsb&X-Amz-Signature=9d760bac3e9bf846eaac133006fe2a3e8bb7f1169bfdc25f7889e47216700b23&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXQSNTKJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3AadZInWRxDT9mWuhTGW8WOqMFQzy6RxYgMVsifYJSAiEAlIqadNCZHp4iBA%2FxNj9ZF%2B7tz5eH%2Bg0wBymKlvGeSjkqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNrd3x7vezWOygeVZircA%2BkYnp%2BuNu%2FU2GWHBTGvNqYrQZABnqXWzVWyhbsfyhSpmqAZV7GBkTmJYhBLatHA5w0g7S%2FT1xsvH6D2BsN61alcmR89KoiBpRrNO6IxPJ4rMDX7b%2BYQ2HY4HlR3xBmCpNxaIhrJMhDVhfoPWxVln%2FOF6%2FOx5c3%2F6oCJhP0NwgZgh%2FdLFN%2BIcMJNZsiAGOhy9CvxQpM2y1v5ou9pbacF5zVchSt1qNTk49k4kFlQUW6N4l1DFTLVKxHj6sVgBqgbkUAhKU%2FUu3M%2F75ogcwFqVTxW6LX3JWrqdp5oA5GnbIw6Dv7VtlMqncnk5y8UckMpsA845xDnGLwOqY9iVR%2BhCbXZjXh0HPHA5vk%2BpswGUU%2ByWjTAyR0WsnV%2FXuAPpRKOZLK%2FsIVSVDzcFWU%2BW3QmmWcU24Dbv72jkHnR9dQQ%2BIgJSXTZI8NcbK9Gok%2BLGb0oP0YT3WUFhnnA9G9H%2FioE%2FGZYVUGIDHrM4nXd7PUxBTakhHPJduTLo5YAStx%2FHVHM67mPgjbLTjAoz0DhO78ebQcWw1FX80Bjgj3G%2F4Wcs0TwaEBr8zaSFF3kl7bKY9s%2B%2FxeeZX6xgX%2BifcMypXYR8MLi81ekO1KB0EizoM4J30rsLO9moMLlT09l%2BFkKMMbQ8LwGOqUB1XO5DOmFXb9HO3kK43lyE4RMZrfoez3R6kL5pmJogPFhzHPIXZ3hKGfaKBgDKReYxypWWBwrw86RSapMTFsyfGuSd6XBhrSCzBDzCsWHfUvAIZBKe3QyyMPNjLTmoebQ%2FKYrhQxYCSNv1jIlIugigJLap92HUIq51Ku3MaOv%2FpziNdhQvmzcou8ygPFFsTCoWVFffM3cD12W984rgcy9ug1YoTv7&X-Amz-Signature=1a72c1b0c755a555391b1e42b860ee9a7ae4f1390a3dad1845e09a936ee23216&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXQSNTKJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3AadZInWRxDT9mWuhTGW8WOqMFQzy6RxYgMVsifYJSAiEAlIqadNCZHp4iBA%2FxNj9ZF%2B7tz5eH%2Bg0wBymKlvGeSjkqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNrd3x7vezWOygeVZircA%2BkYnp%2BuNu%2FU2GWHBTGvNqYrQZABnqXWzVWyhbsfyhSpmqAZV7GBkTmJYhBLatHA5w0g7S%2FT1xsvH6D2BsN61alcmR89KoiBpRrNO6IxPJ4rMDX7b%2BYQ2HY4HlR3xBmCpNxaIhrJMhDVhfoPWxVln%2FOF6%2FOx5c3%2F6oCJhP0NwgZgh%2FdLFN%2BIcMJNZsiAGOhy9CvxQpM2y1v5ou9pbacF5zVchSt1qNTk49k4kFlQUW6N4l1DFTLVKxHj6sVgBqgbkUAhKU%2FUu3M%2F75ogcwFqVTxW6LX3JWrqdp5oA5GnbIw6Dv7VtlMqncnk5y8UckMpsA845xDnGLwOqY9iVR%2BhCbXZjXh0HPHA5vk%2BpswGUU%2ByWjTAyR0WsnV%2FXuAPpRKOZLK%2FsIVSVDzcFWU%2BW3QmmWcU24Dbv72jkHnR9dQQ%2BIgJSXTZI8NcbK9Gok%2BLGb0oP0YT3WUFhnnA9G9H%2FioE%2FGZYVUGIDHrM4nXd7PUxBTakhHPJduTLo5YAStx%2FHVHM67mPgjbLTjAoz0DhO78ebQcWw1FX80Bjgj3G%2F4Wcs0TwaEBr8zaSFF3kl7bKY9s%2B%2FxeeZX6xgX%2BifcMypXYR8MLi81ekO1KB0EizoM4J30rsLO9moMLlT09l%2BFkKMMbQ8LwGOqUB1XO5DOmFXb9HO3kK43lyE4RMZrfoez3R6kL5pmJogPFhzHPIXZ3hKGfaKBgDKReYxypWWBwrw86RSapMTFsyfGuSd6XBhrSCzBDzCsWHfUvAIZBKe3QyyMPNjLTmoebQ%2FKYrhQxYCSNv1jIlIugigJLap92HUIq51Ku3MaOv%2FpziNdhQvmzcou8ygPFFsTCoWVFffM3cD12W984rgcy9ug1YoTv7&X-Amz-Signature=fd3e9b236d4ae6f227b2961d418b6eeb1ab52dd7349ef8f29838a53c7f60f918&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXQSNTKJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3AadZInWRxDT9mWuhTGW8WOqMFQzy6RxYgMVsifYJSAiEAlIqadNCZHp4iBA%2FxNj9ZF%2B7tz5eH%2Bg0wBymKlvGeSjkqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNrd3x7vezWOygeVZircA%2BkYnp%2BuNu%2FU2GWHBTGvNqYrQZABnqXWzVWyhbsfyhSpmqAZV7GBkTmJYhBLatHA5w0g7S%2FT1xsvH6D2BsN61alcmR89KoiBpRrNO6IxPJ4rMDX7b%2BYQ2HY4HlR3xBmCpNxaIhrJMhDVhfoPWxVln%2FOF6%2FOx5c3%2F6oCJhP0NwgZgh%2FdLFN%2BIcMJNZsiAGOhy9CvxQpM2y1v5ou9pbacF5zVchSt1qNTk49k4kFlQUW6N4l1DFTLVKxHj6sVgBqgbkUAhKU%2FUu3M%2F75ogcwFqVTxW6LX3JWrqdp5oA5GnbIw6Dv7VtlMqncnk5y8UckMpsA845xDnGLwOqY9iVR%2BhCbXZjXh0HPHA5vk%2BpswGUU%2ByWjTAyR0WsnV%2FXuAPpRKOZLK%2FsIVSVDzcFWU%2BW3QmmWcU24Dbv72jkHnR9dQQ%2BIgJSXTZI8NcbK9Gok%2BLGb0oP0YT3WUFhnnA9G9H%2FioE%2FGZYVUGIDHrM4nXd7PUxBTakhHPJduTLo5YAStx%2FHVHM67mPgjbLTjAoz0DhO78ebQcWw1FX80Bjgj3G%2F4Wcs0TwaEBr8zaSFF3kl7bKY9s%2B%2FxeeZX6xgX%2BifcMypXYR8MLi81ekO1KB0EizoM4J30rsLO9moMLlT09l%2BFkKMMbQ8LwGOqUB1XO5DOmFXb9HO3kK43lyE4RMZrfoez3R6kL5pmJogPFhzHPIXZ3hKGfaKBgDKReYxypWWBwrw86RSapMTFsyfGuSd6XBhrSCzBDzCsWHfUvAIZBKe3QyyMPNjLTmoebQ%2FKYrhQxYCSNv1jIlIugigJLap92HUIq51Ku3MaOv%2FpziNdhQvmzcou8ygPFFsTCoWVFffM3cD12W984rgcy9ug1YoTv7&X-Amz-Signature=350e2bb2f6e3c0aa7536c2953d6fc71c4db544f84c35c5a5b3aedd922e88d428&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXQSNTKJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3AadZInWRxDT9mWuhTGW8WOqMFQzy6RxYgMVsifYJSAiEAlIqadNCZHp4iBA%2FxNj9ZF%2B7tz5eH%2Bg0wBymKlvGeSjkqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNrd3x7vezWOygeVZircA%2BkYnp%2BuNu%2FU2GWHBTGvNqYrQZABnqXWzVWyhbsfyhSpmqAZV7GBkTmJYhBLatHA5w0g7S%2FT1xsvH6D2BsN61alcmR89KoiBpRrNO6IxPJ4rMDX7b%2BYQ2HY4HlR3xBmCpNxaIhrJMhDVhfoPWxVln%2FOF6%2FOx5c3%2F6oCJhP0NwgZgh%2FdLFN%2BIcMJNZsiAGOhy9CvxQpM2y1v5ou9pbacF5zVchSt1qNTk49k4kFlQUW6N4l1DFTLVKxHj6sVgBqgbkUAhKU%2FUu3M%2F75ogcwFqVTxW6LX3JWrqdp5oA5GnbIw6Dv7VtlMqncnk5y8UckMpsA845xDnGLwOqY9iVR%2BhCbXZjXh0HPHA5vk%2BpswGUU%2ByWjTAyR0WsnV%2FXuAPpRKOZLK%2FsIVSVDzcFWU%2BW3QmmWcU24Dbv72jkHnR9dQQ%2BIgJSXTZI8NcbK9Gok%2BLGb0oP0YT3WUFhnnA9G9H%2FioE%2FGZYVUGIDHrM4nXd7PUxBTakhHPJduTLo5YAStx%2FHVHM67mPgjbLTjAoz0DhO78ebQcWw1FX80Bjgj3G%2F4Wcs0TwaEBr8zaSFF3kl7bKY9s%2B%2FxeeZX6xgX%2BifcMypXYR8MLi81ekO1KB0EizoM4J30rsLO9moMLlT09l%2BFkKMMbQ8LwGOqUB1XO5DOmFXb9HO3kK43lyE4RMZrfoez3R6kL5pmJogPFhzHPIXZ3hKGfaKBgDKReYxypWWBwrw86RSapMTFsyfGuSd6XBhrSCzBDzCsWHfUvAIZBKe3QyyMPNjLTmoebQ%2FKYrhQxYCSNv1jIlIugigJLap92HUIq51Ku3MaOv%2FpziNdhQvmzcou8ygPFFsTCoWVFffM3cD12W984rgcy9ug1YoTv7&X-Amz-Signature=14893a661e38cc039b449e474f0748406d78b476588e84aad1e853f7cc709146&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXQSNTKJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3AadZInWRxDT9mWuhTGW8WOqMFQzy6RxYgMVsifYJSAiEAlIqadNCZHp4iBA%2FxNj9ZF%2B7tz5eH%2Bg0wBymKlvGeSjkqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNrd3x7vezWOygeVZircA%2BkYnp%2BuNu%2FU2GWHBTGvNqYrQZABnqXWzVWyhbsfyhSpmqAZV7GBkTmJYhBLatHA5w0g7S%2FT1xsvH6D2BsN61alcmR89KoiBpRrNO6IxPJ4rMDX7b%2BYQ2HY4HlR3xBmCpNxaIhrJMhDVhfoPWxVln%2FOF6%2FOx5c3%2F6oCJhP0NwgZgh%2FdLFN%2BIcMJNZsiAGOhy9CvxQpM2y1v5ou9pbacF5zVchSt1qNTk49k4kFlQUW6N4l1DFTLVKxHj6sVgBqgbkUAhKU%2FUu3M%2F75ogcwFqVTxW6LX3JWrqdp5oA5GnbIw6Dv7VtlMqncnk5y8UckMpsA845xDnGLwOqY9iVR%2BhCbXZjXh0HPHA5vk%2BpswGUU%2ByWjTAyR0WsnV%2FXuAPpRKOZLK%2FsIVSVDzcFWU%2BW3QmmWcU24Dbv72jkHnR9dQQ%2BIgJSXTZI8NcbK9Gok%2BLGb0oP0YT3WUFhnnA9G9H%2FioE%2FGZYVUGIDHrM4nXd7PUxBTakhHPJduTLo5YAStx%2FHVHM67mPgjbLTjAoz0DhO78ebQcWw1FX80Bjgj3G%2F4Wcs0TwaEBr8zaSFF3kl7bKY9s%2B%2FxeeZX6xgX%2BifcMypXYR8MLi81ekO1KB0EizoM4J30rsLO9moMLlT09l%2BFkKMMbQ8LwGOqUB1XO5DOmFXb9HO3kK43lyE4RMZrfoez3R6kL5pmJogPFhzHPIXZ3hKGfaKBgDKReYxypWWBwrw86RSapMTFsyfGuSd6XBhrSCzBDzCsWHfUvAIZBKe3QyyMPNjLTmoebQ%2FKYrhQxYCSNv1jIlIugigJLap92HUIq51Ku3MaOv%2FpziNdhQvmzcou8ygPFFsTCoWVFffM3cD12W984rgcy9ug1YoTv7&X-Amz-Signature=06575ba61669ed2fb5429acd89ae0fe2e1b8f8f85d203361b87bc6954de16910&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3QUIOUY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzZvVwoNYY9snejzrs%2Fx9iPvqqH08F%2BnwPC72ec186oQIhAPSeAuVZhMQV7Q%2F1G3BuaSJVJkOl1VDmrLUc6usJAqIZKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwHAWdb7Aiusqb7zMq3ANUC%2BwC9AZ1Dtti75UJEb%2Bb1CAjU2UjDbuWbYe2gbLI2jiM24H6nwWt0f4%2F3cpKa4JCxZ9QqklUhSzugONoi8hmWJUCUKlmg2GK5%2B81Jho0wurrKb0Ybjoy6%2BVGgRvI276ro34TCoS2T5A4NFLLyFHC7OAJymh9gjmUHIvfyrJS%2Fs72H3VlnE704BEhX4LbHjN9DR2x3OklW1TWJf%2BuPFN6sGWABWSL%2B5LPNylfCa2ZV5UDsn3vTuyVeBpqPU20gDbw%2BQXr7ct4dkR0qx0toECPiOfIaZ6upvEyTyQkisF2QCMylRYcTwrJqP1D%2F5w915sN7hBQ4au%2BE8T2fzJwJQLFhdWQyFrhw9SOvXtPdrsbcyYw875V36hKUWG3SNuGym5mVYaf7PyO2hp2behhj7mJdTDH9KUm2iQYaiLk6eRvwvgcI6ehYv5ZJFXjHnPzvatyatS9lHTTtmQYRLH9hXr61T0TBau4uh%2BGalfG5K7bLjjMyzwRWjC5W6goO4gSY%2FnlY5szoZLeYaSRqiccpNbX%2Fnz5d2ob94DnMms8jYLX304K%2BLRkmArq9l5iDe%2B0hAqUIj43m9rdyAS3QlJIxTZrgDm%2F6vICM6X1vesQsdA%2BxtMPV8WfsXyjBXPdrDDG0PC8BjqkAcXQcxF8FxoE7mGWv%2FDwy3VKc57%2BnDBcrPf%2ByhLjkAJHLS7c%2FJXh83XWzHTZzISZPbznxZUC6Nf4QpiV%2B8EKhsw1psGbH6zfu%2FF0UZLNT1W00UhE8I55uvPWEL8AXr%2FHNwd2adpJpA1qqRK8yI3t59r8bMuu8NuluR2OVA86A4GQoaC1fm8wP297PfruIAqS6BWJ2RobxhSbV3Naq6ldtX2Jt%2Fsb&X-Amz-Signature=f9100b69f71c5d3b6bb9f34df134c96f449cea356b8463215acc3a698eb63b17&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3QUIOUY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzZvVwoNYY9snejzrs%2Fx9iPvqqH08F%2BnwPC72ec186oQIhAPSeAuVZhMQV7Q%2F1G3BuaSJVJkOl1VDmrLUc6usJAqIZKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwHAWdb7Aiusqb7zMq3ANUC%2BwC9AZ1Dtti75UJEb%2Bb1CAjU2UjDbuWbYe2gbLI2jiM24H6nwWt0f4%2F3cpKa4JCxZ9QqklUhSzugONoi8hmWJUCUKlmg2GK5%2B81Jho0wurrKb0Ybjoy6%2BVGgRvI276ro34TCoS2T5A4NFLLyFHC7OAJymh9gjmUHIvfyrJS%2Fs72H3VlnE704BEhX4LbHjN9DR2x3OklW1TWJf%2BuPFN6sGWABWSL%2B5LPNylfCa2ZV5UDsn3vTuyVeBpqPU20gDbw%2BQXr7ct4dkR0qx0toECPiOfIaZ6upvEyTyQkisF2QCMylRYcTwrJqP1D%2F5w915sN7hBQ4au%2BE8T2fzJwJQLFhdWQyFrhw9SOvXtPdrsbcyYw875V36hKUWG3SNuGym5mVYaf7PyO2hp2behhj7mJdTDH9KUm2iQYaiLk6eRvwvgcI6ehYv5ZJFXjHnPzvatyatS9lHTTtmQYRLH9hXr61T0TBau4uh%2BGalfG5K7bLjjMyzwRWjC5W6goO4gSY%2FnlY5szoZLeYaSRqiccpNbX%2Fnz5d2ob94DnMms8jYLX304K%2BLRkmArq9l5iDe%2B0hAqUIj43m9rdyAS3QlJIxTZrgDm%2F6vICM6X1vesQsdA%2BxtMPV8WfsXyjBXPdrDDG0PC8BjqkAcXQcxF8FxoE7mGWv%2FDwy3VKc57%2BnDBcrPf%2ByhLjkAJHLS7c%2FJXh83XWzHTZzISZPbznxZUC6Nf4QpiV%2B8EKhsw1psGbH6zfu%2FF0UZLNT1W00UhE8I55uvPWEL8AXr%2FHNwd2adpJpA1qqRK8yI3t59r8bMuu8NuluR2OVA86A4GQoaC1fm8wP297PfruIAqS6BWJ2RobxhSbV3Naq6ldtX2Jt%2Fsb&X-Amz-Signature=b0bab02f85f86293d27fba33cb12434e5ff03ca1333067fd49132cd1a83e2ecf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3QUIOUY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzZvVwoNYY9snejzrs%2Fx9iPvqqH08F%2BnwPC72ec186oQIhAPSeAuVZhMQV7Q%2F1G3BuaSJVJkOl1VDmrLUc6usJAqIZKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwHAWdb7Aiusqb7zMq3ANUC%2BwC9AZ1Dtti75UJEb%2Bb1CAjU2UjDbuWbYe2gbLI2jiM24H6nwWt0f4%2F3cpKa4JCxZ9QqklUhSzugONoi8hmWJUCUKlmg2GK5%2B81Jho0wurrKb0Ybjoy6%2BVGgRvI276ro34TCoS2T5A4NFLLyFHC7OAJymh9gjmUHIvfyrJS%2Fs72H3VlnE704BEhX4LbHjN9DR2x3OklW1TWJf%2BuPFN6sGWABWSL%2B5LPNylfCa2ZV5UDsn3vTuyVeBpqPU20gDbw%2BQXr7ct4dkR0qx0toECPiOfIaZ6upvEyTyQkisF2QCMylRYcTwrJqP1D%2F5w915sN7hBQ4au%2BE8T2fzJwJQLFhdWQyFrhw9SOvXtPdrsbcyYw875V36hKUWG3SNuGym5mVYaf7PyO2hp2behhj7mJdTDH9KUm2iQYaiLk6eRvwvgcI6ehYv5ZJFXjHnPzvatyatS9lHTTtmQYRLH9hXr61T0TBau4uh%2BGalfG5K7bLjjMyzwRWjC5W6goO4gSY%2FnlY5szoZLeYaSRqiccpNbX%2Fnz5d2ob94DnMms8jYLX304K%2BLRkmArq9l5iDe%2B0hAqUIj43m9rdyAS3QlJIxTZrgDm%2F6vICM6X1vesQsdA%2BxtMPV8WfsXyjBXPdrDDG0PC8BjqkAcXQcxF8FxoE7mGWv%2FDwy3VKc57%2BnDBcrPf%2ByhLjkAJHLS7c%2FJXh83XWzHTZzISZPbznxZUC6Nf4QpiV%2B8EKhsw1psGbH6zfu%2FF0UZLNT1W00UhE8I55uvPWEL8AXr%2FHNwd2adpJpA1qqRK8yI3t59r8bMuu8NuluR2OVA86A4GQoaC1fm8wP297PfruIAqS6BWJ2RobxhSbV3Naq6ldtX2Jt%2Fsb&X-Amz-Signature=a6eca5057e997a874468cd5587acc7a1f447afa8e76aaafd059a6e9fc14ca9a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3QUIOUY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzZvVwoNYY9snejzrs%2Fx9iPvqqH08F%2BnwPC72ec186oQIhAPSeAuVZhMQV7Q%2F1G3BuaSJVJkOl1VDmrLUc6usJAqIZKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwHAWdb7Aiusqb7zMq3ANUC%2BwC9AZ1Dtti75UJEb%2Bb1CAjU2UjDbuWbYe2gbLI2jiM24H6nwWt0f4%2F3cpKa4JCxZ9QqklUhSzugONoi8hmWJUCUKlmg2GK5%2B81Jho0wurrKb0Ybjoy6%2BVGgRvI276ro34TCoS2T5A4NFLLyFHC7OAJymh9gjmUHIvfyrJS%2Fs72H3VlnE704BEhX4LbHjN9DR2x3OklW1TWJf%2BuPFN6sGWABWSL%2B5LPNylfCa2ZV5UDsn3vTuyVeBpqPU20gDbw%2BQXr7ct4dkR0qx0toECPiOfIaZ6upvEyTyQkisF2QCMylRYcTwrJqP1D%2F5w915sN7hBQ4au%2BE8T2fzJwJQLFhdWQyFrhw9SOvXtPdrsbcyYw875V36hKUWG3SNuGym5mVYaf7PyO2hp2behhj7mJdTDH9KUm2iQYaiLk6eRvwvgcI6ehYv5ZJFXjHnPzvatyatS9lHTTtmQYRLH9hXr61T0TBau4uh%2BGalfG5K7bLjjMyzwRWjC5W6goO4gSY%2FnlY5szoZLeYaSRqiccpNbX%2Fnz5d2ob94DnMms8jYLX304K%2BLRkmArq9l5iDe%2B0hAqUIj43m9rdyAS3QlJIxTZrgDm%2F6vICM6X1vesQsdA%2BxtMPV8WfsXyjBXPdrDDG0PC8BjqkAcXQcxF8FxoE7mGWv%2FDwy3VKc57%2BnDBcrPf%2ByhLjkAJHLS7c%2FJXh83XWzHTZzISZPbznxZUC6Nf4QpiV%2B8EKhsw1psGbH6zfu%2FF0UZLNT1W00UhE8I55uvPWEL8AXr%2FHNwd2adpJpA1qqRK8yI3t59r8bMuu8NuluR2OVA86A4GQoaC1fm8wP297PfruIAqS6BWJ2RobxhSbV3Naq6ldtX2Jt%2Fsb&X-Amz-Signature=fe5b916919a3d3be90209bf56be0b4fe7b9fe663d756767e91f0557b26a6e783&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3QUIOUY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzZvVwoNYY9snejzrs%2Fx9iPvqqH08F%2BnwPC72ec186oQIhAPSeAuVZhMQV7Q%2F1G3BuaSJVJkOl1VDmrLUc6usJAqIZKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwHAWdb7Aiusqb7zMq3ANUC%2BwC9AZ1Dtti75UJEb%2Bb1CAjU2UjDbuWbYe2gbLI2jiM24H6nwWt0f4%2F3cpKa4JCxZ9QqklUhSzugONoi8hmWJUCUKlmg2GK5%2B81Jho0wurrKb0Ybjoy6%2BVGgRvI276ro34TCoS2T5A4NFLLyFHC7OAJymh9gjmUHIvfyrJS%2Fs72H3VlnE704BEhX4LbHjN9DR2x3OklW1TWJf%2BuPFN6sGWABWSL%2B5LPNylfCa2ZV5UDsn3vTuyVeBpqPU20gDbw%2BQXr7ct4dkR0qx0toECPiOfIaZ6upvEyTyQkisF2QCMylRYcTwrJqP1D%2F5w915sN7hBQ4au%2BE8T2fzJwJQLFhdWQyFrhw9SOvXtPdrsbcyYw875V36hKUWG3SNuGym5mVYaf7PyO2hp2behhj7mJdTDH9KUm2iQYaiLk6eRvwvgcI6ehYv5ZJFXjHnPzvatyatS9lHTTtmQYRLH9hXr61T0TBau4uh%2BGalfG5K7bLjjMyzwRWjC5W6goO4gSY%2FnlY5szoZLeYaSRqiccpNbX%2Fnz5d2ob94DnMms8jYLX304K%2BLRkmArq9l5iDe%2B0hAqUIj43m9rdyAS3QlJIxTZrgDm%2F6vICM6X1vesQsdA%2BxtMPV8WfsXyjBXPdrDDG0PC8BjqkAcXQcxF8FxoE7mGWv%2FDwy3VKc57%2BnDBcrPf%2ByhLjkAJHLS7c%2FJXh83XWzHTZzISZPbznxZUC6Nf4QpiV%2B8EKhsw1psGbH6zfu%2FF0UZLNT1W00UhE8I55uvPWEL8AXr%2FHNwd2adpJpA1qqRK8yI3t59r8bMuu8NuluR2OVA86A4GQoaC1fm8wP297PfruIAqS6BWJ2RobxhSbV3Naq6ldtX2Jt%2Fsb&X-Amz-Signature=dce4e8f81963c012e6b21680b060774221c2a31e30f916cf2d498d6933d88e5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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


