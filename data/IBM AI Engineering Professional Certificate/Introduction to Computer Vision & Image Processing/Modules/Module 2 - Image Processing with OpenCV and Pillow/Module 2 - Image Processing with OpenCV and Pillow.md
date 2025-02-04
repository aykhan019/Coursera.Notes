

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AJA5NNS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDUL6csQV9r8OVNeMXmzYJuEngvDf%2FVHNjEN%2FBYonvepwIhAIeWV7toe%2Bf0GDWUrGLccSr%2FO4BVa3DePMwUr3DOoo5kKv8DCCQQABoMNjM3NDIzMTgzODA1IgxuJtyyoQFY5kkN4v8q3AOp%2FFZD0qAfuiELnz5OZlWaLhoNu5DbJZigQccBIeHb%2F5%2FzUdyHnCt%2FY31xkWwdYov4rLqeEza3gkZg%2FDEzMvhjzy1MjxvqYeGXbYTsJT7WexGRqfk1V94VrMDdJGEKznELkb2cEXcyj0zJCshNyx%2BBOMCIig%2B1PZdqjK5MRkZLzBgLmq1ghtzy6eOfjpzVsuOE4Oa%2FZ7II97eNGgcP%2FI8ej6h44Wl1AnYq94%2FFupBVE8rWkfWFNe0PKMRwR30U5Ttorf6q5b3JCGMlPqG9dafO6SDXUTEFCxvdWlyimIZa2DACcnzKp6%2BugH23M1eTEZ7zmkwLKCflq7DbDLIqH7Ku9cpfCug5El%2FfIipmpSrs9IrhAJlPccnC%2Fkzm8cIg7jLprOTDroAu%2Bqn6pd068XX7%2FBpUWwov1x8lVgvz4lUzTczqdVAWq%2BMSXXDP9JqRMcfRPRW%2F61%2FTwCMh0uGLDnjUXuzoVn6I1Bx2vk8Fs5T44ChXoSCvy1BfR0on9AfdPT3Z0aQcGcVZthXOoGccCjRp9xJDXVZITGdAj4tlVtwGyQFB2EKNAKygQ6aBjy8GkunK4Gd7uvP%2B6MMZevBr8%2FT01I8uHVwQVdK%2BdHpoIrcZ2aLH2sCPPnNwPiCe7TDjhIa9BjqkAeIPFNVTcbvEyxxEasHrY6saNsenxi9OIArtX1DfZtXUo%2F8z9cbvHfSsdXKGfsLrbAyp5GlRwD2SbDXMw9sFWXD458deupY5Oa1Hr46g4zTtEU1N1QCyvK21yAJS%2BDgYHDW7zEyNyieez%2BetGw1eYyaZhszPANWOL3%2BHnRPE4lJmipxKYg14IzSwkEBcSDeUwDmw8liC%2BbmtV8pIUwzYAr6P0f%2Fw&X-Amz-Signature=84fc13ecb59a281264cfe7e9d267cf7be178e28fc1f7142294c32a09c5c9f698&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643ZE7HOE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDC89vB9E2ga0N1mdYiJERZBbPAYZhjnb%2FL2ic%2B0m%2FyXwIhAOJpsYnpb2snpKBNKKnumR9SU%2FsmKRESdSa18h3Ordi2Kv8DCCQQABoMNjM3NDIzMTgzODA1Igw2gzlrMfQuXaex8Lsq3AMSTZ57ZIg4cmZSHUgI58hTPFMtGBEwJeAgc5AQo4oA2FJdiYo%2F9VhSurTptBQtdFk3nChf1wvR8VIut%2FhrUW44AhTNwXEVXaOMFUIhf2I2ziVfNR9u5CBaGfpSXE%2FjygEfbO%2BYqp6O3kpzhQYn6bV1CVce11gJQJpg3Wjtor%2BgOYeIWajX3ArNf7WpUVJqFE10h%2Bov%2FQWfnXBCLdu8RbN2Y%2BR037KMh%2FIw3o43%2FPu7XkO%2FJiw1vcSSCYXSzk3oCtQplCND3r7F9bb9LayhNXImgToZ%2F5cJiQcJ8r3jS6YlJ7mtOuSVVvZeTsgT1Hze1h%2FBQ67fkV9fnJiYKiKPwQEbWeUf4lb6jU0aqXKTnQHzdUmTprTRphTjV7f1u3bi8HboG%2FC8ORZvxFjC5nbjG2l0SO37W1mUCYniRbtCThE1auCcZoGWx4t93v%2BavegOpBpto7s2zBscHYvNRmZLdMAKvgBpLNZ1k96RIKVEBMCqGtOyHsZbpCiB3htfOFuYdF2dceYN3u8mWsO2q%2Bm%2FdgCMI0CvVN%2FDZ6x1RK7OSAgytrC9wrmMqfmiRgvuiwTyqXZz658T8yJVSD8860KV%2FcCoX%2Bg%2B4o2oYQXgH7ryMBm%2BIMyfuVQ%2F8uxVeTRs9DDshIa9BjqkAZwyb7vj4QK%2Bb0TPDapXTSMXhxMM9ai69MSA1L1YAwjsCDY6eeie6Y4chOPjnd%2FRidz9Ensz%2FOFswVaiv%2Fn0sMiXvUJCJK7GSrR9dSlqultjUYK2%2Bex80M9N0fQIXyzyCktr4ARyFBGrBO62loCMr2GSguGtbP8jdXyIve8N74KaLP7LQeRqK7dtj7UhY6EFCWRwnqkf74Mv3cvKOwTJwQJ1f0iy&X-Amz-Signature=e82779ac22da03512b23fb08bacf830c415a09d5e58a3aa12aef2b1bbf47dbd2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643ZE7HOE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDC89vB9E2ga0N1mdYiJERZBbPAYZhjnb%2FL2ic%2B0m%2FyXwIhAOJpsYnpb2snpKBNKKnumR9SU%2FsmKRESdSa18h3Ordi2Kv8DCCQQABoMNjM3NDIzMTgzODA1Igw2gzlrMfQuXaex8Lsq3AMSTZ57ZIg4cmZSHUgI58hTPFMtGBEwJeAgc5AQo4oA2FJdiYo%2F9VhSurTptBQtdFk3nChf1wvR8VIut%2FhrUW44AhTNwXEVXaOMFUIhf2I2ziVfNR9u5CBaGfpSXE%2FjygEfbO%2BYqp6O3kpzhQYn6bV1CVce11gJQJpg3Wjtor%2BgOYeIWajX3ArNf7WpUVJqFE10h%2Bov%2FQWfnXBCLdu8RbN2Y%2BR037KMh%2FIw3o43%2FPu7XkO%2FJiw1vcSSCYXSzk3oCtQplCND3r7F9bb9LayhNXImgToZ%2F5cJiQcJ8r3jS6YlJ7mtOuSVVvZeTsgT1Hze1h%2FBQ67fkV9fnJiYKiKPwQEbWeUf4lb6jU0aqXKTnQHzdUmTprTRphTjV7f1u3bi8HboG%2FC8ORZvxFjC5nbjG2l0SO37W1mUCYniRbtCThE1auCcZoGWx4t93v%2BavegOpBpto7s2zBscHYvNRmZLdMAKvgBpLNZ1k96RIKVEBMCqGtOyHsZbpCiB3htfOFuYdF2dceYN3u8mWsO2q%2Bm%2FdgCMI0CvVN%2FDZ6x1RK7OSAgytrC9wrmMqfmiRgvuiwTyqXZz658T8yJVSD8860KV%2FcCoX%2Bg%2B4o2oYQXgH7ryMBm%2BIMyfuVQ%2F8uxVeTRs9DDshIa9BjqkAZwyb7vj4QK%2Bb0TPDapXTSMXhxMM9ai69MSA1L1YAwjsCDY6eeie6Y4chOPjnd%2FRidz9Ensz%2FOFswVaiv%2Fn0sMiXvUJCJK7GSrR9dSlqultjUYK2%2Bex80M9N0fQIXyzyCktr4ARyFBGrBO62loCMr2GSguGtbP8jdXyIve8N74KaLP7LQeRqK7dtj7UhY6EFCWRwnqkf74Mv3cvKOwTJwQJ1f0iy&X-Amz-Signature=22af3233202f78f1081de9c6993d0501062c859f610866eee0c070e4c6c7f7b8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643ZE7HOE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDC89vB9E2ga0N1mdYiJERZBbPAYZhjnb%2FL2ic%2B0m%2FyXwIhAOJpsYnpb2snpKBNKKnumR9SU%2FsmKRESdSa18h3Ordi2Kv8DCCQQABoMNjM3NDIzMTgzODA1Igw2gzlrMfQuXaex8Lsq3AMSTZ57ZIg4cmZSHUgI58hTPFMtGBEwJeAgc5AQo4oA2FJdiYo%2F9VhSurTptBQtdFk3nChf1wvR8VIut%2FhrUW44AhTNwXEVXaOMFUIhf2I2ziVfNR9u5CBaGfpSXE%2FjygEfbO%2BYqp6O3kpzhQYn6bV1CVce11gJQJpg3Wjtor%2BgOYeIWajX3ArNf7WpUVJqFE10h%2Bov%2FQWfnXBCLdu8RbN2Y%2BR037KMh%2FIw3o43%2FPu7XkO%2FJiw1vcSSCYXSzk3oCtQplCND3r7F9bb9LayhNXImgToZ%2F5cJiQcJ8r3jS6YlJ7mtOuSVVvZeTsgT1Hze1h%2FBQ67fkV9fnJiYKiKPwQEbWeUf4lb6jU0aqXKTnQHzdUmTprTRphTjV7f1u3bi8HboG%2FC8ORZvxFjC5nbjG2l0SO37W1mUCYniRbtCThE1auCcZoGWx4t93v%2BavegOpBpto7s2zBscHYvNRmZLdMAKvgBpLNZ1k96RIKVEBMCqGtOyHsZbpCiB3htfOFuYdF2dceYN3u8mWsO2q%2Bm%2FdgCMI0CvVN%2FDZ6x1RK7OSAgytrC9wrmMqfmiRgvuiwTyqXZz658T8yJVSD8860KV%2FcCoX%2Bg%2B4o2oYQXgH7ryMBm%2BIMyfuVQ%2F8uxVeTRs9DDshIa9BjqkAZwyb7vj4QK%2Bb0TPDapXTSMXhxMM9ai69MSA1L1YAwjsCDY6eeie6Y4chOPjnd%2FRidz9Ensz%2FOFswVaiv%2Fn0sMiXvUJCJK7GSrR9dSlqultjUYK2%2Bex80M9N0fQIXyzyCktr4ARyFBGrBO62loCMr2GSguGtbP8jdXyIve8N74KaLP7LQeRqK7dtj7UhY6EFCWRwnqkf74Mv3cvKOwTJwQJ1f0iy&X-Amz-Signature=62bb2b995eb44b69db576cb3afb1c995669fbe5cb05bc92e997a4b7a3435e25f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643ZE7HOE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDC89vB9E2ga0N1mdYiJERZBbPAYZhjnb%2FL2ic%2B0m%2FyXwIhAOJpsYnpb2snpKBNKKnumR9SU%2FsmKRESdSa18h3Ordi2Kv8DCCQQABoMNjM3NDIzMTgzODA1Igw2gzlrMfQuXaex8Lsq3AMSTZ57ZIg4cmZSHUgI58hTPFMtGBEwJeAgc5AQo4oA2FJdiYo%2F9VhSurTptBQtdFk3nChf1wvR8VIut%2FhrUW44AhTNwXEVXaOMFUIhf2I2ziVfNR9u5CBaGfpSXE%2FjygEfbO%2BYqp6O3kpzhQYn6bV1CVce11gJQJpg3Wjtor%2BgOYeIWajX3ArNf7WpUVJqFE10h%2Bov%2FQWfnXBCLdu8RbN2Y%2BR037KMh%2FIw3o43%2FPu7XkO%2FJiw1vcSSCYXSzk3oCtQplCND3r7F9bb9LayhNXImgToZ%2F5cJiQcJ8r3jS6YlJ7mtOuSVVvZeTsgT1Hze1h%2FBQ67fkV9fnJiYKiKPwQEbWeUf4lb6jU0aqXKTnQHzdUmTprTRphTjV7f1u3bi8HboG%2FC8ORZvxFjC5nbjG2l0SO37W1mUCYniRbtCThE1auCcZoGWx4t93v%2BavegOpBpto7s2zBscHYvNRmZLdMAKvgBpLNZ1k96RIKVEBMCqGtOyHsZbpCiB3htfOFuYdF2dceYN3u8mWsO2q%2Bm%2FdgCMI0CvVN%2FDZ6x1RK7OSAgytrC9wrmMqfmiRgvuiwTyqXZz658T8yJVSD8860KV%2FcCoX%2Bg%2B4o2oYQXgH7ryMBm%2BIMyfuVQ%2F8uxVeTRs9DDshIa9BjqkAZwyb7vj4QK%2Bb0TPDapXTSMXhxMM9ai69MSA1L1YAwjsCDY6eeie6Y4chOPjnd%2FRidz9Ensz%2FOFswVaiv%2Fn0sMiXvUJCJK7GSrR9dSlqultjUYK2%2Bex80M9N0fQIXyzyCktr4ARyFBGrBO62loCMr2GSguGtbP8jdXyIve8N74KaLP7LQeRqK7dtj7UhY6EFCWRwnqkf74Mv3cvKOwTJwQJ1f0iy&X-Amz-Signature=b7d16569848efef94707e2ee350cd0b55d250b777c106744f966283962375fec&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643ZE7HOE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDC89vB9E2ga0N1mdYiJERZBbPAYZhjnb%2FL2ic%2B0m%2FyXwIhAOJpsYnpb2snpKBNKKnumR9SU%2FsmKRESdSa18h3Ordi2Kv8DCCQQABoMNjM3NDIzMTgzODA1Igw2gzlrMfQuXaex8Lsq3AMSTZ57ZIg4cmZSHUgI58hTPFMtGBEwJeAgc5AQo4oA2FJdiYo%2F9VhSurTptBQtdFk3nChf1wvR8VIut%2FhrUW44AhTNwXEVXaOMFUIhf2I2ziVfNR9u5CBaGfpSXE%2FjygEfbO%2BYqp6O3kpzhQYn6bV1CVce11gJQJpg3Wjtor%2BgOYeIWajX3ArNf7WpUVJqFE10h%2Bov%2FQWfnXBCLdu8RbN2Y%2BR037KMh%2FIw3o43%2FPu7XkO%2FJiw1vcSSCYXSzk3oCtQplCND3r7F9bb9LayhNXImgToZ%2F5cJiQcJ8r3jS6YlJ7mtOuSVVvZeTsgT1Hze1h%2FBQ67fkV9fnJiYKiKPwQEbWeUf4lb6jU0aqXKTnQHzdUmTprTRphTjV7f1u3bi8HboG%2FC8ORZvxFjC5nbjG2l0SO37W1mUCYniRbtCThE1auCcZoGWx4t93v%2BavegOpBpto7s2zBscHYvNRmZLdMAKvgBpLNZ1k96RIKVEBMCqGtOyHsZbpCiB3htfOFuYdF2dceYN3u8mWsO2q%2Bm%2FdgCMI0CvVN%2FDZ6x1RK7OSAgytrC9wrmMqfmiRgvuiwTyqXZz658T8yJVSD8860KV%2FcCoX%2Bg%2B4o2oYQXgH7ryMBm%2BIMyfuVQ%2F8uxVeTRs9DDshIa9BjqkAZwyb7vj4QK%2Bb0TPDapXTSMXhxMM9ai69MSA1L1YAwjsCDY6eeie6Y4chOPjnd%2FRidz9Ensz%2FOFswVaiv%2Fn0sMiXvUJCJK7GSrR9dSlqultjUYK2%2Bex80M9N0fQIXyzyCktr4ARyFBGrBO62loCMr2GSguGtbP8jdXyIve8N74KaLP7LQeRqK7dtj7UhY6EFCWRwnqkf74Mv3cvKOwTJwQJ1f0iy&X-Amz-Signature=83b8ccc0b0e039babfffe94de06d21860e879fae6e40c4e1808b26474e0e6caa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AJA5NNS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDUL6csQV9r8OVNeMXmzYJuEngvDf%2FVHNjEN%2FBYonvepwIhAIeWV7toe%2Bf0GDWUrGLccSr%2FO4BVa3DePMwUr3DOoo5kKv8DCCQQABoMNjM3NDIzMTgzODA1IgxuJtyyoQFY5kkN4v8q3AOp%2FFZD0qAfuiELnz5OZlWaLhoNu5DbJZigQccBIeHb%2F5%2FzUdyHnCt%2FY31xkWwdYov4rLqeEza3gkZg%2FDEzMvhjzy1MjxvqYeGXbYTsJT7WexGRqfk1V94VrMDdJGEKznELkb2cEXcyj0zJCshNyx%2BBOMCIig%2B1PZdqjK5MRkZLzBgLmq1ghtzy6eOfjpzVsuOE4Oa%2FZ7II97eNGgcP%2FI8ej6h44Wl1AnYq94%2FFupBVE8rWkfWFNe0PKMRwR30U5Ttorf6q5b3JCGMlPqG9dafO6SDXUTEFCxvdWlyimIZa2DACcnzKp6%2BugH23M1eTEZ7zmkwLKCflq7DbDLIqH7Ku9cpfCug5El%2FfIipmpSrs9IrhAJlPccnC%2Fkzm8cIg7jLprOTDroAu%2Bqn6pd068XX7%2FBpUWwov1x8lVgvz4lUzTczqdVAWq%2BMSXXDP9JqRMcfRPRW%2F61%2FTwCMh0uGLDnjUXuzoVn6I1Bx2vk8Fs5T44ChXoSCvy1BfR0on9AfdPT3Z0aQcGcVZthXOoGccCjRp9xJDXVZITGdAj4tlVtwGyQFB2EKNAKygQ6aBjy8GkunK4Gd7uvP%2B6MMZevBr8%2FT01I8uHVwQVdK%2BdHpoIrcZ2aLH2sCPPnNwPiCe7TDjhIa9BjqkAeIPFNVTcbvEyxxEasHrY6saNsenxi9OIArtX1DfZtXUo%2F8z9cbvHfSsdXKGfsLrbAyp5GlRwD2SbDXMw9sFWXD458deupY5Oa1Hr46g4zTtEU1N1QCyvK21yAJS%2BDgYHDW7zEyNyieez%2BetGw1eYyaZhszPANWOL3%2BHnRPE4lJmipxKYg14IzSwkEBcSDeUwDmw8liC%2BbmtV8pIUwzYAr6P0f%2Fw&X-Amz-Signature=fa309e00f75245f98c79a5817ded98f0d7068e8772e029ee379bfbec1a2b9885&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AJA5NNS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDUL6csQV9r8OVNeMXmzYJuEngvDf%2FVHNjEN%2FBYonvepwIhAIeWV7toe%2Bf0GDWUrGLccSr%2FO4BVa3DePMwUr3DOoo5kKv8DCCQQABoMNjM3NDIzMTgzODA1IgxuJtyyoQFY5kkN4v8q3AOp%2FFZD0qAfuiELnz5OZlWaLhoNu5DbJZigQccBIeHb%2F5%2FzUdyHnCt%2FY31xkWwdYov4rLqeEza3gkZg%2FDEzMvhjzy1MjxvqYeGXbYTsJT7WexGRqfk1V94VrMDdJGEKznELkb2cEXcyj0zJCshNyx%2BBOMCIig%2B1PZdqjK5MRkZLzBgLmq1ghtzy6eOfjpzVsuOE4Oa%2FZ7II97eNGgcP%2FI8ej6h44Wl1AnYq94%2FFupBVE8rWkfWFNe0PKMRwR30U5Ttorf6q5b3JCGMlPqG9dafO6SDXUTEFCxvdWlyimIZa2DACcnzKp6%2BugH23M1eTEZ7zmkwLKCflq7DbDLIqH7Ku9cpfCug5El%2FfIipmpSrs9IrhAJlPccnC%2Fkzm8cIg7jLprOTDroAu%2Bqn6pd068XX7%2FBpUWwov1x8lVgvz4lUzTczqdVAWq%2BMSXXDP9JqRMcfRPRW%2F61%2FTwCMh0uGLDnjUXuzoVn6I1Bx2vk8Fs5T44ChXoSCvy1BfR0on9AfdPT3Z0aQcGcVZthXOoGccCjRp9xJDXVZITGdAj4tlVtwGyQFB2EKNAKygQ6aBjy8GkunK4Gd7uvP%2B6MMZevBr8%2FT01I8uHVwQVdK%2BdHpoIrcZ2aLH2sCPPnNwPiCe7TDjhIa9BjqkAeIPFNVTcbvEyxxEasHrY6saNsenxi9OIArtX1DfZtXUo%2F8z9cbvHfSsdXKGfsLrbAyp5GlRwD2SbDXMw9sFWXD458deupY5Oa1Hr46g4zTtEU1N1QCyvK21yAJS%2BDgYHDW7zEyNyieez%2BetGw1eYyaZhszPANWOL3%2BHnRPE4lJmipxKYg14IzSwkEBcSDeUwDmw8liC%2BbmtV8pIUwzYAr6P0f%2Fw&X-Amz-Signature=0c9904fecf3a67deba6489f6aee6a7b04b97cc510028b38b42f1d442f088e7d9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AJA5NNS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDUL6csQV9r8OVNeMXmzYJuEngvDf%2FVHNjEN%2FBYonvepwIhAIeWV7toe%2Bf0GDWUrGLccSr%2FO4BVa3DePMwUr3DOoo5kKv8DCCQQABoMNjM3NDIzMTgzODA1IgxuJtyyoQFY5kkN4v8q3AOp%2FFZD0qAfuiELnz5OZlWaLhoNu5DbJZigQccBIeHb%2F5%2FzUdyHnCt%2FY31xkWwdYov4rLqeEza3gkZg%2FDEzMvhjzy1MjxvqYeGXbYTsJT7WexGRqfk1V94VrMDdJGEKznELkb2cEXcyj0zJCshNyx%2BBOMCIig%2B1PZdqjK5MRkZLzBgLmq1ghtzy6eOfjpzVsuOE4Oa%2FZ7II97eNGgcP%2FI8ej6h44Wl1AnYq94%2FFupBVE8rWkfWFNe0PKMRwR30U5Ttorf6q5b3JCGMlPqG9dafO6SDXUTEFCxvdWlyimIZa2DACcnzKp6%2BugH23M1eTEZ7zmkwLKCflq7DbDLIqH7Ku9cpfCug5El%2FfIipmpSrs9IrhAJlPccnC%2Fkzm8cIg7jLprOTDroAu%2Bqn6pd068XX7%2FBpUWwov1x8lVgvz4lUzTczqdVAWq%2BMSXXDP9JqRMcfRPRW%2F61%2FTwCMh0uGLDnjUXuzoVn6I1Bx2vk8Fs5T44ChXoSCvy1BfR0on9AfdPT3Z0aQcGcVZthXOoGccCjRp9xJDXVZITGdAj4tlVtwGyQFB2EKNAKygQ6aBjy8GkunK4Gd7uvP%2B6MMZevBr8%2FT01I8uHVwQVdK%2BdHpoIrcZ2aLH2sCPPnNwPiCe7TDjhIa9BjqkAeIPFNVTcbvEyxxEasHrY6saNsenxi9OIArtX1DfZtXUo%2F8z9cbvHfSsdXKGfsLrbAyp5GlRwD2SbDXMw9sFWXD458deupY5Oa1Hr46g4zTtEU1N1QCyvK21yAJS%2BDgYHDW7zEyNyieez%2BetGw1eYyaZhszPANWOL3%2BHnRPE4lJmipxKYg14IzSwkEBcSDeUwDmw8liC%2BbmtV8pIUwzYAr6P0f%2Fw&X-Amz-Signature=5a6e1b32fccc4808966e4121f254d84110827d1c33f1744757ca6cb543d75a9d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AJA5NNS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDUL6csQV9r8OVNeMXmzYJuEngvDf%2FVHNjEN%2FBYonvepwIhAIeWV7toe%2Bf0GDWUrGLccSr%2FO4BVa3DePMwUr3DOoo5kKv8DCCQQABoMNjM3NDIzMTgzODA1IgxuJtyyoQFY5kkN4v8q3AOp%2FFZD0qAfuiELnz5OZlWaLhoNu5DbJZigQccBIeHb%2F5%2FzUdyHnCt%2FY31xkWwdYov4rLqeEza3gkZg%2FDEzMvhjzy1MjxvqYeGXbYTsJT7WexGRqfk1V94VrMDdJGEKznELkb2cEXcyj0zJCshNyx%2BBOMCIig%2B1PZdqjK5MRkZLzBgLmq1ghtzy6eOfjpzVsuOE4Oa%2FZ7II97eNGgcP%2FI8ej6h44Wl1AnYq94%2FFupBVE8rWkfWFNe0PKMRwR30U5Ttorf6q5b3JCGMlPqG9dafO6SDXUTEFCxvdWlyimIZa2DACcnzKp6%2BugH23M1eTEZ7zmkwLKCflq7DbDLIqH7Ku9cpfCug5El%2FfIipmpSrs9IrhAJlPccnC%2Fkzm8cIg7jLprOTDroAu%2Bqn6pd068XX7%2FBpUWwov1x8lVgvz4lUzTczqdVAWq%2BMSXXDP9JqRMcfRPRW%2F61%2FTwCMh0uGLDnjUXuzoVn6I1Bx2vk8Fs5T44ChXoSCvy1BfR0on9AfdPT3Z0aQcGcVZthXOoGccCjRp9xJDXVZITGdAj4tlVtwGyQFB2EKNAKygQ6aBjy8GkunK4Gd7uvP%2B6MMZevBr8%2FT01I8uHVwQVdK%2BdHpoIrcZ2aLH2sCPPnNwPiCe7TDjhIa9BjqkAeIPFNVTcbvEyxxEasHrY6saNsenxi9OIArtX1DfZtXUo%2F8z9cbvHfSsdXKGfsLrbAyp5GlRwD2SbDXMw9sFWXD458deupY5Oa1Hr46g4zTtEU1N1QCyvK21yAJS%2BDgYHDW7zEyNyieez%2BetGw1eYyaZhszPANWOL3%2BHnRPE4lJmipxKYg14IzSwkEBcSDeUwDmw8liC%2BbmtV8pIUwzYAr6P0f%2Fw&X-Amz-Signature=a0a5a7c4ce68dc1d37715e72aa22ba663c49b48e42c78c45ed6fee9995a243ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AJA5NNS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQDUL6csQV9r8OVNeMXmzYJuEngvDf%2FVHNjEN%2FBYonvepwIhAIeWV7toe%2Bf0GDWUrGLccSr%2FO4BVa3DePMwUr3DOoo5kKv8DCCQQABoMNjM3NDIzMTgzODA1IgxuJtyyoQFY5kkN4v8q3AOp%2FFZD0qAfuiELnz5OZlWaLhoNu5DbJZigQccBIeHb%2F5%2FzUdyHnCt%2FY31xkWwdYov4rLqeEza3gkZg%2FDEzMvhjzy1MjxvqYeGXbYTsJT7WexGRqfk1V94VrMDdJGEKznELkb2cEXcyj0zJCshNyx%2BBOMCIig%2B1PZdqjK5MRkZLzBgLmq1ghtzy6eOfjpzVsuOE4Oa%2FZ7II97eNGgcP%2FI8ej6h44Wl1AnYq94%2FFupBVE8rWkfWFNe0PKMRwR30U5Ttorf6q5b3JCGMlPqG9dafO6SDXUTEFCxvdWlyimIZa2DACcnzKp6%2BugH23M1eTEZ7zmkwLKCflq7DbDLIqH7Ku9cpfCug5El%2FfIipmpSrs9IrhAJlPccnC%2Fkzm8cIg7jLprOTDroAu%2Bqn6pd068XX7%2FBpUWwov1x8lVgvz4lUzTczqdVAWq%2BMSXXDP9JqRMcfRPRW%2F61%2FTwCMh0uGLDnjUXuzoVn6I1Bx2vk8Fs5T44ChXoSCvy1BfR0on9AfdPT3Z0aQcGcVZthXOoGccCjRp9xJDXVZITGdAj4tlVtwGyQFB2EKNAKygQ6aBjy8GkunK4Gd7uvP%2B6MMZevBr8%2FT01I8uHVwQVdK%2BdHpoIrcZ2aLH2sCPPnNwPiCe7TDjhIa9BjqkAeIPFNVTcbvEyxxEasHrY6saNsenxi9OIArtX1DfZtXUo%2F8z9cbvHfSsdXKGfsLrbAyp5GlRwD2SbDXMw9sFWXD458deupY5Oa1Hr46g4zTtEU1N1QCyvK21yAJS%2BDgYHDW7zEyNyieez%2BetGw1eYyaZhszPANWOL3%2BHnRPE4lJmipxKYg14IzSwkEBcSDeUwDmw8liC%2BbmtV8pIUwzYAr6P0f%2Fw&X-Amz-Signature=af582d0c3504a21c300163fddf1bf15985328661b0ffc82f0501005803c599fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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


