

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625VDHFTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1Y3NieagsYwYgv9iTvQse6wuOYRHzn1d4Mf6x3DoeWAiEA7Wswirq9U4313IsBot5OJy2GmW66ksXGlx3R5lewt00qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELNvadEMJl17ZXQLircAyk6vHdUldvvJmDRQh8wNnjTueirNqwz%2BvC6MxtA43FX0BJojYym8%2F0WenFKy7RCi7bHt7YeBHCcna7EmOeHWrYWzwm%2B2AXXc0lHmskODwUnBho4q6foQSVnhCPD5zV96q0M7%2FzmC6MDTmhnC4ZeUk%2FESIxTOUoIVM1xsY8nvD7GRLTxUzmoiJTOygiyq9qEotRJZh1AlJI7apfIpL3di3MC%2FGqHkfb19XEFsInuTJ2gfKQjazJ7nepFQV78PtSHFjIx2vjD1gxMS6tk0C2tIu7k5uZsZHj3%2BbB%2F2Il8VpvZHel%2FFV7zrtqXH%2FhYzHJSqz2XDYFFv5yeVtiY1fZrXSXoQRm5lAuLSUwfEI6SWH3wCaApszJs7R0dkO7FI0d3P6YvYUoSxvexNAzqtlP11EENYFvVE0VrXSqze3q%2B8ykRgwDbpZRHsLT%2FQmhw3aROFy9CHhc0DjxqjfLGuVhpPVBHw2LOkpwElBSxEzd1WCPPMenHM6X9J3aLOMgo%2B0jQPW7Qm0%2Bk9hIb%2Fu%2F6zpXdOkZu1ahfe15Hsn64KC9QEfzmhAuSbE3JW6E1nWAqYdvGefkox99JnN7mVmsZXxtnCtGTT8u59%2B%2FJsm1lxzG%2B44j5ZrTO%2F1oL2OrvGDs6MODi%2FrwGOqUBHCC57gmfySHVxoId%2FTWIzJyALUYjsCq4jlPTUoR%2BHCIuvdj%2BWocbeWMnJN78N55sh9esypq4g0yXziHCQke3dxluTU9QG9cRh2gRHnyEIhe%2BNZAZ3m%2FWTJiAvwVrLDlqSjtyGCz1wcHNytvmp3hs4c9HoUNTokXiYpOZvaOIAlCQfNf30rE7GXyiBsyAo40w12Bn%2BqSIaYo7n1PgMouV%2BlKJc5is&X-Amz-Signature=f32dffd3f9a969cef2e386067d8f4b6abbc92a42fac93b02c4154e4672479ee2&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IWZTJSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEgQtbbmXV3pE%2BszWdsZSTJ12S4UFNYWxm74n46DcyOKAiB%2BIvrKpO9O7bkUXPWEMh5CEuCY%2BCLWS8W3PLjmeD9YEyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeikETGjKW2rvpU8kKtwDRls4Sv4qhLXKMEn9lYBLhPD8NyfQ4fssZVQfpgTZJhHIzHdODyMGX2tZAPNMKLOIxXgKYOAm604CLsnzLDrvTLB%2F3j7RDBnE9rMbEXp5w8YXH2k3XW5ufFXGGno8Oi22u5%2FXiQYpQb9Haz4G7n2XSgEJRTsieszfbhYmykFfLfXGSBFx%2Fa1YYurMpd4i5tZDtZiANd5g8BSke7pfJdPlXF7Jfj2myEOK7VL2EQ9bIHDtYD4YVzrX9%2BRyRfzWUvz3QpxfLVyR8bnALlyIy%2FIzNTKyM4FCM6VhgUN6YAbfj1p8oqFfmrFDvvh55TwH8VNsv2NO3GxjPtPNbI3X6tgaGz%2BqT4MkRSmIiBb8hi8dEjAtTMKdQB6gJRUOUIDUXPPE5MP%2FFHSBEzsd%2B3Uptg307Rf1hMSnEDvqAXuuIov2AQPhEftaDP0T7MFj7Fo8PuOOAF7%2BaDnq8nkp2XjpYhXvDhOo6wkqrv1m73OTdl4seyEvZGy4z9d1S3ebDuEc8zvZtUgg6kBLlTsa1Pu3azu9QQ24bOzcqCxP7FxfwbPLW%2BjbG1YIEZCDooQGrtcX1uyeRujLeCdO2TMuyG6p%2FENsexC3UiDT7WCPYYYaerdoniHT7460Z6xqwcRp8fUw4tf%2BvAY6pgF4r4%2BwuNbyTZ6sGHGjmsJ5v5i%2BvyUbdj%2FbwrqNJamHcGpv5jm9FfXyuqK8VoHp7BOp92ezIWc%2BQ7SaT%2BS0I0nTskCiBKZ6H9hfEnyERtV23TmFMZMD50t0tZIMOYoLvOn34ps%2BhaI37pLSIQ0IPCJB9Au3pK309tZza7FFrftzQc2aj7MdB9a2qK%2BLDhcjcpvErPmzYdf4b0w9Ou0xK5fr1MEJpiW8&X-Amz-Signature=bbd0e16213245c9cf4b3f681dc63333b5d4cfbd918fe2230827d86d33119f93b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IWZTJSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEgQtbbmXV3pE%2BszWdsZSTJ12S4UFNYWxm74n46DcyOKAiB%2BIvrKpO9O7bkUXPWEMh5CEuCY%2BCLWS8W3PLjmeD9YEyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeikETGjKW2rvpU8kKtwDRls4Sv4qhLXKMEn9lYBLhPD8NyfQ4fssZVQfpgTZJhHIzHdODyMGX2tZAPNMKLOIxXgKYOAm604CLsnzLDrvTLB%2F3j7RDBnE9rMbEXp5w8YXH2k3XW5ufFXGGno8Oi22u5%2FXiQYpQb9Haz4G7n2XSgEJRTsieszfbhYmykFfLfXGSBFx%2Fa1YYurMpd4i5tZDtZiANd5g8BSke7pfJdPlXF7Jfj2myEOK7VL2EQ9bIHDtYD4YVzrX9%2BRyRfzWUvz3QpxfLVyR8bnALlyIy%2FIzNTKyM4FCM6VhgUN6YAbfj1p8oqFfmrFDvvh55TwH8VNsv2NO3GxjPtPNbI3X6tgaGz%2BqT4MkRSmIiBb8hi8dEjAtTMKdQB6gJRUOUIDUXPPE5MP%2FFHSBEzsd%2B3Uptg307Rf1hMSnEDvqAXuuIov2AQPhEftaDP0T7MFj7Fo8PuOOAF7%2BaDnq8nkp2XjpYhXvDhOo6wkqrv1m73OTdl4seyEvZGy4z9d1S3ebDuEc8zvZtUgg6kBLlTsa1Pu3azu9QQ24bOzcqCxP7FxfwbPLW%2BjbG1YIEZCDooQGrtcX1uyeRujLeCdO2TMuyG6p%2FENsexC3UiDT7WCPYYYaerdoniHT7460Z6xqwcRp8fUw4tf%2BvAY6pgF4r4%2BwuNbyTZ6sGHGjmsJ5v5i%2BvyUbdj%2FbwrqNJamHcGpv5jm9FfXyuqK8VoHp7BOp92ezIWc%2BQ7SaT%2BS0I0nTskCiBKZ6H9hfEnyERtV23TmFMZMD50t0tZIMOYoLvOn34ps%2BhaI37pLSIQ0IPCJB9Au3pK309tZza7FFrftzQc2aj7MdB9a2qK%2BLDhcjcpvErPmzYdf4b0w9Ou0xK5fr1MEJpiW8&X-Amz-Signature=8010d5a6917af10e0b4cc05b774972d5f185d273039a46011b7ec5bdd26e92a4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IWZTJSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEgQtbbmXV3pE%2BszWdsZSTJ12S4UFNYWxm74n46DcyOKAiB%2BIvrKpO9O7bkUXPWEMh5CEuCY%2BCLWS8W3PLjmeD9YEyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeikETGjKW2rvpU8kKtwDRls4Sv4qhLXKMEn9lYBLhPD8NyfQ4fssZVQfpgTZJhHIzHdODyMGX2tZAPNMKLOIxXgKYOAm604CLsnzLDrvTLB%2F3j7RDBnE9rMbEXp5w8YXH2k3XW5ufFXGGno8Oi22u5%2FXiQYpQb9Haz4G7n2XSgEJRTsieszfbhYmykFfLfXGSBFx%2Fa1YYurMpd4i5tZDtZiANd5g8BSke7pfJdPlXF7Jfj2myEOK7VL2EQ9bIHDtYD4YVzrX9%2BRyRfzWUvz3QpxfLVyR8bnALlyIy%2FIzNTKyM4FCM6VhgUN6YAbfj1p8oqFfmrFDvvh55TwH8VNsv2NO3GxjPtPNbI3X6tgaGz%2BqT4MkRSmIiBb8hi8dEjAtTMKdQB6gJRUOUIDUXPPE5MP%2FFHSBEzsd%2B3Uptg307Rf1hMSnEDvqAXuuIov2AQPhEftaDP0T7MFj7Fo8PuOOAF7%2BaDnq8nkp2XjpYhXvDhOo6wkqrv1m73OTdl4seyEvZGy4z9d1S3ebDuEc8zvZtUgg6kBLlTsa1Pu3azu9QQ24bOzcqCxP7FxfwbPLW%2BjbG1YIEZCDooQGrtcX1uyeRujLeCdO2TMuyG6p%2FENsexC3UiDT7WCPYYYaerdoniHT7460Z6xqwcRp8fUw4tf%2BvAY6pgF4r4%2BwuNbyTZ6sGHGjmsJ5v5i%2BvyUbdj%2FbwrqNJamHcGpv5jm9FfXyuqK8VoHp7BOp92ezIWc%2BQ7SaT%2BS0I0nTskCiBKZ6H9hfEnyERtV23TmFMZMD50t0tZIMOYoLvOn34ps%2BhaI37pLSIQ0IPCJB9Au3pK309tZza7FFrftzQc2aj7MdB9a2qK%2BLDhcjcpvErPmzYdf4b0w9Ou0xK5fr1MEJpiW8&X-Amz-Signature=8df68787b6f127b8f85266e4d360033e1ce97e4efc4802ef6e9ef8ce1d5d731d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IWZTJSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEgQtbbmXV3pE%2BszWdsZSTJ12S4UFNYWxm74n46DcyOKAiB%2BIvrKpO9O7bkUXPWEMh5CEuCY%2BCLWS8W3PLjmeD9YEyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeikETGjKW2rvpU8kKtwDRls4Sv4qhLXKMEn9lYBLhPD8NyfQ4fssZVQfpgTZJhHIzHdODyMGX2tZAPNMKLOIxXgKYOAm604CLsnzLDrvTLB%2F3j7RDBnE9rMbEXp5w8YXH2k3XW5ufFXGGno8Oi22u5%2FXiQYpQb9Haz4G7n2XSgEJRTsieszfbhYmykFfLfXGSBFx%2Fa1YYurMpd4i5tZDtZiANd5g8BSke7pfJdPlXF7Jfj2myEOK7VL2EQ9bIHDtYD4YVzrX9%2BRyRfzWUvz3QpxfLVyR8bnALlyIy%2FIzNTKyM4FCM6VhgUN6YAbfj1p8oqFfmrFDvvh55TwH8VNsv2NO3GxjPtPNbI3X6tgaGz%2BqT4MkRSmIiBb8hi8dEjAtTMKdQB6gJRUOUIDUXPPE5MP%2FFHSBEzsd%2B3Uptg307Rf1hMSnEDvqAXuuIov2AQPhEftaDP0T7MFj7Fo8PuOOAF7%2BaDnq8nkp2XjpYhXvDhOo6wkqrv1m73OTdl4seyEvZGy4z9d1S3ebDuEc8zvZtUgg6kBLlTsa1Pu3azu9QQ24bOzcqCxP7FxfwbPLW%2BjbG1YIEZCDooQGrtcX1uyeRujLeCdO2TMuyG6p%2FENsexC3UiDT7WCPYYYaerdoniHT7460Z6xqwcRp8fUw4tf%2BvAY6pgF4r4%2BwuNbyTZ6sGHGjmsJ5v5i%2BvyUbdj%2FbwrqNJamHcGpv5jm9FfXyuqK8VoHp7BOp92ezIWc%2BQ7SaT%2BS0I0nTskCiBKZ6H9hfEnyERtV23TmFMZMD50t0tZIMOYoLvOn34ps%2BhaI37pLSIQ0IPCJB9Au3pK309tZza7FFrftzQc2aj7MdB9a2qK%2BLDhcjcpvErPmzYdf4b0w9Ou0xK5fr1MEJpiW8&X-Amz-Signature=c08053e2d189ae2bde3910c5797002ca9ee838938c0c360d7fce384853f5e9fb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IWZTJSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEgQtbbmXV3pE%2BszWdsZSTJ12S4UFNYWxm74n46DcyOKAiB%2BIvrKpO9O7bkUXPWEMh5CEuCY%2BCLWS8W3PLjmeD9YEyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeikETGjKW2rvpU8kKtwDRls4Sv4qhLXKMEn9lYBLhPD8NyfQ4fssZVQfpgTZJhHIzHdODyMGX2tZAPNMKLOIxXgKYOAm604CLsnzLDrvTLB%2F3j7RDBnE9rMbEXp5w8YXH2k3XW5ufFXGGno8Oi22u5%2FXiQYpQb9Haz4G7n2XSgEJRTsieszfbhYmykFfLfXGSBFx%2Fa1YYurMpd4i5tZDtZiANd5g8BSke7pfJdPlXF7Jfj2myEOK7VL2EQ9bIHDtYD4YVzrX9%2BRyRfzWUvz3QpxfLVyR8bnALlyIy%2FIzNTKyM4FCM6VhgUN6YAbfj1p8oqFfmrFDvvh55TwH8VNsv2NO3GxjPtPNbI3X6tgaGz%2BqT4MkRSmIiBb8hi8dEjAtTMKdQB6gJRUOUIDUXPPE5MP%2FFHSBEzsd%2B3Uptg307Rf1hMSnEDvqAXuuIov2AQPhEftaDP0T7MFj7Fo8PuOOAF7%2BaDnq8nkp2XjpYhXvDhOo6wkqrv1m73OTdl4seyEvZGy4z9d1S3ebDuEc8zvZtUgg6kBLlTsa1Pu3azu9QQ24bOzcqCxP7FxfwbPLW%2BjbG1YIEZCDooQGrtcX1uyeRujLeCdO2TMuyG6p%2FENsexC3UiDT7WCPYYYaerdoniHT7460Z6xqwcRp8fUw4tf%2BvAY6pgF4r4%2BwuNbyTZ6sGHGjmsJ5v5i%2BvyUbdj%2FbwrqNJamHcGpv5jm9FfXyuqK8VoHp7BOp92ezIWc%2BQ7SaT%2BS0I0nTskCiBKZ6H9hfEnyERtV23TmFMZMD50t0tZIMOYoLvOn34ps%2BhaI37pLSIQ0IPCJB9Au3pK309tZza7FFrftzQc2aj7MdB9a2qK%2BLDhcjcpvErPmzYdf4b0w9Ou0xK5fr1MEJpiW8&X-Amz-Signature=857fb7c9f32909d4f77f8802f3573cbf3b69dc78ae8bad1bfe3f5fa1f88b65a4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625VDHFTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1Y3NieagsYwYgv9iTvQse6wuOYRHzn1d4Mf6x3DoeWAiEA7Wswirq9U4313IsBot5OJy2GmW66ksXGlx3R5lewt00qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELNvadEMJl17ZXQLircAyk6vHdUldvvJmDRQh8wNnjTueirNqwz%2BvC6MxtA43FX0BJojYym8%2F0WenFKy7RCi7bHt7YeBHCcna7EmOeHWrYWzwm%2B2AXXc0lHmskODwUnBho4q6foQSVnhCPD5zV96q0M7%2FzmC6MDTmhnC4ZeUk%2FESIxTOUoIVM1xsY8nvD7GRLTxUzmoiJTOygiyq9qEotRJZh1AlJI7apfIpL3di3MC%2FGqHkfb19XEFsInuTJ2gfKQjazJ7nepFQV78PtSHFjIx2vjD1gxMS6tk0C2tIu7k5uZsZHj3%2BbB%2F2Il8VpvZHel%2FFV7zrtqXH%2FhYzHJSqz2XDYFFv5yeVtiY1fZrXSXoQRm5lAuLSUwfEI6SWH3wCaApszJs7R0dkO7FI0d3P6YvYUoSxvexNAzqtlP11EENYFvVE0VrXSqze3q%2B8ykRgwDbpZRHsLT%2FQmhw3aROFy9CHhc0DjxqjfLGuVhpPVBHw2LOkpwElBSxEzd1WCPPMenHM6X9J3aLOMgo%2B0jQPW7Qm0%2Bk9hIb%2Fu%2F6zpXdOkZu1ahfe15Hsn64KC9QEfzmhAuSbE3JW6E1nWAqYdvGefkox99JnN7mVmsZXxtnCtGTT8u59%2B%2FJsm1lxzG%2B44j5ZrTO%2F1oL2OrvGDs6MODi%2FrwGOqUBHCC57gmfySHVxoId%2FTWIzJyALUYjsCq4jlPTUoR%2BHCIuvdj%2BWocbeWMnJN78N55sh9esypq4g0yXziHCQke3dxluTU9QG9cRh2gRHnyEIhe%2BNZAZ3m%2FWTJiAvwVrLDlqSjtyGCz1wcHNytvmp3hs4c9HoUNTokXiYpOZvaOIAlCQfNf30rE7GXyiBsyAo40w12Bn%2BqSIaYo7n1PgMouV%2BlKJc5is&X-Amz-Signature=1d7d9a5f51910246dfb64820f34e51f938541e1d862512cc25f906b657b98217&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625VDHFTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1Y3NieagsYwYgv9iTvQse6wuOYRHzn1d4Mf6x3DoeWAiEA7Wswirq9U4313IsBot5OJy2GmW66ksXGlx3R5lewt00qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELNvadEMJl17ZXQLircAyk6vHdUldvvJmDRQh8wNnjTueirNqwz%2BvC6MxtA43FX0BJojYym8%2F0WenFKy7RCi7bHt7YeBHCcna7EmOeHWrYWzwm%2B2AXXc0lHmskODwUnBho4q6foQSVnhCPD5zV96q0M7%2FzmC6MDTmhnC4ZeUk%2FESIxTOUoIVM1xsY8nvD7GRLTxUzmoiJTOygiyq9qEotRJZh1AlJI7apfIpL3di3MC%2FGqHkfb19XEFsInuTJ2gfKQjazJ7nepFQV78PtSHFjIx2vjD1gxMS6tk0C2tIu7k5uZsZHj3%2BbB%2F2Il8VpvZHel%2FFV7zrtqXH%2FhYzHJSqz2XDYFFv5yeVtiY1fZrXSXoQRm5lAuLSUwfEI6SWH3wCaApszJs7R0dkO7FI0d3P6YvYUoSxvexNAzqtlP11EENYFvVE0VrXSqze3q%2B8ykRgwDbpZRHsLT%2FQmhw3aROFy9CHhc0DjxqjfLGuVhpPVBHw2LOkpwElBSxEzd1WCPPMenHM6X9J3aLOMgo%2B0jQPW7Qm0%2Bk9hIb%2Fu%2F6zpXdOkZu1ahfe15Hsn64KC9QEfzmhAuSbE3JW6E1nWAqYdvGefkox99JnN7mVmsZXxtnCtGTT8u59%2B%2FJsm1lxzG%2B44j5ZrTO%2F1oL2OrvGDs6MODi%2FrwGOqUBHCC57gmfySHVxoId%2FTWIzJyALUYjsCq4jlPTUoR%2BHCIuvdj%2BWocbeWMnJN78N55sh9esypq4g0yXziHCQke3dxluTU9QG9cRh2gRHnyEIhe%2BNZAZ3m%2FWTJiAvwVrLDlqSjtyGCz1wcHNytvmp3hs4c9HoUNTokXiYpOZvaOIAlCQfNf30rE7GXyiBsyAo40w12Bn%2BqSIaYo7n1PgMouV%2BlKJc5is&X-Amz-Signature=bbdcdee66c25443e80e4c8bda00e484c60f17816f7354421a1114842cafc5392&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625VDHFTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1Y3NieagsYwYgv9iTvQse6wuOYRHzn1d4Mf6x3DoeWAiEA7Wswirq9U4313IsBot5OJy2GmW66ksXGlx3R5lewt00qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELNvadEMJl17ZXQLircAyk6vHdUldvvJmDRQh8wNnjTueirNqwz%2BvC6MxtA43FX0BJojYym8%2F0WenFKy7RCi7bHt7YeBHCcna7EmOeHWrYWzwm%2B2AXXc0lHmskODwUnBho4q6foQSVnhCPD5zV96q0M7%2FzmC6MDTmhnC4ZeUk%2FESIxTOUoIVM1xsY8nvD7GRLTxUzmoiJTOygiyq9qEotRJZh1AlJI7apfIpL3di3MC%2FGqHkfb19XEFsInuTJ2gfKQjazJ7nepFQV78PtSHFjIx2vjD1gxMS6tk0C2tIu7k5uZsZHj3%2BbB%2F2Il8VpvZHel%2FFV7zrtqXH%2FhYzHJSqz2XDYFFv5yeVtiY1fZrXSXoQRm5lAuLSUwfEI6SWH3wCaApszJs7R0dkO7FI0d3P6YvYUoSxvexNAzqtlP11EENYFvVE0VrXSqze3q%2B8ykRgwDbpZRHsLT%2FQmhw3aROFy9CHhc0DjxqjfLGuVhpPVBHw2LOkpwElBSxEzd1WCPPMenHM6X9J3aLOMgo%2B0jQPW7Qm0%2Bk9hIb%2Fu%2F6zpXdOkZu1ahfe15Hsn64KC9QEfzmhAuSbE3JW6E1nWAqYdvGefkox99JnN7mVmsZXxtnCtGTT8u59%2B%2FJsm1lxzG%2B44j5ZrTO%2F1oL2OrvGDs6MODi%2FrwGOqUBHCC57gmfySHVxoId%2FTWIzJyALUYjsCq4jlPTUoR%2BHCIuvdj%2BWocbeWMnJN78N55sh9esypq4g0yXziHCQke3dxluTU9QG9cRh2gRHnyEIhe%2BNZAZ3m%2FWTJiAvwVrLDlqSjtyGCz1wcHNytvmp3hs4c9HoUNTokXiYpOZvaOIAlCQfNf30rE7GXyiBsyAo40w12Bn%2BqSIaYo7n1PgMouV%2BlKJc5is&X-Amz-Signature=05e7b845bee3f997654481ae3c7326b56fc66529bf45eae4cb50e0854d7ab8dd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625VDHFTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1Y3NieagsYwYgv9iTvQse6wuOYRHzn1d4Mf6x3DoeWAiEA7Wswirq9U4313IsBot5OJy2GmW66ksXGlx3R5lewt00qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELNvadEMJl17ZXQLircAyk6vHdUldvvJmDRQh8wNnjTueirNqwz%2BvC6MxtA43FX0BJojYym8%2F0WenFKy7RCi7bHt7YeBHCcna7EmOeHWrYWzwm%2B2AXXc0lHmskODwUnBho4q6foQSVnhCPD5zV96q0M7%2FzmC6MDTmhnC4ZeUk%2FESIxTOUoIVM1xsY8nvD7GRLTxUzmoiJTOygiyq9qEotRJZh1AlJI7apfIpL3di3MC%2FGqHkfb19XEFsInuTJ2gfKQjazJ7nepFQV78PtSHFjIx2vjD1gxMS6tk0C2tIu7k5uZsZHj3%2BbB%2F2Il8VpvZHel%2FFV7zrtqXH%2FhYzHJSqz2XDYFFv5yeVtiY1fZrXSXoQRm5lAuLSUwfEI6SWH3wCaApszJs7R0dkO7FI0d3P6YvYUoSxvexNAzqtlP11EENYFvVE0VrXSqze3q%2B8ykRgwDbpZRHsLT%2FQmhw3aROFy9CHhc0DjxqjfLGuVhpPVBHw2LOkpwElBSxEzd1WCPPMenHM6X9J3aLOMgo%2B0jQPW7Qm0%2Bk9hIb%2Fu%2F6zpXdOkZu1ahfe15Hsn64KC9QEfzmhAuSbE3JW6E1nWAqYdvGefkox99JnN7mVmsZXxtnCtGTT8u59%2B%2FJsm1lxzG%2B44j5ZrTO%2F1oL2OrvGDs6MODi%2FrwGOqUBHCC57gmfySHVxoId%2FTWIzJyALUYjsCq4jlPTUoR%2BHCIuvdj%2BWocbeWMnJN78N55sh9esypq4g0yXziHCQke3dxluTU9QG9cRh2gRHnyEIhe%2BNZAZ3m%2FWTJiAvwVrLDlqSjtyGCz1wcHNytvmp3hs4c9HoUNTokXiYpOZvaOIAlCQfNf30rE7GXyiBsyAo40w12Bn%2BqSIaYo7n1PgMouV%2BlKJc5is&X-Amz-Signature=88abc32489f7b2845bbd3bbe572dea79491c113b67d74d79b709a04502ed3b31&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625VDHFTF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1Y3NieagsYwYgv9iTvQse6wuOYRHzn1d4Mf6x3DoeWAiEA7Wswirq9U4313IsBot5OJy2GmW66ksXGlx3R5lewt00qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELNvadEMJl17ZXQLircAyk6vHdUldvvJmDRQh8wNnjTueirNqwz%2BvC6MxtA43FX0BJojYym8%2F0WenFKy7RCi7bHt7YeBHCcna7EmOeHWrYWzwm%2B2AXXc0lHmskODwUnBho4q6foQSVnhCPD5zV96q0M7%2FzmC6MDTmhnC4ZeUk%2FESIxTOUoIVM1xsY8nvD7GRLTxUzmoiJTOygiyq9qEotRJZh1AlJI7apfIpL3di3MC%2FGqHkfb19XEFsInuTJ2gfKQjazJ7nepFQV78PtSHFjIx2vjD1gxMS6tk0C2tIu7k5uZsZHj3%2BbB%2F2Il8VpvZHel%2FFV7zrtqXH%2FhYzHJSqz2XDYFFv5yeVtiY1fZrXSXoQRm5lAuLSUwfEI6SWH3wCaApszJs7R0dkO7FI0d3P6YvYUoSxvexNAzqtlP11EENYFvVE0VrXSqze3q%2B8ykRgwDbpZRHsLT%2FQmhw3aROFy9CHhc0DjxqjfLGuVhpPVBHw2LOkpwElBSxEzd1WCPPMenHM6X9J3aLOMgo%2B0jQPW7Qm0%2Bk9hIb%2Fu%2F6zpXdOkZu1ahfe15Hsn64KC9QEfzmhAuSbE3JW6E1nWAqYdvGefkox99JnN7mVmsZXxtnCtGTT8u59%2B%2FJsm1lxzG%2B44j5ZrTO%2F1oL2OrvGDs6MODi%2FrwGOqUBHCC57gmfySHVxoId%2FTWIzJyALUYjsCq4jlPTUoR%2BHCIuvdj%2BWocbeWMnJN78N55sh9esypq4g0yXziHCQke3dxluTU9QG9cRh2gRHnyEIhe%2BNZAZ3m%2FWTJiAvwVrLDlqSjtyGCz1wcHNytvmp3hs4c9HoUNTokXiYpOZvaOIAlCQfNf30rE7GXyiBsyAo40w12Bn%2BqSIaYo7n1PgMouV%2BlKJc5is&X-Amz-Signature=d814befc6001858da6a6835e168d86b72bb56a7f4a2f81d90a1bbcd5202ff23b&X-Amz-SignedHeaders=host&x-id=GetObject)
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


