

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVWXF2NC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVpdEn5Uj1BFzpxtpKPQlDCzQEvQDRGrtcuIWEI3vgyAiEA3U%2B7PyZKcJp7X0b0Q0TwnFvtzOEsM6TeL%2BzyAeAK4aMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRnB4VPWljwCStAeCrcAzvxuFgUU%2FcZlXZiH%2BinD6piRS7E%2F%2BffBE9EjAqsGpwPSjRzvxfiHqDz1vU6lOLezTHyH8y5Pkj0Kw6NHwmz6tII6PU0vYuWYM2pl%2FpGjRD6y7sYIcfZwQFxSuEJ0QuiRacZos2Es0RbpltQw%2BnNVbccsC1dSyLE3MWY3TGfMiwwkOqCb6xaNkJ2uRzDXcXGkoRqrbM2qp5HtOu8Drjt8N0S4XjQaC0CJjZO65fBsZ%2BlpRsRpGsZNLMIud0q0CU%2BoP21ckOKmElnIfZY47bKeMfYfMaicbKv9UmZbLOu3QmlaGMSvUfZ53ENO1Re3t%2F73N2itnmTM1AjVp0wWYHA4B0%2F2GIkCH1vFnyZ%2FS5BBczNtMDl%2FjrsTjGDRoG1IDTgEJfT3x5wwthsVU%2BRt%2Fyaqdw00%2BmAH7%2FLcjLXryjE4ICZj8LoD%2BsFJZP8gUEcdCm1N1R%2FkJisS8PPmYZZDHJcprmNdZsuZPczkbfDDOlqXLBW5P2TRjL2ESsCrlYdCXrWJGPWbfN5yT7uAmVf3deTbfxpFgDe8BCMWJEIq01rllqrt0tauuI1tX%2BUC%2F%2BxPVJXD%2FfMC0luY0rM01rQyqyqd%2FPy%2FyKyb9UUkcrU7qq6GGlshyr3B4wSlk1UNYKeMNje%2FrwGOqUBaDOgmC8WjDrOXooV5Ub8YBOmrsS5VwsM2CI8vPowRmJyVVNmx7HzfvH3wYhspuZkI0Nhv%2Ftik9ccckcD6SjpLigVyMX3hZ%2BgS2Ra1oVvysnsmZYKGSL1wZhd%2FRcj3%2BnrK%2FvL0cqBZEFgf5kjrcrSMiEQJXHvO5fRSLF0Y3c3nGuDDC7lGmLYmag2VJb0kGXGxhD9QKfn6clh4TWHgXEs4nIeH979&X-Amz-Signature=9bcc4525c4d94aca75ebfe072bb4c792b9f9966d1cc2758998f51a2c0f284d5f&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBGBKW27%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGRJLE6IKWbQoTOajomIG9ehlt7QKzNtjByAKBtQVAf3AiEA5m%2FEzVOdhy9IvaDgC0SZHyHNaGDUzFpePNOelnCZCuwqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHFxJJZJN%2BTKjtqYdCrcA4op7gyG%2Fa3BTwfA3rEs44l5x%2BFDVbgSM4eNK5cGAu%2FO78%2FC9aYMfnRyL0jK1rbBBh0dg1L%2FfF2g%2Btu8FPABPN4shG2JcBIbSMV0oGoo6rkAZyjtBNjqmFWX0bIzfmOeGfBqCUbf71m2ABqe3%2FxKyQoBKeGLp3NFw7MYw%2B3AYFaSD2NAHizbs%2FInQQPLsF8f4dlfjoVzgaFL4h3qzUZCs2HUIndHbrPFLGtJoqgkVKsx9Zo0p2uWlqRrm695PCBhWS%2BSbbwgF7aatMjw2hYH3A2%2FlYrprsFWrP5Fb8l1aqXMUl5kJS3m63l6a8mjOALIuMAAplZAcCXcfocGSWuWVW1gdzrnKowei8ujwipqCGG6aT6jKBrJXdXkpseetuQyirQoKkGe1GmmqXXRyAF3MyHLqwNeq9ukiEFB1b8BjQ02s8E2s24klkZwuePRuwqFC3236OMkHsq0q9aT7Q8mZXcSzIv1RyWGZuZIKLD0n8CWnn5c6AIw2ZHW83xkwg6vuqZ9vnUt%2FWkIFWfphW8n4G9CPt5i%2FlNt7N3KNmVch9cJNWRJod1F1ublQig1a99xQM2QUYL0VVId%2FVXbLBNTqpXfcClZlxKMk8gYU0rhSP%2B8P5Trc5jy1KMkVxJRMLfS%2FrwGOqUBDwxbM5IuL9JycFOAjrz4wTzRXKrlDfU3mRtKa7Bb3mcBd8pOEKy7vEk6s2NwPF4LZH33dZk8%2BGh%2FbPhcDWL%2FvojgDw7mRD8nTJ1y8bQSvSHxX7G69wm9nJD%2B5ikwVSlhju2zOzfu%2FI1PgPcpSGvZP2bij5p4AkgFejlhWtP4yIuCe13SDjAKGqLsJcSPXKQrochxPQ53WOIc%2FOmRug%2BIbtiaAhki&X-Amz-Signature=726b6377b6f905fd65ee98c141fc7aacb9b0c0180ac7344790255ee8215a5d02&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBGBKW27%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGRJLE6IKWbQoTOajomIG9ehlt7QKzNtjByAKBtQVAf3AiEA5m%2FEzVOdhy9IvaDgC0SZHyHNaGDUzFpePNOelnCZCuwqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHFxJJZJN%2BTKjtqYdCrcA4op7gyG%2Fa3BTwfA3rEs44l5x%2BFDVbgSM4eNK5cGAu%2FO78%2FC9aYMfnRyL0jK1rbBBh0dg1L%2FfF2g%2Btu8FPABPN4shG2JcBIbSMV0oGoo6rkAZyjtBNjqmFWX0bIzfmOeGfBqCUbf71m2ABqe3%2FxKyQoBKeGLp3NFw7MYw%2B3AYFaSD2NAHizbs%2FInQQPLsF8f4dlfjoVzgaFL4h3qzUZCs2HUIndHbrPFLGtJoqgkVKsx9Zo0p2uWlqRrm695PCBhWS%2BSbbwgF7aatMjw2hYH3A2%2FlYrprsFWrP5Fb8l1aqXMUl5kJS3m63l6a8mjOALIuMAAplZAcCXcfocGSWuWVW1gdzrnKowei8ujwipqCGG6aT6jKBrJXdXkpseetuQyirQoKkGe1GmmqXXRyAF3MyHLqwNeq9ukiEFB1b8BjQ02s8E2s24klkZwuePRuwqFC3236OMkHsq0q9aT7Q8mZXcSzIv1RyWGZuZIKLD0n8CWnn5c6AIw2ZHW83xkwg6vuqZ9vnUt%2FWkIFWfphW8n4G9CPt5i%2FlNt7N3KNmVch9cJNWRJod1F1ublQig1a99xQM2QUYL0VVId%2FVXbLBNTqpXfcClZlxKMk8gYU0rhSP%2B8P5Trc5jy1KMkVxJRMLfS%2FrwGOqUBDwxbM5IuL9JycFOAjrz4wTzRXKrlDfU3mRtKa7Bb3mcBd8pOEKy7vEk6s2NwPF4LZH33dZk8%2BGh%2FbPhcDWL%2FvojgDw7mRD8nTJ1y8bQSvSHxX7G69wm9nJD%2B5ikwVSlhju2zOzfu%2FI1PgPcpSGvZP2bij5p4AkgFejlhWtP4yIuCe13SDjAKGqLsJcSPXKQrochxPQ53WOIc%2FOmRug%2BIbtiaAhki&X-Amz-Signature=64baf5c37714e95bf3917a9404c29f70684e77b6a1b71f23183eb6eee0b782f5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBGBKW27%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGRJLE6IKWbQoTOajomIG9ehlt7QKzNtjByAKBtQVAf3AiEA5m%2FEzVOdhy9IvaDgC0SZHyHNaGDUzFpePNOelnCZCuwqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHFxJJZJN%2BTKjtqYdCrcA4op7gyG%2Fa3BTwfA3rEs44l5x%2BFDVbgSM4eNK5cGAu%2FO78%2FC9aYMfnRyL0jK1rbBBh0dg1L%2FfF2g%2Btu8FPABPN4shG2JcBIbSMV0oGoo6rkAZyjtBNjqmFWX0bIzfmOeGfBqCUbf71m2ABqe3%2FxKyQoBKeGLp3NFw7MYw%2B3AYFaSD2NAHizbs%2FInQQPLsF8f4dlfjoVzgaFL4h3qzUZCs2HUIndHbrPFLGtJoqgkVKsx9Zo0p2uWlqRrm695PCBhWS%2BSbbwgF7aatMjw2hYH3A2%2FlYrprsFWrP5Fb8l1aqXMUl5kJS3m63l6a8mjOALIuMAAplZAcCXcfocGSWuWVW1gdzrnKowei8ujwipqCGG6aT6jKBrJXdXkpseetuQyirQoKkGe1GmmqXXRyAF3MyHLqwNeq9ukiEFB1b8BjQ02s8E2s24klkZwuePRuwqFC3236OMkHsq0q9aT7Q8mZXcSzIv1RyWGZuZIKLD0n8CWnn5c6AIw2ZHW83xkwg6vuqZ9vnUt%2FWkIFWfphW8n4G9CPt5i%2FlNt7N3KNmVch9cJNWRJod1F1ublQig1a99xQM2QUYL0VVId%2FVXbLBNTqpXfcClZlxKMk8gYU0rhSP%2B8P5Trc5jy1KMkVxJRMLfS%2FrwGOqUBDwxbM5IuL9JycFOAjrz4wTzRXKrlDfU3mRtKa7Bb3mcBd8pOEKy7vEk6s2NwPF4LZH33dZk8%2BGh%2FbPhcDWL%2FvojgDw7mRD8nTJ1y8bQSvSHxX7G69wm9nJD%2B5ikwVSlhju2zOzfu%2FI1PgPcpSGvZP2bij5p4AkgFejlhWtP4yIuCe13SDjAKGqLsJcSPXKQrochxPQ53WOIc%2FOmRug%2BIbtiaAhki&X-Amz-Signature=dcf28307feef03a9ea8e419a232a108b01a30f2e4bf507c87ee9c3fd57aef3e9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBGBKW27%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGRJLE6IKWbQoTOajomIG9ehlt7QKzNtjByAKBtQVAf3AiEA5m%2FEzVOdhy9IvaDgC0SZHyHNaGDUzFpePNOelnCZCuwqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHFxJJZJN%2BTKjtqYdCrcA4op7gyG%2Fa3BTwfA3rEs44l5x%2BFDVbgSM4eNK5cGAu%2FO78%2FC9aYMfnRyL0jK1rbBBh0dg1L%2FfF2g%2Btu8FPABPN4shG2JcBIbSMV0oGoo6rkAZyjtBNjqmFWX0bIzfmOeGfBqCUbf71m2ABqe3%2FxKyQoBKeGLp3NFw7MYw%2B3AYFaSD2NAHizbs%2FInQQPLsF8f4dlfjoVzgaFL4h3qzUZCs2HUIndHbrPFLGtJoqgkVKsx9Zo0p2uWlqRrm695PCBhWS%2BSbbwgF7aatMjw2hYH3A2%2FlYrprsFWrP5Fb8l1aqXMUl5kJS3m63l6a8mjOALIuMAAplZAcCXcfocGSWuWVW1gdzrnKowei8ujwipqCGG6aT6jKBrJXdXkpseetuQyirQoKkGe1GmmqXXRyAF3MyHLqwNeq9ukiEFB1b8BjQ02s8E2s24klkZwuePRuwqFC3236OMkHsq0q9aT7Q8mZXcSzIv1RyWGZuZIKLD0n8CWnn5c6AIw2ZHW83xkwg6vuqZ9vnUt%2FWkIFWfphW8n4G9CPt5i%2FlNt7N3KNmVch9cJNWRJod1F1ublQig1a99xQM2QUYL0VVId%2FVXbLBNTqpXfcClZlxKMk8gYU0rhSP%2B8P5Trc5jy1KMkVxJRMLfS%2FrwGOqUBDwxbM5IuL9JycFOAjrz4wTzRXKrlDfU3mRtKa7Bb3mcBd8pOEKy7vEk6s2NwPF4LZH33dZk8%2BGh%2FbPhcDWL%2FvojgDw7mRD8nTJ1y8bQSvSHxX7G69wm9nJD%2B5ikwVSlhju2zOzfu%2FI1PgPcpSGvZP2bij5p4AkgFejlhWtP4yIuCe13SDjAKGqLsJcSPXKQrochxPQ53WOIc%2FOmRug%2BIbtiaAhki&X-Amz-Signature=64b106a09796dcbc70445ef280fca8abff1797e274a957527cdc5459fb36a380&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBGBKW27%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGRJLE6IKWbQoTOajomIG9ehlt7QKzNtjByAKBtQVAf3AiEA5m%2FEzVOdhy9IvaDgC0SZHyHNaGDUzFpePNOelnCZCuwqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHFxJJZJN%2BTKjtqYdCrcA4op7gyG%2Fa3BTwfA3rEs44l5x%2BFDVbgSM4eNK5cGAu%2FO78%2FC9aYMfnRyL0jK1rbBBh0dg1L%2FfF2g%2Btu8FPABPN4shG2JcBIbSMV0oGoo6rkAZyjtBNjqmFWX0bIzfmOeGfBqCUbf71m2ABqe3%2FxKyQoBKeGLp3NFw7MYw%2B3AYFaSD2NAHizbs%2FInQQPLsF8f4dlfjoVzgaFL4h3qzUZCs2HUIndHbrPFLGtJoqgkVKsx9Zo0p2uWlqRrm695PCBhWS%2BSbbwgF7aatMjw2hYH3A2%2FlYrprsFWrP5Fb8l1aqXMUl5kJS3m63l6a8mjOALIuMAAplZAcCXcfocGSWuWVW1gdzrnKowei8ujwipqCGG6aT6jKBrJXdXkpseetuQyirQoKkGe1GmmqXXRyAF3MyHLqwNeq9ukiEFB1b8BjQ02s8E2s24klkZwuePRuwqFC3236OMkHsq0q9aT7Q8mZXcSzIv1RyWGZuZIKLD0n8CWnn5c6AIw2ZHW83xkwg6vuqZ9vnUt%2FWkIFWfphW8n4G9CPt5i%2FlNt7N3KNmVch9cJNWRJod1F1ublQig1a99xQM2QUYL0VVId%2FVXbLBNTqpXfcClZlxKMk8gYU0rhSP%2B8P5Trc5jy1KMkVxJRMLfS%2FrwGOqUBDwxbM5IuL9JycFOAjrz4wTzRXKrlDfU3mRtKa7Bb3mcBd8pOEKy7vEk6s2NwPF4LZH33dZk8%2BGh%2FbPhcDWL%2FvojgDw7mRD8nTJ1y8bQSvSHxX7G69wm9nJD%2B5ikwVSlhju2zOzfu%2FI1PgPcpSGvZP2bij5p4AkgFejlhWtP4yIuCe13SDjAKGqLsJcSPXKQrochxPQ53WOIc%2FOmRug%2BIbtiaAhki&X-Amz-Signature=df056b13b2773aba037e414760e32fad4abd879b060f106d2078a9e0ad68833f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVWXF2NC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVpdEn5Uj1BFzpxtpKPQlDCzQEvQDRGrtcuIWEI3vgyAiEA3U%2B7PyZKcJp7X0b0Q0TwnFvtzOEsM6TeL%2BzyAeAK4aMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRnB4VPWljwCStAeCrcAzvxuFgUU%2FcZlXZiH%2BinD6piRS7E%2F%2BffBE9EjAqsGpwPSjRzvxfiHqDz1vU6lOLezTHyH8y5Pkj0Kw6NHwmz6tII6PU0vYuWYM2pl%2FpGjRD6y7sYIcfZwQFxSuEJ0QuiRacZos2Es0RbpltQw%2BnNVbccsC1dSyLE3MWY3TGfMiwwkOqCb6xaNkJ2uRzDXcXGkoRqrbM2qp5HtOu8Drjt8N0S4XjQaC0CJjZO65fBsZ%2BlpRsRpGsZNLMIud0q0CU%2BoP21ckOKmElnIfZY47bKeMfYfMaicbKv9UmZbLOu3QmlaGMSvUfZ53ENO1Re3t%2F73N2itnmTM1AjVp0wWYHA4B0%2F2GIkCH1vFnyZ%2FS5BBczNtMDl%2FjrsTjGDRoG1IDTgEJfT3x5wwthsVU%2BRt%2Fyaqdw00%2BmAH7%2FLcjLXryjE4ICZj8LoD%2BsFJZP8gUEcdCm1N1R%2FkJisS8PPmYZZDHJcprmNdZsuZPczkbfDDOlqXLBW5P2TRjL2ESsCrlYdCXrWJGPWbfN5yT7uAmVf3deTbfxpFgDe8BCMWJEIq01rllqrt0tauuI1tX%2BUC%2F%2BxPVJXD%2FfMC0luY0rM01rQyqyqd%2FPy%2FyKyb9UUkcrU7qq6GGlshyr3B4wSlk1UNYKeMNje%2FrwGOqUBaDOgmC8WjDrOXooV5Ub8YBOmrsS5VwsM2CI8vPowRmJyVVNmx7HzfvH3wYhspuZkI0Nhv%2Ftik9ccckcD6SjpLigVyMX3hZ%2BgS2Ra1oVvysnsmZYKGSL1wZhd%2FRcj3%2BnrK%2FvL0cqBZEFgf5kjrcrSMiEQJXHvO5fRSLF0Y3c3nGuDDC7lGmLYmag2VJb0kGXGxhD9QKfn6clh4TWHgXEs4nIeH979&X-Amz-Signature=47a667fb029fc496865068228dddb04c5e170453b25e6930d73c86e60fb718a5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVWXF2NC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVpdEn5Uj1BFzpxtpKPQlDCzQEvQDRGrtcuIWEI3vgyAiEA3U%2B7PyZKcJp7X0b0Q0TwnFvtzOEsM6TeL%2BzyAeAK4aMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRnB4VPWljwCStAeCrcAzvxuFgUU%2FcZlXZiH%2BinD6piRS7E%2F%2BffBE9EjAqsGpwPSjRzvxfiHqDz1vU6lOLezTHyH8y5Pkj0Kw6NHwmz6tII6PU0vYuWYM2pl%2FpGjRD6y7sYIcfZwQFxSuEJ0QuiRacZos2Es0RbpltQw%2BnNVbccsC1dSyLE3MWY3TGfMiwwkOqCb6xaNkJ2uRzDXcXGkoRqrbM2qp5HtOu8Drjt8N0S4XjQaC0CJjZO65fBsZ%2BlpRsRpGsZNLMIud0q0CU%2BoP21ckOKmElnIfZY47bKeMfYfMaicbKv9UmZbLOu3QmlaGMSvUfZ53ENO1Re3t%2F73N2itnmTM1AjVp0wWYHA4B0%2F2GIkCH1vFnyZ%2FS5BBczNtMDl%2FjrsTjGDRoG1IDTgEJfT3x5wwthsVU%2BRt%2Fyaqdw00%2BmAH7%2FLcjLXryjE4ICZj8LoD%2BsFJZP8gUEcdCm1N1R%2FkJisS8PPmYZZDHJcprmNdZsuZPczkbfDDOlqXLBW5P2TRjL2ESsCrlYdCXrWJGPWbfN5yT7uAmVf3deTbfxpFgDe8BCMWJEIq01rllqrt0tauuI1tX%2BUC%2F%2BxPVJXD%2FfMC0luY0rM01rQyqyqd%2FPy%2FyKyb9UUkcrU7qq6GGlshyr3B4wSlk1UNYKeMNje%2FrwGOqUBaDOgmC8WjDrOXooV5Ub8YBOmrsS5VwsM2CI8vPowRmJyVVNmx7HzfvH3wYhspuZkI0Nhv%2Ftik9ccckcD6SjpLigVyMX3hZ%2BgS2Ra1oVvysnsmZYKGSL1wZhd%2FRcj3%2BnrK%2FvL0cqBZEFgf5kjrcrSMiEQJXHvO5fRSLF0Y3c3nGuDDC7lGmLYmag2VJb0kGXGxhD9QKfn6clh4TWHgXEs4nIeH979&X-Amz-Signature=9d74a2650c65cc2347b16d0a6c3b3791a399f4d04fb1efa9ccdceef2b8ece911&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVWXF2NC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVpdEn5Uj1BFzpxtpKPQlDCzQEvQDRGrtcuIWEI3vgyAiEA3U%2B7PyZKcJp7X0b0Q0TwnFvtzOEsM6TeL%2BzyAeAK4aMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRnB4VPWljwCStAeCrcAzvxuFgUU%2FcZlXZiH%2BinD6piRS7E%2F%2BffBE9EjAqsGpwPSjRzvxfiHqDz1vU6lOLezTHyH8y5Pkj0Kw6NHwmz6tII6PU0vYuWYM2pl%2FpGjRD6y7sYIcfZwQFxSuEJ0QuiRacZos2Es0RbpltQw%2BnNVbccsC1dSyLE3MWY3TGfMiwwkOqCb6xaNkJ2uRzDXcXGkoRqrbM2qp5HtOu8Drjt8N0S4XjQaC0CJjZO65fBsZ%2BlpRsRpGsZNLMIud0q0CU%2BoP21ckOKmElnIfZY47bKeMfYfMaicbKv9UmZbLOu3QmlaGMSvUfZ53ENO1Re3t%2F73N2itnmTM1AjVp0wWYHA4B0%2F2GIkCH1vFnyZ%2FS5BBczNtMDl%2FjrsTjGDRoG1IDTgEJfT3x5wwthsVU%2BRt%2Fyaqdw00%2BmAH7%2FLcjLXryjE4ICZj8LoD%2BsFJZP8gUEcdCm1N1R%2FkJisS8PPmYZZDHJcprmNdZsuZPczkbfDDOlqXLBW5P2TRjL2ESsCrlYdCXrWJGPWbfN5yT7uAmVf3deTbfxpFgDe8BCMWJEIq01rllqrt0tauuI1tX%2BUC%2F%2BxPVJXD%2FfMC0luY0rM01rQyqyqd%2FPy%2FyKyb9UUkcrU7qq6GGlshyr3B4wSlk1UNYKeMNje%2FrwGOqUBaDOgmC8WjDrOXooV5Ub8YBOmrsS5VwsM2CI8vPowRmJyVVNmx7HzfvH3wYhspuZkI0Nhv%2Ftik9ccckcD6SjpLigVyMX3hZ%2BgS2Ra1oVvysnsmZYKGSL1wZhd%2FRcj3%2BnrK%2FvL0cqBZEFgf5kjrcrSMiEQJXHvO5fRSLF0Y3c3nGuDDC7lGmLYmag2VJb0kGXGxhD9QKfn6clh4TWHgXEs4nIeH979&X-Amz-Signature=d777e0883453f0ae9fb3fd8a5a37ecb95ff994e3267dca5e0599146edc49f96e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVWXF2NC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVpdEn5Uj1BFzpxtpKPQlDCzQEvQDRGrtcuIWEI3vgyAiEA3U%2B7PyZKcJp7X0b0Q0TwnFvtzOEsM6TeL%2BzyAeAK4aMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRnB4VPWljwCStAeCrcAzvxuFgUU%2FcZlXZiH%2BinD6piRS7E%2F%2BffBE9EjAqsGpwPSjRzvxfiHqDz1vU6lOLezTHyH8y5Pkj0Kw6NHwmz6tII6PU0vYuWYM2pl%2FpGjRD6y7sYIcfZwQFxSuEJ0QuiRacZos2Es0RbpltQw%2BnNVbccsC1dSyLE3MWY3TGfMiwwkOqCb6xaNkJ2uRzDXcXGkoRqrbM2qp5HtOu8Drjt8N0S4XjQaC0CJjZO65fBsZ%2BlpRsRpGsZNLMIud0q0CU%2BoP21ckOKmElnIfZY47bKeMfYfMaicbKv9UmZbLOu3QmlaGMSvUfZ53ENO1Re3t%2F73N2itnmTM1AjVp0wWYHA4B0%2F2GIkCH1vFnyZ%2FS5BBczNtMDl%2FjrsTjGDRoG1IDTgEJfT3x5wwthsVU%2BRt%2Fyaqdw00%2BmAH7%2FLcjLXryjE4ICZj8LoD%2BsFJZP8gUEcdCm1N1R%2FkJisS8PPmYZZDHJcprmNdZsuZPczkbfDDOlqXLBW5P2TRjL2ESsCrlYdCXrWJGPWbfN5yT7uAmVf3deTbfxpFgDe8BCMWJEIq01rllqrt0tauuI1tX%2BUC%2F%2BxPVJXD%2FfMC0luY0rM01rQyqyqd%2FPy%2FyKyb9UUkcrU7qq6GGlshyr3B4wSlk1UNYKeMNje%2FrwGOqUBaDOgmC8WjDrOXooV5Ub8YBOmrsS5VwsM2CI8vPowRmJyVVNmx7HzfvH3wYhspuZkI0Nhv%2Ftik9ccckcD6SjpLigVyMX3hZ%2BgS2Ra1oVvysnsmZYKGSL1wZhd%2FRcj3%2BnrK%2FvL0cqBZEFgf5kjrcrSMiEQJXHvO5fRSLF0Y3c3nGuDDC7lGmLYmag2VJb0kGXGxhD9QKfn6clh4TWHgXEs4nIeH979&X-Amz-Signature=71d6031c4e587e3e7aa0fcebfdf1fc6ea6634898ffd597e7193d9605ff2fbc51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVWXF2NC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVpdEn5Uj1BFzpxtpKPQlDCzQEvQDRGrtcuIWEI3vgyAiEA3U%2B7PyZKcJp7X0b0Q0TwnFvtzOEsM6TeL%2BzyAeAK4aMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRnB4VPWljwCStAeCrcAzvxuFgUU%2FcZlXZiH%2BinD6piRS7E%2F%2BffBE9EjAqsGpwPSjRzvxfiHqDz1vU6lOLezTHyH8y5Pkj0Kw6NHwmz6tII6PU0vYuWYM2pl%2FpGjRD6y7sYIcfZwQFxSuEJ0QuiRacZos2Es0RbpltQw%2BnNVbccsC1dSyLE3MWY3TGfMiwwkOqCb6xaNkJ2uRzDXcXGkoRqrbM2qp5HtOu8Drjt8N0S4XjQaC0CJjZO65fBsZ%2BlpRsRpGsZNLMIud0q0CU%2BoP21ckOKmElnIfZY47bKeMfYfMaicbKv9UmZbLOu3QmlaGMSvUfZ53ENO1Re3t%2F73N2itnmTM1AjVp0wWYHA4B0%2F2GIkCH1vFnyZ%2FS5BBczNtMDl%2FjrsTjGDRoG1IDTgEJfT3x5wwthsVU%2BRt%2Fyaqdw00%2BmAH7%2FLcjLXryjE4ICZj8LoD%2BsFJZP8gUEcdCm1N1R%2FkJisS8PPmYZZDHJcprmNdZsuZPczkbfDDOlqXLBW5P2TRjL2ESsCrlYdCXrWJGPWbfN5yT7uAmVf3deTbfxpFgDe8BCMWJEIq01rllqrt0tauuI1tX%2BUC%2F%2BxPVJXD%2FfMC0luY0rM01rQyqyqd%2FPy%2FyKyb9UUkcrU7qq6GGlshyr3B4wSlk1UNYKeMNje%2FrwGOqUBaDOgmC8WjDrOXooV5Ub8YBOmrsS5VwsM2CI8vPowRmJyVVNmx7HzfvH3wYhspuZkI0Nhv%2Ftik9ccckcD6SjpLigVyMX3hZ%2BgS2Ra1oVvysnsmZYKGSL1wZhd%2FRcj3%2BnrK%2FvL0cqBZEFgf5kjrcrSMiEQJXHvO5fRSLF0Y3c3nGuDDC7lGmLYmag2VJb0kGXGxhD9QKfn6clh4TWHgXEs4nIeH979&X-Amz-Signature=61077cad5ce2d0a9635186cc395d4ce03bbcd4d27457d5a719cebe4ac25610f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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


