

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVGLRL3S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHxnjf3qwHmv4P5xi%2Fb9ZL86QBA1FAgsT71GVMdWyp6yAiB7cwxavqJrDbuemjLyug9iuCbyC4%2FMQANmMHWOQ7mhKyr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMJ2XuVGFHNLPndxjkKtwDIbGI5%2BPX%2F0S%2F7qGFbgK6ecU6kZsRcY2uq1fM3Ouc1CmBenL2t9tY%2BIb1MdXQOV2dW2VrKBAwNbahJofxibmAXVuQLCthZ4p7int7WxOn%2FPczISC4cTe5xH60PrUTjcVYlp7FwSZ9Od6wC%2BPBwWJXRfAfR7iSYHsY%2FhwnYH%2BNi%2F6lXOaFKNoG6FoXf3TyaHm6VnAd7sx0I%2F8IbHn3BOcuE9I%2BuJBkEF%2BGs09sWCuYHA8J6sg4u1csnOQdgMA0OlosZYcoQdebH%2FHoDk2bNCJ5ZtVswXSgL0EbugHdCausaVWM7phxjTob0Smtc935%2FnWU04WWTPbaxV29zkY3%2Fya1iTWD3Kw8c0p4D233LAqI9xxYujVmPAAB7TGXnaAy0%2B2c2YBZZD29Sa5Gj62F8bHFU7ujmzl%2FADb8v8sSgGe%2F%2F3NWZdbEukFISfkMqRvas%2BvX6sG5tVty2Iih3ChgDJVJedafSPIKaIvxAwTUPYWAv5kuAINQsg7GaZIyqFEwvgVb3TIzmqMckEQwuNoHLZXXfy33JhKKJgPtnx26B1BoIq5Z32LjRqKjcrBUwTWYoW%2B6mRKg95q6pXl01OBTn0i6y%2BL7u8jnTLqdxOsKZbVf%2F8mdNjUpKSD%2FshDZdLYwi92PvQY6pgEvQ87rDo0N9k%2BW1Mq5WK%2FnK%2BYu%2BeTYT1y9LdN3YQq5ynP5NDDM6r9pcuVcIVhw0lJzQ3lHqYx3zzx75oBKvYHmSCgUpICupo1MbFG5zNMMBmR3vYCcPsqLHr9KZEXPk05F9x2LonVzYedU1jXHmGCa4eKcRRMFSJQLxwgiHZ0jQVJiProjQ5WNqI9QZE3PNriuU9nPP4viOvW2O0rRr7m4Amq6txGQ&X-Amz-Signature=54aa1c55386e2929f6308da8afe88524e9742dbcdbd426255ffbfdcfaf85ff89&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOFHMCZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCICZHeVLwauSH9keBRo2W1fpQOqcF9End%2FVPJ90Uk3Z0lAiEA0jyDhXgK8zGP2RiWUONCybCASi6CUgzOooOCl73GRkYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPy9qkd2zmqVsv%2BoXyrcA25j4C1XbNlCCJZd6n5vROhhrY6MYkRVnKYWTLNnthUlnlMEX0n%2FtQNcAgATe2S3GMgulVA1yGPlTa2LlV%2FCDg3DcLi6ZSMeyG2SIXDQOB2BaHlX63Y1iRTgy8ak6%2B95oTjV2%2FoNBsSCIRIQTrKbh1BDbngyecug%2FNgSyJ6Yirhi%2Fwh5efMjLLThaOCyvLYx2TFWRQ%2B2%2FVMnnCqvYPmHXUtLZzese05ILG%2BxS5mYwuhaJbSV0pQsH45%2Fyoc5u3rgNVLiIbptOJ9MB7Wr%2F%2BXcawVcifgXu1ze7mv5eTjeAX8Ij9CDkr99WDeB2sJiDmMBBe8NPqr%2BqO7Ea4HkJP8H5i51X2apvbNOhXfOELInOgyET2UZdcSY%2F7mADIZrzuk4hvsKnO94ilxyszWmQZVOLL4z%2BMBgv88v07TY6hR81WXNN%2BUrg2zFemKu4C3dPIDu3woWZVKRgpQegHga5KKc94XZJ3oeV6qFhbZ%2Bzf0%2FtslzmkYcv5%2FBPY5avBhtmGKwAWuHzg45OxU0lEv5CnUujjK%2FRBDOSL5J7iNUWYluqQgi8WTbZDxcq44e%2BYoSCSL%2Bm6MqOsYldNMG7fPODrm4MqD6z4smtGqSkyERVrpIQzL2TIVu9j0iU0hfCAG3MMi7jr0GOqUBZzTDyj2jrowc6su72fN4fQhUE%2BS6bQyqWsduDtn%2Bgw%2BJbM6mCpCNvpVVJ4hfWgfdRVfTRjRK3H4IPorBiHdAoXpnyumdqflUkrk5DpCuPtpuURvM5FWWmtb%2FHxU2NBtdooou2%2F0GcuEJ11vOqEoeQQvYLm8sH3w15FuH8gssfb%2F149yk37pKaBkf64vHB%2FEPvC76z0ZhXsvPtLSP1Vd%2FqRXNg9Zs&X-Amz-Signature=8ee49db5c18287c42c0fb01cd32caec974741d38ca3b4269147e6239c8ec2247&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOFHMCZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCICZHeVLwauSH9keBRo2W1fpQOqcF9End%2FVPJ90Uk3Z0lAiEA0jyDhXgK8zGP2RiWUONCybCASi6CUgzOooOCl73GRkYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPy9qkd2zmqVsv%2BoXyrcA25j4C1XbNlCCJZd6n5vROhhrY6MYkRVnKYWTLNnthUlnlMEX0n%2FtQNcAgATe2S3GMgulVA1yGPlTa2LlV%2FCDg3DcLi6ZSMeyG2SIXDQOB2BaHlX63Y1iRTgy8ak6%2B95oTjV2%2FoNBsSCIRIQTrKbh1BDbngyecug%2FNgSyJ6Yirhi%2Fwh5efMjLLThaOCyvLYx2TFWRQ%2B2%2FVMnnCqvYPmHXUtLZzese05ILG%2BxS5mYwuhaJbSV0pQsH45%2Fyoc5u3rgNVLiIbptOJ9MB7Wr%2F%2BXcawVcifgXu1ze7mv5eTjeAX8Ij9CDkr99WDeB2sJiDmMBBe8NPqr%2BqO7Ea4HkJP8H5i51X2apvbNOhXfOELInOgyET2UZdcSY%2F7mADIZrzuk4hvsKnO94ilxyszWmQZVOLL4z%2BMBgv88v07TY6hR81WXNN%2BUrg2zFemKu4C3dPIDu3woWZVKRgpQegHga5KKc94XZJ3oeV6qFhbZ%2Bzf0%2FtslzmkYcv5%2FBPY5avBhtmGKwAWuHzg45OxU0lEv5CnUujjK%2FRBDOSL5J7iNUWYluqQgi8WTbZDxcq44e%2BYoSCSL%2Bm6MqOsYldNMG7fPODrm4MqD6z4smtGqSkyERVrpIQzL2TIVu9j0iU0hfCAG3MMi7jr0GOqUBZzTDyj2jrowc6su72fN4fQhUE%2BS6bQyqWsduDtn%2Bgw%2BJbM6mCpCNvpVVJ4hfWgfdRVfTRjRK3H4IPorBiHdAoXpnyumdqflUkrk5DpCuPtpuURvM5FWWmtb%2FHxU2NBtdooou2%2F0GcuEJ11vOqEoeQQvYLm8sH3w15FuH8gssfb%2F149yk37pKaBkf64vHB%2FEPvC76z0ZhXsvPtLSP1Vd%2FqRXNg9Zs&X-Amz-Signature=55b0048d13bc9d1ad0c03f26455d8a30bfca05bb88a973fd4fabb5de2e6f883d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOFHMCZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCICZHeVLwauSH9keBRo2W1fpQOqcF9End%2FVPJ90Uk3Z0lAiEA0jyDhXgK8zGP2RiWUONCybCASi6CUgzOooOCl73GRkYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPy9qkd2zmqVsv%2BoXyrcA25j4C1XbNlCCJZd6n5vROhhrY6MYkRVnKYWTLNnthUlnlMEX0n%2FtQNcAgATe2S3GMgulVA1yGPlTa2LlV%2FCDg3DcLi6ZSMeyG2SIXDQOB2BaHlX63Y1iRTgy8ak6%2B95oTjV2%2FoNBsSCIRIQTrKbh1BDbngyecug%2FNgSyJ6Yirhi%2Fwh5efMjLLThaOCyvLYx2TFWRQ%2B2%2FVMnnCqvYPmHXUtLZzese05ILG%2BxS5mYwuhaJbSV0pQsH45%2Fyoc5u3rgNVLiIbptOJ9MB7Wr%2F%2BXcawVcifgXu1ze7mv5eTjeAX8Ij9CDkr99WDeB2sJiDmMBBe8NPqr%2BqO7Ea4HkJP8H5i51X2apvbNOhXfOELInOgyET2UZdcSY%2F7mADIZrzuk4hvsKnO94ilxyszWmQZVOLL4z%2BMBgv88v07TY6hR81WXNN%2BUrg2zFemKu4C3dPIDu3woWZVKRgpQegHga5KKc94XZJ3oeV6qFhbZ%2Bzf0%2FtslzmkYcv5%2FBPY5avBhtmGKwAWuHzg45OxU0lEv5CnUujjK%2FRBDOSL5J7iNUWYluqQgi8WTbZDxcq44e%2BYoSCSL%2Bm6MqOsYldNMG7fPODrm4MqD6z4smtGqSkyERVrpIQzL2TIVu9j0iU0hfCAG3MMi7jr0GOqUBZzTDyj2jrowc6su72fN4fQhUE%2BS6bQyqWsduDtn%2Bgw%2BJbM6mCpCNvpVVJ4hfWgfdRVfTRjRK3H4IPorBiHdAoXpnyumdqflUkrk5DpCuPtpuURvM5FWWmtb%2FHxU2NBtdooou2%2F0GcuEJ11vOqEoeQQvYLm8sH3w15FuH8gssfb%2F149yk37pKaBkf64vHB%2FEPvC76z0ZhXsvPtLSP1Vd%2FqRXNg9Zs&X-Amz-Signature=9ef02b850b5809fe7ae45c79308c9689b805a89ec55c1b61698a6d88266689b0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOFHMCZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCICZHeVLwauSH9keBRo2W1fpQOqcF9End%2FVPJ90Uk3Z0lAiEA0jyDhXgK8zGP2RiWUONCybCASi6CUgzOooOCl73GRkYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPy9qkd2zmqVsv%2BoXyrcA25j4C1XbNlCCJZd6n5vROhhrY6MYkRVnKYWTLNnthUlnlMEX0n%2FtQNcAgATe2S3GMgulVA1yGPlTa2LlV%2FCDg3DcLi6ZSMeyG2SIXDQOB2BaHlX63Y1iRTgy8ak6%2B95oTjV2%2FoNBsSCIRIQTrKbh1BDbngyecug%2FNgSyJ6Yirhi%2Fwh5efMjLLThaOCyvLYx2TFWRQ%2B2%2FVMnnCqvYPmHXUtLZzese05ILG%2BxS5mYwuhaJbSV0pQsH45%2Fyoc5u3rgNVLiIbptOJ9MB7Wr%2F%2BXcawVcifgXu1ze7mv5eTjeAX8Ij9CDkr99WDeB2sJiDmMBBe8NPqr%2BqO7Ea4HkJP8H5i51X2apvbNOhXfOELInOgyET2UZdcSY%2F7mADIZrzuk4hvsKnO94ilxyszWmQZVOLL4z%2BMBgv88v07TY6hR81WXNN%2BUrg2zFemKu4C3dPIDu3woWZVKRgpQegHga5KKc94XZJ3oeV6qFhbZ%2Bzf0%2FtslzmkYcv5%2FBPY5avBhtmGKwAWuHzg45OxU0lEv5CnUujjK%2FRBDOSL5J7iNUWYluqQgi8WTbZDxcq44e%2BYoSCSL%2Bm6MqOsYldNMG7fPODrm4MqD6z4smtGqSkyERVrpIQzL2TIVu9j0iU0hfCAG3MMi7jr0GOqUBZzTDyj2jrowc6su72fN4fQhUE%2BS6bQyqWsduDtn%2Bgw%2BJbM6mCpCNvpVVJ4hfWgfdRVfTRjRK3H4IPorBiHdAoXpnyumdqflUkrk5DpCuPtpuURvM5FWWmtb%2FHxU2NBtdooou2%2F0GcuEJ11vOqEoeQQvYLm8sH3w15FuH8gssfb%2F149yk37pKaBkf64vHB%2FEPvC76z0ZhXsvPtLSP1Vd%2FqRXNg9Zs&X-Amz-Signature=6c7eeadb41f4bc85e127baa301618b3d820f758f422e53518646b00ef1f22e40&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOFHMCZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCICZHeVLwauSH9keBRo2W1fpQOqcF9End%2FVPJ90Uk3Z0lAiEA0jyDhXgK8zGP2RiWUONCybCASi6CUgzOooOCl73GRkYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPy9qkd2zmqVsv%2BoXyrcA25j4C1XbNlCCJZd6n5vROhhrY6MYkRVnKYWTLNnthUlnlMEX0n%2FtQNcAgATe2S3GMgulVA1yGPlTa2LlV%2FCDg3DcLi6ZSMeyG2SIXDQOB2BaHlX63Y1iRTgy8ak6%2B95oTjV2%2FoNBsSCIRIQTrKbh1BDbngyecug%2FNgSyJ6Yirhi%2Fwh5efMjLLThaOCyvLYx2TFWRQ%2B2%2FVMnnCqvYPmHXUtLZzese05ILG%2BxS5mYwuhaJbSV0pQsH45%2Fyoc5u3rgNVLiIbptOJ9MB7Wr%2F%2BXcawVcifgXu1ze7mv5eTjeAX8Ij9CDkr99WDeB2sJiDmMBBe8NPqr%2BqO7Ea4HkJP8H5i51X2apvbNOhXfOELInOgyET2UZdcSY%2F7mADIZrzuk4hvsKnO94ilxyszWmQZVOLL4z%2BMBgv88v07TY6hR81WXNN%2BUrg2zFemKu4C3dPIDu3woWZVKRgpQegHga5KKc94XZJ3oeV6qFhbZ%2Bzf0%2FtslzmkYcv5%2FBPY5avBhtmGKwAWuHzg45OxU0lEv5CnUujjK%2FRBDOSL5J7iNUWYluqQgi8WTbZDxcq44e%2BYoSCSL%2Bm6MqOsYldNMG7fPODrm4MqD6z4smtGqSkyERVrpIQzL2TIVu9j0iU0hfCAG3MMi7jr0GOqUBZzTDyj2jrowc6su72fN4fQhUE%2BS6bQyqWsduDtn%2Bgw%2BJbM6mCpCNvpVVJ4hfWgfdRVfTRjRK3H4IPorBiHdAoXpnyumdqflUkrk5DpCuPtpuURvM5FWWmtb%2FHxU2NBtdooou2%2F0GcuEJ11vOqEoeQQvYLm8sH3w15FuH8gssfb%2F149yk37pKaBkf64vHB%2FEPvC76z0ZhXsvPtLSP1Vd%2FqRXNg9Zs&X-Amz-Signature=1430297b8b26e6354d41c8cd0684fa0b9c6a63687037f671945c99070d919247&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVGLRL3S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHxnjf3qwHmv4P5xi%2Fb9ZL86QBA1FAgsT71GVMdWyp6yAiB7cwxavqJrDbuemjLyug9iuCbyC4%2FMQANmMHWOQ7mhKyr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMJ2XuVGFHNLPndxjkKtwDIbGI5%2BPX%2F0S%2F7qGFbgK6ecU6kZsRcY2uq1fM3Ouc1CmBenL2t9tY%2BIb1MdXQOV2dW2VrKBAwNbahJofxibmAXVuQLCthZ4p7int7WxOn%2FPczISC4cTe5xH60PrUTjcVYlp7FwSZ9Od6wC%2BPBwWJXRfAfR7iSYHsY%2FhwnYH%2BNi%2F6lXOaFKNoG6FoXf3TyaHm6VnAd7sx0I%2F8IbHn3BOcuE9I%2BuJBkEF%2BGs09sWCuYHA8J6sg4u1csnOQdgMA0OlosZYcoQdebH%2FHoDk2bNCJ5ZtVswXSgL0EbugHdCausaVWM7phxjTob0Smtc935%2FnWU04WWTPbaxV29zkY3%2Fya1iTWD3Kw8c0p4D233LAqI9xxYujVmPAAB7TGXnaAy0%2B2c2YBZZD29Sa5Gj62F8bHFU7ujmzl%2FADb8v8sSgGe%2F%2F3NWZdbEukFISfkMqRvas%2BvX6sG5tVty2Iih3ChgDJVJedafSPIKaIvxAwTUPYWAv5kuAINQsg7GaZIyqFEwvgVb3TIzmqMckEQwuNoHLZXXfy33JhKKJgPtnx26B1BoIq5Z32LjRqKjcrBUwTWYoW%2B6mRKg95q6pXl01OBTn0i6y%2BL7u8jnTLqdxOsKZbVf%2F8mdNjUpKSD%2FshDZdLYwi92PvQY6pgEvQ87rDo0N9k%2BW1Mq5WK%2FnK%2BYu%2BeTYT1y9LdN3YQq5ynP5NDDM6r9pcuVcIVhw0lJzQ3lHqYx3zzx75oBKvYHmSCgUpICupo1MbFG5zNMMBmR3vYCcPsqLHr9KZEXPk05F9x2LonVzYedU1jXHmGCa4eKcRRMFSJQLxwgiHZ0jQVJiProjQ5WNqI9QZE3PNriuU9nPP4viOvW2O0rRr7m4Amq6txGQ&X-Amz-Signature=747a86b696a3b83c5003a4fecf31194c65cd7dbdca3db3ba93ee02dc045d6be7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVGLRL3S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHxnjf3qwHmv4P5xi%2Fb9ZL86QBA1FAgsT71GVMdWyp6yAiB7cwxavqJrDbuemjLyug9iuCbyC4%2FMQANmMHWOQ7mhKyr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMJ2XuVGFHNLPndxjkKtwDIbGI5%2BPX%2F0S%2F7qGFbgK6ecU6kZsRcY2uq1fM3Ouc1CmBenL2t9tY%2BIb1MdXQOV2dW2VrKBAwNbahJofxibmAXVuQLCthZ4p7int7WxOn%2FPczISC4cTe5xH60PrUTjcVYlp7FwSZ9Od6wC%2BPBwWJXRfAfR7iSYHsY%2FhwnYH%2BNi%2F6lXOaFKNoG6FoXf3TyaHm6VnAd7sx0I%2F8IbHn3BOcuE9I%2BuJBkEF%2BGs09sWCuYHA8J6sg4u1csnOQdgMA0OlosZYcoQdebH%2FHoDk2bNCJ5ZtVswXSgL0EbugHdCausaVWM7phxjTob0Smtc935%2FnWU04WWTPbaxV29zkY3%2Fya1iTWD3Kw8c0p4D233LAqI9xxYujVmPAAB7TGXnaAy0%2B2c2YBZZD29Sa5Gj62F8bHFU7ujmzl%2FADb8v8sSgGe%2F%2F3NWZdbEukFISfkMqRvas%2BvX6sG5tVty2Iih3ChgDJVJedafSPIKaIvxAwTUPYWAv5kuAINQsg7GaZIyqFEwvgVb3TIzmqMckEQwuNoHLZXXfy33JhKKJgPtnx26B1BoIq5Z32LjRqKjcrBUwTWYoW%2B6mRKg95q6pXl01OBTn0i6y%2BL7u8jnTLqdxOsKZbVf%2F8mdNjUpKSD%2FshDZdLYwi92PvQY6pgEvQ87rDo0N9k%2BW1Mq5WK%2FnK%2BYu%2BeTYT1y9LdN3YQq5ynP5NDDM6r9pcuVcIVhw0lJzQ3lHqYx3zzx75oBKvYHmSCgUpICupo1MbFG5zNMMBmR3vYCcPsqLHr9KZEXPk05F9x2LonVzYedU1jXHmGCa4eKcRRMFSJQLxwgiHZ0jQVJiProjQ5WNqI9QZE3PNriuU9nPP4viOvW2O0rRr7m4Amq6txGQ&X-Amz-Signature=a6ed2d8aa369f637c1a1bd8cdd8cf7fb34889f8019b831b2f26d6d442f972874&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVGLRL3S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHxnjf3qwHmv4P5xi%2Fb9ZL86QBA1FAgsT71GVMdWyp6yAiB7cwxavqJrDbuemjLyug9iuCbyC4%2FMQANmMHWOQ7mhKyr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMJ2XuVGFHNLPndxjkKtwDIbGI5%2BPX%2F0S%2F7qGFbgK6ecU6kZsRcY2uq1fM3Ouc1CmBenL2t9tY%2BIb1MdXQOV2dW2VrKBAwNbahJofxibmAXVuQLCthZ4p7int7WxOn%2FPczISC4cTe5xH60PrUTjcVYlp7FwSZ9Od6wC%2BPBwWJXRfAfR7iSYHsY%2FhwnYH%2BNi%2F6lXOaFKNoG6FoXf3TyaHm6VnAd7sx0I%2F8IbHn3BOcuE9I%2BuJBkEF%2BGs09sWCuYHA8J6sg4u1csnOQdgMA0OlosZYcoQdebH%2FHoDk2bNCJ5ZtVswXSgL0EbugHdCausaVWM7phxjTob0Smtc935%2FnWU04WWTPbaxV29zkY3%2Fya1iTWD3Kw8c0p4D233LAqI9xxYujVmPAAB7TGXnaAy0%2B2c2YBZZD29Sa5Gj62F8bHFU7ujmzl%2FADb8v8sSgGe%2F%2F3NWZdbEukFISfkMqRvas%2BvX6sG5tVty2Iih3ChgDJVJedafSPIKaIvxAwTUPYWAv5kuAINQsg7GaZIyqFEwvgVb3TIzmqMckEQwuNoHLZXXfy33JhKKJgPtnx26B1BoIq5Z32LjRqKjcrBUwTWYoW%2B6mRKg95q6pXl01OBTn0i6y%2BL7u8jnTLqdxOsKZbVf%2F8mdNjUpKSD%2FshDZdLYwi92PvQY6pgEvQ87rDo0N9k%2BW1Mq5WK%2FnK%2BYu%2BeTYT1y9LdN3YQq5ynP5NDDM6r9pcuVcIVhw0lJzQ3lHqYx3zzx75oBKvYHmSCgUpICupo1MbFG5zNMMBmR3vYCcPsqLHr9KZEXPk05F9x2LonVzYedU1jXHmGCa4eKcRRMFSJQLxwgiHZ0jQVJiProjQ5WNqI9QZE3PNriuU9nPP4viOvW2O0rRr7m4Amq6txGQ&X-Amz-Signature=b6f100298275431dcba2f002acc3e921224ac8c400c1531a349158f970732123&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVGLRL3S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHxnjf3qwHmv4P5xi%2Fb9ZL86QBA1FAgsT71GVMdWyp6yAiB7cwxavqJrDbuemjLyug9iuCbyC4%2FMQANmMHWOQ7mhKyr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMJ2XuVGFHNLPndxjkKtwDIbGI5%2BPX%2F0S%2F7qGFbgK6ecU6kZsRcY2uq1fM3Ouc1CmBenL2t9tY%2BIb1MdXQOV2dW2VrKBAwNbahJofxibmAXVuQLCthZ4p7int7WxOn%2FPczISC4cTe5xH60PrUTjcVYlp7FwSZ9Od6wC%2BPBwWJXRfAfR7iSYHsY%2FhwnYH%2BNi%2F6lXOaFKNoG6FoXf3TyaHm6VnAd7sx0I%2F8IbHn3BOcuE9I%2BuJBkEF%2BGs09sWCuYHA8J6sg4u1csnOQdgMA0OlosZYcoQdebH%2FHoDk2bNCJ5ZtVswXSgL0EbugHdCausaVWM7phxjTob0Smtc935%2FnWU04WWTPbaxV29zkY3%2Fya1iTWD3Kw8c0p4D233LAqI9xxYujVmPAAB7TGXnaAy0%2B2c2YBZZD29Sa5Gj62F8bHFU7ujmzl%2FADb8v8sSgGe%2F%2F3NWZdbEukFISfkMqRvas%2BvX6sG5tVty2Iih3ChgDJVJedafSPIKaIvxAwTUPYWAv5kuAINQsg7GaZIyqFEwvgVb3TIzmqMckEQwuNoHLZXXfy33JhKKJgPtnx26B1BoIq5Z32LjRqKjcrBUwTWYoW%2B6mRKg95q6pXl01OBTn0i6y%2BL7u8jnTLqdxOsKZbVf%2F8mdNjUpKSD%2FshDZdLYwi92PvQY6pgEvQ87rDo0N9k%2BW1Mq5WK%2FnK%2BYu%2BeTYT1y9LdN3YQq5ynP5NDDM6r9pcuVcIVhw0lJzQ3lHqYx3zzx75oBKvYHmSCgUpICupo1MbFG5zNMMBmR3vYCcPsqLHr9KZEXPk05F9x2LonVzYedU1jXHmGCa4eKcRRMFSJQLxwgiHZ0jQVJiProjQ5WNqI9QZE3PNriuU9nPP4viOvW2O0rRr7m4Amq6txGQ&X-Amz-Signature=e805f35b961f15cb82002b1e760070a3f3b08e94cdb287f46100759a80c2d726&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVGLRL3S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHxnjf3qwHmv4P5xi%2Fb9ZL86QBA1FAgsT71GVMdWyp6yAiB7cwxavqJrDbuemjLyug9iuCbyC4%2FMQANmMHWOQ7mhKyr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMJ2XuVGFHNLPndxjkKtwDIbGI5%2BPX%2F0S%2F7qGFbgK6ecU6kZsRcY2uq1fM3Ouc1CmBenL2t9tY%2BIb1MdXQOV2dW2VrKBAwNbahJofxibmAXVuQLCthZ4p7int7WxOn%2FPczISC4cTe5xH60PrUTjcVYlp7FwSZ9Od6wC%2BPBwWJXRfAfR7iSYHsY%2FhwnYH%2BNi%2F6lXOaFKNoG6FoXf3TyaHm6VnAd7sx0I%2F8IbHn3BOcuE9I%2BuJBkEF%2BGs09sWCuYHA8J6sg4u1csnOQdgMA0OlosZYcoQdebH%2FHoDk2bNCJ5ZtVswXSgL0EbugHdCausaVWM7phxjTob0Smtc935%2FnWU04WWTPbaxV29zkY3%2Fya1iTWD3Kw8c0p4D233LAqI9xxYujVmPAAB7TGXnaAy0%2B2c2YBZZD29Sa5Gj62F8bHFU7ujmzl%2FADb8v8sSgGe%2F%2F3NWZdbEukFISfkMqRvas%2BvX6sG5tVty2Iih3ChgDJVJedafSPIKaIvxAwTUPYWAv5kuAINQsg7GaZIyqFEwvgVb3TIzmqMckEQwuNoHLZXXfy33JhKKJgPtnx26B1BoIq5Z32LjRqKjcrBUwTWYoW%2B6mRKg95q6pXl01OBTn0i6y%2BL7u8jnTLqdxOsKZbVf%2F8mdNjUpKSD%2FshDZdLYwi92PvQY6pgEvQ87rDo0N9k%2BW1Mq5WK%2FnK%2BYu%2BeTYT1y9LdN3YQq5ynP5NDDM6r9pcuVcIVhw0lJzQ3lHqYx3zzx75oBKvYHmSCgUpICupo1MbFG5zNMMBmR3vYCcPsqLHr9KZEXPk05F9x2LonVzYedU1jXHmGCa4eKcRRMFSJQLxwgiHZ0jQVJiProjQ5WNqI9QZE3PNriuU9nPP4viOvW2O0rRr7m4Amq6txGQ&X-Amz-Signature=4ba2f6d3238249ea0e8201db6a65262645c255e2a097c2496307ef5d9e177e23&X-Amz-SignedHeaders=host&x-id=GetObject)
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


