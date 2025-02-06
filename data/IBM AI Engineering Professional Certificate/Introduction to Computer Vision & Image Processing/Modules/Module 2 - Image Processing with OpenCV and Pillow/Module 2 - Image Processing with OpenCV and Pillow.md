

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLKUHVMX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCyw23XjGksMvOBA%2B17utHDZR2sFybV5oKo43MHlbPlmAIhALA9tMcARbVrDg8xrVWnGrajUk3vS8PrtvIt8LqBts6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzL7Mx645PpMuukdvwq3ANq82u8SBojKnU6Z6SmdSM3qkTKy10F4zmZqYHja5bFHMvwjwOwMMtNVXMKK7ittbm8VyVCddEq553ZGYXQ19G4%2Fmz0m2LIMk3LvG9aQptSHv0uNqtMxzb3Ut4jNR0VeZwXFZWejaiOZczM0A8PNk5LubWt8I8rfoaJPDTD2rSvTdp8r%2Fh24x8cMWOz3nSTXKcFeedvDqta5f65NX1v9%2Bg9qj5fWAwbLaiL584CAJHB0vyIbAOclyrqrIlmDvh1Dxwi0WT6g5KhyuWxw%2FJLZGBlfqdzcxShBAGE2nHG345CQWaCuRNQJk3ccWYULUBmiuYgEfmXY%2FsH8ZNF%2BFTCfyHr2k7x%2BoRaTu6E4YoDHqrrByxs0DzPWqQFOjldQrTxJkki4NyzLiwCNLvBV%2FICksnX2lJz7tY05RdgztVFG3Q0xw%2FbsfEV9ehYogPZLQVc4mOYfC6iP48kS%2F6hVY2AQX0v6UDr8sFm2C%2FIZJzzBM72z0g5Puc0SmrqslHhp0mYHXc8amsevgO2s9RFH41SQOwYX1v81SnsKOljWy0bxiwpoon9JrF4smNTsXfj5fifWLSLy07oRUXbKao5KKaSVbFBscRQwAUwLBEqqEKgSpJxMAr4SBdH6TvkFGlaPTCT0ZO9BjqkAf%2BQLbKsaZ%2FHRwgLlczET%2FVIYge%2B%2FLsItkzEsRTeZ2hTT%2BE3vtW4XfDsTd9dZrSaOSUmaISHQECp1ObpFFFR6yg%2BCzGtYDYRcYuTproG04u8v6FK61i%2BEZztxZXdAJjImTRmj7ZDzIOHdaRoNvoxP83v9CuYtWLeRwx%2FACxGyEDf0kebeJaAE69cpukrcrqFoVfmOsoW43aSrw172RZ7lZZS6KC6&X-Amz-Signature=b7d105e7dc9d9df0f79b63c5c06d5ad51019f18a6b71b7a1b2a3222731ac5d85&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I2REY5R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDXCB%2FHIa%2BW4p1devWapB18PiTdCShUiI3nTiwPEDTsRwIhAJRNDLsxG3FxQTXjfrHYcgvnqDpc9ZNTtyTfqPQl1M6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzFx%2BRBvtwBciQMPOgq3AN4w0jMQxPeNyNMsDEQ8p2F%2Bn5kwlzaAOSDNwK9V7ZXZt5%2Bn65PE5x3F9yOu05TCZi1C3Q6TqLT8KOy7c%2FAh9sIP4M%2FCa%2B4q6mFHl61u1tKAjcpCVebKCmiIS6Iz0%2FItjtJDG15f4KdeQ6ErTK60weGMKjmpd3ST2rc0KqhfuLQvy%2FPAnETudM9qmvsJsvl2vUuFHYgnDHfowTNZm7r1BPNIIukZU2AXpMpgRnxNGVybiaWOF80qMGOtvBdJ6I13aQtJdNFxXj53oKCMmgLylZnGgKrQjA3WdSF%2Fxful1FvE9zJ5Ubz8tGgz72OZWTkuqO23Y0xzUTEMYwM3QRwcr0kHZQY1WIFWHd6ZcOESoJRehYFmWHYckrLSl4vQWjRthmsW4Z0ql%2Bxse3GPEOUsnts18fJNiWBr0Og%2BoIANABhMLwOKUX5mYfskppU9%2BtOFn8Wg8BvFCxqii8HvrkCrIGXkd643NSw1o0PYQ4epxSNa6jdrnwBkvmyOSFX%2BTKJPmkZWhfugjWG5%2B6a4I%2BeOe6%2FiGD611cM6YH60tt8VPcfwtLkYOuDzmUYiamlJ0dPNYZ3Z2jcZyMOj0wFNXoNaVmTyoK%2FcS6AHIQTtvBfDey8PFgmwbjIKxCCDzrCGzCJ0ZO9BjqkAYNb3eSI5HK3s7jDiWXk5wvoqc8Abp66FI%2B6viDTAntwArp5u3H63YXOrzGaD6KYk%2BNGEt5oac4sPlw6VYhZTC9wDfk8%2BbVrO4MuNfr8e%2B9IQuVAiudtQqG5TGR6sGLt5T9smJIwr68Mp5gBDyHdZ8tj78CXIVy%2FXEFocIrMtHvSbzybCKPb8KsacO6C2zaPAxeWBZABwVlaSEajOM01SSyklaUM&X-Amz-Signature=607c6cab378f56008cb2f7aad8374684136f3cbeaac7205b0e38df67a018ee3f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I2REY5R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDXCB%2FHIa%2BW4p1devWapB18PiTdCShUiI3nTiwPEDTsRwIhAJRNDLsxG3FxQTXjfrHYcgvnqDpc9ZNTtyTfqPQl1M6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzFx%2BRBvtwBciQMPOgq3AN4w0jMQxPeNyNMsDEQ8p2F%2Bn5kwlzaAOSDNwK9V7ZXZt5%2Bn65PE5x3F9yOu05TCZi1C3Q6TqLT8KOy7c%2FAh9sIP4M%2FCa%2B4q6mFHl61u1tKAjcpCVebKCmiIS6Iz0%2FItjtJDG15f4KdeQ6ErTK60weGMKjmpd3ST2rc0KqhfuLQvy%2FPAnETudM9qmvsJsvl2vUuFHYgnDHfowTNZm7r1BPNIIukZU2AXpMpgRnxNGVybiaWOF80qMGOtvBdJ6I13aQtJdNFxXj53oKCMmgLylZnGgKrQjA3WdSF%2Fxful1FvE9zJ5Ubz8tGgz72OZWTkuqO23Y0xzUTEMYwM3QRwcr0kHZQY1WIFWHd6ZcOESoJRehYFmWHYckrLSl4vQWjRthmsW4Z0ql%2Bxse3GPEOUsnts18fJNiWBr0Og%2BoIANABhMLwOKUX5mYfskppU9%2BtOFn8Wg8BvFCxqii8HvrkCrIGXkd643NSw1o0PYQ4epxSNa6jdrnwBkvmyOSFX%2BTKJPmkZWhfugjWG5%2B6a4I%2BeOe6%2FiGD611cM6YH60tt8VPcfwtLkYOuDzmUYiamlJ0dPNYZ3Z2jcZyMOj0wFNXoNaVmTyoK%2FcS6AHIQTtvBfDey8PFgmwbjIKxCCDzrCGzCJ0ZO9BjqkAYNb3eSI5HK3s7jDiWXk5wvoqc8Abp66FI%2B6viDTAntwArp5u3H63YXOrzGaD6KYk%2BNGEt5oac4sPlw6VYhZTC9wDfk8%2BbVrO4MuNfr8e%2B9IQuVAiudtQqG5TGR6sGLt5T9smJIwr68Mp5gBDyHdZ8tj78CXIVy%2FXEFocIrMtHvSbzybCKPb8KsacO6C2zaPAxeWBZABwVlaSEajOM01SSyklaUM&X-Amz-Signature=819e5905026711516cb18b079d0863cf8ac708efb2f7fc5e0c19e8f5984e62ec&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I2REY5R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDXCB%2FHIa%2BW4p1devWapB18PiTdCShUiI3nTiwPEDTsRwIhAJRNDLsxG3FxQTXjfrHYcgvnqDpc9ZNTtyTfqPQl1M6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzFx%2BRBvtwBciQMPOgq3AN4w0jMQxPeNyNMsDEQ8p2F%2Bn5kwlzaAOSDNwK9V7ZXZt5%2Bn65PE5x3F9yOu05TCZi1C3Q6TqLT8KOy7c%2FAh9sIP4M%2FCa%2B4q6mFHl61u1tKAjcpCVebKCmiIS6Iz0%2FItjtJDG15f4KdeQ6ErTK60weGMKjmpd3ST2rc0KqhfuLQvy%2FPAnETudM9qmvsJsvl2vUuFHYgnDHfowTNZm7r1BPNIIukZU2AXpMpgRnxNGVybiaWOF80qMGOtvBdJ6I13aQtJdNFxXj53oKCMmgLylZnGgKrQjA3WdSF%2Fxful1FvE9zJ5Ubz8tGgz72OZWTkuqO23Y0xzUTEMYwM3QRwcr0kHZQY1WIFWHd6ZcOESoJRehYFmWHYckrLSl4vQWjRthmsW4Z0ql%2Bxse3GPEOUsnts18fJNiWBr0Og%2BoIANABhMLwOKUX5mYfskppU9%2BtOFn8Wg8BvFCxqii8HvrkCrIGXkd643NSw1o0PYQ4epxSNa6jdrnwBkvmyOSFX%2BTKJPmkZWhfugjWG5%2B6a4I%2BeOe6%2FiGD611cM6YH60tt8VPcfwtLkYOuDzmUYiamlJ0dPNYZ3Z2jcZyMOj0wFNXoNaVmTyoK%2FcS6AHIQTtvBfDey8PFgmwbjIKxCCDzrCGzCJ0ZO9BjqkAYNb3eSI5HK3s7jDiWXk5wvoqc8Abp66FI%2B6viDTAntwArp5u3H63YXOrzGaD6KYk%2BNGEt5oac4sPlw6VYhZTC9wDfk8%2BbVrO4MuNfr8e%2B9IQuVAiudtQqG5TGR6sGLt5T9smJIwr68Mp5gBDyHdZ8tj78CXIVy%2FXEFocIrMtHvSbzybCKPb8KsacO6C2zaPAxeWBZABwVlaSEajOM01SSyklaUM&X-Amz-Signature=f295f33507624d2a30c1b5cfbb5d5703e89d3add14d707e6e0b688a74f5b5ece&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I2REY5R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDXCB%2FHIa%2BW4p1devWapB18PiTdCShUiI3nTiwPEDTsRwIhAJRNDLsxG3FxQTXjfrHYcgvnqDpc9ZNTtyTfqPQl1M6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzFx%2BRBvtwBciQMPOgq3AN4w0jMQxPeNyNMsDEQ8p2F%2Bn5kwlzaAOSDNwK9V7ZXZt5%2Bn65PE5x3F9yOu05TCZi1C3Q6TqLT8KOy7c%2FAh9sIP4M%2FCa%2B4q6mFHl61u1tKAjcpCVebKCmiIS6Iz0%2FItjtJDG15f4KdeQ6ErTK60weGMKjmpd3ST2rc0KqhfuLQvy%2FPAnETudM9qmvsJsvl2vUuFHYgnDHfowTNZm7r1BPNIIukZU2AXpMpgRnxNGVybiaWOF80qMGOtvBdJ6I13aQtJdNFxXj53oKCMmgLylZnGgKrQjA3WdSF%2Fxful1FvE9zJ5Ubz8tGgz72OZWTkuqO23Y0xzUTEMYwM3QRwcr0kHZQY1WIFWHd6ZcOESoJRehYFmWHYckrLSl4vQWjRthmsW4Z0ql%2Bxse3GPEOUsnts18fJNiWBr0Og%2BoIANABhMLwOKUX5mYfskppU9%2BtOFn8Wg8BvFCxqii8HvrkCrIGXkd643NSw1o0PYQ4epxSNa6jdrnwBkvmyOSFX%2BTKJPmkZWhfugjWG5%2B6a4I%2BeOe6%2FiGD611cM6YH60tt8VPcfwtLkYOuDzmUYiamlJ0dPNYZ3Z2jcZyMOj0wFNXoNaVmTyoK%2FcS6AHIQTtvBfDey8PFgmwbjIKxCCDzrCGzCJ0ZO9BjqkAYNb3eSI5HK3s7jDiWXk5wvoqc8Abp66FI%2B6viDTAntwArp5u3H63YXOrzGaD6KYk%2BNGEt5oac4sPlw6VYhZTC9wDfk8%2BbVrO4MuNfr8e%2B9IQuVAiudtQqG5TGR6sGLt5T9smJIwr68Mp5gBDyHdZ8tj78CXIVy%2FXEFocIrMtHvSbzybCKPb8KsacO6C2zaPAxeWBZABwVlaSEajOM01SSyklaUM&X-Amz-Signature=4492c15ae3d2508a9c249fec8a71d4cefec824a0711110bf75d2e764d505e41c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I2REY5R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDXCB%2FHIa%2BW4p1devWapB18PiTdCShUiI3nTiwPEDTsRwIhAJRNDLsxG3FxQTXjfrHYcgvnqDpc9ZNTtyTfqPQl1M6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzFx%2BRBvtwBciQMPOgq3AN4w0jMQxPeNyNMsDEQ8p2F%2Bn5kwlzaAOSDNwK9V7ZXZt5%2Bn65PE5x3F9yOu05TCZi1C3Q6TqLT8KOy7c%2FAh9sIP4M%2FCa%2B4q6mFHl61u1tKAjcpCVebKCmiIS6Iz0%2FItjtJDG15f4KdeQ6ErTK60weGMKjmpd3ST2rc0KqhfuLQvy%2FPAnETudM9qmvsJsvl2vUuFHYgnDHfowTNZm7r1BPNIIukZU2AXpMpgRnxNGVybiaWOF80qMGOtvBdJ6I13aQtJdNFxXj53oKCMmgLylZnGgKrQjA3WdSF%2Fxful1FvE9zJ5Ubz8tGgz72OZWTkuqO23Y0xzUTEMYwM3QRwcr0kHZQY1WIFWHd6ZcOESoJRehYFmWHYckrLSl4vQWjRthmsW4Z0ql%2Bxse3GPEOUsnts18fJNiWBr0Og%2BoIANABhMLwOKUX5mYfskppU9%2BtOFn8Wg8BvFCxqii8HvrkCrIGXkd643NSw1o0PYQ4epxSNa6jdrnwBkvmyOSFX%2BTKJPmkZWhfugjWG5%2B6a4I%2BeOe6%2FiGD611cM6YH60tt8VPcfwtLkYOuDzmUYiamlJ0dPNYZ3Z2jcZyMOj0wFNXoNaVmTyoK%2FcS6AHIQTtvBfDey8PFgmwbjIKxCCDzrCGzCJ0ZO9BjqkAYNb3eSI5HK3s7jDiWXk5wvoqc8Abp66FI%2B6viDTAntwArp5u3H63YXOrzGaD6KYk%2BNGEt5oac4sPlw6VYhZTC9wDfk8%2BbVrO4MuNfr8e%2B9IQuVAiudtQqG5TGR6sGLt5T9smJIwr68Mp5gBDyHdZ8tj78CXIVy%2FXEFocIrMtHvSbzybCKPb8KsacO6C2zaPAxeWBZABwVlaSEajOM01SSyklaUM&X-Amz-Signature=587fbfc2c4e82e32cc8fe41bcfc8d4e64f4811680646854942704f590042c049&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLKUHVMX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCyw23XjGksMvOBA%2B17utHDZR2sFybV5oKo43MHlbPlmAIhALA9tMcARbVrDg8xrVWnGrajUk3vS8PrtvIt8LqBts6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzL7Mx645PpMuukdvwq3ANq82u8SBojKnU6Z6SmdSM3qkTKy10F4zmZqYHja5bFHMvwjwOwMMtNVXMKK7ittbm8VyVCddEq553ZGYXQ19G4%2Fmz0m2LIMk3LvG9aQptSHv0uNqtMxzb3Ut4jNR0VeZwXFZWejaiOZczM0A8PNk5LubWt8I8rfoaJPDTD2rSvTdp8r%2Fh24x8cMWOz3nSTXKcFeedvDqta5f65NX1v9%2Bg9qj5fWAwbLaiL584CAJHB0vyIbAOclyrqrIlmDvh1Dxwi0WT6g5KhyuWxw%2FJLZGBlfqdzcxShBAGE2nHG345CQWaCuRNQJk3ccWYULUBmiuYgEfmXY%2FsH8ZNF%2BFTCfyHr2k7x%2BoRaTu6E4YoDHqrrByxs0DzPWqQFOjldQrTxJkki4NyzLiwCNLvBV%2FICksnX2lJz7tY05RdgztVFG3Q0xw%2FbsfEV9ehYogPZLQVc4mOYfC6iP48kS%2F6hVY2AQX0v6UDr8sFm2C%2FIZJzzBM72z0g5Puc0SmrqslHhp0mYHXc8amsevgO2s9RFH41SQOwYX1v81SnsKOljWy0bxiwpoon9JrF4smNTsXfj5fifWLSLy07oRUXbKao5KKaSVbFBscRQwAUwLBEqqEKgSpJxMAr4SBdH6TvkFGlaPTCT0ZO9BjqkAf%2BQLbKsaZ%2FHRwgLlczET%2FVIYge%2B%2FLsItkzEsRTeZ2hTT%2BE3vtW4XfDsTd9dZrSaOSUmaISHQECp1ObpFFFR6yg%2BCzGtYDYRcYuTproG04u8v6FK61i%2BEZztxZXdAJjImTRmj7ZDzIOHdaRoNvoxP83v9CuYtWLeRwx%2FACxGyEDf0kebeJaAE69cpukrcrqFoVfmOsoW43aSrw172RZ7lZZS6KC6&X-Amz-Signature=ddd34c964e5bc291cfd63332a22d53e479ebd74e687b3fa89adeda3fd3724ccf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLKUHVMX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCyw23XjGksMvOBA%2B17utHDZR2sFybV5oKo43MHlbPlmAIhALA9tMcARbVrDg8xrVWnGrajUk3vS8PrtvIt8LqBts6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzL7Mx645PpMuukdvwq3ANq82u8SBojKnU6Z6SmdSM3qkTKy10F4zmZqYHja5bFHMvwjwOwMMtNVXMKK7ittbm8VyVCddEq553ZGYXQ19G4%2Fmz0m2LIMk3LvG9aQptSHv0uNqtMxzb3Ut4jNR0VeZwXFZWejaiOZczM0A8PNk5LubWt8I8rfoaJPDTD2rSvTdp8r%2Fh24x8cMWOz3nSTXKcFeedvDqta5f65NX1v9%2Bg9qj5fWAwbLaiL584CAJHB0vyIbAOclyrqrIlmDvh1Dxwi0WT6g5KhyuWxw%2FJLZGBlfqdzcxShBAGE2nHG345CQWaCuRNQJk3ccWYULUBmiuYgEfmXY%2FsH8ZNF%2BFTCfyHr2k7x%2BoRaTu6E4YoDHqrrByxs0DzPWqQFOjldQrTxJkki4NyzLiwCNLvBV%2FICksnX2lJz7tY05RdgztVFG3Q0xw%2FbsfEV9ehYogPZLQVc4mOYfC6iP48kS%2F6hVY2AQX0v6UDr8sFm2C%2FIZJzzBM72z0g5Puc0SmrqslHhp0mYHXc8amsevgO2s9RFH41SQOwYX1v81SnsKOljWy0bxiwpoon9JrF4smNTsXfj5fifWLSLy07oRUXbKao5KKaSVbFBscRQwAUwLBEqqEKgSpJxMAr4SBdH6TvkFGlaPTCT0ZO9BjqkAf%2BQLbKsaZ%2FHRwgLlczET%2FVIYge%2B%2FLsItkzEsRTeZ2hTT%2BE3vtW4XfDsTd9dZrSaOSUmaISHQECp1ObpFFFR6yg%2BCzGtYDYRcYuTproG04u8v6FK61i%2BEZztxZXdAJjImTRmj7ZDzIOHdaRoNvoxP83v9CuYtWLeRwx%2FACxGyEDf0kebeJaAE69cpukrcrqFoVfmOsoW43aSrw172RZ7lZZS6KC6&X-Amz-Signature=ae0a55a4e19a579bc00fe39ba47e3eb787c1014d2a80afb876a9f8d201bd6934&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLKUHVMX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCyw23XjGksMvOBA%2B17utHDZR2sFybV5oKo43MHlbPlmAIhALA9tMcARbVrDg8xrVWnGrajUk3vS8PrtvIt8LqBts6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzL7Mx645PpMuukdvwq3ANq82u8SBojKnU6Z6SmdSM3qkTKy10F4zmZqYHja5bFHMvwjwOwMMtNVXMKK7ittbm8VyVCddEq553ZGYXQ19G4%2Fmz0m2LIMk3LvG9aQptSHv0uNqtMxzb3Ut4jNR0VeZwXFZWejaiOZczM0A8PNk5LubWt8I8rfoaJPDTD2rSvTdp8r%2Fh24x8cMWOz3nSTXKcFeedvDqta5f65NX1v9%2Bg9qj5fWAwbLaiL584CAJHB0vyIbAOclyrqrIlmDvh1Dxwi0WT6g5KhyuWxw%2FJLZGBlfqdzcxShBAGE2nHG345CQWaCuRNQJk3ccWYULUBmiuYgEfmXY%2FsH8ZNF%2BFTCfyHr2k7x%2BoRaTu6E4YoDHqrrByxs0DzPWqQFOjldQrTxJkki4NyzLiwCNLvBV%2FICksnX2lJz7tY05RdgztVFG3Q0xw%2FbsfEV9ehYogPZLQVc4mOYfC6iP48kS%2F6hVY2AQX0v6UDr8sFm2C%2FIZJzzBM72z0g5Puc0SmrqslHhp0mYHXc8amsevgO2s9RFH41SQOwYX1v81SnsKOljWy0bxiwpoon9JrF4smNTsXfj5fifWLSLy07oRUXbKao5KKaSVbFBscRQwAUwLBEqqEKgSpJxMAr4SBdH6TvkFGlaPTCT0ZO9BjqkAf%2BQLbKsaZ%2FHRwgLlczET%2FVIYge%2B%2FLsItkzEsRTeZ2hTT%2BE3vtW4XfDsTd9dZrSaOSUmaISHQECp1ObpFFFR6yg%2BCzGtYDYRcYuTproG04u8v6FK61i%2BEZztxZXdAJjImTRmj7ZDzIOHdaRoNvoxP83v9CuYtWLeRwx%2FACxGyEDf0kebeJaAE69cpukrcrqFoVfmOsoW43aSrw172RZ7lZZS6KC6&X-Amz-Signature=ca7f2b0aa4bd001be35404feabf1f2408e498cb9099acd8fa28fa42b245d1c6a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLKUHVMX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCyw23XjGksMvOBA%2B17utHDZR2sFybV5oKo43MHlbPlmAIhALA9tMcARbVrDg8xrVWnGrajUk3vS8PrtvIt8LqBts6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzL7Mx645PpMuukdvwq3ANq82u8SBojKnU6Z6SmdSM3qkTKy10F4zmZqYHja5bFHMvwjwOwMMtNVXMKK7ittbm8VyVCddEq553ZGYXQ19G4%2Fmz0m2LIMk3LvG9aQptSHv0uNqtMxzb3Ut4jNR0VeZwXFZWejaiOZczM0A8PNk5LubWt8I8rfoaJPDTD2rSvTdp8r%2Fh24x8cMWOz3nSTXKcFeedvDqta5f65NX1v9%2Bg9qj5fWAwbLaiL584CAJHB0vyIbAOclyrqrIlmDvh1Dxwi0WT6g5KhyuWxw%2FJLZGBlfqdzcxShBAGE2nHG345CQWaCuRNQJk3ccWYULUBmiuYgEfmXY%2FsH8ZNF%2BFTCfyHr2k7x%2BoRaTu6E4YoDHqrrByxs0DzPWqQFOjldQrTxJkki4NyzLiwCNLvBV%2FICksnX2lJz7tY05RdgztVFG3Q0xw%2FbsfEV9ehYogPZLQVc4mOYfC6iP48kS%2F6hVY2AQX0v6UDr8sFm2C%2FIZJzzBM72z0g5Puc0SmrqslHhp0mYHXc8amsevgO2s9RFH41SQOwYX1v81SnsKOljWy0bxiwpoon9JrF4smNTsXfj5fifWLSLy07oRUXbKao5KKaSVbFBscRQwAUwLBEqqEKgSpJxMAr4SBdH6TvkFGlaPTCT0ZO9BjqkAf%2BQLbKsaZ%2FHRwgLlczET%2FVIYge%2B%2FLsItkzEsRTeZ2hTT%2BE3vtW4XfDsTd9dZrSaOSUmaISHQECp1ObpFFFR6yg%2BCzGtYDYRcYuTproG04u8v6FK61i%2BEZztxZXdAJjImTRmj7ZDzIOHdaRoNvoxP83v9CuYtWLeRwx%2FACxGyEDf0kebeJaAE69cpukrcrqFoVfmOsoW43aSrw172RZ7lZZS6KC6&X-Amz-Signature=f243d4c6ef30b73e6f2f637151b148a6a9c79c08f62603088b7b2b319be754d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLKUHVMX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCyw23XjGksMvOBA%2B17utHDZR2sFybV5oKo43MHlbPlmAIhALA9tMcARbVrDg8xrVWnGrajUk3vS8PrtvIt8LqBts6NKv8DCGIQABoMNjM3NDIzMTgzODA1IgzL7Mx645PpMuukdvwq3ANq82u8SBojKnU6Z6SmdSM3qkTKy10F4zmZqYHja5bFHMvwjwOwMMtNVXMKK7ittbm8VyVCddEq553ZGYXQ19G4%2Fmz0m2LIMk3LvG9aQptSHv0uNqtMxzb3Ut4jNR0VeZwXFZWejaiOZczM0A8PNk5LubWt8I8rfoaJPDTD2rSvTdp8r%2Fh24x8cMWOz3nSTXKcFeedvDqta5f65NX1v9%2Bg9qj5fWAwbLaiL584CAJHB0vyIbAOclyrqrIlmDvh1Dxwi0WT6g5KhyuWxw%2FJLZGBlfqdzcxShBAGE2nHG345CQWaCuRNQJk3ccWYULUBmiuYgEfmXY%2FsH8ZNF%2BFTCfyHr2k7x%2BoRaTu6E4YoDHqrrByxs0DzPWqQFOjldQrTxJkki4NyzLiwCNLvBV%2FICksnX2lJz7tY05RdgztVFG3Q0xw%2FbsfEV9ehYogPZLQVc4mOYfC6iP48kS%2F6hVY2AQX0v6UDr8sFm2C%2FIZJzzBM72z0g5Puc0SmrqslHhp0mYHXc8amsevgO2s9RFH41SQOwYX1v81SnsKOljWy0bxiwpoon9JrF4smNTsXfj5fifWLSLy07oRUXbKao5KKaSVbFBscRQwAUwLBEqqEKgSpJxMAr4SBdH6TvkFGlaPTCT0ZO9BjqkAf%2BQLbKsaZ%2FHRwgLlczET%2FVIYge%2B%2FLsItkzEsRTeZ2hTT%2BE3vtW4XfDsTd9dZrSaOSUmaISHQECp1ObpFFFR6yg%2BCzGtYDYRcYuTproG04u8v6FK61i%2BEZztxZXdAJjImTRmj7ZDzIOHdaRoNvoxP83v9CuYtWLeRwx%2FACxGyEDf0kebeJaAE69cpukrcrqFoVfmOsoW43aSrw172RZ7lZZS6KC6&X-Amz-Signature=12391f4a8395bb6dc4be5a72bdaa0553cddbeff735224523e65b093c3a1ab61b&X-Amz-SignedHeaders=host&x-id=GetObject)
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


