

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665USWZCPZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIEoIbLhur9ihVkrkbLC2MXf93YaozUldYKanY7uahN8YAiBFNlAlswJWI%2BRD4Gaggv5ZGdFEOTlyuBb6hU68Pif9FCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMp4Rsqihx2au6WczSKtwDg2MMU8L%2BNLeB9xuKSbf6xjMe84EIwxswYXvI9iDFVRGQ%2Fru5Kzzsc9NxiZi1iFsCUvxkm1IQutYWZBaDhK7OOanrvenSIGv0KPlTzyy6nYIYtBaMwYU3qgfVuPhKjXQ2uFkR2lNKCnCmK7f%2FipSOTFOhLej3U%2Fw76vOTi%2FmYfZSTQRQVOwffDeh%2FkHSX4AVOCaYANQHZuoOaG%2BGNpFH00j67MaO5AG1e1AcW2RGMVKk7W9EI5KOF4dMJK5wrjgUBvlQy1G9wI3lZi6Bol4dslyqfq%2BHrHWoI8bAmUXu9q9HGH7U5hCZ8zLRiGFk6q3PBltSgmPCrdSwJXnJO8iBqEaSanMI4RrjGOiXuGZ6kEgkpYlyHjOUJVheyV2O3NO81EmXYjhGgu2XQoAYl8xliOq9%2BPW8UQXsbXDHBEKIdRtyctfc%2FVodQn0axM4VrlWyClqrmr%2BnrlFbfOYwhXhY22o21RObxzyxoRru1CcCys4OhJPTwSA68Vt8A5a0pqh2t%2B4nrsLazw9GDdQ3GCbHQfoMENP4SwNTokdDkQQrm%2F1BLPTAVVq7cUsYYw%2FQZRLT5XaDeX6PiQU%2B5yBZvguN6Dd3lEEq%2FRd5zBhAulGD0URWuYv2ElVqXcbvXF3MwlZaMvQY6pgHFRAUl1vbGN9O%2Frpn8F%2F49Mx%2B1ZbCE5J%2F4xIA5jr1DIohQHakmCXrz34Ti7Kp14bFnXA3uQ6AMsV4%2FAqtuKu%2FObEHFB2IqnV%2FY%2BtcwZKxa5Fi4Dvx8bsaCbrx7QS0sK2KSR7ZeH2f2LCqte%2BdsZRrsdcWYs%2FfDJ6Ks4E%2BaYbHPg3N%2Bo%2FrKjhsLxAMQGdGoJ4wF7r%2B3kcVrrtYaM4ig%2B2r0VS2ir99%2B&X-Amz-Signature=9e67a1812ecdd4f6c6c6a7a010b160b12ae928fc2e844ce2f7e76be49df468ea&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FNNKHOY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDSHL5AWG%2BFIW6tW%2Ft0O%2F8pDcRq6aMN3VixKAkv3JUqbAIhAJIDK3EmE7GMtPakM5pUmb0GFTsYyd%2BtGxe8YG6mfLURKv8DCEAQABoMNjM3NDIzMTgzODA1IgxTxKvB9tMW%2BQd%2BFEIq3ANe0n6pMAno%2BSVB%2BemKAnF3gH0qtYIE%2BKAG4BQA96%2BoOADPFSYtWeCt%2FgY6SJvrZSF8vBQFByqBKYZ5hu%2BlTGrcQgMiZ3JPpCjj3L7Z26u97AXH3%2FJfbcEPYiSjmSWkpa9sMcg1heQ7mR2%2BbAw%2B1KtXFbMSQqxJb4gXOeFQ0V8BgPCxBhAV6pJrOEfxMqUBUmjpOwjYnhKLoX%2Fn%2B5tYcPht5sTb18wjJiVCAkI9VD3RmBxkMbKB6CflOQMQYdTX3%2BStonBKBnxhvzHJ6raV0mO%2FGgmrixrhSF%2F4O6h9hmkAGa8BtTwJAp3fMpG2iaBMYVvOAjrCO77D1WntwtaGAZpyLszTHU77ceMHLBjASwUfA0bIVPgjWLRWCP9atWbB31tF1By21ReE6uXuDq0QvXSyj7v6ZJW1HU6iZH%2B1CpRkD1yvGOlnKmYQFoPxnaiHF4kbIaEDtN7v426vzO0BAJvGA9RYu%2FNw45h3Hm0aKlASJz9f2Ym4qX%2F84mAP6s7rFlbytDR%2FHKBSm9xMVQsv%2Ff60Yf47P1n3e6h4pjbknpOGGTyLT01Y29P%2FJC8mbuYJG%2Frx2Jmezc1tTjTOAUpYe0kgcXIzYDHWQTbWKl3bnskS6Vjz1wqE%2BliPY8YMMjCCloy9BjqkAVqucYNBPvZl5iKH0v5vBZoyiQCqeZ3AQFOor4FKB7wkHV0M0c57pFFcPts37%2BQpO31mxVObK1h5x1n6lakFn%2FL9vBOT0990hBDftvRDX0wOxD%2B7BJmcMqFQeTz%2Fhmawm9F%2FpSsdq2GvHFCxtZVaTpJpyF%2FlwHcBeFXqMlNvhkh7ofmMX1bioO9CchAih44vXgmNWTBF9XqckFVwmqUWrfNLtwb5&X-Amz-Signature=ae2bca5e5a96f444e18d5232f827f72bb57809b88021d46013a82e64782e8313&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FNNKHOY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDSHL5AWG%2BFIW6tW%2Ft0O%2F8pDcRq6aMN3VixKAkv3JUqbAIhAJIDK3EmE7GMtPakM5pUmb0GFTsYyd%2BtGxe8YG6mfLURKv8DCEAQABoMNjM3NDIzMTgzODA1IgxTxKvB9tMW%2BQd%2BFEIq3ANe0n6pMAno%2BSVB%2BemKAnF3gH0qtYIE%2BKAG4BQA96%2BoOADPFSYtWeCt%2FgY6SJvrZSF8vBQFByqBKYZ5hu%2BlTGrcQgMiZ3JPpCjj3L7Z26u97AXH3%2FJfbcEPYiSjmSWkpa9sMcg1heQ7mR2%2BbAw%2B1KtXFbMSQqxJb4gXOeFQ0V8BgPCxBhAV6pJrOEfxMqUBUmjpOwjYnhKLoX%2Fn%2B5tYcPht5sTb18wjJiVCAkI9VD3RmBxkMbKB6CflOQMQYdTX3%2BStonBKBnxhvzHJ6raV0mO%2FGgmrixrhSF%2F4O6h9hmkAGa8BtTwJAp3fMpG2iaBMYVvOAjrCO77D1WntwtaGAZpyLszTHU77ceMHLBjASwUfA0bIVPgjWLRWCP9atWbB31tF1By21ReE6uXuDq0QvXSyj7v6ZJW1HU6iZH%2B1CpRkD1yvGOlnKmYQFoPxnaiHF4kbIaEDtN7v426vzO0BAJvGA9RYu%2FNw45h3Hm0aKlASJz9f2Ym4qX%2F84mAP6s7rFlbytDR%2FHKBSm9xMVQsv%2Ff60Yf47P1n3e6h4pjbknpOGGTyLT01Y29P%2FJC8mbuYJG%2Frx2Jmezc1tTjTOAUpYe0kgcXIzYDHWQTbWKl3bnskS6Vjz1wqE%2BliPY8YMMjCCloy9BjqkAVqucYNBPvZl5iKH0v5vBZoyiQCqeZ3AQFOor4FKB7wkHV0M0c57pFFcPts37%2BQpO31mxVObK1h5x1n6lakFn%2FL9vBOT0990hBDftvRDX0wOxD%2B7BJmcMqFQeTz%2Fhmawm9F%2FpSsdq2GvHFCxtZVaTpJpyF%2FlwHcBeFXqMlNvhkh7ofmMX1bioO9CchAih44vXgmNWTBF9XqckFVwmqUWrfNLtwb5&X-Amz-Signature=60b7a8d042070d9205764eb04f9b53e5a225f587f501e6446183d7ca0ca7f5ba&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FNNKHOY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDSHL5AWG%2BFIW6tW%2Ft0O%2F8pDcRq6aMN3VixKAkv3JUqbAIhAJIDK3EmE7GMtPakM5pUmb0GFTsYyd%2BtGxe8YG6mfLURKv8DCEAQABoMNjM3NDIzMTgzODA1IgxTxKvB9tMW%2BQd%2BFEIq3ANe0n6pMAno%2BSVB%2BemKAnF3gH0qtYIE%2BKAG4BQA96%2BoOADPFSYtWeCt%2FgY6SJvrZSF8vBQFByqBKYZ5hu%2BlTGrcQgMiZ3JPpCjj3L7Z26u97AXH3%2FJfbcEPYiSjmSWkpa9sMcg1heQ7mR2%2BbAw%2B1KtXFbMSQqxJb4gXOeFQ0V8BgPCxBhAV6pJrOEfxMqUBUmjpOwjYnhKLoX%2Fn%2B5tYcPht5sTb18wjJiVCAkI9VD3RmBxkMbKB6CflOQMQYdTX3%2BStonBKBnxhvzHJ6raV0mO%2FGgmrixrhSF%2F4O6h9hmkAGa8BtTwJAp3fMpG2iaBMYVvOAjrCO77D1WntwtaGAZpyLszTHU77ceMHLBjASwUfA0bIVPgjWLRWCP9atWbB31tF1By21ReE6uXuDq0QvXSyj7v6ZJW1HU6iZH%2B1CpRkD1yvGOlnKmYQFoPxnaiHF4kbIaEDtN7v426vzO0BAJvGA9RYu%2FNw45h3Hm0aKlASJz9f2Ym4qX%2F84mAP6s7rFlbytDR%2FHKBSm9xMVQsv%2Ff60Yf47P1n3e6h4pjbknpOGGTyLT01Y29P%2FJC8mbuYJG%2Frx2Jmezc1tTjTOAUpYe0kgcXIzYDHWQTbWKl3bnskS6Vjz1wqE%2BliPY8YMMjCCloy9BjqkAVqucYNBPvZl5iKH0v5vBZoyiQCqeZ3AQFOor4FKB7wkHV0M0c57pFFcPts37%2BQpO31mxVObK1h5x1n6lakFn%2FL9vBOT0990hBDftvRDX0wOxD%2B7BJmcMqFQeTz%2Fhmawm9F%2FpSsdq2GvHFCxtZVaTpJpyF%2FlwHcBeFXqMlNvhkh7ofmMX1bioO9CchAih44vXgmNWTBF9XqckFVwmqUWrfNLtwb5&X-Amz-Signature=e16850ce64db9322ac27bda2f222af6e84711d379b2a6f8ca543f05fe7df1888&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FNNKHOY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDSHL5AWG%2BFIW6tW%2Ft0O%2F8pDcRq6aMN3VixKAkv3JUqbAIhAJIDK3EmE7GMtPakM5pUmb0GFTsYyd%2BtGxe8YG6mfLURKv8DCEAQABoMNjM3NDIzMTgzODA1IgxTxKvB9tMW%2BQd%2BFEIq3ANe0n6pMAno%2BSVB%2BemKAnF3gH0qtYIE%2BKAG4BQA96%2BoOADPFSYtWeCt%2FgY6SJvrZSF8vBQFByqBKYZ5hu%2BlTGrcQgMiZ3JPpCjj3L7Z26u97AXH3%2FJfbcEPYiSjmSWkpa9sMcg1heQ7mR2%2BbAw%2B1KtXFbMSQqxJb4gXOeFQ0V8BgPCxBhAV6pJrOEfxMqUBUmjpOwjYnhKLoX%2Fn%2B5tYcPht5sTb18wjJiVCAkI9VD3RmBxkMbKB6CflOQMQYdTX3%2BStonBKBnxhvzHJ6raV0mO%2FGgmrixrhSF%2F4O6h9hmkAGa8BtTwJAp3fMpG2iaBMYVvOAjrCO77D1WntwtaGAZpyLszTHU77ceMHLBjASwUfA0bIVPgjWLRWCP9atWbB31tF1By21ReE6uXuDq0QvXSyj7v6ZJW1HU6iZH%2B1CpRkD1yvGOlnKmYQFoPxnaiHF4kbIaEDtN7v426vzO0BAJvGA9RYu%2FNw45h3Hm0aKlASJz9f2Ym4qX%2F84mAP6s7rFlbytDR%2FHKBSm9xMVQsv%2Ff60Yf47P1n3e6h4pjbknpOGGTyLT01Y29P%2FJC8mbuYJG%2Frx2Jmezc1tTjTOAUpYe0kgcXIzYDHWQTbWKl3bnskS6Vjz1wqE%2BliPY8YMMjCCloy9BjqkAVqucYNBPvZl5iKH0v5vBZoyiQCqeZ3AQFOor4FKB7wkHV0M0c57pFFcPts37%2BQpO31mxVObK1h5x1n6lakFn%2FL9vBOT0990hBDftvRDX0wOxD%2B7BJmcMqFQeTz%2Fhmawm9F%2FpSsdq2GvHFCxtZVaTpJpyF%2FlwHcBeFXqMlNvhkh7ofmMX1bioO9CchAih44vXgmNWTBF9XqckFVwmqUWrfNLtwb5&X-Amz-Signature=51d638fc6fa0d79d3e2d7220737849083d8601e4af899fef7089d200f325ce87&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FNNKHOY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDSHL5AWG%2BFIW6tW%2Ft0O%2F8pDcRq6aMN3VixKAkv3JUqbAIhAJIDK3EmE7GMtPakM5pUmb0GFTsYyd%2BtGxe8YG6mfLURKv8DCEAQABoMNjM3NDIzMTgzODA1IgxTxKvB9tMW%2BQd%2BFEIq3ANe0n6pMAno%2BSVB%2BemKAnF3gH0qtYIE%2BKAG4BQA96%2BoOADPFSYtWeCt%2FgY6SJvrZSF8vBQFByqBKYZ5hu%2BlTGrcQgMiZ3JPpCjj3L7Z26u97AXH3%2FJfbcEPYiSjmSWkpa9sMcg1heQ7mR2%2BbAw%2B1KtXFbMSQqxJb4gXOeFQ0V8BgPCxBhAV6pJrOEfxMqUBUmjpOwjYnhKLoX%2Fn%2B5tYcPht5sTb18wjJiVCAkI9VD3RmBxkMbKB6CflOQMQYdTX3%2BStonBKBnxhvzHJ6raV0mO%2FGgmrixrhSF%2F4O6h9hmkAGa8BtTwJAp3fMpG2iaBMYVvOAjrCO77D1WntwtaGAZpyLszTHU77ceMHLBjASwUfA0bIVPgjWLRWCP9atWbB31tF1By21ReE6uXuDq0QvXSyj7v6ZJW1HU6iZH%2B1CpRkD1yvGOlnKmYQFoPxnaiHF4kbIaEDtN7v426vzO0BAJvGA9RYu%2FNw45h3Hm0aKlASJz9f2Ym4qX%2F84mAP6s7rFlbytDR%2FHKBSm9xMVQsv%2Ff60Yf47P1n3e6h4pjbknpOGGTyLT01Y29P%2FJC8mbuYJG%2Frx2Jmezc1tTjTOAUpYe0kgcXIzYDHWQTbWKl3bnskS6Vjz1wqE%2BliPY8YMMjCCloy9BjqkAVqucYNBPvZl5iKH0v5vBZoyiQCqeZ3AQFOor4FKB7wkHV0M0c57pFFcPts37%2BQpO31mxVObK1h5x1n6lakFn%2FL9vBOT0990hBDftvRDX0wOxD%2B7BJmcMqFQeTz%2Fhmawm9F%2FpSsdq2GvHFCxtZVaTpJpyF%2FlwHcBeFXqMlNvhkh7ofmMX1bioO9CchAih44vXgmNWTBF9XqckFVwmqUWrfNLtwb5&X-Amz-Signature=509a283a2e8b7ce5b0dd64c6596c8bd567d26073020b423f4202a09a3369ad03&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665USWZCPZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIEoIbLhur9ihVkrkbLC2MXf93YaozUldYKanY7uahN8YAiBFNlAlswJWI%2BRD4Gaggv5ZGdFEOTlyuBb6hU68Pif9FCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMp4Rsqihx2au6WczSKtwDg2MMU8L%2BNLeB9xuKSbf6xjMe84EIwxswYXvI9iDFVRGQ%2Fru5Kzzsc9NxiZi1iFsCUvxkm1IQutYWZBaDhK7OOanrvenSIGv0KPlTzyy6nYIYtBaMwYU3qgfVuPhKjXQ2uFkR2lNKCnCmK7f%2FipSOTFOhLej3U%2Fw76vOTi%2FmYfZSTQRQVOwffDeh%2FkHSX4AVOCaYANQHZuoOaG%2BGNpFH00j67MaO5AG1e1AcW2RGMVKk7W9EI5KOF4dMJK5wrjgUBvlQy1G9wI3lZi6Bol4dslyqfq%2BHrHWoI8bAmUXu9q9HGH7U5hCZ8zLRiGFk6q3PBltSgmPCrdSwJXnJO8iBqEaSanMI4RrjGOiXuGZ6kEgkpYlyHjOUJVheyV2O3NO81EmXYjhGgu2XQoAYl8xliOq9%2BPW8UQXsbXDHBEKIdRtyctfc%2FVodQn0axM4VrlWyClqrmr%2BnrlFbfOYwhXhY22o21RObxzyxoRru1CcCys4OhJPTwSA68Vt8A5a0pqh2t%2B4nrsLazw9GDdQ3GCbHQfoMENP4SwNTokdDkQQrm%2F1BLPTAVVq7cUsYYw%2FQZRLT5XaDeX6PiQU%2B5yBZvguN6Dd3lEEq%2FRd5zBhAulGD0URWuYv2ElVqXcbvXF3MwlZaMvQY6pgHFRAUl1vbGN9O%2Frpn8F%2F49Mx%2B1ZbCE5J%2F4xIA5jr1DIohQHakmCXrz34Ti7Kp14bFnXA3uQ6AMsV4%2FAqtuKu%2FObEHFB2IqnV%2FY%2BtcwZKxa5Fi4Dvx8bsaCbrx7QS0sK2KSR7ZeH2f2LCqte%2BdsZRrsdcWYs%2FfDJ6Ks4E%2BaYbHPg3N%2Bo%2FrKjhsLxAMQGdGoJ4wF7r%2B3kcVrrtYaM4ig%2B2r0VS2ir99%2B&X-Amz-Signature=5bfafcf8886513025f0271751b819bc29433d0729244fbc078a3f8d9ad05eac3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665USWZCPZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIEoIbLhur9ihVkrkbLC2MXf93YaozUldYKanY7uahN8YAiBFNlAlswJWI%2BRD4Gaggv5ZGdFEOTlyuBb6hU68Pif9FCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMp4Rsqihx2au6WczSKtwDg2MMU8L%2BNLeB9xuKSbf6xjMe84EIwxswYXvI9iDFVRGQ%2Fru5Kzzsc9NxiZi1iFsCUvxkm1IQutYWZBaDhK7OOanrvenSIGv0KPlTzyy6nYIYtBaMwYU3qgfVuPhKjXQ2uFkR2lNKCnCmK7f%2FipSOTFOhLej3U%2Fw76vOTi%2FmYfZSTQRQVOwffDeh%2FkHSX4AVOCaYANQHZuoOaG%2BGNpFH00j67MaO5AG1e1AcW2RGMVKk7W9EI5KOF4dMJK5wrjgUBvlQy1G9wI3lZi6Bol4dslyqfq%2BHrHWoI8bAmUXu9q9HGH7U5hCZ8zLRiGFk6q3PBltSgmPCrdSwJXnJO8iBqEaSanMI4RrjGOiXuGZ6kEgkpYlyHjOUJVheyV2O3NO81EmXYjhGgu2XQoAYl8xliOq9%2BPW8UQXsbXDHBEKIdRtyctfc%2FVodQn0axM4VrlWyClqrmr%2BnrlFbfOYwhXhY22o21RObxzyxoRru1CcCys4OhJPTwSA68Vt8A5a0pqh2t%2B4nrsLazw9GDdQ3GCbHQfoMENP4SwNTokdDkQQrm%2F1BLPTAVVq7cUsYYw%2FQZRLT5XaDeX6PiQU%2B5yBZvguN6Dd3lEEq%2FRd5zBhAulGD0URWuYv2ElVqXcbvXF3MwlZaMvQY6pgHFRAUl1vbGN9O%2Frpn8F%2F49Mx%2B1ZbCE5J%2F4xIA5jr1DIohQHakmCXrz34Ti7Kp14bFnXA3uQ6AMsV4%2FAqtuKu%2FObEHFB2IqnV%2FY%2BtcwZKxa5Fi4Dvx8bsaCbrx7QS0sK2KSR7ZeH2f2LCqte%2BdsZRrsdcWYs%2FfDJ6Ks4E%2BaYbHPg3N%2Bo%2FrKjhsLxAMQGdGoJ4wF7r%2B3kcVrrtYaM4ig%2B2r0VS2ir99%2B&X-Amz-Signature=0ce46fbd798e251fcc4a4d6514179177b332b494b4d561de2d34b4327578b327&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665USWZCPZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIEoIbLhur9ihVkrkbLC2MXf93YaozUldYKanY7uahN8YAiBFNlAlswJWI%2BRD4Gaggv5ZGdFEOTlyuBb6hU68Pif9FCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMp4Rsqihx2au6WczSKtwDg2MMU8L%2BNLeB9xuKSbf6xjMe84EIwxswYXvI9iDFVRGQ%2Fru5Kzzsc9NxiZi1iFsCUvxkm1IQutYWZBaDhK7OOanrvenSIGv0KPlTzyy6nYIYtBaMwYU3qgfVuPhKjXQ2uFkR2lNKCnCmK7f%2FipSOTFOhLej3U%2Fw76vOTi%2FmYfZSTQRQVOwffDeh%2FkHSX4AVOCaYANQHZuoOaG%2BGNpFH00j67MaO5AG1e1AcW2RGMVKk7W9EI5KOF4dMJK5wrjgUBvlQy1G9wI3lZi6Bol4dslyqfq%2BHrHWoI8bAmUXu9q9HGH7U5hCZ8zLRiGFk6q3PBltSgmPCrdSwJXnJO8iBqEaSanMI4RrjGOiXuGZ6kEgkpYlyHjOUJVheyV2O3NO81EmXYjhGgu2XQoAYl8xliOq9%2BPW8UQXsbXDHBEKIdRtyctfc%2FVodQn0axM4VrlWyClqrmr%2BnrlFbfOYwhXhY22o21RObxzyxoRru1CcCys4OhJPTwSA68Vt8A5a0pqh2t%2B4nrsLazw9GDdQ3GCbHQfoMENP4SwNTokdDkQQrm%2F1BLPTAVVq7cUsYYw%2FQZRLT5XaDeX6PiQU%2B5yBZvguN6Dd3lEEq%2FRd5zBhAulGD0URWuYv2ElVqXcbvXF3MwlZaMvQY6pgHFRAUl1vbGN9O%2Frpn8F%2F49Mx%2B1ZbCE5J%2F4xIA5jr1DIohQHakmCXrz34Ti7Kp14bFnXA3uQ6AMsV4%2FAqtuKu%2FObEHFB2IqnV%2FY%2BtcwZKxa5Fi4Dvx8bsaCbrx7QS0sK2KSR7ZeH2f2LCqte%2BdsZRrsdcWYs%2FfDJ6Ks4E%2BaYbHPg3N%2Bo%2FrKjhsLxAMQGdGoJ4wF7r%2B3kcVrrtYaM4ig%2B2r0VS2ir99%2B&X-Amz-Signature=7a287e93733cf26a7f726d2a2978f97c00ed90125f8dfb5f3251bd09fec3b186&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665USWZCPZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIEoIbLhur9ihVkrkbLC2MXf93YaozUldYKanY7uahN8YAiBFNlAlswJWI%2BRD4Gaggv5ZGdFEOTlyuBb6hU68Pif9FCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMp4Rsqihx2au6WczSKtwDg2MMU8L%2BNLeB9xuKSbf6xjMe84EIwxswYXvI9iDFVRGQ%2Fru5Kzzsc9NxiZi1iFsCUvxkm1IQutYWZBaDhK7OOanrvenSIGv0KPlTzyy6nYIYtBaMwYU3qgfVuPhKjXQ2uFkR2lNKCnCmK7f%2FipSOTFOhLej3U%2Fw76vOTi%2FmYfZSTQRQVOwffDeh%2FkHSX4AVOCaYANQHZuoOaG%2BGNpFH00j67MaO5AG1e1AcW2RGMVKk7W9EI5KOF4dMJK5wrjgUBvlQy1G9wI3lZi6Bol4dslyqfq%2BHrHWoI8bAmUXu9q9HGH7U5hCZ8zLRiGFk6q3PBltSgmPCrdSwJXnJO8iBqEaSanMI4RrjGOiXuGZ6kEgkpYlyHjOUJVheyV2O3NO81EmXYjhGgu2XQoAYl8xliOq9%2BPW8UQXsbXDHBEKIdRtyctfc%2FVodQn0axM4VrlWyClqrmr%2BnrlFbfOYwhXhY22o21RObxzyxoRru1CcCys4OhJPTwSA68Vt8A5a0pqh2t%2B4nrsLazw9GDdQ3GCbHQfoMENP4SwNTokdDkQQrm%2F1BLPTAVVq7cUsYYw%2FQZRLT5XaDeX6PiQU%2B5yBZvguN6Dd3lEEq%2FRd5zBhAulGD0URWuYv2ElVqXcbvXF3MwlZaMvQY6pgHFRAUl1vbGN9O%2Frpn8F%2F49Mx%2B1ZbCE5J%2F4xIA5jr1DIohQHakmCXrz34Ti7Kp14bFnXA3uQ6AMsV4%2FAqtuKu%2FObEHFB2IqnV%2FY%2BtcwZKxa5Fi4Dvx8bsaCbrx7QS0sK2KSR7ZeH2f2LCqte%2BdsZRrsdcWYs%2FfDJ6Ks4E%2BaYbHPg3N%2Bo%2FrKjhsLxAMQGdGoJ4wF7r%2B3kcVrrtYaM4ig%2B2r0VS2ir99%2B&X-Amz-Signature=ba07a15c6b9d46260d236bd0a908c034cf63727828bde6aafb51dfa2814a0845&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665USWZCPZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIEoIbLhur9ihVkrkbLC2MXf93YaozUldYKanY7uahN8YAiBFNlAlswJWI%2BRD4Gaggv5ZGdFEOTlyuBb6hU68Pif9FCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMp4Rsqihx2au6WczSKtwDg2MMU8L%2BNLeB9xuKSbf6xjMe84EIwxswYXvI9iDFVRGQ%2Fru5Kzzsc9NxiZi1iFsCUvxkm1IQutYWZBaDhK7OOanrvenSIGv0KPlTzyy6nYIYtBaMwYU3qgfVuPhKjXQ2uFkR2lNKCnCmK7f%2FipSOTFOhLej3U%2Fw76vOTi%2FmYfZSTQRQVOwffDeh%2FkHSX4AVOCaYANQHZuoOaG%2BGNpFH00j67MaO5AG1e1AcW2RGMVKk7W9EI5KOF4dMJK5wrjgUBvlQy1G9wI3lZi6Bol4dslyqfq%2BHrHWoI8bAmUXu9q9HGH7U5hCZ8zLRiGFk6q3PBltSgmPCrdSwJXnJO8iBqEaSanMI4RrjGOiXuGZ6kEgkpYlyHjOUJVheyV2O3NO81EmXYjhGgu2XQoAYl8xliOq9%2BPW8UQXsbXDHBEKIdRtyctfc%2FVodQn0axM4VrlWyClqrmr%2BnrlFbfOYwhXhY22o21RObxzyxoRru1CcCys4OhJPTwSA68Vt8A5a0pqh2t%2B4nrsLazw9GDdQ3GCbHQfoMENP4SwNTokdDkQQrm%2F1BLPTAVVq7cUsYYw%2FQZRLT5XaDeX6PiQU%2B5yBZvguN6Dd3lEEq%2FRd5zBhAulGD0URWuYv2ElVqXcbvXF3MwlZaMvQY6pgHFRAUl1vbGN9O%2Frpn8F%2F49Mx%2B1ZbCE5J%2F4xIA5jr1DIohQHakmCXrz34Ti7Kp14bFnXA3uQ6AMsV4%2FAqtuKu%2FObEHFB2IqnV%2FY%2BtcwZKxa5Fi4Dvx8bsaCbrx7QS0sK2KSR7ZeH2f2LCqte%2BdsZRrsdcWYs%2FfDJ6Ks4E%2BaYbHPg3N%2Bo%2FrKjhsLxAMQGdGoJ4wF7r%2B3kcVrrtYaM4ig%2B2r0VS2ir99%2B&X-Amz-Signature=3a1b3caea0a0403c203ac339e62e7cd923a1e916f645a5f5a119c8a1b5761a18&X-Amz-SignedHeaders=host&x-id=GetObject)
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


