

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO3QHIAY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIG7IHsai%2FSTVwrn%2FrcdgydjLLoeVzGZM24Ymmq3TXI%2F9AiEAitXapU1yUP%2FvUX9pHO9%2BcbCYLiVwy7k1orX3pyS7Hdoq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMhWvWjllctLMDyHkSrcA402ybkXCFvM5qFwHMGOlG2Ui688WST8yE2dOdrXzspzv%2FxSfoOD7y279%2BUCO%2BFkHBRuhZi%2BeQZURIx9ERLOkmieHTNMUhp9YfgH6JnFx8nxEq3nCv87wiwio1qKVOxHIvBU%2F19Y9ndllgK7fp5aClePpSDEsaa3z64MebsMFhz4uJJzVSGhtBr1RR2mhF068bmXHWjbqsnn%2FipxSQjNsCW9KfNyI2HH88zLpAQaDqDaZr4utsd04chsQpxqjMLkT%2F2wi8Vq3vhS97Ih0VbDQ%2Bd1%2F%2BoS0AOsLgcOKzAtfFAQElzPwLGMaXYoxWwXUSTAlnaVeIY0rwE1IDxwbSeqshFXhVA2ZTeJc4cTNQCtzrEGPVOHcOml7J1VAWC1fs655UVWjMbYRP23nbMLoNsB2ibB2j8WPf1GvxKbGvPT7MDuNFlneEgZfQkqAQbfRKh67UljfbQTalmJ5tmTXSrHXowJe7NAZMhJcGtcNxdLTw6tPJfyU71hOVeL4hdq%2FFw%2B5jFA9IHaXizvBK4uPxmjQT4R%2Fxz%2B11VAb3iI6ARYNJngas2KaKY%2BLYIoDSFfrLbMi586SqHgCYu1f3c55z%2FwOkS7MqJ8CaOY6GN4tn8Jhj%2BHPHZ2K7uXrZx6EQpKMMOZkb0GOqUBWsn41sbKBwgVNIN%2BDU94vgVg5Hc9MUjzU%2BNBpaxB8HWMWM%2FHN6VGYJVeoyZI8KhMayHLwiIYsaG3sYerXEr3GNfrs7GN4mReUyGaSYpz8MsdfDLCxbpIUBaySV0xQCyyGvE%2FXl8mYd2FvE%2FpfHGXM%2BHpYzF4FlhVwuHJMu8BIExXYQhhnjwZvECc8cNWUidImFSzeaQsnjSxHZnEJkHEZcTZrwh1&X-Amz-Signature=be184971909ab55312c7d82e6f473e1be1ca3ca04e0fc9ae69e29e9986495c24&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUTTIRP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIAoZCykh2g3EwXWLjA7vT3Y%2BrPE%2BUECNHDX0w7TFbmiMAiEAm0JnmJM%2Fh9syG7bM2sdBP%2BiGdduBJAStpYymMeQSbjIq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDM0DmV%2BflojL%2Bo%2B0ACrcA5M66%2BtZBSrwJLf80Req4akb8oJ8Dh8sh6RyGLLkdmbsQesV%2BLz1%2BRnBj52014MmFf6BNm%2Bv5R8NFQyLHxRMzbw3dbLPAet63gPxzPOU%2B8u5mOpVj8C%2F7gk9BF021wbPbcR1xGW6MWIeqOCk4h%2FXegXBXMc9G60utChZ0Z4HiJoA4DJjBG62dOTNlP5o23l9LYJmjRJ7v%2BYBH1Z1GbkgSEyXX3ggbwhE7oRb2t942FFXSfuAr41mcgHNtrYeYJBkQ%2Fz1ACST26sY5etTTgNbmtu5Vw4HyLbXusJq%2FhNci9VhoBMTaJLCv82UoSbCQEmrOkguhZUXo4RUjaRtswjDjtFBOXkIp4H3k7H%2BRo%2FAcYp0FZr0BaQoN6iMv5XHSGXrtBxiCjH3N3JBDhwKbV%2BLtRiMB09zbNpdKpfVb0mnblr4Tmd2LjBpNPH6kRTT0PVUHWr52FZXf%2BcIszWYlw%2BElBp6%2FYkXe5uU7%2B6eO3uXzEyl1LIw8SYj%2BJ6apRNzwlmj8M6%2BgNUX6KTfXAIEH30B8rCocw91heXn0uEDTDu6%2FksWTIPRtfNdSADpx78%2F0fIZomDVVpB1BISe%2FfgzP0mAXSXVsHElSK7n6L7jFbMcXmSH%2BNxZKoOzw1ntpEfxMISZkb0GOqUBaEWuvDO57pW%2BIuJP9ViewYdpVJAZEGKAlz77%2BoOVNgCygoJlDWePdE7tQeDOyGX76XSixva%2Fovsv%2B74%2FeHX4Y1rMJSKbRvuJbdY2pakHQQQmG%2FyWUHKXf66TyEgMe4Yp0aG51bbIeXeM3BSxldojUHvdLUyvXf%2B5%2BJI218EdTLUsbFlxftv9wnvtej5TfX%2FrpGGfBfJtKHzM7bPOT10Dl26dVlnf&X-Amz-Signature=369b845400319c0563168949a3f74065afe628cf969ea98e71855706dab16ad0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUTTIRP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIAoZCykh2g3EwXWLjA7vT3Y%2BrPE%2BUECNHDX0w7TFbmiMAiEAm0JnmJM%2Fh9syG7bM2sdBP%2BiGdduBJAStpYymMeQSbjIq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDM0DmV%2BflojL%2Bo%2B0ACrcA5M66%2BtZBSrwJLf80Req4akb8oJ8Dh8sh6RyGLLkdmbsQesV%2BLz1%2BRnBj52014MmFf6BNm%2Bv5R8NFQyLHxRMzbw3dbLPAet63gPxzPOU%2B8u5mOpVj8C%2F7gk9BF021wbPbcR1xGW6MWIeqOCk4h%2FXegXBXMc9G60utChZ0Z4HiJoA4DJjBG62dOTNlP5o23l9LYJmjRJ7v%2BYBH1Z1GbkgSEyXX3ggbwhE7oRb2t942FFXSfuAr41mcgHNtrYeYJBkQ%2Fz1ACST26sY5etTTgNbmtu5Vw4HyLbXusJq%2FhNci9VhoBMTaJLCv82UoSbCQEmrOkguhZUXo4RUjaRtswjDjtFBOXkIp4H3k7H%2BRo%2FAcYp0FZr0BaQoN6iMv5XHSGXrtBxiCjH3N3JBDhwKbV%2BLtRiMB09zbNpdKpfVb0mnblr4Tmd2LjBpNPH6kRTT0PVUHWr52FZXf%2BcIszWYlw%2BElBp6%2FYkXe5uU7%2B6eO3uXzEyl1LIw8SYj%2BJ6apRNzwlmj8M6%2BgNUX6KTfXAIEH30B8rCocw91heXn0uEDTDu6%2FksWTIPRtfNdSADpx78%2F0fIZomDVVpB1BISe%2FfgzP0mAXSXVsHElSK7n6L7jFbMcXmSH%2BNxZKoOzw1ntpEfxMISZkb0GOqUBaEWuvDO57pW%2BIuJP9ViewYdpVJAZEGKAlz77%2BoOVNgCygoJlDWePdE7tQeDOyGX76XSixva%2Fovsv%2B74%2FeHX4Y1rMJSKbRvuJbdY2pakHQQQmG%2FyWUHKXf66TyEgMe4Yp0aG51bbIeXeM3BSxldojUHvdLUyvXf%2B5%2BJI218EdTLUsbFlxftv9wnvtej5TfX%2FrpGGfBfJtKHzM7bPOT10Dl26dVlnf&X-Amz-Signature=d20e8fcea659ebc75011d8318f0a1295ed07e273a1b05d2605ca7f11187fd186&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUTTIRP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIAoZCykh2g3EwXWLjA7vT3Y%2BrPE%2BUECNHDX0w7TFbmiMAiEAm0JnmJM%2Fh9syG7bM2sdBP%2BiGdduBJAStpYymMeQSbjIq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDM0DmV%2BflojL%2Bo%2B0ACrcA5M66%2BtZBSrwJLf80Req4akb8oJ8Dh8sh6RyGLLkdmbsQesV%2BLz1%2BRnBj52014MmFf6BNm%2Bv5R8NFQyLHxRMzbw3dbLPAet63gPxzPOU%2B8u5mOpVj8C%2F7gk9BF021wbPbcR1xGW6MWIeqOCk4h%2FXegXBXMc9G60utChZ0Z4HiJoA4DJjBG62dOTNlP5o23l9LYJmjRJ7v%2BYBH1Z1GbkgSEyXX3ggbwhE7oRb2t942FFXSfuAr41mcgHNtrYeYJBkQ%2Fz1ACST26sY5etTTgNbmtu5Vw4HyLbXusJq%2FhNci9VhoBMTaJLCv82UoSbCQEmrOkguhZUXo4RUjaRtswjDjtFBOXkIp4H3k7H%2BRo%2FAcYp0FZr0BaQoN6iMv5XHSGXrtBxiCjH3N3JBDhwKbV%2BLtRiMB09zbNpdKpfVb0mnblr4Tmd2LjBpNPH6kRTT0PVUHWr52FZXf%2BcIszWYlw%2BElBp6%2FYkXe5uU7%2B6eO3uXzEyl1LIw8SYj%2BJ6apRNzwlmj8M6%2BgNUX6KTfXAIEH30B8rCocw91heXn0uEDTDu6%2FksWTIPRtfNdSADpx78%2F0fIZomDVVpB1BISe%2FfgzP0mAXSXVsHElSK7n6L7jFbMcXmSH%2BNxZKoOzw1ntpEfxMISZkb0GOqUBaEWuvDO57pW%2BIuJP9ViewYdpVJAZEGKAlz77%2BoOVNgCygoJlDWePdE7tQeDOyGX76XSixva%2Fovsv%2B74%2FeHX4Y1rMJSKbRvuJbdY2pakHQQQmG%2FyWUHKXf66TyEgMe4Yp0aG51bbIeXeM3BSxldojUHvdLUyvXf%2B5%2BJI218EdTLUsbFlxftv9wnvtej5TfX%2FrpGGfBfJtKHzM7bPOT10Dl26dVlnf&X-Amz-Signature=15247805d342e685b32dfed3afa92218091d60cf93e4fbe6f9d5ddb765508125&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUTTIRP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIAoZCykh2g3EwXWLjA7vT3Y%2BrPE%2BUECNHDX0w7TFbmiMAiEAm0JnmJM%2Fh9syG7bM2sdBP%2BiGdduBJAStpYymMeQSbjIq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDM0DmV%2BflojL%2Bo%2B0ACrcA5M66%2BtZBSrwJLf80Req4akb8oJ8Dh8sh6RyGLLkdmbsQesV%2BLz1%2BRnBj52014MmFf6BNm%2Bv5R8NFQyLHxRMzbw3dbLPAet63gPxzPOU%2B8u5mOpVj8C%2F7gk9BF021wbPbcR1xGW6MWIeqOCk4h%2FXegXBXMc9G60utChZ0Z4HiJoA4DJjBG62dOTNlP5o23l9LYJmjRJ7v%2BYBH1Z1GbkgSEyXX3ggbwhE7oRb2t942FFXSfuAr41mcgHNtrYeYJBkQ%2Fz1ACST26sY5etTTgNbmtu5Vw4HyLbXusJq%2FhNci9VhoBMTaJLCv82UoSbCQEmrOkguhZUXo4RUjaRtswjDjtFBOXkIp4H3k7H%2BRo%2FAcYp0FZr0BaQoN6iMv5XHSGXrtBxiCjH3N3JBDhwKbV%2BLtRiMB09zbNpdKpfVb0mnblr4Tmd2LjBpNPH6kRTT0PVUHWr52FZXf%2BcIszWYlw%2BElBp6%2FYkXe5uU7%2B6eO3uXzEyl1LIw8SYj%2BJ6apRNzwlmj8M6%2BgNUX6KTfXAIEH30B8rCocw91heXn0uEDTDu6%2FksWTIPRtfNdSADpx78%2F0fIZomDVVpB1BISe%2FfgzP0mAXSXVsHElSK7n6L7jFbMcXmSH%2BNxZKoOzw1ntpEfxMISZkb0GOqUBaEWuvDO57pW%2BIuJP9ViewYdpVJAZEGKAlz77%2BoOVNgCygoJlDWePdE7tQeDOyGX76XSixva%2Fovsv%2B74%2FeHX4Y1rMJSKbRvuJbdY2pakHQQQmG%2FyWUHKXf66TyEgMe4Yp0aG51bbIeXeM3BSxldojUHvdLUyvXf%2B5%2BJI218EdTLUsbFlxftv9wnvtej5TfX%2FrpGGfBfJtKHzM7bPOT10Dl26dVlnf&X-Amz-Signature=405cff8dcada0104a7863dbf3994250e543e82129da5d91f04745d84d443ae1c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DUTTIRP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIAoZCykh2g3EwXWLjA7vT3Y%2BrPE%2BUECNHDX0w7TFbmiMAiEAm0JnmJM%2Fh9syG7bM2sdBP%2BiGdduBJAStpYymMeQSbjIq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDM0DmV%2BflojL%2Bo%2B0ACrcA5M66%2BtZBSrwJLf80Req4akb8oJ8Dh8sh6RyGLLkdmbsQesV%2BLz1%2BRnBj52014MmFf6BNm%2Bv5R8NFQyLHxRMzbw3dbLPAet63gPxzPOU%2B8u5mOpVj8C%2F7gk9BF021wbPbcR1xGW6MWIeqOCk4h%2FXegXBXMc9G60utChZ0Z4HiJoA4DJjBG62dOTNlP5o23l9LYJmjRJ7v%2BYBH1Z1GbkgSEyXX3ggbwhE7oRb2t942FFXSfuAr41mcgHNtrYeYJBkQ%2Fz1ACST26sY5etTTgNbmtu5Vw4HyLbXusJq%2FhNci9VhoBMTaJLCv82UoSbCQEmrOkguhZUXo4RUjaRtswjDjtFBOXkIp4H3k7H%2BRo%2FAcYp0FZr0BaQoN6iMv5XHSGXrtBxiCjH3N3JBDhwKbV%2BLtRiMB09zbNpdKpfVb0mnblr4Tmd2LjBpNPH6kRTT0PVUHWr52FZXf%2BcIszWYlw%2BElBp6%2FYkXe5uU7%2B6eO3uXzEyl1LIw8SYj%2BJ6apRNzwlmj8M6%2BgNUX6KTfXAIEH30B8rCocw91heXn0uEDTDu6%2FksWTIPRtfNdSADpx78%2F0fIZomDVVpB1BISe%2FfgzP0mAXSXVsHElSK7n6L7jFbMcXmSH%2BNxZKoOzw1ntpEfxMISZkb0GOqUBaEWuvDO57pW%2BIuJP9ViewYdpVJAZEGKAlz77%2BoOVNgCygoJlDWePdE7tQeDOyGX76XSixva%2Fovsv%2B74%2FeHX4Y1rMJSKbRvuJbdY2pakHQQQmG%2FyWUHKXf66TyEgMe4Yp0aG51bbIeXeM3BSxldojUHvdLUyvXf%2B5%2BJI218EdTLUsbFlxftv9wnvtej5TfX%2FrpGGfBfJtKHzM7bPOT10Dl26dVlnf&X-Amz-Signature=9bb5996b5cdd7855b401ebcefad89060a69082cfa464d7257c245c9b107afe65&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO3QHIAY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIG7IHsai%2FSTVwrn%2FrcdgydjLLoeVzGZM24Ymmq3TXI%2F9AiEAitXapU1yUP%2FvUX9pHO9%2BcbCYLiVwy7k1orX3pyS7Hdoq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMhWvWjllctLMDyHkSrcA402ybkXCFvM5qFwHMGOlG2Ui688WST8yE2dOdrXzspzv%2FxSfoOD7y279%2BUCO%2BFkHBRuhZi%2BeQZURIx9ERLOkmieHTNMUhp9YfgH6JnFx8nxEq3nCv87wiwio1qKVOxHIvBU%2F19Y9ndllgK7fp5aClePpSDEsaa3z64MebsMFhz4uJJzVSGhtBr1RR2mhF068bmXHWjbqsnn%2FipxSQjNsCW9KfNyI2HH88zLpAQaDqDaZr4utsd04chsQpxqjMLkT%2F2wi8Vq3vhS97Ih0VbDQ%2Bd1%2F%2BoS0AOsLgcOKzAtfFAQElzPwLGMaXYoxWwXUSTAlnaVeIY0rwE1IDxwbSeqshFXhVA2ZTeJc4cTNQCtzrEGPVOHcOml7J1VAWC1fs655UVWjMbYRP23nbMLoNsB2ibB2j8WPf1GvxKbGvPT7MDuNFlneEgZfQkqAQbfRKh67UljfbQTalmJ5tmTXSrHXowJe7NAZMhJcGtcNxdLTw6tPJfyU71hOVeL4hdq%2FFw%2B5jFA9IHaXizvBK4uPxmjQT4R%2Fxz%2B11VAb3iI6ARYNJngas2KaKY%2BLYIoDSFfrLbMi586SqHgCYu1f3c55z%2FwOkS7MqJ8CaOY6GN4tn8Jhj%2BHPHZ2K7uXrZx6EQpKMMOZkb0GOqUBWsn41sbKBwgVNIN%2BDU94vgVg5Hc9MUjzU%2BNBpaxB8HWMWM%2FHN6VGYJVeoyZI8KhMayHLwiIYsaG3sYerXEr3GNfrs7GN4mReUyGaSYpz8MsdfDLCxbpIUBaySV0xQCyyGvE%2FXl8mYd2FvE%2FpfHGXM%2BHpYzF4FlhVwuHJMu8BIExXYQhhnjwZvECc8cNWUidImFSzeaQsnjSxHZnEJkHEZcTZrwh1&X-Amz-Signature=f1a6e1f19340afc51f9a8edef4aa27566ff9ea9480302c09eca921c0cae6de44&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO3QHIAY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIG7IHsai%2FSTVwrn%2FrcdgydjLLoeVzGZM24Ymmq3TXI%2F9AiEAitXapU1yUP%2FvUX9pHO9%2BcbCYLiVwy7k1orX3pyS7Hdoq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMhWvWjllctLMDyHkSrcA402ybkXCFvM5qFwHMGOlG2Ui688WST8yE2dOdrXzspzv%2FxSfoOD7y279%2BUCO%2BFkHBRuhZi%2BeQZURIx9ERLOkmieHTNMUhp9YfgH6JnFx8nxEq3nCv87wiwio1qKVOxHIvBU%2F19Y9ndllgK7fp5aClePpSDEsaa3z64MebsMFhz4uJJzVSGhtBr1RR2mhF068bmXHWjbqsnn%2FipxSQjNsCW9KfNyI2HH88zLpAQaDqDaZr4utsd04chsQpxqjMLkT%2F2wi8Vq3vhS97Ih0VbDQ%2Bd1%2F%2BoS0AOsLgcOKzAtfFAQElzPwLGMaXYoxWwXUSTAlnaVeIY0rwE1IDxwbSeqshFXhVA2ZTeJc4cTNQCtzrEGPVOHcOml7J1VAWC1fs655UVWjMbYRP23nbMLoNsB2ibB2j8WPf1GvxKbGvPT7MDuNFlneEgZfQkqAQbfRKh67UljfbQTalmJ5tmTXSrHXowJe7NAZMhJcGtcNxdLTw6tPJfyU71hOVeL4hdq%2FFw%2B5jFA9IHaXizvBK4uPxmjQT4R%2Fxz%2B11VAb3iI6ARYNJngas2KaKY%2BLYIoDSFfrLbMi586SqHgCYu1f3c55z%2FwOkS7MqJ8CaOY6GN4tn8Jhj%2BHPHZ2K7uXrZx6EQpKMMOZkb0GOqUBWsn41sbKBwgVNIN%2BDU94vgVg5Hc9MUjzU%2BNBpaxB8HWMWM%2FHN6VGYJVeoyZI8KhMayHLwiIYsaG3sYerXEr3GNfrs7GN4mReUyGaSYpz8MsdfDLCxbpIUBaySV0xQCyyGvE%2FXl8mYd2FvE%2FpfHGXM%2BHpYzF4FlhVwuHJMu8BIExXYQhhnjwZvECc8cNWUidImFSzeaQsnjSxHZnEJkHEZcTZrwh1&X-Amz-Signature=9b92cd1a929acca29da896aa2aafcc6b459fd037c6a14f2937f7f6a6a2851a0b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO3QHIAY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIG7IHsai%2FSTVwrn%2FrcdgydjLLoeVzGZM24Ymmq3TXI%2F9AiEAitXapU1yUP%2FvUX9pHO9%2BcbCYLiVwy7k1orX3pyS7Hdoq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMhWvWjllctLMDyHkSrcA402ybkXCFvM5qFwHMGOlG2Ui688WST8yE2dOdrXzspzv%2FxSfoOD7y279%2BUCO%2BFkHBRuhZi%2BeQZURIx9ERLOkmieHTNMUhp9YfgH6JnFx8nxEq3nCv87wiwio1qKVOxHIvBU%2F19Y9ndllgK7fp5aClePpSDEsaa3z64MebsMFhz4uJJzVSGhtBr1RR2mhF068bmXHWjbqsnn%2FipxSQjNsCW9KfNyI2HH88zLpAQaDqDaZr4utsd04chsQpxqjMLkT%2F2wi8Vq3vhS97Ih0VbDQ%2Bd1%2F%2BoS0AOsLgcOKzAtfFAQElzPwLGMaXYoxWwXUSTAlnaVeIY0rwE1IDxwbSeqshFXhVA2ZTeJc4cTNQCtzrEGPVOHcOml7J1VAWC1fs655UVWjMbYRP23nbMLoNsB2ibB2j8WPf1GvxKbGvPT7MDuNFlneEgZfQkqAQbfRKh67UljfbQTalmJ5tmTXSrHXowJe7NAZMhJcGtcNxdLTw6tPJfyU71hOVeL4hdq%2FFw%2B5jFA9IHaXizvBK4uPxmjQT4R%2Fxz%2B11VAb3iI6ARYNJngas2KaKY%2BLYIoDSFfrLbMi586SqHgCYu1f3c55z%2FwOkS7MqJ8CaOY6GN4tn8Jhj%2BHPHZ2K7uXrZx6EQpKMMOZkb0GOqUBWsn41sbKBwgVNIN%2BDU94vgVg5Hc9MUjzU%2BNBpaxB8HWMWM%2FHN6VGYJVeoyZI8KhMayHLwiIYsaG3sYerXEr3GNfrs7GN4mReUyGaSYpz8MsdfDLCxbpIUBaySV0xQCyyGvE%2FXl8mYd2FvE%2FpfHGXM%2BHpYzF4FlhVwuHJMu8BIExXYQhhnjwZvECc8cNWUidImFSzeaQsnjSxHZnEJkHEZcTZrwh1&X-Amz-Signature=865de7ce194aaa0d67be4cfa71a3e16aa603ff10f2885fc25d346caa857ca7e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO3QHIAY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIG7IHsai%2FSTVwrn%2FrcdgydjLLoeVzGZM24Ymmq3TXI%2F9AiEAitXapU1yUP%2FvUX9pHO9%2BcbCYLiVwy7k1orX3pyS7Hdoq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMhWvWjllctLMDyHkSrcA402ybkXCFvM5qFwHMGOlG2Ui688WST8yE2dOdrXzspzv%2FxSfoOD7y279%2BUCO%2BFkHBRuhZi%2BeQZURIx9ERLOkmieHTNMUhp9YfgH6JnFx8nxEq3nCv87wiwio1qKVOxHIvBU%2F19Y9ndllgK7fp5aClePpSDEsaa3z64MebsMFhz4uJJzVSGhtBr1RR2mhF068bmXHWjbqsnn%2FipxSQjNsCW9KfNyI2HH88zLpAQaDqDaZr4utsd04chsQpxqjMLkT%2F2wi8Vq3vhS97Ih0VbDQ%2Bd1%2F%2BoS0AOsLgcOKzAtfFAQElzPwLGMaXYoxWwXUSTAlnaVeIY0rwE1IDxwbSeqshFXhVA2ZTeJc4cTNQCtzrEGPVOHcOml7J1VAWC1fs655UVWjMbYRP23nbMLoNsB2ibB2j8WPf1GvxKbGvPT7MDuNFlneEgZfQkqAQbfRKh67UljfbQTalmJ5tmTXSrHXowJe7NAZMhJcGtcNxdLTw6tPJfyU71hOVeL4hdq%2FFw%2B5jFA9IHaXizvBK4uPxmjQT4R%2Fxz%2B11VAb3iI6ARYNJngas2KaKY%2BLYIoDSFfrLbMi586SqHgCYu1f3c55z%2FwOkS7MqJ8CaOY6GN4tn8Jhj%2BHPHZ2K7uXrZx6EQpKMMOZkb0GOqUBWsn41sbKBwgVNIN%2BDU94vgVg5Hc9MUjzU%2BNBpaxB8HWMWM%2FHN6VGYJVeoyZI8KhMayHLwiIYsaG3sYerXEr3GNfrs7GN4mReUyGaSYpz8MsdfDLCxbpIUBaySV0xQCyyGvE%2FXl8mYd2FvE%2FpfHGXM%2BHpYzF4FlhVwuHJMu8BIExXYQhhnjwZvECc8cNWUidImFSzeaQsnjSxHZnEJkHEZcTZrwh1&X-Amz-Signature=a5c031915b2ee1722c55774baccc95e15e905cd11ffaebf3d5c6c22ff83f320b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO3QHIAY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIG7IHsai%2FSTVwrn%2FrcdgydjLLoeVzGZM24Ymmq3TXI%2F9AiEAitXapU1yUP%2FvUX9pHO9%2BcbCYLiVwy7k1orX3pyS7Hdoq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMhWvWjllctLMDyHkSrcA402ybkXCFvM5qFwHMGOlG2Ui688WST8yE2dOdrXzspzv%2FxSfoOD7y279%2BUCO%2BFkHBRuhZi%2BeQZURIx9ERLOkmieHTNMUhp9YfgH6JnFx8nxEq3nCv87wiwio1qKVOxHIvBU%2F19Y9ndllgK7fp5aClePpSDEsaa3z64MebsMFhz4uJJzVSGhtBr1RR2mhF068bmXHWjbqsnn%2FipxSQjNsCW9KfNyI2HH88zLpAQaDqDaZr4utsd04chsQpxqjMLkT%2F2wi8Vq3vhS97Ih0VbDQ%2Bd1%2F%2BoS0AOsLgcOKzAtfFAQElzPwLGMaXYoxWwXUSTAlnaVeIY0rwE1IDxwbSeqshFXhVA2ZTeJc4cTNQCtzrEGPVOHcOml7J1VAWC1fs655UVWjMbYRP23nbMLoNsB2ibB2j8WPf1GvxKbGvPT7MDuNFlneEgZfQkqAQbfRKh67UljfbQTalmJ5tmTXSrHXowJe7NAZMhJcGtcNxdLTw6tPJfyU71hOVeL4hdq%2FFw%2B5jFA9IHaXizvBK4uPxmjQT4R%2Fxz%2B11VAb3iI6ARYNJngas2KaKY%2BLYIoDSFfrLbMi586SqHgCYu1f3c55z%2FwOkS7MqJ8CaOY6GN4tn8Jhj%2BHPHZ2K7uXrZx6EQpKMMOZkb0GOqUBWsn41sbKBwgVNIN%2BDU94vgVg5Hc9MUjzU%2BNBpaxB8HWMWM%2FHN6VGYJVeoyZI8KhMayHLwiIYsaG3sYerXEr3GNfrs7GN4mReUyGaSYpz8MsdfDLCxbpIUBaySV0xQCyyGvE%2FXl8mYd2FvE%2FpfHGXM%2BHpYzF4FlhVwuHJMu8BIExXYQhhnjwZvECc8cNWUidImFSzeaQsnjSxHZnEJkHEZcTZrwh1&X-Amz-Signature=1d180b83463363cabf47f039612fc3b3addebf83b5918616363df7071e84295d&X-Amz-SignedHeaders=host&x-id=GetObject)
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


