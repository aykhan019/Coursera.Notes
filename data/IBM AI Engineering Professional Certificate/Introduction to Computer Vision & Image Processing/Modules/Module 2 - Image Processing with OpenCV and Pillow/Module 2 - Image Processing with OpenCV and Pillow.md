

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQYPGRSB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEMGnR4czz%2F114b5%2FxZJH0RyTS00HWXvCvKnWwQkdFyFAiEAplcJ1lqJ%2B%2BTgf6TmxqajdNl%2BkQIAQxxYWeNqQAdBPvkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDM%2BjL6aFpkFTxYQs3CrcA3z2w0HR67Ei0v6NRuxrQIWusgF9T8xIOqKpL6lmiaqrnjxcnJMGf1aghA%2FHvWPN0SEcHBj27K6I%2BgDm18841uHZJ3yO1IFkOzBKsngiAShiselYFkargdLg3vT9Z3QiisS01sCBVpC9lXjOrFFW0J1JtMyF9EXSUZAofj%2FyRBPcedZxFIpYfULVdSt3Y7XH2Rl5PCInMO77n2FFeq%2Bogf10XKVb%2F3Wfd0SOc3XFmU4g6buUhZhegYhAjnNqyNAKSbzTKepBYRbsjltNknSo3L3PclrH9L26kTzQ1XRwSNCkZSyy8OKqtaVjQ3Bu6xwu5Bm12Ro2cbNEh05D6gO3xGoEpjXcoHMrIoG2rJIyEGX27fZK%2FtXNfJpiERpjhWQvj6h6XBl27XgX3h%2F7VYh7Mt1KxfDjGXfq8mVwzJI0zEYq5aVck5WouI1NrooetOQzoxpR8butVcEx%2BU1SHTSjhbqXK6%2FicjfWqIuf4jCOgIuEQqUj8OsahZSHYDaOiWdOs%2B1h9l9xx3HkshHjI2f7UXkVRmrerDch3PPe85R9Sq5L3nCdorrSfSBiP94XYRPV9ZO60lOBqyT8VdzN%2BXpsojBjWzXClOk7nvVXE%2Fu1AQe2KJiYPpZrgMPcLJpFMJ7zgb0GOqUBZ6UUvsyEsKWL6SoEC9jFfGiOrkWX1IhzBxi1pVZFr%2BSNw%2BVJkwZwM4tYmaFfNSYFy5s%2BTDPiOiK2yACx7ciHDLfYeIUmiOcMB3Sth2tR4ahknWVL%2FJnPvHp2gEi7MxEOZcM0CLisW0bif715pwjraziiu13UdEQfNM6HZ7Wfx3on59U1DFtWL0eB3f619JVaIzkJpQQuTFJi0YHtQrVYlk04z%2FGl&X-Amz-Signature=449f227c45e9947d39e0abb713ff82310ed10c10413218ae9005ee511376462e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OBBZOJI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNutC60vvM755rkVw6Wef1jK8NYF3EX1Wqb4fcsmG6GAiBDd3QwT4nf2aP6GcRRFIDItLVA9u2IT4mUWkwJSJpWbCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2FcwGj0IS5xnMvA4JKtwD14u%2BLcmb0Mv41Y3ZxJGpY89eiKdqAm8yUxjM4MqOQEZy2I%2BiUkqYlevNu0rIKbWoEmWXFnh2M590uEDzivCh%2FSYFtZoq7%2Fv5ffSr3xkBgsj6Msxep1gWeGcGxwvA7JRJ2U5zWzASHR1L4cVmGEEhztkLluqGPHQxQoGvI00IjbYBdtrlSr65XypptCxduErgswuDfECQ95sj3ySo11f4wssSF8uPLVeE08sa7UU2vovd5w%2Fqcd3Eut60VrLAi8LG4nUir93eF3KatFIBHOYna3Pc6SGuGrcwzeH%2BBchQLyzvlaodnTDl%2BNssGkgVz9LJrTfERGUtvetL0%2BA11GfTHZ8pi4tX7iL4dZTVYJ5cJo2DJyw8pVwefKgh7Jig2wydtqYGZFhBuCgYfhsZzWxjleIkJsofW2kXtXnG8Q4CeNNoZbOnoqevulCO5swoW9Aj3llyz6FD0%2BjpRQSuAd0qkVs9ogU8g1JDxoW%2FQoayjyytf67MCcfxhBIbsqwM4Rot00abZLX5Ayycjb4Ueyya239OQg3oZZkafSeVYI0HsUYdf4O0yGu3naS5iiasNMBywvXUQrLRu9L3K6%2Ft0sk0T%2B9YrLldrWVeJ08a90dt1OqL2TBrlQexI93KsT8wzfOBvQY6pgFV%2BNBX9ekZonic8%2BNMG2IKlNiY7p5KwcsJJ8SoB5ltaZWKE6H3J8lioHYf5c5glTnsidNIaEYo0YJSzO2RgXiIGLj6P34FLOqf061uYA%2BdxOS4eiPq2RtkDo7GWuOE%2FVer0lqtretOeyMdiBHfBqk32GvS3GQPUJReginlx6sIySRWMGGSySSmYu4kDEXO0wfRSLkBmnZpjpO%2BjpLjbuqI8KEvStGA&X-Amz-Signature=7564c55c2b242545994b850745c496a5026c73a5e2ef65f1de903b4287e93eea&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OBBZOJI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNutC60vvM755rkVw6Wef1jK8NYF3EX1Wqb4fcsmG6GAiBDd3QwT4nf2aP6GcRRFIDItLVA9u2IT4mUWkwJSJpWbCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2FcwGj0IS5xnMvA4JKtwD14u%2BLcmb0Mv41Y3ZxJGpY89eiKdqAm8yUxjM4MqOQEZy2I%2BiUkqYlevNu0rIKbWoEmWXFnh2M590uEDzivCh%2FSYFtZoq7%2Fv5ffSr3xkBgsj6Msxep1gWeGcGxwvA7JRJ2U5zWzASHR1L4cVmGEEhztkLluqGPHQxQoGvI00IjbYBdtrlSr65XypptCxduErgswuDfECQ95sj3ySo11f4wssSF8uPLVeE08sa7UU2vovd5w%2Fqcd3Eut60VrLAi8LG4nUir93eF3KatFIBHOYna3Pc6SGuGrcwzeH%2BBchQLyzvlaodnTDl%2BNssGkgVz9LJrTfERGUtvetL0%2BA11GfTHZ8pi4tX7iL4dZTVYJ5cJo2DJyw8pVwefKgh7Jig2wydtqYGZFhBuCgYfhsZzWxjleIkJsofW2kXtXnG8Q4CeNNoZbOnoqevulCO5swoW9Aj3llyz6FD0%2BjpRQSuAd0qkVs9ogU8g1JDxoW%2FQoayjyytf67MCcfxhBIbsqwM4Rot00abZLX5Ayycjb4Ueyya239OQg3oZZkafSeVYI0HsUYdf4O0yGu3naS5iiasNMBywvXUQrLRu9L3K6%2Ft0sk0T%2B9YrLldrWVeJ08a90dt1OqL2TBrlQexI93KsT8wzfOBvQY6pgFV%2BNBX9ekZonic8%2BNMG2IKlNiY7p5KwcsJJ8SoB5ltaZWKE6H3J8lioHYf5c5glTnsidNIaEYo0YJSzO2RgXiIGLj6P34FLOqf061uYA%2BdxOS4eiPq2RtkDo7GWuOE%2FVer0lqtretOeyMdiBHfBqk32GvS3GQPUJReginlx6sIySRWMGGSySSmYu4kDEXO0wfRSLkBmnZpjpO%2BjpLjbuqI8KEvStGA&X-Amz-Signature=0fbb29f876b5051bb20299e43da26a95c39e412aecbed6173419eb0f7f14d215&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OBBZOJI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNutC60vvM755rkVw6Wef1jK8NYF3EX1Wqb4fcsmG6GAiBDd3QwT4nf2aP6GcRRFIDItLVA9u2IT4mUWkwJSJpWbCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2FcwGj0IS5xnMvA4JKtwD14u%2BLcmb0Mv41Y3ZxJGpY89eiKdqAm8yUxjM4MqOQEZy2I%2BiUkqYlevNu0rIKbWoEmWXFnh2M590uEDzivCh%2FSYFtZoq7%2Fv5ffSr3xkBgsj6Msxep1gWeGcGxwvA7JRJ2U5zWzASHR1L4cVmGEEhztkLluqGPHQxQoGvI00IjbYBdtrlSr65XypptCxduErgswuDfECQ95sj3ySo11f4wssSF8uPLVeE08sa7UU2vovd5w%2Fqcd3Eut60VrLAi8LG4nUir93eF3KatFIBHOYna3Pc6SGuGrcwzeH%2BBchQLyzvlaodnTDl%2BNssGkgVz9LJrTfERGUtvetL0%2BA11GfTHZ8pi4tX7iL4dZTVYJ5cJo2DJyw8pVwefKgh7Jig2wydtqYGZFhBuCgYfhsZzWxjleIkJsofW2kXtXnG8Q4CeNNoZbOnoqevulCO5swoW9Aj3llyz6FD0%2BjpRQSuAd0qkVs9ogU8g1JDxoW%2FQoayjyytf67MCcfxhBIbsqwM4Rot00abZLX5Ayycjb4Ueyya239OQg3oZZkafSeVYI0HsUYdf4O0yGu3naS5iiasNMBywvXUQrLRu9L3K6%2Ft0sk0T%2B9YrLldrWVeJ08a90dt1OqL2TBrlQexI93KsT8wzfOBvQY6pgFV%2BNBX9ekZonic8%2BNMG2IKlNiY7p5KwcsJJ8SoB5ltaZWKE6H3J8lioHYf5c5glTnsidNIaEYo0YJSzO2RgXiIGLj6P34FLOqf061uYA%2BdxOS4eiPq2RtkDo7GWuOE%2FVer0lqtretOeyMdiBHfBqk32GvS3GQPUJReginlx6sIySRWMGGSySSmYu4kDEXO0wfRSLkBmnZpjpO%2BjpLjbuqI8KEvStGA&X-Amz-Signature=37b341fb5f8a7365ef6f42c460e641a5851c67eb9c1531226285c7fbfd9fe7f8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OBBZOJI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNutC60vvM755rkVw6Wef1jK8NYF3EX1Wqb4fcsmG6GAiBDd3QwT4nf2aP6GcRRFIDItLVA9u2IT4mUWkwJSJpWbCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2FcwGj0IS5xnMvA4JKtwD14u%2BLcmb0Mv41Y3ZxJGpY89eiKdqAm8yUxjM4MqOQEZy2I%2BiUkqYlevNu0rIKbWoEmWXFnh2M590uEDzivCh%2FSYFtZoq7%2Fv5ffSr3xkBgsj6Msxep1gWeGcGxwvA7JRJ2U5zWzASHR1L4cVmGEEhztkLluqGPHQxQoGvI00IjbYBdtrlSr65XypptCxduErgswuDfECQ95sj3ySo11f4wssSF8uPLVeE08sa7UU2vovd5w%2Fqcd3Eut60VrLAi8LG4nUir93eF3KatFIBHOYna3Pc6SGuGrcwzeH%2BBchQLyzvlaodnTDl%2BNssGkgVz9LJrTfERGUtvetL0%2BA11GfTHZ8pi4tX7iL4dZTVYJ5cJo2DJyw8pVwefKgh7Jig2wydtqYGZFhBuCgYfhsZzWxjleIkJsofW2kXtXnG8Q4CeNNoZbOnoqevulCO5swoW9Aj3llyz6FD0%2BjpRQSuAd0qkVs9ogU8g1JDxoW%2FQoayjyytf67MCcfxhBIbsqwM4Rot00abZLX5Ayycjb4Ueyya239OQg3oZZkafSeVYI0HsUYdf4O0yGu3naS5iiasNMBywvXUQrLRu9L3K6%2Ft0sk0T%2B9YrLldrWVeJ08a90dt1OqL2TBrlQexI93KsT8wzfOBvQY6pgFV%2BNBX9ekZonic8%2BNMG2IKlNiY7p5KwcsJJ8SoB5ltaZWKE6H3J8lioHYf5c5glTnsidNIaEYo0YJSzO2RgXiIGLj6P34FLOqf061uYA%2BdxOS4eiPq2RtkDo7GWuOE%2FVer0lqtretOeyMdiBHfBqk32GvS3GQPUJReginlx6sIySRWMGGSySSmYu4kDEXO0wfRSLkBmnZpjpO%2BjpLjbuqI8KEvStGA&X-Amz-Signature=b872a81d49bd74b3cc569c7d4377857a3072c95b26d193bd7995b57347bc1045&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OBBZOJI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNutC60vvM755rkVw6Wef1jK8NYF3EX1Wqb4fcsmG6GAiBDd3QwT4nf2aP6GcRRFIDItLVA9u2IT4mUWkwJSJpWbCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM%2FcwGj0IS5xnMvA4JKtwD14u%2BLcmb0Mv41Y3ZxJGpY89eiKdqAm8yUxjM4MqOQEZy2I%2BiUkqYlevNu0rIKbWoEmWXFnh2M590uEDzivCh%2FSYFtZoq7%2Fv5ffSr3xkBgsj6Msxep1gWeGcGxwvA7JRJ2U5zWzASHR1L4cVmGEEhztkLluqGPHQxQoGvI00IjbYBdtrlSr65XypptCxduErgswuDfECQ95sj3ySo11f4wssSF8uPLVeE08sa7UU2vovd5w%2Fqcd3Eut60VrLAi8LG4nUir93eF3KatFIBHOYna3Pc6SGuGrcwzeH%2BBchQLyzvlaodnTDl%2BNssGkgVz9LJrTfERGUtvetL0%2BA11GfTHZ8pi4tX7iL4dZTVYJ5cJo2DJyw8pVwefKgh7Jig2wydtqYGZFhBuCgYfhsZzWxjleIkJsofW2kXtXnG8Q4CeNNoZbOnoqevulCO5swoW9Aj3llyz6FD0%2BjpRQSuAd0qkVs9ogU8g1JDxoW%2FQoayjyytf67MCcfxhBIbsqwM4Rot00abZLX5Ayycjb4Ueyya239OQg3oZZkafSeVYI0HsUYdf4O0yGu3naS5iiasNMBywvXUQrLRu9L3K6%2Ft0sk0T%2B9YrLldrWVeJ08a90dt1OqL2TBrlQexI93KsT8wzfOBvQY6pgFV%2BNBX9ekZonic8%2BNMG2IKlNiY7p5KwcsJJ8SoB5ltaZWKE6H3J8lioHYf5c5glTnsidNIaEYo0YJSzO2RgXiIGLj6P34FLOqf061uYA%2BdxOS4eiPq2RtkDo7GWuOE%2FVer0lqtretOeyMdiBHfBqk32GvS3GQPUJReginlx6sIySRWMGGSySSmYu4kDEXO0wfRSLkBmnZpjpO%2BjpLjbuqI8KEvStGA&X-Amz-Signature=3e8c95b9c79115a00c5cca592fb59fb9468a6ba3d197dd0b116f08006f6f92e9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQYPGRSB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEMGnR4czz%2F114b5%2FxZJH0RyTS00HWXvCvKnWwQkdFyFAiEAplcJ1lqJ%2B%2BTgf6TmxqajdNl%2BkQIAQxxYWeNqQAdBPvkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDM%2BjL6aFpkFTxYQs3CrcA3z2w0HR67Ei0v6NRuxrQIWusgF9T8xIOqKpL6lmiaqrnjxcnJMGf1aghA%2FHvWPN0SEcHBj27K6I%2BgDm18841uHZJ3yO1IFkOzBKsngiAShiselYFkargdLg3vT9Z3QiisS01sCBVpC9lXjOrFFW0J1JtMyF9EXSUZAofj%2FyRBPcedZxFIpYfULVdSt3Y7XH2Rl5PCInMO77n2FFeq%2Bogf10XKVb%2F3Wfd0SOc3XFmU4g6buUhZhegYhAjnNqyNAKSbzTKepBYRbsjltNknSo3L3PclrH9L26kTzQ1XRwSNCkZSyy8OKqtaVjQ3Bu6xwu5Bm12Ro2cbNEh05D6gO3xGoEpjXcoHMrIoG2rJIyEGX27fZK%2FtXNfJpiERpjhWQvj6h6XBl27XgX3h%2F7VYh7Mt1KxfDjGXfq8mVwzJI0zEYq5aVck5WouI1NrooetOQzoxpR8butVcEx%2BU1SHTSjhbqXK6%2FicjfWqIuf4jCOgIuEQqUj8OsahZSHYDaOiWdOs%2B1h9l9xx3HkshHjI2f7UXkVRmrerDch3PPe85R9Sq5L3nCdorrSfSBiP94XYRPV9ZO60lOBqyT8VdzN%2BXpsojBjWzXClOk7nvVXE%2Fu1AQe2KJiYPpZrgMPcLJpFMJ7zgb0GOqUBZ6UUvsyEsKWL6SoEC9jFfGiOrkWX1IhzBxi1pVZFr%2BSNw%2BVJkwZwM4tYmaFfNSYFy5s%2BTDPiOiK2yACx7ciHDLfYeIUmiOcMB3Sth2tR4ahknWVL%2FJnPvHp2gEi7MxEOZcM0CLisW0bif715pwjraziiu13UdEQfNM6HZ7Wfx3on59U1DFtWL0eB3f619JVaIzkJpQQuTFJi0YHtQrVYlk04z%2FGl&X-Amz-Signature=f4ba0fcc7df8ae88a288536dfd34acffd482d2685a0f63bc33ccc5cd7f2ed5c8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQYPGRSB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEMGnR4czz%2F114b5%2FxZJH0RyTS00HWXvCvKnWwQkdFyFAiEAplcJ1lqJ%2B%2BTgf6TmxqajdNl%2BkQIAQxxYWeNqQAdBPvkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDM%2BjL6aFpkFTxYQs3CrcA3z2w0HR67Ei0v6NRuxrQIWusgF9T8xIOqKpL6lmiaqrnjxcnJMGf1aghA%2FHvWPN0SEcHBj27K6I%2BgDm18841uHZJ3yO1IFkOzBKsngiAShiselYFkargdLg3vT9Z3QiisS01sCBVpC9lXjOrFFW0J1JtMyF9EXSUZAofj%2FyRBPcedZxFIpYfULVdSt3Y7XH2Rl5PCInMO77n2FFeq%2Bogf10XKVb%2F3Wfd0SOc3XFmU4g6buUhZhegYhAjnNqyNAKSbzTKepBYRbsjltNknSo3L3PclrH9L26kTzQ1XRwSNCkZSyy8OKqtaVjQ3Bu6xwu5Bm12Ro2cbNEh05D6gO3xGoEpjXcoHMrIoG2rJIyEGX27fZK%2FtXNfJpiERpjhWQvj6h6XBl27XgX3h%2F7VYh7Mt1KxfDjGXfq8mVwzJI0zEYq5aVck5WouI1NrooetOQzoxpR8butVcEx%2BU1SHTSjhbqXK6%2FicjfWqIuf4jCOgIuEQqUj8OsahZSHYDaOiWdOs%2B1h9l9xx3HkshHjI2f7UXkVRmrerDch3PPe85R9Sq5L3nCdorrSfSBiP94XYRPV9ZO60lOBqyT8VdzN%2BXpsojBjWzXClOk7nvVXE%2Fu1AQe2KJiYPpZrgMPcLJpFMJ7zgb0GOqUBZ6UUvsyEsKWL6SoEC9jFfGiOrkWX1IhzBxi1pVZFr%2BSNw%2BVJkwZwM4tYmaFfNSYFy5s%2BTDPiOiK2yACx7ciHDLfYeIUmiOcMB3Sth2tR4ahknWVL%2FJnPvHp2gEi7MxEOZcM0CLisW0bif715pwjraziiu13UdEQfNM6HZ7Wfx3on59U1DFtWL0eB3f619JVaIzkJpQQuTFJi0YHtQrVYlk04z%2FGl&X-Amz-Signature=f03d213533902ab38367e38e87e7fc2098feaa4f12d0a41cfec3f107822ed30f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQYPGRSB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEMGnR4czz%2F114b5%2FxZJH0RyTS00HWXvCvKnWwQkdFyFAiEAplcJ1lqJ%2B%2BTgf6TmxqajdNl%2BkQIAQxxYWeNqQAdBPvkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDM%2BjL6aFpkFTxYQs3CrcA3z2w0HR67Ei0v6NRuxrQIWusgF9T8xIOqKpL6lmiaqrnjxcnJMGf1aghA%2FHvWPN0SEcHBj27K6I%2BgDm18841uHZJ3yO1IFkOzBKsngiAShiselYFkargdLg3vT9Z3QiisS01sCBVpC9lXjOrFFW0J1JtMyF9EXSUZAofj%2FyRBPcedZxFIpYfULVdSt3Y7XH2Rl5PCInMO77n2FFeq%2Bogf10XKVb%2F3Wfd0SOc3XFmU4g6buUhZhegYhAjnNqyNAKSbzTKepBYRbsjltNknSo3L3PclrH9L26kTzQ1XRwSNCkZSyy8OKqtaVjQ3Bu6xwu5Bm12Ro2cbNEh05D6gO3xGoEpjXcoHMrIoG2rJIyEGX27fZK%2FtXNfJpiERpjhWQvj6h6XBl27XgX3h%2F7VYh7Mt1KxfDjGXfq8mVwzJI0zEYq5aVck5WouI1NrooetOQzoxpR8butVcEx%2BU1SHTSjhbqXK6%2FicjfWqIuf4jCOgIuEQqUj8OsahZSHYDaOiWdOs%2B1h9l9xx3HkshHjI2f7UXkVRmrerDch3PPe85R9Sq5L3nCdorrSfSBiP94XYRPV9ZO60lOBqyT8VdzN%2BXpsojBjWzXClOk7nvVXE%2Fu1AQe2KJiYPpZrgMPcLJpFMJ7zgb0GOqUBZ6UUvsyEsKWL6SoEC9jFfGiOrkWX1IhzBxi1pVZFr%2BSNw%2BVJkwZwM4tYmaFfNSYFy5s%2BTDPiOiK2yACx7ciHDLfYeIUmiOcMB3Sth2tR4ahknWVL%2FJnPvHp2gEi7MxEOZcM0CLisW0bif715pwjraziiu13UdEQfNM6HZ7Wfx3on59U1DFtWL0eB3f619JVaIzkJpQQuTFJi0YHtQrVYlk04z%2FGl&X-Amz-Signature=4f73d29ff6085f3e0474b3b5795270464189b63bb647f62504427c6713b61818&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQYPGRSB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEMGnR4czz%2F114b5%2FxZJH0RyTS00HWXvCvKnWwQkdFyFAiEAplcJ1lqJ%2B%2BTgf6TmxqajdNl%2BkQIAQxxYWeNqQAdBPvkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDM%2BjL6aFpkFTxYQs3CrcA3z2w0HR67Ei0v6NRuxrQIWusgF9T8xIOqKpL6lmiaqrnjxcnJMGf1aghA%2FHvWPN0SEcHBj27K6I%2BgDm18841uHZJ3yO1IFkOzBKsngiAShiselYFkargdLg3vT9Z3QiisS01sCBVpC9lXjOrFFW0J1JtMyF9EXSUZAofj%2FyRBPcedZxFIpYfULVdSt3Y7XH2Rl5PCInMO77n2FFeq%2Bogf10XKVb%2F3Wfd0SOc3XFmU4g6buUhZhegYhAjnNqyNAKSbzTKepBYRbsjltNknSo3L3PclrH9L26kTzQ1XRwSNCkZSyy8OKqtaVjQ3Bu6xwu5Bm12Ro2cbNEh05D6gO3xGoEpjXcoHMrIoG2rJIyEGX27fZK%2FtXNfJpiERpjhWQvj6h6XBl27XgX3h%2F7VYh7Mt1KxfDjGXfq8mVwzJI0zEYq5aVck5WouI1NrooetOQzoxpR8butVcEx%2BU1SHTSjhbqXK6%2FicjfWqIuf4jCOgIuEQqUj8OsahZSHYDaOiWdOs%2B1h9l9xx3HkshHjI2f7UXkVRmrerDch3PPe85R9Sq5L3nCdorrSfSBiP94XYRPV9ZO60lOBqyT8VdzN%2BXpsojBjWzXClOk7nvVXE%2Fu1AQe2KJiYPpZrgMPcLJpFMJ7zgb0GOqUBZ6UUvsyEsKWL6SoEC9jFfGiOrkWX1IhzBxi1pVZFr%2BSNw%2BVJkwZwM4tYmaFfNSYFy5s%2BTDPiOiK2yACx7ciHDLfYeIUmiOcMB3Sth2tR4ahknWVL%2FJnPvHp2gEi7MxEOZcM0CLisW0bif715pwjraziiu13UdEQfNM6HZ7Wfx3on59U1DFtWL0eB3f619JVaIzkJpQQuTFJi0YHtQrVYlk04z%2FGl&X-Amz-Signature=7434d9eeca6f11da427bda3d585b6fc3db8a6182e7a335a22936fa408759e050&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQYPGRSB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEMGnR4czz%2F114b5%2FxZJH0RyTS00HWXvCvKnWwQkdFyFAiEAplcJ1lqJ%2B%2BTgf6TmxqajdNl%2BkQIAQxxYWeNqQAdBPvkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDM%2BjL6aFpkFTxYQs3CrcA3z2w0HR67Ei0v6NRuxrQIWusgF9T8xIOqKpL6lmiaqrnjxcnJMGf1aghA%2FHvWPN0SEcHBj27K6I%2BgDm18841uHZJ3yO1IFkOzBKsngiAShiselYFkargdLg3vT9Z3QiisS01sCBVpC9lXjOrFFW0J1JtMyF9EXSUZAofj%2FyRBPcedZxFIpYfULVdSt3Y7XH2Rl5PCInMO77n2FFeq%2Bogf10XKVb%2F3Wfd0SOc3XFmU4g6buUhZhegYhAjnNqyNAKSbzTKepBYRbsjltNknSo3L3PclrH9L26kTzQ1XRwSNCkZSyy8OKqtaVjQ3Bu6xwu5Bm12Ro2cbNEh05D6gO3xGoEpjXcoHMrIoG2rJIyEGX27fZK%2FtXNfJpiERpjhWQvj6h6XBl27XgX3h%2F7VYh7Mt1KxfDjGXfq8mVwzJI0zEYq5aVck5WouI1NrooetOQzoxpR8butVcEx%2BU1SHTSjhbqXK6%2FicjfWqIuf4jCOgIuEQqUj8OsahZSHYDaOiWdOs%2B1h9l9xx3HkshHjI2f7UXkVRmrerDch3PPe85R9Sq5L3nCdorrSfSBiP94XYRPV9ZO60lOBqyT8VdzN%2BXpsojBjWzXClOk7nvVXE%2Fu1AQe2KJiYPpZrgMPcLJpFMJ7zgb0GOqUBZ6UUvsyEsKWL6SoEC9jFfGiOrkWX1IhzBxi1pVZFr%2BSNw%2BVJkwZwM4tYmaFfNSYFy5s%2BTDPiOiK2yACx7ciHDLfYeIUmiOcMB3Sth2tR4ahknWVL%2FJnPvHp2gEi7MxEOZcM0CLisW0bif715pwjraziiu13UdEQfNM6HZ7Wfx3on59U1DFtWL0eB3f619JVaIzkJpQQuTFJi0YHtQrVYlk04z%2FGl&X-Amz-Signature=dfa88c77b7a72dc768f726fd182279e1ad11dd0b5d35a88387018d6a0274752e&X-Amz-SignedHeaders=host&x-id=GetObject)
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


