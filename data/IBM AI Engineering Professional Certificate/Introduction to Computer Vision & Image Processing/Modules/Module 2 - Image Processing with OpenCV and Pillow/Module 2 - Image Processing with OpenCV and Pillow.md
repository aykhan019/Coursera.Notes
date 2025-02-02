

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7M4UO7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2dAfH8VBU0Dh%2FWwAhqlkaIfLrNuO0s%2Fm4P5NuaVJUuAIhAMHVIzCw8zFL9ITI35wF7ZfD7QFhkdz3e48aesGfOYT3KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfeCL8RwHW3DyTO5Yq3APM3mH%2FOx3gXmXvj6kOvxfcF9Fsk2SaLSJKKOvyo4QPx8atZGvDwSQWZqBlWzyyhu%2BPmAuElPz5ZmxiNuNxKzAqL4SIBEteBB9KanBPVIO1CFoyJ848BGYtxrhfoiIfhDray%2FtEYEJv3gFALRoe8l9%2BExLxzqUmzwmu6MIzGhVzr7Dk6QicWBpZXf4YPmmmVxsoouWhBoBgkqrStyOgu17mGq%2BXY%2FwJoLtLlcPoVZdr2d93FzqH3D5aaF2mR%2FSWlwYzsex7vQqetOF%2FE7cbfBHF3ncuVJWZQstNBrvDw%2BxSjoGsA0ajptYzDul5lbmBATrATuAThm0xQLoi%2BJz8ErznyWahJkJu3%2BzLd8ZvqFVFI5WoDU0aCmxb9k7m7TUQiagIpA9xscXrHHjrzH7J9SJqget7PZzPkxxuyH7L85GQK9Q8qOdn3zNPEXJTBhV7I4b6nTzw2LoMYHsFCj4VrNixdVVnGbI13xVemTMaBNlNKalfyg5H%2Ft3m6VCXsbOnIp5fz4nLdkT64R%2FtHami8raPqsSClBcgtptHOhKGyRZkO%2FZtlNO73E%2B%2FuLtV8VOqeIF2mauZO0RQ%2FpIQFm7mMSGMmBOlfPHdsguyEZ613VgrzX%2FZoSTeBSKj7095nDD5m%2Fy8BjqkAVEP%2BRoIIvjaPWqGIznJKxTwBOeiAMg6wfu4Di%2BrSt%2FfVst2ssiIQs0ztQgJX%2Bp%2BB4cO9Uet5bpPTbwEOZTOWYAM7ZW6RTC4ycZJ24%2Bkb7P8dzai7%2FJtjARbL%2BrRiYtBxITNMdyFVChXetArqOGzm3%2BazWCt776L%2Fm4hel4vCpBvesAZCvgqP14DBnbcTyTbZugsI8Ukzi0Oqz53Y2VhPEZoKf7l&X-Amz-Signature=ab87d6a57cb25751b50371e0dc6a7cf5b3c2ef0d02f0f498a3e9e03a0f2fe2d5&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IVMKHQD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxlqKf%2FXt5O0sYTAD%2Fp7cylhbtVnuOfgRGnfmgzcTE3AIgW1kYJwt3sYdgVc03PeHWVYHQ2Nfg6Kgm%2Bu35LNyaQCsqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2FpEjIqJEHXRoemSSrcA15VB6n8lW9lCLv74ycKRwYFpAhWmmxtdlvlW1CrjljNA8447cdiyVUcGNXAbjwb9tyRYF%2FV2hxRkykJb%2BJJmEfFABwBcf6d1BpeLxQ2qpvF3Igu2LkyaFPo9xFYkPnXvFVWOkPHt2PbcrzedIXeV%2BqUj9TmNGMb920XiFZxJxBPkAdsb2oUN8fP4aS7E%2F1N0bnwRn2bxK4zPpYP9OelccSGB2DL9WM2y%2B8zoGqGCaq%2BVHimK1ZPv9FS30%2FmeurKyPl9D6gLdxiOCvg%2FPcSp57EVA%2B9bUCHntxaA6GEelKsNnRnWjyNUC5N8nuHiPmDf72cx2lVagtgnqRaBQPyP1IBt5vvTlDJrZ%2BPWpsBUIXHgG347g2chI7b188ClsV6UEDm5E%2BjlHjJbvnqwICes%2Bl4ZtzMPEfSghqdv%2F2Y3dSme0conEh%2BMzcwljDVCZAJM%2F%2FeS7EDjJvzHM6qVa2bx9jIwJH8xiU0ZlM4QQhJ8VoiOrFdblfwzlPpR7VLR9t2%2F5ikROE5ED4PzZArbwgImnsc7Ih3Dn2WDAXpQvUhSKDdvWjymxtBZ%2BpWPp%2BfCjteEtoLH88BdK9EIXXmSBVwVCAnQeJzU3HvwVfAsTSL%2B044y1jPASV5WgUXQKW4wMKrh%2B7wGOqUBbXEdffQDmrLZk9fu%2FVhmHREGdJVggW2r4kJxXcspXZ9Jn2MTFZUwAeyQDpHedPsMoYKgH949kQc3PlfsF6XgfQRTllsNJty6KTlBwHjZQInWXMUN9X9DI10fFljZ3lG5N7U7y5KhNAB73uIwnhQJrz5wD1McJVJjTmRp5KWB7ic8LzE6kKzmUZW%2B4MbI8S6T5aaeDK2FACzHxPyA1Irj7SeuHf5C&X-Amz-Signature=bf36e04b6cbff1430b291249b52abb1111a65f9e3bee0b532f6d72edd4f9b64a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IVMKHQD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxlqKf%2FXt5O0sYTAD%2Fp7cylhbtVnuOfgRGnfmgzcTE3AIgW1kYJwt3sYdgVc03PeHWVYHQ2Nfg6Kgm%2Bu35LNyaQCsqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2FpEjIqJEHXRoemSSrcA15VB6n8lW9lCLv74ycKRwYFpAhWmmxtdlvlW1CrjljNA8447cdiyVUcGNXAbjwb9tyRYF%2FV2hxRkykJb%2BJJmEfFABwBcf6d1BpeLxQ2qpvF3Igu2LkyaFPo9xFYkPnXvFVWOkPHt2PbcrzedIXeV%2BqUj9TmNGMb920XiFZxJxBPkAdsb2oUN8fP4aS7E%2F1N0bnwRn2bxK4zPpYP9OelccSGB2DL9WM2y%2B8zoGqGCaq%2BVHimK1ZPv9FS30%2FmeurKyPl9D6gLdxiOCvg%2FPcSp57EVA%2B9bUCHntxaA6GEelKsNnRnWjyNUC5N8nuHiPmDf72cx2lVagtgnqRaBQPyP1IBt5vvTlDJrZ%2BPWpsBUIXHgG347g2chI7b188ClsV6UEDm5E%2BjlHjJbvnqwICes%2Bl4ZtzMPEfSghqdv%2F2Y3dSme0conEh%2BMzcwljDVCZAJM%2F%2FeS7EDjJvzHM6qVa2bx9jIwJH8xiU0ZlM4QQhJ8VoiOrFdblfwzlPpR7VLR9t2%2F5ikROE5ED4PzZArbwgImnsc7Ih3Dn2WDAXpQvUhSKDdvWjymxtBZ%2BpWPp%2BfCjteEtoLH88BdK9EIXXmSBVwVCAnQeJzU3HvwVfAsTSL%2B044y1jPASV5WgUXQKW4wMKrh%2B7wGOqUBbXEdffQDmrLZk9fu%2FVhmHREGdJVggW2r4kJxXcspXZ9Jn2MTFZUwAeyQDpHedPsMoYKgH949kQc3PlfsF6XgfQRTllsNJty6KTlBwHjZQInWXMUN9X9DI10fFljZ3lG5N7U7y5KhNAB73uIwnhQJrz5wD1McJVJjTmRp5KWB7ic8LzE6kKzmUZW%2B4MbI8S6T5aaeDK2FACzHxPyA1Irj7SeuHf5C&X-Amz-Signature=ec9caa5a3375f1d85ba334968ff58b9915bbe46c788bb8015fe5f8da2268ce1f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IVMKHQD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxlqKf%2FXt5O0sYTAD%2Fp7cylhbtVnuOfgRGnfmgzcTE3AIgW1kYJwt3sYdgVc03PeHWVYHQ2Nfg6Kgm%2Bu35LNyaQCsqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2FpEjIqJEHXRoemSSrcA15VB6n8lW9lCLv74ycKRwYFpAhWmmxtdlvlW1CrjljNA8447cdiyVUcGNXAbjwb9tyRYF%2FV2hxRkykJb%2BJJmEfFABwBcf6d1BpeLxQ2qpvF3Igu2LkyaFPo9xFYkPnXvFVWOkPHt2PbcrzedIXeV%2BqUj9TmNGMb920XiFZxJxBPkAdsb2oUN8fP4aS7E%2F1N0bnwRn2bxK4zPpYP9OelccSGB2DL9WM2y%2B8zoGqGCaq%2BVHimK1ZPv9FS30%2FmeurKyPl9D6gLdxiOCvg%2FPcSp57EVA%2B9bUCHntxaA6GEelKsNnRnWjyNUC5N8nuHiPmDf72cx2lVagtgnqRaBQPyP1IBt5vvTlDJrZ%2BPWpsBUIXHgG347g2chI7b188ClsV6UEDm5E%2BjlHjJbvnqwICes%2Bl4ZtzMPEfSghqdv%2F2Y3dSme0conEh%2BMzcwljDVCZAJM%2F%2FeS7EDjJvzHM6qVa2bx9jIwJH8xiU0ZlM4QQhJ8VoiOrFdblfwzlPpR7VLR9t2%2F5ikROE5ED4PzZArbwgImnsc7Ih3Dn2WDAXpQvUhSKDdvWjymxtBZ%2BpWPp%2BfCjteEtoLH88BdK9EIXXmSBVwVCAnQeJzU3HvwVfAsTSL%2B044y1jPASV5WgUXQKW4wMKrh%2B7wGOqUBbXEdffQDmrLZk9fu%2FVhmHREGdJVggW2r4kJxXcspXZ9Jn2MTFZUwAeyQDpHedPsMoYKgH949kQc3PlfsF6XgfQRTllsNJty6KTlBwHjZQInWXMUN9X9DI10fFljZ3lG5N7U7y5KhNAB73uIwnhQJrz5wD1McJVJjTmRp5KWB7ic8LzE6kKzmUZW%2B4MbI8S6T5aaeDK2FACzHxPyA1Irj7SeuHf5C&X-Amz-Signature=1443eee07372ef65bdaf199fbf8e91cb672c484e8abbb68783055fec216ceb85&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IVMKHQD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxlqKf%2FXt5O0sYTAD%2Fp7cylhbtVnuOfgRGnfmgzcTE3AIgW1kYJwt3sYdgVc03PeHWVYHQ2Nfg6Kgm%2Bu35LNyaQCsqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2FpEjIqJEHXRoemSSrcA15VB6n8lW9lCLv74ycKRwYFpAhWmmxtdlvlW1CrjljNA8447cdiyVUcGNXAbjwb9tyRYF%2FV2hxRkykJb%2BJJmEfFABwBcf6d1BpeLxQ2qpvF3Igu2LkyaFPo9xFYkPnXvFVWOkPHt2PbcrzedIXeV%2BqUj9TmNGMb920XiFZxJxBPkAdsb2oUN8fP4aS7E%2F1N0bnwRn2bxK4zPpYP9OelccSGB2DL9WM2y%2B8zoGqGCaq%2BVHimK1ZPv9FS30%2FmeurKyPl9D6gLdxiOCvg%2FPcSp57EVA%2B9bUCHntxaA6GEelKsNnRnWjyNUC5N8nuHiPmDf72cx2lVagtgnqRaBQPyP1IBt5vvTlDJrZ%2BPWpsBUIXHgG347g2chI7b188ClsV6UEDm5E%2BjlHjJbvnqwICes%2Bl4ZtzMPEfSghqdv%2F2Y3dSme0conEh%2BMzcwljDVCZAJM%2F%2FeS7EDjJvzHM6qVa2bx9jIwJH8xiU0ZlM4QQhJ8VoiOrFdblfwzlPpR7VLR9t2%2F5ikROE5ED4PzZArbwgImnsc7Ih3Dn2WDAXpQvUhSKDdvWjymxtBZ%2BpWPp%2BfCjteEtoLH88BdK9EIXXmSBVwVCAnQeJzU3HvwVfAsTSL%2B044y1jPASV5WgUXQKW4wMKrh%2B7wGOqUBbXEdffQDmrLZk9fu%2FVhmHREGdJVggW2r4kJxXcspXZ9Jn2MTFZUwAeyQDpHedPsMoYKgH949kQc3PlfsF6XgfQRTllsNJty6KTlBwHjZQInWXMUN9X9DI10fFljZ3lG5N7U7y5KhNAB73uIwnhQJrz5wD1McJVJjTmRp5KWB7ic8LzE6kKzmUZW%2B4MbI8S6T5aaeDK2FACzHxPyA1Irj7SeuHf5C&X-Amz-Signature=e5da2076faec2beffd418075b333977225ef20db70ee057e9e0a5d801a61837f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IVMKHQD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxlqKf%2FXt5O0sYTAD%2Fp7cylhbtVnuOfgRGnfmgzcTE3AIgW1kYJwt3sYdgVc03PeHWVYHQ2Nfg6Kgm%2Bu35LNyaQCsqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2FpEjIqJEHXRoemSSrcA15VB6n8lW9lCLv74ycKRwYFpAhWmmxtdlvlW1CrjljNA8447cdiyVUcGNXAbjwb9tyRYF%2FV2hxRkykJb%2BJJmEfFABwBcf6d1BpeLxQ2qpvF3Igu2LkyaFPo9xFYkPnXvFVWOkPHt2PbcrzedIXeV%2BqUj9TmNGMb920XiFZxJxBPkAdsb2oUN8fP4aS7E%2F1N0bnwRn2bxK4zPpYP9OelccSGB2DL9WM2y%2B8zoGqGCaq%2BVHimK1ZPv9FS30%2FmeurKyPl9D6gLdxiOCvg%2FPcSp57EVA%2B9bUCHntxaA6GEelKsNnRnWjyNUC5N8nuHiPmDf72cx2lVagtgnqRaBQPyP1IBt5vvTlDJrZ%2BPWpsBUIXHgG347g2chI7b188ClsV6UEDm5E%2BjlHjJbvnqwICes%2Bl4ZtzMPEfSghqdv%2F2Y3dSme0conEh%2BMzcwljDVCZAJM%2F%2FeS7EDjJvzHM6qVa2bx9jIwJH8xiU0ZlM4QQhJ8VoiOrFdblfwzlPpR7VLR9t2%2F5ikROE5ED4PzZArbwgImnsc7Ih3Dn2WDAXpQvUhSKDdvWjymxtBZ%2BpWPp%2BfCjteEtoLH88BdK9EIXXmSBVwVCAnQeJzU3HvwVfAsTSL%2B044y1jPASV5WgUXQKW4wMKrh%2B7wGOqUBbXEdffQDmrLZk9fu%2FVhmHREGdJVggW2r4kJxXcspXZ9Jn2MTFZUwAeyQDpHedPsMoYKgH949kQc3PlfsF6XgfQRTllsNJty6KTlBwHjZQInWXMUN9X9DI10fFljZ3lG5N7U7y5KhNAB73uIwnhQJrz5wD1McJVJjTmRp5KWB7ic8LzE6kKzmUZW%2B4MbI8S6T5aaeDK2FACzHxPyA1Irj7SeuHf5C&X-Amz-Signature=95371d0f557ed428724b6951eb52fa4711c40b67df5372e1fe78d83fe5cc213f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7M4UO7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2dAfH8VBU0Dh%2FWwAhqlkaIfLrNuO0s%2Fm4P5NuaVJUuAIhAMHVIzCw8zFL9ITI35wF7ZfD7QFhkdz3e48aesGfOYT3KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfeCL8RwHW3DyTO5Yq3APM3mH%2FOx3gXmXvj6kOvxfcF9Fsk2SaLSJKKOvyo4QPx8atZGvDwSQWZqBlWzyyhu%2BPmAuElPz5ZmxiNuNxKzAqL4SIBEteBB9KanBPVIO1CFoyJ848BGYtxrhfoiIfhDray%2FtEYEJv3gFALRoe8l9%2BExLxzqUmzwmu6MIzGhVzr7Dk6QicWBpZXf4YPmmmVxsoouWhBoBgkqrStyOgu17mGq%2BXY%2FwJoLtLlcPoVZdr2d93FzqH3D5aaF2mR%2FSWlwYzsex7vQqetOF%2FE7cbfBHF3ncuVJWZQstNBrvDw%2BxSjoGsA0ajptYzDul5lbmBATrATuAThm0xQLoi%2BJz8ErznyWahJkJu3%2BzLd8ZvqFVFI5WoDU0aCmxb9k7m7TUQiagIpA9xscXrHHjrzH7J9SJqget7PZzPkxxuyH7L85GQK9Q8qOdn3zNPEXJTBhV7I4b6nTzw2LoMYHsFCj4VrNixdVVnGbI13xVemTMaBNlNKalfyg5H%2Ft3m6VCXsbOnIp5fz4nLdkT64R%2FtHami8raPqsSClBcgtptHOhKGyRZkO%2FZtlNO73E%2B%2FuLtV8VOqeIF2mauZO0RQ%2FpIQFm7mMSGMmBOlfPHdsguyEZ613VgrzX%2FZoSTeBSKj7095nDD5m%2Fy8BjqkAVEP%2BRoIIvjaPWqGIznJKxTwBOeiAMg6wfu4Di%2BrSt%2FfVst2ssiIQs0ztQgJX%2Bp%2BB4cO9Uet5bpPTbwEOZTOWYAM7ZW6RTC4ycZJ24%2Bkb7P8dzai7%2FJtjARbL%2BrRiYtBxITNMdyFVChXetArqOGzm3%2BazWCt776L%2Fm4hel4vCpBvesAZCvgqP14DBnbcTyTbZugsI8Ukzi0Oqz53Y2VhPEZoKf7l&X-Amz-Signature=7831a816fd48f07fb791bcbf22679101ac4013094340837c7fb39f9c7beaa56b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7M4UO7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2dAfH8VBU0Dh%2FWwAhqlkaIfLrNuO0s%2Fm4P5NuaVJUuAIhAMHVIzCw8zFL9ITI35wF7ZfD7QFhkdz3e48aesGfOYT3KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfeCL8RwHW3DyTO5Yq3APM3mH%2FOx3gXmXvj6kOvxfcF9Fsk2SaLSJKKOvyo4QPx8atZGvDwSQWZqBlWzyyhu%2BPmAuElPz5ZmxiNuNxKzAqL4SIBEteBB9KanBPVIO1CFoyJ848BGYtxrhfoiIfhDray%2FtEYEJv3gFALRoe8l9%2BExLxzqUmzwmu6MIzGhVzr7Dk6QicWBpZXf4YPmmmVxsoouWhBoBgkqrStyOgu17mGq%2BXY%2FwJoLtLlcPoVZdr2d93FzqH3D5aaF2mR%2FSWlwYzsex7vQqetOF%2FE7cbfBHF3ncuVJWZQstNBrvDw%2BxSjoGsA0ajptYzDul5lbmBATrATuAThm0xQLoi%2BJz8ErznyWahJkJu3%2BzLd8ZvqFVFI5WoDU0aCmxb9k7m7TUQiagIpA9xscXrHHjrzH7J9SJqget7PZzPkxxuyH7L85GQK9Q8qOdn3zNPEXJTBhV7I4b6nTzw2LoMYHsFCj4VrNixdVVnGbI13xVemTMaBNlNKalfyg5H%2Ft3m6VCXsbOnIp5fz4nLdkT64R%2FtHami8raPqsSClBcgtptHOhKGyRZkO%2FZtlNO73E%2B%2FuLtV8VOqeIF2mauZO0RQ%2FpIQFm7mMSGMmBOlfPHdsguyEZ613VgrzX%2FZoSTeBSKj7095nDD5m%2Fy8BjqkAVEP%2BRoIIvjaPWqGIznJKxTwBOeiAMg6wfu4Di%2BrSt%2FfVst2ssiIQs0ztQgJX%2Bp%2BB4cO9Uet5bpPTbwEOZTOWYAM7ZW6RTC4ycZJ24%2Bkb7P8dzai7%2FJtjARbL%2BrRiYtBxITNMdyFVChXetArqOGzm3%2BazWCt776L%2Fm4hel4vCpBvesAZCvgqP14DBnbcTyTbZugsI8Ukzi0Oqz53Y2VhPEZoKf7l&X-Amz-Signature=214e793f21ba4e61a9aac4cb4408e8027efbfd6d594487012451a23060fa2de4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7M4UO7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2dAfH8VBU0Dh%2FWwAhqlkaIfLrNuO0s%2Fm4P5NuaVJUuAIhAMHVIzCw8zFL9ITI35wF7ZfD7QFhkdz3e48aesGfOYT3KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfeCL8RwHW3DyTO5Yq3APM3mH%2FOx3gXmXvj6kOvxfcF9Fsk2SaLSJKKOvyo4QPx8atZGvDwSQWZqBlWzyyhu%2BPmAuElPz5ZmxiNuNxKzAqL4SIBEteBB9KanBPVIO1CFoyJ848BGYtxrhfoiIfhDray%2FtEYEJv3gFALRoe8l9%2BExLxzqUmzwmu6MIzGhVzr7Dk6QicWBpZXf4YPmmmVxsoouWhBoBgkqrStyOgu17mGq%2BXY%2FwJoLtLlcPoVZdr2d93FzqH3D5aaF2mR%2FSWlwYzsex7vQqetOF%2FE7cbfBHF3ncuVJWZQstNBrvDw%2BxSjoGsA0ajptYzDul5lbmBATrATuAThm0xQLoi%2BJz8ErznyWahJkJu3%2BzLd8ZvqFVFI5WoDU0aCmxb9k7m7TUQiagIpA9xscXrHHjrzH7J9SJqget7PZzPkxxuyH7L85GQK9Q8qOdn3zNPEXJTBhV7I4b6nTzw2LoMYHsFCj4VrNixdVVnGbI13xVemTMaBNlNKalfyg5H%2Ft3m6VCXsbOnIp5fz4nLdkT64R%2FtHami8raPqsSClBcgtptHOhKGyRZkO%2FZtlNO73E%2B%2FuLtV8VOqeIF2mauZO0RQ%2FpIQFm7mMSGMmBOlfPHdsguyEZ613VgrzX%2FZoSTeBSKj7095nDD5m%2Fy8BjqkAVEP%2BRoIIvjaPWqGIznJKxTwBOeiAMg6wfu4Di%2BrSt%2FfVst2ssiIQs0ztQgJX%2Bp%2BB4cO9Uet5bpPTbwEOZTOWYAM7ZW6RTC4ycZJ24%2Bkb7P8dzai7%2FJtjARbL%2BrRiYtBxITNMdyFVChXetArqOGzm3%2BazWCt776L%2Fm4hel4vCpBvesAZCvgqP14DBnbcTyTbZugsI8Ukzi0Oqz53Y2VhPEZoKf7l&X-Amz-Signature=ef4d56e79a65c8c54b2868d7a25281df73fa505ed4da51cd0c4d3e60a4b06083&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7M4UO7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2dAfH8VBU0Dh%2FWwAhqlkaIfLrNuO0s%2Fm4P5NuaVJUuAIhAMHVIzCw8zFL9ITI35wF7ZfD7QFhkdz3e48aesGfOYT3KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfeCL8RwHW3DyTO5Yq3APM3mH%2FOx3gXmXvj6kOvxfcF9Fsk2SaLSJKKOvyo4QPx8atZGvDwSQWZqBlWzyyhu%2BPmAuElPz5ZmxiNuNxKzAqL4SIBEteBB9KanBPVIO1CFoyJ848BGYtxrhfoiIfhDray%2FtEYEJv3gFALRoe8l9%2BExLxzqUmzwmu6MIzGhVzr7Dk6QicWBpZXf4YPmmmVxsoouWhBoBgkqrStyOgu17mGq%2BXY%2FwJoLtLlcPoVZdr2d93FzqH3D5aaF2mR%2FSWlwYzsex7vQqetOF%2FE7cbfBHF3ncuVJWZQstNBrvDw%2BxSjoGsA0ajptYzDul5lbmBATrATuAThm0xQLoi%2BJz8ErznyWahJkJu3%2BzLd8ZvqFVFI5WoDU0aCmxb9k7m7TUQiagIpA9xscXrHHjrzH7J9SJqget7PZzPkxxuyH7L85GQK9Q8qOdn3zNPEXJTBhV7I4b6nTzw2LoMYHsFCj4VrNixdVVnGbI13xVemTMaBNlNKalfyg5H%2Ft3m6VCXsbOnIp5fz4nLdkT64R%2FtHami8raPqsSClBcgtptHOhKGyRZkO%2FZtlNO73E%2B%2FuLtV8VOqeIF2mauZO0RQ%2FpIQFm7mMSGMmBOlfPHdsguyEZ613VgrzX%2FZoSTeBSKj7095nDD5m%2Fy8BjqkAVEP%2BRoIIvjaPWqGIznJKxTwBOeiAMg6wfu4Di%2BrSt%2FfVst2ssiIQs0ztQgJX%2Bp%2BB4cO9Uet5bpPTbwEOZTOWYAM7ZW6RTC4ycZJ24%2Bkb7P8dzai7%2FJtjARbL%2BrRiYtBxITNMdyFVChXetArqOGzm3%2BazWCt776L%2Fm4hel4vCpBvesAZCvgqP14DBnbcTyTbZugsI8Ukzi0Oqz53Y2VhPEZoKf7l&X-Amz-Signature=78986d8fe1b97e6aa9ac50212a113d032aef9d1efeb26569900453f93f96c977&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7M4UO7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2dAfH8VBU0Dh%2FWwAhqlkaIfLrNuO0s%2Fm4P5NuaVJUuAIhAMHVIzCw8zFL9ITI35wF7ZfD7QFhkdz3e48aesGfOYT3KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfeCL8RwHW3DyTO5Yq3APM3mH%2FOx3gXmXvj6kOvxfcF9Fsk2SaLSJKKOvyo4QPx8atZGvDwSQWZqBlWzyyhu%2BPmAuElPz5ZmxiNuNxKzAqL4SIBEteBB9KanBPVIO1CFoyJ848BGYtxrhfoiIfhDray%2FtEYEJv3gFALRoe8l9%2BExLxzqUmzwmu6MIzGhVzr7Dk6QicWBpZXf4YPmmmVxsoouWhBoBgkqrStyOgu17mGq%2BXY%2FwJoLtLlcPoVZdr2d93FzqH3D5aaF2mR%2FSWlwYzsex7vQqetOF%2FE7cbfBHF3ncuVJWZQstNBrvDw%2BxSjoGsA0ajptYzDul5lbmBATrATuAThm0xQLoi%2BJz8ErznyWahJkJu3%2BzLd8ZvqFVFI5WoDU0aCmxb9k7m7TUQiagIpA9xscXrHHjrzH7J9SJqget7PZzPkxxuyH7L85GQK9Q8qOdn3zNPEXJTBhV7I4b6nTzw2LoMYHsFCj4VrNixdVVnGbI13xVemTMaBNlNKalfyg5H%2Ft3m6VCXsbOnIp5fz4nLdkT64R%2FtHami8raPqsSClBcgtptHOhKGyRZkO%2FZtlNO73E%2B%2FuLtV8VOqeIF2mauZO0RQ%2FpIQFm7mMSGMmBOlfPHdsguyEZ613VgrzX%2FZoSTeBSKj7095nDD5m%2Fy8BjqkAVEP%2BRoIIvjaPWqGIznJKxTwBOeiAMg6wfu4Di%2BrSt%2FfVst2ssiIQs0ztQgJX%2Bp%2BB4cO9Uet5bpPTbwEOZTOWYAM7ZW6RTC4ycZJ24%2Bkb7P8dzai7%2FJtjARbL%2BrRiYtBxITNMdyFVChXetArqOGzm3%2BazWCt776L%2Fm4hel4vCpBvesAZCvgqP14DBnbcTyTbZugsI8Ukzi0Oqz53Y2VhPEZoKf7l&X-Amz-Signature=26915063fd89ed241a7a218f0d14380271039af0119ccb09c158afe8101098db&X-Amz-SignedHeaders=host&x-id=GetObject)
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


