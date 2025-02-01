

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA4YA3B5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHqx4i5E0%2B9u0CSW7vPBDv4Lm8W3CDKREV5Qc3ZxiEnQIhANWxE4ypkxAvQqhTCQFitKEWT0nGmOi3tXILeKqhL%2BtvKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAcCtzKkv%2F9gDK%2F5sq3AP82MRDq%2B1uYRyoJ3KebaywzP5ROcJICki2th5zyie90A9Er4f0kTnL4Ry9yz44ZSKaDMqUVGdaNLW9ljoAPOmpVoeVmTDYF%2BAmzVwW6p8Ywf1ihBIGswK0eoxYuhtDmEzMQ5itP4NqhZJ4JK36eYNHe755cm2CEtaTneKPhjoYEQmRGnSKwRlAwbOt8huogw4FOO6sZ4Xvvn%2FgneE0JHODgtkfknzybe6s80DteT5Z6Cw6Lkxu%2B%2B8h282kjsQ%2BZGDFxiP9jRpdzYsVflyuNNjT%2BA11ZmPpRXtNQJwUOycFk0ghraSdv5efBWgpEOv6PlorWF%2BY9RQbiXfcCxbc8QGgJHvAKAr%2FQy%2FGqwFSgWkWc28OuXsIDr0zudJh4TqZyLwMMGnuSIfK5Rlt5xz2%2FNdORvvn%2FiZAHkHceFOPSUI0OLZ66sPjmV63zubTagrGRa3f2IeSVdsgKRmBLbaeHstSCYgc0DL0RHYB0H17sltTWGJx08UpMWIifreerOjXALduvQkRBn4OmpH2EIjXTu3zjNMLdYIuvApXK%2FxIVtde6HBp2BdNkJhpMp%2BHGuBOkqewymyDUcs48i6%2FGazHEw4zaZnu04a4MNDpwLY4QTW3VBaCwcXhVag81qJDrjDypfa8BjqkAaIpu5aCLT3wqZRNAYnUD8dlylY5UBDRwqKp89TrTVe439yEexnh7Fc3gsc28FwYtjMuxccrjO5yz5175686QPFqZBQqy8qZLInt3BESFLI%2FUgFF3VJ1VfMlx5xy%2FyA3Fglo%2B%2FTpA8BaNO9j18pSWTAedy%2FaxD4OkZle0aiyodmTX0jO9xtYlKfrwhfK8JQsZF3b0XW%2FUxDHRD3COj0aHZfMhPVQ&X-Amz-Signature=b7efc1345c8f37c85fae3cb9f656471c47ac2d3b0891900f9e6438ef94f090dc&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRZDOTRO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGR2O1XDI5oxITu%2BReUT2IpqtktT4wvI6dGSkrbAKGDhAiEAviATqO%2BrLVspQ3RKB9zQVM7EWE3hiLqKTbwZHlL0SxUqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNI5KQ1eeYJ1MDHRqSrcAw7gfdeEMN5B%2FBjPbVYDp31LD58jjfCYDrGKSiymATC%2FEjx8Ij4dY1ZDuioE0XDSxDYUKTzpt%2FwAtu%2FanrTRYbSiv1bvkTSK5GT%2FJzRuWzFTfZkUXpS78KSsDSvrfsrCifCkMBfj5CXJCvFpnld3uRhXsZdumuwJLBvoC6S%2FRrk914FBuf4eizY0iwUL9jlVs6BrZUgK%2FixhETvjFjXVg8sScLF7ngxhy51E6X9d9FD%2FYYiBqd2mknWv0KVrBt3xM5CTvvVI6Vmu82s1jix4eeVFQzuawUpS49Y5SZWmFsVZT6ZnKyY2oN%2BkFYRmlkty8fAGv24lDSnJvVGi8vEIChd7%2FdmuosAQRWYatx2%2F6GYhBMkWbEMv5LaONpq%2FPMgW1j21LJ8hSgmXVKfCcReRCBph%2F1GCvGV1pbu4hzArrOMV3ZVU7Vwvy%2F3V%2BUwqXKee9ENCvFhw50CbAio6QVc2j8j1Oe38EbZOSIr1fNBtCxCgzG3ZZs315bb%2BnzmRsIukpym%2BbZGzk1sGzOebDKcVnZSdqsrTubvZjn29ja%2FgX2ivd08zZh8LxYZ2ZtVoZITNT%2FR20Oz47unHl%2FvOk%2BpLGS5mw9d4CWbDGNen3y7sY9ZKQBYXovh3ZHYV6Lr2MIOm9rwGOqUBepLtU2sEpojWMKI%2FUD7ls%2FTEF%2F%2FgaSWHO33O7EWskmY%2FUTJF5cKMZ%2FjLLZ4SIfxyRBcAqeiFXVf9X5b5xohRTcmzp5dJleaY1LwlkK6boZAr6CchJFvedOzB97tsyig1TTRj5Ciii6XDs0uUq8jkRAe5njtM6SVsJh3EnXkb8lV0MyIkfNI3sV7FYn80wnjwX1Rt5Nid%2FKVJWqLqP8Y5hptxe8VF&X-Amz-Signature=89d0cb054ec2212f0742818de289fbec6f83bcd8d805603c70471f9ea18169d8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRZDOTRO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGR2O1XDI5oxITu%2BReUT2IpqtktT4wvI6dGSkrbAKGDhAiEAviATqO%2BrLVspQ3RKB9zQVM7EWE3hiLqKTbwZHlL0SxUqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNI5KQ1eeYJ1MDHRqSrcAw7gfdeEMN5B%2FBjPbVYDp31LD58jjfCYDrGKSiymATC%2FEjx8Ij4dY1ZDuioE0XDSxDYUKTzpt%2FwAtu%2FanrTRYbSiv1bvkTSK5GT%2FJzRuWzFTfZkUXpS78KSsDSvrfsrCifCkMBfj5CXJCvFpnld3uRhXsZdumuwJLBvoC6S%2FRrk914FBuf4eizY0iwUL9jlVs6BrZUgK%2FixhETvjFjXVg8sScLF7ngxhy51E6X9d9FD%2FYYiBqd2mknWv0KVrBt3xM5CTvvVI6Vmu82s1jix4eeVFQzuawUpS49Y5SZWmFsVZT6ZnKyY2oN%2BkFYRmlkty8fAGv24lDSnJvVGi8vEIChd7%2FdmuosAQRWYatx2%2F6GYhBMkWbEMv5LaONpq%2FPMgW1j21LJ8hSgmXVKfCcReRCBph%2F1GCvGV1pbu4hzArrOMV3ZVU7Vwvy%2F3V%2BUwqXKee9ENCvFhw50CbAio6QVc2j8j1Oe38EbZOSIr1fNBtCxCgzG3ZZs315bb%2BnzmRsIukpym%2BbZGzk1sGzOebDKcVnZSdqsrTubvZjn29ja%2FgX2ivd08zZh8LxYZ2ZtVoZITNT%2FR20Oz47unHl%2FvOk%2BpLGS5mw9d4CWbDGNen3y7sY9ZKQBYXovh3ZHYV6Lr2MIOm9rwGOqUBepLtU2sEpojWMKI%2FUD7ls%2FTEF%2F%2FgaSWHO33O7EWskmY%2FUTJF5cKMZ%2FjLLZ4SIfxyRBcAqeiFXVf9X5b5xohRTcmzp5dJleaY1LwlkK6boZAr6CchJFvedOzB97tsyig1TTRj5Ciii6XDs0uUq8jkRAe5njtM6SVsJh3EnXkb8lV0MyIkfNI3sV7FYn80wnjwX1Rt5Nid%2FKVJWqLqP8Y5hptxe8VF&X-Amz-Signature=613272dea0b39719a6387f5715eb8e075cf11fbf24f0cd5cdfbf5bb6088dab5e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRZDOTRO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGR2O1XDI5oxITu%2BReUT2IpqtktT4wvI6dGSkrbAKGDhAiEAviATqO%2BrLVspQ3RKB9zQVM7EWE3hiLqKTbwZHlL0SxUqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNI5KQ1eeYJ1MDHRqSrcAw7gfdeEMN5B%2FBjPbVYDp31LD58jjfCYDrGKSiymATC%2FEjx8Ij4dY1ZDuioE0XDSxDYUKTzpt%2FwAtu%2FanrTRYbSiv1bvkTSK5GT%2FJzRuWzFTfZkUXpS78KSsDSvrfsrCifCkMBfj5CXJCvFpnld3uRhXsZdumuwJLBvoC6S%2FRrk914FBuf4eizY0iwUL9jlVs6BrZUgK%2FixhETvjFjXVg8sScLF7ngxhy51E6X9d9FD%2FYYiBqd2mknWv0KVrBt3xM5CTvvVI6Vmu82s1jix4eeVFQzuawUpS49Y5SZWmFsVZT6ZnKyY2oN%2BkFYRmlkty8fAGv24lDSnJvVGi8vEIChd7%2FdmuosAQRWYatx2%2F6GYhBMkWbEMv5LaONpq%2FPMgW1j21LJ8hSgmXVKfCcReRCBph%2F1GCvGV1pbu4hzArrOMV3ZVU7Vwvy%2F3V%2BUwqXKee9ENCvFhw50CbAio6QVc2j8j1Oe38EbZOSIr1fNBtCxCgzG3ZZs315bb%2BnzmRsIukpym%2BbZGzk1sGzOebDKcVnZSdqsrTubvZjn29ja%2FgX2ivd08zZh8LxYZ2ZtVoZITNT%2FR20Oz47unHl%2FvOk%2BpLGS5mw9d4CWbDGNen3y7sY9ZKQBYXovh3ZHYV6Lr2MIOm9rwGOqUBepLtU2sEpojWMKI%2FUD7ls%2FTEF%2F%2FgaSWHO33O7EWskmY%2FUTJF5cKMZ%2FjLLZ4SIfxyRBcAqeiFXVf9X5b5xohRTcmzp5dJleaY1LwlkK6boZAr6CchJFvedOzB97tsyig1TTRj5Ciii6XDs0uUq8jkRAe5njtM6SVsJh3EnXkb8lV0MyIkfNI3sV7FYn80wnjwX1Rt5Nid%2FKVJWqLqP8Y5hptxe8VF&X-Amz-Signature=a9ee440405f1dd7c938bf6109f864413528bdccecf77c883d902696f68fc49ac&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRZDOTRO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGR2O1XDI5oxITu%2BReUT2IpqtktT4wvI6dGSkrbAKGDhAiEAviATqO%2BrLVspQ3RKB9zQVM7EWE3hiLqKTbwZHlL0SxUqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNI5KQ1eeYJ1MDHRqSrcAw7gfdeEMN5B%2FBjPbVYDp31LD58jjfCYDrGKSiymATC%2FEjx8Ij4dY1ZDuioE0XDSxDYUKTzpt%2FwAtu%2FanrTRYbSiv1bvkTSK5GT%2FJzRuWzFTfZkUXpS78KSsDSvrfsrCifCkMBfj5CXJCvFpnld3uRhXsZdumuwJLBvoC6S%2FRrk914FBuf4eizY0iwUL9jlVs6BrZUgK%2FixhETvjFjXVg8sScLF7ngxhy51E6X9d9FD%2FYYiBqd2mknWv0KVrBt3xM5CTvvVI6Vmu82s1jix4eeVFQzuawUpS49Y5SZWmFsVZT6ZnKyY2oN%2BkFYRmlkty8fAGv24lDSnJvVGi8vEIChd7%2FdmuosAQRWYatx2%2F6GYhBMkWbEMv5LaONpq%2FPMgW1j21LJ8hSgmXVKfCcReRCBph%2F1GCvGV1pbu4hzArrOMV3ZVU7Vwvy%2F3V%2BUwqXKee9ENCvFhw50CbAio6QVc2j8j1Oe38EbZOSIr1fNBtCxCgzG3ZZs315bb%2BnzmRsIukpym%2BbZGzk1sGzOebDKcVnZSdqsrTubvZjn29ja%2FgX2ivd08zZh8LxYZ2ZtVoZITNT%2FR20Oz47unHl%2FvOk%2BpLGS5mw9d4CWbDGNen3y7sY9ZKQBYXovh3ZHYV6Lr2MIOm9rwGOqUBepLtU2sEpojWMKI%2FUD7ls%2FTEF%2F%2FgaSWHO33O7EWskmY%2FUTJF5cKMZ%2FjLLZ4SIfxyRBcAqeiFXVf9X5b5xohRTcmzp5dJleaY1LwlkK6boZAr6CchJFvedOzB97tsyig1TTRj5Ciii6XDs0uUq8jkRAe5njtM6SVsJh3EnXkb8lV0MyIkfNI3sV7FYn80wnjwX1Rt5Nid%2FKVJWqLqP8Y5hptxe8VF&X-Amz-Signature=61bf6241f1ad884d9380b767e708859f8b7d9903e34aaff3c26c0c64f4f1e0b4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRZDOTRO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGR2O1XDI5oxITu%2BReUT2IpqtktT4wvI6dGSkrbAKGDhAiEAviATqO%2BrLVspQ3RKB9zQVM7EWE3hiLqKTbwZHlL0SxUqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNI5KQ1eeYJ1MDHRqSrcAw7gfdeEMN5B%2FBjPbVYDp31LD58jjfCYDrGKSiymATC%2FEjx8Ij4dY1ZDuioE0XDSxDYUKTzpt%2FwAtu%2FanrTRYbSiv1bvkTSK5GT%2FJzRuWzFTfZkUXpS78KSsDSvrfsrCifCkMBfj5CXJCvFpnld3uRhXsZdumuwJLBvoC6S%2FRrk914FBuf4eizY0iwUL9jlVs6BrZUgK%2FixhETvjFjXVg8sScLF7ngxhy51E6X9d9FD%2FYYiBqd2mknWv0KVrBt3xM5CTvvVI6Vmu82s1jix4eeVFQzuawUpS49Y5SZWmFsVZT6ZnKyY2oN%2BkFYRmlkty8fAGv24lDSnJvVGi8vEIChd7%2FdmuosAQRWYatx2%2F6GYhBMkWbEMv5LaONpq%2FPMgW1j21LJ8hSgmXVKfCcReRCBph%2F1GCvGV1pbu4hzArrOMV3ZVU7Vwvy%2F3V%2BUwqXKee9ENCvFhw50CbAio6QVc2j8j1Oe38EbZOSIr1fNBtCxCgzG3ZZs315bb%2BnzmRsIukpym%2BbZGzk1sGzOebDKcVnZSdqsrTubvZjn29ja%2FgX2ivd08zZh8LxYZ2ZtVoZITNT%2FR20Oz47unHl%2FvOk%2BpLGS5mw9d4CWbDGNen3y7sY9ZKQBYXovh3ZHYV6Lr2MIOm9rwGOqUBepLtU2sEpojWMKI%2FUD7ls%2FTEF%2F%2FgaSWHO33O7EWskmY%2FUTJF5cKMZ%2FjLLZ4SIfxyRBcAqeiFXVf9X5b5xohRTcmzp5dJleaY1LwlkK6boZAr6CchJFvedOzB97tsyig1TTRj5Ciii6XDs0uUq8jkRAe5njtM6SVsJh3EnXkb8lV0MyIkfNI3sV7FYn80wnjwX1Rt5Nid%2FKVJWqLqP8Y5hptxe8VF&X-Amz-Signature=ef9e3dc0f1746c31279f79de2132fae9d254da4862ef2ad7f47d8f0baa0d1a31&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA4YA3B5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHqx4i5E0%2B9u0CSW7vPBDv4Lm8W3CDKREV5Qc3ZxiEnQIhANWxE4ypkxAvQqhTCQFitKEWT0nGmOi3tXILeKqhL%2BtvKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAcCtzKkv%2F9gDK%2F5sq3AP82MRDq%2B1uYRyoJ3KebaywzP5ROcJICki2th5zyie90A9Er4f0kTnL4Ry9yz44ZSKaDMqUVGdaNLW9ljoAPOmpVoeVmTDYF%2BAmzVwW6p8Ywf1ihBIGswK0eoxYuhtDmEzMQ5itP4NqhZJ4JK36eYNHe755cm2CEtaTneKPhjoYEQmRGnSKwRlAwbOt8huogw4FOO6sZ4Xvvn%2FgneE0JHODgtkfknzybe6s80DteT5Z6Cw6Lkxu%2B%2B8h282kjsQ%2BZGDFxiP9jRpdzYsVflyuNNjT%2BA11ZmPpRXtNQJwUOycFk0ghraSdv5efBWgpEOv6PlorWF%2BY9RQbiXfcCxbc8QGgJHvAKAr%2FQy%2FGqwFSgWkWc28OuXsIDr0zudJh4TqZyLwMMGnuSIfK5Rlt5xz2%2FNdORvvn%2FiZAHkHceFOPSUI0OLZ66sPjmV63zubTagrGRa3f2IeSVdsgKRmBLbaeHstSCYgc0DL0RHYB0H17sltTWGJx08UpMWIifreerOjXALduvQkRBn4OmpH2EIjXTu3zjNMLdYIuvApXK%2FxIVtde6HBp2BdNkJhpMp%2BHGuBOkqewymyDUcs48i6%2FGazHEw4zaZnu04a4MNDpwLY4QTW3VBaCwcXhVag81qJDrjDypfa8BjqkAaIpu5aCLT3wqZRNAYnUD8dlylY5UBDRwqKp89TrTVe439yEexnh7Fc3gsc28FwYtjMuxccrjO5yz5175686QPFqZBQqy8qZLInt3BESFLI%2FUgFF3VJ1VfMlx5xy%2FyA3Fglo%2B%2FTpA8BaNO9j18pSWTAedy%2FaxD4OkZle0aiyodmTX0jO9xtYlKfrwhfK8JQsZF3b0XW%2FUxDHRD3COj0aHZfMhPVQ&X-Amz-Signature=6187813fba6c17a22f63387865b79d531503c3d62b5d946808e4ffe23e1e71ef&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA4YA3B5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHqx4i5E0%2B9u0CSW7vPBDv4Lm8W3CDKREV5Qc3ZxiEnQIhANWxE4ypkxAvQqhTCQFitKEWT0nGmOi3tXILeKqhL%2BtvKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAcCtzKkv%2F9gDK%2F5sq3AP82MRDq%2B1uYRyoJ3KebaywzP5ROcJICki2th5zyie90A9Er4f0kTnL4Ry9yz44ZSKaDMqUVGdaNLW9ljoAPOmpVoeVmTDYF%2BAmzVwW6p8Ywf1ihBIGswK0eoxYuhtDmEzMQ5itP4NqhZJ4JK36eYNHe755cm2CEtaTneKPhjoYEQmRGnSKwRlAwbOt8huogw4FOO6sZ4Xvvn%2FgneE0JHODgtkfknzybe6s80DteT5Z6Cw6Lkxu%2B%2B8h282kjsQ%2BZGDFxiP9jRpdzYsVflyuNNjT%2BA11ZmPpRXtNQJwUOycFk0ghraSdv5efBWgpEOv6PlorWF%2BY9RQbiXfcCxbc8QGgJHvAKAr%2FQy%2FGqwFSgWkWc28OuXsIDr0zudJh4TqZyLwMMGnuSIfK5Rlt5xz2%2FNdORvvn%2FiZAHkHceFOPSUI0OLZ66sPjmV63zubTagrGRa3f2IeSVdsgKRmBLbaeHstSCYgc0DL0RHYB0H17sltTWGJx08UpMWIifreerOjXALduvQkRBn4OmpH2EIjXTu3zjNMLdYIuvApXK%2FxIVtde6HBp2BdNkJhpMp%2BHGuBOkqewymyDUcs48i6%2FGazHEw4zaZnu04a4MNDpwLY4QTW3VBaCwcXhVag81qJDrjDypfa8BjqkAaIpu5aCLT3wqZRNAYnUD8dlylY5UBDRwqKp89TrTVe439yEexnh7Fc3gsc28FwYtjMuxccrjO5yz5175686QPFqZBQqy8qZLInt3BESFLI%2FUgFF3VJ1VfMlx5xy%2FyA3Fglo%2B%2FTpA8BaNO9j18pSWTAedy%2FaxD4OkZle0aiyodmTX0jO9xtYlKfrwhfK8JQsZF3b0XW%2FUxDHRD3COj0aHZfMhPVQ&X-Amz-Signature=84d7ff254c72b67f65506cdea4c119711140e0fb9076a08cce0e90d49b2e5989&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA4YA3B5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHqx4i5E0%2B9u0CSW7vPBDv4Lm8W3CDKREV5Qc3ZxiEnQIhANWxE4ypkxAvQqhTCQFitKEWT0nGmOi3tXILeKqhL%2BtvKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAcCtzKkv%2F9gDK%2F5sq3AP82MRDq%2B1uYRyoJ3KebaywzP5ROcJICki2th5zyie90A9Er4f0kTnL4Ry9yz44ZSKaDMqUVGdaNLW9ljoAPOmpVoeVmTDYF%2BAmzVwW6p8Ywf1ihBIGswK0eoxYuhtDmEzMQ5itP4NqhZJ4JK36eYNHe755cm2CEtaTneKPhjoYEQmRGnSKwRlAwbOt8huogw4FOO6sZ4Xvvn%2FgneE0JHODgtkfknzybe6s80DteT5Z6Cw6Lkxu%2B%2B8h282kjsQ%2BZGDFxiP9jRpdzYsVflyuNNjT%2BA11ZmPpRXtNQJwUOycFk0ghraSdv5efBWgpEOv6PlorWF%2BY9RQbiXfcCxbc8QGgJHvAKAr%2FQy%2FGqwFSgWkWc28OuXsIDr0zudJh4TqZyLwMMGnuSIfK5Rlt5xz2%2FNdORvvn%2FiZAHkHceFOPSUI0OLZ66sPjmV63zubTagrGRa3f2IeSVdsgKRmBLbaeHstSCYgc0DL0RHYB0H17sltTWGJx08UpMWIifreerOjXALduvQkRBn4OmpH2EIjXTu3zjNMLdYIuvApXK%2FxIVtde6HBp2BdNkJhpMp%2BHGuBOkqewymyDUcs48i6%2FGazHEw4zaZnu04a4MNDpwLY4QTW3VBaCwcXhVag81qJDrjDypfa8BjqkAaIpu5aCLT3wqZRNAYnUD8dlylY5UBDRwqKp89TrTVe439yEexnh7Fc3gsc28FwYtjMuxccrjO5yz5175686QPFqZBQqy8qZLInt3BESFLI%2FUgFF3VJ1VfMlx5xy%2FyA3Fglo%2B%2FTpA8BaNO9j18pSWTAedy%2FaxD4OkZle0aiyodmTX0jO9xtYlKfrwhfK8JQsZF3b0XW%2FUxDHRD3COj0aHZfMhPVQ&X-Amz-Signature=30b99fae6af0a4df257a1070298584f1e1ad56404fce53a218d6949ddf7b0fea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA4YA3B5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHqx4i5E0%2B9u0CSW7vPBDv4Lm8W3CDKREV5Qc3ZxiEnQIhANWxE4ypkxAvQqhTCQFitKEWT0nGmOi3tXILeKqhL%2BtvKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAcCtzKkv%2F9gDK%2F5sq3AP82MRDq%2B1uYRyoJ3KebaywzP5ROcJICki2th5zyie90A9Er4f0kTnL4Ry9yz44ZSKaDMqUVGdaNLW9ljoAPOmpVoeVmTDYF%2BAmzVwW6p8Ywf1ihBIGswK0eoxYuhtDmEzMQ5itP4NqhZJ4JK36eYNHe755cm2CEtaTneKPhjoYEQmRGnSKwRlAwbOt8huogw4FOO6sZ4Xvvn%2FgneE0JHODgtkfknzybe6s80DteT5Z6Cw6Lkxu%2B%2B8h282kjsQ%2BZGDFxiP9jRpdzYsVflyuNNjT%2BA11ZmPpRXtNQJwUOycFk0ghraSdv5efBWgpEOv6PlorWF%2BY9RQbiXfcCxbc8QGgJHvAKAr%2FQy%2FGqwFSgWkWc28OuXsIDr0zudJh4TqZyLwMMGnuSIfK5Rlt5xz2%2FNdORvvn%2FiZAHkHceFOPSUI0OLZ66sPjmV63zubTagrGRa3f2IeSVdsgKRmBLbaeHstSCYgc0DL0RHYB0H17sltTWGJx08UpMWIifreerOjXALduvQkRBn4OmpH2EIjXTu3zjNMLdYIuvApXK%2FxIVtde6HBp2BdNkJhpMp%2BHGuBOkqewymyDUcs48i6%2FGazHEw4zaZnu04a4MNDpwLY4QTW3VBaCwcXhVag81qJDrjDypfa8BjqkAaIpu5aCLT3wqZRNAYnUD8dlylY5UBDRwqKp89TrTVe439yEexnh7Fc3gsc28FwYtjMuxccrjO5yz5175686QPFqZBQqy8qZLInt3BESFLI%2FUgFF3VJ1VfMlx5xy%2FyA3Fglo%2B%2FTpA8BaNO9j18pSWTAedy%2FaxD4OkZle0aiyodmTX0jO9xtYlKfrwhfK8JQsZF3b0XW%2FUxDHRD3COj0aHZfMhPVQ&X-Amz-Signature=838efaa3bf3d5268464be0cc6a7a6bd55f05e21d57412d18cc098def03e3c9dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA4YA3B5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHqx4i5E0%2B9u0CSW7vPBDv4Lm8W3CDKREV5Qc3ZxiEnQIhANWxE4ypkxAvQqhTCQFitKEWT0nGmOi3tXILeKqhL%2BtvKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAcCtzKkv%2F9gDK%2F5sq3AP82MRDq%2B1uYRyoJ3KebaywzP5ROcJICki2th5zyie90A9Er4f0kTnL4Ry9yz44ZSKaDMqUVGdaNLW9ljoAPOmpVoeVmTDYF%2BAmzVwW6p8Ywf1ihBIGswK0eoxYuhtDmEzMQ5itP4NqhZJ4JK36eYNHe755cm2CEtaTneKPhjoYEQmRGnSKwRlAwbOt8huogw4FOO6sZ4Xvvn%2FgneE0JHODgtkfknzybe6s80DteT5Z6Cw6Lkxu%2B%2B8h282kjsQ%2BZGDFxiP9jRpdzYsVflyuNNjT%2BA11ZmPpRXtNQJwUOycFk0ghraSdv5efBWgpEOv6PlorWF%2BY9RQbiXfcCxbc8QGgJHvAKAr%2FQy%2FGqwFSgWkWc28OuXsIDr0zudJh4TqZyLwMMGnuSIfK5Rlt5xz2%2FNdORvvn%2FiZAHkHceFOPSUI0OLZ66sPjmV63zubTagrGRa3f2IeSVdsgKRmBLbaeHstSCYgc0DL0RHYB0H17sltTWGJx08UpMWIifreerOjXALduvQkRBn4OmpH2EIjXTu3zjNMLdYIuvApXK%2FxIVtde6HBp2BdNkJhpMp%2BHGuBOkqewymyDUcs48i6%2FGazHEw4zaZnu04a4MNDpwLY4QTW3VBaCwcXhVag81qJDrjDypfa8BjqkAaIpu5aCLT3wqZRNAYnUD8dlylY5UBDRwqKp89TrTVe439yEexnh7Fc3gsc28FwYtjMuxccrjO5yz5175686QPFqZBQqy8qZLInt3BESFLI%2FUgFF3VJ1VfMlx5xy%2FyA3Fglo%2B%2FTpA8BaNO9j18pSWTAedy%2FaxD4OkZle0aiyodmTX0jO9xtYlKfrwhfK8JQsZF3b0XW%2FUxDHRD3COj0aHZfMhPVQ&X-Amz-Signature=97564c72b9045c2f0bb3cfb220f70d9f2b775fc6d8cd47584ac30e89496b6c23&X-Amz-SignedHeaders=host&x-id=GetObject)
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


