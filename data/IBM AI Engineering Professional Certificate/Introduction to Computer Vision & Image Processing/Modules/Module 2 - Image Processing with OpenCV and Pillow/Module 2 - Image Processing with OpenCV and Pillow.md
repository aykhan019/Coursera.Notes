

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N7K7OWO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgi%2BQLYXRFDjjc1lnXYcHF%2FPmJ%2B%2FOdOeTw4iSWFs35VAiEAm%2BhMqZ%2BhOHCmJyESJiFcA4MSzOf5ozLsyaI88hclPRoqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMg3OHABxmZ0Kn0%2BlyrcA%2FKONadBHvsi1iPCQOA5aDW48M7qEj9EDqsY4c9ulnQRmEYq33FprxwACJ5dNvsFMjvNnA4MEqfEPPUON1qIENHWKJs7v3NyegEDGn3b9uov2kfWMwCV9O9nNOKMC2%2FSb58yO76N62SR1EJWO6mWSaCeJfwJZYxRiHFLlhaXhtqeJIfSC5VcWZsd1AJ2lEdyDPRIU%2FrohrAlamBLaBVlcFBAjCeUC7UiY2qa0QrieYQjbvnG5WcyENlsqwOnaf7rZWEmTfdXwjMdCQFHO8xX8SO8T%2Fr9HK21gdkoqhO90W0VjRzgafvw2TsfUrgzpBKp%2BvZXCaIENPhXkTxEupQnAzmD%2FmLYF5OGS2VqwNU6nyiN3ckbXOzqzV7HZKhX945C16RSCKBDohcbmvkK3A261%2BnScKLQ%2FGbgTvASWYRv3jI3jJVb8bqwZw1x6Sy39I7ZtO4dwB2d7P7W%2BSlGCGF7bXb%2F38M4jhrJx8%2B4l0rB8l5QgTvaJ5dPgz2KIT81r%2BOuAxzL5QnXQ5NX76ZedtfKAXhyQBQHUx1KxOAlsTNR0qDuiH%2BDj22kTtu%2FyMEibEkWfn1JkUN80lf%2FOCyFzVR2YzevsofjfN0%2B1wcsVWcYa9YTj736YicHALLKBQ9tMLDI87wGOqUBLBGfLTfuRI56FKBn8N7KaXNVgmoFiV9K%2Ft4VAdYnnXftynglndDfcatURBv2zxeojRwwzGd7jEvH3VuQ9wXyep6E41uhU9BP9nstkqpChCitJl93q4nkVg5iMIHphFL1XMfjh%2FsBwQVaOS%2F69%2F%2F3MNUyPJl9%2BQm9%2BVZq6Bs%2FARupJ3CXZVuRFQUKwN%2Bc4RA9bgV82OlkPmPrw4pZdQc6O3vMGz5g&X-Amz-Signature=ec267c4e05a11593f1549282499cb452bcd6b85b1e5fbb2d8b714d7a822cb66b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OTPMJWU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuv6ML83NkEIXyQwFDI2SvKQNNxikvquc3Da7%2FFXsfRAiBdYztmo4e6XbbczUCyYc%2FvLSJ810Ykn9z544usxCEiyyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjtHHIBKYHrkazIBGKtwDALsmfTEfpO%2FY2o%2BUjqNShgwvZpx63YIianKOStIM8xmMBnO2MP6kIL8welnDaw8uBpiuFh6g4qjon2WJOFk64skGvu7lMz2EpD2rP1bF4ZDx7IyA7N%2BgYeLxuFaUD%2BByi6nEWYAT3Nu6bQBuuvTYhB86NTqWaGmh1fihSC9kRbWCDsBNTAc2pnxYpx0B%2BxAXkh3B%2FlYc8sDFzhDamA5KOwtKEEV8dqRrI9fZkJ7ivDHBbzB20vAYaZyELpUWhQhTLU6yGz2QaCOfPA3Rji1vlVLcZA08F%2F1IoeliKt%2F3mwSuFyuHazCxrvy2tcfMzClFUeEubapshDmcK81rb5GuIZye0wR0ApHbtG1%2FqwBveh2z8iUNi0yIkaBUBL1HWRQP%2F%2FwdlfdEt2BqPUYGjUUiGkdZkBIQfmno4SUPtdITQspL8ky3QULbXBB2iOgVfIhMGfwFUSeG4hJEqQwCuEly0OUl6tSIY71JIrwcvA2FLCQMB0lGdpm%2FofGo0UTDGpR5rHeeQOoZpHE%2FlxLvN2rP8Po%2FRGqrkifxGPH9R0oFMgHcHrz4RXqIaO%2F6Rd25H%2F%2F%2Ftseh%2FNXiRfq3Lc580aFqK2w%2BNJSoNlCIPN2DfSp07PrrQbl8uNxPRnjmVo8wgsjzvAY6pgFTZxaVYB0icLHWGB1QtLPsSDWJAZ7UGurFkCdD3jd6nYdgXtV0qqgT0k0INNwFqRMvkYgTuNuE7QVgvZRbyUwCVCrSPuNbOaMHZWcVWoeqEJutcezCQA6p%2BZSag8%2BvADjaYz8IgMZ9DgWSxS6ZRnJmHsTJ8lkMjJmj8LugpqKmXgFt5mJWPty8NBqIzTmLPzSb%2B%2B9mlsMahpat5RtanGweKo40zY8q&X-Amz-Signature=ce289eefff9f43c1524507512a53dc2909694a36b290ed01b74652d38ab7fa5e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OTPMJWU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuv6ML83NkEIXyQwFDI2SvKQNNxikvquc3Da7%2FFXsfRAiBdYztmo4e6XbbczUCyYc%2FvLSJ810Ykn9z544usxCEiyyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjtHHIBKYHrkazIBGKtwDALsmfTEfpO%2FY2o%2BUjqNShgwvZpx63YIianKOStIM8xmMBnO2MP6kIL8welnDaw8uBpiuFh6g4qjon2WJOFk64skGvu7lMz2EpD2rP1bF4ZDx7IyA7N%2BgYeLxuFaUD%2BByi6nEWYAT3Nu6bQBuuvTYhB86NTqWaGmh1fihSC9kRbWCDsBNTAc2pnxYpx0B%2BxAXkh3B%2FlYc8sDFzhDamA5KOwtKEEV8dqRrI9fZkJ7ivDHBbzB20vAYaZyELpUWhQhTLU6yGz2QaCOfPA3Rji1vlVLcZA08F%2F1IoeliKt%2F3mwSuFyuHazCxrvy2tcfMzClFUeEubapshDmcK81rb5GuIZye0wR0ApHbtG1%2FqwBveh2z8iUNi0yIkaBUBL1HWRQP%2F%2FwdlfdEt2BqPUYGjUUiGkdZkBIQfmno4SUPtdITQspL8ky3QULbXBB2iOgVfIhMGfwFUSeG4hJEqQwCuEly0OUl6tSIY71JIrwcvA2FLCQMB0lGdpm%2FofGo0UTDGpR5rHeeQOoZpHE%2FlxLvN2rP8Po%2FRGqrkifxGPH9R0oFMgHcHrz4RXqIaO%2F6Rd25H%2F%2F%2Ftseh%2FNXiRfq3Lc580aFqK2w%2BNJSoNlCIPN2DfSp07PrrQbl8uNxPRnjmVo8wgsjzvAY6pgFTZxaVYB0icLHWGB1QtLPsSDWJAZ7UGurFkCdD3jd6nYdgXtV0qqgT0k0INNwFqRMvkYgTuNuE7QVgvZRbyUwCVCrSPuNbOaMHZWcVWoeqEJutcezCQA6p%2BZSag8%2BvADjaYz8IgMZ9DgWSxS6ZRnJmHsTJ8lkMjJmj8LugpqKmXgFt5mJWPty8NBqIzTmLPzSb%2B%2B9mlsMahpat5RtanGweKo40zY8q&X-Amz-Signature=b3e5d7a66afe59ca1b67f237153e94d41166e00437ed796c3c59393956fc29b8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OTPMJWU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuv6ML83NkEIXyQwFDI2SvKQNNxikvquc3Da7%2FFXsfRAiBdYztmo4e6XbbczUCyYc%2FvLSJ810Ykn9z544usxCEiyyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjtHHIBKYHrkazIBGKtwDALsmfTEfpO%2FY2o%2BUjqNShgwvZpx63YIianKOStIM8xmMBnO2MP6kIL8welnDaw8uBpiuFh6g4qjon2WJOFk64skGvu7lMz2EpD2rP1bF4ZDx7IyA7N%2BgYeLxuFaUD%2BByi6nEWYAT3Nu6bQBuuvTYhB86NTqWaGmh1fihSC9kRbWCDsBNTAc2pnxYpx0B%2BxAXkh3B%2FlYc8sDFzhDamA5KOwtKEEV8dqRrI9fZkJ7ivDHBbzB20vAYaZyELpUWhQhTLU6yGz2QaCOfPA3Rji1vlVLcZA08F%2F1IoeliKt%2F3mwSuFyuHazCxrvy2tcfMzClFUeEubapshDmcK81rb5GuIZye0wR0ApHbtG1%2FqwBveh2z8iUNi0yIkaBUBL1HWRQP%2F%2FwdlfdEt2BqPUYGjUUiGkdZkBIQfmno4SUPtdITQspL8ky3QULbXBB2iOgVfIhMGfwFUSeG4hJEqQwCuEly0OUl6tSIY71JIrwcvA2FLCQMB0lGdpm%2FofGo0UTDGpR5rHeeQOoZpHE%2FlxLvN2rP8Po%2FRGqrkifxGPH9R0oFMgHcHrz4RXqIaO%2F6Rd25H%2F%2F%2Ftseh%2FNXiRfq3Lc580aFqK2w%2BNJSoNlCIPN2DfSp07PrrQbl8uNxPRnjmVo8wgsjzvAY6pgFTZxaVYB0icLHWGB1QtLPsSDWJAZ7UGurFkCdD3jd6nYdgXtV0qqgT0k0INNwFqRMvkYgTuNuE7QVgvZRbyUwCVCrSPuNbOaMHZWcVWoeqEJutcezCQA6p%2BZSag8%2BvADjaYz8IgMZ9DgWSxS6ZRnJmHsTJ8lkMjJmj8LugpqKmXgFt5mJWPty8NBqIzTmLPzSb%2B%2B9mlsMahpat5RtanGweKo40zY8q&X-Amz-Signature=81339f2dff2eeb143a4a5302795307a6e49191a32fef80e765608b434431b394&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OTPMJWU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuv6ML83NkEIXyQwFDI2SvKQNNxikvquc3Da7%2FFXsfRAiBdYztmo4e6XbbczUCyYc%2FvLSJ810Ykn9z544usxCEiyyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjtHHIBKYHrkazIBGKtwDALsmfTEfpO%2FY2o%2BUjqNShgwvZpx63YIianKOStIM8xmMBnO2MP6kIL8welnDaw8uBpiuFh6g4qjon2WJOFk64skGvu7lMz2EpD2rP1bF4ZDx7IyA7N%2BgYeLxuFaUD%2BByi6nEWYAT3Nu6bQBuuvTYhB86NTqWaGmh1fihSC9kRbWCDsBNTAc2pnxYpx0B%2BxAXkh3B%2FlYc8sDFzhDamA5KOwtKEEV8dqRrI9fZkJ7ivDHBbzB20vAYaZyELpUWhQhTLU6yGz2QaCOfPA3Rji1vlVLcZA08F%2F1IoeliKt%2F3mwSuFyuHazCxrvy2tcfMzClFUeEubapshDmcK81rb5GuIZye0wR0ApHbtG1%2FqwBveh2z8iUNi0yIkaBUBL1HWRQP%2F%2FwdlfdEt2BqPUYGjUUiGkdZkBIQfmno4SUPtdITQspL8ky3QULbXBB2iOgVfIhMGfwFUSeG4hJEqQwCuEly0OUl6tSIY71JIrwcvA2FLCQMB0lGdpm%2FofGo0UTDGpR5rHeeQOoZpHE%2FlxLvN2rP8Po%2FRGqrkifxGPH9R0oFMgHcHrz4RXqIaO%2F6Rd25H%2F%2F%2Ftseh%2FNXiRfq3Lc580aFqK2w%2BNJSoNlCIPN2DfSp07PrrQbl8uNxPRnjmVo8wgsjzvAY6pgFTZxaVYB0icLHWGB1QtLPsSDWJAZ7UGurFkCdD3jd6nYdgXtV0qqgT0k0INNwFqRMvkYgTuNuE7QVgvZRbyUwCVCrSPuNbOaMHZWcVWoeqEJutcezCQA6p%2BZSag8%2BvADjaYz8IgMZ9DgWSxS6ZRnJmHsTJ8lkMjJmj8LugpqKmXgFt5mJWPty8NBqIzTmLPzSb%2B%2B9mlsMahpat5RtanGweKo40zY8q&X-Amz-Signature=6832de984cd073d725bb0272974a11665a03257e189b4270654fc49ee2a379fc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OTPMJWU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuv6ML83NkEIXyQwFDI2SvKQNNxikvquc3Da7%2FFXsfRAiBdYztmo4e6XbbczUCyYc%2FvLSJ810Ykn9z544usxCEiyyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjtHHIBKYHrkazIBGKtwDALsmfTEfpO%2FY2o%2BUjqNShgwvZpx63YIianKOStIM8xmMBnO2MP6kIL8welnDaw8uBpiuFh6g4qjon2WJOFk64skGvu7lMz2EpD2rP1bF4ZDx7IyA7N%2BgYeLxuFaUD%2BByi6nEWYAT3Nu6bQBuuvTYhB86NTqWaGmh1fihSC9kRbWCDsBNTAc2pnxYpx0B%2BxAXkh3B%2FlYc8sDFzhDamA5KOwtKEEV8dqRrI9fZkJ7ivDHBbzB20vAYaZyELpUWhQhTLU6yGz2QaCOfPA3Rji1vlVLcZA08F%2F1IoeliKt%2F3mwSuFyuHazCxrvy2tcfMzClFUeEubapshDmcK81rb5GuIZye0wR0ApHbtG1%2FqwBveh2z8iUNi0yIkaBUBL1HWRQP%2F%2FwdlfdEt2BqPUYGjUUiGkdZkBIQfmno4SUPtdITQspL8ky3QULbXBB2iOgVfIhMGfwFUSeG4hJEqQwCuEly0OUl6tSIY71JIrwcvA2FLCQMB0lGdpm%2FofGo0UTDGpR5rHeeQOoZpHE%2FlxLvN2rP8Po%2FRGqrkifxGPH9R0oFMgHcHrz4RXqIaO%2F6Rd25H%2F%2F%2Ftseh%2FNXiRfq3Lc580aFqK2w%2BNJSoNlCIPN2DfSp07PrrQbl8uNxPRnjmVo8wgsjzvAY6pgFTZxaVYB0icLHWGB1QtLPsSDWJAZ7UGurFkCdD3jd6nYdgXtV0qqgT0k0INNwFqRMvkYgTuNuE7QVgvZRbyUwCVCrSPuNbOaMHZWcVWoeqEJutcezCQA6p%2BZSag8%2BvADjaYz8IgMZ9DgWSxS6ZRnJmHsTJ8lkMjJmj8LugpqKmXgFt5mJWPty8NBqIzTmLPzSb%2B%2B9mlsMahpat5RtanGweKo40zY8q&X-Amz-Signature=db1d23f0b7e5ddc968d2073b9da10e1d19432072b53e61c5f8ffb4e31f02d0d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N7K7OWO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgi%2BQLYXRFDjjc1lnXYcHF%2FPmJ%2B%2FOdOeTw4iSWFs35VAiEAm%2BhMqZ%2BhOHCmJyESJiFcA4MSzOf5ozLsyaI88hclPRoqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMg3OHABxmZ0Kn0%2BlyrcA%2FKONadBHvsi1iPCQOA5aDW48M7qEj9EDqsY4c9ulnQRmEYq33FprxwACJ5dNvsFMjvNnA4MEqfEPPUON1qIENHWKJs7v3NyegEDGn3b9uov2kfWMwCV9O9nNOKMC2%2FSb58yO76N62SR1EJWO6mWSaCeJfwJZYxRiHFLlhaXhtqeJIfSC5VcWZsd1AJ2lEdyDPRIU%2FrohrAlamBLaBVlcFBAjCeUC7UiY2qa0QrieYQjbvnG5WcyENlsqwOnaf7rZWEmTfdXwjMdCQFHO8xX8SO8T%2Fr9HK21gdkoqhO90W0VjRzgafvw2TsfUrgzpBKp%2BvZXCaIENPhXkTxEupQnAzmD%2FmLYF5OGS2VqwNU6nyiN3ckbXOzqzV7HZKhX945C16RSCKBDohcbmvkK3A261%2BnScKLQ%2FGbgTvASWYRv3jI3jJVb8bqwZw1x6Sy39I7ZtO4dwB2d7P7W%2BSlGCGF7bXb%2F38M4jhrJx8%2B4l0rB8l5QgTvaJ5dPgz2KIT81r%2BOuAxzL5QnXQ5NX76ZedtfKAXhyQBQHUx1KxOAlsTNR0qDuiH%2BDj22kTtu%2FyMEibEkWfn1JkUN80lf%2FOCyFzVR2YzevsofjfN0%2B1wcsVWcYa9YTj736YicHALLKBQ9tMLDI87wGOqUBLBGfLTfuRI56FKBn8N7KaXNVgmoFiV9K%2Ft4VAdYnnXftynglndDfcatURBv2zxeojRwwzGd7jEvH3VuQ9wXyep6E41uhU9BP9nstkqpChCitJl93q4nkVg5iMIHphFL1XMfjh%2FsBwQVaOS%2F69%2F%2F3MNUyPJl9%2BQm9%2BVZq6Bs%2FARupJ3CXZVuRFQUKwN%2Bc4RA9bgV82OlkPmPrw4pZdQc6O3vMGz5g&X-Amz-Signature=b88aa6cc2646cc06323cbeb7ac7b0c7f6b362a641fde3691ecd5cc4ac08970bc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N7K7OWO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgi%2BQLYXRFDjjc1lnXYcHF%2FPmJ%2B%2FOdOeTw4iSWFs35VAiEAm%2BhMqZ%2BhOHCmJyESJiFcA4MSzOf5ozLsyaI88hclPRoqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMg3OHABxmZ0Kn0%2BlyrcA%2FKONadBHvsi1iPCQOA5aDW48M7qEj9EDqsY4c9ulnQRmEYq33FprxwACJ5dNvsFMjvNnA4MEqfEPPUON1qIENHWKJs7v3NyegEDGn3b9uov2kfWMwCV9O9nNOKMC2%2FSb58yO76N62SR1EJWO6mWSaCeJfwJZYxRiHFLlhaXhtqeJIfSC5VcWZsd1AJ2lEdyDPRIU%2FrohrAlamBLaBVlcFBAjCeUC7UiY2qa0QrieYQjbvnG5WcyENlsqwOnaf7rZWEmTfdXwjMdCQFHO8xX8SO8T%2Fr9HK21gdkoqhO90W0VjRzgafvw2TsfUrgzpBKp%2BvZXCaIENPhXkTxEupQnAzmD%2FmLYF5OGS2VqwNU6nyiN3ckbXOzqzV7HZKhX945C16RSCKBDohcbmvkK3A261%2BnScKLQ%2FGbgTvASWYRv3jI3jJVb8bqwZw1x6Sy39I7ZtO4dwB2d7P7W%2BSlGCGF7bXb%2F38M4jhrJx8%2B4l0rB8l5QgTvaJ5dPgz2KIT81r%2BOuAxzL5QnXQ5NX76ZedtfKAXhyQBQHUx1KxOAlsTNR0qDuiH%2BDj22kTtu%2FyMEibEkWfn1JkUN80lf%2FOCyFzVR2YzevsofjfN0%2B1wcsVWcYa9YTj736YicHALLKBQ9tMLDI87wGOqUBLBGfLTfuRI56FKBn8N7KaXNVgmoFiV9K%2Ft4VAdYnnXftynglndDfcatURBv2zxeojRwwzGd7jEvH3VuQ9wXyep6E41uhU9BP9nstkqpChCitJl93q4nkVg5iMIHphFL1XMfjh%2FsBwQVaOS%2F69%2F%2F3MNUyPJl9%2BQm9%2BVZq6Bs%2FARupJ3CXZVuRFQUKwN%2Bc4RA9bgV82OlkPmPrw4pZdQc6O3vMGz5g&X-Amz-Signature=b52149560deae90ab759ff87ccc3eba3fc949289e029a8faa4159fd66faad1e5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N7K7OWO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgi%2BQLYXRFDjjc1lnXYcHF%2FPmJ%2B%2FOdOeTw4iSWFs35VAiEAm%2BhMqZ%2BhOHCmJyESJiFcA4MSzOf5ozLsyaI88hclPRoqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMg3OHABxmZ0Kn0%2BlyrcA%2FKONadBHvsi1iPCQOA5aDW48M7qEj9EDqsY4c9ulnQRmEYq33FprxwACJ5dNvsFMjvNnA4MEqfEPPUON1qIENHWKJs7v3NyegEDGn3b9uov2kfWMwCV9O9nNOKMC2%2FSb58yO76N62SR1EJWO6mWSaCeJfwJZYxRiHFLlhaXhtqeJIfSC5VcWZsd1AJ2lEdyDPRIU%2FrohrAlamBLaBVlcFBAjCeUC7UiY2qa0QrieYQjbvnG5WcyENlsqwOnaf7rZWEmTfdXwjMdCQFHO8xX8SO8T%2Fr9HK21gdkoqhO90W0VjRzgafvw2TsfUrgzpBKp%2BvZXCaIENPhXkTxEupQnAzmD%2FmLYF5OGS2VqwNU6nyiN3ckbXOzqzV7HZKhX945C16RSCKBDohcbmvkK3A261%2BnScKLQ%2FGbgTvASWYRv3jI3jJVb8bqwZw1x6Sy39I7ZtO4dwB2d7P7W%2BSlGCGF7bXb%2F38M4jhrJx8%2B4l0rB8l5QgTvaJ5dPgz2KIT81r%2BOuAxzL5QnXQ5NX76ZedtfKAXhyQBQHUx1KxOAlsTNR0qDuiH%2BDj22kTtu%2FyMEibEkWfn1JkUN80lf%2FOCyFzVR2YzevsofjfN0%2B1wcsVWcYa9YTj736YicHALLKBQ9tMLDI87wGOqUBLBGfLTfuRI56FKBn8N7KaXNVgmoFiV9K%2Ft4VAdYnnXftynglndDfcatURBv2zxeojRwwzGd7jEvH3VuQ9wXyep6E41uhU9BP9nstkqpChCitJl93q4nkVg5iMIHphFL1XMfjh%2FsBwQVaOS%2F69%2F%2F3MNUyPJl9%2BQm9%2BVZq6Bs%2FARupJ3CXZVuRFQUKwN%2Bc4RA9bgV82OlkPmPrw4pZdQc6O3vMGz5g&X-Amz-Signature=279bbd8ea62c1f1a765b2db3f791d8df399140f62e699dd78656c47187a82a1b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N7K7OWO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgi%2BQLYXRFDjjc1lnXYcHF%2FPmJ%2B%2FOdOeTw4iSWFs35VAiEAm%2BhMqZ%2BhOHCmJyESJiFcA4MSzOf5ozLsyaI88hclPRoqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMg3OHABxmZ0Kn0%2BlyrcA%2FKONadBHvsi1iPCQOA5aDW48M7qEj9EDqsY4c9ulnQRmEYq33FprxwACJ5dNvsFMjvNnA4MEqfEPPUON1qIENHWKJs7v3NyegEDGn3b9uov2kfWMwCV9O9nNOKMC2%2FSb58yO76N62SR1EJWO6mWSaCeJfwJZYxRiHFLlhaXhtqeJIfSC5VcWZsd1AJ2lEdyDPRIU%2FrohrAlamBLaBVlcFBAjCeUC7UiY2qa0QrieYQjbvnG5WcyENlsqwOnaf7rZWEmTfdXwjMdCQFHO8xX8SO8T%2Fr9HK21gdkoqhO90W0VjRzgafvw2TsfUrgzpBKp%2BvZXCaIENPhXkTxEupQnAzmD%2FmLYF5OGS2VqwNU6nyiN3ckbXOzqzV7HZKhX945C16RSCKBDohcbmvkK3A261%2BnScKLQ%2FGbgTvASWYRv3jI3jJVb8bqwZw1x6Sy39I7ZtO4dwB2d7P7W%2BSlGCGF7bXb%2F38M4jhrJx8%2B4l0rB8l5QgTvaJ5dPgz2KIT81r%2BOuAxzL5QnXQ5NX76ZedtfKAXhyQBQHUx1KxOAlsTNR0qDuiH%2BDj22kTtu%2FyMEibEkWfn1JkUN80lf%2FOCyFzVR2YzevsofjfN0%2B1wcsVWcYa9YTj736YicHALLKBQ9tMLDI87wGOqUBLBGfLTfuRI56FKBn8N7KaXNVgmoFiV9K%2Ft4VAdYnnXftynglndDfcatURBv2zxeojRwwzGd7jEvH3VuQ9wXyep6E41uhU9BP9nstkqpChCitJl93q4nkVg5iMIHphFL1XMfjh%2FsBwQVaOS%2F69%2F%2F3MNUyPJl9%2BQm9%2BVZq6Bs%2FARupJ3CXZVuRFQUKwN%2Bc4RA9bgV82OlkPmPrw4pZdQc6O3vMGz5g&X-Amz-Signature=82fc7089f9ae76624ea0f9d7f50bba7eb42bdeae4a9dfeed5d76567d113fa3e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N7K7OWO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgi%2BQLYXRFDjjc1lnXYcHF%2FPmJ%2B%2FOdOeTw4iSWFs35VAiEAm%2BhMqZ%2BhOHCmJyESJiFcA4MSzOf5ozLsyaI88hclPRoqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMg3OHABxmZ0Kn0%2BlyrcA%2FKONadBHvsi1iPCQOA5aDW48M7qEj9EDqsY4c9ulnQRmEYq33FprxwACJ5dNvsFMjvNnA4MEqfEPPUON1qIENHWKJs7v3NyegEDGn3b9uov2kfWMwCV9O9nNOKMC2%2FSb58yO76N62SR1EJWO6mWSaCeJfwJZYxRiHFLlhaXhtqeJIfSC5VcWZsd1AJ2lEdyDPRIU%2FrohrAlamBLaBVlcFBAjCeUC7UiY2qa0QrieYQjbvnG5WcyENlsqwOnaf7rZWEmTfdXwjMdCQFHO8xX8SO8T%2Fr9HK21gdkoqhO90W0VjRzgafvw2TsfUrgzpBKp%2BvZXCaIENPhXkTxEupQnAzmD%2FmLYF5OGS2VqwNU6nyiN3ckbXOzqzV7HZKhX945C16RSCKBDohcbmvkK3A261%2BnScKLQ%2FGbgTvASWYRv3jI3jJVb8bqwZw1x6Sy39I7ZtO4dwB2d7P7W%2BSlGCGF7bXb%2F38M4jhrJx8%2B4l0rB8l5QgTvaJ5dPgz2KIT81r%2BOuAxzL5QnXQ5NX76ZedtfKAXhyQBQHUx1KxOAlsTNR0qDuiH%2BDj22kTtu%2FyMEibEkWfn1JkUN80lf%2FOCyFzVR2YzevsofjfN0%2B1wcsVWcYa9YTj736YicHALLKBQ9tMLDI87wGOqUBLBGfLTfuRI56FKBn8N7KaXNVgmoFiV9K%2Ft4VAdYnnXftynglndDfcatURBv2zxeojRwwzGd7jEvH3VuQ9wXyep6E41uhU9BP9nstkqpChCitJl93q4nkVg5iMIHphFL1XMfjh%2FsBwQVaOS%2F69%2F%2F3MNUyPJl9%2BQm9%2BVZq6Bs%2FARupJ3CXZVuRFQUKwN%2Bc4RA9bgV82OlkPmPrw4pZdQc6O3vMGz5g&X-Amz-Signature=0e9f6731ace78eec6eb81f142ef583594c1048fb3f4d94f2c959caac753a625d&X-Amz-SignedHeaders=host&x-id=GetObject)
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


