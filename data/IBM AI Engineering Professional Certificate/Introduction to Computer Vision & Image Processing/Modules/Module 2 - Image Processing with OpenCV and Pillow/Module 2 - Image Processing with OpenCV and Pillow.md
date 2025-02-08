

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRNE3O42%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDXFHUfVhjevPo6NCIngikJQ5lz3oejfYziqo8jmuERHAIgKtGQAQa1OKqmwHEQ2i87zVoGp4cB%2Bdj0mngzxwKqEEQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2BBZseD0h3mOeA2aCrcA46nM2keYM9NS%2FaUaOnowm3YbgVrl4zd2jvOt95MMFXvu0asYtBQnbVM2usXeXgonBnMEKYjTf3mW4%2FO7OtGx0A%2FYHfdiL%2F0irT3A8QNJ7Jog4U9p%2BqEafyo2dhR70OmiPMFUO%2FTv9l1mpkp7Qn6ClEMRZ7TiRqJ2UE2jOR4DNKAJeDO8GYUdmsNaYHo%2B4n9EcxoEF%2BIAzI4KEv9N4l6vPmgghvlqqvmziCH4BomckzHAdXWw28r8b8o3WMlKNs57V2hAsTkglDWb00EN%2FZ8tTrzsAjZ%2FOJBomlPcA1PIjPNh04KWkVXdSX9KtXRsqKwgkarS3X7gNFi70bF6wtAXUA2DkUHY5A81sXUc64Cm6KMpe57Xk4D%2F7OcuVd4cHrIjc0P%2BW10AdQg8ItwtVtZCpIUYuRQd7OrX8cNreRG0m3uJxjvyrgMwE5ciiSBwjkDzcjgpUXDWWSPJ9Hf%2F%2Binv9knxro%2FbdEA1taXuYEhT6T8KQGrlvZMb%2FAzSkj7SBoO%2BmCtodoKLoGQy0GGAm24bvV1p9ODhgearlMWkJM%2BSNU%2FDvsl6XzWvEWfCFuM2bpJIbd%2FxGJUPGzBMXy%2F7gJJ3GZE2UC5DaDpKLJGKowit3MUVbam%2BOKGYZzTFfMDMLiFnb0GOqUBtO3lKvGWX8exo%2FqASbF58g0LkBKnVcoFBN%2FIr%2F0gFMBodGhU0irrEpxTbBAepE%2B4eFGfY9vU0yPzIWGfJ4VGD723eD5WmhHMBrGuv2Mgk7d%2BQTp3FCgPyQa0bLYZ13uVGspHQ7UTi4woAam%2FZPnpxrzZkOA1rcBglywZ2vTe%2Bq3BG7n%2FUbegEwlt9r5ywosjZaTaxAP9vE2o%2BOsHisNN7uMnV0XI&X-Amz-Signature=e9db0781d6a81e26000efd45e633c329132a85b0b26195b9fa3b9db5dfeb58db&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C5THVR6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDeltrosm06nPlwItiSjTmoYRym3PezeY68KKWV1DgLLAIgb%2BvZuvCo30pOUpPEUudbAxR39OpD9UJOWTgIII3O3zQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD3TaZ1OkyPKhIChGCrcA8UzO2xaitn4ahs6VuJEYznS60Q8jL3iLTODbi8Zn5jl1HfOk7zZDiJYu8r9V61X%2BrqDurY%2B3hQbX84bqNiF5AQTqS3Qq%2FNdd1Vdw1piCskZjMD9nRuAznOHmDR%2B9aROGfKKHHZ6Z2wV70wkJQVuUrqIfqe0z8lGp4g3C5ENMM%2F3pNQDdhXQWyo0hINnetqzvYZKsmxJISjLvD9zvEoEsvsGB1lCWs19Kb0c9mhmu9yTUJel6NFtfSEiUP4N0AVQosteixvUDG4f9tNcuh51rIUYBHYgfZ1S0Rl1BUYJb5FmrGJ%2Bcr9lhycSvpN2ouWSKq0N5MjH4hWbMxIlXpJ0EoZXXp%2BQZi77Qvkyv3HCxwpZJOAjJRt4oRfqBY4jOV8%2FRYpRo8f%2FT7MtNeM9OQo06Gyhz%2FR3qhHn5RfxN4mxC1TulGOxkAh5kcLO0hWY1Zv7U3tlsMlkazhR7gTv0ES9JC%2BQpyPgec81zj4iP9%2BZ5g3S3HxNMNk%2FFGEgH8oX1gSuJmAVegCGYzsdZ%2FjUMVdGivRKO8H2K4%2Bfsbw5oIYUvjny%2B6WHvyv2nhEmqQ28Kiy5wxSirzPXWAZrqrrIiN8yAaCgICRY9fMZ4QCD2IUyiLxX25DNcboMVf9Jf%2BwcMKKFnb0GOqUB988%2Bcm3sSt98OuQ94U8WJ1Pw5%2BNDto2EDfhQhH0ZtetNNs6%2FFA7iIGEP2e7Ctg7Ex2WEtxNTl4iOJ78i8CSZhcCn%2BPszNFHrvAa5Ts%2BcnIyPPqa3hGwAORNePo0PivkVwqJRmCwoipIQU36Z2HeE7Ikxd3TIppfZtzmxa07WsYKkebt4Y6t6hApOrbcKAYgrsjYSLRo%2BNM3DQo6ix%2BwLEAVQdIhM&X-Amz-Signature=d5296065d90c563906e7a7a8c193a38feb00dfe9c91e9a6b3b45fe00dec3ad58&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C5THVR6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDeltrosm06nPlwItiSjTmoYRym3PezeY68KKWV1DgLLAIgb%2BvZuvCo30pOUpPEUudbAxR39OpD9UJOWTgIII3O3zQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD3TaZ1OkyPKhIChGCrcA8UzO2xaitn4ahs6VuJEYznS60Q8jL3iLTODbi8Zn5jl1HfOk7zZDiJYu8r9V61X%2BrqDurY%2B3hQbX84bqNiF5AQTqS3Qq%2FNdd1Vdw1piCskZjMD9nRuAznOHmDR%2B9aROGfKKHHZ6Z2wV70wkJQVuUrqIfqe0z8lGp4g3C5ENMM%2F3pNQDdhXQWyo0hINnetqzvYZKsmxJISjLvD9zvEoEsvsGB1lCWs19Kb0c9mhmu9yTUJel6NFtfSEiUP4N0AVQosteixvUDG4f9tNcuh51rIUYBHYgfZ1S0Rl1BUYJb5FmrGJ%2Bcr9lhycSvpN2ouWSKq0N5MjH4hWbMxIlXpJ0EoZXXp%2BQZi77Qvkyv3HCxwpZJOAjJRt4oRfqBY4jOV8%2FRYpRo8f%2FT7MtNeM9OQo06Gyhz%2FR3qhHn5RfxN4mxC1TulGOxkAh5kcLO0hWY1Zv7U3tlsMlkazhR7gTv0ES9JC%2BQpyPgec81zj4iP9%2BZ5g3S3HxNMNk%2FFGEgH8oX1gSuJmAVegCGYzsdZ%2FjUMVdGivRKO8H2K4%2Bfsbw5oIYUvjny%2B6WHvyv2nhEmqQ28Kiy5wxSirzPXWAZrqrrIiN8yAaCgICRY9fMZ4QCD2IUyiLxX25DNcboMVf9Jf%2BwcMKKFnb0GOqUB988%2Bcm3sSt98OuQ94U8WJ1Pw5%2BNDto2EDfhQhH0ZtetNNs6%2FFA7iIGEP2e7Ctg7Ex2WEtxNTl4iOJ78i8CSZhcCn%2BPszNFHrvAa5Ts%2BcnIyPPqa3hGwAORNePo0PivkVwqJRmCwoipIQU36Z2HeE7Ikxd3TIppfZtzmxa07WsYKkebt4Y6t6hApOrbcKAYgrsjYSLRo%2BNM3DQo6ix%2BwLEAVQdIhM&X-Amz-Signature=466ecb9a2918e586c518672972c8a0dd1b1237315c45d0c35d0142c97e670fdf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C5THVR6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDeltrosm06nPlwItiSjTmoYRym3PezeY68KKWV1DgLLAIgb%2BvZuvCo30pOUpPEUudbAxR39OpD9UJOWTgIII3O3zQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD3TaZ1OkyPKhIChGCrcA8UzO2xaitn4ahs6VuJEYznS60Q8jL3iLTODbi8Zn5jl1HfOk7zZDiJYu8r9V61X%2BrqDurY%2B3hQbX84bqNiF5AQTqS3Qq%2FNdd1Vdw1piCskZjMD9nRuAznOHmDR%2B9aROGfKKHHZ6Z2wV70wkJQVuUrqIfqe0z8lGp4g3C5ENMM%2F3pNQDdhXQWyo0hINnetqzvYZKsmxJISjLvD9zvEoEsvsGB1lCWs19Kb0c9mhmu9yTUJel6NFtfSEiUP4N0AVQosteixvUDG4f9tNcuh51rIUYBHYgfZ1S0Rl1BUYJb5FmrGJ%2Bcr9lhycSvpN2ouWSKq0N5MjH4hWbMxIlXpJ0EoZXXp%2BQZi77Qvkyv3HCxwpZJOAjJRt4oRfqBY4jOV8%2FRYpRo8f%2FT7MtNeM9OQo06Gyhz%2FR3qhHn5RfxN4mxC1TulGOxkAh5kcLO0hWY1Zv7U3tlsMlkazhR7gTv0ES9JC%2BQpyPgec81zj4iP9%2BZ5g3S3HxNMNk%2FFGEgH8oX1gSuJmAVegCGYzsdZ%2FjUMVdGivRKO8H2K4%2Bfsbw5oIYUvjny%2B6WHvyv2nhEmqQ28Kiy5wxSirzPXWAZrqrrIiN8yAaCgICRY9fMZ4QCD2IUyiLxX25DNcboMVf9Jf%2BwcMKKFnb0GOqUB988%2Bcm3sSt98OuQ94U8WJ1Pw5%2BNDto2EDfhQhH0ZtetNNs6%2FFA7iIGEP2e7Ctg7Ex2WEtxNTl4iOJ78i8CSZhcCn%2BPszNFHrvAa5Ts%2BcnIyPPqa3hGwAORNePo0PivkVwqJRmCwoipIQU36Z2HeE7Ikxd3TIppfZtzmxa07WsYKkebt4Y6t6hApOrbcKAYgrsjYSLRo%2BNM3DQo6ix%2BwLEAVQdIhM&X-Amz-Signature=75600b54bc54d58f52b47c860c4fa0943dce47cf6464af8fa8b342ff880d4d53&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C5THVR6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDeltrosm06nPlwItiSjTmoYRym3PezeY68KKWV1DgLLAIgb%2BvZuvCo30pOUpPEUudbAxR39OpD9UJOWTgIII3O3zQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD3TaZ1OkyPKhIChGCrcA8UzO2xaitn4ahs6VuJEYznS60Q8jL3iLTODbi8Zn5jl1HfOk7zZDiJYu8r9V61X%2BrqDurY%2B3hQbX84bqNiF5AQTqS3Qq%2FNdd1Vdw1piCskZjMD9nRuAznOHmDR%2B9aROGfKKHHZ6Z2wV70wkJQVuUrqIfqe0z8lGp4g3C5ENMM%2F3pNQDdhXQWyo0hINnetqzvYZKsmxJISjLvD9zvEoEsvsGB1lCWs19Kb0c9mhmu9yTUJel6NFtfSEiUP4N0AVQosteixvUDG4f9tNcuh51rIUYBHYgfZ1S0Rl1BUYJb5FmrGJ%2Bcr9lhycSvpN2ouWSKq0N5MjH4hWbMxIlXpJ0EoZXXp%2BQZi77Qvkyv3HCxwpZJOAjJRt4oRfqBY4jOV8%2FRYpRo8f%2FT7MtNeM9OQo06Gyhz%2FR3qhHn5RfxN4mxC1TulGOxkAh5kcLO0hWY1Zv7U3tlsMlkazhR7gTv0ES9JC%2BQpyPgec81zj4iP9%2BZ5g3S3HxNMNk%2FFGEgH8oX1gSuJmAVegCGYzsdZ%2FjUMVdGivRKO8H2K4%2Bfsbw5oIYUvjny%2B6WHvyv2nhEmqQ28Kiy5wxSirzPXWAZrqrrIiN8yAaCgICRY9fMZ4QCD2IUyiLxX25DNcboMVf9Jf%2BwcMKKFnb0GOqUB988%2Bcm3sSt98OuQ94U8WJ1Pw5%2BNDto2EDfhQhH0ZtetNNs6%2FFA7iIGEP2e7Ctg7Ex2WEtxNTl4iOJ78i8CSZhcCn%2BPszNFHrvAa5Ts%2BcnIyPPqa3hGwAORNePo0PivkVwqJRmCwoipIQU36Z2HeE7Ikxd3TIppfZtzmxa07WsYKkebt4Y6t6hApOrbcKAYgrsjYSLRo%2BNM3DQo6ix%2BwLEAVQdIhM&X-Amz-Signature=f9523e6fc30b7b4f9caf2930ce70f6360d215f1f4eacc8bb3e3552f78f41de60&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C5THVR6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDeltrosm06nPlwItiSjTmoYRym3PezeY68KKWV1DgLLAIgb%2BvZuvCo30pOUpPEUudbAxR39OpD9UJOWTgIII3O3zQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD3TaZ1OkyPKhIChGCrcA8UzO2xaitn4ahs6VuJEYznS60Q8jL3iLTODbi8Zn5jl1HfOk7zZDiJYu8r9V61X%2BrqDurY%2B3hQbX84bqNiF5AQTqS3Qq%2FNdd1Vdw1piCskZjMD9nRuAznOHmDR%2B9aROGfKKHHZ6Z2wV70wkJQVuUrqIfqe0z8lGp4g3C5ENMM%2F3pNQDdhXQWyo0hINnetqzvYZKsmxJISjLvD9zvEoEsvsGB1lCWs19Kb0c9mhmu9yTUJel6NFtfSEiUP4N0AVQosteixvUDG4f9tNcuh51rIUYBHYgfZ1S0Rl1BUYJb5FmrGJ%2Bcr9lhycSvpN2ouWSKq0N5MjH4hWbMxIlXpJ0EoZXXp%2BQZi77Qvkyv3HCxwpZJOAjJRt4oRfqBY4jOV8%2FRYpRo8f%2FT7MtNeM9OQo06Gyhz%2FR3qhHn5RfxN4mxC1TulGOxkAh5kcLO0hWY1Zv7U3tlsMlkazhR7gTv0ES9JC%2BQpyPgec81zj4iP9%2BZ5g3S3HxNMNk%2FFGEgH8oX1gSuJmAVegCGYzsdZ%2FjUMVdGivRKO8H2K4%2Bfsbw5oIYUvjny%2B6WHvyv2nhEmqQ28Kiy5wxSirzPXWAZrqrrIiN8yAaCgICRY9fMZ4QCD2IUyiLxX25DNcboMVf9Jf%2BwcMKKFnb0GOqUB988%2Bcm3sSt98OuQ94U8WJ1Pw5%2BNDto2EDfhQhH0ZtetNNs6%2FFA7iIGEP2e7Ctg7Ex2WEtxNTl4iOJ78i8CSZhcCn%2BPszNFHrvAa5Ts%2BcnIyPPqa3hGwAORNePo0PivkVwqJRmCwoipIQU36Z2HeE7Ikxd3TIppfZtzmxa07WsYKkebt4Y6t6hApOrbcKAYgrsjYSLRo%2BNM3DQo6ix%2BwLEAVQdIhM&X-Amz-Signature=a5420d1c765e202b7cefceb1390dc0197c09d4867ff67c8f7b2e69babe4cb81d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRNE3O42%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDXFHUfVhjevPo6NCIngikJQ5lz3oejfYziqo8jmuERHAIgKtGQAQa1OKqmwHEQ2i87zVoGp4cB%2Bdj0mngzxwKqEEQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2BBZseD0h3mOeA2aCrcA46nM2keYM9NS%2FaUaOnowm3YbgVrl4zd2jvOt95MMFXvu0asYtBQnbVM2usXeXgonBnMEKYjTf3mW4%2FO7OtGx0A%2FYHfdiL%2F0irT3A8QNJ7Jog4U9p%2BqEafyo2dhR70OmiPMFUO%2FTv9l1mpkp7Qn6ClEMRZ7TiRqJ2UE2jOR4DNKAJeDO8GYUdmsNaYHo%2B4n9EcxoEF%2BIAzI4KEv9N4l6vPmgghvlqqvmziCH4BomckzHAdXWw28r8b8o3WMlKNs57V2hAsTkglDWb00EN%2FZ8tTrzsAjZ%2FOJBomlPcA1PIjPNh04KWkVXdSX9KtXRsqKwgkarS3X7gNFi70bF6wtAXUA2DkUHY5A81sXUc64Cm6KMpe57Xk4D%2F7OcuVd4cHrIjc0P%2BW10AdQg8ItwtVtZCpIUYuRQd7OrX8cNreRG0m3uJxjvyrgMwE5ciiSBwjkDzcjgpUXDWWSPJ9Hf%2F%2Binv9knxro%2FbdEA1taXuYEhT6T8KQGrlvZMb%2FAzSkj7SBoO%2BmCtodoKLoGQy0GGAm24bvV1p9ODhgearlMWkJM%2BSNU%2FDvsl6XzWvEWfCFuM2bpJIbd%2FxGJUPGzBMXy%2F7gJJ3GZE2UC5DaDpKLJGKowit3MUVbam%2BOKGYZzTFfMDMLiFnb0GOqUBtO3lKvGWX8exo%2FqASbF58g0LkBKnVcoFBN%2FIr%2F0gFMBodGhU0irrEpxTbBAepE%2B4eFGfY9vU0yPzIWGfJ4VGD723eD5WmhHMBrGuv2Mgk7d%2BQTp3FCgPyQa0bLYZ13uVGspHQ7UTi4woAam%2FZPnpxrzZkOA1rcBglywZ2vTe%2Bq3BG7n%2FUbegEwlt9r5ywosjZaTaxAP9vE2o%2BOsHisNN7uMnV0XI&X-Amz-Signature=c0cd69c35259a996f524c4ce28a6eeb593e4ee1a0254f3fb43d0c62cd24a134a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRNE3O42%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDXFHUfVhjevPo6NCIngikJQ5lz3oejfYziqo8jmuERHAIgKtGQAQa1OKqmwHEQ2i87zVoGp4cB%2Bdj0mngzxwKqEEQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2BBZseD0h3mOeA2aCrcA46nM2keYM9NS%2FaUaOnowm3YbgVrl4zd2jvOt95MMFXvu0asYtBQnbVM2usXeXgonBnMEKYjTf3mW4%2FO7OtGx0A%2FYHfdiL%2F0irT3A8QNJ7Jog4U9p%2BqEafyo2dhR70OmiPMFUO%2FTv9l1mpkp7Qn6ClEMRZ7TiRqJ2UE2jOR4DNKAJeDO8GYUdmsNaYHo%2B4n9EcxoEF%2BIAzI4KEv9N4l6vPmgghvlqqvmziCH4BomckzHAdXWw28r8b8o3WMlKNs57V2hAsTkglDWb00EN%2FZ8tTrzsAjZ%2FOJBomlPcA1PIjPNh04KWkVXdSX9KtXRsqKwgkarS3X7gNFi70bF6wtAXUA2DkUHY5A81sXUc64Cm6KMpe57Xk4D%2F7OcuVd4cHrIjc0P%2BW10AdQg8ItwtVtZCpIUYuRQd7OrX8cNreRG0m3uJxjvyrgMwE5ciiSBwjkDzcjgpUXDWWSPJ9Hf%2F%2Binv9knxro%2FbdEA1taXuYEhT6T8KQGrlvZMb%2FAzSkj7SBoO%2BmCtodoKLoGQy0GGAm24bvV1p9ODhgearlMWkJM%2BSNU%2FDvsl6XzWvEWfCFuM2bpJIbd%2FxGJUPGzBMXy%2F7gJJ3GZE2UC5DaDpKLJGKowit3MUVbam%2BOKGYZzTFfMDMLiFnb0GOqUBtO3lKvGWX8exo%2FqASbF58g0LkBKnVcoFBN%2FIr%2F0gFMBodGhU0irrEpxTbBAepE%2B4eFGfY9vU0yPzIWGfJ4VGD723eD5WmhHMBrGuv2Mgk7d%2BQTp3FCgPyQa0bLYZ13uVGspHQ7UTi4woAam%2FZPnpxrzZkOA1rcBglywZ2vTe%2Bq3BG7n%2FUbegEwlt9r5ywosjZaTaxAP9vE2o%2BOsHisNN7uMnV0XI&X-Amz-Signature=ba1e1e0b0b9d3832928f8fdb412be522aa3c9cc561c3f8a8bd6cd9dd28a8d518&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRNE3O42%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDXFHUfVhjevPo6NCIngikJQ5lz3oejfYziqo8jmuERHAIgKtGQAQa1OKqmwHEQ2i87zVoGp4cB%2Bdj0mngzxwKqEEQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2BBZseD0h3mOeA2aCrcA46nM2keYM9NS%2FaUaOnowm3YbgVrl4zd2jvOt95MMFXvu0asYtBQnbVM2usXeXgonBnMEKYjTf3mW4%2FO7OtGx0A%2FYHfdiL%2F0irT3A8QNJ7Jog4U9p%2BqEafyo2dhR70OmiPMFUO%2FTv9l1mpkp7Qn6ClEMRZ7TiRqJ2UE2jOR4DNKAJeDO8GYUdmsNaYHo%2B4n9EcxoEF%2BIAzI4KEv9N4l6vPmgghvlqqvmziCH4BomckzHAdXWw28r8b8o3WMlKNs57V2hAsTkglDWb00EN%2FZ8tTrzsAjZ%2FOJBomlPcA1PIjPNh04KWkVXdSX9KtXRsqKwgkarS3X7gNFi70bF6wtAXUA2DkUHY5A81sXUc64Cm6KMpe57Xk4D%2F7OcuVd4cHrIjc0P%2BW10AdQg8ItwtVtZCpIUYuRQd7OrX8cNreRG0m3uJxjvyrgMwE5ciiSBwjkDzcjgpUXDWWSPJ9Hf%2F%2Binv9knxro%2FbdEA1taXuYEhT6T8KQGrlvZMb%2FAzSkj7SBoO%2BmCtodoKLoGQy0GGAm24bvV1p9ODhgearlMWkJM%2BSNU%2FDvsl6XzWvEWfCFuM2bpJIbd%2FxGJUPGzBMXy%2F7gJJ3GZE2UC5DaDpKLJGKowit3MUVbam%2BOKGYZzTFfMDMLiFnb0GOqUBtO3lKvGWX8exo%2FqASbF58g0LkBKnVcoFBN%2FIr%2F0gFMBodGhU0irrEpxTbBAepE%2B4eFGfY9vU0yPzIWGfJ4VGD723eD5WmhHMBrGuv2Mgk7d%2BQTp3FCgPyQa0bLYZ13uVGspHQ7UTi4woAam%2FZPnpxrzZkOA1rcBglywZ2vTe%2Bq3BG7n%2FUbegEwlt9r5ywosjZaTaxAP9vE2o%2BOsHisNN7uMnV0XI&X-Amz-Signature=f2408ad3f0d369a6bf7c466396946538fb44c8cb317e83eb3f91f21a1bdb8f74&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRNE3O42%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDXFHUfVhjevPo6NCIngikJQ5lz3oejfYziqo8jmuERHAIgKtGQAQa1OKqmwHEQ2i87zVoGp4cB%2Bdj0mngzxwKqEEQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2BBZseD0h3mOeA2aCrcA46nM2keYM9NS%2FaUaOnowm3YbgVrl4zd2jvOt95MMFXvu0asYtBQnbVM2usXeXgonBnMEKYjTf3mW4%2FO7OtGx0A%2FYHfdiL%2F0irT3A8QNJ7Jog4U9p%2BqEafyo2dhR70OmiPMFUO%2FTv9l1mpkp7Qn6ClEMRZ7TiRqJ2UE2jOR4DNKAJeDO8GYUdmsNaYHo%2B4n9EcxoEF%2BIAzI4KEv9N4l6vPmgghvlqqvmziCH4BomckzHAdXWw28r8b8o3WMlKNs57V2hAsTkglDWb00EN%2FZ8tTrzsAjZ%2FOJBomlPcA1PIjPNh04KWkVXdSX9KtXRsqKwgkarS3X7gNFi70bF6wtAXUA2DkUHY5A81sXUc64Cm6KMpe57Xk4D%2F7OcuVd4cHrIjc0P%2BW10AdQg8ItwtVtZCpIUYuRQd7OrX8cNreRG0m3uJxjvyrgMwE5ciiSBwjkDzcjgpUXDWWSPJ9Hf%2F%2Binv9knxro%2FbdEA1taXuYEhT6T8KQGrlvZMb%2FAzSkj7SBoO%2BmCtodoKLoGQy0GGAm24bvV1p9ODhgearlMWkJM%2BSNU%2FDvsl6XzWvEWfCFuM2bpJIbd%2FxGJUPGzBMXy%2F7gJJ3GZE2UC5DaDpKLJGKowit3MUVbam%2BOKGYZzTFfMDMLiFnb0GOqUBtO3lKvGWX8exo%2FqASbF58g0LkBKnVcoFBN%2FIr%2F0gFMBodGhU0irrEpxTbBAepE%2B4eFGfY9vU0yPzIWGfJ4VGD723eD5WmhHMBrGuv2Mgk7d%2BQTp3FCgPyQa0bLYZ13uVGspHQ7UTi4woAam%2FZPnpxrzZkOA1rcBglywZ2vTe%2Bq3BG7n%2FUbegEwlt9r5ywosjZaTaxAP9vE2o%2BOsHisNN7uMnV0XI&X-Amz-Signature=b038d6679af89f32f03b01fe3044e80e984f655657954ac45b95005653b9e852&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRNE3O42%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDXFHUfVhjevPo6NCIngikJQ5lz3oejfYziqo8jmuERHAIgKtGQAQa1OKqmwHEQ2i87zVoGp4cB%2Bdj0mngzxwKqEEQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2BBZseD0h3mOeA2aCrcA46nM2keYM9NS%2FaUaOnowm3YbgVrl4zd2jvOt95MMFXvu0asYtBQnbVM2usXeXgonBnMEKYjTf3mW4%2FO7OtGx0A%2FYHfdiL%2F0irT3A8QNJ7Jog4U9p%2BqEafyo2dhR70OmiPMFUO%2FTv9l1mpkp7Qn6ClEMRZ7TiRqJ2UE2jOR4DNKAJeDO8GYUdmsNaYHo%2B4n9EcxoEF%2BIAzI4KEv9N4l6vPmgghvlqqvmziCH4BomckzHAdXWw28r8b8o3WMlKNs57V2hAsTkglDWb00EN%2FZ8tTrzsAjZ%2FOJBomlPcA1PIjPNh04KWkVXdSX9KtXRsqKwgkarS3X7gNFi70bF6wtAXUA2DkUHY5A81sXUc64Cm6KMpe57Xk4D%2F7OcuVd4cHrIjc0P%2BW10AdQg8ItwtVtZCpIUYuRQd7OrX8cNreRG0m3uJxjvyrgMwE5ciiSBwjkDzcjgpUXDWWSPJ9Hf%2F%2Binv9knxro%2FbdEA1taXuYEhT6T8KQGrlvZMb%2FAzSkj7SBoO%2BmCtodoKLoGQy0GGAm24bvV1p9ODhgearlMWkJM%2BSNU%2FDvsl6XzWvEWfCFuM2bpJIbd%2FxGJUPGzBMXy%2F7gJJ3GZE2UC5DaDpKLJGKowit3MUVbam%2BOKGYZzTFfMDMLiFnb0GOqUBtO3lKvGWX8exo%2FqASbF58g0LkBKnVcoFBN%2FIr%2F0gFMBodGhU0irrEpxTbBAepE%2B4eFGfY9vU0yPzIWGfJ4VGD723eD5WmhHMBrGuv2Mgk7d%2BQTp3FCgPyQa0bLYZ13uVGspHQ7UTi4woAam%2FZPnpxrzZkOA1rcBglywZ2vTe%2Bq3BG7n%2FUbegEwlt9r5ywosjZaTaxAP9vE2o%2BOsHisNN7uMnV0XI&X-Amz-Signature=8e081f03a2674e3ca5e2cb08b249b5ad083c4f2dfd710c2d4b2f531e71544ecd&X-Amz-SignedHeaders=host&x-id=GetObject)
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


