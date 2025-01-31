

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRIWSMGX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBQ%2FpPOGICdgkuA8NBSzH4oZaSUSsfW%2BNQvg%2BnO6gk9QIhAONVqhnlTzqCEH49UBFGkNW88zOihMXj0ZL5IZO2hX7JKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwgPQyi2OQTS8bRq%2Bgq3APQLyK9%2B3NsoKn5%2BaWW4h6Rv%2FweXE4mC%2Bs7chRBPGEqgNZkLQ5kqED5QXxVS3xSvZ%2BAMeIiiHaLQ67AcKraYSr4IoDO%2FJAUFN7ObQzCYUFRS5uaEbax5nccHLv7gZu1P%2F67ozE4m1H94DF4fAcr1th7xZY8pENUik76%2BArs7taME%2B1w1NptVaWwvJmYo4YNOmJV9dGCHcYdt7c3ZbQqHhBgSdAnTGaoaigryDjE9sla2yi3lGaKjF7mcr144f32WYo1AhgAZsfAylyAg8%2B%2FgPHrOhhTWcu9%2Fr3YvHVsLyIrrzDW98jvTxJ9eEXcsw6G3wlFWMR%2B92RYXF8jQFXrCraxjbEACyTecDxFMvINtCeoMGZ6%2FgpbagImhRTR76VVatM57HMC8tOzYH6tfDc6pHgfaP22SsBHmIe5MeMSOkWzTS9V8wxWbeoHJoWqDUAqMWzDLWKQSmfyPDuGpg5%2Fmi5YDKA9g9e5ujfhdK1ipAhOMQdU%2BvNeSco51C%2F6elQb%2FFRnFFS2uynA6QJSNzT6RAqj5rGwFRHWux%2FDI4I%2FB27NHdMGYiqGbfQqKUbpOOGr3oThRqdzxKW%2FkEXVvyYQ%2FRciFas6291K7%2F2YbjLK2sP42uWw41%2Fs6yDbybLw%2BzDUlPW8BjqkAW4GXQj7eEGD%2FdD167XbMtD9cJsXuNB66zhvJi1nzigstbe4DIkAUe6KBFYFKG8IfQYs4myw1rnac9Xr1P%2FIQB2bJ926tpncaY6nIeDQyaQgB6aR1yj1XL5rWFEonggnMWmKLbftnq19gU6QitXnqXRREoaoESKS8W8WIXuQlcieaoVP3i6kCb1HiAmtp6VzVJkgcv2PzV0CVFox9LMXaxz1ME6H&X-Amz-Signature=87ca03b53174174592f8825feddf7edaa658a937219fe8d1d414936845e55299&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGHCYPJS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq2quPyiXdGS70O9g5VCynn0M5Ucc4MMEHffgmrkDN4AiB33jxiiL4kYqjGHI35q3zdUZ6OJYfcXvCjPAqZxSJawiqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMePGYiRztxOhSS7NDKtwDbuYJIoikjxRzNk8do7iNucMmc59hk%2FoGFLc4r7xu%2FZGTKgV7YUuUA9s7StwYdzNvLr1ibbpTEbVxzVLiJblLFNZmZnQ8TU5nngliAfU%2BS4QkTBIb8weeNRoefixv535i8dLP5P%2FxxK6FgNgGNRtmxxni3ZHAiufkCwGHLrLmGElSlEO5waQ3mOsOGNV0hGM0r3Mfo6q2lOrNyefLFVAq3MQZcPOZww7RFNxQrAaBLXQTD7OdkWuyxxOE%2F4L%2Bus4fj1Q8%2FtSy%2FJYf7AzpyFrsfAkq1oWg8ADcueTEWqGE7ij1u6iey0Nv0I5q8mFkxY05QpbcyzhS7XVd8KKjVHGXTvopKtqIpzyNHAyo6V%2BMFF%2BmJrmMmPuzRf6sl8S1vUKWnWLBfdGqZLx8%2FOzAEZUHiUQOBIIM4%2Bmn8Ltys%2BiqMc4thFhqRU5cTUn2IRi4fnWdTDr8RsOk%2F7W3Pm1sputg5SFH4t1zm36rM27ahBNQINY37LYaT1DKtiiStW0Qhw54QHAUZ4Yj8u6KqH%2FFaM6FP%2FVdm%2F%2FEDE8GHYhaDAb6wsy9pYpmbHkRTJDCi0jHgAHBb6dQz0KWb6V78fYgC4tx9P6FH0T1cvYtO2ZhgyLbJ35s8nbZ%2FaSwSs%2FwOHkwnZX1vAY6pgHS2RoSIuLsw5wPmf9DI%2BmH4HPRBtM2qowZ2tl6WGVCrfVJJVwnQnKPQ8ELV74z%2BA0G7Co%2Bf8XIjgaDjNNO04Vb%2F5Qh4uFaCt2vPGhfNpFczAxkmLcn0nRXuS5qXnBnSTHmHCRRxhDi1Nniq%2FuSWiNFKmdElst2l8Ud9wGxH9URY7%2B6bYHOiaKgOVBqLQ%2FCWV0h%2BGDRQiwFT1DwDiu5QjWCG2xX0aYJ&X-Amz-Signature=38c366ca06b4318d63e2227436005b1843a8bd04319ff90b2608a91b7d18de38&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGHCYPJS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq2quPyiXdGS70O9g5VCynn0M5Ucc4MMEHffgmrkDN4AiB33jxiiL4kYqjGHI35q3zdUZ6OJYfcXvCjPAqZxSJawiqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMePGYiRztxOhSS7NDKtwDbuYJIoikjxRzNk8do7iNucMmc59hk%2FoGFLc4r7xu%2FZGTKgV7YUuUA9s7StwYdzNvLr1ibbpTEbVxzVLiJblLFNZmZnQ8TU5nngliAfU%2BS4QkTBIb8weeNRoefixv535i8dLP5P%2FxxK6FgNgGNRtmxxni3ZHAiufkCwGHLrLmGElSlEO5waQ3mOsOGNV0hGM0r3Mfo6q2lOrNyefLFVAq3MQZcPOZww7RFNxQrAaBLXQTD7OdkWuyxxOE%2F4L%2Bus4fj1Q8%2FtSy%2FJYf7AzpyFrsfAkq1oWg8ADcueTEWqGE7ij1u6iey0Nv0I5q8mFkxY05QpbcyzhS7XVd8KKjVHGXTvopKtqIpzyNHAyo6V%2BMFF%2BmJrmMmPuzRf6sl8S1vUKWnWLBfdGqZLx8%2FOzAEZUHiUQOBIIM4%2Bmn8Ltys%2BiqMc4thFhqRU5cTUn2IRi4fnWdTDr8RsOk%2F7W3Pm1sputg5SFH4t1zm36rM27ahBNQINY37LYaT1DKtiiStW0Qhw54QHAUZ4Yj8u6KqH%2FFaM6FP%2FVdm%2F%2FEDE8GHYhaDAb6wsy9pYpmbHkRTJDCi0jHgAHBb6dQz0KWb6V78fYgC4tx9P6FH0T1cvYtO2ZhgyLbJ35s8nbZ%2FaSwSs%2FwOHkwnZX1vAY6pgHS2RoSIuLsw5wPmf9DI%2BmH4HPRBtM2qowZ2tl6WGVCrfVJJVwnQnKPQ8ELV74z%2BA0G7Co%2Bf8XIjgaDjNNO04Vb%2F5Qh4uFaCt2vPGhfNpFczAxkmLcn0nRXuS5qXnBnSTHmHCRRxhDi1Nniq%2FuSWiNFKmdElst2l8Ud9wGxH9URY7%2B6bYHOiaKgOVBqLQ%2FCWV0h%2BGDRQiwFT1DwDiu5QjWCG2xX0aYJ&X-Amz-Signature=8b48d4ba58f2b4bd02689d150681f3afd17af9ac2ab30003ed1acca29e1156b8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGHCYPJS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq2quPyiXdGS70O9g5VCynn0M5Ucc4MMEHffgmrkDN4AiB33jxiiL4kYqjGHI35q3zdUZ6OJYfcXvCjPAqZxSJawiqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMePGYiRztxOhSS7NDKtwDbuYJIoikjxRzNk8do7iNucMmc59hk%2FoGFLc4r7xu%2FZGTKgV7YUuUA9s7StwYdzNvLr1ibbpTEbVxzVLiJblLFNZmZnQ8TU5nngliAfU%2BS4QkTBIb8weeNRoefixv535i8dLP5P%2FxxK6FgNgGNRtmxxni3ZHAiufkCwGHLrLmGElSlEO5waQ3mOsOGNV0hGM0r3Mfo6q2lOrNyefLFVAq3MQZcPOZww7RFNxQrAaBLXQTD7OdkWuyxxOE%2F4L%2Bus4fj1Q8%2FtSy%2FJYf7AzpyFrsfAkq1oWg8ADcueTEWqGE7ij1u6iey0Nv0I5q8mFkxY05QpbcyzhS7XVd8KKjVHGXTvopKtqIpzyNHAyo6V%2BMFF%2BmJrmMmPuzRf6sl8S1vUKWnWLBfdGqZLx8%2FOzAEZUHiUQOBIIM4%2Bmn8Ltys%2BiqMc4thFhqRU5cTUn2IRi4fnWdTDr8RsOk%2F7W3Pm1sputg5SFH4t1zm36rM27ahBNQINY37LYaT1DKtiiStW0Qhw54QHAUZ4Yj8u6KqH%2FFaM6FP%2FVdm%2F%2FEDE8GHYhaDAb6wsy9pYpmbHkRTJDCi0jHgAHBb6dQz0KWb6V78fYgC4tx9P6FH0T1cvYtO2ZhgyLbJ35s8nbZ%2FaSwSs%2FwOHkwnZX1vAY6pgHS2RoSIuLsw5wPmf9DI%2BmH4HPRBtM2qowZ2tl6WGVCrfVJJVwnQnKPQ8ELV74z%2BA0G7Co%2Bf8XIjgaDjNNO04Vb%2F5Qh4uFaCt2vPGhfNpFczAxkmLcn0nRXuS5qXnBnSTHmHCRRxhDi1Nniq%2FuSWiNFKmdElst2l8Ud9wGxH9URY7%2B6bYHOiaKgOVBqLQ%2FCWV0h%2BGDRQiwFT1DwDiu5QjWCG2xX0aYJ&X-Amz-Signature=0b354439d94f5df97d72f5d6aeb7804a58347f9b7058fa41663f2ec3dadf32fb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGHCYPJS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq2quPyiXdGS70O9g5VCynn0M5Ucc4MMEHffgmrkDN4AiB33jxiiL4kYqjGHI35q3zdUZ6OJYfcXvCjPAqZxSJawiqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMePGYiRztxOhSS7NDKtwDbuYJIoikjxRzNk8do7iNucMmc59hk%2FoGFLc4r7xu%2FZGTKgV7YUuUA9s7StwYdzNvLr1ibbpTEbVxzVLiJblLFNZmZnQ8TU5nngliAfU%2BS4QkTBIb8weeNRoefixv535i8dLP5P%2FxxK6FgNgGNRtmxxni3ZHAiufkCwGHLrLmGElSlEO5waQ3mOsOGNV0hGM0r3Mfo6q2lOrNyefLFVAq3MQZcPOZww7RFNxQrAaBLXQTD7OdkWuyxxOE%2F4L%2Bus4fj1Q8%2FtSy%2FJYf7AzpyFrsfAkq1oWg8ADcueTEWqGE7ij1u6iey0Nv0I5q8mFkxY05QpbcyzhS7XVd8KKjVHGXTvopKtqIpzyNHAyo6V%2BMFF%2BmJrmMmPuzRf6sl8S1vUKWnWLBfdGqZLx8%2FOzAEZUHiUQOBIIM4%2Bmn8Ltys%2BiqMc4thFhqRU5cTUn2IRi4fnWdTDr8RsOk%2F7W3Pm1sputg5SFH4t1zm36rM27ahBNQINY37LYaT1DKtiiStW0Qhw54QHAUZ4Yj8u6KqH%2FFaM6FP%2FVdm%2F%2FEDE8GHYhaDAb6wsy9pYpmbHkRTJDCi0jHgAHBb6dQz0KWb6V78fYgC4tx9P6FH0T1cvYtO2ZhgyLbJ35s8nbZ%2FaSwSs%2FwOHkwnZX1vAY6pgHS2RoSIuLsw5wPmf9DI%2BmH4HPRBtM2qowZ2tl6WGVCrfVJJVwnQnKPQ8ELV74z%2BA0G7Co%2Bf8XIjgaDjNNO04Vb%2F5Qh4uFaCt2vPGhfNpFczAxkmLcn0nRXuS5qXnBnSTHmHCRRxhDi1Nniq%2FuSWiNFKmdElst2l8Ud9wGxH9URY7%2B6bYHOiaKgOVBqLQ%2FCWV0h%2BGDRQiwFT1DwDiu5QjWCG2xX0aYJ&X-Amz-Signature=3d1d4b572c80c83dd9a788c680232cbe5d5157f3efa21b13ff2a92150633a214&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGHCYPJS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq2quPyiXdGS70O9g5VCynn0M5Ucc4MMEHffgmrkDN4AiB33jxiiL4kYqjGHI35q3zdUZ6OJYfcXvCjPAqZxSJawiqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMePGYiRztxOhSS7NDKtwDbuYJIoikjxRzNk8do7iNucMmc59hk%2FoGFLc4r7xu%2FZGTKgV7YUuUA9s7StwYdzNvLr1ibbpTEbVxzVLiJblLFNZmZnQ8TU5nngliAfU%2BS4QkTBIb8weeNRoefixv535i8dLP5P%2FxxK6FgNgGNRtmxxni3ZHAiufkCwGHLrLmGElSlEO5waQ3mOsOGNV0hGM0r3Mfo6q2lOrNyefLFVAq3MQZcPOZww7RFNxQrAaBLXQTD7OdkWuyxxOE%2F4L%2Bus4fj1Q8%2FtSy%2FJYf7AzpyFrsfAkq1oWg8ADcueTEWqGE7ij1u6iey0Nv0I5q8mFkxY05QpbcyzhS7XVd8KKjVHGXTvopKtqIpzyNHAyo6V%2BMFF%2BmJrmMmPuzRf6sl8S1vUKWnWLBfdGqZLx8%2FOzAEZUHiUQOBIIM4%2Bmn8Ltys%2BiqMc4thFhqRU5cTUn2IRi4fnWdTDr8RsOk%2F7W3Pm1sputg5SFH4t1zm36rM27ahBNQINY37LYaT1DKtiiStW0Qhw54QHAUZ4Yj8u6KqH%2FFaM6FP%2FVdm%2F%2FEDE8GHYhaDAb6wsy9pYpmbHkRTJDCi0jHgAHBb6dQz0KWb6V78fYgC4tx9P6FH0T1cvYtO2ZhgyLbJ35s8nbZ%2FaSwSs%2FwOHkwnZX1vAY6pgHS2RoSIuLsw5wPmf9DI%2BmH4HPRBtM2qowZ2tl6WGVCrfVJJVwnQnKPQ8ELV74z%2BA0G7Co%2Bf8XIjgaDjNNO04Vb%2F5Qh4uFaCt2vPGhfNpFczAxkmLcn0nRXuS5qXnBnSTHmHCRRxhDi1Nniq%2FuSWiNFKmdElst2l8Ud9wGxH9URY7%2B6bYHOiaKgOVBqLQ%2FCWV0h%2BGDRQiwFT1DwDiu5QjWCG2xX0aYJ&X-Amz-Signature=68c2087421c0404ed5cf857aefaf5e30a3298876f8920cd0029a9581891a5c19&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRIWSMGX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBQ%2FpPOGICdgkuA8NBSzH4oZaSUSsfW%2BNQvg%2BnO6gk9QIhAONVqhnlTzqCEH49UBFGkNW88zOihMXj0ZL5IZO2hX7JKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwgPQyi2OQTS8bRq%2Bgq3APQLyK9%2B3NsoKn5%2BaWW4h6Rv%2FweXE4mC%2Bs7chRBPGEqgNZkLQ5kqED5QXxVS3xSvZ%2BAMeIiiHaLQ67AcKraYSr4IoDO%2FJAUFN7ObQzCYUFRS5uaEbax5nccHLv7gZu1P%2F67ozE4m1H94DF4fAcr1th7xZY8pENUik76%2BArs7taME%2B1w1NptVaWwvJmYo4YNOmJV9dGCHcYdt7c3ZbQqHhBgSdAnTGaoaigryDjE9sla2yi3lGaKjF7mcr144f32WYo1AhgAZsfAylyAg8%2B%2FgPHrOhhTWcu9%2Fr3YvHVsLyIrrzDW98jvTxJ9eEXcsw6G3wlFWMR%2B92RYXF8jQFXrCraxjbEACyTecDxFMvINtCeoMGZ6%2FgpbagImhRTR76VVatM57HMC8tOzYH6tfDc6pHgfaP22SsBHmIe5MeMSOkWzTS9V8wxWbeoHJoWqDUAqMWzDLWKQSmfyPDuGpg5%2Fmi5YDKA9g9e5ujfhdK1ipAhOMQdU%2BvNeSco51C%2F6elQb%2FFRnFFS2uynA6QJSNzT6RAqj5rGwFRHWux%2FDI4I%2FB27NHdMGYiqGbfQqKUbpOOGr3oThRqdzxKW%2FkEXVvyYQ%2FRciFas6291K7%2F2YbjLK2sP42uWw41%2Fs6yDbybLw%2BzDUlPW8BjqkAW4GXQj7eEGD%2FdD167XbMtD9cJsXuNB66zhvJi1nzigstbe4DIkAUe6KBFYFKG8IfQYs4myw1rnac9Xr1P%2FIQB2bJ926tpncaY6nIeDQyaQgB6aR1yj1XL5rWFEonggnMWmKLbftnq19gU6QitXnqXRREoaoESKS8W8WIXuQlcieaoVP3i6kCb1HiAmtp6VzVJkgcv2PzV0CVFox9LMXaxz1ME6H&X-Amz-Signature=aed9a1fd237d0bde5be8c9bcb2043df24d83d3d6ec552cd3d24046ca7e6c5f83&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRIWSMGX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBQ%2FpPOGICdgkuA8NBSzH4oZaSUSsfW%2BNQvg%2BnO6gk9QIhAONVqhnlTzqCEH49UBFGkNW88zOihMXj0ZL5IZO2hX7JKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwgPQyi2OQTS8bRq%2Bgq3APQLyK9%2B3NsoKn5%2BaWW4h6Rv%2FweXE4mC%2Bs7chRBPGEqgNZkLQ5kqED5QXxVS3xSvZ%2BAMeIiiHaLQ67AcKraYSr4IoDO%2FJAUFN7ObQzCYUFRS5uaEbax5nccHLv7gZu1P%2F67ozE4m1H94DF4fAcr1th7xZY8pENUik76%2BArs7taME%2B1w1NptVaWwvJmYo4YNOmJV9dGCHcYdt7c3ZbQqHhBgSdAnTGaoaigryDjE9sla2yi3lGaKjF7mcr144f32WYo1AhgAZsfAylyAg8%2B%2FgPHrOhhTWcu9%2Fr3YvHVsLyIrrzDW98jvTxJ9eEXcsw6G3wlFWMR%2B92RYXF8jQFXrCraxjbEACyTecDxFMvINtCeoMGZ6%2FgpbagImhRTR76VVatM57HMC8tOzYH6tfDc6pHgfaP22SsBHmIe5MeMSOkWzTS9V8wxWbeoHJoWqDUAqMWzDLWKQSmfyPDuGpg5%2Fmi5YDKA9g9e5ujfhdK1ipAhOMQdU%2BvNeSco51C%2F6elQb%2FFRnFFS2uynA6QJSNzT6RAqj5rGwFRHWux%2FDI4I%2FB27NHdMGYiqGbfQqKUbpOOGr3oThRqdzxKW%2FkEXVvyYQ%2FRciFas6291K7%2F2YbjLK2sP42uWw41%2Fs6yDbybLw%2BzDUlPW8BjqkAW4GXQj7eEGD%2FdD167XbMtD9cJsXuNB66zhvJi1nzigstbe4DIkAUe6KBFYFKG8IfQYs4myw1rnac9Xr1P%2FIQB2bJ926tpncaY6nIeDQyaQgB6aR1yj1XL5rWFEonggnMWmKLbftnq19gU6QitXnqXRREoaoESKS8W8WIXuQlcieaoVP3i6kCb1HiAmtp6VzVJkgcv2PzV0CVFox9LMXaxz1ME6H&X-Amz-Signature=26a58e1a03d6c21155e42d9db1b6a862a7409793a2835645fda662ff2340b6e7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRIWSMGX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBQ%2FpPOGICdgkuA8NBSzH4oZaSUSsfW%2BNQvg%2BnO6gk9QIhAONVqhnlTzqCEH49UBFGkNW88zOihMXj0ZL5IZO2hX7JKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwgPQyi2OQTS8bRq%2Bgq3APQLyK9%2B3NsoKn5%2BaWW4h6Rv%2FweXE4mC%2Bs7chRBPGEqgNZkLQ5kqED5QXxVS3xSvZ%2BAMeIiiHaLQ67AcKraYSr4IoDO%2FJAUFN7ObQzCYUFRS5uaEbax5nccHLv7gZu1P%2F67ozE4m1H94DF4fAcr1th7xZY8pENUik76%2BArs7taME%2B1w1NptVaWwvJmYo4YNOmJV9dGCHcYdt7c3ZbQqHhBgSdAnTGaoaigryDjE9sla2yi3lGaKjF7mcr144f32WYo1AhgAZsfAylyAg8%2B%2FgPHrOhhTWcu9%2Fr3YvHVsLyIrrzDW98jvTxJ9eEXcsw6G3wlFWMR%2B92RYXF8jQFXrCraxjbEACyTecDxFMvINtCeoMGZ6%2FgpbagImhRTR76VVatM57HMC8tOzYH6tfDc6pHgfaP22SsBHmIe5MeMSOkWzTS9V8wxWbeoHJoWqDUAqMWzDLWKQSmfyPDuGpg5%2Fmi5YDKA9g9e5ujfhdK1ipAhOMQdU%2BvNeSco51C%2F6elQb%2FFRnFFS2uynA6QJSNzT6RAqj5rGwFRHWux%2FDI4I%2FB27NHdMGYiqGbfQqKUbpOOGr3oThRqdzxKW%2FkEXVvyYQ%2FRciFas6291K7%2F2YbjLK2sP42uWw41%2Fs6yDbybLw%2BzDUlPW8BjqkAW4GXQj7eEGD%2FdD167XbMtD9cJsXuNB66zhvJi1nzigstbe4DIkAUe6KBFYFKG8IfQYs4myw1rnac9Xr1P%2FIQB2bJ926tpncaY6nIeDQyaQgB6aR1yj1XL5rWFEonggnMWmKLbftnq19gU6QitXnqXRREoaoESKS8W8WIXuQlcieaoVP3i6kCb1HiAmtp6VzVJkgcv2PzV0CVFox9LMXaxz1ME6H&X-Amz-Signature=5d541994208786d74f1e9b63b40aa65bf315e81903a4c4c42575d4c4b5055a5f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRIWSMGX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBQ%2FpPOGICdgkuA8NBSzH4oZaSUSsfW%2BNQvg%2BnO6gk9QIhAONVqhnlTzqCEH49UBFGkNW88zOihMXj0ZL5IZO2hX7JKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwgPQyi2OQTS8bRq%2Bgq3APQLyK9%2B3NsoKn5%2BaWW4h6Rv%2FweXE4mC%2Bs7chRBPGEqgNZkLQ5kqED5QXxVS3xSvZ%2BAMeIiiHaLQ67AcKraYSr4IoDO%2FJAUFN7ObQzCYUFRS5uaEbax5nccHLv7gZu1P%2F67ozE4m1H94DF4fAcr1th7xZY8pENUik76%2BArs7taME%2B1w1NptVaWwvJmYo4YNOmJV9dGCHcYdt7c3ZbQqHhBgSdAnTGaoaigryDjE9sla2yi3lGaKjF7mcr144f32WYo1AhgAZsfAylyAg8%2B%2FgPHrOhhTWcu9%2Fr3YvHVsLyIrrzDW98jvTxJ9eEXcsw6G3wlFWMR%2B92RYXF8jQFXrCraxjbEACyTecDxFMvINtCeoMGZ6%2FgpbagImhRTR76VVatM57HMC8tOzYH6tfDc6pHgfaP22SsBHmIe5MeMSOkWzTS9V8wxWbeoHJoWqDUAqMWzDLWKQSmfyPDuGpg5%2Fmi5YDKA9g9e5ujfhdK1ipAhOMQdU%2BvNeSco51C%2F6elQb%2FFRnFFS2uynA6QJSNzT6RAqj5rGwFRHWux%2FDI4I%2FB27NHdMGYiqGbfQqKUbpOOGr3oThRqdzxKW%2FkEXVvyYQ%2FRciFas6291K7%2F2YbjLK2sP42uWw41%2Fs6yDbybLw%2BzDUlPW8BjqkAW4GXQj7eEGD%2FdD167XbMtD9cJsXuNB66zhvJi1nzigstbe4DIkAUe6KBFYFKG8IfQYs4myw1rnac9Xr1P%2FIQB2bJ926tpncaY6nIeDQyaQgB6aR1yj1XL5rWFEonggnMWmKLbftnq19gU6QitXnqXRREoaoESKS8W8WIXuQlcieaoVP3i6kCb1HiAmtp6VzVJkgcv2PzV0CVFox9LMXaxz1ME6H&X-Amz-Signature=0d09b2f490ed8a66bf4bd5a547d7292b0c79f4e85a30b00cbaa2a946c23c3144&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRIWSMGX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBQ%2FpPOGICdgkuA8NBSzH4oZaSUSsfW%2BNQvg%2BnO6gk9QIhAONVqhnlTzqCEH49UBFGkNW88zOihMXj0ZL5IZO2hX7JKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwgPQyi2OQTS8bRq%2Bgq3APQLyK9%2B3NsoKn5%2BaWW4h6Rv%2FweXE4mC%2Bs7chRBPGEqgNZkLQ5kqED5QXxVS3xSvZ%2BAMeIiiHaLQ67AcKraYSr4IoDO%2FJAUFN7ObQzCYUFRS5uaEbax5nccHLv7gZu1P%2F67ozE4m1H94DF4fAcr1th7xZY8pENUik76%2BArs7taME%2B1w1NptVaWwvJmYo4YNOmJV9dGCHcYdt7c3ZbQqHhBgSdAnTGaoaigryDjE9sla2yi3lGaKjF7mcr144f32WYo1AhgAZsfAylyAg8%2B%2FgPHrOhhTWcu9%2Fr3YvHVsLyIrrzDW98jvTxJ9eEXcsw6G3wlFWMR%2B92RYXF8jQFXrCraxjbEACyTecDxFMvINtCeoMGZ6%2FgpbagImhRTR76VVatM57HMC8tOzYH6tfDc6pHgfaP22SsBHmIe5MeMSOkWzTS9V8wxWbeoHJoWqDUAqMWzDLWKQSmfyPDuGpg5%2Fmi5YDKA9g9e5ujfhdK1ipAhOMQdU%2BvNeSco51C%2F6elQb%2FFRnFFS2uynA6QJSNzT6RAqj5rGwFRHWux%2FDI4I%2FB27NHdMGYiqGbfQqKUbpOOGr3oThRqdzxKW%2FkEXVvyYQ%2FRciFas6291K7%2F2YbjLK2sP42uWw41%2Fs6yDbybLw%2BzDUlPW8BjqkAW4GXQj7eEGD%2FdD167XbMtD9cJsXuNB66zhvJi1nzigstbe4DIkAUe6KBFYFKG8IfQYs4myw1rnac9Xr1P%2FIQB2bJ926tpncaY6nIeDQyaQgB6aR1yj1XL5rWFEonggnMWmKLbftnq19gU6QitXnqXRREoaoESKS8W8WIXuQlcieaoVP3i6kCb1HiAmtp6VzVJkgcv2PzV0CVFox9LMXaxz1ME6H&X-Amz-Signature=e811df70edad3e255e07aa62e810e44761ec1668d7728736887ee25101e56d64&X-Amz-SignedHeaders=host&x-id=GetObject)
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


