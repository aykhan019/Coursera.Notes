

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS5HMAKJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC8jec6ziwPhPLdEYjU7uvuqLVJG6w9V%2FcjDK5uKImu3AIgO2xpKghwCVmICqPL638D1qSe0QjY%2B%2FyeUBCot5%2BpZ88q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJLZ%2F98OCFppcMHaOSrcA%2FtUlbdORId8Eg%2BE0PnmujvDe2AK03y4wl4tOxDKUmTRKzRNXGLUY9HWmoJNlza%2Bf46NMIrJtOjH%2BDsGBZaceVmys0rE%2BerPoS0DubFDxLDU4axkp4VFSbDN%2FTQlY2akBNB9IwVBUc2y1tW9HEHr6itGEQgA7IVsb5TSYRpOjwVYpricrh%2BFZ0a%2BY3tCvAdsXSoMlNe9xQl286SLw1LXQn5sFOdXB2pXp6rwfLODvZJNYdt908VTYE%2BdroraxR7xW%2BnIhYK08ZGaaGW39OqiHnaLRLW5PaaTaL5UymB25J9j13I3or1ecwfjr7pkkN5xbHT8qZ3GgRfcqgyrW5xuohckG5S54F5rwd9b%2BYG8f9J8uBtGxiUYhArhwtskc5n4YqFXQAmOUzXEdewW9lDh5G3J%2F9JWZjYLc%2B5h78NDned5VsPQSwtQAUpKVJXe57UZ2hJxRmauawSKHGkAuM0YeuWwN%2FnV%2BumUYFEKnKQrcUdzV5BTBBSuvmllKRBE%2FLxULDx73Bbk4cH90ED66ZIRE%2BjpxpM96I%2BvBb0hBPlvXxNcPJ3am8Wmm%2Fl1J0CKAe1Oz6ucpPrh1RlsWnzh8OY6OH7lx%2BbH58NArFh0Qfk9SzWL5mG9Gn%2Fy7sQVnl9uMLPZhL0GOqUBf3Htp9t9nm0aHI7PJr42cqctf%2F8YGfRWfoWFbmqpMZbhf2fF7yepX8S9PnOAUqJOnFW80jQIf5jVx9JFvm3b0qTtwNQUYZ2FOYIxjMGwzF%2B1IIo19NCo21Vl%2F855gvgaW82SG1CWyJr8elMPauCMiTfWd1y4JAOCgaWT8k3xDdLnDXuImtS8Jz2%2Bp5nR3xD3HsdvAbJ%2FhEWgiFBf6ZFYj%2BdHhEp2&X-Amz-Signature=504662a48f98cfb32097f3fc24a83f14edd1aee6e9dba45c679804e167dea5a2&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K4EDQ3O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIG49MsN%2Fv4F3ZLuR07iIubboCOB9YCvHTysaZSEwdlyYAiEA6afuhmfHPDqvBjPdlHo90bahjqNjoaVYnFCNdKjVVrMq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDNyQl5GW3kvuzKN0jSrcA6Yx1yFRlJPCqNFbfoITG1bQi3rmEwknF5h765Tx4pau1XAn3cPEubcBnFHgFSenY6DzJq8HqDsYM2Fgt8J4AgiJLJABvfjpV9j5u5KlFA49n1NrTNP9ZlHyX0bMn1RxacdjW6csuuANCcXySgsK6%2FQM%2FPQU0WAyKJOEmKukc8I%2BEaYDruhItT4%2FPiw%2B1Wh0BmA3w6HcurpuRovekqz%2BW8tTiO%2FkiFeZk%2BVaoAxFyFlbyvd38%2BhrLx%2BUGpTjNfsBF8qMetMol57SLmUnjt2RZFj0r5Uk6M8uqn9kvFqX41I9foeaUq852mSPn87FHB%2B8TcWys4TomdvJWRC%2Bv89uYTIT7CsBLXRXiklceepPgghfXGPK7fXyiyMskl0g0hX4qQoAxPcUCiUFpT2%2FGWcF3n1T87WtmEYoVGI66ZC7Nc1%2BZzFTxjZzF5xHYRlEXKTivvdq7gWUsoN5vMS0gL2Ukt%2FHncvTxhIeaNUg8ZCXn5tH9PbD2AUbyKIjv6jrCO0FXyG4YUKAqdaumq9vccToHu3JGDhAmovJWczS%2FpA5Q7sJ%2FVtb%2B9jgJsaGX7OkMu1yJYVMBL6acNkViR9va%2B7Xx1UagBQRfBXPqusFPbd27dCjzANv3BQjh35DyxFZMP7ZhL0GOqUBXdgMArZAPAvma3T0hs4HUrQjiVHbluawFrVK6lD3g7EqaY9bGw9VLvwVSeS4YgsdR5CltUF78HuqOpf%2FvwQOPkpBKSUrEqX3FR4x7kC0NzrTEzk%2BL9T3Q8Ys61CF5uxOBmjEOOnYwllI8lLpNiE2zfxiUTGloHSzB0NiASab3dNf19Q8D7%2FRE5plZaYLqAUD%2F8y7niFqD995%2FSzLMCkoDGr9ROWH&X-Amz-Signature=394c932b3dbd05e7ef4af683d8f3f3a2e2ff665eaa0c397b213bb69b8231b571&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K4EDQ3O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIG49MsN%2Fv4F3ZLuR07iIubboCOB9YCvHTysaZSEwdlyYAiEA6afuhmfHPDqvBjPdlHo90bahjqNjoaVYnFCNdKjVVrMq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDNyQl5GW3kvuzKN0jSrcA6Yx1yFRlJPCqNFbfoITG1bQi3rmEwknF5h765Tx4pau1XAn3cPEubcBnFHgFSenY6DzJq8HqDsYM2Fgt8J4AgiJLJABvfjpV9j5u5KlFA49n1NrTNP9ZlHyX0bMn1RxacdjW6csuuANCcXySgsK6%2FQM%2FPQU0WAyKJOEmKukc8I%2BEaYDruhItT4%2FPiw%2B1Wh0BmA3w6HcurpuRovekqz%2BW8tTiO%2FkiFeZk%2BVaoAxFyFlbyvd38%2BhrLx%2BUGpTjNfsBF8qMetMol57SLmUnjt2RZFj0r5Uk6M8uqn9kvFqX41I9foeaUq852mSPn87FHB%2B8TcWys4TomdvJWRC%2Bv89uYTIT7CsBLXRXiklceepPgghfXGPK7fXyiyMskl0g0hX4qQoAxPcUCiUFpT2%2FGWcF3n1T87WtmEYoVGI66ZC7Nc1%2BZzFTxjZzF5xHYRlEXKTivvdq7gWUsoN5vMS0gL2Ukt%2FHncvTxhIeaNUg8ZCXn5tH9PbD2AUbyKIjv6jrCO0FXyG4YUKAqdaumq9vccToHu3JGDhAmovJWczS%2FpA5Q7sJ%2FVtb%2B9jgJsaGX7OkMu1yJYVMBL6acNkViR9va%2B7Xx1UagBQRfBXPqusFPbd27dCjzANv3BQjh35DyxFZMP7ZhL0GOqUBXdgMArZAPAvma3T0hs4HUrQjiVHbluawFrVK6lD3g7EqaY9bGw9VLvwVSeS4YgsdR5CltUF78HuqOpf%2FvwQOPkpBKSUrEqX3FR4x7kC0NzrTEzk%2BL9T3Q8Ys61CF5uxOBmjEOOnYwllI8lLpNiE2zfxiUTGloHSzB0NiASab3dNf19Q8D7%2FRE5plZaYLqAUD%2F8y7niFqD995%2FSzLMCkoDGr9ROWH&X-Amz-Signature=b7e42e1e1c5406e343f6f93a43b3a3aaa540d5e66d061f8ba2bcf9e37445d134&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K4EDQ3O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIG49MsN%2Fv4F3ZLuR07iIubboCOB9YCvHTysaZSEwdlyYAiEA6afuhmfHPDqvBjPdlHo90bahjqNjoaVYnFCNdKjVVrMq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDNyQl5GW3kvuzKN0jSrcA6Yx1yFRlJPCqNFbfoITG1bQi3rmEwknF5h765Tx4pau1XAn3cPEubcBnFHgFSenY6DzJq8HqDsYM2Fgt8J4AgiJLJABvfjpV9j5u5KlFA49n1NrTNP9ZlHyX0bMn1RxacdjW6csuuANCcXySgsK6%2FQM%2FPQU0WAyKJOEmKukc8I%2BEaYDruhItT4%2FPiw%2B1Wh0BmA3w6HcurpuRovekqz%2BW8tTiO%2FkiFeZk%2BVaoAxFyFlbyvd38%2BhrLx%2BUGpTjNfsBF8qMetMol57SLmUnjt2RZFj0r5Uk6M8uqn9kvFqX41I9foeaUq852mSPn87FHB%2B8TcWys4TomdvJWRC%2Bv89uYTIT7CsBLXRXiklceepPgghfXGPK7fXyiyMskl0g0hX4qQoAxPcUCiUFpT2%2FGWcF3n1T87WtmEYoVGI66ZC7Nc1%2BZzFTxjZzF5xHYRlEXKTivvdq7gWUsoN5vMS0gL2Ukt%2FHncvTxhIeaNUg8ZCXn5tH9PbD2AUbyKIjv6jrCO0FXyG4YUKAqdaumq9vccToHu3JGDhAmovJWczS%2FpA5Q7sJ%2FVtb%2B9jgJsaGX7OkMu1yJYVMBL6acNkViR9va%2B7Xx1UagBQRfBXPqusFPbd27dCjzANv3BQjh35DyxFZMP7ZhL0GOqUBXdgMArZAPAvma3T0hs4HUrQjiVHbluawFrVK6lD3g7EqaY9bGw9VLvwVSeS4YgsdR5CltUF78HuqOpf%2FvwQOPkpBKSUrEqX3FR4x7kC0NzrTEzk%2BL9T3Q8Ys61CF5uxOBmjEOOnYwllI8lLpNiE2zfxiUTGloHSzB0NiASab3dNf19Q8D7%2FRE5plZaYLqAUD%2F8y7niFqD995%2FSzLMCkoDGr9ROWH&X-Amz-Signature=2ea5334dd1b250acca6fd393d4229f89045ae3d737a3d37b229fab49809bdd5f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K4EDQ3O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIG49MsN%2Fv4F3ZLuR07iIubboCOB9YCvHTysaZSEwdlyYAiEA6afuhmfHPDqvBjPdlHo90bahjqNjoaVYnFCNdKjVVrMq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDNyQl5GW3kvuzKN0jSrcA6Yx1yFRlJPCqNFbfoITG1bQi3rmEwknF5h765Tx4pau1XAn3cPEubcBnFHgFSenY6DzJq8HqDsYM2Fgt8J4AgiJLJABvfjpV9j5u5KlFA49n1NrTNP9ZlHyX0bMn1RxacdjW6csuuANCcXySgsK6%2FQM%2FPQU0WAyKJOEmKukc8I%2BEaYDruhItT4%2FPiw%2B1Wh0BmA3w6HcurpuRovekqz%2BW8tTiO%2FkiFeZk%2BVaoAxFyFlbyvd38%2BhrLx%2BUGpTjNfsBF8qMetMol57SLmUnjt2RZFj0r5Uk6M8uqn9kvFqX41I9foeaUq852mSPn87FHB%2B8TcWys4TomdvJWRC%2Bv89uYTIT7CsBLXRXiklceepPgghfXGPK7fXyiyMskl0g0hX4qQoAxPcUCiUFpT2%2FGWcF3n1T87WtmEYoVGI66ZC7Nc1%2BZzFTxjZzF5xHYRlEXKTivvdq7gWUsoN5vMS0gL2Ukt%2FHncvTxhIeaNUg8ZCXn5tH9PbD2AUbyKIjv6jrCO0FXyG4YUKAqdaumq9vccToHu3JGDhAmovJWczS%2FpA5Q7sJ%2FVtb%2B9jgJsaGX7OkMu1yJYVMBL6acNkViR9va%2B7Xx1UagBQRfBXPqusFPbd27dCjzANv3BQjh35DyxFZMP7ZhL0GOqUBXdgMArZAPAvma3T0hs4HUrQjiVHbluawFrVK6lD3g7EqaY9bGw9VLvwVSeS4YgsdR5CltUF78HuqOpf%2FvwQOPkpBKSUrEqX3FR4x7kC0NzrTEzk%2BL9T3Q8Ys61CF5uxOBmjEOOnYwllI8lLpNiE2zfxiUTGloHSzB0NiASab3dNf19Q8D7%2FRE5plZaYLqAUD%2F8y7niFqD995%2FSzLMCkoDGr9ROWH&X-Amz-Signature=d960522944acbdf4278bba27feb864a2494023259fdbb2d9253800a2e5b9687e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K4EDQ3O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIG49MsN%2Fv4F3ZLuR07iIubboCOB9YCvHTysaZSEwdlyYAiEA6afuhmfHPDqvBjPdlHo90bahjqNjoaVYnFCNdKjVVrMq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDNyQl5GW3kvuzKN0jSrcA6Yx1yFRlJPCqNFbfoITG1bQi3rmEwknF5h765Tx4pau1XAn3cPEubcBnFHgFSenY6DzJq8HqDsYM2Fgt8J4AgiJLJABvfjpV9j5u5KlFA49n1NrTNP9ZlHyX0bMn1RxacdjW6csuuANCcXySgsK6%2FQM%2FPQU0WAyKJOEmKukc8I%2BEaYDruhItT4%2FPiw%2B1Wh0BmA3w6HcurpuRovekqz%2BW8tTiO%2FkiFeZk%2BVaoAxFyFlbyvd38%2BhrLx%2BUGpTjNfsBF8qMetMol57SLmUnjt2RZFj0r5Uk6M8uqn9kvFqX41I9foeaUq852mSPn87FHB%2B8TcWys4TomdvJWRC%2Bv89uYTIT7CsBLXRXiklceepPgghfXGPK7fXyiyMskl0g0hX4qQoAxPcUCiUFpT2%2FGWcF3n1T87WtmEYoVGI66ZC7Nc1%2BZzFTxjZzF5xHYRlEXKTivvdq7gWUsoN5vMS0gL2Ukt%2FHncvTxhIeaNUg8ZCXn5tH9PbD2AUbyKIjv6jrCO0FXyG4YUKAqdaumq9vccToHu3JGDhAmovJWczS%2FpA5Q7sJ%2FVtb%2B9jgJsaGX7OkMu1yJYVMBL6acNkViR9va%2B7Xx1UagBQRfBXPqusFPbd27dCjzANv3BQjh35DyxFZMP7ZhL0GOqUBXdgMArZAPAvma3T0hs4HUrQjiVHbluawFrVK6lD3g7EqaY9bGw9VLvwVSeS4YgsdR5CltUF78HuqOpf%2FvwQOPkpBKSUrEqX3FR4x7kC0NzrTEzk%2BL9T3Q8Ys61CF5uxOBmjEOOnYwllI8lLpNiE2zfxiUTGloHSzB0NiASab3dNf19Q8D7%2FRE5plZaYLqAUD%2F8y7niFqD995%2FSzLMCkoDGr9ROWH&X-Amz-Signature=ea413b074607450c236d7a71a2759ddf3898b5b2ce6546bea96544a10518ad0a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS5HMAKJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC8jec6ziwPhPLdEYjU7uvuqLVJG6w9V%2FcjDK5uKImu3AIgO2xpKghwCVmICqPL638D1qSe0QjY%2B%2FyeUBCot5%2BpZ88q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJLZ%2F98OCFppcMHaOSrcA%2FtUlbdORId8Eg%2BE0PnmujvDe2AK03y4wl4tOxDKUmTRKzRNXGLUY9HWmoJNlza%2Bf46NMIrJtOjH%2BDsGBZaceVmys0rE%2BerPoS0DubFDxLDU4axkp4VFSbDN%2FTQlY2akBNB9IwVBUc2y1tW9HEHr6itGEQgA7IVsb5TSYRpOjwVYpricrh%2BFZ0a%2BY3tCvAdsXSoMlNe9xQl286SLw1LXQn5sFOdXB2pXp6rwfLODvZJNYdt908VTYE%2BdroraxR7xW%2BnIhYK08ZGaaGW39OqiHnaLRLW5PaaTaL5UymB25J9j13I3or1ecwfjr7pkkN5xbHT8qZ3GgRfcqgyrW5xuohckG5S54F5rwd9b%2BYG8f9J8uBtGxiUYhArhwtskc5n4YqFXQAmOUzXEdewW9lDh5G3J%2F9JWZjYLc%2B5h78NDned5VsPQSwtQAUpKVJXe57UZ2hJxRmauawSKHGkAuM0YeuWwN%2FnV%2BumUYFEKnKQrcUdzV5BTBBSuvmllKRBE%2FLxULDx73Bbk4cH90ED66ZIRE%2BjpxpM96I%2BvBb0hBPlvXxNcPJ3am8Wmm%2Fl1J0CKAe1Oz6ucpPrh1RlsWnzh8OY6OH7lx%2BbH58NArFh0Qfk9SzWL5mG9Gn%2Fy7sQVnl9uMLPZhL0GOqUBf3Htp9t9nm0aHI7PJr42cqctf%2F8YGfRWfoWFbmqpMZbhf2fF7yepX8S9PnOAUqJOnFW80jQIf5jVx9JFvm3b0qTtwNQUYZ2FOYIxjMGwzF%2B1IIo19NCo21Vl%2F855gvgaW82SG1CWyJr8elMPauCMiTfWd1y4JAOCgaWT8k3xDdLnDXuImtS8Jz2%2Bp5nR3xD3HsdvAbJ%2FhEWgiFBf6ZFYj%2BdHhEp2&X-Amz-Signature=bff10aa9fb036d717506080eaeb253cf1b6c226f86111315238c3ca12ab1c0ab&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS5HMAKJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC8jec6ziwPhPLdEYjU7uvuqLVJG6w9V%2FcjDK5uKImu3AIgO2xpKghwCVmICqPL638D1qSe0QjY%2B%2FyeUBCot5%2BpZ88q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJLZ%2F98OCFppcMHaOSrcA%2FtUlbdORId8Eg%2BE0PnmujvDe2AK03y4wl4tOxDKUmTRKzRNXGLUY9HWmoJNlza%2Bf46NMIrJtOjH%2BDsGBZaceVmys0rE%2BerPoS0DubFDxLDU4axkp4VFSbDN%2FTQlY2akBNB9IwVBUc2y1tW9HEHr6itGEQgA7IVsb5TSYRpOjwVYpricrh%2BFZ0a%2BY3tCvAdsXSoMlNe9xQl286SLw1LXQn5sFOdXB2pXp6rwfLODvZJNYdt908VTYE%2BdroraxR7xW%2BnIhYK08ZGaaGW39OqiHnaLRLW5PaaTaL5UymB25J9j13I3or1ecwfjr7pkkN5xbHT8qZ3GgRfcqgyrW5xuohckG5S54F5rwd9b%2BYG8f9J8uBtGxiUYhArhwtskc5n4YqFXQAmOUzXEdewW9lDh5G3J%2F9JWZjYLc%2B5h78NDned5VsPQSwtQAUpKVJXe57UZ2hJxRmauawSKHGkAuM0YeuWwN%2FnV%2BumUYFEKnKQrcUdzV5BTBBSuvmllKRBE%2FLxULDx73Bbk4cH90ED66ZIRE%2BjpxpM96I%2BvBb0hBPlvXxNcPJ3am8Wmm%2Fl1J0CKAe1Oz6ucpPrh1RlsWnzh8OY6OH7lx%2BbH58NArFh0Qfk9SzWL5mG9Gn%2Fy7sQVnl9uMLPZhL0GOqUBf3Htp9t9nm0aHI7PJr42cqctf%2F8YGfRWfoWFbmqpMZbhf2fF7yepX8S9PnOAUqJOnFW80jQIf5jVx9JFvm3b0qTtwNQUYZ2FOYIxjMGwzF%2B1IIo19NCo21Vl%2F855gvgaW82SG1CWyJr8elMPauCMiTfWd1y4JAOCgaWT8k3xDdLnDXuImtS8Jz2%2Bp5nR3xD3HsdvAbJ%2FhEWgiFBf6ZFYj%2BdHhEp2&X-Amz-Signature=11fe086fd01ed600b443d19de456cfed5a719bbecca8bf0da4b4b022e39e62d8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS5HMAKJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC8jec6ziwPhPLdEYjU7uvuqLVJG6w9V%2FcjDK5uKImu3AIgO2xpKghwCVmICqPL638D1qSe0QjY%2B%2FyeUBCot5%2BpZ88q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJLZ%2F98OCFppcMHaOSrcA%2FtUlbdORId8Eg%2BE0PnmujvDe2AK03y4wl4tOxDKUmTRKzRNXGLUY9HWmoJNlza%2Bf46NMIrJtOjH%2BDsGBZaceVmys0rE%2BerPoS0DubFDxLDU4axkp4VFSbDN%2FTQlY2akBNB9IwVBUc2y1tW9HEHr6itGEQgA7IVsb5TSYRpOjwVYpricrh%2BFZ0a%2BY3tCvAdsXSoMlNe9xQl286SLw1LXQn5sFOdXB2pXp6rwfLODvZJNYdt908VTYE%2BdroraxR7xW%2BnIhYK08ZGaaGW39OqiHnaLRLW5PaaTaL5UymB25J9j13I3or1ecwfjr7pkkN5xbHT8qZ3GgRfcqgyrW5xuohckG5S54F5rwd9b%2BYG8f9J8uBtGxiUYhArhwtskc5n4YqFXQAmOUzXEdewW9lDh5G3J%2F9JWZjYLc%2B5h78NDned5VsPQSwtQAUpKVJXe57UZ2hJxRmauawSKHGkAuM0YeuWwN%2FnV%2BumUYFEKnKQrcUdzV5BTBBSuvmllKRBE%2FLxULDx73Bbk4cH90ED66ZIRE%2BjpxpM96I%2BvBb0hBPlvXxNcPJ3am8Wmm%2Fl1J0CKAe1Oz6ucpPrh1RlsWnzh8OY6OH7lx%2BbH58NArFh0Qfk9SzWL5mG9Gn%2Fy7sQVnl9uMLPZhL0GOqUBf3Htp9t9nm0aHI7PJr42cqctf%2F8YGfRWfoWFbmqpMZbhf2fF7yepX8S9PnOAUqJOnFW80jQIf5jVx9JFvm3b0qTtwNQUYZ2FOYIxjMGwzF%2B1IIo19NCo21Vl%2F855gvgaW82SG1CWyJr8elMPauCMiTfWd1y4JAOCgaWT8k3xDdLnDXuImtS8Jz2%2Bp5nR3xD3HsdvAbJ%2FhEWgiFBf6ZFYj%2BdHhEp2&X-Amz-Signature=492427c2bb9e8223195ece7527fdd3f505fdf0a358e1a9dd9acdb5018341d515&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS5HMAKJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC8jec6ziwPhPLdEYjU7uvuqLVJG6w9V%2FcjDK5uKImu3AIgO2xpKghwCVmICqPL638D1qSe0QjY%2B%2FyeUBCot5%2BpZ88q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJLZ%2F98OCFppcMHaOSrcA%2FtUlbdORId8Eg%2BE0PnmujvDe2AK03y4wl4tOxDKUmTRKzRNXGLUY9HWmoJNlza%2Bf46NMIrJtOjH%2BDsGBZaceVmys0rE%2BerPoS0DubFDxLDU4axkp4VFSbDN%2FTQlY2akBNB9IwVBUc2y1tW9HEHr6itGEQgA7IVsb5TSYRpOjwVYpricrh%2BFZ0a%2BY3tCvAdsXSoMlNe9xQl286SLw1LXQn5sFOdXB2pXp6rwfLODvZJNYdt908VTYE%2BdroraxR7xW%2BnIhYK08ZGaaGW39OqiHnaLRLW5PaaTaL5UymB25J9j13I3or1ecwfjr7pkkN5xbHT8qZ3GgRfcqgyrW5xuohckG5S54F5rwd9b%2BYG8f9J8uBtGxiUYhArhwtskc5n4YqFXQAmOUzXEdewW9lDh5G3J%2F9JWZjYLc%2B5h78NDned5VsPQSwtQAUpKVJXe57UZ2hJxRmauawSKHGkAuM0YeuWwN%2FnV%2BumUYFEKnKQrcUdzV5BTBBSuvmllKRBE%2FLxULDx73Bbk4cH90ED66ZIRE%2BjpxpM96I%2BvBb0hBPlvXxNcPJ3am8Wmm%2Fl1J0CKAe1Oz6ucpPrh1RlsWnzh8OY6OH7lx%2BbH58NArFh0Qfk9SzWL5mG9Gn%2Fy7sQVnl9uMLPZhL0GOqUBf3Htp9t9nm0aHI7PJr42cqctf%2F8YGfRWfoWFbmqpMZbhf2fF7yepX8S9PnOAUqJOnFW80jQIf5jVx9JFvm3b0qTtwNQUYZ2FOYIxjMGwzF%2B1IIo19NCo21Vl%2F855gvgaW82SG1CWyJr8elMPauCMiTfWd1y4JAOCgaWT8k3xDdLnDXuImtS8Jz2%2Bp5nR3xD3HsdvAbJ%2FhEWgiFBf6ZFYj%2BdHhEp2&X-Amz-Signature=a32c2366f424ea7da337559bead69dd29d5f8fccedd70848e6d4d73c3b339f3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS5HMAKJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQC8jec6ziwPhPLdEYjU7uvuqLVJG6w9V%2FcjDK5uKImu3AIgO2xpKghwCVmICqPL638D1qSe0QjY%2B%2FyeUBCot5%2BpZ88q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJLZ%2F98OCFppcMHaOSrcA%2FtUlbdORId8Eg%2BE0PnmujvDe2AK03y4wl4tOxDKUmTRKzRNXGLUY9HWmoJNlza%2Bf46NMIrJtOjH%2BDsGBZaceVmys0rE%2BerPoS0DubFDxLDU4axkp4VFSbDN%2FTQlY2akBNB9IwVBUc2y1tW9HEHr6itGEQgA7IVsb5TSYRpOjwVYpricrh%2BFZ0a%2BY3tCvAdsXSoMlNe9xQl286SLw1LXQn5sFOdXB2pXp6rwfLODvZJNYdt908VTYE%2BdroraxR7xW%2BnIhYK08ZGaaGW39OqiHnaLRLW5PaaTaL5UymB25J9j13I3or1ecwfjr7pkkN5xbHT8qZ3GgRfcqgyrW5xuohckG5S54F5rwd9b%2BYG8f9J8uBtGxiUYhArhwtskc5n4YqFXQAmOUzXEdewW9lDh5G3J%2F9JWZjYLc%2B5h78NDned5VsPQSwtQAUpKVJXe57UZ2hJxRmauawSKHGkAuM0YeuWwN%2FnV%2BumUYFEKnKQrcUdzV5BTBBSuvmllKRBE%2FLxULDx73Bbk4cH90ED66ZIRE%2BjpxpM96I%2BvBb0hBPlvXxNcPJ3am8Wmm%2Fl1J0CKAe1Oz6ucpPrh1RlsWnzh8OY6OH7lx%2BbH58NArFh0Qfk9SzWL5mG9Gn%2Fy7sQVnl9uMLPZhL0GOqUBf3Htp9t9nm0aHI7PJr42cqctf%2F8YGfRWfoWFbmqpMZbhf2fF7yepX8S9PnOAUqJOnFW80jQIf5jVx9JFvm3b0qTtwNQUYZ2FOYIxjMGwzF%2B1IIo19NCo21Vl%2F855gvgaW82SG1CWyJr8elMPauCMiTfWd1y4JAOCgaWT8k3xDdLnDXuImtS8Jz2%2Bp5nR3xD3HsdvAbJ%2FhEWgiFBf6ZFYj%2BdHhEp2&X-Amz-Signature=15161d02a419a25547c293d7e6c300d236310ce7dfa31bb12d6893ce76ab9995&X-Amz-SignedHeaders=host&x-id=GetObject)
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


