

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJCJCEJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDnFVIhN8DOPFylyrTdmXffIeSJHjKcm8pxttxK4wf9AiBlaGtFkOrfHsfvVraAOHqoGGO2GXHLCw6Bs6Bzw1C4eSqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp6Lo7Ea3HX%2B81W2gKtwDrsG3goajb581Xv%2FrDwT0l%2Fd63M6Kv670J8GMq0yVx97%2F9saK5EBF5zYuoVESDq4WihVqacHVqU0vdbD%2F3Jfoj8xk0l%2FfhMUgsbLNZDLxxjijH%2B3MWncP00AGimv1hv43VorfK83jPYjy61V3PAbbfoRXKM2E%2BEmRjtioMX96T47N4TVk63eFujO%2FEP4w3c9AKEudBS1zZ1rNaNs9encr0gYGimpKUf6GkQUfD6wXKZQjNUdz8sTZcgO6ZztHig3rP9WHgt3Iax9%2BljDqZPrt7DvM8qLearpQY3vrkujSg6ODuvS1nN01A9g6j%2BoS4P%2FmwI%2BCP9MTUCJ1rJrHcFp1H0vPvjjIETmog%2BK9UVS3Th3Ao4uD%2Fim8EwPq19ucz464OGIBcV3YC117SPWg73UdL8k3s%2B6HKgDXKm0WeCtQgVT9zGbiVXPp3A76E9LilCwIMqL06RUWI2kq%2FdtIOythb%2FH2ngiAaNsj1AOQINMlZlKUPnWMLnWD%2F4A1dZREA6ShcCvxW61beQdQ%2BaoXr5jdlvBoh0xCkPi1EO1YWYSSjIYs%2BT8GVsKi%2FYrcYMcgvZucMWzP8E2Rfppxpy7dBhdEVUYpXuGyNaggNge%2FIgXfLOJizYzfxIyvd0XnJPAw96nvvAY6pgHs4VQlmMUc9dxV4WugXod158la12abATGQx3N8I7Xmos%2FFPkAcJP0hR8R5r3sN30sfi39DR9J%2BvyS2g0cO0bSfGlDSxqNBxxj3OYqTIQc9K%2B%2BaWKH8%2Fx3Qub9zT4XmYRDNGcNgRIdUjXIaVrdVMOZUEBDFbh0wLdgu9Nwc2Cvswxe74nFMSzMfyh74nyH3pzK%2Fhy%2Fg4%2FgyPoAiyRjvYLtaRN6h86VT&X-Amz-Signature=fbcabe132414c14d5720e01af413bf0a33d8d6482e9fe884aa0952334a67abb4&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672O2RBIR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA%2BnyAnOpYeB9%2BwFtFF%2BlN5m0%2Bzy0IU98MomqIDqi3%2BZAiEAq%2F3erkSxvq0tHAGVZhr0Wm9kGnoDpdfIp2iXBBNNKBwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHK5RfRIqAq6ZPoc5ircA7LOuFkitOXzG2YK8XZjXAEFzk3BXwZjcUfbUFPOxKZPHyWKXFZAt0LNulzgP1JBqN9XQH9NLps21%2FBYKP1ARVld4d8eq7HpRwkKUPeebvoGs1HiMfWn5rM9Wl1eQEq9fD0k6Y%2BY6NvrdFITZkja3G4BWWIbpJtIeVJNPzV6S9fcbdTC%2F3FubZ2Y6r4bHVtACDScNQOf5H4QnUZfoa9g0TAx330NF22tCzHNEDPhFnm7%2Br9zEZ5LCmN5ON%2B%2F9QIq55YOFCKi60FstklOnR1FTzq4QRPzmPA9difcvwxf4eMUtpmzCxN4fhNF5MoV5BPocKsZhXW4PCa1xk7zHO6nWhA0pfAW4cPrWAp7T7en52V%2Ba1iO%2BF35RxK%2FNb3Lri8m0Ovvi9POacqJEmdrqd3DPalgMaIizvSrGKPnzmwpzWtBImI5id%2FhEf0M851A8XYjhN36OR4wtvDKOSHK09l7K6%2FE7Ng0DtWme1cTw%2BhLuOQw%2Fqc5OvLugM%2F4QtYktZhuzPS%2BZ5%2BjHaa2O6551rNO4XFdYmRdwm9vIhriDytqOT0el0ZJYYQ%2FN9aWrNVdukK0iMm%2BVSIOWEkMX70fw20mSVAyZKMlUA1ZgX2ZqNlf5xsB2ePh7LyvPtNXXioGMIeq77wGOqUBo7jdMB%2BpcuuXCInNYt%2BiENuA9qVq0q7VOn3BuG4octImDd4F3MF%2BRmh5w7ngq6WH0joCMRDGKbVuOhnSnsLLzs11Cd%2BjDL0oJtfS1F%2FElCTghAQpOxcb07L3677hTVPYwEkKV95t%2FhQZ03k%2FqPraaIVf5ylBzaDEg30bIQ6lTnAKjYx3wCN9J6nJ17MGlnIcoYFwCS9z2UW9W6JtVT1RUU3i%2BebU&X-Amz-Signature=7d74f5bef0ce98155779ffda3ea34d8cbf93fc9d9b9c7e917afbe89e6ecd16ff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672O2RBIR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA%2BnyAnOpYeB9%2BwFtFF%2BlN5m0%2Bzy0IU98MomqIDqi3%2BZAiEAq%2F3erkSxvq0tHAGVZhr0Wm9kGnoDpdfIp2iXBBNNKBwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHK5RfRIqAq6ZPoc5ircA7LOuFkitOXzG2YK8XZjXAEFzk3BXwZjcUfbUFPOxKZPHyWKXFZAt0LNulzgP1JBqN9XQH9NLps21%2FBYKP1ARVld4d8eq7HpRwkKUPeebvoGs1HiMfWn5rM9Wl1eQEq9fD0k6Y%2BY6NvrdFITZkja3G4BWWIbpJtIeVJNPzV6S9fcbdTC%2F3FubZ2Y6r4bHVtACDScNQOf5H4QnUZfoa9g0TAx330NF22tCzHNEDPhFnm7%2Br9zEZ5LCmN5ON%2B%2F9QIq55YOFCKi60FstklOnR1FTzq4QRPzmPA9difcvwxf4eMUtpmzCxN4fhNF5MoV5BPocKsZhXW4PCa1xk7zHO6nWhA0pfAW4cPrWAp7T7en52V%2Ba1iO%2BF35RxK%2FNb3Lri8m0Ovvi9POacqJEmdrqd3DPalgMaIizvSrGKPnzmwpzWtBImI5id%2FhEf0M851A8XYjhN36OR4wtvDKOSHK09l7K6%2FE7Ng0DtWme1cTw%2BhLuOQw%2Fqc5OvLugM%2F4QtYktZhuzPS%2BZ5%2BjHaa2O6551rNO4XFdYmRdwm9vIhriDytqOT0el0ZJYYQ%2FN9aWrNVdukK0iMm%2BVSIOWEkMX70fw20mSVAyZKMlUA1ZgX2ZqNlf5xsB2ePh7LyvPtNXXioGMIeq77wGOqUBo7jdMB%2BpcuuXCInNYt%2BiENuA9qVq0q7VOn3BuG4octImDd4F3MF%2BRmh5w7ngq6WH0joCMRDGKbVuOhnSnsLLzs11Cd%2BjDL0oJtfS1F%2FElCTghAQpOxcb07L3677hTVPYwEkKV95t%2FhQZ03k%2FqPraaIVf5ylBzaDEg30bIQ6lTnAKjYx3wCN9J6nJ17MGlnIcoYFwCS9z2UW9W6JtVT1RUU3i%2BebU&X-Amz-Signature=2975ebf0dbb1d93f87ffa14dd78d1addbcf9768bdc9f940798392abb3f34cc95&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672O2RBIR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA%2BnyAnOpYeB9%2BwFtFF%2BlN5m0%2Bzy0IU98MomqIDqi3%2BZAiEAq%2F3erkSxvq0tHAGVZhr0Wm9kGnoDpdfIp2iXBBNNKBwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHK5RfRIqAq6ZPoc5ircA7LOuFkitOXzG2YK8XZjXAEFzk3BXwZjcUfbUFPOxKZPHyWKXFZAt0LNulzgP1JBqN9XQH9NLps21%2FBYKP1ARVld4d8eq7HpRwkKUPeebvoGs1HiMfWn5rM9Wl1eQEq9fD0k6Y%2BY6NvrdFITZkja3G4BWWIbpJtIeVJNPzV6S9fcbdTC%2F3FubZ2Y6r4bHVtACDScNQOf5H4QnUZfoa9g0TAx330NF22tCzHNEDPhFnm7%2Br9zEZ5LCmN5ON%2B%2F9QIq55YOFCKi60FstklOnR1FTzq4QRPzmPA9difcvwxf4eMUtpmzCxN4fhNF5MoV5BPocKsZhXW4PCa1xk7zHO6nWhA0pfAW4cPrWAp7T7en52V%2Ba1iO%2BF35RxK%2FNb3Lri8m0Ovvi9POacqJEmdrqd3DPalgMaIizvSrGKPnzmwpzWtBImI5id%2FhEf0M851A8XYjhN36OR4wtvDKOSHK09l7K6%2FE7Ng0DtWme1cTw%2BhLuOQw%2Fqc5OvLugM%2F4QtYktZhuzPS%2BZ5%2BjHaa2O6551rNO4XFdYmRdwm9vIhriDytqOT0el0ZJYYQ%2FN9aWrNVdukK0iMm%2BVSIOWEkMX70fw20mSVAyZKMlUA1ZgX2ZqNlf5xsB2ePh7LyvPtNXXioGMIeq77wGOqUBo7jdMB%2BpcuuXCInNYt%2BiENuA9qVq0q7VOn3BuG4octImDd4F3MF%2BRmh5w7ngq6WH0joCMRDGKbVuOhnSnsLLzs11Cd%2BjDL0oJtfS1F%2FElCTghAQpOxcb07L3677hTVPYwEkKV95t%2FhQZ03k%2FqPraaIVf5ylBzaDEg30bIQ6lTnAKjYx3wCN9J6nJ17MGlnIcoYFwCS9z2UW9W6JtVT1RUU3i%2BebU&X-Amz-Signature=f044db2f1806b32b3befed49fec62924c69ad8a96da0551a8e0ea4322010279b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672O2RBIR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA%2BnyAnOpYeB9%2BwFtFF%2BlN5m0%2Bzy0IU98MomqIDqi3%2BZAiEAq%2F3erkSxvq0tHAGVZhr0Wm9kGnoDpdfIp2iXBBNNKBwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHK5RfRIqAq6ZPoc5ircA7LOuFkitOXzG2YK8XZjXAEFzk3BXwZjcUfbUFPOxKZPHyWKXFZAt0LNulzgP1JBqN9XQH9NLps21%2FBYKP1ARVld4d8eq7HpRwkKUPeebvoGs1HiMfWn5rM9Wl1eQEq9fD0k6Y%2BY6NvrdFITZkja3G4BWWIbpJtIeVJNPzV6S9fcbdTC%2F3FubZ2Y6r4bHVtACDScNQOf5H4QnUZfoa9g0TAx330NF22tCzHNEDPhFnm7%2Br9zEZ5LCmN5ON%2B%2F9QIq55YOFCKi60FstklOnR1FTzq4QRPzmPA9difcvwxf4eMUtpmzCxN4fhNF5MoV5BPocKsZhXW4PCa1xk7zHO6nWhA0pfAW4cPrWAp7T7en52V%2Ba1iO%2BF35RxK%2FNb3Lri8m0Ovvi9POacqJEmdrqd3DPalgMaIizvSrGKPnzmwpzWtBImI5id%2FhEf0M851A8XYjhN36OR4wtvDKOSHK09l7K6%2FE7Ng0DtWme1cTw%2BhLuOQw%2Fqc5OvLugM%2F4QtYktZhuzPS%2BZ5%2BjHaa2O6551rNO4XFdYmRdwm9vIhriDytqOT0el0ZJYYQ%2FN9aWrNVdukK0iMm%2BVSIOWEkMX70fw20mSVAyZKMlUA1ZgX2ZqNlf5xsB2ePh7LyvPtNXXioGMIeq77wGOqUBo7jdMB%2BpcuuXCInNYt%2BiENuA9qVq0q7VOn3BuG4octImDd4F3MF%2BRmh5w7ngq6WH0joCMRDGKbVuOhnSnsLLzs11Cd%2BjDL0oJtfS1F%2FElCTghAQpOxcb07L3677hTVPYwEkKV95t%2FhQZ03k%2FqPraaIVf5ylBzaDEg30bIQ6lTnAKjYx3wCN9J6nJ17MGlnIcoYFwCS9z2UW9W6JtVT1RUU3i%2BebU&X-Amz-Signature=ce2b624852030d9cffd185046ac2e2e5ffd0cc940363b9ddda031f5b190a4652&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672O2RBIR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA%2BnyAnOpYeB9%2BwFtFF%2BlN5m0%2Bzy0IU98MomqIDqi3%2BZAiEAq%2F3erkSxvq0tHAGVZhr0Wm9kGnoDpdfIp2iXBBNNKBwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHK5RfRIqAq6ZPoc5ircA7LOuFkitOXzG2YK8XZjXAEFzk3BXwZjcUfbUFPOxKZPHyWKXFZAt0LNulzgP1JBqN9XQH9NLps21%2FBYKP1ARVld4d8eq7HpRwkKUPeebvoGs1HiMfWn5rM9Wl1eQEq9fD0k6Y%2BY6NvrdFITZkja3G4BWWIbpJtIeVJNPzV6S9fcbdTC%2F3FubZ2Y6r4bHVtACDScNQOf5H4QnUZfoa9g0TAx330NF22tCzHNEDPhFnm7%2Br9zEZ5LCmN5ON%2B%2F9QIq55YOFCKi60FstklOnR1FTzq4QRPzmPA9difcvwxf4eMUtpmzCxN4fhNF5MoV5BPocKsZhXW4PCa1xk7zHO6nWhA0pfAW4cPrWAp7T7en52V%2Ba1iO%2BF35RxK%2FNb3Lri8m0Ovvi9POacqJEmdrqd3DPalgMaIizvSrGKPnzmwpzWtBImI5id%2FhEf0M851A8XYjhN36OR4wtvDKOSHK09l7K6%2FE7Ng0DtWme1cTw%2BhLuOQw%2Fqc5OvLugM%2F4QtYktZhuzPS%2BZ5%2BjHaa2O6551rNO4XFdYmRdwm9vIhriDytqOT0el0ZJYYQ%2FN9aWrNVdukK0iMm%2BVSIOWEkMX70fw20mSVAyZKMlUA1ZgX2ZqNlf5xsB2ePh7LyvPtNXXioGMIeq77wGOqUBo7jdMB%2BpcuuXCInNYt%2BiENuA9qVq0q7VOn3BuG4octImDd4F3MF%2BRmh5w7ngq6WH0joCMRDGKbVuOhnSnsLLzs11Cd%2BjDL0oJtfS1F%2FElCTghAQpOxcb07L3677hTVPYwEkKV95t%2FhQZ03k%2FqPraaIVf5ylBzaDEg30bIQ6lTnAKjYx3wCN9J6nJ17MGlnIcoYFwCS9z2UW9W6JtVT1RUU3i%2BebU&X-Amz-Signature=bcde705593b7950c094c935a1e4f911da5b52811be1318bcf711e1a6d99d4bcb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJCJCEJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDnFVIhN8DOPFylyrTdmXffIeSJHjKcm8pxttxK4wf9AiBlaGtFkOrfHsfvVraAOHqoGGO2GXHLCw6Bs6Bzw1C4eSqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp6Lo7Ea3HX%2B81W2gKtwDrsG3goajb581Xv%2FrDwT0l%2Fd63M6Kv670J8GMq0yVx97%2F9saK5EBF5zYuoVESDq4WihVqacHVqU0vdbD%2F3Jfoj8xk0l%2FfhMUgsbLNZDLxxjijH%2B3MWncP00AGimv1hv43VorfK83jPYjy61V3PAbbfoRXKM2E%2BEmRjtioMX96T47N4TVk63eFujO%2FEP4w3c9AKEudBS1zZ1rNaNs9encr0gYGimpKUf6GkQUfD6wXKZQjNUdz8sTZcgO6ZztHig3rP9WHgt3Iax9%2BljDqZPrt7DvM8qLearpQY3vrkujSg6ODuvS1nN01A9g6j%2BoS4P%2FmwI%2BCP9MTUCJ1rJrHcFp1H0vPvjjIETmog%2BK9UVS3Th3Ao4uD%2Fim8EwPq19ucz464OGIBcV3YC117SPWg73UdL8k3s%2B6HKgDXKm0WeCtQgVT9zGbiVXPp3A76E9LilCwIMqL06RUWI2kq%2FdtIOythb%2FH2ngiAaNsj1AOQINMlZlKUPnWMLnWD%2F4A1dZREA6ShcCvxW61beQdQ%2BaoXr5jdlvBoh0xCkPi1EO1YWYSSjIYs%2BT8GVsKi%2FYrcYMcgvZucMWzP8E2Rfppxpy7dBhdEVUYpXuGyNaggNge%2FIgXfLOJizYzfxIyvd0XnJPAw96nvvAY6pgHs4VQlmMUc9dxV4WugXod158la12abATGQx3N8I7Xmos%2FFPkAcJP0hR8R5r3sN30sfi39DR9J%2BvyS2g0cO0bSfGlDSxqNBxxj3OYqTIQc9K%2B%2BaWKH8%2Fx3Qub9zT4XmYRDNGcNgRIdUjXIaVrdVMOZUEBDFbh0wLdgu9Nwc2Cvswxe74nFMSzMfyh74nyH3pzK%2Fhy%2Fg4%2FgyPoAiyRjvYLtaRN6h86VT&X-Amz-Signature=67210e65b34d1b014001652dd2788188fd341ba46069c5c9ede6cc7e06ecdaf1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJCJCEJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDnFVIhN8DOPFylyrTdmXffIeSJHjKcm8pxttxK4wf9AiBlaGtFkOrfHsfvVraAOHqoGGO2GXHLCw6Bs6Bzw1C4eSqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp6Lo7Ea3HX%2B81W2gKtwDrsG3goajb581Xv%2FrDwT0l%2Fd63M6Kv670J8GMq0yVx97%2F9saK5EBF5zYuoVESDq4WihVqacHVqU0vdbD%2F3Jfoj8xk0l%2FfhMUgsbLNZDLxxjijH%2B3MWncP00AGimv1hv43VorfK83jPYjy61V3PAbbfoRXKM2E%2BEmRjtioMX96T47N4TVk63eFujO%2FEP4w3c9AKEudBS1zZ1rNaNs9encr0gYGimpKUf6GkQUfD6wXKZQjNUdz8sTZcgO6ZztHig3rP9WHgt3Iax9%2BljDqZPrt7DvM8qLearpQY3vrkujSg6ODuvS1nN01A9g6j%2BoS4P%2FmwI%2BCP9MTUCJ1rJrHcFp1H0vPvjjIETmog%2BK9UVS3Th3Ao4uD%2Fim8EwPq19ucz464OGIBcV3YC117SPWg73UdL8k3s%2B6HKgDXKm0WeCtQgVT9zGbiVXPp3A76E9LilCwIMqL06RUWI2kq%2FdtIOythb%2FH2ngiAaNsj1AOQINMlZlKUPnWMLnWD%2F4A1dZREA6ShcCvxW61beQdQ%2BaoXr5jdlvBoh0xCkPi1EO1YWYSSjIYs%2BT8GVsKi%2FYrcYMcgvZucMWzP8E2Rfppxpy7dBhdEVUYpXuGyNaggNge%2FIgXfLOJizYzfxIyvd0XnJPAw96nvvAY6pgHs4VQlmMUc9dxV4WugXod158la12abATGQx3N8I7Xmos%2FFPkAcJP0hR8R5r3sN30sfi39DR9J%2BvyS2g0cO0bSfGlDSxqNBxxj3OYqTIQc9K%2B%2BaWKH8%2Fx3Qub9zT4XmYRDNGcNgRIdUjXIaVrdVMOZUEBDFbh0wLdgu9Nwc2Cvswxe74nFMSzMfyh74nyH3pzK%2Fhy%2Fg4%2FgyPoAiyRjvYLtaRN6h86VT&X-Amz-Signature=cb2432d2441604eeb65ac95efeba10992c4b1b38b7602ce11f9ade017cf882d7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJCJCEJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDnFVIhN8DOPFylyrTdmXffIeSJHjKcm8pxttxK4wf9AiBlaGtFkOrfHsfvVraAOHqoGGO2GXHLCw6Bs6Bzw1C4eSqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp6Lo7Ea3HX%2B81W2gKtwDrsG3goajb581Xv%2FrDwT0l%2Fd63M6Kv670J8GMq0yVx97%2F9saK5EBF5zYuoVESDq4WihVqacHVqU0vdbD%2F3Jfoj8xk0l%2FfhMUgsbLNZDLxxjijH%2B3MWncP00AGimv1hv43VorfK83jPYjy61V3PAbbfoRXKM2E%2BEmRjtioMX96T47N4TVk63eFujO%2FEP4w3c9AKEudBS1zZ1rNaNs9encr0gYGimpKUf6GkQUfD6wXKZQjNUdz8sTZcgO6ZztHig3rP9WHgt3Iax9%2BljDqZPrt7DvM8qLearpQY3vrkujSg6ODuvS1nN01A9g6j%2BoS4P%2FmwI%2BCP9MTUCJ1rJrHcFp1H0vPvjjIETmog%2BK9UVS3Th3Ao4uD%2Fim8EwPq19ucz464OGIBcV3YC117SPWg73UdL8k3s%2B6HKgDXKm0WeCtQgVT9zGbiVXPp3A76E9LilCwIMqL06RUWI2kq%2FdtIOythb%2FH2ngiAaNsj1AOQINMlZlKUPnWMLnWD%2F4A1dZREA6ShcCvxW61beQdQ%2BaoXr5jdlvBoh0xCkPi1EO1YWYSSjIYs%2BT8GVsKi%2FYrcYMcgvZucMWzP8E2Rfppxpy7dBhdEVUYpXuGyNaggNge%2FIgXfLOJizYzfxIyvd0XnJPAw96nvvAY6pgHs4VQlmMUc9dxV4WugXod158la12abATGQx3N8I7Xmos%2FFPkAcJP0hR8R5r3sN30sfi39DR9J%2BvyS2g0cO0bSfGlDSxqNBxxj3OYqTIQc9K%2B%2BaWKH8%2Fx3Qub9zT4XmYRDNGcNgRIdUjXIaVrdVMOZUEBDFbh0wLdgu9Nwc2Cvswxe74nFMSzMfyh74nyH3pzK%2Fhy%2Fg4%2FgyPoAiyRjvYLtaRN6h86VT&X-Amz-Signature=98f16f4013ba4883296e7166532b59b8495f8f29db5559a783523266f61bae54&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJCJCEJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDnFVIhN8DOPFylyrTdmXffIeSJHjKcm8pxttxK4wf9AiBlaGtFkOrfHsfvVraAOHqoGGO2GXHLCw6Bs6Bzw1C4eSqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp6Lo7Ea3HX%2B81W2gKtwDrsG3goajb581Xv%2FrDwT0l%2Fd63M6Kv670J8GMq0yVx97%2F9saK5EBF5zYuoVESDq4WihVqacHVqU0vdbD%2F3Jfoj8xk0l%2FfhMUgsbLNZDLxxjijH%2B3MWncP00AGimv1hv43VorfK83jPYjy61V3PAbbfoRXKM2E%2BEmRjtioMX96T47N4TVk63eFujO%2FEP4w3c9AKEudBS1zZ1rNaNs9encr0gYGimpKUf6GkQUfD6wXKZQjNUdz8sTZcgO6ZztHig3rP9WHgt3Iax9%2BljDqZPrt7DvM8qLearpQY3vrkujSg6ODuvS1nN01A9g6j%2BoS4P%2FmwI%2BCP9MTUCJ1rJrHcFp1H0vPvjjIETmog%2BK9UVS3Th3Ao4uD%2Fim8EwPq19ucz464OGIBcV3YC117SPWg73UdL8k3s%2B6HKgDXKm0WeCtQgVT9zGbiVXPp3A76E9LilCwIMqL06RUWI2kq%2FdtIOythb%2FH2ngiAaNsj1AOQINMlZlKUPnWMLnWD%2F4A1dZREA6ShcCvxW61beQdQ%2BaoXr5jdlvBoh0xCkPi1EO1YWYSSjIYs%2BT8GVsKi%2FYrcYMcgvZucMWzP8E2Rfppxpy7dBhdEVUYpXuGyNaggNge%2FIgXfLOJizYzfxIyvd0XnJPAw96nvvAY6pgHs4VQlmMUc9dxV4WugXod158la12abATGQx3N8I7Xmos%2FFPkAcJP0hR8R5r3sN30sfi39DR9J%2BvyS2g0cO0bSfGlDSxqNBxxj3OYqTIQc9K%2B%2BaWKH8%2Fx3Qub9zT4XmYRDNGcNgRIdUjXIaVrdVMOZUEBDFbh0wLdgu9Nwc2Cvswxe74nFMSzMfyh74nyH3pzK%2Fhy%2Fg4%2FgyPoAiyRjvYLtaRN6h86VT&X-Amz-Signature=ef11ed3907ad629153a23bcfb06bd08178c63354b3e43b45b5e4af0050bb4816&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJCJCEJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDnFVIhN8DOPFylyrTdmXffIeSJHjKcm8pxttxK4wf9AiBlaGtFkOrfHsfvVraAOHqoGGO2GXHLCw6Bs6Bzw1C4eSqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp6Lo7Ea3HX%2B81W2gKtwDrsG3goajb581Xv%2FrDwT0l%2Fd63M6Kv670J8GMq0yVx97%2F9saK5EBF5zYuoVESDq4WihVqacHVqU0vdbD%2F3Jfoj8xk0l%2FfhMUgsbLNZDLxxjijH%2B3MWncP00AGimv1hv43VorfK83jPYjy61V3PAbbfoRXKM2E%2BEmRjtioMX96T47N4TVk63eFujO%2FEP4w3c9AKEudBS1zZ1rNaNs9encr0gYGimpKUf6GkQUfD6wXKZQjNUdz8sTZcgO6ZztHig3rP9WHgt3Iax9%2BljDqZPrt7DvM8qLearpQY3vrkujSg6ODuvS1nN01A9g6j%2BoS4P%2FmwI%2BCP9MTUCJ1rJrHcFp1H0vPvjjIETmog%2BK9UVS3Th3Ao4uD%2Fim8EwPq19ucz464OGIBcV3YC117SPWg73UdL8k3s%2B6HKgDXKm0WeCtQgVT9zGbiVXPp3A76E9LilCwIMqL06RUWI2kq%2FdtIOythb%2FH2ngiAaNsj1AOQINMlZlKUPnWMLnWD%2F4A1dZREA6ShcCvxW61beQdQ%2BaoXr5jdlvBoh0xCkPi1EO1YWYSSjIYs%2BT8GVsKi%2FYrcYMcgvZucMWzP8E2Rfppxpy7dBhdEVUYpXuGyNaggNge%2FIgXfLOJizYzfxIyvd0XnJPAw96nvvAY6pgHs4VQlmMUc9dxV4WugXod158la12abATGQx3N8I7Xmos%2FFPkAcJP0hR8R5r3sN30sfi39DR9J%2BvyS2g0cO0bSfGlDSxqNBxxj3OYqTIQc9K%2B%2BaWKH8%2Fx3Qub9zT4XmYRDNGcNgRIdUjXIaVrdVMOZUEBDFbh0wLdgu9Nwc2Cvswxe74nFMSzMfyh74nyH3pzK%2Fhy%2Fg4%2FgyPoAiyRjvYLtaRN6h86VT&X-Amz-Signature=88c9253f6da7940fd30806919f3895f683b7aa3ca8b6a0375284264058b7e7d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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


