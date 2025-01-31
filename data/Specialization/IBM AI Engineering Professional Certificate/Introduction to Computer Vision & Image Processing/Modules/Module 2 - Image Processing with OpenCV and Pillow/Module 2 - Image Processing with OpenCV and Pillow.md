

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV27AUSR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIo46TWOJytc63RBc%2FMmTaecJ0BA3FnsEXNyaVeXNX0wIgYjR5dwZEmMoNPiYYXQQx3cyYHOgZIVAnspYaLUmgBhcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1VTxu8At6INmZG1SrcAyLzBpyYzHJNrRvSwa8hyWPCY2K4Pke8R8kTqoZEUsPKuuSKqzdtFKzd4bOcRSFAgGU0rEA3LIdRj9Z5VqT2mjtYFUApZ1jYqphgXKx49pnypysVxeqLnwlFkwtLcsC3vuJFVChJJYVrQzIABTK%2BOvCRpKzQjqHVlEiTKik3HCR6TrF56FSQzztVlojAZkkLMwCy8hHRp7CWbqtaf10rsP94RolBezZnrnEsgKUZpbvB7G9q6uRKDOtVQMLzm9iU5iXD0bQ4jeYDZckqeJBiHyPA%2FrMtJWl%2B45h5tNl5K7uXQMYqBH0qHT8y6t%2F%2BGRwk9OrL1pLGpvv4a3LK4knRwJf%2B8v0UbzGrBvWChUsiqs%2FpjJtqA28qyEd7gu%2FMRVUhDb6tVT7J2Y5cMZzqBg30NZhCWTUjJHaR5hMidsVPRdCgQG0ZyOekwz2qIYEj27CPu1dZSknszEYPWVHyCUnYefEqDvg9DXW%2F%2F5JVOOuDp2voYRxQr%2FJ5sLcUJ5tsGjwHdYWLv3nZolj6X%2BTfmN5HYcXQ6kfyTHaI3DzE0ruakA5Aw2iyTt%2BCD%2Bf5tYcJ1DbobHEvZB9a7qUCBlRdrkIb8EDjU2bV17XEHJNA6%2BQ%2BzdddhS6YYKl9RCCxmp8BMK628rwGOqUBQ5fHhSYrs2Nc1n8RcB8nrFnU%2Fv5CtXph7v1XVp18Y6EkpgtMDaG8DMjPWIfG2nBP0VXs2xoOYNX6JWxX5Go7KL%2B0%2FNIcY1vEklClkkUGTyS%2BKFxDump4D02GMhEbg8aoFHxoDtpAwuzmy9o8jzyLKaguxOhaA0Wk9Svk3%2Fee9DEF4J0Hr7FJHJHtFKKrekog1y5LRiWqyqdrvbkOy4H7eDrITS3%2B&X-Amz-Signature=30425a8fce97538a18a81ef7424c9d13f4e4cade1d44418063a3a835a81cf1a1&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFXI2LTX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkv00QTOxx%2BIfEZNuoo6BKET8M20muY10PBst%2FPubswIhAM%2FiaPFNoMs%2FJLS39CRf1C%2BudRdLTF30%2FZCIhLyVifu9KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1NEGmYFrEjDzJ8sgq3ANe%2B9i6CVs%2BeyyClVB8okOf%2FE6GeOBiO5kePLyLzgFs%2F6FO5Ynn%2B0ASlHi8EvNAHqsgvRF0iZ%2BMPc0ctHRsG7EL9P%2FlSytDGHrfsc0Iq5uEawbl3e5A3RtM7uh7Ao34QJpwPqar8U3%2BQFFnCtTEXjHHX3l4IaE6Ml8IfMWC4cT6wr61Q4rcKCVxzr2VHo1s7y%2BmM42sp%2BGZ85aQ3JiXpmZd3FLE7Mmv1hHX46x7PWQrKFqHi05koFBsHKReTh4iMpa0dq3JmRr8Nee1un15rInVjgc3NbNljiE3LHpf06pLIeQoyG7VmrXaRrsuTBGZQwA0n4n9j6TCbxiIYB1iJM%2BnNQX1XlzIi2Fm4x7Ge%2FT4nUJVF14Odocw9qizpjtP8LHiI28sPkUzJh5doaEHRdfaDosTbfzXqqBehLiTBvevB8MCZeEOVkVzy%2Bp8l904a5lBEixrl5x%2BZpHfne0vjsBkxfIrQ0eo8L6R%2BYY9T0JJLqae19zEUAuXQ7d71pfr5WPp9YwVoEFtruMOLpyEur34TdCov9tqHHD7PUcBjavB8o%2FvvM8e7kzpYWtukG6jix%2B25Q8Fs%2FaSg9E%2FUYOLBlTNHO1dCqOjz%2Bm3lhL6vyaKGGeUO8bdBd0HpvkWNTDEt%2FK8BjqkAU7WFeea97%2F015ubKuSkmCC8rDpowVQ041awq89zwvRPm8UQ7zXejcuFFw8WYXcLjueMPsyPtkmKc%2FHU3uFuKvopbvef2xy1eMsNOSrs8feG7qMg05C%2Fh5wJeKcBK3OSp%2F6x7UAjqadE0ESoUJghhgV8IxgK8EjPhJUS2I7gajd0dYoejKt%2B10DTvXRz34Vsw1tt1cuQy%2FASC7nStkbjssc9qD4n&X-Amz-Signature=4525dcc0cd86828310670abbf29a0235ebed499d7bb4f32c27ef23e450fffdfc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFXI2LTX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkv00QTOxx%2BIfEZNuoo6BKET8M20muY10PBst%2FPubswIhAM%2FiaPFNoMs%2FJLS39CRf1C%2BudRdLTF30%2FZCIhLyVifu9KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1NEGmYFrEjDzJ8sgq3ANe%2B9i6CVs%2BeyyClVB8okOf%2FE6GeOBiO5kePLyLzgFs%2F6FO5Ynn%2B0ASlHi8EvNAHqsgvRF0iZ%2BMPc0ctHRsG7EL9P%2FlSytDGHrfsc0Iq5uEawbl3e5A3RtM7uh7Ao34QJpwPqar8U3%2BQFFnCtTEXjHHX3l4IaE6Ml8IfMWC4cT6wr61Q4rcKCVxzr2VHo1s7y%2BmM42sp%2BGZ85aQ3JiXpmZd3FLE7Mmv1hHX46x7PWQrKFqHi05koFBsHKReTh4iMpa0dq3JmRr8Nee1un15rInVjgc3NbNljiE3LHpf06pLIeQoyG7VmrXaRrsuTBGZQwA0n4n9j6TCbxiIYB1iJM%2BnNQX1XlzIi2Fm4x7Ge%2FT4nUJVF14Odocw9qizpjtP8LHiI28sPkUzJh5doaEHRdfaDosTbfzXqqBehLiTBvevB8MCZeEOVkVzy%2Bp8l904a5lBEixrl5x%2BZpHfne0vjsBkxfIrQ0eo8L6R%2BYY9T0JJLqae19zEUAuXQ7d71pfr5WPp9YwVoEFtruMOLpyEur34TdCov9tqHHD7PUcBjavB8o%2FvvM8e7kzpYWtukG6jix%2B25Q8Fs%2FaSg9E%2FUYOLBlTNHO1dCqOjz%2Bm3lhL6vyaKGGeUO8bdBd0HpvkWNTDEt%2FK8BjqkAU7WFeea97%2F015ubKuSkmCC8rDpowVQ041awq89zwvRPm8UQ7zXejcuFFw8WYXcLjueMPsyPtkmKc%2FHU3uFuKvopbvef2xy1eMsNOSrs8feG7qMg05C%2Fh5wJeKcBK3OSp%2F6x7UAjqadE0ESoUJghhgV8IxgK8EjPhJUS2I7gajd0dYoejKt%2B10DTvXRz34Vsw1tt1cuQy%2FASC7nStkbjssc9qD4n&X-Amz-Signature=d31023d3376d377d75a6643362c0b7b65f1207f9a76b2dae5cd75c7c83130ad7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFXI2LTX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkv00QTOxx%2BIfEZNuoo6BKET8M20muY10PBst%2FPubswIhAM%2FiaPFNoMs%2FJLS39CRf1C%2BudRdLTF30%2FZCIhLyVifu9KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1NEGmYFrEjDzJ8sgq3ANe%2B9i6CVs%2BeyyClVB8okOf%2FE6GeOBiO5kePLyLzgFs%2F6FO5Ynn%2B0ASlHi8EvNAHqsgvRF0iZ%2BMPc0ctHRsG7EL9P%2FlSytDGHrfsc0Iq5uEawbl3e5A3RtM7uh7Ao34QJpwPqar8U3%2BQFFnCtTEXjHHX3l4IaE6Ml8IfMWC4cT6wr61Q4rcKCVxzr2VHo1s7y%2BmM42sp%2BGZ85aQ3JiXpmZd3FLE7Mmv1hHX46x7PWQrKFqHi05koFBsHKReTh4iMpa0dq3JmRr8Nee1un15rInVjgc3NbNljiE3LHpf06pLIeQoyG7VmrXaRrsuTBGZQwA0n4n9j6TCbxiIYB1iJM%2BnNQX1XlzIi2Fm4x7Ge%2FT4nUJVF14Odocw9qizpjtP8LHiI28sPkUzJh5doaEHRdfaDosTbfzXqqBehLiTBvevB8MCZeEOVkVzy%2Bp8l904a5lBEixrl5x%2BZpHfne0vjsBkxfIrQ0eo8L6R%2BYY9T0JJLqae19zEUAuXQ7d71pfr5WPp9YwVoEFtruMOLpyEur34TdCov9tqHHD7PUcBjavB8o%2FvvM8e7kzpYWtukG6jix%2B25Q8Fs%2FaSg9E%2FUYOLBlTNHO1dCqOjz%2Bm3lhL6vyaKGGeUO8bdBd0HpvkWNTDEt%2FK8BjqkAU7WFeea97%2F015ubKuSkmCC8rDpowVQ041awq89zwvRPm8UQ7zXejcuFFw8WYXcLjueMPsyPtkmKc%2FHU3uFuKvopbvef2xy1eMsNOSrs8feG7qMg05C%2Fh5wJeKcBK3OSp%2F6x7UAjqadE0ESoUJghhgV8IxgK8EjPhJUS2I7gajd0dYoejKt%2B10DTvXRz34Vsw1tt1cuQy%2FASC7nStkbjssc9qD4n&X-Amz-Signature=ba0af78c194d5db53a6bf6d863ff4ccdc4a5d4729643aaeafdde4339213a35be&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFXI2LTX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkv00QTOxx%2BIfEZNuoo6BKET8M20muY10PBst%2FPubswIhAM%2FiaPFNoMs%2FJLS39CRf1C%2BudRdLTF30%2FZCIhLyVifu9KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1NEGmYFrEjDzJ8sgq3ANe%2B9i6CVs%2BeyyClVB8okOf%2FE6GeOBiO5kePLyLzgFs%2F6FO5Ynn%2B0ASlHi8EvNAHqsgvRF0iZ%2BMPc0ctHRsG7EL9P%2FlSytDGHrfsc0Iq5uEawbl3e5A3RtM7uh7Ao34QJpwPqar8U3%2BQFFnCtTEXjHHX3l4IaE6Ml8IfMWC4cT6wr61Q4rcKCVxzr2VHo1s7y%2BmM42sp%2BGZ85aQ3JiXpmZd3FLE7Mmv1hHX46x7PWQrKFqHi05koFBsHKReTh4iMpa0dq3JmRr8Nee1un15rInVjgc3NbNljiE3LHpf06pLIeQoyG7VmrXaRrsuTBGZQwA0n4n9j6TCbxiIYB1iJM%2BnNQX1XlzIi2Fm4x7Ge%2FT4nUJVF14Odocw9qizpjtP8LHiI28sPkUzJh5doaEHRdfaDosTbfzXqqBehLiTBvevB8MCZeEOVkVzy%2Bp8l904a5lBEixrl5x%2BZpHfne0vjsBkxfIrQ0eo8L6R%2BYY9T0JJLqae19zEUAuXQ7d71pfr5WPp9YwVoEFtruMOLpyEur34TdCov9tqHHD7PUcBjavB8o%2FvvM8e7kzpYWtukG6jix%2B25Q8Fs%2FaSg9E%2FUYOLBlTNHO1dCqOjz%2Bm3lhL6vyaKGGeUO8bdBd0HpvkWNTDEt%2FK8BjqkAU7WFeea97%2F015ubKuSkmCC8rDpowVQ041awq89zwvRPm8UQ7zXejcuFFw8WYXcLjueMPsyPtkmKc%2FHU3uFuKvopbvef2xy1eMsNOSrs8feG7qMg05C%2Fh5wJeKcBK3OSp%2F6x7UAjqadE0ESoUJghhgV8IxgK8EjPhJUS2I7gajd0dYoejKt%2B10DTvXRz34Vsw1tt1cuQy%2FASC7nStkbjssc9qD4n&X-Amz-Signature=97f0f9bfab9bc91858807daad89a6429d04ba8df41f064305d52320e0adef587&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFXI2LTX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkv00QTOxx%2BIfEZNuoo6BKET8M20muY10PBst%2FPubswIhAM%2FiaPFNoMs%2FJLS39CRf1C%2BudRdLTF30%2FZCIhLyVifu9KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1NEGmYFrEjDzJ8sgq3ANe%2B9i6CVs%2BeyyClVB8okOf%2FE6GeOBiO5kePLyLzgFs%2F6FO5Ynn%2B0ASlHi8EvNAHqsgvRF0iZ%2BMPc0ctHRsG7EL9P%2FlSytDGHrfsc0Iq5uEawbl3e5A3RtM7uh7Ao34QJpwPqar8U3%2BQFFnCtTEXjHHX3l4IaE6Ml8IfMWC4cT6wr61Q4rcKCVxzr2VHo1s7y%2BmM42sp%2BGZ85aQ3JiXpmZd3FLE7Mmv1hHX46x7PWQrKFqHi05koFBsHKReTh4iMpa0dq3JmRr8Nee1un15rInVjgc3NbNljiE3LHpf06pLIeQoyG7VmrXaRrsuTBGZQwA0n4n9j6TCbxiIYB1iJM%2BnNQX1XlzIi2Fm4x7Ge%2FT4nUJVF14Odocw9qizpjtP8LHiI28sPkUzJh5doaEHRdfaDosTbfzXqqBehLiTBvevB8MCZeEOVkVzy%2Bp8l904a5lBEixrl5x%2BZpHfne0vjsBkxfIrQ0eo8L6R%2BYY9T0JJLqae19zEUAuXQ7d71pfr5WPp9YwVoEFtruMOLpyEur34TdCov9tqHHD7PUcBjavB8o%2FvvM8e7kzpYWtukG6jix%2B25Q8Fs%2FaSg9E%2FUYOLBlTNHO1dCqOjz%2Bm3lhL6vyaKGGeUO8bdBd0HpvkWNTDEt%2FK8BjqkAU7WFeea97%2F015ubKuSkmCC8rDpowVQ041awq89zwvRPm8UQ7zXejcuFFw8WYXcLjueMPsyPtkmKc%2FHU3uFuKvopbvef2xy1eMsNOSrs8feG7qMg05C%2Fh5wJeKcBK3OSp%2F6x7UAjqadE0ESoUJghhgV8IxgK8EjPhJUS2I7gajd0dYoejKt%2B10DTvXRz34Vsw1tt1cuQy%2FASC7nStkbjssc9qD4n&X-Amz-Signature=779bb0d097153c124fbe053ff6fa560fb4ef2c342c0846ffc63f503e5205d27b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV27AUSR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIo46TWOJytc63RBc%2FMmTaecJ0BA3FnsEXNyaVeXNX0wIgYjR5dwZEmMoNPiYYXQQx3cyYHOgZIVAnspYaLUmgBhcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1VTxu8At6INmZG1SrcAyLzBpyYzHJNrRvSwa8hyWPCY2K4Pke8R8kTqoZEUsPKuuSKqzdtFKzd4bOcRSFAgGU0rEA3LIdRj9Z5VqT2mjtYFUApZ1jYqphgXKx49pnypysVxeqLnwlFkwtLcsC3vuJFVChJJYVrQzIABTK%2BOvCRpKzQjqHVlEiTKik3HCR6TrF56FSQzztVlojAZkkLMwCy8hHRp7CWbqtaf10rsP94RolBezZnrnEsgKUZpbvB7G9q6uRKDOtVQMLzm9iU5iXD0bQ4jeYDZckqeJBiHyPA%2FrMtJWl%2B45h5tNl5K7uXQMYqBH0qHT8y6t%2F%2BGRwk9OrL1pLGpvv4a3LK4knRwJf%2B8v0UbzGrBvWChUsiqs%2FpjJtqA28qyEd7gu%2FMRVUhDb6tVT7J2Y5cMZzqBg30NZhCWTUjJHaR5hMidsVPRdCgQG0ZyOekwz2qIYEj27CPu1dZSknszEYPWVHyCUnYefEqDvg9DXW%2F%2F5JVOOuDp2voYRxQr%2FJ5sLcUJ5tsGjwHdYWLv3nZolj6X%2BTfmN5HYcXQ6kfyTHaI3DzE0ruakA5Aw2iyTt%2BCD%2Bf5tYcJ1DbobHEvZB9a7qUCBlRdrkIb8EDjU2bV17XEHJNA6%2BQ%2BzdddhS6YYKl9RCCxmp8BMK628rwGOqUBQ5fHhSYrs2Nc1n8RcB8nrFnU%2Fv5CtXph7v1XVp18Y6EkpgtMDaG8DMjPWIfG2nBP0VXs2xoOYNX6JWxX5Go7KL%2B0%2FNIcY1vEklClkkUGTyS%2BKFxDump4D02GMhEbg8aoFHxoDtpAwuzmy9o8jzyLKaguxOhaA0Wk9Svk3%2Fee9DEF4J0Hr7FJHJHtFKKrekog1y5LRiWqyqdrvbkOy4H7eDrITS3%2B&X-Amz-Signature=8a086066dbc498be098ac7789fe89baa7dba27280766c45e206a31026795ed79&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV27AUSR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIo46TWOJytc63RBc%2FMmTaecJ0BA3FnsEXNyaVeXNX0wIgYjR5dwZEmMoNPiYYXQQx3cyYHOgZIVAnspYaLUmgBhcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1VTxu8At6INmZG1SrcAyLzBpyYzHJNrRvSwa8hyWPCY2K4Pke8R8kTqoZEUsPKuuSKqzdtFKzd4bOcRSFAgGU0rEA3LIdRj9Z5VqT2mjtYFUApZ1jYqphgXKx49pnypysVxeqLnwlFkwtLcsC3vuJFVChJJYVrQzIABTK%2BOvCRpKzQjqHVlEiTKik3HCR6TrF56FSQzztVlojAZkkLMwCy8hHRp7CWbqtaf10rsP94RolBezZnrnEsgKUZpbvB7G9q6uRKDOtVQMLzm9iU5iXD0bQ4jeYDZckqeJBiHyPA%2FrMtJWl%2B45h5tNl5K7uXQMYqBH0qHT8y6t%2F%2BGRwk9OrL1pLGpvv4a3LK4knRwJf%2B8v0UbzGrBvWChUsiqs%2FpjJtqA28qyEd7gu%2FMRVUhDb6tVT7J2Y5cMZzqBg30NZhCWTUjJHaR5hMidsVPRdCgQG0ZyOekwz2qIYEj27CPu1dZSknszEYPWVHyCUnYefEqDvg9DXW%2F%2F5JVOOuDp2voYRxQr%2FJ5sLcUJ5tsGjwHdYWLv3nZolj6X%2BTfmN5HYcXQ6kfyTHaI3DzE0ruakA5Aw2iyTt%2BCD%2Bf5tYcJ1DbobHEvZB9a7qUCBlRdrkIb8EDjU2bV17XEHJNA6%2BQ%2BzdddhS6YYKl9RCCxmp8BMK628rwGOqUBQ5fHhSYrs2Nc1n8RcB8nrFnU%2Fv5CtXph7v1XVp18Y6EkpgtMDaG8DMjPWIfG2nBP0VXs2xoOYNX6JWxX5Go7KL%2B0%2FNIcY1vEklClkkUGTyS%2BKFxDump4D02GMhEbg8aoFHxoDtpAwuzmy9o8jzyLKaguxOhaA0Wk9Svk3%2Fee9DEF4J0Hr7FJHJHtFKKrekog1y5LRiWqyqdrvbkOy4H7eDrITS3%2B&X-Amz-Signature=c4afdc0f072ca702f82938f0789483a2e59e9b950ce8d9f6b03f53615dbef2d6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV27AUSR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIo46TWOJytc63RBc%2FMmTaecJ0BA3FnsEXNyaVeXNX0wIgYjR5dwZEmMoNPiYYXQQx3cyYHOgZIVAnspYaLUmgBhcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1VTxu8At6INmZG1SrcAyLzBpyYzHJNrRvSwa8hyWPCY2K4Pke8R8kTqoZEUsPKuuSKqzdtFKzd4bOcRSFAgGU0rEA3LIdRj9Z5VqT2mjtYFUApZ1jYqphgXKx49pnypysVxeqLnwlFkwtLcsC3vuJFVChJJYVrQzIABTK%2BOvCRpKzQjqHVlEiTKik3HCR6TrF56FSQzztVlojAZkkLMwCy8hHRp7CWbqtaf10rsP94RolBezZnrnEsgKUZpbvB7G9q6uRKDOtVQMLzm9iU5iXD0bQ4jeYDZckqeJBiHyPA%2FrMtJWl%2B45h5tNl5K7uXQMYqBH0qHT8y6t%2F%2BGRwk9OrL1pLGpvv4a3LK4knRwJf%2B8v0UbzGrBvWChUsiqs%2FpjJtqA28qyEd7gu%2FMRVUhDb6tVT7J2Y5cMZzqBg30NZhCWTUjJHaR5hMidsVPRdCgQG0ZyOekwz2qIYEj27CPu1dZSknszEYPWVHyCUnYefEqDvg9DXW%2F%2F5JVOOuDp2voYRxQr%2FJ5sLcUJ5tsGjwHdYWLv3nZolj6X%2BTfmN5HYcXQ6kfyTHaI3DzE0ruakA5Aw2iyTt%2BCD%2Bf5tYcJ1DbobHEvZB9a7qUCBlRdrkIb8EDjU2bV17XEHJNA6%2BQ%2BzdddhS6YYKl9RCCxmp8BMK628rwGOqUBQ5fHhSYrs2Nc1n8RcB8nrFnU%2Fv5CtXph7v1XVp18Y6EkpgtMDaG8DMjPWIfG2nBP0VXs2xoOYNX6JWxX5Go7KL%2B0%2FNIcY1vEklClkkUGTyS%2BKFxDump4D02GMhEbg8aoFHxoDtpAwuzmy9o8jzyLKaguxOhaA0Wk9Svk3%2Fee9DEF4J0Hr7FJHJHtFKKrekog1y5LRiWqyqdrvbkOy4H7eDrITS3%2B&X-Amz-Signature=8589bb539912bbbc75443c22b323addfbc201a90edc138da13fb737b37298677&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV27AUSR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIo46TWOJytc63RBc%2FMmTaecJ0BA3FnsEXNyaVeXNX0wIgYjR5dwZEmMoNPiYYXQQx3cyYHOgZIVAnspYaLUmgBhcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1VTxu8At6INmZG1SrcAyLzBpyYzHJNrRvSwa8hyWPCY2K4Pke8R8kTqoZEUsPKuuSKqzdtFKzd4bOcRSFAgGU0rEA3LIdRj9Z5VqT2mjtYFUApZ1jYqphgXKx49pnypysVxeqLnwlFkwtLcsC3vuJFVChJJYVrQzIABTK%2BOvCRpKzQjqHVlEiTKik3HCR6TrF56FSQzztVlojAZkkLMwCy8hHRp7CWbqtaf10rsP94RolBezZnrnEsgKUZpbvB7G9q6uRKDOtVQMLzm9iU5iXD0bQ4jeYDZckqeJBiHyPA%2FrMtJWl%2B45h5tNl5K7uXQMYqBH0qHT8y6t%2F%2BGRwk9OrL1pLGpvv4a3LK4knRwJf%2B8v0UbzGrBvWChUsiqs%2FpjJtqA28qyEd7gu%2FMRVUhDb6tVT7J2Y5cMZzqBg30NZhCWTUjJHaR5hMidsVPRdCgQG0ZyOekwz2qIYEj27CPu1dZSknszEYPWVHyCUnYefEqDvg9DXW%2F%2F5JVOOuDp2voYRxQr%2FJ5sLcUJ5tsGjwHdYWLv3nZolj6X%2BTfmN5HYcXQ6kfyTHaI3DzE0ruakA5Aw2iyTt%2BCD%2Bf5tYcJ1DbobHEvZB9a7qUCBlRdrkIb8EDjU2bV17XEHJNA6%2BQ%2BzdddhS6YYKl9RCCxmp8BMK628rwGOqUBQ5fHhSYrs2Nc1n8RcB8nrFnU%2Fv5CtXph7v1XVp18Y6EkpgtMDaG8DMjPWIfG2nBP0VXs2xoOYNX6JWxX5Go7KL%2B0%2FNIcY1vEklClkkUGTyS%2BKFxDump4D02GMhEbg8aoFHxoDtpAwuzmy9o8jzyLKaguxOhaA0Wk9Svk3%2Fee9DEF4J0Hr7FJHJHtFKKrekog1y5LRiWqyqdrvbkOy4H7eDrITS3%2B&X-Amz-Signature=69f93edd80758c9775deae2b0993768997bf2a6780e8069788f2d12ed5f6072c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV27AUSR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIo46TWOJytc63RBc%2FMmTaecJ0BA3FnsEXNyaVeXNX0wIgYjR5dwZEmMoNPiYYXQQx3cyYHOgZIVAnspYaLUmgBhcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1VTxu8At6INmZG1SrcAyLzBpyYzHJNrRvSwa8hyWPCY2K4Pke8R8kTqoZEUsPKuuSKqzdtFKzd4bOcRSFAgGU0rEA3LIdRj9Z5VqT2mjtYFUApZ1jYqphgXKx49pnypysVxeqLnwlFkwtLcsC3vuJFVChJJYVrQzIABTK%2BOvCRpKzQjqHVlEiTKik3HCR6TrF56FSQzztVlojAZkkLMwCy8hHRp7CWbqtaf10rsP94RolBezZnrnEsgKUZpbvB7G9q6uRKDOtVQMLzm9iU5iXD0bQ4jeYDZckqeJBiHyPA%2FrMtJWl%2B45h5tNl5K7uXQMYqBH0qHT8y6t%2F%2BGRwk9OrL1pLGpvv4a3LK4knRwJf%2B8v0UbzGrBvWChUsiqs%2FpjJtqA28qyEd7gu%2FMRVUhDb6tVT7J2Y5cMZzqBg30NZhCWTUjJHaR5hMidsVPRdCgQG0ZyOekwz2qIYEj27CPu1dZSknszEYPWVHyCUnYefEqDvg9DXW%2F%2F5JVOOuDp2voYRxQr%2FJ5sLcUJ5tsGjwHdYWLv3nZolj6X%2BTfmN5HYcXQ6kfyTHaI3DzE0ruakA5Aw2iyTt%2BCD%2Bf5tYcJ1DbobHEvZB9a7qUCBlRdrkIb8EDjU2bV17XEHJNA6%2BQ%2BzdddhS6YYKl9RCCxmp8BMK628rwGOqUBQ5fHhSYrs2Nc1n8RcB8nrFnU%2Fv5CtXph7v1XVp18Y6EkpgtMDaG8DMjPWIfG2nBP0VXs2xoOYNX6JWxX5Go7KL%2B0%2FNIcY1vEklClkkUGTyS%2BKFxDump4D02GMhEbg8aoFHxoDtpAwuzmy9o8jzyLKaguxOhaA0Wk9Svk3%2Fee9DEF4J0Hr7FJHJHtFKKrekog1y5LRiWqyqdrvbkOy4H7eDrITS3%2B&X-Amz-Signature=4337d3e04a43e971ddaae3aaee923303e15ce5b4114d23270b62e9c5e892e9d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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


