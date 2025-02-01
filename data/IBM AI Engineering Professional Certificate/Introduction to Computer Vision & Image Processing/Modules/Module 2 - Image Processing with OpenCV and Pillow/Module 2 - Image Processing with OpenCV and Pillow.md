

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JRSWWRQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ6gIu7rRPWcUU5ovTJW7FD3f9r7L8%2B6pWhKm1XjfsPwIhAPlQ14P7pZ56GqlAt8s3gBwcHdOTTuClijYmFv5BRXtIKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5j%2F9BZ4RCqDJpaEEq3APVQSVWi5ooG1nSh0KR%2FMlI5I8symk54uEegw%2FrXFukjMhmJ3QDZtj%2BuzYd5CqBb7YiVQPOy1yyWGjwR5xm22zTIoiLj6ZwUAcoP1pogdA8rGiw2KEsPKldM4gYheMzwa5DjseHQzhotuPEcZVmRwb3gHPrjCjROD8A9GawMA8XV25E7yqRPTpWLcfjsK70nvH4EmqTTI9mD5mccgwljDTyv90ClkKQ4nMHzMtBFBfCKGMr1tfw67GTcnhJ4yrnlxwi07FgXPZuQtxy6uepAS0jcOHvgIfRB%2FpUo3EywDVEEmfZ%2BndNVv2VEfD8Y%2BFw8KD33ZtLPmXvdR9j7gRjaIhgUy53ge0R0WT6FUtJ6mlsP0%2FSadQ%2F%2Bte7Z3RygMYCmKTCYD6%2FjcC76mIezlf4JCxwsCp8eNOR%2B5l1uBVg5Uj5r74j%2FFgvm8AZ8EbR518YTOKI3OHYTaA2QFzmXqGrzAtbuBtWQfJ6%2FN1Fwd4WrbngdTardUbhW0cN0QTqHPYghsMrwZNiYHIPzWmMLPL5WLIkdtumdnwDUiteUacUNmaVbh8kRYsP8lmgXl28S%2BOwGlS%2BT%2FTNk9dTvtcGbwoajg96JSguQCB1oBC9f7zIB%2FO75E8Z3UxpnOUkObtrtjDuvfi8BjqkASFDp2%2BJIa0WSspDdPwNj1RgrMegU4tLi46k5xtZGN6AD85wvRzBL8NYIA9EMMiEiCCGkBGs2qRTC%2FLVp8iFHfgf%2Bcvk17TzPhMiFjKRoz0SXQIqrlisLdaIdK7Z44BEXlUvyRSVPjdMVIsPT9HonJZJrLEil%2FKNNLg%2FAuicl40oohMee%2BWqGm0DHMcWj0m6ZTM7QSTDawLngPQs482bJ6PPkoCa&X-Amz-Signature=852de7a8423b2d33900849b310043d776b9045723fedb1c71b43095880dfb0fd&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFTJPOVI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmtAUTv%2Ff8NOuyU48rTIHx7brd%2BQwQeDjjtcJ0RVKDywIhAN7LdFqyjEsOxVhcVBZko44FvvbUJ3q3L6UFLy1dKFOoKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzosldfjfP0PYOO1Uwq3APdnwUxx3tph1geQRuOdcKlxqhCDEuB5nCuxtKY8ydk92fGGTa%2FVudi2CgR8%2BmogmilpIZUeFZE9qXSSXLKY2lSDf7Vn1oqaKOu8RaehhMZJHJnqeeX%2BD7ltse6n4VqRbjcuWMQh6IUDc5YaF0p%2BnDkfzcfOfMNWi2a4L1VDMR4uZZgKKgI31AKNFbK4ej7iGkM4Q89sI7RX0c%2FKACt5COEFAbOfqI5av2BPLKrwTzRrOTPBT1iDQ%2BXN%2FN9tNA%2F04iqIYN%2FUyMmKhWqeAz8f9z3lL3RZpTFCtcY%2BN%2BULixmIOsIPfZAR%2BR5%2BOUjlMD7JotB%2BInr%2BY%2BGLQa0kGD9wYKQuXtdJpECivyYc%2BYtp8WEGmzVaAf%2FDKX1j6FW1UDCtUSgUZXEdWiegvylfWtJ%2FRuWBdiYqn6Yn5%2B3DfMMtI9XuqFvf%2FsEeFTV0UiE6IHgYJIPV30oFoqOpuYEuXHwRP2Zn7D%2FVLtEJep%2BMKYrl9D5rzsYfLIeLYq754wqw6TVBzWaTCTz2DEmaL6Wc8dgW2rVKCGBbttPSptALlpPUXFRnGTRgqN%2B4P30TO90d1uoTxKZ1WW%2FEbFKjCt1N4UxryHairgo2uHA4zzpxLrvgQMOku9IJDjKg3vWJlcnOjCvyPi8BjqkAV3qZXnQE20Tk54UpZdJPtirXAxlqVQxZ1w4DtN5smecthhXYIJptC9MmZb0jb4wAJts2DXeuW8PtLzlSvU0Ki4ja%2FRfMPdexH1I3SlBDuJ1RTCvC%2Bvx4GpXl0XPgLxXporvuw3SXjFIX1TWL0lWuANK17TYIzGelCN6xwFhP%2FX6p%2FFNt4d742F1%2B5yh0LALnzM4B2nyz6S0c5rV1nhE0JhXnS9e&X-Amz-Signature=a37b35aa264bd1655119fd1a043357ec2aa4a919c288852a46be8a1cc089edf0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFTJPOVI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmtAUTv%2Ff8NOuyU48rTIHx7brd%2BQwQeDjjtcJ0RVKDywIhAN7LdFqyjEsOxVhcVBZko44FvvbUJ3q3L6UFLy1dKFOoKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzosldfjfP0PYOO1Uwq3APdnwUxx3tph1geQRuOdcKlxqhCDEuB5nCuxtKY8ydk92fGGTa%2FVudi2CgR8%2BmogmilpIZUeFZE9qXSSXLKY2lSDf7Vn1oqaKOu8RaehhMZJHJnqeeX%2BD7ltse6n4VqRbjcuWMQh6IUDc5YaF0p%2BnDkfzcfOfMNWi2a4L1VDMR4uZZgKKgI31AKNFbK4ej7iGkM4Q89sI7RX0c%2FKACt5COEFAbOfqI5av2BPLKrwTzRrOTPBT1iDQ%2BXN%2FN9tNA%2F04iqIYN%2FUyMmKhWqeAz8f9z3lL3RZpTFCtcY%2BN%2BULixmIOsIPfZAR%2BR5%2BOUjlMD7JotB%2BInr%2BY%2BGLQa0kGD9wYKQuXtdJpECivyYc%2BYtp8WEGmzVaAf%2FDKX1j6FW1UDCtUSgUZXEdWiegvylfWtJ%2FRuWBdiYqn6Yn5%2B3DfMMtI9XuqFvf%2FsEeFTV0UiE6IHgYJIPV30oFoqOpuYEuXHwRP2Zn7D%2FVLtEJep%2BMKYrl9D5rzsYfLIeLYq754wqw6TVBzWaTCTz2DEmaL6Wc8dgW2rVKCGBbttPSptALlpPUXFRnGTRgqN%2B4P30TO90d1uoTxKZ1WW%2FEbFKjCt1N4UxryHairgo2uHA4zzpxLrvgQMOku9IJDjKg3vWJlcnOjCvyPi8BjqkAV3qZXnQE20Tk54UpZdJPtirXAxlqVQxZ1w4DtN5smecthhXYIJptC9MmZb0jb4wAJts2DXeuW8PtLzlSvU0Ki4ja%2FRfMPdexH1I3SlBDuJ1RTCvC%2Bvx4GpXl0XPgLxXporvuw3SXjFIX1TWL0lWuANK17TYIzGelCN6xwFhP%2FX6p%2FFNt4d742F1%2B5yh0LALnzM4B2nyz6S0c5rV1nhE0JhXnS9e&X-Amz-Signature=51710ab1689194737786142581e29760c9b4143af0d6427c48691e09b0fb5859&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFTJPOVI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmtAUTv%2Ff8NOuyU48rTIHx7brd%2BQwQeDjjtcJ0RVKDywIhAN7LdFqyjEsOxVhcVBZko44FvvbUJ3q3L6UFLy1dKFOoKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzosldfjfP0PYOO1Uwq3APdnwUxx3tph1geQRuOdcKlxqhCDEuB5nCuxtKY8ydk92fGGTa%2FVudi2CgR8%2BmogmilpIZUeFZE9qXSSXLKY2lSDf7Vn1oqaKOu8RaehhMZJHJnqeeX%2BD7ltse6n4VqRbjcuWMQh6IUDc5YaF0p%2BnDkfzcfOfMNWi2a4L1VDMR4uZZgKKgI31AKNFbK4ej7iGkM4Q89sI7RX0c%2FKACt5COEFAbOfqI5av2BPLKrwTzRrOTPBT1iDQ%2BXN%2FN9tNA%2F04iqIYN%2FUyMmKhWqeAz8f9z3lL3RZpTFCtcY%2BN%2BULixmIOsIPfZAR%2BR5%2BOUjlMD7JotB%2BInr%2BY%2BGLQa0kGD9wYKQuXtdJpECivyYc%2BYtp8WEGmzVaAf%2FDKX1j6FW1UDCtUSgUZXEdWiegvylfWtJ%2FRuWBdiYqn6Yn5%2B3DfMMtI9XuqFvf%2FsEeFTV0UiE6IHgYJIPV30oFoqOpuYEuXHwRP2Zn7D%2FVLtEJep%2BMKYrl9D5rzsYfLIeLYq754wqw6TVBzWaTCTz2DEmaL6Wc8dgW2rVKCGBbttPSptALlpPUXFRnGTRgqN%2B4P30TO90d1uoTxKZ1WW%2FEbFKjCt1N4UxryHairgo2uHA4zzpxLrvgQMOku9IJDjKg3vWJlcnOjCvyPi8BjqkAV3qZXnQE20Tk54UpZdJPtirXAxlqVQxZ1w4DtN5smecthhXYIJptC9MmZb0jb4wAJts2DXeuW8PtLzlSvU0Ki4ja%2FRfMPdexH1I3SlBDuJ1RTCvC%2Bvx4GpXl0XPgLxXporvuw3SXjFIX1TWL0lWuANK17TYIzGelCN6xwFhP%2FX6p%2FFNt4d742F1%2B5yh0LALnzM4B2nyz6S0c5rV1nhE0JhXnS9e&X-Amz-Signature=dce661cbf896ed6f4bcc3365f12d8e23e4c693918fa17371186d8a10fa2b90dd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFTJPOVI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmtAUTv%2Ff8NOuyU48rTIHx7brd%2BQwQeDjjtcJ0RVKDywIhAN7LdFqyjEsOxVhcVBZko44FvvbUJ3q3L6UFLy1dKFOoKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzosldfjfP0PYOO1Uwq3APdnwUxx3tph1geQRuOdcKlxqhCDEuB5nCuxtKY8ydk92fGGTa%2FVudi2CgR8%2BmogmilpIZUeFZE9qXSSXLKY2lSDf7Vn1oqaKOu8RaehhMZJHJnqeeX%2BD7ltse6n4VqRbjcuWMQh6IUDc5YaF0p%2BnDkfzcfOfMNWi2a4L1VDMR4uZZgKKgI31AKNFbK4ej7iGkM4Q89sI7RX0c%2FKACt5COEFAbOfqI5av2BPLKrwTzRrOTPBT1iDQ%2BXN%2FN9tNA%2F04iqIYN%2FUyMmKhWqeAz8f9z3lL3RZpTFCtcY%2BN%2BULixmIOsIPfZAR%2BR5%2BOUjlMD7JotB%2BInr%2BY%2BGLQa0kGD9wYKQuXtdJpECivyYc%2BYtp8WEGmzVaAf%2FDKX1j6FW1UDCtUSgUZXEdWiegvylfWtJ%2FRuWBdiYqn6Yn5%2B3DfMMtI9XuqFvf%2FsEeFTV0UiE6IHgYJIPV30oFoqOpuYEuXHwRP2Zn7D%2FVLtEJep%2BMKYrl9D5rzsYfLIeLYq754wqw6TVBzWaTCTz2DEmaL6Wc8dgW2rVKCGBbttPSptALlpPUXFRnGTRgqN%2B4P30TO90d1uoTxKZ1WW%2FEbFKjCt1N4UxryHairgo2uHA4zzpxLrvgQMOku9IJDjKg3vWJlcnOjCvyPi8BjqkAV3qZXnQE20Tk54UpZdJPtirXAxlqVQxZ1w4DtN5smecthhXYIJptC9MmZb0jb4wAJts2DXeuW8PtLzlSvU0Ki4ja%2FRfMPdexH1I3SlBDuJ1RTCvC%2Bvx4GpXl0XPgLxXporvuw3SXjFIX1TWL0lWuANK17TYIzGelCN6xwFhP%2FX6p%2FFNt4d742F1%2B5yh0LALnzM4B2nyz6S0c5rV1nhE0JhXnS9e&X-Amz-Signature=f607220912a69cd2b1865e89294aa0415c7fd94b655a7d68b49ea0ea5d16c04c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFTJPOVI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmtAUTv%2Ff8NOuyU48rTIHx7brd%2BQwQeDjjtcJ0RVKDywIhAN7LdFqyjEsOxVhcVBZko44FvvbUJ3q3L6UFLy1dKFOoKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzosldfjfP0PYOO1Uwq3APdnwUxx3tph1geQRuOdcKlxqhCDEuB5nCuxtKY8ydk92fGGTa%2FVudi2CgR8%2BmogmilpIZUeFZE9qXSSXLKY2lSDf7Vn1oqaKOu8RaehhMZJHJnqeeX%2BD7ltse6n4VqRbjcuWMQh6IUDc5YaF0p%2BnDkfzcfOfMNWi2a4L1VDMR4uZZgKKgI31AKNFbK4ej7iGkM4Q89sI7RX0c%2FKACt5COEFAbOfqI5av2BPLKrwTzRrOTPBT1iDQ%2BXN%2FN9tNA%2F04iqIYN%2FUyMmKhWqeAz8f9z3lL3RZpTFCtcY%2BN%2BULixmIOsIPfZAR%2BR5%2BOUjlMD7JotB%2BInr%2BY%2BGLQa0kGD9wYKQuXtdJpECivyYc%2BYtp8WEGmzVaAf%2FDKX1j6FW1UDCtUSgUZXEdWiegvylfWtJ%2FRuWBdiYqn6Yn5%2B3DfMMtI9XuqFvf%2FsEeFTV0UiE6IHgYJIPV30oFoqOpuYEuXHwRP2Zn7D%2FVLtEJep%2BMKYrl9D5rzsYfLIeLYq754wqw6TVBzWaTCTz2DEmaL6Wc8dgW2rVKCGBbttPSptALlpPUXFRnGTRgqN%2B4P30TO90d1uoTxKZ1WW%2FEbFKjCt1N4UxryHairgo2uHA4zzpxLrvgQMOku9IJDjKg3vWJlcnOjCvyPi8BjqkAV3qZXnQE20Tk54UpZdJPtirXAxlqVQxZ1w4DtN5smecthhXYIJptC9MmZb0jb4wAJts2DXeuW8PtLzlSvU0Ki4ja%2FRfMPdexH1I3SlBDuJ1RTCvC%2Bvx4GpXl0XPgLxXporvuw3SXjFIX1TWL0lWuANK17TYIzGelCN6xwFhP%2FX6p%2FFNt4d742F1%2B5yh0LALnzM4B2nyz6S0c5rV1nhE0JhXnS9e&X-Amz-Signature=0461c5c2cccf11398c4353005a7f13811376e23b0b9aba7260cf9b9a204cf261&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JRSWWRQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ6gIu7rRPWcUU5ovTJW7FD3f9r7L8%2B6pWhKm1XjfsPwIhAPlQ14P7pZ56GqlAt8s3gBwcHdOTTuClijYmFv5BRXtIKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5j%2F9BZ4RCqDJpaEEq3APVQSVWi5ooG1nSh0KR%2FMlI5I8symk54uEegw%2FrXFukjMhmJ3QDZtj%2BuzYd5CqBb7YiVQPOy1yyWGjwR5xm22zTIoiLj6ZwUAcoP1pogdA8rGiw2KEsPKldM4gYheMzwa5DjseHQzhotuPEcZVmRwb3gHPrjCjROD8A9GawMA8XV25E7yqRPTpWLcfjsK70nvH4EmqTTI9mD5mccgwljDTyv90ClkKQ4nMHzMtBFBfCKGMr1tfw67GTcnhJ4yrnlxwi07FgXPZuQtxy6uepAS0jcOHvgIfRB%2FpUo3EywDVEEmfZ%2BndNVv2VEfD8Y%2BFw8KD33ZtLPmXvdR9j7gRjaIhgUy53ge0R0WT6FUtJ6mlsP0%2FSadQ%2F%2Bte7Z3RygMYCmKTCYD6%2FjcC76mIezlf4JCxwsCp8eNOR%2B5l1uBVg5Uj5r74j%2FFgvm8AZ8EbR518YTOKI3OHYTaA2QFzmXqGrzAtbuBtWQfJ6%2FN1Fwd4WrbngdTardUbhW0cN0QTqHPYghsMrwZNiYHIPzWmMLPL5WLIkdtumdnwDUiteUacUNmaVbh8kRYsP8lmgXl28S%2BOwGlS%2BT%2FTNk9dTvtcGbwoajg96JSguQCB1oBC9f7zIB%2FO75E8Z3UxpnOUkObtrtjDuvfi8BjqkASFDp2%2BJIa0WSspDdPwNj1RgrMegU4tLi46k5xtZGN6AD85wvRzBL8NYIA9EMMiEiCCGkBGs2qRTC%2FLVp8iFHfgf%2Bcvk17TzPhMiFjKRoz0SXQIqrlisLdaIdK7Z44BEXlUvyRSVPjdMVIsPT9HonJZJrLEil%2FKNNLg%2FAuicl40oohMee%2BWqGm0DHMcWj0m6ZTM7QSTDawLngPQs482bJ6PPkoCa&X-Amz-Signature=44c521ccc7786dd9b4408b04b9ba853f2d9d468d35b62acf4c0b2079a109f98b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JRSWWRQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ6gIu7rRPWcUU5ovTJW7FD3f9r7L8%2B6pWhKm1XjfsPwIhAPlQ14P7pZ56GqlAt8s3gBwcHdOTTuClijYmFv5BRXtIKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5j%2F9BZ4RCqDJpaEEq3APVQSVWi5ooG1nSh0KR%2FMlI5I8symk54uEegw%2FrXFukjMhmJ3QDZtj%2BuzYd5CqBb7YiVQPOy1yyWGjwR5xm22zTIoiLj6ZwUAcoP1pogdA8rGiw2KEsPKldM4gYheMzwa5DjseHQzhotuPEcZVmRwb3gHPrjCjROD8A9GawMA8XV25E7yqRPTpWLcfjsK70nvH4EmqTTI9mD5mccgwljDTyv90ClkKQ4nMHzMtBFBfCKGMr1tfw67GTcnhJ4yrnlxwi07FgXPZuQtxy6uepAS0jcOHvgIfRB%2FpUo3EywDVEEmfZ%2BndNVv2VEfD8Y%2BFw8KD33ZtLPmXvdR9j7gRjaIhgUy53ge0R0WT6FUtJ6mlsP0%2FSadQ%2F%2Bte7Z3RygMYCmKTCYD6%2FjcC76mIezlf4JCxwsCp8eNOR%2B5l1uBVg5Uj5r74j%2FFgvm8AZ8EbR518YTOKI3OHYTaA2QFzmXqGrzAtbuBtWQfJ6%2FN1Fwd4WrbngdTardUbhW0cN0QTqHPYghsMrwZNiYHIPzWmMLPL5WLIkdtumdnwDUiteUacUNmaVbh8kRYsP8lmgXl28S%2BOwGlS%2BT%2FTNk9dTvtcGbwoajg96JSguQCB1oBC9f7zIB%2FO75E8Z3UxpnOUkObtrtjDuvfi8BjqkASFDp2%2BJIa0WSspDdPwNj1RgrMegU4tLi46k5xtZGN6AD85wvRzBL8NYIA9EMMiEiCCGkBGs2qRTC%2FLVp8iFHfgf%2Bcvk17TzPhMiFjKRoz0SXQIqrlisLdaIdK7Z44BEXlUvyRSVPjdMVIsPT9HonJZJrLEil%2FKNNLg%2FAuicl40oohMee%2BWqGm0DHMcWj0m6ZTM7QSTDawLngPQs482bJ6PPkoCa&X-Amz-Signature=622c5c35a03f530bc8a9ecb1c59bc056de21818c27e11ae4ea5e58e14c0dac47&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JRSWWRQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ6gIu7rRPWcUU5ovTJW7FD3f9r7L8%2B6pWhKm1XjfsPwIhAPlQ14P7pZ56GqlAt8s3gBwcHdOTTuClijYmFv5BRXtIKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5j%2F9BZ4RCqDJpaEEq3APVQSVWi5ooG1nSh0KR%2FMlI5I8symk54uEegw%2FrXFukjMhmJ3QDZtj%2BuzYd5CqBb7YiVQPOy1yyWGjwR5xm22zTIoiLj6ZwUAcoP1pogdA8rGiw2KEsPKldM4gYheMzwa5DjseHQzhotuPEcZVmRwb3gHPrjCjROD8A9GawMA8XV25E7yqRPTpWLcfjsK70nvH4EmqTTI9mD5mccgwljDTyv90ClkKQ4nMHzMtBFBfCKGMr1tfw67GTcnhJ4yrnlxwi07FgXPZuQtxy6uepAS0jcOHvgIfRB%2FpUo3EywDVEEmfZ%2BndNVv2VEfD8Y%2BFw8KD33ZtLPmXvdR9j7gRjaIhgUy53ge0R0WT6FUtJ6mlsP0%2FSadQ%2F%2Bte7Z3RygMYCmKTCYD6%2FjcC76mIezlf4JCxwsCp8eNOR%2B5l1uBVg5Uj5r74j%2FFgvm8AZ8EbR518YTOKI3OHYTaA2QFzmXqGrzAtbuBtWQfJ6%2FN1Fwd4WrbngdTardUbhW0cN0QTqHPYghsMrwZNiYHIPzWmMLPL5WLIkdtumdnwDUiteUacUNmaVbh8kRYsP8lmgXl28S%2BOwGlS%2BT%2FTNk9dTvtcGbwoajg96JSguQCB1oBC9f7zIB%2FO75E8Z3UxpnOUkObtrtjDuvfi8BjqkASFDp2%2BJIa0WSspDdPwNj1RgrMegU4tLi46k5xtZGN6AD85wvRzBL8NYIA9EMMiEiCCGkBGs2qRTC%2FLVp8iFHfgf%2Bcvk17TzPhMiFjKRoz0SXQIqrlisLdaIdK7Z44BEXlUvyRSVPjdMVIsPT9HonJZJrLEil%2FKNNLg%2FAuicl40oohMee%2BWqGm0DHMcWj0m6ZTM7QSTDawLngPQs482bJ6PPkoCa&X-Amz-Signature=797cfab32d9b0b28ea72e252fc4857c09a98c7d9b8ee31470c1c236bd2be0864&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JRSWWRQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ6gIu7rRPWcUU5ovTJW7FD3f9r7L8%2B6pWhKm1XjfsPwIhAPlQ14P7pZ56GqlAt8s3gBwcHdOTTuClijYmFv5BRXtIKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5j%2F9BZ4RCqDJpaEEq3APVQSVWi5ooG1nSh0KR%2FMlI5I8symk54uEegw%2FrXFukjMhmJ3QDZtj%2BuzYd5CqBb7YiVQPOy1yyWGjwR5xm22zTIoiLj6ZwUAcoP1pogdA8rGiw2KEsPKldM4gYheMzwa5DjseHQzhotuPEcZVmRwb3gHPrjCjROD8A9GawMA8XV25E7yqRPTpWLcfjsK70nvH4EmqTTI9mD5mccgwljDTyv90ClkKQ4nMHzMtBFBfCKGMr1tfw67GTcnhJ4yrnlxwi07FgXPZuQtxy6uepAS0jcOHvgIfRB%2FpUo3EywDVEEmfZ%2BndNVv2VEfD8Y%2BFw8KD33ZtLPmXvdR9j7gRjaIhgUy53ge0R0WT6FUtJ6mlsP0%2FSadQ%2F%2Bte7Z3RygMYCmKTCYD6%2FjcC76mIezlf4JCxwsCp8eNOR%2B5l1uBVg5Uj5r74j%2FFgvm8AZ8EbR518YTOKI3OHYTaA2QFzmXqGrzAtbuBtWQfJ6%2FN1Fwd4WrbngdTardUbhW0cN0QTqHPYghsMrwZNiYHIPzWmMLPL5WLIkdtumdnwDUiteUacUNmaVbh8kRYsP8lmgXl28S%2BOwGlS%2BT%2FTNk9dTvtcGbwoajg96JSguQCB1oBC9f7zIB%2FO75E8Z3UxpnOUkObtrtjDuvfi8BjqkASFDp2%2BJIa0WSspDdPwNj1RgrMegU4tLi46k5xtZGN6AD85wvRzBL8NYIA9EMMiEiCCGkBGs2qRTC%2FLVp8iFHfgf%2Bcvk17TzPhMiFjKRoz0SXQIqrlisLdaIdK7Z44BEXlUvyRSVPjdMVIsPT9HonJZJrLEil%2FKNNLg%2FAuicl40oohMee%2BWqGm0DHMcWj0m6ZTM7QSTDawLngPQs482bJ6PPkoCa&X-Amz-Signature=be9bf52a1f7b9082950711ac4100130850687813fc9c291aa11f28c2a9236cc8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JRSWWRQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ6gIu7rRPWcUU5ovTJW7FD3f9r7L8%2B6pWhKm1XjfsPwIhAPlQ14P7pZ56GqlAt8s3gBwcHdOTTuClijYmFv5BRXtIKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5j%2F9BZ4RCqDJpaEEq3APVQSVWi5ooG1nSh0KR%2FMlI5I8symk54uEegw%2FrXFukjMhmJ3QDZtj%2BuzYd5CqBb7YiVQPOy1yyWGjwR5xm22zTIoiLj6ZwUAcoP1pogdA8rGiw2KEsPKldM4gYheMzwa5DjseHQzhotuPEcZVmRwb3gHPrjCjROD8A9GawMA8XV25E7yqRPTpWLcfjsK70nvH4EmqTTI9mD5mccgwljDTyv90ClkKQ4nMHzMtBFBfCKGMr1tfw67GTcnhJ4yrnlxwi07FgXPZuQtxy6uepAS0jcOHvgIfRB%2FpUo3EywDVEEmfZ%2BndNVv2VEfD8Y%2BFw8KD33ZtLPmXvdR9j7gRjaIhgUy53ge0R0WT6FUtJ6mlsP0%2FSadQ%2F%2Bte7Z3RygMYCmKTCYD6%2FjcC76mIezlf4JCxwsCp8eNOR%2B5l1uBVg5Uj5r74j%2FFgvm8AZ8EbR518YTOKI3OHYTaA2QFzmXqGrzAtbuBtWQfJ6%2FN1Fwd4WrbngdTardUbhW0cN0QTqHPYghsMrwZNiYHIPzWmMLPL5WLIkdtumdnwDUiteUacUNmaVbh8kRYsP8lmgXl28S%2BOwGlS%2BT%2FTNk9dTvtcGbwoajg96JSguQCB1oBC9f7zIB%2FO75E8Z3UxpnOUkObtrtjDuvfi8BjqkASFDp2%2BJIa0WSspDdPwNj1RgrMegU4tLi46k5xtZGN6AD85wvRzBL8NYIA9EMMiEiCCGkBGs2qRTC%2FLVp8iFHfgf%2Bcvk17TzPhMiFjKRoz0SXQIqrlisLdaIdK7Z44BEXlUvyRSVPjdMVIsPT9HonJZJrLEil%2FKNNLg%2FAuicl40oohMee%2BWqGm0DHMcWj0m6ZTM7QSTDawLngPQs482bJ6PPkoCa&X-Amz-Signature=e5d21ef25274d9c971406957c0e06914dc566e73863044103b174bdb51866ff0&X-Amz-SignedHeaders=host&x-id=GetObject)
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


