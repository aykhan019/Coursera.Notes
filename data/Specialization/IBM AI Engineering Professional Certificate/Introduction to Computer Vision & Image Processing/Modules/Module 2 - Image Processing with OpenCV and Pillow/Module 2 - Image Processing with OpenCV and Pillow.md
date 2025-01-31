

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T56K2S22%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4Q1%2B0WoIIcNe1KeNm0vj9R8bQ63VripLE9GAcun5pXAiAdOAzI3BDMhLMRZgk4652U1YMV8Mc8doht78qcW8DWGCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMTE9Tu6q0oP7V9TnKtwDu1wZmrZt9uQyHMJUvtNfZUnqkq0KiRJa1%2FK3sxCytZePBwosWDMoR3d2WfYpaw3%2FbmSFkc3WolSV7B7z9faFIfH1I8TfDsG%2Fd%2BblUdddK4P4dxE6WqHcLyEgXkvdpeBxDhFJCcBNi5V%2B5GEuHfp6m0vtr4YmVgI7Au117Ksq7H0Plhl24L0%2Fh8TrBaaAx%2BzaBrs0yi1iAgnKrUHUntDaqpE4MIUhvPQgLyAGO0mODp3uACkjivlX6mj4Bl%2F6TCKceljaAd3Ybjmi1c3982B23BsEw%2B63lxYBeAQY6eCIunnDks8cA7m5iQ3laPEbCbspEyVLLA3iSPqgVTchKU18%2FfIoTJH2E%2FfX%2BSkX17Dt2EEdLA3bt7OvsM2oTe6BznjgLuoEzdftM8%2Fng1hoZ6npzJbLAAudE%2BzGWsTQ80FLu4YLhFcEqmTadG58wxmSRAUqkTHHxJdAKKlu6y16ESRiwXktT4kjsMI3JZWRfQZTwJcKyG609qWAK8ZesH1%2B9oak3%2BhGndss1Yn2DjeO4ECiE%2FXbaVuwBbRBOiszLDDJeIWuFHIidJ57hxggCwDB%2Fvip8vgbVwi4t06T6YwVGwdZND5zlh9vxHG7PpD21Hrrow4W%2Bz6AiBf8BPqywXQw39DwvAY6pgFuoEgSHPMlifvCfhK3XIKDAmPTFkoElmmhtIb9i2fU0sMOhFJehlZ63raIdVCttlB9Sizfe0z4vdqBS%2FrLmg%2BFxT5qo%2FWNOwe%2FMGeAaVqSp9n1jgvMNATE4ZiORm1FxWqmmON2BnYYsukSie072VMabgI%2B5HXI6lnJW23HolMHNCLn18ZI3FUWb9rgQWXMAyLY8zI%2FusSNNpxuH9FLhP7pZqZqEo0L&X-Amz-Signature=c1a823c00380525ff35f8381957e518c2f5c06b5a154b70ac15e94075de0b06b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQZJYQCN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHlrV0bJm6XIKA0EZwxI%2FPK%2F8vNRbmX%2BZcOwdU6f9%2FOSAiBv141ZZKk9xA0GLcUivTgLBW4%2Fn5LN959nE73DluNKXCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BKBa7cbz6cX9dp%2B1KtwDJTwEeunKuMKcTRFq%2FQ9wfZWMPnfpQeeG%2B3fSf6Qs88L2kEtxnFIqJ6Idr9qnC2sswQ%2FBHj2LQe%2B7xAHb17Fs0y0Cs47jBOmjxR%2Fosl3nJbS8M8ZCUIBB5NsrlbqqVkrzZY52Ca9K9V0IeL7%2BWox9zvLVirisBuuaNhmIiRkQz0yNucunmFDkEeWBGPePhUYYj7a3a73feSPKoG%2FW4VkTVs7%2FancL5AjNvjJqlf1TED8tGm69ientWUZvOQ%2BV95b9QLamyKwO%2Fs%2F4%2BnZhywmtBydKaLXsIexZ6Bbu05kkikbX3JV62FpGPn%2BlQKfcn0aIIsBapfhoXvv%2BPPZ6xqqL1%2BTnWuygbeF4yk3EuOl7WpGfDsckyIWfc43BHb%2FPvempdEFJ7IbhQdEIzDs1ZNsc2m6f%2F2hjWujd1Qt%2FwIljXWK220luTg865nAi89IHOCs5%2BLn%2BEiLzMUbRPGm4b7HKvuCTvt9nhRfR%2BlP%2BvTJd9PgY7qoE6VHE9j%2Bl%2ByDRPEJ5pjJE6ahiX9mPmy2RU5%2Frs5Tixay3l4RAYefNoeIzBzatrw19TndmzywPx05Lm5Xm%2BeTtdODVOkyifxm00oGVUgQR5H1wZOOCICx3tVpjIBSLCu8%2FBQhgt%2FBXGHYwnNDwvAY6pgEenzCf%2BQg%2FyB4y0LkUWXFsKqa7C5B75W6ure0soEELyCnKspMqhD4QUTdnX94fYRR6Tq24nNs5nRUGlB0MEveoooc5HIWQ2QDQUwO9C%2F232cDfdCTgElJA1aCVMdSLlFmgUtDIkwTkPBohIZwEjVFZXAwkMywVvDHyt0oQ4sSvhq7ZSEpCcaPgv%2Bx6Vzv%2BGum3poMqkb0KzXoxdm5K76i2sGqEvfGr&X-Amz-Signature=4227f061dc412664dda399e65200c293d59408e237a64d070a35311b12738f54&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQZJYQCN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHlrV0bJm6XIKA0EZwxI%2FPK%2F8vNRbmX%2BZcOwdU6f9%2FOSAiBv141ZZKk9xA0GLcUivTgLBW4%2Fn5LN959nE73DluNKXCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BKBa7cbz6cX9dp%2B1KtwDJTwEeunKuMKcTRFq%2FQ9wfZWMPnfpQeeG%2B3fSf6Qs88L2kEtxnFIqJ6Idr9qnC2sswQ%2FBHj2LQe%2B7xAHb17Fs0y0Cs47jBOmjxR%2Fosl3nJbS8M8ZCUIBB5NsrlbqqVkrzZY52Ca9K9V0IeL7%2BWox9zvLVirisBuuaNhmIiRkQz0yNucunmFDkEeWBGPePhUYYj7a3a73feSPKoG%2FW4VkTVs7%2FancL5AjNvjJqlf1TED8tGm69ientWUZvOQ%2BV95b9QLamyKwO%2Fs%2F4%2BnZhywmtBydKaLXsIexZ6Bbu05kkikbX3JV62FpGPn%2BlQKfcn0aIIsBapfhoXvv%2BPPZ6xqqL1%2BTnWuygbeF4yk3EuOl7WpGfDsckyIWfc43BHb%2FPvempdEFJ7IbhQdEIzDs1ZNsc2m6f%2F2hjWujd1Qt%2FwIljXWK220luTg865nAi89IHOCs5%2BLn%2BEiLzMUbRPGm4b7HKvuCTvt9nhRfR%2BlP%2BvTJd9PgY7qoE6VHE9j%2Bl%2ByDRPEJ5pjJE6ahiX9mPmy2RU5%2Frs5Tixay3l4RAYefNoeIzBzatrw19TndmzywPx05Lm5Xm%2BeTtdODVOkyifxm00oGVUgQR5H1wZOOCICx3tVpjIBSLCu8%2FBQhgt%2FBXGHYwnNDwvAY6pgEenzCf%2BQg%2FyB4y0LkUWXFsKqa7C5B75W6ure0soEELyCnKspMqhD4QUTdnX94fYRR6Tq24nNs5nRUGlB0MEveoooc5HIWQ2QDQUwO9C%2F232cDfdCTgElJA1aCVMdSLlFmgUtDIkwTkPBohIZwEjVFZXAwkMywVvDHyt0oQ4sSvhq7ZSEpCcaPgv%2Bx6Vzv%2BGum3poMqkb0KzXoxdm5K76i2sGqEvfGr&X-Amz-Signature=7c92b0a4b9d9afe11ca809a103fc71a1034fba009b85fd7a4721985f392f778f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQZJYQCN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHlrV0bJm6XIKA0EZwxI%2FPK%2F8vNRbmX%2BZcOwdU6f9%2FOSAiBv141ZZKk9xA0GLcUivTgLBW4%2Fn5LN959nE73DluNKXCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BKBa7cbz6cX9dp%2B1KtwDJTwEeunKuMKcTRFq%2FQ9wfZWMPnfpQeeG%2B3fSf6Qs88L2kEtxnFIqJ6Idr9qnC2sswQ%2FBHj2LQe%2B7xAHb17Fs0y0Cs47jBOmjxR%2Fosl3nJbS8M8ZCUIBB5NsrlbqqVkrzZY52Ca9K9V0IeL7%2BWox9zvLVirisBuuaNhmIiRkQz0yNucunmFDkEeWBGPePhUYYj7a3a73feSPKoG%2FW4VkTVs7%2FancL5AjNvjJqlf1TED8tGm69ientWUZvOQ%2BV95b9QLamyKwO%2Fs%2F4%2BnZhywmtBydKaLXsIexZ6Bbu05kkikbX3JV62FpGPn%2BlQKfcn0aIIsBapfhoXvv%2BPPZ6xqqL1%2BTnWuygbeF4yk3EuOl7WpGfDsckyIWfc43BHb%2FPvempdEFJ7IbhQdEIzDs1ZNsc2m6f%2F2hjWujd1Qt%2FwIljXWK220luTg865nAi89IHOCs5%2BLn%2BEiLzMUbRPGm4b7HKvuCTvt9nhRfR%2BlP%2BvTJd9PgY7qoE6VHE9j%2Bl%2ByDRPEJ5pjJE6ahiX9mPmy2RU5%2Frs5Tixay3l4RAYefNoeIzBzatrw19TndmzywPx05Lm5Xm%2BeTtdODVOkyifxm00oGVUgQR5H1wZOOCICx3tVpjIBSLCu8%2FBQhgt%2FBXGHYwnNDwvAY6pgEenzCf%2BQg%2FyB4y0LkUWXFsKqa7C5B75W6ure0soEELyCnKspMqhD4QUTdnX94fYRR6Tq24nNs5nRUGlB0MEveoooc5HIWQ2QDQUwO9C%2F232cDfdCTgElJA1aCVMdSLlFmgUtDIkwTkPBohIZwEjVFZXAwkMywVvDHyt0oQ4sSvhq7ZSEpCcaPgv%2Bx6Vzv%2BGum3poMqkb0KzXoxdm5K76i2sGqEvfGr&X-Amz-Signature=86b8bc01f95c2d4638a157d21960b58537cad7bfe0f88235855a2691a45dd0bf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQZJYQCN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHlrV0bJm6XIKA0EZwxI%2FPK%2F8vNRbmX%2BZcOwdU6f9%2FOSAiBv141ZZKk9xA0GLcUivTgLBW4%2Fn5LN959nE73DluNKXCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BKBa7cbz6cX9dp%2B1KtwDJTwEeunKuMKcTRFq%2FQ9wfZWMPnfpQeeG%2B3fSf6Qs88L2kEtxnFIqJ6Idr9qnC2sswQ%2FBHj2LQe%2B7xAHb17Fs0y0Cs47jBOmjxR%2Fosl3nJbS8M8ZCUIBB5NsrlbqqVkrzZY52Ca9K9V0IeL7%2BWox9zvLVirisBuuaNhmIiRkQz0yNucunmFDkEeWBGPePhUYYj7a3a73feSPKoG%2FW4VkTVs7%2FancL5AjNvjJqlf1TED8tGm69ientWUZvOQ%2BV95b9QLamyKwO%2Fs%2F4%2BnZhywmtBydKaLXsIexZ6Bbu05kkikbX3JV62FpGPn%2BlQKfcn0aIIsBapfhoXvv%2BPPZ6xqqL1%2BTnWuygbeF4yk3EuOl7WpGfDsckyIWfc43BHb%2FPvempdEFJ7IbhQdEIzDs1ZNsc2m6f%2F2hjWujd1Qt%2FwIljXWK220luTg865nAi89IHOCs5%2BLn%2BEiLzMUbRPGm4b7HKvuCTvt9nhRfR%2BlP%2BvTJd9PgY7qoE6VHE9j%2Bl%2ByDRPEJ5pjJE6ahiX9mPmy2RU5%2Frs5Tixay3l4RAYefNoeIzBzatrw19TndmzywPx05Lm5Xm%2BeTtdODVOkyifxm00oGVUgQR5H1wZOOCICx3tVpjIBSLCu8%2FBQhgt%2FBXGHYwnNDwvAY6pgEenzCf%2BQg%2FyB4y0LkUWXFsKqa7C5B75W6ure0soEELyCnKspMqhD4QUTdnX94fYRR6Tq24nNs5nRUGlB0MEveoooc5HIWQ2QDQUwO9C%2F232cDfdCTgElJA1aCVMdSLlFmgUtDIkwTkPBohIZwEjVFZXAwkMywVvDHyt0oQ4sSvhq7ZSEpCcaPgv%2Bx6Vzv%2BGum3poMqkb0KzXoxdm5K76i2sGqEvfGr&X-Amz-Signature=6f51a6fdc335fe314188419c50499bd991b20b5d372517a9be243014fa7ec3ba&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQZJYQCN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHlrV0bJm6XIKA0EZwxI%2FPK%2F8vNRbmX%2BZcOwdU6f9%2FOSAiBv141ZZKk9xA0GLcUivTgLBW4%2Fn5LN959nE73DluNKXCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BKBa7cbz6cX9dp%2B1KtwDJTwEeunKuMKcTRFq%2FQ9wfZWMPnfpQeeG%2B3fSf6Qs88L2kEtxnFIqJ6Idr9qnC2sswQ%2FBHj2LQe%2B7xAHb17Fs0y0Cs47jBOmjxR%2Fosl3nJbS8M8ZCUIBB5NsrlbqqVkrzZY52Ca9K9V0IeL7%2BWox9zvLVirisBuuaNhmIiRkQz0yNucunmFDkEeWBGPePhUYYj7a3a73feSPKoG%2FW4VkTVs7%2FancL5AjNvjJqlf1TED8tGm69ientWUZvOQ%2BV95b9QLamyKwO%2Fs%2F4%2BnZhywmtBydKaLXsIexZ6Bbu05kkikbX3JV62FpGPn%2BlQKfcn0aIIsBapfhoXvv%2BPPZ6xqqL1%2BTnWuygbeF4yk3EuOl7WpGfDsckyIWfc43BHb%2FPvempdEFJ7IbhQdEIzDs1ZNsc2m6f%2F2hjWujd1Qt%2FwIljXWK220luTg865nAi89IHOCs5%2BLn%2BEiLzMUbRPGm4b7HKvuCTvt9nhRfR%2BlP%2BvTJd9PgY7qoE6VHE9j%2Bl%2ByDRPEJ5pjJE6ahiX9mPmy2RU5%2Frs5Tixay3l4RAYefNoeIzBzatrw19TndmzywPx05Lm5Xm%2BeTtdODVOkyifxm00oGVUgQR5H1wZOOCICx3tVpjIBSLCu8%2FBQhgt%2FBXGHYwnNDwvAY6pgEenzCf%2BQg%2FyB4y0LkUWXFsKqa7C5B75W6ure0soEELyCnKspMqhD4QUTdnX94fYRR6Tq24nNs5nRUGlB0MEveoooc5HIWQ2QDQUwO9C%2F232cDfdCTgElJA1aCVMdSLlFmgUtDIkwTkPBohIZwEjVFZXAwkMywVvDHyt0oQ4sSvhq7ZSEpCcaPgv%2Bx6Vzv%2BGum3poMqkb0KzXoxdm5K76i2sGqEvfGr&X-Amz-Signature=f08bd6976af45d7849e81c46ab8eaef761d7a878d464f0250b170fd3c6883158&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T56K2S22%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4Q1%2B0WoIIcNe1KeNm0vj9R8bQ63VripLE9GAcun5pXAiAdOAzI3BDMhLMRZgk4652U1YMV8Mc8doht78qcW8DWGCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMTE9Tu6q0oP7V9TnKtwDu1wZmrZt9uQyHMJUvtNfZUnqkq0KiRJa1%2FK3sxCytZePBwosWDMoR3d2WfYpaw3%2FbmSFkc3WolSV7B7z9faFIfH1I8TfDsG%2Fd%2BblUdddK4P4dxE6WqHcLyEgXkvdpeBxDhFJCcBNi5V%2B5GEuHfp6m0vtr4YmVgI7Au117Ksq7H0Plhl24L0%2Fh8TrBaaAx%2BzaBrs0yi1iAgnKrUHUntDaqpE4MIUhvPQgLyAGO0mODp3uACkjivlX6mj4Bl%2F6TCKceljaAd3Ybjmi1c3982B23BsEw%2B63lxYBeAQY6eCIunnDks8cA7m5iQ3laPEbCbspEyVLLA3iSPqgVTchKU18%2FfIoTJH2E%2FfX%2BSkX17Dt2EEdLA3bt7OvsM2oTe6BznjgLuoEzdftM8%2Fng1hoZ6npzJbLAAudE%2BzGWsTQ80FLu4YLhFcEqmTadG58wxmSRAUqkTHHxJdAKKlu6y16ESRiwXktT4kjsMI3JZWRfQZTwJcKyG609qWAK8ZesH1%2B9oak3%2BhGndss1Yn2DjeO4ECiE%2FXbaVuwBbRBOiszLDDJeIWuFHIidJ57hxggCwDB%2Fvip8vgbVwi4t06T6YwVGwdZND5zlh9vxHG7PpD21Hrrow4W%2Bz6AiBf8BPqywXQw39DwvAY6pgFuoEgSHPMlifvCfhK3XIKDAmPTFkoElmmhtIb9i2fU0sMOhFJehlZ63raIdVCttlB9Sizfe0z4vdqBS%2FrLmg%2BFxT5qo%2FWNOwe%2FMGeAaVqSp9n1jgvMNATE4ZiORm1FxWqmmON2BnYYsukSie072VMabgI%2B5HXI6lnJW23HolMHNCLn18ZI3FUWb9rgQWXMAyLY8zI%2FusSNNpxuH9FLhP7pZqZqEo0L&X-Amz-Signature=64b100714dee88e2bf0a7e40e44ee76905f0a04289ae6c20391b2eef7cabed64&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T56K2S22%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4Q1%2B0WoIIcNe1KeNm0vj9R8bQ63VripLE9GAcun5pXAiAdOAzI3BDMhLMRZgk4652U1YMV8Mc8doht78qcW8DWGCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMTE9Tu6q0oP7V9TnKtwDu1wZmrZt9uQyHMJUvtNfZUnqkq0KiRJa1%2FK3sxCytZePBwosWDMoR3d2WfYpaw3%2FbmSFkc3WolSV7B7z9faFIfH1I8TfDsG%2Fd%2BblUdddK4P4dxE6WqHcLyEgXkvdpeBxDhFJCcBNi5V%2B5GEuHfp6m0vtr4YmVgI7Au117Ksq7H0Plhl24L0%2Fh8TrBaaAx%2BzaBrs0yi1iAgnKrUHUntDaqpE4MIUhvPQgLyAGO0mODp3uACkjivlX6mj4Bl%2F6TCKceljaAd3Ybjmi1c3982B23BsEw%2B63lxYBeAQY6eCIunnDks8cA7m5iQ3laPEbCbspEyVLLA3iSPqgVTchKU18%2FfIoTJH2E%2FfX%2BSkX17Dt2EEdLA3bt7OvsM2oTe6BznjgLuoEzdftM8%2Fng1hoZ6npzJbLAAudE%2BzGWsTQ80FLu4YLhFcEqmTadG58wxmSRAUqkTHHxJdAKKlu6y16ESRiwXktT4kjsMI3JZWRfQZTwJcKyG609qWAK8ZesH1%2B9oak3%2BhGndss1Yn2DjeO4ECiE%2FXbaVuwBbRBOiszLDDJeIWuFHIidJ57hxggCwDB%2Fvip8vgbVwi4t06T6YwVGwdZND5zlh9vxHG7PpD21Hrrow4W%2Bz6AiBf8BPqywXQw39DwvAY6pgFuoEgSHPMlifvCfhK3XIKDAmPTFkoElmmhtIb9i2fU0sMOhFJehlZ63raIdVCttlB9Sizfe0z4vdqBS%2FrLmg%2BFxT5qo%2FWNOwe%2FMGeAaVqSp9n1jgvMNATE4ZiORm1FxWqmmON2BnYYsukSie072VMabgI%2B5HXI6lnJW23HolMHNCLn18ZI3FUWb9rgQWXMAyLY8zI%2FusSNNpxuH9FLhP7pZqZqEo0L&X-Amz-Signature=33b6ab35b022263f3161d180b1e69185a8820d28ff37120cc3134283e7b91af6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T56K2S22%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4Q1%2B0WoIIcNe1KeNm0vj9R8bQ63VripLE9GAcun5pXAiAdOAzI3BDMhLMRZgk4652U1YMV8Mc8doht78qcW8DWGCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMTE9Tu6q0oP7V9TnKtwDu1wZmrZt9uQyHMJUvtNfZUnqkq0KiRJa1%2FK3sxCytZePBwosWDMoR3d2WfYpaw3%2FbmSFkc3WolSV7B7z9faFIfH1I8TfDsG%2Fd%2BblUdddK4P4dxE6WqHcLyEgXkvdpeBxDhFJCcBNi5V%2B5GEuHfp6m0vtr4YmVgI7Au117Ksq7H0Plhl24L0%2Fh8TrBaaAx%2BzaBrs0yi1iAgnKrUHUntDaqpE4MIUhvPQgLyAGO0mODp3uACkjivlX6mj4Bl%2F6TCKceljaAd3Ybjmi1c3982B23BsEw%2B63lxYBeAQY6eCIunnDks8cA7m5iQ3laPEbCbspEyVLLA3iSPqgVTchKU18%2FfIoTJH2E%2FfX%2BSkX17Dt2EEdLA3bt7OvsM2oTe6BznjgLuoEzdftM8%2Fng1hoZ6npzJbLAAudE%2BzGWsTQ80FLu4YLhFcEqmTadG58wxmSRAUqkTHHxJdAKKlu6y16ESRiwXktT4kjsMI3JZWRfQZTwJcKyG609qWAK8ZesH1%2B9oak3%2BhGndss1Yn2DjeO4ECiE%2FXbaVuwBbRBOiszLDDJeIWuFHIidJ57hxggCwDB%2Fvip8vgbVwi4t06T6YwVGwdZND5zlh9vxHG7PpD21Hrrow4W%2Bz6AiBf8BPqywXQw39DwvAY6pgFuoEgSHPMlifvCfhK3XIKDAmPTFkoElmmhtIb9i2fU0sMOhFJehlZ63raIdVCttlB9Sizfe0z4vdqBS%2FrLmg%2BFxT5qo%2FWNOwe%2FMGeAaVqSp9n1jgvMNATE4ZiORm1FxWqmmON2BnYYsukSie072VMabgI%2B5HXI6lnJW23HolMHNCLn18ZI3FUWb9rgQWXMAyLY8zI%2FusSNNpxuH9FLhP7pZqZqEo0L&X-Amz-Signature=eed4b6345ca4e60d9b2a7f2caedf9c70b33d442bf1fa1057538370dfcc54e32d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T56K2S22%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4Q1%2B0WoIIcNe1KeNm0vj9R8bQ63VripLE9GAcun5pXAiAdOAzI3BDMhLMRZgk4652U1YMV8Mc8doht78qcW8DWGCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMTE9Tu6q0oP7V9TnKtwDu1wZmrZt9uQyHMJUvtNfZUnqkq0KiRJa1%2FK3sxCytZePBwosWDMoR3d2WfYpaw3%2FbmSFkc3WolSV7B7z9faFIfH1I8TfDsG%2Fd%2BblUdddK4P4dxE6WqHcLyEgXkvdpeBxDhFJCcBNi5V%2B5GEuHfp6m0vtr4YmVgI7Au117Ksq7H0Plhl24L0%2Fh8TrBaaAx%2BzaBrs0yi1iAgnKrUHUntDaqpE4MIUhvPQgLyAGO0mODp3uACkjivlX6mj4Bl%2F6TCKceljaAd3Ybjmi1c3982B23BsEw%2B63lxYBeAQY6eCIunnDks8cA7m5iQ3laPEbCbspEyVLLA3iSPqgVTchKU18%2FfIoTJH2E%2FfX%2BSkX17Dt2EEdLA3bt7OvsM2oTe6BznjgLuoEzdftM8%2Fng1hoZ6npzJbLAAudE%2BzGWsTQ80FLu4YLhFcEqmTadG58wxmSRAUqkTHHxJdAKKlu6y16ESRiwXktT4kjsMI3JZWRfQZTwJcKyG609qWAK8ZesH1%2B9oak3%2BhGndss1Yn2DjeO4ECiE%2FXbaVuwBbRBOiszLDDJeIWuFHIidJ57hxggCwDB%2Fvip8vgbVwi4t06T6YwVGwdZND5zlh9vxHG7PpD21Hrrow4W%2Bz6AiBf8BPqywXQw39DwvAY6pgFuoEgSHPMlifvCfhK3XIKDAmPTFkoElmmhtIb9i2fU0sMOhFJehlZ63raIdVCttlB9Sizfe0z4vdqBS%2FrLmg%2BFxT5qo%2FWNOwe%2FMGeAaVqSp9n1jgvMNATE4ZiORm1FxWqmmON2BnYYsukSie072VMabgI%2B5HXI6lnJW23HolMHNCLn18ZI3FUWb9rgQWXMAyLY8zI%2FusSNNpxuH9FLhP7pZqZqEo0L&X-Amz-Signature=695a4da9dd8b4e2e97c72e48dba70d3f47f0685f423ce1aacca71edfa9a94084&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T56K2S22%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4Q1%2B0WoIIcNe1KeNm0vj9R8bQ63VripLE9GAcun5pXAiAdOAzI3BDMhLMRZgk4652U1YMV8Mc8doht78qcW8DWGCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMTE9Tu6q0oP7V9TnKtwDu1wZmrZt9uQyHMJUvtNfZUnqkq0KiRJa1%2FK3sxCytZePBwosWDMoR3d2WfYpaw3%2FbmSFkc3WolSV7B7z9faFIfH1I8TfDsG%2Fd%2BblUdddK4P4dxE6WqHcLyEgXkvdpeBxDhFJCcBNi5V%2B5GEuHfp6m0vtr4YmVgI7Au117Ksq7H0Plhl24L0%2Fh8TrBaaAx%2BzaBrs0yi1iAgnKrUHUntDaqpE4MIUhvPQgLyAGO0mODp3uACkjivlX6mj4Bl%2F6TCKceljaAd3Ybjmi1c3982B23BsEw%2B63lxYBeAQY6eCIunnDks8cA7m5iQ3laPEbCbspEyVLLA3iSPqgVTchKU18%2FfIoTJH2E%2FfX%2BSkX17Dt2EEdLA3bt7OvsM2oTe6BznjgLuoEzdftM8%2Fng1hoZ6npzJbLAAudE%2BzGWsTQ80FLu4YLhFcEqmTadG58wxmSRAUqkTHHxJdAKKlu6y16ESRiwXktT4kjsMI3JZWRfQZTwJcKyG609qWAK8ZesH1%2B9oak3%2BhGndss1Yn2DjeO4ECiE%2FXbaVuwBbRBOiszLDDJeIWuFHIidJ57hxggCwDB%2Fvip8vgbVwi4t06T6YwVGwdZND5zlh9vxHG7PpD21Hrrow4W%2Bz6AiBf8BPqywXQw39DwvAY6pgFuoEgSHPMlifvCfhK3XIKDAmPTFkoElmmhtIb9i2fU0sMOhFJehlZ63raIdVCttlB9Sizfe0z4vdqBS%2FrLmg%2BFxT5qo%2FWNOwe%2FMGeAaVqSp9n1jgvMNATE4ZiORm1FxWqmmON2BnYYsukSie072VMabgI%2B5HXI6lnJW23HolMHNCLn18ZI3FUWb9rgQWXMAyLY8zI%2FusSNNpxuH9FLhP7pZqZqEo0L&X-Amz-Signature=9290c83c8519ea0a4c4fafd2a05cfa106bf754c85ae81bb436409acd4093c4f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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


