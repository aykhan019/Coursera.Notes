

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN3665IH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCYKF%2FlvMRc%2FOqBUnsqHPki7dM2uVKZIdmR4HC2HUN5BAIgR4%2B9HXmMIw0%2F85gjhnk8wdyftAFxZDwCqHftrFQSXSMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKC%2Bb9%2FxUpunN3L8jCrcAz3o0L3BMVK6cijcjWinax%2FWkBQ8AISStIXM0Lc9U0s4eLblxNXHFImUd3491eZCNqz3LP1wvnpDXIxSNW9mwqbpROht2UYV4Xs2Mo%2B8F8W15VRxFiPx6N3505AbN6%2BLis%2FfKbRLj2EiXLZxo6dMTCGZipfCKlPgRfD%2B8t4FZTv%2Bmq75OclPK1hrUKyurZ4F7WictS0LVS9nZnMS4MBK7asGVp2LRS0yG0C90VjaD4ZXnW505mwWY1aLZlgJH%2BftElGVu0NZQNfhhbHAb91ykaji0ab%2F2iWaVkMKB6DUZ5zUuABX3Ccy6bIT2myYiCTUerTH6RX8oealNypBks3P5ztILiyduF87Ah5%2F0DEgrWZ73S%2BpLVoCdQzSSLkK9%2F3BXNtufXr5PDLmHbSmQQc6zhN3DYOJ%2FXxZybcNz5TG7GOGDOBagscTEUDcBRsnDrb7TSxN3Jazz2kHpwZSukipsivQSg%2F9Z2OEyBiayi7%2BDoFDlei1UT52SqwQUp3FnD0kkZ%2FZfJYWMyRJwQSfjKI6frImegry8LaoTnee%2FjoI8lm2BOFsXJL6f8Jv%2FMpfLklUqQE9MZGdvSTb2tPccbPp68765AjGQWohiBxGaGzQ0CDH%2BYLLX0W%2FlzdSOBjHMOj7mL0GOqUBeer7sjdI5yQLzw3mIvHPTmbrbLNEtDm6vlg%2B5ueGwoZxh9ITun5Z%2BZJpU8hejUTAB%2BgwrghmEbiQtL5gnPfI3d07k4fPZ%2B9n7NAcgzcs6P0fHSSux%2FYSbRreN7YuLShR87FhIOSXT0l9eSoMQ7v4AfBpdufOIbdc6%2BQSsgbsKphlOss2LMQ2YsiDLK1kNwbVMefXFJnYC8r%2B2XrxU%2F5tSfISN2Mn&X-Amz-Signature=4f44f6a8e868e657489860c1146a932901481499f93b92758896fa8446070a86&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5XGBTVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCjdld7YvQIYuLLMpI7vC3ClGVNiDCW%2BZLXyb%2B0%2FkToDgIhALPJmmYKp3sCLZyN9AG8E5zKw6YG%2FvLVmaRjFh3s5Gr%2FKv8DCHoQABoMNjM3NDIzMTgzODA1Igzj%2BuYsM2lrZ2AQBW0q3AMYobazFE37xcLV1VNBNYV%2Bm4Xq0Zpip3PAgPdPRRPghlYywccsditDFvzhdHmSkHHer%2FwJidHBZg5kljwFkgjtVEMi4xAAjy6CC%2FruP5rW3XIf365W7%2Fn3vkymNCUu7GOcK3ZXyv89eWxxzLUxmp4yoP7ro%2FTNWxqexzGIuUyxtj5kqlVmh7XvI3o2%2B2tqcZoXYazgS37RUHvZVe0CdspBZBSGUYixi8xBDoKn6srQnsD9C786mzXRVR%2BJbab0XX1cC1q1iezR2ipzCU91xl1k0t9K9dZlN03NnQXsfPieJmtwIXQSbF9ld3DAMKIyELewJCjsQa3sgNMoHxJv5xFL2cXq5nrdffiQ6QkO6MY6%2FhnXMMwyWNu6pn9cpixdrALBJkfKmWTn3B1dfHw8ITcKqcGFvc9SYgf%2F0%2Bqmq2WrsEppKKNi98Wna7yn0twM5B9R84yRg9Wtj4sW5pG7jNmtNRqB4mVQ1d35ExoNgYK9UBGTj3pzbCUjV2ndlDZDAPGaCARyfss0QcNDhJ67hMC%2FDfhxOBdMnlPj8vzCwgwqThLwzsTosSuZUv32B%2Fk644yy7orG019lOaBNjzlq0hWp%2FYxBlVTnSrGtJoFUD%2BrpILbDc4fYtCvzXZGF6TDk%2B5i9BjqkAYN7b6UD7SnFBRKuTc5FzjFjkQnc%2FVTW%2F9R8iQJ6zfwgDYeaAazsp6FSuD6drOT4Xcl%2FHzBbNBLe3S3%2BvdNjMMAPSLrc1ALt2bHKzCroWhGqSygZMpJV%2BDDsbSN6quifeSYle1RRReh13WxzPwTdFdWkPrTXIQSgyBldqEaUkoPnOdIyUgZk97AQol1gDhPd0Ai8xBNXzGxA4tFsU9Rkc5BZh1Rf&X-Amz-Signature=4f7605e427cd39103dc50a486d559a6c535692cb1110570de3772ef9dd8bf842&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5XGBTVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCjdld7YvQIYuLLMpI7vC3ClGVNiDCW%2BZLXyb%2B0%2FkToDgIhALPJmmYKp3sCLZyN9AG8E5zKw6YG%2FvLVmaRjFh3s5Gr%2FKv8DCHoQABoMNjM3NDIzMTgzODA1Igzj%2BuYsM2lrZ2AQBW0q3AMYobazFE37xcLV1VNBNYV%2Bm4Xq0Zpip3PAgPdPRRPghlYywccsditDFvzhdHmSkHHer%2FwJidHBZg5kljwFkgjtVEMi4xAAjy6CC%2FruP5rW3XIf365W7%2Fn3vkymNCUu7GOcK3ZXyv89eWxxzLUxmp4yoP7ro%2FTNWxqexzGIuUyxtj5kqlVmh7XvI3o2%2B2tqcZoXYazgS37RUHvZVe0CdspBZBSGUYixi8xBDoKn6srQnsD9C786mzXRVR%2BJbab0XX1cC1q1iezR2ipzCU91xl1k0t9K9dZlN03NnQXsfPieJmtwIXQSbF9ld3DAMKIyELewJCjsQa3sgNMoHxJv5xFL2cXq5nrdffiQ6QkO6MY6%2FhnXMMwyWNu6pn9cpixdrALBJkfKmWTn3B1dfHw8ITcKqcGFvc9SYgf%2F0%2Bqmq2WrsEppKKNi98Wna7yn0twM5B9R84yRg9Wtj4sW5pG7jNmtNRqB4mVQ1d35ExoNgYK9UBGTj3pzbCUjV2ndlDZDAPGaCARyfss0QcNDhJ67hMC%2FDfhxOBdMnlPj8vzCwgwqThLwzsTosSuZUv32B%2Fk644yy7orG019lOaBNjzlq0hWp%2FYxBlVTnSrGtJoFUD%2BrpILbDc4fYtCvzXZGF6TDk%2B5i9BjqkAYN7b6UD7SnFBRKuTc5FzjFjkQnc%2FVTW%2F9R8iQJ6zfwgDYeaAazsp6FSuD6drOT4Xcl%2FHzBbNBLe3S3%2BvdNjMMAPSLrc1ALt2bHKzCroWhGqSygZMpJV%2BDDsbSN6quifeSYle1RRReh13WxzPwTdFdWkPrTXIQSgyBldqEaUkoPnOdIyUgZk97AQol1gDhPd0Ai8xBNXzGxA4tFsU9Rkc5BZh1Rf&X-Amz-Signature=c417567d09ef22a80d9775afff102b8ef0cc1b300a2c62014b0cb34399d6b71d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5XGBTVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCjdld7YvQIYuLLMpI7vC3ClGVNiDCW%2BZLXyb%2B0%2FkToDgIhALPJmmYKp3sCLZyN9AG8E5zKw6YG%2FvLVmaRjFh3s5Gr%2FKv8DCHoQABoMNjM3NDIzMTgzODA1Igzj%2BuYsM2lrZ2AQBW0q3AMYobazFE37xcLV1VNBNYV%2Bm4Xq0Zpip3PAgPdPRRPghlYywccsditDFvzhdHmSkHHer%2FwJidHBZg5kljwFkgjtVEMi4xAAjy6CC%2FruP5rW3XIf365W7%2Fn3vkymNCUu7GOcK3ZXyv89eWxxzLUxmp4yoP7ro%2FTNWxqexzGIuUyxtj5kqlVmh7XvI3o2%2B2tqcZoXYazgS37RUHvZVe0CdspBZBSGUYixi8xBDoKn6srQnsD9C786mzXRVR%2BJbab0XX1cC1q1iezR2ipzCU91xl1k0t9K9dZlN03NnQXsfPieJmtwIXQSbF9ld3DAMKIyELewJCjsQa3sgNMoHxJv5xFL2cXq5nrdffiQ6QkO6MY6%2FhnXMMwyWNu6pn9cpixdrALBJkfKmWTn3B1dfHw8ITcKqcGFvc9SYgf%2F0%2Bqmq2WrsEppKKNi98Wna7yn0twM5B9R84yRg9Wtj4sW5pG7jNmtNRqB4mVQ1d35ExoNgYK9UBGTj3pzbCUjV2ndlDZDAPGaCARyfss0QcNDhJ67hMC%2FDfhxOBdMnlPj8vzCwgwqThLwzsTosSuZUv32B%2Fk644yy7orG019lOaBNjzlq0hWp%2FYxBlVTnSrGtJoFUD%2BrpILbDc4fYtCvzXZGF6TDk%2B5i9BjqkAYN7b6UD7SnFBRKuTc5FzjFjkQnc%2FVTW%2F9R8iQJ6zfwgDYeaAazsp6FSuD6drOT4Xcl%2FHzBbNBLe3S3%2BvdNjMMAPSLrc1ALt2bHKzCroWhGqSygZMpJV%2BDDsbSN6quifeSYle1RRReh13WxzPwTdFdWkPrTXIQSgyBldqEaUkoPnOdIyUgZk97AQol1gDhPd0Ai8xBNXzGxA4tFsU9Rkc5BZh1Rf&X-Amz-Signature=592cd6bcc4f0176ca479a68de2a561a06bc17b79f17b469d02b184d8d73b4e4a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5XGBTVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCjdld7YvQIYuLLMpI7vC3ClGVNiDCW%2BZLXyb%2B0%2FkToDgIhALPJmmYKp3sCLZyN9AG8E5zKw6YG%2FvLVmaRjFh3s5Gr%2FKv8DCHoQABoMNjM3NDIzMTgzODA1Igzj%2BuYsM2lrZ2AQBW0q3AMYobazFE37xcLV1VNBNYV%2Bm4Xq0Zpip3PAgPdPRRPghlYywccsditDFvzhdHmSkHHer%2FwJidHBZg5kljwFkgjtVEMi4xAAjy6CC%2FruP5rW3XIf365W7%2Fn3vkymNCUu7GOcK3ZXyv89eWxxzLUxmp4yoP7ro%2FTNWxqexzGIuUyxtj5kqlVmh7XvI3o2%2B2tqcZoXYazgS37RUHvZVe0CdspBZBSGUYixi8xBDoKn6srQnsD9C786mzXRVR%2BJbab0XX1cC1q1iezR2ipzCU91xl1k0t9K9dZlN03NnQXsfPieJmtwIXQSbF9ld3DAMKIyELewJCjsQa3sgNMoHxJv5xFL2cXq5nrdffiQ6QkO6MY6%2FhnXMMwyWNu6pn9cpixdrALBJkfKmWTn3B1dfHw8ITcKqcGFvc9SYgf%2F0%2Bqmq2WrsEppKKNi98Wna7yn0twM5B9R84yRg9Wtj4sW5pG7jNmtNRqB4mVQ1d35ExoNgYK9UBGTj3pzbCUjV2ndlDZDAPGaCARyfss0QcNDhJ67hMC%2FDfhxOBdMnlPj8vzCwgwqThLwzsTosSuZUv32B%2Fk644yy7orG019lOaBNjzlq0hWp%2FYxBlVTnSrGtJoFUD%2BrpILbDc4fYtCvzXZGF6TDk%2B5i9BjqkAYN7b6UD7SnFBRKuTc5FzjFjkQnc%2FVTW%2F9R8iQJ6zfwgDYeaAazsp6FSuD6drOT4Xcl%2FHzBbNBLe3S3%2BvdNjMMAPSLrc1ALt2bHKzCroWhGqSygZMpJV%2BDDsbSN6quifeSYle1RRReh13WxzPwTdFdWkPrTXIQSgyBldqEaUkoPnOdIyUgZk97AQol1gDhPd0Ai8xBNXzGxA4tFsU9Rkc5BZh1Rf&X-Amz-Signature=2b17a17dbe54044f11f6b724be9ea11173a5b8a8b44105dd7899e045d22cbcf8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5XGBTVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCjdld7YvQIYuLLMpI7vC3ClGVNiDCW%2BZLXyb%2B0%2FkToDgIhALPJmmYKp3sCLZyN9AG8E5zKw6YG%2FvLVmaRjFh3s5Gr%2FKv8DCHoQABoMNjM3NDIzMTgzODA1Igzj%2BuYsM2lrZ2AQBW0q3AMYobazFE37xcLV1VNBNYV%2Bm4Xq0Zpip3PAgPdPRRPghlYywccsditDFvzhdHmSkHHer%2FwJidHBZg5kljwFkgjtVEMi4xAAjy6CC%2FruP5rW3XIf365W7%2Fn3vkymNCUu7GOcK3ZXyv89eWxxzLUxmp4yoP7ro%2FTNWxqexzGIuUyxtj5kqlVmh7XvI3o2%2B2tqcZoXYazgS37RUHvZVe0CdspBZBSGUYixi8xBDoKn6srQnsD9C786mzXRVR%2BJbab0XX1cC1q1iezR2ipzCU91xl1k0t9K9dZlN03NnQXsfPieJmtwIXQSbF9ld3DAMKIyELewJCjsQa3sgNMoHxJv5xFL2cXq5nrdffiQ6QkO6MY6%2FhnXMMwyWNu6pn9cpixdrALBJkfKmWTn3B1dfHw8ITcKqcGFvc9SYgf%2F0%2Bqmq2WrsEppKKNi98Wna7yn0twM5B9R84yRg9Wtj4sW5pG7jNmtNRqB4mVQ1d35ExoNgYK9UBGTj3pzbCUjV2ndlDZDAPGaCARyfss0QcNDhJ67hMC%2FDfhxOBdMnlPj8vzCwgwqThLwzsTosSuZUv32B%2Fk644yy7orG019lOaBNjzlq0hWp%2FYxBlVTnSrGtJoFUD%2BrpILbDc4fYtCvzXZGF6TDk%2B5i9BjqkAYN7b6UD7SnFBRKuTc5FzjFjkQnc%2FVTW%2F9R8iQJ6zfwgDYeaAazsp6FSuD6drOT4Xcl%2FHzBbNBLe3S3%2BvdNjMMAPSLrc1ALt2bHKzCroWhGqSygZMpJV%2BDDsbSN6quifeSYle1RRReh13WxzPwTdFdWkPrTXIQSgyBldqEaUkoPnOdIyUgZk97AQol1gDhPd0Ai8xBNXzGxA4tFsU9Rkc5BZh1Rf&X-Amz-Signature=8b158df646c8649ead5f7a7cbf8fcdcc9ad9df356b132c8df81b3e573ac615e0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN3665IH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCYKF%2FlvMRc%2FOqBUnsqHPki7dM2uVKZIdmR4HC2HUN5BAIgR4%2B9HXmMIw0%2F85gjhnk8wdyftAFxZDwCqHftrFQSXSMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKC%2Bb9%2FxUpunN3L8jCrcAz3o0L3BMVK6cijcjWinax%2FWkBQ8AISStIXM0Lc9U0s4eLblxNXHFImUd3491eZCNqz3LP1wvnpDXIxSNW9mwqbpROht2UYV4Xs2Mo%2B8F8W15VRxFiPx6N3505AbN6%2BLis%2FfKbRLj2EiXLZxo6dMTCGZipfCKlPgRfD%2B8t4FZTv%2Bmq75OclPK1hrUKyurZ4F7WictS0LVS9nZnMS4MBK7asGVp2LRS0yG0C90VjaD4ZXnW505mwWY1aLZlgJH%2BftElGVu0NZQNfhhbHAb91ykaji0ab%2F2iWaVkMKB6DUZ5zUuABX3Ccy6bIT2myYiCTUerTH6RX8oealNypBks3P5ztILiyduF87Ah5%2F0DEgrWZ73S%2BpLVoCdQzSSLkK9%2F3BXNtufXr5PDLmHbSmQQc6zhN3DYOJ%2FXxZybcNz5TG7GOGDOBagscTEUDcBRsnDrb7TSxN3Jazz2kHpwZSukipsivQSg%2F9Z2OEyBiayi7%2BDoFDlei1UT52SqwQUp3FnD0kkZ%2FZfJYWMyRJwQSfjKI6frImegry8LaoTnee%2FjoI8lm2BOFsXJL6f8Jv%2FMpfLklUqQE9MZGdvSTb2tPccbPp68765AjGQWohiBxGaGzQ0CDH%2BYLLX0W%2FlzdSOBjHMOj7mL0GOqUBeer7sjdI5yQLzw3mIvHPTmbrbLNEtDm6vlg%2B5ueGwoZxh9ITun5Z%2BZJpU8hejUTAB%2BgwrghmEbiQtL5gnPfI3d07k4fPZ%2B9n7NAcgzcs6P0fHSSux%2FYSbRreN7YuLShR87FhIOSXT0l9eSoMQ7v4AfBpdufOIbdc6%2BQSsgbsKphlOss2LMQ2YsiDLK1kNwbVMefXFJnYC8r%2B2XrxU%2F5tSfISN2Mn&X-Amz-Signature=bea1786896370a2ac09b13abbc661794f4cbb02d342ea5a3ca252ea1792ca5c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN3665IH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCYKF%2FlvMRc%2FOqBUnsqHPki7dM2uVKZIdmR4HC2HUN5BAIgR4%2B9HXmMIw0%2F85gjhnk8wdyftAFxZDwCqHftrFQSXSMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKC%2Bb9%2FxUpunN3L8jCrcAz3o0L3BMVK6cijcjWinax%2FWkBQ8AISStIXM0Lc9U0s4eLblxNXHFImUd3491eZCNqz3LP1wvnpDXIxSNW9mwqbpROht2UYV4Xs2Mo%2B8F8W15VRxFiPx6N3505AbN6%2BLis%2FfKbRLj2EiXLZxo6dMTCGZipfCKlPgRfD%2B8t4FZTv%2Bmq75OclPK1hrUKyurZ4F7WictS0LVS9nZnMS4MBK7asGVp2LRS0yG0C90VjaD4ZXnW505mwWY1aLZlgJH%2BftElGVu0NZQNfhhbHAb91ykaji0ab%2F2iWaVkMKB6DUZ5zUuABX3Ccy6bIT2myYiCTUerTH6RX8oealNypBks3P5ztILiyduF87Ah5%2F0DEgrWZ73S%2BpLVoCdQzSSLkK9%2F3BXNtufXr5PDLmHbSmQQc6zhN3DYOJ%2FXxZybcNz5TG7GOGDOBagscTEUDcBRsnDrb7TSxN3Jazz2kHpwZSukipsivQSg%2F9Z2OEyBiayi7%2BDoFDlei1UT52SqwQUp3FnD0kkZ%2FZfJYWMyRJwQSfjKI6frImegry8LaoTnee%2FjoI8lm2BOFsXJL6f8Jv%2FMpfLklUqQE9MZGdvSTb2tPccbPp68765AjGQWohiBxGaGzQ0CDH%2BYLLX0W%2FlzdSOBjHMOj7mL0GOqUBeer7sjdI5yQLzw3mIvHPTmbrbLNEtDm6vlg%2B5ueGwoZxh9ITun5Z%2BZJpU8hejUTAB%2BgwrghmEbiQtL5gnPfI3d07k4fPZ%2B9n7NAcgzcs6P0fHSSux%2FYSbRreN7YuLShR87FhIOSXT0l9eSoMQ7v4AfBpdufOIbdc6%2BQSsgbsKphlOss2LMQ2YsiDLK1kNwbVMefXFJnYC8r%2B2XrxU%2F5tSfISN2Mn&X-Amz-Signature=e0b1bf5249fe50a4c24bb363c907e509340c231272306db5dc7567da9dff15bf&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN3665IH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCYKF%2FlvMRc%2FOqBUnsqHPki7dM2uVKZIdmR4HC2HUN5BAIgR4%2B9HXmMIw0%2F85gjhnk8wdyftAFxZDwCqHftrFQSXSMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKC%2Bb9%2FxUpunN3L8jCrcAz3o0L3BMVK6cijcjWinax%2FWkBQ8AISStIXM0Lc9U0s4eLblxNXHFImUd3491eZCNqz3LP1wvnpDXIxSNW9mwqbpROht2UYV4Xs2Mo%2B8F8W15VRxFiPx6N3505AbN6%2BLis%2FfKbRLj2EiXLZxo6dMTCGZipfCKlPgRfD%2B8t4FZTv%2Bmq75OclPK1hrUKyurZ4F7WictS0LVS9nZnMS4MBK7asGVp2LRS0yG0C90VjaD4ZXnW505mwWY1aLZlgJH%2BftElGVu0NZQNfhhbHAb91ykaji0ab%2F2iWaVkMKB6DUZ5zUuABX3Ccy6bIT2myYiCTUerTH6RX8oealNypBks3P5ztILiyduF87Ah5%2F0DEgrWZ73S%2BpLVoCdQzSSLkK9%2F3BXNtufXr5PDLmHbSmQQc6zhN3DYOJ%2FXxZybcNz5TG7GOGDOBagscTEUDcBRsnDrb7TSxN3Jazz2kHpwZSukipsivQSg%2F9Z2OEyBiayi7%2BDoFDlei1UT52SqwQUp3FnD0kkZ%2FZfJYWMyRJwQSfjKI6frImegry8LaoTnee%2FjoI8lm2BOFsXJL6f8Jv%2FMpfLklUqQE9MZGdvSTb2tPccbPp68765AjGQWohiBxGaGzQ0CDH%2BYLLX0W%2FlzdSOBjHMOj7mL0GOqUBeer7sjdI5yQLzw3mIvHPTmbrbLNEtDm6vlg%2B5ueGwoZxh9ITun5Z%2BZJpU8hejUTAB%2BgwrghmEbiQtL5gnPfI3d07k4fPZ%2B9n7NAcgzcs6P0fHSSux%2FYSbRreN7YuLShR87FhIOSXT0l9eSoMQ7v4AfBpdufOIbdc6%2BQSsgbsKphlOss2LMQ2YsiDLK1kNwbVMefXFJnYC8r%2B2XrxU%2F5tSfISN2Mn&X-Amz-Signature=0223d021a475ed27a1566a8b647c78c80711f61b043128a24922ce4227641fb8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN3665IH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCYKF%2FlvMRc%2FOqBUnsqHPki7dM2uVKZIdmR4HC2HUN5BAIgR4%2B9HXmMIw0%2F85gjhnk8wdyftAFxZDwCqHftrFQSXSMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKC%2Bb9%2FxUpunN3L8jCrcAz3o0L3BMVK6cijcjWinax%2FWkBQ8AISStIXM0Lc9U0s4eLblxNXHFImUd3491eZCNqz3LP1wvnpDXIxSNW9mwqbpROht2UYV4Xs2Mo%2B8F8W15VRxFiPx6N3505AbN6%2BLis%2FfKbRLj2EiXLZxo6dMTCGZipfCKlPgRfD%2B8t4FZTv%2Bmq75OclPK1hrUKyurZ4F7WictS0LVS9nZnMS4MBK7asGVp2LRS0yG0C90VjaD4ZXnW505mwWY1aLZlgJH%2BftElGVu0NZQNfhhbHAb91ykaji0ab%2F2iWaVkMKB6DUZ5zUuABX3Ccy6bIT2myYiCTUerTH6RX8oealNypBks3P5ztILiyduF87Ah5%2F0DEgrWZ73S%2BpLVoCdQzSSLkK9%2F3BXNtufXr5PDLmHbSmQQc6zhN3DYOJ%2FXxZybcNz5TG7GOGDOBagscTEUDcBRsnDrb7TSxN3Jazz2kHpwZSukipsivQSg%2F9Z2OEyBiayi7%2BDoFDlei1UT52SqwQUp3FnD0kkZ%2FZfJYWMyRJwQSfjKI6frImegry8LaoTnee%2FjoI8lm2BOFsXJL6f8Jv%2FMpfLklUqQE9MZGdvSTb2tPccbPp68765AjGQWohiBxGaGzQ0CDH%2BYLLX0W%2FlzdSOBjHMOj7mL0GOqUBeer7sjdI5yQLzw3mIvHPTmbrbLNEtDm6vlg%2B5ueGwoZxh9ITun5Z%2BZJpU8hejUTAB%2BgwrghmEbiQtL5gnPfI3d07k4fPZ%2B9n7NAcgzcs6P0fHSSux%2FYSbRreN7YuLShR87FhIOSXT0l9eSoMQ7v4AfBpdufOIbdc6%2BQSsgbsKphlOss2LMQ2YsiDLK1kNwbVMefXFJnYC8r%2B2XrxU%2F5tSfISN2Mn&X-Amz-Signature=6c26166899bf027cf2d45c5b1bc83bb88f12b17d6b74376bfbc68a2679901209&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN3665IH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCYKF%2FlvMRc%2FOqBUnsqHPki7dM2uVKZIdmR4HC2HUN5BAIgR4%2B9HXmMIw0%2F85gjhnk8wdyftAFxZDwCqHftrFQSXSMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKC%2Bb9%2FxUpunN3L8jCrcAz3o0L3BMVK6cijcjWinax%2FWkBQ8AISStIXM0Lc9U0s4eLblxNXHFImUd3491eZCNqz3LP1wvnpDXIxSNW9mwqbpROht2UYV4Xs2Mo%2B8F8W15VRxFiPx6N3505AbN6%2BLis%2FfKbRLj2EiXLZxo6dMTCGZipfCKlPgRfD%2B8t4FZTv%2Bmq75OclPK1hrUKyurZ4F7WictS0LVS9nZnMS4MBK7asGVp2LRS0yG0C90VjaD4ZXnW505mwWY1aLZlgJH%2BftElGVu0NZQNfhhbHAb91ykaji0ab%2F2iWaVkMKB6DUZ5zUuABX3Ccy6bIT2myYiCTUerTH6RX8oealNypBks3P5ztILiyduF87Ah5%2F0DEgrWZ73S%2BpLVoCdQzSSLkK9%2F3BXNtufXr5PDLmHbSmQQc6zhN3DYOJ%2FXxZybcNz5TG7GOGDOBagscTEUDcBRsnDrb7TSxN3Jazz2kHpwZSukipsivQSg%2F9Z2OEyBiayi7%2BDoFDlei1UT52SqwQUp3FnD0kkZ%2FZfJYWMyRJwQSfjKI6frImegry8LaoTnee%2FjoI8lm2BOFsXJL6f8Jv%2FMpfLklUqQE9MZGdvSTb2tPccbPp68765AjGQWohiBxGaGzQ0CDH%2BYLLX0W%2FlzdSOBjHMOj7mL0GOqUBeer7sjdI5yQLzw3mIvHPTmbrbLNEtDm6vlg%2B5ueGwoZxh9ITun5Z%2BZJpU8hejUTAB%2BgwrghmEbiQtL5gnPfI3d07k4fPZ%2B9n7NAcgzcs6P0fHSSux%2FYSbRreN7YuLShR87FhIOSXT0l9eSoMQ7v4AfBpdufOIbdc6%2BQSsgbsKphlOss2LMQ2YsiDLK1kNwbVMefXFJnYC8r%2B2XrxU%2F5tSfISN2Mn&X-Amz-Signature=0a616580257188118e2b43b20affd2859312869dc889570d1c70ae9893db675b&X-Amz-SignedHeaders=host&x-id=GetObject)
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


