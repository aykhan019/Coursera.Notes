

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B5RP6AZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLXNSCD6olifRb4QqZ5ZnizwRC%2FumLWpsYJP0Wn4N4%2FQIhANe8y5la1QGM4utMb7ugvDS%2BXa9ptjUl1djTmUbGtpOsKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyezurI2DQassogAuQq3APfQKFn36SgbFkfxYTJe6w5TXrDr5JOoHjb3sWdhflvP%2BwSzHnwxkC9YS1inEQ96I%2BJRGs7FkEsMAKO0HsIOVx7p%2F67p9FotKhnTP8%2F6UEz5r0hMkapMjisCXpl0EmeNdII4pFWRnmi2LALr6Z%2BQyjexJC2AtuYTf7yw6XDleqLwBekOEqw%2BJXRvj4ZXhTaDKPKaTlul7uIBAwjbvwpHCmXuYkHipjR7sEuX8UjWAj2b4EbBgzIDTLmx6VY367NghZfYoYZ3apWWFNi0kkNt4xMq643Berj%2FE5PAlTxzF3uTZpjqR37favrMIrX7bJS6XZjbM8jOPuECGm6SN3m1b4lg3kjDoiQLLJngzhBriSKHb2RIjpku0viijtuAQU3sEe78l9mkObWOlIoem8KtcQbVYPigSwajverR2K2UnpxY%2FmIxxKh1i9DMtq1i%2BeNO1Jx379gdVBxvfhUP702pwT6emH5JfWE4Rx%2FLmcYOJOSXccDX%2BzYkYw1CWEk%2FCz9BAJCGJnHysf7RpEBBXaV3P%2FGdPGql%2FSkBajKa%2Foq1XuFLm4SqEqcniTKXPtIbq0qeksYX2tYMAQ3g7pt4Qa%2BK2leaxtnlm%2FGovMTIlyRySn2jdkdczkaBKmtQ%2FcqizDtl%2B68BjqkAddyHoe5NdMWsawMurYWAQq4wHycIaAM7Jl5hBviLKiXKfYQUUartU4uZ1VpXfzQNWr8PBp9zK3JD2d3H3mQ02btys4JUoPogUvlzyH3A%2BVMZh54uZqRMOGzcWZLzcvJS5Fsb7VUK6ZwYvVpsMs%2ByjDK4xFha3qa9rdpmEO3Wj8O7tfUcMVYK8vsJ7CR0f4J3pZBu88HUf%2FnU1Iq6qDzIfXn3BpE&X-Amz-Signature=a098411f1114697fc784e1c0d2020afc03a2187683dde1f3e1d0b28275c8be89&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TK7MDM33%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpBQ%2BIDCDstu0XYoZfMBjgtpL%2FmKmcY%2BArX13YSnAnyAiBuBUMhJ8BiypTHEXyMeHyJ7tUGdN%2FXTak6PlMqAaC%2FwCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK1eRod9Ytoc8wYGqKtwDHT3GceZ4739epv1QWh9hN1LIWP24jnETv5XhO9Wn3nir8nCuUmNkDmXD0pzXAKEAoJ8Pk6xsRRM1Tge20YnQD6RtQvVB8wN7tId8l58AwEKyu3VyYSS5vmpvsNdP55dlDwA%2BC1V%2FVYgAgy5X9sdRkR8kFcriReqfID0B%2Fzo0%2BYAtCCIpFKR%2F84wjy%2FzUcRqQbFZ3bY%2FIvINcLcnApbiw7oH%2BgPuJy4kqHQC83eedssJsHtEbkp8wxqdk2D8l%2FpZF4VaaAYbQM%2FT0h3pGCpo4GGobvRrx7ikaazsJE%2B2kv%2BC7usJ1hq1YW%2Fn0L2DCF32%2Bnf%2FSPtoDGIHXOhnpUkVup5YMQtSNPJh2nNqYxF5QsN5Cq%2B2HCUMuoG8MZeVdegX7FvLT02auEvkrp48bpiS2wxarUV9MSC6G635kYmH9cmjdz2gVTk4FdqRMaPjp32y9RzEnim2ZmXUX5%2FshQlYaas3oGBxN5lMux%2BBsZRsiXJb2zykeW59hXaWTqM1tIE0vMruHcHnZ6iQyoXMY03zltwASLeO0Fp8e2LHLitfnYDnUI78yDCZJprhf2FmB2RfCIVnnwwjQZvdM%2Fe88AL1tgZD6I6bMTwAtqRTdTxSn9fMJHLNCX5itoxrpd8sw0pfuvAY6pgHso3ORdYCVPYplmC4ePbwEADimD3yewARLGiy4Ed3TdUrz7z2nGJWf6eAdCZ0K8s0iL3abq%2FxDCSyTGs3c9hiGuhH6ynxfRl%2Bt036v5JBPSNLkJDdHND3kdSGzSo70TURhwEiqjnhsQk56p9Kl%2FQFd3%2BKOyaPXtRsLylYq%2FruYRrHEtXUQ6Ti5dQQ1Z%2F%2BnDNuHWdZzHU4TK7VCpqiFRelOgT%2B8ybyA&X-Amz-Signature=c9031ee1c08b8a19ff969bfba7c3bd1388021d051a1b2c3f90d24abe3f5f8b2c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TK7MDM33%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpBQ%2BIDCDstu0XYoZfMBjgtpL%2FmKmcY%2BArX13YSnAnyAiBuBUMhJ8BiypTHEXyMeHyJ7tUGdN%2FXTak6PlMqAaC%2FwCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK1eRod9Ytoc8wYGqKtwDHT3GceZ4739epv1QWh9hN1LIWP24jnETv5XhO9Wn3nir8nCuUmNkDmXD0pzXAKEAoJ8Pk6xsRRM1Tge20YnQD6RtQvVB8wN7tId8l58AwEKyu3VyYSS5vmpvsNdP55dlDwA%2BC1V%2FVYgAgy5X9sdRkR8kFcriReqfID0B%2Fzo0%2BYAtCCIpFKR%2F84wjy%2FzUcRqQbFZ3bY%2FIvINcLcnApbiw7oH%2BgPuJy4kqHQC83eedssJsHtEbkp8wxqdk2D8l%2FpZF4VaaAYbQM%2FT0h3pGCpo4GGobvRrx7ikaazsJE%2B2kv%2BC7usJ1hq1YW%2Fn0L2DCF32%2Bnf%2FSPtoDGIHXOhnpUkVup5YMQtSNPJh2nNqYxF5QsN5Cq%2B2HCUMuoG8MZeVdegX7FvLT02auEvkrp48bpiS2wxarUV9MSC6G635kYmH9cmjdz2gVTk4FdqRMaPjp32y9RzEnim2ZmXUX5%2FshQlYaas3oGBxN5lMux%2BBsZRsiXJb2zykeW59hXaWTqM1tIE0vMruHcHnZ6iQyoXMY03zltwASLeO0Fp8e2LHLitfnYDnUI78yDCZJprhf2FmB2RfCIVnnwwjQZvdM%2Fe88AL1tgZD6I6bMTwAtqRTdTxSn9fMJHLNCX5itoxrpd8sw0pfuvAY6pgHso3ORdYCVPYplmC4ePbwEADimD3yewARLGiy4Ed3TdUrz7z2nGJWf6eAdCZ0K8s0iL3abq%2FxDCSyTGs3c9hiGuhH6ynxfRl%2Bt036v5JBPSNLkJDdHND3kdSGzSo70TURhwEiqjnhsQk56p9Kl%2FQFd3%2BKOyaPXtRsLylYq%2FruYRrHEtXUQ6Ti5dQQ1Z%2F%2BnDNuHWdZzHU4TK7VCpqiFRelOgT%2B8ybyA&X-Amz-Signature=02f946fca10ba5a7472df1453d104d94e7cd0c3e059719c83b42ecba6aa9d6c9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TK7MDM33%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpBQ%2BIDCDstu0XYoZfMBjgtpL%2FmKmcY%2BArX13YSnAnyAiBuBUMhJ8BiypTHEXyMeHyJ7tUGdN%2FXTak6PlMqAaC%2FwCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK1eRod9Ytoc8wYGqKtwDHT3GceZ4739epv1QWh9hN1LIWP24jnETv5XhO9Wn3nir8nCuUmNkDmXD0pzXAKEAoJ8Pk6xsRRM1Tge20YnQD6RtQvVB8wN7tId8l58AwEKyu3VyYSS5vmpvsNdP55dlDwA%2BC1V%2FVYgAgy5X9sdRkR8kFcriReqfID0B%2Fzo0%2BYAtCCIpFKR%2F84wjy%2FzUcRqQbFZ3bY%2FIvINcLcnApbiw7oH%2BgPuJy4kqHQC83eedssJsHtEbkp8wxqdk2D8l%2FpZF4VaaAYbQM%2FT0h3pGCpo4GGobvRrx7ikaazsJE%2B2kv%2BC7usJ1hq1YW%2Fn0L2DCF32%2Bnf%2FSPtoDGIHXOhnpUkVup5YMQtSNPJh2nNqYxF5QsN5Cq%2B2HCUMuoG8MZeVdegX7FvLT02auEvkrp48bpiS2wxarUV9MSC6G635kYmH9cmjdz2gVTk4FdqRMaPjp32y9RzEnim2ZmXUX5%2FshQlYaas3oGBxN5lMux%2BBsZRsiXJb2zykeW59hXaWTqM1tIE0vMruHcHnZ6iQyoXMY03zltwASLeO0Fp8e2LHLitfnYDnUI78yDCZJprhf2FmB2RfCIVnnwwjQZvdM%2Fe88AL1tgZD6I6bMTwAtqRTdTxSn9fMJHLNCX5itoxrpd8sw0pfuvAY6pgHso3ORdYCVPYplmC4ePbwEADimD3yewARLGiy4Ed3TdUrz7z2nGJWf6eAdCZ0K8s0iL3abq%2FxDCSyTGs3c9hiGuhH6ynxfRl%2Bt036v5JBPSNLkJDdHND3kdSGzSo70TURhwEiqjnhsQk56p9Kl%2FQFd3%2BKOyaPXtRsLylYq%2FruYRrHEtXUQ6Ti5dQQ1Z%2F%2BnDNuHWdZzHU4TK7VCpqiFRelOgT%2B8ybyA&X-Amz-Signature=29fb045cd87ec2e816c5a7e40f80f304552f468c430b327bab918d82387bb7a8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TK7MDM33%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpBQ%2BIDCDstu0XYoZfMBjgtpL%2FmKmcY%2BArX13YSnAnyAiBuBUMhJ8BiypTHEXyMeHyJ7tUGdN%2FXTak6PlMqAaC%2FwCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK1eRod9Ytoc8wYGqKtwDHT3GceZ4739epv1QWh9hN1LIWP24jnETv5XhO9Wn3nir8nCuUmNkDmXD0pzXAKEAoJ8Pk6xsRRM1Tge20YnQD6RtQvVB8wN7tId8l58AwEKyu3VyYSS5vmpvsNdP55dlDwA%2BC1V%2FVYgAgy5X9sdRkR8kFcriReqfID0B%2Fzo0%2BYAtCCIpFKR%2F84wjy%2FzUcRqQbFZ3bY%2FIvINcLcnApbiw7oH%2BgPuJy4kqHQC83eedssJsHtEbkp8wxqdk2D8l%2FpZF4VaaAYbQM%2FT0h3pGCpo4GGobvRrx7ikaazsJE%2B2kv%2BC7usJ1hq1YW%2Fn0L2DCF32%2Bnf%2FSPtoDGIHXOhnpUkVup5YMQtSNPJh2nNqYxF5QsN5Cq%2B2HCUMuoG8MZeVdegX7FvLT02auEvkrp48bpiS2wxarUV9MSC6G635kYmH9cmjdz2gVTk4FdqRMaPjp32y9RzEnim2ZmXUX5%2FshQlYaas3oGBxN5lMux%2BBsZRsiXJb2zykeW59hXaWTqM1tIE0vMruHcHnZ6iQyoXMY03zltwASLeO0Fp8e2LHLitfnYDnUI78yDCZJprhf2FmB2RfCIVnnwwjQZvdM%2Fe88AL1tgZD6I6bMTwAtqRTdTxSn9fMJHLNCX5itoxrpd8sw0pfuvAY6pgHso3ORdYCVPYplmC4ePbwEADimD3yewARLGiy4Ed3TdUrz7z2nGJWf6eAdCZ0K8s0iL3abq%2FxDCSyTGs3c9hiGuhH6ynxfRl%2Bt036v5JBPSNLkJDdHND3kdSGzSo70TURhwEiqjnhsQk56p9Kl%2FQFd3%2BKOyaPXtRsLylYq%2FruYRrHEtXUQ6Ti5dQQ1Z%2F%2BnDNuHWdZzHU4TK7VCpqiFRelOgT%2B8ybyA&X-Amz-Signature=dfbe02f162b1ec46c0b91e46450e9e8e01e723d8de8b0c84412576b495499a28&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TK7MDM33%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpBQ%2BIDCDstu0XYoZfMBjgtpL%2FmKmcY%2BArX13YSnAnyAiBuBUMhJ8BiypTHEXyMeHyJ7tUGdN%2FXTak6PlMqAaC%2FwCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK1eRod9Ytoc8wYGqKtwDHT3GceZ4739epv1QWh9hN1LIWP24jnETv5XhO9Wn3nir8nCuUmNkDmXD0pzXAKEAoJ8Pk6xsRRM1Tge20YnQD6RtQvVB8wN7tId8l58AwEKyu3VyYSS5vmpvsNdP55dlDwA%2BC1V%2FVYgAgy5X9sdRkR8kFcriReqfID0B%2Fzo0%2BYAtCCIpFKR%2F84wjy%2FzUcRqQbFZ3bY%2FIvINcLcnApbiw7oH%2BgPuJy4kqHQC83eedssJsHtEbkp8wxqdk2D8l%2FpZF4VaaAYbQM%2FT0h3pGCpo4GGobvRrx7ikaazsJE%2B2kv%2BC7usJ1hq1YW%2Fn0L2DCF32%2Bnf%2FSPtoDGIHXOhnpUkVup5YMQtSNPJh2nNqYxF5QsN5Cq%2B2HCUMuoG8MZeVdegX7FvLT02auEvkrp48bpiS2wxarUV9MSC6G635kYmH9cmjdz2gVTk4FdqRMaPjp32y9RzEnim2ZmXUX5%2FshQlYaas3oGBxN5lMux%2BBsZRsiXJb2zykeW59hXaWTqM1tIE0vMruHcHnZ6iQyoXMY03zltwASLeO0Fp8e2LHLitfnYDnUI78yDCZJprhf2FmB2RfCIVnnwwjQZvdM%2Fe88AL1tgZD6I6bMTwAtqRTdTxSn9fMJHLNCX5itoxrpd8sw0pfuvAY6pgHso3ORdYCVPYplmC4ePbwEADimD3yewARLGiy4Ed3TdUrz7z2nGJWf6eAdCZ0K8s0iL3abq%2FxDCSyTGs3c9hiGuhH6ynxfRl%2Bt036v5JBPSNLkJDdHND3kdSGzSo70TURhwEiqjnhsQk56p9Kl%2FQFd3%2BKOyaPXtRsLylYq%2FruYRrHEtXUQ6Ti5dQQ1Z%2F%2BnDNuHWdZzHU4TK7VCpqiFRelOgT%2B8ybyA&X-Amz-Signature=2b340a358c53b1863d982d708e35efc2de8ad3785df81c85219dda9efc50c131&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B5RP6AZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLXNSCD6olifRb4QqZ5ZnizwRC%2FumLWpsYJP0Wn4N4%2FQIhANe8y5la1QGM4utMb7ugvDS%2BXa9ptjUl1djTmUbGtpOsKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyezurI2DQassogAuQq3APfQKFn36SgbFkfxYTJe6w5TXrDr5JOoHjb3sWdhflvP%2BwSzHnwxkC9YS1inEQ96I%2BJRGs7FkEsMAKO0HsIOVx7p%2F67p9FotKhnTP8%2F6UEz5r0hMkapMjisCXpl0EmeNdII4pFWRnmi2LALr6Z%2BQyjexJC2AtuYTf7yw6XDleqLwBekOEqw%2BJXRvj4ZXhTaDKPKaTlul7uIBAwjbvwpHCmXuYkHipjR7sEuX8UjWAj2b4EbBgzIDTLmx6VY367NghZfYoYZ3apWWFNi0kkNt4xMq643Berj%2FE5PAlTxzF3uTZpjqR37favrMIrX7bJS6XZjbM8jOPuECGm6SN3m1b4lg3kjDoiQLLJngzhBriSKHb2RIjpku0viijtuAQU3sEe78l9mkObWOlIoem8KtcQbVYPigSwajverR2K2UnpxY%2FmIxxKh1i9DMtq1i%2BeNO1Jx379gdVBxvfhUP702pwT6emH5JfWE4Rx%2FLmcYOJOSXccDX%2BzYkYw1CWEk%2FCz9BAJCGJnHysf7RpEBBXaV3P%2FGdPGql%2FSkBajKa%2Foq1XuFLm4SqEqcniTKXPtIbq0qeksYX2tYMAQ3g7pt4Qa%2BK2leaxtnlm%2FGovMTIlyRySn2jdkdczkaBKmtQ%2FcqizDtl%2B68BjqkAddyHoe5NdMWsawMurYWAQq4wHycIaAM7Jl5hBviLKiXKfYQUUartU4uZ1VpXfzQNWr8PBp9zK3JD2d3H3mQ02btys4JUoPogUvlzyH3A%2BVMZh54uZqRMOGzcWZLzcvJS5Fsb7VUK6ZwYvVpsMs%2ByjDK4xFha3qa9rdpmEO3Wj8O7tfUcMVYK8vsJ7CR0f4J3pZBu88HUf%2FnU1Iq6qDzIfXn3BpE&X-Amz-Signature=58039b3524cad7c6b4584871fed3c60f163ea9e240671e1c3a1b58cfe60e180f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B5RP6AZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLXNSCD6olifRb4QqZ5ZnizwRC%2FumLWpsYJP0Wn4N4%2FQIhANe8y5la1QGM4utMb7ugvDS%2BXa9ptjUl1djTmUbGtpOsKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyezurI2DQassogAuQq3APfQKFn36SgbFkfxYTJe6w5TXrDr5JOoHjb3sWdhflvP%2BwSzHnwxkC9YS1inEQ96I%2BJRGs7FkEsMAKO0HsIOVx7p%2F67p9FotKhnTP8%2F6UEz5r0hMkapMjisCXpl0EmeNdII4pFWRnmi2LALr6Z%2BQyjexJC2AtuYTf7yw6XDleqLwBekOEqw%2BJXRvj4ZXhTaDKPKaTlul7uIBAwjbvwpHCmXuYkHipjR7sEuX8UjWAj2b4EbBgzIDTLmx6VY367NghZfYoYZ3apWWFNi0kkNt4xMq643Berj%2FE5PAlTxzF3uTZpjqR37favrMIrX7bJS6XZjbM8jOPuECGm6SN3m1b4lg3kjDoiQLLJngzhBriSKHb2RIjpku0viijtuAQU3sEe78l9mkObWOlIoem8KtcQbVYPigSwajverR2K2UnpxY%2FmIxxKh1i9DMtq1i%2BeNO1Jx379gdVBxvfhUP702pwT6emH5JfWE4Rx%2FLmcYOJOSXccDX%2BzYkYw1CWEk%2FCz9BAJCGJnHysf7RpEBBXaV3P%2FGdPGql%2FSkBajKa%2Foq1XuFLm4SqEqcniTKXPtIbq0qeksYX2tYMAQ3g7pt4Qa%2BK2leaxtnlm%2FGovMTIlyRySn2jdkdczkaBKmtQ%2FcqizDtl%2B68BjqkAddyHoe5NdMWsawMurYWAQq4wHycIaAM7Jl5hBviLKiXKfYQUUartU4uZ1VpXfzQNWr8PBp9zK3JD2d3H3mQ02btys4JUoPogUvlzyH3A%2BVMZh54uZqRMOGzcWZLzcvJS5Fsb7VUK6ZwYvVpsMs%2ByjDK4xFha3qa9rdpmEO3Wj8O7tfUcMVYK8vsJ7CR0f4J3pZBu88HUf%2FnU1Iq6qDzIfXn3BpE&X-Amz-Signature=bd41e052f780694133a4d5aba60f7023b4e76164f4bc15171c372f8bc1c6b7e0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B5RP6AZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLXNSCD6olifRb4QqZ5ZnizwRC%2FumLWpsYJP0Wn4N4%2FQIhANe8y5la1QGM4utMb7ugvDS%2BXa9ptjUl1djTmUbGtpOsKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyezurI2DQassogAuQq3APfQKFn36SgbFkfxYTJe6w5TXrDr5JOoHjb3sWdhflvP%2BwSzHnwxkC9YS1inEQ96I%2BJRGs7FkEsMAKO0HsIOVx7p%2F67p9FotKhnTP8%2F6UEz5r0hMkapMjisCXpl0EmeNdII4pFWRnmi2LALr6Z%2BQyjexJC2AtuYTf7yw6XDleqLwBekOEqw%2BJXRvj4ZXhTaDKPKaTlul7uIBAwjbvwpHCmXuYkHipjR7sEuX8UjWAj2b4EbBgzIDTLmx6VY367NghZfYoYZ3apWWFNi0kkNt4xMq643Berj%2FE5PAlTxzF3uTZpjqR37favrMIrX7bJS6XZjbM8jOPuECGm6SN3m1b4lg3kjDoiQLLJngzhBriSKHb2RIjpku0viijtuAQU3sEe78l9mkObWOlIoem8KtcQbVYPigSwajverR2K2UnpxY%2FmIxxKh1i9DMtq1i%2BeNO1Jx379gdVBxvfhUP702pwT6emH5JfWE4Rx%2FLmcYOJOSXccDX%2BzYkYw1CWEk%2FCz9BAJCGJnHysf7RpEBBXaV3P%2FGdPGql%2FSkBajKa%2Foq1XuFLm4SqEqcniTKXPtIbq0qeksYX2tYMAQ3g7pt4Qa%2BK2leaxtnlm%2FGovMTIlyRySn2jdkdczkaBKmtQ%2FcqizDtl%2B68BjqkAddyHoe5NdMWsawMurYWAQq4wHycIaAM7Jl5hBviLKiXKfYQUUartU4uZ1VpXfzQNWr8PBp9zK3JD2d3H3mQ02btys4JUoPogUvlzyH3A%2BVMZh54uZqRMOGzcWZLzcvJS5Fsb7VUK6ZwYvVpsMs%2ByjDK4xFha3qa9rdpmEO3Wj8O7tfUcMVYK8vsJ7CR0f4J3pZBu88HUf%2FnU1Iq6qDzIfXn3BpE&X-Amz-Signature=9a03c08e827e01fc40347d284089ba0cf50845c3a482cd868a0fe6952b8b5f02&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B5RP6AZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLXNSCD6olifRb4QqZ5ZnizwRC%2FumLWpsYJP0Wn4N4%2FQIhANe8y5la1QGM4utMb7ugvDS%2BXa9ptjUl1djTmUbGtpOsKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyezurI2DQassogAuQq3APfQKFn36SgbFkfxYTJe6w5TXrDr5JOoHjb3sWdhflvP%2BwSzHnwxkC9YS1inEQ96I%2BJRGs7FkEsMAKO0HsIOVx7p%2F67p9FotKhnTP8%2F6UEz5r0hMkapMjisCXpl0EmeNdII4pFWRnmi2LALr6Z%2BQyjexJC2AtuYTf7yw6XDleqLwBekOEqw%2BJXRvj4ZXhTaDKPKaTlul7uIBAwjbvwpHCmXuYkHipjR7sEuX8UjWAj2b4EbBgzIDTLmx6VY367NghZfYoYZ3apWWFNi0kkNt4xMq643Berj%2FE5PAlTxzF3uTZpjqR37favrMIrX7bJS6XZjbM8jOPuECGm6SN3m1b4lg3kjDoiQLLJngzhBriSKHb2RIjpku0viijtuAQU3sEe78l9mkObWOlIoem8KtcQbVYPigSwajverR2K2UnpxY%2FmIxxKh1i9DMtq1i%2BeNO1Jx379gdVBxvfhUP702pwT6emH5JfWE4Rx%2FLmcYOJOSXccDX%2BzYkYw1CWEk%2FCz9BAJCGJnHysf7RpEBBXaV3P%2FGdPGql%2FSkBajKa%2Foq1XuFLm4SqEqcniTKXPtIbq0qeksYX2tYMAQ3g7pt4Qa%2BK2leaxtnlm%2FGovMTIlyRySn2jdkdczkaBKmtQ%2FcqizDtl%2B68BjqkAddyHoe5NdMWsawMurYWAQq4wHycIaAM7Jl5hBviLKiXKfYQUUartU4uZ1VpXfzQNWr8PBp9zK3JD2d3H3mQ02btys4JUoPogUvlzyH3A%2BVMZh54uZqRMOGzcWZLzcvJS5Fsb7VUK6ZwYvVpsMs%2ByjDK4xFha3qa9rdpmEO3Wj8O7tfUcMVYK8vsJ7CR0f4J3pZBu88HUf%2FnU1Iq6qDzIfXn3BpE&X-Amz-Signature=28d1d9042673038f95ceda336fd234d0feefd49c7def35b3f56712fc2de1d53d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B5RP6AZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLXNSCD6olifRb4QqZ5ZnizwRC%2FumLWpsYJP0Wn4N4%2FQIhANe8y5la1QGM4utMb7ugvDS%2BXa9ptjUl1djTmUbGtpOsKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyezurI2DQassogAuQq3APfQKFn36SgbFkfxYTJe6w5TXrDr5JOoHjb3sWdhflvP%2BwSzHnwxkC9YS1inEQ96I%2BJRGs7FkEsMAKO0HsIOVx7p%2F67p9FotKhnTP8%2F6UEz5r0hMkapMjisCXpl0EmeNdII4pFWRnmi2LALr6Z%2BQyjexJC2AtuYTf7yw6XDleqLwBekOEqw%2BJXRvj4ZXhTaDKPKaTlul7uIBAwjbvwpHCmXuYkHipjR7sEuX8UjWAj2b4EbBgzIDTLmx6VY367NghZfYoYZ3apWWFNi0kkNt4xMq643Berj%2FE5PAlTxzF3uTZpjqR37favrMIrX7bJS6XZjbM8jOPuECGm6SN3m1b4lg3kjDoiQLLJngzhBriSKHb2RIjpku0viijtuAQU3sEe78l9mkObWOlIoem8KtcQbVYPigSwajverR2K2UnpxY%2FmIxxKh1i9DMtq1i%2BeNO1Jx379gdVBxvfhUP702pwT6emH5JfWE4Rx%2FLmcYOJOSXccDX%2BzYkYw1CWEk%2FCz9BAJCGJnHysf7RpEBBXaV3P%2FGdPGql%2FSkBajKa%2Foq1XuFLm4SqEqcniTKXPtIbq0qeksYX2tYMAQ3g7pt4Qa%2BK2leaxtnlm%2FGovMTIlyRySn2jdkdczkaBKmtQ%2FcqizDtl%2B68BjqkAddyHoe5NdMWsawMurYWAQq4wHycIaAM7Jl5hBviLKiXKfYQUUartU4uZ1VpXfzQNWr8PBp9zK3JD2d3H3mQ02btys4JUoPogUvlzyH3A%2BVMZh54uZqRMOGzcWZLzcvJS5Fsb7VUK6ZwYvVpsMs%2ByjDK4xFha3qa9rdpmEO3Wj8O7tfUcMVYK8vsJ7CR0f4J3pZBu88HUf%2FnU1Iq6qDzIfXn3BpE&X-Amz-Signature=bea207165df63aeb21c40939264e28911eb9b6d7d199ef6797bb9415ceffcd76&X-Amz-SignedHeaders=host&x-id=GetObject)
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


