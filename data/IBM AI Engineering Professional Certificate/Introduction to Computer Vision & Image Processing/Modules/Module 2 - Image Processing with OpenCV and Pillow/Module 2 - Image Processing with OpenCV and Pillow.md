

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSMA7J2G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIArLln%2B1FPJjx8sAi0goeQaCVVUyBtxHTqveCYHVPAbyAiBBpS2f8g4kyjFHKPTG%2BGyCvwlgzDcCCADhNhvLx0DcDCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMptksCtxr2mQAWi6dKtwDrh0zoBMZBMk2Y9ZfKRHMQ6Kts4QbbZd2X5%2BhwBT1R79FV8htIUKc698HYnS%2B74TyBNGn9Ni%2BjoFSLV%2FxEJ3ny3X8MsLjMITxQ%2BpAoVUYLjY07Kofh%2Fu68gXybvGlK5mF6cgzSUNduQ8E233zCoCOxyiLteVtqJgFS7iXTV5QKvbGKrvJLCcMvp6NnEUxh3zhbzkApLiLo2c3t%2BsvmTMESNUuHBUjiPdaiXciJpCm8xfXj3TnFv2IavrZWu5muM3litOucK0i9mWNZ3Ys9iDZf0CZDI%2FD0%2BaGhm%2FHiA%2Bwak6dcXfhkSQNqGsKjlRxvSZkLFE1kBus840jCt62jWGPnVR74y9gncv7HW9V9fUyOCbxTvyUzswDyNaArWaXfjqqWYVeAPlQBeIyf92RfxTxDaY%2BE8gAW89uwhYkH7Vp%2B5rvGsx5%2FOEEZ9ijnZGNjcSNpeCXDsYKVdttSnfSdVYptKH4t5aGIdrUQ33J9Olk9gMD8zceOiEDfqFtbD0%2BPdRbNI4GUxfY%2B2ff4dViYN0EUgNLp7eI3%2BRY%2B3t2DgGmHoVRvlcvWjyDGmp0jRt3LGubdEgs8l1vpYezK78cVsZoPC0NJhiRr49RMjccbA%2B6eZuNaSBawIKuwnDA5Dsw%2FbqOvQY6pgFG91c9ai1i0rCqzcVYlPiW4I%2F8uDyXS4gAgDNujbnAO%2FsvXpU55hkS9hc9SHcWaVCiANPeY5WJ8hyvsT8IO4%2F%2FEw%2BhkcDWSll3p9i0Cd1%2BPPunVVhrwWww3wZrHZAWgnBe4gikIndVOH2FGmpt5SCP9yjavTn8SpmEv6VVgT41l8tJomN1z5%2FC9od4hAT1P42cC6cH3iSD0qVC0jOcBinen6wm7Duj&X-Amz-Signature=a368e9ad7e3af8bb419f3aa5dc9bfed153b57fb91c26d5dcb50b74ed0b6dd263&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGXEO7UQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIAY71yZhSdIiOykUKFZDVoGa4kEzeKdkaLY9YpS%2B5CNVAiEA5Shn7wKM39bKcglBpZjmoueMvGnfEGbgm%2BoIRjLdQHIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDIFxa4d2tTuLBPMZ8CrcA5AiJexVfX9ZcP8wqnUO1mHBCZNXc%2BrPRFhN3DnCdzNuicoK4zyA%2FUK9BfJ09cR%2BepWA%2FX6vdO3Ai706dTUnNMN%2BZT2HE4OLhlmyoXokmvvCRc1tfYYvmNC1bakuxhVDe1XlIcnJ%2FO5o8TVICe35uIkLC%2BxSMX7ytXidpOWq2SM645BHuK4EdgnViFT2ylvrYlawTVvGn00akQmuRXs1Y%2FEgklYR%2Bt65utdDxbXqhMO7cz9F2bt4Bpo98UN14gJ3oNCfDCkFJ1NO0R%2Bj0I%2FiYma9vq%2BdXB3hVhl4LJOX4VzPM1807%2BrM9hk3TTQuPhbu%2BGgZI%2F0E37vsa53mkrTqgUmZyU4X0uu67KfufhCI8rpfL1sf157kg2%2FWcdDluiC%2FAoNoe%2FFSRZ%2B1MEsA04ta%2BIUcCYiciYA6UYrmAG6s00GrYLgEWKLyqAX3yAynznVT0q6BeqSdojplq0zs1XGQ7CpQcUIqUaMJqHUxE84Mftmf5VksU4OFk%2F84xrPi%2F%2FdXP2fcOfHqf4kPgfTnj0zfRZpzpaFKZ3pfR0Cs7m4KWmk5mR6Vrn3RIC6nvTeIqFZthsEPLOTfUjyGckRlPOAn3yA5WxIjkV3OGGlFkbvcoMRRCRZ3UmBy7wF3COyeMKO6jr0GOqUB%2BPRpMUgvxnYl9oLXN9fg21k1OiHQ331f6XQ19lxct%2BR5ozp6gdj1Dy0SFF4cr%2F%2FY%2F7iEekl3Bnw%2FEzhCAUcOR09nDfWmC%2BwchQnxVBI1Cn7OGGpsVfpPEoFeVDl0dBNC%2FCoabsDAs39nu2%2BQLqNGE3UqAcWTXiMPahkEs9RJWytWsWz7tLQPGj3BLWgHybFm8ALYS6pmCeioM%2F8yXsZV9Ah0X1pg&X-Amz-Signature=efd5b1e594bc39f090f05f57951aaeb1ced00ddeecd1b5a9c91988c81947ba03&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGXEO7UQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIAY71yZhSdIiOykUKFZDVoGa4kEzeKdkaLY9YpS%2B5CNVAiEA5Shn7wKM39bKcglBpZjmoueMvGnfEGbgm%2BoIRjLdQHIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDIFxa4d2tTuLBPMZ8CrcA5AiJexVfX9ZcP8wqnUO1mHBCZNXc%2BrPRFhN3DnCdzNuicoK4zyA%2FUK9BfJ09cR%2BepWA%2FX6vdO3Ai706dTUnNMN%2BZT2HE4OLhlmyoXokmvvCRc1tfYYvmNC1bakuxhVDe1XlIcnJ%2FO5o8TVICe35uIkLC%2BxSMX7ytXidpOWq2SM645BHuK4EdgnViFT2ylvrYlawTVvGn00akQmuRXs1Y%2FEgklYR%2Bt65utdDxbXqhMO7cz9F2bt4Bpo98UN14gJ3oNCfDCkFJ1NO0R%2Bj0I%2FiYma9vq%2BdXB3hVhl4LJOX4VzPM1807%2BrM9hk3TTQuPhbu%2BGgZI%2F0E37vsa53mkrTqgUmZyU4X0uu67KfufhCI8rpfL1sf157kg2%2FWcdDluiC%2FAoNoe%2FFSRZ%2B1MEsA04ta%2BIUcCYiciYA6UYrmAG6s00GrYLgEWKLyqAX3yAynznVT0q6BeqSdojplq0zs1XGQ7CpQcUIqUaMJqHUxE84Mftmf5VksU4OFk%2F84xrPi%2F%2FdXP2fcOfHqf4kPgfTnj0zfRZpzpaFKZ3pfR0Cs7m4KWmk5mR6Vrn3RIC6nvTeIqFZthsEPLOTfUjyGckRlPOAn3yA5WxIjkV3OGGlFkbvcoMRRCRZ3UmBy7wF3COyeMKO6jr0GOqUB%2BPRpMUgvxnYl9oLXN9fg21k1OiHQ331f6XQ19lxct%2BR5ozp6gdj1Dy0SFF4cr%2F%2FY%2F7iEekl3Bnw%2FEzhCAUcOR09nDfWmC%2BwchQnxVBI1Cn7OGGpsVfpPEoFeVDl0dBNC%2FCoabsDAs39nu2%2BQLqNGE3UqAcWTXiMPahkEs9RJWytWsWz7tLQPGj3BLWgHybFm8ALYS6pmCeioM%2F8yXsZV9Ah0X1pg&X-Amz-Signature=cdffb35d74424256a2eb65a3206120a1931acf7c5c368206b406b2c0fb8956c3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGXEO7UQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIAY71yZhSdIiOykUKFZDVoGa4kEzeKdkaLY9YpS%2B5CNVAiEA5Shn7wKM39bKcglBpZjmoueMvGnfEGbgm%2BoIRjLdQHIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDIFxa4d2tTuLBPMZ8CrcA5AiJexVfX9ZcP8wqnUO1mHBCZNXc%2BrPRFhN3DnCdzNuicoK4zyA%2FUK9BfJ09cR%2BepWA%2FX6vdO3Ai706dTUnNMN%2BZT2HE4OLhlmyoXokmvvCRc1tfYYvmNC1bakuxhVDe1XlIcnJ%2FO5o8TVICe35uIkLC%2BxSMX7ytXidpOWq2SM645BHuK4EdgnViFT2ylvrYlawTVvGn00akQmuRXs1Y%2FEgklYR%2Bt65utdDxbXqhMO7cz9F2bt4Bpo98UN14gJ3oNCfDCkFJ1NO0R%2Bj0I%2FiYma9vq%2BdXB3hVhl4LJOX4VzPM1807%2BrM9hk3TTQuPhbu%2BGgZI%2F0E37vsa53mkrTqgUmZyU4X0uu67KfufhCI8rpfL1sf157kg2%2FWcdDluiC%2FAoNoe%2FFSRZ%2B1MEsA04ta%2BIUcCYiciYA6UYrmAG6s00GrYLgEWKLyqAX3yAynznVT0q6BeqSdojplq0zs1XGQ7CpQcUIqUaMJqHUxE84Mftmf5VksU4OFk%2F84xrPi%2F%2FdXP2fcOfHqf4kPgfTnj0zfRZpzpaFKZ3pfR0Cs7m4KWmk5mR6Vrn3RIC6nvTeIqFZthsEPLOTfUjyGckRlPOAn3yA5WxIjkV3OGGlFkbvcoMRRCRZ3UmBy7wF3COyeMKO6jr0GOqUB%2BPRpMUgvxnYl9oLXN9fg21k1OiHQ331f6XQ19lxct%2BR5ozp6gdj1Dy0SFF4cr%2F%2FY%2F7iEekl3Bnw%2FEzhCAUcOR09nDfWmC%2BwchQnxVBI1Cn7OGGpsVfpPEoFeVDl0dBNC%2FCoabsDAs39nu2%2BQLqNGE3UqAcWTXiMPahkEs9RJWytWsWz7tLQPGj3BLWgHybFm8ALYS6pmCeioM%2F8yXsZV9Ah0X1pg&X-Amz-Signature=d5d6600fd6c8b23fe5994b1f88f1c114412c40c64324a8fa3464ffba31c4ea1e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGXEO7UQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIAY71yZhSdIiOykUKFZDVoGa4kEzeKdkaLY9YpS%2B5CNVAiEA5Shn7wKM39bKcglBpZjmoueMvGnfEGbgm%2BoIRjLdQHIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDIFxa4d2tTuLBPMZ8CrcA5AiJexVfX9ZcP8wqnUO1mHBCZNXc%2BrPRFhN3DnCdzNuicoK4zyA%2FUK9BfJ09cR%2BepWA%2FX6vdO3Ai706dTUnNMN%2BZT2HE4OLhlmyoXokmvvCRc1tfYYvmNC1bakuxhVDe1XlIcnJ%2FO5o8TVICe35uIkLC%2BxSMX7ytXidpOWq2SM645BHuK4EdgnViFT2ylvrYlawTVvGn00akQmuRXs1Y%2FEgklYR%2Bt65utdDxbXqhMO7cz9F2bt4Bpo98UN14gJ3oNCfDCkFJ1NO0R%2Bj0I%2FiYma9vq%2BdXB3hVhl4LJOX4VzPM1807%2BrM9hk3TTQuPhbu%2BGgZI%2F0E37vsa53mkrTqgUmZyU4X0uu67KfufhCI8rpfL1sf157kg2%2FWcdDluiC%2FAoNoe%2FFSRZ%2B1MEsA04ta%2BIUcCYiciYA6UYrmAG6s00GrYLgEWKLyqAX3yAynznVT0q6BeqSdojplq0zs1XGQ7CpQcUIqUaMJqHUxE84Mftmf5VksU4OFk%2F84xrPi%2F%2FdXP2fcOfHqf4kPgfTnj0zfRZpzpaFKZ3pfR0Cs7m4KWmk5mR6Vrn3RIC6nvTeIqFZthsEPLOTfUjyGckRlPOAn3yA5WxIjkV3OGGlFkbvcoMRRCRZ3UmBy7wF3COyeMKO6jr0GOqUB%2BPRpMUgvxnYl9oLXN9fg21k1OiHQ331f6XQ19lxct%2BR5ozp6gdj1Dy0SFF4cr%2F%2FY%2F7iEekl3Bnw%2FEzhCAUcOR09nDfWmC%2BwchQnxVBI1Cn7OGGpsVfpPEoFeVDl0dBNC%2FCoabsDAs39nu2%2BQLqNGE3UqAcWTXiMPahkEs9RJWytWsWz7tLQPGj3BLWgHybFm8ALYS6pmCeioM%2F8yXsZV9Ah0X1pg&X-Amz-Signature=73974cd37949f1ff322bc0cbcc85c7b10eb0549bac63b90b4bce0fc8d9cb55d5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGXEO7UQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIAY71yZhSdIiOykUKFZDVoGa4kEzeKdkaLY9YpS%2B5CNVAiEA5Shn7wKM39bKcglBpZjmoueMvGnfEGbgm%2BoIRjLdQHIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDIFxa4d2tTuLBPMZ8CrcA5AiJexVfX9ZcP8wqnUO1mHBCZNXc%2BrPRFhN3DnCdzNuicoK4zyA%2FUK9BfJ09cR%2BepWA%2FX6vdO3Ai706dTUnNMN%2BZT2HE4OLhlmyoXokmvvCRc1tfYYvmNC1bakuxhVDe1XlIcnJ%2FO5o8TVICe35uIkLC%2BxSMX7ytXidpOWq2SM645BHuK4EdgnViFT2ylvrYlawTVvGn00akQmuRXs1Y%2FEgklYR%2Bt65utdDxbXqhMO7cz9F2bt4Bpo98UN14gJ3oNCfDCkFJ1NO0R%2Bj0I%2FiYma9vq%2BdXB3hVhl4LJOX4VzPM1807%2BrM9hk3TTQuPhbu%2BGgZI%2F0E37vsa53mkrTqgUmZyU4X0uu67KfufhCI8rpfL1sf157kg2%2FWcdDluiC%2FAoNoe%2FFSRZ%2B1MEsA04ta%2BIUcCYiciYA6UYrmAG6s00GrYLgEWKLyqAX3yAynznVT0q6BeqSdojplq0zs1XGQ7CpQcUIqUaMJqHUxE84Mftmf5VksU4OFk%2F84xrPi%2F%2FdXP2fcOfHqf4kPgfTnj0zfRZpzpaFKZ3pfR0Cs7m4KWmk5mR6Vrn3RIC6nvTeIqFZthsEPLOTfUjyGckRlPOAn3yA5WxIjkV3OGGlFkbvcoMRRCRZ3UmBy7wF3COyeMKO6jr0GOqUB%2BPRpMUgvxnYl9oLXN9fg21k1OiHQ331f6XQ19lxct%2BR5ozp6gdj1Dy0SFF4cr%2F%2FY%2F7iEekl3Bnw%2FEzhCAUcOR09nDfWmC%2BwchQnxVBI1Cn7OGGpsVfpPEoFeVDl0dBNC%2FCoabsDAs39nu2%2BQLqNGE3UqAcWTXiMPahkEs9RJWytWsWz7tLQPGj3BLWgHybFm8ALYS6pmCeioM%2F8yXsZV9Ah0X1pg&X-Amz-Signature=cc6f28f5aecff684f8fee35eca51100577d3bce4d330f3d9000923bc34e64d89&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSMA7J2G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIArLln%2B1FPJjx8sAi0goeQaCVVUyBtxHTqveCYHVPAbyAiBBpS2f8g4kyjFHKPTG%2BGyCvwlgzDcCCADhNhvLx0DcDCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMptksCtxr2mQAWi6dKtwDrh0zoBMZBMk2Y9ZfKRHMQ6Kts4QbbZd2X5%2BhwBT1R79FV8htIUKc698HYnS%2B74TyBNGn9Ni%2BjoFSLV%2FxEJ3ny3X8MsLjMITxQ%2BpAoVUYLjY07Kofh%2Fu68gXybvGlK5mF6cgzSUNduQ8E233zCoCOxyiLteVtqJgFS7iXTV5QKvbGKrvJLCcMvp6NnEUxh3zhbzkApLiLo2c3t%2BsvmTMESNUuHBUjiPdaiXciJpCm8xfXj3TnFv2IavrZWu5muM3litOucK0i9mWNZ3Ys9iDZf0CZDI%2FD0%2BaGhm%2FHiA%2Bwak6dcXfhkSQNqGsKjlRxvSZkLFE1kBus840jCt62jWGPnVR74y9gncv7HW9V9fUyOCbxTvyUzswDyNaArWaXfjqqWYVeAPlQBeIyf92RfxTxDaY%2BE8gAW89uwhYkH7Vp%2B5rvGsx5%2FOEEZ9ijnZGNjcSNpeCXDsYKVdttSnfSdVYptKH4t5aGIdrUQ33J9Olk9gMD8zceOiEDfqFtbD0%2BPdRbNI4GUxfY%2B2ff4dViYN0EUgNLp7eI3%2BRY%2B3t2DgGmHoVRvlcvWjyDGmp0jRt3LGubdEgs8l1vpYezK78cVsZoPC0NJhiRr49RMjccbA%2B6eZuNaSBawIKuwnDA5Dsw%2FbqOvQY6pgFG91c9ai1i0rCqzcVYlPiW4I%2F8uDyXS4gAgDNujbnAO%2FsvXpU55hkS9hc9SHcWaVCiANPeY5WJ8hyvsT8IO4%2F%2FEw%2BhkcDWSll3p9i0Cd1%2BPPunVVhrwWww3wZrHZAWgnBe4gikIndVOH2FGmpt5SCP9yjavTn8SpmEv6VVgT41l8tJomN1z5%2FC9od4hAT1P42cC6cH3iSD0qVC0jOcBinen6wm7Duj&X-Amz-Signature=5a6e29c687f33676a9b40458855b1e6ef242f69364e989ed062dcb917503de80&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSMA7J2G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIArLln%2B1FPJjx8sAi0goeQaCVVUyBtxHTqveCYHVPAbyAiBBpS2f8g4kyjFHKPTG%2BGyCvwlgzDcCCADhNhvLx0DcDCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMptksCtxr2mQAWi6dKtwDrh0zoBMZBMk2Y9ZfKRHMQ6Kts4QbbZd2X5%2BhwBT1R79FV8htIUKc698HYnS%2B74TyBNGn9Ni%2BjoFSLV%2FxEJ3ny3X8MsLjMITxQ%2BpAoVUYLjY07Kofh%2Fu68gXybvGlK5mF6cgzSUNduQ8E233zCoCOxyiLteVtqJgFS7iXTV5QKvbGKrvJLCcMvp6NnEUxh3zhbzkApLiLo2c3t%2BsvmTMESNUuHBUjiPdaiXciJpCm8xfXj3TnFv2IavrZWu5muM3litOucK0i9mWNZ3Ys9iDZf0CZDI%2FD0%2BaGhm%2FHiA%2Bwak6dcXfhkSQNqGsKjlRxvSZkLFE1kBus840jCt62jWGPnVR74y9gncv7HW9V9fUyOCbxTvyUzswDyNaArWaXfjqqWYVeAPlQBeIyf92RfxTxDaY%2BE8gAW89uwhYkH7Vp%2B5rvGsx5%2FOEEZ9ijnZGNjcSNpeCXDsYKVdttSnfSdVYptKH4t5aGIdrUQ33J9Olk9gMD8zceOiEDfqFtbD0%2BPdRbNI4GUxfY%2B2ff4dViYN0EUgNLp7eI3%2BRY%2B3t2DgGmHoVRvlcvWjyDGmp0jRt3LGubdEgs8l1vpYezK78cVsZoPC0NJhiRr49RMjccbA%2B6eZuNaSBawIKuwnDA5Dsw%2FbqOvQY6pgFG91c9ai1i0rCqzcVYlPiW4I%2F8uDyXS4gAgDNujbnAO%2FsvXpU55hkS9hc9SHcWaVCiANPeY5WJ8hyvsT8IO4%2F%2FEw%2BhkcDWSll3p9i0Cd1%2BPPunVVhrwWww3wZrHZAWgnBe4gikIndVOH2FGmpt5SCP9yjavTn8SpmEv6VVgT41l8tJomN1z5%2FC9od4hAT1P42cC6cH3iSD0qVC0jOcBinen6wm7Duj&X-Amz-Signature=ccd7f303dc98d97d7283aac456bd045a7dc7747bbbee8c92bde34c38b36aef3a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSMA7J2G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIArLln%2B1FPJjx8sAi0goeQaCVVUyBtxHTqveCYHVPAbyAiBBpS2f8g4kyjFHKPTG%2BGyCvwlgzDcCCADhNhvLx0DcDCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMptksCtxr2mQAWi6dKtwDrh0zoBMZBMk2Y9ZfKRHMQ6Kts4QbbZd2X5%2BhwBT1R79FV8htIUKc698HYnS%2B74TyBNGn9Ni%2BjoFSLV%2FxEJ3ny3X8MsLjMITxQ%2BpAoVUYLjY07Kofh%2Fu68gXybvGlK5mF6cgzSUNduQ8E233zCoCOxyiLteVtqJgFS7iXTV5QKvbGKrvJLCcMvp6NnEUxh3zhbzkApLiLo2c3t%2BsvmTMESNUuHBUjiPdaiXciJpCm8xfXj3TnFv2IavrZWu5muM3litOucK0i9mWNZ3Ys9iDZf0CZDI%2FD0%2BaGhm%2FHiA%2Bwak6dcXfhkSQNqGsKjlRxvSZkLFE1kBus840jCt62jWGPnVR74y9gncv7HW9V9fUyOCbxTvyUzswDyNaArWaXfjqqWYVeAPlQBeIyf92RfxTxDaY%2BE8gAW89uwhYkH7Vp%2B5rvGsx5%2FOEEZ9ijnZGNjcSNpeCXDsYKVdttSnfSdVYptKH4t5aGIdrUQ33J9Olk9gMD8zceOiEDfqFtbD0%2BPdRbNI4GUxfY%2B2ff4dViYN0EUgNLp7eI3%2BRY%2B3t2DgGmHoVRvlcvWjyDGmp0jRt3LGubdEgs8l1vpYezK78cVsZoPC0NJhiRr49RMjccbA%2B6eZuNaSBawIKuwnDA5Dsw%2FbqOvQY6pgFG91c9ai1i0rCqzcVYlPiW4I%2F8uDyXS4gAgDNujbnAO%2FsvXpU55hkS9hc9SHcWaVCiANPeY5WJ8hyvsT8IO4%2F%2FEw%2BhkcDWSll3p9i0Cd1%2BPPunVVhrwWww3wZrHZAWgnBe4gikIndVOH2FGmpt5SCP9yjavTn8SpmEv6VVgT41l8tJomN1z5%2FC9od4hAT1P42cC6cH3iSD0qVC0jOcBinen6wm7Duj&X-Amz-Signature=9b6e1464fe0f6d9315fe3bde2e2bf852b98ee0d2d91a4d604ca18b65060c0250&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSMA7J2G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIArLln%2B1FPJjx8sAi0goeQaCVVUyBtxHTqveCYHVPAbyAiBBpS2f8g4kyjFHKPTG%2BGyCvwlgzDcCCADhNhvLx0DcDCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMptksCtxr2mQAWi6dKtwDrh0zoBMZBMk2Y9ZfKRHMQ6Kts4QbbZd2X5%2BhwBT1R79FV8htIUKc698HYnS%2B74TyBNGn9Ni%2BjoFSLV%2FxEJ3ny3X8MsLjMITxQ%2BpAoVUYLjY07Kofh%2Fu68gXybvGlK5mF6cgzSUNduQ8E233zCoCOxyiLteVtqJgFS7iXTV5QKvbGKrvJLCcMvp6NnEUxh3zhbzkApLiLo2c3t%2BsvmTMESNUuHBUjiPdaiXciJpCm8xfXj3TnFv2IavrZWu5muM3litOucK0i9mWNZ3Ys9iDZf0CZDI%2FD0%2BaGhm%2FHiA%2Bwak6dcXfhkSQNqGsKjlRxvSZkLFE1kBus840jCt62jWGPnVR74y9gncv7HW9V9fUyOCbxTvyUzswDyNaArWaXfjqqWYVeAPlQBeIyf92RfxTxDaY%2BE8gAW89uwhYkH7Vp%2B5rvGsx5%2FOEEZ9ijnZGNjcSNpeCXDsYKVdttSnfSdVYptKH4t5aGIdrUQ33J9Olk9gMD8zceOiEDfqFtbD0%2BPdRbNI4GUxfY%2B2ff4dViYN0EUgNLp7eI3%2BRY%2B3t2DgGmHoVRvlcvWjyDGmp0jRt3LGubdEgs8l1vpYezK78cVsZoPC0NJhiRr49RMjccbA%2B6eZuNaSBawIKuwnDA5Dsw%2FbqOvQY6pgFG91c9ai1i0rCqzcVYlPiW4I%2F8uDyXS4gAgDNujbnAO%2FsvXpU55hkS9hc9SHcWaVCiANPeY5WJ8hyvsT8IO4%2F%2FEw%2BhkcDWSll3p9i0Cd1%2BPPunVVhrwWww3wZrHZAWgnBe4gikIndVOH2FGmpt5SCP9yjavTn8SpmEv6VVgT41l8tJomN1z5%2FC9od4hAT1P42cC6cH3iSD0qVC0jOcBinen6wm7Duj&X-Amz-Signature=49edb8474d3ac107f7b9c943246268191f851e681b3b0929d74bd460d2f053da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSMA7J2G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIArLln%2B1FPJjx8sAi0goeQaCVVUyBtxHTqveCYHVPAbyAiBBpS2f8g4kyjFHKPTG%2BGyCvwlgzDcCCADhNhvLx0DcDCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMptksCtxr2mQAWi6dKtwDrh0zoBMZBMk2Y9ZfKRHMQ6Kts4QbbZd2X5%2BhwBT1R79FV8htIUKc698HYnS%2B74TyBNGn9Ni%2BjoFSLV%2FxEJ3ny3X8MsLjMITxQ%2BpAoVUYLjY07Kofh%2Fu68gXybvGlK5mF6cgzSUNduQ8E233zCoCOxyiLteVtqJgFS7iXTV5QKvbGKrvJLCcMvp6NnEUxh3zhbzkApLiLo2c3t%2BsvmTMESNUuHBUjiPdaiXciJpCm8xfXj3TnFv2IavrZWu5muM3litOucK0i9mWNZ3Ys9iDZf0CZDI%2FD0%2BaGhm%2FHiA%2Bwak6dcXfhkSQNqGsKjlRxvSZkLFE1kBus840jCt62jWGPnVR74y9gncv7HW9V9fUyOCbxTvyUzswDyNaArWaXfjqqWYVeAPlQBeIyf92RfxTxDaY%2BE8gAW89uwhYkH7Vp%2B5rvGsx5%2FOEEZ9ijnZGNjcSNpeCXDsYKVdttSnfSdVYptKH4t5aGIdrUQ33J9Olk9gMD8zceOiEDfqFtbD0%2BPdRbNI4GUxfY%2B2ff4dViYN0EUgNLp7eI3%2BRY%2B3t2DgGmHoVRvlcvWjyDGmp0jRt3LGubdEgs8l1vpYezK78cVsZoPC0NJhiRr49RMjccbA%2B6eZuNaSBawIKuwnDA5Dsw%2FbqOvQY6pgFG91c9ai1i0rCqzcVYlPiW4I%2F8uDyXS4gAgDNujbnAO%2FsvXpU55hkS9hc9SHcWaVCiANPeY5WJ8hyvsT8IO4%2F%2FEw%2BhkcDWSll3p9i0Cd1%2BPPunVVhrwWww3wZrHZAWgnBe4gikIndVOH2FGmpt5SCP9yjavTn8SpmEv6VVgT41l8tJomN1z5%2FC9od4hAT1P42cC6cH3iSD0qVC0jOcBinen6wm7Duj&X-Amz-Signature=9c1bfd0147440bf4d0f4cb1ab73d139683fba660a37579895bd8bd3eed5353a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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


