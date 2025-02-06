

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JUMORZ5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCQCHEVbPKwkytUJ4qLwO6v%2Fz9M%2BOT6SAe6vMKtL6JwygIgcSVg2FAqsVsR49QJYib0rlac0v24h96oV5dquogqYcUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDALVmtl%2BE3CVAeoM9yrcAwnXPRyudOoQeSefKb0IivL7zkOI5IKX5GLa7PZ%2FkCQxf%2BVtTI4adI%2BhwAXshPyuZo0WOnAOVEmHQxTZFXMT9SA0MUE0Q8xUUazjHTYnVJKHWEUxDmswXiiJEhAwsvVA4YW665WYEXJ5NuAqBlhiINABizTC0%2FCXSJOr58NrIB9RbNvfuVCRL6kSyljngJNVAd3JUQSLMNZyoZ09wlUfm6avJxltBNPfvKO2tiYJ14Zj4m1q9LOq0Zb2fZBAZCw7LgGYlh%2Fby1t%2BEodCvqyKcyYIwJ62Jqrl8YDLXIcpC3dKldWwaqmJDOQZjiXy2PbI%2FhYPA6W36Ish%2FQWyCWqOioh7CoZwvCdIS6TKFo1AojFQeyFib0bupcnyeV%2F36AGC9w7djNaAsrNPsHI56st3eIPBIwnIwV9e9TOr8iNxtTA6skJmwBLhPKDeRFYASFBPosAcZkTPLPa1YTtWG5a2Uzcvsly9UYWtatcbJIIfxYfYtbS7lkGJ1zP8K4%2FFHXyfaHCkgYMtHtMF8N2XsBodl3AKMQy86eo9EWg1TAJlYCRDCJNkZEYTvOfAKnO7VaVazxi0cQJDIyxjx3zYY%2FW0eyz6zlQ9nu%2FMNKKlz30oDVjxeSHWqo%2F8BH47ICgyMJvskb0GOqUB8RHHCT4rztt0d2KtX8j%2Bx9sKqs8Z4LIIhuHXf1qYepUaCq7oScAvj%2F7BZwPDVvXDRQ1KiMdSHlzPBuNQnTJMEHsrlKl%2FHN%2FPFDfQQV74KwfYDYmfOQ5BbCNz1gNH6NR44mb2fDMytZfzJpHFiGiligDCpt7e4uk3liD7H%2B3cHxgyeHlmRS15636wqaPSQ26RAU08hUTrKquNtVV7pyFfIIGAWWEz&X-Amz-Signature=277add2edab888caedbf9a382fdbf366c5421a1bdaf8edef6e167339ee8aede2&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R63YPC57%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIFgkCWSTevWe6BoUg7t1khRza%2Fttl1nOf0YyBaUw0HMdAiEA5hjtJ90gASeVKEGZGY1drRjblcGmPw%2FyE7frio35cX8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDNw8AmLUlfbM%2Fl0oLircA38Aq7Ls6Avq8aNxaWhY9wp388ZqcEciCzgv5ii0o7Jof%2BgCRbMmolPO9Flx1EceQS%2BnCML7xUDCksD0h8xZLwrDHiY5SrXgDnj2JVfRF701x6tY2C%2Boyk4Q8m1tfCbXmaKjPs6e77pgN%2BCPheKWhKFBvnzQie29dsp7YnM5ZNLmzQVKfAVQTS%2Fax41mHULjaKWWhaMEy6UXlZqhSQ7RudQQ9Nqyigk0164ha3Pol2JcrR%2BBBnmgEJAsFCmYAlcIBjqAvTIJCs2rnknaFcQnoix1SjFx%2F6Lg3x6hlsslqMNOkpnGzQqL%2FKPk5Xx4tFkugLoj2WH61gmojYrEdvf2FytlEbyM%2FvIg0oqN1ByPAy%2F8BHeRwgSbxisDP4mxLtOWE7itDhvo1IDxUjn8aTWH2%2BMBsTFec6CvzVp4eI0VOJPCzfcc0lPix3jumMxIciakTp2Im8Ts6%2F8N0XBgVsLraSOzuucmiPaT%2FjryAMlSWlF1t%2FZPqOv98X%2FVK6zFAcFbgC2hfWSE%2F2NGq2lVqMd7vOsMk1XlV8NphC%2BC%2FjlnXoQxSa9THuBLO5K0LPTVWVUC88ejAmeyEx9sPyNH3FUaFxwy8d4zasL4dg5DStcdKk8wHzyu5ZTJoAN8NJOYMIHskb0GOqUB77i0h8n0Mevj2y9D1qw1eORzIqc5hfOHvZafjU4E2YjUaYlFIgNfxPriBB5WD3V6E8JPcIJh5e2Xu4aCIDyNuxMZkj9RjvApO6teI5WeevJsj%2BRDSEqfvZ1AJTTJoR%2Fo1IZViFMbTpjwvKh0CnhjcPH6CCNH014yyjpg49DgeM%2FJ8ShF5pLu4%2BNSxkFrY5NFdPiCQmeHdHyt7lvm3PtI%2Bv3nIWK%2B&X-Amz-Signature=5ae7d95a87e6d695de5eb62f7bf467ce8fb870f2edf6af604e896d0f6c19e464&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R63YPC57%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIFgkCWSTevWe6BoUg7t1khRza%2Fttl1nOf0YyBaUw0HMdAiEA5hjtJ90gASeVKEGZGY1drRjblcGmPw%2FyE7frio35cX8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDNw8AmLUlfbM%2Fl0oLircA38Aq7Ls6Avq8aNxaWhY9wp388ZqcEciCzgv5ii0o7Jof%2BgCRbMmolPO9Flx1EceQS%2BnCML7xUDCksD0h8xZLwrDHiY5SrXgDnj2JVfRF701x6tY2C%2Boyk4Q8m1tfCbXmaKjPs6e77pgN%2BCPheKWhKFBvnzQie29dsp7YnM5ZNLmzQVKfAVQTS%2Fax41mHULjaKWWhaMEy6UXlZqhSQ7RudQQ9Nqyigk0164ha3Pol2JcrR%2BBBnmgEJAsFCmYAlcIBjqAvTIJCs2rnknaFcQnoix1SjFx%2F6Lg3x6hlsslqMNOkpnGzQqL%2FKPk5Xx4tFkugLoj2WH61gmojYrEdvf2FytlEbyM%2FvIg0oqN1ByPAy%2F8BHeRwgSbxisDP4mxLtOWE7itDhvo1IDxUjn8aTWH2%2BMBsTFec6CvzVp4eI0VOJPCzfcc0lPix3jumMxIciakTp2Im8Ts6%2F8N0XBgVsLraSOzuucmiPaT%2FjryAMlSWlF1t%2FZPqOv98X%2FVK6zFAcFbgC2hfWSE%2F2NGq2lVqMd7vOsMk1XlV8NphC%2BC%2FjlnXoQxSa9THuBLO5K0LPTVWVUC88ejAmeyEx9sPyNH3FUaFxwy8d4zasL4dg5DStcdKk8wHzyu5ZTJoAN8NJOYMIHskb0GOqUB77i0h8n0Mevj2y9D1qw1eORzIqc5hfOHvZafjU4E2YjUaYlFIgNfxPriBB5WD3V6E8JPcIJh5e2Xu4aCIDyNuxMZkj9RjvApO6teI5WeevJsj%2BRDSEqfvZ1AJTTJoR%2Fo1IZViFMbTpjwvKh0CnhjcPH6CCNH014yyjpg49DgeM%2FJ8ShF5pLu4%2BNSxkFrY5NFdPiCQmeHdHyt7lvm3PtI%2Bv3nIWK%2B&X-Amz-Signature=1644a6cbb8bea2e88bc1bed9e01202fea2b17679396951ffdccac54098a0ebd4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R63YPC57%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIFgkCWSTevWe6BoUg7t1khRza%2Fttl1nOf0YyBaUw0HMdAiEA5hjtJ90gASeVKEGZGY1drRjblcGmPw%2FyE7frio35cX8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDNw8AmLUlfbM%2Fl0oLircA38Aq7Ls6Avq8aNxaWhY9wp388ZqcEciCzgv5ii0o7Jof%2BgCRbMmolPO9Flx1EceQS%2BnCML7xUDCksD0h8xZLwrDHiY5SrXgDnj2JVfRF701x6tY2C%2Boyk4Q8m1tfCbXmaKjPs6e77pgN%2BCPheKWhKFBvnzQie29dsp7YnM5ZNLmzQVKfAVQTS%2Fax41mHULjaKWWhaMEy6UXlZqhSQ7RudQQ9Nqyigk0164ha3Pol2JcrR%2BBBnmgEJAsFCmYAlcIBjqAvTIJCs2rnknaFcQnoix1SjFx%2F6Lg3x6hlsslqMNOkpnGzQqL%2FKPk5Xx4tFkugLoj2WH61gmojYrEdvf2FytlEbyM%2FvIg0oqN1ByPAy%2F8BHeRwgSbxisDP4mxLtOWE7itDhvo1IDxUjn8aTWH2%2BMBsTFec6CvzVp4eI0VOJPCzfcc0lPix3jumMxIciakTp2Im8Ts6%2F8N0XBgVsLraSOzuucmiPaT%2FjryAMlSWlF1t%2FZPqOv98X%2FVK6zFAcFbgC2hfWSE%2F2NGq2lVqMd7vOsMk1XlV8NphC%2BC%2FjlnXoQxSa9THuBLO5K0LPTVWVUC88ejAmeyEx9sPyNH3FUaFxwy8d4zasL4dg5DStcdKk8wHzyu5ZTJoAN8NJOYMIHskb0GOqUB77i0h8n0Mevj2y9D1qw1eORzIqc5hfOHvZafjU4E2YjUaYlFIgNfxPriBB5WD3V6E8JPcIJh5e2Xu4aCIDyNuxMZkj9RjvApO6teI5WeevJsj%2BRDSEqfvZ1AJTTJoR%2Fo1IZViFMbTpjwvKh0CnhjcPH6CCNH014yyjpg49DgeM%2FJ8ShF5pLu4%2BNSxkFrY5NFdPiCQmeHdHyt7lvm3PtI%2Bv3nIWK%2B&X-Amz-Signature=63a9c06636caa7d6f52f7dfaae240f21ccd63d1cbe0839ed9cd841d992daeaa3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R63YPC57%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIFgkCWSTevWe6BoUg7t1khRza%2Fttl1nOf0YyBaUw0HMdAiEA5hjtJ90gASeVKEGZGY1drRjblcGmPw%2FyE7frio35cX8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDNw8AmLUlfbM%2Fl0oLircA38Aq7Ls6Avq8aNxaWhY9wp388ZqcEciCzgv5ii0o7Jof%2BgCRbMmolPO9Flx1EceQS%2BnCML7xUDCksD0h8xZLwrDHiY5SrXgDnj2JVfRF701x6tY2C%2Boyk4Q8m1tfCbXmaKjPs6e77pgN%2BCPheKWhKFBvnzQie29dsp7YnM5ZNLmzQVKfAVQTS%2Fax41mHULjaKWWhaMEy6UXlZqhSQ7RudQQ9Nqyigk0164ha3Pol2JcrR%2BBBnmgEJAsFCmYAlcIBjqAvTIJCs2rnknaFcQnoix1SjFx%2F6Lg3x6hlsslqMNOkpnGzQqL%2FKPk5Xx4tFkugLoj2WH61gmojYrEdvf2FytlEbyM%2FvIg0oqN1ByPAy%2F8BHeRwgSbxisDP4mxLtOWE7itDhvo1IDxUjn8aTWH2%2BMBsTFec6CvzVp4eI0VOJPCzfcc0lPix3jumMxIciakTp2Im8Ts6%2F8N0XBgVsLraSOzuucmiPaT%2FjryAMlSWlF1t%2FZPqOv98X%2FVK6zFAcFbgC2hfWSE%2F2NGq2lVqMd7vOsMk1XlV8NphC%2BC%2FjlnXoQxSa9THuBLO5K0LPTVWVUC88ejAmeyEx9sPyNH3FUaFxwy8d4zasL4dg5DStcdKk8wHzyu5ZTJoAN8NJOYMIHskb0GOqUB77i0h8n0Mevj2y9D1qw1eORzIqc5hfOHvZafjU4E2YjUaYlFIgNfxPriBB5WD3V6E8JPcIJh5e2Xu4aCIDyNuxMZkj9RjvApO6teI5WeevJsj%2BRDSEqfvZ1AJTTJoR%2Fo1IZViFMbTpjwvKh0CnhjcPH6CCNH014yyjpg49DgeM%2FJ8ShF5pLu4%2BNSxkFrY5NFdPiCQmeHdHyt7lvm3PtI%2Bv3nIWK%2B&X-Amz-Signature=5e4dcb7374509e56baf1573edacb5a16a177137091b2fe49efcd5233843a31f9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R63YPC57%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIFgkCWSTevWe6BoUg7t1khRza%2Fttl1nOf0YyBaUw0HMdAiEA5hjtJ90gASeVKEGZGY1drRjblcGmPw%2FyE7frio35cX8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDNw8AmLUlfbM%2Fl0oLircA38Aq7Ls6Avq8aNxaWhY9wp388ZqcEciCzgv5ii0o7Jof%2BgCRbMmolPO9Flx1EceQS%2BnCML7xUDCksD0h8xZLwrDHiY5SrXgDnj2JVfRF701x6tY2C%2Boyk4Q8m1tfCbXmaKjPs6e77pgN%2BCPheKWhKFBvnzQie29dsp7YnM5ZNLmzQVKfAVQTS%2Fax41mHULjaKWWhaMEy6UXlZqhSQ7RudQQ9Nqyigk0164ha3Pol2JcrR%2BBBnmgEJAsFCmYAlcIBjqAvTIJCs2rnknaFcQnoix1SjFx%2F6Lg3x6hlsslqMNOkpnGzQqL%2FKPk5Xx4tFkugLoj2WH61gmojYrEdvf2FytlEbyM%2FvIg0oqN1ByPAy%2F8BHeRwgSbxisDP4mxLtOWE7itDhvo1IDxUjn8aTWH2%2BMBsTFec6CvzVp4eI0VOJPCzfcc0lPix3jumMxIciakTp2Im8Ts6%2F8N0XBgVsLraSOzuucmiPaT%2FjryAMlSWlF1t%2FZPqOv98X%2FVK6zFAcFbgC2hfWSE%2F2NGq2lVqMd7vOsMk1XlV8NphC%2BC%2FjlnXoQxSa9THuBLO5K0LPTVWVUC88ejAmeyEx9sPyNH3FUaFxwy8d4zasL4dg5DStcdKk8wHzyu5ZTJoAN8NJOYMIHskb0GOqUB77i0h8n0Mevj2y9D1qw1eORzIqc5hfOHvZafjU4E2YjUaYlFIgNfxPriBB5WD3V6E8JPcIJh5e2Xu4aCIDyNuxMZkj9RjvApO6teI5WeevJsj%2BRDSEqfvZ1AJTTJoR%2Fo1IZViFMbTpjwvKh0CnhjcPH6CCNH014yyjpg49DgeM%2FJ8ShF5pLu4%2BNSxkFrY5NFdPiCQmeHdHyt7lvm3PtI%2Bv3nIWK%2B&X-Amz-Signature=ad3eaacd7be247b0878a8c4799c126e02b79131084a9d100e1c5f87612cdf1a2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JUMORZ5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCQCHEVbPKwkytUJ4qLwO6v%2Fz9M%2BOT6SAe6vMKtL6JwygIgcSVg2FAqsVsR49QJYib0rlac0v24h96oV5dquogqYcUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDALVmtl%2BE3CVAeoM9yrcAwnXPRyudOoQeSefKb0IivL7zkOI5IKX5GLa7PZ%2FkCQxf%2BVtTI4adI%2BhwAXshPyuZo0WOnAOVEmHQxTZFXMT9SA0MUE0Q8xUUazjHTYnVJKHWEUxDmswXiiJEhAwsvVA4YW665WYEXJ5NuAqBlhiINABizTC0%2FCXSJOr58NrIB9RbNvfuVCRL6kSyljngJNVAd3JUQSLMNZyoZ09wlUfm6avJxltBNPfvKO2tiYJ14Zj4m1q9LOq0Zb2fZBAZCw7LgGYlh%2Fby1t%2BEodCvqyKcyYIwJ62Jqrl8YDLXIcpC3dKldWwaqmJDOQZjiXy2PbI%2FhYPA6W36Ish%2FQWyCWqOioh7CoZwvCdIS6TKFo1AojFQeyFib0bupcnyeV%2F36AGC9w7djNaAsrNPsHI56st3eIPBIwnIwV9e9TOr8iNxtTA6skJmwBLhPKDeRFYASFBPosAcZkTPLPa1YTtWG5a2Uzcvsly9UYWtatcbJIIfxYfYtbS7lkGJ1zP8K4%2FFHXyfaHCkgYMtHtMF8N2XsBodl3AKMQy86eo9EWg1TAJlYCRDCJNkZEYTvOfAKnO7VaVazxi0cQJDIyxjx3zYY%2FW0eyz6zlQ9nu%2FMNKKlz30oDVjxeSHWqo%2F8BH47ICgyMJvskb0GOqUB8RHHCT4rztt0d2KtX8j%2Bx9sKqs8Z4LIIhuHXf1qYepUaCq7oScAvj%2F7BZwPDVvXDRQ1KiMdSHlzPBuNQnTJMEHsrlKl%2FHN%2FPFDfQQV74KwfYDYmfOQ5BbCNz1gNH6NR44mb2fDMytZfzJpHFiGiligDCpt7e4uk3liD7H%2B3cHxgyeHlmRS15636wqaPSQ26RAU08hUTrKquNtVV7pyFfIIGAWWEz&X-Amz-Signature=4070b389dff66ada49f12b62eb4a9825d65682f16355f7dbcba191b4b9d9b748&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JUMORZ5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCQCHEVbPKwkytUJ4qLwO6v%2Fz9M%2BOT6SAe6vMKtL6JwygIgcSVg2FAqsVsR49QJYib0rlac0v24h96oV5dquogqYcUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDALVmtl%2BE3CVAeoM9yrcAwnXPRyudOoQeSefKb0IivL7zkOI5IKX5GLa7PZ%2FkCQxf%2BVtTI4adI%2BhwAXshPyuZo0WOnAOVEmHQxTZFXMT9SA0MUE0Q8xUUazjHTYnVJKHWEUxDmswXiiJEhAwsvVA4YW665WYEXJ5NuAqBlhiINABizTC0%2FCXSJOr58NrIB9RbNvfuVCRL6kSyljngJNVAd3JUQSLMNZyoZ09wlUfm6avJxltBNPfvKO2tiYJ14Zj4m1q9LOq0Zb2fZBAZCw7LgGYlh%2Fby1t%2BEodCvqyKcyYIwJ62Jqrl8YDLXIcpC3dKldWwaqmJDOQZjiXy2PbI%2FhYPA6W36Ish%2FQWyCWqOioh7CoZwvCdIS6TKFo1AojFQeyFib0bupcnyeV%2F36AGC9w7djNaAsrNPsHI56st3eIPBIwnIwV9e9TOr8iNxtTA6skJmwBLhPKDeRFYASFBPosAcZkTPLPa1YTtWG5a2Uzcvsly9UYWtatcbJIIfxYfYtbS7lkGJ1zP8K4%2FFHXyfaHCkgYMtHtMF8N2XsBodl3AKMQy86eo9EWg1TAJlYCRDCJNkZEYTvOfAKnO7VaVazxi0cQJDIyxjx3zYY%2FW0eyz6zlQ9nu%2FMNKKlz30oDVjxeSHWqo%2F8BH47ICgyMJvskb0GOqUB8RHHCT4rztt0d2KtX8j%2Bx9sKqs8Z4LIIhuHXf1qYepUaCq7oScAvj%2F7BZwPDVvXDRQ1KiMdSHlzPBuNQnTJMEHsrlKl%2FHN%2FPFDfQQV74KwfYDYmfOQ5BbCNz1gNH6NR44mb2fDMytZfzJpHFiGiligDCpt7e4uk3liD7H%2B3cHxgyeHlmRS15636wqaPSQ26RAU08hUTrKquNtVV7pyFfIIGAWWEz&X-Amz-Signature=fb36ff631c295269d6264fb1b095dad071c7f8a653b5f1e76f116f71a196dd35&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JUMORZ5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCQCHEVbPKwkytUJ4qLwO6v%2Fz9M%2BOT6SAe6vMKtL6JwygIgcSVg2FAqsVsR49QJYib0rlac0v24h96oV5dquogqYcUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDALVmtl%2BE3CVAeoM9yrcAwnXPRyudOoQeSefKb0IivL7zkOI5IKX5GLa7PZ%2FkCQxf%2BVtTI4adI%2BhwAXshPyuZo0WOnAOVEmHQxTZFXMT9SA0MUE0Q8xUUazjHTYnVJKHWEUxDmswXiiJEhAwsvVA4YW665WYEXJ5NuAqBlhiINABizTC0%2FCXSJOr58NrIB9RbNvfuVCRL6kSyljngJNVAd3JUQSLMNZyoZ09wlUfm6avJxltBNPfvKO2tiYJ14Zj4m1q9LOq0Zb2fZBAZCw7LgGYlh%2Fby1t%2BEodCvqyKcyYIwJ62Jqrl8YDLXIcpC3dKldWwaqmJDOQZjiXy2PbI%2FhYPA6W36Ish%2FQWyCWqOioh7CoZwvCdIS6TKFo1AojFQeyFib0bupcnyeV%2F36AGC9w7djNaAsrNPsHI56st3eIPBIwnIwV9e9TOr8iNxtTA6skJmwBLhPKDeRFYASFBPosAcZkTPLPa1YTtWG5a2Uzcvsly9UYWtatcbJIIfxYfYtbS7lkGJ1zP8K4%2FFHXyfaHCkgYMtHtMF8N2XsBodl3AKMQy86eo9EWg1TAJlYCRDCJNkZEYTvOfAKnO7VaVazxi0cQJDIyxjx3zYY%2FW0eyz6zlQ9nu%2FMNKKlz30oDVjxeSHWqo%2F8BH47ICgyMJvskb0GOqUB8RHHCT4rztt0d2KtX8j%2Bx9sKqs8Z4LIIhuHXf1qYepUaCq7oScAvj%2F7BZwPDVvXDRQ1KiMdSHlzPBuNQnTJMEHsrlKl%2FHN%2FPFDfQQV74KwfYDYmfOQ5BbCNz1gNH6NR44mb2fDMytZfzJpHFiGiligDCpt7e4uk3liD7H%2B3cHxgyeHlmRS15636wqaPSQ26RAU08hUTrKquNtVV7pyFfIIGAWWEz&X-Amz-Signature=e086570922f4a08db40946c0e191306334341d3e88c0d1a7c6f8b5c8ab81c822&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JUMORZ5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCQCHEVbPKwkytUJ4qLwO6v%2Fz9M%2BOT6SAe6vMKtL6JwygIgcSVg2FAqsVsR49QJYib0rlac0v24h96oV5dquogqYcUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDALVmtl%2BE3CVAeoM9yrcAwnXPRyudOoQeSefKb0IivL7zkOI5IKX5GLa7PZ%2FkCQxf%2BVtTI4adI%2BhwAXshPyuZo0WOnAOVEmHQxTZFXMT9SA0MUE0Q8xUUazjHTYnVJKHWEUxDmswXiiJEhAwsvVA4YW665WYEXJ5NuAqBlhiINABizTC0%2FCXSJOr58NrIB9RbNvfuVCRL6kSyljngJNVAd3JUQSLMNZyoZ09wlUfm6avJxltBNPfvKO2tiYJ14Zj4m1q9LOq0Zb2fZBAZCw7LgGYlh%2Fby1t%2BEodCvqyKcyYIwJ62Jqrl8YDLXIcpC3dKldWwaqmJDOQZjiXy2PbI%2FhYPA6W36Ish%2FQWyCWqOioh7CoZwvCdIS6TKFo1AojFQeyFib0bupcnyeV%2F36AGC9w7djNaAsrNPsHI56st3eIPBIwnIwV9e9TOr8iNxtTA6skJmwBLhPKDeRFYASFBPosAcZkTPLPa1YTtWG5a2Uzcvsly9UYWtatcbJIIfxYfYtbS7lkGJ1zP8K4%2FFHXyfaHCkgYMtHtMF8N2XsBodl3AKMQy86eo9EWg1TAJlYCRDCJNkZEYTvOfAKnO7VaVazxi0cQJDIyxjx3zYY%2FW0eyz6zlQ9nu%2FMNKKlz30oDVjxeSHWqo%2F8BH47ICgyMJvskb0GOqUB8RHHCT4rztt0d2KtX8j%2Bx9sKqs8Z4LIIhuHXf1qYepUaCq7oScAvj%2F7BZwPDVvXDRQ1KiMdSHlzPBuNQnTJMEHsrlKl%2FHN%2FPFDfQQV74KwfYDYmfOQ5BbCNz1gNH6NR44mb2fDMytZfzJpHFiGiligDCpt7e4uk3liD7H%2B3cHxgyeHlmRS15636wqaPSQ26RAU08hUTrKquNtVV7pyFfIIGAWWEz&X-Amz-Signature=73255e9b56deabdc8071cd082b4e62ca5c36eaf223c4f9144d54cf52b7e32416&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JUMORZ5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCQCHEVbPKwkytUJ4qLwO6v%2Fz9M%2BOT6SAe6vMKtL6JwygIgcSVg2FAqsVsR49QJYib0rlac0v24h96oV5dquogqYcUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDALVmtl%2BE3CVAeoM9yrcAwnXPRyudOoQeSefKb0IivL7zkOI5IKX5GLa7PZ%2FkCQxf%2BVtTI4adI%2BhwAXshPyuZo0WOnAOVEmHQxTZFXMT9SA0MUE0Q8xUUazjHTYnVJKHWEUxDmswXiiJEhAwsvVA4YW665WYEXJ5NuAqBlhiINABizTC0%2FCXSJOr58NrIB9RbNvfuVCRL6kSyljngJNVAd3JUQSLMNZyoZ09wlUfm6avJxltBNPfvKO2tiYJ14Zj4m1q9LOq0Zb2fZBAZCw7LgGYlh%2Fby1t%2BEodCvqyKcyYIwJ62Jqrl8YDLXIcpC3dKldWwaqmJDOQZjiXy2PbI%2FhYPA6W36Ish%2FQWyCWqOioh7CoZwvCdIS6TKFo1AojFQeyFib0bupcnyeV%2F36AGC9w7djNaAsrNPsHI56st3eIPBIwnIwV9e9TOr8iNxtTA6skJmwBLhPKDeRFYASFBPosAcZkTPLPa1YTtWG5a2Uzcvsly9UYWtatcbJIIfxYfYtbS7lkGJ1zP8K4%2FFHXyfaHCkgYMtHtMF8N2XsBodl3AKMQy86eo9EWg1TAJlYCRDCJNkZEYTvOfAKnO7VaVazxi0cQJDIyxjx3zYY%2FW0eyz6zlQ9nu%2FMNKKlz30oDVjxeSHWqo%2F8BH47ICgyMJvskb0GOqUB8RHHCT4rztt0d2KtX8j%2Bx9sKqs8Z4LIIhuHXf1qYepUaCq7oScAvj%2F7BZwPDVvXDRQ1KiMdSHlzPBuNQnTJMEHsrlKl%2FHN%2FPFDfQQV74KwfYDYmfOQ5BbCNz1gNH6NR44mb2fDMytZfzJpHFiGiligDCpt7e4uk3liD7H%2B3cHxgyeHlmRS15636wqaPSQ26RAU08hUTrKquNtVV7pyFfIIGAWWEz&X-Amz-Signature=12f0fe7b6ae2aa2b83daeb9b37c107c7e478e0bd8b4453f56091a587548baf56&X-Amz-SignedHeaders=host&x-id=GetObject)
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


