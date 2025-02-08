

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCQ3DNQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIF%2BeTv%2Bpy8EIcm%2F8PX6Zdpajz6MfIHgEIsM5YBwZJh%2FGAiAMfP5TZ%2FUVxfGEo%2B%2Badyb38tfCLFFUNArtKg5ufv%2BtLCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMveuo2McPExxmqBaZKtwDgCv9kqJgBiWBHFvypcKwEph6KJ9Emm1zlN4Edhbm42dNwtv3zQcGUJImEa8TTmEgrrbsDwNfPpqGDnFItU5ycrnJbkauCT0C78ke6pZq%2BcbtIgVNorbvVKFx3jnA5QdgCsNvlTDAMRbbHrQsqvccbP1RuiVFo0LVvheGRxD7t%2B04NmRpmCCDfkVF5BnpmjBGHhwXDGUc6LffEHniNiCsnGnRs2Pm2iDBiMS4tbtx%2BVlb%2BtzELyjUCzYWnbz6uMvg0usQ5mMS09lmFEgy7ie80LnkCdHaR4G8TGoUSYNGf7%2FAKEB%2BQH6vBnu%2Fxr2HCTysR2nmplc%2F5%2BENQ%2BMDnKbJe8Hpyl%2B3bGo%2FaUeJ800wEd3GieJLHg9mJdk2Rcw10mfkcWaTrjw0fPCgiPmiU1464JLeCptUtvg01O1M%2FLg2NiWVieT01lQV%2BDpzxTpiKHOjkDTiGbUUmV0615gbv%2Bq70C3jLtuz6iOfR2lmbnWyxcYFdNf6MxlnaVj2xkZ3rO6HWpMdiAGjCJ4DGzyQg8Lyqf7osesnYeNRrd7FkhB2YDtMK6XCWTram7ubfKZTRS7%2FYCWC8YPVsGclX2JXExM32jzFKFpbC96bsLz3DoNKyxxzA0%2F%2BgxnVv%2BR8xAMwooWdvQY6pgF7Bgge4Mt9gm8wyS%2BJOTkyX3381qIX%2BMo8figzOt9dSRRg%2FHgTLrhv4t9QCuCf8qAn3eW75rABmXvg1CeytzUZISH2CrPePbMzYgU9w%2FIEx8rR0AJZgk9TLN0H%2FSdHYATX4iPQxneg4EhgEdSYu67iphBFVOGEnc0LF%2FkI7Pgr0z0Mh%2FvnDXVpxyQziaLxRk2H48Y6MB3MPNAS7dlfk5koNjGo%2FnkB&X-Amz-Signature=455ca109405d371c02cb37619f978b6caa289db346966d310b7654274fa3eb84&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQZPXTQC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLyyWmWc%2BGpOXiV3sw1VDZRh7KiOnw3YWfzUxXHsIuXgIgBMQUyutZoX1OlsZZDdPnQHWdkm4XSea%2BIn0g3089JRcqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsc7cDtZcoNtrllvSrcA%2BtkoR2m2Ka6dIDGjgeIX59esxkCNCJuj7EVadqiA%2BFJb1q8jC9nh9nSDTBVDGUWAHc4tc1SV9RNwf0BKEX8rQjRRAtpUrQOZGwkDzxAoFfStgmfzTjyF2Uh%2BEvLjXLn17QN09ceOscgQXQ5kCeGWLwm2eTGQP%2FrF8Ey%2Bk8gpW7zppMVlJz1lih4WLczJ5bJy4z3U6FS25Zvn1ywXJuc3LdJrK06eIrjiTkDVIs2qx7fapgvXZ1CimW7r7PcfwWct6h%2FeOAh4uMM8YBqwg5zyzkjwyR9RmBjrVH3M%2FWNgURKNyLGkvzEqXccjDY9LsLKA%2B0YHzKEGRoMUdoZY2YA4PsINhk8EpMWeW9aRR2%2B0xtp7AvE6uMEJx6JENR1v4XHjTAMKAaGgrz%2Fr98%2Bq2eakc8TE%2B52j5o3hQta6DwGhqJxSrGfhXskbthwgrnkJVcegj0PAiFj2A%2FME674CtMOywzuv%2B1509hqVQoA15WPGJrxEFfwTA9I5Oy2wpewU1WhmcRmfZPwhA1C%2BAW43FyZavFAfm3ECWlmSqNF5eK%2F6UsHa1Ap9decxuHviHOmzj%2B%2Fs0iVAudWiv%2F4V5NBg%2BF2en7P6bQVlyflqxa%2BQZAhbE%2FXeJU0bx7vuGQc8bV6MLOFnb0GOqUBnxYM8%2BThFj8xaLOn8gpniLZ7k%2FARwxAmud6K%2Btbal0E8z0g2ya0tmV45b%2B1vPVJ8843Yqf5TPMvRXn%2BqJwneyXN5TlwjQ28u2FuMVJNcqH93oIOXUQpQxPsotB2awe9rbYbmt8r3BdyGpalzkwjN7UW1gIVDyNBSexI%2FO40e8NyeOcSdfuAlOm4AbyuJnTaCVxt3cYl5afhMa63%2FKS%2FdC%2FqzqMRj&X-Amz-Signature=268a4e3058311d90e4b5cbb256dfae1cc43932fb477f3efca9a5aae7a4e048be&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQZPXTQC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLyyWmWc%2BGpOXiV3sw1VDZRh7KiOnw3YWfzUxXHsIuXgIgBMQUyutZoX1OlsZZDdPnQHWdkm4XSea%2BIn0g3089JRcqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsc7cDtZcoNtrllvSrcA%2BtkoR2m2Ka6dIDGjgeIX59esxkCNCJuj7EVadqiA%2BFJb1q8jC9nh9nSDTBVDGUWAHc4tc1SV9RNwf0BKEX8rQjRRAtpUrQOZGwkDzxAoFfStgmfzTjyF2Uh%2BEvLjXLn17QN09ceOscgQXQ5kCeGWLwm2eTGQP%2FrF8Ey%2Bk8gpW7zppMVlJz1lih4WLczJ5bJy4z3U6FS25Zvn1ywXJuc3LdJrK06eIrjiTkDVIs2qx7fapgvXZ1CimW7r7PcfwWct6h%2FeOAh4uMM8YBqwg5zyzkjwyR9RmBjrVH3M%2FWNgURKNyLGkvzEqXccjDY9LsLKA%2B0YHzKEGRoMUdoZY2YA4PsINhk8EpMWeW9aRR2%2B0xtp7AvE6uMEJx6JENR1v4XHjTAMKAaGgrz%2Fr98%2Bq2eakc8TE%2B52j5o3hQta6DwGhqJxSrGfhXskbthwgrnkJVcegj0PAiFj2A%2FME674CtMOywzuv%2B1509hqVQoA15WPGJrxEFfwTA9I5Oy2wpewU1WhmcRmfZPwhA1C%2BAW43FyZavFAfm3ECWlmSqNF5eK%2F6UsHa1Ap9decxuHviHOmzj%2B%2Fs0iVAudWiv%2F4V5NBg%2BF2en7P6bQVlyflqxa%2BQZAhbE%2FXeJU0bx7vuGQc8bV6MLOFnb0GOqUBnxYM8%2BThFj8xaLOn8gpniLZ7k%2FARwxAmud6K%2Btbal0E8z0g2ya0tmV45b%2B1vPVJ8843Yqf5TPMvRXn%2BqJwneyXN5TlwjQ28u2FuMVJNcqH93oIOXUQpQxPsotB2awe9rbYbmt8r3BdyGpalzkwjN7UW1gIVDyNBSexI%2FO40e8NyeOcSdfuAlOm4AbyuJnTaCVxt3cYl5afhMa63%2FKS%2FdC%2FqzqMRj&X-Amz-Signature=3bd684255d7b1cc54a54824943735bd62cd54d237b1316878e22074908a9f2a0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQZPXTQC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLyyWmWc%2BGpOXiV3sw1VDZRh7KiOnw3YWfzUxXHsIuXgIgBMQUyutZoX1OlsZZDdPnQHWdkm4XSea%2BIn0g3089JRcqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsc7cDtZcoNtrllvSrcA%2BtkoR2m2Ka6dIDGjgeIX59esxkCNCJuj7EVadqiA%2BFJb1q8jC9nh9nSDTBVDGUWAHc4tc1SV9RNwf0BKEX8rQjRRAtpUrQOZGwkDzxAoFfStgmfzTjyF2Uh%2BEvLjXLn17QN09ceOscgQXQ5kCeGWLwm2eTGQP%2FrF8Ey%2Bk8gpW7zppMVlJz1lih4WLczJ5bJy4z3U6FS25Zvn1ywXJuc3LdJrK06eIrjiTkDVIs2qx7fapgvXZ1CimW7r7PcfwWct6h%2FeOAh4uMM8YBqwg5zyzkjwyR9RmBjrVH3M%2FWNgURKNyLGkvzEqXccjDY9LsLKA%2B0YHzKEGRoMUdoZY2YA4PsINhk8EpMWeW9aRR2%2B0xtp7AvE6uMEJx6JENR1v4XHjTAMKAaGgrz%2Fr98%2Bq2eakc8TE%2B52j5o3hQta6DwGhqJxSrGfhXskbthwgrnkJVcegj0PAiFj2A%2FME674CtMOywzuv%2B1509hqVQoA15WPGJrxEFfwTA9I5Oy2wpewU1WhmcRmfZPwhA1C%2BAW43FyZavFAfm3ECWlmSqNF5eK%2F6UsHa1Ap9decxuHviHOmzj%2B%2Fs0iVAudWiv%2F4V5NBg%2BF2en7P6bQVlyflqxa%2BQZAhbE%2FXeJU0bx7vuGQc8bV6MLOFnb0GOqUBnxYM8%2BThFj8xaLOn8gpniLZ7k%2FARwxAmud6K%2Btbal0E8z0g2ya0tmV45b%2B1vPVJ8843Yqf5TPMvRXn%2BqJwneyXN5TlwjQ28u2FuMVJNcqH93oIOXUQpQxPsotB2awe9rbYbmt8r3BdyGpalzkwjN7UW1gIVDyNBSexI%2FO40e8NyeOcSdfuAlOm4AbyuJnTaCVxt3cYl5afhMa63%2FKS%2FdC%2FqzqMRj&X-Amz-Signature=80c8729736ab3fad63b258c4c7034b106f7fe1d8bc9c03001fa8926a43e81c71&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQZPXTQC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLyyWmWc%2BGpOXiV3sw1VDZRh7KiOnw3YWfzUxXHsIuXgIgBMQUyutZoX1OlsZZDdPnQHWdkm4XSea%2BIn0g3089JRcqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsc7cDtZcoNtrllvSrcA%2BtkoR2m2Ka6dIDGjgeIX59esxkCNCJuj7EVadqiA%2BFJb1q8jC9nh9nSDTBVDGUWAHc4tc1SV9RNwf0BKEX8rQjRRAtpUrQOZGwkDzxAoFfStgmfzTjyF2Uh%2BEvLjXLn17QN09ceOscgQXQ5kCeGWLwm2eTGQP%2FrF8Ey%2Bk8gpW7zppMVlJz1lih4WLczJ5bJy4z3U6FS25Zvn1ywXJuc3LdJrK06eIrjiTkDVIs2qx7fapgvXZ1CimW7r7PcfwWct6h%2FeOAh4uMM8YBqwg5zyzkjwyR9RmBjrVH3M%2FWNgURKNyLGkvzEqXccjDY9LsLKA%2B0YHzKEGRoMUdoZY2YA4PsINhk8EpMWeW9aRR2%2B0xtp7AvE6uMEJx6JENR1v4XHjTAMKAaGgrz%2Fr98%2Bq2eakc8TE%2B52j5o3hQta6DwGhqJxSrGfhXskbthwgrnkJVcegj0PAiFj2A%2FME674CtMOywzuv%2B1509hqVQoA15WPGJrxEFfwTA9I5Oy2wpewU1WhmcRmfZPwhA1C%2BAW43FyZavFAfm3ECWlmSqNF5eK%2F6UsHa1Ap9decxuHviHOmzj%2B%2Fs0iVAudWiv%2F4V5NBg%2BF2en7P6bQVlyflqxa%2BQZAhbE%2FXeJU0bx7vuGQc8bV6MLOFnb0GOqUBnxYM8%2BThFj8xaLOn8gpniLZ7k%2FARwxAmud6K%2Btbal0E8z0g2ya0tmV45b%2B1vPVJ8843Yqf5TPMvRXn%2BqJwneyXN5TlwjQ28u2FuMVJNcqH93oIOXUQpQxPsotB2awe9rbYbmt8r3BdyGpalzkwjN7UW1gIVDyNBSexI%2FO40e8NyeOcSdfuAlOm4AbyuJnTaCVxt3cYl5afhMa63%2FKS%2FdC%2FqzqMRj&X-Amz-Signature=140502be8df43c22fc48d11656e4f4c2c1acd7e3eafae7ae749400c01c9a048b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQZPXTQC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLyyWmWc%2BGpOXiV3sw1VDZRh7KiOnw3YWfzUxXHsIuXgIgBMQUyutZoX1OlsZZDdPnQHWdkm4XSea%2BIn0g3089JRcqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsc7cDtZcoNtrllvSrcA%2BtkoR2m2Ka6dIDGjgeIX59esxkCNCJuj7EVadqiA%2BFJb1q8jC9nh9nSDTBVDGUWAHc4tc1SV9RNwf0BKEX8rQjRRAtpUrQOZGwkDzxAoFfStgmfzTjyF2Uh%2BEvLjXLn17QN09ceOscgQXQ5kCeGWLwm2eTGQP%2FrF8Ey%2Bk8gpW7zppMVlJz1lih4WLczJ5bJy4z3U6FS25Zvn1ywXJuc3LdJrK06eIrjiTkDVIs2qx7fapgvXZ1CimW7r7PcfwWct6h%2FeOAh4uMM8YBqwg5zyzkjwyR9RmBjrVH3M%2FWNgURKNyLGkvzEqXccjDY9LsLKA%2B0YHzKEGRoMUdoZY2YA4PsINhk8EpMWeW9aRR2%2B0xtp7AvE6uMEJx6JENR1v4XHjTAMKAaGgrz%2Fr98%2Bq2eakc8TE%2B52j5o3hQta6DwGhqJxSrGfhXskbthwgrnkJVcegj0PAiFj2A%2FME674CtMOywzuv%2B1509hqVQoA15WPGJrxEFfwTA9I5Oy2wpewU1WhmcRmfZPwhA1C%2BAW43FyZavFAfm3ECWlmSqNF5eK%2F6UsHa1Ap9decxuHviHOmzj%2B%2Fs0iVAudWiv%2F4V5NBg%2BF2en7P6bQVlyflqxa%2BQZAhbE%2FXeJU0bx7vuGQc8bV6MLOFnb0GOqUBnxYM8%2BThFj8xaLOn8gpniLZ7k%2FARwxAmud6K%2Btbal0E8z0g2ya0tmV45b%2B1vPVJ8843Yqf5TPMvRXn%2BqJwneyXN5TlwjQ28u2FuMVJNcqH93oIOXUQpQxPsotB2awe9rbYbmt8r3BdyGpalzkwjN7UW1gIVDyNBSexI%2FO40e8NyeOcSdfuAlOm4AbyuJnTaCVxt3cYl5afhMa63%2FKS%2FdC%2FqzqMRj&X-Amz-Signature=dad472eef1e8c154add774b5907329fa6c56c6c287fd9ad697c22793d7b85081&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCQ3DNQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIF%2BeTv%2Bpy8EIcm%2F8PX6Zdpajz6MfIHgEIsM5YBwZJh%2FGAiAMfP5TZ%2FUVxfGEo%2B%2Badyb38tfCLFFUNArtKg5ufv%2BtLCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMveuo2McPExxmqBaZKtwDgCv9kqJgBiWBHFvypcKwEph6KJ9Emm1zlN4Edhbm42dNwtv3zQcGUJImEa8TTmEgrrbsDwNfPpqGDnFItU5ycrnJbkauCT0C78ke6pZq%2BcbtIgVNorbvVKFx3jnA5QdgCsNvlTDAMRbbHrQsqvccbP1RuiVFo0LVvheGRxD7t%2B04NmRpmCCDfkVF5BnpmjBGHhwXDGUc6LffEHniNiCsnGnRs2Pm2iDBiMS4tbtx%2BVlb%2BtzELyjUCzYWnbz6uMvg0usQ5mMS09lmFEgy7ie80LnkCdHaR4G8TGoUSYNGf7%2FAKEB%2BQH6vBnu%2Fxr2HCTysR2nmplc%2F5%2BENQ%2BMDnKbJe8Hpyl%2B3bGo%2FaUeJ800wEd3GieJLHg9mJdk2Rcw10mfkcWaTrjw0fPCgiPmiU1464JLeCptUtvg01O1M%2FLg2NiWVieT01lQV%2BDpzxTpiKHOjkDTiGbUUmV0615gbv%2Bq70C3jLtuz6iOfR2lmbnWyxcYFdNf6MxlnaVj2xkZ3rO6HWpMdiAGjCJ4DGzyQg8Lyqf7osesnYeNRrd7FkhB2YDtMK6XCWTram7ubfKZTRS7%2FYCWC8YPVsGclX2JXExM32jzFKFpbC96bsLz3DoNKyxxzA0%2F%2BgxnVv%2BR8xAMwooWdvQY6pgF7Bgge4Mt9gm8wyS%2BJOTkyX3381qIX%2BMo8figzOt9dSRRg%2FHgTLrhv4t9QCuCf8qAn3eW75rABmXvg1CeytzUZISH2CrPePbMzYgU9w%2FIEx8rR0AJZgk9TLN0H%2FSdHYATX4iPQxneg4EhgEdSYu67iphBFVOGEnc0LF%2FkI7Pgr0z0Mh%2FvnDXVpxyQziaLxRk2H48Y6MB3MPNAS7dlfk5koNjGo%2FnkB&X-Amz-Signature=cd062d3ccf2ba30d89d9e1c6f846dc3675e068a31d5f71e3f5d2b4318b5212d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCQ3DNQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIF%2BeTv%2Bpy8EIcm%2F8PX6Zdpajz6MfIHgEIsM5YBwZJh%2FGAiAMfP5TZ%2FUVxfGEo%2B%2Badyb38tfCLFFUNArtKg5ufv%2BtLCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMveuo2McPExxmqBaZKtwDgCv9kqJgBiWBHFvypcKwEph6KJ9Emm1zlN4Edhbm42dNwtv3zQcGUJImEa8TTmEgrrbsDwNfPpqGDnFItU5ycrnJbkauCT0C78ke6pZq%2BcbtIgVNorbvVKFx3jnA5QdgCsNvlTDAMRbbHrQsqvccbP1RuiVFo0LVvheGRxD7t%2B04NmRpmCCDfkVF5BnpmjBGHhwXDGUc6LffEHniNiCsnGnRs2Pm2iDBiMS4tbtx%2BVlb%2BtzELyjUCzYWnbz6uMvg0usQ5mMS09lmFEgy7ie80LnkCdHaR4G8TGoUSYNGf7%2FAKEB%2BQH6vBnu%2Fxr2HCTysR2nmplc%2F5%2BENQ%2BMDnKbJe8Hpyl%2B3bGo%2FaUeJ800wEd3GieJLHg9mJdk2Rcw10mfkcWaTrjw0fPCgiPmiU1464JLeCptUtvg01O1M%2FLg2NiWVieT01lQV%2BDpzxTpiKHOjkDTiGbUUmV0615gbv%2Bq70C3jLtuz6iOfR2lmbnWyxcYFdNf6MxlnaVj2xkZ3rO6HWpMdiAGjCJ4DGzyQg8Lyqf7osesnYeNRrd7FkhB2YDtMK6XCWTram7ubfKZTRS7%2FYCWC8YPVsGclX2JXExM32jzFKFpbC96bsLz3DoNKyxxzA0%2F%2BgxnVv%2BR8xAMwooWdvQY6pgF7Bgge4Mt9gm8wyS%2BJOTkyX3381qIX%2BMo8figzOt9dSRRg%2FHgTLrhv4t9QCuCf8qAn3eW75rABmXvg1CeytzUZISH2CrPePbMzYgU9w%2FIEx8rR0AJZgk9TLN0H%2FSdHYATX4iPQxneg4EhgEdSYu67iphBFVOGEnc0LF%2FkI7Pgr0z0Mh%2FvnDXVpxyQziaLxRk2H48Y6MB3MPNAS7dlfk5koNjGo%2FnkB&X-Amz-Signature=05991d648c3bd4b6db5783f1620f775c5f98b2aad743b0be8d810615719f9bda&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCQ3DNQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIF%2BeTv%2Bpy8EIcm%2F8PX6Zdpajz6MfIHgEIsM5YBwZJh%2FGAiAMfP5TZ%2FUVxfGEo%2B%2Badyb38tfCLFFUNArtKg5ufv%2BtLCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMveuo2McPExxmqBaZKtwDgCv9kqJgBiWBHFvypcKwEph6KJ9Emm1zlN4Edhbm42dNwtv3zQcGUJImEa8TTmEgrrbsDwNfPpqGDnFItU5ycrnJbkauCT0C78ke6pZq%2BcbtIgVNorbvVKFx3jnA5QdgCsNvlTDAMRbbHrQsqvccbP1RuiVFo0LVvheGRxD7t%2B04NmRpmCCDfkVF5BnpmjBGHhwXDGUc6LffEHniNiCsnGnRs2Pm2iDBiMS4tbtx%2BVlb%2BtzELyjUCzYWnbz6uMvg0usQ5mMS09lmFEgy7ie80LnkCdHaR4G8TGoUSYNGf7%2FAKEB%2BQH6vBnu%2Fxr2HCTysR2nmplc%2F5%2BENQ%2BMDnKbJe8Hpyl%2B3bGo%2FaUeJ800wEd3GieJLHg9mJdk2Rcw10mfkcWaTrjw0fPCgiPmiU1464JLeCptUtvg01O1M%2FLg2NiWVieT01lQV%2BDpzxTpiKHOjkDTiGbUUmV0615gbv%2Bq70C3jLtuz6iOfR2lmbnWyxcYFdNf6MxlnaVj2xkZ3rO6HWpMdiAGjCJ4DGzyQg8Lyqf7osesnYeNRrd7FkhB2YDtMK6XCWTram7ubfKZTRS7%2FYCWC8YPVsGclX2JXExM32jzFKFpbC96bsLz3DoNKyxxzA0%2F%2BgxnVv%2BR8xAMwooWdvQY6pgF7Bgge4Mt9gm8wyS%2BJOTkyX3381qIX%2BMo8figzOt9dSRRg%2FHgTLrhv4t9QCuCf8qAn3eW75rABmXvg1CeytzUZISH2CrPePbMzYgU9w%2FIEx8rR0AJZgk9TLN0H%2FSdHYATX4iPQxneg4EhgEdSYu67iphBFVOGEnc0LF%2FkI7Pgr0z0Mh%2FvnDXVpxyQziaLxRk2H48Y6MB3MPNAS7dlfk5koNjGo%2FnkB&X-Amz-Signature=84a94655bdfa15136572245b05d6e799b346705afcfb320c2c797424854cb54d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCQ3DNQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIF%2BeTv%2Bpy8EIcm%2F8PX6Zdpajz6MfIHgEIsM5YBwZJh%2FGAiAMfP5TZ%2FUVxfGEo%2B%2Badyb38tfCLFFUNArtKg5ufv%2BtLCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMveuo2McPExxmqBaZKtwDgCv9kqJgBiWBHFvypcKwEph6KJ9Emm1zlN4Edhbm42dNwtv3zQcGUJImEa8TTmEgrrbsDwNfPpqGDnFItU5ycrnJbkauCT0C78ke6pZq%2BcbtIgVNorbvVKFx3jnA5QdgCsNvlTDAMRbbHrQsqvccbP1RuiVFo0LVvheGRxD7t%2B04NmRpmCCDfkVF5BnpmjBGHhwXDGUc6LffEHniNiCsnGnRs2Pm2iDBiMS4tbtx%2BVlb%2BtzELyjUCzYWnbz6uMvg0usQ5mMS09lmFEgy7ie80LnkCdHaR4G8TGoUSYNGf7%2FAKEB%2BQH6vBnu%2Fxr2HCTysR2nmplc%2F5%2BENQ%2BMDnKbJe8Hpyl%2B3bGo%2FaUeJ800wEd3GieJLHg9mJdk2Rcw10mfkcWaTrjw0fPCgiPmiU1464JLeCptUtvg01O1M%2FLg2NiWVieT01lQV%2BDpzxTpiKHOjkDTiGbUUmV0615gbv%2Bq70C3jLtuz6iOfR2lmbnWyxcYFdNf6MxlnaVj2xkZ3rO6HWpMdiAGjCJ4DGzyQg8Lyqf7osesnYeNRrd7FkhB2YDtMK6XCWTram7ubfKZTRS7%2FYCWC8YPVsGclX2JXExM32jzFKFpbC96bsLz3DoNKyxxzA0%2F%2BgxnVv%2BR8xAMwooWdvQY6pgF7Bgge4Mt9gm8wyS%2BJOTkyX3381qIX%2BMo8figzOt9dSRRg%2FHgTLrhv4t9QCuCf8qAn3eW75rABmXvg1CeytzUZISH2CrPePbMzYgU9w%2FIEx8rR0AJZgk9TLN0H%2FSdHYATX4iPQxneg4EhgEdSYu67iphBFVOGEnc0LF%2FkI7Pgr0z0Mh%2FvnDXVpxyQziaLxRk2H48Y6MB3MPNAS7dlfk5koNjGo%2FnkB&X-Amz-Signature=442f4372dd6566533ac0b8ce317c8e3de14cac14ea43bc72e9949163a5adc92d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCQ3DNQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIF%2BeTv%2Bpy8EIcm%2F8PX6Zdpajz6MfIHgEIsM5YBwZJh%2FGAiAMfP5TZ%2FUVxfGEo%2B%2Badyb38tfCLFFUNArtKg5ufv%2BtLCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMveuo2McPExxmqBaZKtwDgCv9kqJgBiWBHFvypcKwEph6KJ9Emm1zlN4Edhbm42dNwtv3zQcGUJImEa8TTmEgrrbsDwNfPpqGDnFItU5ycrnJbkauCT0C78ke6pZq%2BcbtIgVNorbvVKFx3jnA5QdgCsNvlTDAMRbbHrQsqvccbP1RuiVFo0LVvheGRxD7t%2B04NmRpmCCDfkVF5BnpmjBGHhwXDGUc6LffEHniNiCsnGnRs2Pm2iDBiMS4tbtx%2BVlb%2BtzELyjUCzYWnbz6uMvg0usQ5mMS09lmFEgy7ie80LnkCdHaR4G8TGoUSYNGf7%2FAKEB%2BQH6vBnu%2Fxr2HCTysR2nmplc%2F5%2BENQ%2BMDnKbJe8Hpyl%2B3bGo%2FaUeJ800wEd3GieJLHg9mJdk2Rcw10mfkcWaTrjw0fPCgiPmiU1464JLeCptUtvg01O1M%2FLg2NiWVieT01lQV%2BDpzxTpiKHOjkDTiGbUUmV0615gbv%2Bq70C3jLtuz6iOfR2lmbnWyxcYFdNf6MxlnaVj2xkZ3rO6HWpMdiAGjCJ4DGzyQg8Lyqf7osesnYeNRrd7FkhB2YDtMK6XCWTram7ubfKZTRS7%2FYCWC8YPVsGclX2JXExM32jzFKFpbC96bsLz3DoNKyxxzA0%2F%2BgxnVv%2BR8xAMwooWdvQY6pgF7Bgge4Mt9gm8wyS%2BJOTkyX3381qIX%2BMo8figzOt9dSRRg%2FHgTLrhv4t9QCuCf8qAn3eW75rABmXvg1CeytzUZISH2CrPePbMzYgU9w%2FIEx8rR0AJZgk9TLN0H%2FSdHYATX4iPQxneg4EhgEdSYu67iphBFVOGEnc0LF%2FkI7Pgr0z0Mh%2FvnDXVpxyQziaLxRk2H48Y6MB3MPNAS7dlfk5koNjGo%2FnkB&X-Amz-Signature=89efceba7633f6a0c5b53ff1a33d69724af5bb3c0e128dea75a6a99b74770dcc&X-Amz-SignedHeaders=host&x-id=GetObject)
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


