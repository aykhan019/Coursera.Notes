

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKCOSOAG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoWhaa%2B3RceC6F0KOXAnwwUckKyqatKb51QtAXXNrHwAiB%2Bj994bGX10GuetkP6qX6DF8g3HiddpeCpENwfNxZ5PSqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMnXBvvTIuwsIAW91KtwDjoZD%2F0qk9C3sb8UrMPtQzZPcA8iG7s0nAaUJx%2BUmWxlhJTHJujqZGAoKleoDT4ZX1Jnk7o%2Fruq7Tl4FUuXB0kTkU6Zi7%2B0h8Dkv1D4uTiR1HKznVTsbvipVzxXdZ0BlJqkX%2FOgZgzFDAkUAxwp%2BJbv4DD6zi7ltdC7UY3eKpZV1fdMAX4CtZHxyn5dASdNo1P6svHvTRgzb4jdHAaF1XHdHTdGg0CvOOdrUeKp0qp5qc%2Fd1ezEcM2NmhjDoqbijRFJ0BXX4cooRY74hX04ReM9PRzL77EOVzEBFtX8m4euIKudYDsj5yY%2FRtUKzziUZApP8tMtjRhubdLYERV4PwfEhtgD5ldZPF%2Bj21cP7JhZB5%2FPWDySRJIwCgEZ8E4wLaoHnXx2zvv29POW9QDPOKBLuqIzbnArRtVunLVaavhk%2Bn2VWfboo3jeQc2qYMD7clDSQ68l0STo9CXhUc3tOQR64xTpcxVc8n8mg4ANAIybwcs5Sec4L9t6nY1QvLFQZ%2BxVXVsDlKxq3oN1xQ8djgnh54UnjSK%2B%2Figqasagbn0Dob%2Fx0Osc34bUvtY7jiYYp1PX0zwODOXx6xaELopdHQrTQaE3ta%2BeiZKGV%2B39jvRz59UyJ%2FvWytjIwo6Ncw7IPpvAY6pgHiGiUtNv5X7Pheb7YjxEIHILCDQ%2BcZVOP6PrM0X3Lu64zn82ppz%2BF6D5Si2ZElNF2Xv11R6mTWcP79TJLfc9vl5pHFI5KC%2BbrBGfDI5vktxbjhryfQLF1s3gY1bclsI1llCLqthTGtJT92QXhF1HF3vljLzLl6P7%2B5C1Q3TwpHdgJk4AJ388jtkGEbZPv7CBgh8Sw9vnp0LvT%2BHZ5Ghzwfy6WMZGIh&X-Amz-Signature=38bc9397b22bb7921c48ca3b85b36a527437e98219ba558ce34138149fc5aaf7&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXEOYBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPPiHMTf5SZUiw9E7927uswjM%2FFe2JE2tjJPZcCRpJawIhAN38FZVVneOI9Moyu5bHHVmk6d3W25KFflugrXqtBJtgKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmuche6gq%2BdCS3snkq3AMhr7YSuaZF1uko6Om0hAgoWlR%2FprO0a6mnjuTJ46WcycCs44DYmPxU5Li1HAIBXY4AAhiJ%2FvNXAtdJn3pUP3kRe%2FcLRvT5c32z7YYDjNRCzcNQVgAudRk8bjkUhaxxCpt0tH6w6L7q8OXxfjbhmFCv3MdZj4dyBZP1mPLWIQc7e%2FqlohDOVlUnwqXBc9mCriduuwfYGnKIh5Gpx4DBNqkiU4fsyKMP8arVEd73jrtCKCuG2fUO3%2BfDGvzWLLmej8xdxUtl79fHN8aW7D%2Fjc397xO7nMIORPabKXq5N0MEYwCSsMc9CRI8FReefap8fHYWL3wksjXfonm3iIujy2U1EkifD0GE3zAGoAM4icJSE%2Fwx%2F3UCUbUBz3rmCkpPIxSOsEspoPfaUKvuSZOSQ5TYNBQoP5qC%2BgXVo1NqLCkSUSo%2Fgjp3ZpsDV0ylUKjPfR0wFjrISwcrkyGHgpS9O6%2B%2BJ1suPq94dpF1qfinNQJcfqt1VaoLNuod4st6%2FP6bH5lA3mztku2KgReOMr6pMdhghxCFPkVuzs5v0QXdhgFUs9kyVexs1yA8OM9ZDF7krb1HtGPqlu%2FClQBg0rAxF3VgHcg69W70dyS6IQ%2BWfaAEfYBDErSdjXA5zTFGO1TCGhOm8BjqkAeV9r%2FeIslQn4WiVJapcRXcCgNGEnVOmywv22Xi3QTDbW4jLS9oGrnDbF2fG1m9OK7fuLTUDNIgn8GI76pDt0hQszqrdp5gjm0BN%2B0zXQwOn2yJkG0WzfXMmCF02cPd2viO4SletdytUKnBRd%2BW88oE39q%2FJd64YIm9QZ7tolfVwpLJm%2F3R3yH1DIU7fjqySeUFdfNwL2rPPAt0CT8M5agalvhMh&X-Amz-Signature=7a316657f9d86c0401e79db49d38c5b6dc7506f24ade8cb6b7ef7fc2133406af&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXEOYBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPPiHMTf5SZUiw9E7927uswjM%2FFe2JE2tjJPZcCRpJawIhAN38FZVVneOI9Moyu5bHHVmk6d3W25KFflugrXqtBJtgKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmuche6gq%2BdCS3snkq3AMhr7YSuaZF1uko6Om0hAgoWlR%2FprO0a6mnjuTJ46WcycCs44DYmPxU5Li1HAIBXY4AAhiJ%2FvNXAtdJn3pUP3kRe%2FcLRvT5c32z7YYDjNRCzcNQVgAudRk8bjkUhaxxCpt0tH6w6L7q8OXxfjbhmFCv3MdZj4dyBZP1mPLWIQc7e%2FqlohDOVlUnwqXBc9mCriduuwfYGnKIh5Gpx4DBNqkiU4fsyKMP8arVEd73jrtCKCuG2fUO3%2BfDGvzWLLmej8xdxUtl79fHN8aW7D%2Fjc397xO7nMIORPabKXq5N0MEYwCSsMc9CRI8FReefap8fHYWL3wksjXfonm3iIujy2U1EkifD0GE3zAGoAM4icJSE%2Fwx%2F3UCUbUBz3rmCkpPIxSOsEspoPfaUKvuSZOSQ5TYNBQoP5qC%2BgXVo1NqLCkSUSo%2Fgjp3ZpsDV0ylUKjPfR0wFjrISwcrkyGHgpS9O6%2B%2BJ1suPq94dpF1qfinNQJcfqt1VaoLNuod4st6%2FP6bH5lA3mztku2KgReOMr6pMdhghxCFPkVuzs5v0QXdhgFUs9kyVexs1yA8OM9ZDF7krb1HtGPqlu%2FClQBg0rAxF3VgHcg69W70dyS6IQ%2BWfaAEfYBDErSdjXA5zTFGO1TCGhOm8BjqkAeV9r%2FeIslQn4WiVJapcRXcCgNGEnVOmywv22Xi3QTDbW4jLS9oGrnDbF2fG1m9OK7fuLTUDNIgn8GI76pDt0hQszqrdp5gjm0BN%2B0zXQwOn2yJkG0WzfXMmCF02cPd2viO4SletdytUKnBRd%2BW88oE39q%2FJd64YIm9QZ7tolfVwpLJm%2F3R3yH1DIU7fjqySeUFdfNwL2rPPAt0CT8M5agalvhMh&X-Amz-Signature=b3273ebd89c702cb0b26520a44a4842ad5211c1614ebce629ac30b515bed85f8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXEOYBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPPiHMTf5SZUiw9E7927uswjM%2FFe2JE2tjJPZcCRpJawIhAN38FZVVneOI9Moyu5bHHVmk6d3W25KFflugrXqtBJtgKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmuche6gq%2BdCS3snkq3AMhr7YSuaZF1uko6Om0hAgoWlR%2FprO0a6mnjuTJ46WcycCs44DYmPxU5Li1HAIBXY4AAhiJ%2FvNXAtdJn3pUP3kRe%2FcLRvT5c32z7YYDjNRCzcNQVgAudRk8bjkUhaxxCpt0tH6w6L7q8OXxfjbhmFCv3MdZj4dyBZP1mPLWIQc7e%2FqlohDOVlUnwqXBc9mCriduuwfYGnKIh5Gpx4DBNqkiU4fsyKMP8arVEd73jrtCKCuG2fUO3%2BfDGvzWLLmej8xdxUtl79fHN8aW7D%2Fjc397xO7nMIORPabKXq5N0MEYwCSsMc9CRI8FReefap8fHYWL3wksjXfonm3iIujy2U1EkifD0GE3zAGoAM4icJSE%2Fwx%2F3UCUbUBz3rmCkpPIxSOsEspoPfaUKvuSZOSQ5TYNBQoP5qC%2BgXVo1NqLCkSUSo%2Fgjp3ZpsDV0ylUKjPfR0wFjrISwcrkyGHgpS9O6%2B%2BJ1suPq94dpF1qfinNQJcfqt1VaoLNuod4st6%2FP6bH5lA3mztku2KgReOMr6pMdhghxCFPkVuzs5v0QXdhgFUs9kyVexs1yA8OM9ZDF7krb1HtGPqlu%2FClQBg0rAxF3VgHcg69W70dyS6IQ%2BWfaAEfYBDErSdjXA5zTFGO1TCGhOm8BjqkAeV9r%2FeIslQn4WiVJapcRXcCgNGEnVOmywv22Xi3QTDbW4jLS9oGrnDbF2fG1m9OK7fuLTUDNIgn8GI76pDt0hQszqrdp5gjm0BN%2B0zXQwOn2yJkG0WzfXMmCF02cPd2viO4SletdytUKnBRd%2BW88oE39q%2FJd64YIm9QZ7tolfVwpLJm%2F3R3yH1DIU7fjqySeUFdfNwL2rPPAt0CT8M5agalvhMh&X-Amz-Signature=fa85ed1fddfdba9b70f14e263defe70a5795de7ab22e1bf1574e7ca04233d4fc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXEOYBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPPiHMTf5SZUiw9E7927uswjM%2FFe2JE2tjJPZcCRpJawIhAN38FZVVneOI9Moyu5bHHVmk6d3W25KFflugrXqtBJtgKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmuche6gq%2BdCS3snkq3AMhr7YSuaZF1uko6Om0hAgoWlR%2FprO0a6mnjuTJ46WcycCs44DYmPxU5Li1HAIBXY4AAhiJ%2FvNXAtdJn3pUP3kRe%2FcLRvT5c32z7YYDjNRCzcNQVgAudRk8bjkUhaxxCpt0tH6w6L7q8OXxfjbhmFCv3MdZj4dyBZP1mPLWIQc7e%2FqlohDOVlUnwqXBc9mCriduuwfYGnKIh5Gpx4DBNqkiU4fsyKMP8arVEd73jrtCKCuG2fUO3%2BfDGvzWLLmej8xdxUtl79fHN8aW7D%2Fjc397xO7nMIORPabKXq5N0MEYwCSsMc9CRI8FReefap8fHYWL3wksjXfonm3iIujy2U1EkifD0GE3zAGoAM4icJSE%2Fwx%2F3UCUbUBz3rmCkpPIxSOsEspoPfaUKvuSZOSQ5TYNBQoP5qC%2BgXVo1NqLCkSUSo%2Fgjp3ZpsDV0ylUKjPfR0wFjrISwcrkyGHgpS9O6%2B%2BJ1suPq94dpF1qfinNQJcfqt1VaoLNuod4st6%2FP6bH5lA3mztku2KgReOMr6pMdhghxCFPkVuzs5v0QXdhgFUs9kyVexs1yA8OM9ZDF7krb1HtGPqlu%2FClQBg0rAxF3VgHcg69W70dyS6IQ%2BWfaAEfYBDErSdjXA5zTFGO1TCGhOm8BjqkAeV9r%2FeIslQn4WiVJapcRXcCgNGEnVOmywv22Xi3QTDbW4jLS9oGrnDbF2fG1m9OK7fuLTUDNIgn8GI76pDt0hQszqrdp5gjm0BN%2B0zXQwOn2yJkG0WzfXMmCF02cPd2viO4SletdytUKnBRd%2BW88oE39q%2FJd64YIm9QZ7tolfVwpLJm%2F3R3yH1DIU7fjqySeUFdfNwL2rPPAt0CT8M5agalvhMh&X-Amz-Signature=b9ab23b72af5757d0866289f4a876c5f905909a97aa938f626e7f9071d66e96d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIXEOYBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPPiHMTf5SZUiw9E7927uswjM%2FFe2JE2tjJPZcCRpJawIhAN38FZVVneOI9Moyu5bHHVmk6d3W25KFflugrXqtBJtgKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmuche6gq%2BdCS3snkq3AMhr7YSuaZF1uko6Om0hAgoWlR%2FprO0a6mnjuTJ46WcycCs44DYmPxU5Li1HAIBXY4AAhiJ%2FvNXAtdJn3pUP3kRe%2FcLRvT5c32z7YYDjNRCzcNQVgAudRk8bjkUhaxxCpt0tH6w6L7q8OXxfjbhmFCv3MdZj4dyBZP1mPLWIQc7e%2FqlohDOVlUnwqXBc9mCriduuwfYGnKIh5Gpx4DBNqkiU4fsyKMP8arVEd73jrtCKCuG2fUO3%2BfDGvzWLLmej8xdxUtl79fHN8aW7D%2Fjc397xO7nMIORPabKXq5N0MEYwCSsMc9CRI8FReefap8fHYWL3wksjXfonm3iIujy2U1EkifD0GE3zAGoAM4icJSE%2Fwx%2F3UCUbUBz3rmCkpPIxSOsEspoPfaUKvuSZOSQ5TYNBQoP5qC%2BgXVo1NqLCkSUSo%2Fgjp3ZpsDV0ylUKjPfR0wFjrISwcrkyGHgpS9O6%2B%2BJ1suPq94dpF1qfinNQJcfqt1VaoLNuod4st6%2FP6bH5lA3mztku2KgReOMr6pMdhghxCFPkVuzs5v0QXdhgFUs9kyVexs1yA8OM9ZDF7krb1HtGPqlu%2FClQBg0rAxF3VgHcg69W70dyS6IQ%2BWfaAEfYBDErSdjXA5zTFGO1TCGhOm8BjqkAeV9r%2FeIslQn4WiVJapcRXcCgNGEnVOmywv22Xi3QTDbW4jLS9oGrnDbF2fG1m9OK7fuLTUDNIgn8GI76pDt0hQszqrdp5gjm0BN%2B0zXQwOn2yJkG0WzfXMmCF02cPd2viO4SletdytUKnBRd%2BW88oE39q%2FJd64YIm9QZ7tolfVwpLJm%2F3R3yH1DIU7fjqySeUFdfNwL2rPPAt0CT8M5agalvhMh&X-Amz-Signature=8f386271d9ec2479b5941ccb4930b8711ac3b9be897f0d6b1652874f00c88447&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKCOSOAG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoWhaa%2B3RceC6F0KOXAnwwUckKyqatKb51QtAXXNrHwAiB%2Bj994bGX10GuetkP6qX6DF8g3HiddpeCpENwfNxZ5PSqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMnXBvvTIuwsIAW91KtwDjoZD%2F0qk9C3sb8UrMPtQzZPcA8iG7s0nAaUJx%2BUmWxlhJTHJujqZGAoKleoDT4ZX1Jnk7o%2Fruq7Tl4FUuXB0kTkU6Zi7%2B0h8Dkv1D4uTiR1HKznVTsbvipVzxXdZ0BlJqkX%2FOgZgzFDAkUAxwp%2BJbv4DD6zi7ltdC7UY3eKpZV1fdMAX4CtZHxyn5dASdNo1P6svHvTRgzb4jdHAaF1XHdHTdGg0CvOOdrUeKp0qp5qc%2Fd1ezEcM2NmhjDoqbijRFJ0BXX4cooRY74hX04ReM9PRzL77EOVzEBFtX8m4euIKudYDsj5yY%2FRtUKzziUZApP8tMtjRhubdLYERV4PwfEhtgD5ldZPF%2Bj21cP7JhZB5%2FPWDySRJIwCgEZ8E4wLaoHnXx2zvv29POW9QDPOKBLuqIzbnArRtVunLVaavhk%2Bn2VWfboo3jeQc2qYMD7clDSQ68l0STo9CXhUc3tOQR64xTpcxVc8n8mg4ANAIybwcs5Sec4L9t6nY1QvLFQZ%2BxVXVsDlKxq3oN1xQ8djgnh54UnjSK%2B%2Figqasagbn0Dob%2Fx0Osc34bUvtY7jiYYp1PX0zwODOXx6xaELopdHQrTQaE3ta%2BeiZKGV%2B39jvRz59UyJ%2FvWytjIwo6Ncw7IPpvAY6pgHiGiUtNv5X7Pheb7YjxEIHILCDQ%2BcZVOP6PrM0X3Lu64zn82ppz%2BF6D5Si2ZElNF2Xv11R6mTWcP79TJLfc9vl5pHFI5KC%2BbrBGfDI5vktxbjhryfQLF1s3gY1bclsI1llCLqthTGtJT92QXhF1HF3vljLzLl6P7%2B5C1Q3TwpHdgJk4AJ388jtkGEbZPv7CBgh8Sw9vnp0LvT%2BHZ5Ghzwfy6WMZGIh&X-Amz-Signature=6147a149a490b0020cca5f79ab89bc03e38c70dae9b6ddccac681895d620a613&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKCOSOAG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoWhaa%2B3RceC6F0KOXAnwwUckKyqatKb51QtAXXNrHwAiB%2Bj994bGX10GuetkP6qX6DF8g3HiddpeCpENwfNxZ5PSqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMnXBvvTIuwsIAW91KtwDjoZD%2F0qk9C3sb8UrMPtQzZPcA8iG7s0nAaUJx%2BUmWxlhJTHJujqZGAoKleoDT4ZX1Jnk7o%2Fruq7Tl4FUuXB0kTkU6Zi7%2B0h8Dkv1D4uTiR1HKznVTsbvipVzxXdZ0BlJqkX%2FOgZgzFDAkUAxwp%2BJbv4DD6zi7ltdC7UY3eKpZV1fdMAX4CtZHxyn5dASdNo1P6svHvTRgzb4jdHAaF1XHdHTdGg0CvOOdrUeKp0qp5qc%2Fd1ezEcM2NmhjDoqbijRFJ0BXX4cooRY74hX04ReM9PRzL77EOVzEBFtX8m4euIKudYDsj5yY%2FRtUKzziUZApP8tMtjRhubdLYERV4PwfEhtgD5ldZPF%2Bj21cP7JhZB5%2FPWDySRJIwCgEZ8E4wLaoHnXx2zvv29POW9QDPOKBLuqIzbnArRtVunLVaavhk%2Bn2VWfboo3jeQc2qYMD7clDSQ68l0STo9CXhUc3tOQR64xTpcxVc8n8mg4ANAIybwcs5Sec4L9t6nY1QvLFQZ%2BxVXVsDlKxq3oN1xQ8djgnh54UnjSK%2B%2Figqasagbn0Dob%2Fx0Osc34bUvtY7jiYYp1PX0zwODOXx6xaELopdHQrTQaE3ta%2BeiZKGV%2B39jvRz59UyJ%2FvWytjIwo6Ncw7IPpvAY6pgHiGiUtNv5X7Pheb7YjxEIHILCDQ%2BcZVOP6PrM0X3Lu64zn82ppz%2BF6D5Si2ZElNF2Xv11R6mTWcP79TJLfc9vl5pHFI5KC%2BbrBGfDI5vktxbjhryfQLF1s3gY1bclsI1llCLqthTGtJT92QXhF1HF3vljLzLl6P7%2B5C1Q3TwpHdgJk4AJ388jtkGEbZPv7CBgh8Sw9vnp0LvT%2BHZ5Ghzwfy6WMZGIh&X-Amz-Signature=e6ae84590b137063140a78ddf793eb24a6b819f8423f287884275cc42c56f928&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKCOSOAG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoWhaa%2B3RceC6F0KOXAnwwUckKyqatKb51QtAXXNrHwAiB%2Bj994bGX10GuetkP6qX6DF8g3HiddpeCpENwfNxZ5PSqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMnXBvvTIuwsIAW91KtwDjoZD%2F0qk9C3sb8UrMPtQzZPcA8iG7s0nAaUJx%2BUmWxlhJTHJujqZGAoKleoDT4ZX1Jnk7o%2Fruq7Tl4FUuXB0kTkU6Zi7%2B0h8Dkv1D4uTiR1HKznVTsbvipVzxXdZ0BlJqkX%2FOgZgzFDAkUAxwp%2BJbv4DD6zi7ltdC7UY3eKpZV1fdMAX4CtZHxyn5dASdNo1P6svHvTRgzb4jdHAaF1XHdHTdGg0CvOOdrUeKp0qp5qc%2Fd1ezEcM2NmhjDoqbijRFJ0BXX4cooRY74hX04ReM9PRzL77EOVzEBFtX8m4euIKudYDsj5yY%2FRtUKzziUZApP8tMtjRhubdLYERV4PwfEhtgD5ldZPF%2Bj21cP7JhZB5%2FPWDySRJIwCgEZ8E4wLaoHnXx2zvv29POW9QDPOKBLuqIzbnArRtVunLVaavhk%2Bn2VWfboo3jeQc2qYMD7clDSQ68l0STo9CXhUc3tOQR64xTpcxVc8n8mg4ANAIybwcs5Sec4L9t6nY1QvLFQZ%2BxVXVsDlKxq3oN1xQ8djgnh54UnjSK%2B%2Figqasagbn0Dob%2Fx0Osc34bUvtY7jiYYp1PX0zwODOXx6xaELopdHQrTQaE3ta%2BeiZKGV%2B39jvRz59UyJ%2FvWytjIwo6Ncw7IPpvAY6pgHiGiUtNv5X7Pheb7YjxEIHILCDQ%2BcZVOP6PrM0X3Lu64zn82ppz%2BF6D5Si2ZElNF2Xv11R6mTWcP79TJLfc9vl5pHFI5KC%2BbrBGfDI5vktxbjhryfQLF1s3gY1bclsI1llCLqthTGtJT92QXhF1HF3vljLzLl6P7%2B5C1Q3TwpHdgJk4AJ388jtkGEbZPv7CBgh8Sw9vnp0LvT%2BHZ5Ghzwfy6WMZGIh&X-Amz-Signature=54ca8fad0c543de49c595a6908b6b2c24d89507d55c7c3123c07e5472bd8d599&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKCOSOAG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoWhaa%2B3RceC6F0KOXAnwwUckKyqatKb51QtAXXNrHwAiB%2Bj994bGX10GuetkP6qX6DF8g3HiddpeCpENwfNxZ5PSqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMnXBvvTIuwsIAW91KtwDjoZD%2F0qk9C3sb8UrMPtQzZPcA8iG7s0nAaUJx%2BUmWxlhJTHJujqZGAoKleoDT4ZX1Jnk7o%2Fruq7Tl4FUuXB0kTkU6Zi7%2B0h8Dkv1D4uTiR1HKznVTsbvipVzxXdZ0BlJqkX%2FOgZgzFDAkUAxwp%2BJbv4DD6zi7ltdC7UY3eKpZV1fdMAX4CtZHxyn5dASdNo1P6svHvTRgzb4jdHAaF1XHdHTdGg0CvOOdrUeKp0qp5qc%2Fd1ezEcM2NmhjDoqbijRFJ0BXX4cooRY74hX04ReM9PRzL77EOVzEBFtX8m4euIKudYDsj5yY%2FRtUKzziUZApP8tMtjRhubdLYERV4PwfEhtgD5ldZPF%2Bj21cP7JhZB5%2FPWDySRJIwCgEZ8E4wLaoHnXx2zvv29POW9QDPOKBLuqIzbnArRtVunLVaavhk%2Bn2VWfboo3jeQc2qYMD7clDSQ68l0STo9CXhUc3tOQR64xTpcxVc8n8mg4ANAIybwcs5Sec4L9t6nY1QvLFQZ%2BxVXVsDlKxq3oN1xQ8djgnh54UnjSK%2B%2Figqasagbn0Dob%2Fx0Osc34bUvtY7jiYYp1PX0zwODOXx6xaELopdHQrTQaE3ta%2BeiZKGV%2B39jvRz59UyJ%2FvWytjIwo6Ncw7IPpvAY6pgHiGiUtNv5X7Pheb7YjxEIHILCDQ%2BcZVOP6PrM0X3Lu64zn82ppz%2BF6D5Si2ZElNF2Xv11R6mTWcP79TJLfc9vl5pHFI5KC%2BbrBGfDI5vktxbjhryfQLF1s3gY1bclsI1llCLqthTGtJT92QXhF1HF3vljLzLl6P7%2B5C1Q3TwpHdgJk4AJ388jtkGEbZPv7CBgh8Sw9vnp0LvT%2BHZ5Ghzwfy6WMZGIh&X-Amz-Signature=cb1870beab9fe310160bec8575e867522cc17467fb587ebad4d87501d1f12beb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKCOSOAG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoWhaa%2B3RceC6F0KOXAnwwUckKyqatKb51QtAXXNrHwAiB%2Bj994bGX10GuetkP6qX6DF8g3HiddpeCpENwfNxZ5PSqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMnXBvvTIuwsIAW91KtwDjoZD%2F0qk9C3sb8UrMPtQzZPcA8iG7s0nAaUJx%2BUmWxlhJTHJujqZGAoKleoDT4ZX1Jnk7o%2Fruq7Tl4FUuXB0kTkU6Zi7%2B0h8Dkv1D4uTiR1HKznVTsbvipVzxXdZ0BlJqkX%2FOgZgzFDAkUAxwp%2BJbv4DD6zi7ltdC7UY3eKpZV1fdMAX4CtZHxyn5dASdNo1P6svHvTRgzb4jdHAaF1XHdHTdGg0CvOOdrUeKp0qp5qc%2Fd1ezEcM2NmhjDoqbijRFJ0BXX4cooRY74hX04ReM9PRzL77EOVzEBFtX8m4euIKudYDsj5yY%2FRtUKzziUZApP8tMtjRhubdLYERV4PwfEhtgD5ldZPF%2Bj21cP7JhZB5%2FPWDySRJIwCgEZ8E4wLaoHnXx2zvv29POW9QDPOKBLuqIzbnArRtVunLVaavhk%2Bn2VWfboo3jeQc2qYMD7clDSQ68l0STo9CXhUc3tOQR64xTpcxVc8n8mg4ANAIybwcs5Sec4L9t6nY1QvLFQZ%2BxVXVsDlKxq3oN1xQ8djgnh54UnjSK%2B%2Figqasagbn0Dob%2Fx0Osc34bUvtY7jiYYp1PX0zwODOXx6xaELopdHQrTQaE3ta%2BeiZKGV%2B39jvRz59UyJ%2FvWytjIwo6Ncw7IPpvAY6pgHiGiUtNv5X7Pheb7YjxEIHILCDQ%2BcZVOP6PrM0X3Lu64zn82ppz%2BF6D5Si2ZElNF2Xv11R6mTWcP79TJLfc9vl5pHFI5KC%2BbrBGfDI5vktxbjhryfQLF1s3gY1bclsI1llCLqthTGtJT92QXhF1HF3vljLzLl6P7%2B5C1Q3TwpHdgJk4AJ388jtkGEbZPv7CBgh8Sw9vnp0LvT%2BHZ5Ghzwfy6WMZGIh&X-Amz-Signature=6909c6e5f962cc88f8e4a0a1e7b032da5e75769cd8f2d05dcd691486e411a421&X-Amz-SignedHeaders=host&x-id=GetObject)
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


