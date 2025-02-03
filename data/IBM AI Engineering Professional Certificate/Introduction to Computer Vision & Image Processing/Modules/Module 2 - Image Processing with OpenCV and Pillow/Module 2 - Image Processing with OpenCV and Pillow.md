

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DBC4IGU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBMXk6lKglFO2aUscsbhkOzkIYYmso2rja3lLbh6GA59AiEAj09DDhpk8zpA4njkNygU321Lty11QDAevtAvBt2K9WgqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA2iM3RvNjIlc01fvSrcAw56UBrcZFreIr8DRRsej5mfuqU5fkOlpBPfbHNuTP0gC%2FrZHQUdzIer%2FLYCnB3lOhqFoCbOpnq8u4FjMWSrbI6zi%2BsYjYZF3UxRV0CfxJirDKVYpPazFm4AlC0Kg%2BUtvGL4Kp1Tk8UK5AcnAePrhFtk04no%2BU%2Bj9NTZhOGCwOpQQXIXS7cnTO3DTZ0toT78caRhOhdDCV4oF%2FCESxZBnhKBK9EsOnpMYFAvAKyY90u6O9Cgx9dpZXc7WAwsiLwKaSUjnJVwt74LxFZZehkpMEIWj7r5CpCLgCDnGDoNFrxiULlYT5TDh%2BOJDqINZZFm1xHzAP%2BQNInGwlTwsbjapf%2Buuw8t5QsVhpsaczRS19IbK%2B7cPR7Z%2BYbfV9eadJqzNOLFPoDWO%2B1XEsAK6SCzCxoQSqmbQmyAWHI4%2F2VlZo6WL0mJVVjdpXjMFrpRXWcKrVf5oRNNx4AZglnpjvlDBkXm4cl5QztIsVhBSxmgt94zKbqRDcK653jJ0PS3chwYCAe6MZ6l7G0uWzIER0m1XvqUyw85A7iiYMUcxSGYjdkyPMZW7NDx%2BUH7nA9T2KEk%2FvNBgg6f3nvsoUQ79YHW6honK3vSP%2F1JPXJEBYNFYfkfWhFFSL06HloT5vFWMNi%2FgL0GOqUBL%2BwjqmPyboFrUNvcyCGCvHSLDoUcmqtDujJlB8kS4X7Re8xsTw%2BtnJjCKxcqc4eJDXHnpxpzkldYEX4tnLwDda2XLGQ4N0mewRQJTeIIHuWFENAOSc7G41%2FOWKIqeo9SJgIGsNMnrvvUIBPXet0%2BJ2AS13%2FqfchiVHFHP269TLmdlxSBnPOkRGBdTKuAgw5tdcEl9A7buS%2B2YTrhbKccAj4kSeiG&X-Amz-Signature=87d701be07c6b28470be2014e8129769876b6a25a8d1f292ca8891407aacffaf&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYRQ2RIV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrgYkG5bD16l0Fz1mNn48%2BKduWEmHlfTUZccQZhcgslwIhAP8tjaP6zJLyuelKrmpfgpmECVbroOB1qHin7nE15R84KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz63CHOmYZ%2BN0l1SPQq3AO9M%2Fto%2BgSvWkPPcnsvB5Eao9eF0EeNHb51APGflBfwL4KWt2ehL%2Bg8PXmdmoJyXZawpzmH292GlXPdODBjpmbcDjKDOuGoUfd2L421%2FM0v5ppwTiAAzm6dCeRO%2BdHd7KDzXzTEfWkI9momSf8OLr2tdvoCG1UMCD8%2BpSx6l1N%2Bl010clRTWs0YnsW5SiQkuFKJW7wLn%2BXfbuFCdzaWXRjct6tVc9syUlQzHrMO5xZrmIB438CMMBPt8U52mTVBi6TVsiqomhHTVyJ4QsTzvPR3jtIdPMA0G50klC1qaKxpUfJoGi7%2BfW4C52bowM0me6peTxOg2m1i6BdvViL2uOTuVxpfDXK8FOuXwngRMpxD3kZrHEuDE0GcdXcgRaWmCqeDcnIZk8ywCRSifqe%2B%2B0%2Fusjh8W1t6qnJ9fufTxD%2FFcq4bjiyNopyLHWHNcjqzpqC6hGw3WfXuPIGoJkiMTrxjDKAA2pmbH1DXMuy0%2FD4J7reIPVCHba78IAIorS5D5Zg7jOCgqsaGxSHXM6PjTaqfW8wNQm6irgy8hbyfZEc7%2FWwvyxzMdR%2BV3K2NDywdIC9x2NjgvRBPfLatiJ4FteZTvX0aw9k7dc3a%2FiX6myPVqtBCyefJtFinFPEFMjDxv4C9BjqkASkO2oeONxypqWftoeFDY8hZlzknCGVt6XDGsp5MMc%2BNwTurkYwoJY51BtQB6l3ayUOwaJ9ksKLt53qQe2CtiiFC4b9oHPN8QTpqzen0qH6FtP8QceD%2ByOeJWa5o3KNXCDHO85fsGlxs8tiijxl2e4konEybEEAkc%2B68%2FlGPM%2B%2B5Ri4bCYiTpkhT8vE1CVAVNH1bJolyfbJ8R%2BvLo%2FuqjRTUP9dO&X-Amz-Signature=fe6f68e43b6bd0579c8e00af0356ff2b70b0fd99b6d64b16dbe2afa20698bb09&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYRQ2RIV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrgYkG5bD16l0Fz1mNn48%2BKduWEmHlfTUZccQZhcgslwIhAP8tjaP6zJLyuelKrmpfgpmECVbroOB1qHin7nE15R84KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz63CHOmYZ%2BN0l1SPQq3AO9M%2Fto%2BgSvWkPPcnsvB5Eao9eF0EeNHb51APGflBfwL4KWt2ehL%2Bg8PXmdmoJyXZawpzmH292GlXPdODBjpmbcDjKDOuGoUfd2L421%2FM0v5ppwTiAAzm6dCeRO%2BdHd7KDzXzTEfWkI9momSf8OLr2tdvoCG1UMCD8%2BpSx6l1N%2Bl010clRTWs0YnsW5SiQkuFKJW7wLn%2BXfbuFCdzaWXRjct6tVc9syUlQzHrMO5xZrmIB438CMMBPt8U52mTVBi6TVsiqomhHTVyJ4QsTzvPR3jtIdPMA0G50klC1qaKxpUfJoGi7%2BfW4C52bowM0me6peTxOg2m1i6BdvViL2uOTuVxpfDXK8FOuXwngRMpxD3kZrHEuDE0GcdXcgRaWmCqeDcnIZk8ywCRSifqe%2B%2B0%2Fusjh8W1t6qnJ9fufTxD%2FFcq4bjiyNopyLHWHNcjqzpqC6hGw3WfXuPIGoJkiMTrxjDKAA2pmbH1DXMuy0%2FD4J7reIPVCHba78IAIorS5D5Zg7jOCgqsaGxSHXM6PjTaqfW8wNQm6irgy8hbyfZEc7%2FWwvyxzMdR%2BV3K2NDywdIC9x2NjgvRBPfLatiJ4FteZTvX0aw9k7dc3a%2FiX6myPVqtBCyefJtFinFPEFMjDxv4C9BjqkASkO2oeONxypqWftoeFDY8hZlzknCGVt6XDGsp5MMc%2BNwTurkYwoJY51BtQB6l3ayUOwaJ9ksKLt53qQe2CtiiFC4b9oHPN8QTpqzen0qH6FtP8QceD%2ByOeJWa5o3KNXCDHO85fsGlxs8tiijxl2e4konEybEEAkc%2B68%2FlGPM%2B%2B5Ri4bCYiTpkhT8vE1CVAVNH1bJolyfbJ8R%2BvLo%2FuqjRTUP9dO&X-Amz-Signature=deeaf3c9e857519543a7914ecf7a103e79aee4707bff52dcf93af9350818b08e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYRQ2RIV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrgYkG5bD16l0Fz1mNn48%2BKduWEmHlfTUZccQZhcgslwIhAP8tjaP6zJLyuelKrmpfgpmECVbroOB1qHin7nE15R84KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz63CHOmYZ%2BN0l1SPQq3AO9M%2Fto%2BgSvWkPPcnsvB5Eao9eF0EeNHb51APGflBfwL4KWt2ehL%2Bg8PXmdmoJyXZawpzmH292GlXPdODBjpmbcDjKDOuGoUfd2L421%2FM0v5ppwTiAAzm6dCeRO%2BdHd7KDzXzTEfWkI9momSf8OLr2tdvoCG1UMCD8%2BpSx6l1N%2Bl010clRTWs0YnsW5SiQkuFKJW7wLn%2BXfbuFCdzaWXRjct6tVc9syUlQzHrMO5xZrmIB438CMMBPt8U52mTVBi6TVsiqomhHTVyJ4QsTzvPR3jtIdPMA0G50klC1qaKxpUfJoGi7%2BfW4C52bowM0me6peTxOg2m1i6BdvViL2uOTuVxpfDXK8FOuXwngRMpxD3kZrHEuDE0GcdXcgRaWmCqeDcnIZk8ywCRSifqe%2B%2B0%2Fusjh8W1t6qnJ9fufTxD%2FFcq4bjiyNopyLHWHNcjqzpqC6hGw3WfXuPIGoJkiMTrxjDKAA2pmbH1DXMuy0%2FD4J7reIPVCHba78IAIorS5D5Zg7jOCgqsaGxSHXM6PjTaqfW8wNQm6irgy8hbyfZEc7%2FWwvyxzMdR%2BV3K2NDywdIC9x2NjgvRBPfLatiJ4FteZTvX0aw9k7dc3a%2FiX6myPVqtBCyefJtFinFPEFMjDxv4C9BjqkASkO2oeONxypqWftoeFDY8hZlzknCGVt6XDGsp5MMc%2BNwTurkYwoJY51BtQB6l3ayUOwaJ9ksKLt53qQe2CtiiFC4b9oHPN8QTpqzen0qH6FtP8QceD%2ByOeJWa5o3KNXCDHO85fsGlxs8tiijxl2e4konEybEEAkc%2B68%2FlGPM%2B%2B5Ri4bCYiTpkhT8vE1CVAVNH1bJolyfbJ8R%2BvLo%2FuqjRTUP9dO&X-Amz-Signature=1d81acfbd2fbd8c7ea7d41bb19149cab90496fd7f426c0995e38da0e54cb1d98&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYRQ2RIV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrgYkG5bD16l0Fz1mNn48%2BKduWEmHlfTUZccQZhcgslwIhAP8tjaP6zJLyuelKrmpfgpmECVbroOB1qHin7nE15R84KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz63CHOmYZ%2BN0l1SPQq3AO9M%2Fto%2BgSvWkPPcnsvB5Eao9eF0EeNHb51APGflBfwL4KWt2ehL%2Bg8PXmdmoJyXZawpzmH292GlXPdODBjpmbcDjKDOuGoUfd2L421%2FM0v5ppwTiAAzm6dCeRO%2BdHd7KDzXzTEfWkI9momSf8OLr2tdvoCG1UMCD8%2BpSx6l1N%2Bl010clRTWs0YnsW5SiQkuFKJW7wLn%2BXfbuFCdzaWXRjct6tVc9syUlQzHrMO5xZrmIB438CMMBPt8U52mTVBi6TVsiqomhHTVyJ4QsTzvPR3jtIdPMA0G50klC1qaKxpUfJoGi7%2BfW4C52bowM0me6peTxOg2m1i6BdvViL2uOTuVxpfDXK8FOuXwngRMpxD3kZrHEuDE0GcdXcgRaWmCqeDcnIZk8ywCRSifqe%2B%2B0%2Fusjh8W1t6qnJ9fufTxD%2FFcq4bjiyNopyLHWHNcjqzpqC6hGw3WfXuPIGoJkiMTrxjDKAA2pmbH1DXMuy0%2FD4J7reIPVCHba78IAIorS5D5Zg7jOCgqsaGxSHXM6PjTaqfW8wNQm6irgy8hbyfZEc7%2FWwvyxzMdR%2BV3K2NDywdIC9x2NjgvRBPfLatiJ4FteZTvX0aw9k7dc3a%2FiX6myPVqtBCyefJtFinFPEFMjDxv4C9BjqkASkO2oeONxypqWftoeFDY8hZlzknCGVt6XDGsp5MMc%2BNwTurkYwoJY51BtQB6l3ayUOwaJ9ksKLt53qQe2CtiiFC4b9oHPN8QTpqzen0qH6FtP8QceD%2ByOeJWa5o3KNXCDHO85fsGlxs8tiijxl2e4konEybEEAkc%2B68%2FlGPM%2B%2B5Ri4bCYiTpkhT8vE1CVAVNH1bJolyfbJ8R%2BvLo%2FuqjRTUP9dO&X-Amz-Signature=e7584c77d9cb04c4a501304b67fe31dbeddea5bd8380bc9346cb301cf109b488&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYRQ2RIV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrgYkG5bD16l0Fz1mNn48%2BKduWEmHlfTUZccQZhcgslwIhAP8tjaP6zJLyuelKrmpfgpmECVbroOB1qHin7nE15R84KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz63CHOmYZ%2BN0l1SPQq3AO9M%2Fto%2BgSvWkPPcnsvB5Eao9eF0EeNHb51APGflBfwL4KWt2ehL%2Bg8PXmdmoJyXZawpzmH292GlXPdODBjpmbcDjKDOuGoUfd2L421%2FM0v5ppwTiAAzm6dCeRO%2BdHd7KDzXzTEfWkI9momSf8OLr2tdvoCG1UMCD8%2BpSx6l1N%2Bl010clRTWs0YnsW5SiQkuFKJW7wLn%2BXfbuFCdzaWXRjct6tVc9syUlQzHrMO5xZrmIB438CMMBPt8U52mTVBi6TVsiqomhHTVyJ4QsTzvPR3jtIdPMA0G50klC1qaKxpUfJoGi7%2BfW4C52bowM0me6peTxOg2m1i6BdvViL2uOTuVxpfDXK8FOuXwngRMpxD3kZrHEuDE0GcdXcgRaWmCqeDcnIZk8ywCRSifqe%2B%2B0%2Fusjh8W1t6qnJ9fufTxD%2FFcq4bjiyNopyLHWHNcjqzpqC6hGw3WfXuPIGoJkiMTrxjDKAA2pmbH1DXMuy0%2FD4J7reIPVCHba78IAIorS5D5Zg7jOCgqsaGxSHXM6PjTaqfW8wNQm6irgy8hbyfZEc7%2FWwvyxzMdR%2BV3K2NDywdIC9x2NjgvRBPfLatiJ4FteZTvX0aw9k7dc3a%2FiX6myPVqtBCyefJtFinFPEFMjDxv4C9BjqkASkO2oeONxypqWftoeFDY8hZlzknCGVt6XDGsp5MMc%2BNwTurkYwoJY51BtQB6l3ayUOwaJ9ksKLt53qQe2CtiiFC4b9oHPN8QTpqzen0qH6FtP8QceD%2ByOeJWa5o3KNXCDHO85fsGlxs8tiijxl2e4konEybEEAkc%2B68%2FlGPM%2B%2B5Ri4bCYiTpkhT8vE1CVAVNH1bJolyfbJ8R%2BvLo%2FuqjRTUP9dO&X-Amz-Signature=458c20a8d0cd24bc97fba0b3cd53bf650e3c1ccb43c15a1a5b3cfe8209fcf8b1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DBC4IGU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBMXk6lKglFO2aUscsbhkOzkIYYmso2rja3lLbh6GA59AiEAj09DDhpk8zpA4njkNygU321Lty11QDAevtAvBt2K9WgqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA2iM3RvNjIlc01fvSrcAw56UBrcZFreIr8DRRsej5mfuqU5fkOlpBPfbHNuTP0gC%2FrZHQUdzIer%2FLYCnB3lOhqFoCbOpnq8u4FjMWSrbI6zi%2BsYjYZF3UxRV0CfxJirDKVYpPazFm4AlC0Kg%2BUtvGL4Kp1Tk8UK5AcnAePrhFtk04no%2BU%2Bj9NTZhOGCwOpQQXIXS7cnTO3DTZ0toT78caRhOhdDCV4oF%2FCESxZBnhKBK9EsOnpMYFAvAKyY90u6O9Cgx9dpZXc7WAwsiLwKaSUjnJVwt74LxFZZehkpMEIWj7r5CpCLgCDnGDoNFrxiULlYT5TDh%2BOJDqINZZFm1xHzAP%2BQNInGwlTwsbjapf%2Buuw8t5QsVhpsaczRS19IbK%2B7cPR7Z%2BYbfV9eadJqzNOLFPoDWO%2B1XEsAK6SCzCxoQSqmbQmyAWHI4%2F2VlZo6WL0mJVVjdpXjMFrpRXWcKrVf5oRNNx4AZglnpjvlDBkXm4cl5QztIsVhBSxmgt94zKbqRDcK653jJ0PS3chwYCAe6MZ6l7G0uWzIER0m1XvqUyw85A7iiYMUcxSGYjdkyPMZW7NDx%2BUH7nA9T2KEk%2FvNBgg6f3nvsoUQ79YHW6honK3vSP%2F1JPXJEBYNFYfkfWhFFSL06HloT5vFWMNi%2FgL0GOqUBL%2BwjqmPyboFrUNvcyCGCvHSLDoUcmqtDujJlB8kS4X7Re8xsTw%2BtnJjCKxcqc4eJDXHnpxpzkldYEX4tnLwDda2XLGQ4N0mewRQJTeIIHuWFENAOSc7G41%2FOWKIqeo9SJgIGsNMnrvvUIBPXet0%2BJ2AS13%2FqfchiVHFHP269TLmdlxSBnPOkRGBdTKuAgw5tdcEl9A7buS%2B2YTrhbKccAj4kSeiG&X-Amz-Signature=dfd5b0e27c88c8106656586b41df25d17d46e2d966fce8f634e28e500da12980&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DBC4IGU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBMXk6lKglFO2aUscsbhkOzkIYYmso2rja3lLbh6GA59AiEAj09DDhpk8zpA4njkNygU321Lty11QDAevtAvBt2K9WgqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA2iM3RvNjIlc01fvSrcAw56UBrcZFreIr8DRRsej5mfuqU5fkOlpBPfbHNuTP0gC%2FrZHQUdzIer%2FLYCnB3lOhqFoCbOpnq8u4FjMWSrbI6zi%2BsYjYZF3UxRV0CfxJirDKVYpPazFm4AlC0Kg%2BUtvGL4Kp1Tk8UK5AcnAePrhFtk04no%2BU%2Bj9NTZhOGCwOpQQXIXS7cnTO3DTZ0toT78caRhOhdDCV4oF%2FCESxZBnhKBK9EsOnpMYFAvAKyY90u6O9Cgx9dpZXc7WAwsiLwKaSUjnJVwt74LxFZZehkpMEIWj7r5CpCLgCDnGDoNFrxiULlYT5TDh%2BOJDqINZZFm1xHzAP%2BQNInGwlTwsbjapf%2Buuw8t5QsVhpsaczRS19IbK%2B7cPR7Z%2BYbfV9eadJqzNOLFPoDWO%2B1XEsAK6SCzCxoQSqmbQmyAWHI4%2F2VlZo6WL0mJVVjdpXjMFrpRXWcKrVf5oRNNx4AZglnpjvlDBkXm4cl5QztIsVhBSxmgt94zKbqRDcK653jJ0PS3chwYCAe6MZ6l7G0uWzIER0m1XvqUyw85A7iiYMUcxSGYjdkyPMZW7NDx%2BUH7nA9T2KEk%2FvNBgg6f3nvsoUQ79YHW6honK3vSP%2F1JPXJEBYNFYfkfWhFFSL06HloT5vFWMNi%2FgL0GOqUBL%2BwjqmPyboFrUNvcyCGCvHSLDoUcmqtDujJlB8kS4X7Re8xsTw%2BtnJjCKxcqc4eJDXHnpxpzkldYEX4tnLwDda2XLGQ4N0mewRQJTeIIHuWFENAOSc7G41%2FOWKIqeo9SJgIGsNMnrvvUIBPXet0%2BJ2AS13%2FqfchiVHFHP269TLmdlxSBnPOkRGBdTKuAgw5tdcEl9A7buS%2B2YTrhbKccAj4kSeiG&X-Amz-Signature=f54bad5850ef390645680663362e880a9c54fbefc1e37754c52c1e66af4127d8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DBC4IGU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBMXk6lKglFO2aUscsbhkOzkIYYmso2rja3lLbh6GA59AiEAj09DDhpk8zpA4njkNygU321Lty11QDAevtAvBt2K9WgqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA2iM3RvNjIlc01fvSrcAw56UBrcZFreIr8DRRsej5mfuqU5fkOlpBPfbHNuTP0gC%2FrZHQUdzIer%2FLYCnB3lOhqFoCbOpnq8u4FjMWSrbI6zi%2BsYjYZF3UxRV0CfxJirDKVYpPazFm4AlC0Kg%2BUtvGL4Kp1Tk8UK5AcnAePrhFtk04no%2BU%2Bj9NTZhOGCwOpQQXIXS7cnTO3DTZ0toT78caRhOhdDCV4oF%2FCESxZBnhKBK9EsOnpMYFAvAKyY90u6O9Cgx9dpZXc7WAwsiLwKaSUjnJVwt74LxFZZehkpMEIWj7r5CpCLgCDnGDoNFrxiULlYT5TDh%2BOJDqINZZFm1xHzAP%2BQNInGwlTwsbjapf%2Buuw8t5QsVhpsaczRS19IbK%2B7cPR7Z%2BYbfV9eadJqzNOLFPoDWO%2B1XEsAK6SCzCxoQSqmbQmyAWHI4%2F2VlZo6WL0mJVVjdpXjMFrpRXWcKrVf5oRNNx4AZglnpjvlDBkXm4cl5QztIsVhBSxmgt94zKbqRDcK653jJ0PS3chwYCAe6MZ6l7G0uWzIER0m1XvqUyw85A7iiYMUcxSGYjdkyPMZW7NDx%2BUH7nA9T2KEk%2FvNBgg6f3nvsoUQ79YHW6honK3vSP%2F1JPXJEBYNFYfkfWhFFSL06HloT5vFWMNi%2FgL0GOqUBL%2BwjqmPyboFrUNvcyCGCvHSLDoUcmqtDujJlB8kS4X7Re8xsTw%2BtnJjCKxcqc4eJDXHnpxpzkldYEX4tnLwDda2XLGQ4N0mewRQJTeIIHuWFENAOSc7G41%2FOWKIqeo9SJgIGsNMnrvvUIBPXet0%2BJ2AS13%2FqfchiVHFHP269TLmdlxSBnPOkRGBdTKuAgw5tdcEl9A7buS%2B2YTrhbKccAj4kSeiG&X-Amz-Signature=5e932dd17ffc9e253efa0a93ef28f59b47bd31626d14ec1af6210c2ad8cc5f9f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DBC4IGU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBMXk6lKglFO2aUscsbhkOzkIYYmso2rja3lLbh6GA59AiEAj09DDhpk8zpA4njkNygU321Lty11QDAevtAvBt2K9WgqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA2iM3RvNjIlc01fvSrcAw56UBrcZFreIr8DRRsej5mfuqU5fkOlpBPfbHNuTP0gC%2FrZHQUdzIer%2FLYCnB3lOhqFoCbOpnq8u4FjMWSrbI6zi%2BsYjYZF3UxRV0CfxJirDKVYpPazFm4AlC0Kg%2BUtvGL4Kp1Tk8UK5AcnAePrhFtk04no%2BU%2Bj9NTZhOGCwOpQQXIXS7cnTO3DTZ0toT78caRhOhdDCV4oF%2FCESxZBnhKBK9EsOnpMYFAvAKyY90u6O9Cgx9dpZXc7WAwsiLwKaSUjnJVwt74LxFZZehkpMEIWj7r5CpCLgCDnGDoNFrxiULlYT5TDh%2BOJDqINZZFm1xHzAP%2BQNInGwlTwsbjapf%2Buuw8t5QsVhpsaczRS19IbK%2B7cPR7Z%2BYbfV9eadJqzNOLFPoDWO%2B1XEsAK6SCzCxoQSqmbQmyAWHI4%2F2VlZo6WL0mJVVjdpXjMFrpRXWcKrVf5oRNNx4AZglnpjvlDBkXm4cl5QztIsVhBSxmgt94zKbqRDcK653jJ0PS3chwYCAe6MZ6l7G0uWzIER0m1XvqUyw85A7iiYMUcxSGYjdkyPMZW7NDx%2BUH7nA9T2KEk%2FvNBgg6f3nvsoUQ79YHW6honK3vSP%2F1JPXJEBYNFYfkfWhFFSL06HloT5vFWMNi%2FgL0GOqUBL%2BwjqmPyboFrUNvcyCGCvHSLDoUcmqtDujJlB8kS4X7Re8xsTw%2BtnJjCKxcqc4eJDXHnpxpzkldYEX4tnLwDda2XLGQ4N0mewRQJTeIIHuWFENAOSc7G41%2FOWKIqeo9SJgIGsNMnrvvUIBPXet0%2BJ2AS13%2FqfchiVHFHP269TLmdlxSBnPOkRGBdTKuAgw5tdcEl9A7buS%2B2YTrhbKccAj4kSeiG&X-Amz-Signature=266c40de8f9c8adc58c4bd4597c20402a539953be391ac0b00cd01c43096fe7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DBC4IGU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBMXk6lKglFO2aUscsbhkOzkIYYmso2rja3lLbh6GA59AiEAj09DDhpk8zpA4njkNygU321Lty11QDAevtAvBt2K9WgqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA2iM3RvNjIlc01fvSrcAw56UBrcZFreIr8DRRsej5mfuqU5fkOlpBPfbHNuTP0gC%2FrZHQUdzIer%2FLYCnB3lOhqFoCbOpnq8u4FjMWSrbI6zi%2BsYjYZF3UxRV0CfxJirDKVYpPazFm4AlC0Kg%2BUtvGL4Kp1Tk8UK5AcnAePrhFtk04no%2BU%2Bj9NTZhOGCwOpQQXIXS7cnTO3DTZ0toT78caRhOhdDCV4oF%2FCESxZBnhKBK9EsOnpMYFAvAKyY90u6O9Cgx9dpZXc7WAwsiLwKaSUjnJVwt74LxFZZehkpMEIWj7r5CpCLgCDnGDoNFrxiULlYT5TDh%2BOJDqINZZFm1xHzAP%2BQNInGwlTwsbjapf%2Buuw8t5QsVhpsaczRS19IbK%2B7cPR7Z%2BYbfV9eadJqzNOLFPoDWO%2B1XEsAK6SCzCxoQSqmbQmyAWHI4%2F2VlZo6WL0mJVVjdpXjMFrpRXWcKrVf5oRNNx4AZglnpjvlDBkXm4cl5QztIsVhBSxmgt94zKbqRDcK653jJ0PS3chwYCAe6MZ6l7G0uWzIER0m1XvqUyw85A7iiYMUcxSGYjdkyPMZW7NDx%2BUH7nA9T2KEk%2FvNBgg6f3nvsoUQ79YHW6honK3vSP%2F1JPXJEBYNFYfkfWhFFSL06HloT5vFWMNi%2FgL0GOqUBL%2BwjqmPyboFrUNvcyCGCvHSLDoUcmqtDujJlB8kS4X7Re8xsTw%2BtnJjCKxcqc4eJDXHnpxpzkldYEX4tnLwDda2XLGQ4N0mewRQJTeIIHuWFENAOSc7G41%2FOWKIqeo9SJgIGsNMnrvvUIBPXet0%2BJ2AS13%2FqfchiVHFHP269TLmdlxSBnPOkRGBdTKuAgw5tdcEl9A7buS%2B2YTrhbKccAj4kSeiG&X-Amz-Signature=a1f46ea4e92d12d30210f9f07e3af9a375eaf80f5853c126abf432496389b08c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


