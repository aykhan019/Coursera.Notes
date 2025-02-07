

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466343NAGKZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQD2LBAJm5nBDiafjKXIPe8XBxBH2BcEeiYoGmNdFeMtVgIgKkbWIgxtYDPZuTH%2BqqKESn%2FHoSrtJ2mYewLQmTNUALgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDYpKLFa%2BmB9U0HThSrcA9fo3Ap8RDxekH0hs9pFVY5ZGr44ctRUswH8THCg2psprlgPI9BOsESUhF9yivAnrq%2BMyhuwN53ZXg4ppmrKXQLckKSEQQot%2BQRhi8XDG76awAFdBE0wqk%2BYR0gA9v%2BYzb3sekhAPVd3tZIZ3GxviduLU3CvVzf3oO3fa381FQ%2BehXpfs7%2BhZ8de0VvHWBTEvzzILbxYTrbb5U8V44f6RF1wtCY1F0JT1yR%2FMrFGAhF9N5oG6DY%2BRbi8mghStBMuqtFpXexQqnX72otg00QlOds9rBw7UFOY3%2FFh9oH5%2FYF9S%2B%2FhXuaXEFCr7cu7vp1Upv0SKTlqT2YZr39axLA4SNMfeLGj%2FpdM8xvi1EXj4PtkkZSv38vyoqFYaNen3X1EGiCK%2BJRYfdUz9NLnUP489%2F2v8HPsu0RalGmvDgqwrs3Mt5m%2FrFBYUeQNlEaEkaVch7L3hqAnN2P5p9vna6NE664LKxzsCycPCr2Zcdi5md57KhG7cnYykw4722CAOMHSkKgurPENyzx0zPz5MeT8%2BjJKjo3Uq4FCB2ymQLk2owksiH8Ijo0HyniEhMU94DgnxI%2BvIagkvivHdCu7ggxblh0Wh2ZQW32jOj5%2FRCBck0VRcTp%2BSVNHtxEL5ccbMOT%2Bmb0GOqUBEVj%2FJ1J0FfOVkG9n9lpQKkhJzKLpJIkvWYAIW2X5txMMG8jkxsvlFo1EYF7yV7671%2FJJu%2BOCDJzyMdteXC%2BPeYdPnafIbDiD5U7eFvkESrpkkZ%2BibIFo6Hw%2F%2BnSjV4O5AazevQ6oZFOGYeBOxrRjxxkjYm5G88Hqd4HFdUVCyNGTUW0fx1P017CD7%2BGbDZqz77hVWD0TPnIgZNzXa8%2FMbd6pUnbY&X-Amz-Signature=02dfeed3121395b53347d9a04039ef54c81438b64b600489db9996c4cd5e283d&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCJCFMMO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEV4GzGFms9KqqbP%2FxRJmznYn0WhqN9Kt%2BJi%2Br4P0WxSAiEAyfJSXBIMk7470o38pM6txQNxatqotmzL9txLl8jVXlcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDB1hHKjfdCTyxVhGaircA3J7uc4hhJcIVt%2BFyRpGp%2BCv073ApzYXT6U0ly5dsPXOG%2B9r3wwGLK9X4Kx6jb%2BUEVcOOUbHCu7canlJdNcWTfqQKETjau0B%2FefAxa9G0I69asJo8S4Hz75VbFZMjNpY0iqr2iBx6nhx4mXV1FDpMnmkHgyRAj4XlLkeE82nA2b4RbhvvtqtP69cJH35R%2B4iywrkZf6EMfhwABC9OdrpooyCM3YDZRf51oHBVS3bqJPLOBNgYQ5H1wT2cddHNSHqFznptc7QqjjtUOP0nO4RPHjvE%2FnQqx5Vd9UZHVmkRIHgmyeuyhjNHzPcOnv8%2FxqzhrPdD3seawUdZ0ADekjlyoG6bAS9ElSnGpt8070F0SRDIccOF72KiZSqw2P68OJo6LOfclzPMqQsEdeUDeLulLKGE%2FqmBsVKDNRtVFyIx82%2BOtaiGmeSYPHmSeCj3lBlWS88CMQTZhkxLzLe%2FtkgVFUlmvpeeZi2S11%2FV6m6lZ%2BgoCEMvLT2o8yOPgPLQDIInRCiMaMHS8MkB%2BB1IJ%2BImwFqSUJLjWcgr3%2BZM8lSSwEBvKR00bGDupSb00L%2BL4HcYZjiwYKq0bxlDNnR%2FPkPoez676%2BdwAOI%2BlikMITFB%2FQnW7eIlZntqCqG4m7bMNv%2Bmb0GOqUBYpeS9gZDmL%2FsXOkvXEWz88G5VLJT%2FMp%2Bc%2F%2F9d7nGKRbk1boySH%2BEPUXSq%2BQF0Ni8wbtZpZiuyARpXjnIU5GgQD7pDqKFWM%2FdoynMs8M4lChsH%2BTYiR1k0IudVKgFKSIYTEf%2BUYf9v%2Bcu1ke13CcnE56ILtfYNCvJypH1RiHlnhDEkJLBhR8sSodDIXBp%2FHaB19DSXoEl6vuUaz97tERnEaSx%2FJdM&X-Amz-Signature=0ab14bae87eeb63c4920d1cccbddad8aa495f3cb754769bb0be062a3dc59e40c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCJCFMMO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEV4GzGFms9KqqbP%2FxRJmznYn0WhqN9Kt%2BJi%2Br4P0WxSAiEAyfJSXBIMk7470o38pM6txQNxatqotmzL9txLl8jVXlcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDB1hHKjfdCTyxVhGaircA3J7uc4hhJcIVt%2BFyRpGp%2BCv073ApzYXT6U0ly5dsPXOG%2B9r3wwGLK9X4Kx6jb%2BUEVcOOUbHCu7canlJdNcWTfqQKETjau0B%2FefAxa9G0I69asJo8S4Hz75VbFZMjNpY0iqr2iBx6nhx4mXV1FDpMnmkHgyRAj4XlLkeE82nA2b4RbhvvtqtP69cJH35R%2B4iywrkZf6EMfhwABC9OdrpooyCM3YDZRf51oHBVS3bqJPLOBNgYQ5H1wT2cddHNSHqFznptc7QqjjtUOP0nO4RPHjvE%2FnQqx5Vd9UZHVmkRIHgmyeuyhjNHzPcOnv8%2FxqzhrPdD3seawUdZ0ADekjlyoG6bAS9ElSnGpt8070F0SRDIccOF72KiZSqw2P68OJo6LOfclzPMqQsEdeUDeLulLKGE%2FqmBsVKDNRtVFyIx82%2BOtaiGmeSYPHmSeCj3lBlWS88CMQTZhkxLzLe%2FtkgVFUlmvpeeZi2S11%2FV6m6lZ%2BgoCEMvLT2o8yOPgPLQDIInRCiMaMHS8MkB%2BB1IJ%2BImwFqSUJLjWcgr3%2BZM8lSSwEBvKR00bGDupSb00L%2BL4HcYZjiwYKq0bxlDNnR%2FPkPoez676%2BdwAOI%2BlikMITFB%2FQnW7eIlZntqCqG4m7bMNv%2Bmb0GOqUBYpeS9gZDmL%2FsXOkvXEWz88G5VLJT%2FMp%2Bc%2F%2F9d7nGKRbk1boySH%2BEPUXSq%2BQF0Ni8wbtZpZiuyARpXjnIU5GgQD7pDqKFWM%2FdoynMs8M4lChsH%2BTYiR1k0IudVKgFKSIYTEf%2BUYf9v%2Bcu1ke13CcnE56ILtfYNCvJypH1RiHlnhDEkJLBhR8sSodDIXBp%2FHaB19DSXoEl6vuUaz97tERnEaSx%2FJdM&X-Amz-Signature=c291751284b1d4b4af25cf8a79410314fa362e68650fd1c6c4ea89b1130f64d2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCJCFMMO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEV4GzGFms9KqqbP%2FxRJmznYn0WhqN9Kt%2BJi%2Br4P0WxSAiEAyfJSXBIMk7470o38pM6txQNxatqotmzL9txLl8jVXlcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDB1hHKjfdCTyxVhGaircA3J7uc4hhJcIVt%2BFyRpGp%2BCv073ApzYXT6U0ly5dsPXOG%2B9r3wwGLK9X4Kx6jb%2BUEVcOOUbHCu7canlJdNcWTfqQKETjau0B%2FefAxa9G0I69asJo8S4Hz75VbFZMjNpY0iqr2iBx6nhx4mXV1FDpMnmkHgyRAj4XlLkeE82nA2b4RbhvvtqtP69cJH35R%2B4iywrkZf6EMfhwABC9OdrpooyCM3YDZRf51oHBVS3bqJPLOBNgYQ5H1wT2cddHNSHqFznptc7QqjjtUOP0nO4RPHjvE%2FnQqx5Vd9UZHVmkRIHgmyeuyhjNHzPcOnv8%2FxqzhrPdD3seawUdZ0ADekjlyoG6bAS9ElSnGpt8070F0SRDIccOF72KiZSqw2P68OJo6LOfclzPMqQsEdeUDeLulLKGE%2FqmBsVKDNRtVFyIx82%2BOtaiGmeSYPHmSeCj3lBlWS88CMQTZhkxLzLe%2FtkgVFUlmvpeeZi2S11%2FV6m6lZ%2BgoCEMvLT2o8yOPgPLQDIInRCiMaMHS8MkB%2BB1IJ%2BImwFqSUJLjWcgr3%2BZM8lSSwEBvKR00bGDupSb00L%2BL4HcYZjiwYKq0bxlDNnR%2FPkPoez676%2BdwAOI%2BlikMITFB%2FQnW7eIlZntqCqG4m7bMNv%2Bmb0GOqUBYpeS9gZDmL%2FsXOkvXEWz88G5VLJT%2FMp%2Bc%2F%2F9d7nGKRbk1boySH%2BEPUXSq%2BQF0Ni8wbtZpZiuyARpXjnIU5GgQD7pDqKFWM%2FdoynMs8M4lChsH%2BTYiR1k0IudVKgFKSIYTEf%2BUYf9v%2Bcu1ke13CcnE56ILtfYNCvJypH1RiHlnhDEkJLBhR8sSodDIXBp%2FHaB19DSXoEl6vuUaz97tERnEaSx%2FJdM&X-Amz-Signature=17c38662fc3490b598425c321c367ef98110f81bd4520da622073698ff6c4632&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCJCFMMO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEV4GzGFms9KqqbP%2FxRJmznYn0WhqN9Kt%2BJi%2Br4P0WxSAiEAyfJSXBIMk7470o38pM6txQNxatqotmzL9txLl8jVXlcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDB1hHKjfdCTyxVhGaircA3J7uc4hhJcIVt%2BFyRpGp%2BCv073ApzYXT6U0ly5dsPXOG%2B9r3wwGLK9X4Kx6jb%2BUEVcOOUbHCu7canlJdNcWTfqQKETjau0B%2FefAxa9G0I69asJo8S4Hz75VbFZMjNpY0iqr2iBx6nhx4mXV1FDpMnmkHgyRAj4XlLkeE82nA2b4RbhvvtqtP69cJH35R%2B4iywrkZf6EMfhwABC9OdrpooyCM3YDZRf51oHBVS3bqJPLOBNgYQ5H1wT2cddHNSHqFznptc7QqjjtUOP0nO4RPHjvE%2FnQqx5Vd9UZHVmkRIHgmyeuyhjNHzPcOnv8%2FxqzhrPdD3seawUdZ0ADekjlyoG6bAS9ElSnGpt8070F0SRDIccOF72KiZSqw2P68OJo6LOfclzPMqQsEdeUDeLulLKGE%2FqmBsVKDNRtVFyIx82%2BOtaiGmeSYPHmSeCj3lBlWS88CMQTZhkxLzLe%2FtkgVFUlmvpeeZi2S11%2FV6m6lZ%2BgoCEMvLT2o8yOPgPLQDIInRCiMaMHS8MkB%2BB1IJ%2BImwFqSUJLjWcgr3%2BZM8lSSwEBvKR00bGDupSb00L%2BL4HcYZjiwYKq0bxlDNnR%2FPkPoez676%2BdwAOI%2BlikMITFB%2FQnW7eIlZntqCqG4m7bMNv%2Bmb0GOqUBYpeS9gZDmL%2FsXOkvXEWz88G5VLJT%2FMp%2Bc%2F%2F9d7nGKRbk1boySH%2BEPUXSq%2BQF0Ni8wbtZpZiuyARpXjnIU5GgQD7pDqKFWM%2FdoynMs8M4lChsH%2BTYiR1k0IudVKgFKSIYTEf%2BUYf9v%2Bcu1ke13CcnE56ILtfYNCvJypH1RiHlnhDEkJLBhR8sSodDIXBp%2FHaB19DSXoEl6vuUaz97tERnEaSx%2FJdM&X-Amz-Signature=661ca1279103f7c1535f0c92e73e4639e9c24922d20317790e219e9393972f4d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCJCFMMO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEV4GzGFms9KqqbP%2FxRJmznYn0WhqN9Kt%2BJi%2Br4P0WxSAiEAyfJSXBIMk7470o38pM6txQNxatqotmzL9txLl8jVXlcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDB1hHKjfdCTyxVhGaircA3J7uc4hhJcIVt%2BFyRpGp%2BCv073ApzYXT6U0ly5dsPXOG%2B9r3wwGLK9X4Kx6jb%2BUEVcOOUbHCu7canlJdNcWTfqQKETjau0B%2FefAxa9G0I69asJo8S4Hz75VbFZMjNpY0iqr2iBx6nhx4mXV1FDpMnmkHgyRAj4XlLkeE82nA2b4RbhvvtqtP69cJH35R%2B4iywrkZf6EMfhwABC9OdrpooyCM3YDZRf51oHBVS3bqJPLOBNgYQ5H1wT2cddHNSHqFznptc7QqjjtUOP0nO4RPHjvE%2FnQqx5Vd9UZHVmkRIHgmyeuyhjNHzPcOnv8%2FxqzhrPdD3seawUdZ0ADekjlyoG6bAS9ElSnGpt8070F0SRDIccOF72KiZSqw2P68OJo6LOfclzPMqQsEdeUDeLulLKGE%2FqmBsVKDNRtVFyIx82%2BOtaiGmeSYPHmSeCj3lBlWS88CMQTZhkxLzLe%2FtkgVFUlmvpeeZi2S11%2FV6m6lZ%2BgoCEMvLT2o8yOPgPLQDIInRCiMaMHS8MkB%2BB1IJ%2BImwFqSUJLjWcgr3%2BZM8lSSwEBvKR00bGDupSb00L%2BL4HcYZjiwYKq0bxlDNnR%2FPkPoez676%2BdwAOI%2BlikMITFB%2FQnW7eIlZntqCqG4m7bMNv%2Bmb0GOqUBYpeS9gZDmL%2FsXOkvXEWz88G5VLJT%2FMp%2Bc%2F%2F9d7nGKRbk1boySH%2BEPUXSq%2BQF0Ni8wbtZpZiuyARpXjnIU5GgQD7pDqKFWM%2FdoynMs8M4lChsH%2BTYiR1k0IudVKgFKSIYTEf%2BUYf9v%2Bcu1ke13CcnE56ILtfYNCvJypH1RiHlnhDEkJLBhR8sSodDIXBp%2FHaB19DSXoEl6vuUaz97tERnEaSx%2FJdM&X-Amz-Signature=2dc1db0c3dee7fc6cc593f088898a66793cee46ddac97d7ff7b79dd6e39be8f0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466343NAGKZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQD2LBAJm5nBDiafjKXIPe8XBxBH2BcEeiYoGmNdFeMtVgIgKkbWIgxtYDPZuTH%2BqqKESn%2FHoSrtJ2mYewLQmTNUALgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDYpKLFa%2BmB9U0HThSrcA9fo3Ap8RDxekH0hs9pFVY5ZGr44ctRUswH8THCg2psprlgPI9BOsESUhF9yivAnrq%2BMyhuwN53ZXg4ppmrKXQLckKSEQQot%2BQRhi8XDG76awAFdBE0wqk%2BYR0gA9v%2BYzb3sekhAPVd3tZIZ3GxviduLU3CvVzf3oO3fa381FQ%2BehXpfs7%2BhZ8de0VvHWBTEvzzILbxYTrbb5U8V44f6RF1wtCY1F0JT1yR%2FMrFGAhF9N5oG6DY%2BRbi8mghStBMuqtFpXexQqnX72otg00QlOds9rBw7UFOY3%2FFh9oH5%2FYF9S%2B%2FhXuaXEFCr7cu7vp1Upv0SKTlqT2YZr39axLA4SNMfeLGj%2FpdM8xvi1EXj4PtkkZSv38vyoqFYaNen3X1EGiCK%2BJRYfdUz9NLnUP489%2F2v8HPsu0RalGmvDgqwrs3Mt5m%2FrFBYUeQNlEaEkaVch7L3hqAnN2P5p9vna6NE664LKxzsCycPCr2Zcdi5md57KhG7cnYykw4722CAOMHSkKgurPENyzx0zPz5MeT8%2BjJKjo3Uq4FCB2ymQLk2owksiH8Ijo0HyniEhMU94DgnxI%2BvIagkvivHdCu7ggxblh0Wh2ZQW32jOj5%2FRCBck0VRcTp%2BSVNHtxEL5ccbMOT%2Bmb0GOqUBEVj%2FJ1J0FfOVkG9n9lpQKkhJzKLpJIkvWYAIW2X5txMMG8jkxsvlFo1EYF7yV7671%2FJJu%2BOCDJzyMdteXC%2BPeYdPnafIbDiD5U7eFvkESrpkkZ%2BibIFo6Hw%2F%2BnSjV4O5AazevQ6oZFOGYeBOxrRjxxkjYm5G88Hqd4HFdUVCyNGTUW0fx1P017CD7%2BGbDZqz77hVWD0TPnIgZNzXa8%2FMbd6pUnbY&X-Amz-Signature=edd22921c4cff1b93bde06566cdd486e1212a7595ebf5737ad377cfca3978143&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466343NAGKZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQD2LBAJm5nBDiafjKXIPe8XBxBH2BcEeiYoGmNdFeMtVgIgKkbWIgxtYDPZuTH%2BqqKESn%2FHoSrtJ2mYewLQmTNUALgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDYpKLFa%2BmB9U0HThSrcA9fo3Ap8RDxekH0hs9pFVY5ZGr44ctRUswH8THCg2psprlgPI9BOsESUhF9yivAnrq%2BMyhuwN53ZXg4ppmrKXQLckKSEQQot%2BQRhi8XDG76awAFdBE0wqk%2BYR0gA9v%2BYzb3sekhAPVd3tZIZ3GxviduLU3CvVzf3oO3fa381FQ%2BehXpfs7%2BhZ8de0VvHWBTEvzzILbxYTrbb5U8V44f6RF1wtCY1F0JT1yR%2FMrFGAhF9N5oG6DY%2BRbi8mghStBMuqtFpXexQqnX72otg00QlOds9rBw7UFOY3%2FFh9oH5%2FYF9S%2B%2FhXuaXEFCr7cu7vp1Upv0SKTlqT2YZr39axLA4SNMfeLGj%2FpdM8xvi1EXj4PtkkZSv38vyoqFYaNen3X1EGiCK%2BJRYfdUz9NLnUP489%2F2v8HPsu0RalGmvDgqwrs3Mt5m%2FrFBYUeQNlEaEkaVch7L3hqAnN2P5p9vna6NE664LKxzsCycPCr2Zcdi5md57KhG7cnYykw4722CAOMHSkKgurPENyzx0zPz5MeT8%2BjJKjo3Uq4FCB2ymQLk2owksiH8Ijo0HyniEhMU94DgnxI%2BvIagkvivHdCu7ggxblh0Wh2ZQW32jOj5%2FRCBck0VRcTp%2BSVNHtxEL5ccbMOT%2Bmb0GOqUBEVj%2FJ1J0FfOVkG9n9lpQKkhJzKLpJIkvWYAIW2X5txMMG8jkxsvlFo1EYF7yV7671%2FJJu%2BOCDJzyMdteXC%2BPeYdPnafIbDiD5U7eFvkESrpkkZ%2BibIFo6Hw%2F%2BnSjV4O5AazevQ6oZFOGYeBOxrRjxxkjYm5G88Hqd4HFdUVCyNGTUW0fx1P017CD7%2BGbDZqz77hVWD0TPnIgZNzXa8%2FMbd6pUnbY&X-Amz-Signature=1b39a9f6326c37e86ba6de541296bb32ee02d521347c8f7a14e4f53e5d1d4ff5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466343NAGKZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQD2LBAJm5nBDiafjKXIPe8XBxBH2BcEeiYoGmNdFeMtVgIgKkbWIgxtYDPZuTH%2BqqKESn%2FHoSrtJ2mYewLQmTNUALgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDYpKLFa%2BmB9U0HThSrcA9fo3Ap8RDxekH0hs9pFVY5ZGr44ctRUswH8THCg2psprlgPI9BOsESUhF9yivAnrq%2BMyhuwN53ZXg4ppmrKXQLckKSEQQot%2BQRhi8XDG76awAFdBE0wqk%2BYR0gA9v%2BYzb3sekhAPVd3tZIZ3GxviduLU3CvVzf3oO3fa381FQ%2BehXpfs7%2BhZ8de0VvHWBTEvzzILbxYTrbb5U8V44f6RF1wtCY1F0JT1yR%2FMrFGAhF9N5oG6DY%2BRbi8mghStBMuqtFpXexQqnX72otg00QlOds9rBw7UFOY3%2FFh9oH5%2FYF9S%2B%2FhXuaXEFCr7cu7vp1Upv0SKTlqT2YZr39axLA4SNMfeLGj%2FpdM8xvi1EXj4PtkkZSv38vyoqFYaNen3X1EGiCK%2BJRYfdUz9NLnUP489%2F2v8HPsu0RalGmvDgqwrs3Mt5m%2FrFBYUeQNlEaEkaVch7L3hqAnN2P5p9vna6NE664LKxzsCycPCr2Zcdi5md57KhG7cnYykw4722CAOMHSkKgurPENyzx0zPz5MeT8%2BjJKjo3Uq4FCB2ymQLk2owksiH8Ijo0HyniEhMU94DgnxI%2BvIagkvivHdCu7ggxblh0Wh2ZQW32jOj5%2FRCBck0VRcTp%2BSVNHtxEL5ccbMOT%2Bmb0GOqUBEVj%2FJ1J0FfOVkG9n9lpQKkhJzKLpJIkvWYAIW2X5txMMG8jkxsvlFo1EYF7yV7671%2FJJu%2BOCDJzyMdteXC%2BPeYdPnafIbDiD5U7eFvkESrpkkZ%2BibIFo6Hw%2F%2BnSjV4O5AazevQ6oZFOGYeBOxrRjxxkjYm5G88Hqd4HFdUVCyNGTUW0fx1P017CD7%2BGbDZqz77hVWD0TPnIgZNzXa8%2FMbd6pUnbY&X-Amz-Signature=12bb892e0fb33a80e4918fc65b83311aa2dcbc7d9c2c609e09bf72b4447ea4f4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466343NAGKZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQD2LBAJm5nBDiafjKXIPe8XBxBH2BcEeiYoGmNdFeMtVgIgKkbWIgxtYDPZuTH%2BqqKESn%2FHoSrtJ2mYewLQmTNUALgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDYpKLFa%2BmB9U0HThSrcA9fo3Ap8RDxekH0hs9pFVY5ZGr44ctRUswH8THCg2psprlgPI9BOsESUhF9yivAnrq%2BMyhuwN53ZXg4ppmrKXQLckKSEQQot%2BQRhi8XDG76awAFdBE0wqk%2BYR0gA9v%2BYzb3sekhAPVd3tZIZ3GxviduLU3CvVzf3oO3fa381FQ%2BehXpfs7%2BhZ8de0VvHWBTEvzzILbxYTrbb5U8V44f6RF1wtCY1F0JT1yR%2FMrFGAhF9N5oG6DY%2BRbi8mghStBMuqtFpXexQqnX72otg00QlOds9rBw7UFOY3%2FFh9oH5%2FYF9S%2B%2FhXuaXEFCr7cu7vp1Upv0SKTlqT2YZr39axLA4SNMfeLGj%2FpdM8xvi1EXj4PtkkZSv38vyoqFYaNen3X1EGiCK%2BJRYfdUz9NLnUP489%2F2v8HPsu0RalGmvDgqwrs3Mt5m%2FrFBYUeQNlEaEkaVch7L3hqAnN2P5p9vna6NE664LKxzsCycPCr2Zcdi5md57KhG7cnYykw4722CAOMHSkKgurPENyzx0zPz5MeT8%2BjJKjo3Uq4FCB2ymQLk2owksiH8Ijo0HyniEhMU94DgnxI%2BvIagkvivHdCu7ggxblh0Wh2ZQW32jOj5%2FRCBck0VRcTp%2BSVNHtxEL5ccbMOT%2Bmb0GOqUBEVj%2FJ1J0FfOVkG9n9lpQKkhJzKLpJIkvWYAIW2X5txMMG8jkxsvlFo1EYF7yV7671%2FJJu%2BOCDJzyMdteXC%2BPeYdPnafIbDiD5U7eFvkESrpkkZ%2BibIFo6Hw%2F%2BnSjV4O5AazevQ6oZFOGYeBOxrRjxxkjYm5G88Hqd4HFdUVCyNGTUW0fx1P017CD7%2BGbDZqz77hVWD0TPnIgZNzXa8%2FMbd6pUnbY&X-Amz-Signature=30fec032134b8a09427589fe164db685ce104a2a77f49f2d211d9427a75073c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466343NAGKZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQD2LBAJm5nBDiafjKXIPe8XBxBH2BcEeiYoGmNdFeMtVgIgKkbWIgxtYDPZuTH%2BqqKESn%2FHoSrtJ2mYewLQmTNUALgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDYpKLFa%2BmB9U0HThSrcA9fo3Ap8RDxekH0hs9pFVY5ZGr44ctRUswH8THCg2psprlgPI9BOsESUhF9yivAnrq%2BMyhuwN53ZXg4ppmrKXQLckKSEQQot%2BQRhi8XDG76awAFdBE0wqk%2BYR0gA9v%2BYzb3sekhAPVd3tZIZ3GxviduLU3CvVzf3oO3fa381FQ%2BehXpfs7%2BhZ8de0VvHWBTEvzzILbxYTrbb5U8V44f6RF1wtCY1F0JT1yR%2FMrFGAhF9N5oG6DY%2BRbi8mghStBMuqtFpXexQqnX72otg00QlOds9rBw7UFOY3%2FFh9oH5%2FYF9S%2B%2FhXuaXEFCr7cu7vp1Upv0SKTlqT2YZr39axLA4SNMfeLGj%2FpdM8xvi1EXj4PtkkZSv38vyoqFYaNen3X1EGiCK%2BJRYfdUz9NLnUP489%2F2v8HPsu0RalGmvDgqwrs3Mt5m%2FrFBYUeQNlEaEkaVch7L3hqAnN2P5p9vna6NE664LKxzsCycPCr2Zcdi5md57KhG7cnYykw4722CAOMHSkKgurPENyzx0zPz5MeT8%2BjJKjo3Uq4FCB2ymQLk2owksiH8Ijo0HyniEhMU94DgnxI%2BvIagkvivHdCu7ggxblh0Wh2ZQW32jOj5%2FRCBck0VRcTp%2BSVNHtxEL5ccbMOT%2Bmb0GOqUBEVj%2FJ1J0FfOVkG9n9lpQKkhJzKLpJIkvWYAIW2X5txMMG8jkxsvlFo1EYF7yV7671%2FJJu%2BOCDJzyMdteXC%2BPeYdPnafIbDiD5U7eFvkESrpkkZ%2BibIFo6Hw%2F%2BnSjV4O5AazevQ6oZFOGYeBOxrRjxxkjYm5G88Hqd4HFdUVCyNGTUW0fx1P017CD7%2BGbDZqz77hVWD0TPnIgZNzXa8%2FMbd6pUnbY&X-Amz-Signature=a7cca6a9c747f68634afac8c02eac53d283febe43965112b3377654b93e70aa4&X-Amz-SignedHeaders=host&x-id=GetObject)
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


