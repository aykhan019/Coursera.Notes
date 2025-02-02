

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PZUDIFP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBepMe6DgMW9uunhWQ4cdGVfZKVlxaQP0iwJ%2FT5t%2BItkAiAJajY4SPOUAcOU7KlX6tR%2BduJIWb68ETWlDCV5QAABEyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVrepUXsda5cmpk3PKtwDGBuW2sRy6yoSRKrAURgTuoJPvnOd6hprHjjlZSgC0mZcL5ck64Y0HknlDGGzf2GlAHVkdrfi9MzFaDavkPFC6g4bdInGtqUEgVoGflZZdWdJXcCFyK8M0OgFbyrsHwtjK5ctEmsZYJI9iHq2dARfmkN1BLlSCpQCfhJ4vvO9L%2FISDrECvmflNLC%2FCGyXmnG%2BIHk2C9TfMgl2yaBdFMHh71O0TDoW2Tlnxdfm1gwUZMN1J1uLEq1ZBlsyOMnTaTXPqmYxeNBNscIaYDRwpPURikWXV%2Fmtd0VeebO%2BwI4SSYCYBrase1Dv2lAyyrZupOjDXCcAG0gQCGSTGYXRnvsaqIlwHmub2Z%2BAxwnJUpY1g0T05aUV1OFZxyQPCblwQOlzGbRWNqH%2F05Z3FueR2ELkQXapH4BVcibtZHPQZOlUpiU4W9sRhaL0rjj4j5B40bk428%2BqUWiZkSaR8%2B9mZdtgH7eiU3i9NFpdvEApW5GNJWulg70cMOU6WW9yklViftbpRd9KENOw8iJ2YKcnpW9bBVeY2rrrmrRdx6J6hJdqCunTz7fbBWn9%2F%2BAvxJ41JQudxgsqGhCQejfuf3M2EXs0zmeTi398nmC6Nqh9fKt%2FdktZHR9lpya8VfgCaYswx7%2F9vAY6pgGPM%2B8gN7id5tgnt0LWRNfL4m8dr4Q5aKU8%2FzRKC7%2BRphSNlShmTWENxQ%2FWenf3IKdgzPMmhQn%2BN5PNB7ZhIRfC6Q7hE%2FUy5LpIEl3qDGZk6x8xPgaSMmPmoMw4Sdfyf37aES8a3pntiG6YyLPzHHLHBQcLQ8Jt15WMr71Jls%2Fo%2FUYK6kza%2BJleQi380oPYyDMIbqBkuehu03iXbtMtcjRVsDS1tFvF&X-Amz-Signature=b493584d0f07f14590596707a467b2e1201d31b36d54a667385549030a6c62e9&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S3MGJYH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCv%2Fx4nscdwgAjfgc%2FgxRlnRxD1RGX7%2BmXxrwHvub9w1QIgFdPt4CWfamK3Cv2B6w6uCT7kcgT5z2lsDwuUaJgb9f0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAehXkmrmQqmNYXVjCrcAyltAkePXiGAFK8L7QtzTKylxNXXBD14JVNZ11xZnMSYJ5ep4AJptDap6baxWZCjxU1Kndm6UJqEZezEDI%2Fyr3MgbCtXxPeXTGrsZO5H5eKn5VtygEsHW8uRzMF69wmMxdRYZ5Z3%2BOOd93sHlO7KoukpDMCV2ULXpsU8pUkB1OyUtc8J5uBNeyxo2S3FJMY935DYjbUZ3x30QIZ4%2FayQgqpvJb5%2BEmhRaEf30hJVr64Tiqrz2eukdKRLvu2SIbn2CSPun9hD74ooZBBKGv0u1IPCE1WL3fzo7%2FMfvD7EWSPn0XfHgoSrYDUtN%2BflMRgMzvI2uBfT%2FySuwTUOUl1B3X9Oorm3UzTA4W6LWCzb0dpwceCW6EwXgeUDf3OZgi1AI8ZfXpz87Vaw%2BGAVnSR3CP7iZO%2FhudKxhuvFTbDVPKWkjvto5zcuuVD%2BX23pThwLVrfhU9ycjf5HZNbXUZfO1FEv9kxUhtk8lPTKba%2Beec7lOSg%2F18M38EmP3jN8IXbYi0UVaSEW2eMGOqT3MNwvmpTqlmFiKhRtMVxZtQVn6OLT4D1VH815RHTuLkjg4Xvz6CbBzcM2%2B3KQmePMmCy8iVx5iDak0dgSYwidMgpsS7cZqAogYutPUUtQL%2F8zMJKU%2FrwGOqUB3hT5MmcGPvohVODX7FyX%2ByZ26hPXGn20uzt8AprU9OMFyzntDyB6SMhq%2Ba4GmWGY5FTUHMGCK22OYaOdDFe2zWChjYh1huAtvwd33YzaINXdvOysZGMjitMQpim7jMIZSLGPxe6DxrdNVTAarO%2FJgQpDDaK7Ex%2B4dOsJIjBb3N%2FmaPzC5gCCS%2BA3pIdMqG3Sp55xaT8eLJyviX4VS9Yx3NruWbDX&X-Amz-Signature=dc8e698a03a61a3da96799a6905ed1d390cb2efcf4c77aa8045f45df12768941&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S3MGJYH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCv%2Fx4nscdwgAjfgc%2FgxRlnRxD1RGX7%2BmXxrwHvub9w1QIgFdPt4CWfamK3Cv2B6w6uCT7kcgT5z2lsDwuUaJgb9f0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAehXkmrmQqmNYXVjCrcAyltAkePXiGAFK8L7QtzTKylxNXXBD14JVNZ11xZnMSYJ5ep4AJptDap6baxWZCjxU1Kndm6UJqEZezEDI%2Fyr3MgbCtXxPeXTGrsZO5H5eKn5VtygEsHW8uRzMF69wmMxdRYZ5Z3%2BOOd93sHlO7KoukpDMCV2ULXpsU8pUkB1OyUtc8J5uBNeyxo2S3FJMY935DYjbUZ3x30QIZ4%2FayQgqpvJb5%2BEmhRaEf30hJVr64Tiqrz2eukdKRLvu2SIbn2CSPun9hD74ooZBBKGv0u1IPCE1WL3fzo7%2FMfvD7EWSPn0XfHgoSrYDUtN%2BflMRgMzvI2uBfT%2FySuwTUOUl1B3X9Oorm3UzTA4W6LWCzb0dpwceCW6EwXgeUDf3OZgi1AI8ZfXpz87Vaw%2BGAVnSR3CP7iZO%2FhudKxhuvFTbDVPKWkjvto5zcuuVD%2BX23pThwLVrfhU9ycjf5HZNbXUZfO1FEv9kxUhtk8lPTKba%2Beec7lOSg%2F18M38EmP3jN8IXbYi0UVaSEW2eMGOqT3MNwvmpTqlmFiKhRtMVxZtQVn6OLT4D1VH815RHTuLkjg4Xvz6CbBzcM2%2B3KQmePMmCy8iVx5iDak0dgSYwidMgpsS7cZqAogYutPUUtQL%2F8zMJKU%2FrwGOqUB3hT5MmcGPvohVODX7FyX%2ByZ26hPXGn20uzt8AprU9OMFyzntDyB6SMhq%2Ba4GmWGY5FTUHMGCK22OYaOdDFe2zWChjYh1huAtvwd33YzaINXdvOysZGMjitMQpim7jMIZSLGPxe6DxrdNVTAarO%2FJgQpDDaK7Ex%2B4dOsJIjBb3N%2FmaPzC5gCCS%2BA3pIdMqG3Sp55xaT8eLJyviX4VS9Yx3NruWbDX&X-Amz-Signature=ad21b854afaee8f6c33395bae6d91b3402fada0c860491bd1b23184757e5bff7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S3MGJYH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCv%2Fx4nscdwgAjfgc%2FgxRlnRxD1RGX7%2BmXxrwHvub9w1QIgFdPt4CWfamK3Cv2B6w6uCT7kcgT5z2lsDwuUaJgb9f0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAehXkmrmQqmNYXVjCrcAyltAkePXiGAFK8L7QtzTKylxNXXBD14JVNZ11xZnMSYJ5ep4AJptDap6baxWZCjxU1Kndm6UJqEZezEDI%2Fyr3MgbCtXxPeXTGrsZO5H5eKn5VtygEsHW8uRzMF69wmMxdRYZ5Z3%2BOOd93sHlO7KoukpDMCV2ULXpsU8pUkB1OyUtc8J5uBNeyxo2S3FJMY935DYjbUZ3x30QIZ4%2FayQgqpvJb5%2BEmhRaEf30hJVr64Tiqrz2eukdKRLvu2SIbn2CSPun9hD74ooZBBKGv0u1IPCE1WL3fzo7%2FMfvD7EWSPn0XfHgoSrYDUtN%2BflMRgMzvI2uBfT%2FySuwTUOUl1B3X9Oorm3UzTA4W6LWCzb0dpwceCW6EwXgeUDf3OZgi1AI8ZfXpz87Vaw%2BGAVnSR3CP7iZO%2FhudKxhuvFTbDVPKWkjvto5zcuuVD%2BX23pThwLVrfhU9ycjf5HZNbXUZfO1FEv9kxUhtk8lPTKba%2Beec7lOSg%2F18M38EmP3jN8IXbYi0UVaSEW2eMGOqT3MNwvmpTqlmFiKhRtMVxZtQVn6OLT4D1VH815RHTuLkjg4Xvz6CbBzcM2%2B3KQmePMmCy8iVx5iDak0dgSYwidMgpsS7cZqAogYutPUUtQL%2F8zMJKU%2FrwGOqUB3hT5MmcGPvohVODX7FyX%2ByZ26hPXGn20uzt8AprU9OMFyzntDyB6SMhq%2Ba4GmWGY5FTUHMGCK22OYaOdDFe2zWChjYh1huAtvwd33YzaINXdvOysZGMjitMQpim7jMIZSLGPxe6DxrdNVTAarO%2FJgQpDDaK7Ex%2B4dOsJIjBb3N%2FmaPzC5gCCS%2BA3pIdMqG3Sp55xaT8eLJyviX4VS9Yx3NruWbDX&X-Amz-Signature=4ec5f730d04598d1923eaadbe3bfa41f45bb05c85bfb7ec8872cfa537fb84745&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S3MGJYH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCv%2Fx4nscdwgAjfgc%2FgxRlnRxD1RGX7%2BmXxrwHvub9w1QIgFdPt4CWfamK3Cv2B6w6uCT7kcgT5z2lsDwuUaJgb9f0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAehXkmrmQqmNYXVjCrcAyltAkePXiGAFK8L7QtzTKylxNXXBD14JVNZ11xZnMSYJ5ep4AJptDap6baxWZCjxU1Kndm6UJqEZezEDI%2Fyr3MgbCtXxPeXTGrsZO5H5eKn5VtygEsHW8uRzMF69wmMxdRYZ5Z3%2BOOd93sHlO7KoukpDMCV2ULXpsU8pUkB1OyUtc8J5uBNeyxo2S3FJMY935DYjbUZ3x30QIZ4%2FayQgqpvJb5%2BEmhRaEf30hJVr64Tiqrz2eukdKRLvu2SIbn2CSPun9hD74ooZBBKGv0u1IPCE1WL3fzo7%2FMfvD7EWSPn0XfHgoSrYDUtN%2BflMRgMzvI2uBfT%2FySuwTUOUl1B3X9Oorm3UzTA4W6LWCzb0dpwceCW6EwXgeUDf3OZgi1AI8ZfXpz87Vaw%2BGAVnSR3CP7iZO%2FhudKxhuvFTbDVPKWkjvto5zcuuVD%2BX23pThwLVrfhU9ycjf5HZNbXUZfO1FEv9kxUhtk8lPTKba%2Beec7lOSg%2F18M38EmP3jN8IXbYi0UVaSEW2eMGOqT3MNwvmpTqlmFiKhRtMVxZtQVn6OLT4D1VH815RHTuLkjg4Xvz6CbBzcM2%2B3KQmePMmCy8iVx5iDak0dgSYwidMgpsS7cZqAogYutPUUtQL%2F8zMJKU%2FrwGOqUB3hT5MmcGPvohVODX7FyX%2ByZ26hPXGn20uzt8AprU9OMFyzntDyB6SMhq%2Ba4GmWGY5FTUHMGCK22OYaOdDFe2zWChjYh1huAtvwd33YzaINXdvOysZGMjitMQpim7jMIZSLGPxe6DxrdNVTAarO%2FJgQpDDaK7Ex%2B4dOsJIjBb3N%2FmaPzC5gCCS%2BA3pIdMqG3Sp55xaT8eLJyviX4VS9Yx3NruWbDX&X-Amz-Signature=01c27f4e78aeb6713000b7791c37d56d20a7713babf29d99b42d94dfd4089da4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S3MGJYH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCv%2Fx4nscdwgAjfgc%2FgxRlnRxD1RGX7%2BmXxrwHvub9w1QIgFdPt4CWfamK3Cv2B6w6uCT7kcgT5z2lsDwuUaJgb9f0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAehXkmrmQqmNYXVjCrcAyltAkePXiGAFK8L7QtzTKylxNXXBD14JVNZ11xZnMSYJ5ep4AJptDap6baxWZCjxU1Kndm6UJqEZezEDI%2Fyr3MgbCtXxPeXTGrsZO5H5eKn5VtygEsHW8uRzMF69wmMxdRYZ5Z3%2BOOd93sHlO7KoukpDMCV2ULXpsU8pUkB1OyUtc8J5uBNeyxo2S3FJMY935DYjbUZ3x30QIZ4%2FayQgqpvJb5%2BEmhRaEf30hJVr64Tiqrz2eukdKRLvu2SIbn2CSPun9hD74ooZBBKGv0u1IPCE1WL3fzo7%2FMfvD7EWSPn0XfHgoSrYDUtN%2BflMRgMzvI2uBfT%2FySuwTUOUl1B3X9Oorm3UzTA4W6LWCzb0dpwceCW6EwXgeUDf3OZgi1AI8ZfXpz87Vaw%2BGAVnSR3CP7iZO%2FhudKxhuvFTbDVPKWkjvto5zcuuVD%2BX23pThwLVrfhU9ycjf5HZNbXUZfO1FEv9kxUhtk8lPTKba%2Beec7lOSg%2F18M38EmP3jN8IXbYi0UVaSEW2eMGOqT3MNwvmpTqlmFiKhRtMVxZtQVn6OLT4D1VH815RHTuLkjg4Xvz6CbBzcM2%2B3KQmePMmCy8iVx5iDak0dgSYwidMgpsS7cZqAogYutPUUtQL%2F8zMJKU%2FrwGOqUB3hT5MmcGPvohVODX7FyX%2ByZ26hPXGn20uzt8AprU9OMFyzntDyB6SMhq%2Ba4GmWGY5FTUHMGCK22OYaOdDFe2zWChjYh1huAtvwd33YzaINXdvOysZGMjitMQpim7jMIZSLGPxe6DxrdNVTAarO%2FJgQpDDaK7Ex%2B4dOsJIjBb3N%2FmaPzC5gCCS%2BA3pIdMqG3Sp55xaT8eLJyviX4VS9Yx3NruWbDX&X-Amz-Signature=06c024751052112c5d75f2e5c176af3d5aaa51a2e19d4d8c4b4fe471a7bb36af&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PZUDIFP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBepMe6DgMW9uunhWQ4cdGVfZKVlxaQP0iwJ%2FT5t%2BItkAiAJajY4SPOUAcOU7KlX6tR%2BduJIWb68ETWlDCV5QAABEyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVrepUXsda5cmpk3PKtwDGBuW2sRy6yoSRKrAURgTuoJPvnOd6hprHjjlZSgC0mZcL5ck64Y0HknlDGGzf2GlAHVkdrfi9MzFaDavkPFC6g4bdInGtqUEgVoGflZZdWdJXcCFyK8M0OgFbyrsHwtjK5ctEmsZYJI9iHq2dARfmkN1BLlSCpQCfhJ4vvO9L%2FISDrECvmflNLC%2FCGyXmnG%2BIHk2C9TfMgl2yaBdFMHh71O0TDoW2Tlnxdfm1gwUZMN1J1uLEq1ZBlsyOMnTaTXPqmYxeNBNscIaYDRwpPURikWXV%2Fmtd0VeebO%2BwI4SSYCYBrase1Dv2lAyyrZupOjDXCcAG0gQCGSTGYXRnvsaqIlwHmub2Z%2BAxwnJUpY1g0T05aUV1OFZxyQPCblwQOlzGbRWNqH%2F05Z3FueR2ELkQXapH4BVcibtZHPQZOlUpiU4W9sRhaL0rjj4j5B40bk428%2BqUWiZkSaR8%2B9mZdtgH7eiU3i9NFpdvEApW5GNJWulg70cMOU6WW9yklViftbpRd9KENOw8iJ2YKcnpW9bBVeY2rrrmrRdx6J6hJdqCunTz7fbBWn9%2F%2BAvxJ41JQudxgsqGhCQejfuf3M2EXs0zmeTi398nmC6Nqh9fKt%2FdktZHR9lpya8VfgCaYswx7%2F9vAY6pgGPM%2B8gN7id5tgnt0LWRNfL4m8dr4Q5aKU8%2FzRKC7%2BRphSNlShmTWENxQ%2FWenf3IKdgzPMmhQn%2BN5PNB7ZhIRfC6Q7hE%2FUy5LpIEl3qDGZk6x8xPgaSMmPmoMw4Sdfyf37aES8a3pntiG6YyLPzHHLHBQcLQ8Jt15WMr71Jls%2Fo%2FUYK6kza%2BJleQi380oPYyDMIbqBkuehu03iXbtMtcjRVsDS1tFvF&X-Amz-Signature=d396441f1fcc74663d033a43c7ad0b37331af88a69e9184bd187621f69c0e1c0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PZUDIFP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBepMe6DgMW9uunhWQ4cdGVfZKVlxaQP0iwJ%2FT5t%2BItkAiAJajY4SPOUAcOU7KlX6tR%2BduJIWb68ETWlDCV5QAABEyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVrepUXsda5cmpk3PKtwDGBuW2sRy6yoSRKrAURgTuoJPvnOd6hprHjjlZSgC0mZcL5ck64Y0HknlDGGzf2GlAHVkdrfi9MzFaDavkPFC6g4bdInGtqUEgVoGflZZdWdJXcCFyK8M0OgFbyrsHwtjK5ctEmsZYJI9iHq2dARfmkN1BLlSCpQCfhJ4vvO9L%2FISDrECvmflNLC%2FCGyXmnG%2BIHk2C9TfMgl2yaBdFMHh71O0TDoW2Tlnxdfm1gwUZMN1J1uLEq1ZBlsyOMnTaTXPqmYxeNBNscIaYDRwpPURikWXV%2Fmtd0VeebO%2BwI4SSYCYBrase1Dv2lAyyrZupOjDXCcAG0gQCGSTGYXRnvsaqIlwHmub2Z%2BAxwnJUpY1g0T05aUV1OFZxyQPCblwQOlzGbRWNqH%2F05Z3FueR2ELkQXapH4BVcibtZHPQZOlUpiU4W9sRhaL0rjj4j5B40bk428%2BqUWiZkSaR8%2B9mZdtgH7eiU3i9NFpdvEApW5GNJWulg70cMOU6WW9yklViftbpRd9KENOw8iJ2YKcnpW9bBVeY2rrrmrRdx6J6hJdqCunTz7fbBWn9%2F%2BAvxJ41JQudxgsqGhCQejfuf3M2EXs0zmeTi398nmC6Nqh9fKt%2FdktZHR9lpya8VfgCaYswx7%2F9vAY6pgGPM%2B8gN7id5tgnt0LWRNfL4m8dr4Q5aKU8%2FzRKC7%2BRphSNlShmTWENxQ%2FWenf3IKdgzPMmhQn%2BN5PNB7ZhIRfC6Q7hE%2FUy5LpIEl3qDGZk6x8xPgaSMmPmoMw4Sdfyf37aES8a3pntiG6YyLPzHHLHBQcLQ8Jt15WMr71Jls%2Fo%2FUYK6kza%2BJleQi380oPYyDMIbqBkuehu03iXbtMtcjRVsDS1tFvF&X-Amz-Signature=a04f4f75e43c18688e849003f877e5b8375614221395b3b2fc03d6fc0d839c34&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PZUDIFP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBepMe6DgMW9uunhWQ4cdGVfZKVlxaQP0iwJ%2FT5t%2BItkAiAJajY4SPOUAcOU7KlX6tR%2BduJIWb68ETWlDCV5QAABEyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVrepUXsda5cmpk3PKtwDGBuW2sRy6yoSRKrAURgTuoJPvnOd6hprHjjlZSgC0mZcL5ck64Y0HknlDGGzf2GlAHVkdrfi9MzFaDavkPFC6g4bdInGtqUEgVoGflZZdWdJXcCFyK8M0OgFbyrsHwtjK5ctEmsZYJI9iHq2dARfmkN1BLlSCpQCfhJ4vvO9L%2FISDrECvmflNLC%2FCGyXmnG%2BIHk2C9TfMgl2yaBdFMHh71O0TDoW2Tlnxdfm1gwUZMN1J1uLEq1ZBlsyOMnTaTXPqmYxeNBNscIaYDRwpPURikWXV%2Fmtd0VeebO%2BwI4SSYCYBrase1Dv2lAyyrZupOjDXCcAG0gQCGSTGYXRnvsaqIlwHmub2Z%2BAxwnJUpY1g0T05aUV1OFZxyQPCblwQOlzGbRWNqH%2F05Z3FueR2ELkQXapH4BVcibtZHPQZOlUpiU4W9sRhaL0rjj4j5B40bk428%2BqUWiZkSaR8%2B9mZdtgH7eiU3i9NFpdvEApW5GNJWulg70cMOU6WW9yklViftbpRd9KENOw8iJ2YKcnpW9bBVeY2rrrmrRdx6J6hJdqCunTz7fbBWn9%2F%2BAvxJ41JQudxgsqGhCQejfuf3M2EXs0zmeTi398nmC6Nqh9fKt%2FdktZHR9lpya8VfgCaYswx7%2F9vAY6pgGPM%2B8gN7id5tgnt0LWRNfL4m8dr4Q5aKU8%2FzRKC7%2BRphSNlShmTWENxQ%2FWenf3IKdgzPMmhQn%2BN5PNB7ZhIRfC6Q7hE%2FUy5LpIEl3qDGZk6x8xPgaSMmPmoMw4Sdfyf37aES8a3pntiG6YyLPzHHLHBQcLQ8Jt15WMr71Jls%2Fo%2FUYK6kza%2BJleQi380oPYyDMIbqBkuehu03iXbtMtcjRVsDS1tFvF&X-Amz-Signature=8658de5a08d729f03ef4504409a9fcd55791ca3c11aceeb9880aa233aac66f2c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PZUDIFP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBepMe6DgMW9uunhWQ4cdGVfZKVlxaQP0iwJ%2FT5t%2BItkAiAJajY4SPOUAcOU7KlX6tR%2BduJIWb68ETWlDCV5QAABEyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVrepUXsda5cmpk3PKtwDGBuW2sRy6yoSRKrAURgTuoJPvnOd6hprHjjlZSgC0mZcL5ck64Y0HknlDGGzf2GlAHVkdrfi9MzFaDavkPFC6g4bdInGtqUEgVoGflZZdWdJXcCFyK8M0OgFbyrsHwtjK5ctEmsZYJI9iHq2dARfmkN1BLlSCpQCfhJ4vvO9L%2FISDrECvmflNLC%2FCGyXmnG%2BIHk2C9TfMgl2yaBdFMHh71O0TDoW2Tlnxdfm1gwUZMN1J1uLEq1ZBlsyOMnTaTXPqmYxeNBNscIaYDRwpPURikWXV%2Fmtd0VeebO%2BwI4SSYCYBrase1Dv2lAyyrZupOjDXCcAG0gQCGSTGYXRnvsaqIlwHmub2Z%2BAxwnJUpY1g0T05aUV1OFZxyQPCblwQOlzGbRWNqH%2F05Z3FueR2ELkQXapH4BVcibtZHPQZOlUpiU4W9sRhaL0rjj4j5B40bk428%2BqUWiZkSaR8%2B9mZdtgH7eiU3i9NFpdvEApW5GNJWulg70cMOU6WW9yklViftbpRd9KENOw8iJ2YKcnpW9bBVeY2rrrmrRdx6J6hJdqCunTz7fbBWn9%2F%2BAvxJ41JQudxgsqGhCQejfuf3M2EXs0zmeTi398nmC6Nqh9fKt%2FdktZHR9lpya8VfgCaYswx7%2F9vAY6pgGPM%2B8gN7id5tgnt0LWRNfL4m8dr4Q5aKU8%2FzRKC7%2BRphSNlShmTWENxQ%2FWenf3IKdgzPMmhQn%2BN5PNB7ZhIRfC6Q7hE%2FUy5LpIEl3qDGZk6x8xPgaSMmPmoMw4Sdfyf37aES8a3pntiG6YyLPzHHLHBQcLQ8Jt15WMr71Jls%2Fo%2FUYK6kza%2BJleQi380oPYyDMIbqBkuehu03iXbtMtcjRVsDS1tFvF&X-Amz-Signature=52e8e4cb8c994ec4cb1cf9b27a927554c8ee7a125d3fe9640b6f3f2caa644f8a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PZUDIFP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBepMe6DgMW9uunhWQ4cdGVfZKVlxaQP0iwJ%2FT5t%2BItkAiAJajY4SPOUAcOU7KlX6tR%2BduJIWb68ETWlDCV5QAABEyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVrepUXsda5cmpk3PKtwDGBuW2sRy6yoSRKrAURgTuoJPvnOd6hprHjjlZSgC0mZcL5ck64Y0HknlDGGzf2GlAHVkdrfi9MzFaDavkPFC6g4bdInGtqUEgVoGflZZdWdJXcCFyK8M0OgFbyrsHwtjK5ctEmsZYJI9iHq2dARfmkN1BLlSCpQCfhJ4vvO9L%2FISDrECvmflNLC%2FCGyXmnG%2BIHk2C9TfMgl2yaBdFMHh71O0TDoW2Tlnxdfm1gwUZMN1J1uLEq1ZBlsyOMnTaTXPqmYxeNBNscIaYDRwpPURikWXV%2Fmtd0VeebO%2BwI4SSYCYBrase1Dv2lAyyrZupOjDXCcAG0gQCGSTGYXRnvsaqIlwHmub2Z%2BAxwnJUpY1g0T05aUV1OFZxyQPCblwQOlzGbRWNqH%2F05Z3FueR2ELkQXapH4BVcibtZHPQZOlUpiU4W9sRhaL0rjj4j5B40bk428%2BqUWiZkSaR8%2B9mZdtgH7eiU3i9NFpdvEApW5GNJWulg70cMOU6WW9yklViftbpRd9KENOw8iJ2YKcnpW9bBVeY2rrrmrRdx6J6hJdqCunTz7fbBWn9%2F%2BAvxJ41JQudxgsqGhCQejfuf3M2EXs0zmeTi398nmC6Nqh9fKt%2FdktZHR9lpya8VfgCaYswx7%2F9vAY6pgGPM%2B8gN7id5tgnt0LWRNfL4m8dr4Q5aKU8%2FzRKC7%2BRphSNlShmTWENxQ%2FWenf3IKdgzPMmhQn%2BN5PNB7ZhIRfC6Q7hE%2FUy5LpIEl3qDGZk6x8xPgaSMmPmoMw4Sdfyf37aES8a3pntiG6YyLPzHHLHBQcLQ8Jt15WMr71Jls%2Fo%2FUYK6kza%2BJleQi380oPYyDMIbqBkuehu03iXbtMtcjRVsDS1tFvF&X-Amz-Signature=6388a4ed22aa6555740f4ad799c967340d6c7416c4663411a5dcd5ffea36cff7&X-Amz-SignedHeaders=host&x-id=GetObject)
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


