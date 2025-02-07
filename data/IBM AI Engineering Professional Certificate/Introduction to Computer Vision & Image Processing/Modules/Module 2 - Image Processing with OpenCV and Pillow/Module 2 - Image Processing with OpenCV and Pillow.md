

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ336FGJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDh28ONX3wASDwKSs3LMAw7P3bptykBM6%2FuLfcDH8x7gwIgbAGDZbxsjf2uBlmsgKkULkPUoNsuYSG%2FrQZIlJAV3R8q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDGFEW1dEKVll%2BiRtYSrcA8elKNC4EXdlM%2F2D7OGA8M7mtxlJL37c8vNJh7Yxzd2ZxThNiihZhdXa0H61vuVsu5mk2ZYb%2B9HkBovnZfoEV7%2FsBoCDPJGD3KUDiyBYoWXIqyoslNBG8fJdVnAa9ojsW%2FXkKvk%2FGv8%2BFLip4rF5rtEOyMf0jh1mpHMYxTFxjudu2hc2AUs%2BlbEbFqK3SlhGj2Xc2ew8toSCddglmZ2wEIP5CdOokZ7Ibc4QhbgzVzM%2FPC2o%2FghCn%2BqaitmUiVuIBGbUdMvShuRcmFbTopJ1tNQ5jGbi7u2FNyW2XZVw7xNhu73UMcBHQbc2VqqEdOxyUOPQZVE0pYb%2BTX0AA0f8L2fkVW71dDk982wnFilE5sTt5Qv5b%2FKJM03BgKpR74xyUm%2ByE2MftIoqP3IeWmNdLqNR9dLVB6Z7EJnr92CiamQEknTTB1%2BgUjcb%2BkBIuHmklJ1ZTRohzux1PqT3o3pmbtc5fCRZmEYtZ9aS8Uofx8jAEwspikTpdkDbfse3zir7cyXs0fppTc7Q9%2B1Gw81%2Bq%2FtVOI1glGXKrwOPg6kF%2F2rrHLDPDv%2BksYbQPjxtLDfgU95WMChre6Uu%2B9ERQAoCbgwBHE5wyv1muAqmxVRrGaDPs9X1GaPTaV6gNxsYMOv5lr0GOqUB5gI1LfrrcHsNYaHkQSAFaZuc6dHwUrZoU5Cj1XtUFR8w0f1ZV3xB8%2B1ZxZvGgUKSTrBITPynMBD4uVLXg5DuNSkNfWzwkwpRX4WkLI96e9RicnuW7Eoeu%2Fvn2QF%2FJaDVLp8BE7aecTzadrOAHivxCOlyq1NroVqva1U8lE5TeG6NrX9l7z5JsmBneiXuGHrRqLJeDRkb0oQsz8SZtwEuCo0tAky0&X-Amz-Signature=9c8e55981e38676918291557a3096a00ce501eeec0b794f4caafd609c8e34a2b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PX4U4WJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIHxtSdh9M0xewXZfhDrUZcEtcD3jMVrviKwFK4Kj3NsJAiEAsNRCiZyu8F9%2BIax7lBoqltdnCEOc6yj0zCK927CBG0Iq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKAdGPDwem%2Fey6MKKircA6yIKe%2BuQilwuf6gJNpfCPmV5CskeAtE9NUsgxN2Rz2gKO0u3V6wj%2BdIX45Sda7uJ2RQ9SAi0Bub0gzF9gJeq97aeltoL4kG7U04iOBZGwS29kGnwWuIgM9UHsn1arSWvns6cMnSlAuGRGB6JUtD29suk%2BwmgHI3fhVha0iHqPFM7M1j1gWwSQ9%2FBojEcrY4Dfy9yXmzimFkPhCySQFhY7MBzVMuXYOKRL%2FrqTawj9p705i%2FVf4vpnr1RYf0Pkahv1MOPGNfYDMiTuvXAGLHm3lDckLtbIYcgvUJMoQuyxgvpKYiGRQ%2Bc84x6ey6ktptupPYcYw7L27wWIMSPEUxshpFyzTXIZvSTYe1oIJL6e7dFHawzxxyyX%2Fa8i4NClXnyN6p%2FPSnQ0FED05X1ISEECpaoG66AJwANXhCuQU%2FKt1%2BT%2BnYobrjbxLwXUqTJL2deQJnVWKAZDMPDI78jy4n8st1TQXEjZ0LlvA8WuuiDyzv4pU7GtIDwp2ITXTi75xaXchu1g0gwfpEqlBuXtMza3DOEPfhvLcRqPSdS4SCaxVO5fFjkrOcz4mFmcwdrsAjzxAChnn0iJoNi93yCNp8HYI5igK11NRMxCex3FLQCw%2FpQyXY6Cb%2F7MjVjGowMIv6lr0GOqUBdx8IoaD1YH8D1RUp4w57BZF3IOJ%2FKB7eKRoUbzZ%2BG5IlHZWb%2FHi71LTtifmhYD6Nx%2B61UnSBlU7vXppX1Bp2uP9mHePlzrhnQaB%2Fy84NQj5pQoTIw%2FSpXVxQmQcgw9VbqEvc2eU9Gla%2Bgn%2FekTlcQgnQHJuCeudqEL5xTXZsh0tKtnaXr0XHCxQn6y5zwEfiDFH1iXiBG0drgKWpywQwF8bNfEW0&X-Amz-Signature=7074679ad164238217b5b6461f46df7295f3b0524e0dd4aab9ad4038a690fe30&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PX4U4WJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIHxtSdh9M0xewXZfhDrUZcEtcD3jMVrviKwFK4Kj3NsJAiEAsNRCiZyu8F9%2BIax7lBoqltdnCEOc6yj0zCK927CBG0Iq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKAdGPDwem%2Fey6MKKircA6yIKe%2BuQilwuf6gJNpfCPmV5CskeAtE9NUsgxN2Rz2gKO0u3V6wj%2BdIX45Sda7uJ2RQ9SAi0Bub0gzF9gJeq97aeltoL4kG7U04iOBZGwS29kGnwWuIgM9UHsn1arSWvns6cMnSlAuGRGB6JUtD29suk%2BwmgHI3fhVha0iHqPFM7M1j1gWwSQ9%2FBojEcrY4Dfy9yXmzimFkPhCySQFhY7MBzVMuXYOKRL%2FrqTawj9p705i%2FVf4vpnr1RYf0Pkahv1MOPGNfYDMiTuvXAGLHm3lDckLtbIYcgvUJMoQuyxgvpKYiGRQ%2Bc84x6ey6ktptupPYcYw7L27wWIMSPEUxshpFyzTXIZvSTYe1oIJL6e7dFHawzxxyyX%2Fa8i4NClXnyN6p%2FPSnQ0FED05X1ISEECpaoG66AJwANXhCuQU%2FKt1%2BT%2BnYobrjbxLwXUqTJL2deQJnVWKAZDMPDI78jy4n8st1TQXEjZ0LlvA8WuuiDyzv4pU7GtIDwp2ITXTi75xaXchu1g0gwfpEqlBuXtMza3DOEPfhvLcRqPSdS4SCaxVO5fFjkrOcz4mFmcwdrsAjzxAChnn0iJoNi93yCNp8HYI5igK11NRMxCex3FLQCw%2FpQyXY6Cb%2F7MjVjGowMIv6lr0GOqUBdx8IoaD1YH8D1RUp4w57BZF3IOJ%2FKB7eKRoUbzZ%2BG5IlHZWb%2FHi71LTtifmhYD6Nx%2B61UnSBlU7vXppX1Bp2uP9mHePlzrhnQaB%2Fy84NQj5pQoTIw%2FSpXVxQmQcgw9VbqEvc2eU9Gla%2Bgn%2FekTlcQgnQHJuCeudqEL5xTXZsh0tKtnaXr0XHCxQn6y5zwEfiDFH1iXiBG0drgKWpywQwF8bNfEW0&X-Amz-Signature=69f0ce85a950f5a70951397110a64b2972bc1c467a0ba50a4a6cc94425527fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PX4U4WJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIHxtSdh9M0xewXZfhDrUZcEtcD3jMVrviKwFK4Kj3NsJAiEAsNRCiZyu8F9%2BIax7lBoqltdnCEOc6yj0zCK927CBG0Iq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKAdGPDwem%2Fey6MKKircA6yIKe%2BuQilwuf6gJNpfCPmV5CskeAtE9NUsgxN2Rz2gKO0u3V6wj%2BdIX45Sda7uJ2RQ9SAi0Bub0gzF9gJeq97aeltoL4kG7U04iOBZGwS29kGnwWuIgM9UHsn1arSWvns6cMnSlAuGRGB6JUtD29suk%2BwmgHI3fhVha0iHqPFM7M1j1gWwSQ9%2FBojEcrY4Dfy9yXmzimFkPhCySQFhY7MBzVMuXYOKRL%2FrqTawj9p705i%2FVf4vpnr1RYf0Pkahv1MOPGNfYDMiTuvXAGLHm3lDckLtbIYcgvUJMoQuyxgvpKYiGRQ%2Bc84x6ey6ktptupPYcYw7L27wWIMSPEUxshpFyzTXIZvSTYe1oIJL6e7dFHawzxxyyX%2Fa8i4NClXnyN6p%2FPSnQ0FED05X1ISEECpaoG66AJwANXhCuQU%2FKt1%2BT%2BnYobrjbxLwXUqTJL2deQJnVWKAZDMPDI78jy4n8st1TQXEjZ0LlvA8WuuiDyzv4pU7GtIDwp2ITXTi75xaXchu1g0gwfpEqlBuXtMza3DOEPfhvLcRqPSdS4SCaxVO5fFjkrOcz4mFmcwdrsAjzxAChnn0iJoNi93yCNp8HYI5igK11NRMxCex3FLQCw%2FpQyXY6Cb%2F7MjVjGowMIv6lr0GOqUBdx8IoaD1YH8D1RUp4w57BZF3IOJ%2FKB7eKRoUbzZ%2BG5IlHZWb%2FHi71LTtifmhYD6Nx%2B61UnSBlU7vXppX1Bp2uP9mHePlzrhnQaB%2Fy84NQj5pQoTIw%2FSpXVxQmQcgw9VbqEvc2eU9Gla%2Bgn%2FekTlcQgnQHJuCeudqEL5xTXZsh0tKtnaXr0XHCxQn6y5zwEfiDFH1iXiBG0drgKWpywQwF8bNfEW0&X-Amz-Signature=104aee5efebe92db2d61cc7673be64b5ffeb65721aebe13fa1ce40ccb1b8218b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PX4U4WJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIHxtSdh9M0xewXZfhDrUZcEtcD3jMVrviKwFK4Kj3NsJAiEAsNRCiZyu8F9%2BIax7lBoqltdnCEOc6yj0zCK927CBG0Iq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKAdGPDwem%2Fey6MKKircA6yIKe%2BuQilwuf6gJNpfCPmV5CskeAtE9NUsgxN2Rz2gKO0u3V6wj%2BdIX45Sda7uJ2RQ9SAi0Bub0gzF9gJeq97aeltoL4kG7U04iOBZGwS29kGnwWuIgM9UHsn1arSWvns6cMnSlAuGRGB6JUtD29suk%2BwmgHI3fhVha0iHqPFM7M1j1gWwSQ9%2FBojEcrY4Dfy9yXmzimFkPhCySQFhY7MBzVMuXYOKRL%2FrqTawj9p705i%2FVf4vpnr1RYf0Pkahv1MOPGNfYDMiTuvXAGLHm3lDckLtbIYcgvUJMoQuyxgvpKYiGRQ%2Bc84x6ey6ktptupPYcYw7L27wWIMSPEUxshpFyzTXIZvSTYe1oIJL6e7dFHawzxxyyX%2Fa8i4NClXnyN6p%2FPSnQ0FED05X1ISEECpaoG66AJwANXhCuQU%2FKt1%2BT%2BnYobrjbxLwXUqTJL2deQJnVWKAZDMPDI78jy4n8st1TQXEjZ0LlvA8WuuiDyzv4pU7GtIDwp2ITXTi75xaXchu1g0gwfpEqlBuXtMza3DOEPfhvLcRqPSdS4SCaxVO5fFjkrOcz4mFmcwdrsAjzxAChnn0iJoNi93yCNp8HYI5igK11NRMxCex3FLQCw%2FpQyXY6Cb%2F7MjVjGowMIv6lr0GOqUBdx8IoaD1YH8D1RUp4w57BZF3IOJ%2FKB7eKRoUbzZ%2BG5IlHZWb%2FHi71LTtifmhYD6Nx%2B61UnSBlU7vXppX1Bp2uP9mHePlzrhnQaB%2Fy84NQj5pQoTIw%2FSpXVxQmQcgw9VbqEvc2eU9Gla%2Bgn%2FekTlcQgnQHJuCeudqEL5xTXZsh0tKtnaXr0XHCxQn6y5zwEfiDFH1iXiBG0drgKWpywQwF8bNfEW0&X-Amz-Signature=708f9d9c471824af859d2e15bd7db2f9de7de8ffb2883ef6d229c709e4e73f2d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PX4U4WJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIHxtSdh9M0xewXZfhDrUZcEtcD3jMVrviKwFK4Kj3NsJAiEAsNRCiZyu8F9%2BIax7lBoqltdnCEOc6yj0zCK927CBG0Iq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKAdGPDwem%2Fey6MKKircA6yIKe%2BuQilwuf6gJNpfCPmV5CskeAtE9NUsgxN2Rz2gKO0u3V6wj%2BdIX45Sda7uJ2RQ9SAi0Bub0gzF9gJeq97aeltoL4kG7U04iOBZGwS29kGnwWuIgM9UHsn1arSWvns6cMnSlAuGRGB6JUtD29suk%2BwmgHI3fhVha0iHqPFM7M1j1gWwSQ9%2FBojEcrY4Dfy9yXmzimFkPhCySQFhY7MBzVMuXYOKRL%2FrqTawj9p705i%2FVf4vpnr1RYf0Pkahv1MOPGNfYDMiTuvXAGLHm3lDckLtbIYcgvUJMoQuyxgvpKYiGRQ%2Bc84x6ey6ktptupPYcYw7L27wWIMSPEUxshpFyzTXIZvSTYe1oIJL6e7dFHawzxxyyX%2Fa8i4NClXnyN6p%2FPSnQ0FED05X1ISEECpaoG66AJwANXhCuQU%2FKt1%2BT%2BnYobrjbxLwXUqTJL2deQJnVWKAZDMPDI78jy4n8st1TQXEjZ0LlvA8WuuiDyzv4pU7GtIDwp2ITXTi75xaXchu1g0gwfpEqlBuXtMza3DOEPfhvLcRqPSdS4SCaxVO5fFjkrOcz4mFmcwdrsAjzxAChnn0iJoNi93yCNp8HYI5igK11NRMxCex3FLQCw%2FpQyXY6Cb%2F7MjVjGowMIv6lr0GOqUBdx8IoaD1YH8D1RUp4w57BZF3IOJ%2FKB7eKRoUbzZ%2BG5IlHZWb%2FHi71LTtifmhYD6Nx%2B61UnSBlU7vXppX1Bp2uP9mHePlzrhnQaB%2Fy84NQj5pQoTIw%2FSpXVxQmQcgw9VbqEvc2eU9Gla%2Bgn%2FekTlcQgnQHJuCeudqEL5xTXZsh0tKtnaXr0XHCxQn6y5zwEfiDFH1iXiBG0drgKWpywQwF8bNfEW0&X-Amz-Signature=3391de76e829972b81495df7178af006f8c79cb7ecd9d8d2cffde9794a065ed4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ336FGJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDh28ONX3wASDwKSs3LMAw7P3bptykBM6%2FuLfcDH8x7gwIgbAGDZbxsjf2uBlmsgKkULkPUoNsuYSG%2FrQZIlJAV3R8q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDGFEW1dEKVll%2BiRtYSrcA8elKNC4EXdlM%2F2D7OGA8M7mtxlJL37c8vNJh7Yxzd2ZxThNiihZhdXa0H61vuVsu5mk2ZYb%2B9HkBovnZfoEV7%2FsBoCDPJGD3KUDiyBYoWXIqyoslNBG8fJdVnAa9ojsW%2FXkKvk%2FGv8%2BFLip4rF5rtEOyMf0jh1mpHMYxTFxjudu2hc2AUs%2BlbEbFqK3SlhGj2Xc2ew8toSCddglmZ2wEIP5CdOokZ7Ibc4QhbgzVzM%2FPC2o%2FghCn%2BqaitmUiVuIBGbUdMvShuRcmFbTopJ1tNQ5jGbi7u2FNyW2XZVw7xNhu73UMcBHQbc2VqqEdOxyUOPQZVE0pYb%2BTX0AA0f8L2fkVW71dDk982wnFilE5sTt5Qv5b%2FKJM03BgKpR74xyUm%2ByE2MftIoqP3IeWmNdLqNR9dLVB6Z7EJnr92CiamQEknTTB1%2BgUjcb%2BkBIuHmklJ1ZTRohzux1PqT3o3pmbtc5fCRZmEYtZ9aS8Uofx8jAEwspikTpdkDbfse3zir7cyXs0fppTc7Q9%2B1Gw81%2Bq%2FtVOI1glGXKrwOPg6kF%2F2rrHLDPDv%2BksYbQPjxtLDfgU95WMChre6Uu%2B9ERQAoCbgwBHE5wyv1muAqmxVRrGaDPs9X1GaPTaV6gNxsYMOv5lr0GOqUB5gI1LfrrcHsNYaHkQSAFaZuc6dHwUrZoU5Cj1XtUFR8w0f1ZV3xB8%2B1ZxZvGgUKSTrBITPynMBD4uVLXg5DuNSkNfWzwkwpRX4WkLI96e9RicnuW7Eoeu%2Fvn2QF%2FJaDVLp8BE7aecTzadrOAHivxCOlyq1NroVqva1U8lE5TeG6NrX9l7z5JsmBneiXuGHrRqLJeDRkb0oQsz8SZtwEuCo0tAky0&X-Amz-Signature=884c20c99870f0d3663acf05309a90069d5b0c53c9cbf6e730234634e6417f57&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ336FGJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDh28ONX3wASDwKSs3LMAw7P3bptykBM6%2FuLfcDH8x7gwIgbAGDZbxsjf2uBlmsgKkULkPUoNsuYSG%2FrQZIlJAV3R8q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDGFEW1dEKVll%2BiRtYSrcA8elKNC4EXdlM%2F2D7OGA8M7mtxlJL37c8vNJh7Yxzd2ZxThNiihZhdXa0H61vuVsu5mk2ZYb%2B9HkBovnZfoEV7%2FsBoCDPJGD3KUDiyBYoWXIqyoslNBG8fJdVnAa9ojsW%2FXkKvk%2FGv8%2BFLip4rF5rtEOyMf0jh1mpHMYxTFxjudu2hc2AUs%2BlbEbFqK3SlhGj2Xc2ew8toSCddglmZ2wEIP5CdOokZ7Ibc4QhbgzVzM%2FPC2o%2FghCn%2BqaitmUiVuIBGbUdMvShuRcmFbTopJ1tNQ5jGbi7u2FNyW2XZVw7xNhu73UMcBHQbc2VqqEdOxyUOPQZVE0pYb%2BTX0AA0f8L2fkVW71dDk982wnFilE5sTt5Qv5b%2FKJM03BgKpR74xyUm%2ByE2MftIoqP3IeWmNdLqNR9dLVB6Z7EJnr92CiamQEknTTB1%2BgUjcb%2BkBIuHmklJ1ZTRohzux1PqT3o3pmbtc5fCRZmEYtZ9aS8Uofx8jAEwspikTpdkDbfse3zir7cyXs0fppTc7Q9%2B1Gw81%2Bq%2FtVOI1glGXKrwOPg6kF%2F2rrHLDPDv%2BksYbQPjxtLDfgU95WMChre6Uu%2B9ERQAoCbgwBHE5wyv1muAqmxVRrGaDPs9X1GaPTaV6gNxsYMOv5lr0GOqUB5gI1LfrrcHsNYaHkQSAFaZuc6dHwUrZoU5Cj1XtUFR8w0f1ZV3xB8%2B1ZxZvGgUKSTrBITPynMBD4uVLXg5DuNSkNfWzwkwpRX4WkLI96e9RicnuW7Eoeu%2Fvn2QF%2FJaDVLp8BE7aecTzadrOAHivxCOlyq1NroVqva1U8lE5TeG6NrX9l7z5JsmBneiXuGHrRqLJeDRkb0oQsz8SZtwEuCo0tAky0&X-Amz-Signature=2801973a632edf7be30ce0f47ef46f90294a0ba4f4e15ad7fc1764f0fee85e3e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ336FGJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDh28ONX3wASDwKSs3LMAw7P3bptykBM6%2FuLfcDH8x7gwIgbAGDZbxsjf2uBlmsgKkULkPUoNsuYSG%2FrQZIlJAV3R8q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDGFEW1dEKVll%2BiRtYSrcA8elKNC4EXdlM%2F2D7OGA8M7mtxlJL37c8vNJh7Yxzd2ZxThNiihZhdXa0H61vuVsu5mk2ZYb%2B9HkBovnZfoEV7%2FsBoCDPJGD3KUDiyBYoWXIqyoslNBG8fJdVnAa9ojsW%2FXkKvk%2FGv8%2BFLip4rF5rtEOyMf0jh1mpHMYxTFxjudu2hc2AUs%2BlbEbFqK3SlhGj2Xc2ew8toSCddglmZ2wEIP5CdOokZ7Ibc4QhbgzVzM%2FPC2o%2FghCn%2BqaitmUiVuIBGbUdMvShuRcmFbTopJ1tNQ5jGbi7u2FNyW2XZVw7xNhu73UMcBHQbc2VqqEdOxyUOPQZVE0pYb%2BTX0AA0f8L2fkVW71dDk982wnFilE5sTt5Qv5b%2FKJM03BgKpR74xyUm%2ByE2MftIoqP3IeWmNdLqNR9dLVB6Z7EJnr92CiamQEknTTB1%2BgUjcb%2BkBIuHmklJ1ZTRohzux1PqT3o3pmbtc5fCRZmEYtZ9aS8Uofx8jAEwspikTpdkDbfse3zir7cyXs0fppTc7Q9%2B1Gw81%2Bq%2FtVOI1glGXKrwOPg6kF%2F2rrHLDPDv%2BksYbQPjxtLDfgU95WMChre6Uu%2B9ERQAoCbgwBHE5wyv1muAqmxVRrGaDPs9X1GaPTaV6gNxsYMOv5lr0GOqUB5gI1LfrrcHsNYaHkQSAFaZuc6dHwUrZoU5Cj1XtUFR8w0f1ZV3xB8%2B1ZxZvGgUKSTrBITPynMBD4uVLXg5DuNSkNfWzwkwpRX4WkLI96e9RicnuW7Eoeu%2Fvn2QF%2FJaDVLp8BE7aecTzadrOAHivxCOlyq1NroVqva1U8lE5TeG6NrX9l7z5JsmBneiXuGHrRqLJeDRkb0oQsz8SZtwEuCo0tAky0&X-Amz-Signature=4c2da73687c492690726ea3d1830209b150bd0e67a360af7e581107a416a4b07&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ336FGJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDh28ONX3wASDwKSs3LMAw7P3bptykBM6%2FuLfcDH8x7gwIgbAGDZbxsjf2uBlmsgKkULkPUoNsuYSG%2FrQZIlJAV3R8q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDGFEW1dEKVll%2BiRtYSrcA8elKNC4EXdlM%2F2D7OGA8M7mtxlJL37c8vNJh7Yxzd2ZxThNiihZhdXa0H61vuVsu5mk2ZYb%2B9HkBovnZfoEV7%2FsBoCDPJGD3KUDiyBYoWXIqyoslNBG8fJdVnAa9ojsW%2FXkKvk%2FGv8%2BFLip4rF5rtEOyMf0jh1mpHMYxTFxjudu2hc2AUs%2BlbEbFqK3SlhGj2Xc2ew8toSCddglmZ2wEIP5CdOokZ7Ibc4QhbgzVzM%2FPC2o%2FghCn%2BqaitmUiVuIBGbUdMvShuRcmFbTopJ1tNQ5jGbi7u2FNyW2XZVw7xNhu73UMcBHQbc2VqqEdOxyUOPQZVE0pYb%2BTX0AA0f8L2fkVW71dDk982wnFilE5sTt5Qv5b%2FKJM03BgKpR74xyUm%2ByE2MftIoqP3IeWmNdLqNR9dLVB6Z7EJnr92CiamQEknTTB1%2BgUjcb%2BkBIuHmklJ1ZTRohzux1PqT3o3pmbtc5fCRZmEYtZ9aS8Uofx8jAEwspikTpdkDbfse3zir7cyXs0fppTc7Q9%2B1Gw81%2Bq%2FtVOI1glGXKrwOPg6kF%2F2rrHLDPDv%2BksYbQPjxtLDfgU95WMChre6Uu%2B9ERQAoCbgwBHE5wyv1muAqmxVRrGaDPs9X1GaPTaV6gNxsYMOv5lr0GOqUB5gI1LfrrcHsNYaHkQSAFaZuc6dHwUrZoU5Cj1XtUFR8w0f1ZV3xB8%2B1ZxZvGgUKSTrBITPynMBD4uVLXg5DuNSkNfWzwkwpRX4WkLI96e9RicnuW7Eoeu%2Fvn2QF%2FJaDVLp8BE7aecTzadrOAHivxCOlyq1NroVqva1U8lE5TeG6NrX9l7z5JsmBneiXuGHrRqLJeDRkb0oQsz8SZtwEuCo0tAky0&X-Amz-Signature=7db55292b124a34321219c95653d4528e69dae9d53367caabd9c611f73ad5687&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ336FGJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDh28ONX3wASDwKSs3LMAw7P3bptykBM6%2FuLfcDH8x7gwIgbAGDZbxsjf2uBlmsgKkULkPUoNsuYSG%2FrQZIlJAV3R8q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDGFEW1dEKVll%2BiRtYSrcA8elKNC4EXdlM%2F2D7OGA8M7mtxlJL37c8vNJh7Yxzd2ZxThNiihZhdXa0H61vuVsu5mk2ZYb%2B9HkBovnZfoEV7%2FsBoCDPJGD3KUDiyBYoWXIqyoslNBG8fJdVnAa9ojsW%2FXkKvk%2FGv8%2BFLip4rF5rtEOyMf0jh1mpHMYxTFxjudu2hc2AUs%2BlbEbFqK3SlhGj2Xc2ew8toSCddglmZ2wEIP5CdOokZ7Ibc4QhbgzVzM%2FPC2o%2FghCn%2BqaitmUiVuIBGbUdMvShuRcmFbTopJ1tNQ5jGbi7u2FNyW2XZVw7xNhu73UMcBHQbc2VqqEdOxyUOPQZVE0pYb%2BTX0AA0f8L2fkVW71dDk982wnFilE5sTt5Qv5b%2FKJM03BgKpR74xyUm%2ByE2MftIoqP3IeWmNdLqNR9dLVB6Z7EJnr92CiamQEknTTB1%2BgUjcb%2BkBIuHmklJ1ZTRohzux1PqT3o3pmbtc5fCRZmEYtZ9aS8Uofx8jAEwspikTpdkDbfse3zir7cyXs0fppTc7Q9%2B1Gw81%2Bq%2FtVOI1glGXKrwOPg6kF%2F2rrHLDPDv%2BksYbQPjxtLDfgU95WMChre6Uu%2B9ERQAoCbgwBHE5wyv1muAqmxVRrGaDPs9X1GaPTaV6gNxsYMOv5lr0GOqUB5gI1LfrrcHsNYaHkQSAFaZuc6dHwUrZoU5Cj1XtUFR8w0f1ZV3xB8%2B1ZxZvGgUKSTrBITPynMBD4uVLXg5DuNSkNfWzwkwpRX4WkLI96e9RicnuW7Eoeu%2Fvn2QF%2FJaDVLp8BE7aecTzadrOAHivxCOlyq1NroVqva1U8lE5TeG6NrX9l7z5JsmBneiXuGHrRqLJeDRkb0oQsz8SZtwEuCo0tAky0&X-Amz-Signature=91b5bac14fb207f4fcbdf0c2c3b97765edb4c2ea913f6e621585378c6b04c36f&X-Amz-SignedHeaders=host&x-id=GetObject)
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


