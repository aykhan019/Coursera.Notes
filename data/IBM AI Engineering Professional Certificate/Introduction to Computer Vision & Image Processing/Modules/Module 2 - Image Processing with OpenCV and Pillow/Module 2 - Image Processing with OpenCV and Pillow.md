

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVG7ZK3G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIFZNi7CXcnNMzc4Ft9%2BAD3sgDgNCmiAZecU00YX%2FXGJVAiEArOUV%2BjyY8kxR1X59gSTFhvEsfZuWX4NLB0bBaIEOs%2Fgq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDNIuanRNU8tQBIIkwCrcA2Yoo%2FHqyl0wIvRn5HMQmnGRevTa%2FsFxGig46F%2Bx9qzhAJ8XJyrPPSRULqgzBScVjafY4uvezd6%2FuiTyRH0JNgIVOkoiYnc%2BVWw9UqjlEN1FKaX93AFFAQTxJ57QsLylbBk%2FJkwxwuYXq5DzKAGQAE%2Bxz5GQCmidxykzJQbHayuAQAbt%2FolZj8aO8G8s96JrUG03eJIN4vd2EFZi%2BFG6yHrKdO4sSYybwHBb5CUJLhRdDzaJKnnQvgvZBDBZpANuVaOVHrVssCDUjO03CwaaO%2FFJBh2PsjsqlblrarpcsXqR8IaRUFhs986%2FZqN9V4mKAB4LF%2FZx5yrdFyHUscAwJUBa8%2FjaZPav3y8wZlPTnAxb2XlIGMyF4CsA%2FXuJqPDHFVjQpZW90VfIHWcOFRRGQJKdh4CK%2BocPZfwp%2FEa9uXHuGW8SWjUDu5uukv3G5q1EeModVE7UJy3WJk8oA9o85Q51aUqIvlbEIrc5c2z%2FF3YPc3sEHAHqklUaHboSCXF8xlJAvS%2B5S0Cutyu%2Fx0shqkdxU6TNNmT%2FLAXyfHsdzbjBVg3eX9NltN96s9W1vvqhHGED9wAIGEGy6x6sT2XimzEMtACqUrYXqvyCpqtvR5f9IfPCui8dmNkwd3g7MM2djr0GOqUByz8zJP3iXxuv05JjEXRU%2B2BR5jwDPMdEdUuGP%2Bk%2BSRx3UxrBkm7woB195P2xb4Gwk1hdoNRyaJVkOcQSafoBldLhTH7zaqDw0%2BUhonMusPOsvDcVydEAnNZHQ74H1o1%2BNxknGVObkcqtfDorR%2BbWk5vV2lw%2BlYtoCZmMgcOAl30o%2FtI2DgKE%2FQE%2Bcn9VKwGCllpYxH1rTfH6Lz1IuCfoqULLs%2B%2Fg&X-Amz-Signature=0dadad75d8c889b1fe4d226db784d1a8346cba50447e99b08fda42efa6e37d7f&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3KVEVJ6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIASfqH8%2BOYkng3hDmavzugIU3O4swmH1pjAJ8mFSV8REAiBDv7SqjJ6uFqk0Uzy%2F2VzXlXNN9AZoKXyaoPRwk9%2B7kyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMxFoGcas994Ornky1KtwDWBVbm89v%2FNV20w64T3JR6p2bZ3rOuhxsdR73Bv22SawG54r5Losss72fVhirM%2BrCev1GUWgQi5IzKImM0ykSlRUcaqFg3W1R7YfFlS7eeX0IXgSdN2rFrhvnDwefSpqtgZTCyxj7sY7b43ZKiH3aYsEG7HyLxhchaAIKoYXa2w%2F9Khih%2BB9VWW9r8rutNANXmc%2Fz%2FusBwD7QDFI0SZVcO6cIVbPKACy1hLO%2BSuky1IQfCPsS2dvdMOE%2BbRSc97Udzu0LJqoceruC7tuhjzVtSbU7U6rG%2BKu9ZVKDP5SUB1LvJg4mhn6oazQKLQOJhE%2FLb48OvhJUXXADyWFpqyK1jBpEWc%2BvWphYvnnxSun5nfHdOm5M7rKQQ5WhysgbwyOshMZdeuXQXaEXYe%2FqC6vtXEPvMialy%2Fv%2FLLI7HgvXRGTPcKh0BiZWS5CumzE4fFcEaopGM7KRj5mO9WS3elw3j9Bq7u9KfQcWjladnTDx6LCOLc%2BwUhDcIok7Qmgrha%2BubniNibYBTYOlebUQp%2BHlBS39T5m4Oj7%2BCWVjF4rVH4J9EP1GMFpB3U7pZyu%2Bnsp3IsIGWm5BIeu1x7cpKjV%2Fpe3ugCPjS6xy9dub7bCdwmIY5nD8XUr6xLyp%2F8Mwv52OvQY6pgGPmi25FAycUxONWnwZC88l6AAqJMWNKboDv3QlIgn3m7uBLkm7UjXbTAyyGcyPbBrOdIFZ0daIDmDHe10jGMzld1TJCIBIpqv3Nadc1j5nX6JnLHIYYHP9pdibtGFTCOinwlPE%2BTXAcRD9bE4%2ByFWbLxjBEa4cZI5O%2FZlPLv9glzUdVG%2F7jVWXuNuWmsaEJpZH0x2GzsFyHtg3Q4n2K1MTGrJUymyO&X-Amz-Signature=648c72ab33627e1e90a359c6498eea70f4b8213602a8c9ea4ed6791fca59410e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3KVEVJ6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIASfqH8%2BOYkng3hDmavzugIU3O4swmH1pjAJ8mFSV8REAiBDv7SqjJ6uFqk0Uzy%2F2VzXlXNN9AZoKXyaoPRwk9%2B7kyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMxFoGcas994Ornky1KtwDWBVbm89v%2FNV20w64T3JR6p2bZ3rOuhxsdR73Bv22SawG54r5Losss72fVhirM%2BrCev1GUWgQi5IzKImM0ykSlRUcaqFg3W1R7YfFlS7eeX0IXgSdN2rFrhvnDwefSpqtgZTCyxj7sY7b43ZKiH3aYsEG7HyLxhchaAIKoYXa2w%2F9Khih%2BB9VWW9r8rutNANXmc%2Fz%2FusBwD7QDFI0SZVcO6cIVbPKACy1hLO%2BSuky1IQfCPsS2dvdMOE%2BbRSc97Udzu0LJqoceruC7tuhjzVtSbU7U6rG%2BKu9ZVKDP5SUB1LvJg4mhn6oazQKLQOJhE%2FLb48OvhJUXXADyWFpqyK1jBpEWc%2BvWphYvnnxSun5nfHdOm5M7rKQQ5WhysgbwyOshMZdeuXQXaEXYe%2FqC6vtXEPvMialy%2Fv%2FLLI7HgvXRGTPcKh0BiZWS5CumzE4fFcEaopGM7KRj5mO9WS3elw3j9Bq7u9KfQcWjladnTDx6LCOLc%2BwUhDcIok7Qmgrha%2BubniNibYBTYOlebUQp%2BHlBS39T5m4Oj7%2BCWVjF4rVH4J9EP1GMFpB3U7pZyu%2Bnsp3IsIGWm5BIeu1x7cpKjV%2Fpe3ugCPjS6xy9dub7bCdwmIY5nD8XUr6xLyp%2F8Mwv52OvQY6pgGPmi25FAycUxONWnwZC88l6AAqJMWNKboDv3QlIgn3m7uBLkm7UjXbTAyyGcyPbBrOdIFZ0daIDmDHe10jGMzld1TJCIBIpqv3Nadc1j5nX6JnLHIYYHP9pdibtGFTCOinwlPE%2BTXAcRD9bE4%2ByFWbLxjBEa4cZI5O%2FZlPLv9glzUdVG%2F7jVWXuNuWmsaEJpZH0x2GzsFyHtg3Q4n2K1MTGrJUymyO&X-Amz-Signature=61d41e68b8725903817cb3aaf8d9820ab96f7fb3a13729c2dba1f2f75e3884d4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3KVEVJ6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIASfqH8%2BOYkng3hDmavzugIU3O4swmH1pjAJ8mFSV8REAiBDv7SqjJ6uFqk0Uzy%2F2VzXlXNN9AZoKXyaoPRwk9%2B7kyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMxFoGcas994Ornky1KtwDWBVbm89v%2FNV20w64T3JR6p2bZ3rOuhxsdR73Bv22SawG54r5Losss72fVhirM%2BrCev1GUWgQi5IzKImM0ykSlRUcaqFg3W1R7YfFlS7eeX0IXgSdN2rFrhvnDwefSpqtgZTCyxj7sY7b43ZKiH3aYsEG7HyLxhchaAIKoYXa2w%2F9Khih%2BB9VWW9r8rutNANXmc%2Fz%2FusBwD7QDFI0SZVcO6cIVbPKACy1hLO%2BSuky1IQfCPsS2dvdMOE%2BbRSc97Udzu0LJqoceruC7tuhjzVtSbU7U6rG%2BKu9ZVKDP5SUB1LvJg4mhn6oazQKLQOJhE%2FLb48OvhJUXXADyWFpqyK1jBpEWc%2BvWphYvnnxSun5nfHdOm5M7rKQQ5WhysgbwyOshMZdeuXQXaEXYe%2FqC6vtXEPvMialy%2Fv%2FLLI7HgvXRGTPcKh0BiZWS5CumzE4fFcEaopGM7KRj5mO9WS3elw3j9Bq7u9KfQcWjladnTDx6LCOLc%2BwUhDcIok7Qmgrha%2BubniNibYBTYOlebUQp%2BHlBS39T5m4Oj7%2BCWVjF4rVH4J9EP1GMFpB3U7pZyu%2Bnsp3IsIGWm5BIeu1x7cpKjV%2Fpe3ugCPjS6xy9dub7bCdwmIY5nD8XUr6xLyp%2F8Mwv52OvQY6pgGPmi25FAycUxONWnwZC88l6AAqJMWNKboDv3QlIgn3m7uBLkm7UjXbTAyyGcyPbBrOdIFZ0daIDmDHe10jGMzld1TJCIBIpqv3Nadc1j5nX6JnLHIYYHP9pdibtGFTCOinwlPE%2BTXAcRD9bE4%2ByFWbLxjBEa4cZI5O%2FZlPLv9glzUdVG%2F7jVWXuNuWmsaEJpZH0x2GzsFyHtg3Q4n2K1MTGrJUymyO&X-Amz-Signature=6dac847519e50257d52cd981c85d9075a3fe7091c8e22320cc3e4c2b047c24c0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3KVEVJ6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIASfqH8%2BOYkng3hDmavzugIU3O4swmH1pjAJ8mFSV8REAiBDv7SqjJ6uFqk0Uzy%2F2VzXlXNN9AZoKXyaoPRwk9%2B7kyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMxFoGcas994Ornky1KtwDWBVbm89v%2FNV20w64T3JR6p2bZ3rOuhxsdR73Bv22SawG54r5Losss72fVhirM%2BrCev1GUWgQi5IzKImM0ykSlRUcaqFg3W1R7YfFlS7eeX0IXgSdN2rFrhvnDwefSpqtgZTCyxj7sY7b43ZKiH3aYsEG7HyLxhchaAIKoYXa2w%2F9Khih%2BB9VWW9r8rutNANXmc%2Fz%2FusBwD7QDFI0SZVcO6cIVbPKACy1hLO%2BSuky1IQfCPsS2dvdMOE%2BbRSc97Udzu0LJqoceruC7tuhjzVtSbU7U6rG%2BKu9ZVKDP5SUB1LvJg4mhn6oazQKLQOJhE%2FLb48OvhJUXXADyWFpqyK1jBpEWc%2BvWphYvnnxSun5nfHdOm5M7rKQQ5WhysgbwyOshMZdeuXQXaEXYe%2FqC6vtXEPvMialy%2Fv%2FLLI7HgvXRGTPcKh0BiZWS5CumzE4fFcEaopGM7KRj5mO9WS3elw3j9Bq7u9KfQcWjladnTDx6LCOLc%2BwUhDcIok7Qmgrha%2BubniNibYBTYOlebUQp%2BHlBS39T5m4Oj7%2BCWVjF4rVH4J9EP1GMFpB3U7pZyu%2Bnsp3IsIGWm5BIeu1x7cpKjV%2Fpe3ugCPjS6xy9dub7bCdwmIY5nD8XUr6xLyp%2F8Mwv52OvQY6pgGPmi25FAycUxONWnwZC88l6AAqJMWNKboDv3QlIgn3m7uBLkm7UjXbTAyyGcyPbBrOdIFZ0daIDmDHe10jGMzld1TJCIBIpqv3Nadc1j5nX6JnLHIYYHP9pdibtGFTCOinwlPE%2BTXAcRD9bE4%2ByFWbLxjBEa4cZI5O%2FZlPLv9glzUdVG%2F7jVWXuNuWmsaEJpZH0x2GzsFyHtg3Q4n2K1MTGrJUymyO&X-Amz-Signature=b7a17efa926d0b87f10a6aec1cd87d0da911ac0f2c2e5bde172ac77dd7c91f9c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3KVEVJ6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIASfqH8%2BOYkng3hDmavzugIU3O4swmH1pjAJ8mFSV8REAiBDv7SqjJ6uFqk0Uzy%2F2VzXlXNN9AZoKXyaoPRwk9%2B7kyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMxFoGcas994Ornky1KtwDWBVbm89v%2FNV20w64T3JR6p2bZ3rOuhxsdR73Bv22SawG54r5Losss72fVhirM%2BrCev1GUWgQi5IzKImM0ykSlRUcaqFg3W1R7YfFlS7eeX0IXgSdN2rFrhvnDwefSpqtgZTCyxj7sY7b43ZKiH3aYsEG7HyLxhchaAIKoYXa2w%2F9Khih%2BB9VWW9r8rutNANXmc%2Fz%2FusBwD7QDFI0SZVcO6cIVbPKACy1hLO%2BSuky1IQfCPsS2dvdMOE%2BbRSc97Udzu0LJqoceruC7tuhjzVtSbU7U6rG%2BKu9ZVKDP5SUB1LvJg4mhn6oazQKLQOJhE%2FLb48OvhJUXXADyWFpqyK1jBpEWc%2BvWphYvnnxSun5nfHdOm5M7rKQQ5WhysgbwyOshMZdeuXQXaEXYe%2FqC6vtXEPvMialy%2Fv%2FLLI7HgvXRGTPcKh0BiZWS5CumzE4fFcEaopGM7KRj5mO9WS3elw3j9Bq7u9KfQcWjladnTDx6LCOLc%2BwUhDcIok7Qmgrha%2BubniNibYBTYOlebUQp%2BHlBS39T5m4Oj7%2BCWVjF4rVH4J9EP1GMFpB3U7pZyu%2Bnsp3IsIGWm5BIeu1x7cpKjV%2Fpe3ugCPjS6xy9dub7bCdwmIY5nD8XUr6xLyp%2F8Mwv52OvQY6pgGPmi25FAycUxONWnwZC88l6AAqJMWNKboDv3QlIgn3m7uBLkm7UjXbTAyyGcyPbBrOdIFZ0daIDmDHe10jGMzld1TJCIBIpqv3Nadc1j5nX6JnLHIYYHP9pdibtGFTCOinwlPE%2BTXAcRD9bE4%2ByFWbLxjBEa4cZI5O%2FZlPLv9glzUdVG%2F7jVWXuNuWmsaEJpZH0x2GzsFyHtg3Q4n2K1MTGrJUymyO&X-Amz-Signature=c01530b381b9d4fadc3b2915dc088e484472281e41b3c170c8946a20c4388752&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVG7ZK3G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIFZNi7CXcnNMzc4Ft9%2BAD3sgDgNCmiAZecU00YX%2FXGJVAiEArOUV%2BjyY8kxR1X59gSTFhvEsfZuWX4NLB0bBaIEOs%2Fgq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDNIuanRNU8tQBIIkwCrcA2Yoo%2FHqyl0wIvRn5HMQmnGRevTa%2FsFxGig46F%2Bx9qzhAJ8XJyrPPSRULqgzBScVjafY4uvezd6%2FuiTyRH0JNgIVOkoiYnc%2BVWw9UqjlEN1FKaX93AFFAQTxJ57QsLylbBk%2FJkwxwuYXq5DzKAGQAE%2Bxz5GQCmidxykzJQbHayuAQAbt%2FolZj8aO8G8s96JrUG03eJIN4vd2EFZi%2BFG6yHrKdO4sSYybwHBb5CUJLhRdDzaJKnnQvgvZBDBZpANuVaOVHrVssCDUjO03CwaaO%2FFJBh2PsjsqlblrarpcsXqR8IaRUFhs986%2FZqN9V4mKAB4LF%2FZx5yrdFyHUscAwJUBa8%2FjaZPav3y8wZlPTnAxb2XlIGMyF4CsA%2FXuJqPDHFVjQpZW90VfIHWcOFRRGQJKdh4CK%2BocPZfwp%2FEa9uXHuGW8SWjUDu5uukv3G5q1EeModVE7UJy3WJk8oA9o85Q51aUqIvlbEIrc5c2z%2FF3YPc3sEHAHqklUaHboSCXF8xlJAvS%2B5S0Cutyu%2Fx0shqkdxU6TNNmT%2FLAXyfHsdzbjBVg3eX9NltN96s9W1vvqhHGED9wAIGEGy6x6sT2XimzEMtACqUrYXqvyCpqtvR5f9IfPCui8dmNkwd3g7MM2djr0GOqUByz8zJP3iXxuv05JjEXRU%2B2BR5jwDPMdEdUuGP%2Bk%2BSRx3UxrBkm7woB195P2xb4Gwk1hdoNRyaJVkOcQSafoBldLhTH7zaqDw0%2BUhonMusPOsvDcVydEAnNZHQ74H1o1%2BNxknGVObkcqtfDorR%2BbWk5vV2lw%2BlYtoCZmMgcOAl30o%2FtI2DgKE%2FQE%2Bcn9VKwGCllpYxH1rTfH6Lz1IuCfoqULLs%2B%2Fg&X-Amz-Signature=e01249f3b087436f115e875e3cce4b0534af6ffdc60ea909eb850d0c3a525e59&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVG7ZK3G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIFZNi7CXcnNMzc4Ft9%2BAD3sgDgNCmiAZecU00YX%2FXGJVAiEArOUV%2BjyY8kxR1X59gSTFhvEsfZuWX4NLB0bBaIEOs%2Fgq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDNIuanRNU8tQBIIkwCrcA2Yoo%2FHqyl0wIvRn5HMQmnGRevTa%2FsFxGig46F%2Bx9qzhAJ8XJyrPPSRULqgzBScVjafY4uvezd6%2FuiTyRH0JNgIVOkoiYnc%2BVWw9UqjlEN1FKaX93AFFAQTxJ57QsLylbBk%2FJkwxwuYXq5DzKAGQAE%2Bxz5GQCmidxykzJQbHayuAQAbt%2FolZj8aO8G8s96JrUG03eJIN4vd2EFZi%2BFG6yHrKdO4sSYybwHBb5CUJLhRdDzaJKnnQvgvZBDBZpANuVaOVHrVssCDUjO03CwaaO%2FFJBh2PsjsqlblrarpcsXqR8IaRUFhs986%2FZqN9V4mKAB4LF%2FZx5yrdFyHUscAwJUBa8%2FjaZPav3y8wZlPTnAxb2XlIGMyF4CsA%2FXuJqPDHFVjQpZW90VfIHWcOFRRGQJKdh4CK%2BocPZfwp%2FEa9uXHuGW8SWjUDu5uukv3G5q1EeModVE7UJy3WJk8oA9o85Q51aUqIvlbEIrc5c2z%2FF3YPc3sEHAHqklUaHboSCXF8xlJAvS%2B5S0Cutyu%2Fx0shqkdxU6TNNmT%2FLAXyfHsdzbjBVg3eX9NltN96s9W1vvqhHGED9wAIGEGy6x6sT2XimzEMtACqUrYXqvyCpqtvR5f9IfPCui8dmNkwd3g7MM2djr0GOqUByz8zJP3iXxuv05JjEXRU%2B2BR5jwDPMdEdUuGP%2Bk%2BSRx3UxrBkm7woB195P2xb4Gwk1hdoNRyaJVkOcQSafoBldLhTH7zaqDw0%2BUhonMusPOsvDcVydEAnNZHQ74H1o1%2BNxknGVObkcqtfDorR%2BbWk5vV2lw%2BlYtoCZmMgcOAl30o%2FtI2DgKE%2FQE%2Bcn9VKwGCllpYxH1rTfH6Lz1IuCfoqULLs%2B%2Fg&X-Amz-Signature=32c8061ae4741de904352d10fff274e5863be50d046bd208a779264ddb1afed8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVG7ZK3G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIFZNi7CXcnNMzc4Ft9%2BAD3sgDgNCmiAZecU00YX%2FXGJVAiEArOUV%2BjyY8kxR1X59gSTFhvEsfZuWX4NLB0bBaIEOs%2Fgq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDNIuanRNU8tQBIIkwCrcA2Yoo%2FHqyl0wIvRn5HMQmnGRevTa%2FsFxGig46F%2Bx9qzhAJ8XJyrPPSRULqgzBScVjafY4uvezd6%2FuiTyRH0JNgIVOkoiYnc%2BVWw9UqjlEN1FKaX93AFFAQTxJ57QsLylbBk%2FJkwxwuYXq5DzKAGQAE%2Bxz5GQCmidxykzJQbHayuAQAbt%2FolZj8aO8G8s96JrUG03eJIN4vd2EFZi%2BFG6yHrKdO4sSYybwHBb5CUJLhRdDzaJKnnQvgvZBDBZpANuVaOVHrVssCDUjO03CwaaO%2FFJBh2PsjsqlblrarpcsXqR8IaRUFhs986%2FZqN9V4mKAB4LF%2FZx5yrdFyHUscAwJUBa8%2FjaZPav3y8wZlPTnAxb2XlIGMyF4CsA%2FXuJqPDHFVjQpZW90VfIHWcOFRRGQJKdh4CK%2BocPZfwp%2FEa9uXHuGW8SWjUDu5uukv3G5q1EeModVE7UJy3WJk8oA9o85Q51aUqIvlbEIrc5c2z%2FF3YPc3sEHAHqklUaHboSCXF8xlJAvS%2B5S0Cutyu%2Fx0shqkdxU6TNNmT%2FLAXyfHsdzbjBVg3eX9NltN96s9W1vvqhHGED9wAIGEGy6x6sT2XimzEMtACqUrYXqvyCpqtvR5f9IfPCui8dmNkwd3g7MM2djr0GOqUByz8zJP3iXxuv05JjEXRU%2B2BR5jwDPMdEdUuGP%2Bk%2BSRx3UxrBkm7woB195P2xb4Gwk1hdoNRyaJVkOcQSafoBldLhTH7zaqDw0%2BUhonMusPOsvDcVydEAnNZHQ74H1o1%2BNxknGVObkcqtfDorR%2BbWk5vV2lw%2BlYtoCZmMgcOAl30o%2FtI2DgKE%2FQE%2Bcn9VKwGCllpYxH1rTfH6Lz1IuCfoqULLs%2B%2Fg&X-Amz-Signature=13fed0f03963d7d899aa822b88e2f9c35ab585de2e457f4239ceae3cc3963ed6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVG7ZK3G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIFZNi7CXcnNMzc4Ft9%2BAD3sgDgNCmiAZecU00YX%2FXGJVAiEArOUV%2BjyY8kxR1X59gSTFhvEsfZuWX4NLB0bBaIEOs%2Fgq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDNIuanRNU8tQBIIkwCrcA2Yoo%2FHqyl0wIvRn5HMQmnGRevTa%2FsFxGig46F%2Bx9qzhAJ8XJyrPPSRULqgzBScVjafY4uvezd6%2FuiTyRH0JNgIVOkoiYnc%2BVWw9UqjlEN1FKaX93AFFAQTxJ57QsLylbBk%2FJkwxwuYXq5DzKAGQAE%2Bxz5GQCmidxykzJQbHayuAQAbt%2FolZj8aO8G8s96JrUG03eJIN4vd2EFZi%2BFG6yHrKdO4sSYybwHBb5CUJLhRdDzaJKnnQvgvZBDBZpANuVaOVHrVssCDUjO03CwaaO%2FFJBh2PsjsqlblrarpcsXqR8IaRUFhs986%2FZqN9V4mKAB4LF%2FZx5yrdFyHUscAwJUBa8%2FjaZPav3y8wZlPTnAxb2XlIGMyF4CsA%2FXuJqPDHFVjQpZW90VfIHWcOFRRGQJKdh4CK%2BocPZfwp%2FEa9uXHuGW8SWjUDu5uukv3G5q1EeModVE7UJy3WJk8oA9o85Q51aUqIvlbEIrc5c2z%2FF3YPc3sEHAHqklUaHboSCXF8xlJAvS%2B5S0Cutyu%2Fx0shqkdxU6TNNmT%2FLAXyfHsdzbjBVg3eX9NltN96s9W1vvqhHGED9wAIGEGy6x6sT2XimzEMtACqUrYXqvyCpqtvR5f9IfPCui8dmNkwd3g7MM2djr0GOqUByz8zJP3iXxuv05JjEXRU%2B2BR5jwDPMdEdUuGP%2Bk%2BSRx3UxrBkm7woB195P2xb4Gwk1hdoNRyaJVkOcQSafoBldLhTH7zaqDw0%2BUhonMusPOsvDcVydEAnNZHQ74H1o1%2BNxknGVObkcqtfDorR%2BbWk5vV2lw%2BlYtoCZmMgcOAl30o%2FtI2DgKE%2FQE%2Bcn9VKwGCllpYxH1rTfH6Lz1IuCfoqULLs%2B%2Fg&X-Amz-Signature=eb3a23cda86a04f5aa0e4fc3d0fae555ae6ab88acafca7a5bea5acd174236ef1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVG7ZK3G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIFZNi7CXcnNMzc4Ft9%2BAD3sgDgNCmiAZecU00YX%2FXGJVAiEArOUV%2BjyY8kxR1X59gSTFhvEsfZuWX4NLB0bBaIEOs%2Fgq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDNIuanRNU8tQBIIkwCrcA2Yoo%2FHqyl0wIvRn5HMQmnGRevTa%2FsFxGig46F%2Bx9qzhAJ8XJyrPPSRULqgzBScVjafY4uvezd6%2FuiTyRH0JNgIVOkoiYnc%2BVWw9UqjlEN1FKaX93AFFAQTxJ57QsLylbBk%2FJkwxwuYXq5DzKAGQAE%2Bxz5GQCmidxykzJQbHayuAQAbt%2FolZj8aO8G8s96JrUG03eJIN4vd2EFZi%2BFG6yHrKdO4sSYybwHBb5CUJLhRdDzaJKnnQvgvZBDBZpANuVaOVHrVssCDUjO03CwaaO%2FFJBh2PsjsqlblrarpcsXqR8IaRUFhs986%2FZqN9V4mKAB4LF%2FZx5yrdFyHUscAwJUBa8%2FjaZPav3y8wZlPTnAxb2XlIGMyF4CsA%2FXuJqPDHFVjQpZW90VfIHWcOFRRGQJKdh4CK%2BocPZfwp%2FEa9uXHuGW8SWjUDu5uukv3G5q1EeModVE7UJy3WJk8oA9o85Q51aUqIvlbEIrc5c2z%2FF3YPc3sEHAHqklUaHboSCXF8xlJAvS%2B5S0Cutyu%2Fx0shqkdxU6TNNmT%2FLAXyfHsdzbjBVg3eX9NltN96s9W1vvqhHGED9wAIGEGy6x6sT2XimzEMtACqUrYXqvyCpqtvR5f9IfPCui8dmNkwd3g7MM2djr0GOqUByz8zJP3iXxuv05JjEXRU%2B2BR5jwDPMdEdUuGP%2Bk%2BSRx3UxrBkm7woB195P2xb4Gwk1hdoNRyaJVkOcQSafoBldLhTH7zaqDw0%2BUhonMusPOsvDcVydEAnNZHQ74H1o1%2BNxknGVObkcqtfDorR%2BbWk5vV2lw%2BlYtoCZmMgcOAl30o%2FtI2DgKE%2FQE%2Bcn9VKwGCllpYxH1rTfH6Lz1IuCfoqULLs%2B%2Fg&X-Amz-Signature=1f01b03230e083ab97475fbd720564747967f4855195e27808c4814d479c7181&X-Amz-SignedHeaders=host&x-id=GetObject)
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


