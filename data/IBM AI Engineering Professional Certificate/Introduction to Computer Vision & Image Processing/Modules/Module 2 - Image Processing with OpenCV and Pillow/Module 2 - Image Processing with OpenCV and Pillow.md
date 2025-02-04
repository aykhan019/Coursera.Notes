

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCTX4Q2A%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDYZxLiXoI%2FQJau%2Fmqhqk4Dobq4ie%2BnVrbqIpZkRLi2YgIgL%2F5l1wWJpBY1pvu8%2B%2BBwdrZzvEPQDq%2Bp2Gb5VqwBt4Uq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDLWOnM4qfefVn3Vd%2FSrcA7lrjLnKX%2By%2BSM28JANWjp3MkRDRvSZbUiOJWvkLrKjHpr6TEFVGFpMRvvOBn9u4P59xosVHLHMhqzBKX9g89JVdIYn56f4ZAnH1cFeDZ76qf1Ny3qiQ4m4zIB%2Fk8TGL2yFslyATr9MePDi6jSUyCyEMaREDn7d1h8LsJzWBpd8eFiuVPz%2FvSMXTm2EPADfd2qLjJ%2FxfCpmo%2FwydqBfCzVMCPxCpDH%2BYVYe01KIUIbDAPQQzseNzlXa5sF33ZVjeq%2Fej2MJUUiad3%2FKjuBXh%2F6Gu5a74862YL3SU745wIcGCILVWVADnTZPGQL9L5d8G7KN04sFf6LENZiZYS7kqQR4o1EOri5aHyz7Clyn1sXovcXIvIiWAcPa6v%2BV6xatGbUhWEpLg1KLWprz0LxOy2LTpyIHCpOoMOmpLFIXmu5ZCCTUu2jV46RGvWhgD8w6v2PrjvSdzDOOC003yJHERkRYMQjgHfzSH%2F4D66s17fFIuSLq6tZZYY0g3NEgXMycomVXMfOTWf6Cy10rjSZm%2F3exE0sKpKhVxYdIlA7Lh6%2B5VhCySVY96joZaGbVpCTkPigxa9zn2ncwe34P1TcpmGztZwK5FNAZE0UVlSaxfwfKoSMMS37zaL%2FbFzKNYMK%2BCiL0GOqUBXCKRCUM68Wi6z3azNYVBBlTx7SRRsSUitw8gExTYU4tokQPTBJlZ8OpkiEftJS2g%2Bcc1PBT5FSwc0SjKqI9en%2F2URoW7CIks4kbSJj3nB6%2BC7RJhJcYDqc%2FEGgT8ohyVkSum1hYrLZCK8AOIz%2FX2V9FpjEwGbQthI5TQigGye8bRUepylvrpgiJrQlzBEAKQCfwePAmFctkX5kbmjiTXSHxS6miu&X-Amz-Signature=1c2c58534d7f0bf5823d9fa2692c538ca5b02e661348435e76c80bf2ad607259&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VUSMOF2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAHjT2PPp9mAQKOGCp2Z7neEOfUPTfR3nM0jPx%2F3DNQAAiBeQrwAlAcdC6CUdrAvlG87WXabwH4S5iQ2u0%2Fo2sDzXSr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMZrSqV3f10bfKzpUuKtwDUtEWp0ZW2spjxks5XTi8QsPpenvEaIhUTrEiv3mHbmGJL7a5FKoHVcoPeQHHXWwPloMM2kTFNgSPXnnL%2Bp2oyrbegBYJnhXvOUW2dA4qAuqqVPEO8fpe%2BB%2BFknAulMlMwB0YRQyBWoon1mDytUYVToJ35q8dvpv3x0Rl%2FG0H2H1wFLKn%2Bd0lhzW3JhhIGLGFUAg2mqLiqZme%2Be1Pq%2BhHF0Gx9%2BLLKjZFHGOWx4uyP1H2CcNv1IzlJbQYRdIJOCXsBYHVmtWF4DTAm2JwNgTLWupyrNhRm92fvZxRC6NXj0XWy4FKhWhcnWxtWNGidnK%2Fct85PbwssBVFf8FVp6JG1HrmppENJ%2BLTb8llBNXu8A9fFEMDQzq5GRJysgOyZI0EJrupmVi5NmfXf93HfO4RDbGDvCtvekFXVx3V1C8ZSMnbr3PNO8vrqggSXZPKRdZAtFgF8u66qnmsbnUSAK8yOs%2B0%2FFr0Qj0iGQrHlsQuAzdHahM2niIbB80VkZ0vL0bvMg8CYXvsE%2BLsHzHnO1LIUh5GVS2mktespq%2BuI4rHnQDV0nQBKIHLo831ek9jkwni7lpTL0xB%2Fhd51WpbHrjI6LwTCLGq%2BVd0dDODjBMFCg%2FpGfL6kG3rwlzZZUUw6YGIvQY6pgFQls28XBXaAn0Av2TyfIn0yF5hl9U%2BKJa5bnGhs2ISq5CF8ZBPqv9s4WResyXrbhXMac3KIsMAKUgaZF3ZldNE%2BwfKomIVOv%2B2eH3eznPhXQgweJifasRrk9ukAQ9o7D8rtUj6Y%2FWs3kAm0S64%2FvoFrqR0MZuwVrBI9lzzgxx6B3cLrs7BcGZIoC5QPNs2eLjD1eaj9Tj3QptZB7FTnsKG0REOB9H3&X-Amz-Signature=e7f9c920ad0d36061aba3e921df71eff11897f9a458519eef1257f1bdc8de88d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VUSMOF2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAHjT2PPp9mAQKOGCp2Z7neEOfUPTfR3nM0jPx%2F3DNQAAiBeQrwAlAcdC6CUdrAvlG87WXabwH4S5iQ2u0%2Fo2sDzXSr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMZrSqV3f10bfKzpUuKtwDUtEWp0ZW2spjxks5XTi8QsPpenvEaIhUTrEiv3mHbmGJL7a5FKoHVcoPeQHHXWwPloMM2kTFNgSPXnnL%2Bp2oyrbegBYJnhXvOUW2dA4qAuqqVPEO8fpe%2BB%2BFknAulMlMwB0YRQyBWoon1mDytUYVToJ35q8dvpv3x0Rl%2FG0H2H1wFLKn%2Bd0lhzW3JhhIGLGFUAg2mqLiqZme%2Be1Pq%2BhHF0Gx9%2BLLKjZFHGOWx4uyP1H2CcNv1IzlJbQYRdIJOCXsBYHVmtWF4DTAm2JwNgTLWupyrNhRm92fvZxRC6NXj0XWy4FKhWhcnWxtWNGidnK%2Fct85PbwssBVFf8FVp6JG1HrmppENJ%2BLTb8llBNXu8A9fFEMDQzq5GRJysgOyZI0EJrupmVi5NmfXf93HfO4RDbGDvCtvekFXVx3V1C8ZSMnbr3PNO8vrqggSXZPKRdZAtFgF8u66qnmsbnUSAK8yOs%2B0%2FFr0Qj0iGQrHlsQuAzdHahM2niIbB80VkZ0vL0bvMg8CYXvsE%2BLsHzHnO1LIUh5GVS2mktespq%2BuI4rHnQDV0nQBKIHLo831ek9jkwni7lpTL0xB%2Fhd51WpbHrjI6LwTCLGq%2BVd0dDODjBMFCg%2FpGfL6kG3rwlzZZUUw6YGIvQY6pgFQls28XBXaAn0Av2TyfIn0yF5hl9U%2BKJa5bnGhs2ISq5CF8ZBPqv9s4WResyXrbhXMac3KIsMAKUgaZF3ZldNE%2BwfKomIVOv%2B2eH3eznPhXQgweJifasRrk9ukAQ9o7D8rtUj6Y%2FWs3kAm0S64%2FvoFrqR0MZuwVrBI9lzzgxx6B3cLrs7BcGZIoC5QPNs2eLjD1eaj9Tj3QptZB7FTnsKG0REOB9H3&X-Amz-Signature=ce47713dae3a2271641810544a5ad4aad9630be55ce4c885527e49d5638790e5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VUSMOF2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAHjT2PPp9mAQKOGCp2Z7neEOfUPTfR3nM0jPx%2F3DNQAAiBeQrwAlAcdC6CUdrAvlG87WXabwH4S5iQ2u0%2Fo2sDzXSr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMZrSqV3f10bfKzpUuKtwDUtEWp0ZW2spjxks5XTi8QsPpenvEaIhUTrEiv3mHbmGJL7a5FKoHVcoPeQHHXWwPloMM2kTFNgSPXnnL%2Bp2oyrbegBYJnhXvOUW2dA4qAuqqVPEO8fpe%2BB%2BFknAulMlMwB0YRQyBWoon1mDytUYVToJ35q8dvpv3x0Rl%2FG0H2H1wFLKn%2Bd0lhzW3JhhIGLGFUAg2mqLiqZme%2Be1Pq%2BhHF0Gx9%2BLLKjZFHGOWx4uyP1H2CcNv1IzlJbQYRdIJOCXsBYHVmtWF4DTAm2JwNgTLWupyrNhRm92fvZxRC6NXj0XWy4FKhWhcnWxtWNGidnK%2Fct85PbwssBVFf8FVp6JG1HrmppENJ%2BLTb8llBNXu8A9fFEMDQzq5GRJysgOyZI0EJrupmVi5NmfXf93HfO4RDbGDvCtvekFXVx3V1C8ZSMnbr3PNO8vrqggSXZPKRdZAtFgF8u66qnmsbnUSAK8yOs%2B0%2FFr0Qj0iGQrHlsQuAzdHahM2niIbB80VkZ0vL0bvMg8CYXvsE%2BLsHzHnO1LIUh5GVS2mktespq%2BuI4rHnQDV0nQBKIHLo831ek9jkwni7lpTL0xB%2Fhd51WpbHrjI6LwTCLGq%2BVd0dDODjBMFCg%2FpGfL6kG3rwlzZZUUw6YGIvQY6pgFQls28XBXaAn0Av2TyfIn0yF5hl9U%2BKJa5bnGhs2ISq5CF8ZBPqv9s4WResyXrbhXMac3KIsMAKUgaZF3ZldNE%2BwfKomIVOv%2B2eH3eznPhXQgweJifasRrk9ukAQ9o7D8rtUj6Y%2FWs3kAm0S64%2FvoFrqR0MZuwVrBI9lzzgxx6B3cLrs7BcGZIoC5QPNs2eLjD1eaj9Tj3QptZB7FTnsKG0REOB9H3&X-Amz-Signature=0425b62e1ab8c51a9da7fb528a5c9f9aae220b9a72265402957f44b4271b60de&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VUSMOF2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAHjT2PPp9mAQKOGCp2Z7neEOfUPTfR3nM0jPx%2F3DNQAAiBeQrwAlAcdC6CUdrAvlG87WXabwH4S5iQ2u0%2Fo2sDzXSr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMZrSqV3f10bfKzpUuKtwDUtEWp0ZW2spjxks5XTi8QsPpenvEaIhUTrEiv3mHbmGJL7a5FKoHVcoPeQHHXWwPloMM2kTFNgSPXnnL%2Bp2oyrbegBYJnhXvOUW2dA4qAuqqVPEO8fpe%2BB%2BFknAulMlMwB0YRQyBWoon1mDytUYVToJ35q8dvpv3x0Rl%2FG0H2H1wFLKn%2Bd0lhzW3JhhIGLGFUAg2mqLiqZme%2Be1Pq%2BhHF0Gx9%2BLLKjZFHGOWx4uyP1H2CcNv1IzlJbQYRdIJOCXsBYHVmtWF4DTAm2JwNgTLWupyrNhRm92fvZxRC6NXj0XWy4FKhWhcnWxtWNGidnK%2Fct85PbwssBVFf8FVp6JG1HrmppENJ%2BLTb8llBNXu8A9fFEMDQzq5GRJysgOyZI0EJrupmVi5NmfXf93HfO4RDbGDvCtvekFXVx3V1C8ZSMnbr3PNO8vrqggSXZPKRdZAtFgF8u66qnmsbnUSAK8yOs%2B0%2FFr0Qj0iGQrHlsQuAzdHahM2niIbB80VkZ0vL0bvMg8CYXvsE%2BLsHzHnO1LIUh5GVS2mktespq%2BuI4rHnQDV0nQBKIHLo831ek9jkwni7lpTL0xB%2Fhd51WpbHrjI6LwTCLGq%2BVd0dDODjBMFCg%2FpGfL6kG3rwlzZZUUw6YGIvQY6pgFQls28XBXaAn0Av2TyfIn0yF5hl9U%2BKJa5bnGhs2ISq5CF8ZBPqv9s4WResyXrbhXMac3KIsMAKUgaZF3ZldNE%2BwfKomIVOv%2B2eH3eznPhXQgweJifasRrk9ukAQ9o7D8rtUj6Y%2FWs3kAm0S64%2FvoFrqR0MZuwVrBI9lzzgxx6B3cLrs7BcGZIoC5QPNs2eLjD1eaj9Tj3QptZB7FTnsKG0REOB9H3&X-Amz-Signature=5d8d47d9e1dc6107c53caebdd1310a620819d548697b7c684c3222845b59b2e1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VUSMOF2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAHjT2PPp9mAQKOGCp2Z7neEOfUPTfR3nM0jPx%2F3DNQAAiBeQrwAlAcdC6CUdrAvlG87WXabwH4S5iQ2u0%2Fo2sDzXSr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMZrSqV3f10bfKzpUuKtwDUtEWp0ZW2spjxks5XTi8QsPpenvEaIhUTrEiv3mHbmGJL7a5FKoHVcoPeQHHXWwPloMM2kTFNgSPXnnL%2Bp2oyrbegBYJnhXvOUW2dA4qAuqqVPEO8fpe%2BB%2BFknAulMlMwB0YRQyBWoon1mDytUYVToJ35q8dvpv3x0Rl%2FG0H2H1wFLKn%2Bd0lhzW3JhhIGLGFUAg2mqLiqZme%2Be1Pq%2BhHF0Gx9%2BLLKjZFHGOWx4uyP1H2CcNv1IzlJbQYRdIJOCXsBYHVmtWF4DTAm2JwNgTLWupyrNhRm92fvZxRC6NXj0XWy4FKhWhcnWxtWNGidnK%2Fct85PbwssBVFf8FVp6JG1HrmppENJ%2BLTb8llBNXu8A9fFEMDQzq5GRJysgOyZI0EJrupmVi5NmfXf93HfO4RDbGDvCtvekFXVx3V1C8ZSMnbr3PNO8vrqggSXZPKRdZAtFgF8u66qnmsbnUSAK8yOs%2B0%2FFr0Qj0iGQrHlsQuAzdHahM2niIbB80VkZ0vL0bvMg8CYXvsE%2BLsHzHnO1LIUh5GVS2mktespq%2BuI4rHnQDV0nQBKIHLo831ek9jkwni7lpTL0xB%2Fhd51WpbHrjI6LwTCLGq%2BVd0dDODjBMFCg%2FpGfL6kG3rwlzZZUUw6YGIvQY6pgFQls28XBXaAn0Av2TyfIn0yF5hl9U%2BKJa5bnGhs2ISq5CF8ZBPqv9s4WResyXrbhXMac3KIsMAKUgaZF3ZldNE%2BwfKomIVOv%2B2eH3eznPhXQgweJifasRrk9ukAQ9o7D8rtUj6Y%2FWs3kAm0S64%2FvoFrqR0MZuwVrBI9lzzgxx6B3cLrs7BcGZIoC5QPNs2eLjD1eaj9Tj3QptZB7FTnsKG0REOB9H3&X-Amz-Signature=f15fc01b06a2f33979d71fc32328129fc988a68c4e7bc0170759223f03af5a99&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCTX4Q2A%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDYZxLiXoI%2FQJau%2Fmqhqk4Dobq4ie%2BnVrbqIpZkRLi2YgIgL%2F5l1wWJpBY1pvu8%2B%2BBwdrZzvEPQDq%2Bp2Gb5VqwBt4Uq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDLWOnM4qfefVn3Vd%2FSrcA7lrjLnKX%2By%2BSM28JANWjp3MkRDRvSZbUiOJWvkLrKjHpr6TEFVGFpMRvvOBn9u4P59xosVHLHMhqzBKX9g89JVdIYn56f4ZAnH1cFeDZ76qf1Ny3qiQ4m4zIB%2Fk8TGL2yFslyATr9MePDi6jSUyCyEMaREDn7d1h8LsJzWBpd8eFiuVPz%2FvSMXTm2EPADfd2qLjJ%2FxfCpmo%2FwydqBfCzVMCPxCpDH%2BYVYe01KIUIbDAPQQzseNzlXa5sF33ZVjeq%2Fej2MJUUiad3%2FKjuBXh%2F6Gu5a74862YL3SU745wIcGCILVWVADnTZPGQL9L5d8G7KN04sFf6LENZiZYS7kqQR4o1EOri5aHyz7Clyn1sXovcXIvIiWAcPa6v%2BV6xatGbUhWEpLg1KLWprz0LxOy2LTpyIHCpOoMOmpLFIXmu5ZCCTUu2jV46RGvWhgD8w6v2PrjvSdzDOOC003yJHERkRYMQjgHfzSH%2F4D66s17fFIuSLq6tZZYY0g3NEgXMycomVXMfOTWf6Cy10rjSZm%2F3exE0sKpKhVxYdIlA7Lh6%2B5VhCySVY96joZaGbVpCTkPigxa9zn2ncwe34P1TcpmGztZwK5FNAZE0UVlSaxfwfKoSMMS37zaL%2FbFzKNYMK%2BCiL0GOqUBXCKRCUM68Wi6z3azNYVBBlTx7SRRsSUitw8gExTYU4tokQPTBJlZ8OpkiEftJS2g%2Bcc1PBT5FSwc0SjKqI9en%2F2URoW7CIks4kbSJj3nB6%2BC7RJhJcYDqc%2FEGgT8ohyVkSum1hYrLZCK8AOIz%2FX2V9FpjEwGbQthI5TQigGye8bRUepylvrpgiJrQlzBEAKQCfwePAmFctkX5kbmjiTXSHxS6miu&X-Amz-Signature=de7e713a0bcf71c2e7d0732691f941731a2d5e3c8942774aa5dfd64120bc2404&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCTX4Q2A%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDYZxLiXoI%2FQJau%2Fmqhqk4Dobq4ie%2BnVrbqIpZkRLi2YgIgL%2F5l1wWJpBY1pvu8%2B%2BBwdrZzvEPQDq%2Bp2Gb5VqwBt4Uq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDLWOnM4qfefVn3Vd%2FSrcA7lrjLnKX%2By%2BSM28JANWjp3MkRDRvSZbUiOJWvkLrKjHpr6TEFVGFpMRvvOBn9u4P59xosVHLHMhqzBKX9g89JVdIYn56f4ZAnH1cFeDZ76qf1Ny3qiQ4m4zIB%2Fk8TGL2yFslyATr9MePDi6jSUyCyEMaREDn7d1h8LsJzWBpd8eFiuVPz%2FvSMXTm2EPADfd2qLjJ%2FxfCpmo%2FwydqBfCzVMCPxCpDH%2BYVYe01KIUIbDAPQQzseNzlXa5sF33ZVjeq%2Fej2MJUUiad3%2FKjuBXh%2F6Gu5a74862YL3SU745wIcGCILVWVADnTZPGQL9L5d8G7KN04sFf6LENZiZYS7kqQR4o1EOri5aHyz7Clyn1sXovcXIvIiWAcPa6v%2BV6xatGbUhWEpLg1KLWprz0LxOy2LTpyIHCpOoMOmpLFIXmu5ZCCTUu2jV46RGvWhgD8w6v2PrjvSdzDOOC003yJHERkRYMQjgHfzSH%2F4D66s17fFIuSLq6tZZYY0g3NEgXMycomVXMfOTWf6Cy10rjSZm%2F3exE0sKpKhVxYdIlA7Lh6%2B5VhCySVY96joZaGbVpCTkPigxa9zn2ncwe34P1TcpmGztZwK5FNAZE0UVlSaxfwfKoSMMS37zaL%2FbFzKNYMK%2BCiL0GOqUBXCKRCUM68Wi6z3azNYVBBlTx7SRRsSUitw8gExTYU4tokQPTBJlZ8OpkiEftJS2g%2Bcc1PBT5FSwc0SjKqI9en%2F2URoW7CIks4kbSJj3nB6%2BC7RJhJcYDqc%2FEGgT8ohyVkSum1hYrLZCK8AOIz%2FX2V9FpjEwGbQthI5TQigGye8bRUepylvrpgiJrQlzBEAKQCfwePAmFctkX5kbmjiTXSHxS6miu&X-Amz-Signature=77a6b172ea3d7298342178b0ad46c80cf8a0c5173accc640dcfd5f887775c6a6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCTX4Q2A%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDYZxLiXoI%2FQJau%2Fmqhqk4Dobq4ie%2BnVrbqIpZkRLi2YgIgL%2F5l1wWJpBY1pvu8%2B%2BBwdrZzvEPQDq%2Bp2Gb5VqwBt4Uq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDLWOnM4qfefVn3Vd%2FSrcA7lrjLnKX%2By%2BSM28JANWjp3MkRDRvSZbUiOJWvkLrKjHpr6TEFVGFpMRvvOBn9u4P59xosVHLHMhqzBKX9g89JVdIYn56f4ZAnH1cFeDZ76qf1Ny3qiQ4m4zIB%2Fk8TGL2yFslyATr9MePDi6jSUyCyEMaREDn7d1h8LsJzWBpd8eFiuVPz%2FvSMXTm2EPADfd2qLjJ%2FxfCpmo%2FwydqBfCzVMCPxCpDH%2BYVYe01KIUIbDAPQQzseNzlXa5sF33ZVjeq%2Fej2MJUUiad3%2FKjuBXh%2F6Gu5a74862YL3SU745wIcGCILVWVADnTZPGQL9L5d8G7KN04sFf6LENZiZYS7kqQR4o1EOri5aHyz7Clyn1sXovcXIvIiWAcPa6v%2BV6xatGbUhWEpLg1KLWprz0LxOy2LTpyIHCpOoMOmpLFIXmu5ZCCTUu2jV46RGvWhgD8w6v2PrjvSdzDOOC003yJHERkRYMQjgHfzSH%2F4D66s17fFIuSLq6tZZYY0g3NEgXMycomVXMfOTWf6Cy10rjSZm%2F3exE0sKpKhVxYdIlA7Lh6%2B5VhCySVY96joZaGbVpCTkPigxa9zn2ncwe34P1TcpmGztZwK5FNAZE0UVlSaxfwfKoSMMS37zaL%2FbFzKNYMK%2BCiL0GOqUBXCKRCUM68Wi6z3azNYVBBlTx7SRRsSUitw8gExTYU4tokQPTBJlZ8OpkiEftJS2g%2Bcc1PBT5FSwc0SjKqI9en%2F2URoW7CIks4kbSJj3nB6%2BC7RJhJcYDqc%2FEGgT8ohyVkSum1hYrLZCK8AOIz%2FX2V9FpjEwGbQthI5TQigGye8bRUepylvrpgiJrQlzBEAKQCfwePAmFctkX5kbmjiTXSHxS6miu&X-Amz-Signature=777ba57a13980f6558cc8ceaeb3aac69ab5a0a9c667a2da0514a40a63793fa0e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCTX4Q2A%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDYZxLiXoI%2FQJau%2Fmqhqk4Dobq4ie%2BnVrbqIpZkRLi2YgIgL%2F5l1wWJpBY1pvu8%2B%2BBwdrZzvEPQDq%2Bp2Gb5VqwBt4Uq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDLWOnM4qfefVn3Vd%2FSrcA7lrjLnKX%2By%2BSM28JANWjp3MkRDRvSZbUiOJWvkLrKjHpr6TEFVGFpMRvvOBn9u4P59xosVHLHMhqzBKX9g89JVdIYn56f4ZAnH1cFeDZ76qf1Ny3qiQ4m4zIB%2Fk8TGL2yFslyATr9MePDi6jSUyCyEMaREDn7d1h8LsJzWBpd8eFiuVPz%2FvSMXTm2EPADfd2qLjJ%2FxfCpmo%2FwydqBfCzVMCPxCpDH%2BYVYe01KIUIbDAPQQzseNzlXa5sF33ZVjeq%2Fej2MJUUiad3%2FKjuBXh%2F6Gu5a74862YL3SU745wIcGCILVWVADnTZPGQL9L5d8G7KN04sFf6LENZiZYS7kqQR4o1EOri5aHyz7Clyn1sXovcXIvIiWAcPa6v%2BV6xatGbUhWEpLg1KLWprz0LxOy2LTpyIHCpOoMOmpLFIXmu5ZCCTUu2jV46RGvWhgD8w6v2PrjvSdzDOOC003yJHERkRYMQjgHfzSH%2F4D66s17fFIuSLq6tZZYY0g3NEgXMycomVXMfOTWf6Cy10rjSZm%2F3exE0sKpKhVxYdIlA7Lh6%2B5VhCySVY96joZaGbVpCTkPigxa9zn2ncwe34P1TcpmGztZwK5FNAZE0UVlSaxfwfKoSMMS37zaL%2FbFzKNYMK%2BCiL0GOqUBXCKRCUM68Wi6z3azNYVBBlTx7SRRsSUitw8gExTYU4tokQPTBJlZ8OpkiEftJS2g%2Bcc1PBT5FSwc0SjKqI9en%2F2URoW7CIks4kbSJj3nB6%2BC7RJhJcYDqc%2FEGgT8ohyVkSum1hYrLZCK8AOIz%2FX2V9FpjEwGbQthI5TQigGye8bRUepylvrpgiJrQlzBEAKQCfwePAmFctkX5kbmjiTXSHxS6miu&X-Amz-Signature=9e2dad3d1678a8fdbe476eab64425c72ac4a7cadfc77d1ba4f95159f20b357de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCTX4Q2A%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDYZxLiXoI%2FQJau%2Fmqhqk4Dobq4ie%2BnVrbqIpZkRLi2YgIgL%2F5l1wWJpBY1pvu8%2B%2BBwdrZzvEPQDq%2Bp2Gb5VqwBt4Uq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDLWOnM4qfefVn3Vd%2FSrcA7lrjLnKX%2By%2BSM28JANWjp3MkRDRvSZbUiOJWvkLrKjHpr6TEFVGFpMRvvOBn9u4P59xosVHLHMhqzBKX9g89JVdIYn56f4ZAnH1cFeDZ76qf1Ny3qiQ4m4zIB%2Fk8TGL2yFslyATr9MePDi6jSUyCyEMaREDn7d1h8LsJzWBpd8eFiuVPz%2FvSMXTm2EPADfd2qLjJ%2FxfCpmo%2FwydqBfCzVMCPxCpDH%2BYVYe01KIUIbDAPQQzseNzlXa5sF33ZVjeq%2Fej2MJUUiad3%2FKjuBXh%2F6Gu5a74862YL3SU745wIcGCILVWVADnTZPGQL9L5d8G7KN04sFf6LENZiZYS7kqQR4o1EOri5aHyz7Clyn1sXovcXIvIiWAcPa6v%2BV6xatGbUhWEpLg1KLWprz0LxOy2LTpyIHCpOoMOmpLFIXmu5ZCCTUu2jV46RGvWhgD8w6v2PrjvSdzDOOC003yJHERkRYMQjgHfzSH%2F4D66s17fFIuSLq6tZZYY0g3NEgXMycomVXMfOTWf6Cy10rjSZm%2F3exE0sKpKhVxYdIlA7Lh6%2B5VhCySVY96joZaGbVpCTkPigxa9zn2ncwe34P1TcpmGztZwK5FNAZE0UVlSaxfwfKoSMMS37zaL%2FbFzKNYMK%2BCiL0GOqUBXCKRCUM68Wi6z3azNYVBBlTx7SRRsSUitw8gExTYU4tokQPTBJlZ8OpkiEftJS2g%2Bcc1PBT5FSwc0SjKqI9en%2F2URoW7CIks4kbSJj3nB6%2BC7RJhJcYDqc%2FEGgT8ohyVkSum1hYrLZCK8AOIz%2FX2V9FpjEwGbQthI5TQigGye8bRUepylvrpgiJrQlzBEAKQCfwePAmFctkX5kbmjiTXSHxS6miu&X-Amz-Signature=3abca8c34d2c1141bfc3bd5afd28557ee878b9ce3f779062ff7d4a029a12c336&X-Amz-SignedHeaders=host&x-id=GetObject)
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


