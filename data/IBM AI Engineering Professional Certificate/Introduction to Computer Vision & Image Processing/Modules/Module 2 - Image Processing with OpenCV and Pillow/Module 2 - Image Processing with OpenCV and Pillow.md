

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS5QAN4Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEJOKQKDVDufmxhEByfQz68YMJQQNirTooLY2fXtuEJwAiEAm%2FHPO8rDIAvIcVaec%2Fe%2BCqkKUHpXlvjLj1EAXCwDC1wq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDK9MZVCRmsACwg5NCrcA7OUNccSXV3FF%2F0KPCAzt1BE0JqmY6AVB%2BhuiQvci6u98SpoDZnthlgBMB1M1pzpr8lE5XqlUcsE51oola6XtBy95eBlsmxi0YmvF%2Bdt2Y8gmc1E9bIUpddiTFfLWKVmX4LnqLUs48FLuDpUYjzKuqVoAhPagu5YPI82AwlFsQl5HlJVKkYsYmfegvSq6Mr2oWiK%2FOvkr6caGTeZYilQrC1hYNv7VEEef9pg0pAs46XDEkcwHF9TIs%2B8zeGTJUlD1CFLjYrarjFH4wijib4e%2Fm%2F4k38C52Bvpg0nkVaGnJNhEAdadhWbBt4ExdRoDWqhviJ2541ZB7JH0QuUQypc1T36pwmRAb6mXl99HIoNPGG%2BwKnENdwayeMMOnOkHQg4qInJda%2BZPQCy09Yl60W7t6b0XFgE7iSd0h4%2BVvbbIP8hYsLENmMuVGTlzg5C8iYi9JwBuHlTUI%2BaGHRlbGU4oKUQMa8G1uqbl5FJ2r0FbZRElXU8ZyKakWAruQGDwHXCUCLWMZD0plk%2B1eqQsWeccFHcMr1lTqamLEZ2R%2FsISWFi%2FWFd%2BsmVPz9Sw8VlubGDHPtXE533RAagnjWIQxS435h5epuKhJ35p591c5PdtMH0Zmt3Dt6O6n3kXLdTMNz%2Bmb0GOqUB4J%2FFAJZCI2nzrRB3owecgCDU0zMifsZrGus18LYV%2BKf6FHRlUA2CYVaSgABhkL6jC6jB%2FzT0Gp%2BiXphiN2ecX8SPeV%2FJP7awyRlABtShT5EvzWgU2lzwvgCXHhlskzYScoPatiLEUBiptk0TzUiH2pYDfc7Zyc68CIN9qklGEayI4LKPbhJHXM4drYDUI%2FhJ8mpPZH2VOywIxH7OjAD%2FBb%2BrXIDn&X-Amz-Signature=d0fa1048209b623ad5039f4fe74a86ea24275db0ee7d7181a4139ada71834168&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RPQ6XBT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIGZlZnkAv0EiNwu%2BLED%2BRN16tdeXUFpubShjCZdnYg0iAiEA4gc26A750%2FEsvpwTTUS8RQsLm1ltV43dUlt7j%2FSbyK0q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDI%2Fw2%2Fgq8m01lZVCjyrcA4SYb3epyOcH53m1VRR2CbUsxPW1fsQXLiVl5IraJmRsOHpNIbpFkbG%2Fl2EEFiVj%2BivLD7lycReC8CzIWWXpxS6m2y3jMljl9%2BxBoiDJvO1PoUnUMjmm5QiVQHlSEqmfxBuKrWyIp%2FH2OOPNwLT1b8Sir0Y7StiRt3r3TJMAahSKNbovNE2T14%2BUX3w6LsMfYuuIlHz5%2FG5e%2FQvQghJS3vPu5F2ZJNGEx6Oz4ztzHw9A1iSLd9SWqu22SjPQUUunh7494t83Q9yNrVn3FBlVglYj%2F%2FdH70w7Dy24vyuQ8b8C5%2B7B5ZnAMdRbqjqP99flIsS%2BBOxgv72NstTKVGGDa3Js45vuQnekKklqCmYewX5ILBfARrwPn7ryzQ%2B8G2oK%2FXzQLVDmrY%2F2fZfVxez8KVlm0F72yCMGrpRMnPULd5F2o9LA%2Fak5roe2CX3EVGvz044%2BQLiISMoKagXZ3lyQ%2FqWeCb3PHgZFDA1oInGs3SDtme%2BA1XpBnidOpvyryL9xg4q%2Bw%2BQ4SbSFPWzFqTbf1fQqpzJaPfRJrxZKtLyRRY57ppL%2Ba3wQXGyFX%2FzZBx3RlMjLa359fjx90mnz3BdnIw0YmKvwfJ6WyEPjX%2FAMxEVABUA22%2FUEfwgjDUiyMJf%2Bmb0GOqUBcWjd%2F0E0jWAgI4gyDo2FYJeaEJ0uDN9DspE6Tturc%2ByfikMdrz782FIMtQeApXr7MNY%2BE3kQKALuqxa%2FEbtql4OAWauuiUxLZ9IOZ2hbfKFSAuRkAktpP3a6az8tLWzl3T071k02BpDNlLzHVWgQpjzaD4l%2FIKpp9ThG6MeJ16dsDGaxbj3SDvn1YydAB7YGzv%2BMvN2qFE%2BqsMq0w3AsnYBvP833&X-Amz-Signature=1ba8a246cdf78e7b883a8129f0335abdfbd56e4ee1f93135563aa078a1b2d6cf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RPQ6XBT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIGZlZnkAv0EiNwu%2BLED%2BRN16tdeXUFpubShjCZdnYg0iAiEA4gc26A750%2FEsvpwTTUS8RQsLm1ltV43dUlt7j%2FSbyK0q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDI%2Fw2%2Fgq8m01lZVCjyrcA4SYb3epyOcH53m1VRR2CbUsxPW1fsQXLiVl5IraJmRsOHpNIbpFkbG%2Fl2EEFiVj%2BivLD7lycReC8CzIWWXpxS6m2y3jMljl9%2BxBoiDJvO1PoUnUMjmm5QiVQHlSEqmfxBuKrWyIp%2FH2OOPNwLT1b8Sir0Y7StiRt3r3TJMAahSKNbovNE2T14%2BUX3w6LsMfYuuIlHz5%2FG5e%2FQvQghJS3vPu5F2ZJNGEx6Oz4ztzHw9A1iSLd9SWqu22SjPQUUunh7494t83Q9yNrVn3FBlVglYj%2F%2FdH70w7Dy24vyuQ8b8C5%2B7B5ZnAMdRbqjqP99flIsS%2BBOxgv72NstTKVGGDa3Js45vuQnekKklqCmYewX5ILBfARrwPn7ryzQ%2B8G2oK%2FXzQLVDmrY%2F2fZfVxez8KVlm0F72yCMGrpRMnPULd5F2o9LA%2Fak5roe2CX3EVGvz044%2BQLiISMoKagXZ3lyQ%2FqWeCb3PHgZFDA1oInGs3SDtme%2BA1XpBnidOpvyryL9xg4q%2Bw%2BQ4SbSFPWzFqTbf1fQqpzJaPfRJrxZKtLyRRY57ppL%2Ba3wQXGyFX%2FzZBx3RlMjLa359fjx90mnz3BdnIw0YmKvwfJ6WyEPjX%2FAMxEVABUA22%2FUEfwgjDUiyMJf%2Bmb0GOqUBcWjd%2F0E0jWAgI4gyDo2FYJeaEJ0uDN9DspE6Tturc%2ByfikMdrz782FIMtQeApXr7MNY%2BE3kQKALuqxa%2FEbtql4OAWauuiUxLZ9IOZ2hbfKFSAuRkAktpP3a6az8tLWzl3T071k02BpDNlLzHVWgQpjzaD4l%2FIKpp9ThG6MeJ16dsDGaxbj3SDvn1YydAB7YGzv%2BMvN2qFE%2BqsMq0w3AsnYBvP833&X-Amz-Signature=8459d8f64a63699738047b4bd6ae8fb44724f0748a6ecf6c25344c829d309ebc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RPQ6XBT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIGZlZnkAv0EiNwu%2BLED%2BRN16tdeXUFpubShjCZdnYg0iAiEA4gc26A750%2FEsvpwTTUS8RQsLm1ltV43dUlt7j%2FSbyK0q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDI%2Fw2%2Fgq8m01lZVCjyrcA4SYb3epyOcH53m1VRR2CbUsxPW1fsQXLiVl5IraJmRsOHpNIbpFkbG%2Fl2EEFiVj%2BivLD7lycReC8CzIWWXpxS6m2y3jMljl9%2BxBoiDJvO1PoUnUMjmm5QiVQHlSEqmfxBuKrWyIp%2FH2OOPNwLT1b8Sir0Y7StiRt3r3TJMAahSKNbovNE2T14%2BUX3w6LsMfYuuIlHz5%2FG5e%2FQvQghJS3vPu5F2ZJNGEx6Oz4ztzHw9A1iSLd9SWqu22SjPQUUunh7494t83Q9yNrVn3FBlVglYj%2F%2FdH70w7Dy24vyuQ8b8C5%2B7B5ZnAMdRbqjqP99flIsS%2BBOxgv72NstTKVGGDa3Js45vuQnekKklqCmYewX5ILBfARrwPn7ryzQ%2B8G2oK%2FXzQLVDmrY%2F2fZfVxez8KVlm0F72yCMGrpRMnPULd5F2o9LA%2Fak5roe2CX3EVGvz044%2BQLiISMoKagXZ3lyQ%2FqWeCb3PHgZFDA1oInGs3SDtme%2BA1XpBnidOpvyryL9xg4q%2Bw%2BQ4SbSFPWzFqTbf1fQqpzJaPfRJrxZKtLyRRY57ppL%2Ba3wQXGyFX%2FzZBx3RlMjLa359fjx90mnz3BdnIw0YmKvwfJ6WyEPjX%2FAMxEVABUA22%2FUEfwgjDUiyMJf%2Bmb0GOqUBcWjd%2F0E0jWAgI4gyDo2FYJeaEJ0uDN9DspE6Tturc%2ByfikMdrz782FIMtQeApXr7MNY%2BE3kQKALuqxa%2FEbtql4OAWauuiUxLZ9IOZ2hbfKFSAuRkAktpP3a6az8tLWzl3T071k02BpDNlLzHVWgQpjzaD4l%2FIKpp9ThG6MeJ16dsDGaxbj3SDvn1YydAB7YGzv%2BMvN2qFE%2BqsMq0w3AsnYBvP833&X-Amz-Signature=faa78e80fb440cf2a10c72540154ae4fab932f8efbfe1f56ed830ee407a8a902&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RPQ6XBT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIGZlZnkAv0EiNwu%2BLED%2BRN16tdeXUFpubShjCZdnYg0iAiEA4gc26A750%2FEsvpwTTUS8RQsLm1ltV43dUlt7j%2FSbyK0q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDI%2Fw2%2Fgq8m01lZVCjyrcA4SYb3epyOcH53m1VRR2CbUsxPW1fsQXLiVl5IraJmRsOHpNIbpFkbG%2Fl2EEFiVj%2BivLD7lycReC8CzIWWXpxS6m2y3jMljl9%2BxBoiDJvO1PoUnUMjmm5QiVQHlSEqmfxBuKrWyIp%2FH2OOPNwLT1b8Sir0Y7StiRt3r3TJMAahSKNbovNE2T14%2BUX3w6LsMfYuuIlHz5%2FG5e%2FQvQghJS3vPu5F2ZJNGEx6Oz4ztzHw9A1iSLd9SWqu22SjPQUUunh7494t83Q9yNrVn3FBlVglYj%2F%2FdH70w7Dy24vyuQ8b8C5%2B7B5ZnAMdRbqjqP99flIsS%2BBOxgv72NstTKVGGDa3Js45vuQnekKklqCmYewX5ILBfARrwPn7ryzQ%2B8G2oK%2FXzQLVDmrY%2F2fZfVxez8KVlm0F72yCMGrpRMnPULd5F2o9LA%2Fak5roe2CX3EVGvz044%2BQLiISMoKagXZ3lyQ%2FqWeCb3PHgZFDA1oInGs3SDtme%2BA1XpBnidOpvyryL9xg4q%2Bw%2BQ4SbSFPWzFqTbf1fQqpzJaPfRJrxZKtLyRRY57ppL%2Ba3wQXGyFX%2FzZBx3RlMjLa359fjx90mnz3BdnIw0YmKvwfJ6WyEPjX%2FAMxEVABUA22%2FUEfwgjDUiyMJf%2Bmb0GOqUBcWjd%2F0E0jWAgI4gyDo2FYJeaEJ0uDN9DspE6Tturc%2ByfikMdrz782FIMtQeApXr7MNY%2BE3kQKALuqxa%2FEbtql4OAWauuiUxLZ9IOZ2hbfKFSAuRkAktpP3a6az8tLWzl3T071k02BpDNlLzHVWgQpjzaD4l%2FIKpp9ThG6MeJ16dsDGaxbj3SDvn1YydAB7YGzv%2BMvN2qFE%2BqsMq0w3AsnYBvP833&X-Amz-Signature=cf4aaa16ad91cf738436c45b5b4b0bbef8f42944d33d4a10fc34c6afe1e56d5b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RPQ6XBT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIGZlZnkAv0EiNwu%2BLED%2BRN16tdeXUFpubShjCZdnYg0iAiEA4gc26A750%2FEsvpwTTUS8RQsLm1ltV43dUlt7j%2FSbyK0q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDI%2Fw2%2Fgq8m01lZVCjyrcA4SYb3epyOcH53m1VRR2CbUsxPW1fsQXLiVl5IraJmRsOHpNIbpFkbG%2Fl2EEFiVj%2BivLD7lycReC8CzIWWXpxS6m2y3jMljl9%2BxBoiDJvO1PoUnUMjmm5QiVQHlSEqmfxBuKrWyIp%2FH2OOPNwLT1b8Sir0Y7StiRt3r3TJMAahSKNbovNE2T14%2BUX3w6LsMfYuuIlHz5%2FG5e%2FQvQghJS3vPu5F2ZJNGEx6Oz4ztzHw9A1iSLd9SWqu22SjPQUUunh7494t83Q9yNrVn3FBlVglYj%2F%2FdH70w7Dy24vyuQ8b8C5%2B7B5ZnAMdRbqjqP99flIsS%2BBOxgv72NstTKVGGDa3Js45vuQnekKklqCmYewX5ILBfARrwPn7ryzQ%2B8G2oK%2FXzQLVDmrY%2F2fZfVxez8KVlm0F72yCMGrpRMnPULd5F2o9LA%2Fak5roe2CX3EVGvz044%2BQLiISMoKagXZ3lyQ%2FqWeCb3PHgZFDA1oInGs3SDtme%2BA1XpBnidOpvyryL9xg4q%2Bw%2BQ4SbSFPWzFqTbf1fQqpzJaPfRJrxZKtLyRRY57ppL%2Ba3wQXGyFX%2FzZBx3RlMjLa359fjx90mnz3BdnIw0YmKvwfJ6WyEPjX%2FAMxEVABUA22%2FUEfwgjDUiyMJf%2Bmb0GOqUBcWjd%2F0E0jWAgI4gyDo2FYJeaEJ0uDN9DspE6Tturc%2ByfikMdrz782FIMtQeApXr7MNY%2BE3kQKALuqxa%2FEbtql4OAWauuiUxLZ9IOZ2hbfKFSAuRkAktpP3a6az8tLWzl3T071k02BpDNlLzHVWgQpjzaD4l%2FIKpp9ThG6MeJ16dsDGaxbj3SDvn1YydAB7YGzv%2BMvN2qFE%2BqsMq0w3AsnYBvP833&X-Amz-Signature=2003ecadcf5fc0ca857604991f12dcb41a5da80ffdea8ae9eb6149e806df2578&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS5QAN4Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEJOKQKDVDufmxhEByfQz68YMJQQNirTooLY2fXtuEJwAiEAm%2FHPO8rDIAvIcVaec%2Fe%2BCqkKUHpXlvjLj1EAXCwDC1wq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDK9MZVCRmsACwg5NCrcA7OUNccSXV3FF%2F0KPCAzt1BE0JqmY6AVB%2BhuiQvci6u98SpoDZnthlgBMB1M1pzpr8lE5XqlUcsE51oola6XtBy95eBlsmxi0YmvF%2Bdt2Y8gmc1E9bIUpddiTFfLWKVmX4LnqLUs48FLuDpUYjzKuqVoAhPagu5YPI82AwlFsQl5HlJVKkYsYmfegvSq6Mr2oWiK%2FOvkr6caGTeZYilQrC1hYNv7VEEef9pg0pAs46XDEkcwHF9TIs%2B8zeGTJUlD1CFLjYrarjFH4wijib4e%2Fm%2F4k38C52Bvpg0nkVaGnJNhEAdadhWbBt4ExdRoDWqhviJ2541ZB7JH0QuUQypc1T36pwmRAb6mXl99HIoNPGG%2BwKnENdwayeMMOnOkHQg4qInJda%2BZPQCy09Yl60W7t6b0XFgE7iSd0h4%2BVvbbIP8hYsLENmMuVGTlzg5C8iYi9JwBuHlTUI%2BaGHRlbGU4oKUQMa8G1uqbl5FJ2r0FbZRElXU8ZyKakWAruQGDwHXCUCLWMZD0plk%2B1eqQsWeccFHcMr1lTqamLEZ2R%2FsISWFi%2FWFd%2BsmVPz9Sw8VlubGDHPtXE533RAagnjWIQxS435h5epuKhJ35p591c5PdtMH0Zmt3Dt6O6n3kXLdTMNz%2Bmb0GOqUB4J%2FFAJZCI2nzrRB3owecgCDU0zMifsZrGus18LYV%2BKf6FHRlUA2CYVaSgABhkL6jC6jB%2FzT0Gp%2BiXphiN2ecX8SPeV%2FJP7awyRlABtShT5EvzWgU2lzwvgCXHhlskzYScoPatiLEUBiptk0TzUiH2pYDfc7Zyc68CIN9qklGEayI4LKPbhJHXM4drYDUI%2FhJ8mpPZH2VOywIxH7OjAD%2FBb%2BrXIDn&X-Amz-Signature=b49ce195eeb0f752bb51983e28cda3ad83bc10669402952ac1db9df3be06c0cf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS5QAN4Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEJOKQKDVDufmxhEByfQz68YMJQQNirTooLY2fXtuEJwAiEAm%2FHPO8rDIAvIcVaec%2Fe%2BCqkKUHpXlvjLj1EAXCwDC1wq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDK9MZVCRmsACwg5NCrcA7OUNccSXV3FF%2F0KPCAzt1BE0JqmY6AVB%2BhuiQvci6u98SpoDZnthlgBMB1M1pzpr8lE5XqlUcsE51oola6XtBy95eBlsmxi0YmvF%2Bdt2Y8gmc1E9bIUpddiTFfLWKVmX4LnqLUs48FLuDpUYjzKuqVoAhPagu5YPI82AwlFsQl5HlJVKkYsYmfegvSq6Mr2oWiK%2FOvkr6caGTeZYilQrC1hYNv7VEEef9pg0pAs46XDEkcwHF9TIs%2B8zeGTJUlD1CFLjYrarjFH4wijib4e%2Fm%2F4k38C52Bvpg0nkVaGnJNhEAdadhWbBt4ExdRoDWqhviJ2541ZB7JH0QuUQypc1T36pwmRAb6mXl99HIoNPGG%2BwKnENdwayeMMOnOkHQg4qInJda%2BZPQCy09Yl60W7t6b0XFgE7iSd0h4%2BVvbbIP8hYsLENmMuVGTlzg5C8iYi9JwBuHlTUI%2BaGHRlbGU4oKUQMa8G1uqbl5FJ2r0FbZRElXU8ZyKakWAruQGDwHXCUCLWMZD0plk%2B1eqQsWeccFHcMr1lTqamLEZ2R%2FsISWFi%2FWFd%2BsmVPz9Sw8VlubGDHPtXE533RAagnjWIQxS435h5epuKhJ35p591c5PdtMH0Zmt3Dt6O6n3kXLdTMNz%2Bmb0GOqUB4J%2FFAJZCI2nzrRB3owecgCDU0zMifsZrGus18LYV%2BKf6FHRlUA2CYVaSgABhkL6jC6jB%2FzT0Gp%2BiXphiN2ecX8SPeV%2FJP7awyRlABtShT5EvzWgU2lzwvgCXHhlskzYScoPatiLEUBiptk0TzUiH2pYDfc7Zyc68CIN9qklGEayI4LKPbhJHXM4drYDUI%2FhJ8mpPZH2VOywIxH7OjAD%2FBb%2BrXIDn&X-Amz-Signature=c91fde333a8158648da71326c90c65c09a0e32ab6a7527e634320b7e3785ca10&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS5QAN4Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEJOKQKDVDufmxhEByfQz68YMJQQNirTooLY2fXtuEJwAiEAm%2FHPO8rDIAvIcVaec%2Fe%2BCqkKUHpXlvjLj1EAXCwDC1wq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDK9MZVCRmsACwg5NCrcA7OUNccSXV3FF%2F0KPCAzt1BE0JqmY6AVB%2BhuiQvci6u98SpoDZnthlgBMB1M1pzpr8lE5XqlUcsE51oola6XtBy95eBlsmxi0YmvF%2Bdt2Y8gmc1E9bIUpddiTFfLWKVmX4LnqLUs48FLuDpUYjzKuqVoAhPagu5YPI82AwlFsQl5HlJVKkYsYmfegvSq6Mr2oWiK%2FOvkr6caGTeZYilQrC1hYNv7VEEef9pg0pAs46XDEkcwHF9TIs%2B8zeGTJUlD1CFLjYrarjFH4wijib4e%2Fm%2F4k38C52Bvpg0nkVaGnJNhEAdadhWbBt4ExdRoDWqhviJ2541ZB7JH0QuUQypc1T36pwmRAb6mXl99HIoNPGG%2BwKnENdwayeMMOnOkHQg4qInJda%2BZPQCy09Yl60W7t6b0XFgE7iSd0h4%2BVvbbIP8hYsLENmMuVGTlzg5C8iYi9JwBuHlTUI%2BaGHRlbGU4oKUQMa8G1uqbl5FJ2r0FbZRElXU8ZyKakWAruQGDwHXCUCLWMZD0plk%2B1eqQsWeccFHcMr1lTqamLEZ2R%2FsISWFi%2FWFd%2BsmVPz9Sw8VlubGDHPtXE533RAagnjWIQxS435h5epuKhJ35p591c5PdtMH0Zmt3Dt6O6n3kXLdTMNz%2Bmb0GOqUB4J%2FFAJZCI2nzrRB3owecgCDU0zMifsZrGus18LYV%2BKf6FHRlUA2CYVaSgABhkL6jC6jB%2FzT0Gp%2BiXphiN2ecX8SPeV%2FJP7awyRlABtShT5EvzWgU2lzwvgCXHhlskzYScoPatiLEUBiptk0TzUiH2pYDfc7Zyc68CIN9qklGEayI4LKPbhJHXM4drYDUI%2FhJ8mpPZH2VOywIxH7OjAD%2FBb%2BrXIDn&X-Amz-Signature=8cbccd322936ba62b91ce538f10909d8111036e300b1ddad6252107b68af9a55&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS5QAN4Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEJOKQKDVDufmxhEByfQz68YMJQQNirTooLY2fXtuEJwAiEAm%2FHPO8rDIAvIcVaec%2Fe%2BCqkKUHpXlvjLj1EAXCwDC1wq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDK9MZVCRmsACwg5NCrcA7OUNccSXV3FF%2F0KPCAzt1BE0JqmY6AVB%2BhuiQvci6u98SpoDZnthlgBMB1M1pzpr8lE5XqlUcsE51oola6XtBy95eBlsmxi0YmvF%2Bdt2Y8gmc1E9bIUpddiTFfLWKVmX4LnqLUs48FLuDpUYjzKuqVoAhPagu5YPI82AwlFsQl5HlJVKkYsYmfegvSq6Mr2oWiK%2FOvkr6caGTeZYilQrC1hYNv7VEEef9pg0pAs46XDEkcwHF9TIs%2B8zeGTJUlD1CFLjYrarjFH4wijib4e%2Fm%2F4k38C52Bvpg0nkVaGnJNhEAdadhWbBt4ExdRoDWqhviJ2541ZB7JH0QuUQypc1T36pwmRAb6mXl99HIoNPGG%2BwKnENdwayeMMOnOkHQg4qInJda%2BZPQCy09Yl60W7t6b0XFgE7iSd0h4%2BVvbbIP8hYsLENmMuVGTlzg5C8iYi9JwBuHlTUI%2BaGHRlbGU4oKUQMa8G1uqbl5FJ2r0FbZRElXU8ZyKakWAruQGDwHXCUCLWMZD0plk%2B1eqQsWeccFHcMr1lTqamLEZ2R%2FsISWFi%2FWFd%2BsmVPz9Sw8VlubGDHPtXE533RAagnjWIQxS435h5epuKhJ35p591c5PdtMH0Zmt3Dt6O6n3kXLdTMNz%2Bmb0GOqUB4J%2FFAJZCI2nzrRB3owecgCDU0zMifsZrGus18LYV%2BKf6FHRlUA2CYVaSgABhkL6jC6jB%2FzT0Gp%2BiXphiN2ecX8SPeV%2FJP7awyRlABtShT5EvzWgU2lzwvgCXHhlskzYScoPatiLEUBiptk0TzUiH2pYDfc7Zyc68CIN9qklGEayI4LKPbhJHXM4drYDUI%2FhJ8mpPZH2VOywIxH7OjAD%2FBb%2BrXIDn&X-Amz-Signature=bc9875f0b805bbf75e6cfe2e638a9c770f42394aaae0434a7d0fe2e304cbe2e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS5QAN4Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEJOKQKDVDufmxhEByfQz68YMJQQNirTooLY2fXtuEJwAiEAm%2FHPO8rDIAvIcVaec%2Fe%2BCqkKUHpXlvjLj1EAXCwDC1wq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDK9MZVCRmsACwg5NCrcA7OUNccSXV3FF%2F0KPCAzt1BE0JqmY6AVB%2BhuiQvci6u98SpoDZnthlgBMB1M1pzpr8lE5XqlUcsE51oola6XtBy95eBlsmxi0YmvF%2Bdt2Y8gmc1E9bIUpddiTFfLWKVmX4LnqLUs48FLuDpUYjzKuqVoAhPagu5YPI82AwlFsQl5HlJVKkYsYmfegvSq6Mr2oWiK%2FOvkr6caGTeZYilQrC1hYNv7VEEef9pg0pAs46XDEkcwHF9TIs%2B8zeGTJUlD1CFLjYrarjFH4wijib4e%2Fm%2F4k38C52Bvpg0nkVaGnJNhEAdadhWbBt4ExdRoDWqhviJ2541ZB7JH0QuUQypc1T36pwmRAb6mXl99HIoNPGG%2BwKnENdwayeMMOnOkHQg4qInJda%2BZPQCy09Yl60W7t6b0XFgE7iSd0h4%2BVvbbIP8hYsLENmMuVGTlzg5C8iYi9JwBuHlTUI%2BaGHRlbGU4oKUQMa8G1uqbl5FJ2r0FbZRElXU8ZyKakWAruQGDwHXCUCLWMZD0plk%2B1eqQsWeccFHcMr1lTqamLEZ2R%2FsISWFi%2FWFd%2BsmVPz9Sw8VlubGDHPtXE533RAagnjWIQxS435h5epuKhJ35p591c5PdtMH0Zmt3Dt6O6n3kXLdTMNz%2Bmb0GOqUB4J%2FFAJZCI2nzrRB3owecgCDU0zMifsZrGus18LYV%2BKf6FHRlUA2CYVaSgABhkL6jC6jB%2FzT0Gp%2BiXphiN2ecX8SPeV%2FJP7awyRlABtShT5EvzWgU2lzwvgCXHhlskzYScoPatiLEUBiptk0TzUiH2pYDfc7Zyc68CIN9qklGEayI4LKPbhJHXM4drYDUI%2FhJ8mpPZH2VOywIxH7OjAD%2FBb%2BrXIDn&X-Amz-Signature=59e57f5fe148fa06f4b23e78f69449e9bbb3e18e991cca1220bad6b9df35f7f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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


