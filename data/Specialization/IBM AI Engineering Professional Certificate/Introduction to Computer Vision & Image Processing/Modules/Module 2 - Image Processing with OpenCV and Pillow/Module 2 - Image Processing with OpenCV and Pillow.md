

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFQMKXFT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDclW7PX0wj%2BVgea2ucgzqmUvjJxIjfvaWMkFyy0lxi9wIhAKkPKEiLgHGaiet7fnkjLJNeuhXc2UqCAE0WHfhCETR%2FKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFjIr7bTPc4puT7Iq3AOK4YYzUwRnRk1%2B4ua52jZ3JS%2BDl89rieheEVxQ2sLjItbCOSSKrDd0tQFdsXTHlQu1NsN5FyMv%2FLtGVPYeNSTWpsjWdYRI%2FxhQMv1Y3fGM96jUY2ki5bnbpVuVYKEy6oyB092oCefjaBwsziB6ptFRvMhfx8dphcM1njmQqGdxOqu7h2m9y5nrPvJzE40AIVcxA%2B16YsOxVshK6jOkgr3KERJCOmoXiyYomLniXf8Z2I9a3ynFs1pHizdqXGwOlnj8pkh%2BprOPEujxy1esw2%2BjZyDZCUJTiCKGZlE8I%2BR83to4xHaSMfBjDcMv925gzoCE5NXdEDEW5kjedvAAvofAo80JkQ%2Bb844gwhJOFuy00Uxxy1Ji9FiutOAHnD%2BuhWNVt4z3pxvBiSuP8cuEoER6wSw23mBWc5YhKtukmWfkEi46MEKR%2FZkm8nmHdxb%2FeDeBHhaeeMaQGqQ9umzLe742aeHzmdDihbK4uslSuYu%2FunHk7vdAYWJ8ysBoj2YvY4kbX2JnPPOPROS5jP42QLxeqd2uLuLgs56d%2FNZa6IL%2F2NTSw7unuvAiO17bIcywV7SARb2ldkL1375fzrSg72NUPjjT9IGBIVoUxR5Xsz84oby%2FEgH6qa%2F%2FyrwCAjDZmvK8BjqkAex%2BVx66hMP5KHZYG9xpx%2BKygs016DP7nbb9W4U%2BsDCFUg%2Fcv6InvG%2BSVES1arfMQCtrJ%2Ffm48ZrSKe3%2F6UmUuBji8CsC0gdlcP8BhPoDikiU%2FOYH%2BuwXoherHvn6Wl%2FbBTGm5ZlRkneZPYph9cYbCk0K2MTfxKXmrxNq49Vz9DUaVC3IAijSUuPuMZxgv%2BwrCrOAAAWa98qfhPPOqfnzAzIfWR%2B&X-Amz-Signature=b51f698b47936514bace7022acc2906cdd9780ce223e92814e78575c50624ee6&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSOH5IY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8taFso1KNyIsd4cL3viW3RUvrkBMjbEj%2F6H3ST2P6SgIhANshsd6lkDZFTKsqn6Z4hGFGGltcL1OyEoQbz40Y4EGAKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwi%2F%2FhvxC1%2B%2Bl6l0BMq3ANxSt8by7WIpsHvR%2F%2Buisw1ws4kKD6tUVTg7C5PirLB0QPnCHHpQdlfJxFCuFhpZie5mCXLRQH1pYvCgpWzcgeIb401rPZ%2B6ONq703D3kilGw%2F7O%2BndnTzIQ6zAedRPYH2z8K%2F2CikZEbxLBTJYVXqeIDS75W5vsQfFEeiyXScqYnwEX2Vah8Eaz1W9NEyv8cPIWitfNmKw82ZDbgNmn6%2FWypOqq2ERssbA1xlM1ShvBg42dMLkgGdAMrkPBS4TRDGlbx1mMMu%2Bl%2B0MxYlM4ykYBUwxUwk1SABBJd2IG7EbqVIOduF%2B4blKBUHtunmtsLzexY5nkkD2cIeTd2ldg1RJUAGtIaYeBDB1YPmSKypXuvKR6aIwtAAsReRmKE3%2FUIx7kg25icovIALT8KIhl4c%2B%2FFY76rH1XaJmsVzGOzsTIMeMDlNUDrwP9PamVohANjXeCvCmDwSda8pxI7x5GFSU6a%2FGr6epBFHtYV64NNHJB8G8ltaZJiiUbNmaHIYwQ7%2FePfRAd24T7MqSekzJOTSc14g2QmDfPm3K00uDS67nTzLBysjd3ROcXBMFMSmA%2FDe7CIVso%2BPQAe6seT3s889UuencS%2F9%2Fv7ATQ9XTBJXbs%2BcTb90rMi2%2BHh7gdzCumvK8BjqkAe9Lpz2bLQ6boBIur%2FUMh7W7mn6CORgMVb29U2BohZqWg4MmUhWwpPTTbwDRhJ31%2BMq8UetJQSJvJaaifsoeZoYuyYvo6WsvMxS5S0NcSFxrB0Ws5sNhLmtyW7fEbAbfflpkMisWJhLs6OFOVCNr7B2Ot0t9GoKbS3UY2qs3Vcocn%2FltRcqvaAyHUk65Yiw%2Fypm5S3MqRZ6Gr%2FPqUKNqNWHOV03%2B&X-Amz-Signature=e3659fb2db43a8a57f44a3ac6732d2ff7ea4dc116986e19f680be5f3a92bd92c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSOH5IY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8taFso1KNyIsd4cL3viW3RUvrkBMjbEj%2F6H3ST2P6SgIhANshsd6lkDZFTKsqn6Z4hGFGGltcL1OyEoQbz40Y4EGAKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwi%2F%2FhvxC1%2B%2Bl6l0BMq3ANxSt8by7WIpsHvR%2F%2Buisw1ws4kKD6tUVTg7C5PirLB0QPnCHHpQdlfJxFCuFhpZie5mCXLRQH1pYvCgpWzcgeIb401rPZ%2B6ONq703D3kilGw%2F7O%2BndnTzIQ6zAedRPYH2z8K%2F2CikZEbxLBTJYVXqeIDS75W5vsQfFEeiyXScqYnwEX2Vah8Eaz1W9NEyv8cPIWitfNmKw82ZDbgNmn6%2FWypOqq2ERssbA1xlM1ShvBg42dMLkgGdAMrkPBS4TRDGlbx1mMMu%2Bl%2B0MxYlM4ykYBUwxUwk1SABBJd2IG7EbqVIOduF%2B4blKBUHtunmtsLzexY5nkkD2cIeTd2ldg1RJUAGtIaYeBDB1YPmSKypXuvKR6aIwtAAsReRmKE3%2FUIx7kg25icovIALT8KIhl4c%2B%2FFY76rH1XaJmsVzGOzsTIMeMDlNUDrwP9PamVohANjXeCvCmDwSda8pxI7x5GFSU6a%2FGr6epBFHtYV64NNHJB8G8ltaZJiiUbNmaHIYwQ7%2FePfRAd24T7MqSekzJOTSc14g2QmDfPm3K00uDS67nTzLBysjd3ROcXBMFMSmA%2FDe7CIVso%2BPQAe6seT3s889UuencS%2F9%2Fv7ATQ9XTBJXbs%2BcTb90rMi2%2BHh7gdzCumvK8BjqkAe9Lpz2bLQ6boBIur%2FUMh7W7mn6CORgMVb29U2BohZqWg4MmUhWwpPTTbwDRhJ31%2BMq8UetJQSJvJaaifsoeZoYuyYvo6WsvMxS5S0NcSFxrB0Ws5sNhLmtyW7fEbAbfflpkMisWJhLs6OFOVCNr7B2Ot0t9GoKbS3UY2qs3Vcocn%2FltRcqvaAyHUk65Yiw%2Fypm5S3MqRZ6Gr%2FPqUKNqNWHOV03%2B&X-Amz-Signature=35bfa89d86d13c789af1434182577e961e7f982a9ded728743604856d3c85994&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSOH5IY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8taFso1KNyIsd4cL3viW3RUvrkBMjbEj%2F6H3ST2P6SgIhANshsd6lkDZFTKsqn6Z4hGFGGltcL1OyEoQbz40Y4EGAKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwi%2F%2FhvxC1%2B%2Bl6l0BMq3ANxSt8by7WIpsHvR%2F%2Buisw1ws4kKD6tUVTg7C5PirLB0QPnCHHpQdlfJxFCuFhpZie5mCXLRQH1pYvCgpWzcgeIb401rPZ%2B6ONq703D3kilGw%2F7O%2BndnTzIQ6zAedRPYH2z8K%2F2CikZEbxLBTJYVXqeIDS75W5vsQfFEeiyXScqYnwEX2Vah8Eaz1W9NEyv8cPIWitfNmKw82ZDbgNmn6%2FWypOqq2ERssbA1xlM1ShvBg42dMLkgGdAMrkPBS4TRDGlbx1mMMu%2Bl%2B0MxYlM4ykYBUwxUwk1SABBJd2IG7EbqVIOduF%2B4blKBUHtunmtsLzexY5nkkD2cIeTd2ldg1RJUAGtIaYeBDB1YPmSKypXuvKR6aIwtAAsReRmKE3%2FUIx7kg25icovIALT8KIhl4c%2B%2FFY76rH1XaJmsVzGOzsTIMeMDlNUDrwP9PamVohANjXeCvCmDwSda8pxI7x5GFSU6a%2FGr6epBFHtYV64NNHJB8G8ltaZJiiUbNmaHIYwQ7%2FePfRAd24T7MqSekzJOTSc14g2QmDfPm3K00uDS67nTzLBysjd3ROcXBMFMSmA%2FDe7CIVso%2BPQAe6seT3s889UuencS%2F9%2Fv7ATQ9XTBJXbs%2BcTb90rMi2%2BHh7gdzCumvK8BjqkAe9Lpz2bLQ6boBIur%2FUMh7W7mn6CORgMVb29U2BohZqWg4MmUhWwpPTTbwDRhJ31%2BMq8UetJQSJvJaaifsoeZoYuyYvo6WsvMxS5S0NcSFxrB0Ws5sNhLmtyW7fEbAbfflpkMisWJhLs6OFOVCNr7B2Ot0t9GoKbS3UY2qs3Vcocn%2FltRcqvaAyHUk65Yiw%2Fypm5S3MqRZ6Gr%2FPqUKNqNWHOV03%2B&X-Amz-Signature=622faf8df99fb51c3a9f30a8bc207a1628eeaa6f83525814b006562af0ff399a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSOH5IY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8taFso1KNyIsd4cL3viW3RUvrkBMjbEj%2F6H3ST2P6SgIhANshsd6lkDZFTKsqn6Z4hGFGGltcL1OyEoQbz40Y4EGAKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwi%2F%2FhvxC1%2B%2Bl6l0BMq3ANxSt8by7WIpsHvR%2F%2Buisw1ws4kKD6tUVTg7C5PirLB0QPnCHHpQdlfJxFCuFhpZie5mCXLRQH1pYvCgpWzcgeIb401rPZ%2B6ONq703D3kilGw%2F7O%2BndnTzIQ6zAedRPYH2z8K%2F2CikZEbxLBTJYVXqeIDS75W5vsQfFEeiyXScqYnwEX2Vah8Eaz1W9NEyv8cPIWitfNmKw82ZDbgNmn6%2FWypOqq2ERssbA1xlM1ShvBg42dMLkgGdAMrkPBS4TRDGlbx1mMMu%2Bl%2B0MxYlM4ykYBUwxUwk1SABBJd2IG7EbqVIOduF%2B4blKBUHtunmtsLzexY5nkkD2cIeTd2ldg1RJUAGtIaYeBDB1YPmSKypXuvKR6aIwtAAsReRmKE3%2FUIx7kg25icovIALT8KIhl4c%2B%2FFY76rH1XaJmsVzGOzsTIMeMDlNUDrwP9PamVohANjXeCvCmDwSda8pxI7x5GFSU6a%2FGr6epBFHtYV64NNHJB8G8ltaZJiiUbNmaHIYwQ7%2FePfRAd24T7MqSekzJOTSc14g2QmDfPm3K00uDS67nTzLBysjd3ROcXBMFMSmA%2FDe7CIVso%2BPQAe6seT3s889UuencS%2F9%2Fv7ATQ9XTBJXbs%2BcTb90rMi2%2BHh7gdzCumvK8BjqkAe9Lpz2bLQ6boBIur%2FUMh7W7mn6CORgMVb29U2BohZqWg4MmUhWwpPTTbwDRhJ31%2BMq8UetJQSJvJaaifsoeZoYuyYvo6WsvMxS5S0NcSFxrB0Ws5sNhLmtyW7fEbAbfflpkMisWJhLs6OFOVCNr7B2Ot0t9GoKbS3UY2qs3Vcocn%2FltRcqvaAyHUk65Yiw%2Fypm5S3MqRZ6Gr%2FPqUKNqNWHOV03%2B&X-Amz-Signature=2b59846cb4b54449a0d3a1454c6e4d5354078205bb4ca09ad59f9b654fe75979&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSOH5IY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8taFso1KNyIsd4cL3viW3RUvrkBMjbEj%2F6H3ST2P6SgIhANshsd6lkDZFTKsqn6Z4hGFGGltcL1OyEoQbz40Y4EGAKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwi%2F%2FhvxC1%2B%2Bl6l0BMq3ANxSt8by7WIpsHvR%2F%2Buisw1ws4kKD6tUVTg7C5PirLB0QPnCHHpQdlfJxFCuFhpZie5mCXLRQH1pYvCgpWzcgeIb401rPZ%2B6ONq703D3kilGw%2F7O%2BndnTzIQ6zAedRPYH2z8K%2F2CikZEbxLBTJYVXqeIDS75W5vsQfFEeiyXScqYnwEX2Vah8Eaz1W9NEyv8cPIWitfNmKw82ZDbgNmn6%2FWypOqq2ERssbA1xlM1ShvBg42dMLkgGdAMrkPBS4TRDGlbx1mMMu%2Bl%2B0MxYlM4ykYBUwxUwk1SABBJd2IG7EbqVIOduF%2B4blKBUHtunmtsLzexY5nkkD2cIeTd2ldg1RJUAGtIaYeBDB1YPmSKypXuvKR6aIwtAAsReRmKE3%2FUIx7kg25icovIALT8KIhl4c%2B%2FFY76rH1XaJmsVzGOzsTIMeMDlNUDrwP9PamVohANjXeCvCmDwSda8pxI7x5GFSU6a%2FGr6epBFHtYV64NNHJB8G8ltaZJiiUbNmaHIYwQ7%2FePfRAd24T7MqSekzJOTSc14g2QmDfPm3K00uDS67nTzLBysjd3ROcXBMFMSmA%2FDe7CIVso%2BPQAe6seT3s889UuencS%2F9%2Fv7ATQ9XTBJXbs%2BcTb90rMi2%2BHh7gdzCumvK8BjqkAe9Lpz2bLQ6boBIur%2FUMh7W7mn6CORgMVb29U2BohZqWg4MmUhWwpPTTbwDRhJ31%2BMq8UetJQSJvJaaifsoeZoYuyYvo6WsvMxS5S0NcSFxrB0Ws5sNhLmtyW7fEbAbfflpkMisWJhLs6OFOVCNr7B2Ot0t9GoKbS3UY2qs3Vcocn%2FltRcqvaAyHUk65Yiw%2Fypm5S3MqRZ6Gr%2FPqUKNqNWHOV03%2B&X-Amz-Signature=010ce5cf0926a1ab397fa81f4bdc2fc63cff2783687028c4bf64cb434db6bbce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFQMKXFT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDclW7PX0wj%2BVgea2ucgzqmUvjJxIjfvaWMkFyy0lxi9wIhAKkPKEiLgHGaiet7fnkjLJNeuhXc2UqCAE0WHfhCETR%2FKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFjIr7bTPc4puT7Iq3AOK4YYzUwRnRk1%2B4ua52jZ3JS%2BDl89rieheEVxQ2sLjItbCOSSKrDd0tQFdsXTHlQu1NsN5FyMv%2FLtGVPYeNSTWpsjWdYRI%2FxhQMv1Y3fGM96jUY2ki5bnbpVuVYKEy6oyB092oCefjaBwsziB6ptFRvMhfx8dphcM1njmQqGdxOqu7h2m9y5nrPvJzE40AIVcxA%2B16YsOxVshK6jOkgr3KERJCOmoXiyYomLniXf8Z2I9a3ynFs1pHizdqXGwOlnj8pkh%2BprOPEujxy1esw2%2BjZyDZCUJTiCKGZlE8I%2BR83to4xHaSMfBjDcMv925gzoCE5NXdEDEW5kjedvAAvofAo80JkQ%2Bb844gwhJOFuy00Uxxy1Ji9FiutOAHnD%2BuhWNVt4z3pxvBiSuP8cuEoER6wSw23mBWc5YhKtukmWfkEi46MEKR%2FZkm8nmHdxb%2FeDeBHhaeeMaQGqQ9umzLe742aeHzmdDihbK4uslSuYu%2FunHk7vdAYWJ8ysBoj2YvY4kbX2JnPPOPROS5jP42QLxeqd2uLuLgs56d%2FNZa6IL%2F2NTSw7unuvAiO17bIcywV7SARb2ldkL1375fzrSg72NUPjjT9IGBIVoUxR5Xsz84oby%2FEgH6qa%2F%2FyrwCAjDZmvK8BjqkAex%2BVx66hMP5KHZYG9xpx%2BKygs016DP7nbb9W4U%2BsDCFUg%2Fcv6InvG%2BSVES1arfMQCtrJ%2Ffm48ZrSKe3%2F6UmUuBji8CsC0gdlcP8BhPoDikiU%2FOYH%2BuwXoherHvn6Wl%2FbBTGm5ZlRkneZPYph9cYbCk0K2MTfxKXmrxNq49Vz9DUaVC3IAijSUuPuMZxgv%2BwrCrOAAAWa98qfhPPOqfnzAzIfWR%2B&X-Amz-Signature=619ccaf017457bf8f07868aa1edf5be65b367a48f5fb0e6254d85294a5602f11&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFQMKXFT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDclW7PX0wj%2BVgea2ucgzqmUvjJxIjfvaWMkFyy0lxi9wIhAKkPKEiLgHGaiet7fnkjLJNeuhXc2UqCAE0WHfhCETR%2FKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFjIr7bTPc4puT7Iq3AOK4YYzUwRnRk1%2B4ua52jZ3JS%2BDl89rieheEVxQ2sLjItbCOSSKrDd0tQFdsXTHlQu1NsN5FyMv%2FLtGVPYeNSTWpsjWdYRI%2FxhQMv1Y3fGM96jUY2ki5bnbpVuVYKEy6oyB092oCefjaBwsziB6ptFRvMhfx8dphcM1njmQqGdxOqu7h2m9y5nrPvJzE40AIVcxA%2B16YsOxVshK6jOkgr3KERJCOmoXiyYomLniXf8Z2I9a3ynFs1pHizdqXGwOlnj8pkh%2BprOPEujxy1esw2%2BjZyDZCUJTiCKGZlE8I%2BR83to4xHaSMfBjDcMv925gzoCE5NXdEDEW5kjedvAAvofAo80JkQ%2Bb844gwhJOFuy00Uxxy1Ji9FiutOAHnD%2BuhWNVt4z3pxvBiSuP8cuEoER6wSw23mBWc5YhKtukmWfkEi46MEKR%2FZkm8nmHdxb%2FeDeBHhaeeMaQGqQ9umzLe742aeHzmdDihbK4uslSuYu%2FunHk7vdAYWJ8ysBoj2YvY4kbX2JnPPOPROS5jP42QLxeqd2uLuLgs56d%2FNZa6IL%2F2NTSw7unuvAiO17bIcywV7SARb2ldkL1375fzrSg72NUPjjT9IGBIVoUxR5Xsz84oby%2FEgH6qa%2F%2FyrwCAjDZmvK8BjqkAex%2BVx66hMP5KHZYG9xpx%2BKygs016DP7nbb9W4U%2BsDCFUg%2Fcv6InvG%2BSVES1arfMQCtrJ%2Ffm48ZrSKe3%2F6UmUuBji8CsC0gdlcP8BhPoDikiU%2FOYH%2BuwXoherHvn6Wl%2FbBTGm5ZlRkneZPYph9cYbCk0K2MTfxKXmrxNq49Vz9DUaVC3IAijSUuPuMZxgv%2BwrCrOAAAWa98qfhPPOqfnzAzIfWR%2B&X-Amz-Signature=e554dc012e64d3163d7070e753a686680a28e72a583d5b62f565ec7711e7caed&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFQMKXFT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDclW7PX0wj%2BVgea2ucgzqmUvjJxIjfvaWMkFyy0lxi9wIhAKkPKEiLgHGaiet7fnkjLJNeuhXc2UqCAE0WHfhCETR%2FKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFjIr7bTPc4puT7Iq3AOK4YYzUwRnRk1%2B4ua52jZ3JS%2BDl89rieheEVxQ2sLjItbCOSSKrDd0tQFdsXTHlQu1NsN5FyMv%2FLtGVPYeNSTWpsjWdYRI%2FxhQMv1Y3fGM96jUY2ki5bnbpVuVYKEy6oyB092oCefjaBwsziB6ptFRvMhfx8dphcM1njmQqGdxOqu7h2m9y5nrPvJzE40AIVcxA%2B16YsOxVshK6jOkgr3KERJCOmoXiyYomLniXf8Z2I9a3ynFs1pHizdqXGwOlnj8pkh%2BprOPEujxy1esw2%2BjZyDZCUJTiCKGZlE8I%2BR83to4xHaSMfBjDcMv925gzoCE5NXdEDEW5kjedvAAvofAo80JkQ%2Bb844gwhJOFuy00Uxxy1Ji9FiutOAHnD%2BuhWNVt4z3pxvBiSuP8cuEoER6wSw23mBWc5YhKtukmWfkEi46MEKR%2FZkm8nmHdxb%2FeDeBHhaeeMaQGqQ9umzLe742aeHzmdDihbK4uslSuYu%2FunHk7vdAYWJ8ysBoj2YvY4kbX2JnPPOPROS5jP42QLxeqd2uLuLgs56d%2FNZa6IL%2F2NTSw7unuvAiO17bIcywV7SARb2ldkL1375fzrSg72NUPjjT9IGBIVoUxR5Xsz84oby%2FEgH6qa%2F%2FyrwCAjDZmvK8BjqkAex%2BVx66hMP5KHZYG9xpx%2BKygs016DP7nbb9W4U%2BsDCFUg%2Fcv6InvG%2BSVES1arfMQCtrJ%2Ffm48ZrSKe3%2F6UmUuBji8CsC0gdlcP8BhPoDikiU%2FOYH%2BuwXoherHvn6Wl%2FbBTGm5ZlRkneZPYph9cYbCk0K2MTfxKXmrxNq49Vz9DUaVC3IAijSUuPuMZxgv%2BwrCrOAAAWa98qfhPPOqfnzAzIfWR%2B&X-Amz-Signature=6ed90802f6c9b51733d1e50f2ca7d853fa10652eefc72b5b85f451a015b699b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFQMKXFT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDclW7PX0wj%2BVgea2ucgzqmUvjJxIjfvaWMkFyy0lxi9wIhAKkPKEiLgHGaiet7fnkjLJNeuhXc2UqCAE0WHfhCETR%2FKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFjIr7bTPc4puT7Iq3AOK4YYzUwRnRk1%2B4ua52jZ3JS%2BDl89rieheEVxQ2sLjItbCOSSKrDd0tQFdsXTHlQu1NsN5FyMv%2FLtGVPYeNSTWpsjWdYRI%2FxhQMv1Y3fGM96jUY2ki5bnbpVuVYKEy6oyB092oCefjaBwsziB6ptFRvMhfx8dphcM1njmQqGdxOqu7h2m9y5nrPvJzE40AIVcxA%2B16YsOxVshK6jOkgr3KERJCOmoXiyYomLniXf8Z2I9a3ynFs1pHizdqXGwOlnj8pkh%2BprOPEujxy1esw2%2BjZyDZCUJTiCKGZlE8I%2BR83to4xHaSMfBjDcMv925gzoCE5NXdEDEW5kjedvAAvofAo80JkQ%2Bb844gwhJOFuy00Uxxy1Ji9FiutOAHnD%2BuhWNVt4z3pxvBiSuP8cuEoER6wSw23mBWc5YhKtukmWfkEi46MEKR%2FZkm8nmHdxb%2FeDeBHhaeeMaQGqQ9umzLe742aeHzmdDihbK4uslSuYu%2FunHk7vdAYWJ8ysBoj2YvY4kbX2JnPPOPROS5jP42QLxeqd2uLuLgs56d%2FNZa6IL%2F2NTSw7unuvAiO17bIcywV7SARb2ldkL1375fzrSg72NUPjjT9IGBIVoUxR5Xsz84oby%2FEgH6qa%2F%2FyrwCAjDZmvK8BjqkAex%2BVx66hMP5KHZYG9xpx%2BKygs016DP7nbb9W4U%2BsDCFUg%2Fcv6InvG%2BSVES1arfMQCtrJ%2Ffm48ZrSKe3%2F6UmUuBji8CsC0gdlcP8BhPoDikiU%2FOYH%2BuwXoherHvn6Wl%2FbBTGm5ZlRkneZPYph9cYbCk0K2MTfxKXmrxNq49Vz9DUaVC3IAijSUuPuMZxgv%2BwrCrOAAAWa98qfhPPOqfnzAzIfWR%2B&X-Amz-Signature=72fb93667bb8b7ae62b5aebd9c0af739c0da09e56ab944fd5cc3e7c8422225db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFQMKXFT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDclW7PX0wj%2BVgea2ucgzqmUvjJxIjfvaWMkFyy0lxi9wIhAKkPKEiLgHGaiet7fnkjLJNeuhXc2UqCAE0WHfhCETR%2FKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFjIr7bTPc4puT7Iq3AOK4YYzUwRnRk1%2B4ua52jZ3JS%2BDl89rieheEVxQ2sLjItbCOSSKrDd0tQFdsXTHlQu1NsN5FyMv%2FLtGVPYeNSTWpsjWdYRI%2FxhQMv1Y3fGM96jUY2ki5bnbpVuVYKEy6oyB092oCefjaBwsziB6ptFRvMhfx8dphcM1njmQqGdxOqu7h2m9y5nrPvJzE40AIVcxA%2B16YsOxVshK6jOkgr3KERJCOmoXiyYomLniXf8Z2I9a3ynFs1pHizdqXGwOlnj8pkh%2BprOPEujxy1esw2%2BjZyDZCUJTiCKGZlE8I%2BR83to4xHaSMfBjDcMv925gzoCE5NXdEDEW5kjedvAAvofAo80JkQ%2Bb844gwhJOFuy00Uxxy1Ji9FiutOAHnD%2BuhWNVt4z3pxvBiSuP8cuEoER6wSw23mBWc5YhKtukmWfkEi46MEKR%2FZkm8nmHdxb%2FeDeBHhaeeMaQGqQ9umzLe742aeHzmdDihbK4uslSuYu%2FunHk7vdAYWJ8ysBoj2YvY4kbX2JnPPOPROS5jP42QLxeqd2uLuLgs56d%2FNZa6IL%2F2NTSw7unuvAiO17bIcywV7SARb2ldkL1375fzrSg72NUPjjT9IGBIVoUxR5Xsz84oby%2FEgH6qa%2F%2FyrwCAjDZmvK8BjqkAex%2BVx66hMP5KHZYG9xpx%2BKygs016DP7nbb9W4U%2BsDCFUg%2Fcv6InvG%2BSVES1arfMQCtrJ%2Ffm48ZrSKe3%2F6UmUuBji8CsC0gdlcP8BhPoDikiU%2FOYH%2BuwXoherHvn6Wl%2FbBTGm5ZlRkneZPYph9cYbCk0K2MTfxKXmrxNq49Vz9DUaVC3IAijSUuPuMZxgv%2BwrCrOAAAWa98qfhPPOqfnzAzIfWR%2B&X-Amz-Signature=70016424ee218c9ce99f84258327639c79cf476e9d464763de919e8cab52c608&X-Amz-SignedHeaders=host&x-id=GetObject)
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


