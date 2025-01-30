

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBKXLQOX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6KivRsbJwa%2B6U8LquNRSP%2FmK7WXw45orU%2FR55ltR9cgIgFFnQgoZ7S5YQArl4dVcQys3Rv71MCvfTbouC3oee%2BFUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG5bxLl030S7i58BircA%2FWV0wmtk9o0YkpTK%2FWcgurM1F1QWRNI%2BkeOMCWvs%2BSls9PwfWc%2Bdja2vd5HIN%2FlRCOLP%2Bkutj%2BOpf%2Fn9FBBxc0ZOzl8YK9QTiiJXYSCG0GY38IPN5WNVIHSlhrMpxcUda7iPbI3AGmAvA5860Go%2FV%2FmWLU9vRKN8TfP8qlJn%2B%2FdmYizhzenOufiWFPSnUMaEyibtwC2gj43a2DcfAwD0BFokf4nPPlBKg8gbGX61gn%2FDn2vYE69A8nG9kue8jkEp9UOK82%2BUWoJv49zLlS97rC2t9uHrhGcArwoNSzX%2BcSUkOwZ6I8UpvzZhsCLaxnPSJpk%2F5EAlZffBrVjdRXdXzVMhwfSEmnUv2A7Ua1r7qTz%2BOHz4FBZ9mYu9IXHn2rNp6SSRQzvxR83CTaF5mRkYNFdgrxCr6paO0U0lq7ZF0WFZE0hmsMxVdmaNOJRktdDI8%2Fw7wBJvirb%2B7L9Jcf%2FI9APAmdycwdHE%2FU8gBLBCW%2F4UTvpVRXEVLCHmGurOvqiV22AkdIhX1B6huLS07MyVBFh%2FoTbcryOLV071gKzq80pyEKJ63kncDmxXJNvq9QVr1eF595%2BftrDl7fqDKMaMUyqkqF7q6E1aLupgj7y8dZDBXNq3h83c3oOJTLpMKCo7bwGOqUB7AXV9%2Ft3y2iZaz4gEJ8qMUyktqKcWifqIj2QxhtaswvwU1CVoZRIp40hROuxm7bie%2FYE1GV34p80xzlah3gxzJb2jN9JSF1EroeItEOMQhGi7QCoHADl%2BiBRU1KCo9rnyEZgHYW4YNYvPLKsbLmIeHSBbtw0xSWPg35Pn4hDgWT9AQOf73wCViHFV4uRM%2FFFP6l9ePJOlZtPrYlxhUUE4dFy7Aqd&X-Amz-Signature=c9fa99aee06eca1d1db359a258c10c241094bedaf984cb41ca0d83e1b0f6a3a3&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4ZMP42%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBSOT2L3%2BcdoN%2FhbKd21v4JLbLeTj%2FTVgn%2BkUCzGVfYmAiBbNrbmQaOBzz8A3ywgEqn6jVVzTk%2FP%2FhtOpE%2B8ADwrQiqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN4TTUDORomRmU3MqKtwD3HyNSxE5Dzxn1m93wFpyrp3zBX1c45D7kksRlm063Ln17gEYTPh0HF6V93dLxcXnvfdd31TG74EIOaytbVn0LczHlciTe%2F6TiHIr0m9VB2CMkBY9FxREIp%2F3EOFy2UzaeiXuYk7MXSFbAJF7ngn40dkTAKNZFo8qVrxsYDaCM00Gp1VlNB%2F6uH%2FUuCM5Lfzqx2k3OTa85ABTsA8W4AF9btJ97o3zxkkhkfHj9uYTNmMgYwYJf2o4y0bj9%2FvFsvIXB2f4fKsi2Ywo5JBhMmumuBx9sSPvUcAVblFZP4emvyD5tuxWPMBQElPkMK2BUzm7eEAywFt6JODs5ArId6nicyX7fwbi7h4XpIsm7m4IGkW3uSqS2xVSJe%2FCM7oV9Da%2FRHa01D9mLbH0L5GcDNz%2FJ7jtSeKjznZAi7EOknNH7I8s9RwR5CYj5PJm5WkuZaTNJnP0toPndNo2PAMQK7lxOa26aO5z4Q6j5cznAAoUVO%2BRIa7Y5SK%2FIbm2SSGBdqKFCRfWEKeo0Yin%2FYxNfeeV5CXMrM5lNDpixjKtL8Si1x%2Fe%2BslVw91zlu9kTH74495tf0HvSVrMkt%2FXgCtLPjsQ%2B7f410HDryUDqVe%2BkrRYJxC%2Fxogm6y5p1BToFaww7qntvAY6pgE0WEdm6G45sYoMC7uimOOYYeWjlFkL53hw3rXk%2BHPsweUDYBzH%2BsFpv7E5jTECH82r6BYX2IOjZ4ntVMXDuu1FgTBLOLSBoA%2ByNtBtzeQ%2BtO8yS%2BERt%2FMDWAWBLjlEx9M64o%2B3Oa4QjYY%2FtEMPhvOiG1iCQKDyWcx7eiuRjo%2F5dm9dM5vR78wdIKhHL70wBt5lskV5V7aqBrcJsAqr8B%2FUmQM%2BQmnt&X-Amz-Signature=69e8df7bfa0fc82da1e6945057c59c1c581ad14252d8a0f10678d55636736bc6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4ZMP42%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBSOT2L3%2BcdoN%2FhbKd21v4JLbLeTj%2FTVgn%2BkUCzGVfYmAiBbNrbmQaOBzz8A3ywgEqn6jVVzTk%2FP%2FhtOpE%2B8ADwrQiqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN4TTUDORomRmU3MqKtwD3HyNSxE5Dzxn1m93wFpyrp3zBX1c45D7kksRlm063Ln17gEYTPh0HF6V93dLxcXnvfdd31TG74EIOaytbVn0LczHlciTe%2F6TiHIr0m9VB2CMkBY9FxREIp%2F3EOFy2UzaeiXuYk7MXSFbAJF7ngn40dkTAKNZFo8qVrxsYDaCM00Gp1VlNB%2F6uH%2FUuCM5Lfzqx2k3OTa85ABTsA8W4AF9btJ97o3zxkkhkfHj9uYTNmMgYwYJf2o4y0bj9%2FvFsvIXB2f4fKsi2Ywo5JBhMmumuBx9sSPvUcAVblFZP4emvyD5tuxWPMBQElPkMK2BUzm7eEAywFt6JODs5ArId6nicyX7fwbi7h4XpIsm7m4IGkW3uSqS2xVSJe%2FCM7oV9Da%2FRHa01D9mLbH0L5GcDNz%2FJ7jtSeKjznZAi7EOknNH7I8s9RwR5CYj5PJm5WkuZaTNJnP0toPndNo2PAMQK7lxOa26aO5z4Q6j5cznAAoUVO%2BRIa7Y5SK%2FIbm2SSGBdqKFCRfWEKeo0Yin%2FYxNfeeV5CXMrM5lNDpixjKtL8Si1x%2Fe%2BslVw91zlu9kTH74495tf0HvSVrMkt%2FXgCtLPjsQ%2B7f410HDryUDqVe%2BkrRYJxC%2Fxogm6y5p1BToFaww7qntvAY6pgE0WEdm6G45sYoMC7uimOOYYeWjlFkL53hw3rXk%2BHPsweUDYBzH%2BsFpv7E5jTECH82r6BYX2IOjZ4ntVMXDuu1FgTBLOLSBoA%2ByNtBtzeQ%2BtO8yS%2BERt%2FMDWAWBLjlEx9M64o%2B3Oa4QjYY%2FtEMPhvOiG1iCQKDyWcx7eiuRjo%2F5dm9dM5vR78wdIKhHL70wBt5lskV5V7aqBrcJsAqr8B%2FUmQM%2BQmnt&X-Amz-Signature=617748f9aacc37c9e7abc09d84dd814f9844477fecdfef8d47472900d3c3a596&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4ZMP42%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBSOT2L3%2BcdoN%2FhbKd21v4JLbLeTj%2FTVgn%2BkUCzGVfYmAiBbNrbmQaOBzz8A3ywgEqn6jVVzTk%2FP%2FhtOpE%2B8ADwrQiqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN4TTUDORomRmU3MqKtwD3HyNSxE5Dzxn1m93wFpyrp3zBX1c45D7kksRlm063Ln17gEYTPh0HF6V93dLxcXnvfdd31TG74EIOaytbVn0LczHlciTe%2F6TiHIr0m9VB2CMkBY9FxREIp%2F3EOFy2UzaeiXuYk7MXSFbAJF7ngn40dkTAKNZFo8qVrxsYDaCM00Gp1VlNB%2F6uH%2FUuCM5Lfzqx2k3OTa85ABTsA8W4AF9btJ97o3zxkkhkfHj9uYTNmMgYwYJf2o4y0bj9%2FvFsvIXB2f4fKsi2Ywo5JBhMmumuBx9sSPvUcAVblFZP4emvyD5tuxWPMBQElPkMK2BUzm7eEAywFt6JODs5ArId6nicyX7fwbi7h4XpIsm7m4IGkW3uSqS2xVSJe%2FCM7oV9Da%2FRHa01D9mLbH0L5GcDNz%2FJ7jtSeKjznZAi7EOknNH7I8s9RwR5CYj5PJm5WkuZaTNJnP0toPndNo2PAMQK7lxOa26aO5z4Q6j5cznAAoUVO%2BRIa7Y5SK%2FIbm2SSGBdqKFCRfWEKeo0Yin%2FYxNfeeV5CXMrM5lNDpixjKtL8Si1x%2Fe%2BslVw91zlu9kTH74495tf0HvSVrMkt%2FXgCtLPjsQ%2B7f410HDryUDqVe%2BkrRYJxC%2Fxogm6y5p1BToFaww7qntvAY6pgE0WEdm6G45sYoMC7uimOOYYeWjlFkL53hw3rXk%2BHPsweUDYBzH%2BsFpv7E5jTECH82r6BYX2IOjZ4ntVMXDuu1FgTBLOLSBoA%2ByNtBtzeQ%2BtO8yS%2BERt%2FMDWAWBLjlEx9M64o%2B3Oa4QjYY%2FtEMPhvOiG1iCQKDyWcx7eiuRjo%2F5dm9dM5vR78wdIKhHL70wBt5lskV5V7aqBrcJsAqr8B%2FUmQM%2BQmnt&X-Amz-Signature=926fe85439766430258354643e248d649654171f41024b9032cb2c818f2448a2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4ZMP42%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBSOT2L3%2BcdoN%2FhbKd21v4JLbLeTj%2FTVgn%2BkUCzGVfYmAiBbNrbmQaOBzz8A3ywgEqn6jVVzTk%2FP%2FhtOpE%2B8ADwrQiqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN4TTUDORomRmU3MqKtwD3HyNSxE5Dzxn1m93wFpyrp3zBX1c45D7kksRlm063Ln17gEYTPh0HF6V93dLxcXnvfdd31TG74EIOaytbVn0LczHlciTe%2F6TiHIr0m9VB2CMkBY9FxREIp%2F3EOFy2UzaeiXuYk7MXSFbAJF7ngn40dkTAKNZFo8qVrxsYDaCM00Gp1VlNB%2F6uH%2FUuCM5Lfzqx2k3OTa85ABTsA8W4AF9btJ97o3zxkkhkfHj9uYTNmMgYwYJf2o4y0bj9%2FvFsvIXB2f4fKsi2Ywo5JBhMmumuBx9sSPvUcAVblFZP4emvyD5tuxWPMBQElPkMK2BUzm7eEAywFt6JODs5ArId6nicyX7fwbi7h4XpIsm7m4IGkW3uSqS2xVSJe%2FCM7oV9Da%2FRHa01D9mLbH0L5GcDNz%2FJ7jtSeKjznZAi7EOknNH7I8s9RwR5CYj5PJm5WkuZaTNJnP0toPndNo2PAMQK7lxOa26aO5z4Q6j5cznAAoUVO%2BRIa7Y5SK%2FIbm2SSGBdqKFCRfWEKeo0Yin%2FYxNfeeV5CXMrM5lNDpixjKtL8Si1x%2Fe%2BslVw91zlu9kTH74495tf0HvSVrMkt%2FXgCtLPjsQ%2B7f410HDryUDqVe%2BkrRYJxC%2Fxogm6y5p1BToFaww7qntvAY6pgE0WEdm6G45sYoMC7uimOOYYeWjlFkL53hw3rXk%2BHPsweUDYBzH%2BsFpv7E5jTECH82r6BYX2IOjZ4ntVMXDuu1FgTBLOLSBoA%2ByNtBtzeQ%2BtO8yS%2BERt%2FMDWAWBLjlEx9M64o%2B3Oa4QjYY%2FtEMPhvOiG1iCQKDyWcx7eiuRjo%2F5dm9dM5vR78wdIKhHL70wBt5lskV5V7aqBrcJsAqr8B%2FUmQM%2BQmnt&X-Amz-Signature=5f6f66aa443ac40689bc8db31f6efac7e53eba4b58a2c9d4ef65fbe4bef5ada2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4ZMP42%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBSOT2L3%2BcdoN%2FhbKd21v4JLbLeTj%2FTVgn%2BkUCzGVfYmAiBbNrbmQaOBzz8A3ywgEqn6jVVzTk%2FP%2FhtOpE%2B8ADwrQiqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN4TTUDORomRmU3MqKtwD3HyNSxE5Dzxn1m93wFpyrp3zBX1c45D7kksRlm063Ln17gEYTPh0HF6V93dLxcXnvfdd31TG74EIOaytbVn0LczHlciTe%2F6TiHIr0m9VB2CMkBY9FxREIp%2F3EOFy2UzaeiXuYk7MXSFbAJF7ngn40dkTAKNZFo8qVrxsYDaCM00Gp1VlNB%2F6uH%2FUuCM5Lfzqx2k3OTa85ABTsA8W4AF9btJ97o3zxkkhkfHj9uYTNmMgYwYJf2o4y0bj9%2FvFsvIXB2f4fKsi2Ywo5JBhMmumuBx9sSPvUcAVblFZP4emvyD5tuxWPMBQElPkMK2BUzm7eEAywFt6JODs5ArId6nicyX7fwbi7h4XpIsm7m4IGkW3uSqS2xVSJe%2FCM7oV9Da%2FRHa01D9mLbH0L5GcDNz%2FJ7jtSeKjznZAi7EOknNH7I8s9RwR5CYj5PJm5WkuZaTNJnP0toPndNo2PAMQK7lxOa26aO5z4Q6j5cznAAoUVO%2BRIa7Y5SK%2FIbm2SSGBdqKFCRfWEKeo0Yin%2FYxNfeeV5CXMrM5lNDpixjKtL8Si1x%2Fe%2BslVw91zlu9kTH74495tf0HvSVrMkt%2FXgCtLPjsQ%2B7f410HDryUDqVe%2BkrRYJxC%2Fxogm6y5p1BToFaww7qntvAY6pgE0WEdm6G45sYoMC7uimOOYYeWjlFkL53hw3rXk%2BHPsweUDYBzH%2BsFpv7E5jTECH82r6BYX2IOjZ4ntVMXDuu1FgTBLOLSBoA%2ByNtBtzeQ%2BtO8yS%2BERt%2FMDWAWBLjlEx9M64o%2B3Oa4QjYY%2FtEMPhvOiG1iCQKDyWcx7eiuRjo%2F5dm9dM5vR78wdIKhHL70wBt5lskV5V7aqBrcJsAqr8B%2FUmQM%2BQmnt&X-Amz-Signature=39ebe5074a9f6def6b3f2efd9ad328430e325e8f66b18a1ed64b62f180a60410&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBKXLQOX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6KivRsbJwa%2B6U8LquNRSP%2FmK7WXw45orU%2FR55ltR9cgIgFFnQgoZ7S5YQArl4dVcQys3Rv71MCvfTbouC3oee%2BFUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG5bxLl030S7i58BircA%2FWV0wmtk9o0YkpTK%2FWcgurM1F1QWRNI%2BkeOMCWvs%2BSls9PwfWc%2Bdja2vd5HIN%2FlRCOLP%2Bkutj%2BOpf%2Fn9FBBxc0ZOzl8YK9QTiiJXYSCG0GY38IPN5WNVIHSlhrMpxcUda7iPbI3AGmAvA5860Go%2FV%2FmWLU9vRKN8TfP8qlJn%2B%2FdmYizhzenOufiWFPSnUMaEyibtwC2gj43a2DcfAwD0BFokf4nPPlBKg8gbGX61gn%2FDn2vYE69A8nG9kue8jkEp9UOK82%2BUWoJv49zLlS97rC2t9uHrhGcArwoNSzX%2BcSUkOwZ6I8UpvzZhsCLaxnPSJpk%2F5EAlZffBrVjdRXdXzVMhwfSEmnUv2A7Ua1r7qTz%2BOHz4FBZ9mYu9IXHn2rNp6SSRQzvxR83CTaF5mRkYNFdgrxCr6paO0U0lq7ZF0WFZE0hmsMxVdmaNOJRktdDI8%2Fw7wBJvirb%2B7L9Jcf%2FI9APAmdycwdHE%2FU8gBLBCW%2F4UTvpVRXEVLCHmGurOvqiV22AkdIhX1B6huLS07MyVBFh%2FoTbcryOLV071gKzq80pyEKJ63kncDmxXJNvq9QVr1eF595%2BftrDl7fqDKMaMUyqkqF7q6E1aLupgj7y8dZDBXNq3h83c3oOJTLpMKCo7bwGOqUB7AXV9%2Ft3y2iZaz4gEJ8qMUyktqKcWifqIj2QxhtaswvwU1CVoZRIp40hROuxm7bie%2FYE1GV34p80xzlah3gxzJb2jN9JSF1EroeItEOMQhGi7QCoHADl%2BiBRU1KCo9rnyEZgHYW4YNYvPLKsbLmIeHSBbtw0xSWPg35Pn4hDgWT9AQOf73wCViHFV4uRM%2FFFP6l9ePJOlZtPrYlxhUUE4dFy7Aqd&X-Amz-Signature=2f7637f715ca07a09c60b9f7ec74dcc7f38fe88d8a5b5102783711887e492168&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBKXLQOX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6KivRsbJwa%2B6U8LquNRSP%2FmK7WXw45orU%2FR55ltR9cgIgFFnQgoZ7S5YQArl4dVcQys3Rv71MCvfTbouC3oee%2BFUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG5bxLl030S7i58BircA%2FWV0wmtk9o0YkpTK%2FWcgurM1F1QWRNI%2BkeOMCWvs%2BSls9PwfWc%2Bdja2vd5HIN%2FlRCOLP%2Bkutj%2BOpf%2Fn9FBBxc0ZOzl8YK9QTiiJXYSCG0GY38IPN5WNVIHSlhrMpxcUda7iPbI3AGmAvA5860Go%2FV%2FmWLU9vRKN8TfP8qlJn%2B%2FdmYizhzenOufiWFPSnUMaEyibtwC2gj43a2DcfAwD0BFokf4nPPlBKg8gbGX61gn%2FDn2vYE69A8nG9kue8jkEp9UOK82%2BUWoJv49zLlS97rC2t9uHrhGcArwoNSzX%2BcSUkOwZ6I8UpvzZhsCLaxnPSJpk%2F5EAlZffBrVjdRXdXzVMhwfSEmnUv2A7Ua1r7qTz%2BOHz4FBZ9mYu9IXHn2rNp6SSRQzvxR83CTaF5mRkYNFdgrxCr6paO0U0lq7ZF0WFZE0hmsMxVdmaNOJRktdDI8%2Fw7wBJvirb%2B7L9Jcf%2FI9APAmdycwdHE%2FU8gBLBCW%2F4UTvpVRXEVLCHmGurOvqiV22AkdIhX1B6huLS07MyVBFh%2FoTbcryOLV071gKzq80pyEKJ63kncDmxXJNvq9QVr1eF595%2BftrDl7fqDKMaMUyqkqF7q6E1aLupgj7y8dZDBXNq3h83c3oOJTLpMKCo7bwGOqUB7AXV9%2Ft3y2iZaz4gEJ8qMUyktqKcWifqIj2QxhtaswvwU1CVoZRIp40hROuxm7bie%2FYE1GV34p80xzlah3gxzJb2jN9JSF1EroeItEOMQhGi7QCoHADl%2BiBRU1KCo9rnyEZgHYW4YNYvPLKsbLmIeHSBbtw0xSWPg35Pn4hDgWT9AQOf73wCViHFV4uRM%2FFFP6l9ePJOlZtPrYlxhUUE4dFy7Aqd&X-Amz-Signature=d7f6433c262e90a314d18acd43a7870e165d02b4f07bf8b67cf33754a80ae7c8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBKXLQOX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6KivRsbJwa%2B6U8LquNRSP%2FmK7WXw45orU%2FR55ltR9cgIgFFnQgoZ7S5YQArl4dVcQys3Rv71MCvfTbouC3oee%2BFUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG5bxLl030S7i58BircA%2FWV0wmtk9o0YkpTK%2FWcgurM1F1QWRNI%2BkeOMCWvs%2BSls9PwfWc%2Bdja2vd5HIN%2FlRCOLP%2Bkutj%2BOpf%2Fn9FBBxc0ZOzl8YK9QTiiJXYSCG0GY38IPN5WNVIHSlhrMpxcUda7iPbI3AGmAvA5860Go%2FV%2FmWLU9vRKN8TfP8qlJn%2B%2FdmYizhzenOufiWFPSnUMaEyibtwC2gj43a2DcfAwD0BFokf4nPPlBKg8gbGX61gn%2FDn2vYE69A8nG9kue8jkEp9UOK82%2BUWoJv49zLlS97rC2t9uHrhGcArwoNSzX%2BcSUkOwZ6I8UpvzZhsCLaxnPSJpk%2F5EAlZffBrVjdRXdXzVMhwfSEmnUv2A7Ua1r7qTz%2BOHz4FBZ9mYu9IXHn2rNp6SSRQzvxR83CTaF5mRkYNFdgrxCr6paO0U0lq7ZF0WFZE0hmsMxVdmaNOJRktdDI8%2Fw7wBJvirb%2B7L9Jcf%2FI9APAmdycwdHE%2FU8gBLBCW%2F4UTvpVRXEVLCHmGurOvqiV22AkdIhX1B6huLS07MyVBFh%2FoTbcryOLV071gKzq80pyEKJ63kncDmxXJNvq9QVr1eF595%2BftrDl7fqDKMaMUyqkqF7q6E1aLupgj7y8dZDBXNq3h83c3oOJTLpMKCo7bwGOqUB7AXV9%2Ft3y2iZaz4gEJ8qMUyktqKcWifqIj2QxhtaswvwU1CVoZRIp40hROuxm7bie%2FYE1GV34p80xzlah3gxzJb2jN9JSF1EroeItEOMQhGi7QCoHADl%2BiBRU1KCo9rnyEZgHYW4YNYvPLKsbLmIeHSBbtw0xSWPg35Pn4hDgWT9AQOf73wCViHFV4uRM%2FFFP6l9ePJOlZtPrYlxhUUE4dFy7Aqd&X-Amz-Signature=921df51f804e31b7b3928e5cb9e1c1914720881711f29b9c509e82a54c81a05a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBKXLQOX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6KivRsbJwa%2B6U8LquNRSP%2FmK7WXw45orU%2FR55ltR9cgIgFFnQgoZ7S5YQArl4dVcQys3Rv71MCvfTbouC3oee%2BFUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG5bxLl030S7i58BircA%2FWV0wmtk9o0YkpTK%2FWcgurM1F1QWRNI%2BkeOMCWvs%2BSls9PwfWc%2Bdja2vd5HIN%2FlRCOLP%2Bkutj%2BOpf%2Fn9FBBxc0ZOzl8YK9QTiiJXYSCG0GY38IPN5WNVIHSlhrMpxcUda7iPbI3AGmAvA5860Go%2FV%2FmWLU9vRKN8TfP8qlJn%2B%2FdmYizhzenOufiWFPSnUMaEyibtwC2gj43a2DcfAwD0BFokf4nPPlBKg8gbGX61gn%2FDn2vYE69A8nG9kue8jkEp9UOK82%2BUWoJv49zLlS97rC2t9uHrhGcArwoNSzX%2BcSUkOwZ6I8UpvzZhsCLaxnPSJpk%2F5EAlZffBrVjdRXdXzVMhwfSEmnUv2A7Ua1r7qTz%2BOHz4FBZ9mYu9IXHn2rNp6SSRQzvxR83CTaF5mRkYNFdgrxCr6paO0U0lq7ZF0WFZE0hmsMxVdmaNOJRktdDI8%2Fw7wBJvirb%2B7L9Jcf%2FI9APAmdycwdHE%2FU8gBLBCW%2F4UTvpVRXEVLCHmGurOvqiV22AkdIhX1B6huLS07MyVBFh%2FoTbcryOLV071gKzq80pyEKJ63kncDmxXJNvq9QVr1eF595%2BftrDl7fqDKMaMUyqkqF7q6E1aLupgj7y8dZDBXNq3h83c3oOJTLpMKCo7bwGOqUB7AXV9%2Ft3y2iZaz4gEJ8qMUyktqKcWifqIj2QxhtaswvwU1CVoZRIp40hROuxm7bie%2FYE1GV34p80xzlah3gxzJb2jN9JSF1EroeItEOMQhGi7QCoHADl%2BiBRU1KCo9rnyEZgHYW4YNYvPLKsbLmIeHSBbtw0xSWPg35Pn4hDgWT9AQOf73wCViHFV4uRM%2FFFP6l9ePJOlZtPrYlxhUUE4dFy7Aqd&X-Amz-Signature=84ad46530f3420fe4d0447914c5aad343041dd690b1b3ad6b0bb904730e7f277&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBKXLQOX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6KivRsbJwa%2B6U8LquNRSP%2FmK7WXw45orU%2FR55ltR9cgIgFFnQgoZ7S5YQArl4dVcQys3Rv71MCvfTbouC3oee%2BFUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG5bxLl030S7i58BircA%2FWV0wmtk9o0YkpTK%2FWcgurM1F1QWRNI%2BkeOMCWvs%2BSls9PwfWc%2Bdja2vd5HIN%2FlRCOLP%2Bkutj%2BOpf%2Fn9FBBxc0ZOzl8YK9QTiiJXYSCG0GY38IPN5WNVIHSlhrMpxcUda7iPbI3AGmAvA5860Go%2FV%2FmWLU9vRKN8TfP8qlJn%2B%2FdmYizhzenOufiWFPSnUMaEyibtwC2gj43a2DcfAwD0BFokf4nPPlBKg8gbGX61gn%2FDn2vYE69A8nG9kue8jkEp9UOK82%2BUWoJv49zLlS97rC2t9uHrhGcArwoNSzX%2BcSUkOwZ6I8UpvzZhsCLaxnPSJpk%2F5EAlZffBrVjdRXdXzVMhwfSEmnUv2A7Ua1r7qTz%2BOHz4FBZ9mYu9IXHn2rNp6SSRQzvxR83CTaF5mRkYNFdgrxCr6paO0U0lq7ZF0WFZE0hmsMxVdmaNOJRktdDI8%2Fw7wBJvirb%2B7L9Jcf%2FI9APAmdycwdHE%2FU8gBLBCW%2F4UTvpVRXEVLCHmGurOvqiV22AkdIhX1B6huLS07MyVBFh%2FoTbcryOLV071gKzq80pyEKJ63kncDmxXJNvq9QVr1eF595%2BftrDl7fqDKMaMUyqkqF7q6E1aLupgj7y8dZDBXNq3h83c3oOJTLpMKCo7bwGOqUB7AXV9%2Ft3y2iZaz4gEJ8qMUyktqKcWifqIj2QxhtaswvwU1CVoZRIp40hROuxm7bie%2FYE1GV34p80xzlah3gxzJb2jN9JSF1EroeItEOMQhGi7QCoHADl%2BiBRU1KCo9rnyEZgHYW4YNYvPLKsbLmIeHSBbtw0xSWPg35Pn4hDgWT9AQOf73wCViHFV4uRM%2FFFP6l9ePJOlZtPrYlxhUUE4dFy7Aqd&X-Amz-Signature=2cc5310d290e31c478ff892e9da650e4c793f9daeef0dd78a254e19583d04b16&X-Amz-SignedHeaders=host&x-id=GetObject)
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


