

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBCEHVNQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0%2Fdwj9acUxmswDjCTzukXGYvx4Kt18UPXEmX3YqnNqwIhAIHUtTswI6OXB7lr1aNpjfFVOYDicFZuSw5EM0%2BeMS%2FLKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj4C7BQh3eNPARGRQq3AOkvEg3GZ7Z1m5qd%2BW%2FSV6Ix17%2BOiuGu%2B6Y9nh7bGoWul%2FnEP8UJ7XrJ1u9ETbP9wbjWtCkxYcHpuIUoi%2BhniDCFz%2B5GyuprpJcWed8qYrpcqVHdmEac8KteqjnonpYrgF1Q29%2F9lqwnTSRRO2CrgkN5bUd2XATfEiOd7bywD%2BfGg97ylFfSwg6Ay9CgHim9QyBG%2B4pQy2wPkEehrPV70bJaypWenTQB8DPI4sUT0pXWZvo1ddwZqk6KKNDCsrjYh2FA7HzrkrHOtq6J3HIjViOAokPaU9MdhFj%2Bu4fEbh5mhn0CkzIgqbXfgA34Vxiadjnp8Z1f%2BZRRV0Qa3E9cBKAiWrzbkH1R2xNAZSYzJH3b08vZ10fS23ryehVYBdImF0EFW9hFXsmLOdNJs7dBt%2FFd0oe7QaM75qjLt1%2FIiOEgj1Q4LpykT5QZDbRF1bwrieLsbXofNQaLls8858gmh8Mm9bVyhPfFM1v4fR9Lux4Csk9EzcFCsE6P5Z%2BWog7VUWFfhulx0ulRmm9rnLixjGDDtBHUDrEigsD4olEIRFmbINxYgBHVUyP%2F2vBv3Q4E8ai5MCD5CjthzPnexEBELi2F%2FHcUsYA36Bx353%2FQlPv%2FzcQqfYEUSEeBNNIMjDZ4fu8BjqkAXoyuebb3YumbLiYBak9OnyB7Ah7MfYybpO7qREhTJ6NgFdja4XYdUj5tCn3WDwlb4Hq4HfEY9bQyqBEZyoZOFqu%2BWrXdlxgHLxYgNA%2Fp4Uax9uks6lFJ1ZULfCqFHrvxpF%2FQHzLU5enkbJOh2jN%2FPEMSkRbLYurtcPNZTf29nC3DEFcb5aocT%2BP0I1bvcKHDHoaO5dfCMKG9kCr5oCcLi2xsn5D&X-Amz-Signature=0ebc3e6c8e86a132ba4d46370b0202b7ed993b42b0cac591731782761724365e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFTWVLYL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbIjvxmJNSP6kbD8P01Jb1Zd4S1DjZEyiJrCiWxgFidAiEA1AW98tCynSmG3fxBEhGzJd1pSdj0D3IFkjMi2DtlBWkqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOrc5bhy%2FmFV%2Bc%2F9fSrcA9Nx39lJHpngeu3x0mMznRGDo%2B6EkJBs7ipOWGa3bicX2WtiZa3kcT2V3Qnp2tQV0jIPcYmK1ly4vnJud71UHv1f6gCjrHio%2FgLJ%2FHATiK4%2BI17uXj0UuVswmHjjix2A%2B0qYPSpVDJaMaF3N7DuCdXRCiPbUb0wkojQzuZbbfuUVdApPRZ1EzBjgicW44Q%2F80qsmFgi%2Bk6UUU%2FenOHYICQORR5%2BxxdCbz1pxA9ERmYKm52kI6%2F%2BNsagVKHZ8V4OsdHeY41tXmdk8koKH82tPoh%2BoR69dR9q4a4VBjqNnOvATEnCky1LUqLRhbhXoaLwrlbt8yVzsX8%2BdyhLSZcACr7KNNnNkES2%2FK%2FOb7hSBqxNLK4PKfAuDsi0AmZ6ZcTgduDWTny9PcAvF7XMld3ESMxBMooU72fzjfK1fK%2FRJpaS7LC8E4i3WXgqlO4zD7Opt2juTnmI5OgIDlJCD%2FCQRgChwBb6JuBoCooeGuqusk4nMf8SnHuFmgtS11Xw4B6vUj3nhSfbxyDpOl1uU433LzHBYmbTfBsDphd5ves4b4aVyipacJ67FtsrCrn9DOjr8RKbnld3IDap76fEluxGiSqFu2ohg1SJOOfMQzRmDKQnf1P2fBFfheRyPIgIKMNDh%2B7wGOqUBOb4ZFrIOsnWEUrN8AALLhuL4fFQvp7zKGld5IkvzH8XBIQ0dC8tY6Cg3ybwUmmdxoF6Qkf%2BcQh1qD5jsnDgAIG649Gyp9ovp6oyyHyKrd0nZc5ZGlaa5OUnBw%2Bqcn5ozMQZ%2FAqEhzoASMQxPkSBNOKYz20TeCy7fXKGAeReSeBPFrgt4oDX530ZyfC2%2FtI4t0YSYZs%2Br9%2Fz3Esb56tcrLG3n5e0G&X-Amz-Signature=390778fb2bb4334219ec1eff32e1272aebe3fb51802a16f3961365bca10eb510&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFTWVLYL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbIjvxmJNSP6kbD8P01Jb1Zd4S1DjZEyiJrCiWxgFidAiEA1AW98tCynSmG3fxBEhGzJd1pSdj0D3IFkjMi2DtlBWkqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOrc5bhy%2FmFV%2Bc%2F9fSrcA9Nx39lJHpngeu3x0mMznRGDo%2B6EkJBs7ipOWGa3bicX2WtiZa3kcT2V3Qnp2tQV0jIPcYmK1ly4vnJud71UHv1f6gCjrHio%2FgLJ%2FHATiK4%2BI17uXj0UuVswmHjjix2A%2B0qYPSpVDJaMaF3N7DuCdXRCiPbUb0wkojQzuZbbfuUVdApPRZ1EzBjgicW44Q%2F80qsmFgi%2Bk6UUU%2FenOHYICQORR5%2BxxdCbz1pxA9ERmYKm52kI6%2F%2BNsagVKHZ8V4OsdHeY41tXmdk8koKH82tPoh%2BoR69dR9q4a4VBjqNnOvATEnCky1LUqLRhbhXoaLwrlbt8yVzsX8%2BdyhLSZcACr7KNNnNkES2%2FK%2FOb7hSBqxNLK4PKfAuDsi0AmZ6ZcTgduDWTny9PcAvF7XMld3ESMxBMooU72fzjfK1fK%2FRJpaS7LC8E4i3WXgqlO4zD7Opt2juTnmI5OgIDlJCD%2FCQRgChwBb6JuBoCooeGuqusk4nMf8SnHuFmgtS11Xw4B6vUj3nhSfbxyDpOl1uU433LzHBYmbTfBsDphd5ves4b4aVyipacJ67FtsrCrn9DOjr8RKbnld3IDap76fEluxGiSqFu2ohg1SJOOfMQzRmDKQnf1P2fBFfheRyPIgIKMNDh%2B7wGOqUBOb4ZFrIOsnWEUrN8AALLhuL4fFQvp7zKGld5IkvzH8XBIQ0dC8tY6Cg3ybwUmmdxoF6Qkf%2BcQh1qD5jsnDgAIG649Gyp9ovp6oyyHyKrd0nZc5ZGlaa5OUnBw%2Bqcn5ozMQZ%2FAqEhzoASMQxPkSBNOKYz20TeCy7fXKGAeReSeBPFrgt4oDX530ZyfC2%2FtI4t0YSYZs%2Br9%2Fz3Esb56tcrLG3n5e0G&X-Amz-Signature=bc72f9a2cff8ad8196c82d5c175f9d94f19101a7d141639321b2e514ab619aea&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFTWVLYL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbIjvxmJNSP6kbD8P01Jb1Zd4S1DjZEyiJrCiWxgFidAiEA1AW98tCynSmG3fxBEhGzJd1pSdj0D3IFkjMi2DtlBWkqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOrc5bhy%2FmFV%2Bc%2F9fSrcA9Nx39lJHpngeu3x0mMznRGDo%2B6EkJBs7ipOWGa3bicX2WtiZa3kcT2V3Qnp2tQV0jIPcYmK1ly4vnJud71UHv1f6gCjrHio%2FgLJ%2FHATiK4%2BI17uXj0UuVswmHjjix2A%2B0qYPSpVDJaMaF3N7DuCdXRCiPbUb0wkojQzuZbbfuUVdApPRZ1EzBjgicW44Q%2F80qsmFgi%2Bk6UUU%2FenOHYICQORR5%2BxxdCbz1pxA9ERmYKm52kI6%2F%2BNsagVKHZ8V4OsdHeY41tXmdk8koKH82tPoh%2BoR69dR9q4a4VBjqNnOvATEnCky1LUqLRhbhXoaLwrlbt8yVzsX8%2BdyhLSZcACr7KNNnNkES2%2FK%2FOb7hSBqxNLK4PKfAuDsi0AmZ6ZcTgduDWTny9PcAvF7XMld3ESMxBMooU72fzjfK1fK%2FRJpaS7LC8E4i3WXgqlO4zD7Opt2juTnmI5OgIDlJCD%2FCQRgChwBb6JuBoCooeGuqusk4nMf8SnHuFmgtS11Xw4B6vUj3nhSfbxyDpOl1uU433LzHBYmbTfBsDphd5ves4b4aVyipacJ67FtsrCrn9DOjr8RKbnld3IDap76fEluxGiSqFu2ohg1SJOOfMQzRmDKQnf1P2fBFfheRyPIgIKMNDh%2B7wGOqUBOb4ZFrIOsnWEUrN8AALLhuL4fFQvp7zKGld5IkvzH8XBIQ0dC8tY6Cg3ybwUmmdxoF6Qkf%2BcQh1qD5jsnDgAIG649Gyp9ovp6oyyHyKrd0nZc5ZGlaa5OUnBw%2Bqcn5ozMQZ%2FAqEhzoASMQxPkSBNOKYz20TeCy7fXKGAeReSeBPFrgt4oDX530ZyfC2%2FtI4t0YSYZs%2Br9%2Fz3Esb56tcrLG3n5e0G&X-Amz-Signature=823eaf1dbe1318d374e8030566966d309a6326e0776910ec60609341dbd05a99&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFTWVLYL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbIjvxmJNSP6kbD8P01Jb1Zd4S1DjZEyiJrCiWxgFidAiEA1AW98tCynSmG3fxBEhGzJd1pSdj0D3IFkjMi2DtlBWkqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOrc5bhy%2FmFV%2Bc%2F9fSrcA9Nx39lJHpngeu3x0mMznRGDo%2B6EkJBs7ipOWGa3bicX2WtiZa3kcT2V3Qnp2tQV0jIPcYmK1ly4vnJud71UHv1f6gCjrHio%2FgLJ%2FHATiK4%2BI17uXj0UuVswmHjjix2A%2B0qYPSpVDJaMaF3N7DuCdXRCiPbUb0wkojQzuZbbfuUVdApPRZ1EzBjgicW44Q%2F80qsmFgi%2Bk6UUU%2FenOHYICQORR5%2BxxdCbz1pxA9ERmYKm52kI6%2F%2BNsagVKHZ8V4OsdHeY41tXmdk8koKH82tPoh%2BoR69dR9q4a4VBjqNnOvATEnCky1LUqLRhbhXoaLwrlbt8yVzsX8%2BdyhLSZcACr7KNNnNkES2%2FK%2FOb7hSBqxNLK4PKfAuDsi0AmZ6ZcTgduDWTny9PcAvF7XMld3ESMxBMooU72fzjfK1fK%2FRJpaS7LC8E4i3WXgqlO4zD7Opt2juTnmI5OgIDlJCD%2FCQRgChwBb6JuBoCooeGuqusk4nMf8SnHuFmgtS11Xw4B6vUj3nhSfbxyDpOl1uU433LzHBYmbTfBsDphd5ves4b4aVyipacJ67FtsrCrn9DOjr8RKbnld3IDap76fEluxGiSqFu2ohg1SJOOfMQzRmDKQnf1P2fBFfheRyPIgIKMNDh%2B7wGOqUBOb4ZFrIOsnWEUrN8AALLhuL4fFQvp7zKGld5IkvzH8XBIQ0dC8tY6Cg3ybwUmmdxoF6Qkf%2BcQh1qD5jsnDgAIG649Gyp9ovp6oyyHyKrd0nZc5ZGlaa5OUnBw%2Bqcn5ozMQZ%2FAqEhzoASMQxPkSBNOKYz20TeCy7fXKGAeReSeBPFrgt4oDX530ZyfC2%2FtI4t0YSYZs%2Br9%2Fz3Esb56tcrLG3n5e0G&X-Amz-Signature=cf8e63c142f98d64bf8a5f4446922a7b004ceaf0450db2ac45c9ae8b7596973e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFTWVLYL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbIjvxmJNSP6kbD8P01Jb1Zd4S1DjZEyiJrCiWxgFidAiEA1AW98tCynSmG3fxBEhGzJd1pSdj0D3IFkjMi2DtlBWkqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOrc5bhy%2FmFV%2Bc%2F9fSrcA9Nx39lJHpngeu3x0mMznRGDo%2B6EkJBs7ipOWGa3bicX2WtiZa3kcT2V3Qnp2tQV0jIPcYmK1ly4vnJud71UHv1f6gCjrHio%2FgLJ%2FHATiK4%2BI17uXj0UuVswmHjjix2A%2B0qYPSpVDJaMaF3N7DuCdXRCiPbUb0wkojQzuZbbfuUVdApPRZ1EzBjgicW44Q%2F80qsmFgi%2Bk6UUU%2FenOHYICQORR5%2BxxdCbz1pxA9ERmYKm52kI6%2F%2BNsagVKHZ8V4OsdHeY41tXmdk8koKH82tPoh%2BoR69dR9q4a4VBjqNnOvATEnCky1LUqLRhbhXoaLwrlbt8yVzsX8%2BdyhLSZcACr7KNNnNkES2%2FK%2FOb7hSBqxNLK4PKfAuDsi0AmZ6ZcTgduDWTny9PcAvF7XMld3ESMxBMooU72fzjfK1fK%2FRJpaS7LC8E4i3WXgqlO4zD7Opt2juTnmI5OgIDlJCD%2FCQRgChwBb6JuBoCooeGuqusk4nMf8SnHuFmgtS11Xw4B6vUj3nhSfbxyDpOl1uU433LzHBYmbTfBsDphd5ves4b4aVyipacJ67FtsrCrn9DOjr8RKbnld3IDap76fEluxGiSqFu2ohg1SJOOfMQzRmDKQnf1P2fBFfheRyPIgIKMNDh%2B7wGOqUBOb4ZFrIOsnWEUrN8AALLhuL4fFQvp7zKGld5IkvzH8XBIQ0dC8tY6Cg3ybwUmmdxoF6Qkf%2BcQh1qD5jsnDgAIG649Gyp9ovp6oyyHyKrd0nZc5ZGlaa5OUnBw%2Bqcn5ozMQZ%2FAqEhzoASMQxPkSBNOKYz20TeCy7fXKGAeReSeBPFrgt4oDX530ZyfC2%2FtI4t0YSYZs%2Br9%2Fz3Esb56tcrLG3n5e0G&X-Amz-Signature=d6c8d96b3c5ef42ec252026a03eb9faee750bbb9bae9112c88b650e3bc5fc6d9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBCEHVNQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0%2Fdwj9acUxmswDjCTzukXGYvx4Kt18UPXEmX3YqnNqwIhAIHUtTswI6OXB7lr1aNpjfFVOYDicFZuSw5EM0%2BeMS%2FLKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj4C7BQh3eNPARGRQq3AOkvEg3GZ7Z1m5qd%2BW%2FSV6Ix17%2BOiuGu%2B6Y9nh7bGoWul%2FnEP8UJ7XrJ1u9ETbP9wbjWtCkxYcHpuIUoi%2BhniDCFz%2B5GyuprpJcWed8qYrpcqVHdmEac8KteqjnonpYrgF1Q29%2F9lqwnTSRRO2CrgkN5bUd2XATfEiOd7bywD%2BfGg97ylFfSwg6Ay9CgHim9QyBG%2B4pQy2wPkEehrPV70bJaypWenTQB8DPI4sUT0pXWZvo1ddwZqk6KKNDCsrjYh2FA7HzrkrHOtq6J3HIjViOAokPaU9MdhFj%2Bu4fEbh5mhn0CkzIgqbXfgA34Vxiadjnp8Z1f%2BZRRV0Qa3E9cBKAiWrzbkH1R2xNAZSYzJH3b08vZ10fS23ryehVYBdImF0EFW9hFXsmLOdNJs7dBt%2FFd0oe7QaM75qjLt1%2FIiOEgj1Q4LpykT5QZDbRF1bwrieLsbXofNQaLls8858gmh8Mm9bVyhPfFM1v4fR9Lux4Csk9EzcFCsE6P5Z%2BWog7VUWFfhulx0ulRmm9rnLixjGDDtBHUDrEigsD4olEIRFmbINxYgBHVUyP%2F2vBv3Q4E8ai5MCD5CjthzPnexEBELi2F%2FHcUsYA36Bx353%2FQlPv%2FzcQqfYEUSEeBNNIMjDZ4fu8BjqkAXoyuebb3YumbLiYBak9OnyB7Ah7MfYybpO7qREhTJ6NgFdja4XYdUj5tCn3WDwlb4Hq4HfEY9bQyqBEZyoZOFqu%2BWrXdlxgHLxYgNA%2Fp4Uax9uks6lFJ1ZULfCqFHrvxpF%2FQHzLU5enkbJOh2jN%2FPEMSkRbLYurtcPNZTf29nC3DEFcb5aocT%2BP0I1bvcKHDHoaO5dfCMKG9kCr5oCcLi2xsn5D&X-Amz-Signature=c98ca713a3b68e64b0ec1ae4ceaddff2b7f1775045f3f56d2eec3d84fc80dc53&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBCEHVNQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0%2Fdwj9acUxmswDjCTzukXGYvx4Kt18UPXEmX3YqnNqwIhAIHUtTswI6OXB7lr1aNpjfFVOYDicFZuSw5EM0%2BeMS%2FLKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj4C7BQh3eNPARGRQq3AOkvEg3GZ7Z1m5qd%2BW%2FSV6Ix17%2BOiuGu%2B6Y9nh7bGoWul%2FnEP8UJ7XrJ1u9ETbP9wbjWtCkxYcHpuIUoi%2BhniDCFz%2B5GyuprpJcWed8qYrpcqVHdmEac8KteqjnonpYrgF1Q29%2F9lqwnTSRRO2CrgkN5bUd2XATfEiOd7bywD%2BfGg97ylFfSwg6Ay9CgHim9QyBG%2B4pQy2wPkEehrPV70bJaypWenTQB8DPI4sUT0pXWZvo1ddwZqk6KKNDCsrjYh2FA7HzrkrHOtq6J3HIjViOAokPaU9MdhFj%2Bu4fEbh5mhn0CkzIgqbXfgA34Vxiadjnp8Z1f%2BZRRV0Qa3E9cBKAiWrzbkH1R2xNAZSYzJH3b08vZ10fS23ryehVYBdImF0EFW9hFXsmLOdNJs7dBt%2FFd0oe7QaM75qjLt1%2FIiOEgj1Q4LpykT5QZDbRF1bwrieLsbXofNQaLls8858gmh8Mm9bVyhPfFM1v4fR9Lux4Csk9EzcFCsE6P5Z%2BWog7VUWFfhulx0ulRmm9rnLixjGDDtBHUDrEigsD4olEIRFmbINxYgBHVUyP%2F2vBv3Q4E8ai5MCD5CjthzPnexEBELi2F%2FHcUsYA36Bx353%2FQlPv%2FzcQqfYEUSEeBNNIMjDZ4fu8BjqkAXoyuebb3YumbLiYBak9OnyB7Ah7MfYybpO7qREhTJ6NgFdja4XYdUj5tCn3WDwlb4Hq4HfEY9bQyqBEZyoZOFqu%2BWrXdlxgHLxYgNA%2Fp4Uax9uks6lFJ1ZULfCqFHrvxpF%2FQHzLU5enkbJOh2jN%2FPEMSkRbLYurtcPNZTf29nC3DEFcb5aocT%2BP0I1bvcKHDHoaO5dfCMKG9kCr5oCcLi2xsn5D&X-Amz-Signature=691723a6ded255df877700094c058fed824147df4be9b41da28da50338dc5100&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBCEHVNQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0%2Fdwj9acUxmswDjCTzukXGYvx4Kt18UPXEmX3YqnNqwIhAIHUtTswI6OXB7lr1aNpjfFVOYDicFZuSw5EM0%2BeMS%2FLKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj4C7BQh3eNPARGRQq3AOkvEg3GZ7Z1m5qd%2BW%2FSV6Ix17%2BOiuGu%2B6Y9nh7bGoWul%2FnEP8UJ7XrJ1u9ETbP9wbjWtCkxYcHpuIUoi%2BhniDCFz%2B5GyuprpJcWed8qYrpcqVHdmEac8KteqjnonpYrgF1Q29%2F9lqwnTSRRO2CrgkN5bUd2XATfEiOd7bywD%2BfGg97ylFfSwg6Ay9CgHim9QyBG%2B4pQy2wPkEehrPV70bJaypWenTQB8DPI4sUT0pXWZvo1ddwZqk6KKNDCsrjYh2FA7HzrkrHOtq6J3HIjViOAokPaU9MdhFj%2Bu4fEbh5mhn0CkzIgqbXfgA34Vxiadjnp8Z1f%2BZRRV0Qa3E9cBKAiWrzbkH1R2xNAZSYzJH3b08vZ10fS23ryehVYBdImF0EFW9hFXsmLOdNJs7dBt%2FFd0oe7QaM75qjLt1%2FIiOEgj1Q4LpykT5QZDbRF1bwrieLsbXofNQaLls8858gmh8Mm9bVyhPfFM1v4fR9Lux4Csk9EzcFCsE6P5Z%2BWog7VUWFfhulx0ulRmm9rnLixjGDDtBHUDrEigsD4olEIRFmbINxYgBHVUyP%2F2vBv3Q4E8ai5MCD5CjthzPnexEBELi2F%2FHcUsYA36Bx353%2FQlPv%2FzcQqfYEUSEeBNNIMjDZ4fu8BjqkAXoyuebb3YumbLiYBak9OnyB7Ah7MfYybpO7qREhTJ6NgFdja4XYdUj5tCn3WDwlb4Hq4HfEY9bQyqBEZyoZOFqu%2BWrXdlxgHLxYgNA%2Fp4Uax9uks6lFJ1ZULfCqFHrvxpF%2FQHzLU5enkbJOh2jN%2FPEMSkRbLYurtcPNZTf29nC3DEFcb5aocT%2BP0I1bvcKHDHoaO5dfCMKG9kCr5oCcLi2xsn5D&X-Amz-Signature=1cf9098edcd7bbf2ad424297e90392729cd94da88d45937bb286d63233699185&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBCEHVNQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0%2Fdwj9acUxmswDjCTzukXGYvx4Kt18UPXEmX3YqnNqwIhAIHUtTswI6OXB7lr1aNpjfFVOYDicFZuSw5EM0%2BeMS%2FLKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj4C7BQh3eNPARGRQq3AOkvEg3GZ7Z1m5qd%2BW%2FSV6Ix17%2BOiuGu%2B6Y9nh7bGoWul%2FnEP8UJ7XrJ1u9ETbP9wbjWtCkxYcHpuIUoi%2BhniDCFz%2B5GyuprpJcWed8qYrpcqVHdmEac8KteqjnonpYrgF1Q29%2F9lqwnTSRRO2CrgkN5bUd2XATfEiOd7bywD%2BfGg97ylFfSwg6Ay9CgHim9QyBG%2B4pQy2wPkEehrPV70bJaypWenTQB8DPI4sUT0pXWZvo1ddwZqk6KKNDCsrjYh2FA7HzrkrHOtq6J3HIjViOAokPaU9MdhFj%2Bu4fEbh5mhn0CkzIgqbXfgA34Vxiadjnp8Z1f%2BZRRV0Qa3E9cBKAiWrzbkH1R2xNAZSYzJH3b08vZ10fS23ryehVYBdImF0EFW9hFXsmLOdNJs7dBt%2FFd0oe7QaM75qjLt1%2FIiOEgj1Q4LpykT5QZDbRF1bwrieLsbXofNQaLls8858gmh8Mm9bVyhPfFM1v4fR9Lux4Csk9EzcFCsE6P5Z%2BWog7VUWFfhulx0ulRmm9rnLixjGDDtBHUDrEigsD4olEIRFmbINxYgBHVUyP%2F2vBv3Q4E8ai5MCD5CjthzPnexEBELi2F%2FHcUsYA36Bx353%2FQlPv%2FzcQqfYEUSEeBNNIMjDZ4fu8BjqkAXoyuebb3YumbLiYBak9OnyB7Ah7MfYybpO7qREhTJ6NgFdja4XYdUj5tCn3WDwlb4Hq4HfEY9bQyqBEZyoZOFqu%2BWrXdlxgHLxYgNA%2Fp4Uax9uks6lFJ1ZULfCqFHrvxpF%2FQHzLU5enkbJOh2jN%2FPEMSkRbLYurtcPNZTf29nC3DEFcb5aocT%2BP0I1bvcKHDHoaO5dfCMKG9kCr5oCcLi2xsn5D&X-Amz-Signature=8860f772fb8d60806174eb579b86baf71959077551720924ab16dc05e7845454&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBCEHVNQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0%2Fdwj9acUxmswDjCTzukXGYvx4Kt18UPXEmX3YqnNqwIhAIHUtTswI6OXB7lr1aNpjfFVOYDicFZuSw5EM0%2BeMS%2FLKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj4C7BQh3eNPARGRQq3AOkvEg3GZ7Z1m5qd%2BW%2FSV6Ix17%2BOiuGu%2B6Y9nh7bGoWul%2FnEP8UJ7XrJ1u9ETbP9wbjWtCkxYcHpuIUoi%2BhniDCFz%2B5GyuprpJcWed8qYrpcqVHdmEac8KteqjnonpYrgF1Q29%2F9lqwnTSRRO2CrgkN5bUd2XATfEiOd7bywD%2BfGg97ylFfSwg6Ay9CgHim9QyBG%2B4pQy2wPkEehrPV70bJaypWenTQB8DPI4sUT0pXWZvo1ddwZqk6KKNDCsrjYh2FA7HzrkrHOtq6J3HIjViOAokPaU9MdhFj%2Bu4fEbh5mhn0CkzIgqbXfgA34Vxiadjnp8Z1f%2BZRRV0Qa3E9cBKAiWrzbkH1R2xNAZSYzJH3b08vZ10fS23ryehVYBdImF0EFW9hFXsmLOdNJs7dBt%2FFd0oe7QaM75qjLt1%2FIiOEgj1Q4LpykT5QZDbRF1bwrieLsbXofNQaLls8858gmh8Mm9bVyhPfFM1v4fR9Lux4Csk9EzcFCsE6P5Z%2BWog7VUWFfhulx0ulRmm9rnLixjGDDtBHUDrEigsD4olEIRFmbINxYgBHVUyP%2F2vBv3Q4E8ai5MCD5CjthzPnexEBELi2F%2FHcUsYA36Bx353%2FQlPv%2FzcQqfYEUSEeBNNIMjDZ4fu8BjqkAXoyuebb3YumbLiYBak9OnyB7Ah7MfYybpO7qREhTJ6NgFdja4XYdUj5tCn3WDwlb4Hq4HfEY9bQyqBEZyoZOFqu%2BWrXdlxgHLxYgNA%2Fp4Uax9uks6lFJ1ZULfCqFHrvxpF%2FQHzLU5enkbJOh2jN%2FPEMSkRbLYurtcPNZTf29nC3DEFcb5aocT%2BP0I1bvcKHDHoaO5dfCMKG9kCr5oCcLi2xsn5D&X-Amz-Signature=eeaf39a35b42998bdede672779f7d8b3a20e0c7d3622b648025a0f433840c7cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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


