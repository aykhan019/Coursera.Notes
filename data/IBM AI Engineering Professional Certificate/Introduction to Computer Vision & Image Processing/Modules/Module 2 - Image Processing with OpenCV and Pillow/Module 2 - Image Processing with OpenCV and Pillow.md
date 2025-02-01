

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYOAH7TA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDb2kqQAwH9%2BN4Wu%2ByJrFaoZq7P3gO0UM%2FmIVca%2F6qKNAiBbAXLSP40%2BWRrN9AC26wdofKYzNUnP%2F3WfeOZZqRTNoiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHObXEofHeONY89YKtwDmGIdtWxp6hAD9WmtuI%2BGmIaZ9AXA1dSEqeSnY7fu%2BamumP9N8I1ynZ9Jo4Hf0%2FZMQdEOblp3XK4R47iqZV68WXSRhKkv6DwTMV6e6OMO7xBrIYlCLWbZncCVi1cdvHmJr%2FegVMsBlxMvcDJOBGPsATM1ShtKcCCDrpOVOnORL%2FAeRWQfPfyEKUI1hwKjgBccmUmZEr9uf2mMUlerA4Lz8W%2BGxnl62iZhMWKKQz7pT%2B6i1kjLrqZSskkleBQn2IIWWKtG0fvuwq5HBhQtlfbEOTqvxcTh7AfuBbEjTina%2FuR5Y1MRoCbgwIP2kV%2BQubXaGWAMlmK7yerbIQMaUcrgrST2ixQVRch%2FsIfzT0%2BTgGd4HsktB%2FLFcglGHHm7L2ThjdCKCLpoaBN5uOvB4GgZ7hGBxPBZq1VkyuZ%2FctpLGDv2kgQ487wD5U5aHsdIPRKeM4b99sk7LisT56320LypCC0GJq3w%2BZgfd34dbs%2BY7zN1F2dxMcN1GRSZhLV2vuf3ycrQ9vLGfswiaW9cQ7nCLFoxTXSGqIFqHcQwRbXOcEASP%2F4Fd4MiBgqSuYvrr1VdYHnWKpvw5N9KD53oqEe6vAj6dBMqbZrCvHfWpkSq5Bl1gyFhkurz9p0bZjkw0aT3vAY6pgFBOVxlAcR3L1%2BWMPL9OD9uHpNFwDxLzExADyHSP4Jd37YbVaiiOQuCgzae%2BiGpo8VfEGsTdI%2BwZe6s1OqwxaDcc4UKpxf7%2F0JgW3duFF1D6KgKXSZRpK3RYK%2FgpIUl5j15Qh8iLiXMk3saY3%2ByV0G8znxO2MpnW8JBb68dwQ71bAgyPf0d968OLTh4FHGSfuehhG7OchAZXQtCn7r%2BD4pWRrsQ%2BL1g&X-Amz-Signature=e2fc7a0212b2582dbd76830d6cfc7363715fc1b8268c71129ea51e978e648487&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLTH22A6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BoGfPjNhwXekBwziq0NXPY8EbjEIfUJSLs3TbY4SqCAiEApkVSI6PMmXRgidUydbNy9cNNSOlauZg%2FRoaYMtvoi0kqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGRHvFffDMHIecNFayrcA3jxc1xX%2FQDtPfGvUN8o%2BAgLIUYQRpfdpV8zOujbk7NL6wcASfmHoF7U%2F18KxcSN4SMjMv3hEhKQM%2FNwT0vPu7hqwXzTrf5vVlZvJjIs%2FLCRHuE9o7P8MeqRDaPQlmTKLHvyUvTaFHn9hJXR8975tIzID8P7Ljm3IEsz3jFIu8X0ruM8%2FXD6ajokxyPFKoEygc49%2FE7VUcQxf%2BQq%2FoeLOaFsiZtMfBvuV2jBpap7WunTIFKYX0UPeEdIjsX8ySLXMF3OUiz8e0gSii7V1srSyAUUmCbn01Nm9S%2FHIrocbrdiI7p8Aou%2BwpkWg1g4Dj%2FlExo8YVSJ7G7y7TDNxUyTpDoSpfHtOXJeQ%2BM%2FKKe9oHv3qPKSya64oxMbzc7Ztf1gpQ16oPewLZBh1zn56Qb9pxht3nbSxwD7JrRiPN2l30oUNlOS0y%2F859%2F%2BFoLaUrJcWEBOoz3e9JTkdakeTLMZ%2FyoZyJeT1JEelI2mm9HP50QOsxeTxNQ6tq3n0Wl%2BLCxxbJC1kgSmpYtAMu2dxvBV0uvYwCJW54WTOB%2BaKQ7LFO0kdrvK8%2B4PiE9bhiu4NQ4Z3O%2FfBJP6wDCH3y5AN9hmHrUcnOh16ZtYzpJJY8gjrWPmhkXbwrklvO8WRBZbML2k97wGOqUBMGLOvcRtyVqNAuqizr9oK%2FLgM5CRZuJDalAtWimCepqWQDmtP8zOlPjSWWVAVldQCZV0ZXekwj8hDtQlCJ61FfHjjswzd%2Fbt08e%2FYnS%2F3p7pcWerfnickFS0h9jw3ZxYxQlDHOmYrJj6Q9f%2FkXjb3I9D8jNfhNZY4KfbDIU%2BfOIGWqB412zKUYr7rARiIVg596IWgoMUC4EQzn6NaSYITNPvNzYr&X-Amz-Signature=7105265930497bb2cd9f14bc29816a9f46f033ccaf7a87910b945da653e6a1b4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLTH22A6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BoGfPjNhwXekBwziq0NXPY8EbjEIfUJSLs3TbY4SqCAiEApkVSI6PMmXRgidUydbNy9cNNSOlauZg%2FRoaYMtvoi0kqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGRHvFffDMHIecNFayrcA3jxc1xX%2FQDtPfGvUN8o%2BAgLIUYQRpfdpV8zOujbk7NL6wcASfmHoF7U%2F18KxcSN4SMjMv3hEhKQM%2FNwT0vPu7hqwXzTrf5vVlZvJjIs%2FLCRHuE9o7P8MeqRDaPQlmTKLHvyUvTaFHn9hJXR8975tIzID8P7Ljm3IEsz3jFIu8X0ruM8%2FXD6ajokxyPFKoEygc49%2FE7VUcQxf%2BQq%2FoeLOaFsiZtMfBvuV2jBpap7WunTIFKYX0UPeEdIjsX8ySLXMF3OUiz8e0gSii7V1srSyAUUmCbn01Nm9S%2FHIrocbrdiI7p8Aou%2BwpkWg1g4Dj%2FlExo8YVSJ7G7y7TDNxUyTpDoSpfHtOXJeQ%2BM%2FKKe9oHv3qPKSya64oxMbzc7Ztf1gpQ16oPewLZBh1zn56Qb9pxht3nbSxwD7JrRiPN2l30oUNlOS0y%2F859%2F%2BFoLaUrJcWEBOoz3e9JTkdakeTLMZ%2FyoZyJeT1JEelI2mm9HP50QOsxeTxNQ6tq3n0Wl%2BLCxxbJC1kgSmpYtAMu2dxvBV0uvYwCJW54WTOB%2BaKQ7LFO0kdrvK8%2B4PiE9bhiu4NQ4Z3O%2FfBJP6wDCH3y5AN9hmHrUcnOh16ZtYzpJJY8gjrWPmhkXbwrklvO8WRBZbML2k97wGOqUBMGLOvcRtyVqNAuqizr9oK%2FLgM5CRZuJDalAtWimCepqWQDmtP8zOlPjSWWVAVldQCZV0ZXekwj8hDtQlCJ61FfHjjswzd%2Fbt08e%2FYnS%2F3p7pcWerfnickFS0h9jw3ZxYxQlDHOmYrJj6Q9f%2FkXjb3I9D8jNfhNZY4KfbDIU%2BfOIGWqB412zKUYr7rARiIVg596IWgoMUC4EQzn6NaSYITNPvNzYr&X-Amz-Signature=42bd3288df7ba27c809d0e681c8ac1c6973befc30368e9dc6d6a93a98c07ab93&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLTH22A6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BoGfPjNhwXekBwziq0NXPY8EbjEIfUJSLs3TbY4SqCAiEApkVSI6PMmXRgidUydbNy9cNNSOlauZg%2FRoaYMtvoi0kqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGRHvFffDMHIecNFayrcA3jxc1xX%2FQDtPfGvUN8o%2BAgLIUYQRpfdpV8zOujbk7NL6wcASfmHoF7U%2F18KxcSN4SMjMv3hEhKQM%2FNwT0vPu7hqwXzTrf5vVlZvJjIs%2FLCRHuE9o7P8MeqRDaPQlmTKLHvyUvTaFHn9hJXR8975tIzID8P7Ljm3IEsz3jFIu8X0ruM8%2FXD6ajokxyPFKoEygc49%2FE7VUcQxf%2BQq%2FoeLOaFsiZtMfBvuV2jBpap7WunTIFKYX0UPeEdIjsX8ySLXMF3OUiz8e0gSii7V1srSyAUUmCbn01Nm9S%2FHIrocbrdiI7p8Aou%2BwpkWg1g4Dj%2FlExo8YVSJ7G7y7TDNxUyTpDoSpfHtOXJeQ%2BM%2FKKe9oHv3qPKSya64oxMbzc7Ztf1gpQ16oPewLZBh1zn56Qb9pxht3nbSxwD7JrRiPN2l30oUNlOS0y%2F859%2F%2BFoLaUrJcWEBOoz3e9JTkdakeTLMZ%2FyoZyJeT1JEelI2mm9HP50QOsxeTxNQ6tq3n0Wl%2BLCxxbJC1kgSmpYtAMu2dxvBV0uvYwCJW54WTOB%2BaKQ7LFO0kdrvK8%2B4PiE9bhiu4NQ4Z3O%2FfBJP6wDCH3y5AN9hmHrUcnOh16ZtYzpJJY8gjrWPmhkXbwrklvO8WRBZbML2k97wGOqUBMGLOvcRtyVqNAuqizr9oK%2FLgM5CRZuJDalAtWimCepqWQDmtP8zOlPjSWWVAVldQCZV0ZXekwj8hDtQlCJ61FfHjjswzd%2Fbt08e%2FYnS%2F3p7pcWerfnickFS0h9jw3ZxYxQlDHOmYrJj6Q9f%2FkXjb3I9D8jNfhNZY4KfbDIU%2BfOIGWqB412zKUYr7rARiIVg596IWgoMUC4EQzn6NaSYITNPvNzYr&X-Amz-Signature=6cdc8b2ccbef7778145eaa879db0169921c6520766cca7dc8f14a1324a3bb5be&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLTH22A6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BoGfPjNhwXekBwziq0NXPY8EbjEIfUJSLs3TbY4SqCAiEApkVSI6PMmXRgidUydbNy9cNNSOlauZg%2FRoaYMtvoi0kqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGRHvFffDMHIecNFayrcA3jxc1xX%2FQDtPfGvUN8o%2BAgLIUYQRpfdpV8zOujbk7NL6wcASfmHoF7U%2F18KxcSN4SMjMv3hEhKQM%2FNwT0vPu7hqwXzTrf5vVlZvJjIs%2FLCRHuE9o7P8MeqRDaPQlmTKLHvyUvTaFHn9hJXR8975tIzID8P7Ljm3IEsz3jFIu8X0ruM8%2FXD6ajokxyPFKoEygc49%2FE7VUcQxf%2BQq%2FoeLOaFsiZtMfBvuV2jBpap7WunTIFKYX0UPeEdIjsX8ySLXMF3OUiz8e0gSii7V1srSyAUUmCbn01Nm9S%2FHIrocbrdiI7p8Aou%2BwpkWg1g4Dj%2FlExo8YVSJ7G7y7TDNxUyTpDoSpfHtOXJeQ%2BM%2FKKe9oHv3qPKSya64oxMbzc7Ztf1gpQ16oPewLZBh1zn56Qb9pxht3nbSxwD7JrRiPN2l30oUNlOS0y%2F859%2F%2BFoLaUrJcWEBOoz3e9JTkdakeTLMZ%2FyoZyJeT1JEelI2mm9HP50QOsxeTxNQ6tq3n0Wl%2BLCxxbJC1kgSmpYtAMu2dxvBV0uvYwCJW54WTOB%2BaKQ7LFO0kdrvK8%2B4PiE9bhiu4NQ4Z3O%2FfBJP6wDCH3y5AN9hmHrUcnOh16ZtYzpJJY8gjrWPmhkXbwrklvO8WRBZbML2k97wGOqUBMGLOvcRtyVqNAuqizr9oK%2FLgM5CRZuJDalAtWimCepqWQDmtP8zOlPjSWWVAVldQCZV0ZXekwj8hDtQlCJ61FfHjjswzd%2Fbt08e%2FYnS%2F3p7pcWerfnickFS0h9jw3ZxYxQlDHOmYrJj6Q9f%2FkXjb3I9D8jNfhNZY4KfbDIU%2BfOIGWqB412zKUYr7rARiIVg596IWgoMUC4EQzn6NaSYITNPvNzYr&X-Amz-Signature=9285a71f9ba975c128728066d23e85ced45116d0d3ce40be059da3a71cd94704&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLTH22A6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BoGfPjNhwXekBwziq0NXPY8EbjEIfUJSLs3TbY4SqCAiEApkVSI6PMmXRgidUydbNy9cNNSOlauZg%2FRoaYMtvoi0kqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGRHvFffDMHIecNFayrcA3jxc1xX%2FQDtPfGvUN8o%2BAgLIUYQRpfdpV8zOujbk7NL6wcASfmHoF7U%2F18KxcSN4SMjMv3hEhKQM%2FNwT0vPu7hqwXzTrf5vVlZvJjIs%2FLCRHuE9o7P8MeqRDaPQlmTKLHvyUvTaFHn9hJXR8975tIzID8P7Ljm3IEsz3jFIu8X0ruM8%2FXD6ajokxyPFKoEygc49%2FE7VUcQxf%2BQq%2FoeLOaFsiZtMfBvuV2jBpap7WunTIFKYX0UPeEdIjsX8ySLXMF3OUiz8e0gSii7V1srSyAUUmCbn01Nm9S%2FHIrocbrdiI7p8Aou%2BwpkWg1g4Dj%2FlExo8YVSJ7G7y7TDNxUyTpDoSpfHtOXJeQ%2BM%2FKKe9oHv3qPKSya64oxMbzc7Ztf1gpQ16oPewLZBh1zn56Qb9pxht3nbSxwD7JrRiPN2l30oUNlOS0y%2F859%2F%2BFoLaUrJcWEBOoz3e9JTkdakeTLMZ%2FyoZyJeT1JEelI2mm9HP50QOsxeTxNQ6tq3n0Wl%2BLCxxbJC1kgSmpYtAMu2dxvBV0uvYwCJW54WTOB%2BaKQ7LFO0kdrvK8%2B4PiE9bhiu4NQ4Z3O%2FfBJP6wDCH3y5AN9hmHrUcnOh16ZtYzpJJY8gjrWPmhkXbwrklvO8WRBZbML2k97wGOqUBMGLOvcRtyVqNAuqizr9oK%2FLgM5CRZuJDalAtWimCepqWQDmtP8zOlPjSWWVAVldQCZV0ZXekwj8hDtQlCJ61FfHjjswzd%2Fbt08e%2FYnS%2F3p7pcWerfnickFS0h9jw3ZxYxQlDHOmYrJj6Q9f%2FkXjb3I9D8jNfhNZY4KfbDIU%2BfOIGWqB412zKUYr7rARiIVg596IWgoMUC4EQzn6NaSYITNPvNzYr&X-Amz-Signature=7ded8e4a57d1ffb6887b8b7713959ed6474af08e0179d648ffd2c652c640efc2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYOAH7TA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDb2kqQAwH9%2BN4Wu%2ByJrFaoZq7P3gO0UM%2FmIVca%2F6qKNAiBbAXLSP40%2BWRrN9AC26wdofKYzNUnP%2F3WfeOZZqRTNoiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHObXEofHeONY89YKtwDmGIdtWxp6hAD9WmtuI%2BGmIaZ9AXA1dSEqeSnY7fu%2BamumP9N8I1ynZ9Jo4Hf0%2FZMQdEOblp3XK4R47iqZV68WXSRhKkv6DwTMV6e6OMO7xBrIYlCLWbZncCVi1cdvHmJr%2FegVMsBlxMvcDJOBGPsATM1ShtKcCCDrpOVOnORL%2FAeRWQfPfyEKUI1hwKjgBccmUmZEr9uf2mMUlerA4Lz8W%2BGxnl62iZhMWKKQz7pT%2B6i1kjLrqZSskkleBQn2IIWWKtG0fvuwq5HBhQtlfbEOTqvxcTh7AfuBbEjTina%2FuR5Y1MRoCbgwIP2kV%2BQubXaGWAMlmK7yerbIQMaUcrgrST2ixQVRch%2FsIfzT0%2BTgGd4HsktB%2FLFcglGHHm7L2ThjdCKCLpoaBN5uOvB4GgZ7hGBxPBZq1VkyuZ%2FctpLGDv2kgQ487wD5U5aHsdIPRKeM4b99sk7LisT56320LypCC0GJq3w%2BZgfd34dbs%2BY7zN1F2dxMcN1GRSZhLV2vuf3ycrQ9vLGfswiaW9cQ7nCLFoxTXSGqIFqHcQwRbXOcEASP%2F4Fd4MiBgqSuYvrr1VdYHnWKpvw5N9KD53oqEe6vAj6dBMqbZrCvHfWpkSq5Bl1gyFhkurz9p0bZjkw0aT3vAY6pgFBOVxlAcR3L1%2BWMPL9OD9uHpNFwDxLzExADyHSP4Jd37YbVaiiOQuCgzae%2BiGpo8VfEGsTdI%2BwZe6s1OqwxaDcc4UKpxf7%2F0JgW3duFF1D6KgKXSZRpK3RYK%2FgpIUl5j15Qh8iLiXMk3saY3%2ByV0G8znxO2MpnW8JBb68dwQ71bAgyPf0d968OLTh4FHGSfuehhG7OchAZXQtCn7r%2BD4pWRrsQ%2BL1g&X-Amz-Signature=d9bc0324d793d84bb33573d0b09b363409303ee00103d054778ca7c11150dfc1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYOAH7TA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDb2kqQAwH9%2BN4Wu%2ByJrFaoZq7P3gO0UM%2FmIVca%2F6qKNAiBbAXLSP40%2BWRrN9AC26wdofKYzNUnP%2F3WfeOZZqRTNoiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHObXEofHeONY89YKtwDmGIdtWxp6hAD9WmtuI%2BGmIaZ9AXA1dSEqeSnY7fu%2BamumP9N8I1ynZ9Jo4Hf0%2FZMQdEOblp3XK4R47iqZV68WXSRhKkv6DwTMV6e6OMO7xBrIYlCLWbZncCVi1cdvHmJr%2FegVMsBlxMvcDJOBGPsATM1ShtKcCCDrpOVOnORL%2FAeRWQfPfyEKUI1hwKjgBccmUmZEr9uf2mMUlerA4Lz8W%2BGxnl62iZhMWKKQz7pT%2B6i1kjLrqZSskkleBQn2IIWWKtG0fvuwq5HBhQtlfbEOTqvxcTh7AfuBbEjTina%2FuR5Y1MRoCbgwIP2kV%2BQubXaGWAMlmK7yerbIQMaUcrgrST2ixQVRch%2FsIfzT0%2BTgGd4HsktB%2FLFcglGHHm7L2ThjdCKCLpoaBN5uOvB4GgZ7hGBxPBZq1VkyuZ%2FctpLGDv2kgQ487wD5U5aHsdIPRKeM4b99sk7LisT56320LypCC0GJq3w%2BZgfd34dbs%2BY7zN1F2dxMcN1GRSZhLV2vuf3ycrQ9vLGfswiaW9cQ7nCLFoxTXSGqIFqHcQwRbXOcEASP%2F4Fd4MiBgqSuYvrr1VdYHnWKpvw5N9KD53oqEe6vAj6dBMqbZrCvHfWpkSq5Bl1gyFhkurz9p0bZjkw0aT3vAY6pgFBOVxlAcR3L1%2BWMPL9OD9uHpNFwDxLzExADyHSP4Jd37YbVaiiOQuCgzae%2BiGpo8VfEGsTdI%2BwZe6s1OqwxaDcc4UKpxf7%2F0JgW3duFF1D6KgKXSZRpK3RYK%2FgpIUl5j15Qh8iLiXMk3saY3%2ByV0G8znxO2MpnW8JBb68dwQ71bAgyPf0d968OLTh4FHGSfuehhG7OchAZXQtCn7r%2BD4pWRrsQ%2BL1g&X-Amz-Signature=71e31da543d2ba89434aa5747bc44330e052e7f9cf2a222a0ea278ba7f4ef375&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYOAH7TA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDb2kqQAwH9%2BN4Wu%2ByJrFaoZq7P3gO0UM%2FmIVca%2F6qKNAiBbAXLSP40%2BWRrN9AC26wdofKYzNUnP%2F3WfeOZZqRTNoiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHObXEofHeONY89YKtwDmGIdtWxp6hAD9WmtuI%2BGmIaZ9AXA1dSEqeSnY7fu%2BamumP9N8I1ynZ9Jo4Hf0%2FZMQdEOblp3XK4R47iqZV68WXSRhKkv6DwTMV6e6OMO7xBrIYlCLWbZncCVi1cdvHmJr%2FegVMsBlxMvcDJOBGPsATM1ShtKcCCDrpOVOnORL%2FAeRWQfPfyEKUI1hwKjgBccmUmZEr9uf2mMUlerA4Lz8W%2BGxnl62iZhMWKKQz7pT%2B6i1kjLrqZSskkleBQn2IIWWKtG0fvuwq5HBhQtlfbEOTqvxcTh7AfuBbEjTina%2FuR5Y1MRoCbgwIP2kV%2BQubXaGWAMlmK7yerbIQMaUcrgrST2ixQVRch%2FsIfzT0%2BTgGd4HsktB%2FLFcglGHHm7L2ThjdCKCLpoaBN5uOvB4GgZ7hGBxPBZq1VkyuZ%2FctpLGDv2kgQ487wD5U5aHsdIPRKeM4b99sk7LisT56320LypCC0GJq3w%2BZgfd34dbs%2BY7zN1F2dxMcN1GRSZhLV2vuf3ycrQ9vLGfswiaW9cQ7nCLFoxTXSGqIFqHcQwRbXOcEASP%2F4Fd4MiBgqSuYvrr1VdYHnWKpvw5N9KD53oqEe6vAj6dBMqbZrCvHfWpkSq5Bl1gyFhkurz9p0bZjkw0aT3vAY6pgFBOVxlAcR3L1%2BWMPL9OD9uHpNFwDxLzExADyHSP4Jd37YbVaiiOQuCgzae%2BiGpo8VfEGsTdI%2BwZe6s1OqwxaDcc4UKpxf7%2F0JgW3duFF1D6KgKXSZRpK3RYK%2FgpIUl5j15Qh8iLiXMk3saY3%2ByV0G8znxO2MpnW8JBb68dwQ71bAgyPf0d968OLTh4FHGSfuehhG7OchAZXQtCn7r%2BD4pWRrsQ%2BL1g&X-Amz-Signature=0e20c92704f51c843b13feedd3082dbdc849e8b84ca5a5e18b0abd6dbb26e383&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYOAH7TA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDb2kqQAwH9%2BN4Wu%2ByJrFaoZq7P3gO0UM%2FmIVca%2F6qKNAiBbAXLSP40%2BWRrN9AC26wdofKYzNUnP%2F3WfeOZZqRTNoiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHObXEofHeONY89YKtwDmGIdtWxp6hAD9WmtuI%2BGmIaZ9AXA1dSEqeSnY7fu%2BamumP9N8I1ynZ9Jo4Hf0%2FZMQdEOblp3XK4R47iqZV68WXSRhKkv6DwTMV6e6OMO7xBrIYlCLWbZncCVi1cdvHmJr%2FegVMsBlxMvcDJOBGPsATM1ShtKcCCDrpOVOnORL%2FAeRWQfPfyEKUI1hwKjgBccmUmZEr9uf2mMUlerA4Lz8W%2BGxnl62iZhMWKKQz7pT%2B6i1kjLrqZSskkleBQn2IIWWKtG0fvuwq5HBhQtlfbEOTqvxcTh7AfuBbEjTina%2FuR5Y1MRoCbgwIP2kV%2BQubXaGWAMlmK7yerbIQMaUcrgrST2ixQVRch%2FsIfzT0%2BTgGd4HsktB%2FLFcglGHHm7L2ThjdCKCLpoaBN5uOvB4GgZ7hGBxPBZq1VkyuZ%2FctpLGDv2kgQ487wD5U5aHsdIPRKeM4b99sk7LisT56320LypCC0GJq3w%2BZgfd34dbs%2BY7zN1F2dxMcN1GRSZhLV2vuf3ycrQ9vLGfswiaW9cQ7nCLFoxTXSGqIFqHcQwRbXOcEASP%2F4Fd4MiBgqSuYvrr1VdYHnWKpvw5N9KD53oqEe6vAj6dBMqbZrCvHfWpkSq5Bl1gyFhkurz9p0bZjkw0aT3vAY6pgFBOVxlAcR3L1%2BWMPL9OD9uHpNFwDxLzExADyHSP4Jd37YbVaiiOQuCgzae%2BiGpo8VfEGsTdI%2BwZe6s1OqwxaDcc4UKpxf7%2F0JgW3duFF1D6KgKXSZRpK3RYK%2FgpIUl5j15Qh8iLiXMk3saY3%2ByV0G8znxO2MpnW8JBb68dwQ71bAgyPf0d968OLTh4FHGSfuehhG7OchAZXQtCn7r%2BD4pWRrsQ%2BL1g&X-Amz-Signature=14c6cc8693683a72f3759cc2c39f211796ab8f03e35894c6e7fb6aaecb9655e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYOAH7TA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDb2kqQAwH9%2BN4Wu%2ByJrFaoZq7P3gO0UM%2FmIVca%2F6qKNAiBbAXLSP40%2BWRrN9AC26wdofKYzNUnP%2F3WfeOZZqRTNoiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHObXEofHeONY89YKtwDmGIdtWxp6hAD9WmtuI%2BGmIaZ9AXA1dSEqeSnY7fu%2BamumP9N8I1ynZ9Jo4Hf0%2FZMQdEOblp3XK4R47iqZV68WXSRhKkv6DwTMV6e6OMO7xBrIYlCLWbZncCVi1cdvHmJr%2FegVMsBlxMvcDJOBGPsATM1ShtKcCCDrpOVOnORL%2FAeRWQfPfyEKUI1hwKjgBccmUmZEr9uf2mMUlerA4Lz8W%2BGxnl62iZhMWKKQz7pT%2B6i1kjLrqZSskkleBQn2IIWWKtG0fvuwq5HBhQtlfbEOTqvxcTh7AfuBbEjTina%2FuR5Y1MRoCbgwIP2kV%2BQubXaGWAMlmK7yerbIQMaUcrgrST2ixQVRch%2FsIfzT0%2BTgGd4HsktB%2FLFcglGHHm7L2ThjdCKCLpoaBN5uOvB4GgZ7hGBxPBZq1VkyuZ%2FctpLGDv2kgQ487wD5U5aHsdIPRKeM4b99sk7LisT56320LypCC0GJq3w%2BZgfd34dbs%2BY7zN1F2dxMcN1GRSZhLV2vuf3ycrQ9vLGfswiaW9cQ7nCLFoxTXSGqIFqHcQwRbXOcEASP%2F4Fd4MiBgqSuYvrr1VdYHnWKpvw5N9KD53oqEe6vAj6dBMqbZrCvHfWpkSq5Bl1gyFhkurz9p0bZjkw0aT3vAY6pgFBOVxlAcR3L1%2BWMPL9OD9uHpNFwDxLzExADyHSP4Jd37YbVaiiOQuCgzae%2BiGpo8VfEGsTdI%2BwZe6s1OqwxaDcc4UKpxf7%2F0JgW3duFF1D6KgKXSZRpK3RYK%2FgpIUl5j15Qh8iLiXMk3saY3%2ByV0G8znxO2MpnW8JBb68dwQ71bAgyPf0d968OLTh4FHGSfuehhG7OchAZXQtCn7r%2BD4pWRrsQ%2BL1g&X-Amz-Signature=da8602210be93fa84c26f8eb5400fcce0ccd16668d9b9f0fced3552465262954&X-Amz-SignedHeaders=host&x-id=GetObject)
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


