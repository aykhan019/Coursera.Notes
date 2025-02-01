

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F2WOOEP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDstMjoZghSwCONpYMv1UFZnrfjoMiH6dqcnMxpVOlkGAiBHmphukL6DEOR7wWTt9AyqIz5YibdtylRYmv09mfq7vyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYEkQL%2FGuQF50hXJFKtwD62G%2FAggDu%2FOFPspkzcir7q%2BARn%2Flec%2FFMJ7Jepwu%2Fh%2BiTxGIfgDgsi%2FrfclCZ6uWyafavRZVa0bW19mQg26EfF5hNji0y99ILR2XATeyPROqucg6fFqd4hKN2PnsKC1vLu6TEwc6NMxY40hDxVlBUbTiK8J0YVGKZltNnnPOOGyNPyqb1APuCQh7bT5P%2Bkg4ySmqC0Y84snvD2dXII%2FGPIsgD7O2Q0vgFedWVqexSDZwd7eGPuF1dF6gs0PwKg6OfRosL5K76luJRFo%2FfZYhCY41YX0Oh3IhP3DgHVgDgiZg7TYCD4MFyWKi%2FCzxm5mOrg%2FOTS8MzLRBZANdYD8ppq%2FpXKmwiqZktSmGvxIMajGqMJEABOEDCtlZGFAZjqSPCeDFS%2BceAjsQeuLPaQ6Enkb9S3IZKg0%2B4S6MQT9Cfqy%2Bib5eiF42yqBNX5yOLDyMOV3kzajdFTLxP5AI7MMXC9TtycRe1KlMhBUTEp6NvQHEWJz55NFiYOdJKPryoG3hT12S38CwgybL2tmBHNr7MdGLwrZ2BQzz4vP%2F5YeQEU%2FW%2B%2BHr%2BZpW1I3rCAPZrxd3mUPEDypxRO1vW%2BYdJaqSpJ5Qisxjg9Yw6g1%2Fk4XG7j0yNk3svarLUjbdyoEwzcX4vAY6pgFfpBxM7m1SAJxrtgJEnbK9GhccRh9SY0J%2BBn5%2BP4j6jQhoYbLimkY1ZNE4TcTkDFWxSe3HaZJPUmJAF8UZTK2LyxQbKGKZWh6mlr4%2FD81cPDzC9r%2F1o5NB6W1Jhs9D%2FdmXoWx1JGvl42eY%2BDZFu0vaYWrJyz4TWdTdH7avvavbRQ202ZyKAh2Mj5nz8thlv%2FLT2xXrcpX8Lle7C10Yb62h0z1INsvY&X-Amz-Signature=912421791ac49a1e976c31e29459a8bd7bb51c1139d77455fa034ed591492d76&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PH7GYTS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBZXB6bsfp6QHHaeSr0eNYmywxfF9MSBE9dohytI3BW7AiB1G3PnjcPABUCINF9CIDrwA59QrH5hbgDU2280eh6oiyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLQaMLS2vhoh9BlS2KtwDP4RmI9nS0UhYeKPvKSK1pzsn%2FtxHAEcx1TGMryqPlfl%2BHQJvxxIbsBfFr9cvjyBt8rR3aWa7WQMM4g4exLk13QjPpSBQ0cqSzf5Tu%2FBXl2nU1P62LiCq2Lgq3lPRJ%2F1tXQ7bQveRa4Qq34%2BSXhxTkCNYqDwjcGUmlTheWJm96oHW8OnwqVqX8svj%2FKk9D6sKArPxzm0kzt9k7El5LM8a%2BYfoTMDWaw6%2F6ovfhMYjUW4YwW3hCZxLxB0AP9i8Vk%2BnnEZJy%2Fi%2FWmufRGjH9EQC69wowhmM69cv6dKEHPQk3pBeiOSeoSwYfbjl8fWdxPi0oYmoGtIlim8Sadjr6DSuu1TDtAl%2BwxRwW7AqH6TJbjKm%2BE5KxMOnZGc1Tj6gzMDwVSQUBfq7vdOK7EYzs1%2Fakdve%2BEv45nAobOKuzh5AF0sic%2Bhn%2FUXkWojtkHKoCe%2FViY9OyhMcogVfdB1X40tFmrb%2FfBRZHgJkcisIeizLs4AFFbu%2FW3xztPnIkuvBYTGAQPACvKFCoO9%2FqFvmHAkCDbYc6bYZ2nNuBrCvllFcNr7wArBNmTSd%2BawUUZLf3ry0awLMTwqrh5qR48W1mrJZogCZJa%2Bmm2dvslF1fq1%2Bp9KFcaUoHbcLWoB8SiEww8r4vAY6pgEW2gIExSPf4KG1ckfWBKugdux0XhOwG9a%2BkFz1215ivewBCkkmWLDRkh%2FyhFU4yyOAl4fUtl73%2FaXyePLdz%2FIO2iSrhHIwph5nzcrSLDSfKFXfUmIiGGsSQx%2FNMyfGLXTBx0PzE%2BAn5LDrO4RP%2BkbSP35gimZ6XblK2CIGXjJ6Q7QBnUKFcNDdIgRFoCqhKkhZL5qH6ee4QgcUeyZXexeSaxeKHcdA&X-Amz-Signature=9e88289a7379392bd51054312d25c8f1d875a6b336ce2e090b0d66c0847f06fd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PH7GYTS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBZXB6bsfp6QHHaeSr0eNYmywxfF9MSBE9dohytI3BW7AiB1G3PnjcPABUCINF9CIDrwA59QrH5hbgDU2280eh6oiyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLQaMLS2vhoh9BlS2KtwDP4RmI9nS0UhYeKPvKSK1pzsn%2FtxHAEcx1TGMryqPlfl%2BHQJvxxIbsBfFr9cvjyBt8rR3aWa7WQMM4g4exLk13QjPpSBQ0cqSzf5Tu%2FBXl2nU1P62LiCq2Lgq3lPRJ%2F1tXQ7bQveRa4Qq34%2BSXhxTkCNYqDwjcGUmlTheWJm96oHW8OnwqVqX8svj%2FKk9D6sKArPxzm0kzt9k7El5LM8a%2BYfoTMDWaw6%2F6ovfhMYjUW4YwW3hCZxLxB0AP9i8Vk%2BnnEZJy%2Fi%2FWmufRGjH9EQC69wowhmM69cv6dKEHPQk3pBeiOSeoSwYfbjl8fWdxPi0oYmoGtIlim8Sadjr6DSuu1TDtAl%2BwxRwW7AqH6TJbjKm%2BE5KxMOnZGc1Tj6gzMDwVSQUBfq7vdOK7EYzs1%2Fakdve%2BEv45nAobOKuzh5AF0sic%2Bhn%2FUXkWojtkHKoCe%2FViY9OyhMcogVfdB1X40tFmrb%2FfBRZHgJkcisIeizLs4AFFbu%2FW3xztPnIkuvBYTGAQPACvKFCoO9%2FqFvmHAkCDbYc6bYZ2nNuBrCvllFcNr7wArBNmTSd%2BawUUZLf3ry0awLMTwqrh5qR48W1mrJZogCZJa%2Bmm2dvslF1fq1%2Bp9KFcaUoHbcLWoB8SiEww8r4vAY6pgEW2gIExSPf4KG1ckfWBKugdux0XhOwG9a%2BkFz1215ivewBCkkmWLDRkh%2FyhFU4yyOAl4fUtl73%2FaXyePLdz%2FIO2iSrhHIwph5nzcrSLDSfKFXfUmIiGGsSQx%2FNMyfGLXTBx0PzE%2BAn5LDrO4RP%2BkbSP35gimZ6XblK2CIGXjJ6Q7QBnUKFcNDdIgRFoCqhKkhZL5qH6ee4QgcUeyZXexeSaxeKHcdA&X-Amz-Signature=642c2583a74a86415ebd7248005cb5e2452874ea3d8fed17e1fcdc0ec3cd9622&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PH7GYTS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBZXB6bsfp6QHHaeSr0eNYmywxfF9MSBE9dohytI3BW7AiB1G3PnjcPABUCINF9CIDrwA59QrH5hbgDU2280eh6oiyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLQaMLS2vhoh9BlS2KtwDP4RmI9nS0UhYeKPvKSK1pzsn%2FtxHAEcx1TGMryqPlfl%2BHQJvxxIbsBfFr9cvjyBt8rR3aWa7WQMM4g4exLk13QjPpSBQ0cqSzf5Tu%2FBXl2nU1P62LiCq2Lgq3lPRJ%2F1tXQ7bQveRa4Qq34%2BSXhxTkCNYqDwjcGUmlTheWJm96oHW8OnwqVqX8svj%2FKk9D6sKArPxzm0kzt9k7El5LM8a%2BYfoTMDWaw6%2F6ovfhMYjUW4YwW3hCZxLxB0AP9i8Vk%2BnnEZJy%2Fi%2FWmufRGjH9EQC69wowhmM69cv6dKEHPQk3pBeiOSeoSwYfbjl8fWdxPi0oYmoGtIlim8Sadjr6DSuu1TDtAl%2BwxRwW7AqH6TJbjKm%2BE5KxMOnZGc1Tj6gzMDwVSQUBfq7vdOK7EYzs1%2Fakdve%2BEv45nAobOKuzh5AF0sic%2Bhn%2FUXkWojtkHKoCe%2FViY9OyhMcogVfdB1X40tFmrb%2FfBRZHgJkcisIeizLs4AFFbu%2FW3xztPnIkuvBYTGAQPACvKFCoO9%2FqFvmHAkCDbYc6bYZ2nNuBrCvllFcNr7wArBNmTSd%2BawUUZLf3ry0awLMTwqrh5qR48W1mrJZogCZJa%2Bmm2dvslF1fq1%2Bp9KFcaUoHbcLWoB8SiEww8r4vAY6pgEW2gIExSPf4KG1ckfWBKugdux0XhOwG9a%2BkFz1215ivewBCkkmWLDRkh%2FyhFU4yyOAl4fUtl73%2FaXyePLdz%2FIO2iSrhHIwph5nzcrSLDSfKFXfUmIiGGsSQx%2FNMyfGLXTBx0PzE%2BAn5LDrO4RP%2BkbSP35gimZ6XblK2CIGXjJ6Q7QBnUKFcNDdIgRFoCqhKkhZL5qH6ee4QgcUeyZXexeSaxeKHcdA&X-Amz-Signature=88c1ff2739a515abe02e8b0c94e1f0589053ca2706cdf39e05ec0893880f0b58&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PH7GYTS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBZXB6bsfp6QHHaeSr0eNYmywxfF9MSBE9dohytI3BW7AiB1G3PnjcPABUCINF9CIDrwA59QrH5hbgDU2280eh6oiyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLQaMLS2vhoh9BlS2KtwDP4RmI9nS0UhYeKPvKSK1pzsn%2FtxHAEcx1TGMryqPlfl%2BHQJvxxIbsBfFr9cvjyBt8rR3aWa7WQMM4g4exLk13QjPpSBQ0cqSzf5Tu%2FBXl2nU1P62LiCq2Lgq3lPRJ%2F1tXQ7bQveRa4Qq34%2BSXhxTkCNYqDwjcGUmlTheWJm96oHW8OnwqVqX8svj%2FKk9D6sKArPxzm0kzt9k7El5LM8a%2BYfoTMDWaw6%2F6ovfhMYjUW4YwW3hCZxLxB0AP9i8Vk%2BnnEZJy%2Fi%2FWmufRGjH9EQC69wowhmM69cv6dKEHPQk3pBeiOSeoSwYfbjl8fWdxPi0oYmoGtIlim8Sadjr6DSuu1TDtAl%2BwxRwW7AqH6TJbjKm%2BE5KxMOnZGc1Tj6gzMDwVSQUBfq7vdOK7EYzs1%2Fakdve%2BEv45nAobOKuzh5AF0sic%2Bhn%2FUXkWojtkHKoCe%2FViY9OyhMcogVfdB1X40tFmrb%2FfBRZHgJkcisIeizLs4AFFbu%2FW3xztPnIkuvBYTGAQPACvKFCoO9%2FqFvmHAkCDbYc6bYZ2nNuBrCvllFcNr7wArBNmTSd%2BawUUZLf3ry0awLMTwqrh5qR48W1mrJZogCZJa%2Bmm2dvslF1fq1%2Bp9KFcaUoHbcLWoB8SiEww8r4vAY6pgEW2gIExSPf4KG1ckfWBKugdux0XhOwG9a%2BkFz1215ivewBCkkmWLDRkh%2FyhFU4yyOAl4fUtl73%2FaXyePLdz%2FIO2iSrhHIwph5nzcrSLDSfKFXfUmIiGGsSQx%2FNMyfGLXTBx0PzE%2BAn5LDrO4RP%2BkbSP35gimZ6XblK2CIGXjJ6Q7QBnUKFcNDdIgRFoCqhKkhZL5qH6ee4QgcUeyZXexeSaxeKHcdA&X-Amz-Signature=b5d71cacb6a0be46b60f14a9652596fe84798bad39d58b26133dac6c1547188e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PH7GYTS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBZXB6bsfp6QHHaeSr0eNYmywxfF9MSBE9dohytI3BW7AiB1G3PnjcPABUCINF9CIDrwA59QrH5hbgDU2280eh6oiyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLQaMLS2vhoh9BlS2KtwDP4RmI9nS0UhYeKPvKSK1pzsn%2FtxHAEcx1TGMryqPlfl%2BHQJvxxIbsBfFr9cvjyBt8rR3aWa7WQMM4g4exLk13QjPpSBQ0cqSzf5Tu%2FBXl2nU1P62LiCq2Lgq3lPRJ%2F1tXQ7bQveRa4Qq34%2BSXhxTkCNYqDwjcGUmlTheWJm96oHW8OnwqVqX8svj%2FKk9D6sKArPxzm0kzt9k7El5LM8a%2BYfoTMDWaw6%2F6ovfhMYjUW4YwW3hCZxLxB0AP9i8Vk%2BnnEZJy%2Fi%2FWmufRGjH9EQC69wowhmM69cv6dKEHPQk3pBeiOSeoSwYfbjl8fWdxPi0oYmoGtIlim8Sadjr6DSuu1TDtAl%2BwxRwW7AqH6TJbjKm%2BE5KxMOnZGc1Tj6gzMDwVSQUBfq7vdOK7EYzs1%2Fakdve%2BEv45nAobOKuzh5AF0sic%2Bhn%2FUXkWojtkHKoCe%2FViY9OyhMcogVfdB1X40tFmrb%2FfBRZHgJkcisIeizLs4AFFbu%2FW3xztPnIkuvBYTGAQPACvKFCoO9%2FqFvmHAkCDbYc6bYZ2nNuBrCvllFcNr7wArBNmTSd%2BawUUZLf3ry0awLMTwqrh5qR48W1mrJZogCZJa%2Bmm2dvslF1fq1%2Bp9KFcaUoHbcLWoB8SiEww8r4vAY6pgEW2gIExSPf4KG1ckfWBKugdux0XhOwG9a%2BkFz1215ivewBCkkmWLDRkh%2FyhFU4yyOAl4fUtl73%2FaXyePLdz%2FIO2iSrhHIwph5nzcrSLDSfKFXfUmIiGGsSQx%2FNMyfGLXTBx0PzE%2BAn5LDrO4RP%2BkbSP35gimZ6XblK2CIGXjJ6Q7QBnUKFcNDdIgRFoCqhKkhZL5qH6ee4QgcUeyZXexeSaxeKHcdA&X-Amz-Signature=a6368a95fc061d5f3be4e9a21a0be18fca8ad0b7e75740a670b0b657e021b0ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F2WOOEP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDstMjoZghSwCONpYMv1UFZnrfjoMiH6dqcnMxpVOlkGAiBHmphukL6DEOR7wWTt9AyqIz5YibdtylRYmv09mfq7vyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYEkQL%2FGuQF50hXJFKtwD62G%2FAggDu%2FOFPspkzcir7q%2BARn%2Flec%2FFMJ7Jepwu%2Fh%2BiTxGIfgDgsi%2FrfclCZ6uWyafavRZVa0bW19mQg26EfF5hNji0y99ILR2XATeyPROqucg6fFqd4hKN2PnsKC1vLu6TEwc6NMxY40hDxVlBUbTiK8J0YVGKZltNnnPOOGyNPyqb1APuCQh7bT5P%2Bkg4ySmqC0Y84snvD2dXII%2FGPIsgD7O2Q0vgFedWVqexSDZwd7eGPuF1dF6gs0PwKg6OfRosL5K76luJRFo%2FfZYhCY41YX0Oh3IhP3DgHVgDgiZg7TYCD4MFyWKi%2FCzxm5mOrg%2FOTS8MzLRBZANdYD8ppq%2FpXKmwiqZktSmGvxIMajGqMJEABOEDCtlZGFAZjqSPCeDFS%2BceAjsQeuLPaQ6Enkb9S3IZKg0%2B4S6MQT9Cfqy%2Bib5eiF42yqBNX5yOLDyMOV3kzajdFTLxP5AI7MMXC9TtycRe1KlMhBUTEp6NvQHEWJz55NFiYOdJKPryoG3hT12S38CwgybL2tmBHNr7MdGLwrZ2BQzz4vP%2F5YeQEU%2FW%2B%2BHr%2BZpW1I3rCAPZrxd3mUPEDypxRO1vW%2BYdJaqSpJ5Qisxjg9Yw6g1%2Fk4XG7j0yNk3svarLUjbdyoEwzcX4vAY6pgFfpBxM7m1SAJxrtgJEnbK9GhccRh9SY0J%2BBn5%2BP4j6jQhoYbLimkY1ZNE4TcTkDFWxSe3HaZJPUmJAF8UZTK2LyxQbKGKZWh6mlr4%2FD81cPDzC9r%2F1o5NB6W1Jhs9D%2FdmXoWx1JGvl42eY%2BDZFu0vaYWrJyz4TWdTdH7avvavbRQ202ZyKAh2Mj5nz8thlv%2FLT2xXrcpX8Lle7C10Yb62h0z1INsvY&X-Amz-Signature=8fd093b65976500f8251154b1eb2b8b298d762d6177f5a56f78a58719cc92b06&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F2WOOEP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDstMjoZghSwCONpYMv1UFZnrfjoMiH6dqcnMxpVOlkGAiBHmphukL6DEOR7wWTt9AyqIz5YibdtylRYmv09mfq7vyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYEkQL%2FGuQF50hXJFKtwD62G%2FAggDu%2FOFPspkzcir7q%2BARn%2Flec%2FFMJ7Jepwu%2Fh%2BiTxGIfgDgsi%2FrfclCZ6uWyafavRZVa0bW19mQg26EfF5hNji0y99ILR2XATeyPROqucg6fFqd4hKN2PnsKC1vLu6TEwc6NMxY40hDxVlBUbTiK8J0YVGKZltNnnPOOGyNPyqb1APuCQh7bT5P%2Bkg4ySmqC0Y84snvD2dXII%2FGPIsgD7O2Q0vgFedWVqexSDZwd7eGPuF1dF6gs0PwKg6OfRosL5K76luJRFo%2FfZYhCY41YX0Oh3IhP3DgHVgDgiZg7TYCD4MFyWKi%2FCzxm5mOrg%2FOTS8MzLRBZANdYD8ppq%2FpXKmwiqZktSmGvxIMajGqMJEABOEDCtlZGFAZjqSPCeDFS%2BceAjsQeuLPaQ6Enkb9S3IZKg0%2B4S6MQT9Cfqy%2Bib5eiF42yqBNX5yOLDyMOV3kzajdFTLxP5AI7MMXC9TtycRe1KlMhBUTEp6NvQHEWJz55NFiYOdJKPryoG3hT12S38CwgybL2tmBHNr7MdGLwrZ2BQzz4vP%2F5YeQEU%2FW%2B%2BHr%2BZpW1I3rCAPZrxd3mUPEDypxRO1vW%2BYdJaqSpJ5Qisxjg9Yw6g1%2Fk4XG7j0yNk3svarLUjbdyoEwzcX4vAY6pgFfpBxM7m1SAJxrtgJEnbK9GhccRh9SY0J%2BBn5%2BP4j6jQhoYbLimkY1ZNE4TcTkDFWxSe3HaZJPUmJAF8UZTK2LyxQbKGKZWh6mlr4%2FD81cPDzC9r%2F1o5NB6W1Jhs9D%2FdmXoWx1JGvl42eY%2BDZFu0vaYWrJyz4TWdTdH7avvavbRQ202ZyKAh2Mj5nz8thlv%2FLT2xXrcpX8Lle7C10Yb62h0z1INsvY&X-Amz-Signature=d41e8be1754c70d62154143105d1557677382f36b9fddc690e48f4feea121546&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F2WOOEP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDstMjoZghSwCONpYMv1UFZnrfjoMiH6dqcnMxpVOlkGAiBHmphukL6DEOR7wWTt9AyqIz5YibdtylRYmv09mfq7vyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYEkQL%2FGuQF50hXJFKtwD62G%2FAggDu%2FOFPspkzcir7q%2BARn%2Flec%2FFMJ7Jepwu%2Fh%2BiTxGIfgDgsi%2FrfclCZ6uWyafavRZVa0bW19mQg26EfF5hNji0y99ILR2XATeyPROqucg6fFqd4hKN2PnsKC1vLu6TEwc6NMxY40hDxVlBUbTiK8J0YVGKZltNnnPOOGyNPyqb1APuCQh7bT5P%2Bkg4ySmqC0Y84snvD2dXII%2FGPIsgD7O2Q0vgFedWVqexSDZwd7eGPuF1dF6gs0PwKg6OfRosL5K76luJRFo%2FfZYhCY41YX0Oh3IhP3DgHVgDgiZg7TYCD4MFyWKi%2FCzxm5mOrg%2FOTS8MzLRBZANdYD8ppq%2FpXKmwiqZktSmGvxIMajGqMJEABOEDCtlZGFAZjqSPCeDFS%2BceAjsQeuLPaQ6Enkb9S3IZKg0%2B4S6MQT9Cfqy%2Bib5eiF42yqBNX5yOLDyMOV3kzajdFTLxP5AI7MMXC9TtycRe1KlMhBUTEp6NvQHEWJz55NFiYOdJKPryoG3hT12S38CwgybL2tmBHNr7MdGLwrZ2BQzz4vP%2F5YeQEU%2FW%2B%2BHr%2BZpW1I3rCAPZrxd3mUPEDypxRO1vW%2BYdJaqSpJ5Qisxjg9Yw6g1%2Fk4XG7j0yNk3svarLUjbdyoEwzcX4vAY6pgFfpBxM7m1SAJxrtgJEnbK9GhccRh9SY0J%2BBn5%2BP4j6jQhoYbLimkY1ZNE4TcTkDFWxSe3HaZJPUmJAF8UZTK2LyxQbKGKZWh6mlr4%2FD81cPDzC9r%2F1o5NB6W1Jhs9D%2FdmXoWx1JGvl42eY%2BDZFu0vaYWrJyz4TWdTdH7avvavbRQ202ZyKAh2Mj5nz8thlv%2FLT2xXrcpX8Lle7C10Yb62h0z1INsvY&X-Amz-Signature=7f9e92aca594676910e76476c9fc70eadec7d9108fe44841be094052c36aac7c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F2WOOEP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDstMjoZghSwCONpYMv1UFZnrfjoMiH6dqcnMxpVOlkGAiBHmphukL6DEOR7wWTt9AyqIz5YibdtylRYmv09mfq7vyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYEkQL%2FGuQF50hXJFKtwD62G%2FAggDu%2FOFPspkzcir7q%2BARn%2Flec%2FFMJ7Jepwu%2Fh%2BiTxGIfgDgsi%2FrfclCZ6uWyafavRZVa0bW19mQg26EfF5hNji0y99ILR2XATeyPROqucg6fFqd4hKN2PnsKC1vLu6TEwc6NMxY40hDxVlBUbTiK8J0YVGKZltNnnPOOGyNPyqb1APuCQh7bT5P%2Bkg4ySmqC0Y84snvD2dXII%2FGPIsgD7O2Q0vgFedWVqexSDZwd7eGPuF1dF6gs0PwKg6OfRosL5K76luJRFo%2FfZYhCY41YX0Oh3IhP3DgHVgDgiZg7TYCD4MFyWKi%2FCzxm5mOrg%2FOTS8MzLRBZANdYD8ppq%2FpXKmwiqZktSmGvxIMajGqMJEABOEDCtlZGFAZjqSPCeDFS%2BceAjsQeuLPaQ6Enkb9S3IZKg0%2B4S6MQT9Cfqy%2Bib5eiF42yqBNX5yOLDyMOV3kzajdFTLxP5AI7MMXC9TtycRe1KlMhBUTEp6NvQHEWJz55NFiYOdJKPryoG3hT12S38CwgybL2tmBHNr7MdGLwrZ2BQzz4vP%2F5YeQEU%2FW%2B%2BHr%2BZpW1I3rCAPZrxd3mUPEDypxRO1vW%2BYdJaqSpJ5Qisxjg9Yw6g1%2Fk4XG7j0yNk3svarLUjbdyoEwzcX4vAY6pgFfpBxM7m1SAJxrtgJEnbK9GhccRh9SY0J%2BBn5%2BP4j6jQhoYbLimkY1ZNE4TcTkDFWxSe3HaZJPUmJAF8UZTK2LyxQbKGKZWh6mlr4%2FD81cPDzC9r%2F1o5NB6W1Jhs9D%2FdmXoWx1JGvl42eY%2BDZFu0vaYWrJyz4TWdTdH7avvavbRQ202ZyKAh2Mj5nz8thlv%2FLT2xXrcpX8Lle7C10Yb62h0z1INsvY&X-Amz-Signature=b80a96589fa9e202580784ef4db5782e8181b02a69555ea8cfeae4389a3a5bd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F2WOOEP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDstMjoZghSwCONpYMv1UFZnrfjoMiH6dqcnMxpVOlkGAiBHmphukL6DEOR7wWTt9AyqIz5YibdtylRYmv09mfq7vyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYEkQL%2FGuQF50hXJFKtwD62G%2FAggDu%2FOFPspkzcir7q%2BARn%2Flec%2FFMJ7Jepwu%2Fh%2BiTxGIfgDgsi%2FrfclCZ6uWyafavRZVa0bW19mQg26EfF5hNji0y99ILR2XATeyPROqucg6fFqd4hKN2PnsKC1vLu6TEwc6NMxY40hDxVlBUbTiK8J0YVGKZltNnnPOOGyNPyqb1APuCQh7bT5P%2Bkg4ySmqC0Y84snvD2dXII%2FGPIsgD7O2Q0vgFedWVqexSDZwd7eGPuF1dF6gs0PwKg6OfRosL5K76luJRFo%2FfZYhCY41YX0Oh3IhP3DgHVgDgiZg7TYCD4MFyWKi%2FCzxm5mOrg%2FOTS8MzLRBZANdYD8ppq%2FpXKmwiqZktSmGvxIMajGqMJEABOEDCtlZGFAZjqSPCeDFS%2BceAjsQeuLPaQ6Enkb9S3IZKg0%2B4S6MQT9Cfqy%2Bib5eiF42yqBNX5yOLDyMOV3kzajdFTLxP5AI7MMXC9TtycRe1KlMhBUTEp6NvQHEWJz55NFiYOdJKPryoG3hT12S38CwgybL2tmBHNr7MdGLwrZ2BQzz4vP%2F5YeQEU%2FW%2B%2BHr%2BZpW1I3rCAPZrxd3mUPEDypxRO1vW%2BYdJaqSpJ5Qisxjg9Yw6g1%2Fk4XG7j0yNk3svarLUjbdyoEwzcX4vAY6pgFfpBxM7m1SAJxrtgJEnbK9GhccRh9SY0J%2BBn5%2BP4j6jQhoYbLimkY1ZNE4TcTkDFWxSe3HaZJPUmJAF8UZTK2LyxQbKGKZWh6mlr4%2FD81cPDzC9r%2F1o5NB6W1Jhs9D%2FdmXoWx1JGvl42eY%2BDZFu0vaYWrJyz4TWdTdH7avvavbRQ202ZyKAh2Mj5nz8thlv%2FLT2xXrcpX8Lle7C10Yb62h0z1INsvY&X-Amz-Signature=19d6da697ed28b193e50e422d457dfae73378b1a56b11016d982d29827756c5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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


