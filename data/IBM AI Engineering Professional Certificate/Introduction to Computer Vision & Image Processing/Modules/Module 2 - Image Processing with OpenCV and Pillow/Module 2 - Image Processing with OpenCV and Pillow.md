

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4MRHI3D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBnNh0fUn6sSDDJux4CqgHWxRSQEXHlcnsoG1DjTMueHAiEA5P6RjbLagyHHFxkaS9aDeS1LF9prBmeEz6BrdEcecV0qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIc7dusYk30amSco7ircA5YJXfw5rwZ9T42QsVxSQmvwQiFxgANxLa4Dc0hP41Zo674khyNaoe5PwNKYmRoMK8q5939vpd6%2B5fb%2Fdnu5JiVTPrDIVpSWN9EUxanTL78Z85oa7%2FfDOcmNDz0yMVaHU61ZZujhdsA1oTsDViuFFjcvNPZi7WgzF5ch6VX0mFabaWuJKMHJ73FzSWVEd4ddzMc56vMxi5xdn9MseBZ%2Bh02jM3AKkFQ%2FgioXRtg2oy6%2B7Lz60Ia1ZJSa4eR0WvMmT27W9Y9A0q8zr9XI6yYeA4Y7aAeHJmZ%2BQ5BhOLhR8T0rnGMOSWMrusu3BP31xVYkfTS8wTu7F%2FONYdajY%2FCcdpD%2BTztiTi1eb%2F8h9UvGjBiOTe00xXTuHsQB00F7xJVSH96fux9znehacI1PJaRhRi%2FQ%2F46JxVSfb7bOdVadGnB73gMLHx0vvsaOccEth2USmLbjNFEidhaKiNZJUZHAYo62raCsj7mrTKEFDzyvUA0sLsXMdcEulCZMDFJBwLXEBuWp%2B%2BP0KCX3Py6loce44SZNol10%2Fygi3Zm63MMNWEPyB7Sfb0twK5Cfo4Y56CEAn7nwDODpfq9K3b1WkZqYpC%2FlkhkeMr5Jp7TjwbZtpQhacZJWPl8iv34CmHTEMLax%2BrwGOqUB9fJoUPuhwiKKK9iDegdT6WisLA4aQpR%2B1Xru6NvWxWiu0p5YDamihpWHkaBFrRVS1z6dvG%2FKlVBu3sPJIIVqCaM8rUJJDuaGFhJD0PqUc%2FB9C3j5P1gi%2Bkl9c6P9%2BvWRNIvn7u1JIH7UKCRA3RCe%2FDuZzQJvBY%2Bg4ZI%2FPZyHCMQBOrflCXussB91N96qbM%2Fi8gitLVsXL7DglzX1rGR5VX0OvuiE&X-Amz-Signature=7dc8d3a2aa525f8dc179211953cfae1ed0d7fbe1f1f781429ebd5c4ecb7a5cda&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5T4CQHE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtTN5qQKaEJlv%2BRLJzSWPi5Vqwb%2FEggjS8V9zstge1BwIhALlhGRSTI1X0341Kzxm3TdtjzIBCZVHyDC05W9G0BoXzKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYstqtEkHdGWmH7y4q3APwRt6BOoar4G3Rw%2BkjSqitPnaZqDiARHJpcyIlXtwjJ5quBX2kwu643k%2BNNuqNYvNP9zmhxJOMkqtMG8yqx%2BOovHvDM05B7kiZXpQJgQFW1EzJ7FaXNgX7JjdVu5afn%2BaVvJzJ848bFYplhVtYIv1XVQ4LHnbkxewO72XOSGOE%2FxWbhMd%2F5H87Oe1PvtW4%2F7h1IsYEhPajIusXqiPOmOPw2vRV9i69VdRjw29TKSY4QFZXPf8mv68Kjp%2B2md%2B2xqGQmMR%2B3aoVnxduK2ssOKVb8T3%2FykS4i%2BgXd6BCKZo1r7Edtg%2Fb9mj8HbW9f%2BKD7T9H%2FT%2B2hth%2FjHyRO5UT%2FYzfg%2BQMX87MBq8baPOb3ZpyoOOxYqe3AIUf8VPddD7XMtP5f%2FVwLyF%2Bq9EEfG0wH6UMOGXG1M5qo5f%2B55cpyO7IkGHr8fX8qTqVwJq3uofWIHJNA2gzK7S8tw5zFJdgIEZNaQS%2Fi%2BLEkHDis4N6EvU5aayfkoZtO%2BGtv61zan5n34Fq0%2B2DUSrokzEtWkDcfq9xI4fvnLcPYF3P4TxxBqYTpJ0PWu7erjBAMbC%2F27Zcge7xSpYrwXbAcGQoJzaoB8PrmpfG2qyXEIRialt1DSZQbCag0Pjbxq2lgL3GVTD1sPq8BjqkAXXAHSlvKr2tDfeZ10fITXDH7oPWcv3rnpnYStxy8ZceF9N6QrDu3pfzezzdLnp4cgcr3vLIZcLrDpQzI7s4VugVutVKthZBDkhUVSYDtiqJX7%2FjuPbGIxssxyjzWk8vOKag2oEzoHlGNUIR6Z35OsGGbiuutNfbjjb0P5Fc37hUsNLWBZQonaJ2kXOPYos7WOn3JTF5socPu1skq1kK0uuW%2BnG3&X-Amz-Signature=c611a843bafa86b23f182f41f5393c73d9618fc5e31918c556f5fded1206e942&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5T4CQHE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtTN5qQKaEJlv%2BRLJzSWPi5Vqwb%2FEggjS8V9zstge1BwIhALlhGRSTI1X0341Kzxm3TdtjzIBCZVHyDC05W9G0BoXzKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYstqtEkHdGWmH7y4q3APwRt6BOoar4G3Rw%2BkjSqitPnaZqDiARHJpcyIlXtwjJ5quBX2kwu643k%2BNNuqNYvNP9zmhxJOMkqtMG8yqx%2BOovHvDM05B7kiZXpQJgQFW1EzJ7FaXNgX7JjdVu5afn%2BaVvJzJ848bFYplhVtYIv1XVQ4LHnbkxewO72XOSGOE%2FxWbhMd%2F5H87Oe1PvtW4%2F7h1IsYEhPajIusXqiPOmOPw2vRV9i69VdRjw29TKSY4QFZXPf8mv68Kjp%2B2md%2B2xqGQmMR%2B3aoVnxduK2ssOKVb8T3%2FykS4i%2BgXd6BCKZo1r7Edtg%2Fb9mj8HbW9f%2BKD7T9H%2FT%2B2hth%2FjHyRO5UT%2FYzfg%2BQMX87MBq8baPOb3ZpyoOOxYqe3AIUf8VPddD7XMtP5f%2FVwLyF%2Bq9EEfG0wH6UMOGXG1M5qo5f%2B55cpyO7IkGHr8fX8qTqVwJq3uofWIHJNA2gzK7S8tw5zFJdgIEZNaQS%2Fi%2BLEkHDis4N6EvU5aayfkoZtO%2BGtv61zan5n34Fq0%2B2DUSrokzEtWkDcfq9xI4fvnLcPYF3P4TxxBqYTpJ0PWu7erjBAMbC%2F27Zcge7xSpYrwXbAcGQoJzaoB8PrmpfG2qyXEIRialt1DSZQbCag0Pjbxq2lgL3GVTD1sPq8BjqkAXXAHSlvKr2tDfeZ10fITXDH7oPWcv3rnpnYStxy8ZceF9N6QrDu3pfzezzdLnp4cgcr3vLIZcLrDpQzI7s4VugVutVKthZBDkhUVSYDtiqJX7%2FjuPbGIxssxyjzWk8vOKag2oEzoHlGNUIR6Z35OsGGbiuutNfbjjb0P5Fc37hUsNLWBZQonaJ2kXOPYos7WOn3JTF5socPu1skq1kK0uuW%2BnG3&X-Amz-Signature=32e259e28d62c5a0991256532a239b3393cef71e5fba55af66e579106cf2a8a7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5T4CQHE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtTN5qQKaEJlv%2BRLJzSWPi5Vqwb%2FEggjS8V9zstge1BwIhALlhGRSTI1X0341Kzxm3TdtjzIBCZVHyDC05W9G0BoXzKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYstqtEkHdGWmH7y4q3APwRt6BOoar4G3Rw%2BkjSqitPnaZqDiARHJpcyIlXtwjJ5quBX2kwu643k%2BNNuqNYvNP9zmhxJOMkqtMG8yqx%2BOovHvDM05B7kiZXpQJgQFW1EzJ7FaXNgX7JjdVu5afn%2BaVvJzJ848bFYplhVtYIv1XVQ4LHnbkxewO72XOSGOE%2FxWbhMd%2F5H87Oe1PvtW4%2F7h1IsYEhPajIusXqiPOmOPw2vRV9i69VdRjw29TKSY4QFZXPf8mv68Kjp%2B2md%2B2xqGQmMR%2B3aoVnxduK2ssOKVb8T3%2FykS4i%2BgXd6BCKZo1r7Edtg%2Fb9mj8HbW9f%2BKD7T9H%2FT%2B2hth%2FjHyRO5UT%2FYzfg%2BQMX87MBq8baPOb3ZpyoOOxYqe3AIUf8VPddD7XMtP5f%2FVwLyF%2Bq9EEfG0wH6UMOGXG1M5qo5f%2B55cpyO7IkGHr8fX8qTqVwJq3uofWIHJNA2gzK7S8tw5zFJdgIEZNaQS%2Fi%2BLEkHDis4N6EvU5aayfkoZtO%2BGtv61zan5n34Fq0%2B2DUSrokzEtWkDcfq9xI4fvnLcPYF3P4TxxBqYTpJ0PWu7erjBAMbC%2F27Zcge7xSpYrwXbAcGQoJzaoB8PrmpfG2qyXEIRialt1DSZQbCag0Pjbxq2lgL3GVTD1sPq8BjqkAXXAHSlvKr2tDfeZ10fITXDH7oPWcv3rnpnYStxy8ZceF9N6QrDu3pfzezzdLnp4cgcr3vLIZcLrDpQzI7s4VugVutVKthZBDkhUVSYDtiqJX7%2FjuPbGIxssxyjzWk8vOKag2oEzoHlGNUIR6Z35OsGGbiuutNfbjjb0P5Fc37hUsNLWBZQonaJ2kXOPYos7WOn3JTF5socPu1skq1kK0uuW%2BnG3&X-Amz-Signature=84c63da556407830fdc405667a83bfd19972158979d7d750d20b7c1262c529c6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5T4CQHE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtTN5qQKaEJlv%2BRLJzSWPi5Vqwb%2FEggjS8V9zstge1BwIhALlhGRSTI1X0341Kzxm3TdtjzIBCZVHyDC05W9G0BoXzKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYstqtEkHdGWmH7y4q3APwRt6BOoar4G3Rw%2BkjSqitPnaZqDiARHJpcyIlXtwjJ5quBX2kwu643k%2BNNuqNYvNP9zmhxJOMkqtMG8yqx%2BOovHvDM05B7kiZXpQJgQFW1EzJ7FaXNgX7JjdVu5afn%2BaVvJzJ848bFYplhVtYIv1XVQ4LHnbkxewO72XOSGOE%2FxWbhMd%2F5H87Oe1PvtW4%2F7h1IsYEhPajIusXqiPOmOPw2vRV9i69VdRjw29TKSY4QFZXPf8mv68Kjp%2B2md%2B2xqGQmMR%2B3aoVnxduK2ssOKVb8T3%2FykS4i%2BgXd6BCKZo1r7Edtg%2Fb9mj8HbW9f%2BKD7T9H%2FT%2B2hth%2FjHyRO5UT%2FYzfg%2BQMX87MBq8baPOb3ZpyoOOxYqe3AIUf8VPddD7XMtP5f%2FVwLyF%2Bq9EEfG0wH6UMOGXG1M5qo5f%2B55cpyO7IkGHr8fX8qTqVwJq3uofWIHJNA2gzK7S8tw5zFJdgIEZNaQS%2Fi%2BLEkHDis4N6EvU5aayfkoZtO%2BGtv61zan5n34Fq0%2B2DUSrokzEtWkDcfq9xI4fvnLcPYF3P4TxxBqYTpJ0PWu7erjBAMbC%2F27Zcge7xSpYrwXbAcGQoJzaoB8PrmpfG2qyXEIRialt1DSZQbCag0Pjbxq2lgL3GVTD1sPq8BjqkAXXAHSlvKr2tDfeZ10fITXDH7oPWcv3rnpnYStxy8ZceF9N6QrDu3pfzezzdLnp4cgcr3vLIZcLrDpQzI7s4VugVutVKthZBDkhUVSYDtiqJX7%2FjuPbGIxssxyjzWk8vOKag2oEzoHlGNUIR6Z35OsGGbiuutNfbjjb0P5Fc37hUsNLWBZQonaJ2kXOPYos7WOn3JTF5socPu1skq1kK0uuW%2BnG3&X-Amz-Signature=ee00c41f68dde53dba48d57c21f525abc106528c2a9319117a6a5ad9e9e88acb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5T4CQHE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtTN5qQKaEJlv%2BRLJzSWPi5Vqwb%2FEggjS8V9zstge1BwIhALlhGRSTI1X0341Kzxm3TdtjzIBCZVHyDC05W9G0BoXzKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYstqtEkHdGWmH7y4q3APwRt6BOoar4G3Rw%2BkjSqitPnaZqDiARHJpcyIlXtwjJ5quBX2kwu643k%2BNNuqNYvNP9zmhxJOMkqtMG8yqx%2BOovHvDM05B7kiZXpQJgQFW1EzJ7FaXNgX7JjdVu5afn%2BaVvJzJ848bFYplhVtYIv1XVQ4LHnbkxewO72XOSGOE%2FxWbhMd%2F5H87Oe1PvtW4%2F7h1IsYEhPajIusXqiPOmOPw2vRV9i69VdRjw29TKSY4QFZXPf8mv68Kjp%2B2md%2B2xqGQmMR%2B3aoVnxduK2ssOKVb8T3%2FykS4i%2BgXd6BCKZo1r7Edtg%2Fb9mj8HbW9f%2BKD7T9H%2FT%2B2hth%2FjHyRO5UT%2FYzfg%2BQMX87MBq8baPOb3ZpyoOOxYqe3AIUf8VPddD7XMtP5f%2FVwLyF%2Bq9EEfG0wH6UMOGXG1M5qo5f%2B55cpyO7IkGHr8fX8qTqVwJq3uofWIHJNA2gzK7S8tw5zFJdgIEZNaQS%2Fi%2BLEkHDis4N6EvU5aayfkoZtO%2BGtv61zan5n34Fq0%2B2DUSrokzEtWkDcfq9xI4fvnLcPYF3P4TxxBqYTpJ0PWu7erjBAMbC%2F27Zcge7xSpYrwXbAcGQoJzaoB8PrmpfG2qyXEIRialt1DSZQbCag0Pjbxq2lgL3GVTD1sPq8BjqkAXXAHSlvKr2tDfeZ10fITXDH7oPWcv3rnpnYStxy8ZceF9N6QrDu3pfzezzdLnp4cgcr3vLIZcLrDpQzI7s4VugVutVKthZBDkhUVSYDtiqJX7%2FjuPbGIxssxyjzWk8vOKag2oEzoHlGNUIR6Z35OsGGbiuutNfbjjb0P5Fc37hUsNLWBZQonaJ2kXOPYos7WOn3JTF5socPu1skq1kK0uuW%2BnG3&X-Amz-Signature=4c050c20c43fcd15ac53952d9973c51cdf721fe898cc36909dc546a8b23c72b1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4MRHI3D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBnNh0fUn6sSDDJux4CqgHWxRSQEXHlcnsoG1DjTMueHAiEA5P6RjbLagyHHFxkaS9aDeS1LF9prBmeEz6BrdEcecV0qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIc7dusYk30amSco7ircA5YJXfw5rwZ9T42QsVxSQmvwQiFxgANxLa4Dc0hP41Zo674khyNaoe5PwNKYmRoMK8q5939vpd6%2B5fb%2Fdnu5JiVTPrDIVpSWN9EUxanTL78Z85oa7%2FfDOcmNDz0yMVaHU61ZZujhdsA1oTsDViuFFjcvNPZi7WgzF5ch6VX0mFabaWuJKMHJ73FzSWVEd4ddzMc56vMxi5xdn9MseBZ%2Bh02jM3AKkFQ%2FgioXRtg2oy6%2B7Lz60Ia1ZJSa4eR0WvMmT27W9Y9A0q8zr9XI6yYeA4Y7aAeHJmZ%2BQ5BhOLhR8T0rnGMOSWMrusu3BP31xVYkfTS8wTu7F%2FONYdajY%2FCcdpD%2BTztiTi1eb%2F8h9UvGjBiOTe00xXTuHsQB00F7xJVSH96fux9znehacI1PJaRhRi%2FQ%2F46JxVSfb7bOdVadGnB73gMLHx0vvsaOccEth2USmLbjNFEidhaKiNZJUZHAYo62raCsj7mrTKEFDzyvUA0sLsXMdcEulCZMDFJBwLXEBuWp%2B%2BP0KCX3Py6loce44SZNol10%2Fygi3Zm63MMNWEPyB7Sfb0twK5Cfo4Y56CEAn7nwDODpfq9K3b1WkZqYpC%2FlkhkeMr5Jp7TjwbZtpQhacZJWPl8iv34CmHTEMLax%2BrwGOqUB9fJoUPuhwiKKK9iDegdT6WisLA4aQpR%2B1Xru6NvWxWiu0p5YDamihpWHkaBFrRVS1z6dvG%2FKlVBu3sPJIIVqCaM8rUJJDuaGFhJD0PqUc%2FB9C3j5P1gi%2Bkl9c6P9%2BvWRNIvn7u1JIH7UKCRA3RCe%2FDuZzQJvBY%2Bg4ZI%2FPZyHCMQBOrflCXussB91N96qbM%2Fi8gitLVsXL7DglzX1rGR5VX0OvuiE&X-Amz-Signature=3c74061981332a5ec0e26934985d73e668912599c2b8aa3132bdb847d6998bdd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4MRHI3D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBnNh0fUn6sSDDJux4CqgHWxRSQEXHlcnsoG1DjTMueHAiEA5P6RjbLagyHHFxkaS9aDeS1LF9prBmeEz6BrdEcecV0qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIc7dusYk30amSco7ircA5YJXfw5rwZ9T42QsVxSQmvwQiFxgANxLa4Dc0hP41Zo674khyNaoe5PwNKYmRoMK8q5939vpd6%2B5fb%2Fdnu5JiVTPrDIVpSWN9EUxanTL78Z85oa7%2FfDOcmNDz0yMVaHU61ZZujhdsA1oTsDViuFFjcvNPZi7WgzF5ch6VX0mFabaWuJKMHJ73FzSWVEd4ddzMc56vMxi5xdn9MseBZ%2Bh02jM3AKkFQ%2FgioXRtg2oy6%2B7Lz60Ia1ZJSa4eR0WvMmT27W9Y9A0q8zr9XI6yYeA4Y7aAeHJmZ%2BQ5BhOLhR8T0rnGMOSWMrusu3BP31xVYkfTS8wTu7F%2FONYdajY%2FCcdpD%2BTztiTi1eb%2F8h9UvGjBiOTe00xXTuHsQB00F7xJVSH96fux9znehacI1PJaRhRi%2FQ%2F46JxVSfb7bOdVadGnB73gMLHx0vvsaOccEth2USmLbjNFEidhaKiNZJUZHAYo62raCsj7mrTKEFDzyvUA0sLsXMdcEulCZMDFJBwLXEBuWp%2B%2BP0KCX3Py6loce44SZNol10%2Fygi3Zm63MMNWEPyB7Sfb0twK5Cfo4Y56CEAn7nwDODpfq9K3b1WkZqYpC%2FlkhkeMr5Jp7TjwbZtpQhacZJWPl8iv34CmHTEMLax%2BrwGOqUB9fJoUPuhwiKKK9iDegdT6WisLA4aQpR%2B1Xru6NvWxWiu0p5YDamihpWHkaBFrRVS1z6dvG%2FKlVBu3sPJIIVqCaM8rUJJDuaGFhJD0PqUc%2FB9C3j5P1gi%2Bkl9c6P9%2BvWRNIvn7u1JIH7UKCRA3RCe%2FDuZzQJvBY%2Bg4ZI%2FPZyHCMQBOrflCXussB91N96qbM%2Fi8gitLVsXL7DglzX1rGR5VX0OvuiE&X-Amz-Signature=b4f1d96b5b4e7991fcbfe6439c4335e6bbf1a1250c4c1ae79452ca7a3e2d8357&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4MRHI3D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBnNh0fUn6sSDDJux4CqgHWxRSQEXHlcnsoG1DjTMueHAiEA5P6RjbLagyHHFxkaS9aDeS1LF9prBmeEz6BrdEcecV0qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIc7dusYk30amSco7ircA5YJXfw5rwZ9T42QsVxSQmvwQiFxgANxLa4Dc0hP41Zo674khyNaoe5PwNKYmRoMK8q5939vpd6%2B5fb%2Fdnu5JiVTPrDIVpSWN9EUxanTL78Z85oa7%2FfDOcmNDz0yMVaHU61ZZujhdsA1oTsDViuFFjcvNPZi7WgzF5ch6VX0mFabaWuJKMHJ73FzSWVEd4ddzMc56vMxi5xdn9MseBZ%2Bh02jM3AKkFQ%2FgioXRtg2oy6%2B7Lz60Ia1ZJSa4eR0WvMmT27W9Y9A0q8zr9XI6yYeA4Y7aAeHJmZ%2BQ5BhOLhR8T0rnGMOSWMrusu3BP31xVYkfTS8wTu7F%2FONYdajY%2FCcdpD%2BTztiTi1eb%2F8h9UvGjBiOTe00xXTuHsQB00F7xJVSH96fux9znehacI1PJaRhRi%2FQ%2F46JxVSfb7bOdVadGnB73gMLHx0vvsaOccEth2USmLbjNFEidhaKiNZJUZHAYo62raCsj7mrTKEFDzyvUA0sLsXMdcEulCZMDFJBwLXEBuWp%2B%2BP0KCX3Py6loce44SZNol10%2Fygi3Zm63MMNWEPyB7Sfb0twK5Cfo4Y56CEAn7nwDODpfq9K3b1WkZqYpC%2FlkhkeMr5Jp7TjwbZtpQhacZJWPl8iv34CmHTEMLax%2BrwGOqUB9fJoUPuhwiKKK9iDegdT6WisLA4aQpR%2B1Xru6NvWxWiu0p5YDamihpWHkaBFrRVS1z6dvG%2FKlVBu3sPJIIVqCaM8rUJJDuaGFhJD0PqUc%2FB9C3j5P1gi%2Bkl9c6P9%2BvWRNIvn7u1JIH7UKCRA3RCe%2FDuZzQJvBY%2Bg4ZI%2FPZyHCMQBOrflCXussB91N96qbM%2Fi8gitLVsXL7DglzX1rGR5VX0OvuiE&X-Amz-Signature=84a114b4c8c2ea0f47e7522440263b3698d42f791a911a66bc1a025f53c6541a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4MRHI3D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBnNh0fUn6sSDDJux4CqgHWxRSQEXHlcnsoG1DjTMueHAiEA5P6RjbLagyHHFxkaS9aDeS1LF9prBmeEz6BrdEcecV0qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIc7dusYk30amSco7ircA5YJXfw5rwZ9T42QsVxSQmvwQiFxgANxLa4Dc0hP41Zo674khyNaoe5PwNKYmRoMK8q5939vpd6%2B5fb%2Fdnu5JiVTPrDIVpSWN9EUxanTL78Z85oa7%2FfDOcmNDz0yMVaHU61ZZujhdsA1oTsDViuFFjcvNPZi7WgzF5ch6VX0mFabaWuJKMHJ73FzSWVEd4ddzMc56vMxi5xdn9MseBZ%2Bh02jM3AKkFQ%2FgioXRtg2oy6%2B7Lz60Ia1ZJSa4eR0WvMmT27W9Y9A0q8zr9XI6yYeA4Y7aAeHJmZ%2BQ5BhOLhR8T0rnGMOSWMrusu3BP31xVYkfTS8wTu7F%2FONYdajY%2FCcdpD%2BTztiTi1eb%2F8h9UvGjBiOTe00xXTuHsQB00F7xJVSH96fux9znehacI1PJaRhRi%2FQ%2F46JxVSfb7bOdVadGnB73gMLHx0vvsaOccEth2USmLbjNFEidhaKiNZJUZHAYo62raCsj7mrTKEFDzyvUA0sLsXMdcEulCZMDFJBwLXEBuWp%2B%2BP0KCX3Py6loce44SZNol10%2Fygi3Zm63MMNWEPyB7Sfb0twK5Cfo4Y56CEAn7nwDODpfq9K3b1WkZqYpC%2FlkhkeMr5Jp7TjwbZtpQhacZJWPl8iv34CmHTEMLax%2BrwGOqUB9fJoUPuhwiKKK9iDegdT6WisLA4aQpR%2B1Xru6NvWxWiu0p5YDamihpWHkaBFrRVS1z6dvG%2FKlVBu3sPJIIVqCaM8rUJJDuaGFhJD0PqUc%2FB9C3j5P1gi%2Bkl9c6P9%2BvWRNIvn7u1JIH7UKCRA3RCe%2FDuZzQJvBY%2Bg4ZI%2FPZyHCMQBOrflCXussB91N96qbM%2Fi8gitLVsXL7DglzX1rGR5VX0OvuiE&X-Amz-Signature=1be48b14dd59e554b4acdd7cb4c2e96240f8adfdad1a8a612136b61a21627c7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4MRHI3D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBnNh0fUn6sSDDJux4CqgHWxRSQEXHlcnsoG1DjTMueHAiEA5P6RjbLagyHHFxkaS9aDeS1LF9prBmeEz6BrdEcecV0qiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIc7dusYk30amSco7ircA5YJXfw5rwZ9T42QsVxSQmvwQiFxgANxLa4Dc0hP41Zo674khyNaoe5PwNKYmRoMK8q5939vpd6%2B5fb%2Fdnu5JiVTPrDIVpSWN9EUxanTL78Z85oa7%2FfDOcmNDz0yMVaHU61ZZujhdsA1oTsDViuFFjcvNPZi7WgzF5ch6VX0mFabaWuJKMHJ73FzSWVEd4ddzMc56vMxi5xdn9MseBZ%2Bh02jM3AKkFQ%2FgioXRtg2oy6%2B7Lz60Ia1ZJSa4eR0WvMmT27W9Y9A0q8zr9XI6yYeA4Y7aAeHJmZ%2BQ5BhOLhR8T0rnGMOSWMrusu3BP31xVYkfTS8wTu7F%2FONYdajY%2FCcdpD%2BTztiTi1eb%2F8h9UvGjBiOTe00xXTuHsQB00F7xJVSH96fux9znehacI1PJaRhRi%2FQ%2F46JxVSfb7bOdVadGnB73gMLHx0vvsaOccEth2USmLbjNFEidhaKiNZJUZHAYo62raCsj7mrTKEFDzyvUA0sLsXMdcEulCZMDFJBwLXEBuWp%2B%2BP0KCX3Py6loce44SZNol10%2Fygi3Zm63MMNWEPyB7Sfb0twK5Cfo4Y56CEAn7nwDODpfq9K3b1WkZqYpC%2FlkhkeMr5Jp7TjwbZtpQhacZJWPl8iv34CmHTEMLax%2BrwGOqUB9fJoUPuhwiKKK9iDegdT6WisLA4aQpR%2B1Xru6NvWxWiu0p5YDamihpWHkaBFrRVS1z6dvG%2FKlVBu3sPJIIVqCaM8rUJJDuaGFhJD0PqUc%2FB9C3j5P1gi%2Bkl9c6P9%2BvWRNIvn7u1JIH7UKCRA3RCe%2FDuZzQJvBY%2Bg4ZI%2FPZyHCMQBOrflCXussB91N96qbM%2Fi8gitLVsXL7DglzX1rGR5VX0OvuiE&X-Amz-Signature=75fc7a3b78c708ebe6343a681d5d492276763c0ada59f395bfc51a43e76cad44&X-Amz-SignedHeaders=host&x-id=GetObject)
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


