

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYXTT4AS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHUGzCULjsp3FzRDeWkOxHyGV9j3yhjJRhYdx4dR27%2FGAiEAl3ZhInegUXpgevLt2VUqhRYhaB8sjLWHPRFv7nl4mSMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYblKJgsTfLgMPUkircA566CyF4YJh3ofYYArcDEbQF6dsxcFUqS%2FzPhy0LIr3z0K%2Fg5LKuBRvEVBo3Kw9f3yijmAfIyKwVxP%2B6NG5aXcw3uhfWmWogWay7vNS2bENgqIw8AS1VkBRZ%2BC0QAHpx2t%2FVFgmYg6ot3OpIUGT2TGENYxe07zLS3%2Fs7V6BCfvnw1wJy5DxIRHWzYWuOevG4rAF1%2Fy2X77MGJM8FdpYZ9oT9kWyuwzYFsVD5wIj2NcWqpSnZMKiVgnitkWPJgLeuyqT7P1c7ccFREgG9%2BvsMRFpR%2BnPvsxrWnABtVFp6gNRkdhUJcibGf1YWOjjMLBC9pINiInVUpHeiTMPAnQiusKg0YMJGwiLV1yl0XGADEn5PQUpWES%2ByZxe6RtZGDFFGYIUQxZMK7uLfyQHyCq9stNjxw4p9cDfsL%2F92wt1FuMUmSSj4gc5JIA00%2BvtZY5FVJ6siB%2BrqhUToZFYOZ%2FR5Pf1Nh3oDKjSZNVB1PwYGxHR%2B6zTeBdeHbavvGHDX7dXaQkuGKRWTWCZkafxBHr%2Fim3zFT9xOxFLNnFZ99mwEY9o191ebDp1TaXxlyUHB%2F4BPalV%2BHdcBdh%2FSh%2B3YzHlUFudDVkUHld0MwumLh9y6wbC27%2B2wrzY4LsiD9AfQMISp6rwGOqUBdAODWvVxZM3pOxi2BWw3opcErkxYxzPX2nDI9PhZp%2BnKmQpcLBOeqCnOHBWxo4%2FTyv073fVN%2FqZy5%2FoLd2rqo98tfTrycZXVGftsrpI421GjSaIINHn7ohi3EabGDP%2Fbmbsq%2FkaX0BSdbXFXBisnCPX2cPR5rbtinhawa%2Byrvk2OHMfF2M4IHNnclhn0ds5m1cRBBO9PZUhXpDyNJuVvK7a1c%2BgX&X-Amz-Signature=775bf184a6a6db0d4070abf48c3ff9e536dada0991a99b34772fe5861d6b94ef&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE5V2RN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3h4TYh0DijMCWSRrtREeIVwXXImVE24572Ly6hCKpGwIhAIskAVrWvdkEl9WK6negwXlxWnL9QSd4%2B7S5rWXQ9RuBKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz91bBFUY1l6Oy5EmMq3ANRJVRm805Kgl0qg%2Fir62FQNG89nbUQOg5AT2PNzdFmb5OedyDrjeqXymmOCMTDyAWiA3dU0DEPDEkQxpYoFD%2FRWFHMn0nzvGdyWiaBujifAcCoOKVzLDyo8kKVkWgXRdeEBk99XjcF1BbCFjRfU1%2BURI0FRqbuOBiCENTbjx%2BQyp%2BDzKVVtIKz4frdcjDGb%2BkaUYouoCyUkMlOmAJPjER6cpON5f1wyG4jEVEMyNfDFI6iV6wdcSyb532KvYdJsIC3c3bocpkYmGmUV4I6LYJBf8QprRFCHMB29iVlroFS4Buwx1u0yyY9vRcFdQ1cryZNBSSFL8Hsb4sp3KJcrzHScelBxOO8ur5CG3rU0UWfHeacpk5Lg3TUBiWV%2FLMdIdThooJWtTVHu3BSQoayG%2FeZ91p76epwo8lAmmT8x9Syoy4Vh9hTj6kTK7chc7m3R0vWFSiogoALk67PJDcMgl1IxQm%2F%2BaODLe4YdoQBs91CsS2229OiS5YdTlI1O3N2%2Fuhyd1fot2%2BTdk0WreUMR2gExy1qb03kOsEuYB0riG2v67EUfG4B0JUPOZIfo4IfzNZi4KsuXyOfwc6mDOjMB1lHBqA1z9U856DcaXihCFCOh%2FqDXikNYgscYVjWkzCoqeq8BjqkAbG7KyVCnafY4dkTPaYyEmk31x64lCbXxIKdbTPGzhIHIHvZ6vupvsoSUuA8hpuLY6pkSgttYJS%2FVnire6Ef1dUjZ61Ob9xhQhYoBtD2b%2BEJQKbmQnkRAH4RzmdAXtYGqEtuzBUbyzdoyiEs%2BPuR3Y89zMpo2WkkwQweWTRoQIbecydQePSrVUA7p0ckFGYKHoL2WZoDOSwgZMeNEQdATj4a%2BPe%2B&X-Amz-Signature=3bb0ffbc7a65d4a4daaea90857425d17f84114de6062b1d05395f7347d1977eb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE5V2RN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3h4TYh0DijMCWSRrtREeIVwXXImVE24572Ly6hCKpGwIhAIskAVrWvdkEl9WK6negwXlxWnL9QSd4%2B7S5rWXQ9RuBKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz91bBFUY1l6Oy5EmMq3ANRJVRm805Kgl0qg%2Fir62FQNG89nbUQOg5AT2PNzdFmb5OedyDrjeqXymmOCMTDyAWiA3dU0DEPDEkQxpYoFD%2FRWFHMn0nzvGdyWiaBujifAcCoOKVzLDyo8kKVkWgXRdeEBk99XjcF1BbCFjRfU1%2BURI0FRqbuOBiCENTbjx%2BQyp%2BDzKVVtIKz4frdcjDGb%2BkaUYouoCyUkMlOmAJPjER6cpON5f1wyG4jEVEMyNfDFI6iV6wdcSyb532KvYdJsIC3c3bocpkYmGmUV4I6LYJBf8QprRFCHMB29iVlroFS4Buwx1u0yyY9vRcFdQ1cryZNBSSFL8Hsb4sp3KJcrzHScelBxOO8ur5CG3rU0UWfHeacpk5Lg3TUBiWV%2FLMdIdThooJWtTVHu3BSQoayG%2FeZ91p76epwo8lAmmT8x9Syoy4Vh9hTj6kTK7chc7m3R0vWFSiogoALk67PJDcMgl1IxQm%2F%2BaODLe4YdoQBs91CsS2229OiS5YdTlI1O3N2%2Fuhyd1fot2%2BTdk0WreUMR2gExy1qb03kOsEuYB0riG2v67EUfG4B0JUPOZIfo4IfzNZi4KsuXyOfwc6mDOjMB1lHBqA1z9U856DcaXihCFCOh%2FqDXikNYgscYVjWkzCoqeq8BjqkAbG7KyVCnafY4dkTPaYyEmk31x64lCbXxIKdbTPGzhIHIHvZ6vupvsoSUuA8hpuLY6pkSgttYJS%2FVnire6Ef1dUjZ61Ob9xhQhYoBtD2b%2BEJQKbmQnkRAH4RzmdAXtYGqEtuzBUbyzdoyiEs%2BPuR3Y89zMpo2WkkwQweWTRoQIbecydQePSrVUA7p0ckFGYKHoL2WZoDOSwgZMeNEQdATj4a%2BPe%2B&X-Amz-Signature=97a0050d504e7a74319f8cdd82a1151ef52e9d22faab4406cd6aa620949b661a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE5V2RN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3h4TYh0DijMCWSRrtREeIVwXXImVE24572Ly6hCKpGwIhAIskAVrWvdkEl9WK6negwXlxWnL9QSd4%2B7S5rWXQ9RuBKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz91bBFUY1l6Oy5EmMq3ANRJVRm805Kgl0qg%2Fir62FQNG89nbUQOg5AT2PNzdFmb5OedyDrjeqXymmOCMTDyAWiA3dU0DEPDEkQxpYoFD%2FRWFHMn0nzvGdyWiaBujifAcCoOKVzLDyo8kKVkWgXRdeEBk99XjcF1BbCFjRfU1%2BURI0FRqbuOBiCENTbjx%2BQyp%2BDzKVVtIKz4frdcjDGb%2BkaUYouoCyUkMlOmAJPjER6cpON5f1wyG4jEVEMyNfDFI6iV6wdcSyb532KvYdJsIC3c3bocpkYmGmUV4I6LYJBf8QprRFCHMB29iVlroFS4Buwx1u0yyY9vRcFdQ1cryZNBSSFL8Hsb4sp3KJcrzHScelBxOO8ur5CG3rU0UWfHeacpk5Lg3TUBiWV%2FLMdIdThooJWtTVHu3BSQoayG%2FeZ91p76epwo8lAmmT8x9Syoy4Vh9hTj6kTK7chc7m3R0vWFSiogoALk67PJDcMgl1IxQm%2F%2BaODLe4YdoQBs91CsS2229OiS5YdTlI1O3N2%2Fuhyd1fot2%2BTdk0WreUMR2gExy1qb03kOsEuYB0riG2v67EUfG4B0JUPOZIfo4IfzNZi4KsuXyOfwc6mDOjMB1lHBqA1z9U856DcaXihCFCOh%2FqDXikNYgscYVjWkzCoqeq8BjqkAbG7KyVCnafY4dkTPaYyEmk31x64lCbXxIKdbTPGzhIHIHvZ6vupvsoSUuA8hpuLY6pkSgttYJS%2FVnire6Ef1dUjZ61Ob9xhQhYoBtD2b%2BEJQKbmQnkRAH4RzmdAXtYGqEtuzBUbyzdoyiEs%2BPuR3Y89zMpo2WkkwQweWTRoQIbecydQePSrVUA7p0ckFGYKHoL2WZoDOSwgZMeNEQdATj4a%2BPe%2B&X-Amz-Signature=b58767641935872d76f945187c413c4ed41e4d3daa93cdeab5b86403e6e5d86f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE5V2RN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3h4TYh0DijMCWSRrtREeIVwXXImVE24572Ly6hCKpGwIhAIskAVrWvdkEl9WK6negwXlxWnL9QSd4%2B7S5rWXQ9RuBKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz91bBFUY1l6Oy5EmMq3ANRJVRm805Kgl0qg%2Fir62FQNG89nbUQOg5AT2PNzdFmb5OedyDrjeqXymmOCMTDyAWiA3dU0DEPDEkQxpYoFD%2FRWFHMn0nzvGdyWiaBujifAcCoOKVzLDyo8kKVkWgXRdeEBk99XjcF1BbCFjRfU1%2BURI0FRqbuOBiCENTbjx%2BQyp%2BDzKVVtIKz4frdcjDGb%2BkaUYouoCyUkMlOmAJPjER6cpON5f1wyG4jEVEMyNfDFI6iV6wdcSyb532KvYdJsIC3c3bocpkYmGmUV4I6LYJBf8QprRFCHMB29iVlroFS4Buwx1u0yyY9vRcFdQ1cryZNBSSFL8Hsb4sp3KJcrzHScelBxOO8ur5CG3rU0UWfHeacpk5Lg3TUBiWV%2FLMdIdThooJWtTVHu3BSQoayG%2FeZ91p76epwo8lAmmT8x9Syoy4Vh9hTj6kTK7chc7m3R0vWFSiogoALk67PJDcMgl1IxQm%2F%2BaODLe4YdoQBs91CsS2229OiS5YdTlI1O3N2%2Fuhyd1fot2%2BTdk0WreUMR2gExy1qb03kOsEuYB0riG2v67EUfG4B0JUPOZIfo4IfzNZi4KsuXyOfwc6mDOjMB1lHBqA1z9U856DcaXihCFCOh%2FqDXikNYgscYVjWkzCoqeq8BjqkAbG7KyVCnafY4dkTPaYyEmk31x64lCbXxIKdbTPGzhIHIHvZ6vupvsoSUuA8hpuLY6pkSgttYJS%2FVnire6Ef1dUjZ61Ob9xhQhYoBtD2b%2BEJQKbmQnkRAH4RzmdAXtYGqEtuzBUbyzdoyiEs%2BPuR3Y89zMpo2WkkwQweWTRoQIbecydQePSrVUA7p0ckFGYKHoL2WZoDOSwgZMeNEQdATj4a%2BPe%2B&X-Amz-Signature=6b211541305f3efd05ac0e367f3b55eba4521a8db448e315ddc72fde26d6c5c0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE5V2RN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3h4TYh0DijMCWSRrtREeIVwXXImVE24572Ly6hCKpGwIhAIskAVrWvdkEl9WK6negwXlxWnL9QSd4%2B7S5rWXQ9RuBKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz91bBFUY1l6Oy5EmMq3ANRJVRm805Kgl0qg%2Fir62FQNG89nbUQOg5AT2PNzdFmb5OedyDrjeqXymmOCMTDyAWiA3dU0DEPDEkQxpYoFD%2FRWFHMn0nzvGdyWiaBujifAcCoOKVzLDyo8kKVkWgXRdeEBk99XjcF1BbCFjRfU1%2BURI0FRqbuOBiCENTbjx%2BQyp%2BDzKVVtIKz4frdcjDGb%2BkaUYouoCyUkMlOmAJPjER6cpON5f1wyG4jEVEMyNfDFI6iV6wdcSyb532KvYdJsIC3c3bocpkYmGmUV4I6LYJBf8QprRFCHMB29iVlroFS4Buwx1u0yyY9vRcFdQ1cryZNBSSFL8Hsb4sp3KJcrzHScelBxOO8ur5CG3rU0UWfHeacpk5Lg3TUBiWV%2FLMdIdThooJWtTVHu3BSQoayG%2FeZ91p76epwo8lAmmT8x9Syoy4Vh9hTj6kTK7chc7m3R0vWFSiogoALk67PJDcMgl1IxQm%2F%2BaODLe4YdoQBs91CsS2229OiS5YdTlI1O3N2%2Fuhyd1fot2%2BTdk0WreUMR2gExy1qb03kOsEuYB0riG2v67EUfG4B0JUPOZIfo4IfzNZi4KsuXyOfwc6mDOjMB1lHBqA1z9U856DcaXihCFCOh%2FqDXikNYgscYVjWkzCoqeq8BjqkAbG7KyVCnafY4dkTPaYyEmk31x64lCbXxIKdbTPGzhIHIHvZ6vupvsoSUuA8hpuLY6pkSgttYJS%2FVnire6Ef1dUjZ61Ob9xhQhYoBtD2b%2BEJQKbmQnkRAH4RzmdAXtYGqEtuzBUbyzdoyiEs%2BPuR3Y89zMpo2WkkwQweWTRoQIbecydQePSrVUA7p0ckFGYKHoL2WZoDOSwgZMeNEQdATj4a%2BPe%2B&X-Amz-Signature=d668e0ff76dbf71c14162deda353eda6bacd044f755f5eaf5093dd222eb7fcfc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYXTT4AS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHUGzCULjsp3FzRDeWkOxHyGV9j3yhjJRhYdx4dR27%2FGAiEAl3ZhInegUXpgevLt2VUqhRYhaB8sjLWHPRFv7nl4mSMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYblKJgsTfLgMPUkircA566CyF4YJh3ofYYArcDEbQF6dsxcFUqS%2FzPhy0LIr3z0K%2Fg5LKuBRvEVBo3Kw9f3yijmAfIyKwVxP%2B6NG5aXcw3uhfWmWogWay7vNS2bENgqIw8AS1VkBRZ%2BC0QAHpx2t%2FVFgmYg6ot3OpIUGT2TGENYxe07zLS3%2Fs7V6BCfvnw1wJy5DxIRHWzYWuOevG4rAF1%2Fy2X77MGJM8FdpYZ9oT9kWyuwzYFsVD5wIj2NcWqpSnZMKiVgnitkWPJgLeuyqT7P1c7ccFREgG9%2BvsMRFpR%2BnPvsxrWnABtVFp6gNRkdhUJcibGf1YWOjjMLBC9pINiInVUpHeiTMPAnQiusKg0YMJGwiLV1yl0XGADEn5PQUpWES%2ByZxe6RtZGDFFGYIUQxZMK7uLfyQHyCq9stNjxw4p9cDfsL%2F92wt1FuMUmSSj4gc5JIA00%2BvtZY5FVJ6siB%2BrqhUToZFYOZ%2FR5Pf1Nh3oDKjSZNVB1PwYGxHR%2B6zTeBdeHbavvGHDX7dXaQkuGKRWTWCZkafxBHr%2Fim3zFT9xOxFLNnFZ99mwEY9o191ebDp1TaXxlyUHB%2F4BPalV%2BHdcBdh%2FSh%2B3YzHlUFudDVkUHld0MwumLh9y6wbC27%2B2wrzY4LsiD9AfQMISp6rwGOqUBdAODWvVxZM3pOxi2BWw3opcErkxYxzPX2nDI9PhZp%2BnKmQpcLBOeqCnOHBWxo4%2FTyv073fVN%2FqZy5%2FoLd2rqo98tfTrycZXVGftsrpI421GjSaIINHn7ohi3EabGDP%2Fbmbsq%2FkaX0BSdbXFXBisnCPX2cPR5rbtinhawa%2Byrvk2OHMfF2M4IHNnclhn0ds5m1cRBBO9PZUhXpDyNJuVvK7a1c%2BgX&X-Amz-Signature=431a8c34dfb9dabbd3b1145a7292f1bc213eebec74b9711e1739a4e748ef4e91&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYXTT4AS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHUGzCULjsp3FzRDeWkOxHyGV9j3yhjJRhYdx4dR27%2FGAiEAl3ZhInegUXpgevLt2VUqhRYhaB8sjLWHPRFv7nl4mSMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYblKJgsTfLgMPUkircA566CyF4YJh3ofYYArcDEbQF6dsxcFUqS%2FzPhy0LIr3z0K%2Fg5LKuBRvEVBo3Kw9f3yijmAfIyKwVxP%2B6NG5aXcw3uhfWmWogWay7vNS2bENgqIw8AS1VkBRZ%2BC0QAHpx2t%2FVFgmYg6ot3OpIUGT2TGENYxe07zLS3%2Fs7V6BCfvnw1wJy5DxIRHWzYWuOevG4rAF1%2Fy2X77MGJM8FdpYZ9oT9kWyuwzYFsVD5wIj2NcWqpSnZMKiVgnitkWPJgLeuyqT7P1c7ccFREgG9%2BvsMRFpR%2BnPvsxrWnABtVFp6gNRkdhUJcibGf1YWOjjMLBC9pINiInVUpHeiTMPAnQiusKg0YMJGwiLV1yl0XGADEn5PQUpWES%2ByZxe6RtZGDFFGYIUQxZMK7uLfyQHyCq9stNjxw4p9cDfsL%2F92wt1FuMUmSSj4gc5JIA00%2BvtZY5FVJ6siB%2BrqhUToZFYOZ%2FR5Pf1Nh3oDKjSZNVB1PwYGxHR%2B6zTeBdeHbavvGHDX7dXaQkuGKRWTWCZkafxBHr%2Fim3zFT9xOxFLNnFZ99mwEY9o191ebDp1TaXxlyUHB%2F4BPalV%2BHdcBdh%2FSh%2B3YzHlUFudDVkUHld0MwumLh9y6wbC27%2B2wrzY4LsiD9AfQMISp6rwGOqUBdAODWvVxZM3pOxi2BWw3opcErkxYxzPX2nDI9PhZp%2BnKmQpcLBOeqCnOHBWxo4%2FTyv073fVN%2FqZy5%2FoLd2rqo98tfTrycZXVGftsrpI421GjSaIINHn7ohi3EabGDP%2Fbmbsq%2FkaX0BSdbXFXBisnCPX2cPR5rbtinhawa%2Byrvk2OHMfF2M4IHNnclhn0ds5m1cRBBO9PZUhXpDyNJuVvK7a1c%2BgX&X-Amz-Signature=c208b56051e9b1ab3124e1c0b7c44523cdb9c78f8124dba2a08f6d4d99f37723&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYXTT4AS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHUGzCULjsp3FzRDeWkOxHyGV9j3yhjJRhYdx4dR27%2FGAiEAl3ZhInegUXpgevLt2VUqhRYhaB8sjLWHPRFv7nl4mSMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYblKJgsTfLgMPUkircA566CyF4YJh3ofYYArcDEbQF6dsxcFUqS%2FzPhy0LIr3z0K%2Fg5LKuBRvEVBo3Kw9f3yijmAfIyKwVxP%2B6NG5aXcw3uhfWmWogWay7vNS2bENgqIw8AS1VkBRZ%2BC0QAHpx2t%2FVFgmYg6ot3OpIUGT2TGENYxe07zLS3%2Fs7V6BCfvnw1wJy5DxIRHWzYWuOevG4rAF1%2Fy2X77MGJM8FdpYZ9oT9kWyuwzYFsVD5wIj2NcWqpSnZMKiVgnitkWPJgLeuyqT7P1c7ccFREgG9%2BvsMRFpR%2BnPvsxrWnABtVFp6gNRkdhUJcibGf1YWOjjMLBC9pINiInVUpHeiTMPAnQiusKg0YMJGwiLV1yl0XGADEn5PQUpWES%2ByZxe6RtZGDFFGYIUQxZMK7uLfyQHyCq9stNjxw4p9cDfsL%2F92wt1FuMUmSSj4gc5JIA00%2BvtZY5FVJ6siB%2BrqhUToZFYOZ%2FR5Pf1Nh3oDKjSZNVB1PwYGxHR%2B6zTeBdeHbavvGHDX7dXaQkuGKRWTWCZkafxBHr%2Fim3zFT9xOxFLNnFZ99mwEY9o191ebDp1TaXxlyUHB%2F4BPalV%2BHdcBdh%2FSh%2B3YzHlUFudDVkUHld0MwumLh9y6wbC27%2B2wrzY4LsiD9AfQMISp6rwGOqUBdAODWvVxZM3pOxi2BWw3opcErkxYxzPX2nDI9PhZp%2BnKmQpcLBOeqCnOHBWxo4%2FTyv073fVN%2FqZy5%2FoLd2rqo98tfTrycZXVGftsrpI421GjSaIINHn7ohi3EabGDP%2Fbmbsq%2FkaX0BSdbXFXBisnCPX2cPR5rbtinhawa%2Byrvk2OHMfF2M4IHNnclhn0ds5m1cRBBO9PZUhXpDyNJuVvK7a1c%2BgX&X-Amz-Signature=f5fd7da7c3863ac525218244c326cf415ace2d6a087b8e419283cc549448d987&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYXTT4AS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHUGzCULjsp3FzRDeWkOxHyGV9j3yhjJRhYdx4dR27%2FGAiEAl3ZhInegUXpgevLt2VUqhRYhaB8sjLWHPRFv7nl4mSMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYblKJgsTfLgMPUkircA566CyF4YJh3ofYYArcDEbQF6dsxcFUqS%2FzPhy0LIr3z0K%2Fg5LKuBRvEVBo3Kw9f3yijmAfIyKwVxP%2B6NG5aXcw3uhfWmWogWay7vNS2bENgqIw8AS1VkBRZ%2BC0QAHpx2t%2FVFgmYg6ot3OpIUGT2TGENYxe07zLS3%2Fs7V6BCfvnw1wJy5DxIRHWzYWuOevG4rAF1%2Fy2X77MGJM8FdpYZ9oT9kWyuwzYFsVD5wIj2NcWqpSnZMKiVgnitkWPJgLeuyqT7P1c7ccFREgG9%2BvsMRFpR%2BnPvsxrWnABtVFp6gNRkdhUJcibGf1YWOjjMLBC9pINiInVUpHeiTMPAnQiusKg0YMJGwiLV1yl0XGADEn5PQUpWES%2ByZxe6RtZGDFFGYIUQxZMK7uLfyQHyCq9stNjxw4p9cDfsL%2F92wt1FuMUmSSj4gc5JIA00%2BvtZY5FVJ6siB%2BrqhUToZFYOZ%2FR5Pf1Nh3oDKjSZNVB1PwYGxHR%2B6zTeBdeHbavvGHDX7dXaQkuGKRWTWCZkafxBHr%2Fim3zFT9xOxFLNnFZ99mwEY9o191ebDp1TaXxlyUHB%2F4BPalV%2BHdcBdh%2FSh%2B3YzHlUFudDVkUHld0MwumLh9y6wbC27%2B2wrzY4LsiD9AfQMISp6rwGOqUBdAODWvVxZM3pOxi2BWw3opcErkxYxzPX2nDI9PhZp%2BnKmQpcLBOeqCnOHBWxo4%2FTyv073fVN%2FqZy5%2FoLd2rqo98tfTrycZXVGftsrpI421GjSaIINHn7ohi3EabGDP%2Fbmbsq%2FkaX0BSdbXFXBisnCPX2cPR5rbtinhawa%2Byrvk2OHMfF2M4IHNnclhn0ds5m1cRBBO9PZUhXpDyNJuVvK7a1c%2BgX&X-Amz-Signature=d0a7c897f200340bc1b2b882d113b8771414e179a381fa0e1c4854ccbec5751b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYXTT4AS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHUGzCULjsp3FzRDeWkOxHyGV9j3yhjJRhYdx4dR27%2FGAiEAl3ZhInegUXpgevLt2VUqhRYhaB8sjLWHPRFv7nl4mSMqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYblKJgsTfLgMPUkircA566CyF4YJh3ofYYArcDEbQF6dsxcFUqS%2FzPhy0LIr3z0K%2Fg5LKuBRvEVBo3Kw9f3yijmAfIyKwVxP%2B6NG5aXcw3uhfWmWogWay7vNS2bENgqIw8AS1VkBRZ%2BC0QAHpx2t%2FVFgmYg6ot3OpIUGT2TGENYxe07zLS3%2Fs7V6BCfvnw1wJy5DxIRHWzYWuOevG4rAF1%2Fy2X77MGJM8FdpYZ9oT9kWyuwzYFsVD5wIj2NcWqpSnZMKiVgnitkWPJgLeuyqT7P1c7ccFREgG9%2BvsMRFpR%2BnPvsxrWnABtVFp6gNRkdhUJcibGf1YWOjjMLBC9pINiInVUpHeiTMPAnQiusKg0YMJGwiLV1yl0XGADEn5PQUpWES%2ByZxe6RtZGDFFGYIUQxZMK7uLfyQHyCq9stNjxw4p9cDfsL%2F92wt1FuMUmSSj4gc5JIA00%2BvtZY5FVJ6siB%2BrqhUToZFYOZ%2FR5Pf1Nh3oDKjSZNVB1PwYGxHR%2B6zTeBdeHbavvGHDX7dXaQkuGKRWTWCZkafxBHr%2Fim3zFT9xOxFLNnFZ99mwEY9o191ebDp1TaXxlyUHB%2F4BPalV%2BHdcBdh%2FSh%2B3YzHlUFudDVkUHld0MwumLh9y6wbC27%2B2wrzY4LsiD9AfQMISp6rwGOqUBdAODWvVxZM3pOxi2BWw3opcErkxYxzPX2nDI9PhZp%2BnKmQpcLBOeqCnOHBWxo4%2FTyv073fVN%2FqZy5%2FoLd2rqo98tfTrycZXVGftsrpI421GjSaIINHn7ohi3EabGDP%2Fbmbsq%2FkaX0BSdbXFXBisnCPX2cPR5rbtinhawa%2Byrvk2OHMfF2M4IHNnclhn0ds5m1cRBBO9PZUhXpDyNJuVvK7a1c%2BgX&X-Amz-Signature=125de08a8cd03be8942dbb39aa82243b865d46cfd7d3646f321cc62c7a26151c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


