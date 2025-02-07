

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PGGNMZX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCQSR3%2B0wKn7lWcYjwC6PcTTR8dgz%2BU7UHUNJpFad647QIhAP9XDpA7YZIBNBSzAWB29GIYK0sXjph1zTsmTmaYuRBPKv8DCHUQABoMNjM3NDIzMTgzODA1IgwZ7LvUF%2BMO6tsxKlQq3ANqE0s9CVI9%2Fp%2BPhvidwojoA6c9AFQo3zDa7LBiAON0D%2Fj3xnHYx8mDVFpZzn6ief2nzRQEyyOSZ0txHibJKvL7jlqescXH1g2OiGGhtllznC2MuQbSlJ3Yb5b%2F7CwhXbZ%2FpENQVzbcXLuOrhp3IaUtp1Q9v1wbcbdF%2F4nKnE8%2FJ9K8Wy%2FxPCxiFZh7IFFKNGygHRO9J3s1PO5oiekqK8pN0rO0h8idXmRhGvh8cRoAnVrwcZfRvGTmqqpIZ05zhLvUK0xpzxj4N2K0yW%2BK9IXjSn5qlhISWstu8BXAJS%2Bxxg%2B68Zm4xQqSU2hkbCl37ItGv%2BFX20gAb7D%2F9eb8v8YKr1gsKybqX6OftaEP3uspZU1mo%2By1myvJ8XeMAKD7x67xCq1X34JxBMFvkbyq8PtpoTmtt%2B5JRg7IRuD2coBuTvXPxUQc9hnt4AQnmNqP99%2FlTt1QMk5OvWBhI7YfzxqZxtrn9T5UVgpbzvvpr%2BpyNvu7m8fNE71nz3vIKHjZor1X8ycinEiy8XdFmMaB%2F807zrwNE2MFjIOD8ys5RTJyi8Ehm7s2yzHoTXqpV%2F%2BebX2fZ6qHGPrOnc%2BaLCEjCGA7HtI8ZN64gLGI7ScfaP7PlEJQDjFoTzd0JfB5fDC275e9BjqkAQyP46fgA7QZ6oM9E0VMfm0htSjkBY4XYLGJ%2BbmOmlOT83ufaPAB84gVe%2F2YXnxvxN2KmuotbR9nBChx9HGjoY9KJ3CF6Pd%2B91mnz6NxW1LrJ%2FHPtv7JRPJ8J5qVfgGm3gs2RQ%2Fud76%2BdqshMbMdwsqmu2k86t7bwAhM%2BFYP76NwX0UCMU6VHO%2BKi8U8yn74%2FviNX3XX0GzQPqkABpYZXrQKi5I%2F&X-Amz-Signature=ddf206796ea573bd31a9ce9888afcb4e8e1e3a24bc865f8d3cdc9a3624b538ed&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVKB6VPP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQDlxAsm4bcDqPJZyvmTgfEP2bgZPUKf%2FY1gZDIG6%2FZbywIhAJKyFlH5elL39Kys3t1mobKHLK49ZATiZwMhoIUjN5esKv8DCHUQABoMNjM3NDIzMTgzODA1Igz3DEd9GElj1tgXm64q3ANnPWyt3iCifEjJRtIJm5a3ARf3RSmkEM%2FLh%2FRxjCAzzpf6v00AezbmfTMyrRm03Qa5j40fmaZKOkfNrN9Ni5ErSbpmxmSzhOwmIgp%2FypILQVAL%2BChiHwq%2FUEzKsVf2L4qeI%2BXFXI6joN%2BeJ9bhRM10yA50cD0DEDksMQqBPObocCi5sJFddYZKZI3hkAY99%2BZbcCwImKAmoqXPMNIQq0wgC9f43lbgfknL4nFZfy8UurWQ%2F7J56qvOrL2W04BF2Okyvo78uJdS9p%2B5N6ApB%2Ff%2FB9xdeb78Wp1j3TOkkgWfNDfB64HtNqPOeotpetmJCtaSGH0JuGwd9EgyMr%2Bo55PAXFwzo%2BH%2Fdw%2BNfrvf6qADcwFSk%2BZYpkkfHFJgQIlG%2ByxlQUjgFPiACSHPqofs8JJPC0qahbnW38qW7yTC%2FcZjOIGR9hNfubUdpvxV3jWCtyPbAhrUPY%2BlEiEtr8Ph9IrXAN%2FLc5byoBYDBYTZRGJUsj%2BifuQKWR%2BEvcrtOg4iYJA%2FMgemo%2FX32d62%2BN0VdMno7YubOyZIjj05yVODD8G8kd%2Bnc6D3hm6X41%2BHf776q19UI3W1uW8ecOZcX2WY0%2F%2FKDy84c%2BiKZ73EIxMytioI1jspDPGyrtCFidkWRTCd75e9BjqkAdsLJpIPAfjVArLDxhRy75bK7ckkIpFVqNWGGlrzIVxW9m0z5ukCgVT04bQ%2FDzXVsZnaGJedrxhiAXIrlNCDZwwqyTs9DLJAxhQCmJmu14dXJw3Vaw7lWR5sFO8Rto6B5OgB8Tq%2F20Y0iboC96Oh4%2B%2F9bBO5RwHyUDp8ME5eEvKa0dlpl3hBS0d9q8x7nJGx0CPN0q3G2BRBiRQJK7RK32B9%2FP%2F3&X-Amz-Signature=4f9c91bb427cbee2fb597cff9b2c9a119e921458e7c9b097dc8229e9224d8f13&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVKB6VPP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQDlxAsm4bcDqPJZyvmTgfEP2bgZPUKf%2FY1gZDIG6%2FZbywIhAJKyFlH5elL39Kys3t1mobKHLK49ZATiZwMhoIUjN5esKv8DCHUQABoMNjM3NDIzMTgzODA1Igz3DEd9GElj1tgXm64q3ANnPWyt3iCifEjJRtIJm5a3ARf3RSmkEM%2FLh%2FRxjCAzzpf6v00AezbmfTMyrRm03Qa5j40fmaZKOkfNrN9Ni5ErSbpmxmSzhOwmIgp%2FypILQVAL%2BChiHwq%2FUEzKsVf2L4qeI%2BXFXI6joN%2BeJ9bhRM10yA50cD0DEDksMQqBPObocCi5sJFddYZKZI3hkAY99%2BZbcCwImKAmoqXPMNIQq0wgC9f43lbgfknL4nFZfy8UurWQ%2F7J56qvOrL2W04BF2Okyvo78uJdS9p%2B5N6ApB%2Ff%2FB9xdeb78Wp1j3TOkkgWfNDfB64HtNqPOeotpetmJCtaSGH0JuGwd9EgyMr%2Bo55PAXFwzo%2BH%2Fdw%2BNfrvf6qADcwFSk%2BZYpkkfHFJgQIlG%2ByxlQUjgFPiACSHPqofs8JJPC0qahbnW38qW7yTC%2FcZjOIGR9hNfubUdpvxV3jWCtyPbAhrUPY%2BlEiEtr8Ph9IrXAN%2FLc5byoBYDBYTZRGJUsj%2BifuQKWR%2BEvcrtOg4iYJA%2FMgemo%2FX32d62%2BN0VdMno7YubOyZIjj05yVODD8G8kd%2Bnc6D3hm6X41%2BHf776q19UI3W1uW8ecOZcX2WY0%2F%2FKDy84c%2BiKZ73EIxMytioI1jspDPGyrtCFidkWRTCd75e9BjqkAdsLJpIPAfjVArLDxhRy75bK7ckkIpFVqNWGGlrzIVxW9m0z5ukCgVT04bQ%2FDzXVsZnaGJedrxhiAXIrlNCDZwwqyTs9DLJAxhQCmJmu14dXJw3Vaw7lWR5sFO8Rto6B5OgB8Tq%2F20Y0iboC96Oh4%2B%2F9bBO5RwHyUDp8ME5eEvKa0dlpl3hBS0d9q8x7nJGx0CPN0q3G2BRBiRQJK7RK32B9%2FP%2F3&X-Amz-Signature=bcf1426a980cbd0b0fd4372043ff44d08087de0778c9912766efeffb4413c918&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVKB6VPP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQDlxAsm4bcDqPJZyvmTgfEP2bgZPUKf%2FY1gZDIG6%2FZbywIhAJKyFlH5elL39Kys3t1mobKHLK49ZATiZwMhoIUjN5esKv8DCHUQABoMNjM3NDIzMTgzODA1Igz3DEd9GElj1tgXm64q3ANnPWyt3iCifEjJRtIJm5a3ARf3RSmkEM%2FLh%2FRxjCAzzpf6v00AezbmfTMyrRm03Qa5j40fmaZKOkfNrN9Ni5ErSbpmxmSzhOwmIgp%2FypILQVAL%2BChiHwq%2FUEzKsVf2L4qeI%2BXFXI6joN%2BeJ9bhRM10yA50cD0DEDksMQqBPObocCi5sJFddYZKZI3hkAY99%2BZbcCwImKAmoqXPMNIQq0wgC9f43lbgfknL4nFZfy8UurWQ%2F7J56qvOrL2W04BF2Okyvo78uJdS9p%2B5N6ApB%2Ff%2FB9xdeb78Wp1j3TOkkgWfNDfB64HtNqPOeotpetmJCtaSGH0JuGwd9EgyMr%2Bo55PAXFwzo%2BH%2Fdw%2BNfrvf6qADcwFSk%2BZYpkkfHFJgQIlG%2ByxlQUjgFPiACSHPqofs8JJPC0qahbnW38qW7yTC%2FcZjOIGR9hNfubUdpvxV3jWCtyPbAhrUPY%2BlEiEtr8Ph9IrXAN%2FLc5byoBYDBYTZRGJUsj%2BifuQKWR%2BEvcrtOg4iYJA%2FMgemo%2FX32d62%2BN0VdMno7YubOyZIjj05yVODD8G8kd%2Bnc6D3hm6X41%2BHf776q19UI3W1uW8ecOZcX2WY0%2F%2FKDy84c%2BiKZ73EIxMytioI1jspDPGyrtCFidkWRTCd75e9BjqkAdsLJpIPAfjVArLDxhRy75bK7ckkIpFVqNWGGlrzIVxW9m0z5ukCgVT04bQ%2FDzXVsZnaGJedrxhiAXIrlNCDZwwqyTs9DLJAxhQCmJmu14dXJw3Vaw7lWR5sFO8Rto6B5OgB8Tq%2F20Y0iboC96Oh4%2B%2F9bBO5RwHyUDp8ME5eEvKa0dlpl3hBS0d9q8x7nJGx0CPN0q3G2BRBiRQJK7RK32B9%2FP%2F3&X-Amz-Signature=17b56911bb2a10715eeb7293d498092334347baaeea0de5f51153ea61a0b0771&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVKB6VPP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQDlxAsm4bcDqPJZyvmTgfEP2bgZPUKf%2FY1gZDIG6%2FZbywIhAJKyFlH5elL39Kys3t1mobKHLK49ZATiZwMhoIUjN5esKv8DCHUQABoMNjM3NDIzMTgzODA1Igz3DEd9GElj1tgXm64q3ANnPWyt3iCifEjJRtIJm5a3ARf3RSmkEM%2FLh%2FRxjCAzzpf6v00AezbmfTMyrRm03Qa5j40fmaZKOkfNrN9Ni5ErSbpmxmSzhOwmIgp%2FypILQVAL%2BChiHwq%2FUEzKsVf2L4qeI%2BXFXI6joN%2BeJ9bhRM10yA50cD0DEDksMQqBPObocCi5sJFddYZKZI3hkAY99%2BZbcCwImKAmoqXPMNIQq0wgC9f43lbgfknL4nFZfy8UurWQ%2F7J56qvOrL2W04BF2Okyvo78uJdS9p%2B5N6ApB%2Ff%2FB9xdeb78Wp1j3TOkkgWfNDfB64HtNqPOeotpetmJCtaSGH0JuGwd9EgyMr%2Bo55PAXFwzo%2BH%2Fdw%2BNfrvf6qADcwFSk%2BZYpkkfHFJgQIlG%2ByxlQUjgFPiACSHPqofs8JJPC0qahbnW38qW7yTC%2FcZjOIGR9hNfubUdpvxV3jWCtyPbAhrUPY%2BlEiEtr8Ph9IrXAN%2FLc5byoBYDBYTZRGJUsj%2BifuQKWR%2BEvcrtOg4iYJA%2FMgemo%2FX32d62%2BN0VdMno7YubOyZIjj05yVODD8G8kd%2Bnc6D3hm6X41%2BHf776q19UI3W1uW8ecOZcX2WY0%2F%2FKDy84c%2BiKZ73EIxMytioI1jspDPGyrtCFidkWRTCd75e9BjqkAdsLJpIPAfjVArLDxhRy75bK7ckkIpFVqNWGGlrzIVxW9m0z5ukCgVT04bQ%2FDzXVsZnaGJedrxhiAXIrlNCDZwwqyTs9DLJAxhQCmJmu14dXJw3Vaw7lWR5sFO8Rto6B5OgB8Tq%2F20Y0iboC96Oh4%2B%2F9bBO5RwHyUDp8ME5eEvKa0dlpl3hBS0d9q8x7nJGx0CPN0q3G2BRBiRQJK7RK32B9%2FP%2F3&X-Amz-Signature=b0c43f8e0c100f18143ef8d2064d457ca3d35fde082f096f233352ed6e491d90&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVKB6VPP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQDlxAsm4bcDqPJZyvmTgfEP2bgZPUKf%2FY1gZDIG6%2FZbywIhAJKyFlH5elL39Kys3t1mobKHLK49ZATiZwMhoIUjN5esKv8DCHUQABoMNjM3NDIzMTgzODA1Igz3DEd9GElj1tgXm64q3ANnPWyt3iCifEjJRtIJm5a3ARf3RSmkEM%2FLh%2FRxjCAzzpf6v00AezbmfTMyrRm03Qa5j40fmaZKOkfNrN9Ni5ErSbpmxmSzhOwmIgp%2FypILQVAL%2BChiHwq%2FUEzKsVf2L4qeI%2BXFXI6joN%2BeJ9bhRM10yA50cD0DEDksMQqBPObocCi5sJFddYZKZI3hkAY99%2BZbcCwImKAmoqXPMNIQq0wgC9f43lbgfknL4nFZfy8UurWQ%2F7J56qvOrL2W04BF2Okyvo78uJdS9p%2B5N6ApB%2Ff%2FB9xdeb78Wp1j3TOkkgWfNDfB64HtNqPOeotpetmJCtaSGH0JuGwd9EgyMr%2Bo55PAXFwzo%2BH%2Fdw%2BNfrvf6qADcwFSk%2BZYpkkfHFJgQIlG%2ByxlQUjgFPiACSHPqofs8JJPC0qahbnW38qW7yTC%2FcZjOIGR9hNfubUdpvxV3jWCtyPbAhrUPY%2BlEiEtr8Ph9IrXAN%2FLc5byoBYDBYTZRGJUsj%2BifuQKWR%2BEvcrtOg4iYJA%2FMgemo%2FX32d62%2BN0VdMno7YubOyZIjj05yVODD8G8kd%2Bnc6D3hm6X41%2BHf776q19UI3W1uW8ecOZcX2WY0%2F%2FKDy84c%2BiKZ73EIxMytioI1jspDPGyrtCFidkWRTCd75e9BjqkAdsLJpIPAfjVArLDxhRy75bK7ckkIpFVqNWGGlrzIVxW9m0z5ukCgVT04bQ%2FDzXVsZnaGJedrxhiAXIrlNCDZwwqyTs9DLJAxhQCmJmu14dXJw3Vaw7lWR5sFO8Rto6B5OgB8Tq%2F20Y0iboC96Oh4%2B%2F9bBO5RwHyUDp8ME5eEvKa0dlpl3hBS0d9q8x7nJGx0CPN0q3G2BRBiRQJK7RK32B9%2FP%2F3&X-Amz-Signature=236a2992b445204659c797f9ac7c56428be91249e861404c3e7b8711222f6363&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PGGNMZX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCQSR3%2B0wKn7lWcYjwC6PcTTR8dgz%2BU7UHUNJpFad647QIhAP9XDpA7YZIBNBSzAWB29GIYK0sXjph1zTsmTmaYuRBPKv8DCHUQABoMNjM3NDIzMTgzODA1IgwZ7LvUF%2BMO6tsxKlQq3ANqE0s9CVI9%2Fp%2BPhvidwojoA6c9AFQo3zDa7LBiAON0D%2Fj3xnHYx8mDVFpZzn6ief2nzRQEyyOSZ0txHibJKvL7jlqescXH1g2OiGGhtllznC2MuQbSlJ3Yb5b%2F7CwhXbZ%2FpENQVzbcXLuOrhp3IaUtp1Q9v1wbcbdF%2F4nKnE8%2FJ9K8Wy%2FxPCxiFZh7IFFKNGygHRO9J3s1PO5oiekqK8pN0rO0h8idXmRhGvh8cRoAnVrwcZfRvGTmqqpIZ05zhLvUK0xpzxj4N2K0yW%2BK9IXjSn5qlhISWstu8BXAJS%2Bxxg%2B68Zm4xQqSU2hkbCl37ItGv%2BFX20gAb7D%2F9eb8v8YKr1gsKybqX6OftaEP3uspZU1mo%2By1myvJ8XeMAKD7x67xCq1X34JxBMFvkbyq8PtpoTmtt%2B5JRg7IRuD2coBuTvXPxUQc9hnt4AQnmNqP99%2FlTt1QMk5OvWBhI7YfzxqZxtrn9T5UVgpbzvvpr%2BpyNvu7m8fNE71nz3vIKHjZor1X8ycinEiy8XdFmMaB%2F807zrwNE2MFjIOD8ys5RTJyi8Ehm7s2yzHoTXqpV%2F%2BebX2fZ6qHGPrOnc%2BaLCEjCGA7HtI8ZN64gLGI7ScfaP7PlEJQDjFoTzd0JfB5fDC275e9BjqkAQyP46fgA7QZ6oM9E0VMfm0htSjkBY4XYLGJ%2BbmOmlOT83ufaPAB84gVe%2F2YXnxvxN2KmuotbR9nBChx9HGjoY9KJ3CF6Pd%2B91mnz6NxW1LrJ%2FHPtv7JRPJ8J5qVfgGm3gs2RQ%2Fud76%2BdqshMbMdwsqmu2k86t7bwAhM%2BFYP76NwX0UCMU6VHO%2BKi8U8yn74%2FviNX3XX0GzQPqkABpYZXrQKi5I%2F&X-Amz-Signature=9dbcc08a40bb662697f40842e63cbc7c271aa59b4621966b81adae47907ee836&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PGGNMZX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCQSR3%2B0wKn7lWcYjwC6PcTTR8dgz%2BU7UHUNJpFad647QIhAP9XDpA7YZIBNBSzAWB29GIYK0sXjph1zTsmTmaYuRBPKv8DCHUQABoMNjM3NDIzMTgzODA1IgwZ7LvUF%2BMO6tsxKlQq3ANqE0s9CVI9%2Fp%2BPhvidwojoA6c9AFQo3zDa7LBiAON0D%2Fj3xnHYx8mDVFpZzn6ief2nzRQEyyOSZ0txHibJKvL7jlqescXH1g2OiGGhtllznC2MuQbSlJ3Yb5b%2F7CwhXbZ%2FpENQVzbcXLuOrhp3IaUtp1Q9v1wbcbdF%2F4nKnE8%2FJ9K8Wy%2FxPCxiFZh7IFFKNGygHRO9J3s1PO5oiekqK8pN0rO0h8idXmRhGvh8cRoAnVrwcZfRvGTmqqpIZ05zhLvUK0xpzxj4N2K0yW%2BK9IXjSn5qlhISWstu8BXAJS%2Bxxg%2B68Zm4xQqSU2hkbCl37ItGv%2BFX20gAb7D%2F9eb8v8YKr1gsKybqX6OftaEP3uspZU1mo%2By1myvJ8XeMAKD7x67xCq1X34JxBMFvkbyq8PtpoTmtt%2B5JRg7IRuD2coBuTvXPxUQc9hnt4AQnmNqP99%2FlTt1QMk5OvWBhI7YfzxqZxtrn9T5UVgpbzvvpr%2BpyNvu7m8fNE71nz3vIKHjZor1X8ycinEiy8XdFmMaB%2F807zrwNE2MFjIOD8ys5RTJyi8Ehm7s2yzHoTXqpV%2F%2BebX2fZ6qHGPrOnc%2BaLCEjCGA7HtI8ZN64gLGI7ScfaP7PlEJQDjFoTzd0JfB5fDC275e9BjqkAQyP46fgA7QZ6oM9E0VMfm0htSjkBY4XYLGJ%2BbmOmlOT83ufaPAB84gVe%2F2YXnxvxN2KmuotbR9nBChx9HGjoY9KJ3CF6Pd%2B91mnz6NxW1LrJ%2FHPtv7JRPJ8J5qVfgGm3gs2RQ%2Fud76%2BdqshMbMdwsqmu2k86t7bwAhM%2BFYP76NwX0UCMU6VHO%2BKi8U8yn74%2FviNX3XX0GzQPqkABpYZXrQKi5I%2F&X-Amz-Signature=ba7b47c6aef3fa9923da69291b3874b058a2af3eeafc4ee70f6f716998fa6fef&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PGGNMZX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCQSR3%2B0wKn7lWcYjwC6PcTTR8dgz%2BU7UHUNJpFad647QIhAP9XDpA7YZIBNBSzAWB29GIYK0sXjph1zTsmTmaYuRBPKv8DCHUQABoMNjM3NDIzMTgzODA1IgwZ7LvUF%2BMO6tsxKlQq3ANqE0s9CVI9%2Fp%2BPhvidwojoA6c9AFQo3zDa7LBiAON0D%2Fj3xnHYx8mDVFpZzn6ief2nzRQEyyOSZ0txHibJKvL7jlqescXH1g2OiGGhtllznC2MuQbSlJ3Yb5b%2F7CwhXbZ%2FpENQVzbcXLuOrhp3IaUtp1Q9v1wbcbdF%2F4nKnE8%2FJ9K8Wy%2FxPCxiFZh7IFFKNGygHRO9J3s1PO5oiekqK8pN0rO0h8idXmRhGvh8cRoAnVrwcZfRvGTmqqpIZ05zhLvUK0xpzxj4N2K0yW%2BK9IXjSn5qlhISWstu8BXAJS%2Bxxg%2B68Zm4xQqSU2hkbCl37ItGv%2BFX20gAb7D%2F9eb8v8YKr1gsKybqX6OftaEP3uspZU1mo%2By1myvJ8XeMAKD7x67xCq1X34JxBMFvkbyq8PtpoTmtt%2B5JRg7IRuD2coBuTvXPxUQc9hnt4AQnmNqP99%2FlTt1QMk5OvWBhI7YfzxqZxtrn9T5UVgpbzvvpr%2BpyNvu7m8fNE71nz3vIKHjZor1X8ycinEiy8XdFmMaB%2F807zrwNE2MFjIOD8ys5RTJyi8Ehm7s2yzHoTXqpV%2F%2BebX2fZ6qHGPrOnc%2BaLCEjCGA7HtI8ZN64gLGI7ScfaP7PlEJQDjFoTzd0JfB5fDC275e9BjqkAQyP46fgA7QZ6oM9E0VMfm0htSjkBY4XYLGJ%2BbmOmlOT83ufaPAB84gVe%2F2YXnxvxN2KmuotbR9nBChx9HGjoY9KJ3CF6Pd%2B91mnz6NxW1LrJ%2FHPtv7JRPJ8J5qVfgGm3gs2RQ%2Fud76%2BdqshMbMdwsqmu2k86t7bwAhM%2BFYP76NwX0UCMU6VHO%2BKi8U8yn74%2FviNX3XX0GzQPqkABpYZXrQKi5I%2F&X-Amz-Signature=451582182eb255f5ac8a68ac780ed52868048e0af2113499ab57f92aa4091e07&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PGGNMZX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCQSR3%2B0wKn7lWcYjwC6PcTTR8dgz%2BU7UHUNJpFad647QIhAP9XDpA7YZIBNBSzAWB29GIYK0sXjph1zTsmTmaYuRBPKv8DCHUQABoMNjM3NDIzMTgzODA1IgwZ7LvUF%2BMO6tsxKlQq3ANqE0s9CVI9%2Fp%2BPhvidwojoA6c9AFQo3zDa7LBiAON0D%2Fj3xnHYx8mDVFpZzn6ief2nzRQEyyOSZ0txHibJKvL7jlqescXH1g2OiGGhtllznC2MuQbSlJ3Yb5b%2F7CwhXbZ%2FpENQVzbcXLuOrhp3IaUtp1Q9v1wbcbdF%2F4nKnE8%2FJ9K8Wy%2FxPCxiFZh7IFFKNGygHRO9J3s1PO5oiekqK8pN0rO0h8idXmRhGvh8cRoAnVrwcZfRvGTmqqpIZ05zhLvUK0xpzxj4N2K0yW%2BK9IXjSn5qlhISWstu8BXAJS%2Bxxg%2B68Zm4xQqSU2hkbCl37ItGv%2BFX20gAb7D%2F9eb8v8YKr1gsKybqX6OftaEP3uspZU1mo%2By1myvJ8XeMAKD7x67xCq1X34JxBMFvkbyq8PtpoTmtt%2B5JRg7IRuD2coBuTvXPxUQc9hnt4AQnmNqP99%2FlTt1QMk5OvWBhI7YfzxqZxtrn9T5UVgpbzvvpr%2BpyNvu7m8fNE71nz3vIKHjZor1X8ycinEiy8XdFmMaB%2F807zrwNE2MFjIOD8ys5RTJyi8Ehm7s2yzHoTXqpV%2F%2BebX2fZ6qHGPrOnc%2BaLCEjCGA7HtI8ZN64gLGI7ScfaP7PlEJQDjFoTzd0JfB5fDC275e9BjqkAQyP46fgA7QZ6oM9E0VMfm0htSjkBY4XYLGJ%2BbmOmlOT83ufaPAB84gVe%2F2YXnxvxN2KmuotbR9nBChx9HGjoY9KJ3CF6Pd%2B91mnz6NxW1LrJ%2FHPtv7JRPJ8J5qVfgGm3gs2RQ%2Fud76%2BdqshMbMdwsqmu2k86t7bwAhM%2BFYP76NwX0UCMU6VHO%2BKi8U8yn74%2FviNX3XX0GzQPqkABpYZXrQKi5I%2F&X-Amz-Signature=b434f9071d05843bf6ab1c81e13bb37cc809aff9e60d60b382fa6abb34dd2e15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PGGNMZX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCQSR3%2B0wKn7lWcYjwC6PcTTR8dgz%2BU7UHUNJpFad647QIhAP9XDpA7YZIBNBSzAWB29GIYK0sXjph1zTsmTmaYuRBPKv8DCHUQABoMNjM3NDIzMTgzODA1IgwZ7LvUF%2BMO6tsxKlQq3ANqE0s9CVI9%2Fp%2BPhvidwojoA6c9AFQo3zDa7LBiAON0D%2Fj3xnHYx8mDVFpZzn6ief2nzRQEyyOSZ0txHibJKvL7jlqescXH1g2OiGGhtllznC2MuQbSlJ3Yb5b%2F7CwhXbZ%2FpENQVzbcXLuOrhp3IaUtp1Q9v1wbcbdF%2F4nKnE8%2FJ9K8Wy%2FxPCxiFZh7IFFKNGygHRO9J3s1PO5oiekqK8pN0rO0h8idXmRhGvh8cRoAnVrwcZfRvGTmqqpIZ05zhLvUK0xpzxj4N2K0yW%2BK9IXjSn5qlhISWstu8BXAJS%2Bxxg%2B68Zm4xQqSU2hkbCl37ItGv%2BFX20gAb7D%2F9eb8v8YKr1gsKybqX6OftaEP3uspZU1mo%2By1myvJ8XeMAKD7x67xCq1X34JxBMFvkbyq8PtpoTmtt%2B5JRg7IRuD2coBuTvXPxUQc9hnt4AQnmNqP99%2FlTt1QMk5OvWBhI7YfzxqZxtrn9T5UVgpbzvvpr%2BpyNvu7m8fNE71nz3vIKHjZor1X8ycinEiy8XdFmMaB%2F807zrwNE2MFjIOD8ys5RTJyi8Ehm7s2yzHoTXqpV%2F%2BebX2fZ6qHGPrOnc%2BaLCEjCGA7HtI8ZN64gLGI7ScfaP7PlEJQDjFoTzd0JfB5fDC275e9BjqkAQyP46fgA7QZ6oM9E0VMfm0htSjkBY4XYLGJ%2BbmOmlOT83ufaPAB84gVe%2F2YXnxvxN2KmuotbR9nBChx9HGjoY9KJ3CF6Pd%2B91mnz6NxW1LrJ%2FHPtv7JRPJ8J5qVfgGm3gs2RQ%2Fud76%2BdqshMbMdwsqmu2k86t7bwAhM%2BFYP76NwX0UCMU6VHO%2BKi8U8yn74%2FviNX3XX0GzQPqkABpYZXrQKi5I%2F&X-Amz-Signature=a24046e828478d09d50ff3b87a698f67e67ce4d7b63642228b85064e0eee4145&X-Amz-SignedHeaders=host&x-id=GetObject)
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


