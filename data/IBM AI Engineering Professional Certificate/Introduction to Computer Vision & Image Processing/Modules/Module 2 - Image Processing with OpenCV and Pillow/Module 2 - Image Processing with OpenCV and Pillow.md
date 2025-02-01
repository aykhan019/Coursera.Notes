

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN225PYU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqeFyg6lKiKeERP1RyXgIWAdPnWtmsihDKEKGiqriT2AiBczH0aawwsDAYkl%2BWj8hfhXnJTO8jiN9uv5g%2BDcGPxcyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqMbALbP96JRxiK8oKtwD0H20Q8B%2FmHXFLep%2F9NW8FuZ8Y04xzw%2FjZ4zHaEyeEsG30tHB6F7bwbN4wAaYstZGhWHgfSG5ed6WqDzV77Nan3Ji7Die2wZ8dnBLD8w9XaHcG0W%2BrC660ZcaORjqC8IsRfYOaZ2uWdd6v6AD075MPsX4KqHs8WPIx1Klie%2FyJZ9%2FSPJxetCjmrHJGHjlxfbr%2Btb2%2FJ64tEQQw%2F%2F6oGOGPvRnRGoOoU0Plq%2B%2F%2Fq6QPtdUsnp4WVnyReT8jtiUfAmn1kbw3%2FY6REb1kZ%2F8Uxcg10mtKfMb8l6XGfblVxuNuONwJ%2Fb2Y4Sd6Jq9lJJh9r2SVtEpuyej82vv%2BnKkS4WiEBN6ENdmD8GD7muGgDTwjq8ppIo5W9l7lr5c%2Bl0Ph8UnSrwctZNa8U9tDarZ3n5ghuDGBgfJpHY%2FAYpI7NXsKywOS223%2Bbh%2B1KRqkW%2BWc4n%2BAmBFJwSB0eEWvm%2BuxJS7i2KGsPFpn%2B%2FIpqLkvooi%2BWvhLpGGGyC9UVyNRHnufC1ByfiH4VsgLrgyJhnFBvxblxsilMwSv475Gp4v2hLpqIZ18JviG%2B67w%2BCgDiAQTGFppE9FHdUOzRXG3IX8yg%2FPR%2Frf%2FfpWBv4Ei5FvRu%2Blds9fUWF%2FGwWXxfE97Mswuuz1vAY6pgGrxqG3djv6p7GPYtEDDMJrqDSK7EnQ1J1iMZ22I%2B7vfttdARNVAEq1JNLUAOVmZ2gDJT0WGsZn3COsxFJLNFRLhcy0fd7A1rmPBLxgVsNucpzJIiDg70%2BEqufxbS3m6u2IZMAaB9ZEJimhyG96smaoN7t4wzysual9rIGBVvdN4ybuZBNj1dJKsBQvAn6s%2BCQ3b31HQitTJotqtQZrdnG1G2v58Z60&X-Amz-Signature=562fb3984453aa5ab533b2a0e7a3be4c05b68afe2230bfb1c4194491570c37c2&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYJA4DIN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBAwdlUU8kmf1h0ahW8%2FCLjG3vVx%2FPIPuPmX2DQE0ajOAiBL%2F8KXzRf%2FOfIrD%2F0OnVxgvk1%2B068QOONQrssU59bGFyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuv0c3%2BXWB0KQzf3lKtwD2lz3AB43fwh1M3NH3orYkBu1%2FFBqkmwZ%2BX9bHAoivgMuNETlrnVCUJRGjoYdVPIB%2BKD8LRfizFKWoPQlXQTIQ0R3jsuWfUoxyHzY9vAWnuu5uTTEdJ4pbKP92GqGuAd77pgY3%2F%2F2%2BMwCHw7gLpIaAxJynSSpQjMiTPExTlUtcViP5VBdYDZUqA1O5cfHt%2B3caJjhVRJZXw99uobUA0f6rXQDej4KfmpCfxYuWRjROSSoW9HqjxgiOWJFEVlHDPJB%2FjNwdAzy7LqJAIlKBXc1vdpGrX0blg8oSitbleosLBOUwMi%2F8CSnv%2BtE2zITDumsaKN%2BXyB2VyONaKBMgr18Hg%2F3A6U%2BfjzYhXcjMI4ZaT6XIFuAPZ11n3g9sPgUCQpYi2laXZ6cihFk312h8W%2FA%2FfUZxP%2B9Z00lIHuomzV2Ixiln5gVmRF3z4cF6uojSteWtCzdwzZYl0DVRm22SOujy71O%2Fm8uaIgYlx2uwz%2F%2FbVXKrXt9l3M8YKLBPqtaita%2FYYKshsUS6Pb2EkWeaCEt3l67r8tz8UPFmvQoUZuyh7inyMWsqF%2FKyAhLMASWvxnsCYQ29SdYozEf5a%2Bwvhc2Z1h5CY3kaiEQiGbu9qBwx01uPTxCb%2FSZwmgIhuQws%2Bz1vAY6pgH5435xBSkLx9YppfhS4Imzo85FtGitfhLjp1rqMsOU9UuLV%2FDDJLeBSbSWVQPA5jCqOkXK6DvwczBRFHx42Xh0VdATzqxhX%2Bkh%2FBlqPDgr2Qc4nh46%2BHyGAa5L48QrAEYjSofLOkCPCgf1pzV74801v4bWMJ2i4rTeN771J1Lh6oPRYk1sKQSR3uzll8IWFLMTHVhp5TdlmYYXIiaXN9l9U6aCDqoz&X-Amz-Signature=72b226305e6345438f8e02e66165d9b81fc0b0f7c248206d9261ddaa9bdac954&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYJA4DIN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBAwdlUU8kmf1h0ahW8%2FCLjG3vVx%2FPIPuPmX2DQE0ajOAiBL%2F8KXzRf%2FOfIrD%2F0OnVxgvk1%2B068QOONQrssU59bGFyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuv0c3%2BXWB0KQzf3lKtwD2lz3AB43fwh1M3NH3orYkBu1%2FFBqkmwZ%2BX9bHAoivgMuNETlrnVCUJRGjoYdVPIB%2BKD8LRfizFKWoPQlXQTIQ0R3jsuWfUoxyHzY9vAWnuu5uTTEdJ4pbKP92GqGuAd77pgY3%2F%2F2%2BMwCHw7gLpIaAxJynSSpQjMiTPExTlUtcViP5VBdYDZUqA1O5cfHt%2B3caJjhVRJZXw99uobUA0f6rXQDej4KfmpCfxYuWRjROSSoW9HqjxgiOWJFEVlHDPJB%2FjNwdAzy7LqJAIlKBXc1vdpGrX0blg8oSitbleosLBOUwMi%2F8CSnv%2BtE2zITDumsaKN%2BXyB2VyONaKBMgr18Hg%2F3A6U%2BfjzYhXcjMI4ZaT6XIFuAPZ11n3g9sPgUCQpYi2laXZ6cihFk312h8W%2FA%2FfUZxP%2B9Z00lIHuomzV2Ixiln5gVmRF3z4cF6uojSteWtCzdwzZYl0DVRm22SOujy71O%2Fm8uaIgYlx2uwz%2F%2FbVXKrXt9l3M8YKLBPqtaita%2FYYKshsUS6Pb2EkWeaCEt3l67r8tz8UPFmvQoUZuyh7inyMWsqF%2FKyAhLMASWvxnsCYQ29SdYozEf5a%2Bwvhc2Z1h5CY3kaiEQiGbu9qBwx01uPTxCb%2FSZwmgIhuQws%2Bz1vAY6pgH5435xBSkLx9YppfhS4Imzo85FtGitfhLjp1rqMsOU9UuLV%2FDDJLeBSbSWVQPA5jCqOkXK6DvwczBRFHx42Xh0VdATzqxhX%2Bkh%2FBlqPDgr2Qc4nh46%2BHyGAa5L48QrAEYjSofLOkCPCgf1pzV74801v4bWMJ2i4rTeN771J1Lh6oPRYk1sKQSR3uzll8IWFLMTHVhp5TdlmYYXIiaXN9l9U6aCDqoz&X-Amz-Signature=c8d9b9bc982bf3c5c42b0e7b08464af53bfb657addae92bf1958546e7624db38&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYJA4DIN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBAwdlUU8kmf1h0ahW8%2FCLjG3vVx%2FPIPuPmX2DQE0ajOAiBL%2F8KXzRf%2FOfIrD%2F0OnVxgvk1%2B068QOONQrssU59bGFyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuv0c3%2BXWB0KQzf3lKtwD2lz3AB43fwh1M3NH3orYkBu1%2FFBqkmwZ%2BX9bHAoivgMuNETlrnVCUJRGjoYdVPIB%2BKD8LRfizFKWoPQlXQTIQ0R3jsuWfUoxyHzY9vAWnuu5uTTEdJ4pbKP92GqGuAd77pgY3%2F%2F2%2BMwCHw7gLpIaAxJynSSpQjMiTPExTlUtcViP5VBdYDZUqA1O5cfHt%2B3caJjhVRJZXw99uobUA0f6rXQDej4KfmpCfxYuWRjROSSoW9HqjxgiOWJFEVlHDPJB%2FjNwdAzy7LqJAIlKBXc1vdpGrX0blg8oSitbleosLBOUwMi%2F8CSnv%2BtE2zITDumsaKN%2BXyB2VyONaKBMgr18Hg%2F3A6U%2BfjzYhXcjMI4ZaT6XIFuAPZ11n3g9sPgUCQpYi2laXZ6cihFk312h8W%2FA%2FfUZxP%2B9Z00lIHuomzV2Ixiln5gVmRF3z4cF6uojSteWtCzdwzZYl0DVRm22SOujy71O%2Fm8uaIgYlx2uwz%2F%2FbVXKrXt9l3M8YKLBPqtaita%2FYYKshsUS6Pb2EkWeaCEt3l67r8tz8UPFmvQoUZuyh7inyMWsqF%2FKyAhLMASWvxnsCYQ29SdYozEf5a%2Bwvhc2Z1h5CY3kaiEQiGbu9qBwx01uPTxCb%2FSZwmgIhuQws%2Bz1vAY6pgH5435xBSkLx9YppfhS4Imzo85FtGitfhLjp1rqMsOU9UuLV%2FDDJLeBSbSWVQPA5jCqOkXK6DvwczBRFHx42Xh0VdATzqxhX%2Bkh%2FBlqPDgr2Qc4nh46%2BHyGAa5L48QrAEYjSofLOkCPCgf1pzV74801v4bWMJ2i4rTeN771J1Lh6oPRYk1sKQSR3uzll8IWFLMTHVhp5TdlmYYXIiaXN9l9U6aCDqoz&X-Amz-Signature=949d829a9756498da772e87275f3a9e61dd6182c85c38e36a36cfb0087c756d0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYJA4DIN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBAwdlUU8kmf1h0ahW8%2FCLjG3vVx%2FPIPuPmX2DQE0ajOAiBL%2F8KXzRf%2FOfIrD%2F0OnVxgvk1%2B068QOONQrssU59bGFyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuv0c3%2BXWB0KQzf3lKtwD2lz3AB43fwh1M3NH3orYkBu1%2FFBqkmwZ%2BX9bHAoivgMuNETlrnVCUJRGjoYdVPIB%2BKD8LRfizFKWoPQlXQTIQ0R3jsuWfUoxyHzY9vAWnuu5uTTEdJ4pbKP92GqGuAd77pgY3%2F%2F2%2BMwCHw7gLpIaAxJynSSpQjMiTPExTlUtcViP5VBdYDZUqA1O5cfHt%2B3caJjhVRJZXw99uobUA0f6rXQDej4KfmpCfxYuWRjROSSoW9HqjxgiOWJFEVlHDPJB%2FjNwdAzy7LqJAIlKBXc1vdpGrX0blg8oSitbleosLBOUwMi%2F8CSnv%2BtE2zITDumsaKN%2BXyB2VyONaKBMgr18Hg%2F3A6U%2BfjzYhXcjMI4ZaT6XIFuAPZ11n3g9sPgUCQpYi2laXZ6cihFk312h8W%2FA%2FfUZxP%2B9Z00lIHuomzV2Ixiln5gVmRF3z4cF6uojSteWtCzdwzZYl0DVRm22SOujy71O%2Fm8uaIgYlx2uwz%2F%2FbVXKrXt9l3M8YKLBPqtaita%2FYYKshsUS6Pb2EkWeaCEt3l67r8tz8UPFmvQoUZuyh7inyMWsqF%2FKyAhLMASWvxnsCYQ29SdYozEf5a%2Bwvhc2Z1h5CY3kaiEQiGbu9qBwx01uPTxCb%2FSZwmgIhuQws%2Bz1vAY6pgH5435xBSkLx9YppfhS4Imzo85FtGitfhLjp1rqMsOU9UuLV%2FDDJLeBSbSWVQPA5jCqOkXK6DvwczBRFHx42Xh0VdATzqxhX%2Bkh%2FBlqPDgr2Qc4nh46%2BHyGAa5L48QrAEYjSofLOkCPCgf1pzV74801v4bWMJ2i4rTeN771J1Lh6oPRYk1sKQSR3uzll8IWFLMTHVhp5TdlmYYXIiaXN9l9U6aCDqoz&X-Amz-Signature=29d937c609df11a0a5ab9ef3f114498abff511b255a1bcf321b670469b2000b5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYJA4DIN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBAwdlUU8kmf1h0ahW8%2FCLjG3vVx%2FPIPuPmX2DQE0ajOAiBL%2F8KXzRf%2FOfIrD%2F0OnVxgvk1%2B068QOONQrssU59bGFyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuv0c3%2BXWB0KQzf3lKtwD2lz3AB43fwh1M3NH3orYkBu1%2FFBqkmwZ%2BX9bHAoivgMuNETlrnVCUJRGjoYdVPIB%2BKD8LRfizFKWoPQlXQTIQ0R3jsuWfUoxyHzY9vAWnuu5uTTEdJ4pbKP92GqGuAd77pgY3%2F%2F2%2BMwCHw7gLpIaAxJynSSpQjMiTPExTlUtcViP5VBdYDZUqA1O5cfHt%2B3caJjhVRJZXw99uobUA0f6rXQDej4KfmpCfxYuWRjROSSoW9HqjxgiOWJFEVlHDPJB%2FjNwdAzy7LqJAIlKBXc1vdpGrX0blg8oSitbleosLBOUwMi%2F8CSnv%2BtE2zITDumsaKN%2BXyB2VyONaKBMgr18Hg%2F3A6U%2BfjzYhXcjMI4ZaT6XIFuAPZ11n3g9sPgUCQpYi2laXZ6cihFk312h8W%2FA%2FfUZxP%2B9Z00lIHuomzV2Ixiln5gVmRF3z4cF6uojSteWtCzdwzZYl0DVRm22SOujy71O%2Fm8uaIgYlx2uwz%2F%2FbVXKrXt9l3M8YKLBPqtaita%2FYYKshsUS6Pb2EkWeaCEt3l67r8tz8UPFmvQoUZuyh7inyMWsqF%2FKyAhLMASWvxnsCYQ29SdYozEf5a%2Bwvhc2Z1h5CY3kaiEQiGbu9qBwx01uPTxCb%2FSZwmgIhuQws%2Bz1vAY6pgH5435xBSkLx9YppfhS4Imzo85FtGitfhLjp1rqMsOU9UuLV%2FDDJLeBSbSWVQPA5jCqOkXK6DvwczBRFHx42Xh0VdATzqxhX%2Bkh%2FBlqPDgr2Qc4nh46%2BHyGAa5L48QrAEYjSofLOkCPCgf1pzV74801v4bWMJ2i4rTeN771J1Lh6oPRYk1sKQSR3uzll8IWFLMTHVhp5TdlmYYXIiaXN9l9U6aCDqoz&X-Amz-Signature=7bc3a09bf98f133afd29c9da58c854fe3a7ebecc9430cc1b031b8cc9dcdc8c88&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN225PYU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqeFyg6lKiKeERP1RyXgIWAdPnWtmsihDKEKGiqriT2AiBczH0aawwsDAYkl%2BWj8hfhXnJTO8jiN9uv5g%2BDcGPxcyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqMbALbP96JRxiK8oKtwD0H20Q8B%2FmHXFLep%2F9NW8FuZ8Y04xzw%2FjZ4zHaEyeEsG30tHB6F7bwbN4wAaYstZGhWHgfSG5ed6WqDzV77Nan3Ji7Die2wZ8dnBLD8w9XaHcG0W%2BrC660ZcaORjqC8IsRfYOaZ2uWdd6v6AD075MPsX4KqHs8WPIx1Klie%2FyJZ9%2FSPJxetCjmrHJGHjlxfbr%2Btb2%2FJ64tEQQw%2F%2F6oGOGPvRnRGoOoU0Plq%2B%2F%2Fq6QPtdUsnp4WVnyReT8jtiUfAmn1kbw3%2FY6REb1kZ%2F8Uxcg10mtKfMb8l6XGfblVxuNuONwJ%2Fb2Y4Sd6Jq9lJJh9r2SVtEpuyej82vv%2BnKkS4WiEBN6ENdmD8GD7muGgDTwjq8ppIo5W9l7lr5c%2Bl0Ph8UnSrwctZNa8U9tDarZ3n5ghuDGBgfJpHY%2FAYpI7NXsKywOS223%2Bbh%2B1KRqkW%2BWc4n%2BAmBFJwSB0eEWvm%2BuxJS7i2KGsPFpn%2B%2FIpqLkvooi%2BWvhLpGGGyC9UVyNRHnufC1ByfiH4VsgLrgyJhnFBvxblxsilMwSv475Gp4v2hLpqIZ18JviG%2B67w%2BCgDiAQTGFppE9FHdUOzRXG3IX8yg%2FPR%2Frf%2FfpWBv4Ei5FvRu%2Blds9fUWF%2FGwWXxfE97Mswuuz1vAY6pgGrxqG3djv6p7GPYtEDDMJrqDSK7EnQ1J1iMZ22I%2B7vfttdARNVAEq1JNLUAOVmZ2gDJT0WGsZn3COsxFJLNFRLhcy0fd7A1rmPBLxgVsNucpzJIiDg70%2BEqufxbS3m6u2IZMAaB9ZEJimhyG96smaoN7t4wzysual9rIGBVvdN4ybuZBNj1dJKsBQvAn6s%2BCQ3b31HQitTJotqtQZrdnG1G2v58Z60&X-Amz-Signature=bd96c70c018388c57b2be36fc8045b34a90bc472dd0be2f6f99a9d69a65fd419&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN225PYU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqeFyg6lKiKeERP1RyXgIWAdPnWtmsihDKEKGiqriT2AiBczH0aawwsDAYkl%2BWj8hfhXnJTO8jiN9uv5g%2BDcGPxcyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqMbALbP96JRxiK8oKtwD0H20Q8B%2FmHXFLep%2F9NW8FuZ8Y04xzw%2FjZ4zHaEyeEsG30tHB6F7bwbN4wAaYstZGhWHgfSG5ed6WqDzV77Nan3Ji7Die2wZ8dnBLD8w9XaHcG0W%2BrC660ZcaORjqC8IsRfYOaZ2uWdd6v6AD075MPsX4KqHs8WPIx1Klie%2FyJZ9%2FSPJxetCjmrHJGHjlxfbr%2Btb2%2FJ64tEQQw%2F%2F6oGOGPvRnRGoOoU0Plq%2B%2F%2Fq6QPtdUsnp4WVnyReT8jtiUfAmn1kbw3%2FY6REb1kZ%2F8Uxcg10mtKfMb8l6XGfblVxuNuONwJ%2Fb2Y4Sd6Jq9lJJh9r2SVtEpuyej82vv%2BnKkS4WiEBN6ENdmD8GD7muGgDTwjq8ppIo5W9l7lr5c%2Bl0Ph8UnSrwctZNa8U9tDarZ3n5ghuDGBgfJpHY%2FAYpI7NXsKywOS223%2Bbh%2B1KRqkW%2BWc4n%2BAmBFJwSB0eEWvm%2BuxJS7i2KGsPFpn%2B%2FIpqLkvooi%2BWvhLpGGGyC9UVyNRHnufC1ByfiH4VsgLrgyJhnFBvxblxsilMwSv475Gp4v2hLpqIZ18JviG%2B67w%2BCgDiAQTGFppE9FHdUOzRXG3IX8yg%2FPR%2Frf%2FfpWBv4Ei5FvRu%2Blds9fUWF%2FGwWXxfE97Mswuuz1vAY6pgGrxqG3djv6p7GPYtEDDMJrqDSK7EnQ1J1iMZ22I%2B7vfttdARNVAEq1JNLUAOVmZ2gDJT0WGsZn3COsxFJLNFRLhcy0fd7A1rmPBLxgVsNucpzJIiDg70%2BEqufxbS3m6u2IZMAaB9ZEJimhyG96smaoN7t4wzysual9rIGBVvdN4ybuZBNj1dJKsBQvAn6s%2BCQ3b31HQitTJotqtQZrdnG1G2v58Z60&X-Amz-Signature=c2d5994b58962d2cec84f6cc4f40658a1f58e9c5b9df9838efb0129102b4a711&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN225PYU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqeFyg6lKiKeERP1RyXgIWAdPnWtmsihDKEKGiqriT2AiBczH0aawwsDAYkl%2BWj8hfhXnJTO8jiN9uv5g%2BDcGPxcyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqMbALbP96JRxiK8oKtwD0H20Q8B%2FmHXFLep%2F9NW8FuZ8Y04xzw%2FjZ4zHaEyeEsG30tHB6F7bwbN4wAaYstZGhWHgfSG5ed6WqDzV77Nan3Ji7Die2wZ8dnBLD8w9XaHcG0W%2BrC660ZcaORjqC8IsRfYOaZ2uWdd6v6AD075MPsX4KqHs8WPIx1Klie%2FyJZ9%2FSPJxetCjmrHJGHjlxfbr%2Btb2%2FJ64tEQQw%2F%2F6oGOGPvRnRGoOoU0Plq%2B%2F%2Fq6QPtdUsnp4WVnyReT8jtiUfAmn1kbw3%2FY6REb1kZ%2F8Uxcg10mtKfMb8l6XGfblVxuNuONwJ%2Fb2Y4Sd6Jq9lJJh9r2SVtEpuyej82vv%2BnKkS4WiEBN6ENdmD8GD7muGgDTwjq8ppIo5W9l7lr5c%2Bl0Ph8UnSrwctZNa8U9tDarZ3n5ghuDGBgfJpHY%2FAYpI7NXsKywOS223%2Bbh%2B1KRqkW%2BWc4n%2BAmBFJwSB0eEWvm%2BuxJS7i2KGsPFpn%2B%2FIpqLkvooi%2BWvhLpGGGyC9UVyNRHnufC1ByfiH4VsgLrgyJhnFBvxblxsilMwSv475Gp4v2hLpqIZ18JviG%2B67w%2BCgDiAQTGFppE9FHdUOzRXG3IX8yg%2FPR%2Frf%2FfpWBv4Ei5FvRu%2Blds9fUWF%2FGwWXxfE97Mswuuz1vAY6pgGrxqG3djv6p7GPYtEDDMJrqDSK7EnQ1J1iMZ22I%2B7vfttdARNVAEq1JNLUAOVmZ2gDJT0WGsZn3COsxFJLNFRLhcy0fd7A1rmPBLxgVsNucpzJIiDg70%2BEqufxbS3m6u2IZMAaB9ZEJimhyG96smaoN7t4wzysual9rIGBVvdN4ybuZBNj1dJKsBQvAn6s%2BCQ3b31HQitTJotqtQZrdnG1G2v58Z60&X-Amz-Signature=3891f96fb661b2ebbada40b0a78c52528a5355bd2cb21d76c542f98aec36ff6e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN225PYU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqeFyg6lKiKeERP1RyXgIWAdPnWtmsihDKEKGiqriT2AiBczH0aawwsDAYkl%2BWj8hfhXnJTO8jiN9uv5g%2BDcGPxcyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqMbALbP96JRxiK8oKtwD0H20Q8B%2FmHXFLep%2F9NW8FuZ8Y04xzw%2FjZ4zHaEyeEsG30tHB6F7bwbN4wAaYstZGhWHgfSG5ed6WqDzV77Nan3Ji7Die2wZ8dnBLD8w9XaHcG0W%2BrC660ZcaORjqC8IsRfYOaZ2uWdd6v6AD075MPsX4KqHs8WPIx1Klie%2FyJZ9%2FSPJxetCjmrHJGHjlxfbr%2Btb2%2FJ64tEQQw%2F%2F6oGOGPvRnRGoOoU0Plq%2B%2F%2Fq6QPtdUsnp4WVnyReT8jtiUfAmn1kbw3%2FY6REb1kZ%2F8Uxcg10mtKfMb8l6XGfblVxuNuONwJ%2Fb2Y4Sd6Jq9lJJh9r2SVtEpuyej82vv%2BnKkS4WiEBN6ENdmD8GD7muGgDTwjq8ppIo5W9l7lr5c%2Bl0Ph8UnSrwctZNa8U9tDarZ3n5ghuDGBgfJpHY%2FAYpI7NXsKywOS223%2Bbh%2B1KRqkW%2BWc4n%2BAmBFJwSB0eEWvm%2BuxJS7i2KGsPFpn%2B%2FIpqLkvooi%2BWvhLpGGGyC9UVyNRHnufC1ByfiH4VsgLrgyJhnFBvxblxsilMwSv475Gp4v2hLpqIZ18JviG%2B67w%2BCgDiAQTGFppE9FHdUOzRXG3IX8yg%2FPR%2Frf%2FfpWBv4Ei5FvRu%2Blds9fUWF%2FGwWXxfE97Mswuuz1vAY6pgGrxqG3djv6p7GPYtEDDMJrqDSK7EnQ1J1iMZ22I%2B7vfttdARNVAEq1JNLUAOVmZ2gDJT0WGsZn3COsxFJLNFRLhcy0fd7A1rmPBLxgVsNucpzJIiDg70%2BEqufxbS3m6u2IZMAaB9ZEJimhyG96smaoN7t4wzysual9rIGBVvdN4ybuZBNj1dJKsBQvAn6s%2BCQ3b31HQitTJotqtQZrdnG1G2v58Z60&X-Amz-Signature=2b357ab28164a9c51a51a0e527615445429a624e39b9fbd5cd8e1fc4af27e8ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN225PYU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqeFyg6lKiKeERP1RyXgIWAdPnWtmsihDKEKGiqriT2AiBczH0aawwsDAYkl%2BWj8hfhXnJTO8jiN9uv5g%2BDcGPxcyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqMbALbP96JRxiK8oKtwD0H20Q8B%2FmHXFLep%2F9NW8FuZ8Y04xzw%2FjZ4zHaEyeEsG30tHB6F7bwbN4wAaYstZGhWHgfSG5ed6WqDzV77Nan3Ji7Die2wZ8dnBLD8w9XaHcG0W%2BrC660ZcaORjqC8IsRfYOaZ2uWdd6v6AD075MPsX4KqHs8WPIx1Klie%2FyJZ9%2FSPJxetCjmrHJGHjlxfbr%2Btb2%2FJ64tEQQw%2F%2F6oGOGPvRnRGoOoU0Plq%2B%2F%2Fq6QPtdUsnp4WVnyReT8jtiUfAmn1kbw3%2FY6REb1kZ%2F8Uxcg10mtKfMb8l6XGfblVxuNuONwJ%2Fb2Y4Sd6Jq9lJJh9r2SVtEpuyej82vv%2BnKkS4WiEBN6ENdmD8GD7muGgDTwjq8ppIo5W9l7lr5c%2Bl0Ph8UnSrwctZNa8U9tDarZ3n5ghuDGBgfJpHY%2FAYpI7NXsKywOS223%2Bbh%2B1KRqkW%2BWc4n%2BAmBFJwSB0eEWvm%2BuxJS7i2KGsPFpn%2B%2FIpqLkvooi%2BWvhLpGGGyC9UVyNRHnufC1ByfiH4VsgLrgyJhnFBvxblxsilMwSv475Gp4v2hLpqIZ18JviG%2B67w%2BCgDiAQTGFppE9FHdUOzRXG3IX8yg%2FPR%2Frf%2FfpWBv4Ei5FvRu%2Blds9fUWF%2FGwWXxfE97Mswuuz1vAY6pgGrxqG3djv6p7GPYtEDDMJrqDSK7EnQ1J1iMZ22I%2B7vfttdARNVAEq1JNLUAOVmZ2gDJT0WGsZn3COsxFJLNFRLhcy0fd7A1rmPBLxgVsNucpzJIiDg70%2BEqufxbS3m6u2IZMAaB9ZEJimhyG96smaoN7t4wzysual9rIGBVvdN4ybuZBNj1dJKsBQvAn6s%2BCQ3b31HQitTJotqtQZrdnG1G2v58Z60&X-Amz-Signature=b4515c3066df3ab11b841279d8bfe225dbec4938d7fe267bf6c0f8750b7afc5e&X-Amz-SignedHeaders=host&x-id=GetObject)
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


