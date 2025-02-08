

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE76Z2PS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBlBtSDBjLaVDnGKI7CRkARhrStq6WRuVOHKw2N81b4mAiAw6cPCGkwTZYnwno83N3m9TDl2ciWk%2BP0PuNUh1hMFiyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi2uz6Sw0tiXHwD%2FOKtwDQEQCR6Wv%2B45jiekGtT4EF7yK5YSTwzyQZx%2Bk7R23DSxoWXJArGF2vMhThoUscwaxwKXNusl3etT2MKV0h7JR%2BbxKntOpEsopvWKs3%2FvWOWoSDL2Bi8huKSpDILlhyYxCv1gO3eV%2F0I50UjWNJxVZYrrpdGyD4pG9VVe8CzwvsPgi2AKrqFJt5Zb4r8xY1KN3Kn%2FNRF7Pa6U5eafMnzUw3yw7LWPVtmC9lxkMeTxL9we9gb5bNQuBhCZS4iOw6YL8goTStlxBC4OLut4ZKfH7VK5WA%2BhAiPY760YhDiCRlwR4JpuCTPqneOZ4NMvJB17vAWkQ8%2FGe3jykovEhL61EaVmogMUHEmAZZSNzn6nG8p%2Bi5iPlVhdp%2B66T7BxW8FoHUXq6XUIC6cVJlN9a%2FIKwVU0SdLdFuKCPNhIchYA%2BREBwxCqB9sJEIEWVZIvapzC%2B8O7CSOa251YHyth8WA%2F7fjArVK0TjJJPyxOESVfjsLmcRkxeK9JZFP2B4sD9jBU3GcJMlVe6pOOZrlpw8NoZQGVjwgajqFj50s%2BfL0iVA2PbDnybSrqH6%2FMeSroTzNUsJoLXfkvWpaRp1wZcnxwxZHtRxHqg%2F%2B0Iw0U4RicK89fOR6Y6QNFEvoSlgZYwpI6cvQY6pgEbHLNKJ5ffjnOCjZrGO3NQN1Rax9rfnzTLYlpvw1kKNhUPjWO0VFAgctKaI5KJDnC5uenhQj5yKBYp%2FeCJBOrBsL72sIR7mwdYwn3JZ3Vzgboksr8JpDkkw6%2BjFi0U4jJw6VaZXR8ohM4Sv2XGNgoBRoI3RisTYKd%2BFy8D%2Bz5BUV9to1lYFRoIoKud1OTzDkZbXufYE%2BiJBX867aAg7g94%2FFgovyxp&X-Amz-Signature=15f8ab925b5c01b0dd00e6f31c063139be8c1c9739ba5c0c1d440c6011d45f97&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PLOSV2F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIEMaVyI3GhHMkST%2F7Fleno%2For3Nd1%2BuUQEO2Vu4X8DhFAiEApxIDR9i3rJzSuI3wr1t4KainymlkIQHBkKHBmk9CCMEqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGguQ1zM61ANQmSvuyrcA5w7zTXbOteLWd0E7lbnvQQLPUEW30d%2FdOZ7R8Wjsv2EUEB3FG%2Bog4VSXGd%2FqcuTUTcL8jBvdDBvZWwaY0f6j90IBsc6Y37slHQTfPl%2FgKaGnVWhmnA6PnW8sGavDDoHX3e%2BAjr1gzUTjhlXIMrexaFV36UfxoYAyl9SX8KkXPrtUdATXyML1hzalbDaNFYDfcD27tBEhFqvWsPdqMYRhJz%2BxAq7hxrB5ly1OTXisVNhVi1ZBmMiEPBK3F7fy1AWaOZqtGiO9o5KlR%2BcMJxmoNgFVPzbLcn6WzLf5caEdMFmhCsSj1NYPGY571Re25qHRJCOi81WcfVAmZ8jXxm9EollwcPnf%2Fx%2FcDKfd%2FYcLPqsVdVjj%2B7Ck8Nrm8JWXbvdExpIyUvL2MjfmBkM%2BBU%2F1C4mrFYDCoeKe5Sy7WeoAvPLyNzLVGJs7Dua5oNmE4MzhJ9wm9GH9vqhR6tH6tp0gHnF85DQHjFDGyWlnh8cIiLwMrqvM9ryvrlB7BNU4O8kk5ZW%2BKlBLTk5HzV6yoajEucDdaJvoD90fXSRgRPpd6vwveFacg0skFiFf7YG13kSonjHUW%2BxzF0vQ%2BJvhp9iCctfl%2FuM2yA84OENKUVVWWzZt16H4xU75MciLlc8MJmOnL0GOqUBYIbRdTG4DpInCR1s4U9fgLNuMir40iN3GUHwswTG6NEP4U%2B%2BTvL9e5YkIsPOJiWEIeP57MwpoX0n7l0tiHtzB1BbdcsHVBhD%2FN7JsCt%2BfK0GNQjYX5JviJHr7hN%2BBmY96QJnm7kDS2fJ4cAsKbQbSDweOhg6mIKryQHz3rDV687nxwPaURinZrups60wjEfTjXU9ZHtv8tVNUS2Jc4wPg1I12grd&X-Amz-Signature=315edcfc53784e49c32bc2102c0de66a9631232a880f46ae6fc9f62f443ca383&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PLOSV2F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIEMaVyI3GhHMkST%2F7Fleno%2For3Nd1%2BuUQEO2Vu4X8DhFAiEApxIDR9i3rJzSuI3wr1t4KainymlkIQHBkKHBmk9CCMEqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGguQ1zM61ANQmSvuyrcA5w7zTXbOteLWd0E7lbnvQQLPUEW30d%2FdOZ7R8Wjsv2EUEB3FG%2Bog4VSXGd%2FqcuTUTcL8jBvdDBvZWwaY0f6j90IBsc6Y37slHQTfPl%2FgKaGnVWhmnA6PnW8sGavDDoHX3e%2BAjr1gzUTjhlXIMrexaFV36UfxoYAyl9SX8KkXPrtUdATXyML1hzalbDaNFYDfcD27tBEhFqvWsPdqMYRhJz%2BxAq7hxrB5ly1OTXisVNhVi1ZBmMiEPBK3F7fy1AWaOZqtGiO9o5KlR%2BcMJxmoNgFVPzbLcn6WzLf5caEdMFmhCsSj1NYPGY571Re25qHRJCOi81WcfVAmZ8jXxm9EollwcPnf%2Fx%2FcDKfd%2FYcLPqsVdVjj%2B7Ck8Nrm8JWXbvdExpIyUvL2MjfmBkM%2BBU%2F1C4mrFYDCoeKe5Sy7WeoAvPLyNzLVGJs7Dua5oNmE4MzhJ9wm9GH9vqhR6tH6tp0gHnF85DQHjFDGyWlnh8cIiLwMrqvM9ryvrlB7BNU4O8kk5ZW%2BKlBLTk5HzV6yoajEucDdaJvoD90fXSRgRPpd6vwveFacg0skFiFf7YG13kSonjHUW%2BxzF0vQ%2BJvhp9iCctfl%2FuM2yA84OENKUVVWWzZt16H4xU75MciLlc8MJmOnL0GOqUBYIbRdTG4DpInCR1s4U9fgLNuMir40iN3GUHwswTG6NEP4U%2B%2BTvL9e5YkIsPOJiWEIeP57MwpoX0n7l0tiHtzB1BbdcsHVBhD%2FN7JsCt%2BfK0GNQjYX5JviJHr7hN%2BBmY96QJnm7kDS2fJ4cAsKbQbSDweOhg6mIKryQHz3rDV687nxwPaURinZrups60wjEfTjXU9ZHtv8tVNUS2Jc4wPg1I12grd&X-Amz-Signature=042605c96fba4bbd2b9237a6af5ccb89a48c9837bdd363ec51e252d5ed6bb829&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PLOSV2F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIEMaVyI3GhHMkST%2F7Fleno%2For3Nd1%2BuUQEO2Vu4X8DhFAiEApxIDR9i3rJzSuI3wr1t4KainymlkIQHBkKHBmk9CCMEqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGguQ1zM61ANQmSvuyrcA5w7zTXbOteLWd0E7lbnvQQLPUEW30d%2FdOZ7R8Wjsv2EUEB3FG%2Bog4VSXGd%2FqcuTUTcL8jBvdDBvZWwaY0f6j90IBsc6Y37slHQTfPl%2FgKaGnVWhmnA6PnW8sGavDDoHX3e%2BAjr1gzUTjhlXIMrexaFV36UfxoYAyl9SX8KkXPrtUdATXyML1hzalbDaNFYDfcD27tBEhFqvWsPdqMYRhJz%2BxAq7hxrB5ly1OTXisVNhVi1ZBmMiEPBK3F7fy1AWaOZqtGiO9o5KlR%2BcMJxmoNgFVPzbLcn6WzLf5caEdMFmhCsSj1NYPGY571Re25qHRJCOi81WcfVAmZ8jXxm9EollwcPnf%2Fx%2FcDKfd%2FYcLPqsVdVjj%2B7Ck8Nrm8JWXbvdExpIyUvL2MjfmBkM%2BBU%2F1C4mrFYDCoeKe5Sy7WeoAvPLyNzLVGJs7Dua5oNmE4MzhJ9wm9GH9vqhR6tH6tp0gHnF85DQHjFDGyWlnh8cIiLwMrqvM9ryvrlB7BNU4O8kk5ZW%2BKlBLTk5HzV6yoajEucDdaJvoD90fXSRgRPpd6vwveFacg0skFiFf7YG13kSonjHUW%2BxzF0vQ%2BJvhp9iCctfl%2FuM2yA84OENKUVVWWzZt16H4xU75MciLlc8MJmOnL0GOqUBYIbRdTG4DpInCR1s4U9fgLNuMir40iN3GUHwswTG6NEP4U%2B%2BTvL9e5YkIsPOJiWEIeP57MwpoX0n7l0tiHtzB1BbdcsHVBhD%2FN7JsCt%2BfK0GNQjYX5JviJHr7hN%2BBmY96QJnm7kDS2fJ4cAsKbQbSDweOhg6mIKryQHz3rDV687nxwPaURinZrups60wjEfTjXU9ZHtv8tVNUS2Jc4wPg1I12grd&X-Amz-Signature=63cb4eadc8efc128099b2e5c4c9045234b63c216612b0fef6948145a9efc69d4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PLOSV2F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIEMaVyI3GhHMkST%2F7Fleno%2For3Nd1%2BuUQEO2Vu4X8DhFAiEApxIDR9i3rJzSuI3wr1t4KainymlkIQHBkKHBmk9CCMEqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGguQ1zM61ANQmSvuyrcA5w7zTXbOteLWd0E7lbnvQQLPUEW30d%2FdOZ7R8Wjsv2EUEB3FG%2Bog4VSXGd%2FqcuTUTcL8jBvdDBvZWwaY0f6j90IBsc6Y37slHQTfPl%2FgKaGnVWhmnA6PnW8sGavDDoHX3e%2BAjr1gzUTjhlXIMrexaFV36UfxoYAyl9SX8KkXPrtUdATXyML1hzalbDaNFYDfcD27tBEhFqvWsPdqMYRhJz%2BxAq7hxrB5ly1OTXisVNhVi1ZBmMiEPBK3F7fy1AWaOZqtGiO9o5KlR%2BcMJxmoNgFVPzbLcn6WzLf5caEdMFmhCsSj1NYPGY571Re25qHRJCOi81WcfVAmZ8jXxm9EollwcPnf%2Fx%2FcDKfd%2FYcLPqsVdVjj%2B7Ck8Nrm8JWXbvdExpIyUvL2MjfmBkM%2BBU%2F1C4mrFYDCoeKe5Sy7WeoAvPLyNzLVGJs7Dua5oNmE4MzhJ9wm9GH9vqhR6tH6tp0gHnF85DQHjFDGyWlnh8cIiLwMrqvM9ryvrlB7BNU4O8kk5ZW%2BKlBLTk5HzV6yoajEucDdaJvoD90fXSRgRPpd6vwveFacg0skFiFf7YG13kSonjHUW%2BxzF0vQ%2BJvhp9iCctfl%2FuM2yA84OENKUVVWWzZt16H4xU75MciLlc8MJmOnL0GOqUBYIbRdTG4DpInCR1s4U9fgLNuMir40iN3GUHwswTG6NEP4U%2B%2BTvL9e5YkIsPOJiWEIeP57MwpoX0n7l0tiHtzB1BbdcsHVBhD%2FN7JsCt%2BfK0GNQjYX5JviJHr7hN%2BBmY96QJnm7kDS2fJ4cAsKbQbSDweOhg6mIKryQHz3rDV687nxwPaURinZrups60wjEfTjXU9ZHtv8tVNUS2Jc4wPg1I12grd&X-Amz-Signature=4c1ed14d0c820461fcc3dbe230a2f4b82b71d334755876b6a09a9a84cd95da6e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PLOSV2F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIEMaVyI3GhHMkST%2F7Fleno%2For3Nd1%2BuUQEO2Vu4X8DhFAiEApxIDR9i3rJzSuI3wr1t4KainymlkIQHBkKHBmk9CCMEqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGguQ1zM61ANQmSvuyrcA5w7zTXbOteLWd0E7lbnvQQLPUEW30d%2FdOZ7R8Wjsv2EUEB3FG%2Bog4VSXGd%2FqcuTUTcL8jBvdDBvZWwaY0f6j90IBsc6Y37slHQTfPl%2FgKaGnVWhmnA6PnW8sGavDDoHX3e%2BAjr1gzUTjhlXIMrexaFV36UfxoYAyl9SX8KkXPrtUdATXyML1hzalbDaNFYDfcD27tBEhFqvWsPdqMYRhJz%2BxAq7hxrB5ly1OTXisVNhVi1ZBmMiEPBK3F7fy1AWaOZqtGiO9o5KlR%2BcMJxmoNgFVPzbLcn6WzLf5caEdMFmhCsSj1NYPGY571Re25qHRJCOi81WcfVAmZ8jXxm9EollwcPnf%2Fx%2FcDKfd%2FYcLPqsVdVjj%2B7Ck8Nrm8JWXbvdExpIyUvL2MjfmBkM%2BBU%2F1C4mrFYDCoeKe5Sy7WeoAvPLyNzLVGJs7Dua5oNmE4MzhJ9wm9GH9vqhR6tH6tp0gHnF85DQHjFDGyWlnh8cIiLwMrqvM9ryvrlB7BNU4O8kk5ZW%2BKlBLTk5HzV6yoajEucDdaJvoD90fXSRgRPpd6vwveFacg0skFiFf7YG13kSonjHUW%2BxzF0vQ%2BJvhp9iCctfl%2FuM2yA84OENKUVVWWzZt16H4xU75MciLlc8MJmOnL0GOqUBYIbRdTG4DpInCR1s4U9fgLNuMir40iN3GUHwswTG6NEP4U%2B%2BTvL9e5YkIsPOJiWEIeP57MwpoX0n7l0tiHtzB1BbdcsHVBhD%2FN7JsCt%2BfK0GNQjYX5JviJHr7hN%2BBmY96QJnm7kDS2fJ4cAsKbQbSDweOhg6mIKryQHz3rDV687nxwPaURinZrups60wjEfTjXU9ZHtv8tVNUS2Jc4wPg1I12grd&X-Amz-Signature=f7a396ce928f57d5dcaa1fac329821dda1e494095fcce62a7e84db3cc48d8516&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE76Z2PS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBlBtSDBjLaVDnGKI7CRkARhrStq6WRuVOHKw2N81b4mAiAw6cPCGkwTZYnwno83N3m9TDl2ciWk%2BP0PuNUh1hMFiyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi2uz6Sw0tiXHwD%2FOKtwDQEQCR6Wv%2B45jiekGtT4EF7yK5YSTwzyQZx%2Bk7R23DSxoWXJArGF2vMhThoUscwaxwKXNusl3etT2MKV0h7JR%2BbxKntOpEsopvWKs3%2FvWOWoSDL2Bi8huKSpDILlhyYxCv1gO3eV%2F0I50UjWNJxVZYrrpdGyD4pG9VVe8CzwvsPgi2AKrqFJt5Zb4r8xY1KN3Kn%2FNRF7Pa6U5eafMnzUw3yw7LWPVtmC9lxkMeTxL9we9gb5bNQuBhCZS4iOw6YL8goTStlxBC4OLut4ZKfH7VK5WA%2BhAiPY760YhDiCRlwR4JpuCTPqneOZ4NMvJB17vAWkQ8%2FGe3jykovEhL61EaVmogMUHEmAZZSNzn6nG8p%2Bi5iPlVhdp%2B66T7BxW8FoHUXq6XUIC6cVJlN9a%2FIKwVU0SdLdFuKCPNhIchYA%2BREBwxCqB9sJEIEWVZIvapzC%2B8O7CSOa251YHyth8WA%2F7fjArVK0TjJJPyxOESVfjsLmcRkxeK9JZFP2B4sD9jBU3GcJMlVe6pOOZrlpw8NoZQGVjwgajqFj50s%2BfL0iVA2PbDnybSrqH6%2FMeSroTzNUsJoLXfkvWpaRp1wZcnxwxZHtRxHqg%2F%2B0Iw0U4RicK89fOR6Y6QNFEvoSlgZYwpI6cvQY6pgEbHLNKJ5ffjnOCjZrGO3NQN1Rax9rfnzTLYlpvw1kKNhUPjWO0VFAgctKaI5KJDnC5uenhQj5yKBYp%2FeCJBOrBsL72sIR7mwdYwn3JZ3Vzgboksr8JpDkkw6%2BjFi0U4jJw6VaZXR8ohM4Sv2XGNgoBRoI3RisTYKd%2BFy8D%2Bz5BUV9to1lYFRoIoKud1OTzDkZbXufYE%2BiJBX867aAg7g94%2FFgovyxp&X-Amz-Signature=88bfe1c055a1da473c604ff2b38937f3ace0e9f646d7a29d4b5d2dfb5e3e46d2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE76Z2PS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBlBtSDBjLaVDnGKI7CRkARhrStq6WRuVOHKw2N81b4mAiAw6cPCGkwTZYnwno83N3m9TDl2ciWk%2BP0PuNUh1hMFiyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi2uz6Sw0tiXHwD%2FOKtwDQEQCR6Wv%2B45jiekGtT4EF7yK5YSTwzyQZx%2Bk7R23DSxoWXJArGF2vMhThoUscwaxwKXNusl3etT2MKV0h7JR%2BbxKntOpEsopvWKs3%2FvWOWoSDL2Bi8huKSpDILlhyYxCv1gO3eV%2F0I50UjWNJxVZYrrpdGyD4pG9VVe8CzwvsPgi2AKrqFJt5Zb4r8xY1KN3Kn%2FNRF7Pa6U5eafMnzUw3yw7LWPVtmC9lxkMeTxL9we9gb5bNQuBhCZS4iOw6YL8goTStlxBC4OLut4ZKfH7VK5WA%2BhAiPY760YhDiCRlwR4JpuCTPqneOZ4NMvJB17vAWkQ8%2FGe3jykovEhL61EaVmogMUHEmAZZSNzn6nG8p%2Bi5iPlVhdp%2B66T7BxW8FoHUXq6XUIC6cVJlN9a%2FIKwVU0SdLdFuKCPNhIchYA%2BREBwxCqB9sJEIEWVZIvapzC%2B8O7CSOa251YHyth8WA%2F7fjArVK0TjJJPyxOESVfjsLmcRkxeK9JZFP2B4sD9jBU3GcJMlVe6pOOZrlpw8NoZQGVjwgajqFj50s%2BfL0iVA2PbDnybSrqH6%2FMeSroTzNUsJoLXfkvWpaRp1wZcnxwxZHtRxHqg%2F%2B0Iw0U4RicK89fOR6Y6QNFEvoSlgZYwpI6cvQY6pgEbHLNKJ5ffjnOCjZrGO3NQN1Rax9rfnzTLYlpvw1kKNhUPjWO0VFAgctKaI5KJDnC5uenhQj5yKBYp%2FeCJBOrBsL72sIR7mwdYwn3JZ3Vzgboksr8JpDkkw6%2BjFi0U4jJw6VaZXR8ohM4Sv2XGNgoBRoI3RisTYKd%2BFy8D%2Bz5BUV9to1lYFRoIoKud1OTzDkZbXufYE%2BiJBX867aAg7g94%2FFgovyxp&X-Amz-Signature=2845cc8b3807a233d7cafa0ff25c1551d6285463193b6de311fb016f817efb80&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE76Z2PS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBlBtSDBjLaVDnGKI7CRkARhrStq6WRuVOHKw2N81b4mAiAw6cPCGkwTZYnwno83N3m9TDl2ciWk%2BP0PuNUh1hMFiyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi2uz6Sw0tiXHwD%2FOKtwDQEQCR6Wv%2B45jiekGtT4EF7yK5YSTwzyQZx%2Bk7R23DSxoWXJArGF2vMhThoUscwaxwKXNusl3etT2MKV0h7JR%2BbxKntOpEsopvWKs3%2FvWOWoSDL2Bi8huKSpDILlhyYxCv1gO3eV%2F0I50UjWNJxVZYrrpdGyD4pG9VVe8CzwvsPgi2AKrqFJt5Zb4r8xY1KN3Kn%2FNRF7Pa6U5eafMnzUw3yw7LWPVtmC9lxkMeTxL9we9gb5bNQuBhCZS4iOw6YL8goTStlxBC4OLut4ZKfH7VK5WA%2BhAiPY760YhDiCRlwR4JpuCTPqneOZ4NMvJB17vAWkQ8%2FGe3jykovEhL61EaVmogMUHEmAZZSNzn6nG8p%2Bi5iPlVhdp%2B66T7BxW8FoHUXq6XUIC6cVJlN9a%2FIKwVU0SdLdFuKCPNhIchYA%2BREBwxCqB9sJEIEWVZIvapzC%2B8O7CSOa251YHyth8WA%2F7fjArVK0TjJJPyxOESVfjsLmcRkxeK9JZFP2B4sD9jBU3GcJMlVe6pOOZrlpw8NoZQGVjwgajqFj50s%2BfL0iVA2PbDnybSrqH6%2FMeSroTzNUsJoLXfkvWpaRp1wZcnxwxZHtRxHqg%2F%2B0Iw0U4RicK89fOR6Y6QNFEvoSlgZYwpI6cvQY6pgEbHLNKJ5ffjnOCjZrGO3NQN1Rax9rfnzTLYlpvw1kKNhUPjWO0VFAgctKaI5KJDnC5uenhQj5yKBYp%2FeCJBOrBsL72sIR7mwdYwn3JZ3Vzgboksr8JpDkkw6%2BjFi0U4jJw6VaZXR8ohM4Sv2XGNgoBRoI3RisTYKd%2BFy8D%2Bz5BUV9to1lYFRoIoKud1OTzDkZbXufYE%2BiJBX867aAg7g94%2FFgovyxp&X-Amz-Signature=379a25470e9f607fec465c2f2db81e53e2ecbb401c980226d35f36ee1623df70&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE76Z2PS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBlBtSDBjLaVDnGKI7CRkARhrStq6WRuVOHKw2N81b4mAiAw6cPCGkwTZYnwno83N3m9TDl2ciWk%2BP0PuNUh1hMFiyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi2uz6Sw0tiXHwD%2FOKtwDQEQCR6Wv%2B45jiekGtT4EF7yK5YSTwzyQZx%2Bk7R23DSxoWXJArGF2vMhThoUscwaxwKXNusl3etT2MKV0h7JR%2BbxKntOpEsopvWKs3%2FvWOWoSDL2Bi8huKSpDILlhyYxCv1gO3eV%2F0I50UjWNJxVZYrrpdGyD4pG9VVe8CzwvsPgi2AKrqFJt5Zb4r8xY1KN3Kn%2FNRF7Pa6U5eafMnzUw3yw7LWPVtmC9lxkMeTxL9we9gb5bNQuBhCZS4iOw6YL8goTStlxBC4OLut4ZKfH7VK5WA%2BhAiPY760YhDiCRlwR4JpuCTPqneOZ4NMvJB17vAWkQ8%2FGe3jykovEhL61EaVmogMUHEmAZZSNzn6nG8p%2Bi5iPlVhdp%2B66T7BxW8FoHUXq6XUIC6cVJlN9a%2FIKwVU0SdLdFuKCPNhIchYA%2BREBwxCqB9sJEIEWVZIvapzC%2B8O7CSOa251YHyth8WA%2F7fjArVK0TjJJPyxOESVfjsLmcRkxeK9JZFP2B4sD9jBU3GcJMlVe6pOOZrlpw8NoZQGVjwgajqFj50s%2BfL0iVA2PbDnybSrqH6%2FMeSroTzNUsJoLXfkvWpaRp1wZcnxwxZHtRxHqg%2F%2B0Iw0U4RicK89fOR6Y6QNFEvoSlgZYwpI6cvQY6pgEbHLNKJ5ffjnOCjZrGO3NQN1Rax9rfnzTLYlpvw1kKNhUPjWO0VFAgctKaI5KJDnC5uenhQj5yKBYp%2FeCJBOrBsL72sIR7mwdYwn3JZ3Vzgboksr8JpDkkw6%2BjFi0U4jJw6VaZXR8ohM4Sv2XGNgoBRoI3RisTYKd%2BFy8D%2Bz5BUV9to1lYFRoIoKud1OTzDkZbXufYE%2BiJBX867aAg7g94%2FFgovyxp&X-Amz-Signature=052f6c83077416ed81f18a07e673eeac8c13fe036cd21ec79fe06f6c32b2524d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE76Z2PS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBlBtSDBjLaVDnGKI7CRkARhrStq6WRuVOHKw2N81b4mAiAw6cPCGkwTZYnwno83N3m9TDl2ciWk%2BP0PuNUh1hMFiyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi2uz6Sw0tiXHwD%2FOKtwDQEQCR6Wv%2B45jiekGtT4EF7yK5YSTwzyQZx%2Bk7R23DSxoWXJArGF2vMhThoUscwaxwKXNusl3etT2MKV0h7JR%2BbxKntOpEsopvWKs3%2FvWOWoSDL2Bi8huKSpDILlhyYxCv1gO3eV%2F0I50UjWNJxVZYrrpdGyD4pG9VVe8CzwvsPgi2AKrqFJt5Zb4r8xY1KN3Kn%2FNRF7Pa6U5eafMnzUw3yw7LWPVtmC9lxkMeTxL9we9gb5bNQuBhCZS4iOw6YL8goTStlxBC4OLut4ZKfH7VK5WA%2BhAiPY760YhDiCRlwR4JpuCTPqneOZ4NMvJB17vAWkQ8%2FGe3jykovEhL61EaVmogMUHEmAZZSNzn6nG8p%2Bi5iPlVhdp%2B66T7BxW8FoHUXq6XUIC6cVJlN9a%2FIKwVU0SdLdFuKCPNhIchYA%2BREBwxCqB9sJEIEWVZIvapzC%2B8O7CSOa251YHyth8WA%2F7fjArVK0TjJJPyxOESVfjsLmcRkxeK9JZFP2B4sD9jBU3GcJMlVe6pOOZrlpw8NoZQGVjwgajqFj50s%2BfL0iVA2PbDnybSrqH6%2FMeSroTzNUsJoLXfkvWpaRp1wZcnxwxZHtRxHqg%2F%2B0Iw0U4RicK89fOR6Y6QNFEvoSlgZYwpI6cvQY6pgEbHLNKJ5ffjnOCjZrGO3NQN1Rax9rfnzTLYlpvw1kKNhUPjWO0VFAgctKaI5KJDnC5uenhQj5yKBYp%2FeCJBOrBsL72sIR7mwdYwn3JZ3Vzgboksr8JpDkkw6%2BjFi0U4jJw6VaZXR8ohM4Sv2XGNgoBRoI3RisTYKd%2BFy8D%2Bz5BUV9to1lYFRoIoKud1OTzDkZbXufYE%2BiJBX867aAg7g94%2FFgovyxp&X-Amz-Signature=62f939b145a45a9f30e3b500d14c06705a7d5844de333904c5e114be83adf827&X-Amz-SignedHeaders=host&x-id=GetObject)
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


