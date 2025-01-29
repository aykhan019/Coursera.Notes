

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US7G67J5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUgOLkPrw9%2FHBC%2Br7F0UkbbHPjcHln%2B9BkCgJSPQOCDgIhANmytvvJ%2FUTGPU8X%2FLa%2FaqKk9CU3O5HooVokUDlcNxScKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igycjdh4YSELf%2BA%2B9K0q3ANGNtTVA43lSZoUIlithXoLaguNyjzRi75M6L94FXiNjHHZEt9GG7vJ%2B%2BoyWZkZkTSHVyjpPqp2F6wGP52JSS0kksDyWU%2BIeKVX25MOFJmRj2wlcCkJDRrkWGlkC6nh2Qa4wnkwNIqmboGIvyq6BuxLaB3kTt0rmWZCExbTa0K7b5FFNL1kmwi5%2FtSg0VsqO4AJs8mjoQYUC4ImEgxOx%2FsnKwvIFgoNTEiB1JVi9vL2gbyiJDhI7cZyyu6MwGfUFzmNrfpg3R99Jb4qdfwAVTFakwLKKY0Ok7TROlL1p1A2iRx2%2FLFjd50pi%2Fi6ktHkREMQp6XT7c%2B2KCDYg9cX0CPKZjdlRpzuEzOcTG5SMPb%2BFu263DBwR67MdADavEYvAhC2NL1AD%2BG8hvvBNVQXK%2BqGNT7it0CPWReP8xNkw6r1Rs5pfStkl1DrcYjI2tr2tmO9WWGDVjCOK8YO46eF4pZukizgFDfEcwA2L%2BdT0QxRNhrC%2FMdvYvC87XniQKk4ZOFAJvae%2FYnMJMU19F9R1HJ84OU%2FNucMtEf4zOpHV2y18UaI2oUE8MqqC%2Fl9H%2FJbjhxwp5bVCqlrPY6JXfgcFVUJHmx2UF2aWVZcBh4qXZmQPj%2FdHXyY9NLQIEndVTDhu%2Bm8BjqkAaqg67mAM09xq%2F91SroJQm4ff4VXMVEcS72jDtEC2v4tIvVgLOlQC2GFGyi1RQ2vmiCRgkFYML9eGzYDT7yNb0AF0slDkU%2BDADTfxcaRtF4nL4Irt6MINobe3ykNGwvfptApa7eFHbei9EMJSFvjGZubaTsQ%2FzMGp%2BDEBRDari6IaM6%2FGdQPsMOw7UEdcxd4FYedRzT%2BdZ3ppCOxuFzs0Vnifdbh&X-Amz-Signature=1db5f1ed9d530bf74854cc66d9483aa550fe6a0ad70d0d266a6fe621dea52dd2&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIEDQMHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjz6h7Auuto1x%2FkOB0%2FHdhjVpJwgN0z%2BS7FPpoUYrwrwIgSJR287AzOh%2Buq628fVrIIzdkduRic4d2SOM%2F%2BmtQLrMqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMVaLh%2B4svACzK1RCrcA4SuJhoA7Y4VKuExr0N8W1v4%2BNc6nvx%2BCk3kaXdzii%2BP8kQ8FyEnAolZj45c3%2FAgqJyPdOs90eaLC9WTyi7Y9JWYJXr5qe6Da4mKCwxac81oW7dp99W9aOyatqm8NJh6nvmsOQvTx%2BTkwNVRdHNvU9OlPzbIuxH9Ma0Tx907GJGiMim8VTqQkXbGjl8NuhpGcJjPlEuLih%2FEdvsQIq%2FHRPRd7JTku3mKqtHPqNIXHv287o3JQwKVD7QGogOCgHjk9ov2xp3xmHSlJbh%2Bw3zqe2XFhmzbwoXfaiONkCK%2FW1fvXp%2BiSHbnH22fHq%2ByK%2FNVkqZSZlquRTRiMfjvFTD1OalIFDi92DJo9YgzMydP41XgDPUk1oRflgnCC72sQGa5uA62QoaoxV5DzokkwpCNbvOM9KuNPPhz5mdLAPrynhq17TbBsXjJWlbR4IMD1PhTfniZGrrCiznXuztlo1CoWyt%2FqAV%2F%2BSae66H2DBFsjXqR8pYRF7WIw3iQxRFcxqOLk4%2F5vM4fbjVR%2FCOxwJvP0sRnpMOL6HGJK9ICzOVpC0PsscbIPJNV%2FpJMXqMPML4ITl5Qk5WX2g2HM8fPAVtvEOvXDNjP%2B0RPo3%2BhHxJmecRMIeuJTblU21HtfmRIMJm86bwGOqUB8GCEOFYZTjydN8yp1M4UE5fOe2cuzE2lSy%2BVzSKnC9C2KSwOnKIIitzUTOw1XU984hz3ZNmVywV5Yp%2BywI71oERpPAdYdS4FDBaMyHM0Wm7Vf3L4owsfIOmTNWsFL2uHagIh1uC8YFO88iNEBbLzGTWW02kwCSkl%2FqR5r74S6paTX1vwXZ9OPYPN4n3zfbiCATQvm9vS0sD9EuXZB2ggaV%2FKqRpI&X-Amz-Signature=55449a5319d706c6c56bc84043b29344a0530ec7c8c9a824936becde8397cb2b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIEDQMHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjz6h7Auuto1x%2FkOB0%2FHdhjVpJwgN0z%2BS7FPpoUYrwrwIgSJR287AzOh%2Buq628fVrIIzdkduRic4d2SOM%2F%2BmtQLrMqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMVaLh%2B4svACzK1RCrcA4SuJhoA7Y4VKuExr0N8W1v4%2BNc6nvx%2BCk3kaXdzii%2BP8kQ8FyEnAolZj45c3%2FAgqJyPdOs90eaLC9WTyi7Y9JWYJXr5qe6Da4mKCwxac81oW7dp99W9aOyatqm8NJh6nvmsOQvTx%2BTkwNVRdHNvU9OlPzbIuxH9Ma0Tx907GJGiMim8VTqQkXbGjl8NuhpGcJjPlEuLih%2FEdvsQIq%2FHRPRd7JTku3mKqtHPqNIXHv287o3JQwKVD7QGogOCgHjk9ov2xp3xmHSlJbh%2Bw3zqe2XFhmzbwoXfaiONkCK%2FW1fvXp%2BiSHbnH22fHq%2ByK%2FNVkqZSZlquRTRiMfjvFTD1OalIFDi92DJo9YgzMydP41XgDPUk1oRflgnCC72sQGa5uA62QoaoxV5DzokkwpCNbvOM9KuNPPhz5mdLAPrynhq17TbBsXjJWlbR4IMD1PhTfniZGrrCiznXuztlo1CoWyt%2FqAV%2F%2BSae66H2DBFsjXqR8pYRF7WIw3iQxRFcxqOLk4%2F5vM4fbjVR%2FCOxwJvP0sRnpMOL6HGJK9ICzOVpC0PsscbIPJNV%2FpJMXqMPML4ITl5Qk5WX2g2HM8fPAVtvEOvXDNjP%2B0RPo3%2BhHxJmecRMIeuJTblU21HtfmRIMJm86bwGOqUB8GCEOFYZTjydN8yp1M4UE5fOe2cuzE2lSy%2BVzSKnC9C2KSwOnKIIitzUTOw1XU984hz3ZNmVywV5Yp%2BywI71oERpPAdYdS4FDBaMyHM0Wm7Vf3L4owsfIOmTNWsFL2uHagIh1uC8YFO88iNEBbLzGTWW02kwCSkl%2FqR5r74S6paTX1vwXZ9OPYPN4n3zfbiCATQvm9vS0sD9EuXZB2ggaV%2FKqRpI&X-Amz-Signature=09409f179e8ec5e6aca5dfe7268bf4b407c2e3b955dbc86e3e204c933d4f828f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIEDQMHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjz6h7Auuto1x%2FkOB0%2FHdhjVpJwgN0z%2BS7FPpoUYrwrwIgSJR287AzOh%2Buq628fVrIIzdkduRic4d2SOM%2F%2BmtQLrMqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMVaLh%2B4svACzK1RCrcA4SuJhoA7Y4VKuExr0N8W1v4%2BNc6nvx%2BCk3kaXdzii%2BP8kQ8FyEnAolZj45c3%2FAgqJyPdOs90eaLC9WTyi7Y9JWYJXr5qe6Da4mKCwxac81oW7dp99W9aOyatqm8NJh6nvmsOQvTx%2BTkwNVRdHNvU9OlPzbIuxH9Ma0Tx907GJGiMim8VTqQkXbGjl8NuhpGcJjPlEuLih%2FEdvsQIq%2FHRPRd7JTku3mKqtHPqNIXHv287o3JQwKVD7QGogOCgHjk9ov2xp3xmHSlJbh%2Bw3zqe2XFhmzbwoXfaiONkCK%2FW1fvXp%2BiSHbnH22fHq%2ByK%2FNVkqZSZlquRTRiMfjvFTD1OalIFDi92DJo9YgzMydP41XgDPUk1oRflgnCC72sQGa5uA62QoaoxV5DzokkwpCNbvOM9KuNPPhz5mdLAPrynhq17TbBsXjJWlbR4IMD1PhTfniZGrrCiznXuztlo1CoWyt%2FqAV%2F%2BSae66H2DBFsjXqR8pYRF7WIw3iQxRFcxqOLk4%2F5vM4fbjVR%2FCOxwJvP0sRnpMOL6HGJK9ICzOVpC0PsscbIPJNV%2FpJMXqMPML4ITl5Qk5WX2g2HM8fPAVtvEOvXDNjP%2B0RPo3%2BhHxJmecRMIeuJTblU21HtfmRIMJm86bwGOqUB8GCEOFYZTjydN8yp1M4UE5fOe2cuzE2lSy%2BVzSKnC9C2KSwOnKIIitzUTOw1XU984hz3ZNmVywV5Yp%2BywI71oERpPAdYdS4FDBaMyHM0Wm7Vf3L4owsfIOmTNWsFL2uHagIh1uC8YFO88iNEBbLzGTWW02kwCSkl%2FqR5r74S6paTX1vwXZ9OPYPN4n3zfbiCATQvm9vS0sD9EuXZB2ggaV%2FKqRpI&X-Amz-Signature=6154ca6b2cc4c681b19ec3ae9e14cc432b9b2894af5e8ba1117d685541160daa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIEDQMHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjz6h7Auuto1x%2FkOB0%2FHdhjVpJwgN0z%2BS7FPpoUYrwrwIgSJR287AzOh%2Buq628fVrIIzdkduRic4d2SOM%2F%2BmtQLrMqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMVaLh%2B4svACzK1RCrcA4SuJhoA7Y4VKuExr0N8W1v4%2BNc6nvx%2BCk3kaXdzii%2BP8kQ8FyEnAolZj45c3%2FAgqJyPdOs90eaLC9WTyi7Y9JWYJXr5qe6Da4mKCwxac81oW7dp99W9aOyatqm8NJh6nvmsOQvTx%2BTkwNVRdHNvU9OlPzbIuxH9Ma0Tx907GJGiMim8VTqQkXbGjl8NuhpGcJjPlEuLih%2FEdvsQIq%2FHRPRd7JTku3mKqtHPqNIXHv287o3JQwKVD7QGogOCgHjk9ov2xp3xmHSlJbh%2Bw3zqe2XFhmzbwoXfaiONkCK%2FW1fvXp%2BiSHbnH22fHq%2ByK%2FNVkqZSZlquRTRiMfjvFTD1OalIFDi92DJo9YgzMydP41XgDPUk1oRflgnCC72sQGa5uA62QoaoxV5DzokkwpCNbvOM9KuNPPhz5mdLAPrynhq17TbBsXjJWlbR4IMD1PhTfniZGrrCiznXuztlo1CoWyt%2FqAV%2F%2BSae66H2DBFsjXqR8pYRF7WIw3iQxRFcxqOLk4%2F5vM4fbjVR%2FCOxwJvP0sRnpMOL6HGJK9ICzOVpC0PsscbIPJNV%2FpJMXqMPML4ITl5Qk5WX2g2HM8fPAVtvEOvXDNjP%2B0RPo3%2BhHxJmecRMIeuJTblU21HtfmRIMJm86bwGOqUB8GCEOFYZTjydN8yp1M4UE5fOe2cuzE2lSy%2BVzSKnC9C2KSwOnKIIitzUTOw1XU984hz3ZNmVywV5Yp%2BywI71oERpPAdYdS4FDBaMyHM0Wm7Vf3L4owsfIOmTNWsFL2uHagIh1uC8YFO88iNEBbLzGTWW02kwCSkl%2FqR5r74S6paTX1vwXZ9OPYPN4n3zfbiCATQvm9vS0sD9EuXZB2ggaV%2FKqRpI&X-Amz-Signature=89c42f657afa45cdb94a1dd0a6ab7bd588661021b7875c21b385672cefa7710a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIEDQMHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjz6h7Auuto1x%2FkOB0%2FHdhjVpJwgN0z%2BS7FPpoUYrwrwIgSJR287AzOh%2Buq628fVrIIzdkduRic4d2SOM%2F%2BmtQLrMqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMVaLh%2B4svACzK1RCrcA4SuJhoA7Y4VKuExr0N8W1v4%2BNc6nvx%2BCk3kaXdzii%2BP8kQ8FyEnAolZj45c3%2FAgqJyPdOs90eaLC9WTyi7Y9JWYJXr5qe6Da4mKCwxac81oW7dp99W9aOyatqm8NJh6nvmsOQvTx%2BTkwNVRdHNvU9OlPzbIuxH9Ma0Tx907GJGiMim8VTqQkXbGjl8NuhpGcJjPlEuLih%2FEdvsQIq%2FHRPRd7JTku3mKqtHPqNIXHv287o3JQwKVD7QGogOCgHjk9ov2xp3xmHSlJbh%2Bw3zqe2XFhmzbwoXfaiONkCK%2FW1fvXp%2BiSHbnH22fHq%2ByK%2FNVkqZSZlquRTRiMfjvFTD1OalIFDi92DJo9YgzMydP41XgDPUk1oRflgnCC72sQGa5uA62QoaoxV5DzokkwpCNbvOM9KuNPPhz5mdLAPrynhq17TbBsXjJWlbR4IMD1PhTfniZGrrCiznXuztlo1CoWyt%2FqAV%2F%2BSae66H2DBFsjXqR8pYRF7WIw3iQxRFcxqOLk4%2F5vM4fbjVR%2FCOxwJvP0sRnpMOL6HGJK9ICzOVpC0PsscbIPJNV%2FpJMXqMPML4ITl5Qk5WX2g2HM8fPAVtvEOvXDNjP%2B0RPo3%2BhHxJmecRMIeuJTblU21HtfmRIMJm86bwGOqUB8GCEOFYZTjydN8yp1M4UE5fOe2cuzE2lSy%2BVzSKnC9C2KSwOnKIIitzUTOw1XU984hz3ZNmVywV5Yp%2BywI71oERpPAdYdS4FDBaMyHM0Wm7Vf3L4owsfIOmTNWsFL2uHagIh1uC8YFO88iNEBbLzGTWW02kwCSkl%2FqR5r74S6paTX1vwXZ9OPYPN4n3zfbiCATQvm9vS0sD9EuXZB2ggaV%2FKqRpI&X-Amz-Signature=d1bd64503a8cd97ccd7bcde5268609e7505747b78647dbbd9e0b1ca50dd41a26&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US7G67J5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUgOLkPrw9%2FHBC%2Br7F0UkbbHPjcHln%2B9BkCgJSPQOCDgIhANmytvvJ%2FUTGPU8X%2FLa%2FaqKk9CU3O5HooVokUDlcNxScKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igycjdh4YSELf%2BA%2B9K0q3ANGNtTVA43lSZoUIlithXoLaguNyjzRi75M6L94FXiNjHHZEt9GG7vJ%2B%2BoyWZkZkTSHVyjpPqp2F6wGP52JSS0kksDyWU%2BIeKVX25MOFJmRj2wlcCkJDRrkWGlkC6nh2Qa4wnkwNIqmboGIvyq6BuxLaB3kTt0rmWZCExbTa0K7b5FFNL1kmwi5%2FtSg0VsqO4AJs8mjoQYUC4ImEgxOx%2FsnKwvIFgoNTEiB1JVi9vL2gbyiJDhI7cZyyu6MwGfUFzmNrfpg3R99Jb4qdfwAVTFakwLKKY0Ok7TROlL1p1A2iRx2%2FLFjd50pi%2Fi6ktHkREMQp6XT7c%2B2KCDYg9cX0CPKZjdlRpzuEzOcTG5SMPb%2BFu263DBwR67MdADavEYvAhC2NL1AD%2BG8hvvBNVQXK%2BqGNT7it0CPWReP8xNkw6r1Rs5pfStkl1DrcYjI2tr2tmO9WWGDVjCOK8YO46eF4pZukizgFDfEcwA2L%2BdT0QxRNhrC%2FMdvYvC87XniQKk4ZOFAJvae%2FYnMJMU19F9R1HJ84OU%2FNucMtEf4zOpHV2y18UaI2oUE8MqqC%2Fl9H%2FJbjhxwp5bVCqlrPY6JXfgcFVUJHmx2UF2aWVZcBh4qXZmQPj%2FdHXyY9NLQIEndVTDhu%2Bm8BjqkAaqg67mAM09xq%2F91SroJQm4ff4VXMVEcS72jDtEC2v4tIvVgLOlQC2GFGyi1RQ2vmiCRgkFYML9eGzYDT7yNb0AF0slDkU%2BDADTfxcaRtF4nL4Irt6MINobe3ykNGwvfptApa7eFHbei9EMJSFvjGZubaTsQ%2FzMGp%2BDEBRDari6IaM6%2FGdQPsMOw7UEdcxd4FYedRzT%2BdZ3ppCOxuFzs0Vnifdbh&X-Amz-Signature=519cfbd0b13be276f83b5db77e340a9f71f8809a8ce034bc75ef3433bddf0dbe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US7G67J5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUgOLkPrw9%2FHBC%2Br7F0UkbbHPjcHln%2B9BkCgJSPQOCDgIhANmytvvJ%2FUTGPU8X%2FLa%2FaqKk9CU3O5HooVokUDlcNxScKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igycjdh4YSELf%2BA%2B9K0q3ANGNtTVA43lSZoUIlithXoLaguNyjzRi75M6L94FXiNjHHZEt9GG7vJ%2B%2BoyWZkZkTSHVyjpPqp2F6wGP52JSS0kksDyWU%2BIeKVX25MOFJmRj2wlcCkJDRrkWGlkC6nh2Qa4wnkwNIqmboGIvyq6BuxLaB3kTt0rmWZCExbTa0K7b5FFNL1kmwi5%2FtSg0VsqO4AJs8mjoQYUC4ImEgxOx%2FsnKwvIFgoNTEiB1JVi9vL2gbyiJDhI7cZyyu6MwGfUFzmNrfpg3R99Jb4qdfwAVTFakwLKKY0Ok7TROlL1p1A2iRx2%2FLFjd50pi%2Fi6ktHkREMQp6XT7c%2B2KCDYg9cX0CPKZjdlRpzuEzOcTG5SMPb%2BFu263DBwR67MdADavEYvAhC2NL1AD%2BG8hvvBNVQXK%2BqGNT7it0CPWReP8xNkw6r1Rs5pfStkl1DrcYjI2tr2tmO9WWGDVjCOK8YO46eF4pZukizgFDfEcwA2L%2BdT0QxRNhrC%2FMdvYvC87XniQKk4ZOFAJvae%2FYnMJMU19F9R1HJ84OU%2FNucMtEf4zOpHV2y18UaI2oUE8MqqC%2Fl9H%2FJbjhxwp5bVCqlrPY6JXfgcFVUJHmx2UF2aWVZcBh4qXZmQPj%2FdHXyY9NLQIEndVTDhu%2Bm8BjqkAaqg67mAM09xq%2F91SroJQm4ff4VXMVEcS72jDtEC2v4tIvVgLOlQC2GFGyi1RQ2vmiCRgkFYML9eGzYDT7yNb0AF0slDkU%2BDADTfxcaRtF4nL4Irt6MINobe3ykNGwvfptApa7eFHbei9EMJSFvjGZubaTsQ%2FzMGp%2BDEBRDari6IaM6%2FGdQPsMOw7UEdcxd4FYedRzT%2BdZ3ppCOxuFzs0Vnifdbh&X-Amz-Signature=c6e83286ba121afc04aef617e4117f8f5673e05b0aa7fb02e250ac2d99bd9b68&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US7G67J5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUgOLkPrw9%2FHBC%2Br7F0UkbbHPjcHln%2B9BkCgJSPQOCDgIhANmytvvJ%2FUTGPU8X%2FLa%2FaqKk9CU3O5HooVokUDlcNxScKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igycjdh4YSELf%2BA%2B9K0q3ANGNtTVA43lSZoUIlithXoLaguNyjzRi75M6L94FXiNjHHZEt9GG7vJ%2B%2BoyWZkZkTSHVyjpPqp2F6wGP52JSS0kksDyWU%2BIeKVX25MOFJmRj2wlcCkJDRrkWGlkC6nh2Qa4wnkwNIqmboGIvyq6BuxLaB3kTt0rmWZCExbTa0K7b5FFNL1kmwi5%2FtSg0VsqO4AJs8mjoQYUC4ImEgxOx%2FsnKwvIFgoNTEiB1JVi9vL2gbyiJDhI7cZyyu6MwGfUFzmNrfpg3R99Jb4qdfwAVTFakwLKKY0Ok7TROlL1p1A2iRx2%2FLFjd50pi%2Fi6ktHkREMQp6XT7c%2B2KCDYg9cX0CPKZjdlRpzuEzOcTG5SMPb%2BFu263DBwR67MdADavEYvAhC2NL1AD%2BG8hvvBNVQXK%2BqGNT7it0CPWReP8xNkw6r1Rs5pfStkl1DrcYjI2tr2tmO9WWGDVjCOK8YO46eF4pZukizgFDfEcwA2L%2BdT0QxRNhrC%2FMdvYvC87XniQKk4ZOFAJvae%2FYnMJMU19F9R1HJ84OU%2FNucMtEf4zOpHV2y18UaI2oUE8MqqC%2Fl9H%2FJbjhxwp5bVCqlrPY6JXfgcFVUJHmx2UF2aWVZcBh4qXZmQPj%2FdHXyY9NLQIEndVTDhu%2Bm8BjqkAaqg67mAM09xq%2F91SroJQm4ff4VXMVEcS72jDtEC2v4tIvVgLOlQC2GFGyi1RQ2vmiCRgkFYML9eGzYDT7yNb0AF0slDkU%2BDADTfxcaRtF4nL4Irt6MINobe3ykNGwvfptApa7eFHbei9EMJSFvjGZubaTsQ%2FzMGp%2BDEBRDari6IaM6%2FGdQPsMOw7UEdcxd4FYedRzT%2BdZ3ppCOxuFzs0Vnifdbh&X-Amz-Signature=84e3581995cc805d97d371cab58cf2f8c33f3d847eb2e68b6a481e4699771a07&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US7G67J5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUgOLkPrw9%2FHBC%2Br7F0UkbbHPjcHln%2B9BkCgJSPQOCDgIhANmytvvJ%2FUTGPU8X%2FLa%2FaqKk9CU3O5HooVokUDlcNxScKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igycjdh4YSELf%2BA%2B9K0q3ANGNtTVA43lSZoUIlithXoLaguNyjzRi75M6L94FXiNjHHZEt9GG7vJ%2B%2BoyWZkZkTSHVyjpPqp2F6wGP52JSS0kksDyWU%2BIeKVX25MOFJmRj2wlcCkJDRrkWGlkC6nh2Qa4wnkwNIqmboGIvyq6BuxLaB3kTt0rmWZCExbTa0K7b5FFNL1kmwi5%2FtSg0VsqO4AJs8mjoQYUC4ImEgxOx%2FsnKwvIFgoNTEiB1JVi9vL2gbyiJDhI7cZyyu6MwGfUFzmNrfpg3R99Jb4qdfwAVTFakwLKKY0Ok7TROlL1p1A2iRx2%2FLFjd50pi%2Fi6ktHkREMQp6XT7c%2B2KCDYg9cX0CPKZjdlRpzuEzOcTG5SMPb%2BFu263DBwR67MdADavEYvAhC2NL1AD%2BG8hvvBNVQXK%2BqGNT7it0CPWReP8xNkw6r1Rs5pfStkl1DrcYjI2tr2tmO9WWGDVjCOK8YO46eF4pZukizgFDfEcwA2L%2BdT0QxRNhrC%2FMdvYvC87XniQKk4ZOFAJvae%2FYnMJMU19F9R1HJ84OU%2FNucMtEf4zOpHV2y18UaI2oUE8MqqC%2Fl9H%2FJbjhxwp5bVCqlrPY6JXfgcFVUJHmx2UF2aWVZcBh4qXZmQPj%2FdHXyY9NLQIEndVTDhu%2Bm8BjqkAaqg67mAM09xq%2F91SroJQm4ff4VXMVEcS72jDtEC2v4tIvVgLOlQC2GFGyi1RQ2vmiCRgkFYML9eGzYDT7yNb0AF0slDkU%2BDADTfxcaRtF4nL4Irt6MINobe3ykNGwvfptApa7eFHbei9EMJSFvjGZubaTsQ%2FzMGp%2BDEBRDari6IaM6%2FGdQPsMOw7UEdcxd4FYedRzT%2BdZ3ppCOxuFzs0Vnifdbh&X-Amz-Signature=7b2a9d2a2c4dea3867b8b67481aa5cccee1039310bbebc53b421d58edcda99fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US7G67J5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUgOLkPrw9%2FHBC%2Br7F0UkbbHPjcHln%2B9BkCgJSPQOCDgIhANmytvvJ%2FUTGPU8X%2FLa%2FaqKk9CU3O5HooVokUDlcNxScKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igycjdh4YSELf%2BA%2B9K0q3ANGNtTVA43lSZoUIlithXoLaguNyjzRi75M6L94FXiNjHHZEt9GG7vJ%2B%2BoyWZkZkTSHVyjpPqp2F6wGP52JSS0kksDyWU%2BIeKVX25MOFJmRj2wlcCkJDRrkWGlkC6nh2Qa4wnkwNIqmboGIvyq6BuxLaB3kTt0rmWZCExbTa0K7b5FFNL1kmwi5%2FtSg0VsqO4AJs8mjoQYUC4ImEgxOx%2FsnKwvIFgoNTEiB1JVi9vL2gbyiJDhI7cZyyu6MwGfUFzmNrfpg3R99Jb4qdfwAVTFakwLKKY0Ok7TROlL1p1A2iRx2%2FLFjd50pi%2Fi6ktHkREMQp6XT7c%2B2KCDYg9cX0CPKZjdlRpzuEzOcTG5SMPb%2BFu263DBwR67MdADavEYvAhC2NL1AD%2BG8hvvBNVQXK%2BqGNT7it0CPWReP8xNkw6r1Rs5pfStkl1DrcYjI2tr2tmO9WWGDVjCOK8YO46eF4pZukizgFDfEcwA2L%2BdT0QxRNhrC%2FMdvYvC87XniQKk4ZOFAJvae%2FYnMJMU19F9R1HJ84OU%2FNucMtEf4zOpHV2y18UaI2oUE8MqqC%2Fl9H%2FJbjhxwp5bVCqlrPY6JXfgcFVUJHmx2UF2aWVZcBh4qXZmQPj%2FdHXyY9NLQIEndVTDhu%2Bm8BjqkAaqg67mAM09xq%2F91SroJQm4ff4VXMVEcS72jDtEC2v4tIvVgLOlQC2GFGyi1RQ2vmiCRgkFYML9eGzYDT7yNb0AF0slDkU%2BDADTfxcaRtF4nL4Irt6MINobe3ykNGwvfptApa7eFHbei9EMJSFvjGZubaTsQ%2FzMGp%2BDEBRDari6IaM6%2FGdQPsMOw7UEdcxd4FYedRzT%2BdZ3ppCOxuFzs0Vnifdbh&X-Amz-Signature=d980a145e19776635cdbd174b1e3dc037237536a9a4a8cb74f178cad8b9a8f0a&X-Amz-SignedHeaders=host&x-id=GetObject)
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


