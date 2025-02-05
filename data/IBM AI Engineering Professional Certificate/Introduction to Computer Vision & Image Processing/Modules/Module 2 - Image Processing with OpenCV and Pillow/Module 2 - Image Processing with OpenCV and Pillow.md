

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAQGOHC3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIHt5p55zHSWEY7q1VZLhORWcsq0JUIVK9EeQZ9pM7f4QAiBw3OQt640SKTCCHorUWO2tgf6K%2FZVrAeHIXCHt1DKS%2Byr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMgyQhJbnrbxQ9yiXCKtwDA97%2FUSzryqibEZj7s2GboFwJhYMuEA13VnI2MT1GjWRl2e9UwsMdb470poNBkIb1jLzl4ly2G6Cq%2BNikczhPVfc%2BMhnulEBLX5IQkD6Uh8lnoNcsxctDKzs%2FRr5PTkPPjGG6S7U%2BdlJhEKS8PjFA%2BOydatzs18k8ZQlSv9Xa%2Fi3eN7tVcnX%2F85D5M4PsVmhPZ4Rx8Tuv9%2FbAz8tHYelG7y5Bey3tWkKNQ9DXZq1%2F2vR01joZVO29cbjnKqLCT2FCQUHRyHPeCcxGmdXKJz98N51K3z%2B5tOITPNsi5slNr4gYHlH4zdHGClK4wgJDKTTKMSpL8nvk00I2u4PvZTaj9vFCD0AtRpvkLv85WcXZPY6l2RXOL0C2a66J4wxJ68A64fM5YuQh%2Fxp666YCU90MguIJnnsdRPZEVjnzj%2FS8brn%2BK9r7CxYVu%2FibmlLCKy1dMy%2BjTAKXwtS3p7StG26uxFOHjflzsPEs7sQnAuZZUQCKy5Q8EkK35C8UQbn%2Fjss%2FwOZoEedccYFCouuooFV194itDeCMgNcRpoX8vlnKpvpIkDxH4TcDJ2RcM03VH7iHB4ZdTZtvwWTVzANrQOk6CK0qoEDDON50HMdWnVyR92UFTQ4tjvie8EfHXa4wud2LvQY6pgGxF0aWFxsaZvWqLoBIzo6x7GVHbuv31ezXscyK9zZAKXwCNsDXt8OqSvCUp%2BCEwaF%2FOxv6x2u49OcoVl7MkNNfeNv10PAz7VhNnoeWzs%2BFSDfO6tIJ7177%2BUoZTfEZ9XnJo8GYkAP4UTkj4l%2BG%2BZHtXwjpkn8W9s%2BUyaTcaVjnqhiB8EPpWXLgtafz7v7Hwt8L1Y9QxTKFx0WGlE5y51ckWGcLYhN0&X-Amz-Signature=30c6192686bbeaddba4c4d299b64d106dcafd10b1b3c7ef1dc83fd84afe61161&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466434YJPAB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCPJeM0fLOJyNcIHdwIQGoHPBET10u4yJHby0lV5XedhAIgY13vagpj9I8q6IP0lpn3FaXi9RTzZ1sJwI9upRu7suoq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDPvY15owVN8CCiS99SrcAxrKr5r8s7OlVktb%2FDY92fvW8UkhhywLcsaVjg83WMxlGbqWgJ3PLUe%2BbcJG9TKKy32pun56Xl%2F6cgyChwq3wa8i2P1pHHcagkpv2fnMi4j165NHs7lElaxLwC%2Fp%2BDjXMiVstgCKTrar4JORqg0kvb65juG9LlYivuxcKWRjz9tt%2BFvLEMQ7ub3UEOxhEYQY5hPQca%2FUdAw0VN%2Bn8d%2BYePUO%2BPT6kfpdamGQCKdSwBrvmcyPCNBHYKMZxnjrIdQ1eavlHF%2BYIEIh%2BXiaJNTwF54MSbXHIxwJfozBxQn0klSF5LWeVxmG5nilsLOarTMZqxVQWaBrmGfDWoPdzPypIpvyMj7EpfrgyNzSlv69OWCjx%2FvBuXyRvoshZ0HR678AjfOACI11Oxha9YVPQhTom6GN0q1p5W%2BYpavKbj7pTmnjlUEOla%2FjDiNua9l%2FY6iOiNg%2FhR12Cymmh1dWGHLt04u%2B36JWeWfBr2dMeig%2BJBwxhypBqJPsFVywFf0LEvi86zO3xm3qauOGCg6qbmT26LGg4zeWKIZORGAv%2Bv58XyArrtTtrp3mpvcNz4lrnryldeI10LX2Yzl%2FUUrWiLvSShQc5YfdtRmFtDd1zVCzKI%2BqsgWLU75CvxcPSppWMOLdi70GOqUBI90T86pWCNWBZ5CjHnx65nF7v4VWxVTP0o8%2BAJd6B4JrnwDIIxeMoToPNxQHYRjFqqm4JqR6bL%2Fhi4McDAZgOCNwHQ31fbLHlRkzN2YOssizQIhEWGT6G58%2BVpulO4sXqMv%2FP%2BZSqMhpHbf1Th5MuBFV2x7aVEvXnT%2BEzjrBGGusJPFFP2vUexIInAB3Dwzt2PkbIhZWQyYSSYB04SCddKFqcblE&X-Amz-Signature=f072386b02dc690ca89507b2bbc0967ef2f8606ad8467b6afc8498394c096ed2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466434YJPAB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCPJeM0fLOJyNcIHdwIQGoHPBET10u4yJHby0lV5XedhAIgY13vagpj9I8q6IP0lpn3FaXi9RTzZ1sJwI9upRu7suoq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDPvY15owVN8CCiS99SrcAxrKr5r8s7OlVktb%2FDY92fvW8UkhhywLcsaVjg83WMxlGbqWgJ3PLUe%2BbcJG9TKKy32pun56Xl%2F6cgyChwq3wa8i2P1pHHcagkpv2fnMi4j165NHs7lElaxLwC%2Fp%2BDjXMiVstgCKTrar4JORqg0kvb65juG9LlYivuxcKWRjz9tt%2BFvLEMQ7ub3UEOxhEYQY5hPQca%2FUdAw0VN%2Bn8d%2BYePUO%2BPT6kfpdamGQCKdSwBrvmcyPCNBHYKMZxnjrIdQ1eavlHF%2BYIEIh%2BXiaJNTwF54MSbXHIxwJfozBxQn0klSF5LWeVxmG5nilsLOarTMZqxVQWaBrmGfDWoPdzPypIpvyMj7EpfrgyNzSlv69OWCjx%2FvBuXyRvoshZ0HR678AjfOACI11Oxha9YVPQhTom6GN0q1p5W%2BYpavKbj7pTmnjlUEOla%2FjDiNua9l%2FY6iOiNg%2FhR12Cymmh1dWGHLt04u%2B36JWeWfBr2dMeig%2BJBwxhypBqJPsFVywFf0LEvi86zO3xm3qauOGCg6qbmT26LGg4zeWKIZORGAv%2Bv58XyArrtTtrp3mpvcNz4lrnryldeI10LX2Yzl%2FUUrWiLvSShQc5YfdtRmFtDd1zVCzKI%2BqsgWLU75CvxcPSppWMOLdi70GOqUBI90T86pWCNWBZ5CjHnx65nF7v4VWxVTP0o8%2BAJd6B4JrnwDIIxeMoToPNxQHYRjFqqm4JqR6bL%2Fhi4McDAZgOCNwHQ31fbLHlRkzN2YOssizQIhEWGT6G58%2BVpulO4sXqMv%2FP%2BZSqMhpHbf1Th5MuBFV2x7aVEvXnT%2BEzjrBGGusJPFFP2vUexIInAB3Dwzt2PkbIhZWQyYSSYB04SCddKFqcblE&X-Amz-Signature=8fa17e011e053a464b9495a2786b34d657c2503d723377cce6a5ef8ae976270e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466434YJPAB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCPJeM0fLOJyNcIHdwIQGoHPBET10u4yJHby0lV5XedhAIgY13vagpj9I8q6IP0lpn3FaXi9RTzZ1sJwI9upRu7suoq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDPvY15owVN8CCiS99SrcAxrKr5r8s7OlVktb%2FDY92fvW8UkhhywLcsaVjg83WMxlGbqWgJ3PLUe%2BbcJG9TKKy32pun56Xl%2F6cgyChwq3wa8i2P1pHHcagkpv2fnMi4j165NHs7lElaxLwC%2Fp%2BDjXMiVstgCKTrar4JORqg0kvb65juG9LlYivuxcKWRjz9tt%2BFvLEMQ7ub3UEOxhEYQY5hPQca%2FUdAw0VN%2Bn8d%2BYePUO%2BPT6kfpdamGQCKdSwBrvmcyPCNBHYKMZxnjrIdQ1eavlHF%2BYIEIh%2BXiaJNTwF54MSbXHIxwJfozBxQn0klSF5LWeVxmG5nilsLOarTMZqxVQWaBrmGfDWoPdzPypIpvyMj7EpfrgyNzSlv69OWCjx%2FvBuXyRvoshZ0HR678AjfOACI11Oxha9YVPQhTom6GN0q1p5W%2BYpavKbj7pTmnjlUEOla%2FjDiNua9l%2FY6iOiNg%2FhR12Cymmh1dWGHLt04u%2B36JWeWfBr2dMeig%2BJBwxhypBqJPsFVywFf0LEvi86zO3xm3qauOGCg6qbmT26LGg4zeWKIZORGAv%2Bv58XyArrtTtrp3mpvcNz4lrnryldeI10LX2Yzl%2FUUrWiLvSShQc5YfdtRmFtDd1zVCzKI%2BqsgWLU75CvxcPSppWMOLdi70GOqUBI90T86pWCNWBZ5CjHnx65nF7v4VWxVTP0o8%2BAJd6B4JrnwDIIxeMoToPNxQHYRjFqqm4JqR6bL%2Fhi4McDAZgOCNwHQ31fbLHlRkzN2YOssizQIhEWGT6G58%2BVpulO4sXqMv%2FP%2BZSqMhpHbf1Th5MuBFV2x7aVEvXnT%2BEzjrBGGusJPFFP2vUexIInAB3Dwzt2PkbIhZWQyYSSYB04SCddKFqcblE&X-Amz-Signature=74140c224a25dd61bbcdf006536d7903e9c9d5e409f74103e08aa142facf51a7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466434YJPAB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCPJeM0fLOJyNcIHdwIQGoHPBET10u4yJHby0lV5XedhAIgY13vagpj9I8q6IP0lpn3FaXi9RTzZ1sJwI9upRu7suoq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDPvY15owVN8CCiS99SrcAxrKr5r8s7OlVktb%2FDY92fvW8UkhhywLcsaVjg83WMxlGbqWgJ3PLUe%2BbcJG9TKKy32pun56Xl%2F6cgyChwq3wa8i2P1pHHcagkpv2fnMi4j165NHs7lElaxLwC%2Fp%2BDjXMiVstgCKTrar4JORqg0kvb65juG9LlYivuxcKWRjz9tt%2BFvLEMQ7ub3UEOxhEYQY5hPQca%2FUdAw0VN%2Bn8d%2BYePUO%2BPT6kfpdamGQCKdSwBrvmcyPCNBHYKMZxnjrIdQ1eavlHF%2BYIEIh%2BXiaJNTwF54MSbXHIxwJfozBxQn0klSF5LWeVxmG5nilsLOarTMZqxVQWaBrmGfDWoPdzPypIpvyMj7EpfrgyNzSlv69OWCjx%2FvBuXyRvoshZ0HR678AjfOACI11Oxha9YVPQhTom6GN0q1p5W%2BYpavKbj7pTmnjlUEOla%2FjDiNua9l%2FY6iOiNg%2FhR12Cymmh1dWGHLt04u%2B36JWeWfBr2dMeig%2BJBwxhypBqJPsFVywFf0LEvi86zO3xm3qauOGCg6qbmT26LGg4zeWKIZORGAv%2Bv58XyArrtTtrp3mpvcNz4lrnryldeI10LX2Yzl%2FUUrWiLvSShQc5YfdtRmFtDd1zVCzKI%2BqsgWLU75CvxcPSppWMOLdi70GOqUBI90T86pWCNWBZ5CjHnx65nF7v4VWxVTP0o8%2BAJd6B4JrnwDIIxeMoToPNxQHYRjFqqm4JqR6bL%2Fhi4McDAZgOCNwHQ31fbLHlRkzN2YOssizQIhEWGT6G58%2BVpulO4sXqMv%2FP%2BZSqMhpHbf1Th5MuBFV2x7aVEvXnT%2BEzjrBGGusJPFFP2vUexIInAB3Dwzt2PkbIhZWQyYSSYB04SCddKFqcblE&X-Amz-Signature=3e3877ca0956904903606ed9bdd79a05b7cd97245b25c7a27be54ddc335d4afd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466434YJPAB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCPJeM0fLOJyNcIHdwIQGoHPBET10u4yJHby0lV5XedhAIgY13vagpj9I8q6IP0lpn3FaXi9RTzZ1sJwI9upRu7suoq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDPvY15owVN8CCiS99SrcAxrKr5r8s7OlVktb%2FDY92fvW8UkhhywLcsaVjg83WMxlGbqWgJ3PLUe%2BbcJG9TKKy32pun56Xl%2F6cgyChwq3wa8i2P1pHHcagkpv2fnMi4j165NHs7lElaxLwC%2Fp%2BDjXMiVstgCKTrar4JORqg0kvb65juG9LlYivuxcKWRjz9tt%2BFvLEMQ7ub3UEOxhEYQY5hPQca%2FUdAw0VN%2Bn8d%2BYePUO%2BPT6kfpdamGQCKdSwBrvmcyPCNBHYKMZxnjrIdQ1eavlHF%2BYIEIh%2BXiaJNTwF54MSbXHIxwJfozBxQn0klSF5LWeVxmG5nilsLOarTMZqxVQWaBrmGfDWoPdzPypIpvyMj7EpfrgyNzSlv69OWCjx%2FvBuXyRvoshZ0HR678AjfOACI11Oxha9YVPQhTom6GN0q1p5W%2BYpavKbj7pTmnjlUEOla%2FjDiNua9l%2FY6iOiNg%2FhR12Cymmh1dWGHLt04u%2B36JWeWfBr2dMeig%2BJBwxhypBqJPsFVywFf0LEvi86zO3xm3qauOGCg6qbmT26LGg4zeWKIZORGAv%2Bv58XyArrtTtrp3mpvcNz4lrnryldeI10LX2Yzl%2FUUrWiLvSShQc5YfdtRmFtDd1zVCzKI%2BqsgWLU75CvxcPSppWMOLdi70GOqUBI90T86pWCNWBZ5CjHnx65nF7v4VWxVTP0o8%2BAJd6B4JrnwDIIxeMoToPNxQHYRjFqqm4JqR6bL%2Fhi4McDAZgOCNwHQ31fbLHlRkzN2YOssizQIhEWGT6G58%2BVpulO4sXqMv%2FP%2BZSqMhpHbf1Th5MuBFV2x7aVEvXnT%2BEzjrBGGusJPFFP2vUexIInAB3Dwzt2PkbIhZWQyYSSYB04SCddKFqcblE&X-Amz-Signature=650567dd571e252eaf0f029d3b2832793739c4e92053ef36dbc70ef3745eddd4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAQGOHC3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIHt5p55zHSWEY7q1VZLhORWcsq0JUIVK9EeQZ9pM7f4QAiBw3OQt640SKTCCHorUWO2tgf6K%2FZVrAeHIXCHt1DKS%2Byr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMgyQhJbnrbxQ9yiXCKtwDA97%2FUSzryqibEZj7s2GboFwJhYMuEA13VnI2MT1GjWRl2e9UwsMdb470poNBkIb1jLzl4ly2G6Cq%2BNikczhPVfc%2BMhnulEBLX5IQkD6Uh8lnoNcsxctDKzs%2FRr5PTkPPjGG6S7U%2BdlJhEKS8PjFA%2BOydatzs18k8ZQlSv9Xa%2Fi3eN7tVcnX%2F85D5M4PsVmhPZ4Rx8Tuv9%2FbAz8tHYelG7y5Bey3tWkKNQ9DXZq1%2F2vR01joZVO29cbjnKqLCT2FCQUHRyHPeCcxGmdXKJz98N51K3z%2B5tOITPNsi5slNr4gYHlH4zdHGClK4wgJDKTTKMSpL8nvk00I2u4PvZTaj9vFCD0AtRpvkLv85WcXZPY6l2RXOL0C2a66J4wxJ68A64fM5YuQh%2Fxp666YCU90MguIJnnsdRPZEVjnzj%2FS8brn%2BK9r7CxYVu%2FibmlLCKy1dMy%2BjTAKXwtS3p7StG26uxFOHjflzsPEs7sQnAuZZUQCKy5Q8EkK35C8UQbn%2Fjss%2FwOZoEedccYFCouuooFV194itDeCMgNcRpoX8vlnKpvpIkDxH4TcDJ2RcM03VH7iHB4ZdTZtvwWTVzANrQOk6CK0qoEDDON50HMdWnVyR92UFTQ4tjvie8EfHXa4wud2LvQY6pgGxF0aWFxsaZvWqLoBIzo6x7GVHbuv31ezXscyK9zZAKXwCNsDXt8OqSvCUp%2BCEwaF%2FOxv6x2u49OcoVl7MkNNfeNv10PAz7VhNnoeWzs%2BFSDfO6tIJ7177%2BUoZTfEZ9XnJo8GYkAP4UTkj4l%2BG%2BZHtXwjpkn8W9s%2BUyaTcaVjnqhiB8EPpWXLgtafz7v7Hwt8L1Y9QxTKFx0WGlE5y51ckWGcLYhN0&X-Amz-Signature=7452779eef4008cb5999d10d804c7024b081022f56e34a691b38a872fababf43&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAQGOHC3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIHt5p55zHSWEY7q1VZLhORWcsq0JUIVK9EeQZ9pM7f4QAiBw3OQt640SKTCCHorUWO2tgf6K%2FZVrAeHIXCHt1DKS%2Byr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMgyQhJbnrbxQ9yiXCKtwDA97%2FUSzryqibEZj7s2GboFwJhYMuEA13VnI2MT1GjWRl2e9UwsMdb470poNBkIb1jLzl4ly2G6Cq%2BNikczhPVfc%2BMhnulEBLX5IQkD6Uh8lnoNcsxctDKzs%2FRr5PTkPPjGG6S7U%2BdlJhEKS8PjFA%2BOydatzs18k8ZQlSv9Xa%2Fi3eN7tVcnX%2F85D5M4PsVmhPZ4Rx8Tuv9%2FbAz8tHYelG7y5Bey3tWkKNQ9DXZq1%2F2vR01joZVO29cbjnKqLCT2FCQUHRyHPeCcxGmdXKJz98N51K3z%2B5tOITPNsi5slNr4gYHlH4zdHGClK4wgJDKTTKMSpL8nvk00I2u4PvZTaj9vFCD0AtRpvkLv85WcXZPY6l2RXOL0C2a66J4wxJ68A64fM5YuQh%2Fxp666YCU90MguIJnnsdRPZEVjnzj%2FS8brn%2BK9r7CxYVu%2FibmlLCKy1dMy%2BjTAKXwtS3p7StG26uxFOHjflzsPEs7sQnAuZZUQCKy5Q8EkK35C8UQbn%2Fjss%2FwOZoEedccYFCouuooFV194itDeCMgNcRpoX8vlnKpvpIkDxH4TcDJ2RcM03VH7iHB4ZdTZtvwWTVzANrQOk6CK0qoEDDON50HMdWnVyR92UFTQ4tjvie8EfHXa4wud2LvQY6pgGxF0aWFxsaZvWqLoBIzo6x7GVHbuv31ezXscyK9zZAKXwCNsDXt8OqSvCUp%2BCEwaF%2FOxv6x2u49OcoVl7MkNNfeNv10PAz7VhNnoeWzs%2BFSDfO6tIJ7177%2BUoZTfEZ9XnJo8GYkAP4UTkj4l%2BG%2BZHtXwjpkn8W9s%2BUyaTcaVjnqhiB8EPpWXLgtafz7v7Hwt8L1Y9QxTKFx0WGlE5y51ckWGcLYhN0&X-Amz-Signature=4078dfb9e8d56b4f65c70c8cde093605ec5cd93d690dde5c006bedd85af89aae&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAQGOHC3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIHt5p55zHSWEY7q1VZLhORWcsq0JUIVK9EeQZ9pM7f4QAiBw3OQt640SKTCCHorUWO2tgf6K%2FZVrAeHIXCHt1DKS%2Byr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMgyQhJbnrbxQ9yiXCKtwDA97%2FUSzryqibEZj7s2GboFwJhYMuEA13VnI2MT1GjWRl2e9UwsMdb470poNBkIb1jLzl4ly2G6Cq%2BNikczhPVfc%2BMhnulEBLX5IQkD6Uh8lnoNcsxctDKzs%2FRr5PTkPPjGG6S7U%2BdlJhEKS8PjFA%2BOydatzs18k8ZQlSv9Xa%2Fi3eN7tVcnX%2F85D5M4PsVmhPZ4Rx8Tuv9%2FbAz8tHYelG7y5Bey3tWkKNQ9DXZq1%2F2vR01joZVO29cbjnKqLCT2FCQUHRyHPeCcxGmdXKJz98N51K3z%2B5tOITPNsi5slNr4gYHlH4zdHGClK4wgJDKTTKMSpL8nvk00I2u4PvZTaj9vFCD0AtRpvkLv85WcXZPY6l2RXOL0C2a66J4wxJ68A64fM5YuQh%2Fxp666YCU90MguIJnnsdRPZEVjnzj%2FS8brn%2BK9r7CxYVu%2FibmlLCKy1dMy%2BjTAKXwtS3p7StG26uxFOHjflzsPEs7sQnAuZZUQCKy5Q8EkK35C8UQbn%2Fjss%2FwOZoEedccYFCouuooFV194itDeCMgNcRpoX8vlnKpvpIkDxH4TcDJ2RcM03VH7iHB4ZdTZtvwWTVzANrQOk6CK0qoEDDON50HMdWnVyR92UFTQ4tjvie8EfHXa4wud2LvQY6pgGxF0aWFxsaZvWqLoBIzo6x7GVHbuv31ezXscyK9zZAKXwCNsDXt8OqSvCUp%2BCEwaF%2FOxv6x2u49OcoVl7MkNNfeNv10PAz7VhNnoeWzs%2BFSDfO6tIJ7177%2BUoZTfEZ9XnJo8GYkAP4UTkj4l%2BG%2BZHtXwjpkn8W9s%2BUyaTcaVjnqhiB8EPpWXLgtafz7v7Hwt8L1Y9QxTKFx0WGlE5y51ckWGcLYhN0&X-Amz-Signature=71b535fb755bf055c2eb6e5560dfeecacb84c176d8ea645ca65b6253bddc49cc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAQGOHC3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIHt5p55zHSWEY7q1VZLhORWcsq0JUIVK9EeQZ9pM7f4QAiBw3OQt640SKTCCHorUWO2tgf6K%2FZVrAeHIXCHt1DKS%2Byr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMgyQhJbnrbxQ9yiXCKtwDA97%2FUSzryqibEZj7s2GboFwJhYMuEA13VnI2MT1GjWRl2e9UwsMdb470poNBkIb1jLzl4ly2G6Cq%2BNikczhPVfc%2BMhnulEBLX5IQkD6Uh8lnoNcsxctDKzs%2FRr5PTkPPjGG6S7U%2BdlJhEKS8PjFA%2BOydatzs18k8ZQlSv9Xa%2Fi3eN7tVcnX%2F85D5M4PsVmhPZ4Rx8Tuv9%2FbAz8tHYelG7y5Bey3tWkKNQ9DXZq1%2F2vR01joZVO29cbjnKqLCT2FCQUHRyHPeCcxGmdXKJz98N51K3z%2B5tOITPNsi5slNr4gYHlH4zdHGClK4wgJDKTTKMSpL8nvk00I2u4PvZTaj9vFCD0AtRpvkLv85WcXZPY6l2RXOL0C2a66J4wxJ68A64fM5YuQh%2Fxp666YCU90MguIJnnsdRPZEVjnzj%2FS8brn%2BK9r7CxYVu%2FibmlLCKy1dMy%2BjTAKXwtS3p7StG26uxFOHjflzsPEs7sQnAuZZUQCKy5Q8EkK35C8UQbn%2Fjss%2FwOZoEedccYFCouuooFV194itDeCMgNcRpoX8vlnKpvpIkDxH4TcDJ2RcM03VH7iHB4ZdTZtvwWTVzANrQOk6CK0qoEDDON50HMdWnVyR92UFTQ4tjvie8EfHXa4wud2LvQY6pgGxF0aWFxsaZvWqLoBIzo6x7GVHbuv31ezXscyK9zZAKXwCNsDXt8OqSvCUp%2BCEwaF%2FOxv6x2u49OcoVl7MkNNfeNv10PAz7VhNnoeWzs%2BFSDfO6tIJ7177%2BUoZTfEZ9XnJo8GYkAP4UTkj4l%2BG%2BZHtXwjpkn8W9s%2BUyaTcaVjnqhiB8EPpWXLgtafz7v7Hwt8L1Y9QxTKFx0WGlE5y51ckWGcLYhN0&X-Amz-Signature=d1151592b94991b5996a69def55444c1baae6dd3fe579ba78bf5f994d3167faf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAQGOHC3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIHt5p55zHSWEY7q1VZLhORWcsq0JUIVK9EeQZ9pM7f4QAiBw3OQt640SKTCCHorUWO2tgf6K%2FZVrAeHIXCHt1DKS%2Byr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMgyQhJbnrbxQ9yiXCKtwDA97%2FUSzryqibEZj7s2GboFwJhYMuEA13VnI2MT1GjWRl2e9UwsMdb470poNBkIb1jLzl4ly2G6Cq%2BNikczhPVfc%2BMhnulEBLX5IQkD6Uh8lnoNcsxctDKzs%2FRr5PTkPPjGG6S7U%2BdlJhEKS8PjFA%2BOydatzs18k8ZQlSv9Xa%2Fi3eN7tVcnX%2F85D5M4PsVmhPZ4Rx8Tuv9%2FbAz8tHYelG7y5Bey3tWkKNQ9DXZq1%2F2vR01joZVO29cbjnKqLCT2FCQUHRyHPeCcxGmdXKJz98N51K3z%2B5tOITPNsi5slNr4gYHlH4zdHGClK4wgJDKTTKMSpL8nvk00I2u4PvZTaj9vFCD0AtRpvkLv85WcXZPY6l2RXOL0C2a66J4wxJ68A64fM5YuQh%2Fxp666YCU90MguIJnnsdRPZEVjnzj%2FS8brn%2BK9r7CxYVu%2FibmlLCKy1dMy%2BjTAKXwtS3p7StG26uxFOHjflzsPEs7sQnAuZZUQCKy5Q8EkK35C8UQbn%2Fjss%2FwOZoEedccYFCouuooFV194itDeCMgNcRpoX8vlnKpvpIkDxH4TcDJ2RcM03VH7iHB4ZdTZtvwWTVzANrQOk6CK0qoEDDON50HMdWnVyR92UFTQ4tjvie8EfHXa4wud2LvQY6pgGxF0aWFxsaZvWqLoBIzo6x7GVHbuv31ezXscyK9zZAKXwCNsDXt8OqSvCUp%2BCEwaF%2FOxv6x2u49OcoVl7MkNNfeNv10PAz7VhNnoeWzs%2BFSDfO6tIJ7177%2BUoZTfEZ9XnJo8GYkAP4UTkj4l%2BG%2BZHtXwjpkn8W9s%2BUyaTcaVjnqhiB8EPpWXLgtafz7v7Hwt8L1Y9QxTKFx0WGlE5y51ckWGcLYhN0&X-Amz-Signature=5d890108798e634542475b3b28592b7afe249e3cd9a8c2f1b4f11bf1b0789ae7&X-Amz-SignedHeaders=host&x-id=GetObject)
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


