

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLG4BW5H%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIA9%2BcK%2FFvcWsC%2Fn9KN9ZSsPpNOF4H%2Fa2RIoFjoH2IkxoAiEA7xogjKdBXByLysEd%2Bp5UW5g%2ByFdBybjSPFFo0FzHD20qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOxMM9EnatGMhZugircAxxu66ufTCvW0ONomQKPcOjxC5LiL5lxiiObXM3SjZdpLM0NSXbjBPoF65qfaeEYzmUaL9VIulR%2F4BK4hRNok83hwWYT7LYbLQ9d3yivszpsM2W7xLYeLH%2FNOukdrTj5bnciDALt0Zr3yOkJPdjKekuW8DxXKmyXtlfL5aHi5ZgPhPWVlAzOVW%2Fx%2FQlxOYPdErxP9fTzjdYrYVLbdbzinyfYwXwHK%2Bdi96RhiNyiFLiqCwA1qP07GBd3Rgx9Uswdrpi8fKohmG4mvWKqnh7HDsMbpKHu2U0qYfMxK8hr26IKcxWEF4jnRfpsJwY0vL6br%2Fy6%2F6phmMAZSeyAxjuSGiK2URLyLrbLhsrZap3ZVraYpLR8D2NnufrIaD4zTFdcjj65XzuR5uhj6EyORwReqGZOvupv%2Fwj3pwzBYN6m3IPLdXgvJW9%2Fk8qFcZ8vqWJ6ba06PfMZDxBgBYL6esZOtUbnNYx3ZXiWu%2BeMTqcfY%2BcD%2BrxwjrEANxgxt%2BEOjzfDNhNESwWEuksIU7AMxQaui4KXlYg5eBLT4Sduqv%2F6HOVXF7tGDtt9Jbdva9Pn%2Bc0czwZ6%2BhNO8g7QmT%2FRzpQGeFD9oG0oLuLJUB90JhvEQ%2FmlPKLu6xuOwhFpudk0MJO4jr4GOqUB1F1tjrBTK0zQGaRhknwOdL9iDQPTtJHUSYO9EaeiFPqYvrBCoHXPQsu%2FR7oDDs47opPLJJvbK5vuJZeULPmHqAbCBTAaLMk7oJotlQyfcegYa4kAETyIq8EhRCc7T2eCQMgimrdSuaLDq5a0c4ee%2BM%2F20veTuX5Sdijl9wyjSCaankLMJOYcY%2F4hSlBjWGvOT7gtceKS4g5W95UM6eqW6YWu7P8W&X-Amz-Signature=92f708f7eef7047efbfd1c4fa379f7f0ce0fdea84b5d988a1bf20c4b50994e49&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYPNQ2ON%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDU7VdSCwOx12OQdiXSMmXGikPADcYSANP63SdHMx%2F%2B6wIhAOWTuC05LTEjsJCSwa4DR43rAlAs022Of%2BIOy43UY7GaKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb%2FQq3CnRmkrtqAJEq3AMG%2FZa1aCgAFYW0eSp4K0KUJ68n6fDZmFy5UZ63jBVWMX0vcvk6V%2FwfLv%2BLagrcqaYz8pT7RDSe4n96GKWSnDYuk55mb%2Bc%2BOTRBng7oLm91D%2FSXQxFOsSZh9HQc1x70%2FrsX4EhaH0UnmW7IJ2lZ9SxRQABHQbg4xkKVQohVP%2BcSy4Ne8F0wHmet%2Be5t1DLnl2%2For3cRV3qrh9MT2xLdsxCilQEDkgOveQFZyrzDlnkyFhHMPH1Y%2F1M8S7mLyefe1QQhSoYWkPzYG11Pqs0CDqMdrNV8h3cPqMQYB5Hh%2FPxlHA2SWpf9WMOnnFAi8FwiQf7zXai1C%2F5eqoOvxj0lzXdvHuuGXmwxOIBZrkCocLzQOKFWmCteYeKCY%2FUbqRvGPYwx4xDH3dD88XtbblevNYEtwltgP%2BTAJ6JAwN2oBF%2BRjkhcux9n4CSb9RuIj0X0GIGRKEPTBgxyS2bzj6ma04As%2BnpsOrFfAiin6cfuCeMzX%2BgI0lVQAr%2Bo8PWuXTDMvRUdgCVol%2BosAK3UooAv95zSlSAWLvY%2FjwTFo47SGsMiE9u7tye2N%2F%2BeXJMSqN4GfHuHm7omx9J%2BZ1VXfcu7I5NkHK7vqiTc9gC7HPfN755bB4%2B1knq2MkR3b3N33jC2uI6%2BBjqkAdS2eALr22UQPBV%2Bv4WNbeZz8KcCTTTK1%2BXGmB7NfOBM%2FhKElKm94Q5Qoz4dgc%2Bx9nFrujBRDDIq2DtgkWSWVR8rmSfp0jzLAY4fZUChu2lQGVgoF60LhBmfPuv9boTLyW7V1Dfm7wy36LY5978rBUeoePNlwhb4hG6RUwKRoZJ7uNQogiHCDs5AhstnfrE%2B6BTt2p%2FiFFUQyBbc3sAPcEC5QGW%2F&X-Amz-Signature=d1a34d60176152b501c9596d012e3ace196ce136bc0f5e1c7bb486be47973add&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYPNQ2ON%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDU7VdSCwOx12OQdiXSMmXGikPADcYSANP63SdHMx%2F%2B6wIhAOWTuC05LTEjsJCSwa4DR43rAlAs022Of%2BIOy43UY7GaKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb%2FQq3CnRmkrtqAJEq3AMG%2FZa1aCgAFYW0eSp4K0KUJ68n6fDZmFy5UZ63jBVWMX0vcvk6V%2FwfLv%2BLagrcqaYz8pT7RDSe4n96GKWSnDYuk55mb%2Bc%2BOTRBng7oLm91D%2FSXQxFOsSZh9HQc1x70%2FrsX4EhaH0UnmW7IJ2lZ9SxRQABHQbg4xkKVQohVP%2BcSy4Ne8F0wHmet%2Be5t1DLnl2%2For3cRV3qrh9MT2xLdsxCilQEDkgOveQFZyrzDlnkyFhHMPH1Y%2F1M8S7mLyefe1QQhSoYWkPzYG11Pqs0CDqMdrNV8h3cPqMQYB5Hh%2FPxlHA2SWpf9WMOnnFAi8FwiQf7zXai1C%2F5eqoOvxj0lzXdvHuuGXmwxOIBZrkCocLzQOKFWmCteYeKCY%2FUbqRvGPYwx4xDH3dD88XtbblevNYEtwltgP%2BTAJ6JAwN2oBF%2BRjkhcux9n4CSb9RuIj0X0GIGRKEPTBgxyS2bzj6ma04As%2BnpsOrFfAiin6cfuCeMzX%2BgI0lVQAr%2Bo8PWuXTDMvRUdgCVol%2BosAK3UooAv95zSlSAWLvY%2FjwTFo47SGsMiE9u7tye2N%2F%2BeXJMSqN4GfHuHm7omx9J%2BZ1VXfcu7I5NkHK7vqiTc9gC7HPfN755bB4%2B1knq2MkR3b3N33jC2uI6%2BBjqkAdS2eALr22UQPBV%2Bv4WNbeZz8KcCTTTK1%2BXGmB7NfOBM%2FhKElKm94Q5Qoz4dgc%2Bx9nFrujBRDDIq2DtgkWSWVR8rmSfp0jzLAY4fZUChu2lQGVgoF60LhBmfPuv9boTLyW7V1Dfm7wy36LY5978rBUeoePNlwhb4hG6RUwKRoZJ7uNQogiHCDs5AhstnfrE%2B6BTt2p%2FiFFUQyBbc3sAPcEC5QGW%2F&X-Amz-Signature=62a01c13b7d0ef0d63216a5f9ab04add69bdfe0c2aaf2ae5f39a2bc8a335eba8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYPNQ2ON%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDU7VdSCwOx12OQdiXSMmXGikPADcYSANP63SdHMx%2F%2B6wIhAOWTuC05LTEjsJCSwa4DR43rAlAs022Of%2BIOy43UY7GaKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb%2FQq3CnRmkrtqAJEq3AMG%2FZa1aCgAFYW0eSp4K0KUJ68n6fDZmFy5UZ63jBVWMX0vcvk6V%2FwfLv%2BLagrcqaYz8pT7RDSe4n96GKWSnDYuk55mb%2Bc%2BOTRBng7oLm91D%2FSXQxFOsSZh9HQc1x70%2FrsX4EhaH0UnmW7IJ2lZ9SxRQABHQbg4xkKVQohVP%2BcSy4Ne8F0wHmet%2Be5t1DLnl2%2For3cRV3qrh9MT2xLdsxCilQEDkgOveQFZyrzDlnkyFhHMPH1Y%2F1M8S7mLyefe1QQhSoYWkPzYG11Pqs0CDqMdrNV8h3cPqMQYB5Hh%2FPxlHA2SWpf9WMOnnFAi8FwiQf7zXai1C%2F5eqoOvxj0lzXdvHuuGXmwxOIBZrkCocLzQOKFWmCteYeKCY%2FUbqRvGPYwx4xDH3dD88XtbblevNYEtwltgP%2BTAJ6JAwN2oBF%2BRjkhcux9n4CSb9RuIj0X0GIGRKEPTBgxyS2bzj6ma04As%2BnpsOrFfAiin6cfuCeMzX%2BgI0lVQAr%2Bo8PWuXTDMvRUdgCVol%2BosAK3UooAv95zSlSAWLvY%2FjwTFo47SGsMiE9u7tye2N%2F%2BeXJMSqN4GfHuHm7omx9J%2BZ1VXfcu7I5NkHK7vqiTc9gC7HPfN755bB4%2B1knq2MkR3b3N33jC2uI6%2BBjqkAdS2eALr22UQPBV%2Bv4WNbeZz8KcCTTTK1%2BXGmB7NfOBM%2FhKElKm94Q5Qoz4dgc%2Bx9nFrujBRDDIq2DtgkWSWVR8rmSfp0jzLAY4fZUChu2lQGVgoF60LhBmfPuv9boTLyW7V1Dfm7wy36LY5978rBUeoePNlwhb4hG6RUwKRoZJ7uNQogiHCDs5AhstnfrE%2B6BTt2p%2FiFFUQyBbc3sAPcEC5QGW%2F&X-Amz-Signature=7e3e1bb04a08b9e3327a6837b61fa75cbc831e2aceda225fb2ddb0b03c0b625e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYPNQ2ON%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDU7VdSCwOx12OQdiXSMmXGikPADcYSANP63SdHMx%2F%2B6wIhAOWTuC05LTEjsJCSwa4DR43rAlAs022Of%2BIOy43UY7GaKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb%2FQq3CnRmkrtqAJEq3AMG%2FZa1aCgAFYW0eSp4K0KUJ68n6fDZmFy5UZ63jBVWMX0vcvk6V%2FwfLv%2BLagrcqaYz8pT7RDSe4n96GKWSnDYuk55mb%2Bc%2BOTRBng7oLm91D%2FSXQxFOsSZh9HQc1x70%2FrsX4EhaH0UnmW7IJ2lZ9SxRQABHQbg4xkKVQohVP%2BcSy4Ne8F0wHmet%2Be5t1DLnl2%2For3cRV3qrh9MT2xLdsxCilQEDkgOveQFZyrzDlnkyFhHMPH1Y%2F1M8S7mLyefe1QQhSoYWkPzYG11Pqs0CDqMdrNV8h3cPqMQYB5Hh%2FPxlHA2SWpf9WMOnnFAi8FwiQf7zXai1C%2F5eqoOvxj0lzXdvHuuGXmwxOIBZrkCocLzQOKFWmCteYeKCY%2FUbqRvGPYwx4xDH3dD88XtbblevNYEtwltgP%2BTAJ6JAwN2oBF%2BRjkhcux9n4CSb9RuIj0X0GIGRKEPTBgxyS2bzj6ma04As%2BnpsOrFfAiin6cfuCeMzX%2BgI0lVQAr%2Bo8PWuXTDMvRUdgCVol%2BosAK3UooAv95zSlSAWLvY%2FjwTFo47SGsMiE9u7tye2N%2F%2BeXJMSqN4GfHuHm7omx9J%2BZ1VXfcu7I5NkHK7vqiTc9gC7HPfN755bB4%2B1knq2MkR3b3N33jC2uI6%2BBjqkAdS2eALr22UQPBV%2Bv4WNbeZz8KcCTTTK1%2BXGmB7NfOBM%2FhKElKm94Q5Qoz4dgc%2Bx9nFrujBRDDIq2DtgkWSWVR8rmSfp0jzLAY4fZUChu2lQGVgoF60LhBmfPuv9boTLyW7V1Dfm7wy36LY5978rBUeoePNlwhb4hG6RUwKRoZJ7uNQogiHCDs5AhstnfrE%2B6BTt2p%2FiFFUQyBbc3sAPcEC5QGW%2F&X-Amz-Signature=912eec22e5cd79c9fd7edbb9673acb83d19650d571fda1d3714a9a3669b8e88d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYPNQ2ON%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDU7VdSCwOx12OQdiXSMmXGikPADcYSANP63SdHMx%2F%2B6wIhAOWTuC05LTEjsJCSwa4DR43rAlAs022Of%2BIOy43UY7GaKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb%2FQq3CnRmkrtqAJEq3AMG%2FZa1aCgAFYW0eSp4K0KUJ68n6fDZmFy5UZ63jBVWMX0vcvk6V%2FwfLv%2BLagrcqaYz8pT7RDSe4n96GKWSnDYuk55mb%2Bc%2BOTRBng7oLm91D%2FSXQxFOsSZh9HQc1x70%2FrsX4EhaH0UnmW7IJ2lZ9SxRQABHQbg4xkKVQohVP%2BcSy4Ne8F0wHmet%2Be5t1DLnl2%2For3cRV3qrh9MT2xLdsxCilQEDkgOveQFZyrzDlnkyFhHMPH1Y%2F1M8S7mLyefe1QQhSoYWkPzYG11Pqs0CDqMdrNV8h3cPqMQYB5Hh%2FPxlHA2SWpf9WMOnnFAi8FwiQf7zXai1C%2F5eqoOvxj0lzXdvHuuGXmwxOIBZrkCocLzQOKFWmCteYeKCY%2FUbqRvGPYwx4xDH3dD88XtbblevNYEtwltgP%2BTAJ6JAwN2oBF%2BRjkhcux9n4CSb9RuIj0X0GIGRKEPTBgxyS2bzj6ma04As%2BnpsOrFfAiin6cfuCeMzX%2BgI0lVQAr%2Bo8PWuXTDMvRUdgCVol%2BosAK3UooAv95zSlSAWLvY%2FjwTFo47SGsMiE9u7tye2N%2F%2BeXJMSqN4GfHuHm7omx9J%2BZ1VXfcu7I5NkHK7vqiTc9gC7HPfN755bB4%2B1knq2MkR3b3N33jC2uI6%2BBjqkAdS2eALr22UQPBV%2Bv4WNbeZz8KcCTTTK1%2BXGmB7NfOBM%2FhKElKm94Q5Qoz4dgc%2Bx9nFrujBRDDIq2DtgkWSWVR8rmSfp0jzLAY4fZUChu2lQGVgoF60LhBmfPuv9boTLyW7V1Dfm7wy36LY5978rBUeoePNlwhb4hG6RUwKRoZJ7uNQogiHCDs5AhstnfrE%2B6BTt2p%2FiFFUQyBbc3sAPcEC5QGW%2F&X-Amz-Signature=bf8dfe07c449924e0babe749c26d77f7de8fb1597c032942b12eb6d03d0add5f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLG4BW5H%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIA9%2BcK%2FFvcWsC%2Fn9KN9ZSsPpNOF4H%2Fa2RIoFjoH2IkxoAiEA7xogjKdBXByLysEd%2Bp5UW5g%2ByFdBybjSPFFo0FzHD20qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOxMM9EnatGMhZugircAxxu66ufTCvW0ONomQKPcOjxC5LiL5lxiiObXM3SjZdpLM0NSXbjBPoF65qfaeEYzmUaL9VIulR%2F4BK4hRNok83hwWYT7LYbLQ9d3yivszpsM2W7xLYeLH%2FNOukdrTj5bnciDALt0Zr3yOkJPdjKekuW8DxXKmyXtlfL5aHi5ZgPhPWVlAzOVW%2Fx%2FQlxOYPdErxP9fTzjdYrYVLbdbzinyfYwXwHK%2Bdi96RhiNyiFLiqCwA1qP07GBd3Rgx9Uswdrpi8fKohmG4mvWKqnh7HDsMbpKHu2U0qYfMxK8hr26IKcxWEF4jnRfpsJwY0vL6br%2Fy6%2F6phmMAZSeyAxjuSGiK2URLyLrbLhsrZap3ZVraYpLR8D2NnufrIaD4zTFdcjj65XzuR5uhj6EyORwReqGZOvupv%2Fwj3pwzBYN6m3IPLdXgvJW9%2Fk8qFcZ8vqWJ6ba06PfMZDxBgBYL6esZOtUbnNYx3ZXiWu%2BeMTqcfY%2BcD%2BrxwjrEANxgxt%2BEOjzfDNhNESwWEuksIU7AMxQaui4KXlYg5eBLT4Sduqv%2F6HOVXF7tGDtt9Jbdva9Pn%2Bc0czwZ6%2BhNO8g7QmT%2FRzpQGeFD9oG0oLuLJUB90JhvEQ%2FmlPKLu6xuOwhFpudk0MJO4jr4GOqUB1F1tjrBTK0zQGaRhknwOdL9iDQPTtJHUSYO9EaeiFPqYvrBCoHXPQsu%2FR7oDDs47opPLJJvbK5vuJZeULPmHqAbCBTAaLMk7oJotlQyfcegYa4kAETyIq8EhRCc7T2eCQMgimrdSuaLDq5a0c4ee%2BM%2F20veTuX5Sdijl9wyjSCaankLMJOYcY%2F4hSlBjWGvOT7gtceKS4g5W95UM6eqW6YWu7P8W&X-Amz-Signature=2a6dac75ddd619bc7ebfd6541762dc75b401e3da2ccb9984af9f1314056a9cf5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLG4BW5H%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIA9%2BcK%2FFvcWsC%2Fn9KN9ZSsPpNOF4H%2Fa2RIoFjoH2IkxoAiEA7xogjKdBXByLysEd%2Bp5UW5g%2ByFdBybjSPFFo0FzHD20qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOxMM9EnatGMhZugircAxxu66ufTCvW0ONomQKPcOjxC5LiL5lxiiObXM3SjZdpLM0NSXbjBPoF65qfaeEYzmUaL9VIulR%2F4BK4hRNok83hwWYT7LYbLQ9d3yivszpsM2W7xLYeLH%2FNOukdrTj5bnciDALt0Zr3yOkJPdjKekuW8DxXKmyXtlfL5aHi5ZgPhPWVlAzOVW%2Fx%2FQlxOYPdErxP9fTzjdYrYVLbdbzinyfYwXwHK%2Bdi96RhiNyiFLiqCwA1qP07GBd3Rgx9Uswdrpi8fKohmG4mvWKqnh7HDsMbpKHu2U0qYfMxK8hr26IKcxWEF4jnRfpsJwY0vL6br%2Fy6%2F6phmMAZSeyAxjuSGiK2URLyLrbLhsrZap3ZVraYpLR8D2NnufrIaD4zTFdcjj65XzuR5uhj6EyORwReqGZOvupv%2Fwj3pwzBYN6m3IPLdXgvJW9%2Fk8qFcZ8vqWJ6ba06PfMZDxBgBYL6esZOtUbnNYx3ZXiWu%2BeMTqcfY%2BcD%2BrxwjrEANxgxt%2BEOjzfDNhNESwWEuksIU7AMxQaui4KXlYg5eBLT4Sduqv%2F6HOVXF7tGDtt9Jbdva9Pn%2Bc0czwZ6%2BhNO8g7QmT%2FRzpQGeFD9oG0oLuLJUB90JhvEQ%2FmlPKLu6xuOwhFpudk0MJO4jr4GOqUB1F1tjrBTK0zQGaRhknwOdL9iDQPTtJHUSYO9EaeiFPqYvrBCoHXPQsu%2FR7oDDs47opPLJJvbK5vuJZeULPmHqAbCBTAaLMk7oJotlQyfcegYa4kAETyIq8EhRCc7T2eCQMgimrdSuaLDq5a0c4ee%2BM%2F20veTuX5Sdijl9wyjSCaankLMJOYcY%2F4hSlBjWGvOT7gtceKS4g5W95UM6eqW6YWu7P8W&X-Amz-Signature=3e850dbbb2d8beb7202494b120ab47661b3f11a86f6500d723c4ddc2c77fe5a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLG4BW5H%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIA9%2BcK%2FFvcWsC%2Fn9KN9ZSsPpNOF4H%2Fa2RIoFjoH2IkxoAiEA7xogjKdBXByLysEd%2Bp5UW5g%2ByFdBybjSPFFo0FzHD20qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOxMM9EnatGMhZugircAxxu66ufTCvW0ONomQKPcOjxC5LiL5lxiiObXM3SjZdpLM0NSXbjBPoF65qfaeEYzmUaL9VIulR%2F4BK4hRNok83hwWYT7LYbLQ9d3yivszpsM2W7xLYeLH%2FNOukdrTj5bnciDALt0Zr3yOkJPdjKekuW8DxXKmyXtlfL5aHi5ZgPhPWVlAzOVW%2Fx%2FQlxOYPdErxP9fTzjdYrYVLbdbzinyfYwXwHK%2Bdi96RhiNyiFLiqCwA1qP07GBd3Rgx9Uswdrpi8fKohmG4mvWKqnh7HDsMbpKHu2U0qYfMxK8hr26IKcxWEF4jnRfpsJwY0vL6br%2Fy6%2F6phmMAZSeyAxjuSGiK2URLyLrbLhsrZap3ZVraYpLR8D2NnufrIaD4zTFdcjj65XzuR5uhj6EyORwReqGZOvupv%2Fwj3pwzBYN6m3IPLdXgvJW9%2Fk8qFcZ8vqWJ6ba06PfMZDxBgBYL6esZOtUbnNYx3ZXiWu%2BeMTqcfY%2BcD%2BrxwjrEANxgxt%2BEOjzfDNhNESwWEuksIU7AMxQaui4KXlYg5eBLT4Sduqv%2F6HOVXF7tGDtt9Jbdva9Pn%2Bc0czwZ6%2BhNO8g7QmT%2FRzpQGeFD9oG0oLuLJUB90JhvEQ%2FmlPKLu6xuOwhFpudk0MJO4jr4GOqUB1F1tjrBTK0zQGaRhknwOdL9iDQPTtJHUSYO9EaeiFPqYvrBCoHXPQsu%2FR7oDDs47opPLJJvbK5vuJZeULPmHqAbCBTAaLMk7oJotlQyfcegYa4kAETyIq8EhRCc7T2eCQMgimrdSuaLDq5a0c4ee%2BM%2F20veTuX5Sdijl9wyjSCaankLMJOYcY%2F4hSlBjWGvOT7gtceKS4g5W95UM6eqW6YWu7P8W&X-Amz-Signature=b3c7dbc0bccb1b584f8c89e9c180a6d4ef663700ef59c3a98686f2b8f107a744&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLG4BW5H%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIA9%2BcK%2FFvcWsC%2Fn9KN9ZSsPpNOF4H%2Fa2RIoFjoH2IkxoAiEA7xogjKdBXByLysEd%2Bp5UW5g%2ByFdBybjSPFFo0FzHD20qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOxMM9EnatGMhZugircAxxu66ufTCvW0ONomQKPcOjxC5LiL5lxiiObXM3SjZdpLM0NSXbjBPoF65qfaeEYzmUaL9VIulR%2F4BK4hRNok83hwWYT7LYbLQ9d3yivszpsM2W7xLYeLH%2FNOukdrTj5bnciDALt0Zr3yOkJPdjKekuW8DxXKmyXtlfL5aHi5ZgPhPWVlAzOVW%2Fx%2FQlxOYPdErxP9fTzjdYrYVLbdbzinyfYwXwHK%2Bdi96RhiNyiFLiqCwA1qP07GBd3Rgx9Uswdrpi8fKohmG4mvWKqnh7HDsMbpKHu2U0qYfMxK8hr26IKcxWEF4jnRfpsJwY0vL6br%2Fy6%2F6phmMAZSeyAxjuSGiK2URLyLrbLhsrZap3ZVraYpLR8D2NnufrIaD4zTFdcjj65XzuR5uhj6EyORwReqGZOvupv%2Fwj3pwzBYN6m3IPLdXgvJW9%2Fk8qFcZ8vqWJ6ba06PfMZDxBgBYL6esZOtUbnNYx3ZXiWu%2BeMTqcfY%2BcD%2BrxwjrEANxgxt%2BEOjzfDNhNESwWEuksIU7AMxQaui4KXlYg5eBLT4Sduqv%2F6HOVXF7tGDtt9Jbdva9Pn%2Bc0czwZ6%2BhNO8g7QmT%2FRzpQGeFD9oG0oLuLJUB90JhvEQ%2FmlPKLu6xuOwhFpudk0MJO4jr4GOqUB1F1tjrBTK0zQGaRhknwOdL9iDQPTtJHUSYO9EaeiFPqYvrBCoHXPQsu%2FR7oDDs47opPLJJvbK5vuJZeULPmHqAbCBTAaLMk7oJotlQyfcegYa4kAETyIq8EhRCc7T2eCQMgimrdSuaLDq5a0c4ee%2BM%2F20veTuX5Sdijl9wyjSCaankLMJOYcY%2F4hSlBjWGvOT7gtceKS4g5W95UM6eqW6YWu7P8W&X-Amz-Signature=5c8c96564fc04e7f27c9fb70544be315de0bc8f005d25b6e1c69d1a76e3eb2ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLG4BW5H%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIA9%2BcK%2FFvcWsC%2Fn9KN9ZSsPpNOF4H%2Fa2RIoFjoH2IkxoAiEA7xogjKdBXByLysEd%2Bp5UW5g%2ByFdBybjSPFFo0FzHD20qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOxMM9EnatGMhZugircAxxu66ufTCvW0ONomQKPcOjxC5LiL5lxiiObXM3SjZdpLM0NSXbjBPoF65qfaeEYzmUaL9VIulR%2F4BK4hRNok83hwWYT7LYbLQ9d3yivszpsM2W7xLYeLH%2FNOukdrTj5bnciDALt0Zr3yOkJPdjKekuW8DxXKmyXtlfL5aHi5ZgPhPWVlAzOVW%2Fx%2FQlxOYPdErxP9fTzjdYrYVLbdbzinyfYwXwHK%2Bdi96RhiNyiFLiqCwA1qP07GBd3Rgx9Uswdrpi8fKohmG4mvWKqnh7HDsMbpKHu2U0qYfMxK8hr26IKcxWEF4jnRfpsJwY0vL6br%2Fy6%2F6phmMAZSeyAxjuSGiK2URLyLrbLhsrZap3ZVraYpLR8D2NnufrIaD4zTFdcjj65XzuR5uhj6EyORwReqGZOvupv%2Fwj3pwzBYN6m3IPLdXgvJW9%2Fk8qFcZ8vqWJ6ba06PfMZDxBgBYL6esZOtUbnNYx3ZXiWu%2BeMTqcfY%2BcD%2BrxwjrEANxgxt%2BEOjzfDNhNESwWEuksIU7AMxQaui4KXlYg5eBLT4Sduqv%2F6HOVXF7tGDtt9Jbdva9Pn%2Bc0czwZ6%2BhNO8g7QmT%2FRzpQGeFD9oG0oLuLJUB90JhvEQ%2FmlPKLu6xuOwhFpudk0MJO4jr4GOqUB1F1tjrBTK0zQGaRhknwOdL9iDQPTtJHUSYO9EaeiFPqYvrBCoHXPQsu%2FR7oDDs47opPLJJvbK5vuJZeULPmHqAbCBTAaLMk7oJotlQyfcegYa4kAETyIq8EhRCc7T2eCQMgimrdSuaLDq5a0c4ee%2BM%2F20veTuX5Sdijl9wyjSCaankLMJOYcY%2F4hSlBjWGvOT7gtceKS4g5W95UM6eqW6YWu7P8W&X-Amz-Signature=990f0d7da42e6049034e63af3d2a4a828ecf2fa77b5b1059f7402e4f392b44bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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


