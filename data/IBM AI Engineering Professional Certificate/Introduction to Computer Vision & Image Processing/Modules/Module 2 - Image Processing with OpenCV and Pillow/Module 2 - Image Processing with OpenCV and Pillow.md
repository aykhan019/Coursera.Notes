

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3IOQRM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHK5CrglbhLK7YHg%2B4gYpoRV5%2FWTcmWT%2BAQJdMLt8PC3AiEAh2T5Vjbmj4WMzWEt0YDlE1HFdjFZuRyIMJWYt3WbXVEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBWS98tmVsTAxIf4CSrcAwoXLBg1zlf93RPIn%2B3SSan1IyOO%2FOqqMgFvLSVmr8k4Uh4vuxjO%2FcPeR%2FgWLmLA%2FtoWNUpn%2F3nyRSdDz0l%2BzkGPrzctqrS7tft2Pvx1WteWU6KTjBRe7DibEppaSpbxUDOvQzH3zBm6OcmcJXF0fC9tEIk%2BIoeVQu7K5y%2Bc8k1y%2F6UovnHcCejt8ktZq74bzRTdaPhusVxJPTuhqidjtSsEZBwLgH9XD3NkdiKmAEmPlJZRZ2qMW8QwtHk%2By2bPU%2BHnLdh%2BDSkktUxZSChV%2F7LrjvzkflSMXbDlOuwmxukXKXtQyTLvefw0aRCJ7rWmfpWHKLDAEK4XC8VIgyYLDPVvaxr0kcO%2BWsPbs3SpGnkSwKbD9S2DGK3wfbaBapjqw4FROrXc1G%2Bqz6wQ1ZzGNFpL%2BoEdTn9vNtyq6%2F8U%2FwgXGE9NsK7PrsaNlwWS9O29HvGMdsfsN6SFHFBkp6aziMyfMU%2BQsDbhziBSbKhN%2FpwDbkjPHPDXBqADI%2FSrMoq2BD6GBuEXrh7qBFF6Q9gaPsySDoRKnFZx2aQVxja8INnta98FAQv5H%2B8ALYYpqANxNSqN8%2Br6%2Bukd3gTfF3Ia1uD1tiPVUDwnwiTPjnqHFxZLSep7Or03MAfBaKLiMMS6jr0GOqUBCTavvCTOtudf2j3L2HcIZhJmh4R5zaigQZNpE9auHVCqKtHgK4Wjf67RU2xbRiA6yiTO3vZEOB1H0py%2BQC0NYFjfvtZMjxw3Q8%2BxLaiu6t7RyTI6GpJWu2%2B30%2Bj5eHm8gEr5MznVVP7L2gLWG4YLvjMCN3afZIPyUYzDePFNMops1%2FeZZUMI6RyEh7Q%2FHsbD0Rn6tT8vXDyFE3GIAhJvhSaSfoBd&X-Amz-Signature=2f42cb76123bbbd7cf81dd859d2da44bd29c0aa8e41528590b846bd29056c46e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVOKEURJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQC%2FEAzHCLc%2Bw%2FoWXEZpDj%2FCT%2FVoN%2F4oym8S0jD911fK0gIgR9N70Fpbmo%2BQBge78KzbrPjYjljwsUujyX83tewHWt8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBIaS3cFPIzi4Dkz9yrcAwPgwrGnSijIc8VSwV1uhh8qkEcN4A5gTmN7PfM8wPRSSxI6jq%2FPhxIyVXWg07Pe5VU7fz4UDBFOB7xrJzMz6xnFHHol%2BOAY1%2BHnI%2Faie%2Bs2Boq34gF32pKnCfnLdrLydsAC%2FSMg0qlqHDqpo92TOO%2BeK7XPhz9YI2QvrA14oxUfYiCb1uZXBLkaF2tM5%2BgklMBFwS%2BM%2FwfLxcUAL8KpTsA2VRq14ecaiMCQmlKRHjGg6FlhcmlQKo7IdZCS%2BE0fECNAH6SFAmJc2fRjz9VX5D%2BgVkOXdexJ7WzhJ8OD61tLviZwWkPm6%2BE2IH26w6M6GnInt5unt96UyPisEYVKgiXZ4HVb1zG5KfDwSENgcpgnXzqAd04bsXKXIYBMrmuuEoe0e0%2Fq9oRKwECnIxDA5muofKDgb25ugFl5uR79oQmh37ppmWbJKTcIlOevVpo%2B5pXCCRFMZ531wuR0k3YOKB6DKNPV%2BVDsGSUxaZ9fEsWJR3SJdSIKu84SIXQAWTigxs1CQwBhzbXOAeA1kQUU42abHs3CJvfH4fouVA4DWzeIxlq2bbIcVZPkBJNMoe96WwW8Xxmd7KXq7sNkdtgoOAQx1Cp7wp66CLpY519SPE8NsCuAHf0wrjhHedHxMLW6jr0GOqUBMf8rp2laP5O6xkzzjg%2FFxWScaJDC1rBsfjhb8ZBgGD4A7sVdreBa6B0yQObFnk0DWiCp1Afrv%2Fw9m56C2ff5IWOsUQswKelTgNdei1u1rohRWIfpcCTxqsIljiAysOGZp3FbI4tZ0mdLYPiD6ZqAK9V3nCCVpjY19Y12fi%2BFKMp43HIRO%2BHnwUiInjHrILEX3PkzzKTrir9K%2B2ubePGhDWxYLabC&X-Amz-Signature=a64186e02a8ae91df24db67dfbc3265cac19ba5f1fc1a1d8918aba5bead01e4c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVOKEURJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQC%2FEAzHCLc%2Bw%2FoWXEZpDj%2FCT%2FVoN%2F4oym8S0jD911fK0gIgR9N70Fpbmo%2BQBge78KzbrPjYjljwsUujyX83tewHWt8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBIaS3cFPIzi4Dkz9yrcAwPgwrGnSijIc8VSwV1uhh8qkEcN4A5gTmN7PfM8wPRSSxI6jq%2FPhxIyVXWg07Pe5VU7fz4UDBFOB7xrJzMz6xnFHHol%2BOAY1%2BHnI%2Faie%2Bs2Boq34gF32pKnCfnLdrLydsAC%2FSMg0qlqHDqpo92TOO%2BeK7XPhz9YI2QvrA14oxUfYiCb1uZXBLkaF2tM5%2BgklMBFwS%2BM%2FwfLxcUAL8KpTsA2VRq14ecaiMCQmlKRHjGg6FlhcmlQKo7IdZCS%2BE0fECNAH6SFAmJc2fRjz9VX5D%2BgVkOXdexJ7WzhJ8OD61tLviZwWkPm6%2BE2IH26w6M6GnInt5unt96UyPisEYVKgiXZ4HVb1zG5KfDwSENgcpgnXzqAd04bsXKXIYBMrmuuEoe0e0%2Fq9oRKwECnIxDA5muofKDgb25ugFl5uR79oQmh37ppmWbJKTcIlOevVpo%2B5pXCCRFMZ531wuR0k3YOKB6DKNPV%2BVDsGSUxaZ9fEsWJR3SJdSIKu84SIXQAWTigxs1CQwBhzbXOAeA1kQUU42abHs3CJvfH4fouVA4DWzeIxlq2bbIcVZPkBJNMoe96WwW8Xxmd7KXq7sNkdtgoOAQx1Cp7wp66CLpY519SPE8NsCuAHf0wrjhHedHxMLW6jr0GOqUBMf8rp2laP5O6xkzzjg%2FFxWScaJDC1rBsfjhb8ZBgGD4A7sVdreBa6B0yQObFnk0DWiCp1Afrv%2Fw9m56C2ff5IWOsUQswKelTgNdei1u1rohRWIfpcCTxqsIljiAysOGZp3FbI4tZ0mdLYPiD6ZqAK9V3nCCVpjY19Y12fi%2BFKMp43HIRO%2BHnwUiInjHrILEX3PkzzKTrir9K%2B2ubePGhDWxYLabC&X-Amz-Signature=03addb5be5b83f1cbc3bcc0d5f067d306483d020f42420116071a9daae717dda&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVOKEURJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQC%2FEAzHCLc%2Bw%2FoWXEZpDj%2FCT%2FVoN%2F4oym8S0jD911fK0gIgR9N70Fpbmo%2BQBge78KzbrPjYjljwsUujyX83tewHWt8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBIaS3cFPIzi4Dkz9yrcAwPgwrGnSijIc8VSwV1uhh8qkEcN4A5gTmN7PfM8wPRSSxI6jq%2FPhxIyVXWg07Pe5VU7fz4UDBFOB7xrJzMz6xnFHHol%2BOAY1%2BHnI%2Faie%2Bs2Boq34gF32pKnCfnLdrLydsAC%2FSMg0qlqHDqpo92TOO%2BeK7XPhz9YI2QvrA14oxUfYiCb1uZXBLkaF2tM5%2BgklMBFwS%2BM%2FwfLxcUAL8KpTsA2VRq14ecaiMCQmlKRHjGg6FlhcmlQKo7IdZCS%2BE0fECNAH6SFAmJc2fRjz9VX5D%2BgVkOXdexJ7WzhJ8OD61tLviZwWkPm6%2BE2IH26w6M6GnInt5unt96UyPisEYVKgiXZ4HVb1zG5KfDwSENgcpgnXzqAd04bsXKXIYBMrmuuEoe0e0%2Fq9oRKwECnIxDA5muofKDgb25ugFl5uR79oQmh37ppmWbJKTcIlOevVpo%2B5pXCCRFMZ531wuR0k3YOKB6DKNPV%2BVDsGSUxaZ9fEsWJR3SJdSIKu84SIXQAWTigxs1CQwBhzbXOAeA1kQUU42abHs3CJvfH4fouVA4DWzeIxlq2bbIcVZPkBJNMoe96WwW8Xxmd7KXq7sNkdtgoOAQx1Cp7wp66CLpY519SPE8NsCuAHf0wrjhHedHxMLW6jr0GOqUBMf8rp2laP5O6xkzzjg%2FFxWScaJDC1rBsfjhb8ZBgGD4A7sVdreBa6B0yQObFnk0DWiCp1Afrv%2Fw9m56C2ff5IWOsUQswKelTgNdei1u1rohRWIfpcCTxqsIljiAysOGZp3FbI4tZ0mdLYPiD6ZqAK9V3nCCVpjY19Y12fi%2BFKMp43HIRO%2BHnwUiInjHrILEX3PkzzKTrir9K%2B2ubePGhDWxYLabC&X-Amz-Signature=3f7d97fa8b52cc55bfc6ee5385da37c4942d6d7451e7fbe7c73f9d1861bef67a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVOKEURJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQC%2FEAzHCLc%2Bw%2FoWXEZpDj%2FCT%2FVoN%2F4oym8S0jD911fK0gIgR9N70Fpbmo%2BQBge78KzbrPjYjljwsUujyX83tewHWt8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBIaS3cFPIzi4Dkz9yrcAwPgwrGnSijIc8VSwV1uhh8qkEcN4A5gTmN7PfM8wPRSSxI6jq%2FPhxIyVXWg07Pe5VU7fz4UDBFOB7xrJzMz6xnFHHol%2BOAY1%2BHnI%2Faie%2Bs2Boq34gF32pKnCfnLdrLydsAC%2FSMg0qlqHDqpo92TOO%2BeK7XPhz9YI2QvrA14oxUfYiCb1uZXBLkaF2tM5%2BgklMBFwS%2BM%2FwfLxcUAL8KpTsA2VRq14ecaiMCQmlKRHjGg6FlhcmlQKo7IdZCS%2BE0fECNAH6SFAmJc2fRjz9VX5D%2BgVkOXdexJ7WzhJ8OD61tLviZwWkPm6%2BE2IH26w6M6GnInt5unt96UyPisEYVKgiXZ4HVb1zG5KfDwSENgcpgnXzqAd04bsXKXIYBMrmuuEoe0e0%2Fq9oRKwECnIxDA5muofKDgb25ugFl5uR79oQmh37ppmWbJKTcIlOevVpo%2B5pXCCRFMZ531wuR0k3YOKB6DKNPV%2BVDsGSUxaZ9fEsWJR3SJdSIKu84SIXQAWTigxs1CQwBhzbXOAeA1kQUU42abHs3CJvfH4fouVA4DWzeIxlq2bbIcVZPkBJNMoe96WwW8Xxmd7KXq7sNkdtgoOAQx1Cp7wp66CLpY519SPE8NsCuAHf0wrjhHedHxMLW6jr0GOqUBMf8rp2laP5O6xkzzjg%2FFxWScaJDC1rBsfjhb8ZBgGD4A7sVdreBa6B0yQObFnk0DWiCp1Afrv%2Fw9m56C2ff5IWOsUQswKelTgNdei1u1rohRWIfpcCTxqsIljiAysOGZp3FbI4tZ0mdLYPiD6ZqAK9V3nCCVpjY19Y12fi%2BFKMp43HIRO%2BHnwUiInjHrILEX3PkzzKTrir9K%2B2ubePGhDWxYLabC&X-Amz-Signature=cbb6b554663ad663b457f34992da64d2d9149b6a975d9af06655ec0a6ef1b659&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVOKEURJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQC%2FEAzHCLc%2Bw%2FoWXEZpDj%2FCT%2FVoN%2F4oym8S0jD911fK0gIgR9N70Fpbmo%2BQBge78KzbrPjYjljwsUujyX83tewHWt8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBIaS3cFPIzi4Dkz9yrcAwPgwrGnSijIc8VSwV1uhh8qkEcN4A5gTmN7PfM8wPRSSxI6jq%2FPhxIyVXWg07Pe5VU7fz4UDBFOB7xrJzMz6xnFHHol%2BOAY1%2BHnI%2Faie%2Bs2Boq34gF32pKnCfnLdrLydsAC%2FSMg0qlqHDqpo92TOO%2BeK7XPhz9YI2QvrA14oxUfYiCb1uZXBLkaF2tM5%2BgklMBFwS%2BM%2FwfLxcUAL8KpTsA2VRq14ecaiMCQmlKRHjGg6FlhcmlQKo7IdZCS%2BE0fECNAH6SFAmJc2fRjz9VX5D%2BgVkOXdexJ7WzhJ8OD61tLviZwWkPm6%2BE2IH26w6M6GnInt5unt96UyPisEYVKgiXZ4HVb1zG5KfDwSENgcpgnXzqAd04bsXKXIYBMrmuuEoe0e0%2Fq9oRKwECnIxDA5muofKDgb25ugFl5uR79oQmh37ppmWbJKTcIlOevVpo%2B5pXCCRFMZ531wuR0k3YOKB6DKNPV%2BVDsGSUxaZ9fEsWJR3SJdSIKu84SIXQAWTigxs1CQwBhzbXOAeA1kQUU42abHs3CJvfH4fouVA4DWzeIxlq2bbIcVZPkBJNMoe96WwW8Xxmd7KXq7sNkdtgoOAQx1Cp7wp66CLpY519SPE8NsCuAHf0wrjhHedHxMLW6jr0GOqUBMf8rp2laP5O6xkzzjg%2FFxWScaJDC1rBsfjhb8ZBgGD4A7sVdreBa6B0yQObFnk0DWiCp1Afrv%2Fw9m56C2ff5IWOsUQswKelTgNdei1u1rohRWIfpcCTxqsIljiAysOGZp3FbI4tZ0mdLYPiD6ZqAK9V3nCCVpjY19Y12fi%2BFKMp43HIRO%2BHnwUiInjHrILEX3PkzzKTrir9K%2B2ubePGhDWxYLabC&X-Amz-Signature=60f4b4b2fd98eaf78f4d108bf41e3bb87c1d6552d83b7ae584c96e1fa5fa3425&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3IOQRM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHK5CrglbhLK7YHg%2B4gYpoRV5%2FWTcmWT%2BAQJdMLt8PC3AiEAh2T5Vjbmj4WMzWEt0YDlE1HFdjFZuRyIMJWYt3WbXVEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBWS98tmVsTAxIf4CSrcAwoXLBg1zlf93RPIn%2B3SSan1IyOO%2FOqqMgFvLSVmr8k4Uh4vuxjO%2FcPeR%2FgWLmLA%2FtoWNUpn%2F3nyRSdDz0l%2BzkGPrzctqrS7tft2Pvx1WteWU6KTjBRe7DibEppaSpbxUDOvQzH3zBm6OcmcJXF0fC9tEIk%2BIoeVQu7K5y%2Bc8k1y%2F6UovnHcCejt8ktZq74bzRTdaPhusVxJPTuhqidjtSsEZBwLgH9XD3NkdiKmAEmPlJZRZ2qMW8QwtHk%2By2bPU%2BHnLdh%2BDSkktUxZSChV%2F7LrjvzkflSMXbDlOuwmxukXKXtQyTLvefw0aRCJ7rWmfpWHKLDAEK4XC8VIgyYLDPVvaxr0kcO%2BWsPbs3SpGnkSwKbD9S2DGK3wfbaBapjqw4FROrXc1G%2Bqz6wQ1ZzGNFpL%2BoEdTn9vNtyq6%2F8U%2FwgXGE9NsK7PrsaNlwWS9O29HvGMdsfsN6SFHFBkp6aziMyfMU%2BQsDbhziBSbKhN%2FpwDbkjPHPDXBqADI%2FSrMoq2BD6GBuEXrh7qBFF6Q9gaPsySDoRKnFZx2aQVxja8INnta98FAQv5H%2B8ALYYpqANxNSqN8%2Br6%2Bukd3gTfF3Ia1uD1tiPVUDwnwiTPjnqHFxZLSep7Or03MAfBaKLiMMS6jr0GOqUBCTavvCTOtudf2j3L2HcIZhJmh4R5zaigQZNpE9auHVCqKtHgK4Wjf67RU2xbRiA6yiTO3vZEOB1H0py%2BQC0NYFjfvtZMjxw3Q8%2BxLaiu6t7RyTI6GpJWu2%2B30%2Bj5eHm8gEr5MznVVP7L2gLWG4YLvjMCN3afZIPyUYzDePFNMops1%2FeZZUMI6RyEh7Q%2FHsbD0Rn6tT8vXDyFE3GIAhJvhSaSfoBd&X-Amz-Signature=adb72c232ff7a12c0c40723707eb612052ea5c53053cf797004f639f57f92f82&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3IOQRM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHK5CrglbhLK7YHg%2B4gYpoRV5%2FWTcmWT%2BAQJdMLt8PC3AiEAh2T5Vjbmj4WMzWEt0YDlE1HFdjFZuRyIMJWYt3WbXVEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBWS98tmVsTAxIf4CSrcAwoXLBg1zlf93RPIn%2B3SSan1IyOO%2FOqqMgFvLSVmr8k4Uh4vuxjO%2FcPeR%2FgWLmLA%2FtoWNUpn%2F3nyRSdDz0l%2BzkGPrzctqrS7tft2Pvx1WteWU6KTjBRe7DibEppaSpbxUDOvQzH3zBm6OcmcJXF0fC9tEIk%2BIoeVQu7K5y%2Bc8k1y%2F6UovnHcCejt8ktZq74bzRTdaPhusVxJPTuhqidjtSsEZBwLgH9XD3NkdiKmAEmPlJZRZ2qMW8QwtHk%2By2bPU%2BHnLdh%2BDSkktUxZSChV%2F7LrjvzkflSMXbDlOuwmxukXKXtQyTLvefw0aRCJ7rWmfpWHKLDAEK4XC8VIgyYLDPVvaxr0kcO%2BWsPbs3SpGnkSwKbD9S2DGK3wfbaBapjqw4FROrXc1G%2Bqz6wQ1ZzGNFpL%2BoEdTn9vNtyq6%2F8U%2FwgXGE9NsK7PrsaNlwWS9O29HvGMdsfsN6SFHFBkp6aziMyfMU%2BQsDbhziBSbKhN%2FpwDbkjPHPDXBqADI%2FSrMoq2BD6GBuEXrh7qBFF6Q9gaPsySDoRKnFZx2aQVxja8INnta98FAQv5H%2B8ALYYpqANxNSqN8%2Br6%2Bukd3gTfF3Ia1uD1tiPVUDwnwiTPjnqHFxZLSep7Or03MAfBaKLiMMS6jr0GOqUBCTavvCTOtudf2j3L2HcIZhJmh4R5zaigQZNpE9auHVCqKtHgK4Wjf67RU2xbRiA6yiTO3vZEOB1H0py%2BQC0NYFjfvtZMjxw3Q8%2BxLaiu6t7RyTI6GpJWu2%2B30%2Bj5eHm8gEr5MznVVP7L2gLWG4YLvjMCN3afZIPyUYzDePFNMops1%2FeZZUMI6RyEh7Q%2FHsbD0Rn6tT8vXDyFE3GIAhJvhSaSfoBd&X-Amz-Signature=7e586bc2de67311e287c5b20a4fae77c549669e569bb7e40a52375b30877f13b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3IOQRM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHK5CrglbhLK7YHg%2B4gYpoRV5%2FWTcmWT%2BAQJdMLt8PC3AiEAh2T5Vjbmj4WMzWEt0YDlE1HFdjFZuRyIMJWYt3WbXVEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBWS98tmVsTAxIf4CSrcAwoXLBg1zlf93RPIn%2B3SSan1IyOO%2FOqqMgFvLSVmr8k4Uh4vuxjO%2FcPeR%2FgWLmLA%2FtoWNUpn%2F3nyRSdDz0l%2BzkGPrzctqrS7tft2Pvx1WteWU6KTjBRe7DibEppaSpbxUDOvQzH3zBm6OcmcJXF0fC9tEIk%2BIoeVQu7K5y%2Bc8k1y%2F6UovnHcCejt8ktZq74bzRTdaPhusVxJPTuhqidjtSsEZBwLgH9XD3NkdiKmAEmPlJZRZ2qMW8QwtHk%2By2bPU%2BHnLdh%2BDSkktUxZSChV%2F7LrjvzkflSMXbDlOuwmxukXKXtQyTLvefw0aRCJ7rWmfpWHKLDAEK4XC8VIgyYLDPVvaxr0kcO%2BWsPbs3SpGnkSwKbD9S2DGK3wfbaBapjqw4FROrXc1G%2Bqz6wQ1ZzGNFpL%2BoEdTn9vNtyq6%2F8U%2FwgXGE9NsK7PrsaNlwWS9O29HvGMdsfsN6SFHFBkp6aziMyfMU%2BQsDbhziBSbKhN%2FpwDbkjPHPDXBqADI%2FSrMoq2BD6GBuEXrh7qBFF6Q9gaPsySDoRKnFZx2aQVxja8INnta98FAQv5H%2B8ALYYpqANxNSqN8%2Br6%2Bukd3gTfF3Ia1uD1tiPVUDwnwiTPjnqHFxZLSep7Or03MAfBaKLiMMS6jr0GOqUBCTavvCTOtudf2j3L2HcIZhJmh4R5zaigQZNpE9auHVCqKtHgK4Wjf67RU2xbRiA6yiTO3vZEOB1H0py%2BQC0NYFjfvtZMjxw3Q8%2BxLaiu6t7RyTI6GpJWu2%2B30%2Bj5eHm8gEr5MznVVP7L2gLWG4YLvjMCN3afZIPyUYzDePFNMops1%2FeZZUMI6RyEh7Q%2FHsbD0Rn6tT8vXDyFE3GIAhJvhSaSfoBd&X-Amz-Signature=cff271bb2fac22962a5b4f4e5bdbc53da66793b628d1e26ab8ed6db3c874c8ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3IOQRM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHK5CrglbhLK7YHg%2B4gYpoRV5%2FWTcmWT%2BAQJdMLt8PC3AiEAh2T5Vjbmj4WMzWEt0YDlE1HFdjFZuRyIMJWYt3WbXVEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBWS98tmVsTAxIf4CSrcAwoXLBg1zlf93RPIn%2B3SSan1IyOO%2FOqqMgFvLSVmr8k4Uh4vuxjO%2FcPeR%2FgWLmLA%2FtoWNUpn%2F3nyRSdDz0l%2BzkGPrzctqrS7tft2Pvx1WteWU6KTjBRe7DibEppaSpbxUDOvQzH3zBm6OcmcJXF0fC9tEIk%2BIoeVQu7K5y%2Bc8k1y%2F6UovnHcCejt8ktZq74bzRTdaPhusVxJPTuhqidjtSsEZBwLgH9XD3NkdiKmAEmPlJZRZ2qMW8QwtHk%2By2bPU%2BHnLdh%2BDSkktUxZSChV%2F7LrjvzkflSMXbDlOuwmxukXKXtQyTLvefw0aRCJ7rWmfpWHKLDAEK4XC8VIgyYLDPVvaxr0kcO%2BWsPbs3SpGnkSwKbD9S2DGK3wfbaBapjqw4FROrXc1G%2Bqz6wQ1ZzGNFpL%2BoEdTn9vNtyq6%2F8U%2FwgXGE9NsK7PrsaNlwWS9O29HvGMdsfsN6SFHFBkp6aziMyfMU%2BQsDbhziBSbKhN%2FpwDbkjPHPDXBqADI%2FSrMoq2BD6GBuEXrh7qBFF6Q9gaPsySDoRKnFZx2aQVxja8INnta98FAQv5H%2B8ALYYpqANxNSqN8%2Br6%2Bukd3gTfF3Ia1uD1tiPVUDwnwiTPjnqHFxZLSep7Or03MAfBaKLiMMS6jr0GOqUBCTavvCTOtudf2j3L2HcIZhJmh4R5zaigQZNpE9auHVCqKtHgK4Wjf67RU2xbRiA6yiTO3vZEOB1H0py%2BQC0NYFjfvtZMjxw3Q8%2BxLaiu6t7RyTI6GpJWu2%2B30%2Bj5eHm8gEr5MznVVP7L2gLWG4YLvjMCN3afZIPyUYzDePFNMops1%2FeZZUMI6RyEh7Q%2FHsbD0Rn6tT8vXDyFE3GIAhJvhSaSfoBd&X-Amz-Signature=fbaaa4b37d97f31aee4c13b9b91ee25fba0043d56860c6d7bb53e2f77f6c0d1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3IOQRM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHK5CrglbhLK7YHg%2B4gYpoRV5%2FWTcmWT%2BAQJdMLt8PC3AiEAh2T5Vjbmj4WMzWEt0YDlE1HFdjFZuRyIMJWYt3WbXVEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBWS98tmVsTAxIf4CSrcAwoXLBg1zlf93RPIn%2B3SSan1IyOO%2FOqqMgFvLSVmr8k4Uh4vuxjO%2FcPeR%2FgWLmLA%2FtoWNUpn%2F3nyRSdDz0l%2BzkGPrzctqrS7tft2Pvx1WteWU6KTjBRe7DibEppaSpbxUDOvQzH3zBm6OcmcJXF0fC9tEIk%2BIoeVQu7K5y%2Bc8k1y%2F6UovnHcCejt8ktZq74bzRTdaPhusVxJPTuhqidjtSsEZBwLgH9XD3NkdiKmAEmPlJZRZ2qMW8QwtHk%2By2bPU%2BHnLdh%2BDSkktUxZSChV%2F7LrjvzkflSMXbDlOuwmxukXKXtQyTLvefw0aRCJ7rWmfpWHKLDAEK4XC8VIgyYLDPVvaxr0kcO%2BWsPbs3SpGnkSwKbD9S2DGK3wfbaBapjqw4FROrXc1G%2Bqz6wQ1ZzGNFpL%2BoEdTn9vNtyq6%2F8U%2FwgXGE9NsK7PrsaNlwWS9O29HvGMdsfsN6SFHFBkp6aziMyfMU%2BQsDbhziBSbKhN%2FpwDbkjPHPDXBqADI%2FSrMoq2BD6GBuEXrh7qBFF6Q9gaPsySDoRKnFZx2aQVxja8INnta98FAQv5H%2B8ALYYpqANxNSqN8%2Br6%2Bukd3gTfF3Ia1uD1tiPVUDwnwiTPjnqHFxZLSep7Or03MAfBaKLiMMS6jr0GOqUBCTavvCTOtudf2j3L2HcIZhJmh4R5zaigQZNpE9auHVCqKtHgK4Wjf67RU2xbRiA6yiTO3vZEOB1H0py%2BQC0NYFjfvtZMjxw3Q8%2BxLaiu6t7RyTI6GpJWu2%2B30%2Bj5eHm8gEr5MznVVP7L2gLWG4YLvjMCN3afZIPyUYzDePFNMops1%2FeZZUMI6RyEh7Q%2FHsbD0Rn6tT8vXDyFE3GIAhJvhSaSfoBd&X-Amz-Signature=db1e808bb0a1ae7c65dbaa02c51bf292fb8b1fdcaa7cdc0459e34e701927ab73&X-Amz-SignedHeaders=host&x-id=GetObject)
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


