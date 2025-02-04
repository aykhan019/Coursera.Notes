

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPE72Q54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDVvbaaOMcaCO35q3gqbrXNWg%2FLpVLIQWgQ1T%2F6BzNJ3AiEApJ0OfvWIGKhp52620X8VbS8jioYAP1r1wUexgueQY%2BEq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDBpwwITPj23PbqHm6yrcA0l1XDzXQGAX%2FPvlW1HgG0XG9dhBEFw4JVTzW7wRBiOT7kYfMH3N%2FfPjcLCxAjhEwhTFXuc1IoSy0YOCMM6E2%2FoHTVO7ZmCkDs%2BYukw9B0apnXX0ZgN3iUt8U7o%2BC2NmOhK9aWSZJVDbncSRFo16NWRjlLskr6x15u8TgzfYv5sAf9SCwoy4gQFFfVaXNm1ntzO2huHn7EsMRPGU8JGedTxMZ5BjwTT%2F4FmkqO1dPdJEeJA1%2BQnkyKVplWiUThVuhH8kyyMv0isxtO2IvFENCs%2FkPscrX8FB0SY14wYkdr8zDm%2FEVDbN9qKP%2Bi1%2BuzCvfaC%2FIWrDPHS77P60gbDD%2Ba%2B7d%2Bh6k6cQtoFUj5EKt%2BZY4UWx3XCu%2FLSMlrKRs065dA3qQn0N%2Bu7COXnYCtcbNJpuANWbqYSTsJKTe5Bo5%2Ba0aMlbA%2BvLRshsZrsLarsg8wV61xefqFpl92RKgHcggSXrXFS4YcEN8zkvw6srGR88PHd8Gd8oNzV90fjNMmLBAX8XWD2ahFYZirJdqZ0O9I39cajVmEVDj2Y%2FakYPMqCg7GgGF0eJvY%2FFw%2FxOSP0vsvkdq9Wny1YFlNm3FYXncdClNTAwqW18CzPYOjP2Yz7JWoUfG8zj%2BMEVdHagMO6gib0GOqUBQTTWNV2%2F2akiUdyllCUJhM1o%2BPG1rVOrXncAlbL6U%2FwTmkckEC90tIJR532XMeghbpQtQE6YJW8ty8beZSijIFRany30th4bfFFLsrAnne6Fj1yAluELtb0kY1J0VB0rld2YjUt2nn82R6eLMsbtmc3Yjgzo9CuHpPQpr%2BxEkFLaZmEwOvtpQxH1ze2oMh%2FJyqlvvASzNHFZW3YvGWO95ij31MA7&X-Amz-Signature=3e2e3b1dd0c7a71f7cd075ee635a3ed7c746c5d674c0ff02a1529de4be43ccfc&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSEI3KI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQC7oej1SCwfv5WbcjRaibwRh44gP4yqq%2BG2vKTXYD2B9AIgMVQnNiF8nmerTeeHm9qy5Bpve9JB6VwQWMEHFiKSf3Mq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDMjAzS%2Bcmx4eByxhgCrcA9fxW9aEE0CR0%2Bmya5BrlPe%2Beo6B3sIoID4DM1UjBfyy8l7BUTP3L7jc8gv4ZBnTB4NGXYLcTmPv2jbdDWLosEv5BPLn88P2RRXji6tdgho0m%2FGEJDyibQxI1o6HQAXreJsQYEgCfk6DoVsdjzL08j8v9UlQbv7FlldZruAKJCmOB5hyVTw0o0W1oSf5ECoO%2BRzkqOv6FI7%2B4fttA1AcU6X%2F29fJg03cK%2FHyt6Km6WbxL7ouQ82%2BQ2kCM24v6mSAoswLgSxDPeJFktS7xZRCVk3PM0ylPZQg%2FrPcgvdgS5B0khbu1dy25fmPFw%2FXgoNxsBTooGXMOPs6w7GHephtAqmXWx8uI%2Fcj%2BmcUZ8IEUAqzU1pB3zoK%2FEiPdhzsyUEKAnlaPw3sPGcpMmMK5d8X%2BJe6EHGXoKi%2FCsYyTfM5wbDu0Cmhw%2Bf8nlO9h0jrPg7jmcGMfHl30BCE2s4Yj8zuW7zopaE4YURF%2B3k3bOkrwzZHq0oa4J9Poggtn%2F%2FF0Pf%2FBVUiRODPMf%2FHe3JeJIw0Arjp%2FmcPhHizweQWIZjFyfvwiVyPn0Os6dGD5dAguf2ffwXa044twtyKq9dIlp%2FF2UJ0yr5ivh6p4RAz0vBvtgC8ZL67kytYqHReao09MJehib0GOqUB2%2FTYavC6%2BcnwVTA%2FJsFf3ujBlrBD2OLPzSJ%2BMzuQmJFJZTK7d9N%2FW097c5%2Bi4KoEuykxwCgvY5W%2BfbFYt4yV5FnDxKbGAKoG3Owl006TJVLZcHv0jZi1gBw5GBrC9gMKktStLvnLjRh6jtPs8A9aTviOK0ImbHnHPwsXIMdTNTjsSV4CGXA6d6Z2PffaDNhjwaJ2qVG5WKCHR153O0MG4zi%2BTWU7&X-Amz-Signature=cf88ce7a2631bef2129d1f2bed46acdafcd13f140c60405014914fd4abb371a9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSEI3KI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQC7oej1SCwfv5WbcjRaibwRh44gP4yqq%2BG2vKTXYD2B9AIgMVQnNiF8nmerTeeHm9qy5Bpve9JB6VwQWMEHFiKSf3Mq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDMjAzS%2Bcmx4eByxhgCrcA9fxW9aEE0CR0%2Bmya5BrlPe%2Beo6B3sIoID4DM1UjBfyy8l7BUTP3L7jc8gv4ZBnTB4NGXYLcTmPv2jbdDWLosEv5BPLn88P2RRXji6tdgho0m%2FGEJDyibQxI1o6HQAXreJsQYEgCfk6DoVsdjzL08j8v9UlQbv7FlldZruAKJCmOB5hyVTw0o0W1oSf5ECoO%2BRzkqOv6FI7%2B4fttA1AcU6X%2F29fJg03cK%2FHyt6Km6WbxL7ouQ82%2BQ2kCM24v6mSAoswLgSxDPeJFktS7xZRCVk3PM0ylPZQg%2FrPcgvdgS5B0khbu1dy25fmPFw%2FXgoNxsBTooGXMOPs6w7GHephtAqmXWx8uI%2Fcj%2BmcUZ8IEUAqzU1pB3zoK%2FEiPdhzsyUEKAnlaPw3sPGcpMmMK5d8X%2BJe6EHGXoKi%2FCsYyTfM5wbDu0Cmhw%2Bf8nlO9h0jrPg7jmcGMfHl30BCE2s4Yj8zuW7zopaE4YURF%2B3k3bOkrwzZHq0oa4J9Poggtn%2F%2FF0Pf%2FBVUiRODPMf%2FHe3JeJIw0Arjp%2FmcPhHizweQWIZjFyfvwiVyPn0Os6dGD5dAguf2ffwXa044twtyKq9dIlp%2FF2UJ0yr5ivh6p4RAz0vBvtgC8ZL67kytYqHReao09MJehib0GOqUB2%2FTYavC6%2BcnwVTA%2FJsFf3ujBlrBD2OLPzSJ%2BMzuQmJFJZTK7d9N%2FW097c5%2Bi4KoEuykxwCgvY5W%2BfbFYt4yV5FnDxKbGAKoG3Owl006TJVLZcHv0jZi1gBw5GBrC9gMKktStLvnLjRh6jtPs8A9aTviOK0ImbHnHPwsXIMdTNTjsSV4CGXA6d6Z2PffaDNhjwaJ2qVG5WKCHR153O0MG4zi%2BTWU7&X-Amz-Signature=75925570c62d461422aa8d0c97ff9dd78ee022ea16a9cca9a20366d2980c17a9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSEI3KI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQC7oej1SCwfv5WbcjRaibwRh44gP4yqq%2BG2vKTXYD2B9AIgMVQnNiF8nmerTeeHm9qy5Bpve9JB6VwQWMEHFiKSf3Mq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDMjAzS%2Bcmx4eByxhgCrcA9fxW9aEE0CR0%2Bmya5BrlPe%2Beo6B3sIoID4DM1UjBfyy8l7BUTP3L7jc8gv4ZBnTB4NGXYLcTmPv2jbdDWLosEv5BPLn88P2RRXji6tdgho0m%2FGEJDyibQxI1o6HQAXreJsQYEgCfk6DoVsdjzL08j8v9UlQbv7FlldZruAKJCmOB5hyVTw0o0W1oSf5ECoO%2BRzkqOv6FI7%2B4fttA1AcU6X%2F29fJg03cK%2FHyt6Km6WbxL7ouQ82%2BQ2kCM24v6mSAoswLgSxDPeJFktS7xZRCVk3PM0ylPZQg%2FrPcgvdgS5B0khbu1dy25fmPFw%2FXgoNxsBTooGXMOPs6w7GHephtAqmXWx8uI%2Fcj%2BmcUZ8IEUAqzU1pB3zoK%2FEiPdhzsyUEKAnlaPw3sPGcpMmMK5d8X%2BJe6EHGXoKi%2FCsYyTfM5wbDu0Cmhw%2Bf8nlO9h0jrPg7jmcGMfHl30BCE2s4Yj8zuW7zopaE4YURF%2B3k3bOkrwzZHq0oa4J9Poggtn%2F%2FF0Pf%2FBVUiRODPMf%2FHe3JeJIw0Arjp%2FmcPhHizweQWIZjFyfvwiVyPn0Os6dGD5dAguf2ffwXa044twtyKq9dIlp%2FF2UJ0yr5ivh6p4RAz0vBvtgC8ZL67kytYqHReao09MJehib0GOqUB2%2FTYavC6%2BcnwVTA%2FJsFf3ujBlrBD2OLPzSJ%2BMzuQmJFJZTK7d9N%2FW097c5%2Bi4KoEuykxwCgvY5W%2BfbFYt4yV5FnDxKbGAKoG3Owl006TJVLZcHv0jZi1gBw5GBrC9gMKktStLvnLjRh6jtPs8A9aTviOK0ImbHnHPwsXIMdTNTjsSV4CGXA6d6Z2PffaDNhjwaJ2qVG5WKCHR153O0MG4zi%2BTWU7&X-Amz-Signature=b4e2d1e16ef1ed481a4e00175e3377e9122f0990200fa2603b5669364c339585&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSEI3KI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQC7oej1SCwfv5WbcjRaibwRh44gP4yqq%2BG2vKTXYD2B9AIgMVQnNiF8nmerTeeHm9qy5Bpve9JB6VwQWMEHFiKSf3Mq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDMjAzS%2Bcmx4eByxhgCrcA9fxW9aEE0CR0%2Bmya5BrlPe%2Beo6B3sIoID4DM1UjBfyy8l7BUTP3L7jc8gv4ZBnTB4NGXYLcTmPv2jbdDWLosEv5BPLn88P2RRXji6tdgho0m%2FGEJDyibQxI1o6HQAXreJsQYEgCfk6DoVsdjzL08j8v9UlQbv7FlldZruAKJCmOB5hyVTw0o0W1oSf5ECoO%2BRzkqOv6FI7%2B4fttA1AcU6X%2F29fJg03cK%2FHyt6Km6WbxL7ouQ82%2BQ2kCM24v6mSAoswLgSxDPeJFktS7xZRCVk3PM0ylPZQg%2FrPcgvdgS5B0khbu1dy25fmPFw%2FXgoNxsBTooGXMOPs6w7GHephtAqmXWx8uI%2Fcj%2BmcUZ8IEUAqzU1pB3zoK%2FEiPdhzsyUEKAnlaPw3sPGcpMmMK5d8X%2BJe6EHGXoKi%2FCsYyTfM5wbDu0Cmhw%2Bf8nlO9h0jrPg7jmcGMfHl30BCE2s4Yj8zuW7zopaE4YURF%2B3k3bOkrwzZHq0oa4J9Poggtn%2F%2FF0Pf%2FBVUiRODPMf%2FHe3JeJIw0Arjp%2FmcPhHizweQWIZjFyfvwiVyPn0Os6dGD5dAguf2ffwXa044twtyKq9dIlp%2FF2UJ0yr5ivh6p4RAz0vBvtgC8ZL67kytYqHReao09MJehib0GOqUB2%2FTYavC6%2BcnwVTA%2FJsFf3ujBlrBD2OLPzSJ%2BMzuQmJFJZTK7d9N%2FW097c5%2Bi4KoEuykxwCgvY5W%2BfbFYt4yV5FnDxKbGAKoG3Owl006TJVLZcHv0jZi1gBw5GBrC9gMKktStLvnLjRh6jtPs8A9aTviOK0ImbHnHPwsXIMdTNTjsSV4CGXA6d6Z2PffaDNhjwaJ2qVG5WKCHR153O0MG4zi%2BTWU7&X-Amz-Signature=59e15752eff012303a66f63086f411f0c3501bb96e221836ec136dfa95f8ae82&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSEI3KI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQC7oej1SCwfv5WbcjRaibwRh44gP4yqq%2BG2vKTXYD2B9AIgMVQnNiF8nmerTeeHm9qy5Bpve9JB6VwQWMEHFiKSf3Mq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDMjAzS%2Bcmx4eByxhgCrcA9fxW9aEE0CR0%2Bmya5BrlPe%2Beo6B3sIoID4DM1UjBfyy8l7BUTP3L7jc8gv4ZBnTB4NGXYLcTmPv2jbdDWLosEv5BPLn88P2RRXji6tdgho0m%2FGEJDyibQxI1o6HQAXreJsQYEgCfk6DoVsdjzL08j8v9UlQbv7FlldZruAKJCmOB5hyVTw0o0W1oSf5ECoO%2BRzkqOv6FI7%2B4fttA1AcU6X%2F29fJg03cK%2FHyt6Km6WbxL7ouQ82%2BQ2kCM24v6mSAoswLgSxDPeJFktS7xZRCVk3PM0ylPZQg%2FrPcgvdgS5B0khbu1dy25fmPFw%2FXgoNxsBTooGXMOPs6w7GHephtAqmXWx8uI%2Fcj%2BmcUZ8IEUAqzU1pB3zoK%2FEiPdhzsyUEKAnlaPw3sPGcpMmMK5d8X%2BJe6EHGXoKi%2FCsYyTfM5wbDu0Cmhw%2Bf8nlO9h0jrPg7jmcGMfHl30BCE2s4Yj8zuW7zopaE4YURF%2B3k3bOkrwzZHq0oa4J9Poggtn%2F%2FF0Pf%2FBVUiRODPMf%2FHe3JeJIw0Arjp%2FmcPhHizweQWIZjFyfvwiVyPn0Os6dGD5dAguf2ffwXa044twtyKq9dIlp%2FF2UJ0yr5ivh6p4RAz0vBvtgC8ZL67kytYqHReao09MJehib0GOqUB2%2FTYavC6%2BcnwVTA%2FJsFf3ujBlrBD2OLPzSJ%2BMzuQmJFJZTK7d9N%2FW097c5%2Bi4KoEuykxwCgvY5W%2BfbFYt4yV5FnDxKbGAKoG3Owl006TJVLZcHv0jZi1gBw5GBrC9gMKktStLvnLjRh6jtPs8A9aTviOK0ImbHnHPwsXIMdTNTjsSV4CGXA6d6Z2PffaDNhjwaJ2qVG5WKCHR153O0MG4zi%2BTWU7&X-Amz-Signature=3eada8a1c5211b67d68102e2f8036626a738f26e69b1cd2fecf9f6a6729d053e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPE72Q54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDVvbaaOMcaCO35q3gqbrXNWg%2FLpVLIQWgQ1T%2F6BzNJ3AiEApJ0OfvWIGKhp52620X8VbS8jioYAP1r1wUexgueQY%2BEq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDBpwwITPj23PbqHm6yrcA0l1XDzXQGAX%2FPvlW1HgG0XG9dhBEFw4JVTzW7wRBiOT7kYfMH3N%2FfPjcLCxAjhEwhTFXuc1IoSy0YOCMM6E2%2FoHTVO7ZmCkDs%2BYukw9B0apnXX0ZgN3iUt8U7o%2BC2NmOhK9aWSZJVDbncSRFo16NWRjlLskr6x15u8TgzfYv5sAf9SCwoy4gQFFfVaXNm1ntzO2huHn7EsMRPGU8JGedTxMZ5BjwTT%2F4FmkqO1dPdJEeJA1%2BQnkyKVplWiUThVuhH8kyyMv0isxtO2IvFENCs%2FkPscrX8FB0SY14wYkdr8zDm%2FEVDbN9qKP%2Bi1%2BuzCvfaC%2FIWrDPHS77P60gbDD%2Ba%2B7d%2Bh6k6cQtoFUj5EKt%2BZY4UWx3XCu%2FLSMlrKRs065dA3qQn0N%2Bu7COXnYCtcbNJpuANWbqYSTsJKTe5Bo5%2Ba0aMlbA%2BvLRshsZrsLarsg8wV61xefqFpl92RKgHcggSXrXFS4YcEN8zkvw6srGR88PHd8Gd8oNzV90fjNMmLBAX8XWD2ahFYZirJdqZ0O9I39cajVmEVDj2Y%2FakYPMqCg7GgGF0eJvY%2FFw%2FxOSP0vsvkdq9Wny1YFlNm3FYXncdClNTAwqW18CzPYOjP2Yz7JWoUfG8zj%2BMEVdHagMO6gib0GOqUBQTTWNV2%2F2akiUdyllCUJhM1o%2BPG1rVOrXncAlbL6U%2FwTmkckEC90tIJR532XMeghbpQtQE6YJW8ty8beZSijIFRany30th4bfFFLsrAnne6Fj1yAluELtb0kY1J0VB0rld2YjUt2nn82R6eLMsbtmc3Yjgzo9CuHpPQpr%2BxEkFLaZmEwOvtpQxH1ze2oMh%2FJyqlvvASzNHFZW3YvGWO95ij31MA7&X-Amz-Signature=33fea6bb71f2ab668c9d72e41dbf891afed22681345690bbedcf0d3467d60a67&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPE72Q54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDVvbaaOMcaCO35q3gqbrXNWg%2FLpVLIQWgQ1T%2F6BzNJ3AiEApJ0OfvWIGKhp52620X8VbS8jioYAP1r1wUexgueQY%2BEq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDBpwwITPj23PbqHm6yrcA0l1XDzXQGAX%2FPvlW1HgG0XG9dhBEFw4JVTzW7wRBiOT7kYfMH3N%2FfPjcLCxAjhEwhTFXuc1IoSy0YOCMM6E2%2FoHTVO7ZmCkDs%2BYukw9B0apnXX0ZgN3iUt8U7o%2BC2NmOhK9aWSZJVDbncSRFo16NWRjlLskr6x15u8TgzfYv5sAf9SCwoy4gQFFfVaXNm1ntzO2huHn7EsMRPGU8JGedTxMZ5BjwTT%2F4FmkqO1dPdJEeJA1%2BQnkyKVplWiUThVuhH8kyyMv0isxtO2IvFENCs%2FkPscrX8FB0SY14wYkdr8zDm%2FEVDbN9qKP%2Bi1%2BuzCvfaC%2FIWrDPHS77P60gbDD%2Ba%2B7d%2Bh6k6cQtoFUj5EKt%2BZY4UWx3XCu%2FLSMlrKRs065dA3qQn0N%2Bu7COXnYCtcbNJpuANWbqYSTsJKTe5Bo5%2Ba0aMlbA%2BvLRshsZrsLarsg8wV61xefqFpl92RKgHcggSXrXFS4YcEN8zkvw6srGR88PHd8Gd8oNzV90fjNMmLBAX8XWD2ahFYZirJdqZ0O9I39cajVmEVDj2Y%2FakYPMqCg7GgGF0eJvY%2FFw%2FxOSP0vsvkdq9Wny1YFlNm3FYXncdClNTAwqW18CzPYOjP2Yz7JWoUfG8zj%2BMEVdHagMO6gib0GOqUBQTTWNV2%2F2akiUdyllCUJhM1o%2BPG1rVOrXncAlbL6U%2FwTmkckEC90tIJR532XMeghbpQtQE6YJW8ty8beZSijIFRany30th4bfFFLsrAnne6Fj1yAluELtb0kY1J0VB0rld2YjUt2nn82R6eLMsbtmc3Yjgzo9CuHpPQpr%2BxEkFLaZmEwOvtpQxH1ze2oMh%2FJyqlvvASzNHFZW3YvGWO95ij31MA7&X-Amz-Signature=fd0eee4964542df15c5e4a6203a9ec9d9efc0d17057d91fc30e7bb118b836552&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPE72Q54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDVvbaaOMcaCO35q3gqbrXNWg%2FLpVLIQWgQ1T%2F6BzNJ3AiEApJ0OfvWIGKhp52620X8VbS8jioYAP1r1wUexgueQY%2BEq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDBpwwITPj23PbqHm6yrcA0l1XDzXQGAX%2FPvlW1HgG0XG9dhBEFw4JVTzW7wRBiOT7kYfMH3N%2FfPjcLCxAjhEwhTFXuc1IoSy0YOCMM6E2%2FoHTVO7ZmCkDs%2BYukw9B0apnXX0ZgN3iUt8U7o%2BC2NmOhK9aWSZJVDbncSRFo16NWRjlLskr6x15u8TgzfYv5sAf9SCwoy4gQFFfVaXNm1ntzO2huHn7EsMRPGU8JGedTxMZ5BjwTT%2F4FmkqO1dPdJEeJA1%2BQnkyKVplWiUThVuhH8kyyMv0isxtO2IvFENCs%2FkPscrX8FB0SY14wYkdr8zDm%2FEVDbN9qKP%2Bi1%2BuzCvfaC%2FIWrDPHS77P60gbDD%2Ba%2B7d%2Bh6k6cQtoFUj5EKt%2BZY4UWx3XCu%2FLSMlrKRs065dA3qQn0N%2Bu7COXnYCtcbNJpuANWbqYSTsJKTe5Bo5%2Ba0aMlbA%2BvLRshsZrsLarsg8wV61xefqFpl92RKgHcggSXrXFS4YcEN8zkvw6srGR88PHd8Gd8oNzV90fjNMmLBAX8XWD2ahFYZirJdqZ0O9I39cajVmEVDj2Y%2FakYPMqCg7GgGF0eJvY%2FFw%2FxOSP0vsvkdq9Wny1YFlNm3FYXncdClNTAwqW18CzPYOjP2Yz7JWoUfG8zj%2BMEVdHagMO6gib0GOqUBQTTWNV2%2F2akiUdyllCUJhM1o%2BPG1rVOrXncAlbL6U%2FwTmkckEC90tIJR532XMeghbpQtQE6YJW8ty8beZSijIFRany30th4bfFFLsrAnne6Fj1yAluELtb0kY1J0VB0rld2YjUt2nn82R6eLMsbtmc3Yjgzo9CuHpPQpr%2BxEkFLaZmEwOvtpQxH1ze2oMh%2FJyqlvvASzNHFZW3YvGWO95ij31MA7&X-Amz-Signature=9a8e42c8b5cdc4d1ac297fac25543362c4d3412867a0b00e5d962e0e7e85147d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPE72Q54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDVvbaaOMcaCO35q3gqbrXNWg%2FLpVLIQWgQ1T%2F6BzNJ3AiEApJ0OfvWIGKhp52620X8VbS8jioYAP1r1wUexgueQY%2BEq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDBpwwITPj23PbqHm6yrcA0l1XDzXQGAX%2FPvlW1HgG0XG9dhBEFw4JVTzW7wRBiOT7kYfMH3N%2FfPjcLCxAjhEwhTFXuc1IoSy0YOCMM6E2%2FoHTVO7ZmCkDs%2BYukw9B0apnXX0ZgN3iUt8U7o%2BC2NmOhK9aWSZJVDbncSRFo16NWRjlLskr6x15u8TgzfYv5sAf9SCwoy4gQFFfVaXNm1ntzO2huHn7EsMRPGU8JGedTxMZ5BjwTT%2F4FmkqO1dPdJEeJA1%2BQnkyKVplWiUThVuhH8kyyMv0isxtO2IvFENCs%2FkPscrX8FB0SY14wYkdr8zDm%2FEVDbN9qKP%2Bi1%2BuzCvfaC%2FIWrDPHS77P60gbDD%2Ba%2B7d%2Bh6k6cQtoFUj5EKt%2BZY4UWx3XCu%2FLSMlrKRs065dA3qQn0N%2Bu7COXnYCtcbNJpuANWbqYSTsJKTe5Bo5%2Ba0aMlbA%2BvLRshsZrsLarsg8wV61xefqFpl92RKgHcggSXrXFS4YcEN8zkvw6srGR88PHd8Gd8oNzV90fjNMmLBAX8XWD2ahFYZirJdqZ0O9I39cajVmEVDj2Y%2FakYPMqCg7GgGF0eJvY%2FFw%2FxOSP0vsvkdq9Wny1YFlNm3FYXncdClNTAwqW18CzPYOjP2Yz7JWoUfG8zj%2BMEVdHagMO6gib0GOqUBQTTWNV2%2F2akiUdyllCUJhM1o%2BPG1rVOrXncAlbL6U%2FwTmkckEC90tIJR532XMeghbpQtQE6YJW8ty8beZSijIFRany30th4bfFFLsrAnne6Fj1yAluELtb0kY1J0VB0rld2YjUt2nn82R6eLMsbtmc3Yjgzo9CuHpPQpr%2BxEkFLaZmEwOvtpQxH1ze2oMh%2FJyqlvvASzNHFZW3YvGWO95ij31MA7&X-Amz-Signature=af518a293572cbd72002b7ce0f3e95662404831042c1954886d2a17afd5ae4d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPE72Q54%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDVvbaaOMcaCO35q3gqbrXNWg%2FLpVLIQWgQ1T%2F6BzNJ3AiEApJ0OfvWIGKhp52620X8VbS8jioYAP1r1wUexgueQY%2BEq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDBpwwITPj23PbqHm6yrcA0l1XDzXQGAX%2FPvlW1HgG0XG9dhBEFw4JVTzW7wRBiOT7kYfMH3N%2FfPjcLCxAjhEwhTFXuc1IoSy0YOCMM6E2%2FoHTVO7ZmCkDs%2BYukw9B0apnXX0ZgN3iUt8U7o%2BC2NmOhK9aWSZJVDbncSRFo16NWRjlLskr6x15u8TgzfYv5sAf9SCwoy4gQFFfVaXNm1ntzO2huHn7EsMRPGU8JGedTxMZ5BjwTT%2F4FmkqO1dPdJEeJA1%2BQnkyKVplWiUThVuhH8kyyMv0isxtO2IvFENCs%2FkPscrX8FB0SY14wYkdr8zDm%2FEVDbN9qKP%2Bi1%2BuzCvfaC%2FIWrDPHS77P60gbDD%2Ba%2B7d%2Bh6k6cQtoFUj5EKt%2BZY4UWx3XCu%2FLSMlrKRs065dA3qQn0N%2Bu7COXnYCtcbNJpuANWbqYSTsJKTe5Bo5%2Ba0aMlbA%2BvLRshsZrsLarsg8wV61xefqFpl92RKgHcggSXrXFS4YcEN8zkvw6srGR88PHd8Gd8oNzV90fjNMmLBAX8XWD2ahFYZirJdqZ0O9I39cajVmEVDj2Y%2FakYPMqCg7GgGF0eJvY%2FFw%2FxOSP0vsvkdq9Wny1YFlNm3FYXncdClNTAwqW18CzPYOjP2Yz7JWoUfG8zj%2BMEVdHagMO6gib0GOqUBQTTWNV2%2F2akiUdyllCUJhM1o%2BPG1rVOrXncAlbL6U%2FwTmkckEC90tIJR532XMeghbpQtQE6YJW8ty8beZSijIFRany30th4bfFFLsrAnne6Fj1yAluELtb0kY1J0VB0rld2YjUt2nn82R6eLMsbtmc3Yjgzo9CuHpPQpr%2BxEkFLaZmEwOvtpQxH1ze2oMh%2FJyqlvvASzNHFZW3YvGWO95ij31MA7&X-Amz-Signature=60e266a1186917d760e9704c6f73fcc92d49a2b424299a0db0a8a5c48ed8cdaf&X-Amz-SignedHeaders=host&x-id=GetObject)
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


