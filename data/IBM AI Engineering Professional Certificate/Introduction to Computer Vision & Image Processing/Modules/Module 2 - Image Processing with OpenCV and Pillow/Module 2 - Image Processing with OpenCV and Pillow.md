

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMNE74N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBtgSp4u3jDRlw6A7zXAiqHT9P7rN7jn9QmlBvTHGdYzAiA316Qcbd5%2BFLGURdZZwbQs%2Be5QwnTbAw8t1OtriKMmsSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMVcfXej8y8ZrEHsXCKtwDCkMImy8EhFuXgdoIGzLb0orTDgOgt6zQlNy3HXa0x2UKmLRwzsTfVxIHRH%2Fk52yl%2Fo2dSrHllZEb124PF%2FnRxkc%2Fct%2BeiMoJEZJVv5wDn8yo5SQ%2FAu3itSEKb24Oa0KlfUA%2F0s0uALxYLb%2FQynQ%2BoemuS7OeBstutfb36yfEWjv83%2FC6%2FXKYx0VsR9PI2VP3cU%2BJ8G3Yfq6HFjb54Jl33lRLcIoQm%2B0UzmUKdBaudL4OU3QDnXEIv0ZWVExHVu6qpQkkunSPLzf8840lTTaaBnfdmpGGn9IF8MioynNhfHTo7F6EA7vLa7UnRuvlP%2FFPZE7Xye%2Ba8ltTnC3WsS2MOqpB3BgTSPH0dmaYHoBTdN5O2gHeFBRN8yncWkBAfPRDFrWvxshm%2B2lrOXbHwI%2Fy4pIMmpq98VO8Rwp%2FcpvuQnNTCCHrKGvJrpmS016K%2BZTU%2Bn%2BvrFR%2BsTsb7kjLacK94I9KkcIxWkFP%2BDwv%2BP9SL1VYIqZ7cLYX25WiYWprdSquCbdV4Jrp%2Fx12DlHDU8Wf2kwLNS%2BXsk2y5pkAF7gtuxQ%2BaX4Ac%2F2ST3ev%2FT4FGIDmo6Iljnvlp8EXypUOXN1JSY3EKbwvRluoNYeXJIg5MIXN6fh0nCQCMGibUgEwg72IvQY6pgHqgiI8agSAgZ8aPxeoCCXCWwmVUmJh1bl6iQh8KBN3F%2BF0m4TYsRn8RZMSWVEOkl%2BQ6OYTYgrw00zmtRbBqa14dbh%2Bj9DC3e5BMyEk1BiI2AE1Wyq2ZMucBcOt6iJG7rmCkZ7gTaWIYmJhKo70e6HbHve7oJyxCMa8hnX4WD6yhRIWOSRJu7zo5dkFH37Ls5vU1dUn9f%2BjGUJ6n12p8nJL1hBr1wqi&X-Amz-Signature=31ab63367ed3cf60702569a8143b941a7cf4db390cfad81f7bd2baadcdbd9435&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XNO4BAM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIH%2FihX4VqUgCc0VYx15CC4xuhRpeVQlW4pZpBJ2x3KiXAiAAgUe6oskuKQqZRm3haoUQtGxiV6yDYTUzzbMHLdqR4Cr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMTcuBKI7PIJPDtP22KtwDjoMzQhlsHlZ50bK45%2FRQwasSC8bKCXz8c0it4glSrsOwpRVFsh1uH2%2BVRT52cOWw0DEfj0W4ETpk3Ln1L8JHyR04QTlV%2Be%2BrrdJ%2Frt51ODUk6H0IoDUmw%2F8%2Bz%2FA2TPWXApFVDUxaWT7qSK0Wm%2BC7%2FoHAFIMoEvandqLFg5OjCUTe66C85y%2FMp%2BtcGEXS%2BPtYIsmjr%2F51t4jcyDf0YvSId0S3wtcPXrOxZGbpsfI4o6z0yg%2F1A5c%2FGY%2BXu%2F2APo2a%2FB9Bt36iTAfPBjcCtnR2RN9UaMDK7nDwZRmi1EctDtLN%2FmJUpaokC2wcOwy9iXiKyQXDm0zPmMmX2WAArWMQuFRo1otlACW3sSTPJimkSogbsUZ1exeRfgWV0VINYdqxO0BVt3LxHvWeuLKpMGkbz5JHHLCWfBhoNg%2BCGIQkEjTyWedWs%2BmszRBcTcIGzK0pvjX9SUXYMn9gOT4iglyjHBdD6krN1oX0B4xzyxZpHBLVFGmqm8Ro4as1OplQ%2BKcXu0E7bUrDb9JWkUMBm6jO8iR3qXgjb3hP50yE9Sv1fGGdv6Qv308tgfzSXZpbHtcD8gOdvBLwuPazfPG%2FPIIcnqEpR42clMg7GGM48p9dGXGOITwWd2lLReandU8wyryIvQY6pgEPLmctAHrNmbRLB%2FWmrCA1kBzsMc5x8SF7B2vCFJgHIa79jvz2VAe30jVcexKYT0MpkqyWtBAjfz5EFJULbmx1uYyLEkq4P6LBtLYU4BPpi%2BPiEPahf0989kzN60rzqBs2VSOMRTTDNkd4nKhYKdIiDi8HbomRF1ypqu4Twl3ajv%2B6yby8ye9ytUpHZzz%2BUgs8YjsjG6EQfzLH8ENonkVvSIpHyRDp&X-Amz-Signature=4faaddf6a6a58886fdaef8d6917de799f43a52856985a2626df56da13123a900&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XNO4BAM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIH%2FihX4VqUgCc0VYx15CC4xuhRpeVQlW4pZpBJ2x3KiXAiAAgUe6oskuKQqZRm3haoUQtGxiV6yDYTUzzbMHLdqR4Cr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMTcuBKI7PIJPDtP22KtwDjoMzQhlsHlZ50bK45%2FRQwasSC8bKCXz8c0it4glSrsOwpRVFsh1uH2%2BVRT52cOWw0DEfj0W4ETpk3Ln1L8JHyR04QTlV%2Be%2BrrdJ%2Frt51ODUk6H0IoDUmw%2F8%2Bz%2FA2TPWXApFVDUxaWT7qSK0Wm%2BC7%2FoHAFIMoEvandqLFg5OjCUTe66C85y%2FMp%2BtcGEXS%2BPtYIsmjr%2F51t4jcyDf0YvSId0S3wtcPXrOxZGbpsfI4o6z0yg%2F1A5c%2FGY%2BXu%2F2APo2a%2FB9Bt36iTAfPBjcCtnR2RN9UaMDK7nDwZRmi1EctDtLN%2FmJUpaokC2wcOwy9iXiKyQXDm0zPmMmX2WAArWMQuFRo1otlACW3sSTPJimkSogbsUZ1exeRfgWV0VINYdqxO0BVt3LxHvWeuLKpMGkbz5JHHLCWfBhoNg%2BCGIQkEjTyWedWs%2BmszRBcTcIGzK0pvjX9SUXYMn9gOT4iglyjHBdD6krN1oX0B4xzyxZpHBLVFGmqm8Ro4as1OplQ%2BKcXu0E7bUrDb9JWkUMBm6jO8iR3qXgjb3hP50yE9Sv1fGGdv6Qv308tgfzSXZpbHtcD8gOdvBLwuPazfPG%2FPIIcnqEpR42clMg7GGM48p9dGXGOITwWd2lLReandU8wyryIvQY6pgEPLmctAHrNmbRLB%2FWmrCA1kBzsMc5x8SF7B2vCFJgHIa79jvz2VAe30jVcexKYT0MpkqyWtBAjfz5EFJULbmx1uYyLEkq4P6LBtLYU4BPpi%2BPiEPahf0989kzN60rzqBs2VSOMRTTDNkd4nKhYKdIiDi8HbomRF1ypqu4Twl3ajv%2B6yby8ye9ytUpHZzz%2BUgs8YjsjG6EQfzLH8ENonkVvSIpHyRDp&X-Amz-Signature=61a216e9cc1f1e8a4ea50bd5d6d2c86bd8495f9efe9687701ba8ab3e935ab4c8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XNO4BAM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIH%2FihX4VqUgCc0VYx15CC4xuhRpeVQlW4pZpBJ2x3KiXAiAAgUe6oskuKQqZRm3haoUQtGxiV6yDYTUzzbMHLdqR4Cr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMTcuBKI7PIJPDtP22KtwDjoMzQhlsHlZ50bK45%2FRQwasSC8bKCXz8c0it4glSrsOwpRVFsh1uH2%2BVRT52cOWw0DEfj0W4ETpk3Ln1L8JHyR04QTlV%2Be%2BrrdJ%2Frt51ODUk6H0IoDUmw%2F8%2Bz%2FA2TPWXApFVDUxaWT7qSK0Wm%2BC7%2FoHAFIMoEvandqLFg5OjCUTe66C85y%2FMp%2BtcGEXS%2BPtYIsmjr%2F51t4jcyDf0YvSId0S3wtcPXrOxZGbpsfI4o6z0yg%2F1A5c%2FGY%2BXu%2F2APo2a%2FB9Bt36iTAfPBjcCtnR2RN9UaMDK7nDwZRmi1EctDtLN%2FmJUpaokC2wcOwy9iXiKyQXDm0zPmMmX2WAArWMQuFRo1otlACW3sSTPJimkSogbsUZ1exeRfgWV0VINYdqxO0BVt3LxHvWeuLKpMGkbz5JHHLCWfBhoNg%2BCGIQkEjTyWedWs%2BmszRBcTcIGzK0pvjX9SUXYMn9gOT4iglyjHBdD6krN1oX0B4xzyxZpHBLVFGmqm8Ro4as1OplQ%2BKcXu0E7bUrDb9JWkUMBm6jO8iR3qXgjb3hP50yE9Sv1fGGdv6Qv308tgfzSXZpbHtcD8gOdvBLwuPazfPG%2FPIIcnqEpR42clMg7GGM48p9dGXGOITwWd2lLReandU8wyryIvQY6pgEPLmctAHrNmbRLB%2FWmrCA1kBzsMc5x8SF7B2vCFJgHIa79jvz2VAe30jVcexKYT0MpkqyWtBAjfz5EFJULbmx1uYyLEkq4P6LBtLYU4BPpi%2BPiEPahf0989kzN60rzqBs2VSOMRTTDNkd4nKhYKdIiDi8HbomRF1ypqu4Twl3ajv%2B6yby8ye9ytUpHZzz%2BUgs8YjsjG6EQfzLH8ENonkVvSIpHyRDp&X-Amz-Signature=cedf84f28a5e3292bb7a1533c0ced5f91592aae8f7de9fc30bafc35e45335840&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XNO4BAM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIH%2FihX4VqUgCc0VYx15CC4xuhRpeVQlW4pZpBJ2x3KiXAiAAgUe6oskuKQqZRm3haoUQtGxiV6yDYTUzzbMHLdqR4Cr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMTcuBKI7PIJPDtP22KtwDjoMzQhlsHlZ50bK45%2FRQwasSC8bKCXz8c0it4glSrsOwpRVFsh1uH2%2BVRT52cOWw0DEfj0W4ETpk3Ln1L8JHyR04QTlV%2Be%2BrrdJ%2Frt51ODUk6H0IoDUmw%2F8%2Bz%2FA2TPWXApFVDUxaWT7qSK0Wm%2BC7%2FoHAFIMoEvandqLFg5OjCUTe66C85y%2FMp%2BtcGEXS%2BPtYIsmjr%2F51t4jcyDf0YvSId0S3wtcPXrOxZGbpsfI4o6z0yg%2F1A5c%2FGY%2BXu%2F2APo2a%2FB9Bt36iTAfPBjcCtnR2RN9UaMDK7nDwZRmi1EctDtLN%2FmJUpaokC2wcOwy9iXiKyQXDm0zPmMmX2WAArWMQuFRo1otlACW3sSTPJimkSogbsUZ1exeRfgWV0VINYdqxO0BVt3LxHvWeuLKpMGkbz5JHHLCWfBhoNg%2BCGIQkEjTyWedWs%2BmszRBcTcIGzK0pvjX9SUXYMn9gOT4iglyjHBdD6krN1oX0B4xzyxZpHBLVFGmqm8Ro4as1OplQ%2BKcXu0E7bUrDb9JWkUMBm6jO8iR3qXgjb3hP50yE9Sv1fGGdv6Qv308tgfzSXZpbHtcD8gOdvBLwuPazfPG%2FPIIcnqEpR42clMg7GGM48p9dGXGOITwWd2lLReandU8wyryIvQY6pgEPLmctAHrNmbRLB%2FWmrCA1kBzsMc5x8SF7B2vCFJgHIa79jvz2VAe30jVcexKYT0MpkqyWtBAjfz5EFJULbmx1uYyLEkq4P6LBtLYU4BPpi%2BPiEPahf0989kzN60rzqBs2VSOMRTTDNkd4nKhYKdIiDi8HbomRF1ypqu4Twl3ajv%2B6yby8ye9ytUpHZzz%2BUgs8YjsjG6EQfzLH8ENonkVvSIpHyRDp&X-Amz-Signature=f1906be6cca39c534389df5dc23a5883118d7b11e20ecba71b4cef6c462a9374&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XNO4BAM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIH%2FihX4VqUgCc0VYx15CC4xuhRpeVQlW4pZpBJ2x3KiXAiAAgUe6oskuKQqZRm3haoUQtGxiV6yDYTUzzbMHLdqR4Cr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMTcuBKI7PIJPDtP22KtwDjoMzQhlsHlZ50bK45%2FRQwasSC8bKCXz8c0it4glSrsOwpRVFsh1uH2%2BVRT52cOWw0DEfj0W4ETpk3Ln1L8JHyR04QTlV%2Be%2BrrdJ%2Frt51ODUk6H0IoDUmw%2F8%2Bz%2FA2TPWXApFVDUxaWT7qSK0Wm%2BC7%2FoHAFIMoEvandqLFg5OjCUTe66C85y%2FMp%2BtcGEXS%2BPtYIsmjr%2F51t4jcyDf0YvSId0S3wtcPXrOxZGbpsfI4o6z0yg%2F1A5c%2FGY%2BXu%2F2APo2a%2FB9Bt36iTAfPBjcCtnR2RN9UaMDK7nDwZRmi1EctDtLN%2FmJUpaokC2wcOwy9iXiKyQXDm0zPmMmX2WAArWMQuFRo1otlACW3sSTPJimkSogbsUZ1exeRfgWV0VINYdqxO0BVt3LxHvWeuLKpMGkbz5JHHLCWfBhoNg%2BCGIQkEjTyWedWs%2BmszRBcTcIGzK0pvjX9SUXYMn9gOT4iglyjHBdD6krN1oX0B4xzyxZpHBLVFGmqm8Ro4as1OplQ%2BKcXu0E7bUrDb9JWkUMBm6jO8iR3qXgjb3hP50yE9Sv1fGGdv6Qv308tgfzSXZpbHtcD8gOdvBLwuPazfPG%2FPIIcnqEpR42clMg7GGM48p9dGXGOITwWd2lLReandU8wyryIvQY6pgEPLmctAHrNmbRLB%2FWmrCA1kBzsMc5x8SF7B2vCFJgHIa79jvz2VAe30jVcexKYT0MpkqyWtBAjfz5EFJULbmx1uYyLEkq4P6LBtLYU4BPpi%2BPiEPahf0989kzN60rzqBs2VSOMRTTDNkd4nKhYKdIiDi8HbomRF1ypqu4Twl3ajv%2B6yby8ye9ytUpHZzz%2BUgs8YjsjG6EQfzLH8ENonkVvSIpHyRDp&X-Amz-Signature=9455ec24d1e173ccd54db88e34980ef62ffba75c7c547699caf2b9f0a62ddb5a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMNE74N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBtgSp4u3jDRlw6A7zXAiqHT9P7rN7jn9QmlBvTHGdYzAiA316Qcbd5%2BFLGURdZZwbQs%2Be5QwnTbAw8t1OtriKMmsSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMVcfXej8y8ZrEHsXCKtwDCkMImy8EhFuXgdoIGzLb0orTDgOgt6zQlNy3HXa0x2UKmLRwzsTfVxIHRH%2Fk52yl%2Fo2dSrHllZEb124PF%2FnRxkc%2Fct%2BeiMoJEZJVv5wDn8yo5SQ%2FAu3itSEKb24Oa0KlfUA%2F0s0uALxYLb%2FQynQ%2BoemuS7OeBstutfb36yfEWjv83%2FC6%2FXKYx0VsR9PI2VP3cU%2BJ8G3Yfq6HFjb54Jl33lRLcIoQm%2B0UzmUKdBaudL4OU3QDnXEIv0ZWVExHVu6qpQkkunSPLzf8840lTTaaBnfdmpGGn9IF8MioynNhfHTo7F6EA7vLa7UnRuvlP%2FFPZE7Xye%2Ba8ltTnC3WsS2MOqpB3BgTSPH0dmaYHoBTdN5O2gHeFBRN8yncWkBAfPRDFrWvxshm%2B2lrOXbHwI%2Fy4pIMmpq98VO8Rwp%2FcpvuQnNTCCHrKGvJrpmS016K%2BZTU%2Bn%2BvrFR%2BsTsb7kjLacK94I9KkcIxWkFP%2BDwv%2BP9SL1VYIqZ7cLYX25WiYWprdSquCbdV4Jrp%2Fx12DlHDU8Wf2kwLNS%2BXsk2y5pkAF7gtuxQ%2BaX4Ac%2F2ST3ev%2FT4FGIDmo6Iljnvlp8EXypUOXN1JSY3EKbwvRluoNYeXJIg5MIXN6fh0nCQCMGibUgEwg72IvQY6pgHqgiI8agSAgZ8aPxeoCCXCWwmVUmJh1bl6iQh8KBN3F%2BF0m4TYsRn8RZMSWVEOkl%2BQ6OYTYgrw00zmtRbBqa14dbh%2Bj9DC3e5BMyEk1BiI2AE1Wyq2ZMucBcOt6iJG7rmCkZ7gTaWIYmJhKo70e6HbHve7oJyxCMa8hnX4WD6yhRIWOSRJu7zo5dkFH37Ls5vU1dUn9f%2BjGUJ6n12p8nJL1hBr1wqi&X-Amz-Signature=0ee7998fee31b0e1d0dbd8e23e87ae0b63208adf7833e26195c8b49d133969a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMNE74N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBtgSp4u3jDRlw6A7zXAiqHT9P7rN7jn9QmlBvTHGdYzAiA316Qcbd5%2BFLGURdZZwbQs%2Be5QwnTbAw8t1OtriKMmsSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMVcfXej8y8ZrEHsXCKtwDCkMImy8EhFuXgdoIGzLb0orTDgOgt6zQlNy3HXa0x2UKmLRwzsTfVxIHRH%2Fk52yl%2Fo2dSrHllZEb124PF%2FnRxkc%2Fct%2BeiMoJEZJVv5wDn8yo5SQ%2FAu3itSEKb24Oa0KlfUA%2F0s0uALxYLb%2FQynQ%2BoemuS7OeBstutfb36yfEWjv83%2FC6%2FXKYx0VsR9PI2VP3cU%2BJ8G3Yfq6HFjb54Jl33lRLcIoQm%2B0UzmUKdBaudL4OU3QDnXEIv0ZWVExHVu6qpQkkunSPLzf8840lTTaaBnfdmpGGn9IF8MioynNhfHTo7F6EA7vLa7UnRuvlP%2FFPZE7Xye%2Ba8ltTnC3WsS2MOqpB3BgTSPH0dmaYHoBTdN5O2gHeFBRN8yncWkBAfPRDFrWvxshm%2B2lrOXbHwI%2Fy4pIMmpq98VO8Rwp%2FcpvuQnNTCCHrKGvJrpmS016K%2BZTU%2Bn%2BvrFR%2BsTsb7kjLacK94I9KkcIxWkFP%2BDwv%2BP9SL1VYIqZ7cLYX25WiYWprdSquCbdV4Jrp%2Fx12DlHDU8Wf2kwLNS%2BXsk2y5pkAF7gtuxQ%2BaX4Ac%2F2ST3ev%2FT4FGIDmo6Iljnvlp8EXypUOXN1JSY3EKbwvRluoNYeXJIg5MIXN6fh0nCQCMGibUgEwg72IvQY6pgHqgiI8agSAgZ8aPxeoCCXCWwmVUmJh1bl6iQh8KBN3F%2BF0m4TYsRn8RZMSWVEOkl%2BQ6OYTYgrw00zmtRbBqa14dbh%2Bj9DC3e5BMyEk1BiI2AE1Wyq2ZMucBcOt6iJG7rmCkZ7gTaWIYmJhKo70e6HbHve7oJyxCMa8hnX4WD6yhRIWOSRJu7zo5dkFH37Ls5vU1dUn9f%2BjGUJ6n12p8nJL1hBr1wqi&X-Amz-Signature=e7aec5e42c498461e946f78decf75f8e07e08930ece1a81b0a0028d93b1ceb37&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMNE74N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBtgSp4u3jDRlw6A7zXAiqHT9P7rN7jn9QmlBvTHGdYzAiA316Qcbd5%2BFLGURdZZwbQs%2Be5QwnTbAw8t1OtriKMmsSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMVcfXej8y8ZrEHsXCKtwDCkMImy8EhFuXgdoIGzLb0orTDgOgt6zQlNy3HXa0x2UKmLRwzsTfVxIHRH%2Fk52yl%2Fo2dSrHllZEb124PF%2FnRxkc%2Fct%2BeiMoJEZJVv5wDn8yo5SQ%2FAu3itSEKb24Oa0KlfUA%2F0s0uALxYLb%2FQynQ%2BoemuS7OeBstutfb36yfEWjv83%2FC6%2FXKYx0VsR9PI2VP3cU%2BJ8G3Yfq6HFjb54Jl33lRLcIoQm%2B0UzmUKdBaudL4OU3QDnXEIv0ZWVExHVu6qpQkkunSPLzf8840lTTaaBnfdmpGGn9IF8MioynNhfHTo7F6EA7vLa7UnRuvlP%2FFPZE7Xye%2Ba8ltTnC3WsS2MOqpB3BgTSPH0dmaYHoBTdN5O2gHeFBRN8yncWkBAfPRDFrWvxshm%2B2lrOXbHwI%2Fy4pIMmpq98VO8Rwp%2FcpvuQnNTCCHrKGvJrpmS016K%2BZTU%2Bn%2BvrFR%2BsTsb7kjLacK94I9KkcIxWkFP%2BDwv%2BP9SL1VYIqZ7cLYX25WiYWprdSquCbdV4Jrp%2Fx12DlHDU8Wf2kwLNS%2BXsk2y5pkAF7gtuxQ%2BaX4Ac%2F2ST3ev%2FT4FGIDmo6Iljnvlp8EXypUOXN1JSY3EKbwvRluoNYeXJIg5MIXN6fh0nCQCMGibUgEwg72IvQY6pgHqgiI8agSAgZ8aPxeoCCXCWwmVUmJh1bl6iQh8KBN3F%2BF0m4TYsRn8RZMSWVEOkl%2BQ6OYTYgrw00zmtRbBqa14dbh%2Bj9DC3e5BMyEk1BiI2AE1Wyq2ZMucBcOt6iJG7rmCkZ7gTaWIYmJhKo70e6HbHve7oJyxCMa8hnX4WD6yhRIWOSRJu7zo5dkFH37Ls5vU1dUn9f%2BjGUJ6n12p8nJL1hBr1wqi&X-Amz-Signature=27a65e3ca5c345be95520e6d15f0479703f2e0b6320d607f35e2405130acb02b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMNE74N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBtgSp4u3jDRlw6A7zXAiqHT9P7rN7jn9QmlBvTHGdYzAiA316Qcbd5%2BFLGURdZZwbQs%2Be5QwnTbAw8t1OtriKMmsSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMVcfXej8y8ZrEHsXCKtwDCkMImy8EhFuXgdoIGzLb0orTDgOgt6zQlNy3HXa0x2UKmLRwzsTfVxIHRH%2Fk52yl%2Fo2dSrHllZEb124PF%2FnRxkc%2Fct%2BeiMoJEZJVv5wDn8yo5SQ%2FAu3itSEKb24Oa0KlfUA%2F0s0uALxYLb%2FQynQ%2BoemuS7OeBstutfb36yfEWjv83%2FC6%2FXKYx0VsR9PI2VP3cU%2BJ8G3Yfq6HFjb54Jl33lRLcIoQm%2B0UzmUKdBaudL4OU3QDnXEIv0ZWVExHVu6qpQkkunSPLzf8840lTTaaBnfdmpGGn9IF8MioynNhfHTo7F6EA7vLa7UnRuvlP%2FFPZE7Xye%2Ba8ltTnC3WsS2MOqpB3BgTSPH0dmaYHoBTdN5O2gHeFBRN8yncWkBAfPRDFrWvxshm%2B2lrOXbHwI%2Fy4pIMmpq98VO8Rwp%2FcpvuQnNTCCHrKGvJrpmS016K%2BZTU%2Bn%2BvrFR%2BsTsb7kjLacK94I9KkcIxWkFP%2BDwv%2BP9SL1VYIqZ7cLYX25WiYWprdSquCbdV4Jrp%2Fx12DlHDU8Wf2kwLNS%2BXsk2y5pkAF7gtuxQ%2BaX4Ac%2F2ST3ev%2FT4FGIDmo6Iljnvlp8EXypUOXN1JSY3EKbwvRluoNYeXJIg5MIXN6fh0nCQCMGibUgEwg72IvQY6pgHqgiI8agSAgZ8aPxeoCCXCWwmVUmJh1bl6iQh8KBN3F%2BF0m4TYsRn8RZMSWVEOkl%2BQ6OYTYgrw00zmtRbBqa14dbh%2Bj9DC3e5BMyEk1BiI2AE1Wyq2ZMucBcOt6iJG7rmCkZ7gTaWIYmJhKo70e6HbHve7oJyxCMa8hnX4WD6yhRIWOSRJu7zo5dkFH37Ls5vU1dUn9f%2BjGUJ6n12p8nJL1hBr1wqi&X-Amz-Signature=905a29c9ea2357fd963bb91f389cbb23cb1380d32f1552f72c189aebf4b55fcc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMNE74N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIBtgSp4u3jDRlw6A7zXAiqHT9P7rN7jn9QmlBvTHGdYzAiA316Qcbd5%2BFLGURdZZwbQs%2Be5QwnTbAw8t1OtriKMmsSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMVcfXej8y8ZrEHsXCKtwDCkMImy8EhFuXgdoIGzLb0orTDgOgt6zQlNy3HXa0x2UKmLRwzsTfVxIHRH%2Fk52yl%2Fo2dSrHllZEb124PF%2FnRxkc%2Fct%2BeiMoJEZJVv5wDn8yo5SQ%2FAu3itSEKb24Oa0KlfUA%2F0s0uALxYLb%2FQynQ%2BoemuS7OeBstutfb36yfEWjv83%2FC6%2FXKYx0VsR9PI2VP3cU%2BJ8G3Yfq6HFjb54Jl33lRLcIoQm%2B0UzmUKdBaudL4OU3QDnXEIv0ZWVExHVu6qpQkkunSPLzf8840lTTaaBnfdmpGGn9IF8MioynNhfHTo7F6EA7vLa7UnRuvlP%2FFPZE7Xye%2Ba8ltTnC3WsS2MOqpB3BgTSPH0dmaYHoBTdN5O2gHeFBRN8yncWkBAfPRDFrWvxshm%2B2lrOXbHwI%2Fy4pIMmpq98VO8Rwp%2FcpvuQnNTCCHrKGvJrpmS016K%2BZTU%2Bn%2BvrFR%2BsTsb7kjLacK94I9KkcIxWkFP%2BDwv%2BP9SL1VYIqZ7cLYX25WiYWprdSquCbdV4Jrp%2Fx12DlHDU8Wf2kwLNS%2BXsk2y5pkAF7gtuxQ%2BaX4Ac%2F2ST3ev%2FT4FGIDmo6Iljnvlp8EXypUOXN1JSY3EKbwvRluoNYeXJIg5MIXN6fh0nCQCMGibUgEwg72IvQY6pgHqgiI8agSAgZ8aPxeoCCXCWwmVUmJh1bl6iQh8KBN3F%2BF0m4TYsRn8RZMSWVEOkl%2BQ6OYTYgrw00zmtRbBqa14dbh%2Bj9DC3e5BMyEk1BiI2AE1Wyq2ZMucBcOt6iJG7rmCkZ7gTaWIYmJhKo70e6HbHve7oJyxCMa8hnX4WD6yhRIWOSRJu7zo5dkFH37Ls5vU1dUn9f%2BjGUJ6n12p8nJL1hBr1wqi&X-Amz-Signature=e8fc94bece930689a440a37215c384e3b42fd362222d7e21d71b1618d4eeda82&X-Amz-SignedHeaders=host&x-id=GetObject)
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


