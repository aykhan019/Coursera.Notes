

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q5NXY3C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIA7eAbYP7%2FGE%2B1hFVZjISF1v3SUlPw6nPI4miB7CuLIwAiEAi2QsKnkN4kI9EkttjnQFBe5%2FT5D%2FNVvVhwZnQJEFCP8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJTPZlrgNcZruzsTjircA1WKKClyrULVlpEC5757auP8wtmOLnfyjPNToH2MNrq8InJDC%2B7NmVsDqLMeYJUJwmzqkBW1oyqRZrynK%2FjahGheWufebaPwRxqIcvb44fmGRhV9l515gTFCgIi8D1jnPljgpFuH2G%2BoggFh%2BohcNyRCenLWXNEJsNnDwxoCUVQq0iARF1LBKg2nO5LNxiSvRGwb5h0I707oIhi6I4MUh7PhBBzxdvFgD6PBugECbq0R7bbz9lWw6s3JIAE8NR8XYns8DxynEB6zp8jZmHQa9ZvhYZiQ2nRmPhyHx3A1kvP77lT5W6bv2e5uuoiXX6U%2F2XST7432q4gPZp4tszrb1%2F84AbQKyInHetLLlb%2B0KUwbltdL6jXkrMxB77zos2JaCSXOR%2BCUVmX%2Bg8eu2kKnidOwd8M6TmoDtyMgFJqJbYwbO0nWnXtPchOG64L26hQ%2BytV8u3e4F%2B%2BfxY1glRsyead0GzD2LATZHzAmfQoV6pPucZatumW5dQshSeTytnlZL5tG0AcpmQQyUwz%2BiEy9GR8%2FIaAzOaeOLs4yF%2BZCc2gbBoFm%2Btdj5%2Fr0KEgbEAW1bbBB4%2BLFq0D%2F0Tb6j5sUcAiN%2Be1xFwHv0aKW1EVCHMVjhezYUmCVb53QRH0hMJLskb0GOqUBoR6aQrtBlVUMkNz6Tir4ljUcAqfB5YVvdVq%2B9Qq0fyO%2FXn%2FwJDXKrDyhNRXpvB87Sli%2FyEe2nYxNnZCn1%2FDHT%2BONegfaH0ZbKZmbEGKdDDdiv0MjDifHClx8sq2FdbLRqE1t%2FhwlcjIyEZuItFeUwXHXbVnNKYErr%2BmAqH%2BqY8uxX8vQDxqoh5zfY831%2BBhtLyjSSOzNIjaH9MtIF18bQPOvnfwG&X-Amz-Signature=a79d18a7b5829233e2100a5004a0b2c164d898ac54953b393988d522054e8373&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LEKYJZ2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIEaDAMR3jfakxdDAneVfo2mjQXDYOgDL%2BBDcQELEC%2B%2FOAiEA6lW4%2FFawZtMUez6iBrWcnmWswRFUpKf%2FKnF57CSMUlsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJLJv3HHwToh5NMdRircA43CapSAz3vdCybloumjNu3QzKo5WmWImCo2v2h0uvrViMxhOCf7QrqaROYIvoCY%2FLGw8QvcdSBozxEmhXQbFP0iPL4FkSlXVF6E0qOzRo5AyRsA99uvYKQ9rT1WHUaylUWiTigXyYQbn5Oqsc%2FIsExAiDqIprpiaqjxtwpwBhYQ69mfgMh8lEfGD%2FY%2FAD7HcZg9Rt6Ql2XVUFcwTqIQJl8qUHLwsX%2Fz%2BWP7ATap7JbMYtVk9kTfLZ1P3svrwM2GUKHYdswPCIpqdbjykMV7tsphMZhzkWYOZY%2F1760nOJnwMo7%2Bsw31SUYWVgeKYCfii6HVUFojfXAv93RVySQ4hBJDKuUD1sUoD5Rbvj11Zy%2F4cqaybCfUMb%2BH1zX95JkchrE980IA2yWXZ0umGAugASuyCA9g75dgLukQXQeQYTcZ0sVw6NR5NvZvKGpOIqKFug7C4psGEbeDn3sV3vdUSjzeoGYLBM5svMB5tCAVnZXsRlt%2ByBleS9Vr53ZMqlAV35ZccRLZwP0x%2FKL8UaN1wLyPfYDtytlYLSaL7kp0JXUCdTld6k4Rwn9BID4p8e7Chst8aBkVI8CllArpgMMmLYlDBfVgjhhnQxMv%2BmElX2O2qZFLYu2DZvf0EAiGMLPskb0GOqUBeS6Cwj3GdbB%2FW4Bi5t0ah%2FdpP1gFj6YP0bG4kSJb%2FuZ0qrqub5S0asW%2FsHvXO2DZKvJ9I3RDM8%2BNOMVLYu%2Fw2wi54mcMEPdU5T1gXWnSN26AzQuf%2Bxb9Z%2F6ktnhy8XQceQSDbDGIltv%2Byg0jCog3RUkJUoU1YaiOPT6x7TyJ8OYEKUvEQa%2FReiDS2FaPf5uykVKwSLJCMJ%2B5j0ILcnlSt3pbp0ke&X-Amz-Signature=42d094116de834258467127efdf227982c32e3917b54e91d4c587937feb18981&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LEKYJZ2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIEaDAMR3jfakxdDAneVfo2mjQXDYOgDL%2BBDcQELEC%2B%2FOAiEA6lW4%2FFawZtMUez6iBrWcnmWswRFUpKf%2FKnF57CSMUlsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJLJv3HHwToh5NMdRircA43CapSAz3vdCybloumjNu3QzKo5WmWImCo2v2h0uvrViMxhOCf7QrqaROYIvoCY%2FLGw8QvcdSBozxEmhXQbFP0iPL4FkSlXVF6E0qOzRo5AyRsA99uvYKQ9rT1WHUaylUWiTigXyYQbn5Oqsc%2FIsExAiDqIprpiaqjxtwpwBhYQ69mfgMh8lEfGD%2FY%2FAD7HcZg9Rt6Ql2XVUFcwTqIQJl8qUHLwsX%2Fz%2BWP7ATap7JbMYtVk9kTfLZ1P3svrwM2GUKHYdswPCIpqdbjykMV7tsphMZhzkWYOZY%2F1760nOJnwMo7%2Bsw31SUYWVgeKYCfii6HVUFojfXAv93RVySQ4hBJDKuUD1sUoD5Rbvj11Zy%2F4cqaybCfUMb%2BH1zX95JkchrE980IA2yWXZ0umGAugASuyCA9g75dgLukQXQeQYTcZ0sVw6NR5NvZvKGpOIqKFug7C4psGEbeDn3sV3vdUSjzeoGYLBM5svMB5tCAVnZXsRlt%2ByBleS9Vr53ZMqlAV35ZccRLZwP0x%2FKL8UaN1wLyPfYDtytlYLSaL7kp0JXUCdTld6k4Rwn9BID4p8e7Chst8aBkVI8CllArpgMMmLYlDBfVgjhhnQxMv%2BmElX2O2qZFLYu2DZvf0EAiGMLPskb0GOqUBeS6Cwj3GdbB%2FW4Bi5t0ah%2FdpP1gFj6YP0bG4kSJb%2FuZ0qrqub5S0asW%2FsHvXO2DZKvJ9I3RDM8%2BNOMVLYu%2Fw2wi54mcMEPdU5T1gXWnSN26AzQuf%2Bxb9Z%2F6ktnhy8XQceQSDbDGIltv%2Byg0jCog3RUkJUoU1YaiOPT6x7TyJ8OYEKUvEQa%2FReiDS2FaPf5uykVKwSLJCMJ%2B5j0ILcnlSt3pbp0ke&X-Amz-Signature=5296eb216e823e0564e64eaa84a6664bb365d5d2acf17ffe13b7935554855fbb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LEKYJZ2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIEaDAMR3jfakxdDAneVfo2mjQXDYOgDL%2BBDcQELEC%2B%2FOAiEA6lW4%2FFawZtMUez6iBrWcnmWswRFUpKf%2FKnF57CSMUlsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJLJv3HHwToh5NMdRircA43CapSAz3vdCybloumjNu3QzKo5WmWImCo2v2h0uvrViMxhOCf7QrqaROYIvoCY%2FLGw8QvcdSBozxEmhXQbFP0iPL4FkSlXVF6E0qOzRo5AyRsA99uvYKQ9rT1WHUaylUWiTigXyYQbn5Oqsc%2FIsExAiDqIprpiaqjxtwpwBhYQ69mfgMh8lEfGD%2FY%2FAD7HcZg9Rt6Ql2XVUFcwTqIQJl8qUHLwsX%2Fz%2BWP7ATap7JbMYtVk9kTfLZ1P3svrwM2GUKHYdswPCIpqdbjykMV7tsphMZhzkWYOZY%2F1760nOJnwMo7%2Bsw31SUYWVgeKYCfii6HVUFojfXAv93RVySQ4hBJDKuUD1sUoD5Rbvj11Zy%2F4cqaybCfUMb%2BH1zX95JkchrE980IA2yWXZ0umGAugASuyCA9g75dgLukQXQeQYTcZ0sVw6NR5NvZvKGpOIqKFug7C4psGEbeDn3sV3vdUSjzeoGYLBM5svMB5tCAVnZXsRlt%2ByBleS9Vr53ZMqlAV35ZccRLZwP0x%2FKL8UaN1wLyPfYDtytlYLSaL7kp0JXUCdTld6k4Rwn9BID4p8e7Chst8aBkVI8CllArpgMMmLYlDBfVgjhhnQxMv%2BmElX2O2qZFLYu2DZvf0EAiGMLPskb0GOqUBeS6Cwj3GdbB%2FW4Bi5t0ah%2FdpP1gFj6YP0bG4kSJb%2FuZ0qrqub5S0asW%2FsHvXO2DZKvJ9I3RDM8%2BNOMVLYu%2Fw2wi54mcMEPdU5T1gXWnSN26AzQuf%2Bxb9Z%2F6ktnhy8XQceQSDbDGIltv%2Byg0jCog3RUkJUoU1YaiOPT6x7TyJ8OYEKUvEQa%2FReiDS2FaPf5uykVKwSLJCMJ%2B5j0ILcnlSt3pbp0ke&X-Amz-Signature=65eb1310e0e21f3ffd9e0e7039dabfafce7b06b9c78e6b08aac5a1a632918ae0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LEKYJZ2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIEaDAMR3jfakxdDAneVfo2mjQXDYOgDL%2BBDcQELEC%2B%2FOAiEA6lW4%2FFawZtMUez6iBrWcnmWswRFUpKf%2FKnF57CSMUlsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJLJv3HHwToh5NMdRircA43CapSAz3vdCybloumjNu3QzKo5WmWImCo2v2h0uvrViMxhOCf7QrqaROYIvoCY%2FLGw8QvcdSBozxEmhXQbFP0iPL4FkSlXVF6E0qOzRo5AyRsA99uvYKQ9rT1WHUaylUWiTigXyYQbn5Oqsc%2FIsExAiDqIprpiaqjxtwpwBhYQ69mfgMh8lEfGD%2FY%2FAD7HcZg9Rt6Ql2XVUFcwTqIQJl8qUHLwsX%2Fz%2BWP7ATap7JbMYtVk9kTfLZ1P3svrwM2GUKHYdswPCIpqdbjykMV7tsphMZhzkWYOZY%2F1760nOJnwMo7%2Bsw31SUYWVgeKYCfii6HVUFojfXAv93RVySQ4hBJDKuUD1sUoD5Rbvj11Zy%2F4cqaybCfUMb%2BH1zX95JkchrE980IA2yWXZ0umGAugASuyCA9g75dgLukQXQeQYTcZ0sVw6NR5NvZvKGpOIqKFug7C4psGEbeDn3sV3vdUSjzeoGYLBM5svMB5tCAVnZXsRlt%2ByBleS9Vr53ZMqlAV35ZccRLZwP0x%2FKL8UaN1wLyPfYDtytlYLSaL7kp0JXUCdTld6k4Rwn9BID4p8e7Chst8aBkVI8CllArpgMMmLYlDBfVgjhhnQxMv%2BmElX2O2qZFLYu2DZvf0EAiGMLPskb0GOqUBeS6Cwj3GdbB%2FW4Bi5t0ah%2FdpP1gFj6YP0bG4kSJb%2FuZ0qrqub5S0asW%2FsHvXO2DZKvJ9I3RDM8%2BNOMVLYu%2Fw2wi54mcMEPdU5T1gXWnSN26AzQuf%2Bxb9Z%2F6ktnhy8XQceQSDbDGIltv%2Byg0jCog3RUkJUoU1YaiOPT6x7TyJ8OYEKUvEQa%2FReiDS2FaPf5uykVKwSLJCMJ%2B5j0ILcnlSt3pbp0ke&X-Amz-Signature=c27069aedb5ceb2be5d4f4996f7f3b5bd0fc7861e0b920a96fecb8a4a0398749&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LEKYJZ2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIEaDAMR3jfakxdDAneVfo2mjQXDYOgDL%2BBDcQELEC%2B%2FOAiEA6lW4%2FFawZtMUez6iBrWcnmWswRFUpKf%2FKnF57CSMUlsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJLJv3HHwToh5NMdRircA43CapSAz3vdCybloumjNu3QzKo5WmWImCo2v2h0uvrViMxhOCf7QrqaROYIvoCY%2FLGw8QvcdSBozxEmhXQbFP0iPL4FkSlXVF6E0qOzRo5AyRsA99uvYKQ9rT1WHUaylUWiTigXyYQbn5Oqsc%2FIsExAiDqIprpiaqjxtwpwBhYQ69mfgMh8lEfGD%2FY%2FAD7HcZg9Rt6Ql2XVUFcwTqIQJl8qUHLwsX%2Fz%2BWP7ATap7JbMYtVk9kTfLZ1P3svrwM2GUKHYdswPCIpqdbjykMV7tsphMZhzkWYOZY%2F1760nOJnwMo7%2Bsw31SUYWVgeKYCfii6HVUFojfXAv93RVySQ4hBJDKuUD1sUoD5Rbvj11Zy%2F4cqaybCfUMb%2BH1zX95JkchrE980IA2yWXZ0umGAugASuyCA9g75dgLukQXQeQYTcZ0sVw6NR5NvZvKGpOIqKFug7C4psGEbeDn3sV3vdUSjzeoGYLBM5svMB5tCAVnZXsRlt%2ByBleS9Vr53ZMqlAV35ZccRLZwP0x%2FKL8UaN1wLyPfYDtytlYLSaL7kp0JXUCdTld6k4Rwn9BID4p8e7Chst8aBkVI8CllArpgMMmLYlDBfVgjhhnQxMv%2BmElX2O2qZFLYu2DZvf0EAiGMLPskb0GOqUBeS6Cwj3GdbB%2FW4Bi5t0ah%2FdpP1gFj6YP0bG4kSJb%2FuZ0qrqub5S0asW%2FsHvXO2DZKvJ9I3RDM8%2BNOMVLYu%2Fw2wi54mcMEPdU5T1gXWnSN26AzQuf%2Bxb9Z%2F6ktnhy8XQceQSDbDGIltv%2Byg0jCog3RUkJUoU1YaiOPT6x7TyJ8OYEKUvEQa%2FReiDS2FaPf5uykVKwSLJCMJ%2B5j0ILcnlSt3pbp0ke&X-Amz-Signature=1dda6c4be7ff3c89a66d00470ad64e3e66621331ccc792b64e469bda8f2d5320&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q5NXY3C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIA7eAbYP7%2FGE%2B1hFVZjISF1v3SUlPw6nPI4miB7CuLIwAiEAi2QsKnkN4kI9EkttjnQFBe5%2FT5D%2FNVvVhwZnQJEFCP8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJTPZlrgNcZruzsTjircA1WKKClyrULVlpEC5757auP8wtmOLnfyjPNToH2MNrq8InJDC%2B7NmVsDqLMeYJUJwmzqkBW1oyqRZrynK%2FjahGheWufebaPwRxqIcvb44fmGRhV9l515gTFCgIi8D1jnPljgpFuH2G%2BoggFh%2BohcNyRCenLWXNEJsNnDwxoCUVQq0iARF1LBKg2nO5LNxiSvRGwb5h0I707oIhi6I4MUh7PhBBzxdvFgD6PBugECbq0R7bbz9lWw6s3JIAE8NR8XYns8DxynEB6zp8jZmHQa9ZvhYZiQ2nRmPhyHx3A1kvP77lT5W6bv2e5uuoiXX6U%2F2XST7432q4gPZp4tszrb1%2F84AbQKyInHetLLlb%2B0KUwbltdL6jXkrMxB77zos2JaCSXOR%2BCUVmX%2Bg8eu2kKnidOwd8M6TmoDtyMgFJqJbYwbO0nWnXtPchOG64L26hQ%2BytV8u3e4F%2B%2BfxY1glRsyead0GzD2LATZHzAmfQoV6pPucZatumW5dQshSeTytnlZL5tG0AcpmQQyUwz%2BiEy9GR8%2FIaAzOaeOLs4yF%2BZCc2gbBoFm%2Btdj5%2Fr0KEgbEAW1bbBB4%2BLFq0D%2F0Tb6j5sUcAiN%2Be1xFwHv0aKW1EVCHMVjhezYUmCVb53QRH0hMJLskb0GOqUBoR6aQrtBlVUMkNz6Tir4ljUcAqfB5YVvdVq%2B9Qq0fyO%2FXn%2FwJDXKrDyhNRXpvB87Sli%2FyEe2nYxNnZCn1%2FDHT%2BONegfaH0ZbKZmbEGKdDDdiv0MjDifHClx8sq2FdbLRqE1t%2FhwlcjIyEZuItFeUwXHXbVnNKYErr%2BmAqH%2BqY8uxX8vQDxqoh5zfY831%2BBhtLyjSSOzNIjaH9MtIF18bQPOvnfwG&X-Amz-Signature=6fff10d1a67b941b75ccf599a6ed53295285ff12e4176aa7837757c75ddbb7e4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q5NXY3C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIA7eAbYP7%2FGE%2B1hFVZjISF1v3SUlPw6nPI4miB7CuLIwAiEAi2QsKnkN4kI9EkttjnQFBe5%2FT5D%2FNVvVhwZnQJEFCP8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJTPZlrgNcZruzsTjircA1WKKClyrULVlpEC5757auP8wtmOLnfyjPNToH2MNrq8InJDC%2B7NmVsDqLMeYJUJwmzqkBW1oyqRZrynK%2FjahGheWufebaPwRxqIcvb44fmGRhV9l515gTFCgIi8D1jnPljgpFuH2G%2BoggFh%2BohcNyRCenLWXNEJsNnDwxoCUVQq0iARF1LBKg2nO5LNxiSvRGwb5h0I707oIhi6I4MUh7PhBBzxdvFgD6PBugECbq0R7bbz9lWw6s3JIAE8NR8XYns8DxynEB6zp8jZmHQa9ZvhYZiQ2nRmPhyHx3A1kvP77lT5W6bv2e5uuoiXX6U%2F2XST7432q4gPZp4tszrb1%2F84AbQKyInHetLLlb%2B0KUwbltdL6jXkrMxB77zos2JaCSXOR%2BCUVmX%2Bg8eu2kKnidOwd8M6TmoDtyMgFJqJbYwbO0nWnXtPchOG64L26hQ%2BytV8u3e4F%2B%2BfxY1glRsyead0GzD2LATZHzAmfQoV6pPucZatumW5dQshSeTytnlZL5tG0AcpmQQyUwz%2BiEy9GR8%2FIaAzOaeOLs4yF%2BZCc2gbBoFm%2Btdj5%2Fr0KEgbEAW1bbBB4%2BLFq0D%2F0Tb6j5sUcAiN%2Be1xFwHv0aKW1EVCHMVjhezYUmCVb53QRH0hMJLskb0GOqUBoR6aQrtBlVUMkNz6Tir4ljUcAqfB5YVvdVq%2B9Qq0fyO%2FXn%2FwJDXKrDyhNRXpvB87Sli%2FyEe2nYxNnZCn1%2FDHT%2BONegfaH0ZbKZmbEGKdDDdiv0MjDifHClx8sq2FdbLRqE1t%2FhwlcjIyEZuItFeUwXHXbVnNKYErr%2BmAqH%2BqY8uxX8vQDxqoh5zfY831%2BBhtLyjSSOzNIjaH9MtIF18bQPOvnfwG&X-Amz-Signature=06ab683b900f2b8b9a2f5721ff6b281f508d790eb212f1f21c54b39b13ad1ecf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q5NXY3C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIA7eAbYP7%2FGE%2B1hFVZjISF1v3SUlPw6nPI4miB7CuLIwAiEAi2QsKnkN4kI9EkttjnQFBe5%2FT5D%2FNVvVhwZnQJEFCP8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJTPZlrgNcZruzsTjircA1WKKClyrULVlpEC5757auP8wtmOLnfyjPNToH2MNrq8InJDC%2B7NmVsDqLMeYJUJwmzqkBW1oyqRZrynK%2FjahGheWufebaPwRxqIcvb44fmGRhV9l515gTFCgIi8D1jnPljgpFuH2G%2BoggFh%2BohcNyRCenLWXNEJsNnDwxoCUVQq0iARF1LBKg2nO5LNxiSvRGwb5h0I707oIhi6I4MUh7PhBBzxdvFgD6PBugECbq0R7bbz9lWw6s3JIAE8NR8XYns8DxynEB6zp8jZmHQa9ZvhYZiQ2nRmPhyHx3A1kvP77lT5W6bv2e5uuoiXX6U%2F2XST7432q4gPZp4tszrb1%2F84AbQKyInHetLLlb%2B0KUwbltdL6jXkrMxB77zos2JaCSXOR%2BCUVmX%2Bg8eu2kKnidOwd8M6TmoDtyMgFJqJbYwbO0nWnXtPchOG64L26hQ%2BytV8u3e4F%2B%2BfxY1glRsyead0GzD2LATZHzAmfQoV6pPucZatumW5dQshSeTytnlZL5tG0AcpmQQyUwz%2BiEy9GR8%2FIaAzOaeOLs4yF%2BZCc2gbBoFm%2Btdj5%2Fr0KEgbEAW1bbBB4%2BLFq0D%2F0Tb6j5sUcAiN%2Be1xFwHv0aKW1EVCHMVjhezYUmCVb53QRH0hMJLskb0GOqUBoR6aQrtBlVUMkNz6Tir4ljUcAqfB5YVvdVq%2B9Qq0fyO%2FXn%2FwJDXKrDyhNRXpvB87Sli%2FyEe2nYxNnZCn1%2FDHT%2BONegfaH0ZbKZmbEGKdDDdiv0MjDifHClx8sq2FdbLRqE1t%2FhwlcjIyEZuItFeUwXHXbVnNKYErr%2BmAqH%2BqY8uxX8vQDxqoh5zfY831%2BBhtLyjSSOzNIjaH9MtIF18bQPOvnfwG&X-Amz-Signature=6ae3d5e7bc57385b4f2d91b4d437c22d5a71f6a37a2b4bc0c186774aa39a4bdc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q5NXY3C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIA7eAbYP7%2FGE%2B1hFVZjISF1v3SUlPw6nPI4miB7CuLIwAiEAi2QsKnkN4kI9EkttjnQFBe5%2FT5D%2FNVvVhwZnQJEFCP8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJTPZlrgNcZruzsTjircA1WKKClyrULVlpEC5757auP8wtmOLnfyjPNToH2MNrq8InJDC%2B7NmVsDqLMeYJUJwmzqkBW1oyqRZrynK%2FjahGheWufebaPwRxqIcvb44fmGRhV9l515gTFCgIi8D1jnPljgpFuH2G%2BoggFh%2BohcNyRCenLWXNEJsNnDwxoCUVQq0iARF1LBKg2nO5LNxiSvRGwb5h0I707oIhi6I4MUh7PhBBzxdvFgD6PBugECbq0R7bbz9lWw6s3JIAE8NR8XYns8DxynEB6zp8jZmHQa9ZvhYZiQ2nRmPhyHx3A1kvP77lT5W6bv2e5uuoiXX6U%2F2XST7432q4gPZp4tszrb1%2F84AbQKyInHetLLlb%2B0KUwbltdL6jXkrMxB77zos2JaCSXOR%2BCUVmX%2Bg8eu2kKnidOwd8M6TmoDtyMgFJqJbYwbO0nWnXtPchOG64L26hQ%2BytV8u3e4F%2B%2BfxY1glRsyead0GzD2LATZHzAmfQoV6pPucZatumW5dQshSeTytnlZL5tG0AcpmQQyUwz%2BiEy9GR8%2FIaAzOaeOLs4yF%2BZCc2gbBoFm%2Btdj5%2Fr0KEgbEAW1bbBB4%2BLFq0D%2F0Tb6j5sUcAiN%2Be1xFwHv0aKW1EVCHMVjhezYUmCVb53QRH0hMJLskb0GOqUBoR6aQrtBlVUMkNz6Tir4ljUcAqfB5YVvdVq%2B9Qq0fyO%2FXn%2FwJDXKrDyhNRXpvB87Sli%2FyEe2nYxNnZCn1%2FDHT%2BONegfaH0ZbKZmbEGKdDDdiv0MjDifHClx8sq2FdbLRqE1t%2FhwlcjIyEZuItFeUwXHXbVnNKYErr%2BmAqH%2BqY8uxX8vQDxqoh5zfY831%2BBhtLyjSSOzNIjaH9MtIF18bQPOvnfwG&X-Amz-Signature=651895a06de2bc79bd253671c315b1828a1e6d6f20cbe7d98fdd92b6c7eea3ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q5NXY3C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIA7eAbYP7%2FGE%2B1hFVZjISF1v3SUlPw6nPI4miB7CuLIwAiEAi2QsKnkN4kI9EkttjnQFBe5%2FT5D%2FNVvVhwZnQJEFCP8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJTPZlrgNcZruzsTjircA1WKKClyrULVlpEC5757auP8wtmOLnfyjPNToH2MNrq8InJDC%2B7NmVsDqLMeYJUJwmzqkBW1oyqRZrynK%2FjahGheWufebaPwRxqIcvb44fmGRhV9l515gTFCgIi8D1jnPljgpFuH2G%2BoggFh%2BohcNyRCenLWXNEJsNnDwxoCUVQq0iARF1LBKg2nO5LNxiSvRGwb5h0I707oIhi6I4MUh7PhBBzxdvFgD6PBugECbq0R7bbz9lWw6s3JIAE8NR8XYns8DxynEB6zp8jZmHQa9ZvhYZiQ2nRmPhyHx3A1kvP77lT5W6bv2e5uuoiXX6U%2F2XST7432q4gPZp4tszrb1%2F84AbQKyInHetLLlb%2B0KUwbltdL6jXkrMxB77zos2JaCSXOR%2BCUVmX%2Bg8eu2kKnidOwd8M6TmoDtyMgFJqJbYwbO0nWnXtPchOG64L26hQ%2BytV8u3e4F%2B%2BfxY1glRsyead0GzD2LATZHzAmfQoV6pPucZatumW5dQshSeTytnlZL5tG0AcpmQQyUwz%2BiEy9GR8%2FIaAzOaeOLs4yF%2BZCc2gbBoFm%2Btdj5%2Fr0KEgbEAW1bbBB4%2BLFq0D%2F0Tb6j5sUcAiN%2Be1xFwHv0aKW1EVCHMVjhezYUmCVb53QRH0hMJLskb0GOqUBoR6aQrtBlVUMkNz6Tir4ljUcAqfB5YVvdVq%2B9Qq0fyO%2FXn%2FwJDXKrDyhNRXpvB87Sli%2FyEe2nYxNnZCn1%2FDHT%2BONegfaH0ZbKZmbEGKdDDdiv0MjDifHClx8sq2FdbLRqE1t%2FhwlcjIyEZuItFeUwXHXbVnNKYErr%2BmAqH%2BqY8uxX8vQDxqoh5zfY831%2BBhtLyjSSOzNIjaH9MtIF18bQPOvnfwG&X-Amz-Signature=e68855389c946002ada773fbd867f6514508d075034630c4e860f1319a170804&X-Amz-SignedHeaders=host&x-id=GetObject)
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


