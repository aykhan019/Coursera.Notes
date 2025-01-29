

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T74HZTW3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXNBaAOyzSAZe3%2B0Guhc8dMDVXZ7DFOMyPRAgc%2FxbKZAiEA%2FtvUHuuVa1%2BefJrQGE0QVROlOYomADyXKm%2FZm9K7TXMqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMwGcZKaWueGbIMaWSrcA4O3u3GLCHe6De2R1QQFAEyqTQ7HlfYrK3N%2BSWLYKwO%2BVy3lSun7vBkkdiV9kY381YH%2Ffemghl9fOspGrsHFR%2BJa802KKQm8fNkWDUnbF5br08wosAqG55ZR5k9I3by4oXZvBegstrjpO1MHrjObolM1P3%2FLFDou6Yf8LZwkGW4Q%2BP75svkKZkMk%2FBjDWqxZDxthVRmQrk45HXx1ZfSa2pBv%2BP6GabqMy6UOG00N66b5nlQGPgBQDN%2BhUuITzWTTzgQva07ROgrMn0FrXd8nIsc3NF7fcn4YEwzA0NVDZ2RJ1SlnkBOyYJp0UyXSw2nyRHPORiOgEsk8p9YqLZsaiESdNh7AFzlVWg9tWetv95k7a8Vl0ah0YmMyIKoSS%2Bgu3xcFBfhpN4khvDi6ccZLzqLk47mCHp19jott6%2BRPlNKb5vflQMvaPpZHC0soz04x0wN1NLLDkYg92RVGzOEA1H4iALhz%2B0QyFEvmiL5yDJUh4o8NrOr0XUovfcowREiAyRlOAQNuJmDj2%2F%2FI3WHczLsMZa%2FyeUnskOxep1T2JCtd8TBN9TU3TAR6ZMTG5XZNGzFcoawlwA%2B0NzwsWaxjp%2BtwahE91ngu%2BLGzQXnIsePOa0KGXAhWOr4WS7PNMJ7n6LwGOqUBV6dmAYAjbZvqS%2FiFM6c5n3Sb9p5%2Bg4Pgg%2F4SZO7Fy1syfXaftw3wN7kITG6gGKeU7RfUJj2yp3VelOeYxjWVcHEwH1IxoILxgBajKP26pEqt3r1gG8ZU7waZSXqJGzGSrHg5zBCkeV4K%2BMZIM0Gc7IjYUz%2BNpHNOHIIjTfFjp5aTOWjY938aJzCLVfM6g9FB75ZttVui6qtXFPP8068zxTSJVtZH&X-Amz-Signature=011d17a97f5d2ceeb9e4b3226ed68201f9dc5cd5880c08392416109f4e6461d0&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHYTCTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq4XW7pwlYrESJMsdZBGFltTN0twpN979I2EVb%2BvaDTAiBB6Xq1rOsFZW94LsILt8wBITBfbtAeueguLlboOJL49SqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMg63a7ENsb4pLbArLKtwDKkLt8EeEhSof59N5JL4tjo2hhSuPKz%2Bag3aYfwpVdr5vRqimx8efEPhQtQwMIT8nmMEGu1MLSSd8M%2BAhs69p1Wmyjb5Nwr2JWK3hl6D6Tp5NmaDwfJjMOS6TZ331%2BTDFgTyxPsHJScIO%2Bh4Pkz2FSEbB1xImG7WzxsKWN0c2VPoIEzUag%2B99aMKd4wrzHPs3mA1DLvV0Ol3WiWe5qJlhMzvp5zRBd5zQ2P5gHxTERwaojCrKstQn3Y2YYmFsLxke5QcP8YTsB3tvcXWCTQ9lpYQ4iILrgwyvMh9cZovcSswj%2FDtxogBBmkfFgcew9NhEKgSaTdvO4KthRIap9JO3XGPFnhoW%2BjT0mlXph0v6vQDpqEs3NQBajg0TGDgVJADJgKO%2BvGV8q6rbsIqNmNDmpqJvvgRhjPrsl%2BrjR0D2MGoSJBt9Zf4e0%2FD4pxvmJcD7CPC8SOH7YtQOxionquzCahFRo8Vum56trkDOHm3kgtjZq6SPCZCVOSLE7NKNZmqkuh9SImaFS9CsbS%2BEo32PV8Ojo4HnICImb%2Bq6PDmXRBcDBryf28zDoy41ipUkUTh9SdnFCz2ecqoj7btuRNh%2FYGUpQZqP7UimbH7UaEOj6D1BExBMwePpNlVddGYwgefovAY6pgHzY4eLe2tBFg3mx7TCiVrkSP4wvm6sP9jW7HOTI98E8QOn3tKHoWTcLNurQPIzeA4QTDod8dmSw3BM8oPstsy33H%2B0f2YAuA7ZE%2B2rLwlRESEIcVerx1mFbKlOVmkpeYrJhiqJasqDxoMXuqpWNZfSG92RqpT8MPDw1cYLGFtHfJNp1jhCDhzBUYLCdt7qSBczzxjeC%2FvqZeZHpV0cpFsSulB1KKwM&X-Amz-Signature=18cced3a310959fec9211ce7d0d503f55234b682cd923ce3b482ce63869435e9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHYTCTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq4XW7pwlYrESJMsdZBGFltTN0twpN979I2EVb%2BvaDTAiBB6Xq1rOsFZW94LsILt8wBITBfbtAeueguLlboOJL49SqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMg63a7ENsb4pLbArLKtwDKkLt8EeEhSof59N5JL4tjo2hhSuPKz%2Bag3aYfwpVdr5vRqimx8efEPhQtQwMIT8nmMEGu1MLSSd8M%2BAhs69p1Wmyjb5Nwr2JWK3hl6D6Tp5NmaDwfJjMOS6TZ331%2BTDFgTyxPsHJScIO%2Bh4Pkz2FSEbB1xImG7WzxsKWN0c2VPoIEzUag%2B99aMKd4wrzHPs3mA1DLvV0Ol3WiWe5qJlhMzvp5zRBd5zQ2P5gHxTERwaojCrKstQn3Y2YYmFsLxke5QcP8YTsB3tvcXWCTQ9lpYQ4iILrgwyvMh9cZovcSswj%2FDtxogBBmkfFgcew9NhEKgSaTdvO4KthRIap9JO3XGPFnhoW%2BjT0mlXph0v6vQDpqEs3NQBajg0TGDgVJADJgKO%2BvGV8q6rbsIqNmNDmpqJvvgRhjPrsl%2BrjR0D2MGoSJBt9Zf4e0%2FD4pxvmJcD7CPC8SOH7YtQOxionquzCahFRo8Vum56trkDOHm3kgtjZq6SPCZCVOSLE7NKNZmqkuh9SImaFS9CsbS%2BEo32PV8Ojo4HnICImb%2Bq6PDmXRBcDBryf28zDoy41ipUkUTh9SdnFCz2ecqoj7btuRNh%2FYGUpQZqP7UimbH7UaEOj6D1BExBMwePpNlVddGYwgefovAY6pgHzY4eLe2tBFg3mx7TCiVrkSP4wvm6sP9jW7HOTI98E8QOn3tKHoWTcLNurQPIzeA4QTDod8dmSw3BM8oPstsy33H%2B0f2YAuA7ZE%2B2rLwlRESEIcVerx1mFbKlOVmkpeYrJhiqJasqDxoMXuqpWNZfSG92RqpT8MPDw1cYLGFtHfJNp1jhCDhzBUYLCdt7qSBczzxjeC%2FvqZeZHpV0cpFsSulB1KKwM&X-Amz-Signature=764dfdc22f316727989ad902547d644b4586d8599cfafb984704ce7d22bdd34a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHYTCTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq4XW7pwlYrESJMsdZBGFltTN0twpN979I2EVb%2BvaDTAiBB6Xq1rOsFZW94LsILt8wBITBfbtAeueguLlboOJL49SqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMg63a7ENsb4pLbArLKtwDKkLt8EeEhSof59N5JL4tjo2hhSuPKz%2Bag3aYfwpVdr5vRqimx8efEPhQtQwMIT8nmMEGu1MLSSd8M%2BAhs69p1Wmyjb5Nwr2JWK3hl6D6Tp5NmaDwfJjMOS6TZ331%2BTDFgTyxPsHJScIO%2Bh4Pkz2FSEbB1xImG7WzxsKWN0c2VPoIEzUag%2B99aMKd4wrzHPs3mA1DLvV0Ol3WiWe5qJlhMzvp5zRBd5zQ2P5gHxTERwaojCrKstQn3Y2YYmFsLxke5QcP8YTsB3tvcXWCTQ9lpYQ4iILrgwyvMh9cZovcSswj%2FDtxogBBmkfFgcew9NhEKgSaTdvO4KthRIap9JO3XGPFnhoW%2BjT0mlXph0v6vQDpqEs3NQBajg0TGDgVJADJgKO%2BvGV8q6rbsIqNmNDmpqJvvgRhjPrsl%2BrjR0D2MGoSJBt9Zf4e0%2FD4pxvmJcD7CPC8SOH7YtQOxionquzCahFRo8Vum56trkDOHm3kgtjZq6SPCZCVOSLE7NKNZmqkuh9SImaFS9CsbS%2BEo32PV8Ojo4HnICImb%2Bq6PDmXRBcDBryf28zDoy41ipUkUTh9SdnFCz2ecqoj7btuRNh%2FYGUpQZqP7UimbH7UaEOj6D1BExBMwePpNlVddGYwgefovAY6pgHzY4eLe2tBFg3mx7TCiVrkSP4wvm6sP9jW7HOTI98E8QOn3tKHoWTcLNurQPIzeA4QTDod8dmSw3BM8oPstsy33H%2B0f2YAuA7ZE%2B2rLwlRESEIcVerx1mFbKlOVmkpeYrJhiqJasqDxoMXuqpWNZfSG92RqpT8MPDw1cYLGFtHfJNp1jhCDhzBUYLCdt7qSBczzxjeC%2FvqZeZHpV0cpFsSulB1KKwM&X-Amz-Signature=b67d9b42d880d411a3c2574653d099807fb2fb99b85ed81693751d1815665b43&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHYTCTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq4XW7pwlYrESJMsdZBGFltTN0twpN979I2EVb%2BvaDTAiBB6Xq1rOsFZW94LsILt8wBITBfbtAeueguLlboOJL49SqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMg63a7ENsb4pLbArLKtwDKkLt8EeEhSof59N5JL4tjo2hhSuPKz%2Bag3aYfwpVdr5vRqimx8efEPhQtQwMIT8nmMEGu1MLSSd8M%2BAhs69p1Wmyjb5Nwr2JWK3hl6D6Tp5NmaDwfJjMOS6TZ331%2BTDFgTyxPsHJScIO%2Bh4Pkz2FSEbB1xImG7WzxsKWN0c2VPoIEzUag%2B99aMKd4wrzHPs3mA1DLvV0Ol3WiWe5qJlhMzvp5zRBd5zQ2P5gHxTERwaojCrKstQn3Y2YYmFsLxke5QcP8YTsB3tvcXWCTQ9lpYQ4iILrgwyvMh9cZovcSswj%2FDtxogBBmkfFgcew9NhEKgSaTdvO4KthRIap9JO3XGPFnhoW%2BjT0mlXph0v6vQDpqEs3NQBajg0TGDgVJADJgKO%2BvGV8q6rbsIqNmNDmpqJvvgRhjPrsl%2BrjR0D2MGoSJBt9Zf4e0%2FD4pxvmJcD7CPC8SOH7YtQOxionquzCahFRo8Vum56trkDOHm3kgtjZq6SPCZCVOSLE7NKNZmqkuh9SImaFS9CsbS%2BEo32PV8Ojo4HnICImb%2Bq6PDmXRBcDBryf28zDoy41ipUkUTh9SdnFCz2ecqoj7btuRNh%2FYGUpQZqP7UimbH7UaEOj6D1BExBMwePpNlVddGYwgefovAY6pgHzY4eLe2tBFg3mx7TCiVrkSP4wvm6sP9jW7HOTI98E8QOn3tKHoWTcLNurQPIzeA4QTDod8dmSw3BM8oPstsy33H%2B0f2YAuA7ZE%2B2rLwlRESEIcVerx1mFbKlOVmkpeYrJhiqJasqDxoMXuqpWNZfSG92RqpT8MPDw1cYLGFtHfJNp1jhCDhzBUYLCdt7qSBczzxjeC%2FvqZeZHpV0cpFsSulB1KKwM&X-Amz-Signature=23b4de1988644c1b39774b663a5238b2e70b589ea064fb9e4845a8783fc69ae0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BHYTCTL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICq4XW7pwlYrESJMsdZBGFltTN0twpN979I2EVb%2BvaDTAiBB6Xq1rOsFZW94LsILt8wBITBfbtAeueguLlboOJL49SqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMg63a7ENsb4pLbArLKtwDKkLt8EeEhSof59N5JL4tjo2hhSuPKz%2Bag3aYfwpVdr5vRqimx8efEPhQtQwMIT8nmMEGu1MLSSd8M%2BAhs69p1Wmyjb5Nwr2JWK3hl6D6Tp5NmaDwfJjMOS6TZ331%2BTDFgTyxPsHJScIO%2Bh4Pkz2FSEbB1xImG7WzxsKWN0c2VPoIEzUag%2B99aMKd4wrzHPs3mA1DLvV0Ol3WiWe5qJlhMzvp5zRBd5zQ2P5gHxTERwaojCrKstQn3Y2YYmFsLxke5QcP8YTsB3tvcXWCTQ9lpYQ4iILrgwyvMh9cZovcSswj%2FDtxogBBmkfFgcew9NhEKgSaTdvO4KthRIap9JO3XGPFnhoW%2BjT0mlXph0v6vQDpqEs3NQBajg0TGDgVJADJgKO%2BvGV8q6rbsIqNmNDmpqJvvgRhjPrsl%2BrjR0D2MGoSJBt9Zf4e0%2FD4pxvmJcD7CPC8SOH7YtQOxionquzCahFRo8Vum56trkDOHm3kgtjZq6SPCZCVOSLE7NKNZmqkuh9SImaFS9CsbS%2BEo32PV8Ojo4HnICImb%2Bq6PDmXRBcDBryf28zDoy41ipUkUTh9SdnFCz2ecqoj7btuRNh%2FYGUpQZqP7UimbH7UaEOj6D1BExBMwePpNlVddGYwgefovAY6pgHzY4eLe2tBFg3mx7TCiVrkSP4wvm6sP9jW7HOTI98E8QOn3tKHoWTcLNurQPIzeA4QTDod8dmSw3BM8oPstsy33H%2B0f2YAuA7ZE%2B2rLwlRESEIcVerx1mFbKlOVmkpeYrJhiqJasqDxoMXuqpWNZfSG92RqpT8MPDw1cYLGFtHfJNp1jhCDhzBUYLCdt7qSBczzxjeC%2FvqZeZHpV0cpFsSulB1KKwM&X-Amz-Signature=c6caf826a72a456096913d33f64d90c68dfae9423840a63a33ab7b65bce2b1eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T74HZTW3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXNBaAOyzSAZe3%2B0Guhc8dMDVXZ7DFOMyPRAgc%2FxbKZAiEA%2FtvUHuuVa1%2BefJrQGE0QVROlOYomADyXKm%2FZm9K7TXMqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMwGcZKaWueGbIMaWSrcA4O3u3GLCHe6De2R1QQFAEyqTQ7HlfYrK3N%2BSWLYKwO%2BVy3lSun7vBkkdiV9kY381YH%2Ffemghl9fOspGrsHFR%2BJa802KKQm8fNkWDUnbF5br08wosAqG55ZR5k9I3by4oXZvBegstrjpO1MHrjObolM1P3%2FLFDou6Yf8LZwkGW4Q%2BP75svkKZkMk%2FBjDWqxZDxthVRmQrk45HXx1ZfSa2pBv%2BP6GabqMy6UOG00N66b5nlQGPgBQDN%2BhUuITzWTTzgQva07ROgrMn0FrXd8nIsc3NF7fcn4YEwzA0NVDZ2RJ1SlnkBOyYJp0UyXSw2nyRHPORiOgEsk8p9YqLZsaiESdNh7AFzlVWg9tWetv95k7a8Vl0ah0YmMyIKoSS%2Bgu3xcFBfhpN4khvDi6ccZLzqLk47mCHp19jott6%2BRPlNKb5vflQMvaPpZHC0soz04x0wN1NLLDkYg92RVGzOEA1H4iALhz%2B0QyFEvmiL5yDJUh4o8NrOr0XUovfcowREiAyRlOAQNuJmDj2%2F%2FI3WHczLsMZa%2FyeUnskOxep1T2JCtd8TBN9TU3TAR6ZMTG5XZNGzFcoawlwA%2B0NzwsWaxjp%2BtwahE91ngu%2BLGzQXnIsePOa0KGXAhWOr4WS7PNMJ7n6LwGOqUBV6dmAYAjbZvqS%2FiFM6c5n3Sb9p5%2Bg4Pgg%2F4SZO7Fy1syfXaftw3wN7kITG6gGKeU7RfUJj2yp3VelOeYxjWVcHEwH1IxoILxgBajKP26pEqt3r1gG8ZU7waZSXqJGzGSrHg5zBCkeV4K%2BMZIM0Gc7IjYUz%2BNpHNOHIIjTfFjp5aTOWjY938aJzCLVfM6g9FB75ZttVui6qtXFPP8068zxTSJVtZH&X-Amz-Signature=cec2da3c25c201e0812944c912b4716d77990e0fa9019cc8bad4df42bf81f522&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T74HZTW3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXNBaAOyzSAZe3%2B0Guhc8dMDVXZ7DFOMyPRAgc%2FxbKZAiEA%2FtvUHuuVa1%2BefJrQGE0QVROlOYomADyXKm%2FZm9K7TXMqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMwGcZKaWueGbIMaWSrcA4O3u3GLCHe6De2R1QQFAEyqTQ7HlfYrK3N%2BSWLYKwO%2BVy3lSun7vBkkdiV9kY381YH%2Ffemghl9fOspGrsHFR%2BJa802KKQm8fNkWDUnbF5br08wosAqG55ZR5k9I3by4oXZvBegstrjpO1MHrjObolM1P3%2FLFDou6Yf8LZwkGW4Q%2BP75svkKZkMk%2FBjDWqxZDxthVRmQrk45HXx1ZfSa2pBv%2BP6GabqMy6UOG00N66b5nlQGPgBQDN%2BhUuITzWTTzgQva07ROgrMn0FrXd8nIsc3NF7fcn4YEwzA0NVDZ2RJ1SlnkBOyYJp0UyXSw2nyRHPORiOgEsk8p9YqLZsaiESdNh7AFzlVWg9tWetv95k7a8Vl0ah0YmMyIKoSS%2Bgu3xcFBfhpN4khvDi6ccZLzqLk47mCHp19jott6%2BRPlNKb5vflQMvaPpZHC0soz04x0wN1NLLDkYg92RVGzOEA1H4iALhz%2B0QyFEvmiL5yDJUh4o8NrOr0XUovfcowREiAyRlOAQNuJmDj2%2F%2FI3WHczLsMZa%2FyeUnskOxep1T2JCtd8TBN9TU3TAR6ZMTG5XZNGzFcoawlwA%2B0NzwsWaxjp%2BtwahE91ngu%2BLGzQXnIsePOa0KGXAhWOr4WS7PNMJ7n6LwGOqUBV6dmAYAjbZvqS%2FiFM6c5n3Sb9p5%2Bg4Pgg%2F4SZO7Fy1syfXaftw3wN7kITG6gGKeU7RfUJj2yp3VelOeYxjWVcHEwH1IxoILxgBajKP26pEqt3r1gG8ZU7waZSXqJGzGSrHg5zBCkeV4K%2BMZIM0Gc7IjYUz%2BNpHNOHIIjTfFjp5aTOWjY938aJzCLVfM6g9FB75ZttVui6qtXFPP8068zxTSJVtZH&X-Amz-Signature=dd3ad27b85c5c1d7b4507c33eda64671ffab274f800e22ac08b7f4ad12bd3719&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T74HZTW3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXNBaAOyzSAZe3%2B0Guhc8dMDVXZ7DFOMyPRAgc%2FxbKZAiEA%2FtvUHuuVa1%2BefJrQGE0QVROlOYomADyXKm%2FZm9K7TXMqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMwGcZKaWueGbIMaWSrcA4O3u3GLCHe6De2R1QQFAEyqTQ7HlfYrK3N%2BSWLYKwO%2BVy3lSun7vBkkdiV9kY381YH%2Ffemghl9fOspGrsHFR%2BJa802KKQm8fNkWDUnbF5br08wosAqG55ZR5k9I3by4oXZvBegstrjpO1MHrjObolM1P3%2FLFDou6Yf8LZwkGW4Q%2BP75svkKZkMk%2FBjDWqxZDxthVRmQrk45HXx1ZfSa2pBv%2BP6GabqMy6UOG00N66b5nlQGPgBQDN%2BhUuITzWTTzgQva07ROgrMn0FrXd8nIsc3NF7fcn4YEwzA0NVDZ2RJ1SlnkBOyYJp0UyXSw2nyRHPORiOgEsk8p9YqLZsaiESdNh7AFzlVWg9tWetv95k7a8Vl0ah0YmMyIKoSS%2Bgu3xcFBfhpN4khvDi6ccZLzqLk47mCHp19jott6%2BRPlNKb5vflQMvaPpZHC0soz04x0wN1NLLDkYg92RVGzOEA1H4iALhz%2B0QyFEvmiL5yDJUh4o8NrOr0XUovfcowREiAyRlOAQNuJmDj2%2F%2FI3WHczLsMZa%2FyeUnskOxep1T2JCtd8TBN9TU3TAR6ZMTG5XZNGzFcoawlwA%2B0NzwsWaxjp%2BtwahE91ngu%2BLGzQXnIsePOa0KGXAhWOr4WS7PNMJ7n6LwGOqUBV6dmAYAjbZvqS%2FiFM6c5n3Sb9p5%2Bg4Pgg%2F4SZO7Fy1syfXaftw3wN7kITG6gGKeU7RfUJj2yp3VelOeYxjWVcHEwH1IxoILxgBajKP26pEqt3r1gG8ZU7waZSXqJGzGSrHg5zBCkeV4K%2BMZIM0Gc7IjYUz%2BNpHNOHIIjTfFjp5aTOWjY938aJzCLVfM6g9FB75ZttVui6qtXFPP8068zxTSJVtZH&X-Amz-Signature=72e890e8dd64fdf5a33bdfcb87f87f2e9dcb35cacaf90520f111ca11c301bc68&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T74HZTW3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXNBaAOyzSAZe3%2B0Guhc8dMDVXZ7DFOMyPRAgc%2FxbKZAiEA%2FtvUHuuVa1%2BefJrQGE0QVROlOYomADyXKm%2FZm9K7TXMqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMwGcZKaWueGbIMaWSrcA4O3u3GLCHe6De2R1QQFAEyqTQ7HlfYrK3N%2BSWLYKwO%2BVy3lSun7vBkkdiV9kY381YH%2Ffemghl9fOspGrsHFR%2BJa802KKQm8fNkWDUnbF5br08wosAqG55ZR5k9I3by4oXZvBegstrjpO1MHrjObolM1P3%2FLFDou6Yf8LZwkGW4Q%2BP75svkKZkMk%2FBjDWqxZDxthVRmQrk45HXx1ZfSa2pBv%2BP6GabqMy6UOG00N66b5nlQGPgBQDN%2BhUuITzWTTzgQva07ROgrMn0FrXd8nIsc3NF7fcn4YEwzA0NVDZ2RJ1SlnkBOyYJp0UyXSw2nyRHPORiOgEsk8p9YqLZsaiESdNh7AFzlVWg9tWetv95k7a8Vl0ah0YmMyIKoSS%2Bgu3xcFBfhpN4khvDi6ccZLzqLk47mCHp19jott6%2BRPlNKb5vflQMvaPpZHC0soz04x0wN1NLLDkYg92RVGzOEA1H4iALhz%2B0QyFEvmiL5yDJUh4o8NrOr0XUovfcowREiAyRlOAQNuJmDj2%2F%2FI3WHczLsMZa%2FyeUnskOxep1T2JCtd8TBN9TU3TAR6ZMTG5XZNGzFcoawlwA%2B0NzwsWaxjp%2BtwahE91ngu%2BLGzQXnIsePOa0KGXAhWOr4WS7PNMJ7n6LwGOqUBV6dmAYAjbZvqS%2FiFM6c5n3Sb9p5%2Bg4Pgg%2F4SZO7Fy1syfXaftw3wN7kITG6gGKeU7RfUJj2yp3VelOeYxjWVcHEwH1IxoILxgBajKP26pEqt3r1gG8ZU7waZSXqJGzGSrHg5zBCkeV4K%2BMZIM0Gc7IjYUz%2BNpHNOHIIjTfFjp5aTOWjY938aJzCLVfM6g9FB75ZttVui6qtXFPP8068zxTSJVtZH&X-Amz-Signature=65c588679fd5d87bf4c60f4c1dffb2a31e4b1f01fd19e2fcd5e62868b1ef509f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T74HZTW3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXNBaAOyzSAZe3%2B0Guhc8dMDVXZ7DFOMyPRAgc%2FxbKZAiEA%2FtvUHuuVa1%2BefJrQGE0QVROlOYomADyXKm%2FZm9K7TXMqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMwGcZKaWueGbIMaWSrcA4O3u3GLCHe6De2R1QQFAEyqTQ7HlfYrK3N%2BSWLYKwO%2BVy3lSun7vBkkdiV9kY381YH%2Ffemghl9fOspGrsHFR%2BJa802KKQm8fNkWDUnbF5br08wosAqG55ZR5k9I3by4oXZvBegstrjpO1MHrjObolM1P3%2FLFDou6Yf8LZwkGW4Q%2BP75svkKZkMk%2FBjDWqxZDxthVRmQrk45HXx1ZfSa2pBv%2BP6GabqMy6UOG00N66b5nlQGPgBQDN%2BhUuITzWTTzgQva07ROgrMn0FrXd8nIsc3NF7fcn4YEwzA0NVDZ2RJ1SlnkBOyYJp0UyXSw2nyRHPORiOgEsk8p9YqLZsaiESdNh7AFzlVWg9tWetv95k7a8Vl0ah0YmMyIKoSS%2Bgu3xcFBfhpN4khvDi6ccZLzqLk47mCHp19jott6%2BRPlNKb5vflQMvaPpZHC0soz04x0wN1NLLDkYg92RVGzOEA1H4iALhz%2B0QyFEvmiL5yDJUh4o8NrOr0XUovfcowREiAyRlOAQNuJmDj2%2F%2FI3WHczLsMZa%2FyeUnskOxep1T2JCtd8TBN9TU3TAR6ZMTG5XZNGzFcoawlwA%2B0NzwsWaxjp%2BtwahE91ngu%2BLGzQXnIsePOa0KGXAhWOr4WS7PNMJ7n6LwGOqUBV6dmAYAjbZvqS%2FiFM6c5n3Sb9p5%2Bg4Pgg%2F4SZO7Fy1syfXaftw3wN7kITG6gGKeU7RfUJj2yp3VelOeYxjWVcHEwH1IxoILxgBajKP26pEqt3r1gG8ZU7waZSXqJGzGSrHg5zBCkeV4K%2BMZIM0Gc7IjYUz%2BNpHNOHIIjTfFjp5aTOWjY938aJzCLVfM6g9FB75ZttVui6qtXFPP8068zxTSJVtZH&X-Amz-Signature=3c5b982e52b4a7985c72ba00d6ca66f9273002366c8baf0cc2995d832e294bca&X-Amz-SignedHeaders=host&x-id=GetObject)
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


