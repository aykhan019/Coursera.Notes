

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQAUWPRC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIEaXzr8xXGiJG9wn6qMWUulUTZI2K0u%2F1GaE7bL20coGAiEAhUtKscfTvhx9GI89CIJi2uy2CG8kEu4IGYICm2xsWZ4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNs6wl1pJ8Vw3J0KyCrcA6vq0oEoeYUXjj0sIwVI1Awd7o2ucT26Vk5dqdl7B9waw8gQg12g%2BzClnRRgFTIBEzukB8Db49ko3FYLM1dQ%2FA1ggxDNLf3Cqi3xb0gizLfND6%2B8rFxG0zJxd8u6H2cI%2B%2BiJy232gnB6YMmEP3I2%2Bs3K7ePN%2BsQ1kEOzehFK5mLMh0feKnhaPq2lrAk1PBAeULWqVSHqdGr7NETgrrd4jOxFd6xglqdNfxfeoL5atG163Zb4yGTVamQ2U5i129khz%2FSiCPHy0gmuWzxO%2BlggzP95yDMPwfe%2BAaHcFKxAnEvwSs0guANhah306vJSrA%2BjqXMScK7esjNoVyRP7jH1yC8aqrcHpniUX2z0gR120rKhYpc4upV3JjhV1hkLZIJ2Vyxm1XjZmlqCRNl%2BJTAx%2BnqTAsVLQY7n%2ByPl1pb6QORN1n7DsIYVeQ8CDCiBWGsHxnyv%2Fcxf8Srvj%2FQBcSnZK6E976U9ep9Y66a9Iq7%2B0IWQP4YoHzyNTytbbzhUNn86%2Fgas%2Fn0bjUTxUY46vh0T9wJkMUKdr0pD21raIys7y8QBxcBLjLsBA9WIM40RrYEodkt4I2JG7phQP0FTy8tLz4d8el5yM91bCg6csbvLZj6wAxmgoMFeVhXafL7FMLeihL0GOqUBR0oLlONGNY5Hi%2Fn49G3hcHgKLT7RRu3xwFMEHbX3cnY7HfpEWRDScR5rJ6MiD0HjeJ7IP9BFr86x%2FijKABWqHa9899MXTdkpaoS6t1Y9zZVmmvOJd8xoIqJi2gUtFJlmfVO9zVriec%2BE%2FtyVMrDGZdaZgW7QvukzkVx1PHl5P3gONOSBd9dPuRsllT75r0r9YNNZp0E%2FOrFshVCWJXnH47HeV14E&X-Amz-Signature=6bc7fd124605673fe425433989ad2fab51e09b246ee712e02dbfa20d1778ac9e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SFDKLTT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDd%2BAfIJ%2Fur8JR4jKk5zsKwW9A1gSJNWR%2Fzm%2BZB%2F%2F%2B9OAIhAIp%2FOet%2BV%2BitZMl1B58GRqJSP27sP3tpje498KTkDt2iKv8DCBwQABoMNjM3NDIzMTgzODA1Igy8FmCaQfKJNGvO%2BhQq3ANehxuQ%2F7%2FjAeShL9zQCQq3iTKTLdqLeoaHPD%2FQS6TG8XFMI8EaIkioOwN8vRARERzUVyHpeWduBBqUNYSsk%2B5mqD9eoY5I1lL%2BjMbiaBcKuDPI%2FbG%2F0aEOUzA3X5a2AzYdIvnui3xPL66s309BqOjBj%2FI377kUixhGJSvCcpeKtYfvvowgYHu6Xk5jpUzLNrLwzRxHLB1UxhGMKuDmWw7X4tuxgcoapGykqt4dEM%2BIGz0%2FVKyIOeBt1ZpCrOzx1jSvbKTfPM5UQ4vGPw%2F8j%2Fxwclwr48PwcaX9z6EiAsXdl%2BBjidjEeJ4p64YEfP4OBwrdclZdHybd5ffQTcwTh2J8Q4EzGeAKynJ4%2FEJfdxuH6cmKbAXYLTUJLtdrKIGUz8ywTpS2yVeIR7U98VlcmqJ2UQLStqClSHjgs%2FArEOobHkMdGdS%2BDXFH7Hn0uDaVc1LKl7j49iH3xNbCBO8PHE3rHY9IZ%2B8yJLNjDpx%2FVYPFKNNfwkJeFwMJg1D1Ez0Qps0lpKbSsfeyVEUjT6HVXD9K9Xn2P66%2FOeHtIRCGCNCSJeQcyeGV0edXOxpOqxy5dvi9NEPJgz6iq0kARuR4HpUvtPDLdg8jKAp9YErWUa9vGROz6fzy8XjKSPJjcDDhoIS9BjqkAXw8dpinP1VY7KwXF1fQZiSx7DBFtNDZlZGaZsJpTpEb5gyxwib0vvVitVBe1lYw6orY0jVPfE8841XxUGZUGtIP%2FxyNtnKldXfSMrMYfIUQG%2FMYrC5N3Y0k2a4bKOn7fHPxN0s0WafR7A0wKR4o3ydoCLKuOECBKTjmjumZcoMnAVMpNImc5wHfR1fYrvqSIWDVAiP49lt6cmars8VEoJhODcpb&X-Amz-Signature=832f45afccb1b71579c737f116a1c529e31ab4691151cd8b6c7f0c3a98a9949c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SFDKLTT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDd%2BAfIJ%2Fur8JR4jKk5zsKwW9A1gSJNWR%2Fzm%2BZB%2F%2F%2B9OAIhAIp%2FOet%2BV%2BitZMl1B58GRqJSP27sP3tpje498KTkDt2iKv8DCBwQABoMNjM3NDIzMTgzODA1Igy8FmCaQfKJNGvO%2BhQq3ANehxuQ%2F7%2FjAeShL9zQCQq3iTKTLdqLeoaHPD%2FQS6TG8XFMI8EaIkioOwN8vRARERzUVyHpeWduBBqUNYSsk%2B5mqD9eoY5I1lL%2BjMbiaBcKuDPI%2FbG%2F0aEOUzA3X5a2AzYdIvnui3xPL66s309BqOjBj%2FI377kUixhGJSvCcpeKtYfvvowgYHu6Xk5jpUzLNrLwzRxHLB1UxhGMKuDmWw7X4tuxgcoapGykqt4dEM%2BIGz0%2FVKyIOeBt1ZpCrOzx1jSvbKTfPM5UQ4vGPw%2F8j%2Fxwclwr48PwcaX9z6EiAsXdl%2BBjidjEeJ4p64YEfP4OBwrdclZdHybd5ffQTcwTh2J8Q4EzGeAKynJ4%2FEJfdxuH6cmKbAXYLTUJLtdrKIGUz8ywTpS2yVeIR7U98VlcmqJ2UQLStqClSHjgs%2FArEOobHkMdGdS%2BDXFH7Hn0uDaVc1LKl7j49iH3xNbCBO8PHE3rHY9IZ%2B8yJLNjDpx%2FVYPFKNNfwkJeFwMJg1D1Ez0Qps0lpKbSsfeyVEUjT6HVXD9K9Xn2P66%2FOeHtIRCGCNCSJeQcyeGV0edXOxpOqxy5dvi9NEPJgz6iq0kARuR4HpUvtPDLdg8jKAp9YErWUa9vGROz6fzy8XjKSPJjcDDhoIS9BjqkAXw8dpinP1VY7KwXF1fQZiSx7DBFtNDZlZGaZsJpTpEb5gyxwib0vvVitVBe1lYw6orY0jVPfE8841XxUGZUGtIP%2FxyNtnKldXfSMrMYfIUQG%2FMYrC5N3Y0k2a4bKOn7fHPxN0s0WafR7A0wKR4o3ydoCLKuOECBKTjmjumZcoMnAVMpNImc5wHfR1fYrvqSIWDVAiP49lt6cmars8VEoJhODcpb&X-Amz-Signature=d58696ca8b3113dce3e127552be2a950667eec6444926f7012c5554144e2c7ff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SFDKLTT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDd%2BAfIJ%2Fur8JR4jKk5zsKwW9A1gSJNWR%2Fzm%2BZB%2F%2F%2B9OAIhAIp%2FOet%2BV%2BitZMl1B58GRqJSP27sP3tpje498KTkDt2iKv8DCBwQABoMNjM3NDIzMTgzODA1Igy8FmCaQfKJNGvO%2BhQq3ANehxuQ%2F7%2FjAeShL9zQCQq3iTKTLdqLeoaHPD%2FQS6TG8XFMI8EaIkioOwN8vRARERzUVyHpeWduBBqUNYSsk%2B5mqD9eoY5I1lL%2BjMbiaBcKuDPI%2FbG%2F0aEOUzA3X5a2AzYdIvnui3xPL66s309BqOjBj%2FI377kUixhGJSvCcpeKtYfvvowgYHu6Xk5jpUzLNrLwzRxHLB1UxhGMKuDmWw7X4tuxgcoapGykqt4dEM%2BIGz0%2FVKyIOeBt1ZpCrOzx1jSvbKTfPM5UQ4vGPw%2F8j%2Fxwclwr48PwcaX9z6EiAsXdl%2BBjidjEeJ4p64YEfP4OBwrdclZdHybd5ffQTcwTh2J8Q4EzGeAKynJ4%2FEJfdxuH6cmKbAXYLTUJLtdrKIGUz8ywTpS2yVeIR7U98VlcmqJ2UQLStqClSHjgs%2FArEOobHkMdGdS%2BDXFH7Hn0uDaVc1LKl7j49iH3xNbCBO8PHE3rHY9IZ%2B8yJLNjDpx%2FVYPFKNNfwkJeFwMJg1D1Ez0Qps0lpKbSsfeyVEUjT6HVXD9K9Xn2P66%2FOeHtIRCGCNCSJeQcyeGV0edXOxpOqxy5dvi9NEPJgz6iq0kARuR4HpUvtPDLdg8jKAp9YErWUa9vGROz6fzy8XjKSPJjcDDhoIS9BjqkAXw8dpinP1VY7KwXF1fQZiSx7DBFtNDZlZGaZsJpTpEb5gyxwib0vvVitVBe1lYw6orY0jVPfE8841XxUGZUGtIP%2FxyNtnKldXfSMrMYfIUQG%2FMYrC5N3Y0k2a4bKOn7fHPxN0s0WafR7A0wKR4o3ydoCLKuOECBKTjmjumZcoMnAVMpNImc5wHfR1fYrvqSIWDVAiP49lt6cmars8VEoJhODcpb&X-Amz-Signature=85bcde9d0eb337e82dac3f12e9afbae9041cf9c59fdc00d501d297d5439f28b4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SFDKLTT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDd%2BAfIJ%2Fur8JR4jKk5zsKwW9A1gSJNWR%2Fzm%2BZB%2F%2F%2B9OAIhAIp%2FOet%2BV%2BitZMl1B58GRqJSP27sP3tpje498KTkDt2iKv8DCBwQABoMNjM3NDIzMTgzODA1Igy8FmCaQfKJNGvO%2BhQq3ANehxuQ%2F7%2FjAeShL9zQCQq3iTKTLdqLeoaHPD%2FQS6TG8XFMI8EaIkioOwN8vRARERzUVyHpeWduBBqUNYSsk%2B5mqD9eoY5I1lL%2BjMbiaBcKuDPI%2FbG%2F0aEOUzA3X5a2AzYdIvnui3xPL66s309BqOjBj%2FI377kUixhGJSvCcpeKtYfvvowgYHu6Xk5jpUzLNrLwzRxHLB1UxhGMKuDmWw7X4tuxgcoapGykqt4dEM%2BIGz0%2FVKyIOeBt1ZpCrOzx1jSvbKTfPM5UQ4vGPw%2F8j%2Fxwclwr48PwcaX9z6EiAsXdl%2BBjidjEeJ4p64YEfP4OBwrdclZdHybd5ffQTcwTh2J8Q4EzGeAKynJ4%2FEJfdxuH6cmKbAXYLTUJLtdrKIGUz8ywTpS2yVeIR7U98VlcmqJ2UQLStqClSHjgs%2FArEOobHkMdGdS%2BDXFH7Hn0uDaVc1LKl7j49iH3xNbCBO8PHE3rHY9IZ%2B8yJLNjDpx%2FVYPFKNNfwkJeFwMJg1D1Ez0Qps0lpKbSsfeyVEUjT6HVXD9K9Xn2P66%2FOeHtIRCGCNCSJeQcyeGV0edXOxpOqxy5dvi9NEPJgz6iq0kARuR4HpUvtPDLdg8jKAp9YErWUa9vGROz6fzy8XjKSPJjcDDhoIS9BjqkAXw8dpinP1VY7KwXF1fQZiSx7DBFtNDZlZGaZsJpTpEb5gyxwib0vvVitVBe1lYw6orY0jVPfE8841XxUGZUGtIP%2FxyNtnKldXfSMrMYfIUQG%2FMYrC5N3Y0k2a4bKOn7fHPxN0s0WafR7A0wKR4o3ydoCLKuOECBKTjmjumZcoMnAVMpNImc5wHfR1fYrvqSIWDVAiP49lt6cmars8VEoJhODcpb&X-Amz-Signature=c9c1e8cde88f5c65723980ecb0a284b9c1d80c219490105743e9828f6bb2cb85&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SFDKLTT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDd%2BAfIJ%2Fur8JR4jKk5zsKwW9A1gSJNWR%2Fzm%2BZB%2F%2F%2B9OAIhAIp%2FOet%2BV%2BitZMl1B58GRqJSP27sP3tpje498KTkDt2iKv8DCBwQABoMNjM3NDIzMTgzODA1Igy8FmCaQfKJNGvO%2BhQq3ANehxuQ%2F7%2FjAeShL9zQCQq3iTKTLdqLeoaHPD%2FQS6TG8XFMI8EaIkioOwN8vRARERzUVyHpeWduBBqUNYSsk%2B5mqD9eoY5I1lL%2BjMbiaBcKuDPI%2FbG%2F0aEOUzA3X5a2AzYdIvnui3xPL66s309BqOjBj%2FI377kUixhGJSvCcpeKtYfvvowgYHu6Xk5jpUzLNrLwzRxHLB1UxhGMKuDmWw7X4tuxgcoapGykqt4dEM%2BIGz0%2FVKyIOeBt1ZpCrOzx1jSvbKTfPM5UQ4vGPw%2F8j%2Fxwclwr48PwcaX9z6EiAsXdl%2BBjidjEeJ4p64YEfP4OBwrdclZdHybd5ffQTcwTh2J8Q4EzGeAKynJ4%2FEJfdxuH6cmKbAXYLTUJLtdrKIGUz8ywTpS2yVeIR7U98VlcmqJ2UQLStqClSHjgs%2FArEOobHkMdGdS%2BDXFH7Hn0uDaVc1LKl7j49iH3xNbCBO8PHE3rHY9IZ%2B8yJLNjDpx%2FVYPFKNNfwkJeFwMJg1D1Ez0Qps0lpKbSsfeyVEUjT6HVXD9K9Xn2P66%2FOeHtIRCGCNCSJeQcyeGV0edXOxpOqxy5dvi9NEPJgz6iq0kARuR4HpUvtPDLdg8jKAp9YErWUa9vGROz6fzy8XjKSPJjcDDhoIS9BjqkAXw8dpinP1VY7KwXF1fQZiSx7DBFtNDZlZGaZsJpTpEb5gyxwib0vvVitVBe1lYw6orY0jVPfE8841XxUGZUGtIP%2FxyNtnKldXfSMrMYfIUQG%2FMYrC5N3Y0k2a4bKOn7fHPxN0s0WafR7A0wKR4o3ydoCLKuOECBKTjmjumZcoMnAVMpNImc5wHfR1fYrvqSIWDVAiP49lt6cmars8VEoJhODcpb&X-Amz-Signature=11d170ed33831e49ef5485bc3ab863a51603ffb023a7b29e1f62bb9acfe700e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQAUWPRC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIEaXzr8xXGiJG9wn6qMWUulUTZI2K0u%2F1GaE7bL20coGAiEAhUtKscfTvhx9GI89CIJi2uy2CG8kEu4IGYICm2xsWZ4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNs6wl1pJ8Vw3J0KyCrcA6vq0oEoeYUXjj0sIwVI1Awd7o2ucT26Vk5dqdl7B9waw8gQg12g%2BzClnRRgFTIBEzukB8Db49ko3FYLM1dQ%2FA1ggxDNLf3Cqi3xb0gizLfND6%2B8rFxG0zJxd8u6H2cI%2B%2BiJy232gnB6YMmEP3I2%2Bs3K7ePN%2BsQ1kEOzehFK5mLMh0feKnhaPq2lrAk1PBAeULWqVSHqdGr7NETgrrd4jOxFd6xglqdNfxfeoL5atG163Zb4yGTVamQ2U5i129khz%2FSiCPHy0gmuWzxO%2BlggzP95yDMPwfe%2BAaHcFKxAnEvwSs0guANhah306vJSrA%2BjqXMScK7esjNoVyRP7jH1yC8aqrcHpniUX2z0gR120rKhYpc4upV3JjhV1hkLZIJ2Vyxm1XjZmlqCRNl%2BJTAx%2BnqTAsVLQY7n%2ByPl1pb6QORN1n7DsIYVeQ8CDCiBWGsHxnyv%2Fcxf8Srvj%2FQBcSnZK6E976U9ep9Y66a9Iq7%2B0IWQP4YoHzyNTytbbzhUNn86%2Fgas%2Fn0bjUTxUY46vh0T9wJkMUKdr0pD21raIys7y8QBxcBLjLsBA9WIM40RrYEodkt4I2JG7phQP0FTy8tLz4d8el5yM91bCg6csbvLZj6wAxmgoMFeVhXafL7FMLeihL0GOqUBR0oLlONGNY5Hi%2Fn49G3hcHgKLT7RRu3xwFMEHbX3cnY7HfpEWRDScR5rJ6MiD0HjeJ7IP9BFr86x%2FijKABWqHa9899MXTdkpaoS6t1Y9zZVmmvOJd8xoIqJi2gUtFJlmfVO9zVriec%2BE%2FtyVMrDGZdaZgW7QvukzkVx1PHl5P3gONOSBd9dPuRsllT75r0r9YNNZp0E%2FOrFshVCWJXnH47HeV14E&X-Amz-Signature=27f1dda4c1a4a93461cecc5969bd2e4583c5f4757625ae25873c51551d7c6f68&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQAUWPRC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIEaXzr8xXGiJG9wn6qMWUulUTZI2K0u%2F1GaE7bL20coGAiEAhUtKscfTvhx9GI89CIJi2uy2CG8kEu4IGYICm2xsWZ4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNs6wl1pJ8Vw3J0KyCrcA6vq0oEoeYUXjj0sIwVI1Awd7o2ucT26Vk5dqdl7B9waw8gQg12g%2BzClnRRgFTIBEzukB8Db49ko3FYLM1dQ%2FA1ggxDNLf3Cqi3xb0gizLfND6%2B8rFxG0zJxd8u6H2cI%2B%2BiJy232gnB6YMmEP3I2%2Bs3K7ePN%2BsQ1kEOzehFK5mLMh0feKnhaPq2lrAk1PBAeULWqVSHqdGr7NETgrrd4jOxFd6xglqdNfxfeoL5atG163Zb4yGTVamQ2U5i129khz%2FSiCPHy0gmuWzxO%2BlggzP95yDMPwfe%2BAaHcFKxAnEvwSs0guANhah306vJSrA%2BjqXMScK7esjNoVyRP7jH1yC8aqrcHpniUX2z0gR120rKhYpc4upV3JjhV1hkLZIJ2Vyxm1XjZmlqCRNl%2BJTAx%2BnqTAsVLQY7n%2ByPl1pb6QORN1n7DsIYVeQ8CDCiBWGsHxnyv%2Fcxf8Srvj%2FQBcSnZK6E976U9ep9Y66a9Iq7%2B0IWQP4YoHzyNTytbbzhUNn86%2Fgas%2Fn0bjUTxUY46vh0T9wJkMUKdr0pD21raIys7y8QBxcBLjLsBA9WIM40RrYEodkt4I2JG7phQP0FTy8tLz4d8el5yM91bCg6csbvLZj6wAxmgoMFeVhXafL7FMLeihL0GOqUBR0oLlONGNY5Hi%2Fn49G3hcHgKLT7RRu3xwFMEHbX3cnY7HfpEWRDScR5rJ6MiD0HjeJ7IP9BFr86x%2FijKABWqHa9899MXTdkpaoS6t1Y9zZVmmvOJd8xoIqJi2gUtFJlmfVO9zVriec%2BE%2FtyVMrDGZdaZgW7QvukzkVx1PHl5P3gONOSBd9dPuRsllT75r0r9YNNZp0E%2FOrFshVCWJXnH47HeV14E&X-Amz-Signature=e72ea05b721f04782d95833653dbea192c98a7fe4625b513081fff85ced97be7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQAUWPRC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIEaXzr8xXGiJG9wn6qMWUulUTZI2K0u%2F1GaE7bL20coGAiEAhUtKscfTvhx9GI89CIJi2uy2CG8kEu4IGYICm2xsWZ4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNs6wl1pJ8Vw3J0KyCrcA6vq0oEoeYUXjj0sIwVI1Awd7o2ucT26Vk5dqdl7B9waw8gQg12g%2BzClnRRgFTIBEzukB8Db49ko3FYLM1dQ%2FA1ggxDNLf3Cqi3xb0gizLfND6%2B8rFxG0zJxd8u6H2cI%2B%2BiJy232gnB6YMmEP3I2%2Bs3K7ePN%2BsQ1kEOzehFK5mLMh0feKnhaPq2lrAk1PBAeULWqVSHqdGr7NETgrrd4jOxFd6xglqdNfxfeoL5atG163Zb4yGTVamQ2U5i129khz%2FSiCPHy0gmuWzxO%2BlggzP95yDMPwfe%2BAaHcFKxAnEvwSs0guANhah306vJSrA%2BjqXMScK7esjNoVyRP7jH1yC8aqrcHpniUX2z0gR120rKhYpc4upV3JjhV1hkLZIJ2Vyxm1XjZmlqCRNl%2BJTAx%2BnqTAsVLQY7n%2ByPl1pb6QORN1n7DsIYVeQ8CDCiBWGsHxnyv%2Fcxf8Srvj%2FQBcSnZK6E976U9ep9Y66a9Iq7%2B0IWQP4YoHzyNTytbbzhUNn86%2Fgas%2Fn0bjUTxUY46vh0T9wJkMUKdr0pD21raIys7y8QBxcBLjLsBA9WIM40RrYEodkt4I2JG7phQP0FTy8tLz4d8el5yM91bCg6csbvLZj6wAxmgoMFeVhXafL7FMLeihL0GOqUBR0oLlONGNY5Hi%2Fn49G3hcHgKLT7RRu3xwFMEHbX3cnY7HfpEWRDScR5rJ6MiD0HjeJ7IP9BFr86x%2FijKABWqHa9899MXTdkpaoS6t1Y9zZVmmvOJd8xoIqJi2gUtFJlmfVO9zVriec%2BE%2FtyVMrDGZdaZgW7QvukzkVx1PHl5P3gONOSBd9dPuRsllT75r0r9YNNZp0E%2FOrFshVCWJXnH47HeV14E&X-Amz-Signature=72bdec45bc5af69ad4310a49d72e6943cf40393666a0660f1591204d2385d06d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQAUWPRC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIEaXzr8xXGiJG9wn6qMWUulUTZI2K0u%2F1GaE7bL20coGAiEAhUtKscfTvhx9GI89CIJi2uy2CG8kEu4IGYICm2xsWZ4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNs6wl1pJ8Vw3J0KyCrcA6vq0oEoeYUXjj0sIwVI1Awd7o2ucT26Vk5dqdl7B9waw8gQg12g%2BzClnRRgFTIBEzukB8Db49ko3FYLM1dQ%2FA1ggxDNLf3Cqi3xb0gizLfND6%2B8rFxG0zJxd8u6H2cI%2B%2BiJy232gnB6YMmEP3I2%2Bs3K7ePN%2BsQ1kEOzehFK5mLMh0feKnhaPq2lrAk1PBAeULWqVSHqdGr7NETgrrd4jOxFd6xglqdNfxfeoL5atG163Zb4yGTVamQ2U5i129khz%2FSiCPHy0gmuWzxO%2BlggzP95yDMPwfe%2BAaHcFKxAnEvwSs0guANhah306vJSrA%2BjqXMScK7esjNoVyRP7jH1yC8aqrcHpniUX2z0gR120rKhYpc4upV3JjhV1hkLZIJ2Vyxm1XjZmlqCRNl%2BJTAx%2BnqTAsVLQY7n%2ByPl1pb6QORN1n7DsIYVeQ8CDCiBWGsHxnyv%2Fcxf8Srvj%2FQBcSnZK6E976U9ep9Y66a9Iq7%2B0IWQP4YoHzyNTytbbzhUNn86%2Fgas%2Fn0bjUTxUY46vh0T9wJkMUKdr0pD21raIys7y8QBxcBLjLsBA9WIM40RrYEodkt4I2JG7phQP0FTy8tLz4d8el5yM91bCg6csbvLZj6wAxmgoMFeVhXafL7FMLeihL0GOqUBR0oLlONGNY5Hi%2Fn49G3hcHgKLT7RRu3xwFMEHbX3cnY7HfpEWRDScR5rJ6MiD0HjeJ7IP9BFr86x%2FijKABWqHa9899MXTdkpaoS6t1Y9zZVmmvOJd8xoIqJi2gUtFJlmfVO9zVriec%2BE%2FtyVMrDGZdaZgW7QvukzkVx1PHl5P3gONOSBd9dPuRsllT75r0r9YNNZp0E%2FOrFshVCWJXnH47HeV14E&X-Amz-Signature=df166b91a49da719a8dd2154434f30dcfa4ad55f922054d2e81e900a63bed142&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQAUWPRC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIEaXzr8xXGiJG9wn6qMWUulUTZI2K0u%2F1GaE7bL20coGAiEAhUtKscfTvhx9GI89CIJi2uy2CG8kEu4IGYICm2xsWZ4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNs6wl1pJ8Vw3J0KyCrcA6vq0oEoeYUXjj0sIwVI1Awd7o2ucT26Vk5dqdl7B9waw8gQg12g%2BzClnRRgFTIBEzukB8Db49ko3FYLM1dQ%2FA1ggxDNLf3Cqi3xb0gizLfND6%2B8rFxG0zJxd8u6H2cI%2B%2BiJy232gnB6YMmEP3I2%2Bs3K7ePN%2BsQ1kEOzehFK5mLMh0feKnhaPq2lrAk1PBAeULWqVSHqdGr7NETgrrd4jOxFd6xglqdNfxfeoL5atG163Zb4yGTVamQ2U5i129khz%2FSiCPHy0gmuWzxO%2BlggzP95yDMPwfe%2BAaHcFKxAnEvwSs0guANhah306vJSrA%2BjqXMScK7esjNoVyRP7jH1yC8aqrcHpniUX2z0gR120rKhYpc4upV3JjhV1hkLZIJ2Vyxm1XjZmlqCRNl%2BJTAx%2BnqTAsVLQY7n%2ByPl1pb6QORN1n7DsIYVeQ8CDCiBWGsHxnyv%2Fcxf8Srvj%2FQBcSnZK6E976U9ep9Y66a9Iq7%2B0IWQP4YoHzyNTytbbzhUNn86%2Fgas%2Fn0bjUTxUY46vh0T9wJkMUKdr0pD21raIys7y8QBxcBLjLsBA9WIM40RrYEodkt4I2JG7phQP0FTy8tLz4d8el5yM91bCg6csbvLZj6wAxmgoMFeVhXafL7FMLeihL0GOqUBR0oLlONGNY5Hi%2Fn49G3hcHgKLT7RRu3xwFMEHbX3cnY7HfpEWRDScR5rJ6MiD0HjeJ7IP9BFr86x%2FijKABWqHa9899MXTdkpaoS6t1Y9zZVmmvOJd8xoIqJi2gUtFJlmfVO9zVriec%2BE%2FtyVMrDGZdaZgW7QvukzkVx1PHl5P3gONOSBd9dPuRsllT75r0r9YNNZp0E%2FOrFshVCWJXnH47HeV14E&X-Amz-Signature=1a40d8a35827d7b809f41a5fc850dc293d849c76e38422c148e2a2c9c03f030e&X-Amz-SignedHeaders=host&x-id=GetObject)
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


