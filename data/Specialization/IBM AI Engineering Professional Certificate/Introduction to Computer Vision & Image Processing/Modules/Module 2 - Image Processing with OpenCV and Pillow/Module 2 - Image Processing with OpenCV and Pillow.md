

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627BXXT2W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIANz37tOctkKGjklfj%2Bs3fCIl7hiGArkR1PwjYTNE7rFAiEAp1qHlebgNigdaLcoO7r3lO4hzmV52mmo9MOaJJMs7v0qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGS%2FVDC9R2frNqG5yrcA8eYPBurV6Hn%2FWJPcrGycRGyuJhUphmWMAzklzh8%2BLm%2Bu%2BXmphNO5hyX%2B3xrKtGvmggpa9z4F6SdV3hiXgpspKH%2FHgs7%2FAvH5pSQ8%2Bu6FR8wGGHssFGA15Pup7KU%2BfR2seXtxlFOjQN4JNqsDKHSidCJ2NXvU35xybFlPeNHFAQg3hsAYKXYmzF5zYbhX6%2B2h%2FZO%2BjkL%2F1cfaSQLQcUuUaVsZN8wOK%2F6JIIsdU53ogsp55qkaNXRxvoJ2wbk3ofe%2FGJyUGrvFCZWTUYn5uh94qgjBf5ccb2oc9lZGLtCMJcVFYGeyTuhWKobiR2I61FS1PeI6ge%2B3DDQkfsavsI5oJLvWMZJVYtTKeCboYFceaaEDFBKvAEyqBrj7KLJrjgaUOI9szJ5UYCwvgOuiBOYhJpSX4jQmvPfDux6x%2F%2BhUpchpJanPuvqRprO19lEP1IrD0syRVa25sTm4WtLP7dd1eROEHJFbX6PhIj84bQCmGZNLt6rF6auoY3cw7FaWv9TjWNVft4X9f5Wd28yw%2FfJJolFOdyaGwaTIrVb2FauW0YpXK7NJP0MpolqcZxay%2F0vMN5cgcw4M3P6F28MehEWxpEjhuQWT%2BSZw0T9UsTgNwvqhSJEHeHejCBNewg4MInr7LwGOqUBg7sYytQiBwjpYKnVfoVyBFiSk75DE4M552DIbTXuF6pYOMHkmTQglakCbEZmIxqp6JDVLuOOmA1EZ4DnJMmHM2EjK54ZBMdps9l18j4Qxs0hltqyYlUCh%2FxtctJP1n6mXBTvuJRCk%2FJEsnDZILkUF2j0lBqq4aDuoYqbf70j9o2IrZHjd0wfOzeelMpMKiaoxijMZs71ogjHQROfFV6wLHyomqum&X-Amz-Signature=77d78fd2fa646a7ab0d5763e1d165567aaa40d9223bb5033a1889d27246ea790&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GHQK3QO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPZkxJV2Z6FfeFz4cASPSV1zzILAHjvbvXqUlPEcpcAiAjI6tBHe6As4WEuqH5%2FvSLLSztpno9fr0rBnC4JcrVSiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6aZoxyJK3g6aEUQbKtwD955k5rOl%2FQ4VVBU%2F%2B5bCREKLmZGRz4GnYipk6X21Jct4wm9B96uKppnR9or1vbszO01xFKH9Js3EsYAUEwSKXbiWbdeOujLbWbtZwDouWRIFdU%2F%2Ftd9ipD9JEIuXAJJU0hOTerAijTHDWNVRRCGoMG%2BGcbXX2IBgjlpIY5IGGxk5E%2B5chl4QBxDPfzOSp9h3vhlMPXdbWo%2FIquHyWJUwIFjNNvypyYyvWaWwGYgiSi8QcHFi0BU0PXHEbgFi69PRPjIaktYy7OauEQrPTiZBHWkXZ9tVzLaYo4ZaD51nIEcDrYcl4qcnezBaPaESCI1Zd9KSHcRL97IhkoDt19VlADqAOkSTLg6rku9EO6%2BQeLKacPCRz6GcPotzcKGAqn3a6Jo2%2BoXprla7Qo32iZ1mi7%2FHeBFXy5ZYDJUco3WerDFTTFbK5RZJ0iZcBr6vSE4%2B7VoCYf6M%2BduPjYP18eFFcPzGErkpDZuxID2LzppALMdJ4ckH5vdiHm6h9EYkzJ17o%2FazV%2FdqBrmg1A%2Fd5Vkiy6ff51fK4N8sEr8AdDki3yT6pqrQqLpaZqMORf6mbZQb6ERiDfOIwhEFOirvDTuRB%2Bwf1PG9pQLNRUgcWl4im8p%2Fsr51KChApW7MA4gw7qLsvAY6pgE8kEemdP2HPfSJl4KBw4a3KJ%2BhYy1JJJsveBYVNmblrohCuPJDvLAKwOlIM7a2BuARn5Hve9z65iOP8BqL2mtHaeENpcdi0LQZPaa5Jhf38mEgubdI8K%2BrRNvO0eoSF9bmgA0SNwi40ZeFqnb4tYBExVzhck7ref2tcXzapzE8XmajvpzTzX7hw%2Fb%2Bclhk6%2F6%2Bc6z4FZ2wQHqeio0PrZ7TfdW1uQu8&X-Amz-Signature=eb7a756617b68e56fbf4b8f48dd05e469469a05c00a5d7fbac459ee3decdcaa2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GHQK3QO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPZkxJV2Z6FfeFz4cASPSV1zzILAHjvbvXqUlPEcpcAiAjI6tBHe6As4WEuqH5%2FvSLLSztpno9fr0rBnC4JcrVSiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6aZoxyJK3g6aEUQbKtwD955k5rOl%2FQ4VVBU%2F%2B5bCREKLmZGRz4GnYipk6X21Jct4wm9B96uKppnR9or1vbszO01xFKH9Js3EsYAUEwSKXbiWbdeOujLbWbtZwDouWRIFdU%2F%2Ftd9ipD9JEIuXAJJU0hOTerAijTHDWNVRRCGoMG%2BGcbXX2IBgjlpIY5IGGxk5E%2B5chl4QBxDPfzOSp9h3vhlMPXdbWo%2FIquHyWJUwIFjNNvypyYyvWaWwGYgiSi8QcHFi0BU0PXHEbgFi69PRPjIaktYy7OauEQrPTiZBHWkXZ9tVzLaYo4ZaD51nIEcDrYcl4qcnezBaPaESCI1Zd9KSHcRL97IhkoDt19VlADqAOkSTLg6rku9EO6%2BQeLKacPCRz6GcPotzcKGAqn3a6Jo2%2BoXprla7Qo32iZ1mi7%2FHeBFXy5ZYDJUco3WerDFTTFbK5RZJ0iZcBr6vSE4%2B7VoCYf6M%2BduPjYP18eFFcPzGErkpDZuxID2LzppALMdJ4ckH5vdiHm6h9EYkzJ17o%2FazV%2FdqBrmg1A%2Fd5Vkiy6ff51fK4N8sEr8AdDki3yT6pqrQqLpaZqMORf6mbZQb6ERiDfOIwhEFOirvDTuRB%2Bwf1PG9pQLNRUgcWl4im8p%2Fsr51KChApW7MA4gw7qLsvAY6pgE8kEemdP2HPfSJl4KBw4a3KJ%2BhYy1JJJsveBYVNmblrohCuPJDvLAKwOlIM7a2BuARn5Hve9z65iOP8BqL2mtHaeENpcdi0LQZPaa5Jhf38mEgubdI8K%2BrRNvO0eoSF9bmgA0SNwi40ZeFqnb4tYBExVzhck7ref2tcXzapzE8XmajvpzTzX7hw%2Fb%2Bclhk6%2F6%2Bc6z4FZ2wQHqeio0PrZ7TfdW1uQu8&X-Amz-Signature=cf03e2ca05bb663c14d75fe87b48a7130e90c8f002ff61a7443ded19aaec188f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GHQK3QO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPZkxJV2Z6FfeFz4cASPSV1zzILAHjvbvXqUlPEcpcAiAjI6tBHe6As4WEuqH5%2FvSLLSztpno9fr0rBnC4JcrVSiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6aZoxyJK3g6aEUQbKtwD955k5rOl%2FQ4VVBU%2F%2B5bCREKLmZGRz4GnYipk6X21Jct4wm9B96uKppnR9or1vbszO01xFKH9Js3EsYAUEwSKXbiWbdeOujLbWbtZwDouWRIFdU%2F%2Ftd9ipD9JEIuXAJJU0hOTerAijTHDWNVRRCGoMG%2BGcbXX2IBgjlpIY5IGGxk5E%2B5chl4QBxDPfzOSp9h3vhlMPXdbWo%2FIquHyWJUwIFjNNvypyYyvWaWwGYgiSi8QcHFi0BU0PXHEbgFi69PRPjIaktYy7OauEQrPTiZBHWkXZ9tVzLaYo4ZaD51nIEcDrYcl4qcnezBaPaESCI1Zd9KSHcRL97IhkoDt19VlADqAOkSTLg6rku9EO6%2BQeLKacPCRz6GcPotzcKGAqn3a6Jo2%2BoXprla7Qo32iZ1mi7%2FHeBFXy5ZYDJUco3WerDFTTFbK5RZJ0iZcBr6vSE4%2B7VoCYf6M%2BduPjYP18eFFcPzGErkpDZuxID2LzppALMdJ4ckH5vdiHm6h9EYkzJ17o%2FazV%2FdqBrmg1A%2Fd5Vkiy6ff51fK4N8sEr8AdDki3yT6pqrQqLpaZqMORf6mbZQb6ERiDfOIwhEFOirvDTuRB%2Bwf1PG9pQLNRUgcWl4im8p%2Fsr51KChApW7MA4gw7qLsvAY6pgE8kEemdP2HPfSJl4KBw4a3KJ%2BhYy1JJJsveBYVNmblrohCuPJDvLAKwOlIM7a2BuARn5Hve9z65iOP8BqL2mtHaeENpcdi0LQZPaa5Jhf38mEgubdI8K%2BrRNvO0eoSF9bmgA0SNwi40ZeFqnb4tYBExVzhck7ref2tcXzapzE8XmajvpzTzX7hw%2Fb%2Bclhk6%2F6%2Bc6z4FZ2wQHqeio0PrZ7TfdW1uQu8&X-Amz-Signature=0161083e76870628fd3ee504c319b267cbddc292b84e5bc34551bf5b6b8c0037&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GHQK3QO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPZkxJV2Z6FfeFz4cASPSV1zzILAHjvbvXqUlPEcpcAiAjI6tBHe6As4WEuqH5%2FvSLLSztpno9fr0rBnC4JcrVSiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6aZoxyJK3g6aEUQbKtwD955k5rOl%2FQ4VVBU%2F%2B5bCREKLmZGRz4GnYipk6X21Jct4wm9B96uKppnR9or1vbszO01xFKH9Js3EsYAUEwSKXbiWbdeOujLbWbtZwDouWRIFdU%2F%2Ftd9ipD9JEIuXAJJU0hOTerAijTHDWNVRRCGoMG%2BGcbXX2IBgjlpIY5IGGxk5E%2B5chl4QBxDPfzOSp9h3vhlMPXdbWo%2FIquHyWJUwIFjNNvypyYyvWaWwGYgiSi8QcHFi0BU0PXHEbgFi69PRPjIaktYy7OauEQrPTiZBHWkXZ9tVzLaYo4ZaD51nIEcDrYcl4qcnezBaPaESCI1Zd9KSHcRL97IhkoDt19VlADqAOkSTLg6rku9EO6%2BQeLKacPCRz6GcPotzcKGAqn3a6Jo2%2BoXprla7Qo32iZ1mi7%2FHeBFXy5ZYDJUco3WerDFTTFbK5RZJ0iZcBr6vSE4%2B7VoCYf6M%2BduPjYP18eFFcPzGErkpDZuxID2LzppALMdJ4ckH5vdiHm6h9EYkzJ17o%2FazV%2FdqBrmg1A%2Fd5Vkiy6ff51fK4N8sEr8AdDki3yT6pqrQqLpaZqMORf6mbZQb6ERiDfOIwhEFOirvDTuRB%2Bwf1PG9pQLNRUgcWl4im8p%2Fsr51KChApW7MA4gw7qLsvAY6pgE8kEemdP2HPfSJl4KBw4a3KJ%2BhYy1JJJsveBYVNmblrohCuPJDvLAKwOlIM7a2BuARn5Hve9z65iOP8BqL2mtHaeENpcdi0LQZPaa5Jhf38mEgubdI8K%2BrRNvO0eoSF9bmgA0SNwi40ZeFqnb4tYBExVzhck7ref2tcXzapzE8XmajvpzTzX7hw%2Fb%2Bclhk6%2F6%2Bc6z4FZ2wQHqeio0PrZ7TfdW1uQu8&X-Amz-Signature=6ce2f6945ad08ed5560809ab9ab3d19f9b3cdc158e2dfce1d0907d8e428f686d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GHQK3QO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPZkxJV2Z6FfeFz4cASPSV1zzILAHjvbvXqUlPEcpcAiAjI6tBHe6As4WEuqH5%2FvSLLSztpno9fr0rBnC4JcrVSiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6aZoxyJK3g6aEUQbKtwD955k5rOl%2FQ4VVBU%2F%2B5bCREKLmZGRz4GnYipk6X21Jct4wm9B96uKppnR9or1vbszO01xFKH9Js3EsYAUEwSKXbiWbdeOujLbWbtZwDouWRIFdU%2F%2Ftd9ipD9JEIuXAJJU0hOTerAijTHDWNVRRCGoMG%2BGcbXX2IBgjlpIY5IGGxk5E%2B5chl4QBxDPfzOSp9h3vhlMPXdbWo%2FIquHyWJUwIFjNNvypyYyvWaWwGYgiSi8QcHFi0BU0PXHEbgFi69PRPjIaktYy7OauEQrPTiZBHWkXZ9tVzLaYo4ZaD51nIEcDrYcl4qcnezBaPaESCI1Zd9KSHcRL97IhkoDt19VlADqAOkSTLg6rku9EO6%2BQeLKacPCRz6GcPotzcKGAqn3a6Jo2%2BoXprla7Qo32iZ1mi7%2FHeBFXy5ZYDJUco3WerDFTTFbK5RZJ0iZcBr6vSE4%2B7VoCYf6M%2BduPjYP18eFFcPzGErkpDZuxID2LzppALMdJ4ckH5vdiHm6h9EYkzJ17o%2FazV%2FdqBrmg1A%2Fd5Vkiy6ff51fK4N8sEr8AdDki3yT6pqrQqLpaZqMORf6mbZQb6ERiDfOIwhEFOirvDTuRB%2Bwf1PG9pQLNRUgcWl4im8p%2Fsr51KChApW7MA4gw7qLsvAY6pgE8kEemdP2HPfSJl4KBw4a3KJ%2BhYy1JJJsveBYVNmblrohCuPJDvLAKwOlIM7a2BuARn5Hve9z65iOP8BqL2mtHaeENpcdi0LQZPaa5Jhf38mEgubdI8K%2BrRNvO0eoSF9bmgA0SNwi40ZeFqnb4tYBExVzhck7ref2tcXzapzE8XmajvpzTzX7hw%2Fb%2Bclhk6%2F6%2Bc6z4FZ2wQHqeio0PrZ7TfdW1uQu8&X-Amz-Signature=e114000ae76df23d34bc6ba3f0a70adebefd2e2128b653d780b0047dcb6d2335&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627BXXT2W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIANz37tOctkKGjklfj%2Bs3fCIl7hiGArkR1PwjYTNE7rFAiEAp1qHlebgNigdaLcoO7r3lO4hzmV52mmo9MOaJJMs7v0qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGS%2FVDC9R2frNqG5yrcA8eYPBurV6Hn%2FWJPcrGycRGyuJhUphmWMAzklzh8%2BLm%2Bu%2BXmphNO5hyX%2B3xrKtGvmggpa9z4F6SdV3hiXgpspKH%2FHgs7%2FAvH5pSQ8%2Bu6FR8wGGHssFGA15Pup7KU%2BfR2seXtxlFOjQN4JNqsDKHSidCJ2NXvU35xybFlPeNHFAQg3hsAYKXYmzF5zYbhX6%2B2h%2FZO%2BjkL%2F1cfaSQLQcUuUaVsZN8wOK%2F6JIIsdU53ogsp55qkaNXRxvoJ2wbk3ofe%2FGJyUGrvFCZWTUYn5uh94qgjBf5ccb2oc9lZGLtCMJcVFYGeyTuhWKobiR2I61FS1PeI6ge%2B3DDQkfsavsI5oJLvWMZJVYtTKeCboYFceaaEDFBKvAEyqBrj7KLJrjgaUOI9szJ5UYCwvgOuiBOYhJpSX4jQmvPfDux6x%2F%2BhUpchpJanPuvqRprO19lEP1IrD0syRVa25sTm4WtLP7dd1eROEHJFbX6PhIj84bQCmGZNLt6rF6auoY3cw7FaWv9TjWNVft4X9f5Wd28yw%2FfJJolFOdyaGwaTIrVb2FauW0YpXK7NJP0MpolqcZxay%2F0vMN5cgcw4M3P6F28MehEWxpEjhuQWT%2BSZw0T9UsTgNwvqhSJEHeHejCBNewg4MInr7LwGOqUBg7sYytQiBwjpYKnVfoVyBFiSk75DE4M552DIbTXuF6pYOMHkmTQglakCbEZmIxqp6JDVLuOOmA1EZ4DnJMmHM2EjK54ZBMdps9l18j4Qxs0hltqyYlUCh%2FxtctJP1n6mXBTvuJRCk%2FJEsnDZILkUF2j0lBqq4aDuoYqbf70j9o2IrZHjd0wfOzeelMpMKiaoxijMZs71ogjHQROfFV6wLHyomqum&X-Amz-Signature=9e5004e400082224c3b8be9298c541a7dc6ebbc25a8f21f958e061127bbfa60f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627BXXT2W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIANz37tOctkKGjklfj%2Bs3fCIl7hiGArkR1PwjYTNE7rFAiEAp1qHlebgNigdaLcoO7r3lO4hzmV52mmo9MOaJJMs7v0qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGS%2FVDC9R2frNqG5yrcA8eYPBurV6Hn%2FWJPcrGycRGyuJhUphmWMAzklzh8%2BLm%2Bu%2BXmphNO5hyX%2B3xrKtGvmggpa9z4F6SdV3hiXgpspKH%2FHgs7%2FAvH5pSQ8%2Bu6FR8wGGHssFGA15Pup7KU%2BfR2seXtxlFOjQN4JNqsDKHSidCJ2NXvU35xybFlPeNHFAQg3hsAYKXYmzF5zYbhX6%2B2h%2FZO%2BjkL%2F1cfaSQLQcUuUaVsZN8wOK%2F6JIIsdU53ogsp55qkaNXRxvoJ2wbk3ofe%2FGJyUGrvFCZWTUYn5uh94qgjBf5ccb2oc9lZGLtCMJcVFYGeyTuhWKobiR2I61FS1PeI6ge%2B3DDQkfsavsI5oJLvWMZJVYtTKeCboYFceaaEDFBKvAEyqBrj7KLJrjgaUOI9szJ5UYCwvgOuiBOYhJpSX4jQmvPfDux6x%2F%2BhUpchpJanPuvqRprO19lEP1IrD0syRVa25sTm4WtLP7dd1eROEHJFbX6PhIj84bQCmGZNLt6rF6auoY3cw7FaWv9TjWNVft4X9f5Wd28yw%2FfJJolFOdyaGwaTIrVb2FauW0YpXK7NJP0MpolqcZxay%2F0vMN5cgcw4M3P6F28MehEWxpEjhuQWT%2BSZw0T9UsTgNwvqhSJEHeHejCBNewg4MInr7LwGOqUBg7sYytQiBwjpYKnVfoVyBFiSk75DE4M552DIbTXuF6pYOMHkmTQglakCbEZmIxqp6JDVLuOOmA1EZ4DnJMmHM2EjK54ZBMdps9l18j4Qxs0hltqyYlUCh%2FxtctJP1n6mXBTvuJRCk%2FJEsnDZILkUF2j0lBqq4aDuoYqbf70j9o2IrZHjd0wfOzeelMpMKiaoxijMZs71ogjHQROfFV6wLHyomqum&X-Amz-Signature=24aaef64f0d8ded732f01ec92bc9d6d887d1d54eb55c9ebb1e95eaa1e389da3d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627BXXT2W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIANz37tOctkKGjklfj%2Bs3fCIl7hiGArkR1PwjYTNE7rFAiEAp1qHlebgNigdaLcoO7r3lO4hzmV52mmo9MOaJJMs7v0qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGS%2FVDC9R2frNqG5yrcA8eYPBurV6Hn%2FWJPcrGycRGyuJhUphmWMAzklzh8%2BLm%2Bu%2BXmphNO5hyX%2B3xrKtGvmggpa9z4F6SdV3hiXgpspKH%2FHgs7%2FAvH5pSQ8%2Bu6FR8wGGHssFGA15Pup7KU%2BfR2seXtxlFOjQN4JNqsDKHSidCJ2NXvU35xybFlPeNHFAQg3hsAYKXYmzF5zYbhX6%2B2h%2FZO%2BjkL%2F1cfaSQLQcUuUaVsZN8wOK%2F6JIIsdU53ogsp55qkaNXRxvoJ2wbk3ofe%2FGJyUGrvFCZWTUYn5uh94qgjBf5ccb2oc9lZGLtCMJcVFYGeyTuhWKobiR2I61FS1PeI6ge%2B3DDQkfsavsI5oJLvWMZJVYtTKeCboYFceaaEDFBKvAEyqBrj7KLJrjgaUOI9szJ5UYCwvgOuiBOYhJpSX4jQmvPfDux6x%2F%2BhUpchpJanPuvqRprO19lEP1IrD0syRVa25sTm4WtLP7dd1eROEHJFbX6PhIj84bQCmGZNLt6rF6auoY3cw7FaWv9TjWNVft4X9f5Wd28yw%2FfJJolFOdyaGwaTIrVb2FauW0YpXK7NJP0MpolqcZxay%2F0vMN5cgcw4M3P6F28MehEWxpEjhuQWT%2BSZw0T9UsTgNwvqhSJEHeHejCBNewg4MInr7LwGOqUBg7sYytQiBwjpYKnVfoVyBFiSk75DE4M552DIbTXuF6pYOMHkmTQglakCbEZmIxqp6JDVLuOOmA1EZ4DnJMmHM2EjK54ZBMdps9l18j4Qxs0hltqyYlUCh%2FxtctJP1n6mXBTvuJRCk%2FJEsnDZILkUF2j0lBqq4aDuoYqbf70j9o2IrZHjd0wfOzeelMpMKiaoxijMZs71ogjHQROfFV6wLHyomqum&X-Amz-Signature=85338d8e5c6d35ee3527ce931ac863677ff277d91654036fb3fe76207d4e2d5c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627BXXT2W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIANz37tOctkKGjklfj%2Bs3fCIl7hiGArkR1PwjYTNE7rFAiEAp1qHlebgNigdaLcoO7r3lO4hzmV52mmo9MOaJJMs7v0qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGS%2FVDC9R2frNqG5yrcA8eYPBurV6Hn%2FWJPcrGycRGyuJhUphmWMAzklzh8%2BLm%2Bu%2BXmphNO5hyX%2B3xrKtGvmggpa9z4F6SdV3hiXgpspKH%2FHgs7%2FAvH5pSQ8%2Bu6FR8wGGHssFGA15Pup7KU%2BfR2seXtxlFOjQN4JNqsDKHSidCJ2NXvU35xybFlPeNHFAQg3hsAYKXYmzF5zYbhX6%2B2h%2FZO%2BjkL%2F1cfaSQLQcUuUaVsZN8wOK%2F6JIIsdU53ogsp55qkaNXRxvoJ2wbk3ofe%2FGJyUGrvFCZWTUYn5uh94qgjBf5ccb2oc9lZGLtCMJcVFYGeyTuhWKobiR2I61FS1PeI6ge%2B3DDQkfsavsI5oJLvWMZJVYtTKeCboYFceaaEDFBKvAEyqBrj7KLJrjgaUOI9szJ5UYCwvgOuiBOYhJpSX4jQmvPfDux6x%2F%2BhUpchpJanPuvqRprO19lEP1IrD0syRVa25sTm4WtLP7dd1eROEHJFbX6PhIj84bQCmGZNLt6rF6auoY3cw7FaWv9TjWNVft4X9f5Wd28yw%2FfJJolFOdyaGwaTIrVb2FauW0YpXK7NJP0MpolqcZxay%2F0vMN5cgcw4M3P6F28MehEWxpEjhuQWT%2BSZw0T9UsTgNwvqhSJEHeHejCBNewg4MInr7LwGOqUBg7sYytQiBwjpYKnVfoVyBFiSk75DE4M552DIbTXuF6pYOMHkmTQglakCbEZmIxqp6JDVLuOOmA1EZ4DnJMmHM2EjK54ZBMdps9l18j4Qxs0hltqyYlUCh%2FxtctJP1n6mXBTvuJRCk%2FJEsnDZILkUF2j0lBqq4aDuoYqbf70j9o2IrZHjd0wfOzeelMpMKiaoxijMZs71ogjHQROfFV6wLHyomqum&X-Amz-Signature=379d4f2ac42b6e3540d84be24b6b7f79faa27458c9af9e57851fb4a2e6bf6c0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627BXXT2W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIANz37tOctkKGjklfj%2Bs3fCIl7hiGArkR1PwjYTNE7rFAiEAp1qHlebgNigdaLcoO7r3lO4hzmV52mmo9MOaJJMs7v0qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGS%2FVDC9R2frNqG5yrcA8eYPBurV6Hn%2FWJPcrGycRGyuJhUphmWMAzklzh8%2BLm%2Bu%2BXmphNO5hyX%2B3xrKtGvmggpa9z4F6SdV3hiXgpspKH%2FHgs7%2FAvH5pSQ8%2Bu6FR8wGGHssFGA15Pup7KU%2BfR2seXtxlFOjQN4JNqsDKHSidCJ2NXvU35xybFlPeNHFAQg3hsAYKXYmzF5zYbhX6%2B2h%2FZO%2BjkL%2F1cfaSQLQcUuUaVsZN8wOK%2F6JIIsdU53ogsp55qkaNXRxvoJ2wbk3ofe%2FGJyUGrvFCZWTUYn5uh94qgjBf5ccb2oc9lZGLtCMJcVFYGeyTuhWKobiR2I61FS1PeI6ge%2B3DDQkfsavsI5oJLvWMZJVYtTKeCboYFceaaEDFBKvAEyqBrj7KLJrjgaUOI9szJ5UYCwvgOuiBOYhJpSX4jQmvPfDux6x%2F%2BhUpchpJanPuvqRprO19lEP1IrD0syRVa25sTm4WtLP7dd1eROEHJFbX6PhIj84bQCmGZNLt6rF6auoY3cw7FaWv9TjWNVft4X9f5Wd28yw%2FfJJolFOdyaGwaTIrVb2FauW0YpXK7NJP0MpolqcZxay%2F0vMN5cgcw4M3P6F28MehEWxpEjhuQWT%2BSZw0T9UsTgNwvqhSJEHeHejCBNewg4MInr7LwGOqUBg7sYytQiBwjpYKnVfoVyBFiSk75DE4M552DIbTXuF6pYOMHkmTQglakCbEZmIxqp6JDVLuOOmA1EZ4DnJMmHM2EjK54ZBMdps9l18j4Qxs0hltqyYlUCh%2FxtctJP1n6mXBTvuJRCk%2FJEsnDZILkUF2j0lBqq4aDuoYqbf70j9o2IrZHjd0wfOzeelMpMKiaoxijMZs71ogjHQROfFV6wLHyomqum&X-Amz-Signature=d10cfd1c05b8433d2b55708facfc3dc26cd958354876ce8fdd75d8da3d89a6b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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


