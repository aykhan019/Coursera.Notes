

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674BKVQ24%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6patdpqyGjBw45AP7adwaz2aX5spJ71agHzObkW64%2FgIgRMTTEbMlNbGutBkdzXv2mjurjPj%2FQXkQswnA5NKiSNsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPbHM8uq%2F69SYMQ1tircA2XUbTJMj8r08KdunQreu0P2Oj8gBq8%2FSebFMWkvx1F6VDBhMwkLmw%2BGbI8Q6sMXYgspl1eRpaaleFm3WFfoHu5xeZPCFXzH540dH4ntrI1rGg8prXdGVBhVVhqmsWw5sTdlK0W%2Bc2m4iXm8iQdUPO2X7qZoS2PArdH0HZfMqFmdpvAtfgbuNy8JknM3P8%2F3DMgIDV8abSEVet8aRH81BlJCHCunoT6%2BI9a%2BpW9Az4SD%2BIqwbo9r4zGIEiRHddXugjCcGqessB8PJehzTj%2B%2F5MQUgSHZ32qEDXq1S7N0WEkwnjJFzuUK9W619M7nhoKGAwGaxmQeY1BGlPJUXq43owmoZmkFuxf8P532b%2FWbyMFolN0tLK8zVvKa%2B%2BJdtxd9eQU61Sm6Yr6%2BRavbPz9ybx3vAXzXG7FfMKr4C6Y1MBrxA%2Fn40xDdSFzTXZPGlXmqdlwz%2FAGg5%2FTecd5QW4hsWnj86kXoFuPK6Ze%2FLvREf22f8IO9Ai0Tdkm4VOuDN8kYrWD5BGevpJ%2Ff7brkG%2B7u7HAN%2BcSFgaowxIgA%2Fn3XuDIXPkutiNlIt5VV7thKxjSd5zOGxaRzJsgvUC%2B%2Ff1CQy3jQ8YuxmZ4cJoz8rgcMALWjbAZRFNEIovFCrNDwMLXe7bwGOqUBwGuIhcqyNmGvLCxi%2Fr9s046oq1wbe8n6THVjAdpNIW7qNJvd5Bb4kqXaUy%2FTRnVX3wtxZu2w7T%2FiQnUuNLXCxB88YC4Pwu2LLUdBuvloaTfIeMm3lUEJJymRapapGvijcwM5iTFjV2afWZqHoCz%2FowXwo%2B6lJ9uoHwMVHy7sGOxmVTaw%2FescVhs7j2ZrQgkJBfzj%2B84PHPHxqW7AIZMPE%2FbUflOa&X-Amz-Signature=4f7326ec23343754f80559a7a8d5a7f93818cf8f587af0752b96376b476b9eae&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B4IAJQI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDou4ELozs7JRnIFINXwuxihrk3t5Rf0RbeUtqcGBW%2FxgIhAJIVJhjJhv%2BixA3m9HF37XoXait1TMi6NkX2KbxSi8JAKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyG%2B6VTfZsJPFuV6oq3AOpSGseUHU%2BnRgCDKFv3GuXblY76RofSeGLJJ7Kmu%2FK8VZD4GjzAWBVgF2Mg0mh5AFQcT4PWvRQU633dDQKoNJXcqQEJLp9%2B11ELj4ytZDtIlek7L4RoO4%2FeqzjL2PN%2F66nO%2FhCPryFyamAd6Av7tZllUENhA6uVn6R2FO19SFcY3sAABLwNFJPxxWkXOKIoFnNYAcc01XB5e8Qu9nHCx%2FiEs%2BTd6kJ6IHs0kD%2BbV9ctlf5yL%2Fhp5z6K6uHPUm66jCjmcktD8IMDdrlNYSP%2F5%2FRGCF7WbZsrgkhwqKIxQJfUOKR69BBvvTshpMJVC2x0ULwyni68OH%2BGo56FVjxiORiQNA7apRT9R9SXCwGVFJR4QDomPKaNcqu8K87bPGY%2F0R9qQOJ%2FoX4mY9g37%2F5KtI0Gd9WFj3IDy6TIigbdDYJdCSdcBV%2Blmn2bqTQmXDGaARscg5PSRvmw%2Fhz7R9OMwxKZUhZpgqdgLAdVo6B6eQA0TlEAVOsPBPpvPnmFpXiFAynFI1%2BjOkm26UHODGrffjuPB5EfbzVliXtR0NU4Slp9%2BOYXb568nuWbX75pEmuLJ5e%2FfhfFbQT9wWLBAafpEIUxN0GUwkLBU5DXFRnWQMtOl1%2FpcSy%2BbPuQU0dZTDf3u28BjqkAecKsolJs72BQj2vWc34uH%2B6AL%2FPKqZJ4tBSIZ2nB7VyKjwQ24C3lV5MF8jNqXppbjjxOcDlC0DoKftsoSfFwvJkAttl0%2FQfaa3ORltbnbwE6p8mXtMOBaCwa3aYGOq3ebmbboDljTyfRy6zuHlMt1WWaw5%2BGq4RIjZzl9OMeD8j9JXoLnbTjvAYv1F6M0l%2B6q9LWLY0hh44rJsNNF6Y4HZB4g7X&X-Amz-Signature=3d17131c8d99c4711262b4622f668a500df922e6af6283f6afca154b2ed2f9e6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B4IAJQI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDou4ELozs7JRnIFINXwuxihrk3t5Rf0RbeUtqcGBW%2FxgIhAJIVJhjJhv%2BixA3m9HF37XoXait1TMi6NkX2KbxSi8JAKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyG%2B6VTfZsJPFuV6oq3AOpSGseUHU%2BnRgCDKFv3GuXblY76RofSeGLJJ7Kmu%2FK8VZD4GjzAWBVgF2Mg0mh5AFQcT4PWvRQU633dDQKoNJXcqQEJLp9%2B11ELj4ytZDtIlek7L4RoO4%2FeqzjL2PN%2F66nO%2FhCPryFyamAd6Av7tZllUENhA6uVn6R2FO19SFcY3sAABLwNFJPxxWkXOKIoFnNYAcc01XB5e8Qu9nHCx%2FiEs%2BTd6kJ6IHs0kD%2BbV9ctlf5yL%2Fhp5z6K6uHPUm66jCjmcktD8IMDdrlNYSP%2F5%2FRGCF7WbZsrgkhwqKIxQJfUOKR69BBvvTshpMJVC2x0ULwyni68OH%2BGo56FVjxiORiQNA7apRT9R9SXCwGVFJR4QDomPKaNcqu8K87bPGY%2F0R9qQOJ%2FoX4mY9g37%2F5KtI0Gd9WFj3IDy6TIigbdDYJdCSdcBV%2Blmn2bqTQmXDGaARscg5PSRvmw%2Fhz7R9OMwxKZUhZpgqdgLAdVo6B6eQA0TlEAVOsPBPpvPnmFpXiFAynFI1%2BjOkm26UHODGrffjuPB5EfbzVliXtR0NU4Slp9%2BOYXb568nuWbX75pEmuLJ5e%2FfhfFbQT9wWLBAafpEIUxN0GUwkLBU5DXFRnWQMtOl1%2FpcSy%2BbPuQU0dZTDf3u28BjqkAecKsolJs72BQj2vWc34uH%2B6AL%2FPKqZJ4tBSIZ2nB7VyKjwQ24C3lV5MF8jNqXppbjjxOcDlC0DoKftsoSfFwvJkAttl0%2FQfaa3ORltbnbwE6p8mXtMOBaCwa3aYGOq3ebmbboDljTyfRy6zuHlMt1WWaw5%2BGq4RIjZzl9OMeD8j9JXoLnbTjvAYv1F6M0l%2B6q9LWLY0hh44rJsNNF6Y4HZB4g7X&X-Amz-Signature=3eb7b950428f8afaa37c26b46884990d51c288b1a738ae9266ce2eb3a59d1abb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B4IAJQI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDou4ELozs7JRnIFINXwuxihrk3t5Rf0RbeUtqcGBW%2FxgIhAJIVJhjJhv%2BixA3m9HF37XoXait1TMi6NkX2KbxSi8JAKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyG%2B6VTfZsJPFuV6oq3AOpSGseUHU%2BnRgCDKFv3GuXblY76RofSeGLJJ7Kmu%2FK8VZD4GjzAWBVgF2Mg0mh5AFQcT4PWvRQU633dDQKoNJXcqQEJLp9%2B11ELj4ytZDtIlek7L4RoO4%2FeqzjL2PN%2F66nO%2FhCPryFyamAd6Av7tZllUENhA6uVn6R2FO19SFcY3sAABLwNFJPxxWkXOKIoFnNYAcc01XB5e8Qu9nHCx%2FiEs%2BTd6kJ6IHs0kD%2BbV9ctlf5yL%2Fhp5z6K6uHPUm66jCjmcktD8IMDdrlNYSP%2F5%2FRGCF7WbZsrgkhwqKIxQJfUOKR69BBvvTshpMJVC2x0ULwyni68OH%2BGo56FVjxiORiQNA7apRT9R9SXCwGVFJR4QDomPKaNcqu8K87bPGY%2F0R9qQOJ%2FoX4mY9g37%2F5KtI0Gd9WFj3IDy6TIigbdDYJdCSdcBV%2Blmn2bqTQmXDGaARscg5PSRvmw%2Fhz7R9OMwxKZUhZpgqdgLAdVo6B6eQA0TlEAVOsPBPpvPnmFpXiFAynFI1%2BjOkm26UHODGrffjuPB5EfbzVliXtR0NU4Slp9%2BOYXb568nuWbX75pEmuLJ5e%2FfhfFbQT9wWLBAafpEIUxN0GUwkLBU5DXFRnWQMtOl1%2FpcSy%2BbPuQU0dZTDf3u28BjqkAecKsolJs72BQj2vWc34uH%2B6AL%2FPKqZJ4tBSIZ2nB7VyKjwQ24C3lV5MF8jNqXppbjjxOcDlC0DoKftsoSfFwvJkAttl0%2FQfaa3ORltbnbwE6p8mXtMOBaCwa3aYGOq3ebmbboDljTyfRy6zuHlMt1WWaw5%2BGq4RIjZzl9OMeD8j9JXoLnbTjvAYv1F6M0l%2B6q9LWLY0hh44rJsNNF6Y4HZB4g7X&X-Amz-Signature=db4a0da0ded59b94c4c2ad667874f56bf1d37a016f15351a3b6a2b39f667a188&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B4IAJQI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDou4ELozs7JRnIFINXwuxihrk3t5Rf0RbeUtqcGBW%2FxgIhAJIVJhjJhv%2BixA3m9HF37XoXait1TMi6NkX2KbxSi8JAKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyG%2B6VTfZsJPFuV6oq3AOpSGseUHU%2BnRgCDKFv3GuXblY76RofSeGLJJ7Kmu%2FK8VZD4GjzAWBVgF2Mg0mh5AFQcT4PWvRQU633dDQKoNJXcqQEJLp9%2B11ELj4ytZDtIlek7L4RoO4%2FeqzjL2PN%2F66nO%2FhCPryFyamAd6Av7tZllUENhA6uVn6R2FO19SFcY3sAABLwNFJPxxWkXOKIoFnNYAcc01XB5e8Qu9nHCx%2FiEs%2BTd6kJ6IHs0kD%2BbV9ctlf5yL%2Fhp5z6K6uHPUm66jCjmcktD8IMDdrlNYSP%2F5%2FRGCF7WbZsrgkhwqKIxQJfUOKR69BBvvTshpMJVC2x0ULwyni68OH%2BGo56FVjxiORiQNA7apRT9R9SXCwGVFJR4QDomPKaNcqu8K87bPGY%2F0R9qQOJ%2FoX4mY9g37%2F5KtI0Gd9WFj3IDy6TIigbdDYJdCSdcBV%2Blmn2bqTQmXDGaARscg5PSRvmw%2Fhz7R9OMwxKZUhZpgqdgLAdVo6B6eQA0TlEAVOsPBPpvPnmFpXiFAynFI1%2BjOkm26UHODGrffjuPB5EfbzVliXtR0NU4Slp9%2BOYXb568nuWbX75pEmuLJ5e%2FfhfFbQT9wWLBAafpEIUxN0GUwkLBU5DXFRnWQMtOl1%2FpcSy%2BbPuQU0dZTDf3u28BjqkAecKsolJs72BQj2vWc34uH%2B6AL%2FPKqZJ4tBSIZ2nB7VyKjwQ24C3lV5MF8jNqXppbjjxOcDlC0DoKftsoSfFwvJkAttl0%2FQfaa3ORltbnbwE6p8mXtMOBaCwa3aYGOq3ebmbboDljTyfRy6zuHlMt1WWaw5%2BGq4RIjZzl9OMeD8j9JXoLnbTjvAYv1F6M0l%2B6q9LWLY0hh44rJsNNF6Y4HZB4g7X&X-Amz-Signature=00aba9373286c93aba81fbaf6028c25afbcfec48d9d875af688ef8e4230fd58e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B4IAJQI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDou4ELozs7JRnIFINXwuxihrk3t5Rf0RbeUtqcGBW%2FxgIhAJIVJhjJhv%2BixA3m9HF37XoXait1TMi6NkX2KbxSi8JAKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyG%2B6VTfZsJPFuV6oq3AOpSGseUHU%2BnRgCDKFv3GuXblY76RofSeGLJJ7Kmu%2FK8VZD4GjzAWBVgF2Mg0mh5AFQcT4PWvRQU633dDQKoNJXcqQEJLp9%2B11ELj4ytZDtIlek7L4RoO4%2FeqzjL2PN%2F66nO%2FhCPryFyamAd6Av7tZllUENhA6uVn6R2FO19SFcY3sAABLwNFJPxxWkXOKIoFnNYAcc01XB5e8Qu9nHCx%2FiEs%2BTd6kJ6IHs0kD%2BbV9ctlf5yL%2Fhp5z6K6uHPUm66jCjmcktD8IMDdrlNYSP%2F5%2FRGCF7WbZsrgkhwqKIxQJfUOKR69BBvvTshpMJVC2x0ULwyni68OH%2BGo56FVjxiORiQNA7apRT9R9SXCwGVFJR4QDomPKaNcqu8K87bPGY%2F0R9qQOJ%2FoX4mY9g37%2F5KtI0Gd9WFj3IDy6TIigbdDYJdCSdcBV%2Blmn2bqTQmXDGaARscg5PSRvmw%2Fhz7R9OMwxKZUhZpgqdgLAdVo6B6eQA0TlEAVOsPBPpvPnmFpXiFAynFI1%2BjOkm26UHODGrffjuPB5EfbzVliXtR0NU4Slp9%2BOYXb568nuWbX75pEmuLJ5e%2FfhfFbQT9wWLBAafpEIUxN0GUwkLBU5DXFRnWQMtOl1%2FpcSy%2BbPuQU0dZTDf3u28BjqkAecKsolJs72BQj2vWc34uH%2B6AL%2FPKqZJ4tBSIZ2nB7VyKjwQ24C3lV5MF8jNqXppbjjxOcDlC0DoKftsoSfFwvJkAttl0%2FQfaa3ORltbnbwE6p8mXtMOBaCwa3aYGOq3ebmbboDljTyfRy6zuHlMt1WWaw5%2BGq4RIjZzl9OMeD8j9JXoLnbTjvAYv1F6M0l%2B6q9LWLY0hh44rJsNNF6Y4HZB4g7X&X-Amz-Signature=b6ce3db3c23b09977e3e6a7913da64532c7af2837fc216d0dcfc3b0ed90370b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674BKVQ24%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6patdpqyGjBw45AP7adwaz2aX5spJ71agHzObkW64%2FgIgRMTTEbMlNbGutBkdzXv2mjurjPj%2FQXkQswnA5NKiSNsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPbHM8uq%2F69SYMQ1tircA2XUbTJMj8r08KdunQreu0P2Oj8gBq8%2FSebFMWkvx1F6VDBhMwkLmw%2BGbI8Q6sMXYgspl1eRpaaleFm3WFfoHu5xeZPCFXzH540dH4ntrI1rGg8prXdGVBhVVhqmsWw5sTdlK0W%2Bc2m4iXm8iQdUPO2X7qZoS2PArdH0HZfMqFmdpvAtfgbuNy8JknM3P8%2F3DMgIDV8abSEVet8aRH81BlJCHCunoT6%2BI9a%2BpW9Az4SD%2BIqwbo9r4zGIEiRHddXugjCcGqessB8PJehzTj%2B%2F5MQUgSHZ32qEDXq1S7N0WEkwnjJFzuUK9W619M7nhoKGAwGaxmQeY1BGlPJUXq43owmoZmkFuxf8P532b%2FWbyMFolN0tLK8zVvKa%2B%2BJdtxd9eQU61Sm6Yr6%2BRavbPz9ybx3vAXzXG7FfMKr4C6Y1MBrxA%2Fn40xDdSFzTXZPGlXmqdlwz%2FAGg5%2FTecd5QW4hsWnj86kXoFuPK6Ze%2FLvREf22f8IO9Ai0Tdkm4VOuDN8kYrWD5BGevpJ%2Ff7brkG%2B7u7HAN%2BcSFgaowxIgA%2Fn3XuDIXPkutiNlIt5VV7thKxjSd5zOGxaRzJsgvUC%2B%2Ff1CQy3jQ8YuxmZ4cJoz8rgcMALWjbAZRFNEIovFCrNDwMLXe7bwGOqUBwGuIhcqyNmGvLCxi%2Fr9s046oq1wbe8n6THVjAdpNIW7qNJvd5Bb4kqXaUy%2FTRnVX3wtxZu2w7T%2FiQnUuNLXCxB88YC4Pwu2LLUdBuvloaTfIeMm3lUEJJymRapapGvijcwM5iTFjV2afWZqHoCz%2FowXwo%2B6lJ9uoHwMVHy7sGOxmVTaw%2FescVhs7j2ZrQgkJBfzj%2B84PHPHxqW7AIZMPE%2FbUflOa&X-Amz-Signature=4453d0ace7742b3edc1f0261e7a744fccffe0069bfded4238bddecd41768d267&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674BKVQ24%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6patdpqyGjBw45AP7adwaz2aX5spJ71agHzObkW64%2FgIgRMTTEbMlNbGutBkdzXv2mjurjPj%2FQXkQswnA5NKiSNsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPbHM8uq%2F69SYMQ1tircA2XUbTJMj8r08KdunQreu0P2Oj8gBq8%2FSebFMWkvx1F6VDBhMwkLmw%2BGbI8Q6sMXYgspl1eRpaaleFm3WFfoHu5xeZPCFXzH540dH4ntrI1rGg8prXdGVBhVVhqmsWw5sTdlK0W%2Bc2m4iXm8iQdUPO2X7qZoS2PArdH0HZfMqFmdpvAtfgbuNy8JknM3P8%2F3DMgIDV8abSEVet8aRH81BlJCHCunoT6%2BI9a%2BpW9Az4SD%2BIqwbo9r4zGIEiRHddXugjCcGqessB8PJehzTj%2B%2F5MQUgSHZ32qEDXq1S7N0WEkwnjJFzuUK9W619M7nhoKGAwGaxmQeY1BGlPJUXq43owmoZmkFuxf8P532b%2FWbyMFolN0tLK8zVvKa%2B%2BJdtxd9eQU61Sm6Yr6%2BRavbPz9ybx3vAXzXG7FfMKr4C6Y1MBrxA%2Fn40xDdSFzTXZPGlXmqdlwz%2FAGg5%2FTecd5QW4hsWnj86kXoFuPK6Ze%2FLvREf22f8IO9Ai0Tdkm4VOuDN8kYrWD5BGevpJ%2Ff7brkG%2B7u7HAN%2BcSFgaowxIgA%2Fn3XuDIXPkutiNlIt5VV7thKxjSd5zOGxaRzJsgvUC%2B%2Ff1CQy3jQ8YuxmZ4cJoz8rgcMALWjbAZRFNEIovFCrNDwMLXe7bwGOqUBwGuIhcqyNmGvLCxi%2Fr9s046oq1wbe8n6THVjAdpNIW7qNJvd5Bb4kqXaUy%2FTRnVX3wtxZu2w7T%2FiQnUuNLXCxB88YC4Pwu2LLUdBuvloaTfIeMm3lUEJJymRapapGvijcwM5iTFjV2afWZqHoCz%2FowXwo%2B6lJ9uoHwMVHy7sGOxmVTaw%2FescVhs7j2ZrQgkJBfzj%2B84PHPHxqW7AIZMPE%2FbUflOa&X-Amz-Signature=3ea5b71ec137addb68c5afe336b0bc55ea8d2780701f5842dbcf007f425c2d1f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674BKVQ24%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6patdpqyGjBw45AP7adwaz2aX5spJ71agHzObkW64%2FgIgRMTTEbMlNbGutBkdzXv2mjurjPj%2FQXkQswnA5NKiSNsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPbHM8uq%2F69SYMQ1tircA2XUbTJMj8r08KdunQreu0P2Oj8gBq8%2FSebFMWkvx1F6VDBhMwkLmw%2BGbI8Q6sMXYgspl1eRpaaleFm3WFfoHu5xeZPCFXzH540dH4ntrI1rGg8prXdGVBhVVhqmsWw5sTdlK0W%2Bc2m4iXm8iQdUPO2X7qZoS2PArdH0HZfMqFmdpvAtfgbuNy8JknM3P8%2F3DMgIDV8abSEVet8aRH81BlJCHCunoT6%2BI9a%2BpW9Az4SD%2BIqwbo9r4zGIEiRHddXugjCcGqessB8PJehzTj%2B%2F5MQUgSHZ32qEDXq1S7N0WEkwnjJFzuUK9W619M7nhoKGAwGaxmQeY1BGlPJUXq43owmoZmkFuxf8P532b%2FWbyMFolN0tLK8zVvKa%2B%2BJdtxd9eQU61Sm6Yr6%2BRavbPz9ybx3vAXzXG7FfMKr4C6Y1MBrxA%2Fn40xDdSFzTXZPGlXmqdlwz%2FAGg5%2FTecd5QW4hsWnj86kXoFuPK6Ze%2FLvREf22f8IO9Ai0Tdkm4VOuDN8kYrWD5BGevpJ%2Ff7brkG%2B7u7HAN%2BcSFgaowxIgA%2Fn3XuDIXPkutiNlIt5VV7thKxjSd5zOGxaRzJsgvUC%2B%2Ff1CQy3jQ8YuxmZ4cJoz8rgcMALWjbAZRFNEIovFCrNDwMLXe7bwGOqUBwGuIhcqyNmGvLCxi%2Fr9s046oq1wbe8n6THVjAdpNIW7qNJvd5Bb4kqXaUy%2FTRnVX3wtxZu2w7T%2FiQnUuNLXCxB88YC4Pwu2LLUdBuvloaTfIeMm3lUEJJymRapapGvijcwM5iTFjV2afWZqHoCz%2FowXwo%2B6lJ9uoHwMVHy7sGOxmVTaw%2FescVhs7j2ZrQgkJBfzj%2B84PHPHxqW7AIZMPE%2FbUflOa&X-Amz-Signature=0f347be9ce8cf61491597491ed072b7bb2f8d022f4768d0ffe292972f0365a5c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674BKVQ24%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6patdpqyGjBw45AP7adwaz2aX5spJ71agHzObkW64%2FgIgRMTTEbMlNbGutBkdzXv2mjurjPj%2FQXkQswnA5NKiSNsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPbHM8uq%2F69SYMQ1tircA2XUbTJMj8r08KdunQreu0P2Oj8gBq8%2FSebFMWkvx1F6VDBhMwkLmw%2BGbI8Q6sMXYgspl1eRpaaleFm3WFfoHu5xeZPCFXzH540dH4ntrI1rGg8prXdGVBhVVhqmsWw5sTdlK0W%2Bc2m4iXm8iQdUPO2X7qZoS2PArdH0HZfMqFmdpvAtfgbuNy8JknM3P8%2F3DMgIDV8abSEVet8aRH81BlJCHCunoT6%2BI9a%2BpW9Az4SD%2BIqwbo9r4zGIEiRHddXugjCcGqessB8PJehzTj%2B%2F5MQUgSHZ32qEDXq1S7N0WEkwnjJFzuUK9W619M7nhoKGAwGaxmQeY1BGlPJUXq43owmoZmkFuxf8P532b%2FWbyMFolN0tLK8zVvKa%2B%2BJdtxd9eQU61Sm6Yr6%2BRavbPz9ybx3vAXzXG7FfMKr4C6Y1MBrxA%2Fn40xDdSFzTXZPGlXmqdlwz%2FAGg5%2FTecd5QW4hsWnj86kXoFuPK6Ze%2FLvREf22f8IO9Ai0Tdkm4VOuDN8kYrWD5BGevpJ%2Ff7brkG%2B7u7HAN%2BcSFgaowxIgA%2Fn3XuDIXPkutiNlIt5VV7thKxjSd5zOGxaRzJsgvUC%2B%2Ff1CQy3jQ8YuxmZ4cJoz8rgcMALWjbAZRFNEIovFCrNDwMLXe7bwGOqUBwGuIhcqyNmGvLCxi%2Fr9s046oq1wbe8n6THVjAdpNIW7qNJvd5Bb4kqXaUy%2FTRnVX3wtxZu2w7T%2FiQnUuNLXCxB88YC4Pwu2LLUdBuvloaTfIeMm3lUEJJymRapapGvijcwM5iTFjV2afWZqHoCz%2FowXwo%2B6lJ9uoHwMVHy7sGOxmVTaw%2FescVhs7j2ZrQgkJBfzj%2B84PHPHxqW7AIZMPE%2FbUflOa&X-Amz-Signature=92150364a2d8ccce4e2540fbbcc4df69f14e711d09e68c6de1565f43f571f406&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674BKVQ24%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6patdpqyGjBw45AP7adwaz2aX5spJ71agHzObkW64%2FgIgRMTTEbMlNbGutBkdzXv2mjurjPj%2FQXkQswnA5NKiSNsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPbHM8uq%2F69SYMQ1tircA2XUbTJMj8r08KdunQreu0P2Oj8gBq8%2FSebFMWkvx1F6VDBhMwkLmw%2BGbI8Q6sMXYgspl1eRpaaleFm3WFfoHu5xeZPCFXzH540dH4ntrI1rGg8prXdGVBhVVhqmsWw5sTdlK0W%2Bc2m4iXm8iQdUPO2X7qZoS2PArdH0HZfMqFmdpvAtfgbuNy8JknM3P8%2F3DMgIDV8abSEVet8aRH81BlJCHCunoT6%2BI9a%2BpW9Az4SD%2BIqwbo9r4zGIEiRHddXugjCcGqessB8PJehzTj%2B%2F5MQUgSHZ32qEDXq1S7N0WEkwnjJFzuUK9W619M7nhoKGAwGaxmQeY1BGlPJUXq43owmoZmkFuxf8P532b%2FWbyMFolN0tLK8zVvKa%2B%2BJdtxd9eQU61Sm6Yr6%2BRavbPz9ybx3vAXzXG7FfMKr4C6Y1MBrxA%2Fn40xDdSFzTXZPGlXmqdlwz%2FAGg5%2FTecd5QW4hsWnj86kXoFuPK6Ze%2FLvREf22f8IO9Ai0Tdkm4VOuDN8kYrWD5BGevpJ%2Ff7brkG%2B7u7HAN%2BcSFgaowxIgA%2Fn3XuDIXPkutiNlIt5VV7thKxjSd5zOGxaRzJsgvUC%2B%2Ff1CQy3jQ8YuxmZ4cJoz8rgcMALWjbAZRFNEIovFCrNDwMLXe7bwGOqUBwGuIhcqyNmGvLCxi%2Fr9s046oq1wbe8n6THVjAdpNIW7qNJvd5Bb4kqXaUy%2FTRnVX3wtxZu2w7T%2FiQnUuNLXCxB88YC4Pwu2LLUdBuvloaTfIeMm3lUEJJymRapapGvijcwM5iTFjV2afWZqHoCz%2FowXwo%2B6lJ9uoHwMVHy7sGOxmVTaw%2FescVhs7j2ZrQgkJBfzj%2B84PHPHxqW7AIZMPE%2FbUflOa&X-Amz-Signature=d1fa1af2963ec514125a15076cbfb82edf617f93272d500a85f6bff2f3213c61&X-Amz-SignedHeaders=host&x-id=GetObject)
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


