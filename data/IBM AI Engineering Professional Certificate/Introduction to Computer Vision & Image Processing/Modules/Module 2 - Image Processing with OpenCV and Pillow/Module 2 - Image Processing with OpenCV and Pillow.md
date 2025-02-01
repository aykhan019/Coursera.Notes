

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDEQXXTC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVy45i4zVttcE7gFoDTZkUdQWgdgrAwowkFF%2Br71P7MgIhAIvI1IB87LqIimIa2uH%2FqpwfuHIf5FcMH8sH%2BS4FPATFKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFa79VS%2Bcr4ndyULwq3AOdVQFFK6V25PYjc4tGzlJ1UcXttgD5NYxziZT%2Fou92XO1%2F3fSEfLdEWeE%2F%2FcBwEuctpnf7Tc7K0%2F7Y00t4fgeni0a1hxAyjofRHMN4jdiQL2Y37I3%2BG0cD4ubDhynYkAaj6WArnSSxi0XlH%2BoxkCriZyq0vfPMGQaK37o1xx6l7f9Eh1NStBVsaKhRGYQO3l9F7xwPqYQPdHk1asalYDLkl%2BGCuTAVGzZkH5Fm0tKXekTsp5Of2hHAwfMP9wRPatLymLCRmppADAHQ1QoniZawiD0IbtjuN1U%2FaGrG%2BbjaaLuShw6egMEdBtxPfeulGiGGC02SQ3ODdzZXP767T4JMau7jG1iiZmXZEnPWhCf5UFlCuwXvC9bjBgv5rO%2Bwknzw3caphu5j4I9r%2BomH9dd2g5GGAr%2Flgk0T5iVB3xVqYlb3yeqp82xV39refvBw9KXljep2M8HgY2tLtUZIIjDyGFRGr%2Bv2Z4P%2FVhPYVzzOiucFF0jZgKk91snsY6P9flqKV%2BOavFFh8NH5tKkrOD9Q%2BvQVI0HG%2FU%2BPUdkJihTaXcMLfkAgb%2BEquORDv8DYTyDdIJYrD2bjBEG21f9lc%2B2Z8rkrMw%2BoUFWGxCrNUWZqWPEuTyXg3aoEhmrTBzDT3fa8BjqkAd4BcaehWJtBzlHxbwBUzWyCMYXVb2FbKC%2FbBts%2FAhbCDmJAMAZ9Hgop1IWckK%2BaYNFpQok6DYRb0n7a1Sm9DesMcAx4dKSEdhDHpU4YxmWsj0%2FMVBKl%2FdOUfVtB15RTRkfpmQzLSfnX%2FHu0ynM53qnSA075FPHXa3PA6RAsAbeE37199M%2FsNDKJ1rxVRd74crwY4Q6rBV4TedAhW4%2Fi9FZvD3nL&X-Amz-Signature=da81d3876cbbbeba7f8a6c570ed7a3e640274b57d95e235ac26ff0fb9a44fcfe&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWW7XDTH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuc2t1I1PD3guYRRfEBf%2FIE00gpV4ww%2BOKGgftQ7vhewIgGhBOWgWnaNdIv%2BTAUgF4mXFjVSB21a5XteQf1pIshqgqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDWrGGRzYRJMhh1VircA%2B%2FFPoKuI3Pp1JQ5AlNspCKpEksGQUe%2F1KFd51zLIjekXjlyG1pXFE1JbgSTyz%2BTdfcvLAQMkW52oA0zSj97lUt2QFqbKaHlMa%2By%2B75z9cWYy4zOgEpZDqc0f7gy9Dvdv4aI1cDgGD7bN05rwFY5%2B24TIlyWL%2BXZiNIqdRxBi3%2Bbrtlu6hTzudo%2FgcB2giOKg0Dt5VaisDOrlisQLcuQEg5X028yTU20ZEYPINKU3u2IkfD58jBWXhG8fSs6XFxBJHPK6JrsboMc%2FbTOsrFHOZLXjlfR01gAnQjg%2Fbpw7BtJk2zWyfoaZiWKWC1b3tIE6fnP9VUZ5sjvmcaHj2W9FKgjT%2BBkWMza8d7ofNv8yOx9zP7Rmpytu376sHyyyi40ye%2B7%2BO2V5gE03AnHfahoLmR2EKxbpMi24LfaNXrDKdW%2BOd2d7Dwm%2B3wQxo4UzRhhrrUPvrou3ko80QL%2FCs%2F31rHg0abkbRh43jl8LgUq9UlOWbo64fjA1Uf7PrJQ38yvkZ7zjs%2Ft5WKohkh5NVcmOZolBCSpc8opoBeEbMEI8iDtxKZtQoFO676nbINlQ6J4A4d7vkWz9s%2Faz9buEkLnCJjWqNC0cFmVvBcOxqBBajaYc4h0%2BUxjRqHgH5qsMLzd9rwGOqUBdxmSI7no2ff%2BnkZhOtftwMT37TyX8EF4YG6fy9NEId6%2Buq%2FS07jUSLPRKjtOUP3XRJv737Ix9YpJTX2oCE8lr%2FHsbRiAezIWHH2%2F1sW3ALRwjrbY3FEwxXe%2Fq3HasfM0WtWNdnoRGRGcALFbEZqZuGku%2FH033ZpnU8NfyAj2DLLPG6FPo4Vc4Pr0EThjvTqB6I5c%2FNFBrPsj2PjpvlYBv7N3rgrQ&X-Amz-Signature=1a0252f71091eb4d4d2cfd819a79c9e40d4908996895fef2a3a6fdcbe2c68ce7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWW7XDTH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuc2t1I1PD3guYRRfEBf%2FIE00gpV4ww%2BOKGgftQ7vhewIgGhBOWgWnaNdIv%2BTAUgF4mXFjVSB21a5XteQf1pIshqgqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDWrGGRzYRJMhh1VircA%2B%2FFPoKuI3Pp1JQ5AlNspCKpEksGQUe%2F1KFd51zLIjekXjlyG1pXFE1JbgSTyz%2BTdfcvLAQMkW52oA0zSj97lUt2QFqbKaHlMa%2By%2B75z9cWYy4zOgEpZDqc0f7gy9Dvdv4aI1cDgGD7bN05rwFY5%2B24TIlyWL%2BXZiNIqdRxBi3%2Bbrtlu6hTzudo%2FgcB2giOKg0Dt5VaisDOrlisQLcuQEg5X028yTU20ZEYPINKU3u2IkfD58jBWXhG8fSs6XFxBJHPK6JrsboMc%2FbTOsrFHOZLXjlfR01gAnQjg%2Fbpw7BtJk2zWyfoaZiWKWC1b3tIE6fnP9VUZ5sjvmcaHj2W9FKgjT%2BBkWMza8d7ofNv8yOx9zP7Rmpytu376sHyyyi40ye%2B7%2BO2V5gE03AnHfahoLmR2EKxbpMi24LfaNXrDKdW%2BOd2d7Dwm%2B3wQxo4UzRhhrrUPvrou3ko80QL%2FCs%2F31rHg0abkbRh43jl8LgUq9UlOWbo64fjA1Uf7PrJQ38yvkZ7zjs%2Ft5WKohkh5NVcmOZolBCSpc8opoBeEbMEI8iDtxKZtQoFO676nbINlQ6J4A4d7vkWz9s%2Faz9buEkLnCJjWqNC0cFmVvBcOxqBBajaYc4h0%2BUxjRqHgH5qsMLzd9rwGOqUBdxmSI7no2ff%2BnkZhOtftwMT37TyX8EF4YG6fy9NEId6%2Buq%2FS07jUSLPRKjtOUP3XRJv737Ix9YpJTX2oCE8lr%2FHsbRiAezIWHH2%2F1sW3ALRwjrbY3FEwxXe%2Fq3HasfM0WtWNdnoRGRGcALFbEZqZuGku%2FH033ZpnU8NfyAj2DLLPG6FPo4Vc4Pr0EThjvTqB6I5c%2FNFBrPsj2PjpvlYBv7N3rgrQ&X-Amz-Signature=8b23c92fec656a77e743e1f867c3ed86142d6ea0be11befb8f15641b29a527ad&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWW7XDTH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuc2t1I1PD3guYRRfEBf%2FIE00gpV4ww%2BOKGgftQ7vhewIgGhBOWgWnaNdIv%2BTAUgF4mXFjVSB21a5XteQf1pIshqgqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDWrGGRzYRJMhh1VircA%2B%2FFPoKuI3Pp1JQ5AlNspCKpEksGQUe%2F1KFd51zLIjekXjlyG1pXFE1JbgSTyz%2BTdfcvLAQMkW52oA0zSj97lUt2QFqbKaHlMa%2By%2B75z9cWYy4zOgEpZDqc0f7gy9Dvdv4aI1cDgGD7bN05rwFY5%2B24TIlyWL%2BXZiNIqdRxBi3%2Bbrtlu6hTzudo%2FgcB2giOKg0Dt5VaisDOrlisQLcuQEg5X028yTU20ZEYPINKU3u2IkfD58jBWXhG8fSs6XFxBJHPK6JrsboMc%2FbTOsrFHOZLXjlfR01gAnQjg%2Fbpw7BtJk2zWyfoaZiWKWC1b3tIE6fnP9VUZ5sjvmcaHj2W9FKgjT%2BBkWMza8d7ofNv8yOx9zP7Rmpytu376sHyyyi40ye%2B7%2BO2V5gE03AnHfahoLmR2EKxbpMi24LfaNXrDKdW%2BOd2d7Dwm%2B3wQxo4UzRhhrrUPvrou3ko80QL%2FCs%2F31rHg0abkbRh43jl8LgUq9UlOWbo64fjA1Uf7PrJQ38yvkZ7zjs%2Ft5WKohkh5NVcmOZolBCSpc8opoBeEbMEI8iDtxKZtQoFO676nbINlQ6J4A4d7vkWz9s%2Faz9buEkLnCJjWqNC0cFmVvBcOxqBBajaYc4h0%2BUxjRqHgH5qsMLzd9rwGOqUBdxmSI7no2ff%2BnkZhOtftwMT37TyX8EF4YG6fy9NEId6%2Buq%2FS07jUSLPRKjtOUP3XRJv737Ix9YpJTX2oCE8lr%2FHsbRiAezIWHH2%2F1sW3ALRwjrbY3FEwxXe%2Fq3HasfM0WtWNdnoRGRGcALFbEZqZuGku%2FH033ZpnU8NfyAj2DLLPG6FPo4Vc4Pr0EThjvTqB6I5c%2FNFBrPsj2PjpvlYBv7N3rgrQ&X-Amz-Signature=3bb98b68c2515cf431d906f93887fa14d6b8b661d4c49802cb7cef81c1c5339a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWW7XDTH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuc2t1I1PD3guYRRfEBf%2FIE00gpV4ww%2BOKGgftQ7vhewIgGhBOWgWnaNdIv%2BTAUgF4mXFjVSB21a5XteQf1pIshqgqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDWrGGRzYRJMhh1VircA%2B%2FFPoKuI3Pp1JQ5AlNspCKpEksGQUe%2F1KFd51zLIjekXjlyG1pXFE1JbgSTyz%2BTdfcvLAQMkW52oA0zSj97lUt2QFqbKaHlMa%2By%2B75z9cWYy4zOgEpZDqc0f7gy9Dvdv4aI1cDgGD7bN05rwFY5%2B24TIlyWL%2BXZiNIqdRxBi3%2Bbrtlu6hTzudo%2FgcB2giOKg0Dt5VaisDOrlisQLcuQEg5X028yTU20ZEYPINKU3u2IkfD58jBWXhG8fSs6XFxBJHPK6JrsboMc%2FbTOsrFHOZLXjlfR01gAnQjg%2Fbpw7BtJk2zWyfoaZiWKWC1b3tIE6fnP9VUZ5sjvmcaHj2W9FKgjT%2BBkWMza8d7ofNv8yOx9zP7Rmpytu376sHyyyi40ye%2B7%2BO2V5gE03AnHfahoLmR2EKxbpMi24LfaNXrDKdW%2BOd2d7Dwm%2B3wQxo4UzRhhrrUPvrou3ko80QL%2FCs%2F31rHg0abkbRh43jl8LgUq9UlOWbo64fjA1Uf7PrJQ38yvkZ7zjs%2Ft5WKohkh5NVcmOZolBCSpc8opoBeEbMEI8iDtxKZtQoFO676nbINlQ6J4A4d7vkWz9s%2Faz9buEkLnCJjWqNC0cFmVvBcOxqBBajaYc4h0%2BUxjRqHgH5qsMLzd9rwGOqUBdxmSI7no2ff%2BnkZhOtftwMT37TyX8EF4YG6fy9NEId6%2Buq%2FS07jUSLPRKjtOUP3XRJv737Ix9YpJTX2oCE8lr%2FHsbRiAezIWHH2%2F1sW3ALRwjrbY3FEwxXe%2Fq3HasfM0WtWNdnoRGRGcALFbEZqZuGku%2FH033ZpnU8NfyAj2DLLPG6FPo4Vc4Pr0EThjvTqB6I5c%2FNFBrPsj2PjpvlYBv7N3rgrQ&X-Amz-Signature=05f58472f73ad6f288fbea2fa11674be9637ce196b85f88f0ce5e9979d09995d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWW7XDTH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuc2t1I1PD3guYRRfEBf%2FIE00gpV4ww%2BOKGgftQ7vhewIgGhBOWgWnaNdIv%2BTAUgF4mXFjVSB21a5XteQf1pIshqgqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDWrGGRzYRJMhh1VircA%2B%2FFPoKuI3Pp1JQ5AlNspCKpEksGQUe%2F1KFd51zLIjekXjlyG1pXFE1JbgSTyz%2BTdfcvLAQMkW52oA0zSj97lUt2QFqbKaHlMa%2By%2B75z9cWYy4zOgEpZDqc0f7gy9Dvdv4aI1cDgGD7bN05rwFY5%2B24TIlyWL%2BXZiNIqdRxBi3%2Bbrtlu6hTzudo%2FgcB2giOKg0Dt5VaisDOrlisQLcuQEg5X028yTU20ZEYPINKU3u2IkfD58jBWXhG8fSs6XFxBJHPK6JrsboMc%2FbTOsrFHOZLXjlfR01gAnQjg%2Fbpw7BtJk2zWyfoaZiWKWC1b3tIE6fnP9VUZ5sjvmcaHj2W9FKgjT%2BBkWMza8d7ofNv8yOx9zP7Rmpytu376sHyyyi40ye%2B7%2BO2V5gE03AnHfahoLmR2EKxbpMi24LfaNXrDKdW%2BOd2d7Dwm%2B3wQxo4UzRhhrrUPvrou3ko80QL%2FCs%2F31rHg0abkbRh43jl8LgUq9UlOWbo64fjA1Uf7PrJQ38yvkZ7zjs%2Ft5WKohkh5NVcmOZolBCSpc8opoBeEbMEI8iDtxKZtQoFO676nbINlQ6J4A4d7vkWz9s%2Faz9buEkLnCJjWqNC0cFmVvBcOxqBBajaYc4h0%2BUxjRqHgH5qsMLzd9rwGOqUBdxmSI7no2ff%2BnkZhOtftwMT37TyX8EF4YG6fy9NEId6%2Buq%2FS07jUSLPRKjtOUP3XRJv737Ix9YpJTX2oCE8lr%2FHsbRiAezIWHH2%2F1sW3ALRwjrbY3FEwxXe%2Fq3HasfM0WtWNdnoRGRGcALFbEZqZuGku%2FH033ZpnU8NfyAj2DLLPG6FPo4Vc4Pr0EThjvTqB6I5c%2FNFBrPsj2PjpvlYBv7N3rgrQ&X-Amz-Signature=d4a587b026dfb3912fa8252a55e7b2782b3c064f30a988e489bae99f1e9ce034&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDEQXXTC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVy45i4zVttcE7gFoDTZkUdQWgdgrAwowkFF%2Br71P7MgIhAIvI1IB87LqIimIa2uH%2FqpwfuHIf5FcMH8sH%2BS4FPATFKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFa79VS%2Bcr4ndyULwq3AOdVQFFK6V25PYjc4tGzlJ1UcXttgD5NYxziZT%2Fou92XO1%2F3fSEfLdEWeE%2F%2FcBwEuctpnf7Tc7K0%2F7Y00t4fgeni0a1hxAyjofRHMN4jdiQL2Y37I3%2BG0cD4ubDhynYkAaj6WArnSSxi0XlH%2BoxkCriZyq0vfPMGQaK37o1xx6l7f9Eh1NStBVsaKhRGYQO3l9F7xwPqYQPdHk1asalYDLkl%2BGCuTAVGzZkH5Fm0tKXekTsp5Of2hHAwfMP9wRPatLymLCRmppADAHQ1QoniZawiD0IbtjuN1U%2FaGrG%2BbjaaLuShw6egMEdBtxPfeulGiGGC02SQ3ODdzZXP767T4JMau7jG1iiZmXZEnPWhCf5UFlCuwXvC9bjBgv5rO%2Bwknzw3caphu5j4I9r%2BomH9dd2g5GGAr%2Flgk0T5iVB3xVqYlb3yeqp82xV39refvBw9KXljep2M8HgY2tLtUZIIjDyGFRGr%2Bv2Z4P%2FVhPYVzzOiucFF0jZgKk91snsY6P9flqKV%2BOavFFh8NH5tKkrOD9Q%2BvQVI0HG%2FU%2BPUdkJihTaXcMLfkAgb%2BEquORDv8DYTyDdIJYrD2bjBEG21f9lc%2B2Z8rkrMw%2BoUFWGxCrNUWZqWPEuTyXg3aoEhmrTBzDT3fa8BjqkAd4BcaehWJtBzlHxbwBUzWyCMYXVb2FbKC%2FbBts%2FAhbCDmJAMAZ9Hgop1IWckK%2BaYNFpQok6DYRb0n7a1Sm9DesMcAx4dKSEdhDHpU4YxmWsj0%2FMVBKl%2FdOUfVtB15RTRkfpmQzLSfnX%2FHu0ynM53qnSA075FPHXa3PA6RAsAbeE37199M%2FsNDKJ1rxVRd74crwY4Q6rBV4TedAhW4%2Fi9FZvD3nL&X-Amz-Signature=900d5a19c45e12bb6e3df5e2a315e568358974fb5888bc4947ca9a7265203f59&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDEQXXTC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVy45i4zVttcE7gFoDTZkUdQWgdgrAwowkFF%2Br71P7MgIhAIvI1IB87LqIimIa2uH%2FqpwfuHIf5FcMH8sH%2BS4FPATFKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFa79VS%2Bcr4ndyULwq3AOdVQFFK6V25PYjc4tGzlJ1UcXttgD5NYxziZT%2Fou92XO1%2F3fSEfLdEWeE%2F%2FcBwEuctpnf7Tc7K0%2F7Y00t4fgeni0a1hxAyjofRHMN4jdiQL2Y37I3%2BG0cD4ubDhynYkAaj6WArnSSxi0XlH%2BoxkCriZyq0vfPMGQaK37o1xx6l7f9Eh1NStBVsaKhRGYQO3l9F7xwPqYQPdHk1asalYDLkl%2BGCuTAVGzZkH5Fm0tKXekTsp5Of2hHAwfMP9wRPatLymLCRmppADAHQ1QoniZawiD0IbtjuN1U%2FaGrG%2BbjaaLuShw6egMEdBtxPfeulGiGGC02SQ3ODdzZXP767T4JMau7jG1iiZmXZEnPWhCf5UFlCuwXvC9bjBgv5rO%2Bwknzw3caphu5j4I9r%2BomH9dd2g5GGAr%2Flgk0T5iVB3xVqYlb3yeqp82xV39refvBw9KXljep2M8HgY2tLtUZIIjDyGFRGr%2Bv2Z4P%2FVhPYVzzOiucFF0jZgKk91snsY6P9flqKV%2BOavFFh8NH5tKkrOD9Q%2BvQVI0HG%2FU%2BPUdkJihTaXcMLfkAgb%2BEquORDv8DYTyDdIJYrD2bjBEG21f9lc%2B2Z8rkrMw%2BoUFWGxCrNUWZqWPEuTyXg3aoEhmrTBzDT3fa8BjqkAd4BcaehWJtBzlHxbwBUzWyCMYXVb2FbKC%2FbBts%2FAhbCDmJAMAZ9Hgop1IWckK%2BaYNFpQok6DYRb0n7a1Sm9DesMcAx4dKSEdhDHpU4YxmWsj0%2FMVBKl%2FdOUfVtB15RTRkfpmQzLSfnX%2FHu0ynM53qnSA075FPHXa3PA6RAsAbeE37199M%2FsNDKJ1rxVRd74crwY4Q6rBV4TedAhW4%2Fi9FZvD3nL&X-Amz-Signature=512a79238b6606dd0a45322109f81adaf3af89ded74c1754ac06112b4da293ef&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDEQXXTC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVy45i4zVttcE7gFoDTZkUdQWgdgrAwowkFF%2Br71P7MgIhAIvI1IB87LqIimIa2uH%2FqpwfuHIf5FcMH8sH%2BS4FPATFKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFa79VS%2Bcr4ndyULwq3AOdVQFFK6V25PYjc4tGzlJ1UcXttgD5NYxziZT%2Fou92XO1%2F3fSEfLdEWeE%2F%2FcBwEuctpnf7Tc7K0%2F7Y00t4fgeni0a1hxAyjofRHMN4jdiQL2Y37I3%2BG0cD4ubDhynYkAaj6WArnSSxi0XlH%2BoxkCriZyq0vfPMGQaK37o1xx6l7f9Eh1NStBVsaKhRGYQO3l9F7xwPqYQPdHk1asalYDLkl%2BGCuTAVGzZkH5Fm0tKXekTsp5Of2hHAwfMP9wRPatLymLCRmppADAHQ1QoniZawiD0IbtjuN1U%2FaGrG%2BbjaaLuShw6egMEdBtxPfeulGiGGC02SQ3ODdzZXP767T4JMau7jG1iiZmXZEnPWhCf5UFlCuwXvC9bjBgv5rO%2Bwknzw3caphu5j4I9r%2BomH9dd2g5GGAr%2Flgk0T5iVB3xVqYlb3yeqp82xV39refvBw9KXljep2M8HgY2tLtUZIIjDyGFRGr%2Bv2Z4P%2FVhPYVzzOiucFF0jZgKk91snsY6P9flqKV%2BOavFFh8NH5tKkrOD9Q%2BvQVI0HG%2FU%2BPUdkJihTaXcMLfkAgb%2BEquORDv8DYTyDdIJYrD2bjBEG21f9lc%2B2Z8rkrMw%2BoUFWGxCrNUWZqWPEuTyXg3aoEhmrTBzDT3fa8BjqkAd4BcaehWJtBzlHxbwBUzWyCMYXVb2FbKC%2FbBts%2FAhbCDmJAMAZ9Hgop1IWckK%2BaYNFpQok6DYRb0n7a1Sm9DesMcAx4dKSEdhDHpU4YxmWsj0%2FMVBKl%2FdOUfVtB15RTRkfpmQzLSfnX%2FHu0ynM53qnSA075FPHXa3PA6RAsAbeE37199M%2FsNDKJ1rxVRd74crwY4Q6rBV4TedAhW4%2Fi9FZvD3nL&X-Amz-Signature=ebf40293dc7e4a95f0e26e0d0eba09b90c2c4848ae24ab2855e1e0523f7438eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDEQXXTC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVy45i4zVttcE7gFoDTZkUdQWgdgrAwowkFF%2Br71P7MgIhAIvI1IB87LqIimIa2uH%2FqpwfuHIf5FcMH8sH%2BS4FPATFKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFa79VS%2Bcr4ndyULwq3AOdVQFFK6V25PYjc4tGzlJ1UcXttgD5NYxziZT%2Fou92XO1%2F3fSEfLdEWeE%2F%2FcBwEuctpnf7Tc7K0%2F7Y00t4fgeni0a1hxAyjofRHMN4jdiQL2Y37I3%2BG0cD4ubDhynYkAaj6WArnSSxi0XlH%2BoxkCriZyq0vfPMGQaK37o1xx6l7f9Eh1NStBVsaKhRGYQO3l9F7xwPqYQPdHk1asalYDLkl%2BGCuTAVGzZkH5Fm0tKXekTsp5Of2hHAwfMP9wRPatLymLCRmppADAHQ1QoniZawiD0IbtjuN1U%2FaGrG%2BbjaaLuShw6egMEdBtxPfeulGiGGC02SQ3ODdzZXP767T4JMau7jG1iiZmXZEnPWhCf5UFlCuwXvC9bjBgv5rO%2Bwknzw3caphu5j4I9r%2BomH9dd2g5GGAr%2Flgk0T5iVB3xVqYlb3yeqp82xV39refvBw9KXljep2M8HgY2tLtUZIIjDyGFRGr%2Bv2Z4P%2FVhPYVzzOiucFF0jZgKk91snsY6P9flqKV%2BOavFFh8NH5tKkrOD9Q%2BvQVI0HG%2FU%2BPUdkJihTaXcMLfkAgb%2BEquORDv8DYTyDdIJYrD2bjBEG21f9lc%2B2Z8rkrMw%2BoUFWGxCrNUWZqWPEuTyXg3aoEhmrTBzDT3fa8BjqkAd4BcaehWJtBzlHxbwBUzWyCMYXVb2FbKC%2FbBts%2FAhbCDmJAMAZ9Hgop1IWckK%2BaYNFpQok6DYRb0n7a1Sm9DesMcAx4dKSEdhDHpU4YxmWsj0%2FMVBKl%2FdOUfVtB15RTRkfpmQzLSfnX%2FHu0ynM53qnSA075FPHXa3PA6RAsAbeE37199M%2FsNDKJ1rxVRd74crwY4Q6rBV4TedAhW4%2Fi9FZvD3nL&X-Amz-Signature=f1f4fcbaa5509163e2fe430faa98b603f0a4cbd6b54873ede64a6237eb589f22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDEQXXTC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVy45i4zVttcE7gFoDTZkUdQWgdgrAwowkFF%2Br71P7MgIhAIvI1IB87LqIimIa2uH%2FqpwfuHIf5FcMH8sH%2BS4FPATFKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFa79VS%2Bcr4ndyULwq3AOdVQFFK6V25PYjc4tGzlJ1UcXttgD5NYxziZT%2Fou92XO1%2F3fSEfLdEWeE%2F%2FcBwEuctpnf7Tc7K0%2F7Y00t4fgeni0a1hxAyjofRHMN4jdiQL2Y37I3%2BG0cD4ubDhynYkAaj6WArnSSxi0XlH%2BoxkCriZyq0vfPMGQaK37o1xx6l7f9Eh1NStBVsaKhRGYQO3l9F7xwPqYQPdHk1asalYDLkl%2BGCuTAVGzZkH5Fm0tKXekTsp5Of2hHAwfMP9wRPatLymLCRmppADAHQ1QoniZawiD0IbtjuN1U%2FaGrG%2BbjaaLuShw6egMEdBtxPfeulGiGGC02SQ3ODdzZXP767T4JMau7jG1iiZmXZEnPWhCf5UFlCuwXvC9bjBgv5rO%2Bwknzw3caphu5j4I9r%2BomH9dd2g5GGAr%2Flgk0T5iVB3xVqYlb3yeqp82xV39refvBw9KXljep2M8HgY2tLtUZIIjDyGFRGr%2Bv2Z4P%2FVhPYVzzOiucFF0jZgKk91snsY6P9flqKV%2BOavFFh8NH5tKkrOD9Q%2BvQVI0HG%2FU%2BPUdkJihTaXcMLfkAgb%2BEquORDv8DYTyDdIJYrD2bjBEG21f9lc%2B2Z8rkrMw%2BoUFWGxCrNUWZqWPEuTyXg3aoEhmrTBzDT3fa8BjqkAd4BcaehWJtBzlHxbwBUzWyCMYXVb2FbKC%2FbBts%2FAhbCDmJAMAZ9Hgop1IWckK%2BaYNFpQok6DYRb0n7a1Sm9DesMcAx4dKSEdhDHpU4YxmWsj0%2FMVBKl%2FdOUfVtB15RTRkfpmQzLSfnX%2FHu0ynM53qnSA075FPHXa3PA6RAsAbeE37199M%2FsNDKJ1rxVRd74crwY4Q6rBV4TedAhW4%2Fi9FZvD3nL&X-Amz-Signature=dbb0bafce8442a15cb67ab5eead54832eaa7d401304be2084c9bb41c7075af5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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


