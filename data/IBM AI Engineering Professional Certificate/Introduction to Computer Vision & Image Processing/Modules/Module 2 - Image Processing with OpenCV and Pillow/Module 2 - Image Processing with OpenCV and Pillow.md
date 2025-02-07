

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZB6MIM4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDVjD3d3cPQQQHsEeBnKe3Xufq0IyoUHqWRSTbi9qWTHgIhAMCXuJGPY4kPDXch7kucg0TRdfinPz5tqFOhYbVT0j%2BSKv8DCG8QABoMNjM3NDIzMTgzODA1Igzn8qBocCSBSsIPcoMq3APEOwTJzk3Vpgv03naJX%2B89TJT4Qxf0%2BpCEPFrDCm6jrjXONYS5p%2FLMYxwaErTaSMQjzNZBBF4HT0bW1L614TO1UNJt4nhYVOryr984CevzyZ%2BphRfFcFe%2B8btFnHog3U%2F5%2FKprORWmA1o0MwKbmkdcHad9LUK0JgnVrU7qXHhwt6p9kJJapWTlJkpwTU4f4tbQJfiMbYPcWbA3ioJvyUraTKGjMdleCroAKG9Ni68MWJYeH0KdSJojxRnwIG7b3el%2FJtEpHErTvhfdHcbHWbAa80TWidR%2Bm8QgHhe0gZIrAdZNWh6R93dQ6zoVqzYTBhqOqjGosT7NQDOrz%2FwNOWzvM8ZlB6dcMASUaEGrA4%2F8UzyIgwJTUiQl11y%2FbThMA0bwqyk0FF4mNz%2Bei5r7jJaKYVYZ9M8q0WA5JihTYdVnQQs4t8UjrJ%2BQrUIHmE6Zy3XgMZRrlZd588RzOKgvgYPo2Uu9s78edeZU5ax0MWEGa78hOwUjlPhjBTEcoXu%2FhK%2BYLKsegQXPKK2yO973JGM8TZsEbjJ0YRi49Sy2gSC%2FPcb8WhwsDW2HOSj6dOCa6hEKluk%2BsPv%2FA6k8jXz2BwFDJipuxVuOypzjt0McM%2B2Mn5rQrqrvOv0t9MsTmDDivpa9BjqkAfR8pOS5OTO4oSQTlPWut1yaAhR13UuDfsx%2FU1eizGoWwk8ihLgYRm1365UGTby0Ma2DaXJnDu%2BlrPO8RvjZxmj8LYMjPTvW1YZVZEBjLkiXdsxWLORVyKmC%2FpaXO%2BzGEagDVPfEKjRzJzRHZn%2B6el87VZ2irjO2MDnwiG62u%2FTHIMptF%2BR1zjXHnToy07eE%2BAOGhDjVybHDY2CNztI0d3yCHkbO&X-Amz-Signature=d20aec887e9d40af52c1dfbcdab0dd7df9c37f45d0eb3b2b83605b8f2c2dc32f&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXIA33Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIBvjq1pMna7Z0mC3pbMaH2aaBgAIs45buauXSCfsYzQIAiEAyMuVv27FUj1PT3In5IkKk2m7Da2mwkqFBvWwWzXxFqAq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJrKcCBNPeLSubkcRircA53hXnSxAT%2BPBVc4r%2FjcMPGMeP1prw0mnzkpdqRcw6pMVNOFhs6%2FfE8o4R2GcX0NYRUzNo63JyXqRXJC%2FEIlAr1ApIQd60FKxp0cfmL53tdp8Srq5qVJpTm%2FcppyH8W8R60Ghg8FmsVq0MqoEL6tu5GhK7MNvHTm6%2F1CvOEgYwVMmOtYJ%2BRCqJCYKy8oqTKh3koHQyUEInXHBHYBhpDtknw3krMLLySmQbCMjOwFcvJtfx9L4PeMShCX%2B5xN%2Fe6%2BZJut9RqAz6Y6KUyrqCMYfFrcRf0vQx8jdFH0ELtNfwQKpapJNeo9nSWQVC4wlf0z5GIab0jOREAfDGS%2FAxgYAPo1C6uKDMhA%2BWMoDdWOioOaOFn8eI%2FkvyjhxI2d5nErXmjwmPpozkJubO7bj0vI1Ber68NUeBf48GpdwT33cMdRnAh%2FkL96VpPDbjQSxTILwUBaTgH5widH%2BjO09kvff24I1oUTztyqq4%2B%2BFs4IpAsq%2B4teRgjaRFmAbEbtREgrU%2BJIzolKGREHkIY0XwncwTwl2XGNKkPC%2FZcFf6eRqXFEiWBqNufW5KyU4qdpPu00rvHE2l7zWmwQwIJqU99yih9h%2FBWuxQrzC6pR38Ih6MjYLJ%2Fjb1v3Pr8DIuz2MKy%2Flr0GOqUB5LFbQiSw3z9n6KpIppsMGjfQnA0f9AJz3kO6GaX67%2F0idcLPBAFHW2bkTCMmit6m%2FUBu1Cm4cjZPSBJyFL69v7c7TzxSbyPPru3bZUVEuS2p8AxbRC2UP0PW2eohoZkxn1TL0L78VNpKlge1jMzqRF4zbOwEnKWAFbzeyGWRYJuEWWJCDs9IO4So70TssorIKsSvc2rcyUj2pO2LDQwVV4KVAPtW&X-Amz-Signature=82c698ba8f4284a909486ae6b63120cb2ce5799ca443297ba4efca3735f93486&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXIA33Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIBvjq1pMna7Z0mC3pbMaH2aaBgAIs45buauXSCfsYzQIAiEAyMuVv27FUj1PT3In5IkKk2m7Da2mwkqFBvWwWzXxFqAq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJrKcCBNPeLSubkcRircA53hXnSxAT%2BPBVc4r%2FjcMPGMeP1prw0mnzkpdqRcw6pMVNOFhs6%2FfE8o4R2GcX0NYRUzNo63JyXqRXJC%2FEIlAr1ApIQd60FKxp0cfmL53tdp8Srq5qVJpTm%2FcppyH8W8R60Ghg8FmsVq0MqoEL6tu5GhK7MNvHTm6%2F1CvOEgYwVMmOtYJ%2BRCqJCYKy8oqTKh3koHQyUEInXHBHYBhpDtknw3krMLLySmQbCMjOwFcvJtfx9L4PeMShCX%2B5xN%2Fe6%2BZJut9RqAz6Y6KUyrqCMYfFrcRf0vQx8jdFH0ELtNfwQKpapJNeo9nSWQVC4wlf0z5GIab0jOREAfDGS%2FAxgYAPo1C6uKDMhA%2BWMoDdWOioOaOFn8eI%2FkvyjhxI2d5nErXmjwmPpozkJubO7bj0vI1Ber68NUeBf48GpdwT33cMdRnAh%2FkL96VpPDbjQSxTILwUBaTgH5widH%2BjO09kvff24I1oUTztyqq4%2B%2BFs4IpAsq%2B4teRgjaRFmAbEbtREgrU%2BJIzolKGREHkIY0XwncwTwl2XGNKkPC%2FZcFf6eRqXFEiWBqNufW5KyU4qdpPu00rvHE2l7zWmwQwIJqU99yih9h%2FBWuxQrzC6pR38Ih6MjYLJ%2Fjb1v3Pr8DIuz2MKy%2Flr0GOqUB5LFbQiSw3z9n6KpIppsMGjfQnA0f9AJz3kO6GaX67%2F0idcLPBAFHW2bkTCMmit6m%2FUBu1Cm4cjZPSBJyFL69v7c7TzxSbyPPru3bZUVEuS2p8AxbRC2UP0PW2eohoZkxn1TL0L78VNpKlge1jMzqRF4zbOwEnKWAFbzeyGWRYJuEWWJCDs9IO4So70TssorIKsSvc2rcyUj2pO2LDQwVV4KVAPtW&X-Amz-Signature=9803ed978cca4b3bf187bf1fa0ac5aa29c04fb1f22c7639c3d56ab3a961443bb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXIA33Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIBvjq1pMna7Z0mC3pbMaH2aaBgAIs45buauXSCfsYzQIAiEAyMuVv27FUj1PT3In5IkKk2m7Da2mwkqFBvWwWzXxFqAq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJrKcCBNPeLSubkcRircA53hXnSxAT%2BPBVc4r%2FjcMPGMeP1prw0mnzkpdqRcw6pMVNOFhs6%2FfE8o4R2GcX0NYRUzNo63JyXqRXJC%2FEIlAr1ApIQd60FKxp0cfmL53tdp8Srq5qVJpTm%2FcppyH8W8R60Ghg8FmsVq0MqoEL6tu5GhK7MNvHTm6%2F1CvOEgYwVMmOtYJ%2BRCqJCYKy8oqTKh3koHQyUEInXHBHYBhpDtknw3krMLLySmQbCMjOwFcvJtfx9L4PeMShCX%2B5xN%2Fe6%2BZJut9RqAz6Y6KUyrqCMYfFrcRf0vQx8jdFH0ELtNfwQKpapJNeo9nSWQVC4wlf0z5GIab0jOREAfDGS%2FAxgYAPo1C6uKDMhA%2BWMoDdWOioOaOFn8eI%2FkvyjhxI2d5nErXmjwmPpozkJubO7bj0vI1Ber68NUeBf48GpdwT33cMdRnAh%2FkL96VpPDbjQSxTILwUBaTgH5widH%2BjO09kvff24I1oUTztyqq4%2B%2BFs4IpAsq%2B4teRgjaRFmAbEbtREgrU%2BJIzolKGREHkIY0XwncwTwl2XGNKkPC%2FZcFf6eRqXFEiWBqNufW5KyU4qdpPu00rvHE2l7zWmwQwIJqU99yih9h%2FBWuxQrzC6pR38Ih6MjYLJ%2Fjb1v3Pr8DIuz2MKy%2Flr0GOqUB5LFbQiSw3z9n6KpIppsMGjfQnA0f9AJz3kO6GaX67%2F0idcLPBAFHW2bkTCMmit6m%2FUBu1Cm4cjZPSBJyFL69v7c7TzxSbyPPru3bZUVEuS2p8AxbRC2UP0PW2eohoZkxn1TL0L78VNpKlge1jMzqRF4zbOwEnKWAFbzeyGWRYJuEWWJCDs9IO4So70TssorIKsSvc2rcyUj2pO2LDQwVV4KVAPtW&X-Amz-Signature=fadfcaefe1359ac95c674f064baf4128b0e6194f1e7ebb73683383ef1381c524&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXIA33Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIBvjq1pMna7Z0mC3pbMaH2aaBgAIs45buauXSCfsYzQIAiEAyMuVv27FUj1PT3In5IkKk2m7Da2mwkqFBvWwWzXxFqAq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJrKcCBNPeLSubkcRircA53hXnSxAT%2BPBVc4r%2FjcMPGMeP1prw0mnzkpdqRcw6pMVNOFhs6%2FfE8o4R2GcX0NYRUzNo63JyXqRXJC%2FEIlAr1ApIQd60FKxp0cfmL53tdp8Srq5qVJpTm%2FcppyH8W8R60Ghg8FmsVq0MqoEL6tu5GhK7MNvHTm6%2F1CvOEgYwVMmOtYJ%2BRCqJCYKy8oqTKh3koHQyUEInXHBHYBhpDtknw3krMLLySmQbCMjOwFcvJtfx9L4PeMShCX%2B5xN%2Fe6%2BZJut9RqAz6Y6KUyrqCMYfFrcRf0vQx8jdFH0ELtNfwQKpapJNeo9nSWQVC4wlf0z5GIab0jOREAfDGS%2FAxgYAPo1C6uKDMhA%2BWMoDdWOioOaOFn8eI%2FkvyjhxI2d5nErXmjwmPpozkJubO7bj0vI1Ber68NUeBf48GpdwT33cMdRnAh%2FkL96VpPDbjQSxTILwUBaTgH5widH%2BjO09kvff24I1oUTztyqq4%2B%2BFs4IpAsq%2B4teRgjaRFmAbEbtREgrU%2BJIzolKGREHkIY0XwncwTwl2XGNKkPC%2FZcFf6eRqXFEiWBqNufW5KyU4qdpPu00rvHE2l7zWmwQwIJqU99yih9h%2FBWuxQrzC6pR38Ih6MjYLJ%2Fjb1v3Pr8DIuz2MKy%2Flr0GOqUB5LFbQiSw3z9n6KpIppsMGjfQnA0f9AJz3kO6GaX67%2F0idcLPBAFHW2bkTCMmit6m%2FUBu1Cm4cjZPSBJyFL69v7c7TzxSbyPPru3bZUVEuS2p8AxbRC2UP0PW2eohoZkxn1TL0L78VNpKlge1jMzqRF4zbOwEnKWAFbzeyGWRYJuEWWJCDs9IO4So70TssorIKsSvc2rcyUj2pO2LDQwVV4KVAPtW&X-Amz-Signature=5df64711db07a72ff031f57404ac65f165ba40c977211af64171fc29aa1abcd9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXIA33Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIBvjq1pMna7Z0mC3pbMaH2aaBgAIs45buauXSCfsYzQIAiEAyMuVv27FUj1PT3In5IkKk2m7Da2mwkqFBvWwWzXxFqAq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJrKcCBNPeLSubkcRircA53hXnSxAT%2BPBVc4r%2FjcMPGMeP1prw0mnzkpdqRcw6pMVNOFhs6%2FfE8o4R2GcX0NYRUzNo63JyXqRXJC%2FEIlAr1ApIQd60FKxp0cfmL53tdp8Srq5qVJpTm%2FcppyH8W8R60Ghg8FmsVq0MqoEL6tu5GhK7MNvHTm6%2F1CvOEgYwVMmOtYJ%2BRCqJCYKy8oqTKh3koHQyUEInXHBHYBhpDtknw3krMLLySmQbCMjOwFcvJtfx9L4PeMShCX%2B5xN%2Fe6%2BZJut9RqAz6Y6KUyrqCMYfFrcRf0vQx8jdFH0ELtNfwQKpapJNeo9nSWQVC4wlf0z5GIab0jOREAfDGS%2FAxgYAPo1C6uKDMhA%2BWMoDdWOioOaOFn8eI%2FkvyjhxI2d5nErXmjwmPpozkJubO7bj0vI1Ber68NUeBf48GpdwT33cMdRnAh%2FkL96VpPDbjQSxTILwUBaTgH5widH%2BjO09kvff24I1oUTztyqq4%2B%2BFs4IpAsq%2B4teRgjaRFmAbEbtREgrU%2BJIzolKGREHkIY0XwncwTwl2XGNKkPC%2FZcFf6eRqXFEiWBqNufW5KyU4qdpPu00rvHE2l7zWmwQwIJqU99yih9h%2FBWuxQrzC6pR38Ih6MjYLJ%2Fjb1v3Pr8DIuz2MKy%2Flr0GOqUB5LFbQiSw3z9n6KpIppsMGjfQnA0f9AJz3kO6GaX67%2F0idcLPBAFHW2bkTCMmit6m%2FUBu1Cm4cjZPSBJyFL69v7c7TzxSbyPPru3bZUVEuS2p8AxbRC2UP0PW2eohoZkxn1TL0L78VNpKlge1jMzqRF4zbOwEnKWAFbzeyGWRYJuEWWJCDs9IO4So70TssorIKsSvc2rcyUj2pO2LDQwVV4KVAPtW&X-Amz-Signature=ff0d1f5760f90d062667dcda5ba199166ed31f83060b633eb903c68afd84fa02&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZB6MIM4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDVjD3d3cPQQQHsEeBnKe3Xufq0IyoUHqWRSTbi9qWTHgIhAMCXuJGPY4kPDXch7kucg0TRdfinPz5tqFOhYbVT0j%2BSKv8DCG8QABoMNjM3NDIzMTgzODA1Igzn8qBocCSBSsIPcoMq3APEOwTJzk3Vpgv03naJX%2B89TJT4Qxf0%2BpCEPFrDCm6jrjXONYS5p%2FLMYxwaErTaSMQjzNZBBF4HT0bW1L614TO1UNJt4nhYVOryr984CevzyZ%2BphRfFcFe%2B8btFnHog3U%2F5%2FKprORWmA1o0MwKbmkdcHad9LUK0JgnVrU7qXHhwt6p9kJJapWTlJkpwTU4f4tbQJfiMbYPcWbA3ioJvyUraTKGjMdleCroAKG9Ni68MWJYeH0KdSJojxRnwIG7b3el%2FJtEpHErTvhfdHcbHWbAa80TWidR%2Bm8QgHhe0gZIrAdZNWh6R93dQ6zoVqzYTBhqOqjGosT7NQDOrz%2FwNOWzvM8ZlB6dcMASUaEGrA4%2F8UzyIgwJTUiQl11y%2FbThMA0bwqyk0FF4mNz%2Bei5r7jJaKYVYZ9M8q0WA5JihTYdVnQQs4t8UjrJ%2BQrUIHmE6Zy3XgMZRrlZd588RzOKgvgYPo2Uu9s78edeZU5ax0MWEGa78hOwUjlPhjBTEcoXu%2FhK%2BYLKsegQXPKK2yO973JGM8TZsEbjJ0YRi49Sy2gSC%2FPcb8WhwsDW2HOSj6dOCa6hEKluk%2BsPv%2FA6k8jXz2BwFDJipuxVuOypzjt0McM%2B2Mn5rQrqrvOv0t9MsTmDDivpa9BjqkAfR8pOS5OTO4oSQTlPWut1yaAhR13UuDfsx%2FU1eizGoWwk8ihLgYRm1365UGTby0Ma2DaXJnDu%2BlrPO8RvjZxmj8LYMjPTvW1YZVZEBjLkiXdsxWLORVyKmC%2FpaXO%2BzGEagDVPfEKjRzJzRHZn%2B6el87VZ2irjO2MDnwiG62u%2FTHIMptF%2BR1zjXHnToy07eE%2BAOGhDjVybHDY2CNztI0d3yCHkbO&X-Amz-Signature=1ae177d49bae6111ab4e617b57ab2005a1ac802d14851bca5eae686b7f4bf86e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZB6MIM4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDVjD3d3cPQQQHsEeBnKe3Xufq0IyoUHqWRSTbi9qWTHgIhAMCXuJGPY4kPDXch7kucg0TRdfinPz5tqFOhYbVT0j%2BSKv8DCG8QABoMNjM3NDIzMTgzODA1Igzn8qBocCSBSsIPcoMq3APEOwTJzk3Vpgv03naJX%2B89TJT4Qxf0%2BpCEPFrDCm6jrjXONYS5p%2FLMYxwaErTaSMQjzNZBBF4HT0bW1L614TO1UNJt4nhYVOryr984CevzyZ%2BphRfFcFe%2B8btFnHog3U%2F5%2FKprORWmA1o0MwKbmkdcHad9LUK0JgnVrU7qXHhwt6p9kJJapWTlJkpwTU4f4tbQJfiMbYPcWbA3ioJvyUraTKGjMdleCroAKG9Ni68MWJYeH0KdSJojxRnwIG7b3el%2FJtEpHErTvhfdHcbHWbAa80TWidR%2Bm8QgHhe0gZIrAdZNWh6R93dQ6zoVqzYTBhqOqjGosT7NQDOrz%2FwNOWzvM8ZlB6dcMASUaEGrA4%2F8UzyIgwJTUiQl11y%2FbThMA0bwqyk0FF4mNz%2Bei5r7jJaKYVYZ9M8q0WA5JihTYdVnQQs4t8UjrJ%2BQrUIHmE6Zy3XgMZRrlZd588RzOKgvgYPo2Uu9s78edeZU5ax0MWEGa78hOwUjlPhjBTEcoXu%2FhK%2BYLKsegQXPKK2yO973JGM8TZsEbjJ0YRi49Sy2gSC%2FPcb8WhwsDW2HOSj6dOCa6hEKluk%2BsPv%2FA6k8jXz2BwFDJipuxVuOypzjt0McM%2B2Mn5rQrqrvOv0t9MsTmDDivpa9BjqkAfR8pOS5OTO4oSQTlPWut1yaAhR13UuDfsx%2FU1eizGoWwk8ihLgYRm1365UGTby0Ma2DaXJnDu%2BlrPO8RvjZxmj8LYMjPTvW1YZVZEBjLkiXdsxWLORVyKmC%2FpaXO%2BzGEagDVPfEKjRzJzRHZn%2B6el87VZ2irjO2MDnwiG62u%2FTHIMptF%2BR1zjXHnToy07eE%2BAOGhDjVybHDY2CNztI0d3yCHkbO&X-Amz-Signature=66270856d99e57c6af2478ae62dfe5a62110878920032ea4977c24983bf877fb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZB6MIM4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDVjD3d3cPQQQHsEeBnKe3Xufq0IyoUHqWRSTbi9qWTHgIhAMCXuJGPY4kPDXch7kucg0TRdfinPz5tqFOhYbVT0j%2BSKv8DCG8QABoMNjM3NDIzMTgzODA1Igzn8qBocCSBSsIPcoMq3APEOwTJzk3Vpgv03naJX%2B89TJT4Qxf0%2BpCEPFrDCm6jrjXONYS5p%2FLMYxwaErTaSMQjzNZBBF4HT0bW1L614TO1UNJt4nhYVOryr984CevzyZ%2BphRfFcFe%2B8btFnHog3U%2F5%2FKprORWmA1o0MwKbmkdcHad9LUK0JgnVrU7qXHhwt6p9kJJapWTlJkpwTU4f4tbQJfiMbYPcWbA3ioJvyUraTKGjMdleCroAKG9Ni68MWJYeH0KdSJojxRnwIG7b3el%2FJtEpHErTvhfdHcbHWbAa80TWidR%2Bm8QgHhe0gZIrAdZNWh6R93dQ6zoVqzYTBhqOqjGosT7NQDOrz%2FwNOWzvM8ZlB6dcMASUaEGrA4%2F8UzyIgwJTUiQl11y%2FbThMA0bwqyk0FF4mNz%2Bei5r7jJaKYVYZ9M8q0WA5JihTYdVnQQs4t8UjrJ%2BQrUIHmE6Zy3XgMZRrlZd588RzOKgvgYPo2Uu9s78edeZU5ax0MWEGa78hOwUjlPhjBTEcoXu%2FhK%2BYLKsegQXPKK2yO973JGM8TZsEbjJ0YRi49Sy2gSC%2FPcb8WhwsDW2HOSj6dOCa6hEKluk%2BsPv%2FA6k8jXz2BwFDJipuxVuOypzjt0McM%2B2Mn5rQrqrvOv0t9MsTmDDivpa9BjqkAfR8pOS5OTO4oSQTlPWut1yaAhR13UuDfsx%2FU1eizGoWwk8ihLgYRm1365UGTby0Ma2DaXJnDu%2BlrPO8RvjZxmj8LYMjPTvW1YZVZEBjLkiXdsxWLORVyKmC%2FpaXO%2BzGEagDVPfEKjRzJzRHZn%2B6el87VZ2irjO2MDnwiG62u%2FTHIMptF%2BR1zjXHnToy07eE%2BAOGhDjVybHDY2CNztI0d3yCHkbO&X-Amz-Signature=58b65c942a92c455a9f1bf89127a12fbd906479ac6232bd20dde9f78d1e0bf8d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZB6MIM4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDVjD3d3cPQQQHsEeBnKe3Xufq0IyoUHqWRSTbi9qWTHgIhAMCXuJGPY4kPDXch7kucg0TRdfinPz5tqFOhYbVT0j%2BSKv8DCG8QABoMNjM3NDIzMTgzODA1Igzn8qBocCSBSsIPcoMq3APEOwTJzk3Vpgv03naJX%2B89TJT4Qxf0%2BpCEPFrDCm6jrjXONYS5p%2FLMYxwaErTaSMQjzNZBBF4HT0bW1L614TO1UNJt4nhYVOryr984CevzyZ%2BphRfFcFe%2B8btFnHog3U%2F5%2FKprORWmA1o0MwKbmkdcHad9LUK0JgnVrU7qXHhwt6p9kJJapWTlJkpwTU4f4tbQJfiMbYPcWbA3ioJvyUraTKGjMdleCroAKG9Ni68MWJYeH0KdSJojxRnwIG7b3el%2FJtEpHErTvhfdHcbHWbAa80TWidR%2Bm8QgHhe0gZIrAdZNWh6R93dQ6zoVqzYTBhqOqjGosT7NQDOrz%2FwNOWzvM8ZlB6dcMASUaEGrA4%2F8UzyIgwJTUiQl11y%2FbThMA0bwqyk0FF4mNz%2Bei5r7jJaKYVYZ9M8q0WA5JihTYdVnQQs4t8UjrJ%2BQrUIHmE6Zy3XgMZRrlZd588RzOKgvgYPo2Uu9s78edeZU5ax0MWEGa78hOwUjlPhjBTEcoXu%2FhK%2BYLKsegQXPKK2yO973JGM8TZsEbjJ0YRi49Sy2gSC%2FPcb8WhwsDW2HOSj6dOCa6hEKluk%2BsPv%2FA6k8jXz2BwFDJipuxVuOypzjt0McM%2B2Mn5rQrqrvOv0t9MsTmDDivpa9BjqkAfR8pOS5OTO4oSQTlPWut1yaAhR13UuDfsx%2FU1eizGoWwk8ihLgYRm1365UGTby0Ma2DaXJnDu%2BlrPO8RvjZxmj8LYMjPTvW1YZVZEBjLkiXdsxWLORVyKmC%2FpaXO%2BzGEagDVPfEKjRzJzRHZn%2B6el87VZ2irjO2MDnwiG62u%2FTHIMptF%2BR1zjXHnToy07eE%2BAOGhDjVybHDY2CNztI0d3yCHkbO&X-Amz-Signature=5b30dc0693b23003d4e857f8685b60d33ea312e480dbc11aeb4f61a6d423fe0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZB6MIM4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDVjD3d3cPQQQHsEeBnKe3Xufq0IyoUHqWRSTbi9qWTHgIhAMCXuJGPY4kPDXch7kucg0TRdfinPz5tqFOhYbVT0j%2BSKv8DCG8QABoMNjM3NDIzMTgzODA1Igzn8qBocCSBSsIPcoMq3APEOwTJzk3Vpgv03naJX%2B89TJT4Qxf0%2BpCEPFrDCm6jrjXONYS5p%2FLMYxwaErTaSMQjzNZBBF4HT0bW1L614TO1UNJt4nhYVOryr984CevzyZ%2BphRfFcFe%2B8btFnHog3U%2F5%2FKprORWmA1o0MwKbmkdcHad9LUK0JgnVrU7qXHhwt6p9kJJapWTlJkpwTU4f4tbQJfiMbYPcWbA3ioJvyUraTKGjMdleCroAKG9Ni68MWJYeH0KdSJojxRnwIG7b3el%2FJtEpHErTvhfdHcbHWbAa80TWidR%2Bm8QgHhe0gZIrAdZNWh6R93dQ6zoVqzYTBhqOqjGosT7NQDOrz%2FwNOWzvM8ZlB6dcMASUaEGrA4%2F8UzyIgwJTUiQl11y%2FbThMA0bwqyk0FF4mNz%2Bei5r7jJaKYVYZ9M8q0WA5JihTYdVnQQs4t8UjrJ%2BQrUIHmE6Zy3XgMZRrlZd588RzOKgvgYPo2Uu9s78edeZU5ax0MWEGa78hOwUjlPhjBTEcoXu%2FhK%2BYLKsegQXPKK2yO973JGM8TZsEbjJ0YRi49Sy2gSC%2FPcb8WhwsDW2HOSj6dOCa6hEKluk%2BsPv%2FA6k8jXz2BwFDJipuxVuOypzjt0McM%2B2Mn5rQrqrvOv0t9MsTmDDivpa9BjqkAfR8pOS5OTO4oSQTlPWut1yaAhR13UuDfsx%2FU1eizGoWwk8ihLgYRm1365UGTby0Ma2DaXJnDu%2BlrPO8RvjZxmj8LYMjPTvW1YZVZEBjLkiXdsxWLORVyKmC%2FpaXO%2BzGEagDVPfEKjRzJzRHZn%2B6el87VZ2irjO2MDnwiG62u%2FTHIMptF%2BR1zjXHnToy07eE%2BAOGhDjVybHDY2CNztI0d3yCHkbO&X-Amz-Signature=ddc498b8850bc86092f864d29b47ea58ab5512b49c7e8ba5cd1351d50ad5f9a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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


