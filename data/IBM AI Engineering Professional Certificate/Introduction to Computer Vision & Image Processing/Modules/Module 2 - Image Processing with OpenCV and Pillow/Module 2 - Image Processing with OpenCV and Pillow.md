

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466223IY2B7%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3IST%2BKh%2F%2FBg0LCiYGGz39pxBLXjF3KEUlYXC7ldr%2B5AiEAikUwWmXpNLAyG8XtH0lC%2FKwh1Q%2Bj3V8JYdGn04WKfKsqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQdaus3SrJtP%2BwjoyrcA%2FWy8p%2BTJxVgwk7WV3Z9LWVZEinpDUy650e8sZ9V0IKeXIDr5%2FC%2B3FCoLthaeH1dpLtzoWm6UlD9pWttqNOTyNg6Dhv%2FMLd05lnbvqmqkwP8UNOtZnpvF8nMeH8KQdgaXxvndaHZjyUHMASecCN1iQdfwL7GoyjpxyNvPkDL6CSECa7umfjOUVeY4jYPYZKtZaviilBmjBWf1yw7NgRaXUt8Byaayk18CcPIa13U2RGgqmwxcYnINbO5JyrDJZM8HXANy5ia6fm6OfX8W8p3Vj5Nmj0rOisfWJvnaHi9ARPVUESX%2BW2wyqVPrfnSZuiSrbesuMvI23YgREWLdHwGNuHEhMhEz9oHQ8BeXFIhoyDGutDBENtcDGzPzceMwAP5EnfbboKdhmC9hhEPJhO7rNlL2f%2Fu3VfWTTsUQQvSU0H4MrBr1EKyyp1Kw2N0mY0Z%2FK7AwGJh%2Brc1m0K4V%2Bt8Auj8ebacSC1%2FpmvX5octx6Rwr%2BYDpBdbRQxqwdq9NjuUJXFlSLARa9Pg6rlcj6s650Hr9f9GHIHpKkqLjmCGNCMqp51FwLYJuOBLMhajmAK9%2F0oyfXri0H1GDOTSCFW2%2BAoAkHRXx3H0dt6bgtVB4hST5xhqt%2BcXonG4dTtVMI3Xn70GOqUBWj0N6sdPZ7DI7gceIC7b9o%2BOxks5vlesbyEEFzm%2B34up9hS8oGlNZr76GnO8LccK0EGxxgnxhXYZNk6bNRcZE%2BxDm8nwZ5t3qVYpbrmW5fQBxi1gKumtV%2BrnGGcmBZELgJXcn6TTyWz6YuAFcdp3yuzrahKhFIfZND3yR6mEKgZH%2BgiIZa8jaXbbz%2FTHDqmb4lrm2AFuwhtpMfUSFNN0DA3mZtzb&X-Amz-Signature=991ca5e23826daf17d852783c6c9fd949b3fa15e66d3ec9e54cf6e1b74530324&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYX32XOI%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD48Lho%2FDIByxqoMoQAsf%2B5OVNU1jh5ze3hmOXmsSDS9AIgROU4NhdJzRjy47dF9NQT3PotUI42PmR9zdfEj9xJ6DYqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBoJs3UaKGHCRddCTCrcAwmS5lrcraKcsvqZCfpq5zDCpc7QI27tcI%2BjeJyMeAqocBuMy%2BHd6VtSRI6b9FVNoicnVPSqFz3m251MyaufpAPB7Vlkg7ahkSRFvQYTIegXf9%2FI5X34iAyHvLwD%2B7GJIsy1IjkL%2FwgHAhUdlY5eyJIdud8OMAjgwEyqCGJAQ8BW6TDlwf4%2FBa%2BULpw%2BTXO5ZJtnTZgE%2FK0%2FaF6I0sh9%2BvRD8jDhrFm%2FuHvaygIyJVopiZQKmaAVMQnWuo2AdpbQb9PIN%2BBRv2fSr%2Bx1ArI3BK4r2CFZw4ICxe8cn8pKdlzlbkirrrSEFZGmcQ1huz870Q3Vj%2F%2B95lFOGyHF3KCu313EQH%2BuYS90dU5hZ4P6on3FnYuCqiGErsTqoZ84JzUCUTI%2BYjGJ7zFv3DmjX%2BDpxMYxeLTFh5JrhfpcQ%2F1jzK2vm6PzgjU%2BnHf8TPH60PdJV%2BYNju1DLxayei2%2F9T0co6U%2FtRj1qWNjQc9W9fBltfqxOoTuJfFHbGBJtLRi7uaHHQs0pJoCHFQxvXoIhNP2lH6yndgI6MU9Am%2BD3lhVBFptXQErME8p%2BIjlXf%2FiLIAXJGbiWIHhCS0o0zAyHj%2Fs22XHiAuwOBN94chz%2BnEMBWLnPGlVWzQzDWj8ljePMMDWn70GOqUB27eiSpCv7H%2Fv3u3%2BHvkzWTZMTfwlub6RPapaWX1K9r6xrRkyhyB7iWr9d0QPXYvCayKm1bPixz6c5IbxlWofhi4iB7L28LjJf1z7XtP1p%2FGSWMj4IXUbiYBGNvn9UU8MUV1XgpnurpqHSgNIleqzTV8ihNWACqW%2B18bLw4Ypkrfclf7vlJWN3%2BmLtowHZ6gxZdAZe9lnCRVw2W8mE%2FdtdmfJnPoT&X-Amz-Signature=cedf1d47153b7bd39358e1bf78696e060c43adefcb222b4d8aec90ddb98a49e9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYX32XOI%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD48Lho%2FDIByxqoMoQAsf%2B5OVNU1jh5ze3hmOXmsSDS9AIgROU4NhdJzRjy47dF9NQT3PotUI42PmR9zdfEj9xJ6DYqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBoJs3UaKGHCRddCTCrcAwmS5lrcraKcsvqZCfpq5zDCpc7QI27tcI%2BjeJyMeAqocBuMy%2BHd6VtSRI6b9FVNoicnVPSqFz3m251MyaufpAPB7Vlkg7ahkSRFvQYTIegXf9%2FI5X34iAyHvLwD%2B7GJIsy1IjkL%2FwgHAhUdlY5eyJIdud8OMAjgwEyqCGJAQ8BW6TDlwf4%2FBa%2BULpw%2BTXO5ZJtnTZgE%2FK0%2FaF6I0sh9%2BvRD8jDhrFm%2FuHvaygIyJVopiZQKmaAVMQnWuo2AdpbQb9PIN%2BBRv2fSr%2Bx1ArI3BK4r2CFZw4ICxe8cn8pKdlzlbkirrrSEFZGmcQ1huz870Q3Vj%2F%2B95lFOGyHF3KCu313EQH%2BuYS90dU5hZ4P6on3FnYuCqiGErsTqoZ84JzUCUTI%2BYjGJ7zFv3DmjX%2BDpxMYxeLTFh5JrhfpcQ%2F1jzK2vm6PzgjU%2BnHf8TPH60PdJV%2BYNju1DLxayei2%2F9T0co6U%2FtRj1qWNjQc9W9fBltfqxOoTuJfFHbGBJtLRi7uaHHQs0pJoCHFQxvXoIhNP2lH6yndgI6MU9Am%2BD3lhVBFptXQErME8p%2BIjlXf%2FiLIAXJGbiWIHhCS0o0zAyHj%2Fs22XHiAuwOBN94chz%2BnEMBWLnPGlVWzQzDWj8ljePMMDWn70GOqUB27eiSpCv7H%2Fv3u3%2BHvkzWTZMTfwlub6RPapaWX1K9r6xrRkyhyB7iWr9d0QPXYvCayKm1bPixz6c5IbxlWofhi4iB7L28LjJf1z7XtP1p%2FGSWMj4IXUbiYBGNvn9UU8MUV1XgpnurpqHSgNIleqzTV8ihNWACqW%2B18bLw4Ypkrfclf7vlJWN3%2BmLtowHZ6gxZdAZe9lnCRVw2W8mE%2FdtdmfJnPoT&X-Amz-Signature=6ed5b59fa8cde73d51543fd0465bac3e2c6616d8dac73e7800082c7bec5443ea&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYX32XOI%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD48Lho%2FDIByxqoMoQAsf%2B5OVNU1jh5ze3hmOXmsSDS9AIgROU4NhdJzRjy47dF9NQT3PotUI42PmR9zdfEj9xJ6DYqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBoJs3UaKGHCRddCTCrcAwmS5lrcraKcsvqZCfpq5zDCpc7QI27tcI%2BjeJyMeAqocBuMy%2BHd6VtSRI6b9FVNoicnVPSqFz3m251MyaufpAPB7Vlkg7ahkSRFvQYTIegXf9%2FI5X34iAyHvLwD%2B7GJIsy1IjkL%2FwgHAhUdlY5eyJIdud8OMAjgwEyqCGJAQ8BW6TDlwf4%2FBa%2BULpw%2BTXO5ZJtnTZgE%2FK0%2FaF6I0sh9%2BvRD8jDhrFm%2FuHvaygIyJVopiZQKmaAVMQnWuo2AdpbQb9PIN%2BBRv2fSr%2Bx1ArI3BK4r2CFZw4ICxe8cn8pKdlzlbkirrrSEFZGmcQ1huz870Q3Vj%2F%2B95lFOGyHF3KCu313EQH%2BuYS90dU5hZ4P6on3FnYuCqiGErsTqoZ84JzUCUTI%2BYjGJ7zFv3DmjX%2BDpxMYxeLTFh5JrhfpcQ%2F1jzK2vm6PzgjU%2BnHf8TPH60PdJV%2BYNju1DLxayei2%2F9T0co6U%2FtRj1qWNjQc9W9fBltfqxOoTuJfFHbGBJtLRi7uaHHQs0pJoCHFQxvXoIhNP2lH6yndgI6MU9Am%2BD3lhVBFptXQErME8p%2BIjlXf%2FiLIAXJGbiWIHhCS0o0zAyHj%2Fs22XHiAuwOBN94chz%2BnEMBWLnPGlVWzQzDWj8ljePMMDWn70GOqUB27eiSpCv7H%2Fv3u3%2BHvkzWTZMTfwlub6RPapaWX1K9r6xrRkyhyB7iWr9d0QPXYvCayKm1bPixz6c5IbxlWofhi4iB7L28LjJf1z7XtP1p%2FGSWMj4IXUbiYBGNvn9UU8MUV1XgpnurpqHSgNIleqzTV8ihNWACqW%2B18bLw4Ypkrfclf7vlJWN3%2BmLtowHZ6gxZdAZe9lnCRVw2W8mE%2FdtdmfJnPoT&X-Amz-Signature=f84124922fb5d3c823345e3a602c37016ee6555b16d048b6812ae7bdd30215fa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYX32XOI%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD48Lho%2FDIByxqoMoQAsf%2B5OVNU1jh5ze3hmOXmsSDS9AIgROU4NhdJzRjy47dF9NQT3PotUI42PmR9zdfEj9xJ6DYqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBoJs3UaKGHCRddCTCrcAwmS5lrcraKcsvqZCfpq5zDCpc7QI27tcI%2BjeJyMeAqocBuMy%2BHd6VtSRI6b9FVNoicnVPSqFz3m251MyaufpAPB7Vlkg7ahkSRFvQYTIegXf9%2FI5X34iAyHvLwD%2B7GJIsy1IjkL%2FwgHAhUdlY5eyJIdud8OMAjgwEyqCGJAQ8BW6TDlwf4%2FBa%2BULpw%2BTXO5ZJtnTZgE%2FK0%2FaF6I0sh9%2BvRD8jDhrFm%2FuHvaygIyJVopiZQKmaAVMQnWuo2AdpbQb9PIN%2BBRv2fSr%2Bx1ArI3BK4r2CFZw4ICxe8cn8pKdlzlbkirrrSEFZGmcQ1huz870Q3Vj%2F%2B95lFOGyHF3KCu313EQH%2BuYS90dU5hZ4P6on3FnYuCqiGErsTqoZ84JzUCUTI%2BYjGJ7zFv3DmjX%2BDpxMYxeLTFh5JrhfpcQ%2F1jzK2vm6PzgjU%2BnHf8TPH60PdJV%2BYNju1DLxayei2%2F9T0co6U%2FtRj1qWNjQc9W9fBltfqxOoTuJfFHbGBJtLRi7uaHHQs0pJoCHFQxvXoIhNP2lH6yndgI6MU9Am%2BD3lhVBFptXQErME8p%2BIjlXf%2FiLIAXJGbiWIHhCS0o0zAyHj%2Fs22XHiAuwOBN94chz%2BnEMBWLnPGlVWzQzDWj8ljePMMDWn70GOqUB27eiSpCv7H%2Fv3u3%2BHvkzWTZMTfwlub6RPapaWX1K9r6xrRkyhyB7iWr9d0QPXYvCayKm1bPixz6c5IbxlWofhi4iB7L28LjJf1z7XtP1p%2FGSWMj4IXUbiYBGNvn9UU8MUV1XgpnurpqHSgNIleqzTV8ihNWACqW%2B18bLw4Ypkrfclf7vlJWN3%2BmLtowHZ6gxZdAZe9lnCRVw2W8mE%2FdtdmfJnPoT&X-Amz-Signature=93b8614dbfa496efe64f7aa5c338fa0ad80f2a4863af05ba490a7355bb3e565c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYX32XOI%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD48Lho%2FDIByxqoMoQAsf%2B5OVNU1jh5ze3hmOXmsSDS9AIgROU4NhdJzRjy47dF9NQT3PotUI42PmR9zdfEj9xJ6DYqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBoJs3UaKGHCRddCTCrcAwmS5lrcraKcsvqZCfpq5zDCpc7QI27tcI%2BjeJyMeAqocBuMy%2BHd6VtSRI6b9FVNoicnVPSqFz3m251MyaufpAPB7Vlkg7ahkSRFvQYTIegXf9%2FI5X34iAyHvLwD%2B7GJIsy1IjkL%2FwgHAhUdlY5eyJIdud8OMAjgwEyqCGJAQ8BW6TDlwf4%2FBa%2BULpw%2BTXO5ZJtnTZgE%2FK0%2FaF6I0sh9%2BvRD8jDhrFm%2FuHvaygIyJVopiZQKmaAVMQnWuo2AdpbQb9PIN%2BBRv2fSr%2Bx1ArI3BK4r2CFZw4ICxe8cn8pKdlzlbkirrrSEFZGmcQ1huz870Q3Vj%2F%2B95lFOGyHF3KCu313EQH%2BuYS90dU5hZ4P6on3FnYuCqiGErsTqoZ84JzUCUTI%2BYjGJ7zFv3DmjX%2BDpxMYxeLTFh5JrhfpcQ%2F1jzK2vm6PzgjU%2BnHf8TPH60PdJV%2BYNju1DLxayei2%2F9T0co6U%2FtRj1qWNjQc9W9fBltfqxOoTuJfFHbGBJtLRi7uaHHQs0pJoCHFQxvXoIhNP2lH6yndgI6MU9Am%2BD3lhVBFptXQErME8p%2BIjlXf%2FiLIAXJGbiWIHhCS0o0zAyHj%2Fs22XHiAuwOBN94chz%2BnEMBWLnPGlVWzQzDWj8ljePMMDWn70GOqUB27eiSpCv7H%2Fv3u3%2BHvkzWTZMTfwlub6RPapaWX1K9r6xrRkyhyB7iWr9d0QPXYvCayKm1bPixz6c5IbxlWofhi4iB7L28LjJf1z7XtP1p%2FGSWMj4IXUbiYBGNvn9UU8MUV1XgpnurpqHSgNIleqzTV8ihNWACqW%2B18bLw4Ypkrfclf7vlJWN3%2BmLtowHZ6gxZdAZe9lnCRVw2W8mE%2FdtdmfJnPoT&X-Amz-Signature=7b905a637ce544429d16c2d33ff679ae00dd702ca0fdfae985f51f4ba79fca31&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466223IY2B7%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3IST%2BKh%2F%2FBg0LCiYGGz39pxBLXjF3KEUlYXC7ldr%2B5AiEAikUwWmXpNLAyG8XtH0lC%2FKwh1Q%2Bj3V8JYdGn04WKfKsqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQdaus3SrJtP%2BwjoyrcA%2FWy8p%2BTJxVgwk7WV3Z9LWVZEinpDUy650e8sZ9V0IKeXIDr5%2FC%2B3FCoLthaeH1dpLtzoWm6UlD9pWttqNOTyNg6Dhv%2FMLd05lnbvqmqkwP8UNOtZnpvF8nMeH8KQdgaXxvndaHZjyUHMASecCN1iQdfwL7GoyjpxyNvPkDL6CSECa7umfjOUVeY4jYPYZKtZaviilBmjBWf1yw7NgRaXUt8Byaayk18CcPIa13U2RGgqmwxcYnINbO5JyrDJZM8HXANy5ia6fm6OfX8W8p3Vj5Nmj0rOisfWJvnaHi9ARPVUESX%2BW2wyqVPrfnSZuiSrbesuMvI23YgREWLdHwGNuHEhMhEz9oHQ8BeXFIhoyDGutDBENtcDGzPzceMwAP5EnfbboKdhmC9hhEPJhO7rNlL2f%2Fu3VfWTTsUQQvSU0H4MrBr1EKyyp1Kw2N0mY0Z%2FK7AwGJh%2Brc1m0K4V%2Bt8Auj8ebacSC1%2FpmvX5octx6Rwr%2BYDpBdbRQxqwdq9NjuUJXFlSLARa9Pg6rlcj6s650Hr9f9GHIHpKkqLjmCGNCMqp51FwLYJuOBLMhajmAK9%2F0oyfXri0H1GDOTSCFW2%2BAoAkHRXx3H0dt6bgtVB4hST5xhqt%2BcXonG4dTtVMI3Xn70GOqUBWj0N6sdPZ7DI7gceIC7b9o%2BOxks5vlesbyEEFzm%2B34up9hS8oGlNZr76GnO8LccK0EGxxgnxhXYZNk6bNRcZE%2BxDm8nwZ5t3qVYpbrmW5fQBxi1gKumtV%2BrnGGcmBZELgJXcn6TTyWz6YuAFcdp3yuzrahKhFIfZND3yR6mEKgZH%2BgiIZa8jaXbbz%2FTHDqmb4lrm2AFuwhtpMfUSFNN0DA3mZtzb&X-Amz-Signature=0a029115d84f193acb2caaf4dc23ce009502036991a73298dac71b9e056e2faf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466223IY2B7%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3IST%2BKh%2F%2FBg0LCiYGGz39pxBLXjF3KEUlYXC7ldr%2B5AiEAikUwWmXpNLAyG8XtH0lC%2FKwh1Q%2Bj3V8JYdGn04WKfKsqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQdaus3SrJtP%2BwjoyrcA%2FWy8p%2BTJxVgwk7WV3Z9LWVZEinpDUy650e8sZ9V0IKeXIDr5%2FC%2B3FCoLthaeH1dpLtzoWm6UlD9pWttqNOTyNg6Dhv%2FMLd05lnbvqmqkwP8UNOtZnpvF8nMeH8KQdgaXxvndaHZjyUHMASecCN1iQdfwL7GoyjpxyNvPkDL6CSECa7umfjOUVeY4jYPYZKtZaviilBmjBWf1yw7NgRaXUt8Byaayk18CcPIa13U2RGgqmwxcYnINbO5JyrDJZM8HXANy5ia6fm6OfX8W8p3Vj5Nmj0rOisfWJvnaHi9ARPVUESX%2BW2wyqVPrfnSZuiSrbesuMvI23YgREWLdHwGNuHEhMhEz9oHQ8BeXFIhoyDGutDBENtcDGzPzceMwAP5EnfbboKdhmC9hhEPJhO7rNlL2f%2Fu3VfWTTsUQQvSU0H4MrBr1EKyyp1Kw2N0mY0Z%2FK7AwGJh%2Brc1m0K4V%2Bt8Auj8ebacSC1%2FpmvX5octx6Rwr%2BYDpBdbRQxqwdq9NjuUJXFlSLARa9Pg6rlcj6s650Hr9f9GHIHpKkqLjmCGNCMqp51FwLYJuOBLMhajmAK9%2F0oyfXri0H1GDOTSCFW2%2BAoAkHRXx3H0dt6bgtVB4hST5xhqt%2BcXonG4dTtVMI3Xn70GOqUBWj0N6sdPZ7DI7gceIC7b9o%2BOxks5vlesbyEEFzm%2B34up9hS8oGlNZr76GnO8LccK0EGxxgnxhXYZNk6bNRcZE%2BxDm8nwZ5t3qVYpbrmW5fQBxi1gKumtV%2BrnGGcmBZELgJXcn6TTyWz6YuAFcdp3yuzrahKhFIfZND3yR6mEKgZH%2BgiIZa8jaXbbz%2FTHDqmb4lrm2AFuwhtpMfUSFNN0DA3mZtzb&X-Amz-Signature=108a95976eaa8987fcfdc08b0985145239cc8cb07ec346c413795c62272c5ec6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466223IY2B7%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3IST%2BKh%2F%2FBg0LCiYGGz39pxBLXjF3KEUlYXC7ldr%2B5AiEAikUwWmXpNLAyG8XtH0lC%2FKwh1Q%2Bj3V8JYdGn04WKfKsqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQdaus3SrJtP%2BwjoyrcA%2FWy8p%2BTJxVgwk7WV3Z9LWVZEinpDUy650e8sZ9V0IKeXIDr5%2FC%2B3FCoLthaeH1dpLtzoWm6UlD9pWttqNOTyNg6Dhv%2FMLd05lnbvqmqkwP8UNOtZnpvF8nMeH8KQdgaXxvndaHZjyUHMASecCN1iQdfwL7GoyjpxyNvPkDL6CSECa7umfjOUVeY4jYPYZKtZaviilBmjBWf1yw7NgRaXUt8Byaayk18CcPIa13U2RGgqmwxcYnINbO5JyrDJZM8HXANy5ia6fm6OfX8W8p3Vj5Nmj0rOisfWJvnaHi9ARPVUESX%2BW2wyqVPrfnSZuiSrbesuMvI23YgREWLdHwGNuHEhMhEz9oHQ8BeXFIhoyDGutDBENtcDGzPzceMwAP5EnfbboKdhmC9hhEPJhO7rNlL2f%2Fu3VfWTTsUQQvSU0H4MrBr1EKyyp1Kw2N0mY0Z%2FK7AwGJh%2Brc1m0K4V%2Bt8Auj8ebacSC1%2FpmvX5octx6Rwr%2BYDpBdbRQxqwdq9NjuUJXFlSLARa9Pg6rlcj6s650Hr9f9GHIHpKkqLjmCGNCMqp51FwLYJuOBLMhajmAK9%2F0oyfXri0H1GDOTSCFW2%2BAoAkHRXx3H0dt6bgtVB4hST5xhqt%2BcXonG4dTtVMI3Xn70GOqUBWj0N6sdPZ7DI7gceIC7b9o%2BOxks5vlesbyEEFzm%2B34up9hS8oGlNZr76GnO8LccK0EGxxgnxhXYZNk6bNRcZE%2BxDm8nwZ5t3qVYpbrmW5fQBxi1gKumtV%2BrnGGcmBZELgJXcn6TTyWz6YuAFcdp3yuzrahKhFIfZND3yR6mEKgZH%2BgiIZa8jaXbbz%2FTHDqmb4lrm2AFuwhtpMfUSFNN0DA3mZtzb&X-Amz-Signature=fc56c74071fefc242cf94ffbe07a3ad309cbadc166ebf584ac5cf0c82a547c83&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466223IY2B7%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3IST%2BKh%2F%2FBg0LCiYGGz39pxBLXjF3KEUlYXC7ldr%2B5AiEAikUwWmXpNLAyG8XtH0lC%2FKwh1Q%2Bj3V8JYdGn04WKfKsqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQdaus3SrJtP%2BwjoyrcA%2FWy8p%2BTJxVgwk7WV3Z9LWVZEinpDUy650e8sZ9V0IKeXIDr5%2FC%2B3FCoLthaeH1dpLtzoWm6UlD9pWttqNOTyNg6Dhv%2FMLd05lnbvqmqkwP8UNOtZnpvF8nMeH8KQdgaXxvndaHZjyUHMASecCN1iQdfwL7GoyjpxyNvPkDL6CSECa7umfjOUVeY4jYPYZKtZaviilBmjBWf1yw7NgRaXUt8Byaayk18CcPIa13U2RGgqmwxcYnINbO5JyrDJZM8HXANy5ia6fm6OfX8W8p3Vj5Nmj0rOisfWJvnaHi9ARPVUESX%2BW2wyqVPrfnSZuiSrbesuMvI23YgREWLdHwGNuHEhMhEz9oHQ8BeXFIhoyDGutDBENtcDGzPzceMwAP5EnfbboKdhmC9hhEPJhO7rNlL2f%2Fu3VfWTTsUQQvSU0H4MrBr1EKyyp1Kw2N0mY0Z%2FK7AwGJh%2Brc1m0K4V%2Bt8Auj8ebacSC1%2FpmvX5octx6Rwr%2BYDpBdbRQxqwdq9NjuUJXFlSLARa9Pg6rlcj6s650Hr9f9GHIHpKkqLjmCGNCMqp51FwLYJuOBLMhajmAK9%2F0oyfXri0H1GDOTSCFW2%2BAoAkHRXx3H0dt6bgtVB4hST5xhqt%2BcXonG4dTtVMI3Xn70GOqUBWj0N6sdPZ7DI7gceIC7b9o%2BOxks5vlesbyEEFzm%2B34up9hS8oGlNZr76GnO8LccK0EGxxgnxhXYZNk6bNRcZE%2BxDm8nwZ5t3qVYpbrmW5fQBxi1gKumtV%2BrnGGcmBZELgJXcn6TTyWz6YuAFcdp3yuzrahKhFIfZND3yR6mEKgZH%2BgiIZa8jaXbbz%2FTHDqmb4lrm2AFuwhtpMfUSFNN0DA3mZtzb&X-Amz-Signature=27f3b51561a3b3072b8e0926c163a06df0e689c2bd836fcdc3346e87b5eef4fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466223IY2B7%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA3IST%2BKh%2F%2FBg0LCiYGGz39pxBLXjF3KEUlYXC7ldr%2B5AiEAikUwWmXpNLAyG8XtH0lC%2FKwh1Q%2Bj3V8JYdGn04WKfKsqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQdaus3SrJtP%2BwjoyrcA%2FWy8p%2BTJxVgwk7WV3Z9LWVZEinpDUy650e8sZ9V0IKeXIDr5%2FC%2B3FCoLthaeH1dpLtzoWm6UlD9pWttqNOTyNg6Dhv%2FMLd05lnbvqmqkwP8UNOtZnpvF8nMeH8KQdgaXxvndaHZjyUHMASecCN1iQdfwL7GoyjpxyNvPkDL6CSECa7umfjOUVeY4jYPYZKtZaviilBmjBWf1yw7NgRaXUt8Byaayk18CcPIa13U2RGgqmwxcYnINbO5JyrDJZM8HXANy5ia6fm6OfX8W8p3Vj5Nmj0rOisfWJvnaHi9ARPVUESX%2BW2wyqVPrfnSZuiSrbesuMvI23YgREWLdHwGNuHEhMhEz9oHQ8BeXFIhoyDGutDBENtcDGzPzceMwAP5EnfbboKdhmC9hhEPJhO7rNlL2f%2Fu3VfWTTsUQQvSU0H4MrBr1EKyyp1Kw2N0mY0Z%2FK7AwGJh%2Brc1m0K4V%2Bt8Auj8ebacSC1%2FpmvX5octx6Rwr%2BYDpBdbRQxqwdq9NjuUJXFlSLARa9Pg6rlcj6s650Hr9f9GHIHpKkqLjmCGNCMqp51FwLYJuOBLMhajmAK9%2F0oyfXri0H1GDOTSCFW2%2BAoAkHRXx3H0dt6bgtVB4hST5xhqt%2BcXonG4dTtVMI3Xn70GOqUBWj0N6sdPZ7DI7gceIC7b9o%2BOxks5vlesbyEEFzm%2B34up9hS8oGlNZr76GnO8LccK0EGxxgnxhXYZNk6bNRcZE%2BxDm8nwZ5t3qVYpbrmW5fQBxi1gKumtV%2BrnGGcmBZELgJXcn6TTyWz6YuAFcdp3yuzrahKhFIfZND3yR6mEKgZH%2BgiIZa8jaXbbz%2FTHDqmb4lrm2AFuwhtpMfUSFNN0DA3mZtzb&X-Amz-Signature=8f9002351801c4f5cf7c72b3bd39394f9b8d5b9c3d320e3b5abe498bc62f31fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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


