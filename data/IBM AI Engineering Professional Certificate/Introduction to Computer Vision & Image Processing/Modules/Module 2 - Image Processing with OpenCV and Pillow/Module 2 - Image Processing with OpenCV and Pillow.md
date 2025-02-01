

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466353DYTDO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYg1ZtR6%2BX4TU0r%2FmxHHTQ6AktbbjfEtllOdZDRhodXAiEA0W0EGi%2BI5i9xQEVhsUOUcs1uU%2BvHKc%2FZeQ7i7PEHbl8qiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNrU7B9hkqD1viPoyrcA0mb0DC%2BpqgtNvhssee8FR9vs6x58PtGPrnMGRM2gyQLiWk6cofMP8xE1FRl5dZGcBME17Q92532oV3QXFlBm7jUpJtV%2F8cye%2BA02FO6zuUIvH0kQV7R0UNvHvrhguxHVF8q%2B4v7X9dye9mRPXdEOYEADwCuQadL%2BRZNZa0qKWGldHyqlVZkYn3y7opVQR71p%2Bo65gIzJIezzBaqGn%2F8l%2B5KhOfZH%2BzcET3L8onZvbFLBv0rTnTL4otn4SqjA9goqU4pC1aW2PQTJbqkzWDUbbW%2F4%2FDjvegtnQPg72rq%2Fcbi6JakEFR0Ejin74a3Ft9vPg4RqWR57vzGV37ZcYPnSxCI6yHrPDS2iyaU5gr25uF%2FMc1O71RpbS%2BrQ29JEj%2B2GYYXnIaXGf3ziN7s5YHgklmXElYV6RNbe0Bjv6jzZR6vifWcSqwQIZ%2BspY8tq02KGFbccfP6I8mg7gN5FS1BSVMUoPGDtxpgkRba2iyZ%2FH7KCFR7UwzYU1xoW%2BAJqumS%2FTLOrZ4ffSmgdWTVVbu8OVgkIdyMV77ZvTW%2FLpJkXN8ve%2FkmaLwvYh%2BYRhg%2BAEmASikKOCCr39SblaiBq1zyJqg%2Bxdjm5qEC%2FRq%2FUMuJ3FVpPyT%2FSlE26uup2h1CMPb59rwGOqUBEAOEoLn3z7B4kb3D1MsoHisLVHQi%2BGhowpgW%2Bf7opBU298x2d%2FwkiFTmdRz5rJXi%2FQ6LDmmcemxwL3heKxkvAJncmDTTmpU90tmOkrU75aeMxgaRAfdSekcPpoJ3JiWSRRpF86X0I5kx3g5vbqfPnZ9mJISdDBQWYiWDbt088kXlE9OHOK3pEftN3kvl94Fx7oQD5cye86G0n2YpSC9gYnkvUVff&X-Amz-Signature=fce97bf119ded730ff32b4605fdf0ec265f293b34e3efa781f5a5711cd4efa79&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YNUBLTF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0lUwSo3z6cuKBbDSeh9vEc9ZdWwKw2x65IsNiyB5r8wIhANfSVQBjPGwfxj1PBmdy6PkNpipa1bZ8AcS8KTw5L7krKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLE1ekQrUo5h4lHRYq3AMjH1OFIJIKZPL3i833IFhbx03JBwi9oCQm%2Bwf6hVgeZhc9l13V2cTpgGFsIenNOvBkhSeW3qB%2FWnsa7VAEDtQzgablr3we2RSc8nZj%2Bf4FDziFqFBIM%2FHm5d2i1EbLAoGBiCvUQCDCLb26piobuphw6IVz%2BD0ua7iauqDtpHLxpIYvEQOa0RXJPIzJ89kyjaZN%2FbjtTwKwYROw3bj%2BTXtpNl7M1KNmn7AKUQtJxetbdxjPFmn5Axy7O1Lk22uLUYZ93NdIWnsrE34JYsQUorjHwDf6Drcplkb7I4NF8Ur3kRRlJCPrMu9iQDzYk2u%2BXrdjKt8u8Y7UJzgjMejURiIaMfkXvp39tJVIIwU%2F8H3YAg8gUQmia3ZOuZtsaJkg%2BFGn%2BOgNtg%2FaQG7pRB0rjzOaeYUPqLDrZ3FXjEmzW0zqAbkWwf5Kcj0Qw5c9XnHprfdwrnag%2F6oZ44JD8m0xSctmzNz49MBixG5wxFXFc%2BqqThg0PLPM2AC%2FbWbW%2BV1NOwyAbrb%2B4tQ8PPGnZ80hHQUouF0jHY6roUKSw2fNpB4MKHkhzbLnkTuPqz0ABJgX%2FQgyohmhFhAMi7qSwHuh7BUjANVTtJSPvT%2FMddxfSLL7TzNXI3%2FkL3ZEd0vwKjC9%2Bfa8BjqkAR%2FXXMbPJSt6BtnTPBxSCGmGlMYKwggG1ZDq9iLjuzq%2FKasKxMKEr6xaNXMbbbMyxYYTrfntU13fqHPN05pv6dKUWdWhzYkxL23hhUnvrLyHeCfZm5Lvjb8ij3PXKKxcW3x8%2BwZKeKHkJoU5nN1F5lS0i8FN1VlYDKr8Q0y0sQp0qONWvZ4VSG6dnjF4%2FaetV0U6wG3psR35t3iHQqRK8iYAx0C4&X-Amz-Signature=48cf37c5fb460a40d5b221d27567c57e15cc46d0f469f0e7dc158b05b579ebe1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YNUBLTF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0lUwSo3z6cuKBbDSeh9vEc9ZdWwKw2x65IsNiyB5r8wIhANfSVQBjPGwfxj1PBmdy6PkNpipa1bZ8AcS8KTw5L7krKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLE1ekQrUo5h4lHRYq3AMjH1OFIJIKZPL3i833IFhbx03JBwi9oCQm%2Bwf6hVgeZhc9l13V2cTpgGFsIenNOvBkhSeW3qB%2FWnsa7VAEDtQzgablr3we2RSc8nZj%2Bf4FDziFqFBIM%2FHm5d2i1EbLAoGBiCvUQCDCLb26piobuphw6IVz%2BD0ua7iauqDtpHLxpIYvEQOa0RXJPIzJ89kyjaZN%2FbjtTwKwYROw3bj%2BTXtpNl7M1KNmn7AKUQtJxetbdxjPFmn5Axy7O1Lk22uLUYZ93NdIWnsrE34JYsQUorjHwDf6Drcplkb7I4NF8Ur3kRRlJCPrMu9iQDzYk2u%2BXrdjKt8u8Y7UJzgjMejURiIaMfkXvp39tJVIIwU%2F8H3YAg8gUQmia3ZOuZtsaJkg%2BFGn%2BOgNtg%2FaQG7pRB0rjzOaeYUPqLDrZ3FXjEmzW0zqAbkWwf5Kcj0Qw5c9XnHprfdwrnag%2F6oZ44JD8m0xSctmzNz49MBixG5wxFXFc%2BqqThg0PLPM2AC%2FbWbW%2BV1NOwyAbrb%2B4tQ8PPGnZ80hHQUouF0jHY6roUKSw2fNpB4MKHkhzbLnkTuPqz0ABJgX%2FQgyohmhFhAMi7qSwHuh7BUjANVTtJSPvT%2FMddxfSLL7TzNXI3%2FkL3ZEd0vwKjC9%2Bfa8BjqkAR%2FXXMbPJSt6BtnTPBxSCGmGlMYKwggG1ZDq9iLjuzq%2FKasKxMKEr6xaNXMbbbMyxYYTrfntU13fqHPN05pv6dKUWdWhzYkxL23hhUnvrLyHeCfZm5Lvjb8ij3PXKKxcW3x8%2BwZKeKHkJoU5nN1F5lS0i8FN1VlYDKr8Q0y0sQp0qONWvZ4VSG6dnjF4%2FaetV0U6wG3psR35t3iHQqRK8iYAx0C4&X-Amz-Signature=be3ffbca3082e80b20e32dc6e4bfdbdc4596ff4dcbf1ff78b4918b01e57b2c30&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YNUBLTF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0lUwSo3z6cuKBbDSeh9vEc9ZdWwKw2x65IsNiyB5r8wIhANfSVQBjPGwfxj1PBmdy6PkNpipa1bZ8AcS8KTw5L7krKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLE1ekQrUo5h4lHRYq3AMjH1OFIJIKZPL3i833IFhbx03JBwi9oCQm%2Bwf6hVgeZhc9l13V2cTpgGFsIenNOvBkhSeW3qB%2FWnsa7VAEDtQzgablr3we2RSc8nZj%2Bf4FDziFqFBIM%2FHm5d2i1EbLAoGBiCvUQCDCLb26piobuphw6IVz%2BD0ua7iauqDtpHLxpIYvEQOa0RXJPIzJ89kyjaZN%2FbjtTwKwYROw3bj%2BTXtpNl7M1KNmn7AKUQtJxetbdxjPFmn5Axy7O1Lk22uLUYZ93NdIWnsrE34JYsQUorjHwDf6Drcplkb7I4NF8Ur3kRRlJCPrMu9iQDzYk2u%2BXrdjKt8u8Y7UJzgjMejURiIaMfkXvp39tJVIIwU%2F8H3YAg8gUQmia3ZOuZtsaJkg%2BFGn%2BOgNtg%2FaQG7pRB0rjzOaeYUPqLDrZ3FXjEmzW0zqAbkWwf5Kcj0Qw5c9XnHprfdwrnag%2F6oZ44JD8m0xSctmzNz49MBixG5wxFXFc%2BqqThg0PLPM2AC%2FbWbW%2BV1NOwyAbrb%2B4tQ8PPGnZ80hHQUouF0jHY6roUKSw2fNpB4MKHkhzbLnkTuPqz0ABJgX%2FQgyohmhFhAMi7qSwHuh7BUjANVTtJSPvT%2FMddxfSLL7TzNXI3%2FkL3ZEd0vwKjC9%2Bfa8BjqkAR%2FXXMbPJSt6BtnTPBxSCGmGlMYKwggG1ZDq9iLjuzq%2FKasKxMKEr6xaNXMbbbMyxYYTrfntU13fqHPN05pv6dKUWdWhzYkxL23hhUnvrLyHeCfZm5Lvjb8ij3PXKKxcW3x8%2BwZKeKHkJoU5nN1F5lS0i8FN1VlYDKr8Q0y0sQp0qONWvZ4VSG6dnjF4%2FaetV0U6wG3psR35t3iHQqRK8iYAx0C4&X-Amz-Signature=68523a84fc5bf170338ef91b595284b34daf0ef91a21f2db9a9681f8b672c022&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YNUBLTF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0lUwSo3z6cuKBbDSeh9vEc9ZdWwKw2x65IsNiyB5r8wIhANfSVQBjPGwfxj1PBmdy6PkNpipa1bZ8AcS8KTw5L7krKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLE1ekQrUo5h4lHRYq3AMjH1OFIJIKZPL3i833IFhbx03JBwi9oCQm%2Bwf6hVgeZhc9l13V2cTpgGFsIenNOvBkhSeW3qB%2FWnsa7VAEDtQzgablr3we2RSc8nZj%2Bf4FDziFqFBIM%2FHm5d2i1EbLAoGBiCvUQCDCLb26piobuphw6IVz%2BD0ua7iauqDtpHLxpIYvEQOa0RXJPIzJ89kyjaZN%2FbjtTwKwYROw3bj%2BTXtpNl7M1KNmn7AKUQtJxetbdxjPFmn5Axy7O1Lk22uLUYZ93NdIWnsrE34JYsQUorjHwDf6Drcplkb7I4NF8Ur3kRRlJCPrMu9iQDzYk2u%2BXrdjKt8u8Y7UJzgjMejURiIaMfkXvp39tJVIIwU%2F8H3YAg8gUQmia3ZOuZtsaJkg%2BFGn%2BOgNtg%2FaQG7pRB0rjzOaeYUPqLDrZ3FXjEmzW0zqAbkWwf5Kcj0Qw5c9XnHprfdwrnag%2F6oZ44JD8m0xSctmzNz49MBixG5wxFXFc%2BqqThg0PLPM2AC%2FbWbW%2BV1NOwyAbrb%2B4tQ8PPGnZ80hHQUouF0jHY6roUKSw2fNpB4MKHkhzbLnkTuPqz0ABJgX%2FQgyohmhFhAMi7qSwHuh7BUjANVTtJSPvT%2FMddxfSLL7TzNXI3%2FkL3ZEd0vwKjC9%2Bfa8BjqkAR%2FXXMbPJSt6BtnTPBxSCGmGlMYKwggG1ZDq9iLjuzq%2FKasKxMKEr6xaNXMbbbMyxYYTrfntU13fqHPN05pv6dKUWdWhzYkxL23hhUnvrLyHeCfZm5Lvjb8ij3PXKKxcW3x8%2BwZKeKHkJoU5nN1F5lS0i8FN1VlYDKr8Q0y0sQp0qONWvZ4VSG6dnjF4%2FaetV0U6wG3psR35t3iHQqRK8iYAx0C4&X-Amz-Signature=709197a580ca3f5c45181b6fe41bfc49740d581226ab9b9c50ea92001b53c11c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YNUBLTF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0lUwSo3z6cuKBbDSeh9vEc9ZdWwKw2x65IsNiyB5r8wIhANfSVQBjPGwfxj1PBmdy6PkNpipa1bZ8AcS8KTw5L7krKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLE1ekQrUo5h4lHRYq3AMjH1OFIJIKZPL3i833IFhbx03JBwi9oCQm%2Bwf6hVgeZhc9l13V2cTpgGFsIenNOvBkhSeW3qB%2FWnsa7VAEDtQzgablr3we2RSc8nZj%2Bf4FDziFqFBIM%2FHm5d2i1EbLAoGBiCvUQCDCLb26piobuphw6IVz%2BD0ua7iauqDtpHLxpIYvEQOa0RXJPIzJ89kyjaZN%2FbjtTwKwYROw3bj%2BTXtpNl7M1KNmn7AKUQtJxetbdxjPFmn5Axy7O1Lk22uLUYZ93NdIWnsrE34JYsQUorjHwDf6Drcplkb7I4NF8Ur3kRRlJCPrMu9iQDzYk2u%2BXrdjKt8u8Y7UJzgjMejURiIaMfkXvp39tJVIIwU%2F8H3YAg8gUQmia3ZOuZtsaJkg%2BFGn%2BOgNtg%2FaQG7pRB0rjzOaeYUPqLDrZ3FXjEmzW0zqAbkWwf5Kcj0Qw5c9XnHprfdwrnag%2F6oZ44JD8m0xSctmzNz49MBixG5wxFXFc%2BqqThg0PLPM2AC%2FbWbW%2BV1NOwyAbrb%2B4tQ8PPGnZ80hHQUouF0jHY6roUKSw2fNpB4MKHkhzbLnkTuPqz0ABJgX%2FQgyohmhFhAMi7qSwHuh7BUjANVTtJSPvT%2FMddxfSLL7TzNXI3%2FkL3ZEd0vwKjC9%2Bfa8BjqkAR%2FXXMbPJSt6BtnTPBxSCGmGlMYKwggG1ZDq9iLjuzq%2FKasKxMKEr6xaNXMbbbMyxYYTrfntU13fqHPN05pv6dKUWdWhzYkxL23hhUnvrLyHeCfZm5Lvjb8ij3PXKKxcW3x8%2BwZKeKHkJoU5nN1F5lS0i8FN1VlYDKr8Q0y0sQp0qONWvZ4VSG6dnjF4%2FaetV0U6wG3psR35t3iHQqRK8iYAx0C4&X-Amz-Signature=6bf07ad2204dc887cdc6d6541bb22b38671c6c6512c241c085cf4bc97219930f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466353DYTDO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYg1ZtR6%2BX4TU0r%2FmxHHTQ6AktbbjfEtllOdZDRhodXAiEA0W0EGi%2BI5i9xQEVhsUOUcs1uU%2BvHKc%2FZeQ7i7PEHbl8qiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNrU7B9hkqD1viPoyrcA0mb0DC%2BpqgtNvhssee8FR9vs6x58PtGPrnMGRM2gyQLiWk6cofMP8xE1FRl5dZGcBME17Q92532oV3QXFlBm7jUpJtV%2F8cye%2BA02FO6zuUIvH0kQV7R0UNvHvrhguxHVF8q%2B4v7X9dye9mRPXdEOYEADwCuQadL%2BRZNZa0qKWGldHyqlVZkYn3y7opVQR71p%2Bo65gIzJIezzBaqGn%2F8l%2B5KhOfZH%2BzcET3L8onZvbFLBv0rTnTL4otn4SqjA9goqU4pC1aW2PQTJbqkzWDUbbW%2F4%2FDjvegtnQPg72rq%2Fcbi6JakEFR0Ejin74a3Ft9vPg4RqWR57vzGV37ZcYPnSxCI6yHrPDS2iyaU5gr25uF%2FMc1O71RpbS%2BrQ29JEj%2B2GYYXnIaXGf3ziN7s5YHgklmXElYV6RNbe0Bjv6jzZR6vifWcSqwQIZ%2BspY8tq02KGFbccfP6I8mg7gN5FS1BSVMUoPGDtxpgkRba2iyZ%2FH7KCFR7UwzYU1xoW%2BAJqumS%2FTLOrZ4ffSmgdWTVVbu8OVgkIdyMV77ZvTW%2FLpJkXN8ve%2FkmaLwvYh%2BYRhg%2BAEmASikKOCCr39SblaiBq1zyJqg%2Bxdjm5qEC%2FRq%2FUMuJ3FVpPyT%2FSlE26uup2h1CMPb59rwGOqUBEAOEoLn3z7B4kb3D1MsoHisLVHQi%2BGhowpgW%2Bf7opBU298x2d%2FwkiFTmdRz5rJXi%2FQ6LDmmcemxwL3heKxkvAJncmDTTmpU90tmOkrU75aeMxgaRAfdSekcPpoJ3JiWSRRpF86X0I5kx3g5vbqfPnZ9mJISdDBQWYiWDbt088kXlE9OHOK3pEftN3kvl94Fx7oQD5cye86G0n2YpSC9gYnkvUVff&X-Amz-Signature=5b1ae8c800e65f8d37d8a35d03aeaf19b9a643c6fa47111fc0f10f5c411a18be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466353DYTDO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYg1ZtR6%2BX4TU0r%2FmxHHTQ6AktbbjfEtllOdZDRhodXAiEA0W0EGi%2BI5i9xQEVhsUOUcs1uU%2BvHKc%2FZeQ7i7PEHbl8qiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNrU7B9hkqD1viPoyrcA0mb0DC%2BpqgtNvhssee8FR9vs6x58PtGPrnMGRM2gyQLiWk6cofMP8xE1FRl5dZGcBME17Q92532oV3QXFlBm7jUpJtV%2F8cye%2BA02FO6zuUIvH0kQV7R0UNvHvrhguxHVF8q%2B4v7X9dye9mRPXdEOYEADwCuQadL%2BRZNZa0qKWGldHyqlVZkYn3y7opVQR71p%2Bo65gIzJIezzBaqGn%2F8l%2B5KhOfZH%2BzcET3L8onZvbFLBv0rTnTL4otn4SqjA9goqU4pC1aW2PQTJbqkzWDUbbW%2F4%2FDjvegtnQPg72rq%2Fcbi6JakEFR0Ejin74a3Ft9vPg4RqWR57vzGV37ZcYPnSxCI6yHrPDS2iyaU5gr25uF%2FMc1O71RpbS%2BrQ29JEj%2B2GYYXnIaXGf3ziN7s5YHgklmXElYV6RNbe0Bjv6jzZR6vifWcSqwQIZ%2BspY8tq02KGFbccfP6I8mg7gN5FS1BSVMUoPGDtxpgkRba2iyZ%2FH7KCFR7UwzYU1xoW%2BAJqumS%2FTLOrZ4ffSmgdWTVVbu8OVgkIdyMV77ZvTW%2FLpJkXN8ve%2FkmaLwvYh%2BYRhg%2BAEmASikKOCCr39SblaiBq1zyJqg%2Bxdjm5qEC%2FRq%2FUMuJ3FVpPyT%2FSlE26uup2h1CMPb59rwGOqUBEAOEoLn3z7B4kb3D1MsoHisLVHQi%2BGhowpgW%2Bf7opBU298x2d%2FwkiFTmdRz5rJXi%2FQ6LDmmcemxwL3heKxkvAJncmDTTmpU90tmOkrU75aeMxgaRAfdSekcPpoJ3JiWSRRpF86X0I5kx3g5vbqfPnZ9mJISdDBQWYiWDbt088kXlE9OHOK3pEftN3kvl94Fx7oQD5cye86G0n2YpSC9gYnkvUVff&X-Amz-Signature=af0c84fb43742e2c630ac6be8f0c05b31b598c3c579073fb0fb2a7e4ba0a922e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466353DYTDO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYg1ZtR6%2BX4TU0r%2FmxHHTQ6AktbbjfEtllOdZDRhodXAiEA0W0EGi%2BI5i9xQEVhsUOUcs1uU%2BvHKc%2FZeQ7i7PEHbl8qiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNrU7B9hkqD1viPoyrcA0mb0DC%2BpqgtNvhssee8FR9vs6x58PtGPrnMGRM2gyQLiWk6cofMP8xE1FRl5dZGcBME17Q92532oV3QXFlBm7jUpJtV%2F8cye%2BA02FO6zuUIvH0kQV7R0UNvHvrhguxHVF8q%2B4v7X9dye9mRPXdEOYEADwCuQadL%2BRZNZa0qKWGldHyqlVZkYn3y7opVQR71p%2Bo65gIzJIezzBaqGn%2F8l%2B5KhOfZH%2BzcET3L8onZvbFLBv0rTnTL4otn4SqjA9goqU4pC1aW2PQTJbqkzWDUbbW%2F4%2FDjvegtnQPg72rq%2Fcbi6JakEFR0Ejin74a3Ft9vPg4RqWR57vzGV37ZcYPnSxCI6yHrPDS2iyaU5gr25uF%2FMc1O71RpbS%2BrQ29JEj%2B2GYYXnIaXGf3ziN7s5YHgklmXElYV6RNbe0Bjv6jzZR6vifWcSqwQIZ%2BspY8tq02KGFbccfP6I8mg7gN5FS1BSVMUoPGDtxpgkRba2iyZ%2FH7KCFR7UwzYU1xoW%2BAJqumS%2FTLOrZ4ffSmgdWTVVbu8OVgkIdyMV77ZvTW%2FLpJkXN8ve%2FkmaLwvYh%2BYRhg%2BAEmASikKOCCr39SblaiBq1zyJqg%2Bxdjm5qEC%2FRq%2FUMuJ3FVpPyT%2FSlE26uup2h1CMPb59rwGOqUBEAOEoLn3z7B4kb3D1MsoHisLVHQi%2BGhowpgW%2Bf7opBU298x2d%2FwkiFTmdRz5rJXi%2FQ6LDmmcemxwL3heKxkvAJncmDTTmpU90tmOkrU75aeMxgaRAfdSekcPpoJ3JiWSRRpF86X0I5kx3g5vbqfPnZ9mJISdDBQWYiWDbt088kXlE9OHOK3pEftN3kvl94Fx7oQD5cye86G0n2YpSC9gYnkvUVff&X-Amz-Signature=6650f8b9cc98567e9488b777d6ae89301dd6c96720dae7192c77f67c66e96beb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466353DYTDO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYg1ZtR6%2BX4TU0r%2FmxHHTQ6AktbbjfEtllOdZDRhodXAiEA0W0EGi%2BI5i9xQEVhsUOUcs1uU%2BvHKc%2FZeQ7i7PEHbl8qiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNrU7B9hkqD1viPoyrcA0mb0DC%2BpqgtNvhssee8FR9vs6x58PtGPrnMGRM2gyQLiWk6cofMP8xE1FRl5dZGcBME17Q92532oV3QXFlBm7jUpJtV%2F8cye%2BA02FO6zuUIvH0kQV7R0UNvHvrhguxHVF8q%2B4v7X9dye9mRPXdEOYEADwCuQadL%2BRZNZa0qKWGldHyqlVZkYn3y7opVQR71p%2Bo65gIzJIezzBaqGn%2F8l%2B5KhOfZH%2BzcET3L8onZvbFLBv0rTnTL4otn4SqjA9goqU4pC1aW2PQTJbqkzWDUbbW%2F4%2FDjvegtnQPg72rq%2Fcbi6JakEFR0Ejin74a3Ft9vPg4RqWR57vzGV37ZcYPnSxCI6yHrPDS2iyaU5gr25uF%2FMc1O71RpbS%2BrQ29JEj%2B2GYYXnIaXGf3ziN7s5YHgklmXElYV6RNbe0Bjv6jzZR6vifWcSqwQIZ%2BspY8tq02KGFbccfP6I8mg7gN5FS1BSVMUoPGDtxpgkRba2iyZ%2FH7KCFR7UwzYU1xoW%2BAJqumS%2FTLOrZ4ffSmgdWTVVbu8OVgkIdyMV77ZvTW%2FLpJkXN8ve%2FkmaLwvYh%2BYRhg%2BAEmASikKOCCr39SblaiBq1zyJqg%2Bxdjm5qEC%2FRq%2FUMuJ3FVpPyT%2FSlE26uup2h1CMPb59rwGOqUBEAOEoLn3z7B4kb3D1MsoHisLVHQi%2BGhowpgW%2Bf7opBU298x2d%2FwkiFTmdRz5rJXi%2FQ6LDmmcemxwL3heKxkvAJncmDTTmpU90tmOkrU75aeMxgaRAfdSekcPpoJ3JiWSRRpF86X0I5kx3g5vbqfPnZ9mJISdDBQWYiWDbt088kXlE9OHOK3pEftN3kvl94Fx7oQD5cye86G0n2YpSC9gYnkvUVff&X-Amz-Signature=c2beaf90d6ec3ece6aaf28731e93c461d376915964289fbf9acad9d2485cbc2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466353DYTDO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYg1ZtR6%2BX4TU0r%2FmxHHTQ6AktbbjfEtllOdZDRhodXAiEA0W0EGi%2BI5i9xQEVhsUOUcs1uU%2BvHKc%2FZeQ7i7PEHbl8qiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNrU7B9hkqD1viPoyrcA0mb0DC%2BpqgtNvhssee8FR9vs6x58PtGPrnMGRM2gyQLiWk6cofMP8xE1FRl5dZGcBME17Q92532oV3QXFlBm7jUpJtV%2F8cye%2BA02FO6zuUIvH0kQV7R0UNvHvrhguxHVF8q%2B4v7X9dye9mRPXdEOYEADwCuQadL%2BRZNZa0qKWGldHyqlVZkYn3y7opVQR71p%2Bo65gIzJIezzBaqGn%2F8l%2B5KhOfZH%2BzcET3L8onZvbFLBv0rTnTL4otn4SqjA9goqU4pC1aW2PQTJbqkzWDUbbW%2F4%2FDjvegtnQPg72rq%2Fcbi6JakEFR0Ejin74a3Ft9vPg4RqWR57vzGV37ZcYPnSxCI6yHrPDS2iyaU5gr25uF%2FMc1O71RpbS%2BrQ29JEj%2B2GYYXnIaXGf3ziN7s5YHgklmXElYV6RNbe0Bjv6jzZR6vifWcSqwQIZ%2BspY8tq02KGFbccfP6I8mg7gN5FS1BSVMUoPGDtxpgkRba2iyZ%2FH7KCFR7UwzYU1xoW%2BAJqumS%2FTLOrZ4ffSmgdWTVVbu8OVgkIdyMV77ZvTW%2FLpJkXN8ve%2FkmaLwvYh%2BYRhg%2BAEmASikKOCCr39SblaiBq1zyJqg%2Bxdjm5qEC%2FRq%2FUMuJ3FVpPyT%2FSlE26uup2h1CMPb59rwGOqUBEAOEoLn3z7B4kb3D1MsoHisLVHQi%2BGhowpgW%2Bf7opBU298x2d%2FwkiFTmdRz5rJXi%2FQ6LDmmcemxwL3heKxkvAJncmDTTmpU90tmOkrU75aeMxgaRAfdSekcPpoJ3JiWSRRpF86X0I5kx3g5vbqfPnZ9mJISdDBQWYiWDbt088kXlE9OHOK3pEftN3kvl94Fx7oQD5cye86G0n2YpSC9gYnkvUVff&X-Amz-Signature=735653a538bbafda02c4010367fb4c4bfec3acb94486174a0760d853b360970b&X-Amz-SignedHeaders=host&x-id=GetObject)
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


