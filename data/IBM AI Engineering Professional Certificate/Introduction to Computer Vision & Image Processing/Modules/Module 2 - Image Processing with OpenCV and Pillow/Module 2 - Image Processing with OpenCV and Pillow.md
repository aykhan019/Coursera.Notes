

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZF2PUKR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIEFpEusa%2ByvqEB4Eutz4VebBstS66Yr%2BYtmtOMra%2FZ2AAiB%2FmnthXTVdhPeFkf1sW5bXD4tEqFGzk7j9oPoj0sZKtyr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMOsJGrVwnyTgmn47mKtwDjGFSDOyoki9i5qiciikhDsAg%2BG2igIorfBSmthO26dzwiFz54d%2BG9k7QQ3SlpgKs%2FJGIYj2Us9iBC6%2FH7IVieXfK2WeOprdHphYoPvzeBahzqpOfJar8bAwwjf4YexvOJJXoy%2BcFkuh7RxHz6IzSHWbcmNb3VeoRuTah%2FekmaU%2FGWmi28TnEkeSrwXJOQG6LccxqnZ54zZ5IMK8UtNJO8p%2BexyG8ZXsX%2Fu%2Ft4XcDPF1SmhPpPP1CWAO%2F3Q67Hx3VhvRy%2BPrsfs9L2MV7UvxhLG7%2BvL5TuzUkETWjNMQxFtPSHvtYeiQV9xqOQaquqAA%2BTEsSCtiVrN%2F8kjmpfDNX7xNEqJtV5DSRjAI6mGcDrmJ3lzc593DNeFkDXY6raNnmGYd0J3GinIP5P3RFVaOgmKhbxyv1P3BXJu79L3%2FeplU5V4ZyKKFwWFCspTfEPAg%2B71%2B6zwRTcBHGBDfmxdP5j0CimEOMCIhi5dggKSPOZvhj7WVU8DVpDZ5p%2BaovT7dOS4kZMGn78bUd1TVvdfXYv0FvOOFGvUS4YPWg9pJKJ%2Fn40C9VSFr2EJbMrzOs5%2FFEW6BAD%2Bks76upPjqHUrBy5HNHVOCGhIy9TpwP6y%2FzYomgabffVhhdYpmomX0wwsOSvQY6pgHfusoH3cWs%2F5Ellykyhg912lGIHVSeC%2FAFIi6WV%2F1e6hlv3sf0QlOSqdc8UYN7TEtTmIqX6Ftr6Ese66znCE%2BcU8em07cahgy8RnaL2QniCAvVy1eA4yz%2FppTkbtdNyAn8F98vgl4GsOdE81IQgDUDFq8LA5M1CRLSELq77a24gB90d53MY0%2BLtgK%2Fey6y9g82CAEZOPR5LYm2KXmghyLN8ALklNyu&X-Amz-Signature=5dd31d769da5087ac5136fc2bbd6cd2db397e62a9565fcbcf7ab039f9820c704&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5NYY4WX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIFTKCqfSeIUMLuhuEhP1QaUPr4w85A%2B1VBx5%2F92g7WXVAiBbTTm%2F6yDrPMdqLzqecz1h1rQbGOXraOb09YwsKf0nKir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMoydGRKgj9jcwedBYKtwDanFHHIC2vCfr42UQvNRiknJgaxQ1JNNaLbGzmIai0J%2BG0dZEfCQDpfj5ioKhXBdusoMKw3eZ4JR1nTD6TmjbaWtylKk1iWM3uD07u26b2G%2FhIpoimLndA9IzQBxphif%2BCGnmtYqbB%2FiRtOhDSUCk9pP03J0m0dPTn37ZP1xCVfEm1bdfK8UQelaMk%2BZPdiKAagdrhcIBFZmm6cMXeAs6MZOypDGb8sboG7vr9HDMgc3ZCKvC6I71lRTDI3CGQUbEGhYFx4fRIJsV50mJpazibPzNCq5A6SgmkGo7%2Fel1f1cpmRhRYXGKgE2BAIiUxu4F3HB5OOnTSY7N169TZJnZ5eDtLtdQip0eIHjVHnMBW%2Bnzcc2Kt3r8C16SecIz1LB%2BT861bR4a6Q6%2Bj%2FoRBvxbMeA27NGyoNy8mPDXxodq6tSYbyYcAfW2iGoAblSV14%2F29k5gD%2FehT8xBMIhLrQo9TFZ5Hvn0StD8ftaRB2Cn14CiWaeNXxOFhx1IV407p8F8atdBbGUqBR0SEvmAbI5fwfZUtVGZvXj0JSRh%2F6xA6CkeHeqMQlVccf2z5VHtbIT0errQWmLDtjSq0eSRD6aJiWLrDdz4wYOrSlxZAa7U8Qw7MydJ9kKaEZTlJvMwjsSSvQY6pgEdczeOSGCtoJ8qmthTLbvc0mlsvoh6qJyoeHbLB5aCLDDHoHn6P7hdbvBRldo7SsNtWj2VK2GBhaWpgHfYtlBv2jbEm43gX2kPiyPOAHEZsP54kEVKMCGDwzzt6A9O6n%2FByVvg1kTgkzqpTMDdt8lLmSXOBkEPf4LqQTsgecAAVCUCpPml3eJX5JpGUzKLWKpRCtsPGLnjj%2FNo%2BprG8m%2B%2BfDBmEBmu&X-Amz-Signature=18ff15cf7e303826e748b932fb7e80c529c25e7d323437d5f2f60379442d953c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5NYY4WX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIFTKCqfSeIUMLuhuEhP1QaUPr4w85A%2B1VBx5%2F92g7WXVAiBbTTm%2F6yDrPMdqLzqecz1h1rQbGOXraOb09YwsKf0nKir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMoydGRKgj9jcwedBYKtwDanFHHIC2vCfr42UQvNRiknJgaxQ1JNNaLbGzmIai0J%2BG0dZEfCQDpfj5ioKhXBdusoMKw3eZ4JR1nTD6TmjbaWtylKk1iWM3uD07u26b2G%2FhIpoimLndA9IzQBxphif%2BCGnmtYqbB%2FiRtOhDSUCk9pP03J0m0dPTn37ZP1xCVfEm1bdfK8UQelaMk%2BZPdiKAagdrhcIBFZmm6cMXeAs6MZOypDGb8sboG7vr9HDMgc3ZCKvC6I71lRTDI3CGQUbEGhYFx4fRIJsV50mJpazibPzNCq5A6SgmkGo7%2Fel1f1cpmRhRYXGKgE2BAIiUxu4F3HB5OOnTSY7N169TZJnZ5eDtLtdQip0eIHjVHnMBW%2Bnzcc2Kt3r8C16SecIz1LB%2BT861bR4a6Q6%2Bj%2FoRBvxbMeA27NGyoNy8mPDXxodq6tSYbyYcAfW2iGoAblSV14%2F29k5gD%2FehT8xBMIhLrQo9TFZ5Hvn0StD8ftaRB2Cn14CiWaeNXxOFhx1IV407p8F8atdBbGUqBR0SEvmAbI5fwfZUtVGZvXj0JSRh%2F6xA6CkeHeqMQlVccf2z5VHtbIT0errQWmLDtjSq0eSRD6aJiWLrDdz4wYOrSlxZAa7U8Qw7MydJ9kKaEZTlJvMwjsSSvQY6pgEdczeOSGCtoJ8qmthTLbvc0mlsvoh6qJyoeHbLB5aCLDDHoHn6P7hdbvBRldo7SsNtWj2VK2GBhaWpgHfYtlBv2jbEm43gX2kPiyPOAHEZsP54kEVKMCGDwzzt6A9O6n%2FByVvg1kTgkzqpTMDdt8lLmSXOBkEPf4LqQTsgecAAVCUCpPml3eJX5JpGUzKLWKpRCtsPGLnjj%2FNo%2BprG8m%2B%2BfDBmEBmu&X-Amz-Signature=595204430bf4b826153db7ab36de1dafa12758482a1f8605deda9797cebb3acc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5NYY4WX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIFTKCqfSeIUMLuhuEhP1QaUPr4w85A%2B1VBx5%2F92g7WXVAiBbTTm%2F6yDrPMdqLzqecz1h1rQbGOXraOb09YwsKf0nKir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMoydGRKgj9jcwedBYKtwDanFHHIC2vCfr42UQvNRiknJgaxQ1JNNaLbGzmIai0J%2BG0dZEfCQDpfj5ioKhXBdusoMKw3eZ4JR1nTD6TmjbaWtylKk1iWM3uD07u26b2G%2FhIpoimLndA9IzQBxphif%2BCGnmtYqbB%2FiRtOhDSUCk9pP03J0m0dPTn37ZP1xCVfEm1bdfK8UQelaMk%2BZPdiKAagdrhcIBFZmm6cMXeAs6MZOypDGb8sboG7vr9HDMgc3ZCKvC6I71lRTDI3CGQUbEGhYFx4fRIJsV50mJpazibPzNCq5A6SgmkGo7%2Fel1f1cpmRhRYXGKgE2BAIiUxu4F3HB5OOnTSY7N169TZJnZ5eDtLtdQip0eIHjVHnMBW%2Bnzcc2Kt3r8C16SecIz1LB%2BT861bR4a6Q6%2Bj%2FoRBvxbMeA27NGyoNy8mPDXxodq6tSYbyYcAfW2iGoAblSV14%2F29k5gD%2FehT8xBMIhLrQo9TFZ5Hvn0StD8ftaRB2Cn14CiWaeNXxOFhx1IV407p8F8atdBbGUqBR0SEvmAbI5fwfZUtVGZvXj0JSRh%2F6xA6CkeHeqMQlVccf2z5VHtbIT0errQWmLDtjSq0eSRD6aJiWLrDdz4wYOrSlxZAa7U8Qw7MydJ9kKaEZTlJvMwjsSSvQY6pgEdczeOSGCtoJ8qmthTLbvc0mlsvoh6qJyoeHbLB5aCLDDHoHn6P7hdbvBRldo7SsNtWj2VK2GBhaWpgHfYtlBv2jbEm43gX2kPiyPOAHEZsP54kEVKMCGDwzzt6A9O6n%2FByVvg1kTgkzqpTMDdt8lLmSXOBkEPf4LqQTsgecAAVCUCpPml3eJX5JpGUzKLWKpRCtsPGLnjj%2FNo%2BprG8m%2B%2BfDBmEBmu&X-Amz-Signature=456086c780c52d55d4360c3d7c60ed77d93bdee96c8091980c522966cd19ea02&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5NYY4WX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIFTKCqfSeIUMLuhuEhP1QaUPr4w85A%2B1VBx5%2F92g7WXVAiBbTTm%2F6yDrPMdqLzqecz1h1rQbGOXraOb09YwsKf0nKir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMoydGRKgj9jcwedBYKtwDanFHHIC2vCfr42UQvNRiknJgaxQ1JNNaLbGzmIai0J%2BG0dZEfCQDpfj5ioKhXBdusoMKw3eZ4JR1nTD6TmjbaWtylKk1iWM3uD07u26b2G%2FhIpoimLndA9IzQBxphif%2BCGnmtYqbB%2FiRtOhDSUCk9pP03J0m0dPTn37ZP1xCVfEm1bdfK8UQelaMk%2BZPdiKAagdrhcIBFZmm6cMXeAs6MZOypDGb8sboG7vr9HDMgc3ZCKvC6I71lRTDI3CGQUbEGhYFx4fRIJsV50mJpazibPzNCq5A6SgmkGo7%2Fel1f1cpmRhRYXGKgE2BAIiUxu4F3HB5OOnTSY7N169TZJnZ5eDtLtdQip0eIHjVHnMBW%2Bnzcc2Kt3r8C16SecIz1LB%2BT861bR4a6Q6%2Bj%2FoRBvxbMeA27NGyoNy8mPDXxodq6tSYbyYcAfW2iGoAblSV14%2F29k5gD%2FehT8xBMIhLrQo9TFZ5Hvn0StD8ftaRB2Cn14CiWaeNXxOFhx1IV407p8F8atdBbGUqBR0SEvmAbI5fwfZUtVGZvXj0JSRh%2F6xA6CkeHeqMQlVccf2z5VHtbIT0errQWmLDtjSq0eSRD6aJiWLrDdz4wYOrSlxZAa7U8Qw7MydJ9kKaEZTlJvMwjsSSvQY6pgEdczeOSGCtoJ8qmthTLbvc0mlsvoh6qJyoeHbLB5aCLDDHoHn6P7hdbvBRldo7SsNtWj2VK2GBhaWpgHfYtlBv2jbEm43gX2kPiyPOAHEZsP54kEVKMCGDwzzt6A9O6n%2FByVvg1kTgkzqpTMDdt8lLmSXOBkEPf4LqQTsgecAAVCUCpPml3eJX5JpGUzKLWKpRCtsPGLnjj%2FNo%2BprG8m%2B%2BfDBmEBmu&X-Amz-Signature=1f1e2a11b1ce5594eae60f8067212c8b55ede70cf2cd5eb35ffde200ce15cbaf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5NYY4WX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIFTKCqfSeIUMLuhuEhP1QaUPr4w85A%2B1VBx5%2F92g7WXVAiBbTTm%2F6yDrPMdqLzqecz1h1rQbGOXraOb09YwsKf0nKir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMoydGRKgj9jcwedBYKtwDanFHHIC2vCfr42UQvNRiknJgaxQ1JNNaLbGzmIai0J%2BG0dZEfCQDpfj5ioKhXBdusoMKw3eZ4JR1nTD6TmjbaWtylKk1iWM3uD07u26b2G%2FhIpoimLndA9IzQBxphif%2BCGnmtYqbB%2FiRtOhDSUCk9pP03J0m0dPTn37ZP1xCVfEm1bdfK8UQelaMk%2BZPdiKAagdrhcIBFZmm6cMXeAs6MZOypDGb8sboG7vr9HDMgc3ZCKvC6I71lRTDI3CGQUbEGhYFx4fRIJsV50mJpazibPzNCq5A6SgmkGo7%2Fel1f1cpmRhRYXGKgE2BAIiUxu4F3HB5OOnTSY7N169TZJnZ5eDtLtdQip0eIHjVHnMBW%2Bnzcc2Kt3r8C16SecIz1LB%2BT861bR4a6Q6%2Bj%2FoRBvxbMeA27NGyoNy8mPDXxodq6tSYbyYcAfW2iGoAblSV14%2F29k5gD%2FehT8xBMIhLrQo9TFZ5Hvn0StD8ftaRB2Cn14CiWaeNXxOFhx1IV407p8F8atdBbGUqBR0SEvmAbI5fwfZUtVGZvXj0JSRh%2F6xA6CkeHeqMQlVccf2z5VHtbIT0errQWmLDtjSq0eSRD6aJiWLrDdz4wYOrSlxZAa7U8Qw7MydJ9kKaEZTlJvMwjsSSvQY6pgEdczeOSGCtoJ8qmthTLbvc0mlsvoh6qJyoeHbLB5aCLDDHoHn6P7hdbvBRldo7SsNtWj2VK2GBhaWpgHfYtlBv2jbEm43gX2kPiyPOAHEZsP54kEVKMCGDwzzt6A9O6n%2FByVvg1kTgkzqpTMDdt8lLmSXOBkEPf4LqQTsgecAAVCUCpPml3eJX5JpGUzKLWKpRCtsPGLnjj%2FNo%2BprG8m%2B%2BfDBmEBmu&X-Amz-Signature=e56bebb1521ce5d52062c8901658192bf2cadb7d821aa5f7d7b1b7204d93f75e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZF2PUKR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIEFpEusa%2ByvqEB4Eutz4VebBstS66Yr%2BYtmtOMra%2FZ2AAiB%2FmnthXTVdhPeFkf1sW5bXD4tEqFGzk7j9oPoj0sZKtyr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMOsJGrVwnyTgmn47mKtwDjGFSDOyoki9i5qiciikhDsAg%2BG2igIorfBSmthO26dzwiFz54d%2BG9k7QQ3SlpgKs%2FJGIYj2Us9iBC6%2FH7IVieXfK2WeOprdHphYoPvzeBahzqpOfJar8bAwwjf4YexvOJJXoy%2BcFkuh7RxHz6IzSHWbcmNb3VeoRuTah%2FekmaU%2FGWmi28TnEkeSrwXJOQG6LccxqnZ54zZ5IMK8UtNJO8p%2BexyG8ZXsX%2Fu%2Ft4XcDPF1SmhPpPP1CWAO%2F3Q67Hx3VhvRy%2BPrsfs9L2MV7UvxhLG7%2BvL5TuzUkETWjNMQxFtPSHvtYeiQV9xqOQaquqAA%2BTEsSCtiVrN%2F8kjmpfDNX7xNEqJtV5DSRjAI6mGcDrmJ3lzc593DNeFkDXY6raNnmGYd0J3GinIP5P3RFVaOgmKhbxyv1P3BXJu79L3%2FeplU5V4ZyKKFwWFCspTfEPAg%2B71%2B6zwRTcBHGBDfmxdP5j0CimEOMCIhi5dggKSPOZvhj7WVU8DVpDZ5p%2BaovT7dOS4kZMGn78bUd1TVvdfXYv0FvOOFGvUS4YPWg9pJKJ%2Fn40C9VSFr2EJbMrzOs5%2FFEW6BAD%2Bks76upPjqHUrBy5HNHVOCGhIy9TpwP6y%2FzYomgabffVhhdYpmomX0wwsOSvQY6pgHfusoH3cWs%2F5Ellykyhg912lGIHVSeC%2FAFIi6WV%2F1e6hlv3sf0QlOSqdc8UYN7TEtTmIqX6Ftr6Ese66znCE%2BcU8em07cahgy8RnaL2QniCAvVy1eA4yz%2FppTkbtdNyAn8F98vgl4GsOdE81IQgDUDFq8LA5M1CRLSELq77a24gB90d53MY0%2BLtgK%2Fey6y9g82CAEZOPR5LYm2KXmghyLN8ALklNyu&X-Amz-Signature=5b1613653a5d49c63015727b6baddbd8dfa25c6b4e8e1c3025921f6a9b8035c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZF2PUKR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIEFpEusa%2ByvqEB4Eutz4VebBstS66Yr%2BYtmtOMra%2FZ2AAiB%2FmnthXTVdhPeFkf1sW5bXD4tEqFGzk7j9oPoj0sZKtyr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMOsJGrVwnyTgmn47mKtwDjGFSDOyoki9i5qiciikhDsAg%2BG2igIorfBSmthO26dzwiFz54d%2BG9k7QQ3SlpgKs%2FJGIYj2Us9iBC6%2FH7IVieXfK2WeOprdHphYoPvzeBahzqpOfJar8bAwwjf4YexvOJJXoy%2BcFkuh7RxHz6IzSHWbcmNb3VeoRuTah%2FekmaU%2FGWmi28TnEkeSrwXJOQG6LccxqnZ54zZ5IMK8UtNJO8p%2BexyG8ZXsX%2Fu%2Ft4XcDPF1SmhPpPP1CWAO%2F3Q67Hx3VhvRy%2BPrsfs9L2MV7UvxhLG7%2BvL5TuzUkETWjNMQxFtPSHvtYeiQV9xqOQaquqAA%2BTEsSCtiVrN%2F8kjmpfDNX7xNEqJtV5DSRjAI6mGcDrmJ3lzc593DNeFkDXY6raNnmGYd0J3GinIP5P3RFVaOgmKhbxyv1P3BXJu79L3%2FeplU5V4ZyKKFwWFCspTfEPAg%2B71%2B6zwRTcBHGBDfmxdP5j0CimEOMCIhi5dggKSPOZvhj7WVU8DVpDZ5p%2BaovT7dOS4kZMGn78bUd1TVvdfXYv0FvOOFGvUS4YPWg9pJKJ%2Fn40C9VSFr2EJbMrzOs5%2FFEW6BAD%2Bks76upPjqHUrBy5HNHVOCGhIy9TpwP6y%2FzYomgabffVhhdYpmomX0wwsOSvQY6pgHfusoH3cWs%2F5Ellykyhg912lGIHVSeC%2FAFIi6WV%2F1e6hlv3sf0QlOSqdc8UYN7TEtTmIqX6Ftr6Ese66znCE%2BcU8em07cahgy8RnaL2QniCAvVy1eA4yz%2FppTkbtdNyAn8F98vgl4GsOdE81IQgDUDFq8LA5M1CRLSELq77a24gB90d53MY0%2BLtgK%2Fey6y9g82CAEZOPR5LYm2KXmghyLN8ALklNyu&X-Amz-Signature=585495ade3e6a060b0bce074fa2b1a9159356c82e8ead9ad304ec1f3a7833062&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZF2PUKR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIEFpEusa%2ByvqEB4Eutz4VebBstS66Yr%2BYtmtOMra%2FZ2AAiB%2FmnthXTVdhPeFkf1sW5bXD4tEqFGzk7j9oPoj0sZKtyr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMOsJGrVwnyTgmn47mKtwDjGFSDOyoki9i5qiciikhDsAg%2BG2igIorfBSmthO26dzwiFz54d%2BG9k7QQ3SlpgKs%2FJGIYj2Us9iBC6%2FH7IVieXfK2WeOprdHphYoPvzeBahzqpOfJar8bAwwjf4YexvOJJXoy%2BcFkuh7RxHz6IzSHWbcmNb3VeoRuTah%2FekmaU%2FGWmi28TnEkeSrwXJOQG6LccxqnZ54zZ5IMK8UtNJO8p%2BexyG8ZXsX%2Fu%2Ft4XcDPF1SmhPpPP1CWAO%2F3Q67Hx3VhvRy%2BPrsfs9L2MV7UvxhLG7%2BvL5TuzUkETWjNMQxFtPSHvtYeiQV9xqOQaquqAA%2BTEsSCtiVrN%2F8kjmpfDNX7xNEqJtV5DSRjAI6mGcDrmJ3lzc593DNeFkDXY6raNnmGYd0J3GinIP5P3RFVaOgmKhbxyv1P3BXJu79L3%2FeplU5V4ZyKKFwWFCspTfEPAg%2B71%2B6zwRTcBHGBDfmxdP5j0CimEOMCIhi5dggKSPOZvhj7WVU8DVpDZ5p%2BaovT7dOS4kZMGn78bUd1TVvdfXYv0FvOOFGvUS4YPWg9pJKJ%2Fn40C9VSFr2EJbMrzOs5%2FFEW6BAD%2Bks76upPjqHUrBy5HNHVOCGhIy9TpwP6y%2FzYomgabffVhhdYpmomX0wwsOSvQY6pgHfusoH3cWs%2F5Ellykyhg912lGIHVSeC%2FAFIi6WV%2F1e6hlv3sf0QlOSqdc8UYN7TEtTmIqX6Ftr6Ese66znCE%2BcU8em07cahgy8RnaL2QniCAvVy1eA4yz%2FppTkbtdNyAn8F98vgl4GsOdE81IQgDUDFq8LA5M1CRLSELq77a24gB90d53MY0%2BLtgK%2Fey6y9g82CAEZOPR5LYm2KXmghyLN8ALklNyu&X-Amz-Signature=a3a47a9143d36383140e9e1f4caea3b925cd4a174956dbab91303cfb4859fb1f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZF2PUKR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIEFpEusa%2ByvqEB4Eutz4VebBstS66Yr%2BYtmtOMra%2FZ2AAiB%2FmnthXTVdhPeFkf1sW5bXD4tEqFGzk7j9oPoj0sZKtyr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMOsJGrVwnyTgmn47mKtwDjGFSDOyoki9i5qiciikhDsAg%2BG2igIorfBSmthO26dzwiFz54d%2BG9k7QQ3SlpgKs%2FJGIYj2Us9iBC6%2FH7IVieXfK2WeOprdHphYoPvzeBahzqpOfJar8bAwwjf4YexvOJJXoy%2BcFkuh7RxHz6IzSHWbcmNb3VeoRuTah%2FekmaU%2FGWmi28TnEkeSrwXJOQG6LccxqnZ54zZ5IMK8UtNJO8p%2BexyG8ZXsX%2Fu%2Ft4XcDPF1SmhPpPP1CWAO%2F3Q67Hx3VhvRy%2BPrsfs9L2MV7UvxhLG7%2BvL5TuzUkETWjNMQxFtPSHvtYeiQV9xqOQaquqAA%2BTEsSCtiVrN%2F8kjmpfDNX7xNEqJtV5DSRjAI6mGcDrmJ3lzc593DNeFkDXY6raNnmGYd0J3GinIP5P3RFVaOgmKhbxyv1P3BXJu79L3%2FeplU5V4ZyKKFwWFCspTfEPAg%2B71%2B6zwRTcBHGBDfmxdP5j0CimEOMCIhi5dggKSPOZvhj7WVU8DVpDZ5p%2BaovT7dOS4kZMGn78bUd1TVvdfXYv0FvOOFGvUS4YPWg9pJKJ%2Fn40C9VSFr2EJbMrzOs5%2FFEW6BAD%2Bks76upPjqHUrBy5HNHVOCGhIy9TpwP6y%2FzYomgabffVhhdYpmomX0wwsOSvQY6pgHfusoH3cWs%2F5Ellykyhg912lGIHVSeC%2FAFIi6WV%2F1e6hlv3sf0QlOSqdc8UYN7TEtTmIqX6Ftr6Ese66znCE%2BcU8em07cahgy8RnaL2QniCAvVy1eA4yz%2FppTkbtdNyAn8F98vgl4GsOdE81IQgDUDFq8LA5M1CRLSELq77a24gB90d53MY0%2BLtgK%2Fey6y9g82CAEZOPR5LYm2KXmghyLN8ALklNyu&X-Amz-Signature=e404dae68732cd276f7145a94d480cdeb6fee839c7a3509b684ef1748e253ba5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZF2PUKR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIEFpEusa%2ByvqEB4Eutz4VebBstS66Yr%2BYtmtOMra%2FZ2AAiB%2FmnthXTVdhPeFkf1sW5bXD4tEqFGzk7j9oPoj0sZKtyr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMOsJGrVwnyTgmn47mKtwDjGFSDOyoki9i5qiciikhDsAg%2BG2igIorfBSmthO26dzwiFz54d%2BG9k7QQ3SlpgKs%2FJGIYj2Us9iBC6%2FH7IVieXfK2WeOprdHphYoPvzeBahzqpOfJar8bAwwjf4YexvOJJXoy%2BcFkuh7RxHz6IzSHWbcmNb3VeoRuTah%2FekmaU%2FGWmi28TnEkeSrwXJOQG6LccxqnZ54zZ5IMK8UtNJO8p%2BexyG8ZXsX%2Fu%2Ft4XcDPF1SmhPpPP1CWAO%2F3Q67Hx3VhvRy%2BPrsfs9L2MV7UvxhLG7%2BvL5TuzUkETWjNMQxFtPSHvtYeiQV9xqOQaquqAA%2BTEsSCtiVrN%2F8kjmpfDNX7xNEqJtV5DSRjAI6mGcDrmJ3lzc593DNeFkDXY6raNnmGYd0J3GinIP5P3RFVaOgmKhbxyv1P3BXJu79L3%2FeplU5V4ZyKKFwWFCspTfEPAg%2B71%2B6zwRTcBHGBDfmxdP5j0CimEOMCIhi5dggKSPOZvhj7WVU8DVpDZ5p%2BaovT7dOS4kZMGn78bUd1TVvdfXYv0FvOOFGvUS4YPWg9pJKJ%2Fn40C9VSFr2EJbMrzOs5%2FFEW6BAD%2Bks76upPjqHUrBy5HNHVOCGhIy9TpwP6y%2FzYomgabffVhhdYpmomX0wwsOSvQY6pgHfusoH3cWs%2F5Ellykyhg912lGIHVSeC%2FAFIi6WV%2F1e6hlv3sf0QlOSqdc8UYN7TEtTmIqX6Ftr6Ese66znCE%2BcU8em07cahgy8RnaL2QniCAvVy1eA4yz%2FppTkbtdNyAn8F98vgl4GsOdE81IQgDUDFq8LA5M1CRLSELq77a24gB90d53MY0%2BLtgK%2Fey6y9g82CAEZOPR5LYm2KXmghyLN8ALklNyu&X-Amz-Signature=f6d6ed404569db6e9a31e98bee77030a4235788aefa695b967dff94ea0ee3519&X-Amz-SignedHeaders=host&x-id=GetObject)
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


