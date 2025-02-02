

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GSZRV6J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3U59TNy1APB8y1stLgiSUM50coTnMjOgInXSZpryfVAIhANUQBlxMPVA0X5AFrbJXH1U%2FAA3nP7vCDaumYLlrBNusKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymcO4iIFE94y6yoWYq3AMdtg61%2BDWYvP%2BFa9srtrzXu%2BY%2Fi64eF%2FoPG6u8urb%2B4Q95A5LgD1l8yb%2FBp4bsQT5x5mTw0NDT8QpUv1w9IhDOwTS5tkNylC6KVVWC619zBMSUbiRM7K9%2FTW77O9wIkwSvZK%2BoUP05QTLFjBxQEsvpeQQ%2B0JQv6q1qO4%2FNg6diogPNTxgmgGCIGZmxulIxVk491JeS8FqCZjFEpfo5nKsq8F7O%2FZ54RA9RmB%2FuC9DpQD2xo4gJDVnqC1Hdee86vgNoj8BlsHfazQIo97TiRmk7Wng7EhEIhz5sxjbctXazeu5Tt%2BmM9OggEN8NEbQvWQF0mLFAsnT2%2Bxza%2BoE69qyehS7xAwgdXm2qtwavClD6SUznAuUQAv447W%2BreZzeZJH4kf2ZnIWh0DbxrgMFAqBU%2BO6uJH2FV8dmSbmbqU0ctxICiUR6mTGDaE%2BnGCcpZXPEWUCGwVVHNLKpkodTdzFkqk4MIZ5JZww7zLzUhpRWFlso0bAmvbBOrrUy8UdvYzXnM0iL8%2Fxaqn%2FxBDpyZIlOkQF%2BN4lYki7LSe569QnvR8A5JUlB1OM8m8iaMbnn%2F%2BjKR47hL3jGUut3jqKpdKMd45SKrtGs%2FbjkbG1sBlNEkgrdMoWD4wWFF92K8zC85P68BjqkAW%2ByBu%2FB4a6tGTRPVjM3dpSz1JolmTgqrOEVKwX7wTLI8MRkMwRIO%2Fg%2F5JNuDCAp8i1S%2B7JUZ0Qm59EjxHTiIG%2BpdJZYm5XXN%2BW7ZzmjY%2FNy6iq%2FaxIFes%2FzJG2VdfLqfONTckPRk%2BKQlgrSQGZ0PvJKpUStPxV%2BgK7F0FITazrg%2BCj6VFLlI3CjJvUAkb%2BxJtkMrXOOknbsP5oL6Ur%2FPYL760A0&X-Amz-Signature=8dfd4ed68b59b7aed8c5263cd2eaa333f41247badaa7d2e75d51f81202429715&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UB32I4J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAyCA2QXkCvLOaNt%2B9q24MALJ2lCceAIUB1Z5BRJZwYjAiEA2iIrGHKLzmX6jDUSCHK1pRUyaOjJCWy0qAkjObOHvRkqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLy0brdbGVjrHN3mSrcA9J8297yyJ0Jbyikun2bQ4BjEnq970A7Nu6dpdXLUHqVgZsN%2BdHE9EDJvr5ECRW%2Bch1gZe5vtOBZzaikc6JEIJoLatmUEOl7TD1IYZhMD0x9Nh1HppJNcUNpHeuVoBDFaUwxD%2BM3PzlLNxUrqypn4MHZzKgm4kpUU8TuxWNSY%2BMzHVxBtcGiiMF5kWWItFBE83CIYk36lYQ%2FJS5aeH3WvJsREBnZemq3%2Fp1BZ71eZNe%2FXZx0%2F2s9Zympi7BvHsaFneJ1FWJI1f6LtbgLyb%2BEgP1H6kGMEBQNafw%2BvDAKSAbnl%2FicfV8tHorJF03JAu9Wp2kPiBEUpGwzy8uMmwvWcuYhgWw681ZEtiCYSiKy5ks6yU7cnZp%2Fh5AKGQ28RXk8wJl6GmVpCyeibbfrDUDcFwaNdufujjnKrMgks5BaCv%2B4gyVB9VRb2r%2B5H8wFbQwt34oaOCjdTQUu47KnL2L1drW7EJMU4b%2F%2FeDuO6P%2FtIgEH7EGQSu7DTVtrVB93TXKEJKNud4c3jOSDayk3ZqAAEXO9qbmeQfJlCUBlxiCddz3ZHrRso80OOpGHufNTmfhdg3KEBWw2Q7x7ImJZdOb%2ByByBHnqhg5iIm6myZ%2Fr2ZVUJr1xDzhrvyzHorOeUMOzX%2FrwGOqUBFdoBgkoErD2a8Vqnr5rLLrAT7CXaj8W1XPsnNS7fXVjLrrRizXepHKhUK17hRmAPMwwQb0lurySulToMl6KCTTIDOACVmVAyAoSL%2FHnvG8m1HXfp1Y%2BVIKPfmTLLiaMxUal2lxhfOiqKV27sZdtWQy6t8inbX16RJn6z3I0t6f713pOPwhss8peLDPxzHbo6S0UY5%2BUkqjrbBnSc4cvS5%2B4GDLiP&X-Amz-Signature=cbe08b3bcf27405ab29667739368dc27c5d43d8c065e34afc8fdc52a3be3f552&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UB32I4J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAyCA2QXkCvLOaNt%2B9q24MALJ2lCceAIUB1Z5BRJZwYjAiEA2iIrGHKLzmX6jDUSCHK1pRUyaOjJCWy0qAkjObOHvRkqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLy0brdbGVjrHN3mSrcA9J8297yyJ0Jbyikun2bQ4BjEnq970A7Nu6dpdXLUHqVgZsN%2BdHE9EDJvr5ECRW%2Bch1gZe5vtOBZzaikc6JEIJoLatmUEOl7TD1IYZhMD0x9Nh1HppJNcUNpHeuVoBDFaUwxD%2BM3PzlLNxUrqypn4MHZzKgm4kpUU8TuxWNSY%2BMzHVxBtcGiiMF5kWWItFBE83CIYk36lYQ%2FJS5aeH3WvJsREBnZemq3%2Fp1BZ71eZNe%2FXZx0%2F2s9Zympi7BvHsaFneJ1FWJI1f6LtbgLyb%2BEgP1H6kGMEBQNafw%2BvDAKSAbnl%2FicfV8tHorJF03JAu9Wp2kPiBEUpGwzy8uMmwvWcuYhgWw681ZEtiCYSiKy5ks6yU7cnZp%2Fh5AKGQ28RXk8wJl6GmVpCyeibbfrDUDcFwaNdufujjnKrMgks5BaCv%2B4gyVB9VRb2r%2B5H8wFbQwt34oaOCjdTQUu47KnL2L1drW7EJMU4b%2F%2FeDuO6P%2FtIgEH7EGQSu7DTVtrVB93TXKEJKNud4c3jOSDayk3ZqAAEXO9qbmeQfJlCUBlxiCddz3ZHrRso80OOpGHufNTmfhdg3KEBWw2Q7x7ImJZdOb%2ByByBHnqhg5iIm6myZ%2Fr2ZVUJr1xDzhrvyzHorOeUMOzX%2FrwGOqUBFdoBgkoErD2a8Vqnr5rLLrAT7CXaj8W1XPsnNS7fXVjLrrRizXepHKhUK17hRmAPMwwQb0lurySulToMl6KCTTIDOACVmVAyAoSL%2FHnvG8m1HXfp1Y%2BVIKPfmTLLiaMxUal2lxhfOiqKV27sZdtWQy6t8inbX16RJn6z3I0t6f713pOPwhss8peLDPxzHbo6S0UY5%2BUkqjrbBnSc4cvS5%2B4GDLiP&X-Amz-Signature=74e762a17bb4ae134d90ff6b3d800fbced132cff067696dd3e21f7859fb9a59d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UB32I4J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAyCA2QXkCvLOaNt%2B9q24MALJ2lCceAIUB1Z5BRJZwYjAiEA2iIrGHKLzmX6jDUSCHK1pRUyaOjJCWy0qAkjObOHvRkqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLy0brdbGVjrHN3mSrcA9J8297yyJ0Jbyikun2bQ4BjEnq970A7Nu6dpdXLUHqVgZsN%2BdHE9EDJvr5ECRW%2Bch1gZe5vtOBZzaikc6JEIJoLatmUEOl7TD1IYZhMD0x9Nh1HppJNcUNpHeuVoBDFaUwxD%2BM3PzlLNxUrqypn4MHZzKgm4kpUU8TuxWNSY%2BMzHVxBtcGiiMF5kWWItFBE83CIYk36lYQ%2FJS5aeH3WvJsREBnZemq3%2Fp1BZ71eZNe%2FXZx0%2F2s9Zympi7BvHsaFneJ1FWJI1f6LtbgLyb%2BEgP1H6kGMEBQNafw%2BvDAKSAbnl%2FicfV8tHorJF03JAu9Wp2kPiBEUpGwzy8uMmwvWcuYhgWw681ZEtiCYSiKy5ks6yU7cnZp%2Fh5AKGQ28RXk8wJl6GmVpCyeibbfrDUDcFwaNdufujjnKrMgks5BaCv%2B4gyVB9VRb2r%2B5H8wFbQwt34oaOCjdTQUu47KnL2L1drW7EJMU4b%2F%2FeDuO6P%2FtIgEH7EGQSu7DTVtrVB93TXKEJKNud4c3jOSDayk3ZqAAEXO9qbmeQfJlCUBlxiCddz3ZHrRso80OOpGHufNTmfhdg3KEBWw2Q7x7ImJZdOb%2ByByBHnqhg5iIm6myZ%2Fr2ZVUJr1xDzhrvyzHorOeUMOzX%2FrwGOqUBFdoBgkoErD2a8Vqnr5rLLrAT7CXaj8W1XPsnNS7fXVjLrrRizXepHKhUK17hRmAPMwwQb0lurySulToMl6KCTTIDOACVmVAyAoSL%2FHnvG8m1HXfp1Y%2BVIKPfmTLLiaMxUal2lxhfOiqKV27sZdtWQy6t8inbX16RJn6z3I0t6f713pOPwhss8peLDPxzHbo6S0UY5%2BUkqjrbBnSc4cvS5%2B4GDLiP&X-Amz-Signature=e699bf17014564b5ec11ae887572acde2c202d0b0d68aa0f05864aa38347d579&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UB32I4J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAyCA2QXkCvLOaNt%2B9q24MALJ2lCceAIUB1Z5BRJZwYjAiEA2iIrGHKLzmX6jDUSCHK1pRUyaOjJCWy0qAkjObOHvRkqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLy0brdbGVjrHN3mSrcA9J8297yyJ0Jbyikun2bQ4BjEnq970A7Nu6dpdXLUHqVgZsN%2BdHE9EDJvr5ECRW%2Bch1gZe5vtOBZzaikc6JEIJoLatmUEOl7TD1IYZhMD0x9Nh1HppJNcUNpHeuVoBDFaUwxD%2BM3PzlLNxUrqypn4MHZzKgm4kpUU8TuxWNSY%2BMzHVxBtcGiiMF5kWWItFBE83CIYk36lYQ%2FJS5aeH3WvJsREBnZemq3%2Fp1BZ71eZNe%2FXZx0%2F2s9Zympi7BvHsaFneJ1FWJI1f6LtbgLyb%2BEgP1H6kGMEBQNafw%2BvDAKSAbnl%2FicfV8tHorJF03JAu9Wp2kPiBEUpGwzy8uMmwvWcuYhgWw681ZEtiCYSiKy5ks6yU7cnZp%2Fh5AKGQ28RXk8wJl6GmVpCyeibbfrDUDcFwaNdufujjnKrMgks5BaCv%2B4gyVB9VRb2r%2B5H8wFbQwt34oaOCjdTQUu47KnL2L1drW7EJMU4b%2F%2FeDuO6P%2FtIgEH7EGQSu7DTVtrVB93TXKEJKNud4c3jOSDayk3ZqAAEXO9qbmeQfJlCUBlxiCddz3ZHrRso80OOpGHufNTmfhdg3KEBWw2Q7x7ImJZdOb%2ByByBHnqhg5iIm6myZ%2Fr2ZVUJr1xDzhrvyzHorOeUMOzX%2FrwGOqUBFdoBgkoErD2a8Vqnr5rLLrAT7CXaj8W1XPsnNS7fXVjLrrRizXepHKhUK17hRmAPMwwQb0lurySulToMl6KCTTIDOACVmVAyAoSL%2FHnvG8m1HXfp1Y%2BVIKPfmTLLiaMxUal2lxhfOiqKV27sZdtWQy6t8inbX16RJn6z3I0t6f713pOPwhss8peLDPxzHbo6S0UY5%2BUkqjrbBnSc4cvS5%2B4GDLiP&X-Amz-Signature=5928beb09e1ee75f885395967de1c93cb398bf7acc7d2dcdb8925eaa4856052b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UB32I4J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAyCA2QXkCvLOaNt%2B9q24MALJ2lCceAIUB1Z5BRJZwYjAiEA2iIrGHKLzmX6jDUSCHK1pRUyaOjJCWy0qAkjObOHvRkqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLy0brdbGVjrHN3mSrcA9J8297yyJ0Jbyikun2bQ4BjEnq970A7Nu6dpdXLUHqVgZsN%2BdHE9EDJvr5ECRW%2Bch1gZe5vtOBZzaikc6JEIJoLatmUEOl7TD1IYZhMD0x9Nh1HppJNcUNpHeuVoBDFaUwxD%2BM3PzlLNxUrqypn4MHZzKgm4kpUU8TuxWNSY%2BMzHVxBtcGiiMF5kWWItFBE83CIYk36lYQ%2FJS5aeH3WvJsREBnZemq3%2Fp1BZ71eZNe%2FXZx0%2F2s9Zympi7BvHsaFneJ1FWJI1f6LtbgLyb%2BEgP1H6kGMEBQNafw%2BvDAKSAbnl%2FicfV8tHorJF03JAu9Wp2kPiBEUpGwzy8uMmwvWcuYhgWw681ZEtiCYSiKy5ks6yU7cnZp%2Fh5AKGQ28RXk8wJl6GmVpCyeibbfrDUDcFwaNdufujjnKrMgks5BaCv%2B4gyVB9VRb2r%2B5H8wFbQwt34oaOCjdTQUu47KnL2L1drW7EJMU4b%2F%2FeDuO6P%2FtIgEH7EGQSu7DTVtrVB93TXKEJKNud4c3jOSDayk3ZqAAEXO9qbmeQfJlCUBlxiCddz3ZHrRso80OOpGHufNTmfhdg3KEBWw2Q7x7ImJZdOb%2ByByBHnqhg5iIm6myZ%2Fr2ZVUJr1xDzhrvyzHorOeUMOzX%2FrwGOqUBFdoBgkoErD2a8Vqnr5rLLrAT7CXaj8W1XPsnNS7fXVjLrrRizXepHKhUK17hRmAPMwwQb0lurySulToMl6KCTTIDOACVmVAyAoSL%2FHnvG8m1HXfp1Y%2BVIKPfmTLLiaMxUal2lxhfOiqKV27sZdtWQy6t8inbX16RJn6z3I0t6f713pOPwhss8peLDPxzHbo6S0UY5%2BUkqjrbBnSc4cvS5%2B4GDLiP&X-Amz-Signature=5c2d57ac5fc540d734b09e0268e7cc95c950fd3489c71041eb56ea5d85169add&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GSZRV6J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3U59TNy1APB8y1stLgiSUM50coTnMjOgInXSZpryfVAIhANUQBlxMPVA0X5AFrbJXH1U%2FAA3nP7vCDaumYLlrBNusKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymcO4iIFE94y6yoWYq3AMdtg61%2BDWYvP%2BFa9srtrzXu%2BY%2Fi64eF%2FoPG6u8urb%2B4Q95A5LgD1l8yb%2FBp4bsQT5x5mTw0NDT8QpUv1w9IhDOwTS5tkNylC6KVVWC619zBMSUbiRM7K9%2FTW77O9wIkwSvZK%2BoUP05QTLFjBxQEsvpeQQ%2B0JQv6q1qO4%2FNg6diogPNTxgmgGCIGZmxulIxVk491JeS8FqCZjFEpfo5nKsq8F7O%2FZ54RA9RmB%2FuC9DpQD2xo4gJDVnqC1Hdee86vgNoj8BlsHfazQIo97TiRmk7Wng7EhEIhz5sxjbctXazeu5Tt%2BmM9OggEN8NEbQvWQF0mLFAsnT2%2Bxza%2BoE69qyehS7xAwgdXm2qtwavClD6SUznAuUQAv447W%2BreZzeZJH4kf2ZnIWh0DbxrgMFAqBU%2BO6uJH2FV8dmSbmbqU0ctxICiUR6mTGDaE%2BnGCcpZXPEWUCGwVVHNLKpkodTdzFkqk4MIZ5JZww7zLzUhpRWFlso0bAmvbBOrrUy8UdvYzXnM0iL8%2Fxaqn%2FxBDpyZIlOkQF%2BN4lYki7LSe569QnvR8A5JUlB1OM8m8iaMbnn%2F%2BjKR47hL3jGUut3jqKpdKMd45SKrtGs%2FbjkbG1sBlNEkgrdMoWD4wWFF92K8zC85P68BjqkAW%2ByBu%2FB4a6tGTRPVjM3dpSz1JolmTgqrOEVKwX7wTLI8MRkMwRIO%2Fg%2F5JNuDCAp8i1S%2B7JUZ0Qm59EjxHTiIG%2BpdJZYm5XXN%2BW7ZzmjY%2FNy6iq%2FaxIFes%2FzJG2VdfLqfONTckPRk%2BKQlgrSQGZ0PvJKpUStPxV%2BgK7F0FITazrg%2BCj6VFLlI3CjJvUAkb%2BxJtkMrXOOknbsP5oL6Ur%2FPYL760A0&X-Amz-Signature=a448058928fdf1501e13e304d19b8e3596af1a998564d527d6677365e27bef06&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GSZRV6J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3U59TNy1APB8y1stLgiSUM50coTnMjOgInXSZpryfVAIhANUQBlxMPVA0X5AFrbJXH1U%2FAA3nP7vCDaumYLlrBNusKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymcO4iIFE94y6yoWYq3AMdtg61%2BDWYvP%2BFa9srtrzXu%2BY%2Fi64eF%2FoPG6u8urb%2B4Q95A5LgD1l8yb%2FBp4bsQT5x5mTw0NDT8QpUv1w9IhDOwTS5tkNylC6KVVWC619zBMSUbiRM7K9%2FTW77O9wIkwSvZK%2BoUP05QTLFjBxQEsvpeQQ%2B0JQv6q1qO4%2FNg6diogPNTxgmgGCIGZmxulIxVk491JeS8FqCZjFEpfo5nKsq8F7O%2FZ54RA9RmB%2FuC9DpQD2xo4gJDVnqC1Hdee86vgNoj8BlsHfazQIo97TiRmk7Wng7EhEIhz5sxjbctXazeu5Tt%2BmM9OggEN8NEbQvWQF0mLFAsnT2%2Bxza%2BoE69qyehS7xAwgdXm2qtwavClD6SUznAuUQAv447W%2BreZzeZJH4kf2ZnIWh0DbxrgMFAqBU%2BO6uJH2FV8dmSbmbqU0ctxICiUR6mTGDaE%2BnGCcpZXPEWUCGwVVHNLKpkodTdzFkqk4MIZ5JZww7zLzUhpRWFlso0bAmvbBOrrUy8UdvYzXnM0iL8%2Fxaqn%2FxBDpyZIlOkQF%2BN4lYki7LSe569QnvR8A5JUlB1OM8m8iaMbnn%2F%2BjKR47hL3jGUut3jqKpdKMd45SKrtGs%2FbjkbG1sBlNEkgrdMoWD4wWFF92K8zC85P68BjqkAW%2ByBu%2FB4a6tGTRPVjM3dpSz1JolmTgqrOEVKwX7wTLI8MRkMwRIO%2Fg%2F5JNuDCAp8i1S%2B7JUZ0Qm59EjxHTiIG%2BpdJZYm5XXN%2BW7ZzmjY%2FNy6iq%2FaxIFes%2FzJG2VdfLqfONTckPRk%2BKQlgrSQGZ0PvJKpUStPxV%2BgK7F0FITazrg%2BCj6VFLlI3CjJvUAkb%2BxJtkMrXOOknbsP5oL6Ur%2FPYL760A0&X-Amz-Signature=f7dba124fdc486f49d83a59b9e91089a12f387f5363ea17c28a0f9b85ab62579&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GSZRV6J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3U59TNy1APB8y1stLgiSUM50coTnMjOgInXSZpryfVAIhANUQBlxMPVA0X5AFrbJXH1U%2FAA3nP7vCDaumYLlrBNusKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymcO4iIFE94y6yoWYq3AMdtg61%2BDWYvP%2BFa9srtrzXu%2BY%2Fi64eF%2FoPG6u8urb%2B4Q95A5LgD1l8yb%2FBp4bsQT5x5mTw0NDT8QpUv1w9IhDOwTS5tkNylC6KVVWC619zBMSUbiRM7K9%2FTW77O9wIkwSvZK%2BoUP05QTLFjBxQEsvpeQQ%2B0JQv6q1qO4%2FNg6diogPNTxgmgGCIGZmxulIxVk491JeS8FqCZjFEpfo5nKsq8F7O%2FZ54RA9RmB%2FuC9DpQD2xo4gJDVnqC1Hdee86vgNoj8BlsHfazQIo97TiRmk7Wng7EhEIhz5sxjbctXazeu5Tt%2BmM9OggEN8NEbQvWQF0mLFAsnT2%2Bxza%2BoE69qyehS7xAwgdXm2qtwavClD6SUznAuUQAv447W%2BreZzeZJH4kf2ZnIWh0DbxrgMFAqBU%2BO6uJH2FV8dmSbmbqU0ctxICiUR6mTGDaE%2BnGCcpZXPEWUCGwVVHNLKpkodTdzFkqk4MIZ5JZww7zLzUhpRWFlso0bAmvbBOrrUy8UdvYzXnM0iL8%2Fxaqn%2FxBDpyZIlOkQF%2BN4lYki7LSe569QnvR8A5JUlB1OM8m8iaMbnn%2F%2BjKR47hL3jGUut3jqKpdKMd45SKrtGs%2FbjkbG1sBlNEkgrdMoWD4wWFF92K8zC85P68BjqkAW%2ByBu%2FB4a6tGTRPVjM3dpSz1JolmTgqrOEVKwX7wTLI8MRkMwRIO%2Fg%2F5JNuDCAp8i1S%2B7JUZ0Qm59EjxHTiIG%2BpdJZYm5XXN%2BW7ZzmjY%2FNy6iq%2FaxIFes%2FzJG2VdfLqfONTckPRk%2BKQlgrSQGZ0PvJKpUStPxV%2BgK7F0FITazrg%2BCj6VFLlI3CjJvUAkb%2BxJtkMrXOOknbsP5oL6Ur%2FPYL760A0&X-Amz-Signature=494a464574261505b48704dd9ad7c9f55686058aa4623c2e986652cc85568247&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GSZRV6J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3U59TNy1APB8y1stLgiSUM50coTnMjOgInXSZpryfVAIhANUQBlxMPVA0X5AFrbJXH1U%2FAA3nP7vCDaumYLlrBNusKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymcO4iIFE94y6yoWYq3AMdtg61%2BDWYvP%2BFa9srtrzXu%2BY%2Fi64eF%2FoPG6u8urb%2B4Q95A5LgD1l8yb%2FBp4bsQT5x5mTw0NDT8QpUv1w9IhDOwTS5tkNylC6KVVWC619zBMSUbiRM7K9%2FTW77O9wIkwSvZK%2BoUP05QTLFjBxQEsvpeQQ%2B0JQv6q1qO4%2FNg6diogPNTxgmgGCIGZmxulIxVk491JeS8FqCZjFEpfo5nKsq8F7O%2FZ54RA9RmB%2FuC9DpQD2xo4gJDVnqC1Hdee86vgNoj8BlsHfazQIo97TiRmk7Wng7EhEIhz5sxjbctXazeu5Tt%2BmM9OggEN8NEbQvWQF0mLFAsnT2%2Bxza%2BoE69qyehS7xAwgdXm2qtwavClD6SUznAuUQAv447W%2BreZzeZJH4kf2ZnIWh0DbxrgMFAqBU%2BO6uJH2FV8dmSbmbqU0ctxICiUR6mTGDaE%2BnGCcpZXPEWUCGwVVHNLKpkodTdzFkqk4MIZ5JZww7zLzUhpRWFlso0bAmvbBOrrUy8UdvYzXnM0iL8%2Fxaqn%2FxBDpyZIlOkQF%2BN4lYki7LSe569QnvR8A5JUlB1OM8m8iaMbnn%2F%2BjKR47hL3jGUut3jqKpdKMd45SKrtGs%2FbjkbG1sBlNEkgrdMoWD4wWFF92K8zC85P68BjqkAW%2ByBu%2FB4a6tGTRPVjM3dpSz1JolmTgqrOEVKwX7wTLI8MRkMwRIO%2Fg%2F5JNuDCAp8i1S%2B7JUZ0Qm59EjxHTiIG%2BpdJZYm5XXN%2BW7ZzmjY%2FNy6iq%2FaxIFes%2FzJG2VdfLqfONTckPRk%2BKQlgrSQGZ0PvJKpUStPxV%2BgK7F0FITazrg%2BCj6VFLlI3CjJvUAkb%2BxJtkMrXOOknbsP5oL6Ur%2FPYL760A0&X-Amz-Signature=28eb6f73dd4628272be1f83c1d79999769412c5bcd6978d5c5786b2e91aea87b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GSZRV6J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3U59TNy1APB8y1stLgiSUM50coTnMjOgInXSZpryfVAIhANUQBlxMPVA0X5AFrbJXH1U%2FAA3nP7vCDaumYLlrBNusKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymcO4iIFE94y6yoWYq3AMdtg61%2BDWYvP%2BFa9srtrzXu%2BY%2Fi64eF%2FoPG6u8urb%2B4Q95A5LgD1l8yb%2FBp4bsQT5x5mTw0NDT8QpUv1w9IhDOwTS5tkNylC6KVVWC619zBMSUbiRM7K9%2FTW77O9wIkwSvZK%2BoUP05QTLFjBxQEsvpeQQ%2B0JQv6q1qO4%2FNg6diogPNTxgmgGCIGZmxulIxVk491JeS8FqCZjFEpfo5nKsq8F7O%2FZ54RA9RmB%2FuC9DpQD2xo4gJDVnqC1Hdee86vgNoj8BlsHfazQIo97TiRmk7Wng7EhEIhz5sxjbctXazeu5Tt%2BmM9OggEN8NEbQvWQF0mLFAsnT2%2Bxza%2BoE69qyehS7xAwgdXm2qtwavClD6SUznAuUQAv447W%2BreZzeZJH4kf2ZnIWh0DbxrgMFAqBU%2BO6uJH2FV8dmSbmbqU0ctxICiUR6mTGDaE%2BnGCcpZXPEWUCGwVVHNLKpkodTdzFkqk4MIZ5JZww7zLzUhpRWFlso0bAmvbBOrrUy8UdvYzXnM0iL8%2Fxaqn%2FxBDpyZIlOkQF%2BN4lYki7LSe569QnvR8A5JUlB1OM8m8iaMbnn%2F%2BjKR47hL3jGUut3jqKpdKMd45SKrtGs%2FbjkbG1sBlNEkgrdMoWD4wWFF92K8zC85P68BjqkAW%2ByBu%2FB4a6tGTRPVjM3dpSz1JolmTgqrOEVKwX7wTLI8MRkMwRIO%2Fg%2F5JNuDCAp8i1S%2B7JUZ0Qm59EjxHTiIG%2BpdJZYm5XXN%2BW7ZzmjY%2FNy6iq%2FaxIFes%2FzJG2VdfLqfONTckPRk%2BKQlgrSQGZ0PvJKpUStPxV%2BgK7F0FITazrg%2BCj6VFLlI3CjJvUAkb%2BxJtkMrXOOknbsP5oL6Ur%2FPYL760A0&X-Amz-Signature=93b7df0297f191e48370e15cf85b9a6a8336b3bfd312c0c09d15518b074c73d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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


