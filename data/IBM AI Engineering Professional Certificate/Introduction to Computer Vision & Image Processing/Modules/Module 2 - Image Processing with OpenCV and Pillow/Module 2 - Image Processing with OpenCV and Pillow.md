

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XO2FDR4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQC0D7em9ERTu5v6tA%2FAoLiEFNV09R0BfLxa6pEDB2yypQIgNI5n%2BVavZUYr8OGvaH9ow8%2Fdhyn8F8ZyWRp8fzm1BuAq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOLSKph3PXR%2BalAgCCrcA0Fg2KNmpI%2F2QfuI30hUhGhN7ExcBRJ%2F3w2oaDGgQVUNY%2By0RivYMOsbFg32h8%2Bf3gC4eeZZslRc0RIq286jnUB6obGGNcFGhOAWVUUJMRfMQzMLItWZHMP8EZ4wtDbhNwJ98YxyC%2BS8NHc6IsKAT8aLw0pq9J9OBddRecaZhGEdcSnRXk9A43OwDdjGKr%2F3Xbf%2B93KZMmxw9Zfq%2F09icohicGWpDLuyVDTEkZw%2FpOKBcyOcmOnVAM9ZM2tzVg0M2IpNcoqsWTIi5ZDzEW4T0RbjUHVry%2FwE84qrfoQlCk6qmzBgwKC4vP2Nd821rNjCyGHjuhGBSJUF27hRj82lGTdMWwxViKs%2FMpa0hiSQPCzNIID%2FeoPD9o69NALgyYbMS%2BA3LHqnnPU5s9mre7R7UbNGqPe6HmavsqioE6RpWf4%2FYVmgLjsFNWA0Sf5lRL2%2FquhfoN1y0XHAUi3CZt%2FSmYBEauU%2BRmXpBIUGjOMn10FfN%2BrbZWX1ixgKDS5Udt8VuJHEbjUgO4IQkLB0xhZysilLOMPzsTuvNTNjlvGK9LzDTp6K8kokjp1b2Lg0u%2BLFgqaiOU%2BHfyMoHS1VhAQPQ%2B82DkmJHCRgReySAFs0P6qg7ZhMk7iVf01NhF3yMNTRk70GOqUBm8%2FqKMK8uwAisHM9lrg660pBUfQXs81netqzuiOest2zb%2FVUhdPfO9KhWD8W6iEJS%2Bxjb7A4A6aLEUD7nzE8NrYX9Kug%2BlSZnM%2BzBu%2FpBXSzynyJins02OeBT%2Bfbc%2FfNekA4yF3SJ67vt4W0q2QPhXtOeDbpxvL5L7zFOqUYpKFck7ZtZlOZ60vynoa%2Br67eDTH1biF5y42OBrVuNDKMX6FZ0%2B2P&X-Amz-Signature=85e886f2a692bb1f1873bf014aa27b16035776a04a9d1ba879e091a892647707&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRSOZ7PC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDHRjiviaT4I7uBK5mqlMRK7KzbF0XGyzG8LXLMak4E%2FgIgKDKOFSaHZ%2BKboeBygD%2FfS9rgbLJl1ULEw2xBBDswrMsq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOfNotOYqkjt7ibVLCrcA0Ue8T8438gGPfnfo4%2BjswKGp8B9Ki8is3CUKRfqRsnxQtZDbz%2Fr3Le86csihdLmAe5vMxl%2BgzvBDK%2FbP3KK4HuuEW9JytNH8K%2Bkhzji36uw2Ah8aJv%2BIAmLaUFDjwQBufnkcgh%2Bu8P8clof5S9GHpNp78LIp5pbW%2BFYn6ZkFztXtHWanyb86HZgm%2FBO%2B0%2FnRbkdaeSTuRj%2B9xJWI0rMYg6cSszPYT9N7tkAV41h5HQ6%2FWRKasDzCzRiPfLdpEbXNuMZf%2FBMhtBVH0ofjeTUXsl3bPMpp1cJFlba8Xe%2BmZdWNV178jY1MA%2B1y0wboNDGfsAwdrbrQDwliOIQJK7WgEvCKIJV%2BWzadHwuglVPsxnkIG5s9yCziIxdGmS5VmnIZSYJJF4UeC7u4Jvn4%2BPSGsk5vJEOr5Y7JdS2b0qNUEredl7jIA9C6nuvwomxmw%2FOaZE7qQFYgNCkuQunnSsdxGyhQZQ1o6ca%2FX5mWGtiUOpsM7T6HrphF4sWNYXZ7bPIrmCX9mM6vZQyfsm2DtsOBbdVQ%2F5jZXaTS3NvioFxi2azBB4FxdCL0qDbw4Qy6D%2F9IFwGH3Txps3JHeQgdZaXKTA1r3DTbRD%2BKlnaJJqDoJd6y5MNutEhXGBHbs%2BmMIvRk70GOqUBPZWZvvlxwomSUv5z5cBju8TwgzegeyEloJyd1FNS%2FzjLrBL2C7cMdp7yhVc39%2F%2BhdtmHT49qbJKSLPeksx9ocUI3HdQLe6I7xFecjLbU83UlvjZPurqftAwq0eO2OAYw0lMzj0dD7u9Z%2FgfZETJdbWSSIk7Co80Bd7zMX5q0pennHkXyk0K%2F3K1x4BYOZ0%2BYOlEY38B1xHDbk5u46kCHl4uL8v8j&X-Amz-Signature=5b5021a5b1625bfecf8de9c2c2261ca6dc7c56fdd58039317f46c1ed83fb2c7e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRSOZ7PC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDHRjiviaT4I7uBK5mqlMRK7KzbF0XGyzG8LXLMak4E%2FgIgKDKOFSaHZ%2BKboeBygD%2FfS9rgbLJl1ULEw2xBBDswrMsq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOfNotOYqkjt7ibVLCrcA0Ue8T8438gGPfnfo4%2BjswKGp8B9Ki8is3CUKRfqRsnxQtZDbz%2Fr3Le86csihdLmAe5vMxl%2BgzvBDK%2FbP3KK4HuuEW9JytNH8K%2Bkhzji36uw2Ah8aJv%2BIAmLaUFDjwQBufnkcgh%2Bu8P8clof5S9GHpNp78LIp5pbW%2BFYn6ZkFztXtHWanyb86HZgm%2FBO%2B0%2FnRbkdaeSTuRj%2B9xJWI0rMYg6cSszPYT9N7tkAV41h5HQ6%2FWRKasDzCzRiPfLdpEbXNuMZf%2FBMhtBVH0ofjeTUXsl3bPMpp1cJFlba8Xe%2BmZdWNV178jY1MA%2B1y0wboNDGfsAwdrbrQDwliOIQJK7WgEvCKIJV%2BWzadHwuglVPsxnkIG5s9yCziIxdGmS5VmnIZSYJJF4UeC7u4Jvn4%2BPSGsk5vJEOr5Y7JdS2b0qNUEredl7jIA9C6nuvwomxmw%2FOaZE7qQFYgNCkuQunnSsdxGyhQZQ1o6ca%2FX5mWGtiUOpsM7T6HrphF4sWNYXZ7bPIrmCX9mM6vZQyfsm2DtsOBbdVQ%2F5jZXaTS3NvioFxi2azBB4FxdCL0qDbw4Qy6D%2F9IFwGH3Txps3JHeQgdZaXKTA1r3DTbRD%2BKlnaJJqDoJd6y5MNutEhXGBHbs%2BmMIvRk70GOqUBPZWZvvlxwomSUv5z5cBju8TwgzegeyEloJyd1FNS%2FzjLrBL2C7cMdp7yhVc39%2F%2BhdtmHT49qbJKSLPeksx9ocUI3HdQLe6I7xFecjLbU83UlvjZPurqftAwq0eO2OAYw0lMzj0dD7u9Z%2FgfZETJdbWSSIk7Co80Bd7zMX5q0pennHkXyk0K%2F3K1x4BYOZ0%2BYOlEY38B1xHDbk5u46kCHl4uL8v8j&X-Amz-Signature=a65198147c89d998938ba6eb2fe0217c95e158a9b3d3b2477b4a6ca97c582321&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRSOZ7PC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDHRjiviaT4I7uBK5mqlMRK7KzbF0XGyzG8LXLMak4E%2FgIgKDKOFSaHZ%2BKboeBygD%2FfS9rgbLJl1ULEw2xBBDswrMsq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOfNotOYqkjt7ibVLCrcA0Ue8T8438gGPfnfo4%2BjswKGp8B9Ki8is3CUKRfqRsnxQtZDbz%2Fr3Le86csihdLmAe5vMxl%2BgzvBDK%2FbP3KK4HuuEW9JytNH8K%2Bkhzji36uw2Ah8aJv%2BIAmLaUFDjwQBufnkcgh%2Bu8P8clof5S9GHpNp78LIp5pbW%2BFYn6ZkFztXtHWanyb86HZgm%2FBO%2B0%2FnRbkdaeSTuRj%2B9xJWI0rMYg6cSszPYT9N7tkAV41h5HQ6%2FWRKasDzCzRiPfLdpEbXNuMZf%2FBMhtBVH0ofjeTUXsl3bPMpp1cJFlba8Xe%2BmZdWNV178jY1MA%2B1y0wboNDGfsAwdrbrQDwliOIQJK7WgEvCKIJV%2BWzadHwuglVPsxnkIG5s9yCziIxdGmS5VmnIZSYJJF4UeC7u4Jvn4%2BPSGsk5vJEOr5Y7JdS2b0qNUEredl7jIA9C6nuvwomxmw%2FOaZE7qQFYgNCkuQunnSsdxGyhQZQ1o6ca%2FX5mWGtiUOpsM7T6HrphF4sWNYXZ7bPIrmCX9mM6vZQyfsm2DtsOBbdVQ%2F5jZXaTS3NvioFxi2azBB4FxdCL0qDbw4Qy6D%2F9IFwGH3Txps3JHeQgdZaXKTA1r3DTbRD%2BKlnaJJqDoJd6y5MNutEhXGBHbs%2BmMIvRk70GOqUBPZWZvvlxwomSUv5z5cBju8TwgzegeyEloJyd1FNS%2FzjLrBL2C7cMdp7yhVc39%2F%2BhdtmHT49qbJKSLPeksx9ocUI3HdQLe6I7xFecjLbU83UlvjZPurqftAwq0eO2OAYw0lMzj0dD7u9Z%2FgfZETJdbWSSIk7Co80Bd7zMX5q0pennHkXyk0K%2F3K1x4BYOZ0%2BYOlEY38B1xHDbk5u46kCHl4uL8v8j&X-Amz-Signature=8cd559a82051f4324c9ea40e6a6d127930d73b4fb53552b4a50bbb9cd0f0de28&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRSOZ7PC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDHRjiviaT4I7uBK5mqlMRK7KzbF0XGyzG8LXLMak4E%2FgIgKDKOFSaHZ%2BKboeBygD%2FfS9rgbLJl1ULEw2xBBDswrMsq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOfNotOYqkjt7ibVLCrcA0Ue8T8438gGPfnfo4%2BjswKGp8B9Ki8is3CUKRfqRsnxQtZDbz%2Fr3Le86csihdLmAe5vMxl%2BgzvBDK%2FbP3KK4HuuEW9JytNH8K%2Bkhzji36uw2Ah8aJv%2BIAmLaUFDjwQBufnkcgh%2Bu8P8clof5S9GHpNp78LIp5pbW%2BFYn6ZkFztXtHWanyb86HZgm%2FBO%2B0%2FnRbkdaeSTuRj%2B9xJWI0rMYg6cSszPYT9N7tkAV41h5HQ6%2FWRKasDzCzRiPfLdpEbXNuMZf%2FBMhtBVH0ofjeTUXsl3bPMpp1cJFlba8Xe%2BmZdWNV178jY1MA%2B1y0wboNDGfsAwdrbrQDwliOIQJK7WgEvCKIJV%2BWzadHwuglVPsxnkIG5s9yCziIxdGmS5VmnIZSYJJF4UeC7u4Jvn4%2BPSGsk5vJEOr5Y7JdS2b0qNUEredl7jIA9C6nuvwomxmw%2FOaZE7qQFYgNCkuQunnSsdxGyhQZQ1o6ca%2FX5mWGtiUOpsM7T6HrphF4sWNYXZ7bPIrmCX9mM6vZQyfsm2DtsOBbdVQ%2F5jZXaTS3NvioFxi2azBB4FxdCL0qDbw4Qy6D%2F9IFwGH3Txps3JHeQgdZaXKTA1r3DTbRD%2BKlnaJJqDoJd6y5MNutEhXGBHbs%2BmMIvRk70GOqUBPZWZvvlxwomSUv5z5cBju8TwgzegeyEloJyd1FNS%2FzjLrBL2C7cMdp7yhVc39%2F%2BhdtmHT49qbJKSLPeksx9ocUI3HdQLe6I7xFecjLbU83UlvjZPurqftAwq0eO2OAYw0lMzj0dD7u9Z%2FgfZETJdbWSSIk7Co80Bd7zMX5q0pennHkXyk0K%2F3K1x4BYOZ0%2BYOlEY38B1xHDbk5u46kCHl4uL8v8j&X-Amz-Signature=a630e49e19662ef1a4a21656b1bce89b2470e617d1f39fa4987f9b79f121c7a1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRSOZ7PC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDHRjiviaT4I7uBK5mqlMRK7KzbF0XGyzG8LXLMak4E%2FgIgKDKOFSaHZ%2BKboeBygD%2FfS9rgbLJl1ULEw2xBBDswrMsq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOfNotOYqkjt7ibVLCrcA0Ue8T8438gGPfnfo4%2BjswKGp8B9Ki8is3CUKRfqRsnxQtZDbz%2Fr3Le86csihdLmAe5vMxl%2BgzvBDK%2FbP3KK4HuuEW9JytNH8K%2Bkhzji36uw2Ah8aJv%2BIAmLaUFDjwQBufnkcgh%2Bu8P8clof5S9GHpNp78LIp5pbW%2BFYn6ZkFztXtHWanyb86HZgm%2FBO%2B0%2FnRbkdaeSTuRj%2B9xJWI0rMYg6cSszPYT9N7tkAV41h5HQ6%2FWRKasDzCzRiPfLdpEbXNuMZf%2FBMhtBVH0ofjeTUXsl3bPMpp1cJFlba8Xe%2BmZdWNV178jY1MA%2B1y0wboNDGfsAwdrbrQDwliOIQJK7WgEvCKIJV%2BWzadHwuglVPsxnkIG5s9yCziIxdGmS5VmnIZSYJJF4UeC7u4Jvn4%2BPSGsk5vJEOr5Y7JdS2b0qNUEredl7jIA9C6nuvwomxmw%2FOaZE7qQFYgNCkuQunnSsdxGyhQZQ1o6ca%2FX5mWGtiUOpsM7T6HrphF4sWNYXZ7bPIrmCX9mM6vZQyfsm2DtsOBbdVQ%2F5jZXaTS3NvioFxi2azBB4FxdCL0qDbw4Qy6D%2F9IFwGH3Txps3JHeQgdZaXKTA1r3DTbRD%2BKlnaJJqDoJd6y5MNutEhXGBHbs%2BmMIvRk70GOqUBPZWZvvlxwomSUv5z5cBju8TwgzegeyEloJyd1FNS%2FzjLrBL2C7cMdp7yhVc39%2F%2BhdtmHT49qbJKSLPeksx9ocUI3HdQLe6I7xFecjLbU83UlvjZPurqftAwq0eO2OAYw0lMzj0dD7u9Z%2FgfZETJdbWSSIk7Co80Bd7zMX5q0pennHkXyk0K%2F3K1x4BYOZ0%2BYOlEY38B1xHDbk5u46kCHl4uL8v8j&X-Amz-Signature=ee53aa5b4b5e9c67a826277ba20500f3e80003abc401f03c5734a94ace056c72&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XO2FDR4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQC0D7em9ERTu5v6tA%2FAoLiEFNV09R0BfLxa6pEDB2yypQIgNI5n%2BVavZUYr8OGvaH9ow8%2Fdhyn8F8ZyWRp8fzm1BuAq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOLSKph3PXR%2BalAgCCrcA0Fg2KNmpI%2F2QfuI30hUhGhN7ExcBRJ%2F3w2oaDGgQVUNY%2By0RivYMOsbFg32h8%2Bf3gC4eeZZslRc0RIq286jnUB6obGGNcFGhOAWVUUJMRfMQzMLItWZHMP8EZ4wtDbhNwJ98YxyC%2BS8NHc6IsKAT8aLw0pq9J9OBddRecaZhGEdcSnRXk9A43OwDdjGKr%2F3Xbf%2B93KZMmxw9Zfq%2F09icohicGWpDLuyVDTEkZw%2FpOKBcyOcmOnVAM9ZM2tzVg0M2IpNcoqsWTIi5ZDzEW4T0RbjUHVry%2FwE84qrfoQlCk6qmzBgwKC4vP2Nd821rNjCyGHjuhGBSJUF27hRj82lGTdMWwxViKs%2FMpa0hiSQPCzNIID%2FeoPD9o69NALgyYbMS%2BA3LHqnnPU5s9mre7R7UbNGqPe6HmavsqioE6RpWf4%2FYVmgLjsFNWA0Sf5lRL2%2FquhfoN1y0XHAUi3CZt%2FSmYBEauU%2BRmXpBIUGjOMn10FfN%2BrbZWX1ixgKDS5Udt8VuJHEbjUgO4IQkLB0xhZysilLOMPzsTuvNTNjlvGK9LzDTp6K8kokjp1b2Lg0u%2BLFgqaiOU%2BHfyMoHS1VhAQPQ%2B82DkmJHCRgReySAFs0P6qg7ZhMk7iVf01NhF3yMNTRk70GOqUBm8%2FqKMK8uwAisHM9lrg660pBUfQXs81netqzuiOest2zb%2FVUhdPfO9KhWD8W6iEJS%2Bxjb7A4A6aLEUD7nzE8NrYX9Kug%2BlSZnM%2BzBu%2FpBXSzynyJins02OeBT%2Bfbc%2FfNekA4yF3SJ67vt4W0q2QPhXtOeDbpxvL5L7zFOqUYpKFck7ZtZlOZ60vynoa%2Br67eDTH1biF5y42OBrVuNDKMX6FZ0%2B2P&X-Amz-Signature=b7234e3b8328c786fc0a209af003aa5adfe2be0cc501acf2b1c3c82bea7fd8b0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XO2FDR4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQC0D7em9ERTu5v6tA%2FAoLiEFNV09R0BfLxa6pEDB2yypQIgNI5n%2BVavZUYr8OGvaH9ow8%2Fdhyn8F8ZyWRp8fzm1BuAq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOLSKph3PXR%2BalAgCCrcA0Fg2KNmpI%2F2QfuI30hUhGhN7ExcBRJ%2F3w2oaDGgQVUNY%2By0RivYMOsbFg32h8%2Bf3gC4eeZZslRc0RIq286jnUB6obGGNcFGhOAWVUUJMRfMQzMLItWZHMP8EZ4wtDbhNwJ98YxyC%2BS8NHc6IsKAT8aLw0pq9J9OBddRecaZhGEdcSnRXk9A43OwDdjGKr%2F3Xbf%2B93KZMmxw9Zfq%2F09icohicGWpDLuyVDTEkZw%2FpOKBcyOcmOnVAM9ZM2tzVg0M2IpNcoqsWTIi5ZDzEW4T0RbjUHVry%2FwE84qrfoQlCk6qmzBgwKC4vP2Nd821rNjCyGHjuhGBSJUF27hRj82lGTdMWwxViKs%2FMpa0hiSQPCzNIID%2FeoPD9o69NALgyYbMS%2BA3LHqnnPU5s9mre7R7UbNGqPe6HmavsqioE6RpWf4%2FYVmgLjsFNWA0Sf5lRL2%2FquhfoN1y0XHAUi3CZt%2FSmYBEauU%2BRmXpBIUGjOMn10FfN%2BrbZWX1ixgKDS5Udt8VuJHEbjUgO4IQkLB0xhZysilLOMPzsTuvNTNjlvGK9LzDTp6K8kokjp1b2Lg0u%2BLFgqaiOU%2BHfyMoHS1VhAQPQ%2B82DkmJHCRgReySAFs0P6qg7ZhMk7iVf01NhF3yMNTRk70GOqUBm8%2FqKMK8uwAisHM9lrg660pBUfQXs81netqzuiOest2zb%2FVUhdPfO9KhWD8W6iEJS%2Bxjb7A4A6aLEUD7nzE8NrYX9Kug%2BlSZnM%2BzBu%2FpBXSzynyJins02OeBT%2Bfbc%2FfNekA4yF3SJ67vt4W0q2QPhXtOeDbpxvL5L7zFOqUYpKFck7ZtZlOZ60vynoa%2Br67eDTH1biF5y42OBrVuNDKMX6FZ0%2B2P&X-Amz-Signature=a7d8e1318432c33acf3cb06e602402da3edc4a5b3455b02edc1e83adc250ade2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XO2FDR4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQC0D7em9ERTu5v6tA%2FAoLiEFNV09R0BfLxa6pEDB2yypQIgNI5n%2BVavZUYr8OGvaH9ow8%2Fdhyn8F8ZyWRp8fzm1BuAq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOLSKph3PXR%2BalAgCCrcA0Fg2KNmpI%2F2QfuI30hUhGhN7ExcBRJ%2F3w2oaDGgQVUNY%2By0RivYMOsbFg32h8%2Bf3gC4eeZZslRc0RIq286jnUB6obGGNcFGhOAWVUUJMRfMQzMLItWZHMP8EZ4wtDbhNwJ98YxyC%2BS8NHc6IsKAT8aLw0pq9J9OBddRecaZhGEdcSnRXk9A43OwDdjGKr%2F3Xbf%2B93KZMmxw9Zfq%2F09icohicGWpDLuyVDTEkZw%2FpOKBcyOcmOnVAM9ZM2tzVg0M2IpNcoqsWTIi5ZDzEW4T0RbjUHVry%2FwE84qrfoQlCk6qmzBgwKC4vP2Nd821rNjCyGHjuhGBSJUF27hRj82lGTdMWwxViKs%2FMpa0hiSQPCzNIID%2FeoPD9o69NALgyYbMS%2BA3LHqnnPU5s9mre7R7UbNGqPe6HmavsqioE6RpWf4%2FYVmgLjsFNWA0Sf5lRL2%2FquhfoN1y0XHAUi3CZt%2FSmYBEauU%2BRmXpBIUGjOMn10FfN%2BrbZWX1ixgKDS5Udt8VuJHEbjUgO4IQkLB0xhZysilLOMPzsTuvNTNjlvGK9LzDTp6K8kokjp1b2Lg0u%2BLFgqaiOU%2BHfyMoHS1VhAQPQ%2B82DkmJHCRgReySAFs0P6qg7ZhMk7iVf01NhF3yMNTRk70GOqUBm8%2FqKMK8uwAisHM9lrg660pBUfQXs81netqzuiOest2zb%2FVUhdPfO9KhWD8W6iEJS%2Bxjb7A4A6aLEUD7nzE8NrYX9Kug%2BlSZnM%2BzBu%2FpBXSzynyJins02OeBT%2Bfbc%2FfNekA4yF3SJ67vt4W0q2QPhXtOeDbpxvL5L7zFOqUYpKFck7ZtZlOZ60vynoa%2Br67eDTH1biF5y42OBrVuNDKMX6FZ0%2B2P&X-Amz-Signature=722d0120782c5aa60bd9c24dfa80f2ae4ccc2a8862edaac1491d5bc949095158&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XO2FDR4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQC0D7em9ERTu5v6tA%2FAoLiEFNV09R0BfLxa6pEDB2yypQIgNI5n%2BVavZUYr8OGvaH9ow8%2Fdhyn8F8ZyWRp8fzm1BuAq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOLSKph3PXR%2BalAgCCrcA0Fg2KNmpI%2F2QfuI30hUhGhN7ExcBRJ%2F3w2oaDGgQVUNY%2By0RivYMOsbFg32h8%2Bf3gC4eeZZslRc0RIq286jnUB6obGGNcFGhOAWVUUJMRfMQzMLItWZHMP8EZ4wtDbhNwJ98YxyC%2BS8NHc6IsKAT8aLw0pq9J9OBddRecaZhGEdcSnRXk9A43OwDdjGKr%2F3Xbf%2B93KZMmxw9Zfq%2F09icohicGWpDLuyVDTEkZw%2FpOKBcyOcmOnVAM9ZM2tzVg0M2IpNcoqsWTIi5ZDzEW4T0RbjUHVry%2FwE84qrfoQlCk6qmzBgwKC4vP2Nd821rNjCyGHjuhGBSJUF27hRj82lGTdMWwxViKs%2FMpa0hiSQPCzNIID%2FeoPD9o69NALgyYbMS%2BA3LHqnnPU5s9mre7R7UbNGqPe6HmavsqioE6RpWf4%2FYVmgLjsFNWA0Sf5lRL2%2FquhfoN1y0XHAUi3CZt%2FSmYBEauU%2BRmXpBIUGjOMn10FfN%2BrbZWX1ixgKDS5Udt8VuJHEbjUgO4IQkLB0xhZysilLOMPzsTuvNTNjlvGK9LzDTp6K8kokjp1b2Lg0u%2BLFgqaiOU%2BHfyMoHS1VhAQPQ%2B82DkmJHCRgReySAFs0P6qg7ZhMk7iVf01NhF3yMNTRk70GOqUBm8%2FqKMK8uwAisHM9lrg660pBUfQXs81netqzuiOest2zb%2FVUhdPfO9KhWD8W6iEJS%2Bxjb7A4A6aLEUD7nzE8NrYX9Kug%2BlSZnM%2BzBu%2FpBXSzynyJins02OeBT%2Bfbc%2FfNekA4yF3SJ67vt4W0q2QPhXtOeDbpxvL5L7zFOqUYpKFck7ZtZlOZ60vynoa%2Br67eDTH1biF5y42OBrVuNDKMX6FZ0%2B2P&X-Amz-Signature=9f8f337c358ef7415b5604991aa50252ec3d2ba2a501582bc5bb05e4f78d1262&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XO2FDR4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQC0D7em9ERTu5v6tA%2FAoLiEFNV09R0BfLxa6pEDB2yypQIgNI5n%2BVavZUYr8OGvaH9ow8%2Fdhyn8F8ZyWRp8fzm1BuAq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOLSKph3PXR%2BalAgCCrcA0Fg2KNmpI%2F2QfuI30hUhGhN7ExcBRJ%2F3w2oaDGgQVUNY%2By0RivYMOsbFg32h8%2Bf3gC4eeZZslRc0RIq286jnUB6obGGNcFGhOAWVUUJMRfMQzMLItWZHMP8EZ4wtDbhNwJ98YxyC%2BS8NHc6IsKAT8aLw0pq9J9OBddRecaZhGEdcSnRXk9A43OwDdjGKr%2F3Xbf%2B93KZMmxw9Zfq%2F09icohicGWpDLuyVDTEkZw%2FpOKBcyOcmOnVAM9ZM2tzVg0M2IpNcoqsWTIi5ZDzEW4T0RbjUHVry%2FwE84qrfoQlCk6qmzBgwKC4vP2Nd821rNjCyGHjuhGBSJUF27hRj82lGTdMWwxViKs%2FMpa0hiSQPCzNIID%2FeoPD9o69NALgyYbMS%2BA3LHqnnPU5s9mre7R7UbNGqPe6HmavsqioE6RpWf4%2FYVmgLjsFNWA0Sf5lRL2%2FquhfoN1y0XHAUi3CZt%2FSmYBEauU%2BRmXpBIUGjOMn10FfN%2BrbZWX1ixgKDS5Udt8VuJHEbjUgO4IQkLB0xhZysilLOMPzsTuvNTNjlvGK9LzDTp6K8kokjp1b2Lg0u%2BLFgqaiOU%2BHfyMoHS1VhAQPQ%2B82DkmJHCRgReySAFs0P6qg7ZhMk7iVf01NhF3yMNTRk70GOqUBm8%2FqKMK8uwAisHM9lrg660pBUfQXs81netqzuiOest2zb%2FVUhdPfO9KhWD8W6iEJS%2Bxjb7A4A6aLEUD7nzE8NrYX9Kug%2BlSZnM%2BzBu%2FpBXSzynyJins02OeBT%2Bfbc%2FfNekA4yF3SJ67vt4W0q2QPhXtOeDbpxvL5L7zFOqUYpKFck7ZtZlOZ60vynoa%2Br67eDTH1biF5y42OBrVuNDKMX6FZ0%2B2P&X-Amz-Signature=beacebc0c18b668d64119e2dc8a444b0de0b89fdd3b7e459bff8efaf7d74093f&X-Amz-SignedHeaders=host&x-id=GetObject)
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


