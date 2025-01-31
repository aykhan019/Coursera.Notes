

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G7RQJC3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBxEQfHAYLSTxIGiFdAko9S0y8cNVWvRmjsXAKPkKVSXAiEApET043T58G3KLzWjU%2Bdng5M%2FbmyzyBb%2Fst7YT7lFAJsqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6Bq9vI9Rfu7ralmyrcA5iRWSriiexzljBSUaBqjUqJBriwekZaDaLdafwSCW5WQdnVyv0e36X8UOVh3b4%2FdrYV67u0AxZHPVZVGfak4dv0QjWdIa%2Bo1ULxZHIex2muT6jCb9KdLJzDUgJTqXGZSE1BTICwPJElAlJ9iaghxptDpJrk%2F6PWAg2U4mS3ijRAfObt1hICnYwTQqRJuoHxFXnJ1FA4utMZmSZVJA4luqdhRFzlw484sKS3gQyBdSaEaSrZWFrzlwd35SyulMIOXWPT5kQDH%2FJgSH9OnoExyc%2FCz2hQ%2BhBqL1Tp1ZSw5ny1fFH4lQiJYQxcKZOnuDdXoz0widL8y%2FPBk66l9UVtiOJiU4eZEdm6tvnxac3fW6IDFBzOyLVETplRgcYvQ1MwrQcBilGbOA708ibentigbqBk8g5vJAQL41Xoy9CynmEFOF4nFTFgLWJNu6lkTbKfDtWVAxY9JGMMIf8XgPKQ4Oy%2BAGg7nhlyx%2BTxEFAB%2FZkFbabRf0zfOB9LudkU%2F6KzAE8qWA8gUmCvnUw6PRiRwdt3lSUZ00xWzWjXK3gFx5O9CQqpnkKGNskanGwhSYMGeXnRz7fQ499%2Fam5%2F93DpmpeEt8%2BT2C%2Bg2W3demWXQP3SMWxr%2Fw5sJY7MrES0MPH08rwGOqUBLQH883gZFh1lQ%2FNFzAqJWmxb5Dk%2Bj0VI%2B5CXn4pMMfikWZZ0L7JhE4x90BHXMDop0zWdhp1rzujE4sZbjYlmh3GwJUYGzta8kJrXZXA%2BJ67D03xJSJ4TpuXW3J1BDd%2FSawWUBas4bSdUsa4HIL8CfUXvNDw3fkwz5KoCqcEcQo6rmXOJNAkU1xsWcpI92%2FIuBzJQdwhqac%2BvQl6UIfzbKvj4DSdu&X-Amz-Signature=8f610a9243006f56db41cda27f1ed1a9a7aedced14db1df0068dd56bc301c32a&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WHZ4BSP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEchiRmQOxY1vkHSFbcQrmOaWHLQl5ctn%2B9FV798IoWyAiEA%2FNgLlijxtqBPSLjYqfbt%2B9us363tzec7q2XNPaccWVMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiGNYip5UK3ROpGmyrcA1COHWxQzvxxSCbope%2Fzeht%2FkibL7oWNOR1%2BnWhPvghDqYvFlF6ToQqEIVTBd%2BBq1WxYoKNOvNEV2nAMVCR86hNIO%2FL9dckHtzdTffQZ8N9E%2FVL%2BZf85NiKegVxxRBRbrv0GupA11QqnGQJJ%2F5FW8OEhoL3dqnjg0yKddG%2FyRZvUIwpPUbfhf4W32ycVOwblOyAI9TyUWQNSnkLgDPeCY6bsX%2FpTU%2FCXl%2FhFgHw3%2BB7m0JwueEvt99qAFxlMlkcBBoOEq2S3Z8OABPLHvYO8c1GGXJ937ClrFAQCfxf9nouQ5OTM67DFtTlWIKXbLrwWRuEwVbIumv2DPi21tz2r8OqDExKYqncACR4fZoDCcKiCZlPKDT3O5%2FX%2BjOUsegqFs5nL54HvrwzD%2BCC9y9vEYaGwr2wyzyMfTRRsg3jEsolUpGsR4Tty2wArSnuinv%2BgSEzD5n71vBBX9fkIgm%2BZT0Sf1rsh1xb6E6NqGvL4yRmhmcCwUzNtDDvwYUiXmhsjnNexaI8PXsz6ldg8jXOBlhqjAUaD9bZZ7kDPbOosOR4zChxTYRnZsdU2FyKj2Lk1frujK0AWoTABNFTTGHzLJPTKWOxWa7UUcu0mpQIJXYWbdOgO9Pov4FomslcVMOHz8rwGOqUBhoEOD59BvapCAg4FRmO%2Fi9ehryp8dcofE2DEmsvspaYzyMQgGiq8Dd4M3CnHhHjOf8KD7k2NE%2Fqr2CrHke72YeVrb%2BtozKu9pOVAo1ydxleilQSvr29OQjTOGlJHAhkRW3k8cgmGEh1KGZq75pHQaYXdcvHxwwh14cTcqRHoa48aYTOmp0ldOuzq%2BnPv50p7A7fxBf8PWiPJpeSsL54LybsbLiNg&X-Amz-Signature=0d10164eae5228f2996657f8d7cbc3724388b8f91d26e23f5a58434bf9f3cb57&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WHZ4BSP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEchiRmQOxY1vkHSFbcQrmOaWHLQl5ctn%2B9FV798IoWyAiEA%2FNgLlijxtqBPSLjYqfbt%2B9us363tzec7q2XNPaccWVMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiGNYip5UK3ROpGmyrcA1COHWxQzvxxSCbope%2Fzeht%2FkibL7oWNOR1%2BnWhPvghDqYvFlF6ToQqEIVTBd%2BBq1WxYoKNOvNEV2nAMVCR86hNIO%2FL9dckHtzdTffQZ8N9E%2FVL%2BZf85NiKegVxxRBRbrv0GupA11QqnGQJJ%2F5FW8OEhoL3dqnjg0yKddG%2FyRZvUIwpPUbfhf4W32ycVOwblOyAI9TyUWQNSnkLgDPeCY6bsX%2FpTU%2FCXl%2FhFgHw3%2BB7m0JwueEvt99qAFxlMlkcBBoOEq2S3Z8OABPLHvYO8c1GGXJ937ClrFAQCfxf9nouQ5OTM67DFtTlWIKXbLrwWRuEwVbIumv2DPi21tz2r8OqDExKYqncACR4fZoDCcKiCZlPKDT3O5%2FX%2BjOUsegqFs5nL54HvrwzD%2BCC9y9vEYaGwr2wyzyMfTRRsg3jEsolUpGsR4Tty2wArSnuinv%2BgSEzD5n71vBBX9fkIgm%2BZT0Sf1rsh1xb6E6NqGvL4yRmhmcCwUzNtDDvwYUiXmhsjnNexaI8PXsz6ldg8jXOBlhqjAUaD9bZZ7kDPbOosOR4zChxTYRnZsdU2FyKj2Lk1frujK0AWoTABNFTTGHzLJPTKWOxWa7UUcu0mpQIJXYWbdOgO9Pov4FomslcVMOHz8rwGOqUBhoEOD59BvapCAg4FRmO%2Fi9ehryp8dcofE2DEmsvspaYzyMQgGiq8Dd4M3CnHhHjOf8KD7k2NE%2Fqr2CrHke72YeVrb%2BtozKu9pOVAo1ydxleilQSvr29OQjTOGlJHAhkRW3k8cgmGEh1KGZq75pHQaYXdcvHxwwh14cTcqRHoa48aYTOmp0ldOuzq%2BnPv50p7A7fxBf8PWiPJpeSsL54LybsbLiNg&X-Amz-Signature=ae751a53151577c3c15be573556f80540c3c89a695128c3d2bdf9f00ebc03466&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WHZ4BSP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEchiRmQOxY1vkHSFbcQrmOaWHLQl5ctn%2B9FV798IoWyAiEA%2FNgLlijxtqBPSLjYqfbt%2B9us363tzec7q2XNPaccWVMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiGNYip5UK3ROpGmyrcA1COHWxQzvxxSCbope%2Fzeht%2FkibL7oWNOR1%2BnWhPvghDqYvFlF6ToQqEIVTBd%2BBq1WxYoKNOvNEV2nAMVCR86hNIO%2FL9dckHtzdTffQZ8N9E%2FVL%2BZf85NiKegVxxRBRbrv0GupA11QqnGQJJ%2F5FW8OEhoL3dqnjg0yKddG%2FyRZvUIwpPUbfhf4W32ycVOwblOyAI9TyUWQNSnkLgDPeCY6bsX%2FpTU%2FCXl%2FhFgHw3%2BB7m0JwueEvt99qAFxlMlkcBBoOEq2S3Z8OABPLHvYO8c1GGXJ937ClrFAQCfxf9nouQ5OTM67DFtTlWIKXbLrwWRuEwVbIumv2DPi21tz2r8OqDExKYqncACR4fZoDCcKiCZlPKDT3O5%2FX%2BjOUsegqFs5nL54HvrwzD%2BCC9y9vEYaGwr2wyzyMfTRRsg3jEsolUpGsR4Tty2wArSnuinv%2BgSEzD5n71vBBX9fkIgm%2BZT0Sf1rsh1xb6E6NqGvL4yRmhmcCwUzNtDDvwYUiXmhsjnNexaI8PXsz6ldg8jXOBlhqjAUaD9bZZ7kDPbOosOR4zChxTYRnZsdU2FyKj2Lk1frujK0AWoTABNFTTGHzLJPTKWOxWa7UUcu0mpQIJXYWbdOgO9Pov4FomslcVMOHz8rwGOqUBhoEOD59BvapCAg4FRmO%2Fi9ehryp8dcofE2DEmsvspaYzyMQgGiq8Dd4M3CnHhHjOf8KD7k2NE%2Fqr2CrHke72YeVrb%2BtozKu9pOVAo1ydxleilQSvr29OQjTOGlJHAhkRW3k8cgmGEh1KGZq75pHQaYXdcvHxwwh14cTcqRHoa48aYTOmp0ldOuzq%2BnPv50p7A7fxBf8PWiPJpeSsL54LybsbLiNg&X-Amz-Signature=330847e085e6381b29d2f074da879f83e44f3e923fbdf1580e0fda015582c4c8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WHZ4BSP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEchiRmQOxY1vkHSFbcQrmOaWHLQl5ctn%2B9FV798IoWyAiEA%2FNgLlijxtqBPSLjYqfbt%2B9us363tzec7q2XNPaccWVMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiGNYip5UK3ROpGmyrcA1COHWxQzvxxSCbope%2Fzeht%2FkibL7oWNOR1%2BnWhPvghDqYvFlF6ToQqEIVTBd%2BBq1WxYoKNOvNEV2nAMVCR86hNIO%2FL9dckHtzdTffQZ8N9E%2FVL%2BZf85NiKegVxxRBRbrv0GupA11QqnGQJJ%2F5FW8OEhoL3dqnjg0yKddG%2FyRZvUIwpPUbfhf4W32ycVOwblOyAI9TyUWQNSnkLgDPeCY6bsX%2FpTU%2FCXl%2FhFgHw3%2BB7m0JwueEvt99qAFxlMlkcBBoOEq2S3Z8OABPLHvYO8c1GGXJ937ClrFAQCfxf9nouQ5OTM67DFtTlWIKXbLrwWRuEwVbIumv2DPi21tz2r8OqDExKYqncACR4fZoDCcKiCZlPKDT3O5%2FX%2BjOUsegqFs5nL54HvrwzD%2BCC9y9vEYaGwr2wyzyMfTRRsg3jEsolUpGsR4Tty2wArSnuinv%2BgSEzD5n71vBBX9fkIgm%2BZT0Sf1rsh1xb6E6NqGvL4yRmhmcCwUzNtDDvwYUiXmhsjnNexaI8PXsz6ldg8jXOBlhqjAUaD9bZZ7kDPbOosOR4zChxTYRnZsdU2FyKj2Lk1frujK0AWoTABNFTTGHzLJPTKWOxWa7UUcu0mpQIJXYWbdOgO9Pov4FomslcVMOHz8rwGOqUBhoEOD59BvapCAg4FRmO%2Fi9ehryp8dcofE2DEmsvspaYzyMQgGiq8Dd4M3CnHhHjOf8KD7k2NE%2Fqr2CrHke72YeVrb%2BtozKu9pOVAo1ydxleilQSvr29OQjTOGlJHAhkRW3k8cgmGEh1KGZq75pHQaYXdcvHxwwh14cTcqRHoa48aYTOmp0ldOuzq%2BnPv50p7A7fxBf8PWiPJpeSsL54LybsbLiNg&X-Amz-Signature=b5461b4b2e8b6bd86b751e33165189b69a5d3a5fa55f0e9c06137b98aec7f6b3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WHZ4BSP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEchiRmQOxY1vkHSFbcQrmOaWHLQl5ctn%2B9FV798IoWyAiEA%2FNgLlijxtqBPSLjYqfbt%2B9us363tzec7q2XNPaccWVMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiGNYip5UK3ROpGmyrcA1COHWxQzvxxSCbope%2Fzeht%2FkibL7oWNOR1%2BnWhPvghDqYvFlF6ToQqEIVTBd%2BBq1WxYoKNOvNEV2nAMVCR86hNIO%2FL9dckHtzdTffQZ8N9E%2FVL%2BZf85NiKegVxxRBRbrv0GupA11QqnGQJJ%2F5FW8OEhoL3dqnjg0yKddG%2FyRZvUIwpPUbfhf4W32ycVOwblOyAI9TyUWQNSnkLgDPeCY6bsX%2FpTU%2FCXl%2FhFgHw3%2BB7m0JwueEvt99qAFxlMlkcBBoOEq2S3Z8OABPLHvYO8c1GGXJ937ClrFAQCfxf9nouQ5OTM67DFtTlWIKXbLrwWRuEwVbIumv2DPi21tz2r8OqDExKYqncACR4fZoDCcKiCZlPKDT3O5%2FX%2BjOUsegqFs5nL54HvrwzD%2BCC9y9vEYaGwr2wyzyMfTRRsg3jEsolUpGsR4Tty2wArSnuinv%2BgSEzD5n71vBBX9fkIgm%2BZT0Sf1rsh1xb6E6NqGvL4yRmhmcCwUzNtDDvwYUiXmhsjnNexaI8PXsz6ldg8jXOBlhqjAUaD9bZZ7kDPbOosOR4zChxTYRnZsdU2FyKj2Lk1frujK0AWoTABNFTTGHzLJPTKWOxWa7UUcu0mpQIJXYWbdOgO9Pov4FomslcVMOHz8rwGOqUBhoEOD59BvapCAg4FRmO%2Fi9ehryp8dcofE2DEmsvspaYzyMQgGiq8Dd4M3CnHhHjOf8KD7k2NE%2Fqr2CrHke72YeVrb%2BtozKu9pOVAo1ydxleilQSvr29OQjTOGlJHAhkRW3k8cgmGEh1KGZq75pHQaYXdcvHxwwh14cTcqRHoa48aYTOmp0ldOuzq%2BnPv50p7A7fxBf8PWiPJpeSsL54LybsbLiNg&X-Amz-Signature=88105d2b0426e85ce08106f7275996f4492309acffa24949cc3b221bb627e515&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G7RQJC3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBxEQfHAYLSTxIGiFdAko9S0y8cNVWvRmjsXAKPkKVSXAiEApET043T58G3KLzWjU%2Bdng5M%2FbmyzyBb%2Fst7YT7lFAJsqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6Bq9vI9Rfu7ralmyrcA5iRWSriiexzljBSUaBqjUqJBriwekZaDaLdafwSCW5WQdnVyv0e36X8UOVh3b4%2FdrYV67u0AxZHPVZVGfak4dv0QjWdIa%2Bo1ULxZHIex2muT6jCb9KdLJzDUgJTqXGZSE1BTICwPJElAlJ9iaghxptDpJrk%2F6PWAg2U4mS3ijRAfObt1hICnYwTQqRJuoHxFXnJ1FA4utMZmSZVJA4luqdhRFzlw484sKS3gQyBdSaEaSrZWFrzlwd35SyulMIOXWPT5kQDH%2FJgSH9OnoExyc%2FCz2hQ%2BhBqL1Tp1ZSw5ny1fFH4lQiJYQxcKZOnuDdXoz0widL8y%2FPBk66l9UVtiOJiU4eZEdm6tvnxac3fW6IDFBzOyLVETplRgcYvQ1MwrQcBilGbOA708ibentigbqBk8g5vJAQL41Xoy9CynmEFOF4nFTFgLWJNu6lkTbKfDtWVAxY9JGMMIf8XgPKQ4Oy%2BAGg7nhlyx%2BTxEFAB%2FZkFbabRf0zfOB9LudkU%2F6KzAE8qWA8gUmCvnUw6PRiRwdt3lSUZ00xWzWjXK3gFx5O9CQqpnkKGNskanGwhSYMGeXnRz7fQ499%2Fam5%2F93DpmpeEt8%2BT2C%2Bg2W3demWXQP3SMWxr%2Fw5sJY7MrES0MPH08rwGOqUBLQH883gZFh1lQ%2FNFzAqJWmxb5Dk%2Bj0VI%2B5CXn4pMMfikWZZ0L7JhE4x90BHXMDop0zWdhp1rzujE4sZbjYlmh3GwJUYGzta8kJrXZXA%2BJ67D03xJSJ4TpuXW3J1BDd%2FSawWUBas4bSdUsa4HIL8CfUXvNDw3fkwz5KoCqcEcQo6rmXOJNAkU1xsWcpI92%2FIuBzJQdwhqac%2BvQl6UIfzbKvj4DSdu&X-Amz-Signature=4cecffee357aa3f9461560f0d446b9681e2ccaf0ff55d80d17c9987fcc7c900d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G7RQJC3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBxEQfHAYLSTxIGiFdAko9S0y8cNVWvRmjsXAKPkKVSXAiEApET043T58G3KLzWjU%2Bdng5M%2FbmyzyBb%2Fst7YT7lFAJsqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6Bq9vI9Rfu7ralmyrcA5iRWSriiexzljBSUaBqjUqJBriwekZaDaLdafwSCW5WQdnVyv0e36X8UOVh3b4%2FdrYV67u0AxZHPVZVGfak4dv0QjWdIa%2Bo1ULxZHIex2muT6jCb9KdLJzDUgJTqXGZSE1BTICwPJElAlJ9iaghxptDpJrk%2F6PWAg2U4mS3ijRAfObt1hICnYwTQqRJuoHxFXnJ1FA4utMZmSZVJA4luqdhRFzlw484sKS3gQyBdSaEaSrZWFrzlwd35SyulMIOXWPT5kQDH%2FJgSH9OnoExyc%2FCz2hQ%2BhBqL1Tp1ZSw5ny1fFH4lQiJYQxcKZOnuDdXoz0widL8y%2FPBk66l9UVtiOJiU4eZEdm6tvnxac3fW6IDFBzOyLVETplRgcYvQ1MwrQcBilGbOA708ibentigbqBk8g5vJAQL41Xoy9CynmEFOF4nFTFgLWJNu6lkTbKfDtWVAxY9JGMMIf8XgPKQ4Oy%2BAGg7nhlyx%2BTxEFAB%2FZkFbabRf0zfOB9LudkU%2F6KzAE8qWA8gUmCvnUw6PRiRwdt3lSUZ00xWzWjXK3gFx5O9CQqpnkKGNskanGwhSYMGeXnRz7fQ499%2Fam5%2F93DpmpeEt8%2BT2C%2Bg2W3demWXQP3SMWxr%2Fw5sJY7MrES0MPH08rwGOqUBLQH883gZFh1lQ%2FNFzAqJWmxb5Dk%2Bj0VI%2B5CXn4pMMfikWZZ0L7JhE4x90BHXMDop0zWdhp1rzujE4sZbjYlmh3GwJUYGzta8kJrXZXA%2BJ67D03xJSJ4TpuXW3J1BDd%2FSawWUBas4bSdUsa4HIL8CfUXvNDw3fkwz5KoCqcEcQo6rmXOJNAkU1xsWcpI92%2FIuBzJQdwhqac%2BvQl6UIfzbKvj4DSdu&X-Amz-Signature=06118f9e89d832919e6237e39246fa95b55d2be07e20e93f21e412fc5eeb886a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G7RQJC3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBxEQfHAYLSTxIGiFdAko9S0y8cNVWvRmjsXAKPkKVSXAiEApET043T58G3KLzWjU%2Bdng5M%2FbmyzyBb%2Fst7YT7lFAJsqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6Bq9vI9Rfu7ralmyrcA5iRWSriiexzljBSUaBqjUqJBriwekZaDaLdafwSCW5WQdnVyv0e36X8UOVh3b4%2FdrYV67u0AxZHPVZVGfak4dv0QjWdIa%2Bo1ULxZHIex2muT6jCb9KdLJzDUgJTqXGZSE1BTICwPJElAlJ9iaghxptDpJrk%2F6PWAg2U4mS3ijRAfObt1hICnYwTQqRJuoHxFXnJ1FA4utMZmSZVJA4luqdhRFzlw484sKS3gQyBdSaEaSrZWFrzlwd35SyulMIOXWPT5kQDH%2FJgSH9OnoExyc%2FCz2hQ%2BhBqL1Tp1ZSw5ny1fFH4lQiJYQxcKZOnuDdXoz0widL8y%2FPBk66l9UVtiOJiU4eZEdm6tvnxac3fW6IDFBzOyLVETplRgcYvQ1MwrQcBilGbOA708ibentigbqBk8g5vJAQL41Xoy9CynmEFOF4nFTFgLWJNu6lkTbKfDtWVAxY9JGMMIf8XgPKQ4Oy%2BAGg7nhlyx%2BTxEFAB%2FZkFbabRf0zfOB9LudkU%2F6KzAE8qWA8gUmCvnUw6PRiRwdt3lSUZ00xWzWjXK3gFx5O9CQqpnkKGNskanGwhSYMGeXnRz7fQ499%2Fam5%2F93DpmpeEt8%2BT2C%2Bg2W3demWXQP3SMWxr%2Fw5sJY7MrES0MPH08rwGOqUBLQH883gZFh1lQ%2FNFzAqJWmxb5Dk%2Bj0VI%2B5CXn4pMMfikWZZ0L7JhE4x90BHXMDop0zWdhp1rzujE4sZbjYlmh3GwJUYGzta8kJrXZXA%2BJ67D03xJSJ4TpuXW3J1BDd%2FSawWUBas4bSdUsa4HIL8CfUXvNDw3fkwz5KoCqcEcQo6rmXOJNAkU1xsWcpI92%2FIuBzJQdwhqac%2BvQl6UIfzbKvj4DSdu&X-Amz-Signature=f195f43b8a33ef0de411b368aa0d813f30f8dbc3720770280e3682d99aa78a89&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G7RQJC3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBxEQfHAYLSTxIGiFdAko9S0y8cNVWvRmjsXAKPkKVSXAiEApET043T58G3KLzWjU%2Bdng5M%2FbmyzyBb%2Fst7YT7lFAJsqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6Bq9vI9Rfu7ralmyrcA5iRWSriiexzljBSUaBqjUqJBriwekZaDaLdafwSCW5WQdnVyv0e36X8UOVh3b4%2FdrYV67u0AxZHPVZVGfak4dv0QjWdIa%2Bo1ULxZHIex2muT6jCb9KdLJzDUgJTqXGZSE1BTICwPJElAlJ9iaghxptDpJrk%2F6PWAg2U4mS3ijRAfObt1hICnYwTQqRJuoHxFXnJ1FA4utMZmSZVJA4luqdhRFzlw484sKS3gQyBdSaEaSrZWFrzlwd35SyulMIOXWPT5kQDH%2FJgSH9OnoExyc%2FCz2hQ%2BhBqL1Tp1ZSw5ny1fFH4lQiJYQxcKZOnuDdXoz0widL8y%2FPBk66l9UVtiOJiU4eZEdm6tvnxac3fW6IDFBzOyLVETplRgcYvQ1MwrQcBilGbOA708ibentigbqBk8g5vJAQL41Xoy9CynmEFOF4nFTFgLWJNu6lkTbKfDtWVAxY9JGMMIf8XgPKQ4Oy%2BAGg7nhlyx%2BTxEFAB%2FZkFbabRf0zfOB9LudkU%2F6KzAE8qWA8gUmCvnUw6PRiRwdt3lSUZ00xWzWjXK3gFx5O9CQqpnkKGNskanGwhSYMGeXnRz7fQ499%2Fam5%2F93DpmpeEt8%2BT2C%2Bg2W3demWXQP3SMWxr%2Fw5sJY7MrES0MPH08rwGOqUBLQH883gZFh1lQ%2FNFzAqJWmxb5Dk%2Bj0VI%2B5CXn4pMMfikWZZ0L7JhE4x90BHXMDop0zWdhp1rzujE4sZbjYlmh3GwJUYGzta8kJrXZXA%2BJ67D03xJSJ4TpuXW3J1BDd%2FSawWUBas4bSdUsa4HIL8CfUXvNDw3fkwz5KoCqcEcQo6rmXOJNAkU1xsWcpI92%2FIuBzJQdwhqac%2BvQl6UIfzbKvj4DSdu&X-Amz-Signature=15c9f3c7d186a213bf9910c0b6c9cb369097db9b65c997a9f5a394ddffd7dab0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G7RQJC3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBxEQfHAYLSTxIGiFdAko9S0y8cNVWvRmjsXAKPkKVSXAiEApET043T58G3KLzWjU%2Bdng5M%2FbmyzyBb%2Fst7YT7lFAJsqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6Bq9vI9Rfu7ralmyrcA5iRWSriiexzljBSUaBqjUqJBriwekZaDaLdafwSCW5WQdnVyv0e36X8UOVh3b4%2FdrYV67u0AxZHPVZVGfak4dv0QjWdIa%2Bo1ULxZHIex2muT6jCb9KdLJzDUgJTqXGZSE1BTICwPJElAlJ9iaghxptDpJrk%2F6PWAg2U4mS3ijRAfObt1hICnYwTQqRJuoHxFXnJ1FA4utMZmSZVJA4luqdhRFzlw484sKS3gQyBdSaEaSrZWFrzlwd35SyulMIOXWPT5kQDH%2FJgSH9OnoExyc%2FCz2hQ%2BhBqL1Tp1ZSw5ny1fFH4lQiJYQxcKZOnuDdXoz0widL8y%2FPBk66l9UVtiOJiU4eZEdm6tvnxac3fW6IDFBzOyLVETplRgcYvQ1MwrQcBilGbOA708ibentigbqBk8g5vJAQL41Xoy9CynmEFOF4nFTFgLWJNu6lkTbKfDtWVAxY9JGMMIf8XgPKQ4Oy%2BAGg7nhlyx%2BTxEFAB%2FZkFbabRf0zfOB9LudkU%2F6KzAE8qWA8gUmCvnUw6PRiRwdt3lSUZ00xWzWjXK3gFx5O9CQqpnkKGNskanGwhSYMGeXnRz7fQ499%2Fam5%2F93DpmpeEt8%2BT2C%2Bg2W3demWXQP3SMWxr%2Fw5sJY7MrES0MPH08rwGOqUBLQH883gZFh1lQ%2FNFzAqJWmxb5Dk%2Bj0VI%2B5CXn4pMMfikWZZ0L7JhE4x90BHXMDop0zWdhp1rzujE4sZbjYlmh3GwJUYGzta8kJrXZXA%2BJ67D03xJSJ4TpuXW3J1BDd%2FSawWUBas4bSdUsa4HIL8CfUXvNDw3fkwz5KoCqcEcQo6rmXOJNAkU1xsWcpI92%2FIuBzJQdwhqac%2BvQl6UIfzbKvj4DSdu&X-Amz-Signature=27d2ea81e5fb9961814d4c568065287a40c1c94898f938a6358f449b79f13782&X-Amz-SignedHeaders=host&x-id=GetObject)
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


