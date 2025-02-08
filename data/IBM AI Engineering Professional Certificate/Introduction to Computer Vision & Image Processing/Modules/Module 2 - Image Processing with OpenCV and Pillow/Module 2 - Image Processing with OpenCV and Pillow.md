

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSCY3PRI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCDNLjFRb423PnK2NCVW6ZnwzSi6kQbAu%2Brur3qJkbTMgIgCuLKrgroJlr7%2BWG14uNGBl0JjjkOf4Fq82I5dR1tzZIqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvXccP5xsc6FjTIuSrcA3F6mHoR6YMavwGAqaxRPiPwf4jAOGcteesW%2Bs2eRNhPxVa28nVjsb%2FMq8b2xEPBc1GK9TGteN%2FwXSa1KCROPhgVLPXqBweC4cmtxqG0KNA4vxXKX3PjCC5FfcIzxqMi8vdttPgDM9k%2BhS2HFMHI7zvEvDUWYgw9GTZngKeybLTuZnvu5hkO2W6ohyjZiqKXbBeud%2Fuoei8onPXROxomT9ncNC96OtvV6ZyMiMpxFgKMpmtNfJHFCvZN3slwY1%2FX3mrxjEszc5kI5N0Qn0vpLoRVX4QHMKZUL8Kft8zsau1OaQcMjHSG5EetVeea%2F4vWuvE3VHB63bisHmlU24KbazLhQmSYrjyp%2FUjVywtcfmxeM3WtSvuw%2FrGux0xPgEXMnrGkwGiBF3HIXIWc5g5Si%2F9dvacF%2Bu7D%2BskVOl7SzSAuOVTXl48BAUev31i3itERoA%2FQHurR19JNkPVAmrsq%2B8fcfMClC38jkRVeXb5fGtE9oq9tzuAXW1l4Mwh1uhntnYujTvUa34iL5qpqQ8pXLKjXicl3vgYnHAbPSMtt0oofhrJ12t7ZF35COfSwCfaSaBXrpc%2FyNjsopf1TVQ5CwK%2FzJZL4y9jbR4QsMh39ESoH9rqprCX9KMfGdTnQMJKFnb0GOqUBptjHCYNvrDXxXbwoZ4uNdEeATtRXRSEEZDH2Tw0Hmx8YkHslclOW90nlPfYD6BI0f1fM%2Fj1bKyhoq8kwA1ZI2kPWzG4FuuK2gH570L%2Bm4xIUh0vrFlZphZMs9RCzBcaMsmQ3xEqAKduuM1OCO34ELbT%2BX9xZu8A2j05%2FT11M15CGj%2Fd2zV5phjNltUWSGl2y96XoYV2S8mZwoF9DP0vtzSlJzSVD&X-Amz-Signature=01f1a6f64fa80f307a5d168d5c665fed38af8f9cd62f104fe66192f72646fe38&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBDCDBJ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCpNHsyNhO5jrqp94x2Rcrw%2BWM7hbZu2mHocFrdIsLWEwIgGdrApQFaMpH1F%2BJOC7KDjc9Hf9iA%2Bv8fQvSJUZdBIa4qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlBcQCBQ0x6tCudOyrcA33vVmDgakxQAldF8%2BqZndAqyGTEuiPP40ZqzwNzzr4FNf7irkzEqngNxcfBZDX%2BEb0qmoIjvcKl2YyjKjIwcjqd17lPaEg%2FlCxqux4kws3RdV%2B%2FmA1KMZQDGDYIUB0YyJR%2B1BnIud5MrpkbtOefwdUbBO4L0bvZlrwCmii0IMQOUOzZ0NQG1mGON7VN5fE8DHr0N%2F6JEU9H6wdVieZ92F1KyhWub7rM3GIfgFQAcX7l3AVDrFx4wR6YjqxvMzIIs0Ve1fPi9FfoRmFp9JOLQQA%2FnffLURAsm3YMZjqTFzcSNtaY0P%2FRBoObQd6J2lRD4bcj7wUa1f%2FhOvXjBUZZ1seUXndvJSOv%2BoqEx%2FP%2BmHtVsi5Awc1wEJSW2V6fXez2XjSDrjiQQZriv%2Floj0ncVnEHTtPOsVsQEfc7s0FfOZiEn0wvX4b03YbINuKnv4XVSe6Az7N3iQtRxh4oU1Zvg%2Fjp%2B8kbEp6CdkL7JXPeKgl4hkJsDaD4Jgs5naNbj8ldLgHRc34o8ihujRiMJHSc1S6zxnC15Q7jsnro3Hxp7Kb9nE2ferICa%2BSVRFMaDHzjD0AKg3vTZZWj5fBGrZ4fNPJDF712aTKdMbLvUuX%2Fu9RcPTOoa9%2FHjRmYQ7UNMKmFnb0GOqUBNpTnL1no2AJ0lCr6eQfK5b%2F9Zd6a9Q2F3iqowCMK1Cplip%2FcxxL6CWn3pdS5jEeswJHhxIQB63mKfVCM6wfjrIaPCacTGKfkAo%2FlLx6P0O%2BVr4kTgHhnDiuH%2FpFtoa4mm3Wdjsciw%2FnjtBp0JW4CykHUsQ9jRO3aPbkYVufHTFmTKvI5VbhJ3T%2Bx54CdTadcNjAKL917p0kTyzKe1hg2NK8muRlg&X-Amz-Signature=d2312e5b1bc3f64cd67385b9a9e23415957aaa1807f4eaafc86932c85ec1e72d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBDCDBJ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCpNHsyNhO5jrqp94x2Rcrw%2BWM7hbZu2mHocFrdIsLWEwIgGdrApQFaMpH1F%2BJOC7KDjc9Hf9iA%2Bv8fQvSJUZdBIa4qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlBcQCBQ0x6tCudOyrcA33vVmDgakxQAldF8%2BqZndAqyGTEuiPP40ZqzwNzzr4FNf7irkzEqngNxcfBZDX%2BEb0qmoIjvcKl2YyjKjIwcjqd17lPaEg%2FlCxqux4kws3RdV%2B%2FmA1KMZQDGDYIUB0YyJR%2B1BnIud5MrpkbtOefwdUbBO4L0bvZlrwCmii0IMQOUOzZ0NQG1mGON7VN5fE8DHr0N%2F6JEU9H6wdVieZ92F1KyhWub7rM3GIfgFQAcX7l3AVDrFx4wR6YjqxvMzIIs0Ve1fPi9FfoRmFp9JOLQQA%2FnffLURAsm3YMZjqTFzcSNtaY0P%2FRBoObQd6J2lRD4bcj7wUa1f%2FhOvXjBUZZ1seUXndvJSOv%2BoqEx%2FP%2BmHtVsi5Awc1wEJSW2V6fXez2XjSDrjiQQZriv%2Floj0ncVnEHTtPOsVsQEfc7s0FfOZiEn0wvX4b03YbINuKnv4XVSe6Az7N3iQtRxh4oU1Zvg%2Fjp%2B8kbEp6CdkL7JXPeKgl4hkJsDaD4Jgs5naNbj8ldLgHRc34o8ihujRiMJHSc1S6zxnC15Q7jsnro3Hxp7Kb9nE2ferICa%2BSVRFMaDHzjD0AKg3vTZZWj5fBGrZ4fNPJDF712aTKdMbLvUuX%2Fu9RcPTOoa9%2FHjRmYQ7UNMKmFnb0GOqUBNpTnL1no2AJ0lCr6eQfK5b%2F9Zd6a9Q2F3iqowCMK1Cplip%2FcxxL6CWn3pdS5jEeswJHhxIQB63mKfVCM6wfjrIaPCacTGKfkAo%2FlLx6P0O%2BVr4kTgHhnDiuH%2FpFtoa4mm3Wdjsciw%2FnjtBp0JW4CykHUsQ9jRO3aPbkYVufHTFmTKvI5VbhJ3T%2Bx54CdTadcNjAKL917p0kTyzKe1hg2NK8muRlg&X-Amz-Signature=763cee2e3651127533a57a10eaa404ea8a07f3c73c98ce658fd6f965d134ebc2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBDCDBJ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCpNHsyNhO5jrqp94x2Rcrw%2BWM7hbZu2mHocFrdIsLWEwIgGdrApQFaMpH1F%2BJOC7KDjc9Hf9iA%2Bv8fQvSJUZdBIa4qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlBcQCBQ0x6tCudOyrcA33vVmDgakxQAldF8%2BqZndAqyGTEuiPP40ZqzwNzzr4FNf7irkzEqngNxcfBZDX%2BEb0qmoIjvcKl2YyjKjIwcjqd17lPaEg%2FlCxqux4kws3RdV%2B%2FmA1KMZQDGDYIUB0YyJR%2B1BnIud5MrpkbtOefwdUbBO4L0bvZlrwCmii0IMQOUOzZ0NQG1mGON7VN5fE8DHr0N%2F6JEU9H6wdVieZ92F1KyhWub7rM3GIfgFQAcX7l3AVDrFx4wR6YjqxvMzIIs0Ve1fPi9FfoRmFp9JOLQQA%2FnffLURAsm3YMZjqTFzcSNtaY0P%2FRBoObQd6J2lRD4bcj7wUa1f%2FhOvXjBUZZ1seUXndvJSOv%2BoqEx%2FP%2BmHtVsi5Awc1wEJSW2V6fXez2XjSDrjiQQZriv%2Floj0ncVnEHTtPOsVsQEfc7s0FfOZiEn0wvX4b03YbINuKnv4XVSe6Az7N3iQtRxh4oU1Zvg%2Fjp%2B8kbEp6CdkL7JXPeKgl4hkJsDaD4Jgs5naNbj8ldLgHRc34o8ihujRiMJHSc1S6zxnC15Q7jsnro3Hxp7Kb9nE2ferICa%2BSVRFMaDHzjD0AKg3vTZZWj5fBGrZ4fNPJDF712aTKdMbLvUuX%2Fu9RcPTOoa9%2FHjRmYQ7UNMKmFnb0GOqUBNpTnL1no2AJ0lCr6eQfK5b%2F9Zd6a9Q2F3iqowCMK1Cplip%2FcxxL6CWn3pdS5jEeswJHhxIQB63mKfVCM6wfjrIaPCacTGKfkAo%2FlLx6P0O%2BVr4kTgHhnDiuH%2FpFtoa4mm3Wdjsciw%2FnjtBp0JW4CykHUsQ9jRO3aPbkYVufHTFmTKvI5VbhJ3T%2Bx54CdTadcNjAKL917p0kTyzKe1hg2NK8muRlg&X-Amz-Signature=5375f97d3a7ecb33606367dd014227b3242cfb9481ae4d8e47eb5fe25edd7775&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBDCDBJ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCpNHsyNhO5jrqp94x2Rcrw%2BWM7hbZu2mHocFrdIsLWEwIgGdrApQFaMpH1F%2BJOC7KDjc9Hf9iA%2Bv8fQvSJUZdBIa4qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlBcQCBQ0x6tCudOyrcA33vVmDgakxQAldF8%2BqZndAqyGTEuiPP40ZqzwNzzr4FNf7irkzEqngNxcfBZDX%2BEb0qmoIjvcKl2YyjKjIwcjqd17lPaEg%2FlCxqux4kws3RdV%2B%2FmA1KMZQDGDYIUB0YyJR%2B1BnIud5MrpkbtOefwdUbBO4L0bvZlrwCmii0IMQOUOzZ0NQG1mGON7VN5fE8DHr0N%2F6JEU9H6wdVieZ92F1KyhWub7rM3GIfgFQAcX7l3AVDrFx4wR6YjqxvMzIIs0Ve1fPi9FfoRmFp9JOLQQA%2FnffLURAsm3YMZjqTFzcSNtaY0P%2FRBoObQd6J2lRD4bcj7wUa1f%2FhOvXjBUZZ1seUXndvJSOv%2BoqEx%2FP%2BmHtVsi5Awc1wEJSW2V6fXez2XjSDrjiQQZriv%2Floj0ncVnEHTtPOsVsQEfc7s0FfOZiEn0wvX4b03YbINuKnv4XVSe6Az7N3iQtRxh4oU1Zvg%2Fjp%2B8kbEp6CdkL7JXPeKgl4hkJsDaD4Jgs5naNbj8ldLgHRc34o8ihujRiMJHSc1S6zxnC15Q7jsnro3Hxp7Kb9nE2ferICa%2BSVRFMaDHzjD0AKg3vTZZWj5fBGrZ4fNPJDF712aTKdMbLvUuX%2Fu9RcPTOoa9%2FHjRmYQ7UNMKmFnb0GOqUBNpTnL1no2AJ0lCr6eQfK5b%2F9Zd6a9Q2F3iqowCMK1Cplip%2FcxxL6CWn3pdS5jEeswJHhxIQB63mKfVCM6wfjrIaPCacTGKfkAo%2FlLx6P0O%2BVr4kTgHhnDiuH%2FpFtoa4mm3Wdjsciw%2FnjtBp0JW4CykHUsQ9jRO3aPbkYVufHTFmTKvI5VbhJ3T%2Bx54CdTadcNjAKL917p0kTyzKe1hg2NK8muRlg&X-Amz-Signature=cb3642950ef5d344c86ec005a7e3a337f01e0a4fefe6b409d52acc563b878f9a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBDCDBJ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCpNHsyNhO5jrqp94x2Rcrw%2BWM7hbZu2mHocFrdIsLWEwIgGdrApQFaMpH1F%2BJOC7KDjc9Hf9iA%2Bv8fQvSJUZdBIa4qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlBcQCBQ0x6tCudOyrcA33vVmDgakxQAldF8%2BqZndAqyGTEuiPP40ZqzwNzzr4FNf7irkzEqngNxcfBZDX%2BEb0qmoIjvcKl2YyjKjIwcjqd17lPaEg%2FlCxqux4kws3RdV%2B%2FmA1KMZQDGDYIUB0YyJR%2B1BnIud5MrpkbtOefwdUbBO4L0bvZlrwCmii0IMQOUOzZ0NQG1mGON7VN5fE8DHr0N%2F6JEU9H6wdVieZ92F1KyhWub7rM3GIfgFQAcX7l3AVDrFx4wR6YjqxvMzIIs0Ve1fPi9FfoRmFp9JOLQQA%2FnffLURAsm3YMZjqTFzcSNtaY0P%2FRBoObQd6J2lRD4bcj7wUa1f%2FhOvXjBUZZ1seUXndvJSOv%2BoqEx%2FP%2BmHtVsi5Awc1wEJSW2V6fXez2XjSDrjiQQZriv%2Floj0ncVnEHTtPOsVsQEfc7s0FfOZiEn0wvX4b03YbINuKnv4XVSe6Az7N3iQtRxh4oU1Zvg%2Fjp%2B8kbEp6CdkL7JXPeKgl4hkJsDaD4Jgs5naNbj8ldLgHRc34o8ihujRiMJHSc1S6zxnC15Q7jsnro3Hxp7Kb9nE2ferICa%2BSVRFMaDHzjD0AKg3vTZZWj5fBGrZ4fNPJDF712aTKdMbLvUuX%2Fu9RcPTOoa9%2FHjRmYQ7UNMKmFnb0GOqUBNpTnL1no2AJ0lCr6eQfK5b%2F9Zd6a9Q2F3iqowCMK1Cplip%2FcxxL6CWn3pdS5jEeswJHhxIQB63mKfVCM6wfjrIaPCacTGKfkAo%2FlLx6P0O%2BVr4kTgHhnDiuH%2FpFtoa4mm3Wdjsciw%2FnjtBp0JW4CykHUsQ9jRO3aPbkYVufHTFmTKvI5VbhJ3T%2Bx54CdTadcNjAKL917p0kTyzKe1hg2NK8muRlg&X-Amz-Signature=078ef8afd0969c6a37f281c94aebcf278cd61f803344df4dbe3fb68f63a94f5e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSCY3PRI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCDNLjFRb423PnK2NCVW6ZnwzSi6kQbAu%2Brur3qJkbTMgIgCuLKrgroJlr7%2BWG14uNGBl0JjjkOf4Fq82I5dR1tzZIqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvXccP5xsc6FjTIuSrcA3F6mHoR6YMavwGAqaxRPiPwf4jAOGcteesW%2Bs2eRNhPxVa28nVjsb%2FMq8b2xEPBc1GK9TGteN%2FwXSa1KCROPhgVLPXqBweC4cmtxqG0KNA4vxXKX3PjCC5FfcIzxqMi8vdttPgDM9k%2BhS2HFMHI7zvEvDUWYgw9GTZngKeybLTuZnvu5hkO2W6ohyjZiqKXbBeud%2Fuoei8onPXROxomT9ncNC96OtvV6ZyMiMpxFgKMpmtNfJHFCvZN3slwY1%2FX3mrxjEszc5kI5N0Qn0vpLoRVX4QHMKZUL8Kft8zsau1OaQcMjHSG5EetVeea%2F4vWuvE3VHB63bisHmlU24KbazLhQmSYrjyp%2FUjVywtcfmxeM3WtSvuw%2FrGux0xPgEXMnrGkwGiBF3HIXIWc5g5Si%2F9dvacF%2Bu7D%2BskVOl7SzSAuOVTXl48BAUev31i3itERoA%2FQHurR19JNkPVAmrsq%2B8fcfMClC38jkRVeXb5fGtE9oq9tzuAXW1l4Mwh1uhntnYujTvUa34iL5qpqQ8pXLKjXicl3vgYnHAbPSMtt0oofhrJ12t7ZF35COfSwCfaSaBXrpc%2FyNjsopf1TVQ5CwK%2FzJZL4y9jbR4QsMh39ESoH9rqprCX9KMfGdTnQMJKFnb0GOqUBptjHCYNvrDXxXbwoZ4uNdEeATtRXRSEEZDH2Tw0Hmx8YkHslclOW90nlPfYD6BI0f1fM%2Fj1bKyhoq8kwA1ZI2kPWzG4FuuK2gH570L%2Bm4xIUh0vrFlZphZMs9RCzBcaMsmQ3xEqAKduuM1OCO34ELbT%2BX9xZu8A2j05%2FT11M15CGj%2Fd2zV5phjNltUWSGl2y96XoYV2S8mZwoF9DP0vtzSlJzSVD&X-Amz-Signature=42cdf5755a85bcc58eac55558ae114f30acedc07e02e1024d4e735333b837cba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSCY3PRI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCDNLjFRb423PnK2NCVW6ZnwzSi6kQbAu%2Brur3qJkbTMgIgCuLKrgroJlr7%2BWG14uNGBl0JjjkOf4Fq82I5dR1tzZIqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvXccP5xsc6FjTIuSrcA3F6mHoR6YMavwGAqaxRPiPwf4jAOGcteesW%2Bs2eRNhPxVa28nVjsb%2FMq8b2xEPBc1GK9TGteN%2FwXSa1KCROPhgVLPXqBweC4cmtxqG0KNA4vxXKX3PjCC5FfcIzxqMi8vdttPgDM9k%2BhS2HFMHI7zvEvDUWYgw9GTZngKeybLTuZnvu5hkO2W6ohyjZiqKXbBeud%2Fuoei8onPXROxomT9ncNC96OtvV6ZyMiMpxFgKMpmtNfJHFCvZN3slwY1%2FX3mrxjEszc5kI5N0Qn0vpLoRVX4QHMKZUL8Kft8zsau1OaQcMjHSG5EetVeea%2F4vWuvE3VHB63bisHmlU24KbazLhQmSYrjyp%2FUjVywtcfmxeM3WtSvuw%2FrGux0xPgEXMnrGkwGiBF3HIXIWc5g5Si%2F9dvacF%2Bu7D%2BskVOl7SzSAuOVTXl48BAUev31i3itERoA%2FQHurR19JNkPVAmrsq%2B8fcfMClC38jkRVeXb5fGtE9oq9tzuAXW1l4Mwh1uhntnYujTvUa34iL5qpqQ8pXLKjXicl3vgYnHAbPSMtt0oofhrJ12t7ZF35COfSwCfaSaBXrpc%2FyNjsopf1TVQ5CwK%2FzJZL4y9jbR4QsMh39ESoH9rqprCX9KMfGdTnQMJKFnb0GOqUBptjHCYNvrDXxXbwoZ4uNdEeATtRXRSEEZDH2Tw0Hmx8YkHslclOW90nlPfYD6BI0f1fM%2Fj1bKyhoq8kwA1ZI2kPWzG4FuuK2gH570L%2Bm4xIUh0vrFlZphZMs9RCzBcaMsmQ3xEqAKduuM1OCO34ELbT%2BX9xZu8A2j05%2FT11M15CGj%2Fd2zV5phjNltUWSGl2y96XoYV2S8mZwoF9DP0vtzSlJzSVD&X-Amz-Signature=90db92b698d5a2de169d5901ed1606add927c5fdb5f47154c92d744dc1625114&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSCY3PRI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCDNLjFRb423PnK2NCVW6ZnwzSi6kQbAu%2Brur3qJkbTMgIgCuLKrgroJlr7%2BWG14uNGBl0JjjkOf4Fq82I5dR1tzZIqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvXccP5xsc6FjTIuSrcA3F6mHoR6YMavwGAqaxRPiPwf4jAOGcteesW%2Bs2eRNhPxVa28nVjsb%2FMq8b2xEPBc1GK9TGteN%2FwXSa1KCROPhgVLPXqBweC4cmtxqG0KNA4vxXKX3PjCC5FfcIzxqMi8vdttPgDM9k%2BhS2HFMHI7zvEvDUWYgw9GTZngKeybLTuZnvu5hkO2W6ohyjZiqKXbBeud%2Fuoei8onPXROxomT9ncNC96OtvV6ZyMiMpxFgKMpmtNfJHFCvZN3slwY1%2FX3mrxjEszc5kI5N0Qn0vpLoRVX4QHMKZUL8Kft8zsau1OaQcMjHSG5EetVeea%2F4vWuvE3VHB63bisHmlU24KbazLhQmSYrjyp%2FUjVywtcfmxeM3WtSvuw%2FrGux0xPgEXMnrGkwGiBF3HIXIWc5g5Si%2F9dvacF%2Bu7D%2BskVOl7SzSAuOVTXl48BAUev31i3itERoA%2FQHurR19JNkPVAmrsq%2B8fcfMClC38jkRVeXb5fGtE9oq9tzuAXW1l4Mwh1uhntnYujTvUa34iL5qpqQ8pXLKjXicl3vgYnHAbPSMtt0oofhrJ12t7ZF35COfSwCfaSaBXrpc%2FyNjsopf1TVQ5CwK%2FzJZL4y9jbR4QsMh39ESoH9rqprCX9KMfGdTnQMJKFnb0GOqUBptjHCYNvrDXxXbwoZ4uNdEeATtRXRSEEZDH2Tw0Hmx8YkHslclOW90nlPfYD6BI0f1fM%2Fj1bKyhoq8kwA1ZI2kPWzG4FuuK2gH570L%2Bm4xIUh0vrFlZphZMs9RCzBcaMsmQ3xEqAKduuM1OCO34ELbT%2BX9xZu8A2j05%2FT11M15CGj%2Fd2zV5phjNltUWSGl2y96XoYV2S8mZwoF9DP0vtzSlJzSVD&X-Amz-Signature=cad7140a5a475d876adeb87a264f309e5d7cf24139ffcc0ee11b51eb01b3bbaf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSCY3PRI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCDNLjFRb423PnK2NCVW6ZnwzSi6kQbAu%2Brur3qJkbTMgIgCuLKrgroJlr7%2BWG14uNGBl0JjjkOf4Fq82I5dR1tzZIqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvXccP5xsc6FjTIuSrcA3F6mHoR6YMavwGAqaxRPiPwf4jAOGcteesW%2Bs2eRNhPxVa28nVjsb%2FMq8b2xEPBc1GK9TGteN%2FwXSa1KCROPhgVLPXqBweC4cmtxqG0KNA4vxXKX3PjCC5FfcIzxqMi8vdttPgDM9k%2BhS2HFMHI7zvEvDUWYgw9GTZngKeybLTuZnvu5hkO2W6ohyjZiqKXbBeud%2Fuoei8onPXROxomT9ncNC96OtvV6ZyMiMpxFgKMpmtNfJHFCvZN3slwY1%2FX3mrxjEszc5kI5N0Qn0vpLoRVX4QHMKZUL8Kft8zsau1OaQcMjHSG5EetVeea%2F4vWuvE3VHB63bisHmlU24KbazLhQmSYrjyp%2FUjVywtcfmxeM3WtSvuw%2FrGux0xPgEXMnrGkwGiBF3HIXIWc5g5Si%2F9dvacF%2Bu7D%2BskVOl7SzSAuOVTXl48BAUev31i3itERoA%2FQHurR19JNkPVAmrsq%2B8fcfMClC38jkRVeXb5fGtE9oq9tzuAXW1l4Mwh1uhntnYujTvUa34iL5qpqQ8pXLKjXicl3vgYnHAbPSMtt0oofhrJ12t7ZF35COfSwCfaSaBXrpc%2FyNjsopf1TVQ5CwK%2FzJZL4y9jbR4QsMh39ESoH9rqprCX9KMfGdTnQMJKFnb0GOqUBptjHCYNvrDXxXbwoZ4uNdEeATtRXRSEEZDH2Tw0Hmx8YkHslclOW90nlPfYD6BI0f1fM%2Fj1bKyhoq8kwA1ZI2kPWzG4FuuK2gH570L%2Bm4xIUh0vrFlZphZMs9RCzBcaMsmQ3xEqAKduuM1OCO34ELbT%2BX9xZu8A2j05%2FT11M15CGj%2Fd2zV5phjNltUWSGl2y96XoYV2S8mZwoF9DP0vtzSlJzSVD&X-Amz-Signature=3ac65b2301abb93765ddcf7a474a1c3a388afaeeee4ea117a687a6344d3ff6c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSCY3PRI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCDNLjFRb423PnK2NCVW6ZnwzSi6kQbAu%2Brur3qJkbTMgIgCuLKrgroJlr7%2BWG14uNGBl0JjjkOf4Fq82I5dR1tzZIqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvXccP5xsc6FjTIuSrcA3F6mHoR6YMavwGAqaxRPiPwf4jAOGcteesW%2Bs2eRNhPxVa28nVjsb%2FMq8b2xEPBc1GK9TGteN%2FwXSa1KCROPhgVLPXqBweC4cmtxqG0KNA4vxXKX3PjCC5FfcIzxqMi8vdttPgDM9k%2BhS2HFMHI7zvEvDUWYgw9GTZngKeybLTuZnvu5hkO2W6ohyjZiqKXbBeud%2Fuoei8onPXROxomT9ncNC96OtvV6ZyMiMpxFgKMpmtNfJHFCvZN3slwY1%2FX3mrxjEszc5kI5N0Qn0vpLoRVX4QHMKZUL8Kft8zsau1OaQcMjHSG5EetVeea%2F4vWuvE3VHB63bisHmlU24KbazLhQmSYrjyp%2FUjVywtcfmxeM3WtSvuw%2FrGux0xPgEXMnrGkwGiBF3HIXIWc5g5Si%2F9dvacF%2Bu7D%2BskVOl7SzSAuOVTXl48BAUev31i3itERoA%2FQHurR19JNkPVAmrsq%2B8fcfMClC38jkRVeXb5fGtE9oq9tzuAXW1l4Mwh1uhntnYujTvUa34iL5qpqQ8pXLKjXicl3vgYnHAbPSMtt0oofhrJ12t7ZF35COfSwCfaSaBXrpc%2FyNjsopf1TVQ5CwK%2FzJZL4y9jbR4QsMh39ESoH9rqprCX9KMfGdTnQMJKFnb0GOqUBptjHCYNvrDXxXbwoZ4uNdEeATtRXRSEEZDH2Tw0Hmx8YkHslclOW90nlPfYD6BI0f1fM%2Fj1bKyhoq8kwA1ZI2kPWzG4FuuK2gH570L%2Bm4xIUh0vrFlZphZMs9RCzBcaMsmQ3xEqAKduuM1OCO34ELbT%2BX9xZu8A2j05%2FT11M15CGj%2Fd2zV5phjNltUWSGl2y96XoYV2S8mZwoF9DP0vtzSlJzSVD&X-Amz-Signature=e3ea0b46e5736a88a7adb866d96e2c98b738cb8c17f7acf34e4f39682d264257&X-Amz-SignedHeaders=host&x-id=GetObject)
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


