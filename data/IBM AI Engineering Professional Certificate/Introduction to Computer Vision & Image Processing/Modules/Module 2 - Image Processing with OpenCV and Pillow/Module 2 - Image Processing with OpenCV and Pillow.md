

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4YAY54%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzrago2QRiNUb4UYFdk0is%2BfL2X5BW4lSpN9LBSzn5yQIgMqxjSooXh%2FcJLHn7EI65n85co58PgD9%2Fe0e68ivadsUq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJdULt2%2B9lqwnqIeVircAyvPRbeYJuUzQ9y8e21aoU7xh2KOpVSIaUmQ5whj6CaTmz6VUD6HIkwH%2FVSjoqaFLuTEewr80mGnLxolfBreVVkvbijKV6teEMDEvlI4Wi84B4nAGpqZ2Cc%2FCRvdzwMwm%2FOJJ3LwQ4mbfO18DpEiaRwKDH4gOtdG0o6OLvokFuFCQam5CKvb7ml7ksO91H8OEmscjEyEEk%2FAK%2FkoH6UkSJqwmWSuhTxauXUgJ4uLCFza6RJlJVMK5Y85AiYVZhGvSRDlTiK0ULKpndjIR5hIhhMT0hopwd40Ggm%2FZrd6Z03I1XKjPtLg7Nbc3WrKqJBajWEfqrTsHMcg0jb0wStUbjIoYEUS4I0vo3H%2F1u%2FIZdYcPYQS6LOcE8pEdKeG65Kmt%2BsBjFAJLTqXPAq4K%2FrsVrjjugld35lCBgh3AkODxtTmX066NiRwsdkvzXDFjM4Sd9ytUMnJOzyHuwM5Eltv4eogL3IuOm9OPjFobxRieZHbOOnegWQI%2BD%2BXs%2BPjjbhc0HyGqCtsp7vVVBQ0deHvwsz3jy1kvuKn0Vt1cFOI5smaAIsAQSy0DmraCV6vx1NV5UTBwbNTOBeJdm1VZrfETgiVuKqLymW6%2BUwEq8APQbfkkJ17k8NgWQSirr0RMI7Xgb0GOqUBQE%2BmirhCoybpzJKmKXsXAVRqiO%2BMBHTQ7wOJ5fvri8b77AliZZVqyMW1OajyHyNOG0EL5K0A8m3Ri5T7KUrCAGjUWnj3ONzlRQVHt246WvTdpdinedkUIyPIV9UIjnAp3UrWG6vgiU8aKHD2POPO4iIDhzI8nv6cpBprkSHVQaokaJMbpSb1%2BU3nJFQylbawhAixK%2FfSTWN1n3ckLj%2Fa7wnprIiL&X-Amz-Signature=fa581909435f4e7acbbfbf1655970c7b11fde6d97c7730267a3981808906fa45&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRLNN2B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDse%2B6%2BJpmEA1kjPv%2BVmvL1nHJm4MaE0m6dQh%2F2uy2ldAiEA%2B5vSksdXk0UNNmvLFk2%2BLUr%2FhiZ9R0K5bEHp8L5ihJwq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDOzNC4ZMWlOiiq2thyrcAwaQP3gjAZoOOtj3fzHybxWm%2FdWeCOvCbdJdSD%2BpZM8kaZjSNdbhJDARYKrfHHlkuVNYKB3XXWpIdHgxK0jVgVQOl8f8bHI3clgqzxUV0uxpRAg6%2FpVMK3%2BV5gRc8EdPTzVbM8JO3o5ucCFEO7rwv%2BuDL7IwihOQhJqtwJGmmLX%2FFlbg9kU49CCExvE8omUEoKvLXLLBvTTUE06aixoC22j0sjPyN0Xn%2FHbSXHgxX0kjO9njgw2Ptil2PqO7wTEHTywA%2FrP0LB0%2FBJFRx9o9wFR8IGchbVqr6L50cs8KUwFOgqAFy3w6Saw2ocspBymEU8yg1EfGLXy1yJ10htUCftH1UMStcTgsU0B2CmtFe7KJhDJ7CuxYq5uAR5dMdAPoR4f8iHe7VF6TlDgqVh4QXuOV00Cw8c8oOJVFc8wjMyzHBWf1ThsQFnYRC1AY%2BBrB2g%2F54XfVGGcPCbj2%2FDMe%2BdU4yVNGuepeutwpXOrL8GghP1fM3VY1hc66qQUow3wAgd7sX3BFdBOUzQGL7BEOL06TRQAnuPxG%2B6pdOoaiu8T6Hg%2FAMiLJmEGicCbTs0gpZOZXJeNB%2FX1AcL%2BngwhXoa2XJ3WGGGLWC2wkRpmVhQ1fvrr%2F%2BUGSa1ikU%2B%2BWMIjWgb0GOqUBhCvsDQYp7xZ8d6iJwP%2BsdwcEvnS7TXMcTqTYyUkdGbpZfFCgNCz5Kqm8bAwHTuQK47IwMqHwOQxppzE06YXFRKqaPG9mAEVlI0HmEp%2B4oAyIIm%2Fbu%2FxoZnG99X004Swe%2FxrHIgLjJ4drupcElGcV0nXsjsYfBRhjVVVQ4psdf%2FPZ2VQ8BuGt%2Byuk%2FvitzA4bQN5VFd%2BEsN5uU34Nl8YkDLjQOyeM&X-Amz-Signature=1f6eb761baa2da63517de8be2236b43a1204d844ba09f8451b9e6cfab2833041&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRLNN2B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDse%2B6%2BJpmEA1kjPv%2BVmvL1nHJm4MaE0m6dQh%2F2uy2ldAiEA%2B5vSksdXk0UNNmvLFk2%2BLUr%2FhiZ9R0K5bEHp8L5ihJwq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDOzNC4ZMWlOiiq2thyrcAwaQP3gjAZoOOtj3fzHybxWm%2FdWeCOvCbdJdSD%2BpZM8kaZjSNdbhJDARYKrfHHlkuVNYKB3XXWpIdHgxK0jVgVQOl8f8bHI3clgqzxUV0uxpRAg6%2FpVMK3%2BV5gRc8EdPTzVbM8JO3o5ucCFEO7rwv%2BuDL7IwihOQhJqtwJGmmLX%2FFlbg9kU49CCExvE8omUEoKvLXLLBvTTUE06aixoC22j0sjPyN0Xn%2FHbSXHgxX0kjO9njgw2Ptil2PqO7wTEHTywA%2FrP0LB0%2FBJFRx9o9wFR8IGchbVqr6L50cs8KUwFOgqAFy3w6Saw2ocspBymEU8yg1EfGLXy1yJ10htUCftH1UMStcTgsU0B2CmtFe7KJhDJ7CuxYq5uAR5dMdAPoR4f8iHe7VF6TlDgqVh4QXuOV00Cw8c8oOJVFc8wjMyzHBWf1ThsQFnYRC1AY%2BBrB2g%2F54XfVGGcPCbj2%2FDMe%2BdU4yVNGuepeutwpXOrL8GghP1fM3VY1hc66qQUow3wAgd7sX3BFdBOUzQGL7BEOL06TRQAnuPxG%2B6pdOoaiu8T6Hg%2FAMiLJmEGicCbTs0gpZOZXJeNB%2FX1AcL%2BngwhXoa2XJ3WGGGLWC2wkRpmVhQ1fvrr%2F%2BUGSa1ikU%2B%2BWMIjWgb0GOqUBhCvsDQYp7xZ8d6iJwP%2BsdwcEvnS7TXMcTqTYyUkdGbpZfFCgNCz5Kqm8bAwHTuQK47IwMqHwOQxppzE06YXFRKqaPG9mAEVlI0HmEp%2B4oAyIIm%2Fbu%2FxoZnG99X004Swe%2FxrHIgLjJ4drupcElGcV0nXsjsYfBRhjVVVQ4psdf%2FPZ2VQ8BuGt%2Byuk%2FvitzA4bQN5VFd%2BEsN5uU34Nl8YkDLjQOyeM&X-Amz-Signature=a8615bd86f74943f0f968b366a6e446e9388101e8e344bf7ccd91acd2568d205&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRLNN2B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDse%2B6%2BJpmEA1kjPv%2BVmvL1nHJm4MaE0m6dQh%2F2uy2ldAiEA%2B5vSksdXk0UNNmvLFk2%2BLUr%2FhiZ9R0K5bEHp8L5ihJwq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDOzNC4ZMWlOiiq2thyrcAwaQP3gjAZoOOtj3fzHybxWm%2FdWeCOvCbdJdSD%2BpZM8kaZjSNdbhJDARYKrfHHlkuVNYKB3XXWpIdHgxK0jVgVQOl8f8bHI3clgqzxUV0uxpRAg6%2FpVMK3%2BV5gRc8EdPTzVbM8JO3o5ucCFEO7rwv%2BuDL7IwihOQhJqtwJGmmLX%2FFlbg9kU49CCExvE8omUEoKvLXLLBvTTUE06aixoC22j0sjPyN0Xn%2FHbSXHgxX0kjO9njgw2Ptil2PqO7wTEHTywA%2FrP0LB0%2FBJFRx9o9wFR8IGchbVqr6L50cs8KUwFOgqAFy3w6Saw2ocspBymEU8yg1EfGLXy1yJ10htUCftH1UMStcTgsU0B2CmtFe7KJhDJ7CuxYq5uAR5dMdAPoR4f8iHe7VF6TlDgqVh4QXuOV00Cw8c8oOJVFc8wjMyzHBWf1ThsQFnYRC1AY%2BBrB2g%2F54XfVGGcPCbj2%2FDMe%2BdU4yVNGuepeutwpXOrL8GghP1fM3VY1hc66qQUow3wAgd7sX3BFdBOUzQGL7BEOL06TRQAnuPxG%2B6pdOoaiu8T6Hg%2FAMiLJmEGicCbTs0gpZOZXJeNB%2FX1AcL%2BngwhXoa2XJ3WGGGLWC2wkRpmVhQ1fvrr%2F%2BUGSa1ikU%2B%2BWMIjWgb0GOqUBhCvsDQYp7xZ8d6iJwP%2BsdwcEvnS7TXMcTqTYyUkdGbpZfFCgNCz5Kqm8bAwHTuQK47IwMqHwOQxppzE06YXFRKqaPG9mAEVlI0HmEp%2B4oAyIIm%2Fbu%2FxoZnG99X004Swe%2FxrHIgLjJ4drupcElGcV0nXsjsYfBRhjVVVQ4psdf%2FPZ2VQ8BuGt%2Byuk%2FvitzA4bQN5VFd%2BEsN5uU34Nl8YkDLjQOyeM&X-Amz-Signature=81e0c92a34a45e7f437ab076355bed57bac5ee3ec5255676ceedaac5036ce068&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRLNN2B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDse%2B6%2BJpmEA1kjPv%2BVmvL1nHJm4MaE0m6dQh%2F2uy2ldAiEA%2B5vSksdXk0UNNmvLFk2%2BLUr%2FhiZ9R0K5bEHp8L5ihJwq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDOzNC4ZMWlOiiq2thyrcAwaQP3gjAZoOOtj3fzHybxWm%2FdWeCOvCbdJdSD%2BpZM8kaZjSNdbhJDARYKrfHHlkuVNYKB3XXWpIdHgxK0jVgVQOl8f8bHI3clgqzxUV0uxpRAg6%2FpVMK3%2BV5gRc8EdPTzVbM8JO3o5ucCFEO7rwv%2BuDL7IwihOQhJqtwJGmmLX%2FFlbg9kU49CCExvE8omUEoKvLXLLBvTTUE06aixoC22j0sjPyN0Xn%2FHbSXHgxX0kjO9njgw2Ptil2PqO7wTEHTywA%2FrP0LB0%2FBJFRx9o9wFR8IGchbVqr6L50cs8KUwFOgqAFy3w6Saw2ocspBymEU8yg1EfGLXy1yJ10htUCftH1UMStcTgsU0B2CmtFe7KJhDJ7CuxYq5uAR5dMdAPoR4f8iHe7VF6TlDgqVh4QXuOV00Cw8c8oOJVFc8wjMyzHBWf1ThsQFnYRC1AY%2BBrB2g%2F54XfVGGcPCbj2%2FDMe%2BdU4yVNGuepeutwpXOrL8GghP1fM3VY1hc66qQUow3wAgd7sX3BFdBOUzQGL7BEOL06TRQAnuPxG%2B6pdOoaiu8T6Hg%2FAMiLJmEGicCbTs0gpZOZXJeNB%2FX1AcL%2BngwhXoa2XJ3WGGGLWC2wkRpmVhQ1fvrr%2F%2BUGSa1ikU%2B%2BWMIjWgb0GOqUBhCvsDQYp7xZ8d6iJwP%2BsdwcEvnS7TXMcTqTYyUkdGbpZfFCgNCz5Kqm8bAwHTuQK47IwMqHwOQxppzE06YXFRKqaPG9mAEVlI0HmEp%2B4oAyIIm%2Fbu%2FxoZnG99X004Swe%2FxrHIgLjJ4drupcElGcV0nXsjsYfBRhjVVVQ4psdf%2FPZ2VQ8BuGt%2Byuk%2FvitzA4bQN5VFd%2BEsN5uU34Nl8YkDLjQOyeM&X-Amz-Signature=d575502ab76e335ff4c1027900b47e3d9a2ab3da4b4c73c4cf54f23e6839907b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRLNN2B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDse%2B6%2BJpmEA1kjPv%2BVmvL1nHJm4MaE0m6dQh%2F2uy2ldAiEA%2B5vSksdXk0UNNmvLFk2%2BLUr%2FhiZ9R0K5bEHp8L5ihJwq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDOzNC4ZMWlOiiq2thyrcAwaQP3gjAZoOOtj3fzHybxWm%2FdWeCOvCbdJdSD%2BpZM8kaZjSNdbhJDARYKrfHHlkuVNYKB3XXWpIdHgxK0jVgVQOl8f8bHI3clgqzxUV0uxpRAg6%2FpVMK3%2BV5gRc8EdPTzVbM8JO3o5ucCFEO7rwv%2BuDL7IwihOQhJqtwJGmmLX%2FFlbg9kU49CCExvE8omUEoKvLXLLBvTTUE06aixoC22j0sjPyN0Xn%2FHbSXHgxX0kjO9njgw2Ptil2PqO7wTEHTywA%2FrP0LB0%2FBJFRx9o9wFR8IGchbVqr6L50cs8KUwFOgqAFy3w6Saw2ocspBymEU8yg1EfGLXy1yJ10htUCftH1UMStcTgsU0B2CmtFe7KJhDJ7CuxYq5uAR5dMdAPoR4f8iHe7VF6TlDgqVh4QXuOV00Cw8c8oOJVFc8wjMyzHBWf1ThsQFnYRC1AY%2BBrB2g%2F54XfVGGcPCbj2%2FDMe%2BdU4yVNGuepeutwpXOrL8GghP1fM3VY1hc66qQUow3wAgd7sX3BFdBOUzQGL7BEOL06TRQAnuPxG%2B6pdOoaiu8T6Hg%2FAMiLJmEGicCbTs0gpZOZXJeNB%2FX1AcL%2BngwhXoa2XJ3WGGGLWC2wkRpmVhQ1fvrr%2F%2BUGSa1ikU%2B%2BWMIjWgb0GOqUBhCvsDQYp7xZ8d6iJwP%2BsdwcEvnS7TXMcTqTYyUkdGbpZfFCgNCz5Kqm8bAwHTuQK47IwMqHwOQxppzE06YXFRKqaPG9mAEVlI0HmEp%2B4oAyIIm%2Fbu%2FxoZnG99X004Swe%2FxrHIgLjJ4drupcElGcV0nXsjsYfBRhjVVVQ4psdf%2FPZ2VQ8BuGt%2Byuk%2FvitzA4bQN5VFd%2BEsN5uU34Nl8YkDLjQOyeM&X-Amz-Signature=f85b6fe3cdf60b6fa00033499470a7f14ef2ed31991eda358c02d8333450c61b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4YAY54%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzrago2QRiNUb4UYFdk0is%2BfL2X5BW4lSpN9LBSzn5yQIgMqxjSooXh%2FcJLHn7EI65n85co58PgD9%2Fe0e68ivadsUq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJdULt2%2B9lqwnqIeVircAyvPRbeYJuUzQ9y8e21aoU7xh2KOpVSIaUmQ5whj6CaTmz6VUD6HIkwH%2FVSjoqaFLuTEewr80mGnLxolfBreVVkvbijKV6teEMDEvlI4Wi84B4nAGpqZ2Cc%2FCRvdzwMwm%2FOJJ3LwQ4mbfO18DpEiaRwKDH4gOtdG0o6OLvokFuFCQam5CKvb7ml7ksO91H8OEmscjEyEEk%2FAK%2FkoH6UkSJqwmWSuhTxauXUgJ4uLCFza6RJlJVMK5Y85AiYVZhGvSRDlTiK0ULKpndjIR5hIhhMT0hopwd40Ggm%2FZrd6Z03I1XKjPtLg7Nbc3WrKqJBajWEfqrTsHMcg0jb0wStUbjIoYEUS4I0vo3H%2F1u%2FIZdYcPYQS6LOcE8pEdKeG65Kmt%2BsBjFAJLTqXPAq4K%2FrsVrjjugld35lCBgh3AkODxtTmX066NiRwsdkvzXDFjM4Sd9ytUMnJOzyHuwM5Eltv4eogL3IuOm9OPjFobxRieZHbOOnegWQI%2BD%2BXs%2BPjjbhc0HyGqCtsp7vVVBQ0deHvwsz3jy1kvuKn0Vt1cFOI5smaAIsAQSy0DmraCV6vx1NV5UTBwbNTOBeJdm1VZrfETgiVuKqLymW6%2BUwEq8APQbfkkJ17k8NgWQSirr0RMI7Xgb0GOqUBQE%2BmirhCoybpzJKmKXsXAVRqiO%2BMBHTQ7wOJ5fvri8b77AliZZVqyMW1OajyHyNOG0EL5K0A8m3Ri5T7KUrCAGjUWnj3ONzlRQVHt246WvTdpdinedkUIyPIV9UIjnAp3UrWG6vgiU8aKHD2POPO4iIDhzI8nv6cpBprkSHVQaokaJMbpSb1%2BU3nJFQylbawhAixK%2FfSTWN1n3ckLj%2Fa7wnprIiL&X-Amz-Signature=bfaa4188d10eeb2913246437dbfc576d994fb06e6d7d541b9e6ee0e4a26503a6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4YAY54%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzrago2QRiNUb4UYFdk0is%2BfL2X5BW4lSpN9LBSzn5yQIgMqxjSooXh%2FcJLHn7EI65n85co58PgD9%2Fe0e68ivadsUq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJdULt2%2B9lqwnqIeVircAyvPRbeYJuUzQ9y8e21aoU7xh2KOpVSIaUmQ5whj6CaTmz6VUD6HIkwH%2FVSjoqaFLuTEewr80mGnLxolfBreVVkvbijKV6teEMDEvlI4Wi84B4nAGpqZ2Cc%2FCRvdzwMwm%2FOJJ3LwQ4mbfO18DpEiaRwKDH4gOtdG0o6OLvokFuFCQam5CKvb7ml7ksO91H8OEmscjEyEEk%2FAK%2FkoH6UkSJqwmWSuhTxauXUgJ4uLCFza6RJlJVMK5Y85AiYVZhGvSRDlTiK0ULKpndjIR5hIhhMT0hopwd40Ggm%2FZrd6Z03I1XKjPtLg7Nbc3WrKqJBajWEfqrTsHMcg0jb0wStUbjIoYEUS4I0vo3H%2F1u%2FIZdYcPYQS6LOcE8pEdKeG65Kmt%2BsBjFAJLTqXPAq4K%2FrsVrjjugld35lCBgh3AkODxtTmX066NiRwsdkvzXDFjM4Sd9ytUMnJOzyHuwM5Eltv4eogL3IuOm9OPjFobxRieZHbOOnegWQI%2BD%2BXs%2BPjjbhc0HyGqCtsp7vVVBQ0deHvwsz3jy1kvuKn0Vt1cFOI5smaAIsAQSy0DmraCV6vx1NV5UTBwbNTOBeJdm1VZrfETgiVuKqLymW6%2BUwEq8APQbfkkJ17k8NgWQSirr0RMI7Xgb0GOqUBQE%2BmirhCoybpzJKmKXsXAVRqiO%2BMBHTQ7wOJ5fvri8b77AliZZVqyMW1OajyHyNOG0EL5K0A8m3Ri5T7KUrCAGjUWnj3ONzlRQVHt246WvTdpdinedkUIyPIV9UIjnAp3UrWG6vgiU8aKHD2POPO4iIDhzI8nv6cpBprkSHVQaokaJMbpSb1%2BU3nJFQylbawhAixK%2FfSTWN1n3ckLj%2Fa7wnprIiL&X-Amz-Signature=d242bd331236c958413652576aa8038da0bfe206baac61e5ad177059b809361c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4YAY54%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzrago2QRiNUb4UYFdk0is%2BfL2X5BW4lSpN9LBSzn5yQIgMqxjSooXh%2FcJLHn7EI65n85co58PgD9%2Fe0e68ivadsUq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJdULt2%2B9lqwnqIeVircAyvPRbeYJuUzQ9y8e21aoU7xh2KOpVSIaUmQ5whj6CaTmz6VUD6HIkwH%2FVSjoqaFLuTEewr80mGnLxolfBreVVkvbijKV6teEMDEvlI4Wi84B4nAGpqZ2Cc%2FCRvdzwMwm%2FOJJ3LwQ4mbfO18DpEiaRwKDH4gOtdG0o6OLvokFuFCQam5CKvb7ml7ksO91H8OEmscjEyEEk%2FAK%2FkoH6UkSJqwmWSuhTxauXUgJ4uLCFza6RJlJVMK5Y85AiYVZhGvSRDlTiK0ULKpndjIR5hIhhMT0hopwd40Ggm%2FZrd6Z03I1XKjPtLg7Nbc3WrKqJBajWEfqrTsHMcg0jb0wStUbjIoYEUS4I0vo3H%2F1u%2FIZdYcPYQS6LOcE8pEdKeG65Kmt%2BsBjFAJLTqXPAq4K%2FrsVrjjugld35lCBgh3AkODxtTmX066NiRwsdkvzXDFjM4Sd9ytUMnJOzyHuwM5Eltv4eogL3IuOm9OPjFobxRieZHbOOnegWQI%2BD%2BXs%2BPjjbhc0HyGqCtsp7vVVBQ0deHvwsz3jy1kvuKn0Vt1cFOI5smaAIsAQSy0DmraCV6vx1NV5UTBwbNTOBeJdm1VZrfETgiVuKqLymW6%2BUwEq8APQbfkkJ17k8NgWQSirr0RMI7Xgb0GOqUBQE%2BmirhCoybpzJKmKXsXAVRqiO%2BMBHTQ7wOJ5fvri8b77AliZZVqyMW1OajyHyNOG0EL5K0A8m3Ri5T7KUrCAGjUWnj3ONzlRQVHt246WvTdpdinedkUIyPIV9UIjnAp3UrWG6vgiU8aKHD2POPO4iIDhzI8nv6cpBprkSHVQaokaJMbpSb1%2BU3nJFQylbawhAixK%2FfSTWN1n3ckLj%2Fa7wnprIiL&X-Amz-Signature=b30237efc7a00a0e7c6ab4ec3fb4b3a9bbf28aa51fea962126e477eb1b5f3044&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4YAY54%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzrago2QRiNUb4UYFdk0is%2BfL2X5BW4lSpN9LBSzn5yQIgMqxjSooXh%2FcJLHn7EI65n85co58PgD9%2Fe0e68ivadsUq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJdULt2%2B9lqwnqIeVircAyvPRbeYJuUzQ9y8e21aoU7xh2KOpVSIaUmQ5whj6CaTmz6VUD6HIkwH%2FVSjoqaFLuTEewr80mGnLxolfBreVVkvbijKV6teEMDEvlI4Wi84B4nAGpqZ2Cc%2FCRvdzwMwm%2FOJJ3LwQ4mbfO18DpEiaRwKDH4gOtdG0o6OLvokFuFCQam5CKvb7ml7ksO91H8OEmscjEyEEk%2FAK%2FkoH6UkSJqwmWSuhTxauXUgJ4uLCFza6RJlJVMK5Y85AiYVZhGvSRDlTiK0ULKpndjIR5hIhhMT0hopwd40Ggm%2FZrd6Z03I1XKjPtLg7Nbc3WrKqJBajWEfqrTsHMcg0jb0wStUbjIoYEUS4I0vo3H%2F1u%2FIZdYcPYQS6LOcE8pEdKeG65Kmt%2BsBjFAJLTqXPAq4K%2FrsVrjjugld35lCBgh3AkODxtTmX066NiRwsdkvzXDFjM4Sd9ytUMnJOzyHuwM5Eltv4eogL3IuOm9OPjFobxRieZHbOOnegWQI%2BD%2BXs%2BPjjbhc0HyGqCtsp7vVVBQ0deHvwsz3jy1kvuKn0Vt1cFOI5smaAIsAQSy0DmraCV6vx1NV5UTBwbNTOBeJdm1VZrfETgiVuKqLymW6%2BUwEq8APQbfkkJ17k8NgWQSirr0RMI7Xgb0GOqUBQE%2BmirhCoybpzJKmKXsXAVRqiO%2BMBHTQ7wOJ5fvri8b77AliZZVqyMW1OajyHyNOG0EL5K0A8m3Ri5T7KUrCAGjUWnj3ONzlRQVHt246WvTdpdinedkUIyPIV9UIjnAp3UrWG6vgiU8aKHD2POPO4iIDhzI8nv6cpBprkSHVQaokaJMbpSb1%2BU3nJFQylbawhAixK%2FfSTWN1n3ckLj%2Fa7wnprIiL&X-Amz-Signature=0cc7046a04a243423fa89b14184eb82fdb0c29a791ef327062ec333c54ead4fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4YAY54%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzrago2QRiNUb4UYFdk0is%2BfL2X5BW4lSpN9LBSzn5yQIgMqxjSooXh%2FcJLHn7EI65n85co58PgD9%2Fe0e68ivadsUq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJdULt2%2B9lqwnqIeVircAyvPRbeYJuUzQ9y8e21aoU7xh2KOpVSIaUmQ5whj6CaTmz6VUD6HIkwH%2FVSjoqaFLuTEewr80mGnLxolfBreVVkvbijKV6teEMDEvlI4Wi84B4nAGpqZ2Cc%2FCRvdzwMwm%2FOJJ3LwQ4mbfO18DpEiaRwKDH4gOtdG0o6OLvokFuFCQam5CKvb7ml7ksO91H8OEmscjEyEEk%2FAK%2FkoH6UkSJqwmWSuhTxauXUgJ4uLCFza6RJlJVMK5Y85AiYVZhGvSRDlTiK0ULKpndjIR5hIhhMT0hopwd40Ggm%2FZrd6Z03I1XKjPtLg7Nbc3WrKqJBajWEfqrTsHMcg0jb0wStUbjIoYEUS4I0vo3H%2F1u%2FIZdYcPYQS6LOcE8pEdKeG65Kmt%2BsBjFAJLTqXPAq4K%2FrsVrjjugld35lCBgh3AkODxtTmX066NiRwsdkvzXDFjM4Sd9ytUMnJOzyHuwM5Eltv4eogL3IuOm9OPjFobxRieZHbOOnegWQI%2BD%2BXs%2BPjjbhc0HyGqCtsp7vVVBQ0deHvwsz3jy1kvuKn0Vt1cFOI5smaAIsAQSy0DmraCV6vx1NV5UTBwbNTOBeJdm1VZrfETgiVuKqLymW6%2BUwEq8APQbfkkJ17k8NgWQSirr0RMI7Xgb0GOqUBQE%2BmirhCoybpzJKmKXsXAVRqiO%2BMBHTQ7wOJ5fvri8b77AliZZVqyMW1OajyHyNOG0EL5K0A8m3Ri5T7KUrCAGjUWnj3ONzlRQVHt246WvTdpdinedkUIyPIV9UIjnAp3UrWG6vgiU8aKHD2POPO4iIDhzI8nv6cpBprkSHVQaokaJMbpSb1%2BU3nJFQylbawhAixK%2FfSTWN1n3ckLj%2Fa7wnprIiL&X-Amz-Signature=9c71ac8e0456662b1cfb907559894b07659e915071e1dd1b3645e94b1b6544ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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


