

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRVZ4YUH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDyyyQ3BVRGZ7VUVv3GQHi6CaxUnD4mwZ3i6tqFYLX5cQIgD7H9iqiG9qnBs9ahPN8XjXV%2FJITTCGcEhiHqRTYlJBMq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDFF9qOIPaEtVZcZp5ircA2f2JVMvH1oJAIp2JO%2F%2BdxaHfo1CCWPyXiawFXdyev%2Bcf8gUFZjx1pAWA1pbvBvPxzCs%2FxWDgByHwuLbsARfwbjIN9lJWX5MvsHvzljQl2em34x2VLBQODqUpIrIlgpsZILZcKl7ze0gZpDgyOGzcfr0cS1TcQ%2BSMHh9RCP%2BUBX%2FSTKioQqhvXUHYSc8Sy43ZbD4E%2BsoGbKMfe5DJwuFRhrvVVmnuf99XR5m8e%2Bdc%2Fq5Ha7F0C2RsHJdEnECYCiSUcp82GS0F6pVQc0OE5z8o%2Ff%2B%2FpMcEB91ycymuQBM8mfYVG79p8Cs0zltZwxAhdivM9DauHKRRMZGXJ97n3p%2BrKLHDq6nb0syIo7c5O0TyPNEeSCvLFzY%2Fm5c7oyJrVDLCEOykKeiuux2mWMDJJe%2FDLFrGQLCBXx64L0WbQsymAFzOX2kVf7pXwANcDbCCsWQVf8hIXbRJsFrLRxo%2FNnhSGSfPst9FjEPbemaTQ%2FSBdUrA9DT25uITGzPn0XWyYn6JI2M25afvXX786H0hAxOqjA7MgJTj4xuKmhHIfT%2BXf%2Fp4oyUu1zoebsX6sk18Vyg51D0b9UZlrsgge0kaNaWWBkJpRv8nwHGZal2o80%2BBerDHV35NyGJsgbHM0r0MMCDhL0GOqUBCQFSYq5bRriauyr5gd3IlmgADHnp0vm5tU22x1YoHlxPKLzdyvypcqsIDjjiQknZ64W5ng9DAIOkBTad5X%2F00t8DMTeINNQIa45wsrQERpG%2BpMj5oXYoqVH72yKgzcbHzCZyvo%2B6yVqt7N%2FKJVjRE5FqKsSY1lkDc3cO7NITrjpiLHRVWl5YA04FiN24yNs6GTte9wbmuExfgDhLfxfamElVffkF&X-Amz-Signature=86b74f6bc00f3e9f6d75b61e12f0c1230d09475dcf2d0549ab0bd97c78e19e6f&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOFSSG3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCICcnwvPGfsgeYOTNosH%2BwGs1SCbBcIKTeBKyML3fD%2B65AiEAvMoJPF%2Ba9FjWrzoVQiDFyQ4eWFs6YP%2FRaaiMXb7G1OUq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDMA%2Fca86AfD3vnxchSrcA1SxjZiufTZokN8gchcIlT46qHiZdxktOaYtMpHzVnWnXXue%2BzujuhBweuP%2Bk42samPwHgfhdtnIkzL0ntuMx5e2W4%2Fw1cmeguQoiAkBYcJwwrslnTnHb%2FGssHNj%2Bt8o14CjFDM6f6PwhnLKXm%2BYTSQsXtC5ufJ2wI%2BZPMTIEjxBLxTQnC077ZIeNzVekLslDI3B8CkUiDR9BAFbYBkvkwGdiVKzfGIU4KC5XrugphqfVQH%2BHhmhEos7H6YM%2FOpNQIXYFwB%2BkaL5bURcNO0tmppHpID9LeEQBjuzfTEGDzy5quuUInXkVYpouGjqUHW%2B0ZHZXIfHMXPtNZVWisgpEfJ48cwPXkhzVVhVEoINOc5e%2BwLESUVGS6rNglBMiZK80RoQ9meXgNtpbRRU1UTg5wjLDWenBZI5UI6VWtOw9pjeJWoBPDHS5Vh5FGjdxFWnAPNbg1lZn2sf%2BwZmxpXzR5cwKucZCoKcu2FnWTOUrC3g6KusM5dopXi9Ht273OpvWqnzqgMyKgz15q07KChUUelMklFcsqyNEEKXEzS9fbdp8p7AS3026PH9nCCSoe6tJu0mXXLk9oLEoxuLeMw0q9xjnbg%2FQAKJ76hummdLU1KbLNZllSjNPswgvZLNMKOEhL0GOqUBfI9lPobTOtktPQAJf3DO865HRKO8ofuuUaRWayL%2BIa1dUK%2BTdCWu4GzluDWjVFZY6a90V9%2FNUY43HRlLQkDJwRk68DlAQ%2FuNOw6Uj6amQBKr7t8XYyyekgibl8NAMf6EweKi6krpPdayVWbNfwGWrbSC%2FbIVk2MyKq0dTKwq70ZelEsN1Ebj6If2Pj5hAOfevsdPQFXkUENtUJcfFQ4Dlu92gZoe&X-Amz-Signature=1e7d947289233efe30309c4fdf01595f497b10728cd56bb802aa3b668fac192b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOFSSG3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCICcnwvPGfsgeYOTNosH%2BwGs1SCbBcIKTeBKyML3fD%2B65AiEAvMoJPF%2Ba9FjWrzoVQiDFyQ4eWFs6YP%2FRaaiMXb7G1OUq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDMA%2Fca86AfD3vnxchSrcA1SxjZiufTZokN8gchcIlT46qHiZdxktOaYtMpHzVnWnXXue%2BzujuhBweuP%2Bk42samPwHgfhdtnIkzL0ntuMx5e2W4%2Fw1cmeguQoiAkBYcJwwrslnTnHb%2FGssHNj%2Bt8o14CjFDM6f6PwhnLKXm%2BYTSQsXtC5ufJ2wI%2BZPMTIEjxBLxTQnC077ZIeNzVekLslDI3B8CkUiDR9BAFbYBkvkwGdiVKzfGIU4KC5XrugphqfVQH%2BHhmhEos7H6YM%2FOpNQIXYFwB%2BkaL5bURcNO0tmppHpID9LeEQBjuzfTEGDzy5quuUInXkVYpouGjqUHW%2B0ZHZXIfHMXPtNZVWisgpEfJ48cwPXkhzVVhVEoINOc5e%2BwLESUVGS6rNglBMiZK80RoQ9meXgNtpbRRU1UTg5wjLDWenBZI5UI6VWtOw9pjeJWoBPDHS5Vh5FGjdxFWnAPNbg1lZn2sf%2BwZmxpXzR5cwKucZCoKcu2FnWTOUrC3g6KusM5dopXi9Ht273OpvWqnzqgMyKgz15q07KChUUelMklFcsqyNEEKXEzS9fbdp8p7AS3026PH9nCCSoe6tJu0mXXLk9oLEoxuLeMw0q9xjnbg%2FQAKJ76hummdLU1KbLNZllSjNPswgvZLNMKOEhL0GOqUBfI9lPobTOtktPQAJf3DO865HRKO8ofuuUaRWayL%2BIa1dUK%2BTdCWu4GzluDWjVFZY6a90V9%2FNUY43HRlLQkDJwRk68DlAQ%2FuNOw6Uj6amQBKr7t8XYyyekgibl8NAMf6EweKi6krpPdayVWbNfwGWrbSC%2FbIVk2MyKq0dTKwq70ZelEsN1Ebj6If2Pj5hAOfevsdPQFXkUENtUJcfFQ4Dlu92gZoe&X-Amz-Signature=b1066f41143908307c7b5c58b773f9b35bca2b459b275ebed7ca9ed92b5fcfe0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOFSSG3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCICcnwvPGfsgeYOTNosH%2BwGs1SCbBcIKTeBKyML3fD%2B65AiEAvMoJPF%2Ba9FjWrzoVQiDFyQ4eWFs6YP%2FRaaiMXb7G1OUq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDMA%2Fca86AfD3vnxchSrcA1SxjZiufTZokN8gchcIlT46qHiZdxktOaYtMpHzVnWnXXue%2BzujuhBweuP%2Bk42samPwHgfhdtnIkzL0ntuMx5e2W4%2Fw1cmeguQoiAkBYcJwwrslnTnHb%2FGssHNj%2Bt8o14CjFDM6f6PwhnLKXm%2BYTSQsXtC5ufJ2wI%2BZPMTIEjxBLxTQnC077ZIeNzVekLslDI3B8CkUiDR9BAFbYBkvkwGdiVKzfGIU4KC5XrugphqfVQH%2BHhmhEos7H6YM%2FOpNQIXYFwB%2BkaL5bURcNO0tmppHpID9LeEQBjuzfTEGDzy5quuUInXkVYpouGjqUHW%2B0ZHZXIfHMXPtNZVWisgpEfJ48cwPXkhzVVhVEoINOc5e%2BwLESUVGS6rNglBMiZK80RoQ9meXgNtpbRRU1UTg5wjLDWenBZI5UI6VWtOw9pjeJWoBPDHS5Vh5FGjdxFWnAPNbg1lZn2sf%2BwZmxpXzR5cwKucZCoKcu2FnWTOUrC3g6KusM5dopXi9Ht273OpvWqnzqgMyKgz15q07KChUUelMklFcsqyNEEKXEzS9fbdp8p7AS3026PH9nCCSoe6tJu0mXXLk9oLEoxuLeMw0q9xjnbg%2FQAKJ76hummdLU1KbLNZllSjNPswgvZLNMKOEhL0GOqUBfI9lPobTOtktPQAJf3DO865HRKO8ofuuUaRWayL%2BIa1dUK%2BTdCWu4GzluDWjVFZY6a90V9%2FNUY43HRlLQkDJwRk68DlAQ%2FuNOw6Uj6amQBKr7t8XYyyekgibl8NAMf6EweKi6krpPdayVWbNfwGWrbSC%2FbIVk2MyKq0dTKwq70ZelEsN1Ebj6If2Pj5hAOfevsdPQFXkUENtUJcfFQ4Dlu92gZoe&X-Amz-Signature=32e0cfe95ffd812fd540403fd19240eddd03e2702d5a6e1656861a792faa5229&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOFSSG3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCICcnwvPGfsgeYOTNosH%2BwGs1SCbBcIKTeBKyML3fD%2B65AiEAvMoJPF%2Ba9FjWrzoVQiDFyQ4eWFs6YP%2FRaaiMXb7G1OUq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDMA%2Fca86AfD3vnxchSrcA1SxjZiufTZokN8gchcIlT46qHiZdxktOaYtMpHzVnWnXXue%2BzujuhBweuP%2Bk42samPwHgfhdtnIkzL0ntuMx5e2W4%2Fw1cmeguQoiAkBYcJwwrslnTnHb%2FGssHNj%2Bt8o14CjFDM6f6PwhnLKXm%2BYTSQsXtC5ufJ2wI%2BZPMTIEjxBLxTQnC077ZIeNzVekLslDI3B8CkUiDR9BAFbYBkvkwGdiVKzfGIU4KC5XrugphqfVQH%2BHhmhEos7H6YM%2FOpNQIXYFwB%2BkaL5bURcNO0tmppHpID9LeEQBjuzfTEGDzy5quuUInXkVYpouGjqUHW%2B0ZHZXIfHMXPtNZVWisgpEfJ48cwPXkhzVVhVEoINOc5e%2BwLESUVGS6rNglBMiZK80RoQ9meXgNtpbRRU1UTg5wjLDWenBZI5UI6VWtOw9pjeJWoBPDHS5Vh5FGjdxFWnAPNbg1lZn2sf%2BwZmxpXzR5cwKucZCoKcu2FnWTOUrC3g6KusM5dopXi9Ht273OpvWqnzqgMyKgz15q07KChUUelMklFcsqyNEEKXEzS9fbdp8p7AS3026PH9nCCSoe6tJu0mXXLk9oLEoxuLeMw0q9xjnbg%2FQAKJ76hummdLU1KbLNZllSjNPswgvZLNMKOEhL0GOqUBfI9lPobTOtktPQAJf3DO865HRKO8ofuuUaRWayL%2BIa1dUK%2BTdCWu4GzluDWjVFZY6a90V9%2FNUY43HRlLQkDJwRk68DlAQ%2FuNOw6Uj6amQBKr7t8XYyyekgibl8NAMf6EweKi6krpPdayVWbNfwGWrbSC%2FbIVk2MyKq0dTKwq70ZelEsN1Ebj6If2Pj5hAOfevsdPQFXkUENtUJcfFQ4Dlu92gZoe&X-Amz-Signature=bc3a6a411d607d87f47db47c1b3391ea6832e44bf10c3c6552a67518c4236851&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOFSSG3W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCICcnwvPGfsgeYOTNosH%2BwGs1SCbBcIKTeBKyML3fD%2B65AiEAvMoJPF%2Ba9FjWrzoVQiDFyQ4eWFs6YP%2FRaaiMXb7G1OUq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDMA%2Fca86AfD3vnxchSrcA1SxjZiufTZokN8gchcIlT46qHiZdxktOaYtMpHzVnWnXXue%2BzujuhBweuP%2Bk42samPwHgfhdtnIkzL0ntuMx5e2W4%2Fw1cmeguQoiAkBYcJwwrslnTnHb%2FGssHNj%2Bt8o14CjFDM6f6PwhnLKXm%2BYTSQsXtC5ufJ2wI%2BZPMTIEjxBLxTQnC077ZIeNzVekLslDI3B8CkUiDR9BAFbYBkvkwGdiVKzfGIU4KC5XrugphqfVQH%2BHhmhEos7H6YM%2FOpNQIXYFwB%2BkaL5bURcNO0tmppHpID9LeEQBjuzfTEGDzy5quuUInXkVYpouGjqUHW%2B0ZHZXIfHMXPtNZVWisgpEfJ48cwPXkhzVVhVEoINOc5e%2BwLESUVGS6rNglBMiZK80RoQ9meXgNtpbRRU1UTg5wjLDWenBZI5UI6VWtOw9pjeJWoBPDHS5Vh5FGjdxFWnAPNbg1lZn2sf%2BwZmxpXzR5cwKucZCoKcu2FnWTOUrC3g6KusM5dopXi9Ht273OpvWqnzqgMyKgz15q07KChUUelMklFcsqyNEEKXEzS9fbdp8p7AS3026PH9nCCSoe6tJu0mXXLk9oLEoxuLeMw0q9xjnbg%2FQAKJ76hummdLU1KbLNZllSjNPswgvZLNMKOEhL0GOqUBfI9lPobTOtktPQAJf3DO865HRKO8ofuuUaRWayL%2BIa1dUK%2BTdCWu4GzluDWjVFZY6a90V9%2FNUY43HRlLQkDJwRk68DlAQ%2FuNOw6Uj6amQBKr7t8XYyyekgibl8NAMf6EweKi6krpPdayVWbNfwGWrbSC%2FbIVk2MyKq0dTKwq70ZelEsN1Ebj6If2Pj5hAOfevsdPQFXkUENtUJcfFQ4Dlu92gZoe&X-Amz-Signature=2179cef83ac315b2233bbcfd9d00994462954c7b81f06acaafc81fc645fcb692&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRVZ4YUH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDyyyQ3BVRGZ7VUVv3GQHi6CaxUnD4mwZ3i6tqFYLX5cQIgD7H9iqiG9qnBs9ahPN8XjXV%2FJITTCGcEhiHqRTYlJBMq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDFF9qOIPaEtVZcZp5ircA2f2JVMvH1oJAIp2JO%2F%2BdxaHfo1CCWPyXiawFXdyev%2Bcf8gUFZjx1pAWA1pbvBvPxzCs%2FxWDgByHwuLbsARfwbjIN9lJWX5MvsHvzljQl2em34x2VLBQODqUpIrIlgpsZILZcKl7ze0gZpDgyOGzcfr0cS1TcQ%2BSMHh9RCP%2BUBX%2FSTKioQqhvXUHYSc8Sy43ZbD4E%2BsoGbKMfe5DJwuFRhrvVVmnuf99XR5m8e%2Bdc%2Fq5Ha7F0C2RsHJdEnECYCiSUcp82GS0F6pVQc0OE5z8o%2Ff%2B%2FpMcEB91ycymuQBM8mfYVG79p8Cs0zltZwxAhdivM9DauHKRRMZGXJ97n3p%2BrKLHDq6nb0syIo7c5O0TyPNEeSCvLFzY%2Fm5c7oyJrVDLCEOykKeiuux2mWMDJJe%2FDLFrGQLCBXx64L0WbQsymAFzOX2kVf7pXwANcDbCCsWQVf8hIXbRJsFrLRxo%2FNnhSGSfPst9FjEPbemaTQ%2FSBdUrA9DT25uITGzPn0XWyYn6JI2M25afvXX786H0hAxOqjA7MgJTj4xuKmhHIfT%2BXf%2Fp4oyUu1zoebsX6sk18Vyg51D0b9UZlrsgge0kaNaWWBkJpRv8nwHGZal2o80%2BBerDHV35NyGJsgbHM0r0MMCDhL0GOqUBCQFSYq5bRriauyr5gd3IlmgADHnp0vm5tU22x1YoHlxPKLzdyvypcqsIDjjiQknZ64W5ng9DAIOkBTad5X%2F00t8DMTeINNQIa45wsrQERpG%2BpMj5oXYoqVH72yKgzcbHzCZyvo%2B6yVqt7N%2FKJVjRE5FqKsSY1lkDc3cO7NITrjpiLHRVWl5YA04FiN24yNs6GTte9wbmuExfgDhLfxfamElVffkF&X-Amz-Signature=45fc283f10ad6dc42da2d2978f39266a4627c3e35e92cb3234b191f42d077165&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRVZ4YUH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDyyyQ3BVRGZ7VUVv3GQHi6CaxUnD4mwZ3i6tqFYLX5cQIgD7H9iqiG9qnBs9ahPN8XjXV%2FJITTCGcEhiHqRTYlJBMq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDFF9qOIPaEtVZcZp5ircA2f2JVMvH1oJAIp2JO%2F%2BdxaHfo1CCWPyXiawFXdyev%2Bcf8gUFZjx1pAWA1pbvBvPxzCs%2FxWDgByHwuLbsARfwbjIN9lJWX5MvsHvzljQl2em34x2VLBQODqUpIrIlgpsZILZcKl7ze0gZpDgyOGzcfr0cS1TcQ%2BSMHh9RCP%2BUBX%2FSTKioQqhvXUHYSc8Sy43ZbD4E%2BsoGbKMfe5DJwuFRhrvVVmnuf99XR5m8e%2Bdc%2Fq5Ha7F0C2RsHJdEnECYCiSUcp82GS0F6pVQc0OE5z8o%2Ff%2B%2FpMcEB91ycymuQBM8mfYVG79p8Cs0zltZwxAhdivM9DauHKRRMZGXJ97n3p%2BrKLHDq6nb0syIo7c5O0TyPNEeSCvLFzY%2Fm5c7oyJrVDLCEOykKeiuux2mWMDJJe%2FDLFrGQLCBXx64L0WbQsymAFzOX2kVf7pXwANcDbCCsWQVf8hIXbRJsFrLRxo%2FNnhSGSfPst9FjEPbemaTQ%2FSBdUrA9DT25uITGzPn0XWyYn6JI2M25afvXX786H0hAxOqjA7MgJTj4xuKmhHIfT%2BXf%2Fp4oyUu1zoebsX6sk18Vyg51D0b9UZlrsgge0kaNaWWBkJpRv8nwHGZal2o80%2BBerDHV35NyGJsgbHM0r0MMCDhL0GOqUBCQFSYq5bRriauyr5gd3IlmgADHnp0vm5tU22x1YoHlxPKLzdyvypcqsIDjjiQknZ64W5ng9DAIOkBTad5X%2F00t8DMTeINNQIa45wsrQERpG%2BpMj5oXYoqVH72yKgzcbHzCZyvo%2B6yVqt7N%2FKJVjRE5FqKsSY1lkDc3cO7NITrjpiLHRVWl5YA04FiN24yNs6GTte9wbmuExfgDhLfxfamElVffkF&X-Amz-Signature=e0cdcc9b06b44a730f54cb4eb5f14278d9e8e6207689d2dbf2bbeaa19e520981&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRVZ4YUH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDyyyQ3BVRGZ7VUVv3GQHi6CaxUnD4mwZ3i6tqFYLX5cQIgD7H9iqiG9qnBs9ahPN8XjXV%2FJITTCGcEhiHqRTYlJBMq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDFF9qOIPaEtVZcZp5ircA2f2JVMvH1oJAIp2JO%2F%2BdxaHfo1CCWPyXiawFXdyev%2Bcf8gUFZjx1pAWA1pbvBvPxzCs%2FxWDgByHwuLbsARfwbjIN9lJWX5MvsHvzljQl2em34x2VLBQODqUpIrIlgpsZILZcKl7ze0gZpDgyOGzcfr0cS1TcQ%2BSMHh9RCP%2BUBX%2FSTKioQqhvXUHYSc8Sy43ZbD4E%2BsoGbKMfe5DJwuFRhrvVVmnuf99XR5m8e%2Bdc%2Fq5Ha7F0C2RsHJdEnECYCiSUcp82GS0F6pVQc0OE5z8o%2Ff%2B%2FpMcEB91ycymuQBM8mfYVG79p8Cs0zltZwxAhdivM9DauHKRRMZGXJ97n3p%2BrKLHDq6nb0syIo7c5O0TyPNEeSCvLFzY%2Fm5c7oyJrVDLCEOykKeiuux2mWMDJJe%2FDLFrGQLCBXx64L0WbQsymAFzOX2kVf7pXwANcDbCCsWQVf8hIXbRJsFrLRxo%2FNnhSGSfPst9FjEPbemaTQ%2FSBdUrA9DT25uITGzPn0XWyYn6JI2M25afvXX786H0hAxOqjA7MgJTj4xuKmhHIfT%2BXf%2Fp4oyUu1zoebsX6sk18Vyg51D0b9UZlrsgge0kaNaWWBkJpRv8nwHGZal2o80%2BBerDHV35NyGJsgbHM0r0MMCDhL0GOqUBCQFSYq5bRriauyr5gd3IlmgADHnp0vm5tU22x1YoHlxPKLzdyvypcqsIDjjiQknZ64W5ng9DAIOkBTad5X%2F00t8DMTeINNQIa45wsrQERpG%2BpMj5oXYoqVH72yKgzcbHzCZyvo%2B6yVqt7N%2FKJVjRE5FqKsSY1lkDc3cO7NITrjpiLHRVWl5YA04FiN24yNs6GTte9wbmuExfgDhLfxfamElVffkF&X-Amz-Signature=4eb373bbd45353571b71321f9a2c283576608871c42d241fd0e531bfb190c54d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRVZ4YUH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDyyyQ3BVRGZ7VUVv3GQHi6CaxUnD4mwZ3i6tqFYLX5cQIgD7H9iqiG9qnBs9ahPN8XjXV%2FJITTCGcEhiHqRTYlJBMq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDFF9qOIPaEtVZcZp5ircA2f2JVMvH1oJAIp2JO%2F%2BdxaHfo1CCWPyXiawFXdyev%2Bcf8gUFZjx1pAWA1pbvBvPxzCs%2FxWDgByHwuLbsARfwbjIN9lJWX5MvsHvzljQl2em34x2VLBQODqUpIrIlgpsZILZcKl7ze0gZpDgyOGzcfr0cS1TcQ%2BSMHh9RCP%2BUBX%2FSTKioQqhvXUHYSc8Sy43ZbD4E%2BsoGbKMfe5DJwuFRhrvVVmnuf99XR5m8e%2Bdc%2Fq5Ha7F0C2RsHJdEnECYCiSUcp82GS0F6pVQc0OE5z8o%2Ff%2B%2FpMcEB91ycymuQBM8mfYVG79p8Cs0zltZwxAhdivM9DauHKRRMZGXJ97n3p%2BrKLHDq6nb0syIo7c5O0TyPNEeSCvLFzY%2Fm5c7oyJrVDLCEOykKeiuux2mWMDJJe%2FDLFrGQLCBXx64L0WbQsymAFzOX2kVf7pXwANcDbCCsWQVf8hIXbRJsFrLRxo%2FNnhSGSfPst9FjEPbemaTQ%2FSBdUrA9DT25uITGzPn0XWyYn6JI2M25afvXX786H0hAxOqjA7MgJTj4xuKmhHIfT%2BXf%2Fp4oyUu1zoebsX6sk18Vyg51D0b9UZlrsgge0kaNaWWBkJpRv8nwHGZal2o80%2BBerDHV35NyGJsgbHM0r0MMCDhL0GOqUBCQFSYq5bRriauyr5gd3IlmgADHnp0vm5tU22x1YoHlxPKLzdyvypcqsIDjjiQknZ64W5ng9DAIOkBTad5X%2F00t8DMTeINNQIa45wsrQERpG%2BpMj5oXYoqVH72yKgzcbHzCZyvo%2B6yVqt7N%2FKJVjRE5FqKsSY1lkDc3cO7NITrjpiLHRVWl5YA04FiN24yNs6GTte9wbmuExfgDhLfxfamElVffkF&X-Amz-Signature=018606c0b500204fdc458998970dd8ff06c86c33949d4b5e07e304182252e0d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRVZ4YUH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDyyyQ3BVRGZ7VUVv3GQHi6CaxUnD4mwZ3i6tqFYLX5cQIgD7H9iqiG9qnBs9ahPN8XjXV%2FJITTCGcEhiHqRTYlJBMq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDFF9qOIPaEtVZcZp5ircA2f2JVMvH1oJAIp2JO%2F%2BdxaHfo1CCWPyXiawFXdyev%2Bcf8gUFZjx1pAWA1pbvBvPxzCs%2FxWDgByHwuLbsARfwbjIN9lJWX5MvsHvzljQl2em34x2VLBQODqUpIrIlgpsZILZcKl7ze0gZpDgyOGzcfr0cS1TcQ%2BSMHh9RCP%2BUBX%2FSTKioQqhvXUHYSc8Sy43ZbD4E%2BsoGbKMfe5DJwuFRhrvVVmnuf99XR5m8e%2Bdc%2Fq5Ha7F0C2RsHJdEnECYCiSUcp82GS0F6pVQc0OE5z8o%2Ff%2B%2FpMcEB91ycymuQBM8mfYVG79p8Cs0zltZwxAhdivM9DauHKRRMZGXJ97n3p%2BrKLHDq6nb0syIo7c5O0TyPNEeSCvLFzY%2Fm5c7oyJrVDLCEOykKeiuux2mWMDJJe%2FDLFrGQLCBXx64L0WbQsymAFzOX2kVf7pXwANcDbCCsWQVf8hIXbRJsFrLRxo%2FNnhSGSfPst9FjEPbemaTQ%2FSBdUrA9DT25uITGzPn0XWyYn6JI2M25afvXX786H0hAxOqjA7MgJTj4xuKmhHIfT%2BXf%2Fp4oyUu1zoebsX6sk18Vyg51D0b9UZlrsgge0kaNaWWBkJpRv8nwHGZal2o80%2BBerDHV35NyGJsgbHM0r0MMCDhL0GOqUBCQFSYq5bRriauyr5gd3IlmgADHnp0vm5tU22x1YoHlxPKLzdyvypcqsIDjjiQknZ64W5ng9DAIOkBTad5X%2F00t8DMTeINNQIa45wsrQERpG%2BpMj5oXYoqVH72yKgzcbHzCZyvo%2B6yVqt7N%2FKJVjRE5FqKsSY1lkDc3cO7NITrjpiLHRVWl5YA04FiN24yNs6GTte9wbmuExfgDhLfxfamElVffkF&X-Amz-Signature=6abd601d490c73edc5faf254f5f775773222b911392edb529f7bfcb7681894af&X-Amz-SignedHeaders=host&x-id=GetObject)
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


