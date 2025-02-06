

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZSN3H3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIH2EWmmwgHLuT39gnoWBaS2DrpQVjeTxybzRJNw0AQ6EAiEA7%2FPO7L7DmBEwYcuQ6XWeuMlC7Uk%2FYsQO0nM%2FlE7vXlIq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK%2F8csqxwMgmQZYnAyrcA%2Fg5QWFv5r%2FWRv4AXkM9AWzCeWHkImzn8zjIdL%2Fwhm%2FQxCoCmJKmjlU7b%2BFDZGY%2FOt8IQTvBhZR2LeXkGFXS8LoiY9XG33i1xUdIR2MB089KXK4LvlPzkiQ1A767p0nO9P4fBAwX2ZRViUJ5IJW0MHc3YGGl%2F%2FJ68OSTMw67CH4fiZ%2BJ2yT2cQgTCZ%2B%2FWnztrWosV%2BO2ZojCFa3%2FdeWCbFX8F1wSYFICJOZGxURqRh7Wm5VY9yoIXGzQ4DNR%2F%2FjCxCKOLqOX%2BaZ76NL5Ei2e3bRVX3UGLbyhMqiliDEfFL8muF4%2BGqTCDPh4wlzFk6PcN7kvHgwcg%2B14hNWWZC3qeUuqZqsWF8ZaN9pZl3EGrSbHZcgsG0nX6tLs0wXcIm7EDwYBHj5KxCRRVCdj9qL5p4mhm7WhorhGBPYm1csturwLt3mGmTNcu9TnM%2F5ipW8qT85vcu8yLwqFsZoXRD3CKjMYDkAb4dOlTHKHDL%2BxtEFdIEFniLxIscfmp0f3dGsr%2BLDyTHBrTTidbWUsfOaR73sl7LumZ4sg6atWGCWkBcoZeABlGRD73oBMQkpaivCIfP4m8Pe61bn2aVxz27LqdQKnF%2BWQHeF18L5ChfkUdoRjIh83aDl0vIjW2wFxMObqj70GOqUBKX5ZPHysNjSjZZ8EG%2FbAcDZodoOX8VwKNcA92R%2BlD%2FJzj%2FNMOtylI7a092nLbVx7M8QGvmryEcw%2B2vuAFvjJTzRx2oFCpKj%2BPQpmGLUbTKiIS6YZWTsMI%2B%2BpkWSce1avCEsIQGvUwqRZjLMpMTYn8AneJmzTQrVvZ%2FiF33M9buE9%2BfbVwas%2BIQ8uCzYBjo84arterXCPzHzIpzxSUkvFi0J0JabN&X-Amz-Signature=e13caf70c00f944a7a443502a9eefdc86390be5becc91c7b53886d3af2e9d0fd&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY5BXR7W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDuOuCbDufyg0HsT46RGx1clP%2Fn%2FU0quDtDAPr6KIt3pAIgZ2E5kxydV6MNltZpuRAbLGU1nC5ig2DbSTN7sAFnVbMq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDB52DLnY9RStGdlYAircA2X%2FpV%2B043IcKE1TFymJabepmKJSvCVoCoot%2BComhrvCr82Yl0vc9EQ5DPscuxi8ONXt7xbYul66NQspLwUq6Fclye7F3JuhjTG%2BeAe4uSXyc1267ZVxd7gy%2BB0So4N0gR0Iftk87KW9zGd409Q3ufxtIMJkZe2ysQfuIwVMGw08Ci6DG1BxHT5up4iidbRf5TllcyVmcwsnYOVirxCXIXdqGx8hoSjXmI%2Bx%2BvzHFE3p1y2gV9szcq6tZdBUVENJ%2Fww5pSfFHlvCkNJZGJstJZHJx93x4obE2%2Bt%2Fje2K3WehrmBhRMCQ5JJhDh8Cj0itFTvrLKdfaRSvXsocI43w%2B3Ot8TJBdgvV%2BQxQ7TuTGCYR83%2BD4IuAILPa7zmjTy7yd0ANUzLD5Ve7%2Br5f6UnTEEgBtstiUJUtPqbZOSxavVudcxz%2BZqOv1j5TOP2ZYP7tcv6c7Z3zugfloWk5p27DHX81xCAV9YOQHYP5wIWNp5gYvJY%2FesvPvF42gU0I9V2kHm%2B6VMvo0MGMrTGEtbHpURFiytPIvXEDwxP0svwdXw7P4NueSMu9j%2Fa3dhiCsUtm9utQcbi1zjluyEEymDzr%2B26jrWORwi2zXg0dKBrIJ89VlBXmqzDQOfvcSBiiMPrqj70GOqUBr5xc6ZdcsNfPd6BpIFp4tDcXVUWc%2BBjAOFosJrYD3jbl4pww5OKWM6SW48wcf3zocLqFPl27L0UAkzMyKG6NoNizmnk%2BGCacZNJ6cBhFby6xo%2BI7scisrcl0jhOvlBBfMkO9Wjhqvf0MUnHP0I8NTgrP6%2Fy87hltIDBDEH10lJn7GcWEX30DUdJ13lWynI1WWZ46tBgKaModlD0J1VMwkRebI1gp&X-Amz-Signature=0c79124b8add494a99187c0e67b61164bf8fe0468209b4b1f1059275478b296f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY5BXR7W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDuOuCbDufyg0HsT46RGx1clP%2Fn%2FU0quDtDAPr6KIt3pAIgZ2E5kxydV6MNltZpuRAbLGU1nC5ig2DbSTN7sAFnVbMq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDB52DLnY9RStGdlYAircA2X%2FpV%2B043IcKE1TFymJabepmKJSvCVoCoot%2BComhrvCr82Yl0vc9EQ5DPscuxi8ONXt7xbYul66NQspLwUq6Fclye7F3JuhjTG%2BeAe4uSXyc1267ZVxd7gy%2BB0So4N0gR0Iftk87KW9zGd409Q3ufxtIMJkZe2ysQfuIwVMGw08Ci6DG1BxHT5up4iidbRf5TllcyVmcwsnYOVirxCXIXdqGx8hoSjXmI%2Bx%2BvzHFE3p1y2gV9szcq6tZdBUVENJ%2Fww5pSfFHlvCkNJZGJstJZHJx93x4obE2%2Bt%2Fje2K3WehrmBhRMCQ5JJhDh8Cj0itFTvrLKdfaRSvXsocI43w%2B3Ot8TJBdgvV%2BQxQ7TuTGCYR83%2BD4IuAILPa7zmjTy7yd0ANUzLD5Ve7%2Br5f6UnTEEgBtstiUJUtPqbZOSxavVudcxz%2BZqOv1j5TOP2ZYP7tcv6c7Z3zugfloWk5p27DHX81xCAV9YOQHYP5wIWNp5gYvJY%2FesvPvF42gU0I9V2kHm%2B6VMvo0MGMrTGEtbHpURFiytPIvXEDwxP0svwdXw7P4NueSMu9j%2Fa3dhiCsUtm9utQcbi1zjluyEEymDzr%2B26jrWORwi2zXg0dKBrIJ89VlBXmqzDQOfvcSBiiMPrqj70GOqUBr5xc6ZdcsNfPd6BpIFp4tDcXVUWc%2BBjAOFosJrYD3jbl4pww5OKWM6SW48wcf3zocLqFPl27L0UAkzMyKG6NoNizmnk%2BGCacZNJ6cBhFby6xo%2BI7scisrcl0jhOvlBBfMkO9Wjhqvf0MUnHP0I8NTgrP6%2Fy87hltIDBDEH10lJn7GcWEX30DUdJ13lWynI1WWZ46tBgKaModlD0J1VMwkRebI1gp&X-Amz-Signature=66c3ee8349ec8d4f09aa519a7684d6fd62efd7825da49a603431b4b43114b5b8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY5BXR7W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDuOuCbDufyg0HsT46RGx1clP%2Fn%2FU0quDtDAPr6KIt3pAIgZ2E5kxydV6MNltZpuRAbLGU1nC5ig2DbSTN7sAFnVbMq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDB52DLnY9RStGdlYAircA2X%2FpV%2B043IcKE1TFymJabepmKJSvCVoCoot%2BComhrvCr82Yl0vc9EQ5DPscuxi8ONXt7xbYul66NQspLwUq6Fclye7F3JuhjTG%2BeAe4uSXyc1267ZVxd7gy%2BB0So4N0gR0Iftk87KW9zGd409Q3ufxtIMJkZe2ysQfuIwVMGw08Ci6DG1BxHT5up4iidbRf5TllcyVmcwsnYOVirxCXIXdqGx8hoSjXmI%2Bx%2BvzHFE3p1y2gV9szcq6tZdBUVENJ%2Fww5pSfFHlvCkNJZGJstJZHJx93x4obE2%2Bt%2Fje2K3WehrmBhRMCQ5JJhDh8Cj0itFTvrLKdfaRSvXsocI43w%2B3Ot8TJBdgvV%2BQxQ7TuTGCYR83%2BD4IuAILPa7zmjTy7yd0ANUzLD5Ve7%2Br5f6UnTEEgBtstiUJUtPqbZOSxavVudcxz%2BZqOv1j5TOP2ZYP7tcv6c7Z3zugfloWk5p27DHX81xCAV9YOQHYP5wIWNp5gYvJY%2FesvPvF42gU0I9V2kHm%2B6VMvo0MGMrTGEtbHpURFiytPIvXEDwxP0svwdXw7P4NueSMu9j%2Fa3dhiCsUtm9utQcbi1zjluyEEymDzr%2B26jrWORwi2zXg0dKBrIJ89VlBXmqzDQOfvcSBiiMPrqj70GOqUBr5xc6ZdcsNfPd6BpIFp4tDcXVUWc%2BBjAOFosJrYD3jbl4pww5OKWM6SW48wcf3zocLqFPl27L0UAkzMyKG6NoNizmnk%2BGCacZNJ6cBhFby6xo%2BI7scisrcl0jhOvlBBfMkO9Wjhqvf0MUnHP0I8NTgrP6%2Fy87hltIDBDEH10lJn7GcWEX30DUdJ13lWynI1WWZ46tBgKaModlD0J1VMwkRebI1gp&X-Amz-Signature=713f2100007a40bd0227d2cd8062d1183c834b23a712cd0e6525fb298962ea90&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY5BXR7W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDuOuCbDufyg0HsT46RGx1clP%2Fn%2FU0quDtDAPr6KIt3pAIgZ2E5kxydV6MNltZpuRAbLGU1nC5ig2DbSTN7sAFnVbMq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDB52DLnY9RStGdlYAircA2X%2FpV%2B043IcKE1TFymJabepmKJSvCVoCoot%2BComhrvCr82Yl0vc9EQ5DPscuxi8ONXt7xbYul66NQspLwUq6Fclye7F3JuhjTG%2BeAe4uSXyc1267ZVxd7gy%2BB0So4N0gR0Iftk87KW9zGd409Q3ufxtIMJkZe2ysQfuIwVMGw08Ci6DG1BxHT5up4iidbRf5TllcyVmcwsnYOVirxCXIXdqGx8hoSjXmI%2Bx%2BvzHFE3p1y2gV9szcq6tZdBUVENJ%2Fww5pSfFHlvCkNJZGJstJZHJx93x4obE2%2Bt%2Fje2K3WehrmBhRMCQ5JJhDh8Cj0itFTvrLKdfaRSvXsocI43w%2B3Ot8TJBdgvV%2BQxQ7TuTGCYR83%2BD4IuAILPa7zmjTy7yd0ANUzLD5Ve7%2Br5f6UnTEEgBtstiUJUtPqbZOSxavVudcxz%2BZqOv1j5TOP2ZYP7tcv6c7Z3zugfloWk5p27DHX81xCAV9YOQHYP5wIWNp5gYvJY%2FesvPvF42gU0I9V2kHm%2B6VMvo0MGMrTGEtbHpURFiytPIvXEDwxP0svwdXw7P4NueSMu9j%2Fa3dhiCsUtm9utQcbi1zjluyEEymDzr%2B26jrWORwi2zXg0dKBrIJ89VlBXmqzDQOfvcSBiiMPrqj70GOqUBr5xc6ZdcsNfPd6BpIFp4tDcXVUWc%2BBjAOFosJrYD3jbl4pww5OKWM6SW48wcf3zocLqFPl27L0UAkzMyKG6NoNizmnk%2BGCacZNJ6cBhFby6xo%2BI7scisrcl0jhOvlBBfMkO9Wjhqvf0MUnHP0I8NTgrP6%2Fy87hltIDBDEH10lJn7GcWEX30DUdJ13lWynI1WWZ46tBgKaModlD0J1VMwkRebI1gp&X-Amz-Signature=938ede6160ac390dcfd4bf588b27d64c7c982055cd66200d7706c3813300dc63&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY5BXR7W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDuOuCbDufyg0HsT46RGx1clP%2Fn%2FU0quDtDAPr6KIt3pAIgZ2E5kxydV6MNltZpuRAbLGU1nC5ig2DbSTN7sAFnVbMq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDB52DLnY9RStGdlYAircA2X%2FpV%2B043IcKE1TFymJabepmKJSvCVoCoot%2BComhrvCr82Yl0vc9EQ5DPscuxi8ONXt7xbYul66NQspLwUq6Fclye7F3JuhjTG%2BeAe4uSXyc1267ZVxd7gy%2BB0So4N0gR0Iftk87KW9zGd409Q3ufxtIMJkZe2ysQfuIwVMGw08Ci6DG1BxHT5up4iidbRf5TllcyVmcwsnYOVirxCXIXdqGx8hoSjXmI%2Bx%2BvzHFE3p1y2gV9szcq6tZdBUVENJ%2Fww5pSfFHlvCkNJZGJstJZHJx93x4obE2%2Bt%2Fje2K3WehrmBhRMCQ5JJhDh8Cj0itFTvrLKdfaRSvXsocI43w%2B3Ot8TJBdgvV%2BQxQ7TuTGCYR83%2BD4IuAILPa7zmjTy7yd0ANUzLD5Ve7%2Br5f6UnTEEgBtstiUJUtPqbZOSxavVudcxz%2BZqOv1j5TOP2ZYP7tcv6c7Z3zugfloWk5p27DHX81xCAV9YOQHYP5wIWNp5gYvJY%2FesvPvF42gU0I9V2kHm%2B6VMvo0MGMrTGEtbHpURFiytPIvXEDwxP0svwdXw7P4NueSMu9j%2Fa3dhiCsUtm9utQcbi1zjluyEEymDzr%2B26jrWORwi2zXg0dKBrIJ89VlBXmqzDQOfvcSBiiMPrqj70GOqUBr5xc6ZdcsNfPd6BpIFp4tDcXVUWc%2BBjAOFosJrYD3jbl4pww5OKWM6SW48wcf3zocLqFPl27L0UAkzMyKG6NoNizmnk%2BGCacZNJ6cBhFby6xo%2BI7scisrcl0jhOvlBBfMkO9Wjhqvf0MUnHP0I8NTgrP6%2Fy87hltIDBDEH10lJn7GcWEX30DUdJ13lWynI1WWZ46tBgKaModlD0J1VMwkRebI1gp&X-Amz-Signature=c96e4b32dc6387fa06630d091324b0cb5f79910be9ddf7cbf0ba2339eff9fd5b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZSN3H3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIH2EWmmwgHLuT39gnoWBaS2DrpQVjeTxybzRJNw0AQ6EAiEA7%2FPO7L7DmBEwYcuQ6XWeuMlC7Uk%2FYsQO0nM%2FlE7vXlIq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK%2F8csqxwMgmQZYnAyrcA%2Fg5QWFv5r%2FWRv4AXkM9AWzCeWHkImzn8zjIdL%2Fwhm%2FQxCoCmJKmjlU7b%2BFDZGY%2FOt8IQTvBhZR2LeXkGFXS8LoiY9XG33i1xUdIR2MB089KXK4LvlPzkiQ1A767p0nO9P4fBAwX2ZRViUJ5IJW0MHc3YGGl%2F%2FJ68OSTMw67CH4fiZ%2BJ2yT2cQgTCZ%2B%2FWnztrWosV%2BO2ZojCFa3%2FdeWCbFX8F1wSYFICJOZGxURqRh7Wm5VY9yoIXGzQ4DNR%2F%2FjCxCKOLqOX%2BaZ76NL5Ei2e3bRVX3UGLbyhMqiliDEfFL8muF4%2BGqTCDPh4wlzFk6PcN7kvHgwcg%2B14hNWWZC3qeUuqZqsWF8ZaN9pZl3EGrSbHZcgsG0nX6tLs0wXcIm7EDwYBHj5KxCRRVCdj9qL5p4mhm7WhorhGBPYm1csturwLt3mGmTNcu9TnM%2F5ipW8qT85vcu8yLwqFsZoXRD3CKjMYDkAb4dOlTHKHDL%2BxtEFdIEFniLxIscfmp0f3dGsr%2BLDyTHBrTTidbWUsfOaR73sl7LumZ4sg6atWGCWkBcoZeABlGRD73oBMQkpaivCIfP4m8Pe61bn2aVxz27LqdQKnF%2BWQHeF18L5ChfkUdoRjIh83aDl0vIjW2wFxMObqj70GOqUBKX5ZPHysNjSjZZ8EG%2FbAcDZodoOX8VwKNcA92R%2BlD%2FJzj%2FNMOtylI7a092nLbVx7M8QGvmryEcw%2B2vuAFvjJTzRx2oFCpKj%2BPQpmGLUbTKiIS6YZWTsMI%2B%2BpkWSce1avCEsIQGvUwqRZjLMpMTYn8AneJmzTQrVvZ%2FiF33M9buE9%2BfbVwas%2BIQ8uCzYBjo84arterXCPzHzIpzxSUkvFi0J0JabN&X-Amz-Signature=eb623097a08dfd593596814849a6adf6d2206889a6c18bb20fcea6ca14985daf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZSN3H3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIH2EWmmwgHLuT39gnoWBaS2DrpQVjeTxybzRJNw0AQ6EAiEA7%2FPO7L7DmBEwYcuQ6XWeuMlC7Uk%2FYsQO0nM%2FlE7vXlIq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK%2F8csqxwMgmQZYnAyrcA%2Fg5QWFv5r%2FWRv4AXkM9AWzCeWHkImzn8zjIdL%2Fwhm%2FQxCoCmJKmjlU7b%2BFDZGY%2FOt8IQTvBhZR2LeXkGFXS8LoiY9XG33i1xUdIR2MB089KXK4LvlPzkiQ1A767p0nO9P4fBAwX2ZRViUJ5IJW0MHc3YGGl%2F%2FJ68OSTMw67CH4fiZ%2BJ2yT2cQgTCZ%2B%2FWnztrWosV%2BO2ZojCFa3%2FdeWCbFX8F1wSYFICJOZGxURqRh7Wm5VY9yoIXGzQ4DNR%2F%2FjCxCKOLqOX%2BaZ76NL5Ei2e3bRVX3UGLbyhMqiliDEfFL8muF4%2BGqTCDPh4wlzFk6PcN7kvHgwcg%2B14hNWWZC3qeUuqZqsWF8ZaN9pZl3EGrSbHZcgsG0nX6tLs0wXcIm7EDwYBHj5KxCRRVCdj9qL5p4mhm7WhorhGBPYm1csturwLt3mGmTNcu9TnM%2F5ipW8qT85vcu8yLwqFsZoXRD3CKjMYDkAb4dOlTHKHDL%2BxtEFdIEFniLxIscfmp0f3dGsr%2BLDyTHBrTTidbWUsfOaR73sl7LumZ4sg6atWGCWkBcoZeABlGRD73oBMQkpaivCIfP4m8Pe61bn2aVxz27LqdQKnF%2BWQHeF18L5ChfkUdoRjIh83aDl0vIjW2wFxMObqj70GOqUBKX5ZPHysNjSjZZ8EG%2FbAcDZodoOX8VwKNcA92R%2BlD%2FJzj%2FNMOtylI7a092nLbVx7M8QGvmryEcw%2B2vuAFvjJTzRx2oFCpKj%2BPQpmGLUbTKiIS6YZWTsMI%2B%2BpkWSce1avCEsIQGvUwqRZjLMpMTYn8AneJmzTQrVvZ%2FiF33M9buE9%2BfbVwas%2BIQ8uCzYBjo84arterXCPzHzIpzxSUkvFi0J0JabN&X-Amz-Signature=a19c679fc637311ac52459a037c3d20ffbbda5cf5442226050a8e4bc92a11b50&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZSN3H3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIH2EWmmwgHLuT39gnoWBaS2DrpQVjeTxybzRJNw0AQ6EAiEA7%2FPO7L7DmBEwYcuQ6XWeuMlC7Uk%2FYsQO0nM%2FlE7vXlIq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK%2F8csqxwMgmQZYnAyrcA%2Fg5QWFv5r%2FWRv4AXkM9AWzCeWHkImzn8zjIdL%2Fwhm%2FQxCoCmJKmjlU7b%2BFDZGY%2FOt8IQTvBhZR2LeXkGFXS8LoiY9XG33i1xUdIR2MB089KXK4LvlPzkiQ1A767p0nO9P4fBAwX2ZRViUJ5IJW0MHc3YGGl%2F%2FJ68OSTMw67CH4fiZ%2BJ2yT2cQgTCZ%2B%2FWnztrWosV%2BO2ZojCFa3%2FdeWCbFX8F1wSYFICJOZGxURqRh7Wm5VY9yoIXGzQ4DNR%2F%2FjCxCKOLqOX%2BaZ76NL5Ei2e3bRVX3UGLbyhMqiliDEfFL8muF4%2BGqTCDPh4wlzFk6PcN7kvHgwcg%2B14hNWWZC3qeUuqZqsWF8ZaN9pZl3EGrSbHZcgsG0nX6tLs0wXcIm7EDwYBHj5KxCRRVCdj9qL5p4mhm7WhorhGBPYm1csturwLt3mGmTNcu9TnM%2F5ipW8qT85vcu8yLwqFsZoXRD3CKjMYDkAb4dOlTHKHDL%2BxtEFdIEFniLxIscfmp0f3dGsr%2BLDyTHBrTTidbWUsfOaR73sl7LumZ4sg6atWGCWkBcoZeABlGRD73oBMQkpaivCIfP4m8Pe61bn2aVxz27LqdQKnF%2BWQHeF18L5ChfkUdoRjIh83aDl0vIjW2wFxMObqj70GOqUBKX5ZPHysNjSjZZ8EG%2FbAcDZodoOX8VwKNcA92R%2BlD%2FJzj%2FNMOtylI7a092nLbVx7M8QGvmryEcw%2B2vuAFvjJTzRx2oFCpKj%2BPQpmGLUbTKiIS6YZWTsMI%2B%2BpkWSce1avCEsIQGvUwqRZjLMpMTYn8AneJmzTQrVvZ%2FiF33M9buE9%2BfbVwas%2BIQ8uCzYBjo84arterXCPzHzIpzxSUkvFi0J0JabN&X-Amz-Signature=1d97d3db12a480933885de62b8323d0669f4e6327a52c63a418f1f5502533a0c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZSN3H3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIH2EWmmwgHLuT39gnoWBaS2DrpQVjeTxybzRJNw0AQ6EAiEA7%2FPO7L7DmBEwYcuQ6XWeuMlC7Uk%2FYsQO0nM%2FlE7vXlIq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK%2F8csqxwMgmQZYnAyrcA%2Fg5QWFv5r%2FWRv4AXkM9AWzCeWHkImzn8zjIdL%2Fwhm%2FQxCoCmJKmjlU7b%2BFDZGY%2FOt8IQTvBhZR2LeXkGFXS8LoiY9XG33i1xUdIR2MB089KXK4LvlPzkiQ1A767p0nO9P4fBAwX2ZRViUJ5IJW0MHc3YGGl%2F%2FJ68OSTMw67CH4fiZ%2BJ2yT2cQgTCZ%2B%2FWnztrWosV%2BO2ZojCFa3%2FdeWCbFX8F1wSYFICJOZGxURqRh7Wm5VY9yoIXGzQ4DNR%2F%2FjCxCKOLqOX%2BaZ76NL5Ei2e3bRVX3UGLbyhMqiliDEfFL8muF4%2BGqTCDPh4wlzFk6PcN7kvHgwcg%2B14hNWWZC3qeUuqZqsWF8ZaN9pZl3EGrSbHZcgsG0nX6tLs0wXcIm7EDwYBHj5KxCRRVCdj9qL5p4mhm7WhorhGBPYm1csturwLt3mGmTNcu9TnM%2F5ipW8qT85vcu8yLwqFsZoXRD3CKjMYDkAb4dOlTHKHDL%2BxtEFdIEFniLxIscfmp0f3dGsr%2BLDyTHBrTTidbWUsfOaR73sl7LumZ4sg6atWGCWkBcoZeABlGRD73oBMQkpaivCIfP4m8Pe61bn2aVxz27LqdQKnF%2BWQHeF18L5ChfkUdoRjIh83aDl0vIjW2wFxMObqj70GOqUBKX5ZPHysNjSjZZ8EG%2FbAcDZodoOX8VwKNcA92R%2BlD%2FJzj%2FNMOtylI7a092nLbVx7M8QGvmryEcw%2B2vuAFvjJTzRx2oFCpKj%2BPQpmGLUbTKiIS6YZWTsMI%2B%2BpkWSce1avCEsIQGvUwqRZjLMpMTYn8AneJmzTQrVvZ%2FiF33M9buE9%2BfbVwas%2BIQ8uCzYBjo84arterXCPzHzIpzxSUkvFi0J0JabN&X-Amz-Signature=b7ae5cfdd823e4f2d6b9b29bc99598f1730e972ab8674b279fc441daae2b5820&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZSN3H3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIH2EWmmwgHLuT39gnoWBaS2DrpQVjeTxybzRJNw0AQ6EAiEA7%2FPO7L7DmBEwYcuQ6XWeuMlC7Uk%2FYsQO0nM%2FlE7vXlIq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK%2F8csqxwMgmQZYnAyrcA%2Fg5QWFv5r%2FWRv4AXkM9AWzCeWHkImzn8zjIdL%2Fwhm%2FQxCoCmJKmjlU7b%2BFDZGY%2FOt8IQTvBhZR2LeXkGFXS8LoiY9XG33i1xUdIR2MB089KXK4LvlPzkiQ1A767p0nO9P4fBAwX2ZRViUJ5IJW0MHc3YGGl%2F%2FJ68OSTMw67CH4fiZ%2BJ2yT2cQgTCZ%2B%2FWnztrWosV%2BO2ZojCFa3%2FdeWCbFX8F1wSYFICJOZGxURqRh7Wm5VY9yoIXGzQ4DNR%2F%2FjCxCKOLqOX%2BaZ76NL5Ei2e3bRVX3UGLbyhMqiliDEfFL8muF4%2BGqTCDPh4wlzFk6PcN7kvHgwcg%2B14hNWWZC3qeUuqZqsWF8ZaN9pZl3EGrSbHZcgsG0nX6tLs0wXcIm7EDwYBHj5KxCRRVCdj9qL5p4mhm7WhorhGBPYm1csturwLt3mGmTNcu9TnM%2F5ipW8qT85vcu8yLwqFsZoXRD3CKjMYDkAb4dOlTHKHDL%2BxtEFdIEFniLxIscfmp0f3dGsr%2BLDyTHBrTTidbWUsfOaR73sl7LumZ4sg6atWGCWkBcoZeABlGRD73oBMQkpaivCIfP4m8Pe61bn2aVxz27LqdQKnF%2BWQHeF18L5ChfkUdoRjIh83aDl0vIjW2wFxMObqj70GOqUBKX5ZPHysNjSjZZ8EG%2FbAcDZodoOX8VwKNcA92R%2BlD%2FJzj%2FNMOtylI7a092nLbVx7M8QGvmryEcw%2B2vuAFvjJTzRx2oFCpKj%2BPQpmGLUbTKiIS6YZWTsMI%2B%2BpkWSce1avCEsIQGvUwqRZjLMpMTYn8AneJmzTQrVvZ%2FiF33M9buE9%2BfbVwas%2BIQ8uCzYBjo84arterXCPzHzIpzxSUkvFi0J0JabN&X-Amz-Signature=75e51ab2781895ac95e78ec7c87650cac2962b963bdda2831ed2b30eb546125e&X-Amz-SignedHeaders=host&x-id=GetObject)
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


