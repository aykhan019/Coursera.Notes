

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YGTEBVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQvpMS9AE2%2BLia5yGrEeK%2Bt2CnASaIiT1OlNqh18foigIhANsiwl8MtJSBD26s03X%2F%2FSHnOoRGIp46BXx40tp8i%2FIWKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7%2Bp7Wnt3%2B8K9Vphwq3APCfnJPJ2jnDIbfZKdDqzQi7s12iSyRp%2FrUb2UnhCBB1gU7P9meQH0TuPS7Pb38dUFHHaijp2pjWpczybwZdEt7MrO5yt%2Fjo1mO4P%2FjulhGM1nkey%2BiOnehi87Noj7My6vYHOckOaWX%2Bs1P5gtsh4kMQmuneJXqLVeWG6%2Fwn%2F8frhOIt9rmsdRhlPJPy2Q8Q2gIJ7qAA%2BT2b6n6%2BicLYNLhOcg%2Fxm%2Bm6Rsi%2BK9UU%2Fldkj4iJqW4lEnGsxEUC80jUM%2FdY7x8f8jjwPeTEGTTIIg0VZYg5wVVmSy9OoUSbjpHnfut51tOaCNuA4A5hSXUPKl%2Fea87UZ4YYBrwpaEKr0PrvliIaKUkcT1gdXZ%2BMJ55cBxQpiJMwJD1voEXRB9DVmgU2LC3KD7n8Yup3tNhewyKVgrtKBUfWb4%2B%2BsgrJsiJKvV3V7Ess21stFGISRJWKLA7R%2FU170S1LI3dkGeI0HRckTdZTOCcJAsFMhCYDEcw%2FViez%2BmnjGx0MZ0U6qwfTGLzum7%2FQhR8rtUFLPedXG15csHmwGYIn7pKTfyFlm8eD9PHottCKnanXeUfHy3s4qs8t7eF%2Bagx4RhacfSlUWuohHcupMpoDSzMODo5ZXg9IHePuibpJHoehi57mTDg0PC8BjqkASYNJc6oKL87KboRi%2FT5%2FxTK%2FlidfQ9mY63zx1sLS3yP9hqXjwzhchPAp1birsv3B2fh%2FrzjYcfVL7mr1o66%2Bv%2Fmaf0gHk276lMZI66Qqh3by5c%2B9P%2FUNJmTTtwOr7IvpiasAMna3HKwSwhiHkalhHokIOn5llbXldeoZRd2LhAiOU%2F%2FzvE0zf0VnJzt1mVPDvqf2HXWVj8xh8s7oMDerwRT9P3M&X-Amz-Signature=1146d27f4d250e50acba62a7293c10e8c63bd172b6d990db927d9a275556d49b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH6YHGF2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWUoQLTDP7cEQwtsQf8bJPf3xQRboFDfuj5kmJHVR6swIhAOXYHZlo85x9zAqVNeXEOTdaZbcTHU%2BOzlcf%2BJQJ8ra4KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUXLJ6EnzSLZGWRNsq3APQ72Zce5Bjx7o20tSde%2FXW0cj5TM%2BDKWVZvRfUlbJ8FD4MJ%2BuoUiFQMq0Z6M%2F8vjUUginplcGDlR5qXJ%2B1750alWl105DdHN6kZsduigjbRd0YPHPLpfSUjppYFm2QhTsYIP0RC1x1H2vRdYl%2BaeRSS3gYAWW12J0txc1up2Kk20j3tNarEW7bwQOgUD7Ks4lIjJqswAx7h%2Br0H0PjTJfi%2BUPP74Vpe6fiLC6Tp1KHpYU%2BStCy2%2BGLLO3I5EIyQDnkU3Ku2oLKVkAduKjd51JkUp869jSh6ZgrjPtCz7PGnEhN2KlSss3oXG2dFseif1TqGQloGs3TS7QhErPmDrvgplV2rU9qbe54NHtYxZdQSrmIXpEx9KUr5htr6P8YMROm6vCKQieXhS2tqGze%2BHHT1mLkiNvN4uhsnZeMn1glnWTpT0CLN8R5TEh6cOq63QLf0J8V8qi0xMMp3wB5pKfn%2BHhqeT6%2BAog588acFN%2FaLOkjDmL8uCCp92Ec9KCkRCdb5fS%2BqzeUNQk3iLDp6YoU5b7s4FVeZRxdNvv2LFiRVZ26eQDIoCC4So%2Blw4GRuBnGPGCyCAuwQ2zCgI%2BLTCJ8WB770j5uGKVMOq0q8MiAYJAPICkAE2kz%2FCrwCTDI0PC8BjqkAcrj01VTY8LC1uXZiYCiD56FRUxOw60qVpy%2F5zopFDQxKRZ7WNZIMzjptCJ2bL16aBhwrSxSLfTozW4TRdsw8LcxNlMYpQZBFNVRo5Zcmi8oUN1s3gbYbhxNBkHg730kdMP6vc1my2%2Fl8D%2Bgse5XQMUSqRQ%2ByD8aiVORioNgM1jjcgzOVZ0ENVhpMvVDS6wTuyh96Ob8x2ecXuLlEZdqvSLTw5Dp&X-Amz-Signature=1f591b6c95d49cc1548abe903c1879eb4aa75fe60b54ac25a3b488b47ce9d1bc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH6YHGF2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWUoQLTDP7cEQwtsQf8bJPf3xQRboFDfuj5kmJHVR6swIhAOXYHZlo85x9zAqVNeXEOTdaZbcTHU%2BOzlcf%2BJQJ8ra4KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUXLJ6EnzSLZGWRNsq3APQ72Zce5Bjx7o20tSde%2FXW0cj5TM%2BDKWVZvRfUlbJ8FD4MJ%2BuoUiFQMq0Z6M%2F8vjUUginplcGDlR5qXJ%2B1750alWl105DdHN6kZsduigjbRd0YPHPLpfSUjppYFm2QhTsYIP0RC1x1H2vRdYl%2BaeRSS3gYAWW12J0txc1up2Kk20j3tNarEW7bwQOgUD7Ks4lIjJqswAx7h%2Br0H0PjTJfi%2BUPP74Vpe6fiLC6Tp1KHpYU%2BStCy2%2BGLLO3I5EIyQDnkU3Ku2oLKVkAduKjd51JkUp869jSh6ZgrjPtCz7PGnEhN2KlSss3oXG2dFseif1TqGQloGs3TS7QhErPmDrvgplV2rU9qbe54NHtYxZdQSrmIXpEx9KUr5htr6P8YMROm6vCKQieXhS2tqGze%2BHHT1mLkiNvN4uhsnZeMn1glnWTpT0CLN8R5TEh6cOq63QLf0J8V8qi0xMMp3wB5pKfn%2BHhqeT6%2BAog588acFN%2FaLOkjDmL8uCCp92Ec9KCkRCdb5fS%2BqzeUNQk3iLDp6YoU5b7s4FVeZRxdNvv2LFiRVZ26eQDIoCC4So%2Blw4GRuBnGPGCyCAuwQ2zCgI%2BLTCJ8WB770j5uGKVMOq0q8MiAYJAPICkAE2kz%2FCrwCTDI0PC8BjqkAcrj01VTY8LC1uXZiYCiD56FRUxOw60qVpy%2F5zopFDQxKRZ7WNZIMzjptCJ2bL16aBhwrSxSLfTozW4TRdsw8LcxNlMYpQZBFNVRo5Zcmi8oUN1s3gbYbhxNBkHg730kdMP6vc1my2%2Fl8D%2Bgse5XQMUSqRQ%2ByD8aiVORioNgM1jjcgzOVZ0ENVhpMvVDS6wTuyh96Ob8x2ecXuLlEZdqvSLTw5Dp&X-Amz-Signature=4a37360d9edae46ba542e012a7a8aaed85f275d0ccb7fbfb9079090929dd320a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH6YHGF2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWUoQLTDP7cEQwtsQf8bJPf3xQRboFDfuj5kmJHVR6swIhAOXYHZlo85x9zAqVNeXEOTdaZbcTHU%2BOzlcf%2BJQJ8ra4KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUXLJ6EnzSLZGWRNsq3APQ72Zce5Bjx7o20tSde%2FXW0cj5TM%2BDKWVZvRfUlbJ8FD4MJ%2BuoUiFQMq0Z6M%2F8vjUUginplcGDlR5qXJ%2B1750alWl105DdHN6kZsduigjbRd0YPHPLpfSUjppYFm2QhTsYIP0RC1x1H2vRdYl%2BaeRSS3gYAWW12J0txc1up2Kk20j3tNarEW7bwQOgUD7Ks4lIjJqswAx7h%2Br0H0PjTJfi%2BUPP74Vpe6fiLC6Tp1KHpYU%2BStCy2%2BGLLO3I5EIyQDnkU3Ku2oLKVkAduKjd51JkUp869jSh6ZgrjPtCz7PGnEhN2KlSss3oXG2dFseif1TqGQloGs3TS7QhErPmDrvgplV2rU9qbe54NHtYxZdQSrmIXpEx9KUr5htr6P8YMROm6vCKQieXhS2tqGze%2BHHT1mLkiNvN4uhsnZeMn1glnWTpT0CLN8R5TEh6cOq63QLf0J8V8qi0xMMp3wB5pKfn%2BHhqeT6%2BAog588acFN%2FaLOkjDmL8uCCp92Ec9KCkRCdb5fS%2BqzeUNQk3iLDp6YoU5b7s4FVeZRxdNvv2LFiRVZ26eQDIoCC4So%2Blw4GRuBnGPGCyCAuwQ2zCgI%2BLTCJ8WB770j5uGKVMOq0q8MiAYJAPICkAE2kz%2FCrwCTDI0PC8BjqkAcrj01VTY8LC1uXZiYCiD56FRUxOw60qVpy%2F5zopFDQxKRZ7WNZIMzjptCJ2bL16aBhwrSxSLfTozW4TRdsw8LcxNlMYpQZBFNVRo5Zcmi8oUN1s3gbYbhxNBkHg730kdMP6vc1my2%2Fl8D%2Bgse5XQMUSqRQ%2ByD8aiVORioNgM1jjcgzOVZ0ENVhpMvVDS6wTuyh96Ob8x2ecXuLlEZdqvSLTw5Dp&X-Amz-Signature=1d873d76fa8d7c51cd245c910c088b748799e49614288cb646ad40128cb97a18&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH6YHGF2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWUoQLTDP7cEQwtsQf8bJPf3xQRboFDfuj5kmJHVR6swIhAOXYHZlo85x9zAqVNeXEOTdaZbcTHU%2BOzlcf%2BJQJ8ra4KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUXLJ6EnzSLZGWRNsq3APQ72Zce5Bjx7o20tSde%2FXW0cj5TM%2BDKWVZvRfUlbJ8FD4MJ%2BuoUiFQMq0Z6M%2F8vjUUginplcGDlR5qXJ%2B1750alWl105DdHN6kZsduigjbRd0YPHPLpfSUjppYFm2QhTsYIP0RC1x1H2vRdYl%2BaeRSS3gYAWW12J0txc1up2Kk20j3tNarEW7bwQOgUD7Ks4lIjJqswAx7h%2Br0H0PjTJfi%2BUPP74Vpe6fiLC6Tp1KHpYU%2BStCy2%2BGLLO3I5EIyQDnkU3Ku2oLKVkAduKjd51JkUp869jSh6ZgrjPtCz7PGnEhN2KlSss3oXG2dFseif1TqGQloGs3TS7QhErPmDrvgplV2rU9qbe54NHtYxZdQSrmIXpEx9KUr5htr6P8YMROm6vCKQieXhS2tqGze%2BHHT1mLkiNvN4uhsnZeMn1glnWTpT0CLN8R5TEh6cOq63QLf0J8V8qi0xMMp3wB5pKfn%2BHhqeT6%2BAog588acFN%2FaLOkjDmL8uCCp92Ec9KCkRCdb5fS%2BqzeUNQk3iLDp6YoU5b7s4FVeZRxdNvv2LFiRVZ26eQDIoCC4So%2Blw4GRuBnGPGCyCAuwQ2zCgI%2BLTCJ8WB770j5uGKVMOq0q8MiAYJAPICkAE2kz%2FCrwCTDI0PC8BjqkAcrj01VTY8LC1uXZiYCiD56FRUxOw60qVpy%2F5zopFDQxKRZ7WNZIMzjptCJ2bL16aBhwrSxSLfTozW4TRdsw8LcxNlMYpQZBFNVRo5Zcmi8oUN1s3gbYbhxNBkHg730kdMP6vc1my2%2Fl8D%2Bgse5XQMUSqRQ%2ByD8aiVORioNgM1jjcgzOVZ0ENVhpMvVDS6wTuyh96Ob8x2ecXuLlEZdqvSLTw5Dp&X-Amz-Signature=05d77e5e4f2d4ad50efbb868e730449a2f5d69aaacd57a769c5f9bc49becb56f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH6YHGF2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWUoQLTDP7cEQwtsQf8bJPf3xQRboFDfuj5kmJHVR6swIhAOXYHZlo85x9zAqVNeXEOTdaZbcTHU%2BOzlcf%2BJQJ8ra4KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUXLJ6EnzSLZGWRNsq3APQ72Zce5Bjx7o20tSde%2FXW0cj5TM%2BDKWVZvRfUlbJ8FD4MJ%2BuoUiFQMq0Z6M%2F8vjUUginplcGDlR5qXJ%2B1750alWl105DdHN6kZsduigjbRd0YPHPLpfSUjppYFm2QhTsYIP0RC1x1H2vRdYl%2BaeRSS3gYAWW12J0txc1up2Kk20j3tNarEW7bwQOgUD7Ks4lIjJqswAx7h%2Br0H0PjTJfi%2BUPP74Vpe6fiLC6Tp1KHpYU%2BStCy2%2BGLLO3I5EIyQDnkU3Ku2oLKVkAduKjd51JkUp869jSh6ZgrjPtCz7PGnEhN2KlSss3oXG2dFseif1TqGQloGs3TS7QhErPmDrvgplV2rU9qbe54NHtYxZdQSrmIXpEx9KUr5htr6P8YMROm6vCKQieXhS2tqGze%2BHHT1mLkiNvN4uhsnZeMn1glnWTpT0CLN8R5TEh6cOq63QLf0J8V8qi0xMMp3wB5pKfn%2BHhqeT6%2BAog588acFN%2FaLOkjDmL8uCCp92Ec9KCkRCdb5fS%2BqzeUNQk3iLDp6YoU5b7s4FVeZRxdNvv2LFiRVZ26eQDIoCC4So%2Blw4GRuBnGPGCyCAuwQ2zCgI%2BLTCJ8WB770j5uGKVMOq0q8MiAYJAPICkAE2kz%2FCrwCTDI0PC8BjqkAcrj01VTY8LC1uXZiYCiD56FRUxOw60qVpy%2F5zopFDQxKRZ7WNZIMzjptCJ2bL16aBhwrSxSLfTozW4TRdsw8LcxNlMYpQZBFNVRo5Zcmi8oUN1s3gbYbhxNBkHg730kdMP6vc1my2%2Fl8D%2Bgse5XQMUSqRQ%2ByD8aiVORioNgM1jjcgzOVZ0ENVhpMvVDS6wTuyh96Ob8x2ecXuLlEZdqvSLTw5Dp&X-Amz-Signature=0149d716c76f783342d2a573b6a48c941055d6ad03cbd16c3ef5e0efc8e5a487&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YGTEBVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQvpMS9AE2%2BLia5yGrEeK%2Bt2CnASaIiT1OlNqh18foigIhANsiwl8MtJSBD26s03X%2F%2FSHnOoRGIp46BXx40tp8i%2FIWKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7%2Bp7Wnt3%2B8K9Vphwq3APCfnJPJ2jnDIbfZKdDqzQi7s12iSyRp%2FrUb2UnhCBB1gU7P9meQH0TuPS7Pb38dUFHHaijp2pjWpczybwZdEt7MrO5yt%2Fjo1mO4P%2FjulhGM1nkey%2BiOnehi87Noj7My6vYHOckOaWX%2Bs1P5gtsh4kMQmuneJXqLVeWG6%2Fwn%2F8frhOIt9rmsdRhlPJPy2Q8Q2gIJ7qAA%2BT2b6n6%2BicLYNLhOcg%2Fxm%2Bm6Rsi%2BK9UU%2Fldkj4iJqW4lEnGsxEUC80jUM%2FdY7x8f8jjwPeTEGTTIIg0VZYg5wVVmSy9OoUSbjpHnfut51tOaCNuA4A5hSXUPKl%2Fea87UZ4YYBrwpaEKr0PrvliIaKUkcT1gdXZ%2BMJ55cBxQpiJMwJD1voEXRB9DVmgU2LC3KD7n8Yup3tNhewyKVgrtKBUfWb4%2B%2BsgrJsiJKvV3V7Ess21stFGISRJWKLA7R%2FU170S1LI3dkGeI0HRckTdZTOCcJAsFMhCYDEcw%2FViez%2BmnjGx0MZ0U6qwfTGLzum7%2FQhR8rtUFLPedXG15csHmwGYIn7pKTfyFlm8eD9PHottCKnanXeUfHy3s4qs8t7eF%2Bagx4RhacfSlUWuohHcupMpoDSzMODo5ZXg9IHePuibpJHoehi57mTDg0PC8BjqkASYNJc6oKL87KboRi%2FT5%2FxTK%2FlidfQ9mY63zx1sLS3yP9hqXjwzhchPAp1birsv3B2fh%2FrzjYcfVL7mr1o66%2Bv%2Fmaf0gHk276lMZI66Qqh3by5c%2B9P%2FUNJmTTtwOr7IvpiasAMna3HKwSwhiHkalhHokIOn5llbXldeoZRd2LhAiOU%2F%2FzvE0zf0VnJzt1mVPDvqf2HXWVj8xh8s7oMDerwRT9P3M&X-Amz-Signature=e2140a4a17ef8493a9ee67aa96b621f7457e39eb850e0d3a6ba108198da3943e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YGTEBVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQvpMS9AE2%2BLia5yGrEeK%2Bt2CnASaIiT1OlNqh18foigIhANsiwl8MtJSBD26s03X%2F%2FSHnOoRGIp46BXx40tp8i%2FIWKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7%2Bp7Wnt3%2B8K9Vphwq3APCfnJPJ2jnDIbfZKdDqzQi7s12iSyRp%2FrUb2UnhCBB1gU7P9meQH0TuPS7Pb38dUFHHaijp2pjWpczybwZdEt7MrO5yt%2Fjo1mO4P%2FjulhGM1nkey%2BiOnehi87Noj7My6vYHOckOaWX%2Bs1P5gtsh4kMQmuneJXqLVeWG6%2Fwn%2F8frhOIt9rmsdRhlPJPy2Q8Q2gIJ7qAA%2BT2b6n6%2BicLYNLhOcg%2Fxm%2Bm6Rsi%2BK9UU%2Fldkj4iJqW4lEnGsxEUC80jUM%2FdY7x8f8jjwPeTEGTTIIg0VZYg5wVVmSy9OoUSbjpHnfut51tOaCNuA4A5hSXUPKl%2Fea87UZ4YYBrwpaEKr0PrvliIaKUkcT1gdXZ%2BMJ55cBxQpiJMwJD1voEXRB9DVmgU2LC3KD7n8Yup3tNhewyKVgrtKBUfWb4%2B%2BsgrJsiJKvV3V7Ess21stFGISRJWKLA7R%2FU170S1LI3dkGeI0HRckTdZTOCcJAsFMhCYDEcw%2FViez%2BmnjGx0MZ0U6qwfTGLzum7%2FQhR8rtUFLPedXG15csHmwGYIn7pKTfyFlm8eD9PHottCKnanXeUfHy3s4qs8t7eF%2Bagx4RhacfSlUWuohHcupMpoDSzMODo5ZXg9IHePuibpJHoehi57mTDg0PC8BjqkASYNJc6oKL87KboRi%2FT5%2FxTK%2FlidfQ9mY63zx1sLS3yP9hqXjwzhchPAp1birsv3B2fh%2FrzjYcfVL7mr1o66%2Bv%2Fmaf0gHk276lMZI66Qqh3by5c%2B9P%2FUNJmTTtwOr7IvpiasAMna3HKwSwhiHkalhHokIOn5llbXldeoZRd2LhAiOU%2F%2FzvE0zf0VnJzt1mVPDvqf2HXWVj8xh8s7oMDerwRT9P3M&X-Amz-Signature=4cad004802e35f97600240ac748adcd81009546296d2d4b948e8f046793802da&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YGTEBVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQvpMS9AE2%2BLia5yGrEeK%2Bt2CnASaIiT1OlNqh18foigIhANsiwl8MtJSBD26s03X%2F%2FSHnOoRGIp46BXx40tp8i%2FIWKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7%2Bp7Wnt3%2B8K9Vphwq3APCfnJPJ2jnDIbfZKdDqzQi7s12iSyRp%2FrUb2UnhCBB1gU7P9meQH0TuPS7Pb38dUFHHaijp2pjWpczybwZdEt7MrO5yt%2Fjo1mO4P%2FjulhGM1nkey%2BiOnehi87Noj7My6vYHOckOaWX%2Bs1P5gtsh4kMQmuneJXqLVeWG6%2Fwn%2F8frhOIt9rmsdRhlPJPy2Q8Q2gIJ7qAA%2BT2b6n6%2BicLYNLhOcg%2Fxm%2Bm6Rsi%2BK9UU%2Fldkj4iJqW4lEnGsxEUC80jUM%2FdY7x8f8jjwPeTEGTTIIg0VZYg5wVVmSy9OoUSbjpHnfut51tOaCNuA4A5hSXUPKl%2Fea87UZ4YYBrwpaEKr0PrvliIaKUkcT1gdXZ%2BMJ55cBxQpiJMwJD1voEXRB9DVmgU2LC3KD7n8Yup3tNhewyKVgrtKBUfWb4%2B%2BsgrJsiJKvV3V7Ess21stFGISRJWKLA7R%2FU170S1LI3dkGeI0HRckTdZTOCcJAsFMhCYDEcw%2FViez%2BmnjGx0MZ0U6qwfTGLzum7%2FQhR8rtUFLPedXG15csHmwGYIn7pKTfyFlm8eD9PHottCKnanXeUfHy3s4qs8t7eF%2Bagx4RhacfSlUWuohHcupMpoDSzMODo5ZXg9IHePuibpJHoehi57mTDg0PC8BjqkASYNJc6oKL87KboRi%2FT5%2FxTK%2FlidfQ9mY63zx1sLS3yP9hqXjwzhchPAp1birsv3B2fh%2FrzjYcfVL7mr1o66%2Bv%2Fmaf0gHk276lMZI66Qqh3by5c%2B9P%2FUNJmTTtwOr7IvpiasAMna3HKwSwhiHkalhHokIOn5llbXldeoZRd2LhAiOU%2F%2FzvE0zf0VnJzt1mVPDvqf2HXWVj8xh8s7oMDerwRT9P3M&X-Amz-Signature=7ae3eb446aa97856b2a6e9571c87a074aedf036033aa1822d74ad49a5681d72d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YGTEBVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQvpMS9AE2%2BLia5yGrEeK%2Bt2CnASaIiT1OlNqh18foigIhANsiwl8MtJSBD26s03X%2F%2FSHnOoRGIp46BXx40tp8i%2FIWKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7%2Bp7Wnt3%2B8K9Vphwq3APCfnJPJ2jnDIbfZKdDqzQi7s12iSyRp%2FrUb2UnhCBB1gU7P9meQH0TuPS7Pb38dUFHHaijp2pjWpczybwZdEt7MrO5yt%2Fjo1mO4P%2FjulhGM1nkey%2BiOnehi87Noj7My6vYHOckOaWX%2Bs1P5gtsh4kMQmuneJXqLVeWG6%2Fwn%2F8frhOIt9rmsdRhlPJPy2Q8Q2gIJ7qAA%2BT2b6n6%2BicLYNLhOcg%2Fxm%2Bm6Rsi%2BK9UU%2Fldkj4iJqW4lEnGsxEUC80jUM%2FdY7x8f8jjwPeTEGTTIIg0VZYg5wVVmSy9OoUSbjpHnfut51tOaCNuA4A5hSXUPKl%2Fea87UZ4YYBrwpaEKr0PrvliIaKUkcT1gdXZ%2BMJ55cBxQpiJMwJD1voEXRB9DVmgU2LC3KD7n8Yup3tNhewyKVgrtKBUfWb4%2B%2BsgrJsiJKvV3V7Ess21stFGISRJWKLA7R%2FU170S1LI3dkGeI0HRckTdZTOCcJAsFMhCYDEcw%2FViez%2BmnjGx0MZ0U6qwfTGLzum7%2FQhR8rtUFLPedXG15csHmwGYIn7pKTfyFlm8eD9PHottCKnanXeUfHy3s4qs8t7eF%2Bagx4RhacfSlUWuohHcupMpoDSzMODo5ZXg9IHePuibpJHoehi57mTDg0PC8BjqkASYNJc6oKL87KboRi%2FT5%2FxTK%2FlidfQ9mY63zx1sLS3yP9hqXjwzhchPAp1birsv3B2fh%2FrzjYcfVL7mr1o66%2Bv%2Fmaf0gHk276lMZI66Qqh3by5c%2B9P%2FUNJmTTtwOr7IvpiasAMna3HKwSwhiHkalhHokIOn5llbXldeoZRd2LhAiOU%2F%2FzvE0zf0VnJzt1mVPDvqf2HXWVj8xh8s7oMDerwRT9P3M&X-Amz-Signature=7159f4dde137853801d66c96936d16e8637506f3db6df29f59f82618ae2342b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YGTEBVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQvpMS9AE2%2BLia5yGrEeK%2Bt2CnASaIiT1OlNqh18foigIhANsiwl8MtJSBD26s03X%2F%2FSHnOoRGIp46BXx40tp8i%2FIWKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7%2Bp7Wnt3%2B8K9Vphwq3APCfnJPJ2jnDIbfZKdDqzQi7s12iSyRp%2FrUb2UnhCBB1gU7P9meQH0TuPS7Pb38dUFHHaijp2pjWpczybwZdEt7MrO5yt%2Fjo1mO4P%2FjulhGM1nkey%2BiOnehi87Noj7My6vYHOckOaWX%2Bs1P5gtsh4kMQmuneJXqLVeWG6%2Fwn%2F8frhOIt9rmsdRhlPJPy2Q8Q2gIJ7qAA%2BT2b6n6%2BicLYNLhOcg%2Fxm%2Bm6Rsi%2BK9UU%2Fldkj4iJqW4lEnGsxEUC80jUM%2FdY7x8f8jjwPeTEGTTIIg0VZYg5wVVmSy9OoUSbjpHnfut51tOaCNuA4A5hSXUPKl%2Fea87UZ4YYBrwpaEKr0PrvliIaKUkcT1gdXZ%2BMJ55cBxQpiJMwJD1voEXRB9DVmgU2LC3KD7n8Yup3tNhewyKVgrtKBUfWb4%2B%2BsgrJsiJKvV3V7Ess21stFGISRJWKLA7R%2FU170S1LI3dkGeI0HRckTdZTOCcJAsFMhCYDEcw%2FViez%2BmnjGx0MZ0U6qwfTGLzum7%2FQhR8rtUFLPedXG15csHmwGYIn7pKTfyFlm8eD9PHottCKnanXeUfHy3s4qs8t7eF%2Bagx4RhacfSlUWuohHcupMpoDSzMODo5ZXg9IHePuibpJHoehi57mTDg0PC8BjqkASYNJc6oKL87KboRi%2FT5%2FxTK%2FlidfQ9mY63zx1sLS3yP9hqXjwzhchPAp1birsv3B2fh%2FrzjYcfVL7mr1o66%2Bv%2Fmaf0gHk276lMZI66Qqh3by5c%2B9P%2FUNJmTTtwOr7IvpiasAMna3HKwSwhiHkalhHokIOn5llbXldeoZRd2LhAiOU%2F%2FzvE0zf0VnJzt1mVPDvqf2HXWVj8xh8s7oMDerwRT9P3M&X-Amz-Signature=ac746d4fecf01a2ac48381de64ab8d5f70b0d8def16b6a401b1dd968e8e80f03&X-Amz-SignedHeaders=host&x-id=GetObject)
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


