

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VKVLKN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC4y%2FM0WbV5GTVYRbidgbNTq1twbWJPfJgP21fNjGTpJwIgNEsE7u%2FF7BmwNRksdvhqeatZ0RuquOucEan2q%2Bfy%2FZcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLvhx7bZH8ESc2qP1yrcA7pdqXpHNmZSpGjV3iei%2B1GW4CyKkMsbHeuDLbF1sgx%2FUkpW4Jli5G4%2BZXZQv5p7WEA086OMhIjYe0t656j0AiYfx854jhDQcDzUKdsfK7yhjIcYIFBhZUomsday1fZY%2FPhpxfho6FuzkvuC1OQI41vBD%2FJukk5sV%2Bqxxy6TWmbxaE%2FnvaUbv5F%2F0s%2BQNxF0FBbNnz0c1AeA%2FyU5fsND4IVRlFl9FUavH7f%2FKfCNLb%2FZElWMrgRsUlAvfBBx3iyDqfFsubBcgPZWi0wcvM5UnId1gX3PMSbU1PRCOUMd1XNH2rPBA5i9M8Y92qip5DnCCIxSf%2BxALNajewp3u2uf3aWi9lHSZzUAYRiVQHn7IWJaQn1DoOzVNkgQbk5LbYE3pRx9uYKG4wVtCYOjsIl8o2ZDnddRHvXshC2Sww%2BkRR4csxtaUpFTnB9UD1DIzK6wWHOSp4N0QpqEKF1NRJEP6LMuSnZgXlLi7RndAH7KGEitKgKR4Hu54zQse4vQadDskWEcHJn5CiyQ%2BynB8fOLVY2F5Yvv92LQQ4nLFdEW0aYc%2B0EgBQNDh3OnZW2Ayz3iqg1XcCVHp%2F032u7NmiHrb6rbH4PH1E3J7iwUj%2BTSncEsn8jBVGKxdYhwXSy6MODMir0GOqUBClDw8vcvf73qq2fOPaILY8k%2BZNIYrpfytdy%2BUsBbvT2%2Fj4Zc7gJ3hHUm1tgG0qe7n9dBSByYyVX0vDHc3qO9%2FayOjcd3UcdRS5R2HyaEMashXoDvtID2gCysrN4DKR7i2a%2FmgAqiIbwvSH5Bv0kD9GLRuC4cgatdMvddEW64rNvK7bgY6PxNWtNjqWRaQTQSnk6Sm1HLTny0XQIyOj2ehA5WaZdn&X-Amz-Signature=c4ce1e0255d1aa82131e4c64f1620bc8beb3a6d0efb56c8cc880742dae55cc9a&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y2PFYPX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCUCv4bWG5L8vNZjKbVYFj2c048cUbsUga%2BKgKMXZZfSAIga508BQ1%2FuA6iE8ND7h4mXRI1R5dEscVeyVMolhZTb0gq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDGvW4HjKVZxedJIemyrcA1fpuZeUkBK4c4OQNjF%2F%2B7k6wuNJM5C2hHU7XzJnvvErc7M3X8KeESMikiDyqQrxWoQT%2BfTFTxiaB9hYSJGDN7Sw%2BQFk7%2B4TzlmQi6Nfl2MA7plOQvinOHmC3TAF7QvNG2pIeOPhAX0EOn64n0UL7HmDPQQuCOXupgrpnOm4rGnuimAjd0U%2FVU3PbFHXb4WPn7DS8ffpEzHjmOKwDwLHNJ3yY2iiLZ9%2FRiRMKgsuZXYKOJIcWICLB4yl3cgVMpyy%2BrS6tg9YMc2xOZxFPgODEogTDoysZEyrR6QmW3%2FyQ2VZaEHQXgDAQNYrlSFW9NX1hYDM0UES6AZxMnpVAvfjHAy5QPv34PawDPGks2uqR2tuous5IzHe9Z8NJ856ycttxAUbMUX%2B48keIlKqSyIqEFQr%2F7YTB%2FCmUTWeTzwraLXbnLF%2BGPSg5GcuDLPJhMZl9RXclsOc%2FRbrGDW%2BcGn%2BU5mpxUl94c6JTh7QqKcmlGxTMEIWhOq85WucjyNLRyNqtdFTIWDb%2BYcwfWmvfHbh%2Baf0kzyadRNcFKWrpM3xUMzsVocHLNjGXBBrlSETO7wu2gPzfAPviU3awTuU74hOo2yq6L3G0fItwoGXDlszSWoPdJjsc98X5u70lZTbMNnNir0GOqUBT9d0yS10vSm52Kz%2BjvajETZnii4CFBz0BV4zP4PW%2F%2BiFEA6Y7sV9%2BjpEYHrtAiMVks7EybTgN3d9MoTA5brdWqdFrEXCld4acp87FaYdQz3dHO%2FCZaco2IjzQ4XaoA3yfdYJW%2Fl5JIqwMMA99Gqu3lMiCV3r8e5JcSeAt8S%2BDB378gAwjzyJQK3MCeHkEnud6fYUftEUO8qekX9xKUIESsYPQjVz&X-Amz-Signature=c59acdeebfb3e100e6118d7eaffa21f85e8660a5acb6402b560b0cc89fc733f2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y2PFYPX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCUCv4bWG5L8vNZjKbVYFj2c048cUbsUga%2BKgKMXZZfSAIga508BQ1%2FuA6iE8ND7h4mXRI1R5dEscVeyVMolhZTb0gq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDGvW4HjKVZxedJIemyrcA1fpuZeUkBK4c4OQNjF%2F%2B7k6wuNJM5C2hHU7XzJnvvErc7M3X8KeESMikiDyqQrxWoQT%2BfTFTxiaB9hYSJGDN7Sw%2BQFk7%2B4TzlmQi6Nfl2MA7plOQvinOHmC3TAF7QvNG2pIeOPhAX0EOn64n0UL7HmDPQQuCOXupgrpnOm4rGnuimAjd0U%2FVU3PbFHXb4WPn7DS8ffpEzHjmOKwDwLHNJ3yY2iiLZ9%2FRiRMKgsuZXYKOJIcWICLB4yl3cgVMpyy%2BrS6tg9YMc2xOZxFPgODEogTDoysZEyrR6QmW3%2FyQ2VZaEHQXgDAQNYrlSFW9NX1hYDM0UES6AZxMnpVAvfjHAy5QPv34PawDPGks2uqR2tuous5IzHe9Z8NJ856ycttxAUbMUX%2B48keIlKqSyIqEFQr%2F7YTB%2FCmUTWeTzwraLXbnLF%2BGPSg5GcuDLPJhMZl9RXclsOc%2FRbrGDW%2BcGn%2BU5mpxUl94c6JTh7QqKcmlGxTMEIWhOq85WucjyNLRyNqtdFTIWDb%2BYcwfWmvfHbh%2Baf0kzyadRNcFKWrpM3xUMzsVocHLNjGXBBrlSETO7wu2gPzfAPviU3awTuU74hOo2yq6L3G0fItwoGXDlszSWoPdJjsc98X5u70lZTbMNnNir0GOqUBT9d0yS10vSm52Kz%2BjvajETZnii4CFBz0BV4zP4PW%2F%2BiFEA6Y7sV9%2BjpEYHrtAiMVks7EybTgN3d9MoTA5brdWqdFrEXCld4acp87FaYdQz3dHO%2FCZaco2IjzQ4XaoA3yfdYJW%2Fl5JIqwMMA99Gqu3lMiCV3r8e5JcSeAt8S%2BDB378gAwjzyJQK3MCeHkEnud6fYUftEUO8qekX9xKUIESsYPQjVz&X-Amz-Signature=b1b751a0df01815ea5ff1c6da13851c4480611a7b987f039d4791070d7d89110&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y2PFYPX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCUCv4bWG5L8vNZjKbVYFj2c048cUbsUga%2BKgKMXZZfSAIga508BQ1%2FuA6iE8ND7h4mXRI1R5dEscVeyVMolhZTb0gq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDGvW4HjKVZxedJIemyrcA1fpuZeUkBK4c4OQNjF%2F%2B7k6wuNJM5C2hHU7XzJnvvErc7M3X8KeESMikiDyqQrxWoQT%2BfTFTxiaB9hYSJGDN7Sw%2BQFk7%2B4TzlmQi6Nfl2MA7plOQvinOHmC3TAF7QvNG2pIeOPhAX0EOn64n0UL7HmDPQQuCOXupgrpnOm4rGnuimAjd0U%2FVU3PbFHXb4WPn7DS8ffpEzHjmOKwDwLHNJ3yY2iiLZ9%2FRiRMKgsuZXYKOJIcWICLB4yl3cgVMpyy%2BrS6tg9YMc2xOZxFPgODEogTDoysZEyrR6QmW3%2FyQ2VZaEHQXgDAQNYrlSFW9NX1hYDM0UES6AZxMnpVAvfjHAy5QPv34PawDPGks2uqR2tuous5IzHe9Z8NJ856ycttxAUbMUX%2B48keIlKqSyIqEFQr%2F7YTB%2FCmUTWeTzwraLXbnLF%2BGPSg5GcuDLPJhMZl9RXclsOc%2FRbrGDW%2BcGn%2BU5mpxUl94c6JTh7QqKcmlGxTMEIWhOq85WucjyNLRyNqtdFTIWDb%2BYcwfWmvfHbh%2Baf0kzyadRNcFKWrpM3xUMzsVocHLNjGXBBrlSETO7wu2gPzfAPviU3awTuU74hOo2yq6L3G0fItwoGXDlszSWoPdJjsc98X5u70lZTbMNnNir0GOqUBT9d0yS10vSm52Kz%2BjvajETZnii4CFBz0BV4zP4PW%2F%2BiFEA6Y7sV9%2BjpEYHrtAiMVks7EybTgN3d9MoTA5brdWqdFrEXCld4acp87FaYdQz3dHO%2FCZaco2IjzQ4XaoA3yfdYJW%2Fl5JIqwMMA99Gqu3lMiCV3r8e5JcSeAt8S%2BDB378gAwjzyJQK3MCeHkEnud6fYUftEUO8qekX9xKUIESsYPQjVz&X-Amz-Signature=72f0ff200bb1f5e92726e6c7145e719f0c64677a017459b6efaaed8852ded262&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y2PFYPX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCUCv4bWG5L8vNZjKbVYFj2c048cUbsUga%2BKgKMXZZfSAIga508BQ1%2FuA6iE8ND7h4mXRI1R5dEscVeyVMolhZTb0gq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDGvW4HjKVZxedJIemyrcA1fpuZeUkBK4c4OQNjF%2F%2B7k6wuNJM5C2hHU7XzJnvvErc7M3X8KeESMikiDyqQrxWoQT%2BfTFTxiaB9hYSJGDN7Sw%2BQFk7%2B4TzlmQi6Nfl2MA7plOQvinOHmC3TAF7QvNG2pIeOPhAX0EOn64n0UL7HmDPQQuCOXupgrpnOm4rGnuimAjd0U%2FVU3PbFHXb4WPn7DS8ffpEzHjmOKwDwLHNJ3yY2iiLZ9%2FRiRMKgsuZXYKOJIcWICLB4yl3cgVMpyy%2BrS6tg9YMc2xOZxFPgODEogTDoysZEyrR6QmW3%2FyQ2VZaEHQXgDAQNYrlSFW9NX1hYDM0UES6AZxMnpVAvfjHAy5QPv34PawDPGks2uqR2tuous5IzHe9Z8NJ856ycttxAUbMUX%2B48keIlKqSyIqEFQr%2F7YTB%2FCmUTWeTzwraLXbnLF%2BGPSg5GcuDLPJhMZl9RXclsOc%2FRbrGDW%2BcGn%2BU5mpxUl94c6JTh7QqKcmlGxTMEIWhOq85WucjyNLRyNqtdFTIWDb%2BYcwfWmvfHbh%2Baf0kzyadRNcFKWrpM3xUMzsVocHLNjGXBBrlSETO7wu2gPzfAPviU3awTuU74hOo2yq6L3G0fItwoGXDlszSWoPdJjsc98X5u70lZTbMNnNir0GOqUBT9d0yS10vSm52Kz%2BjvajETZnii4CFBz0BV4zP4PW%2F%2BiFEA6Y7sV9%2BjpEYHrtAiMVks7EybTgN3d9MoTA5brdWqdFrEXCld4acp87FaYdQz3dHO%2FCZaco2IjzQ4XaoA3yfdYJW%2Fl5JIqwMMA99Gqu3lMiCV3r8e5JcSeAt8S%2BDB378gAwjzyJQK3MCeHkEnud6fYUftEUO8qekX9xKUIESsYPQjVz&X-Amz-Signature=9a64ec01a9c19a1711ca2ec0b6f273ffbf139219bf3b3800a2798f5846c67a71&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y2PFYPX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCUCv4bWG5L8vNZjKbVYFj2c048cUbsUga%2BKgKMXZZfSAIga508BQ1%2FuA6iE8ND7h4mXRI1R5dEscVeyVMolhZTb0gq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDGvW4HjKVZxedJIemyrcA1fpuZeUkBK4c4OQNjF%2F%2B7k6wuNJM5C2hHU7XzJnvvErc7M3X8KeESMikiDyqQrxWoQT%2BfTFTxiaB9hYSJGDN7Sw%2BQFk7%2B4TzlmQi6Nfl2MA7plOQvinOHmC3TAF7QvNG2pIeOPhAX0EOn64n0UL7HmDPQQuCOXupgrpnOm4rGnuimAjd0U%2FVU3PbFHXb4WPn7DS8ffpEzHjmOKwDwLHNJ3yY2iiLZ9%2FRiRMKgsuZXYKOJIcWICLB4yl3cgVMpyy%2BrS6tg9YMc2xOZxFPgODEogTDoysZEyrR6QmW3%2FyQ2VZaEHQXgDAQNYrlSFW9NX1hYDM0UES6AZxMnpVAvfjHAy5QPv34PawDPGks2uqR2tuous5IzHe9Z8NJ856ycttxAUbMUX%2B48keIlKqSyIqEFQr%2F7YTB%2FCmUTWeTzwraLXbnLF%2BGPSg5GcuDLPJhMZl9RXclsOc%2FRbrGDW%2BcGn%2BU5mpxUl94c6JTh7QqKcmlGxTMEIWhOq85WucjyNLRyNqtdFTIWDb%2BYcwfWmvfHbh%2Baf0kzyadRNcFKWrpM3xUMzsVocHLNjGXBBrlSETO7wu2gPzfAPviU3awTuU74hOo2yq6L3G0fItwoGXDlszSWoPdJjsc98X5u70lZTbMNnNir0GOqUBT9d0yS10vSm52Kz%2BjvajETZnii4CFBz0BV4zP4PW%2F%2BiFEA6Y7sV9%2BjpEYHrtAiMVks7EybTgN3d9MoTA5brdWqdFrEXCld4acp87FaYdQz3dHO%2FCZaco2IjzQ4XaoA3yfdYJW%2Fl5JIqwMMA99Gqu3lMiCV3r8e5JcSeAt8S%2BDB378gAwjzyJQK3MCeHkEnud6fYUftEUO8qekX9xKUIESsYPQjVz&X-Amz-Signature=c383c564d22cb3f2c4018db27a9afe4d0b270ec84f6d20e1e36e9ab9cde82991&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VKVLKN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC4y%2FM0WbV5GTVYRbidgbNTq1twbWJPfJgP21fNjGTpJwIgNEsE7u%2FF7BmwNRksdvhqeatZ0RuquOucEan2q%2Bfy%2FZcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLvhx7bZH8ESc2qP1yrcA7pdqXpHNmZSpGjV3iei%2B1GW4CyKkMsbHeuDLbF1sgx%2FUkpW4Jli5G4%2BZXZQv5p7WEA086OMhIjYe0t656j0AiYfx854jhDQcDzUKdsfK7yhjIcYIFBhZUomsday1fZY%2FPhpxfho6FuzkvuC1OQI41vBD%2FJukk5sV%2Bqxxy6TWmbxaE%2FnvaUbv5F%2F0s%2BQNxF0FBbNnz0c1AeA%2FyU5fsND4IVRlFl9FUavH7f%2FKfCNLb%2FZElWMrgRsUlAvfBBx3iyDqfFsubBcgPZWi0wcvM5UnId1gX3PMSbU1PRCOUMd1XNH2rPBA5i9M8Y92qip5DnCCIxSf%2BxALNajewp3u2uf3aWi9lHSZzUAYRiVQHn7IWJaQn1DoOzVNkgQbk5LbYE3pRx9uYKG4wVtCYOjsIl8o2ZDnddRHvXshC2Sww%2BkRR4csxtaUpFTnB9UD1DIzK6wWHOSp4N0QpqEKF1NRJEP6LMuSnZgXlLi7RndAH7KGEitKgKR4Hu54zQse4vQadDskWEcHJn5CiyQ%2BynB8fOLVY2F5Yvv92LQQ4nLFdEW0aYc%2B0EgBQNDh3OnZW2Ayz3iqg1XcCVHp%2F032u7NmiHrb6rbH4PH1E3J7iwUj%2BTSncEsn8jBVGKxdYhwXSy6MODMir0GOqUBClDw8vcvf73qq2fOPaILY8k%2BZNIYrpfytdy%2BUsBbvT2%2Fj4Zc7gJ3hHUm1tgG0qe7n9dBSByYyVX0vDHc3qO9%2FayOjcd3UcdRS5R2HyaEMashXoDvtID2gCysrN4DKR7i2a%2FmgAqiIbwvSH5Bv0kD9GLRuC4cgatdMvddEW64rNvK7bgY6PxNWtNjqWRaQTQSnk6Sm1HLTny0XQIyOj2ehA5WaZdn&X-Amz-Signature=ddb4f256e14bc7627cb637c248a8ad4a9e97497cae802d987661feebd4df9a5f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VKVLKN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC4y%2FM0WbV5GTVYRbidgbNTq1twbWJPfJgP21fNjGTpJwIgNEsE7u%2FF7BmwNRksdvhqeatZ0RuquOucEan2q%2Bfy%2FZcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLvhx7bZH8ESc2qP1yrcA7pdqXpHNmZSpGjV3iei%2B1GW4CyKkMsbHeuDLbF1sgx%2FUkpW4Jli5G4%2BZXZQv5p7WEA086OMhIjYe0t656j0AiYfx854jhDQcDzUKdsfK7yhjIcYIFBhZUomsday1fZY%2FPhpxfho6FuzkvuC1OQI41vBD%2FJukk5sV%2Bqxxy6TWmbxaE%2FnvaUbv5F%2F0s%2BQNxF0FBbNnz0c1AeA%2FyU5fsND4IVRlFl9FUavH7f%2FKfCNLb%2FZElWMrgRsUlAvfBBx3iyDqfFsubBcgPZWi0wcvM5UnId1gX3PMSbU1PRCOUMd1XNH2rPBA5i9M8Y92qip5DnCCIxSf%2BxALNajewp3u2uf3aWi9lHSZzUAYRiVQHn7IWJaQn1DoOzVNkgQbk5LbYE3pRx9uYKG4wVtCYOjsIl8o2ZDnddRHvXshC2Sww%2BkRR4csxtaUpFTnB9UD1DIzK6wWHOSp4N0QpqEKF1NRJEP6LMuSnZgXlLi7RndAH7KGEitKgKR4Hu54zQse4vQadDskWEcHJn5CiyQ%2BynB8fOLVY2F5Yvv92LQQ4nLFdEW0aYc%2B0EgBQNDh3OnZW2Ayz3iqg1XcCVHp%2F032u7NmiHrb6rbH4PH1E3J7iwUj%2BTSncEsn8jBVGKxdYhwXSy6MODMir0GOqUBClDw8vcvf73qq2fOPaILY8k%2BZNIYrpfytdy%2BUsBbvT2%2Fj4Zc7gJ3hHUm1tgG0qe7n9dBSByYyVX0vDHc3qO9%2FayOjcd3UcdRS5R2HyaEMashXoDvtID2gCysrN4DKR7i2a%2FmgAqiIbwvSH5Bv0kD9GLRuC4cgatdMvddEW64rNvK7bgY6PxNWtNjqWRaQTQSnk6Sm1HLTny0XQIyOj2ehA5WaZdn&X-Amz-Signature=8ba53b69042c64b89a45d01097c161227e8fe3cf8db29735597222e5eaaed04f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VKVLKN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC4y%2FM0WbV5GTVYRbidgbNTq1twbWJPfJgP21fNjGTpJwIgNEsE7u%2FF7BmwNRksdvhqeatZ0RuquOucEan2q%2Bfy%2FZcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLvhx7bZH8ESc2qP1yrcA7pdqXpHNmZSpGjV3iei%2B1GW4CyKkMsbHeuDLbF1sgx%2FUkpW4Jli5G4%2BZXZQv5p7WEA086OMhIjYe0t656j0AiYfx854jhDQcDzUKdsfK7yhjIcYIFBhZUomsday1fZY%2FPhpxfho6FuzkvuC1OQI41vBD%2FJukk5sV%2Bqxxy6TWmbxaE%2FnvaUbv5F%2F0s%2BQNxF0FBbNnz0c1AeA%2FyU5fsND4IVRlFl9FUavH7f%2FKfCNLb%2FZElWMrgRsUlAvfBBx3iyDqfFsubBcgPZWi0wcvM5UnId1gX3PMSbU1PRCOUMd1XNH2rPBA5i9M8Y92qip5DnCCIxSf%2BxALNajewp3u2uf3aWi9lHSZzUAYRiVQHn7IWJaQn1DoOzVNkgQbk5LbYE3pRx9uYKG4wVtCYOjsIl8o2ZDnddRHvXshC2Sww%2BkRR4csxtaUpFTnB9UD1DIzK6wWHOSp4N0QpqEKF1NRJEP6LMuSnZgXlLi7RndAH7KGEitKgKR4Hu54zQse4vQadDskWEcHJn5CiyQ%2BynB8fOLVY2F5Yvv92LQQ4nLFdEW0aYc%2B0EgBQNDh3OnZW2Ayz3iqg1XcCVHp%2F032u7NmiHrb6rbH4PH1E3J7iwUj%2BTSncEsn8jBVGKxdYhwXSy6MODMir0GOqUBClDw8vcvf73qq2fOPaILY8k%2BZNIYrpfytdy%2BUsBbvT2%2Fj4Zc7gJ3hHUm1tgG0qe7n9dBSByYyVX0vDHc3qO9%2FayOjcd3UcdRS5R2HyaEMashXoDvtID2gCysrN4DKR7i2a%2FmgAqiIbwvSH5Bv0kD9GLRuC4cgatdMvddEW64rNvK7bgY6PxNWtNjqWRaQTQSnk6Sm1HLTny0XQIyOj2ehA5WaZdn&X-Amz-Signature=0702a6757b3f627a3cfede963dd9fe8a54bf93d394d21eb5092a09ea4682307c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VKVLKN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC4y%2FM0WbV5GTVYRbidgbNTq1twbWJPfJgP21fNjGTpJwIgNEsE7u%2FF7BmwNRksdvhqeatZ0RuquOucEan2q%2Bfy%2FZcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLvhx7bZH8ESc2qP1yrcA7pdqXpHNmZSpGjV3iei%2B1GW4CyKkMsbHeuDLbF1sgx%2FUkpW4Jli5G4%2BZXZQv5p7WEA086OMhIjYe0t656j0AiYfx854jhDQcDzUKdsfK7yhjIcYIFBhZUomsday1fZY%2FPhpxfho6FuzkvuC1OQI41vBD%2FJukk5sV%2Bqxxy6TWmbxaE%2FnvaUbv5F%2F0s%2BQNxF0FBbNnz0c1AeA%2FyU5fsND4IVRlFl9FUavH7f%2FKfCNLb%2FZElWMrgRsUlAvfBBx3iyDqfFsubBcgPZWi0wcvM5UnId1gX3PMSbU1PRCOUMd1XNH2rPBA5i9M8Y92qip5DnCCIxSf%2BxALNajewp3u2uf3aWi9lHSZzUAYRiVQHn7IWJaQn1DoOzVNkgQbk5LbYE3pRx9uYKG4wVtCYOjsIl8o2ZDnddRHvXshC2Sww%2BkRR4csxtaUpFTnB9UD1DIzK6wWHOSp4N0QpqEKF1NRJEP6LMuSnZgXlLi7RndAH7KGEitKgKR4Hu54zQse4vQadDskWEcHJn5CiyQ%2BynB8fOLVY2F5Yvv92LQQ4nLFdEW0aYc%2B0EgBQNDh3OnZW2Ayz3iqg1XcCVHp%2F032u7NmiHrb6rbH4PH1E3J7iwUj%2BTSncEsn8jBVGKxdYhwXSy6MODMir0GOqUBClDw8vcvf73qq2fOPaILY8k%2BZNIYrpfytdy%2BUsBbvT2%2Fj4Zc7gJ3hHUm1tgG0qe7n9dBSByYyVX0vDHc3qO9%2FayOjcd3UcdRS5R2HyaEMashXoDvtID2gCysrN4DKR7i2a%2FmgAqiIbwvSH5Bv0kD9GLRuC4cgatdMvddEW64rNvK7bgY6PxNWtNjqWRaQTQSnk6Sm1HLTny0XQIyOj2ehA5WaZdn&X-Amz-Signature=86405b1fb85d42ecd38179fa9c0dfda4f2adda517786f08c1612ce988b5cba0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6VKVLKN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC4y%2FM0WbV5GTVYRbidgbNTq1twbWJPfJgP21fNjGTpJwIgNEsE7u%2FF7BmwNRksdvhqeatZ0RuquOucEan2q%2Bfy%2FZcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLvhx7bZH8ESc2qP1yrcA7pdqXpHNmZSpGjV3iei%2B1GW4CyKkMsbHeuDLbF1sgx%2FUkpW4Jli5G4%2BZXZQv5p7WEA086OMhIjYe0t656j0AiYfx854jhDQcDzUKdsfK7yhjIcYIFBhZUomsday1fZY%2FPhpxfho6FuzkvuC1OQI41vBD%2FJukk5sV%2Bqxxy6TWmbxaE%2FnvaUbv5F%2F0s%2BQNxF0FBbNnz0c1AeA%2FyU5fsND4IVRlFl9FUavH7f%2FKfCNLb%2FZElWMrgRsUlAvfBBx3iyDqfFsubBcgPZWi0wcvM5UnId1gX3PMSbU1PRCOUMd1XNH2rPBA5i9M8Y92qip5DnCCIxSf%2BxALNajewp3u2uf3aWi9lHSZzUAYRiVQHn7IWJaQn1DoOzVNkgQbk5LbYE3pRx9uYKG4wVtCYOjsIl8o2ZDnddRHvXshC2Sww%2BkRR4csxtaUpFTnB9UD1DIzK6wWHOSp4N0QpqEKF1NRJEP6LMuSnZgXlLi7RndAH7KGEitKgKR4Hu54zQse4vQadDskWEcHJn5CiyQ%2BynB8fOLVY2F5Yvv92LQQ4nLFdEW0aYc%2B0EgBQNDh3OnZW2Ayz3iqg1XcCVHp%2F032u7NmiHrb6rbH4PH1E3J7iwUj%2BTSncEsn8jBVGKxdYhwXSy6MODMir0GOqUBClDw8vcvf73qq2fOPaILY8k%2BZNIYrpfytdy%2BUsBbvT2%2Fj4Zc7gJ3hHUm1tgG0qe7n9dBSByYyVX0vDHc3qO9%2FayOjcd3UcdRS5R2HyaEMashXoDvtID2gCysrN4DKR7i2a%2FmgAqiIbwvSH5Bv0kD9GLRuC4cgatdMvddEW64rNvK7bgY6PxNWtNjqWRaQTQSnk6Sm1HLTny0XQIyOj2ehA5WaZdn&X-Amz-Signature=1f8fb50906bb31cc4702a9ca436ede4a5f7f173f29922fd0aa8faae976e6e646&X-Amz-SignedHeaders=host&x-id=GetObject)
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


