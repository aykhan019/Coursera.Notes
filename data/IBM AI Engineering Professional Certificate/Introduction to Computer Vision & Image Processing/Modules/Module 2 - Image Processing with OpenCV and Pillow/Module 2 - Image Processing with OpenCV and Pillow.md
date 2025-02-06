

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHWE7RMN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCiwOl4Dpi9miAvLVmuKm%2FrAWOvU359S4YHXrmEvTi3ZwIhALHeDDWeSvXjAgi4cA2D6W7FrlJii1rP2%2FT8S46k8b5xKv8DCGYQABoMNjM3NDIzMTgzODA1Igzhx934UK0wOKFp%2F0Qq3AMK4qX8q6p47hJ0XMt2zgXCHLrrnCbPMqnj2%2FkwCmxwZAG9xVAP%2BqhKJ8CGPAZOpzqVRzVLL4daCbOrC%2FdSXGL3CM9zMa132FCS8qXRY5xKyRONQLgDbrnVDK1BrwPjX2x0VIiPU8SDuGS2qc4CbfNLG%2BsTz0V9uHSJf%2BMCsPdr1nZZPvKkHmM%2FFWIc%2BC1ilJ6EJK0NmAWtROIKxwJINCYQ8qiX2quu04R4Qlb1Siz6ZwVq8pq1PCb%2BctiBeB0ws4YA8eyaJ5lW%2BUUP71oqjKbwpkbo5zyDTxu9OpgsLGhiL4CYGnPbQlJj6B%2B%2FMjbxo%2FHW8T0TUPzxQnxcG2QKFDkOw9YB%2BpGSvO6HwE1KnyhFtvEzssKA06FBmnFYKM176NaovAzShZ1VIrf%2F0DgpSNKKLloQ0oOi6xijxKKkbfeQVeq0%2FJcX2ckgHmoXbMrAXcGkuZ7zFU8yUcW2%2FXJ09Q6AOKxlb8uCN4auQhEbhJHOuUGHUsqT2jN5lUfpnknMAHdasgR3MDNF3GH0OURlQVVsPj0cYpILAhYquQi3QzwAoN0836wBu6aTgyjmas7N%2BPIWo99kV0%2FlMoDJ3D%2Bo%2BQgkfJaMskCsLhPGmrU6xtdQtrv1QUMm0%2FwrZLWziTDiuJS9BjqkAWfgwCh2fWaPMGC4%2Fn4HfdYaj0cxu%2Fwi4oxf5ufhsZHU0WOU92%2B%2BRUEpHV5iErFYn0%2BaqzvXZqXdXgknCwvRFjHAvgzIrHEGei8b%2BLfjxNZ0x%2Bnm1flQc8IHDojvnDo1VOi3nxtycpB8GoqJSaoLmiAONCIc3zDvkUCb3ulO0h%2F4RHAsNV4VGMSfCryewbcnkGGXnsh9LBxVRlmkIul%2Fv6fRMwkX&X-Amz-Signature=553e3f16865517f178504b737cfb72c7a1cc4fe35b7a3158c43ebfed997b9419&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626FDQ3ST%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIB5SIxtq%2B5k5q2ARoiIeCVhUH1yPOCv4f0RxgwajzXG2AiEApcXw7xuiaolJkkZ7e0U2CQBCQ%2F5XOuF3sv%2B1GdfcGxUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPO2fZTi5vJNb2Q%2BkyrcA7jLqTqNqXzlCtXf3T1KM7M1%2BEkMKOY%2B%2FjGQTSMZYICY0%2FYOaKEFXCLF6s830PVG4uhrikTMov8odf2Gw%2F8XJcAZkc0M7tmNkaUZ3j61WeRlvgRwaUYC75ChCVMP%2FeMf21UdRfcZS5vKeI13JGyBUk8vAe5uDLt3YkGEh2%2Bfv%2BBPBZsSE7NXfDT9EGWyGp8JCOLZqXuOu6uAgMB8K8Z32Ejsx2SBwZWhzp2vppx0UyMNJhWnVjyZKJHB6VcFj6e93kxZrV3lCN%2Fe8m0j7qIAu9ShG9U7hJC%2FuTAgpRSClfmve64OzNIzIE3jwFDmRBVTlQctGPjkcdbocnCrpOWiupJpR4WBD14k4ORSJIv%2F1cSxC4pc3ZSDI44XOzjWwpuAI992iMEx7vUc22hVlcGa8gL1IZVQyS%2FQB5WIgDGzOwzy8ajP12GDgiUu5DvwZEnrVDItcMDUGzGPnsuFuQeqJs2ZIMNXkqcXg9O2Vr38cqUTIBS3sNuNCLibZfoVPf8Kaaqk1RKCotZ32vuqLBtUqaeB4BXOvCXFDadvZMU%2BxxGM3FSKOvSzXDtYsZuwgayCK8XpRTFIi38jUWfNNHkOHB%2B8H0vfwuCWLRe%2BlHG%2BnEQgLr1jMjK9KiWpCTQOMKO4lL0GOqUB3p78MQ%2F7RsVyqQMSMLheg6VmVjuUlthsX1OnhS%2Blsu2PLItkeHcgT9ElbzxdcxeXzRLLuLZ%2BRAOzuAmqvfrzraBpme8WN5hNjvTPvRz2DTRn6hIbEqXpUv8UJiVQCVsMGI8Z5BzhOY7lQ8ZEVtsxJ%2FrFM2XmEIn8R8L56nK46t8oItZbqvHKfurDSkb1uVeq8HonNdsor2rZ9OFVyVJT8pNXPGnw&X-Amz-Signature=6e21cc0e62574ddec91cb656738cb3d94349c1aed731a335f2a159594ca0cb2d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626FDQ3ST%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIB5SIxtq%2B5k5q2ARoiIeCVhUH1yPOCv4f0RxgwajzXG2AiEApcXw7xuiaolJkkZ7e0U2CQBCQ%2F5XOuF3sv%2B1GdfcGxUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPO2fZTi5vJNb2Q%2BkyrcA7jLqTqNqXzlCtXf3T1KM7M1%2BEkMKOY%2B%2FjGQTSMZYICY0%2FYOaKEFXCLF6s830PVG4uhrikTMov8odf2Gw%2F8XJcAZkc0M7tmNkaUZ3j61WeRlvgRwaUYC75ChCVMP%2FeMf21UdRfcZS5vKeI13JGyBUk8vAe5uDLt3YkGEh2%2Bfv%2BBPBZsSE7NXfDT9EGWyGp8JCOLZqXuOu6uAgMB8K8Z32Ejsx2SBwZWhzp2vppx0UyMNJhWnVjyZKJHB6VcFj6e93kxZrV3lCN%2Fe8m0j7qIAu9ShG9U7hJC%2FuTAgpRSClfmve64OzNIzIE3jwFDmRBVTlQctGPjkcdbocnCrpOWiupJpR4WBD14k4ORSJIv%2F1cSxC4pc3ZSDI44XOzjWwpuAI992iMEx7vUc22hVlcGa8gL1IZVQyS%2FQB5WIgDGzOwzy8ajP12GDgiUu5DvwZEnrVDItcMDUGzGPnsuFuQeqJs2ZIMNXkqcXg9O2Vr38cqUTIBS3sNuNCLibZfoVPf8Kaaqk1RKCotZ32vuqLBtUqaeB4BXOvCXFDadvZMU%2BxxGM3FSKOvSzXDtYsZuwgayCK8XpRTFIi38jUWfNNHkOHB%2B8H0vfwuCWLRe%2BlHG%2BnEQgLr1jMjK9KiWpCTQOMKO4lL0GOqUB3p78MQ%2F7RsVyqQMSMLheg6VmVjuUlthsX1OnhS%2Blsu2PLItkeHcgT9ElbzxdcxeXzRLLuLZ%2BRAOzuAmqvfrzraBpme8WN5hNjvTPvRz2DTRn6hIbEqXpUv8UJiVQCVsMGI8Z5BzhOY7lQ8ZEVtsxJ%2FrFM2XmEIn8R8L56nK46t8oItZbqvHKfurDSkb1uVeq8HonNdsor2rZ9OFVyVJT8pNXPGnw&X-Amz-Signature=490ae9ef623d7cb31613ccd275ad821c8bade1b4436c7b6e70f1f50d1774ab4a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626FDQ3ST%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIB5SIxtq%2B5k5q2ARoiIeCVhUH1yPOCv4f0RxgwajzXG2AiEApcXw7xuiaolJkkZ7e0U2CQBCQ%2F5XOuF3sv%2B1GdfcGxUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPO2fZTi5vJNb2Q%2BkyrcA7jLqTqNqXzlCtXf3T1KM7M1%2BEkMKOY%2B%2FjGQTSMZYICY0%2FYOaKEFXCLF6s830PVG4uhrikTMov8odf2Gw%2F8XJcAZkc0M7tmNkaUZ3j61WeRlvgRwaUYC75ChCVMP%2FeMf21UdRfcZS5vKeI13JGyBUk8vAe5uDLt3YkGEh2%2Bfv%2BBPBZsSE7NXfDT9EGWyGp8JCOLZqXuOu6uAgMB8K8Z32Ejsx2SBwZWhzp2vppx0UyMNJhWnVjyZKJHB6VcFj6e93kxZrV3lCN%2Fe8m0j7qIAu9ShG9U7hJC%2FuTAgpRSClfmve64OzNIzIE3jwFDmRBVTlQctGPjkcdbocnCrpOWiupJpR4WBD14k4ORSJIv%2F1cSxC4pc3ZSDI44XOzjWwpuAI992iMEx7vUc22hVlcGa8gL1IZVQyS%2FQB5WIgDGzOwzy8ajP12GDgiUu5DvwZEnrVDItcMDUGzGPnsuFuQeqJs2ZIMNXkqcXg9O2Vr38cqUTIBS3sNuNCLibZfoVPf8Kaaqk1RKCotZ32vuqLBtUqaeB4BXOvCXFDadvZMU%2BxxGM3FSKOvSzXDtYsZuwgayCK8XpRTFIi38jUWfNNHkOHB%2B8H0vfwuCWLRe%2BlHG%2BnEQgLr1jMjK9KiWpCTQOMKO4lL0GOqUB3p78MQ%2F7RsVyqQMSMLheg6VmVjuUlthsX1OnhS%2Blsu2PLItkeHcgT9ElbzxdcxeXzRLLuLZ%2BRAOzuAmqvfrzraBpme8WN5hNjvTPvRz2DTRn6hIbEqXpUv8UJiVQCVsMGI8Z5BzhOY7lQ8ZEVtsxJ%2FrFM2XmEIn8R8L56nK46t8oItZbqvHKfurDSkb1uVeq8HonNdsor2rZ9OFVyVJT8pNXPGnw&X-Amz-Signature=7f4d864020ddfd36df04d16d88a24e6c63a7886e8ac2a500668051aea2f20aee&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626FDQ3ST%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIB5SIxtq%2B5k5q2ARoiIeCVhUH1yPOCv4f0RxgwajzXG2AiEApcXw7xuiaolJkkZ7e0U2CQBCQ%2F5XOuF3sv%2B1GdfcGxUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPO2fZTi5vJNb2Q%2BkyrcA7jLqTqNqXzlCtXf3T1KM7M1%2BEkMKOY%2B%2FjGQTSMZYICY0%2FYOaKEFXCLF6s830PVG4uhrikTMov8odf2Gw%2F8XJcAZkc0M7tmNkaUZ3j61WeRlvgRwaUYC75ChCVMP%2FeMf21UdRfcZS5vKeI13JGyBUk8vAe5uDLt3YkGEh2%2Bfv%2BBPBZsSE7NXfDT9EGWyGp8JCOLZqXuOu6uAgMB8K8Z32Ejsx2SBwZWhzp2vppx0UyMNJhWnVjyZKJHB6VcFj6e93kxZrV3lCN%2Fe8m0j7qIAu9ShG9U7hJC%2FuTAgpRSClfmve64OzNIzIE3jwFDmRBVTlQctGPjkcdbocnCrpOWiupJpR4WBD14k4ORSJIv%2F1cSxC4pc3ZSDI44XOzjWwpuAI992iMEx7vUc22hVlcGa8gL1IZVQyS%2FQB5WIgDGzOwzy8ajP12GDgiUu5DvwZEnrVDItcMDUGzGPnsuFuQeqJs2ZIMNXkqcXg9O2Vr38cqUTIBS3sNuNCLibZfoVPf8Kaaqk1RKCotZ32vuqLBtUqaeB4BXOvCXFDadvZMU%2BxxGM3FSKOvSzXDtYsZuwgayCK8XpRTFIi38jUWfNNHkOHB%2B8H0vfwuCWLRe%2BlHG%2BnEQgLr1jMjK9KiWpCTQOMKO4lL0GOqUB3p78MQ%2F7RsVyqQMSMLheg6VmVjuUlthsX1OnhS%2Blsu2PLItkeHcgT9ElbzxdcxeXzRLLuLZ%2BRAOzuAmqvfrzraBpme8WN5hNjvTPvRz2DTRn6hIbEqXpUv8UJiVQCVsMGI8Z5BzhOY7lQ8ZEVtsxJ%2FrFM2XmEIn8R8L56nK46t8oItZbqvHKfurDSkb1uVeq8HonNdsor2rZ9OFVyVJT8pNXPGnw&X-Amz-Signature=1af1b06151b4fa3b8c49df2204853a3b6b2c49acd1ab906df691de8a4b87069c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626FDQ3ST%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIB5SIxtq%2B5k5q2ARoiIeCVhUH1yPOCv4f0RxgwajzXG2AiEApcXw7xuiaolJkkZ7e0U2CQBCQ%2F5XOuF3sv%2B1GdfcGxUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPO2fZTi5vJNb2Q%2BkyrcA7jLqTqNqXzlCtXf3T1KM7M1%2BEkMKOY%2B%2FjGQTSMZYICY0%2FYOaKEFXCLF6s830PVG4uhrikTMov8odf2Gw%2F8XJcAZkc0M7tmNkaUZ3j61WeRlvgRwaUYC75ChCVMP%2FeMf21UdRfcZS5vKeI13JGyBUk8vAe5uDLt3YkGEh2%2Bfv%2BBPBZsSE7NXfDT9EGWyGp8JCOLZqXuOu6uAgMB8K8Z32Ejsx2SBwZWhzp2vppx0UyMNJhWnVjyZKJHB6VcFj6e93kxZrV3lCN%2Fe8m0j7qIAu9ShG9U7hJC%2FuTAgpRSClfmve64OzNIzIE3jwFDmRBVTlQctGPjkcdbocnCrpOWiupJpR4WBD14k4ORSJIv%2F1cSxC4pc3ZSDI44XOzjWwpuAI992iMEx7vUc22hVlcGa8gL1IZVQyS%2FQB5WIgDGzOwzy8ajP12GDgiUu5DvwZEnrVDItcMDUGzGPnsuFuQeqJs2ZIMNXkqcXg9O2Vr38cqUTIBS3sNuNCLibZfoVPf8Kaaqk1RKCotZ32vuqLBtUqaeB4BXOvCXFDadvZMU%2BxxGM3FSKOvSzXDtYsZuwgayCK8XpRTFIi38jUWfNNHkOHB%2B8H0vfwuCWLRe%2BlHG%2BnEQgLr1jMjK9KiWpCTQOMKO4lL0GOqUB3p78MQ%2F7RsVyqQMSMLheg6VmVjuUlthsX1OnhS%2Blsu2PLItkeHcgT9ElbzxdcxeXzRLLuLZ%2BRAOzuAmqvfrzraBpme8WN5hNjvTPvRz2DTRn6hIbEqXpUv8UJiVQCVsMGI8Z5BzhOY7lQ8ZEVtsxJ%2FrFM2XmEIn8R8L56nK46t8oItZbqvHKfurDSkb1uVeq8HonNdsor2rZ9OFVyVJT8pNXPGnw&X-Amz-Signature=2e10076f7cef78b60fc17ef07527f6141eae1a039af444d24a900b707c032643&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHWE7RMN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCiwOl4Dpi9miAvLVmuKm%2FrAWOvU359S4YHXrmEvTi3ZwIhALHeDDWeSvXjAgi4cA2D6W7FrlJii1rP2%2FT8S46k8b5xKv8DCGYQABoMNjM3NDIzMTgzODA1Igzhx934UK0wOKFp%2F0Qq3AMK4qX8q6p47hJ0XMt2zgXCHLrrnCbPMqnj2%2FkwCmxwZAG9xVAP%2BqhKJ8CGPAZOpzqVRzVLL4daCbOrC%2FdSXGL3CM9zMa132FCS8qXRY5xKyRONQLgDbrnVDK1BrwPjX2x0VIiPU8SDuGS2qc4CbfNLG%2BsTz0V9uHSJf%2BMCsPdr1nZZPvKkHmM%2FFWIc%2BC1ilJ6EJK0NmAWtROIKxwJINCYQ8qiX2quu04R4Qlb1Siz6ZwVq8pq1PCb%2BctiBeB0ws4YA8eyaJ5lW%2BUUP71oqjKbwpkbo5zyDTxu9OpgsLGhiL4CYGnPbQlJj6B%2B%2FMjbxo%2FHW8T0TUPzxQnxcG2QKFDkOw9YB%2BpGSvO6HwE1KnyhFtvEzssKA06FBmnFYKM176NaovAzShZ1VIrf%2F0DgpSNKKLloQ0oOi6xijxKKkbfeQVeq0%2FJcX2ckgHmoXbMrAXcGkuZ7zFU8yUcW2%2FXJ09Q6AOKxlb8uCN4auQhEbhJHOuUGHUsqT2jN5lUfpnknMAHdasgR3MDNF3GH0OURlQVVsPj0cYpILAhYquQi3QzwAoN0836wBu6aTgyjmas7N%2BPIWo99kV0%2FlMoDJ3D%2Bo%2BQgkfJaMskCsLhPGmrU6xtdQtrv1QUMm0%2FwrZLWziTDiuJS9BjqkAWfgwCh2fWaPMGC4%2Fn4HfdYaj0cxu%2Fwi4oxf5ufhsZHU0WOU92%2B%2BRUEpHV5iErFYn0%2BaqzvXZqXdXgknCwvRFjHAvgzIrHEGei8b%2BLfjxNZ0x%2Bnm1flQc8IHDojvnDo1VOi3nxtycpB8GoqJSaoLmiAONCIc3zDvkUCb3ulO0h%2F4RHAsNV4VGMSfCryewbcnkGGXnsh9LBxVRlmkIul%2Fv6fRMwkX&X-Amz-Signature=78c4adbab37af634dc2ad3e9dbbfdb2c8a4541ed9eccb2be1803edf2c74a8746&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHWE7RMN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCiwOl4Dpi9miAvLVmuKm%2FrAWOvU359S4YHXrmEvTi3ZwIhALHeDDWeSvXjAgi4cA2D6W7FrlJii1rP2%2FT8S46k8b5xKv8DCGYQABoMNjM3NDIzMTgzODA1Igzhx934UK0wOKFp%2F0Qq3AMK4qX8q6p47hJ0XMt2zgXCHLrrnCbPMqnj2%2FkwCmxwZAG9xVAP%2BqhKJ8CGPAZOpzqVRzVLL4daCbOrC%2FdSXGL3CM9zMa132FCS8qXRY5xKyRONQLgDbrnVDK1BrwPjX2x0VIiPU8SDuGS2qc4CbfNLG%2BsTz0V9uHSJf%2BMCsPdr1nZZPvKkHmM%2FFWIc%2BC1ilJ6EJK0NmAWtROIKxwJINCYQ8qiX2quu04R4Qlb1Siz6ZwVq8pq1PCb%2BctiBeB0ws4YA8eyaJ5lW%2BUUP71oqjKbwpkbo5zyDTxu9OpgsLGhiL4CYGnPbQlJj6B%2B%2FMjbxo%2FHW8T0TUPzxQnxcG2QKFDkOw9YB%2BpGSvO6HwE1KnyhFtvEzssKA06FBmnFYKM176NaovAzShZ1VIrf%2F0DgpSNKKLloQ0oOi6xijxKKkbfeQVeq0%2FJcX2ckgHmoXbMrAXcGkuZ7zFU8yUcW2%2FXJ09Q6AOKxlb8uCN4auQhEbhJHOuUGHUsqT2jN5lUfpnknMAHdasgR3MDNF3GH0OURlQVVsPj0cYpILAhYquQi3QzwAoN0836wBu6aTgyjmas7N%2BPIWo99kV0%2FlMoDJ3D%2Bo%2BQgkfJaMskCsLhPGmrU6xtdQtrv1QUMm0%2FwrZLWziTDiuJS9BjqkAWfgwCh2fWaPMGC4%2Fn4HfdYaj0cxu%2Fwi4oxf5ufhsZHU0WOU92%2B%2BRUEpHV5iErFYn0%2BaqzvXZqXdXgknCwvRFjHAvgzIrHEGei8b%2BLfjxNZ0x%2Bnm1flQc8IHDojvnDo1VOi3nxtycpB8GoqJSaoLmiAONCIc3zDvkUCb3ulO0h%2F4RHAsNV4VGMSfCryewbcnkGGXnsh9LBxVRlmkIul%2Fv6fRMwkX&X-Amz-Signature=0d924c7ed60083114a51f37f8d9112faed91d0a8d47d204ad31e42f0fd2f3020&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHWE7RMN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCiwOl4Dpi9miAvLVmuKm%2FrAWOvU359S4YHXrmEvTi3ZwIhALHeDDWeSvXjAgi4cA2D6W7FrlJii1rP2%2FT8S46k8b5xKv8DCGYQABoMNjM3NDIzMTgzODA1Igzhx934UK0wOKFp%2F0Qq3AMK4qX8q6p47hJ0XMt2zgXCHLrrnCbPMqnj2%2FkwCmxwZAG9xVAP%2BqhKJ8CGPAZOpzqVRzVLL4daCbOrC%2FdSXGL3CM9zMa132FCS8qXRY5xKyRONQLgDbrnVDK1BrwPjX2x0VIiPU8SDuGS2qc4CbfNLG%2BsTz0V9uHSJf%2BMCsPdr1nZZPvKkHmM%2FFWIc%2BC1ilJ6EJK0NmAWtROIKxwJINCYQ8qiX2quu04R4Qlb1Siz6ZwVq8pq1PCb%2BctiBeB0ws4YA8eyaJ5lW%2BUUP71oqjKbwpkbo5zyDTxu9OpgsLGhiL4CYGnPbQlJj6B%2B%2FMjbxo%2FHW8T0TUPzxQnxcG2QKFDkOw9YB%2BpGSvO6HwE1KnyhFtvEzssKA06FBmnFYKM176NaovAzShZ1VIrf%2F0DgpSNKKLloQ0oOi6xijxKKkbfeQVeq0%2FJcX2ckgHmoXbMrAXcGkuZ7zFU8yUcW2%2FXJ09Q6AOKxlb8uCN4auQhEbhJHOuUGHUsqT2jN5lUfpnknMAHdasgR3MDNF3GH0OURlQVVsPj0cYpILAhYquQi3QzwAoN0836wBu6aTgyjmas7N%2BPIWo99kV0%2FlMoDJ3D%2Bo%2BQgkfJaMskCsLhPGmrU6xtdQtrv1QUMm0%2FwrZLWziTDiuJS9BjqkAWfgwCh2fWaPMGC4%2Fn4HfdYaj0cxu%2Fwi4oxf5ufhsZHU0WOU92%2B%2BRUEpHV5iErFYn0%2BaqzvXZqXdXgknCwvRFjHAvgzIrHEGei8b%2BLfjxNZ0x%2Bnm1flQc8IHDojvnDo1VOi3nxtycpB8GoqJSaoLmiAONCIc3zDvkUCb3ulO0h%2F4RHAsNV4VGMSfCryewbcnkGGXnsh9LBxVRlmkIul%2Fv6fRMwkX&X-Amz-Signature=0369a8e51a1adb14fe27ce9425236e085cc952937c89e176d126ff5e77fda93b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHWE7RMN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCiwOl4Dpi9miAvLVmuKm%2FrAWOvU359S4YHXrmEvTi3ZwIhALHeDDWeSvXjAgi4cA2D6W7FrlJii1rP2%2FT8S46k8b5xKv8DCGYQABoMNjM3NDIzMTgzODA1Igzhx934UK0wOKFp%2F0Qq3AMK4qX8q6p47hJ0XMt2zgXCHLrrnCbPMqnj2%2FkwCmxwZAG9xVAP%2BqhKJ8CGPAZOpzqVRzVLL4daCbOrC%2FdSXGL3CM9zMa132FCS8qXRY5xKyRONQLgDbrnVDK1BrwPjX2x0VIiPU8SDuGS2qc4CbfNLG%2BsTz0V9uHSJf%2BMCsPdr1nZZPvKkHmM%2FFWIc%2BC1ilJ6EJK0NmAWtROIKxwJINCYQ8qiX2quu04R4Qlb1Siz6ZwVq8pq1PCb%2BctiBeB0ws4YA8eyaJ5lW%2BUUP71oqjKbwpkbo5zyDTxu9OpgsLGhiL4CYGnPbQlJj6B%2B%2FMjbxo%2FHW8T0TUPzxQnxcG2QKFDkOw9YB%2BpGSvO6HwE1KnyhFtvEzssKA06FBmnFYKM176NaovAzShZ1VIrf%2F0DgpSNKKLloQ0oOi6xijxKKkbfeQVeq0%2FJcX2ckgHmoXbMrAXcGkuZ7zFU8yUcW2%2FXJ09Q6AOKxlb8uCN4auQhEbhJHOuUGHUsqT2jN5lUfpnknMAHdasgR3MDNF3GH0OURlQVVsPj0cYpILAhYquQi3QzwAoN0836wBu6aTgyjmas7N%2BPIWo99kV0%2FlMoDJ3D%2Bo%2BQgkfJaMskCsLhPGmrU6xtdQtrv1QUMm0%2FwrZLWziTDiuJS9BjqkAWfgwCh2fWaPMGC4%2Fn4HfdYaj0cxu%2Fwi4oxf5ufhsZHU0WOU92%2B%2BRUEpHV5iErFYn0%2BaqzvXZqXdXgknCwvRFjHAvgzIrHEGei8b%2BLfjxNZ0x%2Bnm1flQc8IHDojvnDo1VOi3nxtycpB8GoqJSaoLmiAONCIc3zDvkUCb3ulO0h%2F4RHAsNV4VGMSfCryewbcnkGGXnsh9LBxVRlmkIul%2Fv6fRMwkX&X-Amz-Signature=7b9eda6d25979d84599199d0d258b37a145fccd442cd9dd218dc839a450afdc7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHWE7RMN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCiwOl4Dpi9miAvLVmuKm%2FrAWOvU359S4YHXrmEvTi3ZwIhALHeDDWeSvXjAgi4cA2D6W7FrlJii1rP2%2FT8S46k8b5xKv8DCGYQABoMNjM3NDIzMTgzODA1Igzhx934UK0wOKFp%2F0Qq3AMK4qX8q6p47hJ0XMt2zgXCHLrrnCbPMqnj2%2FkwCmxwZAG9xVAP%2BqhKJ8CGPAZOpzqVRzVLL4daCbOrC%2FdSXGL3CM9zMa132FCS8qXRY5xKyRONQLgDbrnVDK1BrwPjX2x0VIiPU8SDuGS2qc4CbfNLG%2BsTz0V9uHSJf%2BMCsPdr1nZZPvKkHmM%2FFWIc%2BC1ilJ6EJK0NmAWtROIKxwJINCYQ8qiX2quu04R4Qlb1Siz6ZwVq8pq1PCb%2BctiBeB0ws4YA8eyaJ5lW%2BUUP71oqjKbwpkbo5zyDTxu9OpgsLGhiL4CYGnPbQlJj6B%2B%2FMjbxo%2FHW8T0TUPzxQnxcG2QKFDkOw9YB%2BpGSvO6HwE1KnyhFtvEzssKA06FBmnFYKM176NaovAzShZ1VIrf%2F0DgpSNKKLloQ0oOi6xijxKKkbfeQVeq0%2FJcX2ckgHmoXbMrAXcGkuZ7zFU8yUcW2%2FXJ09Q6AOKxlb8uCN4auQhEbhJHOuUGHUsqT2jN5lUfpnknMAHdasgR3MDNF3GH0OURlQVVsPj0cYpILAhYquQi3QzwAoN0836wBu6aTgyjmas7N%2BPIWo99kV0%2FlMoDJ3D%2Bo%2BQgkfJaMskCsLhPGmrU6xtdQtrv1QUMm0%2FwrZLWziTDiuJS9BjqkAWfgwCh2fWaPMGC4%2Fn4HfdYaj0cxu%2Fwi4oxf5ufhsZHU0WOU92%2B%2BRUEpHV5iErFYn0%2BaqzvXZqXdXgknCwvRFjHAvgzIrHEGei8b%2BLfjxNZ0x%2Bnm1flQc8IHDojvnDo1VOi3nxtycpB8GoqJSaoLmiAONCIc3zDvkUCb3ulO0h%2F4RHAsNV4VGMSfCryewbcnkGGXnsh9LBxVRlmkIul%2Fv6fRMwkX&X-Amz-Signature=0ce1dd827aa8d54746f3f5ffd5dbf4aed070cc84d3763510fd7da55172170a7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


