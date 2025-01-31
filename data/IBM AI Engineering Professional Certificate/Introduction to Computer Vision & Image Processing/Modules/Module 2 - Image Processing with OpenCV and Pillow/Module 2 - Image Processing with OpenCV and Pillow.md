

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMMSKMKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFMNrCPK9wMpuQy5Pkvrr85XSBBAwu2QP5BwJ1bJHtxOAiEAqBkGWVlZfV1RuhxAnC0D0GZ16%2BcuwqVw91AYRK3Xl%2FEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BjTSvkckzb0VZ99ircA4ntDlD%2BHNBqCc%2FnHZgTtb4ERGO6XOTykyITQ0rhbQs6pGJTxeMvK3JCkvRMRi6M1ENNBOgnqlMGI9ekD9IP16Kiq7Eu5CuJ3VP5EgjW1A3bQws6M5lpDTzzEJhTwk8dmAlKBVNmyCotSYlOq%2BeE7%2BynaeZgIxV6CVU%2BlYTJiqDUyJK8YBAxqMop9Ofy9ks%2B2Vamh%2B9dQ89TJ1zR1neA9vfRyCPjv2cRlgyWBG0x7BHiK%2BUNCV96SUBWWJ09H1ZwLDDUiMjPnNL%2FcmJfs6kY1gP99DktsQAV9vJHvEkbeioFrqI9re5ocQS5EbpfkxEDue57K3nPo4U3WHu22mVdSlZTKHX4YlPO3vHCuX7DsLQ%2FBKU1tzJd7cESQsvaz7XphBVvxWxkITAELgJ8PZhQ1q4tivlQZ4UIrD7wH57IEcClMX6k4DcNBBUOmv2l9b%2BTsEMDInO2WEJUbzy07VkESIHKI9%2Bu3sWU1%2FHt9KWLJR99O3olurq5bTsmB9YpLW%2FLaL2s2z%2BuoCPmNNiMTnqDuaUZVQgoMlv2dlyd9SsL1MXnA%2FHPnnSVBPrDhJy5OsftLMaAuucHV9i5MgIFYkpBk5J4qrvHnNM%2Fp4IvHK4nKML2VE4n4CjqZ6%2BmD43pMJLs87wGOqUBZsMedpZqhpflatwFpkXCywBF%2FhQzUA0RM83FCAR1dXDh6DGFEqEfdB1x2aqhtUJBMOkjGLkGzT0VUEeyvyBtbJPdi6EeKpTL2YTtXAvk15d27jm%2BaIH1cJO2khh%2BgbuJVtpEW%2B9IEGPJibTf9uD%2BBqdEMhvSJcNJk%2B7jm9e7U7eSHckvsi369XZDVwlWjSQ%2B107W7E%2FdG9m6nF24WbbqD4k72UdJ&X-Amz-Signature=d0deb4096de1750b443683944d8430939d239a0edeca888574429b9483b97ed0&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNUU2Q3C%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkFJKK152C8YuaSzDJSUnwJd%2B%2BWwjjNNuhfOpHahdpvAiEA7vgHDXil2atMYUKPeJZJ22M8rkRi77qCyNYJrnJt1bIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2Bq%2BMb8d61jk5a8mSrcA6WedGf9wCmAB5r%2B9qpLq%2Bo7VJENmj%2BifoR%2BW9UE48kH8E4qicgNf%2BI9tSdIMxz4yJ57jsZKCSc4emcjC8T4wrxdNxhKu7fDbuqnpEjlGAWwZWLMkYOQa7rZfu6uXZGJwssvMZH73W%2FVTnNQTJ7uQ1BWxksoaFUePvxSMfpPEa1offUd%2B8L3LH7S25v286aM4vQh%2B5R2GfnhuSDyBgbKpkfpZ4J6ni1fGVm5eJVkgRWnH9FNywp%2FNSm6xvXHQb2llGoE%2BM4oZq2TQLjfsxhWW089SpKH%2BhQkoORVgehso8EP0re18WU0lkXpcv9W699dGwhkcdWLMUvKRyELwf611NU5lll6PghUd4JIeFU9HavWOG0P%2FHx15KJJD%2FMNGi%2B0Kp0yfm69RcbDKp37d6LVfYgy45saOBYwISlDsZnrizTPgKdqPr3rCe2xqIgDY6R%2BCNJ3ifGaD7X%2F2GgSm1Qmyg4IMo8azavb4xTkyGEPEUQRUWkx3%2B9YMiCd9SihtZJHEE6zIxIhdBZDWruMMBuRx75EDdnHL7AcHZSqYYonHZqHb0cNCXacARveEvqYYcyTsxIJY2wZX8a1ergTPVKwhDSUo406UZf%2Bzeg03LyJSBpZp8bbvBcIMIUAzucuMPnq87wGOqUB7OAef8twz9HDQLpWHBsyNaskum4GRvgdCS51%2Bl6vwT7x6BOKTgpUjqnE4Jf8PBMHwbdUpJRlCNui9NxrTgs%2FW8FqbkgyQMJgeTujsY3BaEhOE%2FuzJsvLxq9FN%2FH7QALXQ1c1KkGNBICNOEmKDDEc4Dxe5GOsPVUPxvBf5doiXRnlzpmNSn1mk4Ba6hUfpqyJ5cuAoQpc7hidcaqcjGZpNgt9XKz1&X-Amz-Signature=e773f00757b9b9bab0a6340c0ca610a2e7ed72fbf2feeea40bc85bce745cc665&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNUU2Q3C%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkFJKK152C8YuaSzDJSUnwJd%2B%2BWwjjNNuhfOpHahdpvAiEA7vgHDXil2atMYUKPeJZJ22M8rkRi77qCyNYJrnJt1bIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2Bq%2BMb8d61jk5a8mSrcA6WedGf9wCmAB5r%2B9qpLq%2Bo7VJENmj%2BifoR%2BW9UE48kH8E4qicgNf%2BI9tSdIMxz4yJ57jsZKCSc4emcjC8T4wrxdNxhKu7fDbuqnpEjlGAWwZWLMkYOQa7rZfu6uXZGJwssvMZH73W%2FVTnNQTJ7uQ1BWxksoaFUePvxSMfpPEa1offUd%2B8L3LH7S25v286aM4vQh%2B5R2GfnhuSDyBgbKpkfpZ4J6ni1fGVm5eJVkgRWnH9FNywp%2FNSm6xvXHQb2llGoE%2BM4oZq2TQLjfsxhWW089SpKH%2BhQkoORVgehso8EP0re18WU0lkXpcv9W699dGwhkcdWLMUvKRyELwf611NU5lll6PghUd4JIeFU9HavWOG0P%2FHx15KJJD%2FMNGi%2B0Kp0yfm69RcbDKp37d6LVfYgy45saOBYwISlDsZnrizTPgKdqPr3rCe2xqIgDY6R%2BCNJ3ifGaD7X%2F2GgSm1Qmyg4IMo8azavb4xTkyGEPEUQRUWkx3%2B9YMiCd9SihtZJHEE6zIxIhdBZDWruMMBuRx75EDdnHL7AcHZSqYYonHZqHb0cNCXacARveEvqYYcyTsxIJY2wZX8a1ergTPVKwhDSUo406UZf%2Bzeg03LyJSBpZp8bbvBcIMIUAzucuMPnq87wGOqUB7OAef8twz9HDQLpWHBsyNaskum4GRvgdCS51%2Bl6vwT7x6BOKTgpUjqnE4Jf8PBMHwbdUpJRlCNui9NxrTgs%2FW8FqbkgyQMJgeTujsY3BaEhOE%2FuzJsvLxq9FN%2FH7QALXQ1c1KkGNBICNOEmKDDEc4Dxe5GOsPVUPxvBf5doiXRnlzpmNSn1mk4Ba6hUfpqyJ5cuAoQpc7hidcaqcjGZpNgt9XKz1&X-Amz-Signature=11cca09c58b02b44654e29e6bd98673a64f56c7bc7924e38bff58f0ed70934cf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNUU2Q3C%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkFJKK152C8YuaSzDJSUnwJd%2B%2BWwjjNNuhfOpHahdpvAiEA7vgHDXil2atMYUKPeJZJ22M8rkRi77qCyNYJrnJt1bIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2Bq%2BMb8d61jk5a8mSrcA6WedGf9wCmAB5r%2B9qpLq%2Bo7VJENmj%2BifoR%2BW9UE48kH8E4qicgNf%2BI9tSdIMxz4yJ57jsZKCSc4emcjC8T4wrxdNxhKu7fDbuqnpEjlGAWwZWLMkYOQa7rZfu6uXZGJwssvMZH73W%2FVTnNQTJ7uQ1BWxksoaFUePvxSMfpPEa1offUd%2B8L3LH7S25v286aM4vQh%2B5R2GfnhuSDyBgbKpkfpZ4J6ni1fGVm5eJVkgRWnH9FNywp%2FNSm6xvXHQb2llGoE%2BM4oZq2TQLjfsxhWW089SpKH%2BhQkoORVgehso8EP0re18WU0lkXpcv9W699dGwhkcdWLMUvKRyELwf611NU5lll6PghUd4JIeFU9HavWOG0P%2FHx15KJJD%2FMNGi%2B0Kp0yfm69RcbDKp37d6LVfYgy45saOBYwISlDsZnrizTPgKdqPr3rCe2xqIgDY6R%2BCNJ3ifGaD7X%2F2GgSm1Qmyg4IMo8azavb4xTkyGEPEUQRUWkx3%2B9YMiCd9SihtZJHEE6zIxIhdBZDWruMMBuRx75EDdnHL7AcHZSqYYonHZqHb0cNCXacARveEvqYYcyTsxIJY2wZX8a1ergTPVKwhDSUo406UZf%2Bzeg03LyJSBpZp8bbvBcIMIUAzucuMPnq87wGOqUB7OAef8twz9HDQLpWHBsyNaskum4GRvgdCS51%2Bl6vwT7x6BOKTgpUjqnE4Jf8PBMHwbdUpJRlCNui9NxrTgs%2FW8FqbkgyQMJgeTujsY3BaEhOE%2FuzJsvLxq9FN%2FH7QALXQ1c1KkGNBICNOEmKDDEc4Dxe5GOsPVUPxvBf5doiXRnlzpmNSn1mk4Ba6hUfpqyJ5cuAoQpc7hidcaqcjGZpNgt9XKz1&X-Amz-Signature=078eee4b0e3ad41eb4146e0748e2cc640299cc5a9bf9db73838bfbdd6b1108f1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNUU2Q3C%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkFJKK152C8YuaSzDJSUnwJd%2B%2BWwjjNNuhfOpHahdpvAiEA7vgHDXil2atMYUKPeJZJ22M8rkRi77qCyNYJrnJt1bIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2Bq%2BMb8d61jk5a8mSrcA6WedGf9wCmAB5r%2B9qpLq%2Bo7VJENmj%2BifoR%2BW9UE48kH8E4qicgNf%2BI9tSdIMxz4yJ57jsZKCSc4emcjC8T4wrxdNxhKu7fDbuqnpEjlGAWwZWLMkYOQa7rZfu6uXZGJwssvMZH73W%2FVTnNQTJ7uQ1BWxksoaFUePvxSMfpPEa1offUd%2B8L3LH7S25v286aM4vQh%2B5R2GfnhuSDyBgbKpkfpZ4J6ni1fGVm5eJVkgRWnH9FNywp%2FNSm6xvXHQb2llGoE%2BM4oZq2TQLjfsxhWW089SpKH%2BhQkoORVgehso8EP0re18WU0lkXpcv9W699dGwhkcdWLMUvKRyELwf611NU5lll6PghUd4JIeFU9HavWOG0P%2FHx15KJJD%2FMNGi%2B0Kp0yfm69RcbDKp37d6LVfYgy45saOBYwISlDsZnrizTPgKdqPr3rCe2xqIgDY6R%2BCNJ3ifGaD7X%2F2GgSm1Qmyg4IMo8azavb4xTkyGEPEUQRUWkx3%2B9YMiCd9SihtZJHEE6zIxIhdBZDWruMMBuRx75EDdnHL7AcHZSqYYonHZqHb0cNCXacARveEvqYYcyTsxIJY2wZX8a1ergTPVKwhDSUo406UZf%2Bzeg03LyJSBpZp8bbvBcIMIUAzucuMPnq87wGOqUB7OAef8twz9HDQLpWHBsyNaskum4GRvgdCS51%2Bl6vwT7x6BOKTgpUjqnE4Jf8PBMHwbdUpJRlCNui9NxrTgs%2FW8FqbkgyQMJgeTujsY3BaEhOE%2FuzJsvLxq9FN%2FH7QALXQ1c1KkGNBICNOEmKDDEc4Dxe5GOsPVUPxvBf5doiXRnlzpmNSn1mk4Ba6hUfpqyJ5cuAoQpc7hidcaqcjGZpNgt9XKz1&X-Amz-Signature=e1e8866f2437e422e3d3f3deba066b61a42c2657f3d1f2ca0bbb4fc8467b222b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNUU2Q3C%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkFJKK152C8YuaSzDJSUnwJd%2B%2BWwjjNNuhfOpHahdpvAiEA7vgHDXil2atMYUKPeJZJ22M8rkRi77qCyNYJrnJt1bIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2Bq%2BMb8d61jk5a8mSrcA6WedGf9wCmAB5r%2B9qpLq%2Bo7VJENmj%2BifoR%2BW9UE48kH8E4qicgNf%2BI9tSdIMxz4yJ57jsZKCSc4emcjC8T4wrxdNxhKu7fDbuqnpEjlGAWwZWLMkYOQa7rZfu6uXZGJwssvMZH73W%2FVTnNQTJ7uQ1BWxksoaFUePvxSMfpPEa1offUd%2B8L3LH7S25v286aM4vQh%2B5R2GfnhuSDyBgbKpkfpZ4J6ni1fGVm5eJVkgRWnH9FNywp%2FNSm6xvXHQb2llGoE%2BM4oZq2TQLjfsxhWW089SpKH%2BhQkoORVgehso8EP0re18WU0lkXpcv9W699dGwhkcdWLMUvKRyELwf611NU5lll6PghUd4JIeFU9HavWOG0P%2FHx15KJJD%2FMNGi%2B0Kp0yfm69RcbDKp37d6LVfYgy45saOBYwISlDsZnrizTPgKdqPr3rCe2xqIgDY6R%2BCNJ3ifGaD7X%2F2GgSm1Qmyg4IMo8azavb4xTkyGEPEUQRUWkx3%2B9YMiCd9SihtZJHEE6zIxIhdBZDWruMMBuRx75EDdnHL7AcHZSqYYonHZqHb0cNCXacARveEvqYYcyTsxIJY2wZX8a1ergTPVKwhDSUo406UZf%2Bzeg03LyJSBpZp8bbvBcIMIUAzucuMPnq87wGOqUB7OAef8twz9HDQLpWHBsyNaskum4GRvgdCS51%2Bl6vwT7x6BOKTgpUjqnE4Jf8PBMHwbdUpJRlCNui9NxrTgs%2FW8FqbkgyQMJgeTujsY3BaEhOE%2FuzJsvLxq9FN%2FH7QALXQ1c1KkGNBICNOEmKDDEc4Dxe5GOsPVUPxvBf5doiXRnlzpmNSn1mk4Ba6hUfpqyJ5cuAoQpc7hidcaqcjGZpNgt9XKz1&X-Amz-Signature=75fba9d31679eb0f798d679776af0e8a12ebe41af2b21264e27fa454d0ef99ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMMSKMKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFMNrCPK9wMpuQy5Pkvrr85XSBBAwu2QP5BwJ1bJHtxOAiEAqBkGWVlZfV1RuhxAnC0D0GZ16%2BcuwqVw91AYRK3Xl%2FEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BjTSvkckzb0VZ99ircA4ntDlD%2BHNBqCc%2FnHZgTtb4ERGO6XOTykyITQ0rhbQs6pGJTxeMvK3JCkvRMRi6M1ENNBOgnqlMGI9ekD9IP16Kiq7Eu5CuJ3VP5EgjW1A3bQws6M5lpDTzzEJhTwk8dmAlKBVNmyCotSYlOq%2BeE7%2BynaeZgIxV6CVU%2BlYTJiqDUyJK8YBAxqMop9Ofy9ks%2B2Vamh%2B9dQ89TJ1zR1neA9vfRyCPjv2cRlgyWBG0x7BHiK%2BUNCV96SUBWWJ09H1ZwLDDUiMjPnNL%2FcmJfs6kY1gP99DktsQAV9vJHvEkbeioFrqI9re5ocQS5EbpfkxEDue57K3nPo4U3WHu22mVdSlZTKHX4YlPO3vHCuX7DsLQ%2FBKU1tzJd7cESQsvaz7XphBVvxWxkITAELgJ8PZhQ1q4tivlQZ4UIrD7wH57IEcClMX6k4DcNBBUOmv2l9b%2BTsEMDInO2WEJUbzy07VkESIHKI9%2Bu3sWU1%2FHt9KWLJR99O3olurq5bTsmB9YpLW%2FLaL2s2z%2BuoCPmNNiMTnqDuaUZVQgoMlv2dlyd9SsL1MXnA%2FHPnnSVBPrDhJy5OsftLMaAuucHV9i5MgIFYkpBk5J4qrvHnNM%2Fp4IvHK4nKML2VE4n4CjqZ6%2BmD43pMJLs87wGOqUBZsMedpZqhpflatwFpkXCywBF%2FhQzUA0RM83FCAR1dXDh6DGFEqEfdB1x2aqhtUJBMOkjGLkGzT0VUEeyvyBtbJPdi6EeKpTL2YTtXAvk15d27jm%2BaIH1cJO2khh%2BgbuJVtpEW%2B9IEGPJibTf9uD%2BBqdEMhvSJcNJk%2B7jm9e7U7eSHckvsi369XZDVwlWjSQ%2B107W7E%2FdG9m6nF24WbbqD4k72UdJ&X-Amz-Signature=1f25132225698c1cd2f09fd08810da30c6003e8a8cd0f2abf79195fe1d43f81f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMMSKMKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFMNrCPK9wMpuQy5Pkvrr85XSBBAwu2QP5BwJ1bJHtxOAiEAqBkGWVlZfV1RuhxAnC0D0GZ16%2BcuwqVw91AYRK3Xl%2FEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BjTSvkckzb0VZ99ircA4ntDlD%2BHNBqCc%2FnHZgTtb4ERGO6XOTykyITQ0rhbQs6pGJTxeMvK3JCkvRMRi6M1ENNBOgnqlMGI9ekD9IP16Kiq7Eu5CuJ3VP5EgjW1A3bQws6M5lpDTzzEJhTwk8dmAlKBVNmyCotSYlOq%2BeE7%2BynaeZgIxV6CVU%2BlYTJiqDUyJK8YBAxqMop9Ofy9ks%2B2Vamh%2B9dQ89TJ1zR1neA9vfRyCPjv2cRlgyWBG0x7BHiK%2BUNCV96SUBWWJ09H1ZwLDDUiMjPnNL%2FcmJfs6kY1gP99DktsQAV9vJHvEkbeioFrqI9re5ocQS5EbpfkxEDue57K3nPo4U3WHu22mVdSlZTKHX4YlPO3vHCuX7DsLQ%2FBKU1tzJd7cESQsvaz7XphBVvxWxkITAELgJ8PZhQ1q4tivlQZ4UIrD7wH57IEcClMX6k4DcNBBUOmv2l9b%2BTsEMDInO2WEJUbzy07VkESIHKI9%2Bu3sWU1%2FHt9KWLJR99O3olurq5bTsmB9YpLW%2FLaL2s2z%2BuoCPmNNiMTnqDuaUZVQgoMlv2dlyd9SsL1MXnA%2FHPnnSVBPrDhJy5OsftLMaAuucHV9i5MgIFYkpBk5J4qrvHnNM%2Fp4IvHK4nKML2VE4n4CjqZ6%2BmD43pMJLs87wGOqUBZsMedpZqhpflatwFpkXCywBF%2FhQzUA0RM83FCAR1dXDh6DGFEqEfdB1x2aqhtUJBMOkjGLkGzT0VUEeyvyBtbJPdi6EeKpTL2YTtXAvk15d27jm%2BaIH1cJO2khh%2BgbuJVtpEW%2B9IEGPJibTf9uD%2BBqdEMhvSJcNJk%2B7jm9e7U7eSHckvsi369XZDVwlWjSQ%2B107W7E%2FdG9m6nF24WbbqD4k72UdJ&X-Amz-Signature=6daf60532afc63c7c1bc70d07338639a4066b252a8b5aac17452be0c8db9d4be&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMMSKMKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFMNrCPK9wMpuQy5Pkvrr85XSBBAwu2QP5BwJ1bJHtxOAiEAqBkGWVlZfV1RuhxAnC0D0GZ16%2BcuwqVw91AYRK3Xl%2FEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BjTSvkckzb0VZ99ircA4ntDlD%2BHNBqCc%2FnHZgTtb4ERGO6XOTykyITQ0rhbQs6pGJTxeMvK3JCkvRMRi6M1ENNBOgnqlMGI9ekD9IP16Kiq7Eu5CuJ3VP5EgjW1A3bQws6M5lpDTzzEJhTwk8dmAlKBVNmyCotSYlOq%2BeE7%2BynaeZgIxV6CVU%2BlYTJiqDUyJK8YBAxqMop9Ofy9ks%2B2Vamh%2B9dQ89TJ1zR1neA9vfRyCPjv2cRlgyWBG0x7BHiK%2BUNCV96SUBWWJ09H1ZwLDDUiMjPnNL%2FcmJfs6kY1gP99DktsQAV9vJHvEkbeioFrqI9re5ocQS5EbpfkxEDue57K3nPo4U3WHu22mVdSlZTKHX4YlPO3vHCuX7DsLQ%2FBKU1tzJd7cESQsvaz7XphBVvxWxkITAELgJ8PZhQ1q4tivlQZ4UIrD7wH57IEcClMX6k4DcNBBUOmv2l9b%2BTsEMDInO2WEJUbzy07VkESIHKI9%2Bu3sWU1%2FHt9KWLJR99O3olurq5bTsmB9YpLW%2FLaL2s2z%2BuoCPmNNiMTnqDuaUZVQgoMlv2dlyd9SsL1MXnA%2FHPnnSVBPrDhJy5OsftLMaAuucHV9i5MgIFYkpBk5J4qrvHnNM%2Fp4IvHK4nKML2VE4n4CjqZ6%2BmD43pMJLs87wGOqUBZsMedpZqhpflatwFpkXCywBF%2FhQzUA0RM83FCAR1dXDh6DGFEqEfdB1x2aqhtUJBMOkjGLkGzT0VUEeyvyBtbJPdi6EeKpTL2YTtXAvk15d27jm%2BaIH1cJO2khh%2BgbuJVtpEW%2B9IEGPJibTf9uD%2BBqdEMhvSJcNJk%2B7jm9e7U7eSHckvsi369XZDVwlWjSQ%2B107W7E%2FdG9m6nF24WbbqD4k72UdJ&X-Amz-Signature=9580b0edf8977a2b465b6bb2dabca9ce428a3923cb83896ef90d94a7e8f44550&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMMSKMKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFMNrCPK9wMpuQy5Pkvrr85XSBBAwu2QP5BwJ1bJHtxOAiEAqBkGWVlZfV1RuhxAnC0D0GZ16%2BcuwqVw91AYRK3Xl%2FEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BjTSvkckzb0VZ99ircA4ntDlD%2BHNBqCc%2FnHZgTtb4ERGO6XOTykyITQ0rhbQs6pGJTxeMvK3JCkvRMRi6M1ENNBOgnqlMGI9ekD9IP16Kiq7Eu5CuJ3VP5EgjW1A3bQws6M5lpDTzzEJhTwk8dmAlKBVNmyCotSYlOq%2BeE7%2BynaeZgIxV6CVU%2BlYTJiqDUyJK8YBAxqMop9Ofy9ks%2B2Vamh%2B9dQ89TJ1zR1neA9vfRyCPjv2cRlgyWBG0x7BHiK%2BUNCV96SUBWWJ09H1ZwLDDUiMjPnNL%2FcmJfs6kY1gP99DktsQAV9vJHvEkbeioFrqI9re5ocQS5EbpfkxEDue57K3nPo4U3WHu22mVdSlZTKHX4YlPO3vHCuX7DsLQ%2FBKU1tzJd7cESQsvaz7XphBVvxWxkITAELgJ8PZhQ1q4tivlQZ4UIrD7wH57IEcClMX6k4DcNBBUOmv2l9b%2BTsEMDInO2WEJUbzy07VkESIHKI9%2Bu3sWU1%2FHt9KWLJR99O3olurq5bTsmB9YpLW%2FLaL2s2z%2BuoCPmNNiMTnqDuaUZVQgoMlv2dlyd9SsL1MXnA%2FHPnnSVBPrDhJy5OsftLMaAuucHV9i5MgIFYkpBk5J4qrvHnNM%2Fp4IvHK4nKML2VE4n4CjqZ6%2BmD43pMJLs87wGOqUBZsMedpZqhpflatwFpkXCywBF%2FhQzUA0RM83FCAR1dXDh6DGFEqEfdB1x2aqhtUJBMOkjGLkGzT0VUEeyvyBtbJPdi6EeKpTL2YTtXAvk15d27jm%2BaIH1cJO2khh%2BgbuJVtpEW%2B9IEGPJibTf9uD%2BBqdEMhvSJcNJk%2B7jm9e7U7eSHckvsi369XZDVwlWjSQ%2B107W7E%2FdG9m6nF24WbbqD4k72UdJ&X-Amz-Signature=8826969ca6d44fe5e8e8daff9dae1504a0e3b0963ea83fd55e2c396f79c81623&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMMSKMKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFMNrCPK9wMpuQy5Pkvrr85XSBBAwu2QP5BwJ1bJHtxOAiEAqBkGWVlZfV1RuhxAnC0D0GZ16%2BcuwqVw91AYRK3Xl%2FEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BjTSvkckzb0VZ99ircA4ntDlD%2BHNBqCc%2FnHZgTtb4ERGO6XOTykyITQ0rhbQs6pGJTxeMvK3JCkvRMRi6M1ENNBOgnqlMGI9ekD9IP16Kiq7Eu5CuJ3VP5EgjW1A3bQws6M5lpDTzzEJhTwk8dmAlKBVNmyCotSYlOq%2BeE7%2BynaeZgIxV6CVU%2BlYTJiqDUyJK8YBAxqMop9Ofy9ks%2B2Vamh%2B9dQ89TJ1zR1neA9vfRyCPjv2cRlgyWBG0x7BHiK%2BUNCV96SUBWWJ09H1ZwLDDUiMjPnNL%2FcmJfs6kY1gP99DktsQAV9vJHvEkbeioFrqI9re5ocQS5EbpfkxEDue57K3nPo4U3WHu22mVdSlZTKHX4YlPO3vHCuX7DsLQ%2FBKU1tzJd7cESQsvaz7XphBVvxWxkITAELgJ8PZhQ1q4tivlQZ4UIrD7wH57IEcClMX6k4DcNBBUOmv2l9b%2BTsEMDInO2WEJUbzy07VkESIHKI9%2Bu3sWU1%2FHt9KWLJR99O3olurq5bTsmB9YpLW%2FLaL2s2z%2BuoCPmNNiMTnqDuaUZVQgoMlv2dlyd9SsL1MXnA%2FHPnnSVBPrDhJy5OsftLMaAuucHV9i5MgIFYkpBk5J4qrvHnNM%2Fp4IvHK4nKML2VE4n4CjqZ6%2BmD43pMJLs87wGOqUBZsMedpZqhpflatwFpkXCywBF%2FhQzUA0RM83FCAR1dXDh6DGFEqEfdB1x2aqhtUJBMOkjGLkGzT0VUEeyvyBtbJPdi6EeKpTL2YTtXAvk15d27jm%2BaIH1cJO2khh%2BgbuJVtpEW%2B9IEGPJibTf9uD%2BBqdEMhvSJcNJk%2B7jm9e7U7eSHckvsi369XZDVwlWjSQ%2B107W7E%2FdG9m6nF24WbbqD4k72UdJ&X-Amz-Signature=e293c4c3b5c3c46f51a27258baf0f956ef7466ed0579645b9161ede8e89b6730&X-Amz-SignedHeaders=host&x-id=GetObject)
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


