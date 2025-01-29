

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7MUVK3G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFE5Vjxymntfim3QCtGWB6uMDxyL41ev4%2FuMSp86HzdaAiApO0w9ophSPF7YhHclLaRDxIK57%2Fx37AK9WUsKoAH7QiqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM8tyQ4O%2Bea2XSi6sKtwDFZGjoUDgbCqaaWdGDWAirQh%2BT%2FT8VoPSfcG0kb0wfKbUgjx5QpSOHrbPh45cR%2FYtalRqMrIjj64xyhbnfQSO6Pp0aXWtoQyk9V1pGPrYfzAbF4ySUllxypY0SzK%2Fs1RRxaCbpgPAkmqZx%2BZBrkXZdXchwkn0z1uQZXqxsonb8PV6GW0fz529lQ7QfF7rJguXW9yZq7K4tNaNfX2vYEtO%2BmjcMev7tPBQxEwkjvwNJlui6i80DaaLDbPDXF97bdQDmd1u%2BiZMCM8RcnJgJtEsa3cY733QrlQO0H8%2F3ElIMnhMaVBxBg6CTeS%2FMBPATrGBIkQloAy0XtOBryVh92AfXic4tHyPv9m6NNh6bowzYgO6WgrTzRCVrQze%2B6zpFpY%2BjfG2foh06dpxy5zPpqUbJ4o%2F90iKXkjYdd%2FpX9Fsp9TJ%2F7P1%2FsEuXHb%2Bew8dnmWnMnXp%2F4VsGGK%2B7So7EwWi7QgcrjeywmybZT8dF7SPMRit97DFUv146TCu8%2FudDMk592vdaYqRIgtu%2FjXSzVAy1lCGqw3gxlqcpEmuAzWBra9S8TjOCtM3ONwlun3Y3D%2B9wQuX4bn6oZqZPqFdQLZ%2FsHODkXo7dJrsMWxLERhaFngFGeNhzn%2Fnda3gR5Yw0qznvAY6pgFQqrFL22NRHVTqLhGpMM0Yvnh%2BJDW69mXU0QJYAgZL%2FWWBqDTAL8fua6WNjE0gzpdycGP2Kw5ehqZSxPQ2I%2BWio6OSWPadSjBigZiZDW4Om%2FfpZ32zHjCyrOrXX4pXoyo8QxOX%2FnRJcfnmWVNgOwYbDY1adadjXGEmAG74XlATNm60ORJprPqr8Uvyl0ol7JKylc4dWGQh9cxlnBW00IBp1CVdJsls&X-Amz-Signature=50de8290324bee5ae44b4eaf5f4ac8d06caa40c161b8a631186e789ae025032e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4T6ZYE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDk0iBLeVQ1hO7WpwXgKkgPX8CJGQ%2FRer3wn8nlQLYmbAiAk1fW5PBLZEp5KR5FEZ05UQ0KqoccYUDahEYIMKFQg%2FCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcmgMPBr%2FatfcJ%2BpaKtwDZjZP7snFgxh4OpeDF9UnLXImSGNqpTIZsaR4rXF9hm5AqSqM6mAe2MSXkbKr55uxEOC8PqOLN5HKVboedsU1iC6U%2BwTJjRP29UX5dQzfciQ6Lpw4Ndd1qYQjqleQlJhBtYgXPWOTz7NOlJpAB0XufcBBOtd%2B%2FnxZZ%2Fc%2B8cOy2TSjCla7RijwDnOvScpbVFniiYcCf%2FpYXV7fa4OuITIbWAHGflQ%2B5CwaiIs3%2BoheW1EQBUTw3dkb6XMlzoWTua1tl1uc5L68q2BMr9TGoSa8TLtTfsxW4Beedv%2BQjV%2BTK3v%2FxJzYWdZfD9BNkMyejTPDnjN%2FtU17kO2zZ9vu0EgCaRHfnkulQZDoXron2lJtAeb3IRQehTp4CmpgICzcMpLeJR8s1eacyB7CSMrqK5HtfjePrG85Qb2D0wyxIbLIjufOsjvO%2BCxfdmC%2BZSIabt8blXMEU1klh8C1O1STKCnOVYqWkshO3AL2aaBwFr2cVn5%2Bg%2FQJfjXh%2BWlQ0E9ZB7cRbfUNPALmRzzLaVcWSOMXK8zld7xoPB12Lw4C2%2BZt48aY4T6mtjfUWynGjFBOS3AKZS3q49EC6nfrYdVNbeA%2FqKN5F1uWcAhbf4RFwqppFONudKsn9gTHryHzH1swl8fnvAY6pgHLJo0HU58yEg0Qe1UjlyM64Rmzy2mT7TuuIxYUV95WlYvdU2fa0QF0dtK4dcMUSpTw3bm1VFNuPS7DNVcHeA4D0Wsvwof4ZljPPWauiSBBETxqrc%2Bf9H03Fx%2B%2FeDWOdOJbcM%2B4lBqsiTce%2BfhAp9aN096Oik3x37xNmmomcBRd5oqFEf27o65tR2wBhu%2Be1k1V41ECoSrh45pWl3UT8BrmIdmdBWeZ&X-Amz-Signature=8670c46a234a7713b8982443a9366d94e15415a6c76da655b3c502e734b6b084&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4T6ZYE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDk0iBLeVQ1hO7WpwXgKkgPX8CJGQ%2FRer3wn8nlQLYmbAiAk1fW5PBLZEp5KR5FEZ05UQ0KqoccYUDahEYIMKFQg%2FCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcmgMPBr%2FatfcJ%2BpaKtwDZjZP7snFgxh4OpeDF9UnLXImSGNqpTIZsaR4rXF9hm5AqSqM6mAe2MSXkbKr55uxEOC8PqOLN5HKVboedsU1iC6U%2BwTJjRP29UX5dQzfciQ6Lpw4Ndd1qYQjqleQlJhBtYgXPWOTz7NOlJpAB0XufcBBOtd%2B%2FnxZZ%2Fc%2B8cOy2TSjCla7RijwDnOvScpbVFniiYcCf%2FpYXV7fa4OuITIbWAHGflQ%2B5CwaiIs3%2BoheW1EQBUTw3dkb6XMlzoWTua1tl1uc5L68q2BMr9TGoSa8TLtTfsxW4Beedv%2BQjV%2BTK3v%2FxJzYWdZfD9BNkMyejTPDnjN%2FtU17kO2zZ9vu0EgCaRHfnkulQZDoXron2lJtAeb3IRQehTp4CmpgICzcMpLeJR8s1eacyB7CSMrqK5HtfjePrG85Qb2D0wyxIbLIjufOsjvO%2BCxfdmC%2BZSIabt8blXMEU1klh8C1O1STKCnOVYqWkshO3AL2aaBwFr2cVn5%2Bg%2FQJfjXh%2BWlQ0E9ZB7cRbfUNPALmRzzLaVcWSOMXK8zld7xoPB12Lw4C2%2BZt48aY4T6mtjfUWynGjFBOS3AKZS3q49EC6nfrYdVNbeA%2FqKN5F1uWcAhbf4RFwqppFONudKsn9gTHryHzH1swl8fnvAY6pgHLJo0HU58yEg0Qe1UjlyM64Rmzy2mT7TuuIxYUV95WlYvdU2fa0QF0dtK4dcMUSpTw3bm1VFNuPS7DNVcHeA4D0Wsvwof4ZljPPWauiSBBETxqrc%2Bf9H03Fx%2B%2FeDWOdOJbcM%2B4lBqsiTce%2BfhAp9aN096Oik3x37xNmmomcBRd5oqFEf27o65tR2wBhu%2Be1k1V41ECoSrh45pWl3UT8BrmIdmdBWeZ&X-Amz-Signature=a34fba4bc99920733343dac34a0630cd00eb244bced358c7871eec6cdae8c24e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4T6ZYE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDk0iBLeVQ1hO7WpwXgKkgPX8CJGQ%2FRer3wn8nlQLYmbAiAk1fW5PBLZEp5KR5FEZ05UQ0KqoccYUDahEYIMKFQg%2FCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcmgMPBr%2FatfcJ%2BpaKtwDZjZP7snFgxh4OpeDF9UnLXImSGNqpTIZsaR4rXF9hm5AqSqM6mAe2MSXkbKr55uxEOC8PqOLN5HKVboedsU1iC6U%2BwTJjRP29UX5dQzfciQ6Lpw4Ndd1qYQjqleQlJhBtYgXPWOTz7NOlJpAB0XufcBBOtd%2B%2FnxZZ%2Fc%2B8cOy2TSjCla7RijwDnOvScpbVFniiYcCf%2FpYXV7fa4OuITIbWAHGflQ%2B5CwaiIs3%2BoheW1EQBUTw3dkb6XMlzoWTua1tl1uc5L68q2BMr9TGoSa8TLtTfsxW4Beedv%2BQjV%2BTK3v%2FxJzYWdZfD9BNkMyejTPDnjN%2FtU17kO2zZ9vu0EgCaRHfnkulQZDoXron2lJtAeb3IRQehTp4CmpgICzcMpLeJR8s1eacyB7CSMrqK5HtfjePrG85Qb2D0wyxIbLIjufOsjvO%2BCxfdmC%2BZSIabt8blXMEU1klh8C1O1STKCnOVYqWkshO3AL2aaBwFr2cVn5%2Bg%2FQJfjXh%2BWlQ0E9ZB7cRbfUNPALmRzzLaVcWSOMXK8zld7xoPB12Lw4C2%2BZt48aY4T6mtjfUWynGjFBOS3AKZS3q49EC6nfrYdVNbeA%2FqKN5F1uWcAhbf4RFwqppFONudKsn9gTHryHzH1swl8fnvAY6pgHLJo0HU58yEg0Qe1UjlyM64Rmzy2mT7TuuIxYUV95WlYvdU2fa0QF0dtK4dcMUSpTw3bm1VFNuPS7DNVcHeA4D0Wsvwof4ZljPPWauiSBBETxqrc%2Bf9H03Fx%2B%2FeDWOdOJbcM%2B4lBqsiTce%2BfhAp9aN096Oik3x37xNmmomcBRd5oqFEf27o65tR2wBhu%2Be1k1V41ECoSrh45pWl3UT8BrmIdmdBWeZ&X-Amz-Signature=2672f04b7b842cedd2fbc5db7ca3eabc4410d92a9814f19cb7effecca38135b3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4T6ZYE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDk0iBLeVQ1hO7WpwXgKkgPX8CJGQ%2FRer3wn8nlQLYmbAiAk1fW5PBLZEp5KR5FEZ05UQ0KqoccYUDahEYIMKFQg%2FCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcmgMPBr%2FatfcJ%2BpaKtwDZjZP7snFgxh4OpeDF9UnLXImSGNqpTIZsaR4rXF9hm5AqSqM6mAe2MSXkbKr55uxEOC8PqOLN5HKVboedsU1iC6U%2BwTJjRP29UX5dQzfciQ6Lpw4Ndd1qYQjqleQlJhBtYgXPWOTz7NOlJpAB0XufcBBOtd%2B%2FnxZZ%2Fc%2B8cOy2TSjCla7RijwDnOvScpbVFniiYcCf%2FpYXV7fa4OuITIbWAHGflQ%2B5CwaiIs3%2BoheW1EQBUTw3dkb6XMlzoWTua1tl1uc5L68q2BMr9TGoSa8TLtTfsxW4Beedv%2BQjV%2BTK3v%2FxJzYWdZfD9BNkMyejTPDnjN%2FtU17kO2zZ9vu0EgCaRHfnkulQZDoXron2lJtAeb3IRQehTp4CmpgICzcMpLeJR8s1eacyB7CSMrqK5HtfjePrG85Qb2D0wyxIbLIjufOsjvO%2BCxfdmC%2BZSIabt8blXMEU1klh8C1O1STKCnOVYqWkshO3AL2aaBwFr2cVn5%2Bg%2FQJfjXh%2BWlQ0E9ZB7cRbfUNPALmRzzLaVcWSOMXK8zld7xoPB12Lw4C2%2BZt48aY4T6mtjfUWynGjFBOS3AKZS3q49EC6nfrYdVNbeA%2FqKN5F1uWcAhbf4RFwqppFONudKsn9gTHryHzH1swl8fnvAY6pgHLJo0HU58yEg0Qe1UjlyM64Rmzy2mT7TuuIxYUV95WlYvdU2fa0QF0dtK4dcMUSpTw3bm1VFNuPS7DNVcHeA4D0Wsvwof4ZljPPWauiSBBETxqrc%2Bf9H03Fx%2B%2FeDWOdOJbcM%2B4lBqsiTce%2BfhAp9aN096Oik3x37xNmmomcBRd5oqFEf27o65tR2wBhu%2Be1k1V41ECoSrh45pWl3UT8BrmIdmdBWeZ&X-Amz-Signature=adfa518730635ccef529e3a849dbd74f7010727bdd6fbae87f01d0b117878b27&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4T6ZYE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDk0iBLeVQ1hO7WpwXgKkgPX8CJGQ%2FRer3wn8nlQLYmbAiAk1fW5PBLZEp5KR5FEZ05UQ0KqoccYUDahEYIMKFQg%2FCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcmgMPBr%2FatfcJ%2BpaKtwDZjZP7snFgxh4OpeDF9UnLXImSGNqpTIZsaR4rXF9hm5AqSqM6mAe2MSXkbKr55uxEOC8PqOLN5HKVboedsU1iC6U%2BwTJjRP29UX5dQzfciQ6Lpw4Ndd1qYQjqleQlJhBtYgXPWOTz7NOlJpAB0XufcBBOtd%2B%2FnxZZ%2Fc%2B8cOy2TSjCla7RijwDnOvScpbVFniiYcCf%2FpYXV7fa4OuITIbWAHGflQ%2B5CwaiIs3%2BoheW1EQBUTw3dkb6XMlzoWTua1tl1uc5L68q2BMr9TGoSa8TLtTfsxW4Beedv%2BQjV%2BTK3v%2FxJzYWdZfD9BNkMyejTPDnjN%2FtU17kO2zZ9vu0EgCaRHfnkulQZDoXron2lJtAeb3IRQehTp4CmpgICzcMpLeJR8s1eacyB7CSMrqK5HtfjePrG85Qb2D0wyxIbLIjufOsjvO%2BCxfdmC%2BZSIabt8blXMEU1klh8C1O1STKCnOVYqWkshO3AL2aaBwFr2cVn5%2Bg%2FQJfjXh%2BWlQ0E9ZB7cRbfUNPALmRzzLaVcWSOMXK8zld7xoPB12Lw4C2%2BZt48aY4T6mtjfUWynGjFBOS3AKZS3q49EC6nfrYdVNbeA%2FqKN5F1uWcAhbf4RFwqppFONudKsn9gTHryHzH1swl8fnvAY6pgHLJo0HU58yEg0Qe1UjlyM64Rmzy2mT7TuuIxYUV95WlYvdU2fa0QF0dtK4dcMUSpTw3bm1VFNuPS7DNVcHeA4D0Wsvwof4ZljPPWauiSBBETxqrc%2Bf9H03Fx%2B%2FeDWOdOJbcM%2B4lBqsiTce%2BfhAp9aN096Oik3x37xNmmomcBRd5oqFEf27o65tR2wBhu%2Be1k1V41ECoSrh45pWl3UT8BrmIdmdBWeZ&X-Amz-Signature=1783172cfa03058bbc6fde8c72a1853f7789fef23b3314df4a4a500239aeec3e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7MUVK3G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFE5Vjxymntfim3QCtGWB6uMDxyL41ev4%2FuMSp86HzdaAiApO0w9ophSPF7YhHclLaRDxIK57%2Fx37AK9WUsKoAH7QiqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM8tyQ4O%2Bea2XSi6sKtwDFZGjoUDgbCqaaWdGDWAirQh%2BT%2FT8VoPSfcG0kb0wfKbUgjx5QpSOHrbPh45cR%2FYtalRqMrIjj64xyhbnfQSO6Pp0aXWtoQyk9V1pGPrYfzAbF4ySUllxypY0SzK%2Fs1RRxaCbpgPAkmqZx%2BZBrkXZdXchwkn0z1uQZXqxsonb8PV6GW0fz529lQ7QfF7rJguXW9yZq7K4tNaNfX2vYEtO%2BmjcMev7tPBQxEwkjvwNJlui6i80DaaLDbPDXF97bdQDmd1u%2BiZMCM8RcnJgJtEsa3cY733QrlQO0H8%2F3ElIMnhMaVBxBg6CTeS%2FMBPATrGBIkQloAy0XtOBryVh92AfXic4tHyPv9m6NNh6bowzYgO6WgrTzRCVrQze%2B6zpFpY%2BjfG2foh06dpxy5zPpqUbJ4o%2F90iKXkjYdd%2FpX9Fsp9TJ%2F7P1%2FsEuXHb%2Bew8dnmWnMnXp%2F4VsGGK%2B7So7EwWi7QgcrjeywmybZT8dF7SPMRit97DFUv146TCu8%2FudDMk592vdaYqRIgtu%2FjXSzVAy1lCGqw3gxlqcpEmuAzWBra9S8TjOCtM3ONwlun3Y3D%2B9wQuX4bn6oZqZPqFdQLZ%2FsHODkXo7dJrsMWxLERhaFngFGeNhzn%2Fnda3gR5Yw0qznvAY6pgFQqrFL22NRHVTqLhGpMM0Yvnh%2BJDW69mXU0QJYAgZL%2FWWBqDTAL8fua6WNjE0gzpdycGP2Kw5ehqZSxPQ2I%2BWio6OSWPadSjBigZiZDW4Om%2FfpZ32zHjCyrOrXX4pXoyo8QxOX%2FnRJcfnmWVNgOwYbDY1adadjXGEmAG74XlATNm60ORJprPqr8Uvyl0ol7JKylc4dWGQh9cxlnBW00IBp1CVdJsls&X-Amz-Signature=1a0fd38b7bb50b970a3db74ce05b5d0c469c048812b6376de2c75c12ed9d1274&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7MUVK3G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFE5Vjxymntfim3QCtGWB6uMDxyL41ev4%2FuMSp86HzdaAiApO0w9ophSPF7YhHclLaRDxIK57%2Fx37AK9WUsKoAH7QiqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM8tyQ4O%2Bea2XSi6sKtwDFZGjoUDgbCqaaWdGDWAirQh%2BT%2FT8VoPSfcG0kb0wfKbUgjx5QpSOHrbPh45cR%2FYtalRqMrIjj64xyhbnfQSO6Pp0aXWtoQyk9V1pGPrYfzAbF4ySUllxypY0SzK%2Fs1RRxaCbpgPAkmqZx%2BZBrkXZdXchwkn0z1uQZXqxsonb8PV6GW0fz529lQ7QfF7rJguXW9yZq7K4tNaNfX2vYEtO%2BmjcMev7tPBQxEwkjvwNJlui6i80DaaLDbPDXF97bdQDmd1u%2BiZMCM8RcnJgJtEsa3cY733QrlQO0H8%2F3ElIMnhMaVBxBg6CTeS%2FMBPATrGBIkQloAy0XtOBryVh92AfXic4tHyPv9m6NNh6bowzYgO6WgrTzRCVrQze%2B6zpFpY%2BjfG2foh06dpxy5zPpqUbJ4o%2F90iKXkjYdd%2FpX9Fsp9TJ%2F7P1%2FsEuXHb%2Bew8dnmWnMnXp%2F4VsGGK%2B7So7EwWi7QgcrjeywmybZT8dF7SPMRit97DFUv146TCu8%2FudDMk592vdaYqRIgtu%2FjXSzVAy1lCGqw3gxlqcpEmuAzWBra9S8TjOCtM3ONwlun3Y3D%2B9wQuX4bn6oZqZPqFdQLZ%2FsHODkXo7dJrsMWxLERhaFngFGeNhzn%2Fnda3gR5Yw0qznvAY6pgFQqrFL22NRHVTqLhGpMM0Yvnh%2BJDW69mXU0QJYAgZL%2FWWBqDTAL8fua6WNjE0gzpdycGP2Kw5ehqZSxPQ2I%2BWio6OSWPadSjBigZiZDW4Om%2FfpZ32zHjCyrOrXX4pXoyo8QxOX%2FnRJcfnmWVNgOwYbDY1adadjXGEmAG74XlATNm60ORJprPqr8Uvyl0ol7JKylc4dWGQh9cxlnBW00IBp1CVdJsls&X-Amz-Signature=956bae7d3bca5bee7f1369c2cfab6fb534e548cdcc3c67c5dd2240963fb3d7c4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7MUVK3G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFE5Vjxymntfim3QCtGWB6uMDxyL41ev4%2FuMSp86HzdaAiApO0w9ophSPF7YhHclLaRDxIK57%2Fx37AK9WUsKoAH7QiqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM8tyQ4O%2Bea2XSi6sKtwDFZGjoUDgbCqaaWdGDWAirQh%2BT%2FT8VoPSfcG0kb0wfKbUgjx5QpSOHrbPh45cR%2FYtalRqMrIjj64xyhbnfQSO6Pp0aXWtoQyk9V1pGPrYfzAbF4ySUllxypY0SzK%2Fs1RRxaCbpgPAkmqZx%2BZBrkXZdXchwkn0z1uQZXqxsonb8PV6GW0fz529lQ7QfF7rJguXW9yZq7K4tNaNfX2vYEtO%2BmjcMev7tPBQxEwkjvwNJlui6i80DaaLDbPDXF97bdQDmd1u%2BiZMCM8RcnJgJtEsa3cY733QrlQO0H8%2F3ElIMnhMaVBxBg6CTeS%2FMBPATrGBIkQloAy0XtOBryVh92AfXic4tHyPv9m6NNh6bowzYgO6WgrTzRCVrQze%2B6zpFpY%2BjfG2foh06dpxy5zPpqUbJ4o%2F90iKXkjYdd%2FpX9Fsp9TJ%2F7P1%2FsEuXHb%2Bew8dnmWnMnXp%2F4VsGGK%2B7So7EwWi7QgcrjeywmybZT8dF7SPMRit97DFUv146TCu8%2FudDMk592vdaYqRIgtu%2FjXSzVAy1lCGqw3gxlqcpEmuAzWBra9S8TjOCtM3ONwlun3Y3D%2B9wQuX4bn6oZqZPqFdQLZ%2FsHODkXo7dJrsMWxLERhaFngFGeNhzn%2Fnda3gR5Yw0qznvAY6pgFQqrFL22NRHVTqLhGpMM0Yvnh%2BJDW69mXU0QJYAgZL%2FWWBqDTAL8fua6WNjE0gzpdycGP2Kw5ehqZSxPQ2I%2BWio6OSWPadSjBigZiZDW4Om%2FfpZ32zHjCyrOrXX4pXoyo8QxOX%2FnRJcfnmWVNgOwYbDY1adadjXGEmAG74XlATNm60ORJprPqr8Uvyl0ol7JKylc4dWGQh9cxlnBW00IBp1CVdJsls&X-Amz-Signature=5f76de4b466830aadb3001eb5a3ad59985b3c186175fa56ed906d2ab9f381e16&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7MUVK3G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFE5Vjxymntfim3QCtGWB6uMDxyL41ev4%2FuMSp86HzdaAiApO0w9ophSPF7YhHclLaRDxIK57%2Fx37AK9WUsKoAH7QiqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM8tyQ4O%2Bea2XSi6sKtwDFZGjoUDgbCqaaWdGDWAirQh%2BT%2FT8VoPSfcG0kb0wfKbUgjx5QpSOHrbPh45cR%2FYtalRqMrIjj64xyhbnfQSO6Pp0aXWtoQyk9V1pGPrYfzAbF4ySUllxypY0SzK%2Fs1RRxaCbpgPAkmqZx%2BZBrkXZdXchwkn0z1uQZXqxsonb8PV6GW0fz529lQ7QfF7rJguXW9yZq7K4tNaNfX2vYEtO%2BmjcMev7tPBQxEwkjvwNJlui6i80DaaLDbPDXF97bdQDmd1u%2BiZMCM8RcnJgJtEsa3cY733QrlQO0H8%2F3ElIMnhMaVBxBg6CTeS%2FMBPATrGBIkQloAy0XtOBryVh92AfXic4tHyPv9m6NNh6bowzYgO6WgrTzRCVrQze%2B6zpFpY%2BjfG2foh06dpxy5zPpqUbJ4o%2F90iKXkjYdd%2FpX9Fsp9TJ%2F7P1%2FsEuXHb%2Bew8dnmWnMnXp%2F4VsGGK%2B7So7EwWi7QgcrjeywmybZT8dF7SPMRit97DFUv146TCu8%2FudDMk592vdaYqRIgtu%2FjXSzVAy1lCGqw3gxlqcpEmuAzWBra9S8TjOCtM3ONwlun3Y3D%2B9wQuX4bn6oZqZPqFdQLZ%2FsHODkXo7dJrsMWxLERhaFngFGeNhzn%2Fnda3gR5Yw0qznvAY6pgFQqrFL22NRHVTqLhGpMM0Yvnh%2BJDW69mXU0QJYAgZL%2FWWBqDTAL8fua6WNjE0gzpdycGP2Kw5ehqZSxPQ2I%2BWio6OSWPadSjBigZiZDW4Om%2FfpZ32zHjCyrOrXX4pXoyo8QxOX%2FnRJcfnmWVNgOwYbDY1adadjXGEmAG74XlATNm60ORJprPqr8Uvyl0ol7JKylc4dWGQh9cxlnBW00IBp1CVdJsls&X-Amz-Signature=d0c198e647c54a2a356511040c72383181a1db2cd4f4121e0e8bab9df1a30126&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7MUVK3G%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFE5Vjxymntfim3QCtGWB6uMDxyL41ev4%2FuMSp86HzdaAiApO0w9ophSPF7YhHclLaRDxIK57%2Fx37AK9WUsKoAH7QiqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM8tyQ4O%2Bea2XSi6sKtwDFZGjoUDgbCqaaWdGDWAirQh%2BT%2FT8VoPSfcG0kb0wfKbUgjx5QpSOHrbPh45cR%2FYtalRqMrIjj64xyhbnfQSO6Pp0aXWtoQyk9V1pGPrYfzAbF4ySUllxypY0SzK%2Fs1RRxaCbpgPAkmqZx%2BZBrkXZdXchwkn0z1uQZXqxsonb8PV6GW0fz529lQ7QfF7rJguXW9yZq7K4tNaNfX2vYEtO%2BmjcMev7tPBQxEwkjvwNJlui6i80DaaLDbPDXF97bdQDmd1u%2BiZMCM8RcnJgJtEsa3cY733QrlQO0H8%2F3ElIMnhMaVBxBg6CTeS%2FMBPATrGBIkQloAy0XtOBryVh92AfXic4tHyPv9m6NNh6bowzYgO6WgrTzRCVrQze%2B6zpFpY%2BjfG2foh06dpxy5zPpqUbJ4o%2F90iKXkjYdd%2FpX9Fsp9TJ%2F7P1%2FsEuXHb%2Bew8dnmWnMnXp%2F4VsGGK%2B7So7EwWi7QgcrjeywmybZT8dF7SPMRit97DFUv146TCu8%2FudDMk592vdaYqRIgtu%2FjXSzVAy1lCGqw3gxlqcpEmuAzWBra9S8TjOCtM3ONwlun3Y3D%2B9wQuX4bn6oZqZPqFdQLZ%2FsHODkXo7dJrsMWxLERhaFngFGeNhzn%2Fnda3gR5Yw0qznvAY6pgFQqrFL22NRHVTqLhGpMM0Yvnh%2BJDW69mXU0QJYAgZL%2FWWBqDTAL8fua6WNjE0gzpdycGP2Kw5ehqZSxPQ2I%2BWio6OSWPadSjBigZiZDW4Om%2FfpZ32zHjCyrOrXX4pXoyo8QxOX%2FnRJcfnmWVNgOwYbDY1adadjXGEmAG74XlATNm60ORJprPqr8Uvyl0ol7JKylc4dWGQh9cxlnBW00IBp1CVdJsls&X-Amz-Signature=9850e95e2ae394a55c1cecab7690bb2a6bdb05d6baef15f22eb5024a9597a25f&X-Amz-SignedHeaders=host&x-id=GetObject)
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


