

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653GHUHEI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIDx8gW%2FE3kUXOH7TiYo9mM1kMmteamj4RYKXaXBUD0yJAiAmx9oRAUxnLkCe3iFsGUnjd9qvOTciHAovyId4bDenJSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLw3U4LDfrtHgOyerKtwDtsILfv7STJPFOZ5xrmMe%2BMTvEidyigov5NEFQ1sVZM5qi3qvva2%2FV5PcXDh%2B%2BrOoEfE5%2BXqNQdasYB8qbA5LsquKLpIS%2B3ZSfPUSiY6Ky3u%2Fm1KOl6lLN3d%2BKkdRST2PT%2FVRlt16CGcCnjAKawYpn044IWDeXLVp5%2B2XI1sT7SF8uOisqZ5o%2BbP4jothH3t0R%2FKgqzdmzSyD9KMvAI%2F7J5lfiX0d%2FBhhf539MCrkX2AVdxWvCHVfx8bt%2BawR4yYPnN1nCDOTir92qV%2FqkesBRyc%2FWzfkmQ6Hhm3aa6yWbQvfek0WujTKuOPzJj1NUveKePWlEm6eAnxqOwjli5ztZ84ASXwlof3GJx3UR4WXv0UpEJtCQRIMkJbw4x7v6fNo7hK%2Bl9%2BooFkTfprsEcAw6swTuIu0Ez32E8Ho3tdzpEiqJzdtz%2F2Srw8x6%2BFq%2Fb0H5vQuRD4scKuETOu9QJKLqaujt%2B3WqkGHHHHgDIE3aijzyX0n45vrk2B%2F4ljoq1T7%2FGIdo6rXKdrEzjmoHYd8IQuaAmcTuVCCYJQZbwvxSJrpIecXBg%2FtPORudiVFvgiabanMjVn4dpN97kBikwQSMO%2F9%2FLwRa%2BJJQ8PuRL4NxMsvpMoPXMsLi7ROOcEw15DnvAY6pgGGH%2Fja7b%2BblMve8bjN%2FQ9Ptr4S0nnnXyTLazauhzCUdnwwCNlZ1nP%2Fpjo%2FqQPJU4f7EkHjudIGyPOPVtzOX0ITyvtX6Bq5VLib9x2eixQX6laKqrOZcnuVvmxkB64Q1OxLfUBj9cNq4XXYTwHXLsA0UZBHRZbRTlZKokk518qUAjewiMUNFLwZhEFqUjHB3kWSKwpgOIwPj%2Fn99ErTZ9UqGc6Z4zny&X-Amz-Signature=cddc20bfbee0709bdb8fc8051511d68aac83f0295ed558ea70f571d0dc746c3a&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653NHLVCZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIEiDirPFjE7ZQYQs0b90f6xvy%2FI8R21FecWVExQ4QxXMAiEAs%2Ft%2BH2rxdU9fv30Az4lW0dGj9%2FnZSr15urE7gcJO%2BYQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyIO%2BA7yiEGWXRynSrcAxI9nizf1NmtESB9CIj8%2BpCnY71N3c3NaG5NEks8sDmKXmcdoHZ9ZX%2BuL%2BFdmtZIi0BHLmyZLdJWwax3wqi4pUqe6HMsslJJS4Il6AmNvuS4kOR0usp91ZCEBipvHd0BuO9KfNutz9oCUT9akIZhJfDqA3LLIV4aoFPBNKfYl8YGNIKeht%2BqdevG8H8epKIG8NftEgn%2BGOS9w0R2Fn5qvdxLUro4vIr1zCJngp%2F9Sg6Wq8cDSwtmaPcqX35L3OK5NkUvw30465IciF20VFR2DTVwwBcQ3jDJ1h0u%2BnMU70UOGMrPqZ1csthPHhBFUpJdTo9Sew6xGehAiEgToel6OJUIM9vH2Ioe351LsOlZ6qOWv2TeUgw8MsSIIdTOybRfQoIqs9l4PNQtAjLmHW6J0NZabe4eMrZGMSdiHvw3TZuhC9he0YELco7OkIELSKJAU2pM1qKc2uEZJMyvFzlLSdk1ZlGRCV0Fu1OSMLbq1o5phlgQHjB8JYS9oRy2WIl%2FR8P%2FjwxSwQyjFgCfRco%2FVUbFFDT7y4DQ9p8dfFqRPPFeNvwDclKyGE8MRAQej2bRgXi%2FDXOrJd9zy1P9Lad2q9GcX5Bhbw%2Bep4yHR%2FS4XwsjjO8Bgdpz%2FDp%2BAg%2BMMMaQ57wGOqUBBbTpfJJo9hSxFenhYEs2nyxHIT7Qm7Th6u4mjh3si8an6sJEYcsKUkfgCBgieDYiST1yVHyMaaCh6YyDQWFMMtDYHts6yXPqKwAt%2F7EMRGF7r6MvpyUToQOQL%2FrG%2BqEIokOXPXysiPNRFPSA9tbrV6xJAkndnTSPOfmUMyxjGXqfyRtQIHzz9hSXPyEtkSi0%2B9qC5v8e%2BroG%2FQNdM9PWFPUb%2B3wR&X-Amz-Signature=0c5d39d29dfc39c2c9bad640b6bfd68978dd45c73a64459052bd229e940674d6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653NHLVCZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIEiDirPFjE7ZQYQs0b90f6xvy%2FI8R21FecWVExQ4QxXMAiEAs%2Ft%2BH2rxdU9fv30Az4lW0dGj9%2FnZSr15urE7gcJO%2BYQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyIO%2BA7yiEGWXRynSrcAxI9nizf1NmtESB9CIj8%2BpCnY71N3c3NaG5NEks8sDmKXmcdoHZ9ZX%2BuL%2BFdmtZIi0BHLmyZLdJWwax3wqi4pUqe6HMsslJJS4Il6AmNvuS4kOR0usp91ZCEBipvHd0BuO9KfNutz9oCUT9akIZhJfDqA3LLIV4aoFPBNKfYl8YGNIKeht%2BqdevG8H8epKIG8NftEgn%2BGOS9w0R2Fn5qvdxLUro4vIr1zCJngp%2F9Sg6Wq8cDSwtmaPcqX35L3OK5NkUvw30465IciF20VFR2DTVwwBcQ3jDJ1h0u%2BnMU70UOGMrPqZ1csthPHhBFUpJdTo9Sew6xGehAiEgToel6OJUIM9vH2Ioe351LsOlZ6qOWv2TeUgw8MsSIIdTOybRfQoIqs9l4PNQtAjLmHW6J0NZabe4eMrZGMSdiHvw3TZuhC9he0YELco7OkIELSKJAU2pM1qKc2uEZJMyvFzlLSdk1ZlGRCV0Fu1OSMLbq1o5phlgQHjB8JYS9oRy2WIl%2FR8P%2FjwxSwQyjFgCfRco%2FVUbFFDT7y4DQ9p8dfFqRPPFeNvwDclKyGE8MRAQej2bRgXi%2FDXOrJd9zy1P9Lad2q9GcX5Bhbw%2Bep4yHR%2FS4XwsjjO8Bgdpz%2FDp%2BAg%2BMMMaQ57wGOqUBBbTpfJJo9hSxFenhYEs2nyxHIT7Qm7Th6u4mjh3si8an6sJEYcsKUkfgCBgieDYiST1yVHyMaaCh6YyDQWFMMtDYHts6yXPqKwAt%2F7EMRGF7r6MvpyUToQOQL%2FrG%2BqEIokOXPXysiPNRFPSA9tbrV6xJAkndnTSPOfmUMyxjGXqfyRtQIHzz9hSXPyEtkSi0%2B9qC5v8e%2BroG%2FQNdM9PWFPUb%2B3wR&X-Amz-Signature=1535630786ff8645c23d251586f4506b52f064cd1e5dbf2453a64cc4dd4e1845&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653NHLVCZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIEiDirPFjE7ZQYQs0b90f6xvy%2FI8R21FecWVExQ4QxXMAiEAs%2Ft%2BH2rxdU9fv30Az4lW0dGj9%2FnZSr15urE7gcJO%2BYQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyIO%2BA7yiEGWXRynSrcAxI9nizf1NmtESB9CIj8%2BpCnY71N3c3NaG5NEks8sDmKXmcdoHZ9ZX%2BuL%2BFdmtZIi0BHLmyZLdJWwax3wqi4pUqe6HMsslJJS4Il6AmNvuS4kOR0usp91ZCEBipvHd0BuO9KfNutz9oCUT9akIZhJfDqA3LLIV4aoFPBNKfYl8YGNIKeht%2BqdevG8H8epKIG8NftEgn%2BGOS9w0R2Fn5qvdxLUro4vIr1zCJngp%2F9Sg6Wq8cDSwtmaPcqX35L3OK5NkUvw30465IciF20VFR2DTVwwBcQ3jDJ1h0u%2BnMU70UOGMrPqZ1csthPHhBFUpJdTo9Sew6xGehAiEgToel6OJUIM9vH2Ioe351LsOlZ6qOWv2TeUgw8MsSIIdTOybRfQoIqs9l4PNQtAjLmHW6J0NZabe4eMrZGMSdiHvw3TZuhC9he0YELco7OkIELSKJAU2pM1qKc2uEZJMyvFzlLSdk1ZlGRCV0Fu1OSMLbq1o5phlgQHjB8JYS9oRy2WIl%2FR8P%2FjwxSwQyjFgCfRco%2FVUbFFDT7y4DQ9p8dfFqRPPFeNvwDclKyGE8MRAQej2bRgXi%2FDXOrJd9zy1P9Lad2q9GcX5Bhbw%2Bep4yHR%2FS4XwsjjO8Bgdpz%2FDp%2BAg%2BMMMaQ57wGOqUBBbTpfJJo9hSxFenhYEs2nyxHIT7Qm7Th6u4mjh3si8an6sJEYcsKUkfgCBgieDYiST1yVHyMaaCh6YyDQWFMMtDYHts6yXPqKwAt%2F7EMRGF7r6MvpyUToQOQL%2FrG%2BqEIokOXPXysiPNRFPSA9tbrV6xJAkndnTSPOfmUMyxjGXqfyRtQIHzz9hSXPyEtkSi0%2B9qC5v8e%2BroG%2FQNdM9PWFPUb%2B3wR&X-Amz-Signature=1efdb775ba14038aec362c92e7512ecb4bd50b80515714bc600f7abd41102575&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653NHLVCZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIEiDirPFjE7ZQYQs0b90f6xvy%2FI8R21FecWVExQ4QxXMAiEAs%2Ft%2BH2rxdU9fv30Az4lW0dGj9%2FnZSr15urE7gcJO%2BYQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyIO%2BA7yiEGWXRynSrcAxI9nizf1NmtESB9CIj8%2BpCnY71N3c3NaG5NEks8sDmKXmcdoHZ9ZX%2BuL%2BFdmtZIi0BHLmyZLdJWwax3wqi4pUqe6HMsslJJS4Il6AmNvuS4kOR0usp91ZCEBipvHd0BuO9KfNutz9oCUT9akIZhJfDqA3LLIV4aoFPBNKfYl8YGNIKeht%2BqdevG8H8epKIG8NftEgn%2BGOS9w0R2Fn5qvdxLUro4vIr1zCJngp%2F9Sg6Wq8cDSwtmaPcqX35L3OK5NkUvw30465IciF20VFR2DTVwwBcQ3jDJ1h0u%2BnMU70UOGMrPqZ1csthPHhBFUpJdTo9Sew6xGehAiEgToel6OJUIM9vH2Ioe351LsOlZ6qOWv2TeUgw8MsSIIdTOybRfQoIqs9l4PNQtAjLmHW6J0NZabe4eMrZGMSdiHvw3TZuhC9he0YELco7OkIELSKJAU2pM1qKc2uEZJMyvFzlLSdk1ZlGRCV0Fu1OSMLbq1o5phlgQHjB8JYS9oRy2WIl%2FR8P%2FjwxSwQyjFgCfRco%2FVUbFFDT7y4DQ9p8dfFqRPPFeNvwDclKyGE8MRAQej2bRgXi%2FDXOrJd9zy1P9Lad2q9GcX5Bhbw%2Bep4yHR%2FS4XwsjjO8Bgdpz%2FDp%2BAg%2BMMMaQ57wGOqUBBbTpfJJo9hSxFenhYEs2nyxHIT7Qm7Th6u4mjh3si8an6sJEYcsKUkfgCBgieDYiST1yVHyMaaCh6YyDQWFMMtDYHts6yXPqKwAt%2F7EMRGF7r6MvpyUToQOQL%2FrG%2BqEIokOXPXysiPNRFPSA9tbrV6xJAkndnTSPOfmUMyxjGXqfyRtQIHzz9hSXPyEtkSi0%2B9qC5v8e%2BroG%2FQNdM9PWFPUb%2B3wR&X-Amz-Signature=3a8684c97bf09b5828826c8373ab49a6008bf8e664e2dbbaccc6168afb5d4db5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653NHLVCZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIEiDirPFjE7ZQYQs0b90f6xvy%2FI8R21FecWVExQ4QxXMAiEAs%2Ft%2BH2rxdU9fv30Az4lW0dGj9%2FnZSr15urE7gcJO%2BYQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyIO%2BA7yiEGWXRynSrcAxI9nizf1NmtESB9CIj8%2BpCnY71N3c3NaG5NEks8sDmKXmcdoHZ9ZX%2BuL%2BFdmtZIi0BHLmyZLdJWwax3wqi4pUqe6HMsslJJS4Il6AmNvuS4kOR0usp91ZCEBipvHd0BuO9KfNutz9oCUT9akIZhJfDqA3LLIV4aoFPBNKfYl8YGNIKeht%2BqdevG8H8epKIG8NftEgn%2BGOS9w0R2Fn5qvdxLUro4vIr1zCJngp%2F9Sg6Wq8cDSwtmaPcqX35L3OK5NkUvw30465IciF20VFR2DTVwwBcQ3jDJ1h0u%2BnMU70UOGMrPqZ1csthPHhBFUpJdTo9Sew6xGehAiEgToel6OJUIM9vH2Ioe351LsOlZ6qOWv2TeUgw8MsSIIdTOybRfQoIqs9l4PNQtAjLmHW6J0NZabe4eMrZGMSdiHvw3TZuhC9he0YELco7OkIELSKJAU2pM1qKc2uEZJMyvFzlLSdk1ZlGRCV0Fu1OSMLbq1o5phlgQHjB8JYS9oRy2WIl%2FR8P%2FjwxSwQyjFgCfRco%2FVUbFFDT7y4DQ9p8dfFqRPPFeNvwDclKyGE8MRAQej2bRgXi%2FDXOrJd9zy1P9Lad2q9GcX5Bhbw%2Bep4yHR%2FS4XwsjjO8Bgdpz%2FDp%2BAg%2BMMMaQ57wGOqUBBbTpfJJo9hSxFenhYEs2nyxHIT7Qm7Th6u4mjh3si8an6sJEYcsKUkfgCBgieDYiST1yVHyMaaCh6YyDQWFMMtDYHts6yXPqKwAt%2F7EMRGF7r6MvpyUToQOQL%2FrG%2BqEIokOXPXysiPNRFPSA9tbrV6xJAkndnTSPOfmUMyxjGXqfyRtQIHzz9hSXPyEtkSi0%2B9qC5v8e%2BroG%2FQNdM9PWFPUb%2B3wR&X-Amz-Signature=502bf24f697db3b8a602b781d851f1a0030e6058dc250171ffb7b252d09ee72a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653GHUHEI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIDx8gW%2FE3kUXOH7TiYo9mM1kMmteamj4RYKXaXBUD0yJAiAmx9oRAUxnLkCe3iFsGUnjd9qvOTciHAovyId4bDenJSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLw3U4LDfrtHgOyerKtwDtsILfv7STJPFOZ5xrmMe%2BMTvEidyigov5NEFQ1sVZM5qi3qvva2%2FV5PcXDh%2B%2BrOoEfE5%2BXqNQdasYB8qbA5LsquKLpIS%2B3ZSfPUSiY6Ky3u%2Fm1KOl6lLN3d%2BKkdRST2PT%2FVRlt16CGcCnjAKawYpn044IWDeXLVp5%2B2XI1sT7SF8uOisqZ5o%2BbP4jothH3t0R%2FKgqzdmzSyD9KMvAI%2F7J5lfiX0d%2FBhhf539MCrkX2AVdxWvCHVfx8bt%2BawR4yYPnN1nCDOTir92qV%2FqkesBRyc%2FWzfkmQ6Hhm3aa6yWbQvfek0WujTKuOPzJj1NUveKePWlEm6eAnxqOwjli5ztZ84ASXwlof3GJx3UR4WXv0UpEJtCQRIMkJbw4x7v6fNo7hK%2Bl9%2BooFkTfprsEcAw6swTuIu0Ez32E8Ho3tdzpEiqJzdtz%2F2Srw8x6%2BFq%2Fb0H5vQuRD4scKuETOu9QJKLqaujt%2B3WqkGHHHHgDIE3aijzyX0n45vrk2B%2F4ljoq1T7%2FGIdo6rXKdrEzjmoHYd8IQuaAmcTuVCCYJQZbwvxSJrpIecXBg%2FtPORudiVFvgiabanMjVn4dpN97kBikwQSMO%2F9%2FLwRa%2BJJQ8PuRL4NxMsvpMoPXMsLi7ROOcEw15DnvAY6pgGGH%2Fja7b%2BblMve8bjN%2FQ9Ptr4S0nnnXyTLazauhzCUdnwwCNlZ1nP%2Fpjo%2FqQPJU4f7EkHjudIGyPOPVtzOX0ITyvtX6Bq5VLib9x2eixQX6laKqrOZcnuVvmxkB64Q1OxLfUBj9cNq4XXYTwHXLsA0UZBHRZbRTlZKokk518qUAjewiMUNFLwZhEFqUjHB3kWSKwpgOIwPj%2Fn99ErTZ9UqGc6Z4zny&X-Amz-Signature=5ccd2c2fce0ea24d5d276069d2fc51628c791b170f51f01455b4e00e2f4261c2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653GHUHEI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIDx8gW%2FE3kUXOH7TiYo9mM1kMmteamj4RYKXaXBUD0yJAiAmx9oRAUxnLkCe3iFsGUnjd9qvOTciHAovyId4bDenJSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLw3U4LDfrtHgOyerKtwDtsILfv7STJPFOZ5xrmMe%2BMTvEidyigov5NEFQ1sVZM5qi3qvva2%2FV5PcXDh%2B%2BrOoEfE5%2BXqNQdasYB8qbA5LsquKLpIS%2B3ZSfPUSiY6Ky3u%2Fm1KOl6lLN3d%2BKkdRST2PT%2FVRlt16CGcCnjAKawYpn044IWDeXLVp5%2B2XI1sT7SF8uOisqZ5o%2BbP4jothH3t0R%2FKgqzdmzSyD9KMvAI%2F7J5lfiX0d%2FBhhf539MCrkX2AVdxWvCHVfx8bt%2BawR4yYPnN1nCDOTir92qV%2FqkesBRyc%2FWzfkmQ6Hhm3aa6yWbQvfek0WujTKuOPzJj1NUveKePWlEm6eAnxqOwjli5ztZ84ASXwlof3GJx3UR4WXv0UpEJtCQRIMkJbw4x7v6fNo7hK%2Bl9%2BooFkTfprsEcAw6swTuIu0Ez32E8Ho3tdzpEiqJzdtz%2F2Srw8x6%2BFq%2Fb0H5vQuRD4scKuETOu9QJKLqaujt%2B3WqkGHHHHgDIE3aijzyX0n45vrk2B%2F4ljoq1T7%2FGIdo6rXKdrEzjmoHYd8IQuaAmcTuVCCYJQZbwvxSJrpIecXBg%2FtPORudiVFvgiabanMjVn4dpN97kBikwQSMO%2F9%2FLwRa%2BJJQ8PuRL4NxMsvpMoPXMsLi7ROOcEw15DnvAY6pgGGH%2Fja7b%2BblMve8bjN%2FQ9Ptr4S0nnnXyTLazauhzCUdnwwCNlZ1nP%2Fpjo%2FqQPJU4f7EkHjudIGyPOPVtzOX0ITyvtX6Bq5VLib9x2eixQX6laKqrOZcnuVvmxkB64Q1OxLfUBj9cNq4XXYTwHXLsA0UZBHRZbRTlZKokk518qUAjewiMUNFLwZhEFqUjHB3kWSKwpgOIwPj%2Fn99ErTZ9UqGc6Z4zny&X-Amz-Signature=e7a177c270d81e1cd7cbad931c72cc63b6ecdc16ac1ff20b51b649ec4fecda71&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653GHUHEI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIDx8gW%2FE3kUXOH7TiYo9mM1kMmteamj4RYKXaXBUD0yJAiAmx9oRAUxnLkCe3iFsGUnjd9qvOTciHAovyId4bDenJSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLw3U4LDfrtHgOyerKtwDtsILfv7STJPFOZ5xrmMe%2BMTvEidyigov5NEFQ1sVZM5qi3qvva2%2FV5PcXDh%2B%2BrOoEfE5%2BXqNQdasYB8qbA5LsquKLpIS%2B3ZSfPUSiY6Ky3u%2Fm1KOl6lLN3d%2BKkdRST2PT%2FVRlt16CGcCnjAKawYpn044IWDeXLVp5%2B2XI1sT7SF8uOisqZ5o%2BbP4jothH3t0R%2FKgqzdmzSyD9KMvAI%2F7J5lfiX0d%2FBhhf539MCrkX2AVdxWvCHVfx8bt%2BawR4yYPnN1nCDOTir92qV%2FqkesBRyc%2FWzfkmQ6Hhm3aa6yWbQvfek0WujTKuOPzJj1NUveKePWlEm6eAnxqOwjli5ztZ84ASXwlof3GJx3UR4WXv0UpEJtCQRIMkJbw4x7v6fNo7hK%2Bl9%2BooFkTfprsEcAw6swTuIu0Ez32E8Ho3tdzpEiqJzdtz%2F2Srw8x6%2BFq%2Fb0H5vQuRD4scKuETOu9QJKLqaujt%2B3WqkGHHHHgDIE3aijzyX0n45vrk2B%2F4ljoq1T7%2FGIdo6rXKdrEzjmoHYd8IQuaAmcTuVCCYJQZbwvxSJrpIecXBg%2FtPORudiVFvgiabanMjVn4dpN97kBikwQSMO%2F9%2FLwRa%2BJJQ8PuRL4NxMsvpMoPXMsLi7ROOcEw15DnvAY6pgGGH%2Fja7b%2BblMve8bjN%2FQ9Ptr4S0nnnXyTLazauhzCUdnwwCNlZ1nP%2Fpjo%2FqQPJU4f7EkHjudIGyPOPVtzOX0ITyvtX6Bq5VLib9x2eixQX6laKqrOZcnuVvmxkB64Q1OxLfUBj9cNq4XXYTwHXLsA0UZBHRZbRTlZKokk518qUAjewiMUNFLwZhEFqUjHB3kWSKwpgOIwPj%2Fn99ErTZ9UqGc6Z4zny&X-Amz-Signature=5bb8ffbb2c937a2e78530b6f60175d26935030534e5a3c9a4facc3783560abb1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653GHUHEI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIDx8gW%2FE3kUXOH7TiYo9mM1kMmteamj4RYKXaXBUD0yJAiAmx9oRAUxnLkCe3iFsGUnjd9qvOTciHAovyId4bDenJSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLw3U4LDfrtHgOyerKtwDtsILfv7STJPFOZ5xrmMe%2BMTvEidyigov5NEFQ1sVZM5qi3qvva2%2FV5PcXDh%2B%2BrOoEfE5%2BXqNQdasYB8qbA5LsquKLpIS%2B3ZSfPUSiY6Ky3u%2Fm1KOl6lLN3d%2BKkdRST2PT%2FVRlt16CGcCnjAKawYpn044IWDeXLVp5%2B2XI1sT7SF8uOisqZ5o%2BbP4jothH3t0R%2FKgqzdmzSyD9KMvAI%2F7J5lfiX0d%2FBhhf539MCrkX2AVdxWvCHVfx8bt%2BawR4yYPnN1nCDOTir92qV%2FqkesBRyc%2FWzfkmQ6Hhm3aa6yWbQvfek0WujTKuOPzJj1NUveKePWlEm6eAnxqOwjli5ztZ84ASXwlof3GJx3UR4WXv0UpEJtCQRIMkJbw4x7v6fNo7hK%2Bl9%2BooFkTfprsEcAw6swTuIu0Ez32E8Ho3tdzpEiqJzdtz%2F2Srw8x6%2BFq%2Fb0H5vQuRD4scKuETOu9QJKLqaujt%2B3WqkGHHHHgDIE3aijzyX0n45vrk2B%2F4ljoq1T7%2FGIdo6rXKdrEzjmoHYd8IQuaAmcTuVCCYJQZbwvxSJrpIecXBg%2FtPORudiVFvgiabanMjVn4dpN97kBikwQSMO%2F9%2FLwRa%2BJJQ8PuRL4NxMsvpMoPXMsLi7ROOcEw15DnvAY6pgGGH%2Fja7b%2BblMve8bjN%2FQ9Ptr4S0nnnXyTLazauhzCUdnwwCNlZ1nP%2Fpjo%2FqQPJU4f7EkHjudIGyPOPVtzOX0ITyvtX6Bq5VLib9x2eixQX6laKqrOZcnuVvmxkB64Q1OxLfUBj9cNq4XXYTwHXLsA0UZBHRZbRTlZKokk518qUAjewiMUNFLwZhEFqUjHB3kWSKwpgOIwPj%2Fn99ErTZ9UqGc6Z4zny&X-Amz-Signature=06e59f8a3571e5182dd80d04de4dc1a1b4fba87652485796af6a1f31a53a62ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653GHUHEI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIDx8gW%2FE3kUXOH7TiYo9mM1kMmteamj4RYKXaXBUD0yJAiAmx9oRAUxnLkCe3iFsGUnjd9qvOTciHAovyId4bDenJSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLw3U4LDfrtHgOyerKtwDtsILfv7STJPFOZ5xrmMe%2BMTvEidyigov5NEFQ1sVZM5qi3qvva2%2FV5PcXDh%2B%2BrOoEfE5%2BXqNQdasYB8qbA5LsquKLpIS%2B3ZSfPUSiY6Ky3u%2Fm1KOl6lLN3d%2BKkdRST2PT%2FVRlt16CGcCnjAKawYpn044IWDeXLVp5%2B2XI1sT7SF8uOisqZ5o%2BbP4jothH3t0R%2FKgqzdmzSyD9KMvAI%2F7J5lfiX0d%2FBhhf539MCrkX2AVdxWvCHVfx8bt%2BawR4yYPnN1nCDOTir92qV%2FqkesBRyc%2FWzfkmQ6Hhm3aa6yWbQvfek0WujTKuOPzJj1NUveKePWlEm6eAnxqOwjli5ztZ84ASXwlof3GJx3UR4WXv0UpEJtCQRIMkJbw4x7v6fNo7hK%2Bl9%2BooFkTfprsEcAw6swTuIu0Ez32E8Ho3tdzpEiqJzdtz%2F2Srw8x6%2BFq%2Fb0H5vQuRD4scKuETOu9QJKLqaujt%2B3WqkGHHHHgDIE3aijzyX0n45vrk2B%2F4ljoq1T7%2FGIdo6rXKdrEzjmoHYd8IQuaAmcTuVCCYJQZbwvxSJrpIecXBg%2FtPORudiVFvgiabanMjVn4dpN97kBikwQSMO%2F9%2FLwRa%2BJJQ8PuRL4NxMsvpMoPXMsLi7ROOcEw15DnvAY6pgGGH%2Fja7b%2BblMve8bjN%2FQ9Ptr4S0nnnXyTLazauhzCUdnwwCNlZ1nP%2Fpjo%2FqQPJU4f7EkHjudIGyPOPVtzOX0ITyvtX6Bq5VLib9x2eixQX6laKqrOZcnuVvmxkB64Q1OxLfUBj9cNq4XXYTwHXLsA0UZBHRZbRTlZKokk518qUAjewiMUNFLwZhEFqUjHB3kWSKwpgOIwPj%2Fn99ErTZ9UqGc6Z4zny&X-Amz-Signature=c687ed54fe2bc7a8c2fc4b99de60030e8149fa2bbbe9ef82bd1aac8f9002d6a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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


