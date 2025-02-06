

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRR4AONB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAkf%2Fcgc8mq6XFq465X8pzxXZOd8Ce7UMlfiGoBjVDZmAiEA7muWzwHhwRB3VQdxlTzywzDePwIupRGO9QRxe1V2dM4q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDFVPRhGQkWgi2jdUVircA1LJVQVnbdHnLQEiInDJeXdfDbyzL9271rwUPhokngzF8UUnT0jZw779vB5r4ifdOvMPq1mC2PBEWVDHaqBKx30VpcXbmtnU%2FjiCTKHQ5MinU%2FvFhGrATR8rIOzYfrVI3jJo76IateVOt%2FPHK07guvrvI1NOEQFYGK6KRpxO72Cuag0i7dtkXFQ7ENXYTY3LeupWPriK8jAW5ZmcwC9zfg8FOAqviZYJLsyMdk90GQwa1B4BBxBa431PUeGx31yog7bsb9wCqnVCktsqYN%2F9RoIb2WDE3R%2Bwc9K8INvIprLdprgbt0TkgtdGczS8z%2BqRz90dSsY95OvECvyoo5Zy9h%2FE1CJxpNLw4OewPkwy3KrqDrgYhslpCa68QpdJG09LcEzD2c2jzUActDmt112Ol0HWhPm23A%2BwtXIruuHIOBugPMWbrUXH8daDIKe%2BKL67J5oQ0%2FrKrCgOa5kJ5DKA5MQEjPFibOlrRCginsgO1Je3fas1x59fN3JO9HOoJ8ASqIY7tr%2Bzmih40JLTOpyLVk25b3zqZ%2BQJI3t4f7JgId51FixFCySqUCIZVLdHn4zBxrMt2sas4Mu8ko08gaZrDEtrl%2Bpjs13AiUP0AjA5J0Jth4TmlKOzp2XqhrJLMJ%2Frj70GOqUB6qHXUGt32z4%2FCK5w1G3bUrkvcHFB3bUw3IR1R2jY7FAOZeBkV7l3tzPqSYVLXwgoXSv8MgZpbt5IV5YLLykLwRuSKLmu%2FOixm3rGlSeZH%2FqbfHLQ1zEatvI8iGCMn2jNV6%2BTgldjwDVjNgmFl2HsumKrqiuqnuK73gRxg2HehnYN1brqJx6Ocf%2BOnRu%2B3uP5luYVQal36BlrwwURucbfldWogy3E&X-Amz-Signature=090f04b286383a52153c20ad2e3642e08c1ee70fcb10f919a3871c9446a0f4a5&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7R4UQT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAtfnD6FpPqjpH5L3R4OcYl7VONZwvJcqrEs%2FEnox49MAiEA3yqUbBlg4%2BgdDgVuAA%2FtJeXLDFN7Msbdr3M%2FPRWtAtAq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDGTrg0VSk6J7stZqVyrcA0jsZIiX0PNBtSWWT33bnxhVrFpMk886B6OWSRd8NYntwa2hv5bBatFCbzV3n9wbbZg4ve02RUHsYrZX4OQa0Lf9Zxhz9yUyaMvQspXjeVowwrQmE0ygA7jmLBzA44IkvgcV7BbXw8dNQ0HJEIUvTOUQDjN8LnxLVq%2BSYSNJtotL2wGaN2rJIXLtFrFGheqNY7Raa%2Fk7GA8NMnP3TfaNaMCuZxpHSghcT9PxwuZPiP88PjIw5%2BjFaG5t%2BTbHIq79GXezyCXPhG2LPBSBDgBnhEXPnE2PdBelozT%2BI1Nx%2BN45rF9fVRU3EBYp31SO0ixPfh08pgl2dMLUy6HA%2FKNOyQBOtw4DDLN9VmXW3G0dIzV9agR%2FP2OresZJb3GMiqKJx1hyMLltvx3iiwqztEkMqNFHXtc70r%2FXPMUBQmOKjoDmHT3kuhkIlW%2FvUMxIgD0EwXxcat1Qy353N2zavK%2FpxWDbDuRTZn6fANgUiF2RkZaD9P3BxfNlpwWHxoh7xWTC0RfcAzgUrJYq61NHEzyac46uHYztHiQkQrGesnC%2BXu91yAHoSRk8s62kRXXm1CMsWZLfbo6clqekTh0OEXFhi1AR7QmMQjXSE6VVE7FzMVk0ylb5nXtrYJr9aHiKMPjqj70GOqUBmT9AwXwVFwU0CXq4gHQkQIEDBZv%2BMqwJSQl2oBkhD%2Fwfq2FKDGZ1%2FgEG2rrckn%2FpN%2FRrN75UmztzCelGqmBdc6TyvGMKhBDPRPD6VJ7xJpdeexX27l5mjieHcifzSksLFHao08rHda%2Fc%2FBw2aOfvvafpfAJcoUwSwAmrxtQqWRRnQTqa3fLtLlUiJjdNQw4fyMA7gFTMWJm4tB%2FeiC8PxxQQqfPm&X-Amz-Signature=410af6ac66817ad6db776d1ffcae82596965ccc90c220db32dfeb9e7e8636f7b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7R4UQT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAtfnD6FpPqjpH5L3R4OcYl7VONZwvJcqrEs%2FEnox49MAiEA3yqUbBlg4%2BgdDgVuAA%2FtJeXLDFN7Msbdr3M%2FPRWtAtAq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDGTrg0VSk6J7stZqVyrcA0jsZIiX0PNBtSWWT33bnxhVrFpMk886B6OWSRd8NYntwa2hv5bBatFCbzV3n9wbbZg4ve02RUHsYrZX4OQa0Lf9Zxhz9yUyaMvQspXjeVowwrQmE0ygA7jmLBzA44IkvgcV7BbXw8dNQ0HJEIUvTOUQDjN8LnxLVq%2BSYSNJtotL2wGaN2rJIXLtFrFGheqNY7Raa%2Fk7GA8NMnP3TfaNaMCuZxpHSghcT9PxwuZPiP88PjIw5%2BjFaG5t%2BTbHIq79GXezyCXPhG2LPBSBDgBnhEXPnE2PdBelozT%2BI1Nx%2BN45rF9fVRU3EBYp31SO0ixPfh08pgl2dMLUy6HA%2FKNOyQBOtw4DDLN9VmXW3G0dIzV9agR%2FP2OresZJb3GMiqKJx1hyMLltvx3iiwqztEkMqNFHXtc70r%2FXPMUBQmOKjoDmHT3kuhkIlW%2FvUMxIgD0EwXxcat1Qy353N2zavK%2FpxWDbDuRTZn6fANgUiF2RkZaD9P3BxfNlpwWHxoh7xWTC0RfcAzgUrJYq61NHEzyac46uHYztHiQkQrGesnC%2BXu91yAHoSRk8s62kRXXm1CMsWZLfbo6clqekTh0OEXFhi1AR7QmMQjXSE6VVE7FzMVk0ylb5nXtrYJr9aHiKMPjqj70GOqUBmT9AwXwVFwU0CXq4gHQkQIEDBZv%2BMqwJSQl2oBkhD%2Fwfq2FKDGZ1%2FgEG2rrckn%2FpN%2FRrN75UmztzCelGqmBdc6TyvGMKhBDPRPD6VJ7xJpdeexX27l5mjieHcifzSksLFHao08rHda%2Fc%2FBw2aOfvvafpfAJcoUwSwAmrxtQqWRRnQTqa3fLtLlUiJjdNQw4fyMA7gFTMWJm4tB%2FeiC8PxxQQqfPm&X-Amz-Signature=f50ed8727a01f1f910ec8d6d5637f6695fdec7909c605ea3c4e1f168f882374e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7R4UQT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAtfnD6FpPqjpH5L3R4OcYl7VONZwvJcqrEs%2FEnox49MAiEA3yqUbBlg4%2BgdDgVuAA%2FtJeXLDFN7Msbdr3M%2FPRWtAtAq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDGTrg0VSk6J7stZqVyrcA0jsZIiX0PNBtSWWT33bnxhVrFpMk886B6OWSRd8NYntwa2hv5bBatFCbzV3n9wbbZg4ve02RUHsYrZX4OQa0Lf9Zxhz9yUyaMvQspXjeVowwrQmE0ygA7jmLBzA44IkvgcV7BbXw8dNQ0HJEIUvTOUQDjN8LnxLVq%2BSYSNJtotL2wGaN2rJIXLtFrFGheqNY7Raa%2Fk7GA8NMnP3TfaNaMCuZxpHSghcT9PxwuZPiP88PjIw5%2BjFaG5t%2BTbHIq79GXezyCXPhG2LPBSBDgBnhEXPnE2PdBelozT%2BI1Nx%2BN45rF9fVRU3EBYp31SO0ixPfh08pgl2dMLUy6HA%2FKNOyQBOtw4DDLN9VmXW3G0dIzV9agR%2FP2OresZJb3GMiqKJx1hyMLltvx3iiwqztEkMqNFHXtc70r%2FXPMUBQmOKjoDmHT3kuhkIlW%2FvUMxIgD0EwXxcat1Qy353N2zavK%2FpxWDbDuRTZn6fANgUiF2RkZaD9P3BxfNlpwWHxoh7xWTC0RfcAzgUrJYq61NHEzyac46uHYztHiQkQrGesnC%2BXu91yAHoSRk8s62kRXXm1CMsWZLfbo6clqekTh0OEXFhi1AR7QmMQjXSE6VVE7FzMVk0ylb5nXtrYJr9aHiKMPjqj70GOqUBmT9AwXwVFwU0CXq4gHQkQIEDBZv%2BMqwJSQl2oBkhD%2Fwfq2FKDGZ1%2FgEG2rrckn%2FpN%2FRrN75UmztzCelGqmBdc6TyvGMKhBDPRPD6VJ7xJpdeexX27l5mjieHcifzSksLFHao08rHda%2Fc%2FBw2aOfvvafpfAJcoUwSwAmrxtQqWRRnQTqa3fLtLlUiJjdNQw4fyMA7gFTMWJm4tB%2FeiC8PxxQQqfPm&X-Amz-Signature=9639a241c1a812fdf249da035fe984bf7881fac68f284054cb9700b4f787376e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7R4UQT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAtfnD6FpPqjpH5L3R4OcYl7VONZwvJcqrEs%2FEnox49MAiEA3yqUbBlg4%2BgdDgVuAA%2FtJeXLDFN7Msbdr3M%2FPRWtAtAq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDGTrg0VSk6J7stZqVyrcA0jsZIiX0PNBtSWWT33bnxhVrFpMk886B6OWSRd8NYntwa2hv5bBatFCbzV3n9wbbZg4ve02RUHsYrZX4OQa0Lf9Zxhz9yUyaMvQspXjeVowwrQmE0ygA7jmLBzA44IkvgcV7BbXw8dNQ0HJEIUvTOUQDjN8LnxLVq%2BSYSNJtotL2wGaN2rJIXLtFrFGheqNY7Raa%2Fk7GA8NMnP3TfaNaMCuZxpHSghcT9PxwuZPiP88PjIw5%2BjFaG5t%2BTbHIq79GXezyCXPhG2LPBSBDgBnhEXPnE2PdBelozT%2BI1Nx%2BN45rF9fVRU3EBYp31SO0ixPfh08pgl2dMLUy6HA%2FKNOyQBOtw4DDLN9VmXW3G0dIzV9agR%2FP2OresZJb3GMiqKJx1hyMLltvx3iiwqztEkMqNFHXtc70r%2FXPMUBQmOKjoDmHT3kuhkIlW%2FvUMxIgD0EwXxcat1Qy353N2zavK%2FpxWDbDuRTZn6fANgUiF2RkZaD9P3BxfNlpwWHxoh7xWTC0RfcAzgUrJYq61NHEzyac46uHYztHiQkQrGesnC%2BXu91yAHoSRk8s62kRXXm1CMsWZLfbo6clqekTh0OEXFhi1AR7QmMQjXSE6VVE7FzMVk0ylb5nXtrYJr9aHiKMPjqj70GOqUBmT9AwXwVFwU0CXq4gHQkQIEDBZv%2BMqwJSQl2oBkhD%2Fwfq2FKDGZ1%2FgEG2rrckn%2FpN%2FRrN75UmztzCelGqmBdc6TyvGMKhBDPRPD6VJ7xJpdeexX27l5mjieHcifzSksLFHao08rHda%2Fc%2FBw2aOfvvafpfAJcoUwSwAmrxtQqWRRnQTqa3fLtLlUiJjdNQw4fyMA7gFTMWJm4tB%2FeiC8PxxQQqfPm&X-Amz-Signature=9b938b00d4157a568d86992dfb868c16c077c9dca4e473e5f5efaeef0a8bb04c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7R4UQT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAtfnD6FpPqjpH5L3R4OcYl7VONZwvJcqrEs%2FEnox49MAiEA3yqUbBlg4%2BgdDgVuAA%2FtJeXLDFN7Msbdr3M%2FPRWtAtAq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDGTrg0VSk6J7stZqVyrcA0jsZIiX0PNBtSWWT33bnxhVrFpMk886B6OWSRd8NYntwa2hv5bBatFCbzV3n9wbbZg4ve02RUHsYrZX4OQa0Lf9Zxhz9yUyaMvQspXjeVowwrQmE0ygA7jmLBzA44IkvgcV7BbXw8dNQ0HJEIUvTOUQDjN8LnxLVq%2BSYSNJtotL2wGaN2rJIXLtFrFGheqNY7Raa%2Fk7GA8NMnP3TfaNaMCuZxpHSghcT9PxwuZPiP88PjIw5%2BjFaG5t%2BTbHIq79GXezyCXPhG2LPBSBDgBnhEXPnE2PdBelozT%2BI1Nx%2BN45rF9fVRU3EBYp31SO0ixPfh08pgl2dMLUy6HA%2FKNOyQBOtw4DDLN9VmXW3G0dIzV9agR%2FP2OresZJb3GMiqKJx1hyMLltvx3iiwqztEkMqNFHXtc70r%2FXPMUBQmOKjoDmHT3kuhkIlW%2FvUMxIgD0EwXxcat1Qy353N2zavK%2FpxWDbDuRTZn6fANgUiF2RkZaD9P3BxfNlpwWHxoh7xWTC0RfcAzgUrJYq61NHEzyac46uHYztHiQkQrGesnC%2BXu91yAHoSRk8s62kRXXm1CMsWZLfbo6clqekTh0OEXFhi1AR7QmMQjXSE6VVE7FzMVk0ylb5nXtrYJr9aHiKMPjqj70GOqUBmT9AwXwVFwU0CXq4gHQkQIEDBZv%2BMqwJSQl2oBkhD%2Fwfq2FKDGZ1%2FgEG2rrckn%2FpN%2FRrN75UmztzCelGqmBdc6TyvGMKhBDPRPD6VJ7xJpdeexX27l5mjieHcifzSksLFHao08rHda%2Fc%2FBw2aOfvvafpfAJcoUwSwAmrxtQqWRRnQTqa3fLtLlUiJjdNQw4fyMA7gFTMWJm4tB%2FeiC8PxxQQqfPm&X-Amz-Signature=225cf4004097ff4cb4876a8ffec59394aa8dd1fe0ee189baf516af3e4b871fec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRR4AONB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAkf%2Fcgc8mq6XFq465X8pzxXZOd8Ce7UMlfiGoBjVDZmAiEA7muWzwHhwRB3VQdxlTzywzDePwIupRGO9QRxe1V2dM4q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDFVPRhGQkWgi2jdUVircA1LJVQVnbdHnLQEiInDJeXdfDbyzL9271rwUPhokngzF8UUnT0jZw779vB5r4ifdOvMPq1mC2PBEWVDHaqBKx30VpcXbmtnU%2FjiCTKHQ5MinU%2FvFhGrATR8rIOzYfrVI3jJo76IateVOt%2FPHK07guvrvI1NOEQFYGK6KRpxO72Cuag0i7dtkXFQ7ENXYTY3LeupWPriK8jAW5ZmcwC9zfg8FOAqviZYJLsyMdk90GQwa1B4BBxBa431PUeGx31yog7bsb9wCqnVCktsqYN%2F9RoIb2WDE3R%2Bwc9K8INvIprLdprgbt0TkgtdGczS8z%2BqRz90dSsY95OvECvyoo5Zy9h%2FE1CJxpNLw4OewPkwy3KrqDrgYhslpCa68QpdJG09LcEzD2c2jzUActDmt112Ol0HWhPm23A%2BwtXIruuHIOBugPMWbrUXH8daDIKe%2BKL67J5oQ0%2FrKrCgOa5kJ5DKA5MQEjPFibOlrRCginsgO1Je3fas1x59fN3JO9HOoJ8ASqIY7tr%2Bzmih40JLTOpyLVk25b3zqZ%2BQJI3t4f7JgId51FixFCySqUCIZVLdHn4zBxrMt2sas4Mu8ko08gaZrDEtrl%2Bpjs13AiUP0AjA5J0Jth4TmlKOzp2XqhrJLMJ%2Frj70GOqUB6qHXUGt32z4%2FCK5w1G3bUrkvcHFB3bUw3IR1R2jY7FAOZeBkV7l3tzPqSYVLXwgoXSv8MgZpbt5IV5YLLykLwRuSKLmu%2FOixm3rGlSeZH%2FqbfHLQ1zEatvI8iGCMn2jNV6%2BTgldjwDVjNgmFl2HsumKrqiuqnuK73gRxg2HehnYN1brqJx6Ocf%2BOnRu%2B3uP5luYVQal36BlrwwURucbfldWogy3E&X-Amz-Signature=3450e596feb2cb102fc58ad27af314f07ee8bdba6cb0d28976a5c314de064319&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRR4AONB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAkf%2Fcgc8mq6XFq465X8pzxXZOd8Ce7UMlfiGoBjVDZmAiEA7muWzwHhwRB3VQdxlTzywzDePwIupRGO9QRxe1V2dM4q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDFVPRhGQkWgi2jdUVircA1LJVQVnbdHnLQEiInDJeXdfDbyzL9271rwUPhokngzF8UUnT0jZw779vB5r4ifdOvMPq1mC2PBEWVDHaqBKx30VpcXbmtnU%2FjiCTKHQ5MinU%2FvFhGrATR8rIOzYfrVI3jJo76IateVOt%2FPHK07guvrvI1NOEQFYGK6KRpxO72Cuag0i7dtkXFQ7ENXYTY3LeupWPriK8jAW5ZmcwC9zfg8FOAqviZYJLsyMdk90GQwa1B4BBxBa431PUeGx31yog7bsb9wCqnVCktsqYN%2F9RoIb2WDE3R%2Bwc9K8INvIprLdprgbt0TkgtdGczS8z%2BqRz90dSsY95OvECvyoo5Zy9h%2FE1CJxpNLw4OewPkwy3KrqDrgYhslpCa68QpdJG09LcEzD2c2jzUActDmt112Ol0HWhPm23A%2BwtXIruuHIOBugPMWbrUXH8daDIKe%2BKL67J5oQ0%2FrKrCgOa5kJ5DKA5MQEjPFibOlrRCginsgO1Je3fas1x59fN3JO9HOoJ8ASqIY7tr%2Bzmih40JLTOpyLVk25b3zqZ%2BQJI3t4f7JgId51FixFCySqUCIZVLdHn4zBxrMt2sas4Mu8ko08gaZrDEtrl%2Bpjs13AiUP0AjA5J0Jth4TmlKOzp2XqhrJLMJ%2Frj70GOqUB6qHXUGt32z4%2FCK5w1G3bUrkvcHFB3bUw3IR1R2jY7FAOZeBkV7l3tzPqSYVLXwgoXSv8MgZpbt5IV5YLLykLwRuSKLmu%2FOixm3rGlSeZH%2FqbfHLQ1zEatvI8iGCMn2jNV6%2BTgldjwDVjNgmFl2HsumKrqiuqnuK73gRxg2HehnYN1brqJx6Ocf%2BOnRu%2B3uP5luYVQal36BlrwwURucbfldWogy3E&X-Amz-Signature=2e60196dbf6c5a70a8fd9aa81bdb60bb803f54b1fdb93415496cfa295eee491f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRR4AONB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAkf%2Fcgc8mq6XFq465X8pzxXZOd8Ce7UMlfiGoBjVDZmAiEA7muWzwHhwRB3VQdxlTzywzDePwIupRGO9QRxe1V2dM4q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDFVPRhGQkWgi2jdUVircA1LJVQVnbdHnLQEiInDJeXdfDbyzL9271rwUPhokngzF8UUnT0jZw779vB5r4ifdOvMPq1mC2PBEWVDHaqBKx30VpcXbmtnU%2FjiCTKHQ5MinU%2FvFhGrATR8rIOzYfrVI3jJo76IateVOt%2FPHK07guvrvI1NOEQFYGK6KRpxO72Cuag0i7dtkXFQ7ENXYTY3LeupWPriK8jAW5ZmcwC9zfg8FOAqviZYJLsyMdk90GQwa1B4BBxBa431PUeGx31yog7bsb9wCqnVCktsqYN%2F9RoIb2WDE3R%2Bwc9K8INvIprLdprgbt0TkgtdGczS8z%2BqRz90dSsY95OvECvyoo5Zy9h%2FE1CJxpNLw4OewPkwy3KrqDrgYhslpCa68QpdJG09LcEzD2c2jzUActDmt112Ol0HWhPm23A%2BwtXIruuHIOBugPMWbrUXH8daDIKe%2BKL67J5oQ0%2FrKrCgOa5kJ5DKA5MQEjPFibOlrRCginsgO1Je3fas1x59fN3JO9HOoJ8ASqIY7tr%2Bzmih40JLTOpyLVk25b3zqZ%2BQJI3t4f7JgId51FixFCySqUCIZVLdHn4zBxrMt2sas4Mu8ko08gaZrDEtrl%2Bpjs13AiUP0AjA5J0Jth4TmlKOzp2XqhrJLMJ%2Frj70GOqUB6qHXUGt32z4%2FCK5w1G3bUrkvcHFB3bUw3IR1R2jY7FAOZeBkV7l3tzPqSYVLXwgoXSv8MgZpbt5IV5YLLykLwRuSKLmu%2FOixm3rGlSeZH%2FqbfHLQ1zEatvI8iGCMn2jNV6%2BTgldjwDVjNgmFl2HsumKrqiuqnuK73gRxg2HehnYN1brqJx6Ocf%2BOnRu%2B3uP5luYVQal36BlrwwURucbfldWogy3E&X-Amz-Signature=7e88938271440c928ebf2c3fa13e0711c591e59e28151a2860d113f39be4e73b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRR4AONB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAkf%2Fcgc8mq6XFq465X8pzxXZOd8Ce7UMlfiGoBjVDZmAiEA7muWzwHhwRB3VQdxlTzywzDePwIupRGO9QRxe1V2dM4q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDFVPRhGQkWgi2jdUVircA1LJVQVnbdHnLQEiInDJeXdfDbyzL9271rwUPhokngzF8UUnT0jZw779vB5r4ifdOvMPq1mC2PBEWVDHaqBKx30VpcXbmtnU%2FjiCTKHQ5MinU%2FvFhGrATR8rIOzYfrVI3jJo76IateVOt%2FPHK07guvrvI1NOEQFYGK6KRpxO72Cuag0i7dtkXFQ7ENXYTY3LeupWPriK8jAW5ZmcwC9zfg8FOAqviZYJLsyMdk90GQwa1B4BBxBa431PUeGx31yog7bsb9wCqnVCktsqYN%2F9RoIb2WDE3R%2Bwc9K8INvIprLdprgbt0TkgtdGczS8z%2BqRz90dSsY95OvECvyoo5Zy9h%2FE1CJxpNLw4OewPkwy3KrqDrgYhslpCa68QpdJG09LcEzD2c2jzUActDmt112Ol0HWhPm23A%2BwtXIruuHIOBugPMWbrUXH8daDIKe%2BKL67J5oQ0%2FrKrCgOa5kJ5DKA5MQEjPFibOlrRCginsgO1Je3fas1x59fN3JO9HOoJ8ASqIY7tr%2Bzmih40JLTOpyLVk25b3zqZ%2BQJI3t4f7JgId51FixFCySqUCIZVLdHn4zBxrMt2sas4Mu8ko08gaZrDEtrl%2Bpjs13AiUP0AjA5J0Jth4TmlKOzp2XqhrJLMJ%2Frj70GOqUB6qHXUGt32z4%2FCK5w1G3bUrkvcHFB3bUw3IR1R2jY7FAOZeBkV7l3tzPqSYVLXwgoXSv8MgZpbt5IV5YLLykLwRuSKLmu%2FOixm3rGlSeZH%2FqbfHLQ1zEatvI8iGCMn2jNV6%2BTgldjwDVjNgmFl2HsumKrqiuqnuK73gRxg2HehnYN1brqJx6Ocf%2BOnRu%2B3uP5luYVQal36BlrwwURucbfldWogy3E&X-Amz-Signature=8b5d7fb9dff80c5d432d9665f9637199fab1ffeeac5bea586a1d2e6017d1d5c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRR4AONB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAkf%2Fcgc8mq6XFq465X8pzxXZOd8Ce7UMlfiGoBjVDZmAiEA7muWzwHhwRB3VQdxlTzywzDePwIupRGO9QRxe1V2dM4q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDFVPRhGQkWgi2jdUVircA1LJVQVnbdHnLQEiInDJeXdfDbyzL9271rwUPhokngzF8UUnT0jZw779vB5r4ifdOvMPq1mC2PBEWVDHaqBKx30VpcXbmtnU%2FjiCTKHQ5MinU%2FvFhGrATR8rIOzYfrVI3jJo76IateVOt%2FPHK07guvrvI1NOEQFYGK6KRpxO72Cuag0i7dtkXFQ7ENXYTY3LeupWPriK8jAW5ZmcwC9zfg8FOAqviZYJLsyMdk90GQwa1B4BBxBa431PUeGx31yog7bsb9wCqnVCktsqYN%2F9RoIb2WDE3R%2Bwc9K8INvIprLdprgbt0TkgtdGczS8z%2BqRz90dSsY95OvECvyoo5Zy9h%2FE1CJxpNLw4OewPkwy3KrqDrgYhslpCa68QpdJG09LcEzD2c2jzUActDmt112Ol0HWhPm23A%2BwtXIruuHIOBugPMWbrUXH8daDIKe%2BKL67J5oQ0%2FrKrCgOa5kJ5DKA5MQEjPFibOlrRCginsgO1Je3fas1x59fN3JO9HOoJ8ASqIY7tr%2Bzmih40JLTOpyLVk25b3zqZ%2BQJI3t4f7JgId51FixFCySqUCIZVLdHn4zBxrMt2sas4Mu8ko08gaZrDEtrl%2Bpjs13AiUP0AjA5J0Jth4TmlKOzp2XqhrJLMJ%2Frj70GOqUB6qHXUGt32z4%2FCK5w1G3bUrkvcHFB3bUw3IR1R2jY7FAOZeBkV7l3tzPqSYVLXwgoXSv8MgZpbt5IV5YLLykLwRuSKLmu%2FOixm3rGlSeZH%2FqbfHLQ1zEatvI8iGCMn2jNV6%2BTgldjwDVjNgmFl2HsumKrqiuqnuK73gRxg2HehnYN1brqJx6Ocf%2BOnRu%2B3uP5luYVQal36BlrwwURucbfldWogy3E&X-Amz-Signature=a1336f557f720049d44b065e16e749f107fb75e15c4fc6d36b984554239f6307&X-Amz-SignedHeaders=host&x-id=GetObject)
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


