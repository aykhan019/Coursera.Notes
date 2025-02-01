

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNWQWTMP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7svxBnCYjCowXdOkng9pJ7q%2BE%2F12kXotauUmvwa48QAiB75RURcAr9luGpAy%2Bhigz2lED%2FYXEWB0GzwfkRCm2g0yqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz2oa4TSRSykHsaTbKtwDAQe8940H3YojASt%2FjSAu%2BbEXwemAMFX4vpNEO%2BTRn8W18ENdMorfv4fWCkZRN9ftanqipxSp8TNL0JW4aTaTdNBMtoam9IdAjHB8wOOZJxsX%2BJ69yTfWHEgswQg9MtJTD%2F1RbOh%2BXHERCKtHQzEvZE1XzoqrQxQpteZEKnmF6Z%2BIEc6U4QhAjARW4cb%2FMBuZ5Zswqf2vCT4V8QMR1GSJQRk2waxqPlKf629Isc3SPMwscCHboZyl1Wp72WfK6RZx090OycNxQoXoB%2BZd6MRsyQboVyKVwszHWxPpSR%2B41cOrdS2bIGdbSPbOTGoNB8beD3iRwPfNDvRq3QsAXPc7Px5qOHHpadyRcRaH6KUyZcHQ6LTZ%2B6XGKJeeqg0cjJt%2B9hGGMqvsQEikDx0ash%2BYGnWnqDEU5wVhd0xb0EE81sPm6Ddj8ne%2FjA9R%2F7qXCbZQQHHiw7PfZ7Njw7K2C2xdykeHUjdo7HQ%2FxxSSzokdWWADMgqkK0YZ%2B5OIu8iV1uliDimdt6dVcCoQgrlKWVasnIux9R6%2BjQ%2FFXzLaaEWxaxy2zuofpVHIOnZFW8FeKzCQcQqoaaUgj6A5Mj732gMQfIQ3x7TnVglFZGvl%2BZqqn%2BJmorChonlyEOehUlEwoLH6vAY6pgE1TNABnDrW58v8VOxR%2BzhFQhhgTWtmVDKuPXpanvOkimrV10fPODm5zunIgnvZJAMwBT2qPuG2xRKyeY4gnzEVwouLSqI%2Bn5B6jYecbANrRTpav6V4xpKJXziqQ9IEsPVT%2B50XDhlRRh5gw%2BO0prZ%2BtjiJaury9JHnIQj0GaY68vi6%2Bz3UqfLpWdxlCke3c%2Bb6NKWWLFXvA4Wo3clLWqUcfylqXWsK&X-Amz-Signature=ef0ee26b867a047f0b055de03df7391a22114c4021a9648c7c5a618211771b41&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQXFOK6O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqDnGaWZvijmkzCUDSSrMzYICMaqrBclBJugqMGwI4bAiAQiM8cvvJSLBLW1myiaxKVs6aQrjBkNJgBHN6Pieqi9SqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaU33RyJOb%2Fvm%2FixDKtwD7LBvM0ESw2e8OPBtLisha%2BTveKusVVlLnM0iVdxzFJ0wbxHbHvLn%2FN1s9FMOiYaP1eTjmpYRbQ4m7gVVWvpARCz5Za0pQm1nSLgny0tqc%2BaHaCgJjwJOP0Rq36PxSQz%2F3i6mKRKEF3XnDbd001FDQDT1L0QHLF0vQfzuZdoAHP36RYGRQDhr3Jdhda66s2mGzjO6OujsDg1SbhrpGs8Jv3fiKZ%2FVav3AzUdsdSPfzj1YETJBslCGHtY21a%2FEysKj57L4FbOj5KsWARotPA8vDZRlLKGnz5PJF1zmCS95csVxFUjKMMKu2fsDneuiQiIicziym8jZ9hSOHX1DPVesc3NgDZWY%2FjY2xiynCmG0MhSwzUpiVIRMg66pB9yOe%2BiLARl%2BJ4ZVCeIsxrSLahcR0PHrwmQnEOccVlJHyS0cZKCllW8IdqyPzABg1UWJ6bSHe0rien69FooJtnx69kiyrzh%2B2s7pWVzp8TMLQT4uw3%2B3jAwzCU4DgiW51ru9pi2UMIDJE546wsTW4lAPQWdlgpv2wsW4LD36fFsIvvUqMFUWR2MXNgVwFAPdQi4o1JwWcOuVDeFdrqc1cJdlnt0se1xJMeqFgWb%2Bq7H0U5UsKEvlvY1ENNiiNrdYRnowyLH6vAY6pgFfGQDR%2BJf%2FQaQ3XCExBExj3aXJG8pkUrDkQDySfQCb%2B8ClOL6b6ji6OjOkEK%2B%2F93iuZFAgXlLrNSUimPrxj2XPGNoDYPp%2Fmg3F87tnOh14L4CG%2BoXVe6H73cVJq27SKLAgrAsuNrAAGKSpJPxdvNROjgs16o0kDZVQ7GDcWHzg6sHlR6euFTWZS9gcvT3OFGK4iRAK4eqkx1V2u7%2B9OVRy%2FUmRjpOB&X-Amz-Signature=d3b1ebd9311e18ccf88487edf977b6d36b5b84075de1fb69daa16dce86fa33af&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQXFOK6O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqDnGaWZvijmkzCUDSSrMzYICMaqrBclBJugqMGwI4bAiAQiM8cvvJSLBLW1myiaxKVs6aQrjBkNJgBHN6Pieqi9SqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaU33RyJOb%2Fvm%2FixDKtwD7LBvM0ESw2e8OPBtLisha%2BTveKusVVlLnM0iVdxzFJ0wbxHbHvLn%2FN1s9FMOiYaP1eTjmpYRbQ4m7gVVWvpARCz5Za0pQm1nSLgny0tqc%2BaHaCgJjwJOP0Rq36PxSQz%2F3i6mKRKEF3XnDbd001FDQDT1L0QHLF0vQfzuZdoAHP36RYGRQDhr3Jdhda66s2mGzjO6OujsDg1SbhrpGs8Jv3fiKZ%2FVav3AzUdsdSPfzj1YETJBslCGHtY21a%2FEysKj57L4FbOj5KsWARotPA8vDZRlLKGnz5PJF1zmCS95csVxFUjKMMKu2fsDneuiQiIicziym8jZ9hSOHX1DPVesc3NgDZWY%2FjY2xiynCmG0MhSwzUpiVIRMg66pB9yOe%2BiLARl%2BJ4ZVCeIsxrSLahcR0PHrwmQnEOccVlJHyS0cZKCllW8IdqyPzABg1UWJ6bSHe0rien69FooJtnx69kiyrzh%2B2s7pWVzp8TMLQT4uw3%2B3jAwzCU4DgiW51ru9pi2UMIDJE546wsTW4lAPQWdlgpv2wsW4LD36fFsIvvUqMFUWR2MXNgVwFAPdQi4o1JwWcOuVDeFdrqc1cJdlnt0se1xJMeqFgWb%2Bq7H0U5UsKEvlvY1ENNiiNrdYRnowyLH6vAY6pgFfGQDR%2BJf%2FQaQ3XCExBExj3aXJG8pkUrDkQDySfQCb%2B8ClOL6b6ji6OjOkEK%2B%2F93iuZFAgXlLrNSUimPrxj2XPGNoDYPp%2Fmg3F87tnOh14L4CG%2BoXVe6H73cVJq27SKLAgrAsuNrAAGKSpJPxdvNROjgs16o0kDZVQ7GDcWHzg6sHlR6euFTWZS9gcvT3OFGK4iRAK4eqkx1V2u7%2B9OVRy%2FUmRjpOB&X-Amz-Signature=6c924135a5e91f6e0cb71e86d53a7912c0798482b9db38c2de80c7e42f510c1c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQXFOK6O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqDnGaWZvijmkzCUDSSrMzYICMaqrBclBJugqMGwI4bAiAQiM8cvvJSLBLW1myiaxKVs6aQrjBkNJgBHN6Pieqi9SqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaU33RyJOb%2Fvm%2FixDKtwD7LBvM0ESw2e8OPBtLisha%2BTveKusVVlLnM0iVdxzFJ0wbxHbHvLn%2FN1s9FMOiYaP1eTjmpYRbQ4m7gVVWvpARCz5Za0pQm1nSLgny0tqc%2BaHaCgJjwJOP0Rq36PxSQz%2F3i6mKRKEF3XnDbd001FDQDT1L0QHLF0vQfzuZdoAHP36RYGRQDhr3Jdhda66s2mGzjO6OujsDg1SbhrpGs8Jv3fiKZ%2FVav3AzUdsdSPfzj1YETJBslCGHtY21a%2FEysKj57L4FbOj5KsWARotPA8vDZRlLKGnz5PJF1zmCS95csVxFUjKMMKu2fsDneuiQiIicziym8jZ9hSOHX1DPVesc3NgDZWY%2FjY2xiynCmG0MhSwzUpiVIRMg66pB9yOe%2BiLARl%2BJ4ZVCeIsxrSLahcR0PHrwmQnEOccVlJHyS0cZKCllW8IdqyPzABg1UWJ6bSHe0rien69FooJtnx69kiyrzh%2B2s7pWVzp8TMLQT4uw3%2B3jAwzCU4DgiW51ru9pi2UMIDJE546wsTW4lAPQWdlgpv2wsW4LD36fFsIvvUqMFUWR2MXNgVwFAPdQi4o1JwWcOuVDeFdrqc1cJdlnt0se1xJMeqFgWb%2Bq7H0U5UsKEvlvY1ENNiiNrdYRnowyLH6vAY6pgFfGQDR%2BJf%2FQaQ3XCExBExj3aXJG8pkUrDkQDySfQCb%2B8ClOL6b6ji6OjOkEK%2B%2F93iuZFAgXlLrNSUimPrxj2XPGNoDYPp%2Fmg3F87tnOh14L4CG%2BoXVe6H73cVJq27SKLAgrAsuNrAAGKSpJPxdvNROjgs16o0kDZVQ7GDcWHzg6sHlR6euFTWZS9gcvT3OFGK4iRAK4eqkx1V2u7%2B9OVRy%2FUmRjpOB&X-Amz-Signature=864a60dd7f64fba17d8a8eb0b5e1aa2ac62c7edb038f15da282be4849b22c30b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQXFOK6O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqDnGaWZvijmkzCUDSSrMzYICMaqrBclBJugqMGwI4bAiAQiM8cvvJSLBLW1myiaxKVs6aQrjBkNJgBHN6Pieqi9SqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaU33RyJOb%2Fvm%2FixDKtwD7LBvM0ESw2e8OPBtLisha%2BTveKusVVlLnM0iVdxzFJ0wbxHbHvLn%2FN1s9FMOiYaP1eTjmpYRbQ4m7gVVWvpARCz5Za0pQm1nSLgny0tqc%2BaHaCgJjwJOP0Rq36PxSQz%2F3i6mKRKEF3XnDbd001FDQDT1L0QHLF0vQfzuZdoAHP36RYGRQDhr3Jdhda66s2mGzjO6OujsDg1SbhrpGs8Jv3fiKZ%2FVav3AzUdsdSPfzj1YETJBslCGHtY21a%2FEysKj57L4FbOj5KsWARotPA8vDZRlLKGnz5PJF1zmCS95csVxFUjKMMKu2fsDneuiQiIicziym8jZ9hSOHX1DPVesc3NgDZWY%2FjY2xiynCmG0MhSwzUpiVIRMg66pB9yOe%2BiLARl%2BJ4ZVCeIsxrSLahcR0PHrwmQnEOccVlJHyS0cZKCllW8IdqyPzABg1UWJ6bSHe0rien69FooJtnx69kiyrzh%2B2s7pWVzp8TMLQT4uw3%2B3jAwzCU4DgiW51ru9pi2UMIDJE546wsTW4lAPQWdlgpv2wsW4LD36fFsIvvUqMFUWR2MXNgVwFAPdQi4o1JwWcOuVDeFdrqc1cJdlnt0se1xJMeqFgWb%2Bq7H0U5UsKEvlvY1ENNiiNrdYRnowyLH6vAY6pgFfGQDR%2BJf%2FQaQ3XCExBExj3aXJG8pkUrDkQDySfQCb%2B8ClOL6b6ji6OjOkEK%2B%2F93iuZFAgXlLrNSUimPrxj2XPGNoDYPp%2Fmg3F87tnOh14L4CG%2BoXVe6H73cVJq27SKLAgrAsuNrAAGKSpJPxdvNROjgs16o0kDZVQ7GDcWHzg6sHlR6euFTWZS9gcvT3OFGK4iRAK4eqkx1V2u7%2B9OVRy%2FUmRjpOB&X-Amz-Signature=4910f832de5093db16f9ecddeb395463988c1287b1b7197886de67e891e14685&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQXFOK6O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqDnGaWZvijmkzCUDSSrMzYICMaqrBclBJugqMGwI4bAiAQiM8cvvJSLBLW1myiaxKVs6aQrjBkNJgBHN6Pieqi9SqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaU33RyJOb%2Fvm%2FixDKtwD7LBvM0ESw2e8OPBtLisha%2BTveKusVVlLnM0iVdxzFJ0wbxHbHvLn%2FN1s9FMOiYaP1eTjmpYRbQ4m7gVVWvpARCz5Za0pQm1nSLgny0tqc%2BaHaCgJjwJOP0Rq36PxSQz%2F3i6mKRKEF3XnDbd001FDQDT1L0QHLF0vQfzuZdoAHP36RYGRQDhr3Jdhda66s2mGzjO6OujsDg1SbhrpGs8Jv3fiKZ%2FVav3AzUdsdSPfzj1YETJBslCGHtY21a%2FEysKj57L4FbOj5KsWARotPA8vDZRlLKGnz5PJF1zmCS95csVxFUjKMMKu2fsDneuiQiIicziym8jZ9hSOHX1DPVesc3NgDZWY%2FjY2xiynCmG0MhSwzUpiVIRMg66pB9yOe%2BiLARl%2BJ4ZVCeIsxrSLahcR0PHrwmQnEOccVlJHyS0cZKCllW8IdqyPzABg1UWJ6bSHe0rien69FooJtnx69kiyrzh%2B2s7pWVzp8TMLQT4uw3%2B3jAwzCU4DgiW51ru9pi2UMIDJE546wsTW4lAPQWdlgpv2wsW4LD36fFsIvvUqMFUWR2MXNgVwFAPdQi4o1JwWcOuVDeFdrqc1cJdlnt0se1xJMeqFgWb%2Bq7H0U5UsKEvlvY1ENNiiNrdYRnowyLH6vAY6pgFfGQDR%2BJf%2FQaQ3XCExBExj3aXJG8pkUrDkQDySfQCb%2B8ClOL6b6ji6OjOkEK%2B%2F93iuZFAgXlLrNSUimPrxj2XPGNoDYPp%2Fmg3F87tnOh14L4CG%2BoXVe6H73cVJq27SKLAgrAsuNrAAGKSpJPxdvNROjgs16o0kDZVQ7GDcWHzg6sHlR6euFTWZS9gcvT3OFGK4iRAK4eqkx1V2u7%2B9OVRy%2FUmRjpOB&X-Amz-Signature=b79fc54f164c373f5259709ff7ce4f1f745085c46bc3ab7d00130241a2c138ab&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNWQWTMP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7svxBnCYjCowXdOkng9pJ7q%2BE%2F12kXotauUmvwa48QAiB75RURcAr9luGpAy%2Bhigz2lED%2FYXEWB0GzwfkRCm2g0yqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz2oa4TSRSykHsaTbKtwDAQe8940H3YojASt%2FjSAu%2BbEXwemAMFX4vpNEO%2BTRn8W18ENdMorfv4fWCkZRN9ftanqipxSp8TNL0JW4aTaTdNBMtoam9IdAjHB8wOOZJxsX%2BJ69yTfWHEgswQg9MtJTD%2F1RbOh%2BXHERCKtHQzEvZE1XzoqrQxQpteZEKnmF6Z%2BIEc6U4QhAjARW4cb%2FMBuZ5Zswqf2vCT4V8QMR1GSJQRk2waxqPlKf629Isc3SPMwscCHboZyl1Wp72WfK6RZx090OycNxQoXoB%2BZd6MRsyQboVyKVwszHWxPpSR%2B41cOrdS2bIGdbSPbOTGoNB8beD3iRwPfNDvRq3QsAXPc7Px5qOHHpadyRcRaH6KUyZcHQ6LTZ%2B6XGKJeeqg0cjJt%2B9hGGMqvsQEikDx0ash%2BYGnWnqDEU5wVhd0xb0EE81sPm6Ddj8ne%2FjA9R%2F7qXCbZQQHHiw7PfZ7Njw7K2C2xdykeHUjdo7HQ%2FxxSSzokdWWADMgqkK0YZ%2B5OIu8iV1uliDimdt6dVcCoQgrlKWVasnIux9R6%2BjQ%2FFXzLaaEWxaxy2zuofpVHIOnZFW8FeKzCQcQqoaaUgj6A5Mj732gMQfIQ3x7TnVglFZGvl%2BZqqn%2BJmorChonlyEOehUlEwoLH6vAY6pgE1TNABnDrW58v8VOxR%2BzhFQhhgTWtmVDKuPXpanvOkimrV10fPODm5zunIgnvZJAMwBT2qPuG2xRKyeY4gnzEVwouLSqI%2Bn5B6jYecbANrRTpav6V4xpKJXziqQ9IEsPVT%2B50XDhlRRh5gw%2BO0prZ%2BtjiJaury9JHnIQj0GaY68vi6%2Bz3UqfLpWdxlCke3c%2Bb6NKWWLFXvA4Wo3clLWqUcfylqXWsK&X-Amz-Signature=03024dd013d3c83ae03855205a3328aab1ff769ea5491ce6b58f858d6276559b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNWQWTMP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7svxBnCYjCowXdOkng9pJ7q%2BE%2F12kXotauUmvwa48QAiB75RURcAr9luGpAy%2Bhigz2lED%2FYXEWB0GzwfkRCm2g0yqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz2oa4TSRSykHsaTbKtwDAQe8940H3YojASt%2FjSAu%2BbEXwemAMFX4vpNEO%2BTRn8W18ENdMorfv4fWCkZRN9ftanqipxSp8TNL0JW4aTaTdNBMtoam9IdAjHB8wOOZJxsX%2BJ69yTfWHEgswQg9MtJTD%2F1RbOh%2BXHERCKtHQzEvZE1XzoqrQxQpteZEKnmF6Z%2BIEc6U4QhAjARW4cb%2FMBuZ5Zswqf2vCT4V8QMR1GSJQRk2waxqPlKf629Isc3SPMwscCHboZyl1Wp72WfK6RZx090OycNxQoXoB%2BZd6MRsyQboVyKVwszHWxPpSR%2B41cOrdS2bIGdbSPbOTGoNB8beD3iRwPfNDvRq3QsAXPc7Px5qOHHpadyRcRaH6KUyZcHQ6LTZ%2B6XGKJeeqg0cjJt%2B9hGGMqvsQEikDx0ash%2BYGnWnqDEU5wVhd0xb0EE81sPm6Ddj8ne%2FjA9R%2F7qXCbZQQHHiw7PfZ7Njw7K2C2xdykeHUjdo7HQ%2FxxSSzokdWWADMgqkK0YZ%2B5OIu8iV1uliDimdt6dVcCoQgrlKWVasnIux9R6%2BjQ%2FFXzLaaEWxaxy2zuofpVHIOnZFW8FeKzCQcQqoaaUgj6A5Mj732gMQfIQ3x7TnVglFZGvl%2BZqqn%2BJmorChonlyEOehUlEwoLH6vAY6pgE1TNABnDrW58v8VOxR%2BzhFQhhgTWtmVDKuPXpanvOkimrV10fPODm5zunIgnvZJAMwBT2qPuG2xRKyeY4gnzEVwouLSqI%2Bn5B6jYecbANrRTpav6V4xpKJXziqQ9IEsPVT%2B50XDhlRRh5gw%2BO0prZ%2BtjiJaury9JHnIQj0GaY68vi6%2Bz3UqfLpWdxlCke3c%2Bb6NKWWLFXvA4Wo3clLWqUcfylqXWsK&X-Amz-Signature=d7dfde4b5cda5ea8ec2fe25cfa78e210fe980112dd0c73eb41f02adea1903acf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNWQWTMP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7svxBnCYjCowXdOkng9pJ7q%2BE%2F12kXotauUmvwa48QAiB75RURcAr9luGpAy%2Bhigz2lED%2FYXEWB0GzwfkRCm2g0yqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz2oa4TSRSykHsaTbKtwDAQe8940H3YojASt%2FjSAu%2BbEXwemAMFX4vpNEO%2BTRn8W18ENdMorfv4fWCkZRN9ftanqipxSp8TNL0JW4aTaTdNBMtoam9IdAjHB8wOOZJxsX%2BJ69yTfWHEgswQg9MtJTD%2F1RbOh%2BXHERCKtHQzEvZE1XzoqrQxQpteZEKnmF6Z%2BIEc6U4QhAjARW4cb%2FMBuZ5Zswqf2vCT4V8QMR1GSJQRk2waxqPlKf629Isc3SPMwscCHboZyl1Wp72WfK6RZx090OycNxQoXoB%2BZd6MRsyQboVyKVwszHWxPpSR%2B41cOrdS2bIGdbSPbOTGoNB8beD3iRwPfNDvRq3QsAXPc7Px5qOHHpadyRcRaH6KUyZcHQ6LTZ%2B6XGKJeeqg0cjJt%2B9hGGMqvsQEikDx0ash%2BYGnWnqDEU5wVhd0xb0EE81sPm6Ddj8ne%2FjA9R%2F7qXCbZQQHHiw7PfZ7Njw7K2C2xdykeHUjdo7HQ%2FxxSSzokdWWADMgqkK0YZ%2B5OIu8iV1uliDimdt6dVcCoQgrlKWVasnIux9R6%2BjQ%2FFXzLaaEWxaxy2zuofpVHIOnZFW8FeKzCQcQqoaaUgj6A5Mj732gMQfIQ3x7TnVglFZGvl%2BZqqn%2BJmorChonlyEOehUlEwoLH6vAY6pgE1TNABnDrW58v8VOxR%2BzhFQhhgTWtmVDKuPXpanvOkimrV10fPODm5zunIgnvZJAMwBT2qPuG2xRKyeY4gnzEVwouLSqI%2Bn5B6jYecbANrRTpav6V4xpKJXziqQ9IEsPVT%2B50XDhlRRh5gw%2BO0prZ%2BtjiJaury9JHnIQj0GaY68vi6%2Bz3UqfLpWdxlCke3c%2Bb6NKWWLFXvA4Wo3clLWqUcfylqXWsK&X-Amz-Signature=fd5996b98cd70cea8f0c0502db48e635a7c8abe27142a1fb7a717f617c57d4fc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNWQWTMP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7svxBnCYjCowXdOkng9pJ7q%2BE%2F12kXotauUmvwa48QAiB75RURcAr9luGpAy%2Bhigz2lED%2FYXEWB0GzwfkRCm2g0yqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz2oa4TSRSykHsaTbKtwDAQe8940H3YojASt%2FjSAu%2BbEXwemAMFX4vpNEO%2BTRn8W18ENdMorfv4fWCkZRN9ftanqipxSp8TNL0JW4aTaTdNBMtoam9IdAjHB8wOOZJxsX%2BJ69yTfWHEgswQg9MtJTD%2F1RbOh%2BXHERCKtHQzEvZE1XzoqrQxQpteZEKnmF6Z%2BIEc6U4QhAjARW4cb%2FMBuZ5Zswqf2vCT4V8QMR1GSJQRk2waxqPlKf629Isc3SPMwscCHboZyl1Wp72WfK6RZx090OycNxQoXoB%2BZd6MRsyQboVyKVwszHWxPpSR%2B41cOrdS2bIGdbSPbOTGoNB8beD3iRwPfNDvRq3QsAXPc7Px5qOHHpadyRcRaH6KUyZcHQ6LTZ%2B6XGKJeeqg0cjJt%2B9hGGMqvsQEikDx0ash%2BYGnWnqDEU5wVhd0xb0EE81sPm6Ddj8ne%2FjA9R%2F7qXCbZQQHHiw7PfZ7Njw7K2C2xdykeHUjdo7HQ%2FxxSSzokdWWADMgqkK0YZ%2B5OIu8iV1uliDimdt6dVcCoQgrlKWVasnIux9R6%2BjQ%2FFXzLaaEWxaxy2zuofpVHIOnZFW8FeKzCQcQqoaaUgj6A5Mj732gMQfIQ3x7TnVglFZGvl%2BZqqn%2BJmorChonlyEOehUlEwoLH6vAY6pgE1TNABnDrW58v8VOxR%2BzhFQhhgTWtmVDKuPXpanvOkimrV10fPODm5zunIgnvZJAMwBT2qPuG2xRKyeY4gnzEVwouLSqI%2Bn5B6jYecbANrRTpav6V4xpKJXziqQ9IEsPVT%2B50XDhlRRh5gw%2BO0prZ%2BtjiJaury9JHnIQj0GaY68vi6%2Bz3UqfLpWdxlCke3c%2Bb6NKWWLFXvA4Wo3clLWqUcfylqXWsK&X-Amz-Signature=2a3955c16dfcf8ae1a34f379c23fb8029440aca39942a64f7940fece97c17154&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNWQWTMP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7svxBnCYjCowXdOkng9pJ7q%2BE%2F12kXotauUmvwa48QAiB75RURcAr9luGpAy%2Bhigz2lED%2FYXEWB0GzwfkRCm2g0yqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz2oa4TSRSykHsaTbKtwDAQe8940H3YojASt%2FjSAu%2BbEXwemAMFX4vpNEO%2BTRn8W18ENdMorfv4fWCkZRN9ftanqipxSp8TNL0JW4aTaTdNBMtoam9IdAjHB8wOOZJxsX%2BJ69yTfWHEgswQg9MtJTD%2F1RbOh%2BXHERCKtHQzEvZE1XzoqrQxQpteZEKnmF6Z%2BIEc6U4QhAjARW4cb%2FMBuZ5Zswqf2vCT4V8QMR1GSJQRk2waxqPlKf629Isc3SPMwscCHboZyl1Wp72WfK6RZx090OycNxQoXoB%2BZd6MRsyQboVyKVwszHWxPpSR%2B41cOrdS2bIGdbSPbOTGoNB8beD3iRwPfNDvRq3QsAXPc7Px5qOHHpadyRcRaH6KUyZcHQ6LTZ%2B6XGKJeeqg0cjJt%2B9hGGMqvsQEikDx0ash%2BYGnWnqDEU5wVhd0xb0EE81sPm6Ddj8ne%2FjA9R%2F7qXCbZQQHHiw7PfZ7Njw7K2C2xdykeHUjdo7HQ%2FxxSSzokdWWADMgqkK0YZ%2B5OIu8iV1uliDimdt6dVcCoQgrlKWVasnIux9R6%2BjQ%2FFXzLaaEWxaxy2zuofpVHIOnZFW8FeKzCQcQqoaaUgj6A5Mj732gMQfIQ3x7TnVglFZGvl%2BZqqn%2BJmorChonlyEOehUlEwoLH6vAY6pgE1TNABnDrW58v8VOxR%2BzhFQhhgTWtmVDKuPXpanvOkimrV10fPODm5zunIgnvZJAMwBT2qPuG2xRKyeY4gnzEVwouLSqI%2Bn5B6jYecbANrRTpav6V4xpKJXziqQ9IEsPVT%2B50XDhlRRh5gw%2BO0prZ%2BtjiJaury9JHnIQj0GaY68vi6%2Bz3UqfLpWdxlCke3c%2Bb6NKWWLFXvA4Wo3clLWqUcfylqXWsK&X-Amz-Signature=02d97f603a5dba89c1bfc6cdcefbed470aa1eecf68c517671e99b0d0f604e0ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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


