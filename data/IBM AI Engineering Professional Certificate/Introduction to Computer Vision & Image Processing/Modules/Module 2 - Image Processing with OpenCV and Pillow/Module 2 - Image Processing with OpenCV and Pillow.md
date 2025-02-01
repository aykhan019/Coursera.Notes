

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYYM2SXR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHO%2BeyqQcEZAp8sBGiS4eLooHpNShUp19BSkmOI%2BF%2BcQIgBvxGrEXsT8V03m8AKeU2cHrRyTHK5c%2B7ZEx0vbnf4W8qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDl3ndSuSmJv6SG%2BnCrcA7qI%2F17sJiXv%2BWyB5yj0QADyPDIetwX0h05VTYLZecT1ukMIPmYVY4dg3%2BtOVsliwhfm0vssG60cLPCqCQ0wsSDFUMf9fPU2%2BTfxb2sIEAjF1PLaYX60LiEfHBla17%2BXZoD%2Bu3rv31KatoHOD5Ksx0EnyhT59ZS3a2FThJhIWr93zIgPyRZEFv7ktK31sUZlULQVAdT%2FGdPVrdFnzu2dXxTWCf6KYm3bJYJLW5mZ52vKYBKiP1WaZCGDjL6VmfBX1uVNy9%2FFwHuWF5NXFqChlDA781Uv%2FGMsYl52AZ8yzP1cxr8rhDCLtcOfqeXlXGBD%2Fa8ZyyDKpDGTrn%2Fp%2FFpFW6zMkaAhcTZ4FH%2BE09Odtm4kkhlbTcvVs1Q2TWZZfg1kuTlDGiPXb%2B8AYbPoLZhraBmR2spG%2FU5On29Z7GtPOcHkcckKYzXczFWx9jxgOt1hCbk3ml54WveaLMcO%2FWklwh5q1FYYzAoaxJSz9ckgEYJOmret7Exuwpx%2BVfqyq20cg0Y7blMdppBkfxejzjnm85qmMQiFOXJP8xS1gYTs915ytOaj2c01X8TuS3kXvW3j1XsANcu89uNSk4JMtxV2OBv1aXUPBV%2B%2BX8PT54tkRU5Cg%2BPzVF3vAJnj5lGcMPnJ%2BLwGOqUBr7COdYz%2BUnw2k3eZhadCerj240Ea1Kl8Li1%2BlbJhtsrybioa3ekoCCVYQWSJDRUSJjrdU6%2FWipgJi7ooNKS2myKJjGlo7jS2A3FtdHsJA%2FnvyZ9WIa%2BNQX%2FnmNIquR%2FqdcSXI97%2FKuya2o75CtucPBQPNCTHAQC1ZxuwAX3NwMKzTblu1aSNsAr%2B8eguLBBqBDJgjtjCHPYf6xH%2Bv%2FCkoJTv16fk&X-Amz-Signature=6e4a4f2289f7018c9c3b9db36592f30b0c6118df9d49940c837f55aa97cb6e92&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPJNT2AQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F0RPdVNFNXPBF37QQZBtzPNRwjoQNg7aZRcjseeR2vgIgEJq79HshULrGKLXYOI5Z8%2F0f0LtAen5nKCIxs1202NIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIpvCDm2e3TYoOJqDircAzIPBVRjz039f30PeJ%2FmKPJmFoP9R9eFdzYf06l3tOAVCJNn9s9Ctp1qsN9FCYAXSRDd9oETxt63uj%2Bw0V2%2FiK6t0%2FaGi%2FJODDJ7jyexQ7S9ew1At42JLeCu600he0d47mkdgCcgA%2FfnaGNdJ9dr%2B3j9ESvDxSwmRQrKXdOgYLHRkaPqoIVzEAcnxJIWL%2BmOXZ3tuoe%2FSLQD8WMKRn0xPF9MNG2OGgwJAtqPrFTZvxOcctdYH%2B6EJNCtgvrOdWAmeOhg9UkOEESgJArKeuLMBrBlP1tXULUhyihLgFJ6JY2rRGL9Kjbiot7H4qTnvdvZ%2F0JngPdI3i4mK48n991VkIfA1JuCGutUkQrOgcWaVbHZieTSoh%2BNkUVTrjChs0%2BMmaRb3boFFWDUggC58GcRGG%2FgPfH0pwsLeoqhQVqyEbk5XBKnunYRXY1GHgPVF0XeLqKM%2B9VpVsCyNdmVtww%2BUkURnmA67wh0xWlPpe1lN%2BZjDXdhG8gfnTO8MP7BaSpQkmNYyYvIc8fEYGSo1f9IZumV3AVRuNkrwf22i1KIJTQ8kazT6Z%2Ftp4RyMoNVCi0Ab5BY5v6MwJzjk%2FlgTXi0tLMLh6cX3HqkHcrdy9CFUbA9YUpTGfOwF%2FPInPh%2FMM3F%2BLwGOqUBxiYVPGQVxsJ50guIueQx6SJjFjQg10E9QwsPIA3seaMkXUoMp2Lu7OKHCxasAuU3uw75JF%2FP0CCoDn3EOedfsyQSk7D8%2BgqsaXMRym5Aonif60H8rkUd0BV4Ej3PhZ%2BEaJThXpQWBC6UqoFNJ8apThyom73A9Dp2aci8v1alxh%2FychA3MlNUqntbkpsstpgZhya1411hwbmtouYLPrukixJu%2BqES&X-Amz-Signature=c7428310016118f73aee352d131571514d2c4f179138f0155ade295df3f69d43&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPJNT2AQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F0RPdVNFNXPBF37QQZBtzPNRwjoQNg7aZRcjseeR2vgIgEJq79HshULrGKLXYOI5Z8%2F0f0LtAen5nKCIxs1202NIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIpvCDm2e3TYoOJqDircAzIPBVRjz039f30PeJ%2FmKPJmFoP9R9eFdzYf06l3tOAVCJNn9s9Ctp1qsN9FCYAXSRDd9oETxt63uj%2Bw0V2%2FiK6t0%2FaGi%2FJODDJ7jyexQ7S9ew1At42JLeCu600he0d47mkdgCcgA%2FfnaGNdJ9dr%2B3j9ESvDxSwmRQrKXdOgYLHRkaPqoIVzEAcnxJIWL%2BmOXZ3tuoe%2FSLQD8WMKRn0xPF9MNG2OGgwJAtqPrFTZvxOcctdYH%2B6EJNCtgvrOdWAmeOhg9UkOEESgJArKeuLMBrBlP1tXULUhyihLgFJ6JY2rRGL9Kjbiot7H4qTnvdvZ%2F0JngPdI3i4mK48n991VkIfA1JuCGutUkQrOgcWaVbHZieTSoh%2BNkUVTrjChs0%2BMmaRb3boFFWDUggC58GcRGG%2FgPfH0pwsLeoqhQVqyEbk5XBKnunYRXY1GHgPVF0XeLqKM%2B9VpVsCyNdmVtww%2BUkURnmA67wh0xWlPpe1lN%2BZjDXdhG8gfnTO8MP7BaSpQkmNYyYvIc8fEYGSo1f9IZumV3AVRuNkrwf22i1KIJTQ8kazT6Z%2Ftp4RyMoNVCi0Ab5BY5v6MwJzjk%2FlgTXi0tLMLh6cX3HqkHcrdy9CFUbA9YUpTGfOwF%2FPInPh%2FMM3F%2BLwGOqUBxiYVPGQVxsJ50guIueQx6SJjFjQg10E9QwsPIA3seaMkXUoMp2Lu7OKHCxasAuU3uw75JF%2FP0CCoDn3EOedfsyQSk7D8%2BgqsaXMRym5Aonif60H8rkUd0BV4Ej3PhZ%2BEaJThXpQWBC6UqoFNJ8apThyom73A9Dp2aci8v1alxh%2FychA3MlNUqntbkpsstpgZhya1411hwbmtouYLPrukixJu%2BqES&X-Amz-Signature=ab72ca49fadd133053d2efb360a69434f5d0211c70738faebfb9b96c7142f857&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPJNT2AQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F0RPdVNFNXPBF37QQZBtzPNRwjoQNg7aZRcjseeR2vgIgEJq79HshULrGKLXYOI5Z8%2F0f0LtAen5nKCIxs1202NIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIpvCDm2e3TYoOJqDircAzIPBVRjz039f30PeJ%2FmKPJmFoP9R9eFdzYf06l3tOAVCJNn9s9Ctp1qsN9FCYAXSRDd9oETxt63uj%2Bw0V2%2FiK6t0%2FaGi%2FJODDJ7jyexQ7S9ew1At42JLeCu600he0d47mkdgCcgA%2FfnaGNdJ9dr%2B3j9ESvDxSwmRQrKXdOgYLHRkaPqoIVzEAcnxJIWL%2BmOXZ3tuoe%2FSLQD8WMKRn0xPF9MNG2OGgwJAtqPrFTZvxOcctdYH%2B6EJNCtgvrOdWAmeOhg9UkOEESgJArKeuLMBrBlP1tXULUhyihLgFJ6JY2rRGL9Kjbiot7H4qTnvdvZ%2F0JngPdI3i4mK48n991VkIfA1JuCGutUkQrOgcWaVbHZieTSoh%2BNkUVTrjChs0%2BMmaRb3boFFWDUggC58GcRGG%2FgPfH0pwsLeoqhQVqyEbk5XBKnunYRXY1GHgPVF0XeLqKM%2B9VpVsCyNdmVtww%2BUkURnmA67wh0xWlPpe1lN%2BZjDXdhG8gfnTO8MP7BaSpQkmNYyYvIc8fEYGSo1f9IZumV3AVRuNkrwf22i1KIJTQ8kazT6Z%2Ftp4RyMoNVCi0Ab5BY5v6MwJzjk%2FlgTXi0tLMLh6cX3HqkHcrdy9CFUbA9YUpTGfOwF%2FPInPh%2FMM3F%2BLwGOqUBxiYVPGQVxsJ50guIueQx6SJjFjQg10E9QwsPIA3seaMkXUoMp2Lu7OKHCxasAuU3uw75JF%2FP0CCoDn3EOedfsyQSk7D8%2BgqsaXMRym5Aonif60H8rkUd0BV4Ej3PhZ%2BEaJThXpQWBC6UqoFNJ8apThyom73A9Dp2aci8v1alxh%2FychA3MlNUqntbkpsstpgZhya1411hwbmtouYLPrukixJu%2BqES&X-Amz-Signature=de304372634b35ca272c8d035535a53072e400925fc187eabfb98a2069f87456&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPJNT2AQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F0RPdVNFNXPBF37QQZBtzPNRwjoQNg7aZRcjseeR2vgIgEJq79HshULrGKLXYOI5Z8%2F0f0LtAen5nKCIxs1202NIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIpvCDm2e3TYoOJqDircAzIPBVRjz039f30PeJ%2FmKPJmFoP9R9eFdzYf06l3tOAVCJNn9s9Ctp1qsN9FCYAXSRDd9oETxt63uj%2Bw0V2%2FiK6t0%2FaGi%2FJODDJ7jyexQ7S9ew1At42JLeCu600he0d47mkdgCcgA%2FfnaGNdJ9dr%2B3j9ESvDxSwmRQrKXdOgYLHRkaPqoIVzEAcnxJIWL%2BmOXZ3tuoe%2FSLQD8WMKRn0xPF9MNG2OGgwJAtqPrFTZvxOcctdYH%2B6EJNCtgvrOdWAmeOhg9UkOEESgJArKeuLMBrBlP1tXULUhyihLgFJ6JY2rRGL9Kjbiot7H4qTnvdvZ%2F0JngPdI3i4mK48n991VkIfA1JuCGutUkQrOgcWaVbHZieTSoh%2BNkUVTrjChs0%2BMmaRb3boFFWDUggC58GcRGG%2FgPfH0pwsLeoqhQVqyEbk5XBKnunYRXY1GHgPVF0XeLqKM%2B9VpVsCyNdmVtww%2BUkURnmA67wh0xWlPpe1lN%2BZjDXdhG8gfnTO8MP7BaSpQkmNYyYvIc8fEYGSo1f9IZumV3AVRuNkrwf22i1KIJTQ8kazT6Z%2Ftp4RyMoNVCi0Ab5BY5v6MwJzjk%2FlgTXi0tLMLh6cX3HqkHcrdy9CFUbA9YUpTGfOwF%2FPInPh%2FMM3F%2BLwGOqUBxiYVPGQVxsJ50guIueQx6SJjFjQg10E9QwsPIA3seaMkXUoMp2Lu7OKHCxasAuU3uw75JF%2FP0CCoDn3EOedfsyQSk7D8%2BgqsaXMRym5Aonif60H8rkUd0BV4Ej3PhZ%2BEaJThXpQWBC6UqoFNJ8apThyom73A9Dp2aci8v1alxh%2FychA3MlNUqntbkpsstpgZhya1411hwbmtouYLPrukixJu%2BqES&X-Amz-Signature=52c3ec4dc456e721d72f93cfc938544b4d85af21bbec4353d6223e1726d732f4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPJNT2AQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F0RPdVNFNXPBF37QQZBtzPNRwjoQNg7aZRcjseeR2vgIgEJq79HshULrGKLXYOI5Z8%2F0f0LtAen5nKCIxs1202NIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIpvCDm2e3TYoOJqDircAzIPBVRjz039f30PeJ%2FmKPJmFoP9R9eFdzYf06l3tOAVCJNn9s9Ctp1qsN9FCYAXSRDd9oETxt63uj%2Bw0V2%2FiK6t0%2FaGi%2FJODDJ7jyexQ7S9ew1At42JLeCu600he0d47mkdgCcgA%2FfnaGNdJ9dr%2B3j9ESvDxSwmRQrKXdOgYLHRkaPqoIVzEAcnxJIWL%2BmOXZ3tuoe%2FSLQD8WMKRn0xPF9MNG2OGgwJAtqPrFTZvxOcctdYH%2B6EJNCtgvrOdWAmeOhg9UkOEESgJArKeuLMBrBlP1tXULUhyihLgFJ6JY2rRGL9Kjbiot7H4qTnvdvZ%2F0JngPdI3i4mK48n991VkIfA1JuCGutUkQrOgcWaVbHZieTSoh%2BNkUVTrjChs0%2BMmaRb3boFFWDUggC58GcRGG%2FgPfH0pwsLeoqhQVqyEbk5XBKnunYRXY1GHgPVF0XeLqKM%2B9VpVsCyNdmVtww%2BUkURnmA67wh0xWlPpe1lN%2BZjDXdhG8gfnTO8MP7BaSpQkmNYyYvIc8fEYGSo1f9IZumV3AVRuNkrwf22i1KIJTQ8kazT6Z%2Ftp4RyMoNVCi0Ab5BY5v6MwJzjk%2FlgTXi0tLMLh6cX3HqkHcrdy9CFUbA9YUpTGfOwF%2FPInPh%2FMM3F%2BLwGOqUBxiYVPGQVxsJ50guIueQx6SJjFjQg10E9QwsPIA3seaMkXUoMp2Lu7OKHCxasAuU3uw75JF%2FP0CCoDn3EOedfsyQSk7D8%2BgqsaXMRym5Aonif60H8rkUd0BV4Ej3PhZ%2BEaJThXpQWBC6UqoFNJ8apThyom73A9Dp2aci8v1alxh%2FychA3MlNUqntbkpsstpgZhya1411hwbmtouYLPrukixJu%2BqES&X-Amz-Signature=87a29f48f1fd1d189e0cce938f054f41d27a16a3546dfce435e6a904214743f7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYYM2SXR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHO%2BeyqQcEZAp8sBGiS4eLooHpNShUp19BSkmOI%2BF%2BcQIgBvxGrEXsT8V03m8AKeU2cHrRyTHK5c%2B7ZEx0vbnf4W8qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDl3ndSuSmJv6SG%2BnCrcA7qI%2F17sJiXv%2BWyB5yj0QADyPDIetwX0h05VTYLZecT1ukMIPmYVY4dg3%2BtOVsliwhfm0vssG60cLPCqCQ0wsSDFUMf9fPU2%2BTfxb2sIEAjF1PLaYX60LiEfHBla17%2BXZoD%2Bu3rv31KatoHOD5Ksx0EnyhT59ZS3a2FThJhIWr93zIgPyRZEFv7ktK31sUZlULQVAdT%2FGdPVrdFnzu2dXxTWCf6KYm3bJYJLW5mZ52vKYBKiP1WaZCGDjL6VmfBX1uVNy9%2FFwHuWF5NXFqChlDA781Uv%2FGMsYl52AZ8yzP1cxr8rhDCLtcOfqeXlXGBD%2Fa8ZyyDKpDGTrn%2Fp%2FFpFW6zMkaAhcTZ4FH%2BE09Odtm4kkhlbTcvVs1Q2TWZZfg1kuTlDGiPXb%2B8AYbPoLZhraBmR2spG%2FU5On29Z7GtPOcHkcckKYzXczFWx9jxgOt1hCbk3ml54WveaLMcO%2FWklwh5q1FYYzAoaxJSz9ckgEYJOmret7Exuwpx%2BVfqyq20cg0Y7blMdppBkfxejzjnm85qmMQiFOXJP8xS1gYTs915ytOaj2c01X8TuS3kXvW3j1XsANcu89uNSk4JMtxV2OBv1aXUPBV%2B%2BX8PT54tkRU5Cg%2BPzVF3vAJnj5lGcMPnJ%2BLwGOqUBr7COdYz%2BUnw2k3eZhadCerj240Ea1Kl8Li1%2BlbJhtsrybioa3ekoCCVYQWSJDRUSJjrdU6%2FWipgJi7ooNKS2myKJjGlo7jS2A3FtdHsJA%2FnvyZ9WIa%2BNQX%2FnmNIquR%2FqdcSXI97%2FKuya2o75CtucPBQPNCTHAQC1ZxuwAX3NwMKzTblu1aSNsAr%2B8eguLBBqBDJgjtjCHPYf6xH%2Bv%2FCkoJTv16fk&X-Amz-Signature=29712ab2594432da888146679f01a017a481fc25a9d37440db08d6253fba2a5b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYYM2SXR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHO%2BeyqQcEZAp8sBGiS4eLooHpNShUp19BSkmOI%2BF%2BcQIgBvxGrEXsT8V03m8AKeU2cHrRyTHK5c%2B7ZEx0vbnf4W8qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDl3ndSuSmJv6SG%2BnCrcA7qI%2F17sJiXv%2BWyB5yj0QADyPDIetwX0h05VTYLZecT1ukMIPmYVY4dg3%2BtOVsliwhfm0vssG60cLPCqCQ0wsSDFUMf9fPU2%2BTfxb2sIEAjF1PLaYX60LiEfHBla17%2BXZoD%2Bu3rv31KatoHOD5Ksx0EnyhT59ZS3a2FThJhIWr93zIgPyRZEFv7ktK31sUZlULQVAdT%2FGdPVrdFnzu2dXxTWCf6KYm3bJYJLW5mZ52vKYBKiP1WaZCGDjL6VmfBX1uVNy9%2FFwHuWF5NXFqChlDA781Uv%2FGMsYl52AZ8yzP1cxr8rhDCLtcOfqeXlXGBD%2Fa8ZyyDKpDGTrn%2Fp%2FFpFW6zMkaAhcTZ4FH%2BE09Odtm4kkhlbTcvVs1Q2TWZZfg1kuTlDGiPXb%2B8AYbPoLZhraBmR2spG%2FU5On29Z7GtPOcHkcckKYzXczFWx9jxgOt1hCbk3ml54WveaLMcO%2FWklwh5q1FYYzAoaxJSz9ckgEYJOmret7Exuwpx%2BVfqyq20cg0Y7blMdppBkfxejzjnm85qmMQiFOXJP8xS1gYTs915ytOaj2c01X8TuS3kXvW3j1XsANcu89uNSk4JMtxV2OBv1aXUPBV%2B%2BX8PT54tkRU5Cg%2BPzVF3vAJnj5lGcMPnJ%2BLwGOqUBr7COdYz%2BUnw2k3eZhadCerj240Ea1Kl8Li1%2BlbJhtsrybioa3ekoCCVYQWSJDRUSJjrdU6%2FWipgJi7ooNKS2myKJjGlo7jS2A3FtdHsJA%2FnvyZ9WIa%2BNQX%2FnmNIquR%2FqdcSXI97%2FKuya2o75CtucPBQPNCTHAQC1ZxuwAX3NwMKzTblu1aSNsAr%2B8eguLBBqBDJgjtjCHPYf6xH%2Bv%2FCkoJTv16fk&X-Amz-Signature=d922d3197915352190f31f71a03cfc6399516a53df936cffd3b23e33e053677c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYYM2SXR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHO%2BeyqQcEZAp8sBGiS4eLooHpNShUp19BSkmOI%2BF%2BcQIgBvxGrEXsT8V03m8AKeU2cHrRyTHK5c%2B7ZEx0vbnf4W8qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDl3ndSuSmJv6SG%2BnCrcA7qI%2F17sJiXv%2BWyB5yj0QADyPDIetwX0h05VTYLZecT1ukMIPmYVY4dg3%2BtOVsliwhfm0vssG60cLPCqCQ0wsSDFUMf9fPU2%2BTfxb2sIEAjF1PLaYX60LiEfHBla17%2BXZoD%2Bu3rv31KatoHOD5Ksx0EnyhT59ZS3a2FThJhIWr93zIgPyRZEFv7ktK31sUZlULQVAdT%2FGdPVrdFnzu2dXxTWCf6KYm3bJYJLW5mZ52vKYBKiP1WaZCGDjL6VmfBX1uVNy9%2FFwHuWF5NXFqChlDA781Uv%2FGMsYl52AZ8yzP1cxr8rhDCLtcOfqeXlXGBD%2Fa8ZyyDKpDGTrn%2Fp%2FFpFW6zMkaAhcTZ4FH%2BE09Odtm4kkhlbTcvVs1Q2TWZZfg1kuTlDGiPXb%2B8AYbPoLZhraBmR2spG%2FU5On29Z7GtPOcHkcckKYzXczFWx9jxgOt1hCbk3ml54WveaLMcO%2FWklwh5q1FYYzAoaxJSz9ckgEYJOmret7Exuwpx%2BVfqyq20cg0Y7blMdppBkfxejzjnm85qmMQiFOXJP8xS1gYTs915ytOaj2c01X8TuS3kXvW3j1XsANcu89uNSk4JMtxV2OBv1aXUPBV%2B%2BX8PT54tkRU5Cg%2BPzVF3vAJnj5lGcMPnJ%2BLwGOqUBr7COdYz%2BUnw2k3eZhadCerj240Ea1Kl8Li1%2BlbJhtsrybioa3ekoCCVYQWSJDRUSJjrdU6%2FWipgJi7ooNKS2myKJjGlo7jS2A3FtdHsJA%2FnvyZ9WIa%2BNQX%2FnmNIquR%2FqdcSXI97%2FKuya2o75CtucPBQPNCTHAQC1ZxuwAX3NwMKzTblu1aSNsAr%2B8eguLBBqBDJgjtjCHPYf6xH%2Bv%2FCkoJTv16fk&X-Amz-Signature=9aa77e410259ec76427c28edcbe733a2c2c20f4c5cb5472004f8aaf39327f7a4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYYM2SXR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHO%2BeyqQcEZAp8sBGiS4eLooHpNShUp19BSkmOI%2BF%2BcQIgBvxGrEXsT8V03m8AKeU2cHrRyTHK5c%2B7ZEx0vbnf4W8qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDl3ndSuSmJv6SG%2BnCrcA7qI%2F17sJiXv%2BWyB5yj0QADyPDIetwX0h05VTYLZecT1ukMIPmYVY4dg3%2BtOVsliwhfm0vssG60cLPCqCQ0wsSDFUMf9fPU2%2BTfxb2sIEAjF1PLaYX60LiEfHBla17%2BXZoD%2Bu3rv31KatoHOD5Ksx0EnyhT59ZS3a2FThJhIWr93zIgPyRZEFv7ktK31sUZlULQVAdT%2FGdPVrdFnzu2dXxTWCf6KYm3bJYJLW5mZ52vKYBKiP1WaZCGDjL6VmfBX1uVNy9%2FFwHuWF5NXFqChlDA781Uv%2FGMsYl52AZ8yzP1cxr8rhDCLtcOfqeXlXGBD%2Fa8ZyyDKpDGTrn%2Fp%2FFpFW6zMkaAhcTZ4FH%2BE09Odtm4kkhlbTcvVs1Q2TWZZfg1kuTlDGiPXb%2B8AYbPoLZhraBmR2spG%2FU5On29Z7GtPOcHkcckKYzXczFWx9jxgOt1hCbk3ml54WveaLMcO%2FWklwh5q1FYYzAoaxJSz9ckgEYJOmret7Exuwpx%2BVfqyq20cg0Y7blMdppBkfxejzjnm85qmMQiFOXJP8xS1gYTs915ytOaj2c01X8TuS3kXvW3j1XsANcu89uNSk4JMtxV2OBv1aXUPBV%2B%2BX8PT54tkRU5Cg%2BPzVF3vAJnj5lGcMPnJ%2BLwGOqUBr7COdYz%2BUnw2k3eZhadCerj240Ea1Kl8Li1%2BlbJhtsrybioa3ekoCCVYQWSJDRUSJjrdU6%2FWipgJi7ooNKS2myKJjGlo7jS2A3FtdHsJA%2FnvyZ9WIa%2BNQX%2FnmNIquR%2FqdcSXI97%2FKuya2o75CtucPBQPNCTHAQC1ZxuwAX3NwMKzTblu1aSNsAr%2B8eguLBBqBDJgjtjCHPYf6xH%2Bv%2FCkoJTv16fk&X-Amz-Signature=5cd6beb2bf7fc0ba380edc3a1b1cf0c1dc5c8b48f659037448e785d7a4b40480&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYYM2SXR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHO%2BeyqQcEZAp8sBGiS4eLooHpNShUp19BSkmOI%2BF%2BcQIgBvxGrEXsT8V03m8AKeU2cHrRyTHK5c%2B7ZEx0vbnf4W8qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDl3ndSuSmJv6SG%2BnCrcA7qI%2F17sJiXv%2BWyB5yj0QADyPDIetwX0h05VTYLZecT1ukMIPmYVY4dg3%2BtOVsliwhfm0vssG60cLPCqCQ0wsSDFUMf9fPU2%2BTfxb2sIEAjF1PLaYX60LiEfHBla17%2BXZoD%2Bu3rv31KatoHOD5Ksx0EnyhT59ZS3a2FThJhIWr93zIgPyRZEFv7ktK31sUZlULQVAdT%2FGdPVrdFnzu2dXxTWCf6KYm3bJYJLW5mZ52vKYBKiP1WaZCGDjL6VmfBX1uVNy9%2FFwHuWF5NXFqChlDA781Uv%2FGMsYl52AZ8yzP1cxr8rhDCLtcOfqeXlXGBD%2Fa8ZyyDKpDGTrn%2Fp%2FFpFW6zMkaAhcTZ4FH%2BE09Odtm4kkhlbTcvVs1Q2TWZZfg1kuTlDGiPXb%2B8AYbPoLZhraBmR2spG%2FU5On29Z7GtPOcHkcckKYzXczFWx9jxgOt1hCbk3ml54WveaLMcO%2FWklwh5q1FYYzAoaxJSz9ckgEYJOmret7Exuwpx%2BVfqyq20cg0Y7blMdppBkfxejzjnm85qmMQiFOXJP8xS1gYTs915ytOaj2c01X8TuS3kXvW3j1XsANcu89uNSk4JMtxV2OBv1aXUPBV%2B%2BX8PT54tkRU5Cg%2BPzVF3vAJnj5lGcMPnJ%2BLwGOqUBr7COdYz%2BUnw2k3eZhadCerj240Ea1Kl8Li1%2BlbJhtsrybioa3ekoCCVYQWSJDRUSJjrdU6%2FWipgJi7ooNKS2myKJjGlo7jS2A3FtdHsJA%2FnvyZ9WIa%2BNQX%2FnmNIquR%2FqdcSXI97%2FKuya2o75CtucPBQPNCTHAQC1ZxuwAX3NwMKzTblu1aSNsAr%2B8eguLBBqBDJgjtjCHPYf6xH%2Bv%2FCkoJTv16fk&X-Amz-Signature=59c5ef917458e9f0a440b080192ebb9d10103072448b112066cb84a70f24e13e&X-Amz-SignedHeaders=host&x-id=GetObject)
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


