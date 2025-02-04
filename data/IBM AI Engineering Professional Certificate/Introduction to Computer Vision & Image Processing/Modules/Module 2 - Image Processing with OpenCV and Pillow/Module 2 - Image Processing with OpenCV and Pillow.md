

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VNI65IP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDFg09Ja4NKPvRhZqP9GEHIMM5TpefG9sZQ6DOVCOyGrQIhAO2fTWm1F3zDTZkY%2FNUhAke0iGXEMw7WBaoSocFncrfdKv8DCCYQABoMNjM3NDIzMTgzODA1IgxIN%2BN4TgR6J6hRvtYq3APmDU50KbI7QynLkHATKQgZaxVcUzD8MR9S%2FOgnsEF3C%2FfumcjkA9E1xHzCdPO9y%2B0lE7z0juo9Bm1VkBgMW2VCL0lPjiCrS%2BLwdFuLVXXkrbL2POIi3W%2F1nDNA3FwkVtiL4qDikjfhAFjRt%2B2%2FaE8hJi3bT1OCxjVoghzfd6lxn7XQEIVSsmi4NJfHADI2I%2FT2qDyH%2F5ZsGa36QzfYd3nlqHdA5MZy6oheCW%2Fiu65fN7N9KTSZNt1jlEukrBODNmTCbq1L3g3slgKa2Dple5aYSGHcsw87efd0Z%2FTQ4pIlsodAo4y3YKPnsPqL2FFpKlY35HNTGv1IBEU7hBD5V5Y5%2BFMEDxtJWYIx1zUuNpri3rccxVsy5e8%2BcZmpFUfaMU6Gj%2Fherv%2Bmjy1vfdoxmMIlKBnv%2FjvCbcOSnouYWLWuRcfs9Qe2zvqcIVe5nXjskV%2F4qVoN5JDWlt7P6HA6WT%2F57QY%2BrJSflmIbdzvxID5eazKBLF4Ol8l15v%2F%2FLN4O5dHwDPQM9RDG08HTyi0GEBiaqDSZeOBT5rPt2f73roRJuwblwslaOVu24sAZh8NLGlKpsQrbZMm5oYCw3Vdyu5xdbMsJV%2BlH6lwCm4e74gTP%2FBgR2ozbo0U7mLqqBTDovoa9BjqkAcjbBkmkX3IUiYcRCZFh98A4iDnOcR8675%2Bm0VV5K%2FHhXvs2YCHFazx6C7ryrJ1RPUNbp88WFpBWIoEPdrcBwpK6vI8Vnd6SJ0eZRJkL5bkHHdfMqhYvXs3SBQrkBmaii6yAR1AH4vXsALw9FChOXk5nHs1lNRDfdTHghaW1H6ymvughKDBf6WPNYhGaFpFNhHwJ4ZQwuNcZ9%2F7JCLxO3M%2FuQifr&X-Amz-Signature=2e4ffb42d369fa569a921be5322c01439ae4e162d25098eb7d08fe18bea94c8d&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBJIGXVN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCTi8pljvR%2BiR88LO9nk7BmIzZjZ5DCFld583%2FkYArUHAIhAOJ4hrJV1e5EnbF9iG0GSZD3GSKoIUoxBIsLwfHVmZ2FKv8DCCYQABoMNjM3NDIzMTgzODA1Igx8%2F3M%2FnRZcuHfbrAgq3AN26ptPEznCl%2BSnlwSb3dr7Ascpw6I%2FydErBrU1tbRDxoyEwb0Uy5F5tmXNkyz8KupMoKpSxAmsMngHWSdPUBECHlwdyAztceWyU%2F%2FOEm12BpGYka3UaeBpRg1Wvt4%2BMBQ7GOVLYqBfiGlobYiXzGg1yGEuNJ5h%2B02xoar%2Bsr%2F8BlAQHeSXNgWyfQxBgHGPOqh4y7qqtM1gE1Ml9V35U%2FugJxUqzyX6HJnRwtNbiyCGhpVGk5vI1%2FMKc%2BgQXqesM5ctPQm5ZV8HEAwtYmCFNLR8%2FgX0O2th5Y4mDAr9At0D%2BfFJ3vbE9ALa5FQ0vbhxCNcCyTnkzdwaho5Xh7HipbLo9wBqb%2FBLxOgZW1iJk0pvAHIx2c5FVl1K%2BedBybPXt0WtPB%2BhksCeJsKdtOVp5h6jmE3Ko32U2R5e3BMxSQhJ8PIPM%2F4EWzCeAVpRISjvZgxKdfwu1vai%2BbyhLl3Vv%2BsuZVX4%2BdNS649ZINlgd5VlO4hwNxc57%2FL%2Bt84X3%2F2462xwSlBTOfmLigjWswaQJqm185j7TH0XYseSBT%2B5FKHQBez%2BueYNpjuv%2FDU9ML9VW%2BsNQ%2Fb04yQRNnPqf7xhl%2BI%2F0uDbDyS%2FlwJExKe1LULRw1YkSFZf7x2M5zZ%2BxTDdvoa9BjqkAduIDR6pTrOXdjd4oI5gfMD30BoDTBvTYE2oBWTGjYgX%2FKKxIJiPRVxbOBucyVfFuS11bp882htuZju%2B1ZndtqQ%2BPUGSkGBJ5H76iYJO%2BoBB8qFTCX7ZkTCOzfUngTD%2Be4ZZfM13i9fhEJtR2E1cobyHo24ZWruj4PhHPOErg2pAwKWCFusEwTjt9E6kVR6eihnny65kZxedGfxwTIJ8rH4zCWxP&X-Amz-Signature=110a740ddf65102448e598a7c83819f90df613e47ccdb52acab65ad125cb5cd7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBJIGXVN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCTi8pljvR%2BiR88LO9nk7BmIzZjZ5DCFld583%2FkYArUHAIhAOJ4hrJV1e5EnbF9iG0GSZD3GSKoIUoxBIsLwfHVmZ2FKv8DCCYQABoMNjM3NDIzMTgzODA1Igx8%2F3M%2FnRZcuHfbrAgq3AN26ptPEznCl%2BSnlwSb3dr7Ascpw6I%2FydErBrU1tbRDxoyEwb0Uy5F5tmXNkyz8KupMoKpSxAmsMngHWSdPUBECHlwdyAztceWyU%2F%2FOEm12BpGYka3UaeBpRg1Wvt4%2BMBQ7GOVLYqBfiGlobYiXzGg1yGEuNJ5h%2B02xoar%2Bsr%2F8BlAQHeSXNgWyfQxBgHGPOqh4y7qqtM1gE1Ml9V35U%2FugJxUqzyX6HJnRwtNbiyCGhpVGk5vI1%2FMKc%2BgQXqesM5ctPQm5ZV8HEAwtYmCFNLR8%2FgX0O2th5Y4mDAr9At0D%2BfFJ3vbE9ALa5FQ0vbhxCNcCyTnkzdwaho5Xh7HipbLo9wBqb%2FBLxOgZW1iJk0pvAHIx2c5FVl1K%2BedBybPXt0WtPB%2BhksCeJsKdtOVp5h6jmE3Ko32U2R5e3BMxSQhJ8PIPM%2F4EWzCeAVpRISjvZgxKdfwu1vai%2BbyhLl3Vv%2BsuZVX4%2BdNS649ZINlgd5VlO4hwNxc57%2FL%2Bt84X3%2F2462xwSlBTOfmLigjWswaQJqm185j7TH0XYseSBT%2B5FKHQBez%2BueYNpjuv%2FDU9ML9VW%2BsNQ%2Fb04yQRNnPqf7xhl%2BI%2F0uDbDyS%2FlwJExKe1LULRw1YkSFZf7x2M5zZ%2BxTDdvoa9BjqkAduIDR6pTrOXdjd4oI5gfMD30BoDTBvTYE2oBWTGjYgX%2FKKxIJiPRVxbOBucyVfFuS11bp882htuZju%2B1ZndtqQ%2BPUGSkGBJ5H76iYJO%2BoBB8qFTCX7ZkTCOzfUngTD%2Be4ZZfM13i9fhEJtR2E1cobyHo24ZWruj4PhHPOErg2pAwKWCFusEwTjt9E6kVR6eihnny65kZxedGfxwTIJ8rH4zCWxP&X-Amz-Signature=d2712938cc18246e11fce109aa2b9a4995332f9e1f393dfb546df6f97e38a5fb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBJIGXVN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCTi8pljvR%2BiR88LO9nk7BmIzZjZ5DCFld583%2FkYArUHAIhAOJ4hrJV1e5EnbF9iG0GSZD3GSKoIUoxBIsLwfHVmZ2FKv8DCCYQABoMNjM3NDIzMTgzODA1Igx8%2F3M%2FnRZcuHfbrAgq3AN26ptPEznCl%2BSnlwSb3dr7Ascpw6I%2FydErBrU1tbRDxoyEwb0Uy5F5tmXNkyz8KupMoKpSxAmsMngHWSdPUBECHlwdyAztceWyU%2F%2FOEm12BpGYka3UaeBpRg1Wvt4%2BMBQ7GOVLYqBfiGlobYiXzGg1yGEuNJ5h%2B02xoar%2Bsr%2F8BlAQHeSXNgWyfQxBgHGPOqh4y7qqtM1gE1Ml9V35U%2FugJxUqzyX6HJnRwtNbiyCGhpVGk5vI1%2FMKc%2BgQXqesM5ctPQm5ZV8HEAwtYmCFNLR8%2FgX0O2th5Y4mDAr9At0D%2BfFJ3vbE9ALa5FQ0vbhxCNcCyTnkzdwaho5Xh7HipbLo9wBqb%2FBLxOgZW1iJk0pvAHIx2c5FVl1K%2BedBybPXt0WtPB%2BhksCeJsKdtOVp5h6jmE3Ko32U2R5e3BMxSQhJ8PIPM%2F4EWzCeAVpRISjvZgxKdfwu1vai%2BbyhLl3Vv%2BsuZVX4%2BdNS649ZINlgd5VlO4hwNxc57%2FL%2Bt84X3%2F2462xwSlBTOfmLigjWswaQJqm185j7TH0XYseSBT%2B5FKHQBez%2BueYNpjuv%2FDU9ML9VW%2BsNQ%2Fb04yQRNnPqf7xhl%2BI%2F0uDbDyS%2FlwJExKe1LULRw1YkSFZf7x2M5zZ%2BxTDdvoa9BjqkAduIDR6pTrOXdjd4oI5gfMD30BoDTBvTYE2oBWTGjYgX%2FKKxIJiPRVxbOBucyVfFuS11bp882htuZju%2B1ZndtqQ%2BPUGSkGBJ5H76iYJO%2BoBB8qFTCX7ZkTCOzfUngTD%2Be4ZZfM13i9fhEJtR2E1cobyHo24ZWruj4PhHPOErg2pAwKWCFusEwTjt9E6kVR6eihnny65kZxedGfxwTIJ8rH4zCWxP&X-Amz-Signature=d3bf8deb2476d9955eb0a2f86207f86adeda77fa5bd9b3abf024a93cd700e3cc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBJIGXVN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCTi8pljvR%2BiR88LO9nk7BmIzZjZ5DCFld583%2FkYArUHAIhAOJ4hrJV1e5EnbF9iG0GSZD3GSKoIUoxBIsLwfHVmZ2FKv8DCCYQABoMNjM3NDIzMTgzODA1Igx8%2F3M%2FnRZcuHfbrAgq3AN26ptPEznCl%2BSnlwSb3dr7Ascpw6I%2FydErBrU1tbRDxoyEwb0Uy5F5tmXNkyz8KupMoKpSxAmsMngHWSdPUBECHlwdyAztceWyU%2F%2FOEm12BpGYka3UaeBpRg1Wvt4%2BMBQ7GOVLYqBfiGlobYiXzGg1yGEuNJ5h%2B02xoar%2Bsr%2F8BlAQHeSXNgWyfQxBgHGPOqh4y7qqtM1gE1Ml9V35U%2FugJxUqzyX6HJnRwtNbiyCGhpVGk5vI1%2FMKc%2BgQXqesM5ctPQm5ZV8HEAwtYmCFNLR8%2FgX0O2th5Y4mDAr9At0D%2BfFJ3vbE9ALa5FQ0vbhxCNcCyTnkzdwaho5Xh7HipbLo9wBqb%2FBLxOgZW1iJk0pvAHIx2c5FVl1K%2BedBybPXt0WtPB%2BhksCeJsKdtOVp5h6jmE3Ko32U2R5e3BMxSQhJ8PIPM%2F4EWzCeAVpRISjvZgxKdfwu1vai%2BbyhLl3Vv%2BsuZVX4%2BdNS649ZINlgd5VlO4hwNxc57%2FL%2Bt84X3%2F2462xwSlBTOfmLigjWswaQJqm185j7TH0XYseSBT%2B5FKHQBez%2BueYNpjuv%2FDU9ML9VW%2BsNQ%2Fb04yQRNnPqf7xhl%2BI%2F0uDbDyS%2FlwJExKe1LULRw1YkSFZf7x2M5zZ%2BxTDdvoa9BjqkAduIDR6pTrOXdjd4oI5gfMD30BoDTBvTYE2oBWTGjYgX%2FKKxIJiPRVxbOBucyVfFuS11bp882htuZju%2B1ZndtqQ%2BPUGSkGBJ5H76iYJO%2BoBB8qFTCX7ZkTCOzfUngTD%2Be4ZZfM13i9fhEJtR2E1cobyHo24ZWruj4PhHPOErg2pAwKWCFusEwTjt9E6kVR6eihnny65kZxedGfxwTIJ8rH4zCWxP&X-Amz-Signature=6aed26cf2beeb7a1f4591eb67a80024da1027b19da5837f850ab0a57ef121991&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBJIGXVN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCTi8pljvR%2BiR88LO9nk7BmIzZjZ5DCFld583%2FkYArUHAIhAOJ4hrJV1e5EnbF9iG0GSZD3GSKoIUoxBIsLwfHVmZ2FKv8DCCYQABoMNjM3NDIzMTgzODA1Igx8%2F3M%2FnRZcuHfbrAgq3AN26ptPEznCl%2BSnlwSb3dr7Ascpw6I%2FydErBrU1tbRDxoyEwb0Uy5F5tmXNkyz8KupMoKpSxAmsMngHWSdPUBECHlwdyAztceWyU%2F%2FOEm12BpGYka3UaeBpRg1Wvt4%2BMBQ7GOVLYqBfiGlobYiXzGg1yGEuNJ5h%2B02xoar%2Bsr%2F8BlAQHeSXNgWyfQxBgHGPOqh4y7qqtM1gE1Ml9V35U%2FugJxUqzyX6HJnRwtNbiyCGhpVGk5vI1%2FMKc%2BgQXqesM5ctPQm5ZV8HEAwtYmCFNLR8%2FgX0O2th5Y4mDAr9At0D%2BfFJ3vbE9ALa5FQ0vbhxCNcCyTnkzdwaho5Xh7HipbLo9wBqb%2FBLxOgZW1iJk0pvAHIx2c5FVl1K%2BedBybPXt0WtPB%2BhksCeJsKdtOVp5h6jmE3Ko32U2R5e3BMxSQhJ8PIPM%2F4EWzCeAVpRISjvZgxKdfwu1vai%2BbyhLl3Vv%2BsuZVX4%2BdNS649ZINlgd5VlO4hwNxc57%2FL%2Bt84X3%2F2462xwSlBTOfmLigjWswaQJqm185j7TH0XYseSBT%2B5FKHQBez%2BueYNpjuv%2FDU9ML9VW%2BsNQ%2Fb04yQRNnPqf7xhl%2BI%2F0uDbDyS%2FlwJExKe1LULRw1YkSFZf7x2M5zZ%2BxTDdvoa9BjqkAduIDR6pTrOXdjd4oI5gfMD30BoDTBvTYE2oBWTGjYgX%2FKKxIJiPRVxbOBucyVfFuS11bp882htuZju%2B1ZndtqQ%2BPUGSkGBJ5H76iYJO%2BoBB8qFTCX7ZkTCOzfUngTD%2Be4ZZfM13i9fhEJtR2E1cobyHo24ZWruj4PhHPOErg2pAwKWCFusEwTjt9E6kVR6eihnny65kZxedGfxwTIJ8rH4zCWxP&X-Amz-Signature=bec87b52420da87c95f61b3dc8a771b15f5986defdd430d8d0af1e4d58a05ae1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VNI65IP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDFg09Ja4NKPvRhZqP9GEHIMM5TpefG9sZQ6DOVCOyGrQIhAO2fTWm1F3zDTZkY%2FNUhAke0iGXEMw7WBaoSocFncrfdKv8DCCYQABoMNjM3NDIzMTgzODA1IgxIN%2BN4TgR6J6hRvtYq3APmDU50KbI7QynLkHATKQgZaxVcUzD8MR9S%2FOgnsEF3C%2FfumcjkA9E1xHzCdPO9y%2B0lE7z0juo9Bm1VkBgMW2VCL0lPjiCrS%2BLwdFuLVXXkrbL2POIi3W%2F1nDNA3FwkVtiL4qDikjfhAFjRt%2B2%2FaE8hJi3bT1OCxjVoghzfd6lxn7XQEIVSsmi4NJfHADI2I%2FT2qDyH%2F5ZsGa36QzfYd3nlqHdA5MZy6oheCW%2Fiu65fN7N9KTSZNt1jlEukrBODNmTCbq1L3g3slgKa2Dple5aYSGHcsw87efd0Z%2FTQ4pIlsodAo4y3YKPnsPqL2FFpKlY35HNTGv1IBEU7hBD5V5Y5%2BFMEDxtJWYIx1zUuNpri3rccxVsy5e8%2BcZmpFUfaMU6Gj%2Fherv%2Bmjy1vfdoxmMIlKBnv%2FjvCbcOSnouYWLWuRcfs9Qe2zvqcIVe5nXjskV%2F4qVoN5JDWlt7P6HA6WT%2F57QY%2BrJSflmIbdzvxID5eazKBLF4Ol8l15v%2F%2FLN4O5dHwDPQM9RDG08HTyi0GEBiaqDSZeOBT5rPt2f73roRJuwblwslaOVu24sAZh8NLGlKpsQrbZMm5oYCw3Vdyu5xdbMsJV%2BlH6lwCm4e74gTP%2FBgR2ozbo0U7mLqqBTDovoa9BjqkAcjbBkmkX3IUiYcRCZFh98A4iDnOcR8675%2Bm0VV5K%2FHhXvs2YCHFazx6C7ryrJ1RPUNbp88WFpBWIoEPdrcBwpK6vI8Vnd6SJ0eZRJkL5bkHHdfMqhYvXs3SBQrkBmaii6yAR1AH4vXsALw9FChOXk5nHs1lNRDfdTHghaW1H6ymvughKDBf6WPNYhGaFpFNhHwJ4ZQwuNcZ9%2F7JCLxO3M%2FuQifr&X-Amz-Signature=6a8ef3d01730e0b6146fe1d75c427655228006a31512847d22dccb7fb7f3cc85&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VNI65IP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDFg09Ja4NKPvRhZqP9GEHIMM5TpefG9sZQ6DOVCOyGrQIhAO2fTWm1F3zDTZkY%2FNUhAke0iGXEMw7WBaoSocFncrfdKv8DCCYQABoMNjM3NDIzMTgzODA1IgxIN%2BN4TgR6J6hRvtYq3APmDU50KbI7QynLkHATKQgZaxVcUzD8MR9S%2FOgnsEF3C%2FfumcjkA9E1xHzCdPO9y%2B0lE7z0juo9Bm1VkBgMW2VCL0lPjiCrS%2BLwdFuLVXXkrbL2POIi3W%2F1nDNA3FwkVtiL4qDikjfhAFjRt%2B2%2FaE8hJi3bT1OCxjVoghzfd6lxn7XQEIVSsmi4NJfHADI2I%2FT2qDyH%2F5ZsGa36QzfYd3nlqHdA5MZy6oheCW%2Fiu65fN7N9KTSZNt1jlEukrBODNmTCbq1L3g3slgKa2Dple5aYSGHcsw87efd0Z%2FTQ4pIlsodAo4y3YKPnsPqL2FFpKlY35HNTGv1IBEU7hBD5V5Y5%2BFMEDxtJWYIx1zUuNpri3rccxVsy5e8%2BcZmpFUfaMU6Gj%2Fherv%2Bmjy1vfdoxmMIlKBnv%2FjvCbcOSnouYWLWuRcfs9Qe2zvqcIVe5nXjskV%2F4qVoN5JDWlt7P6HA6WT%2F57QY%2BrJSflmIbdzvxID5eazKBLF4Ol8l15v%2F%2FLN4O5dHwDPQM9RDG08HTyi0GEBiaqDSZeOBT5rPt2f73roRJuwblwslaOVu24sAZh8NLGlKpsQrbZMm5oYCw3Vdyu5xdbMsJV%2BlH6lwCm4e74gTP%2FBgR2ozbo0U7mLqqBTDovoa9BjqkAcjbBkmkX3IUiYcRCZFh98A4iDnOcR8675%2Bm0VV5K%2FHhXvs2YCHFazx6C7ryrJ1RPUNbp88WFpBWIoEPdrcBwpK6vI8Vnd6SJ0eZRJkL5bkHHdfMqhYvXs3SBQrkBmaii6yAR1AH4vXsALw9FChOXk5nHs1lNRDfdTHghaW1H6ymvughKDBf6WPNYhGaFpFNhHwJ4ZQwuNcZ9%2F7JCLxO3M%2FuQifr&X-Amz-Signature=16e6f30b68fadcb5a7874b2013615d2183dfaa4689b832391e457b4bc1331627&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VNI65IP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDFg09Ja4NKPvRhZqP9GEHIMM5TpefG9sZQ6DOVCOyGrQIhAO2fTWm1F3zDTZkY%2FNUhAke0iGXEMw7WBaoSocFncrfdKv8DCCYQABoMNjM3NDIzMTgzODA1IgxIN%2BN4TgR6J6hRvtYq3APmDU50KbI7QynLkHATKQgZaxVcUzD8MR9S%2FOgnsEF3C%2FfumcjkA9E1xHzCdPO9y%2B0lE7z0juo9Bm1VkBgMW2VCL0lPjiCrS%2BLwdFuLVXXkrbL2POIi3W%2F1nDNA3FwkVtiL4qDikjfhAFjRt%2B2%2FaE8hJi3bT1OCxjVoghzfd6lxn7XQEIVSsmi4NJfHADI2I%2FT2qDyH%2F5ZsGa36QzfYd3nlqHdA5MZy6oheCW%2Fiu65fN7N9KTSZNt1jlEukrBODNmTCbq1L3g3slgKa2Dple5aYSGHcsw87efd0Z%2FTQ4pIlsodAo4y3YKPnsPqL2FFpKlY35HNTGv1IBEU7hBD5V5Y5%2BFMEDxtJWYIx1zUuNpri3rccxVsy5e8%2BcZmpFUfaMU6Gj%2Fherv%2Bmjy1vfdoxmMIlKBnv%2FjvCbcOSnouYWLWuRcfs9Qe2zvqcIVe5nXjskV%2F4qVoN5JDWlt7P6HA6WT%2F57QY%2BrJSflmIbdzvxID5eazKBLF4Ol8l15v%2F%2FLN4O5dHwDPQM9RDG08HTyi0GEBiaqDSZeOBT5rPt2f73roRJuwblwslaOVu24sAZh8NLGlKpsQrbZMm5oYCw3Vdyu5xdbMsJV%2BlH6lwCm4e74gTP%2FBgR2ozbo0U7mLqqBTDovoa9BjqkAcjbBkmkX3IUiYcRCZFh98A4iDnOcR8675%2Bm0VV5K%2FHhXvs2YCHFazx6C7ryrJ1RPUNbp88WFpBWIoEPdrcBwpK6vI8Vnd6SJ0eZRJkL5bkHHdfMqhYvXs3SBQrkBmaii6yAR1AH4vXsALw9FChOXk5nHs1lNRDfdTHghaW1H6ymvughKDBf6WPNYhGaFpFNhHwJ4ZQwuNcZ9%2F7JCLxO3M%2FuQifr&X-Amz-Signature=491187cae0d9e9135c3c030feeaf38960ad2b7f4f8453ab0edc038ef93834e09&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VNI65IP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDFg09Ja4NKPvRhZqP9GEHIMM5TpefG9sZQ6DOVCOyGrQIhAO2fTWm1F3zDTZkY%2FNUhAke0iGXEMw7WBaoSocFncrfdKv8DCCYQABoMNjM3NDIzMTgzODA1IgxIN%2BN4TgR6J6hRvtYq3APmDU50KbI7QynLkHATKQgZaxVcUzD8MR9S%2FOgnsEF3C%2FfumcjkA9E1xHzCdPO9y%2B0lE7z0juo9Bm1VkBgMW2VCL0lPjiCrS%2BLwdFuLVXXkrbL2POIi3W%2F1nDNA3FwkVtiL4qDikjfhAFjRt%2B2%2FaE8hJi3bT1OCxjVoghzfd6lxn7XQEIVSsmi4NJfHADI2I%2FT2qDyH%2F5ZsGa36QzfYd3nlqHdA5MZy6oheCW%2Fiu65fN7N9KTSZNt1jlEukrBODNmTCbq1L3g3slgKa2Dple5aYSGHcsw87efd0Z%2FTQ4pIlsodAo4y3YKPnsPqL2FFpKlY35HNTGv1IBEU7hBD5V5Y5%2BFMEDxtJWYIx1zUuNpri3rccxVsy5e8%2BcZmpFUfaMU6Gj%2Fherv%2Bmjy1vfdoxmMIlKBnv%2FjvCbcOSnouYWLWuRcfs9Qe2zvqcIVe5nXjskV%2F4qVoN5JDWlt7P6HA6WT%2F57QY%2BrJSflmIbdzvxID5eazKBLF4Ol8l15v%2F%2FLN4O5dHwDPQM9RDG08HTyi0GEBiaqDSZeOBT5rPt2f73roRJuwblwslaOVu24sAZh8NLGlKpsQrbZMm5oYCw3Vdyu5xdbMsJV%2BlH6lwCm4e74gTP%2FBgR2ozbo0U7mLqqBTDovoa9BjqkAcjbBkmkX3IUiYcRCZFh98A4iDnOcR8675%2Bm0VV5K%2FHhXvs2YCHFazx6C7ryrJ1RPUNbp88WFpBWIoEPdrcBwpK6vI8Vnd6SJ0eZRJkL5bkHHdfMqhYvXs3SBQrkBmaii6yAR1AH4vXsALw9FChOXk5nHs1lNRDfdTHghaW1H6ymvughKDBf6WPNYhGaFpFNhHwJ4ZQwuNcZ9%2F7JCLxO3M%2FuQifr&X-Amz-Signature=8b162374d5fd9f4455be84b2241d5e61a0a0c3320fd3683040a3e79df590f5bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VNI65IP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDFg09Ja4NKPvRhZqP9GEHIMM5TpefG9sZQ6DOVCOyGrQIhAO2fTWm1F3zDTZkY%2FNUhAke0iGXEMw7WBaoSocFncrfdKv8DCCYQABoMNjM3NDIzMTgzODA1IgxIN%2BN4TgR6J6hRvtYq3APmDU50KbI7QynLkHATKQgZaxVcUzD8MR9S%2FOgnsEF3C%2FfumcjkA9E1xHzCdPO9y%2B0lE7z0juo9Bm1VkBgMW2VCL0lPjiCrS%2BLwdFuLVXXkrbL2POIi3W%2F1nDNA3FwkVtiL4qDikjfhAFjRt%2B2%2FaE8hJi3bT1OCxjVoghzfd6lxn7XQEIVSsmi4NJfHADI2I%2FT2qDyH%2F5ZsGa36QzfYd3nlqHdA5MZy6oheCW%2Fiu65fN7N9KTSZNt1jlEukrBODNmTCbq1L3g3slgKa2Dple5aYSGHcsw87efd0Z%2FTQ4pIlsodAo4y3YKPnsPqL2FFpKlY35HNTGv1IBEU7hBD5V5Y5%2BFMEDxtJWYIx1zUuNpri3rccxVsy5e8%2BcZmpFUfaMU6Gj%2Fherv%2Bmjy1vfdoxmMIlKBnv%2FjvCbcOSnouYWLWuRcfs9Qe2zvqcIVe5nXjskV%2F4qVoN5JDWlt7P6HA6WT%2F57QY%2BrJSflmIbdzvxID5eazKBLF4Ol8l15v%2F%2FLN4O5dHwDPQM9RDG08HTyi0GEBiaqDSZeOBT5rPt2f73roRJuwblwslaOVu24sAZh8NLGlKpsQrbZMm5oYCw3Vdyu5xdbMsJV%2BlH6lwCm4e74gTP%2FBgR2ozbo0U7mLqqBTDovoa9BjqkAcjbBkmkX3IUiYcRCZFh98A4iDnOcR8675%2Bm0VV5K%2FHhXvs2YCHFazx6C7ryrJ1RPUNbp88WFpBWIoEPdrcBwpK6vI8Vnd6SJ0eZRJkL5bkHHdfMqhYvXs3SBQrkBmaii6yAR1AH4vXsALw9FChOXk5nHs1lNRDfdTHghaW1H6ymvughKDBf6WPNYhGaFpFNhHwJ4ZQwuNcZ9%2F7JCLxO3M%2FuQifr&X-Amz-Signature=c4b223c5459e1eb7715b55c54d722fb0fc4dd358c636fbcb24309ea13fe13009&X-Amz-SignedHeaders=host&x-id=GetObject)
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


