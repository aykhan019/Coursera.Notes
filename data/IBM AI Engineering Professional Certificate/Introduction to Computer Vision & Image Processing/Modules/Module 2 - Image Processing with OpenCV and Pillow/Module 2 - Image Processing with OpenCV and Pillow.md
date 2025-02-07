

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR24JTSO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCxDQ3rosJzCYN6LfyueuK5IohqLlH5WAGNEAQujCC4vwIgcA6Nad85ohVyT1Ya7etDZZAV%2FSPVHObPGbR1LNSaa9cq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDAgdDmvTnIVvcM7ueSrcAywlIY4w0mlZT2bOMzlKFssOCkkeNxCuoEmiylwvy926At612dVGNhip7FAyyT%2FR9ELANk76RWgwBGxsd7mVSwnr2TU%2FBDZ43rtBuEGIJchGB%2FRmBOh3eL13Bxvn7JWcnzOb1rddoWtIcFYD%2BuA%2BvFqNVmev0hA4buhjLhHCd4jIfBdeLpfzlcvp2pPNl3pF34IwuY5Z%2BurDK6NHUbgkSERx%2Fb5kqBPK2JtdaGCuNNQeqThIDiqvKVXugUsKHykteG8yk%2F26hzH8ZaTNmV566X1E7%2FiAOVXnhaWMuoQjS1x4qYZ9fPPq0mzhGDkTnS7b02oowRStWNels9SADCLMf1iQcnx%2FZqPadlif%2Fd7ZgGEI9qDfdAvL0nkBGn%2BbJbiGREbi3p%2BEEZHZEILP14FnpS0woEGqJnu61df2WtdapC8AX%2FHp7M%2B1yUIxo%2B8JneVEWCUe8HgqR4jYQOi1qs%2Bv5PiKD7LCFSJzijgWwQ223qm20zu0%2By7dEH2ylEKDxFz3z8fgVPf2gMB%2Br1J0m7Q%2BH%2FsKBUwoaTPdWQZgGzR5zQA4Ecs7cCZB3Ffd33WTMz%2FXHIT%2FvZokKV3%2FqM4TnyzRo1b8jEUhWZoGn8c0Q4cEklQXlOBpu1hjz2ncA7I8MNWZmb0GOqUBQnnF5CBtCWb770byRtGULdQa8KQ8gpHV6DKEQ3D2IP7d1m1R6ZkM6KjtT79ae%2Bn7XGAdJiitIEud8eRb8uVb6IAaD4oHIck2E50p4pX%2Bnw2H509Cjgl3SHZFgdzv69%2Be%2BwrLlpr0SEWIOKYUvml0cwB8BfdPoLIxdfQWb2gZGgsTl3waj2G8txjBBpHNoWRzZTDS7hL3tG7gniHpYd9EK4Pnikhu&X-Amz-Signature=17f5615d0cf7123e1be025e50ce02c7cfdc2594cfbd82eb462f684eb9d8fad45&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT3ANH6J%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDjIGWrld0Jo1yZdZmiy9BOPHG7q0Bc7GfTW3eDvdeCWgIgCvaoA1Oe%2BmLMreU%2Fm2aYvSuAse%2B9rTrEVxOIjMKJqrMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDBgbFfpfntlZWX3BnyrcA%2BHY3pZDdlUfOnDcBKXRHsczL7yWGSCdHGAwFvBggXXrvolQEHKzrL2hyPtd748evS1pw7EBWNx059IhxdPUKgjXY5572qJ3zs%2BXSDYT2axE7w5GBCzQLiGzlgomPx9hs2VwJxD0HY%2BVvLr2cx%2B3JfO57kykRXqWIAv%2BET23SiocNWvSrOnk3RCVowZ0zcyIIhurbnu6EVU9Dc7Gt3RT7JSxRL%2BsXOXqdbo2iGqAYn4YcR89CvIFx2aHXpEWLxfdH%2BYAIuOSFdDFJpVAPnolX6A0JQsLpLuKpkFIF9wxaLPrlbBALL6iQCW1es2dn7JJRWafauaTxudFIjnffSAP7xcKZAkNb42vWhuJk1HyquczT%2B3siNvXdjKctBGJ4IYiYoOup2X%2F6cvcjhhegH0YR6y3xyN2MXarJJK1jpB6np8D0Clts%2FrZU%2B6IFiFvTx7lrNlOjzHVmYMpRyq5B15gzyvMLhGRlENKgF4AMmHRHshju3qq%2BSQxnPiGHnIquqvD7vJtnnEifA1%2FH6oJ7tniVbWsC7YKUvBNZ7tjJlkgIJWWQEqoRkDVZyYi8JYbi0NY5ZpB9Tlk%2FPAEyNtG6AdKs6xvhVpc%2FGDDK5dV1lj0nfd31%2FTZPCExOZNoDq6wMJiZmb0GOqUByZKiNj7ibwdc1Lw0NIPKbusPJgoVoW7%2FiMoRzOsF2tMK%2FQmbsuUqmhwTDJU6D1DCXZweN%2FswBwYSWaaLj1z5aqHTUdzU9G9EL2QLwCoIS3gSqOzdsn9QhSMgcTfvZUtiWCVH%2BuiahgoM%2BVOpFEJsZp8HMRf%2Bcpv0%2FshYQjUDKku8mDp3bo2JQym91QDeC6R%2BDximq15uOibFQ%2B6Pf6cmpNZnM3mD&X-Amz-Signature=9f5d28e98dcbc8fbfe85705d134d82f878f82a71758109381e551992bee59cc3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT3ANH6J%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDjIGWrld0Jo1yZdZmiy9BOPHG7q0Bc7GfTW3eDvdeCWgIgCvaoA1Oe%2BmLMreU%2Fm2aYvSuAse%2B9rTrEVxOIjMKJqrMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDBgbFfpfntlZWX3BnyrcA%2BHY3pZDdlUfOnDcBKXRHsczL7yWGSCdHGAwFvBggXXrvolQEHKzrL2hyPtd748evS1pw7EBWNx059IhxdPUKgjXY5572qJ3zs%2BXSDYT2axE7w5GBCzQLiGzlgomPx9hs2VwJxD0HY%2BVvLr2cx%2B3JfO57kykRXqWIAv%2BET23SiocNWvSrOnk3RCVowZ0zcyIIhurbnu6EVU9Dc7Gt3RT7JSxRL%2BsXOXqdbo2iGqAYn4YcR89CvIFx2aHXpEWLxfdH%2BYAIuOSFdDFJpVAPnolX6A0JQsLpLuKpkFIF9wxaLPrlbBALL6iQCW1es2dn7JJRWafauaTxudFIjnffSAP7xcKZAkNb42vWhuJk1HyquczT%2B3siNvXdjKctBGJ4IYiYoOup2X%2F6cvcjhhegH0YR6y3xyN2MXarJJK1jpB6np8D0Clts%2FrZU%2B6IFiFvTx7lrNlOjzHVmYMpRyq5B15gzyvMLhGRlENKgF4AMmHRHshju3qq%2BSQxnPiGHnIquqvD7vJtnnEifA1%2FH6oJ7tniVbWsC7YKUvBNZ7tjJlkgIJWWQEqoRkDVZyYi8JYbi0NY5ZpB9Tlk%2FPAEyNtG6AdKs6xvhVpc%2FGDDK5dV1lj0nfd31%2FTZPCExOZNoDq6wMJiZmb0GOqUByZKiNj7ibwdc1Lw0NIPKbusPJgoVoW7%2FiMoRzOsF2tMK%2FQmbsuUqmhwTDJU6D1DCXZweN%2FswBwYSWaaLj1z5aqHTUdzU9G9EL2QLwCoIS3gSqOzdsn9QhSMgcTfvZUtiWCVH%2BuiahgoM%2BVOpFEJsZp8HMRf%2Bcpv0%2FshYQjUDKku8mDp3bo2JQym91QDeC6R%2BDximq15uOibFQ%2B6Pf6cmpNZnM3mD&X-Amz-Signature=02e2a29c270f65378e9e1d027570adc70e6843254015988e7f885a9f0b5c27ff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT3ANH6J%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDjIGWrld0Jo1yZdZmiy9BOPHG7q0Bc7GfTW3eDvdeCWgIgCvaoA1Oe%2BmLMreU%2Fm2aYvSuAse%2B9rTrEVxOIjMKJqrMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDBgbFfpfntlZWX3BnyrcA%2BHY3pZDdlUfOnDcBKXRHsczL7yWGSCdHGAwFvBggXXrvolQEHKzrL2hyPtd748evS1pw7EBWNx059IhxdPUKgjXY5572qJ3zs%2BXSDYT2axE7w5GBCzQLiGzlgomPx9hs2VwJxD0HY%2BVvLr2cx%2B3JfO57kykRXqWIAv%2BET23SiocNWvSrOnk3RCVowZ0zcyIIhurbnu6EVU9Dc7Gt3RT7JSxRL%2BsXOXqdbo2iGqAYn4YcR89CvIFx2aHXpEWLxfdH%2BYAIuOSFdDFJpVAPnolX6A0JQsLpLuKpkFIF9wxaLPrlbBALL6iQCW1es2dn7JJRWafauaTxudFIjnffSAP7xcKZAkNb42vWhuJk1HyquczT%2B3siNvXdjKctBGJ4IYiYoOup2X%2F6cvcjhhegH0YR6y3xyN2MXarJJK1jpB6np8D0Clts%2FrZU%2B6IFiFvTx7lrNlOjzHVmYMpRyq5B15gzyvMLhGRlENKgF4AMmHRHshju3qq%2BSQxnPiGHnIquqvD7vJtnnEifA1%2FH6oJ7tniVbWsC7YKUvBNZ7tjJlkgIJWWQEqoRkDVZyYi8JYbi0NY5ZpB9Tlk%2FPAEyNtG6AdKs6xvhVpc%2FGDDK5dV1lj0nfd31%2FTZPCExOZNoDq6wMJiZmb0GOqUByZKiNj7ibwdc1Lw0NIPKbusPJgoVoW7%2FiMoRzOsF2tMK%2FQmbsuUqmhwTDJU6D1DCXZweN%2FswBwYSWaaLj1z5aqHTUdzU9G9EL2QLwCoIS3gSqOzdsn9QhSMgcTfvZUtiWCVH%2BuiahgoM%2BVOpFEJsZp8HMRf%2Bcpv0%2FshYQjUDKku8mDp3bo2JQym91QDeC6R%2BDximq15uOibFQ%2B6Pf6cmpNZnM3mD&X-Amz-Signature=8589b14a51e39a87ace6499e4831b914b6d7088f7393aac833ac21d8b4c057ef&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT3ANH6J%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDjIGWrld0Jo1yZdZmiy9BOPHG7q0Bc7GfTW3eDvdeCWgIgCvaoA1Oe%2BmLMreU%2Fm2aYvSuAse%2B9rTrEVxOIjMKJqrMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDBgbFfpfntlZWX3BnyrcA%2BHY3pZDdlUfOnDcBKXRHsczL7yWGSCdHGAwFvBggXXrvolQEHKzrL2hyPtd748evS1pw7EBWNx059IhxdPUKgjXY5572qJ3zs%2BXSDYT2axE7w5GBCzQLiGzlgomPx9hs2VwJxD0HY%2BVvLr2cx%2B3JfO57kykRXqWIAv%2BET23SiocNWvSrOnk3RCVowZ0zcyIIhurbnu6EVU9Dc7Gt3RT7JSxRL%2BsXOXqdbo2iGqAYn4YcR89CvIFx2aHXpEWLxfdH%2BYAIuOSFdDFJpVAPnolX6A0JQsLpLuKpkFIF9wxaLPrlbBALL6iQCW1es2dn7JJRWafauaTxudFIjnffSAP7xcKZAkNb42vWhuJk1HyquczT%2B3siNvXdjKctBGJ4IYiYoOup2X%2F6cvcjhhegH0YR6y3xyN2MXarJJK1jpB6np8D0Clts%2FrZU%2B6IFiFvTx7lrNlOjzHVmYMpRyq5B15gzyvMLhGRlENKgF4AMmHRHshju3qq%2BSQxnPiGHnIquqvD7vJtnnEifA1%2FH6oJ7tniVbWsC7YKUvBNZ7tjJlkgIJWWQEqoRkDVZyYi8JYbi0NY5ZpB9Tlk%2FPAEyNtG6AdKs6xvhVpc%2FGDDK5dV1lj0nfd31%2FTZPCExOZNoDq6wMJiZmb0GOqUByZKiNj7ibwdc1Lw0NIPKbusPJgoVoW7%2FiMoRzOsF2tMK%2FQmbsuUqmhwTDJU6D1DCXZweN%2FswBwYSWaaLj1z5aqHTUdzU9G9EL2QLwCoIS3gSqOzdsn9QhSMgcTfvZUtiWCVH%2BuiahgoM%2BVOpFEJsZp8HMRf%2Bcpv0%2FshYQjUDKku8mDp3bo2JQym91QDeC6R%2BDximq15uOibFQ%2B6Pf6cmpNZnM3mD&X-Amz-Signature=e62aa6b7296b237e20ed4a6735a4d3c7aff442aaf476e43e2f817b5a70e42919&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT3ANH6J%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDjIGWrld0Jo1yZdZmiy9BOPHG7q0Bc7GfTW3eDvdeCWgIgCvaoA1Oe%2BmLMreU%2Fm2aYvSuAse%2B9rTrEVxOIjMKJqrMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDBgbFfpfntlZWX3BnyrcA%2BHY3pZDdlUfOnDcBKXRHsczL7yWGSCdHGAwFvBggXXrvolQEHKzrL2hyPtd748evS1pw7EBWNx059IhxdPUKgjXY5572qJ3zs%2BXSDYT2axE7w5GBCzQLiGzlgomPx9hs2VwJxD0HY%2BVvLr2cx%2B3JfO57kykRXqWIAv%2BET23SiocNWvSrOnk3RCVowZ0zcyIIhurbnu6EVU9Dc7Gt3RT7JSxRL%2BsXOXqdbo2iGqAYn4YcR89CvIFx2aHXpEWLxfdH%2BYAIuOSFdDFJpVAPnolX6A0JQsLpLuKpkFIF9wxaLPrlbBALL6iQCW1es2dn7JJRWafauaTxudFIjnffSAP7xcKZAkNb42vWhuJk1HyquczT%2B3siNvXdjKctBGJ4IYiYoOup2X%2F6cvcjhhegH0YR6y3xyN2MXarJJK1jpB6np8D0Clts%2FrZU%2B6IFiFvTx7lrNlOjzHVmYMpRyq5B15gzyvMLhGRlENKgF4AMmHRHshju3qq%2BSQxnPiGHnIquqvD7vJtnnEifA1%2FH6oJ7tniVbWsC7YKUvBNZ7tjJlkgIJWWQEqoRkDVZyYi8JYbi0NY5ZpB9Tlk%2FPAEyNtG6AdKs6xvhVpc%2FGDDK5dV1lj0nfd31%2FTZPCExOZNoDq6wMJiZmb0GOqUByZKiNj7ibwdc1Lw0NIPKbusPJgoVoW7%2FiMoRzOsF2tMK%2FQmbsuUqmhwTDJU6D1DCXZweN%2FswBwYSWaaLj1z5aqHTUdzU9G9EL2QLwCoIS3gSqOzdsn9QhSMgcTfvZUtiWCVH%2BuiahgoM%2BVOpFEJsZp8HMRf%2Bcpv0%2FshYQjUDKku8mDp3bo2JQym91QDeC6R%2BDximq15uOibFQ%2B6Pf6cmpNZnM3mD&X-Amz-Signature=0ae9a256672f9600b6d8db5898d9536fbc41a933bce072da7a8b6a6840d575a5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR24JTSO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCxDQ3rosJzCYN6LfyueuK5IohqLlH5WAGNEAQujCC4vwIgcA6Nad85ohVyT1Ya7etDZZAV%2FSPVHObPGbR1LNSaa9cq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDAgdDmvTnIVvcM7ueSrcAywlIY4w0mlZT2bOMzlKFssOCkkeNxCuoEmiylwvy926At612dVGNhip7FAyyT%2FR9ELANk76RWgwBGxsd7mVSwnr2TU%2FBDZ43rtBuEGIJchGB%2FRmBOh3eL13Bxvn7JWcnzOb1rddoWtIcFYD%2BuA%2BvFqNVmev0hA4buhjLhHCd4jIfBdeLpfzlcvp2pPNl3pF34IwuY5Z%2BurDK6NHUbgkSERx%2Fb5kqBPK2JtdaGCuNNQeqThIDiqvKVXugUsKHykteG8yk%2F26hzH8ZaTNmV566X1E7%2FiAOVXnhaWMuoQjS1x4qYZ9fPPq0mzhGDkTnS7b02oowRStWNels9SADCLMf1iQcnx%2FZqPadlif%2Fd7ZgGEI9qDfdAvL0nkBGn%2BbJbiGREbi3p%2BEEZHZEILP14FnpS0woEGqJnu61df2WtdapC8AX%2FHp7M%2B1yUIxo%2B8JneVEWCUe8HgqR4jYQOi1qs%2Bv5PiKD7LCFSJzijgWwQ223qm20zu0%2By7dEH2ylEKDxFz3z8fgVPf2gMB%2Br1J0m7Q%2BH%2FsKBUwoaTPdWQZgGzR5zQA4Ecs7cCZB3Ffd33WTMz%2FXHIT%2FvZokKV3%2FqM4TnyzRo1b8jEUhWZoGn8c0Q4cEklQXlOBpu1hjz2ncA7I8MNWZmb0GOqUBQnnF5CBtCWb770byRtGULdQa8KQ8gpHV6DKEQ3D2IP7d1m1R6ZkM6KjtT79ae%2Bn7XGAdJiitIEud8eRb8uVb6IAaD4oHIck2E50p4pX%2Bnw2H509Cjgl3SHZFgdzv69%2Be%2BwrLlpr0SEWIOKYUvml0cwB8BfdPoLIxdfQWb2gZGgsTl3waj2G8txjBBpHNoWRzZTDS7hL3tG7gniHpYd9EK4Pnikhu&X-Amz-Signature=3424c4783866045b9a70191a7d8993cd734146ead5c0ae493e57cdfbe178b1ef&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR24JTSO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCxDQ3rosJzCYN6LfyueuK5IohqLlH5WAGNEAQujCC4vwIgcA6Nad85ohVyT1Ya7etDZZAV%2FSPVHObPGbR1LNSaa9cq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDAgdDmvTnIVvcM7ueSrcAywlIY4w0mlZT2bOMzlKFssOCkkeNxCuoEmiylwvy926At612dVGNhip7FAyyT%2FR9ELANk76RWgwBGxsd7mVSwnr2TU%2FBDZ43rtBuEGIJchGB%2FRmBOh3eL13Bxvn7JWcnzOb1rddoWtIcFYD%2BuA%2BvFqNVmev0hA4buhjLhHCd4jIfBdeLpfzlcvp2pPNl3pF34IwuY5Z%2BurDK6NHUbgkSERx%2Fb5kqBPK2JtdaGCuNNQeqThIDiqvKVXugUsKHykteG8yk%2F26hzH8ZaTNmV566X1E7%2FiAOVXnhaWMuoQjS1x4qYZ9fPPq0mzhGDkTnS7b02oowRStWNels9SADCLMf1iQcnx%2FZqPadlif%2Fd7ZgGEI9qDfdAvL0nkBGn%2BbJbiGREbi3p%2BEEZHZEILP14FnpS0woEGqJnu61df2WtdapC8AX%2FHp7M%2B1yUIxo%2B8JneVEWCUe8HgqR4jYQOi1qs%2Bv5PiKD7LCFSJzijgWwQ223qm20zu0%2By7dEH2ylEKDxFz3z8fgVPf2gMB%2Br1J0m7Q%2BH%2FsKBUwoaTPdWQZgGzR5zQA4Ecs7cCZB3Ffd33WTMz%2FXHIT%2FvZokKV3%2FqM4TnyzRo1b8jEUhWZoGn8c0Q4cEklQXlOBpu1hjz2ncA7I8MNWZmb0GOqUBQnnF5CBtCWb770byRtGULdQa8KQ8gpHV6DKEQ3D2IP7d1m1R6ZkM6KjtT79ae%2Bn7XGAdJiitIEud8eRb8uVb6IAaD4oHIck2E50p4pX%2Bnw2H509Cjgl3SHZFgdzv69%2Be%2BwrLlpr0SEWIOKYUvml0cwB8BfdPoLIxdfQWb2gZGgsTl3waj2G8txjBBpHNoWRzZTDS7hL3tG7gniHpYd9EK4Pnikhu&X-Amz-Signature=b05601caafdc6e225a533ba90cc1d05333bd083a8c5d321ff13c6c440dd52079&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR24JTSO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCxDQ3rosJzCYN6LfyueuK5IohqLlH5WAGNEAQujCC4vwIgcA6Nad85ohVyT1Ya7etDZZAV%2FSPVHObPGbR1LNSaa9cq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDAgdDmvTnIVvcM7ueSrcAywlIY4w0mlZT2bOMzlKFssOCkkeNxCuoEmiylwvy926At612dVGNhip7FAyyT%2FR9ELANk76RWgwBGxsd7mVSwnr2TU%2FBDZ43rtBuEGIJchGB%2FRmBOh3eL13Bxvn7JWcnzOb1rddoWtIcFYD%2BuA%2BvFqNVmev0hA4buhjLhHCd4jIfBdeLpfzlcvp2pPNl3pF34IwuY5Z%2BurDK6NHUbgkSERx%2Fb5kqBPK2JtdaGCuNNQeqThIDiqvKVXugUsKHykteG8yk%2F26hzH8ZaTNmV566X1E7%2FiAOVXnhaWMuoQjS1x4qYZ9fPPq0mzhGDkTnS7b02oowRStWNels9SADCLMf1iQcnx%2FZqPadlif%2Fd7ZgGEI9qDfdAvL0nkBGn%2BbJbiGREbi3p%2BEEZHZEILP14FnpS0woEGqJnu61df2WtdapC8AX%2FHp7M%2B1yUIxo%2B8JneVEWCUe8HgqR4jYQOi1qs%2Bv5PiKD7LCFSJzijgWwQ223qm20zu0%2By7dEH2ylEKDxFz3z8fgVPf2gMB%2Br1J0m7Q%2BH%2FsKBUwoaTPdWQZgGzR5zQA4Ecs7cCZB3Ffd33WTMz%2FXHIT%2FvZokKV3%2FqM4TnyzRo1b8jEUhWZoGn8c0Q4cEklQXlOBpu1hjz2ncA7I8MNWZmb0GOqUBQnnF5CBtCWb770byRtGULdQa8KQ8gpHV6DKEQ3D2IP7d1m1R6ZkM6KjtT79ae%2Bn7XGAdJiitIEud8eRb8uVb6IAaD4oHIck2E50p4pX%2Bnw2H509Cjgl3SHZFgdzv69%2Be%2BwrLlpr0SEWIOKYUvml0cwB8BfdPoLIxdfQWb2gZGgsTl3waj2G8txjBBpHNoWRzZTDS7hL3tG7gniHpYd9EK4Pnikhu&X-Amz-Signature=65d5e61dcf8363f3de0429d16e832b8e5679d0cfcc7dc5bfac54625be4002f08&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR24JTSO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCxDQ3rosJzCYN6LfyueuK5IohqLlH5WAGNEAQujCC4vwIgcA6Nad85ohVyT1Ya7etDZZAV%2FSPVHObPGbR1LNSaa9cq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDAgdDmvTnIVvcM7ueSrcAywlIY4w0mlZT2bOMzlKFssOCkkeNxCuoEmiylwvy926At612dVGNhip7FAyyT%2FR9ELANk76RWgwBGxsd7mVSwnr2TU%2FBDZ43rtBuEGIJchGB%2FRmBOh3eL13Bxvn7JWcnzOb1rddoWtIcFYD%2BuA%2BvFqNVmev0hA4buhjLhHCd4jIfBdeLpfzlcvp2pPNl3pF34IwuY5Z%2BurDK6NHUbgkSERx%2Fb5kqBPK2JtdaGCuNNQeqThIDiqvKVXugUsKHykteG8yk%2F26hzH8ZaTNmV566X1E7%2FiAOVXnhaWMuoQjS1x4qYZ9fPPq0mzhGDkTnS7b02oowRStWNels9SADCLMf1iQcnx%2FZqPadlif%2Fd7ZgGEI9qDfdAvL0nkBGn%2BbJbiGREbi3p%2BEEZHZEILP14FnpS0woEGqJnu61df2WtdapC8AX%2FHp7M%2B1yUIxo%2B8JneVEWCUe8HgqR4jYQOi1qs%2Bv5PiKD7LCFSJzijgWwQ223qm20zu0%2By7dEH2ylEKDxFz3z8fgVPf2gMB%2Br1J0m7Q%2BH%2FsKBUwoaTPdWQZgGzR5zQA4Ecs7cCZB3Ffd33WTMz%2FXHIT%2FvZokKV3%2FqM4TnyzRo1b8jEUhWZoGn8c0Q4cEklQXlOBpu1hjz2ncA7I8MNWZmb0GOqUBQnnF5CBtCWb770byRtGULdQa8KQ8gpHV6DKEQ3D2IP7d1m1R6ZkM6KjtT79ae%2Bn7XGAdJiitIEud8eRb8uVb6IAaD4oHIck2E50p4pX%2Bnw2H509Cjgl3SHZFgdzv69%2Be%2BwrLlpr0SEWIOKYUvml0cwB8BfdPoLIxdfQWb2gZGgsTl3waj2G8txjBBpHNoWRzZTDS7hL3tG7gniHpYd9EK4Pnikhu&X-Amz-Signature=b60ab5906fbcc5e5e9be98ca94960651c4a697846456df4bb01b28b07096ae36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR24JTSO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCxDQ3rosJzCYN6LfyueuK5IohqLlH5WAGNEAQujCC4vwIgcA6Nad85ohVyT1Ya7etDZZAV%2FSPVHObPGbR1LNSaa9cq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDAgdDmvTnIVvcM7ueSrcAywlIY4w0mlZT2bOMzlKFssOCkkeNxCuoEmiylwvy926At612dVGNhip7FAyyT%2FR9ELANk76RWgwBGxsd7mVSwnr2TU%2FBDZ43rtBuEGIJchGB%2FRmBOh3eL13Bxvn7JWcnzOb1rddoWtIcFYD%2BuA%2BvFqNVmev0hA4buhjLhHCd4jIfBdeLpfzlcvp2pPNl3pF34IwuY5Z%2BurDK6NHUbgkSERx%2Fb5kqBPK2JtdaGCuNNQeqThIDiqvKVXugUsKHykteG8yk%2F26hzH8ZaTNmV566X1E7%2FiAOVXnhaWMuoQjS1x4qYZ9fPPq0mzhGDkTnS7b02oowRStWNels9SADCLMf1iQcnx%2FZqPadlif%2Fd7ZgGEI9qDfdAvL0nkBGn%2BbJbiGREbi3p%2BEEZHZEILP14FnpS0woEGqJnu61df2WtdapC8AX%2FHp7M%2B1yUIxo%2B8JneVEWCUe8HgqR4jYQOi1qs%2Bv5PiKD7LCFSJzijgWwQ223qm20zu0%2By7dEH2ylEKDxFz3z8fgVPf2gMB%2Br1J0m7Q%2BH%2FsKBUwoaTPdWQZgGzR5zQA4Ecs7cCZB3Ffd33WTMz%2FXHIT%2FvZokKV3%2FqM4TnyzRo1b8jEUhWZoGn8c0Q4cEklQXlOBpu1hjz2ncA7I8MNWZmb0GOqUBQnnF5CBtCWb770byRtGULdQa8KQ8gpHV6DKEQ3D2IP7d1m1R6ZkM6KjtT79ae%2Bn7XGAdJiitIEud8eRb8uVb6IAaD4oHIck2E50p4pX%2Bnw2H509Cjgl3SHZFgdzv69%2Be%2BwrLlpr0SEWIOKYUvml0cwB8BfdPoLIxdfQWb2gZGgsTl3waj2G8txjBBpHNoWRzZTDS7hL3tG7gniHpYd9EK4Pnikhu&X-Amz-Signature=6c8378ecb1c5955857fcb8cd208ae08953995d054ea4873f81fdaa47280886d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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


