

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAPX2ZNE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIDsGkPERbcCB2lB3%2FvxYO7%2BDgN3vv4WNvTd2Ae0tLqDFAiEA7W%2BBZn4mNWwKIsr3YQlY%2BlTfGTCWN%2FNTg8YVJNkRLHwq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM8xrqTYJSk%2FubhsoSrcA21YZNHikCICksj6tJZ71KXE3P4f1Ij42gvi9JwI3p2tvymFXrQnYI6luSqHel3f552b0X6g7%2BSb%2FvZRTIV6VrnMCxeShs6PDrdqYbwiNWMh%2FEr%2BxOg60KOqdI1Q1bCmPl5hize115u%2BmjHrf%2FcHbfFc6Pn%2F1biTLA%2BFzL4gIPgcGDazFKESB10i7LtJuSzNRny3SS0p%2BuhWK0AF64eQsvl74koptX5UERIGKyKkZUmEb9IVu7J4nvETqY1Eb0UHRk1JeFQJi98gfjzhih%2BgeY77KnEb1Z8HA4tbPtr%2F654d5XBzAQDBGTJYLu%2FXr6%2FFkxL%2BUViU6qpK8NiejBTRQXWvlAAVVu8SGOwdH2CjhNYUlUVaGqRs1KcJI0ifgCXTleLe1ajSzu9nkaBOQyo79hXv6G2eSINZbc4PqsN6LNIawgFUUYqmgHaH%2Ff6ACHNZg63ZRdeovqCrYzzYc3sEHWIG2KZRh0YjGCmJriapuzBz2iXvt81p7IOnxZWMbOacE5xMfL2skeFZUH6CDe5FL%2Fsf%2F4C4ME0T77ys6OsDkAsafrbON%2BIVUwTiF5epl%2BQsUF4cNe1X%2Bh%2BhzsiW7UGzSkL%2FFWWKj5dZY7xaLGVUaohAbfn9XRkL2b%2FaHNWdMJDRkb0GOqUBMIbmx9RDxpM8G0Bjd7M6x7uITYbmEJGyh3swWSmlk6x%2BUWk1YD5PVv7Xaf4Or6wSn%2FH57b94OAdMzoQ5kle8c8CeFafkZalTEeP4C3JqSv%2BeD5l3cLTh%2FDVEQ1MFnv%2FxDisCZXf3jty4hozeAx5b%2FE1hNXR17dYZxgZAU9wpP3GbvgGPIGJOP3CmbQTNUmrl1UxPOqf%2BU3j%2Fx4aZsAbeLoW%2FBAIr&X-Amz-Signature=cf7c8ba018df987e56cd7acdf833f1625b1a698d0247c001942ce88bff0e8aaf&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQONBBDG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCFIsTX%2BS6HbrqjMsw1lAqDH4VvYfF8bDrbzMSIFqOAgAIhALLhKlNQ9ygFYe4d%2FMuTbVXqrKIRealeKRPPalA8hdsqKv8DCFkQABoMNjM3NDIzMTgzODA1IgwE8Tqd%2FTCbTs11AZsq3AMlDbmkMOX0MoZbxUZXKFhXpcn3CdeDhzRkXIamIiFxetJk3ExvlKopNf%2BlItlTLcXHHajLf71KxRkkny3zmGRdl2ucstdf0DZTqSzNH0mQyx3KQBXkr0Yq1GUdj%2FH74%2F5TEsNNstbeQnE%2FS%2Bmg6O%2Bvx41vzH65UO%2Bt47G5n14jXr9mz4EROPxG2NwMRDa%2FYW4YCU6iYuq%2FZKAYMUtcN3VY318AmUh5cuekO9Lma%2B%2BBWysNgcmRlnhGjFXdC69%2BgisVKl%2BoVmqgnqkZdgC0sQ9JGryMj9DWq04jhK5VaOPNeslcxSF710t5VJBg7wSCB%2BhPg2FYA44Y%2Fw39FTwzKnOqQXhE2JfOsojR0IDtnakTXkFoXel6Hd3l32ozZII%2FGvQVwGAGWwpYK5I7sK4sqqLjoAev3FChxohkPauIVzpZPMXJV6CzBYi%2BbVneZ%2B%2B3qyiDLvFWVbsIeGJw0V2zxGhP6uVyScl0t2ne9mFw1yOyg%2B8UnmnC0YNBnl38qjtOAAaxKyUXFdawvjp27Lwkm9fluLNVbnz1ONErsm8lb6uDKL1iYBD3%2FUInj9LPE7QXcPYLag1F7SwzxglMUV6ICyu1xdbAB9mABScq42X93IMWEqyiYA%2Fo%2FzhhAT92yzDp0ZG9BjqkAbPwswliIusnEdOfLblbRYo9ebQ%2B2wIppCcUQK%2BHFxlN69pnG%2BDjhVYefic7rps4vsO1shWZW410mLVbSqQQ5MmjIVB4686MIChxVGhY5Uq65L6hJT72t6JcE2U1hCZpGp8d5z4%2BJ%2FsJROeGM4Kf8SRZK%2FupvQmirC%2F68ZYfR6A7uB6A%2BZozMi%2Fgwg%2Bwuty%2FuwPOkUbuXhjbr%2FIdwsZ4plBe9oMG&X-Amz-Signature=a9f52f660cf9aeaebe0f00ab139fd7e0b84aff68208656406292bcd3f440180f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQONBBDG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCFIsTX%2BS6HbrqjMsw1lAqDH4VvYfF8bDrbzMSIFqOAgAIhALLhKlNQ9ygFYe4d%2FMuTbVXqrKIRealeKRPPalA8hdsqKv8DCFkQABoMNjM3NDIzMTgzODA1IgwE8Tqd%2FTCbTs11AZsq3AMlDbmkMOX0MoZbxUZXKFhXpcn3CdeDhzRkXIamIiFxetJk3ExvlKopNf%2BlItlTLcXHHajLf71KxRkkny3zmGRdl2ucstdf0DZTqSzNH0mQyx3KQBXkr0Yq1GUdj%2FH74%2F5TEsNNstbeQnE%2FS%2Bmg6O%2Bvx41vzH65UO%2Bt47G5n14jXr9mz4EROPxG2NwMRDa%2FYW4YCU6iYuq%2FZKAYMUtcN3VY318AmUh5cuekO9Lma%2B%2BBWysNgcmRlnhGjFXdC69%2BgisVKl%2BoVmqgnqkZdgC0sQ9JGryMj9DWq04jhK5VaOPNeslcxSF710t5VJBg7wSCB%2BhPg2FYA44Y%2Fw39FTwzKnOqQXhE2JfOsojR0IDtnakTXkFoXel6Hd3l32ozZII%2FGvQVwGAGWwpYK5I7sK4sqqLjoAev3FChxohkPauIVzpZPMXJV6CzBYi%2BbVneZ%2B%2B3qyiDLvFWVbsIeGJw0V2zxGhP6uVyScl0t2ne9mFw1yOyg%2B8UnmnC0YNBnl38qjtOAAaxKyUXFdawvjp27Lwkm9fluLNVbnz1ONErsm8lb6uDKL1iYBD3%2FUInj9LPE7QXcPYLag1F7SwzxglMUV6ICyu1xdbAB9mABScq42X93IMWEqyiYA%2Fo%2FzhhAT92yzDp0ZG9BjqkAbPwswliIusnEdOfLblbRYo9ebQ%2B2wIppCcUQK%2BHFxlN69pnG%2BDjhVYefic7rps4vsO1shWZW410mLVbSqQQ5MmjIVB4686MIChxVGhY5Uq65L6hJT72t6JcE2U1hCZpGp8d5z4%2BJ%2FsJROeGM4Kf8SRZK%2FupvQmirC%2F68ZYfR6A7uB6A%2BZozMi%2Fgwg%2Bwuty%2FuwPOkUbuXhjbr%2FIdwsZ4plBe9oMG&X-Amz-Signature=2e33d45bd528de3d89a5fd4b74799c0951a442cb34b29bb708154c45fb6c4cfe&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQONBBDG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCFIsTX%2BS6HbrqjMsw1lAqDH4VvYfF8bDrbzMSIFqOAgAIhALLhKlNQ9ygFYe4d%2FMuTbVXqrKIRealeKRPPalA8hdsqKv8DCFkQABoMNjM3NDIzMTgzODA1IgwE8Tqd%2FTCbTs11AZsq3AMlDbmkMOX0MoZbxUZXKFhXpcn3CdeDhzRkXIamIiFxetJk3ExvlKopNf%2BlItlTLcXHHajLf71KxRkkny3zmGRdl2ucstdf0DZTqSzNH0mQyx3KQBXkr0Yq1GUdj%2FH74%2F5TEsNNstbeQnE%2FS%2Bmg6O%2Bvx41vzH65UO%2Bt47G5n14jXr9mz4EROPxG2NwMRDa%2FYW4YCU6iYuq%2FZKAYMUtcN3VY318AmUh5cuekO9Lma%2B%2BBWysNgcmRlnhGjFXdC69%2BgisVKl%2BoVmqgnqkZdgC0sQ9JGryMj9DWq04jhK5VaOPNeslcxSF710t5VJBg7wSCB%2BhPg2FYA44Y%2Fw39FTwzKnOqQXhE2JfOsojR0IDtnakTXkFoXel6Hd3l32ozZII%2FGvQVwGAGWwpYK5I7sK4sqqLjoAev3FChxohkPauIVzpZPMXJV6CzBYi%2BbVneZ%2B%2B3qyiDLvFWVbsIeGJw0V2zxGhP6uVyScl0t2ne9mFw1yOyg%2B8UnmnC0YNBnl38qjtOAAaxKyUXFdawvjp27Lwkm9fluLNVbnz1ONErsm8lb6uDKL1iYBD3%2FUInj9LPE7QXcPYLag1F7SwzxglMUV6ICyu1xdbAB9mABScq42X93IMWEqyiYA%2Fo%2FzhhAT92yzDp0ZG9BjqkAbPwswliIusnEdOfLblbRYo9ebQ%2B2wIppCcUQK%2BHFxlN69pnG%2BDjhVYefic7rps4vsO1shWZW410mLVbSqQQ5MmjIVB4686MIChxVGhY5Uq65L6hJT72t6JcE2U1hCZpGp8d5z4%2BJ%2FsJROeGM4Kf8SRZK%2FupvQmirC%2F68ZYfR6A7uB6A%2BZozMi%2Fgwg%2Bwuty%2FuwPOkUbuXhjbr%2FIdwsZ4plBe9oMG&X-Amz-Signature=018876ab7e0732d5ebd8074a0ea82f051ce992fe3b5ff5d2180a6b10aebd1a5c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQONBBDG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCFIsTX%2BS6HbrqjMsw1lAqDH4VvYfF8bDrbzMSIFqOAgAIhALLhKlNQ9ygFYe4d%2FMuTbVXqrKIRealeKRPPalA8hdsqKv8DCFkQABoMNjM3NDIzMTgzODA1IgwE8Tqd%2FTCbTs11AZsq3AMlDbmkMOX0MoZbxUZXKFhXpcn3CdeDhzRkXIamIiFxetJk3ExvlKopNf%2BlItlTLcXHHajLf71KxRkkny3zmGRdl2ucstdf0DZTqSzNH0mQyx3KQBXkr0Yq1GUdj%2FH74%2F5TEsNNstbeQnE%2FS%2Bmg6O%2Bvx41vzH65UO%2Bt47G5n14jXr9mz4EROPxG2NwMRDa%2FYW4YCU6iYuq%2FZKAYMUtcN3VY318AmUh5cuekO9Lma%2B%2BBWysNgcmRlnhGjFXdC69%2BgisVKl%2BoVmqgnqkZdgC0sQ9JGryMj9DWq04jhK5VaOPNeslcxSF710t5VJBg7wSCB%2BhPg2FYA44Y%2Fw39FTwzKnOqQXhE2JfOsojR0IDtnakTXkFoXel6Hd3l32ozZII%2FGvQVwGAGWwpYK5I7sK4sqqLjoAev3FChxohkPauIVzpZPMXJV6CzBYi%2BbVneZ%2B%2B3qyiDLvFWVbsIeGJw0V2zxGhP6uVyScl0t2ne9mFw1yOyg%2B8UnmnC0YNBnl38qjtOAAaxKyUXFdawvjp27Lwkm9fluLNVbnz1ONErsm8lb6uDKL1iYBD3%2FUInj9LPE7QXcPYLag1F7SwzxglMUV6ICyu1xdbAB9mABScq42X93IMWEqyiYA%2Fo%2FzhhAT92yzDp0ZG9BjqkAbPwswliIusnEdOfLblbRYo9ebQ%2B2wIppCcUQK%2BHFxlN69pnG%2BDjhVYefic7rps4vsO1shWZW410mLVbSqQQ5MmjIVB4686MIChxVGhY5Uq65L6hJT72t6JcE2U1hCZpGp8d5z4%2BJ%2FsJROeGM4Kf8SRZK%2FupvQmirC%2F68ZYfR6A7uB6A%2BZozMi%2Fgwg%2Bwuty%2FuwPOkUbuXhjbr%2FIdwsZ4plBe9oMG&X-Amz-Signature=19c99d38614ce80a932edd80abf13b54fb72645907c0fc70db064e9ad61f8352&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQONBBDG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCFIsTX%2BS6HbrqjMsw1lAqDH4VvYfF8bDrbzMSIFqOAgAIhALLhKlNQ9ygFYe4d%2FMuTbVXqrKIRealeKRPPalA8hdsqKv8DCFkQABoMNjM3NDIzMTgzODA1IgwE8Tqd%2FTCbTs11AZsq3AMlDbmkMOX0MoZbxUZXKFhXpcn3CdeDhzRkXIamIiFxetJk3ExvlKopNf%2BlItlTLcXHHajLf71KxRkkny3zmGRdl2ucstdf0DZTqSzNH0mQyx3KQBXkr0Yq1GUdj%2FH74%2F5TEsNNstbeQnE%2FS%2Bmg6O%2Bvx41vzH65UO%2Bt47G5n14jXr9mz4EROPxG2NwMRDa%2FYW4YCU6iYuq%2FZKAYMUtcN3VY318AmUh5cuekO9Lma%2B%2BBWysNgcmRlnhGjFXdC69%2BgisVKl%2BoVmqgnqkZdgC0sQ9JGryMj9DWq04jhK5VaOPNeslcxSF710t5VJBg7wSCB%2BhPg2FYA44Y%2Fw39FTwzKnOqQXhE2JfOsojR0IDtnakTXkFoXel6Hd3l32ozZII%2FGvQVwGAGWwpYK5I7sK4sqqLjoAev3FChxohkPauIVzpZPMXJV6CzBYi%2BbVneZ%2B%2B3qyiDLvFWVbsIeGJw0V2zxGhP6uVyScl0t2ne9mFw1yOyg%2B8UnmnC0YNBnl38qjtOAAaxKyUXFdawvjp27Lwkm9fluLNVbnz1ONErsm8lb6uDKL1iYBD3%2FUInj9LPE7QXcPYLag1F7SwzxglMUV6ICyu1xdbAB9mABScq42X93IMWEqyiYA%2Fo%2FzhhAT92yzDp0ZG9BjqkAbPwswliIusnEdOfLblbRYo9ebQ%2B2wIppCcUQK%2BHFxlN69pnG%2BDjhVYefic7rps4vsO1shWZW410mLVbSqQQ5MmjIVB4686MIChxVGhY5Uq65L6hJT72t6JcE2U1hCZpGp8d5z4%2BJ%2FsJROeGM4Kf8SRZK%2FupvQmirC%2F68ZYfR6A7uB6A%2BZozMi%2Fgwg%2Bwuty%2FuwPOkUbuXhjbr%2FIdwsZ4plBe9oMG&X-Amz-Signature=8aca60a3dd7896e7e0a88f9442c87b02e26d001e89266aea0f5df753b72337c4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAPX2ZNE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIDsGkPERbcCB2lB3%2FvxYO7%2BDgN3vv4WNvTd2Ae0tLqDFAiEA7W%2BBZn4mNWwKIsr3YQlY%2BlTfGTCWN%2FNTg8YVJNkRLHwq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM8xrqTYJSk%2FubhsoSrcA21YZNHikCICksj6tJZ71KXE3P4f1Ij42gvi9JwI3p2tvymFXrQnYI6luSqHel3f552b0X6g7%2BSb%2FvZRTIV6VrnMCxeShs6PDrdqYbwiNWMh%2FEr%2BxOg60KOqdI1Q1bCmPl5hize115u%2BmjHrf%2FcHbfFc6Pn%2F1biTLA%2BFzL4gIPgcGDazFKESB10i7LtJuSzNRny3SS0p%2BuhWK0AF64eQsvl74koptX5UERIGKyKkZUmEb9IVu7J4nvETqY1Eb0UHRk1JeFQJi98gfjzhih%2BgeY77KnEb1Z8HA4tbPtr%2F654d5XBzAQDBGTJYLu%2FXr6%2FFkxL%2BUViU6qpK8NiejBTRQXWvlAAVVu8SGOwdH2CjhNYUlUVaGqRs1KcJI0ifgCXTleLe1ajSzu9nkaBOQyo79hXv6G2eSINZbc4PqsN6LNIawgFUUYqmgHaH%2Ff6ACHNZg63ZRdeovqCrYzzYc3sEHWIG2KZRh0YjGCmJriapuzBz2iXvt81p7IOnxZWMbOacE5xMfL2skeFZUH6CDe5FL%2Fsf%2F4C4ME0T77ys6OsDkAsafrbON%2BIVUwTiF5epl%2BQsUF4cNe1X%2Bh%2BhzsiW7UGzSkL%2FFWWKj5dZY7xaLGVUaohAbfn9XRkL2b%2FaHNWdMJDRkb0GOqUBMIbmx9RDxpM8G0Bjd7M6x7uITYbmEJGyh3swWSmlk6x%2BUWk1YD5PVv7Xaf4Or6wSn%2FH57b94OAdMzoQ5kle8c8CeFafkZalTEeP4C3JqSv%2BeD5l3cLTh%2FDVEQ1MFnv%2FxDisCZXf3jty4hozeAx5b%2FE1hNXR17dYZxgZAU9wpP3GbvgGPIGJOP3CmbQTNUmrl1UxPOqf%2BU3j%2Fx4aZsAbeLoW%2FBAIr&X-Amz-Signature=b92ffe17072ec4ad5aa64fb3591325227c19bdd1d6e7dd80bf1b9cbd30b5cdf3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAPX2ZNE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIDsGkPERbcCB2lB3%2FvxYO7%2BDgN3vv4WNvTd2Ae0tLqDFAiEA7W%2BBZn4mNWwKIsr3YQlY%2BlTfGTCWN%2FNTg8YVJNkRLHwq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM8xrqTYJSk%2FubhsoSrcA21YZNHikCICksj6tJZ71KXE3P4f1Ij42gvi9JwI3p2tvymFXrQnYI6luSqHel3f552b0X6g7%2BSb%2FvZRTIV6VrnMCxeShs6PDrdqYbwiNWMh%2FEr%2BxOg60KOqdI1Q1bCmPl5hize115u%2BmjHrf%2FcHbfFc6Pn%2F1biTLA%2BFzL4gIPgcGDazFKESB10i7LtJuSzNRny3SS0p%2BuhWK0AF64eQsvl74koptX5UERIGKyKkZUmEb9IVu7J4nvETqY1Eb0UHRk1JeFQJi98gfjzhih%2BgeY77KnEb1Z8HA4tbPtr%2F654d5XBzAQDBGTJYLu%2FXr6%2FFkxL%2BUViU6qpK8NiejBTRQXWvlAAVVu8SGOwdH2CjhNYUlUVaGqRs1KcJI0ifgCXTleLe1ajSzu9nkaBOQyo79hXv6G2eSINZbc4PqsN6LNIawgFUUYqmgHaH%2Ff6ACHNZg63ZRdeovqCrYzzYc3sEHWIG2KZRh0YjGCmJriapuzBz2iXvt81p7IOnxZWMbOacE5xMfL2skeFZUH6CDe5FL%2Fsf%2F4C4ME0T77ys6OsDkAsafrbON%2BIVUwTiF5epl%2BQsUF4cNe1X%2Bh%2BhzsiW7UGzSkL%2FFWWKj5dZY7xaLGVUaohAbfn9XRkL2b%2FaHNWdMJDRkb0GOqUBMIbmx9RDxpM8G0Bjd7M6x7uITYbmEJGyh3swWSmlk6x%2BUWk1YD5PVv7Xaf4Or6wSn%2FH57b94OAdMzoQ5kle8c8CeFafkZalTEeP4C3JqSv%2BeD5l3cLTh%2FDVEQ1MFnv%2FxDisCZXf3jty4hozeAx5b%2FE1hNXR17dYZxgZAU9wpP3GbvgGPIGJOP3CmbQTNUmrl1UxPOqf%2BU3j%2Fx4aZsAbeLoW%2FBAIr&X-Amz-Signature=9f4f1e41a646d0696a41a89f740f58a196cc1455a3a1dc93dc52865f59b3ad04&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAPX2ZNE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIDsGkPERbcCB2lB3%2FvxYO7%2BDgN3vv4WNvTd2Ae0tLqDFAiEA7W%2BBZn4mNWwKIsr3YQlY%2BlTfGTCWN%2FNTg8YVJNkRLHwq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM8xrqTYJSk%2FubhsoSrcA21YZNHikCICksj6tJZ71KXE3P4f1Ij42gvi9JwI3p2tvymFXrQnYI6luSqHel3f552b0X6g7%2BSb%2FvZRTIV6VrnMCxeShs6PDrdqYbwiNWMh%2FEr%2BxOg60KOqdI1Q1bCmPl5hize115u%2BmjHrf%2FcHbfFc6Pn%2F1biTLA%2BFzL4gIPgcGDazFKESB10i7LtJuSzNRny3SS0p%2BuhWK0AF64eQsvl74koptX5UERIGKyKkZUmEb9IVu7J4nvETqY1Eb0UHRk1JeFQJi98gfjzhih%2BgeY77KnEb1Z8HA4tbPtr%2F654d5XBzAQDBGTJYLu%2FXr6%2FFkxL%2BUViU6qpK8NiejBTRQXWvlAAVVu8SGOwdH2CjhNYUlUVaGqRs1KcJI0ifgCXTleLe1ajSzu9nkaBOQyo79hXv6G2eSINZbc4PqsN6LNIawgFUUYqmgHaH%2Ff6ACHNZg63ZRdeovqCrYzzYc3sEHWIG2KZRh0YjGCmJriapuzBz2iXvt81p7IOnxZWMbOacE5xMfL2skeFZUH6CDe5FL%2Fsf%2F4C4ME0T77ys6OsDkAsafrbON%2BIVUwTiF5epl%2BQsUF4cNe1X%2Bh%2BhzsiW7UGzSkL%2FFWWKj5dZY7xaLGVUaohAbfn9XRkL2b%2FaHNWdMJDRkb0GOqUBMIbmx9RDxpM8G0Bjd7M6x7uITYbmEJGyh3swWSmlk6x%2BUWk1YD5PVv7Xaf4Or6wSn%2FH57b94OAdMzoQ5kle8c8CeFafkZalTEeP4C3JqSv%2BeD5l3cLTh%2FDVEQ1MFnv%2FxDisCZXf3jty4hozeAx5b%2FE1hNXR17dYZxgZAU9wpP3GbvgGPIGJOP3CmbQTNUmrl1UxPOqf%2BU3j%2Fx4aZsAbeLoW%2FBAIr&X-Amz-Signature=ec9e1ef56fe61485938f98d7716a1b469aee65ec43297c36c1ead1cc97482cf6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAPX2ZNE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIDsGkPERbcCB2lB3%2FvxYO7%2BDgN3vv4WNvTd2Ae0tLqDFAiEA7W%2BBZn4mNWwKIsr3YQlY%2BlTfGTCWN%2FNTg8YVJNkRLHwq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM8xrqTYJSk%2FubhsoSrcA21YZNHikCICksj6tJZ71KXE3P4f1Ij42gvi9JwI3p2tvymFXrQnYI6luSqHel3f552b0X6g7%2BSb%2FvZRTIV6VrnMCxeShs6PDrdqYbwiNWMh%2FEr%2BxOg60KOqdI1Q1bCmPl5hize115u%2BmjHrf%2FcHbfFc6Pn%2F1biTLA%2BFzL4gIPgcGDazFKESB10i7LtJuSzNRny3SS0p%2BuhWK0AF64eQsvl74koptX5UERIGKyKkZUmEb9IVu7J4nvETqY1Eb0UHRk1JeFQJi98gfjzhih%2BgeY77KnEb1Z8HA4tbPtr%2F654d5XBzAQDBGTJYLu%2FXr6%2FFkxL%2BUViU6qpK8NiejBTRQXWvlAAVVu8SGOwdH2CjhNYUlUVaGqRs1KcJI0ifgCXTleLe1ajSzu9nkaBOQyo79hXv6G2eSINZbc4PqsN6LNIawgFUUYqmgHaH%2Ff6ACHNZg63ZRdeovqCrYzzYc3sEHWIG2KZRh0YjGCmJriapuzBz2iXvt81p7IOnxZWMbOacE5xMfL2skeFZUH6CDe5FL%2Fsf%2F4C4ME0T77ys6OsDkAsafrbON%2BIVUwTiF5epl%2BQsUF4cNe1X%2Bh%2BhzsiW7UGzSkL%2FFWWKj5dZY7xaLGVUaohAbfn9XRkL2b%2FaHNWdMJDRkb0GOqUBMIbmx9RDxpM8G0Bjd7M6x7uITYbmEJGyh3swWSmlk6x%2BUWk1YD5PVv7Xaf4Or6wSn%2FH57b94OAdMzoQ5kle8c8CeFafkZalTEeP4C3JqSv%2BeD5l3cLTh%2FDVEQ1MFnv%2FxDisCZXf3jty4hozeAx5b%2FE1hNXR17dYZxgZAU9wpP3GbvgGPIGJOP3CmbQTNUmrl1UxPOqf%2BU3j%2Fx4aZsAbeLoW%2FBAIr&X-Amz-Signature=cbac3ed779c7880f7290ebe986ebb3a0b6d2fea0753383092b876d65d53fa2d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAPX2ZNE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIDsGkPERbcCB2lB3%2FvxYO7%2BDgN3vv4WNvTd2Ae0tLqDFAiEA7W%2BBZn4mNWwKIsr3YQlY%2BlTfGTCWN%2FNTg8YVJNkRLHwq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM8xrqTYJSk%2FubhsoSrcA21YZNHikCICksj6tJZ71KXE3P4f1Ij42gvi9JwI3p2tvymFXrQnYI6luSqHel3f552b0X6g7%2BSb%2FvZRTIV6VrnMCxeShs6PDrdqYbwiNWMh%2FEr%2BxOg60KOqdI1Q1bCmPl5hize115u%2BmjHrf%2FcHbfFc6Pn%2F1biTLA%2BFzL4gIPgcGDazFKESB10i7LtJuSzNRny3SS0p%2BuhWK0AF64eQsvl74koptX5UERIGKyKkZUmEb9IVu7J4nvETqY1Eb0UHRk1JeFQJi98gfjzhih%2BgeY77KnEb1Z8HA4tbPtr%2F654d5XBzAQDBGTJYLu%2FXr6%2FFkxL%2BUViU6qpK8NiejBTRQXWvlAAVVu8SGOwdH2CjhNYUlUVaGqRs1KcJI0ifgCXTleLe1ajSzu9nkaBOQyo79hXv6G2eSINZbc4PqsN6LNIawgFUUYqmgHaH%2Ff6ACHNZg63ZRdeovqCrYzzYc3sEHWIG2KZRh0YjGCmJriapuzBz2iXvt81p7IOnxZWMbOacE5xMfL2skeFZUH6CDe5FL%2Fsf%2F4C4ME0T77ys6OsDkAsafrbON%2BIVUwTiF5epl%2BQsUF4cNe1X%2Bh%2BhzsiW7UGzSkL%2FFWWKj5dZY7xaLGVUaohAbfn9XRkL2b%2FaHNWdMJDRkb0GOqUBMIbmx9RDxpM8G0Bjd7M6x7uITYbmEJGyh3swWSmlk6x%2BUWk1YD5PVv7Xaf4Or6wSn%2FH57b94OAdMzoQ5kle8c8CeFafkZalTEeP4C3JqSv%2BeD5l3cLTh%2FDVEQ1MFnv%2FxDisCZXf3jty4hozeAx5b%2FE1hNXR17dYZxgZAU9wpP3GbvgGPIGJOP3CmbQTNUmrl1UxPOqf%2BU3j%2Fx4aZsAbeLoW%2FBAIr&X-Amz-Signature=bdb69635e9bc5c78770fdc1975aa0e36c0b5038aad89b1ce3b22bc0108183662&X-Amz-SignedHeaders=host&x-id=GetObject)
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


