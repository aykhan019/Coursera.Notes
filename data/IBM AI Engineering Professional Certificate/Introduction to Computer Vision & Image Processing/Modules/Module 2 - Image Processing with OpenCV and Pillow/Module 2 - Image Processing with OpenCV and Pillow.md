

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSTLUUBG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCSfU7II%2B4pXI%2BC%2BqBYo4gQEiF%2FYHdyvXiUpcY7Py%2F2tQIgc8PNuQo%2FhvposoMVr7ByME3fHO8Ppd6%2FACCuhEHnmMgq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAOS6OzSdSAIUk5XKyrcAzXrVI9OJajt%2F%2BOBIW831tSBGr8vLMbWB5GRaKfl24JzijTMX%2BzfTiDBWjqixMYKFU3btIpEpgH9Yhm22lR5ZarCwhgeGbUNssW%2FS%2Bti%2FXtz6G72B8UFcBjZvjLkzUR4qdSEfTAgz27oqvxRVdMHohzmvDExqJLScNY64eAPnggG31QjUN2G3RTOVuoEY3pZvzfv5hIgFcKFtmfrkw9xxsdMODHbToimix3huubGt%2BLJAHejba2WIWYKOU7%2Bpt4DVLPaoDqhl0ua4CEgPUWbdDcSVChapNhMvCa28Otit97RZNgHd7Xm4qltxBicyH%2F9V2bisjVOXD6lXrYC4hUl0fwoNgpas6X9gNEIGgL4gUcSf0VVog848On2snq%2BwM5X4oVTQLhRbPUBef2pR9UsYouUgBR0Q6VNXepavfgXcLx3opbFbKlfXN%2FQkv%2FkmRaPZFeVL44gXqejqLzBNNMRCMYdhAG%2B6X2Bf6WbWE4gtEjrghpy%2B0K3WMU0wzvOhODBZDBN4mVKXblz6F2w78O%2BcoLn4j0fnLGw8YtrYdaTXODZIWJvVqJa6Q6ArxDZu4Xvx9zOD2kCl4gDN8eEm7zUIyhsOO2L%2BMp5obpowQUDPgAt%2BCe9sPzCJgk71Y8aMKLNir0GOqUBVt7nx4ND2oC3Xnf4%2Fx1A5kdo7xjzEc0nQrRHbyOKHWsPiGrnWVwYGwxZndgoZHPf4trkQX%2FCJDLsqdUg9y34hweHAcY3ByTwBeEG3WGw%2F7kaRrSykCvutEtOVjpq2NhJSnQEqPKRGqfk7%2FHmbeXs4r8NI1QaIKBB08tD6S6IhvwgH5xWD9ux03sqOk9aZJze1HhyaDsPhc31xjdfMoNGCn4yKnAw&X-Amz-Signature=afcd25a4535dac7d5c5d028337517af473537046d2d0a9a3963930670a78675c&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YG5ZKDDA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCWfncB9jzncn6ycC5P2wo5s08BymDgjY1avnMqn%2FL3sQIgYxnRk1Vp1L4z%2BSz3QLpI1Fyw2SMgrZBhYP4nBBtCo6Aq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDHtcvfpHaKIzYP5d5yrcA2fsBmKZsrXMnubKhal3mQkGJ%2Bv1beUjx3oOxwEOWaPZjq7vqIhMcNz9fNJ0T6tUX4vKIB8EhMaVjhNTvfGElWkDrIHq2cv4fd68X%2Fpr5o3mOofknRlPCWLIt84dhWj%2FQ7acZODWitieMO91FlokCHAXAuUXi7S9gb2fJUEusQDG8UVV%2F6g60f%2FWKay00UaGiDGc0sNSdoaxFuK5uc92Umny%2BDK11gFDzsn5V2c3xCUfQ9aI3pF7ZuKvHAe3unMWXoHytkqcUn58cR4cqKHtfz9Qzrg0z4IY0ZlNFJSuHVdX88R3bCXAPo1anTBR%2BvCKQ115tk%2BP9NtGfPqT92bQ96cOM6M7PF2oew8Wvot6kdYuais854kPVjU7mLd3Th%2FJker0rM1Ck6LvyOnDxLrc12e%2FJ2zuRPZsVoHmuxddskrRND1N%2BqrD682QB324uNaPyKT%2FOAap4hUBRSSYKMWtSlYwWzO3tIO50QxnMwMG2%2BnrXwRkRIWWDPERbHQBZkvI9vWN6OTregUbRnbhPFCIJB6PcU2mPioxOtwinY60W%2FogjGf%2FmilQ9Zq1Xo0yXzgI1h94k2xt%2BTexq5QC9xdVFZjxwocLsFVKsMWrxtOusImmDd8a%2BmUqAPuEqpcnML3Nir0GOqUBHwAZC9NvofZc6s3wLIJv%2Fwj7KrWrz2R2S0hur5J0%2B3FFGbDFUrCHtdxnlwJFeqvlypszUh3QhdX%2BAN6IzxPbuFgp9sTJdKO%2Fya3U5awPMHbDSq%2FDys1KR%2B3sGEW%2B9Y2FWCusfbPBi6evI1d6m5fK9skO4bhy9QeKAC87WQpLMDyCYMqnSeUITUFLrfZO%2BIL5yYZg7Q0O69JQPq9y8R1ecwW2qA8a&X-Amz-Signature=38517303606d918089d9b3b6c67fc4fe66a4d3226605b5ba5b123d27209fa126&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YG5ZKDDA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCWfncB9jzncn6ycC5P2wo5s08BymDgjY1avnMqn%2FL3sQIgYxnRk1Vp1L4z%2BSz3QLpI1Fyw2SMgrZBhYP4nBBtCo6Aq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDHtcvfpHaKIzYP5d5yrcA2fsBmKZsrXMnubKhal3mQkGJ%2Bv1beUjx3oOxwEOWaPZjq7vqIhMcNz9fNJ0T6tUX4vKIB8EhMaVjhNTvfGElWkDrIHq2cv4fd68X%2Fpr5o3mOofknRlPCWLIt84dhWj%2FQ7acZODWitieMO91FlokCHAXAuUXi7S9gb2fJUEusQDG8UVV%2F6g60f%2FWKay00UaGiDGc0sNSdoaxFuK5uc92Umny%2BDK11gFDzsn5V2c3xCUfQ9aI3pF7ZuKvHAe3unMWXoHytkqcUn58cR4cqKHtfz9Qzrg0z4IY0ZlNFJSuHVdX88R3bCXAPo1anTBR%2BvCKQ115tk%2BP9NtGfPqT92bQ96cOM6M7PF2oew8Wvot6kdYuais854kPVjU7mLd3Th%2FJker0rM1Ck6LvyOnDxLrc12e%2FJ2zuRPZsVoHmuxddskrRND1N%2BqrD682QB324uNaPyKT%2FOAap4hUBRSSYKMWtSlYwWzO3tIO50QxnMwMG2%2BnrXwRkRIWWDPERbHQBZkvI9vWN6OTregUbRnbhPFCIJB6PcU2mPioxOtwinY60W%2FogjGf%2FmilQ9Zq1Xo0yXzgI1h94k2xt%2BTexq5QC9xdVFZjxwocLsFVKsMWrxtOusImmDd8a%2BmUqAPuEqpcnML3Nir0GOqUBHwAZC9NvofZc6s3wLIJv%2Fwj7KrWrz2R2S0hur5J0%2B3FFGbDFUrCHtdxnlwJFeqvlypszUh3QhdX%2BAN6IzxPbuFgp9sTJdKO%2Fya3U5awPMHbDSq%2FDys1KR%2B3sGEW%2B9Y2FWCusfbPBi6evI1d6m5fK9skO4bhy9QeKAC87WQpLMDyCYMqnSeUITUFLrfZO%2BIL5yYZg7Q0O69JQPq9y8R1ecwW2qA8a&X-Amz-Signature=aabd093cd2559ede0e384cd04dfb5a71cb1eb93fc9e8008293238b529a124ff7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YG5ZKDDA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCWfncB9jzncn6ycC5P2wo5s08BymDgjY1avnMqn%2FL3sQIgYxnRk1Vp1L4z%2BSz3QLpI1Fyw2SMgrZBhYP4nBBtCo6Aq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDHtcvfpHaKIzYP5d5yrcA2fsBmKZsrXMnubKhal3mQkGJ%2Bv1beUjx3oOxwEOWaPZjq7vqIhMcNz9fNJ0T6tUX4vKIB8EhMaVjhNTvfGElWkDrIHq2cv4fd68X%2Fpr5o3mOofknRlPCWLIt84dhWj%2FQ7acZODWitieMO91FlokCHAXAuUXi7S9gb2fJUEusQDG8UVV%2F6g60f%2FWKay00UaGiDGc0sNSdoaxFuK5uc92Umny%2BDK11gFDzsn5V2c3xCUfQ9aI3pF7ZuKvHAe3unMWXoHytkqcUn58cR4cqKHtfz9Qzrg0z4IY0ZlNFJSuHVdX88R3bCXAPo1anTBR%2BvCKQ115tk%2BP9NtGfPqT92bQ96cOM6M7PF2oew8Wvot6kdYuais854kPVjU7mLd3Th%2FJker0rM1Ck6LvyOnDxLrc12e%2FJ2zuRPZsVoHmuxddskrRND1N%2BqrD682QB324uNaPyKT%2FOAap4hUBRSSYKMWtSlYwWzO3tIO50QxnMwMG2%2BnrXwRkRIWWDPERbHQBZkvI9vWN6OTregUbRnbhPFCIJB6PcU2mPioxOtwinY60W%2FogjGf%2FmilQ9Zq1Xo0yXzgI1h94k2xt%2BTexq5QC9xdVFZjxwocLsFVKsMWrxtOusImmDd8a%2BmUqAPuEqpcnML3Nir0GOqUBHwAZC9NvofZc6s3wLIJv%2Fwj7KrWrz2R2S0hur5J0%2B3FFGbDFUrCHtdxnlwJFeqvlypszUh3QhdX%2BAN6IzxPbuFgp9sTJdKO%2Fya3U5awPMHbDSq%2FDys1KR%2B3sGEW%2B9Y2FWCusfbPBi6evI1d6m5fK9skO4bhy9QeKAC87WQpLMDyCYMqnSeUITUFLrfZO%2BIL5yYZg7Q0O69JQPq9y8R1ecwW2qA8a&X-Amz-Signature=f9a85889a8baf4182d2375319235bba229543a5b20530ee52bbb426d1c245864&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YG5ZKDDA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCWfncB9jzncn6ycC5P2wo5s08BymDgjY1avnMqn%2FL3sQIgYxnRk1Vp1L4z%2BSz3QLpI1Fyw2SMgrZBhYP4nBBtCo6Aq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDHtcvfpHaKIzYP5d5yrcA2fsBmKZsrXMnubKhal3mQkGJ%2Bv1beUjx3oOxwEOWaPZjq7vqIhMcNz9fNJ0T6tUX4vKIB8EhMaVjhNTvfGElWkDrIHq2cv4fd68X%2Fpr5o3mOofknRlPCWLIt84dhWj%2FQ7acZODWitieMO91FlokCHAXAuUXi7S9gb2fJUEusQDG8UVV%2F6g60f%2FWKay00UaGiDGc0sNSdoaxFuK5uc92Umny%2BDK11gFDzsn5V2c3xCUfQ9aI3pF7ZuKvHAe3unMWXoHytkqcUn58cR4cqKHtfz9Qzrg0z4IY0ZlNFJSuHVdX88R3bCXAPo1anTBR%2BvCKQ115tk%2BP9NtGfPqT92bQ96cOM6M7PF2oew8Wvot6kdYuais854kPVjU7mLd3Th%2FJker0rM1Ck6LvyOnDxLrc12e%2FJ2zuRPZsVoHmuxddskrRND1N%2BqrD682QB324uNaPyKT%2FOAap4hUBRSSYKMWtSlYwWzO3tIO50QxnMwMG2%2BnrXwRkRIWWDPERbHQBZkvI9vWN6OTregUbRnbhPFCIJB6PcU2mPioxOtwinY60W%2FogjGf%2FmilQ9Zq1Xo0yXzgI1h94k2xt%2BTexq5QC9xdVFZjxwocLsFVKsMWrxtOusImmDd8a%2BmUqAPuEqpcnML3Nir0GOqUBHwAZC9NvofZc6s3wLIJv%2Fwj7KrWrz2R2S0hur5J0%2B3FFGbDFUrCHtdxnlwJFeqvlypszUh3QhdX%2BAN6IzxPbuFgp9sTJdKO%2Fya3U5awPMHbDSq%2FDys1KR%2B3sGEW%2B9Y2FWCusfbPBi6evI1d6m5fK9skO4bhy9QeKAC87WQpLMDyCYMqnSeUITUFLrfZO%2BIL5yYZg7Q0O69JQPq9y8R1ecwW2qA8a&X-Amz-Signature=9fcad4726ba66d44b865034cb344cdc888350fb8d74d6d4435d8e94e74fd5d3b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YG5ZKDDA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCWfncB9jzncn6ycC5P2wo5s08BymDgjY1avnMqn%2FL3sQIgYxnRk1Vp1L4z%2BSz3QLpI1Fyw2SMgrZBhYP4nBBtCo6Aq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDHtcvfpHaKIzYP5d5yrcA2fsBmKZsrXMnubKhal3mQkGJ%2Bv1beUjx3oOxwEOWaPZjq7vqIhMcNz9fNJ0T6tUX4vKIB8EhMaVjhNTvfGElWkDrIHq2cv4fd68X%2Fpr5o3mOofknRlPCWLIt84dhWj%2FQ7acZODWitieMO91FlokCHAXAuUXi7S9gb2fJUEusQDG8UVV%2F6g60f%2FWKay00UaGiDGc0sNSdoaxFuK5uc92Umny%2BDK11gFDzsn5V2c3xCUfQ9aI3pF7ZuKvHAe3unMWXoHytkqcUn58cR4cqKHtfz9Qzrg0z4IY0ZlNFJSuHVdX88R3bCXAPo1anTBR%2BvCKQ115tk%2BP9NtGfPqT92bQ96cOM6M7PF2oew8Wvot6kdYuais854kPVjU7mLd3Th%2FJker0rM1Ck6LvyOnDxLrc12e%2FJ2zuRPZsVoHmuxddskrRND1N%2BqrD682QB324uNaPyKT%2FOAap4hUBRSSYKMWtSlYwWzO3tIO50QxnMwMG2%2BnrXwRkRIWWDPERbHQBZkvI9vWN6OTregUbRnbhPFCIJB6PcU2mPioxOtwinY60W%2FogjGf%2FmilQ9Zq1Xo0yXzgI1h94k2xt%2BTexq5QC9xdVFZjxwocLsFVKsMWrxtOusImmDd8a%2BmUqAPuEqpcnML3Nir0GOqUBHwAZC9NvofZc6s3wLIJv%2Fwj7KrWrz2R2S0hur5J0%2B3FFGbDFUrCHtdxnlwJFeqvlypszUh3QhdX%2BAN6IzxPbuFgp9sTJdKO%2Fya3U5awPMHbDSq%2FDys1KR%2B3sGEW%2B9Y2FWCusfbPBi6evI1d6m5fK9skO4bhy9QeKAC87WQpLMDyCYMqnSeUITUFLrfZO%2BIL5yYZg7Q0O69JQPq9y8R1ecwW2qA8a&X-Amz-Signature=9914bb79ae40c11b34896dd9a129403189360ab68012a9b03a9f72b0a9b056fa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSTLUUBG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCSfU7II%2B4pXI%2BC%2BqBYo4gQEiF%2FYHdyvXiUpcY7Py%2F2tQIgc8PNuQo%2FhvposoMVr7ByME3fHO8Ppd6%2FACCuhEHnmMgq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAOS6OzSdSAIUk5XKyrcAzXrVI9OJajt%2F%2BOBIW831tSBGr8vLMbWB5GRaKfl24JzijTMX%2BzfTiDBWjqixMYKFU3btIpEpgH9Yhm22lR5ZarCwhgeGbUNssW%2FS%2Bti%2FXtz6G72B8UFcBjZvjLkzUR4qdSEfTAgz27oqvxRVdMHohzmvDExqJLScNY64eAPnggG31QjUN2G3RTOVuoEY3pZvzfv5hIgFcKFtmfrkw9xxsdMODHbToimix3huubGt%2BLJAHejba2WIWYKOU7%2Bpt4DVLPaoDqhl0ua4CEgPUWbdDcSVChapNhMvCa28Otit97RZNgHd7Xm4qltxBicyH%2F9V2bisjVOXD6lXrYC4hUl0fwoNgpas6X9gNEIGgL4gUcSf0VVog848On2snq%2BwM5X4oVTQLhRbPUBef2pR9UsYouUgBR0Q6VNXepavfgXcLx3opbFbKlfXN%2FQkv%2FkmRaPZFeVL44gXqejqLzBNNMRCMYdhAG%2B6X2Bf6WbWE4gtEjrghpy%2B0K3WMU0wzvOhODBZDBN4mVKXblz6F2w78O%2BcoLn4j0fnLGw8YtrYdaTXODZIWJvVqJa6Q6ArxDZu4Xvx9zOD2kCl4gDN8eEm7zUIyhsOO2L%2BMp5obpowQUDPgAt%2BCe9sPzCJgk71Y8aMKLNir0GOqUBVt7nx4ND2oC3Xnf4%2Fx1A5kdo7xjzEc0nQrRHbyOKHWsPiGrnWVwYGwxZndgoZHPf4trkQX%2FCJDLsqdUg9y34hweHAcY3ByTwBeEG3WGw%2F7kaRrSykCvutEtOVjpq2NhJSnQEqPKRGqfk7%2FHmbeXs4r8NI1QaIKBB08tD6S6IhvwgH5xWD9ux03sqOk9aZJze1HhyaDsPhc31xjdfMoNGCn4yKnAw&X-Amz-Signature=3bbb95d4b8e811a516e23b88802775df2ac673fd59b7758e1df6b9ffdbe66dd9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSTLUUBG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCSfU7II%2B4pXI%2BC%2BqBYo4gQEiF%2FYHdyvXiUpcY7Py%2F2tQIgc8PNuQo%2FhvposoMVr7ByME3fHO8Ppd6%2FACCuhEHnmMgq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAOS6OzSdSAIUk5XKyrcAzXrVI9OJajt%2F%2BOBIW831tSBGr8vLMbWB5GRaKfl24JzijTMX%2BzfTiDBWjqixMYKFU3btIpEpgH9Yhm22lR5ZarCwhgeGbUNssW%2FS%2Bti%2FXtz6G72B8UFcBjZvjLkzUR4qdSEfTAgz27oqvxRVdMHohzmvDExqJLScNY64eAPnggG31QjUN2G3RTOVuoEY3pZvzfv5hIgFcKFtmfrkw9xxsdMODHbToimix3huubGt%2BLJAHejba2WIWYKOU7%2Bpt4DVLPaoDqhl0ua4CEgPUWbdDcSVChapNhMvCa28Otit97RZNgHd7Xm4qltxBicyH%2F9V2bisjVOXD6lXrYC4hUl0fwoNgpas6X9gNEIGgL4gUcSf0VVog848On2snq%2BwM5X4oVTQLhRbPUBef2pR9UsYouUgBR0Q6VNXepavfgXcLx3opbFbKlfXN%2FQkv%2FkmRaPZFeVL44gXqejqLzBNNMRCMYdhAG%2B6X2Bf6WbWE4gtEjrghpy%2B0K3WMU0wzvOhODBZDBN4mVKXblz6F2w78O%2BcoLn4j0fnLGw8YtrYdaTXODZIWJvVqJa6Q6ArxDZu4Xvx9zOD2kCl4gDN8eEm7zUIyhsOO2L%2BMp5obpowQUDPgAt%2BCe9sPzCJgk71Y8aMKLNir0GOqUBVt7nx4ND2oC3Xnf4%2Fx1A5kdo7xjzEc0nQrRHbyOKHWsPiGrnWVwYGwxZndgoZHPf4trkQX%2FCJDLsqdUg9y34hweHAcY3ByTwBeEG3WGw%2F7kaRrSykCvutEtOVjpq2NhJSnQEqPKRGqfk7%2FHmbeXs4r8NI1QaIKBB08tD6S6IhvwgH5xWD9ux03sqOk9aZJze1HhyaDsPhc31xjdfMoNGCn4yKnAw&X-Amz-Signature=292244143dd479fc91e97885bc9215273b6c95fc59faa0f742b57b4fb0daa4ef&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSTLUUBG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCSfU7II%2B4pXI%2BC%2BqBYo4gQEiF%2FYHdyvXiUpcY7Py%2F2tQIgc8PNuQo%2FhvposoMVr7ByME3fHO8Ppd6%2FACCuhEHnmMgq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAOS6OzSdSAIUk5XKyrcAzXrVI9OJajt%2F%2BOBIW831tSBGr8vLMbWB5GRaKfl24JzijTMX%2BzfTiDBWjqixMYKFU3btIpEpgH9Yhm22lR5ZarCwhgeGbUNssW%2FS%2Bti%2FXtz6G72B8UFcBjZvjLkzUR4qdSEfTAgz27oqvxRVdMHohzmvDExqJLScNY64eAPnggG31QjUN2G3RTOVuoEY3pZvzfv5hIgFcKFtmfrkw9xxsdMODHbToimix3huubGt%2BLJAHejba2WIWYKOU7%2Bpt4DVLPaoDqhl0ua4CEgPUWbdDcSVChapNhMvCa28Otit97RZNgHd7Xm4qltxBicyH%2F9V2bisjVOXD6lXrYC4hUl0fwoNgpas6X9gNEIGgL4gUcSf0VVog848On2snq%2BwM5X4oVTQLhRbPUBef2pR9UsYouUgBR0Q6VNXepavfgXcLx3opbFbKlfXN%2FQkv%2FkmRaPZFeVL44gXqejqLzBNNMRCMYdhAG%2B6X2Bf6WbWE4gtEjrghpy%2B0K3WMU0wzvOhODBZDBN4mVKXblz6F2w78O%2BcoLn4j0fnLGw8YtrYdaTXODZIWJvVqJa6Q6ArxDZu4Xvx9zOD2kCl4gDN8eEm7zUIyhsOO2L%2BMp5obpowQUDPgAt%2BCe9sPzCJgk71Y8aMKLNir0GOqUBVt7nx4ND2oC3Xnf4%2Fx1A5kdo7xjzEc0nQrRHbyOKHWsPiGrnWVwYGwxZndgoZHPf4trkQX%2FCJDLsqdUg9y34hweHAcY3ByTwBeEG3WGw%2F7kaRrSykCvutEtOVjpq2NhJSnQEqPKRGqfk7%2FHmbeXs4r8NI1QaIKBB08tD6S6IhvwgH5xWD9ux03sqOk9aZJze1HhyaDsPhc31xjdfMoNGCn4yKnAw&X-Amz-Signature=5627894af07754d0157c68ecfeea3bcb7346df9f02cca1f9bbda50caad6c2515&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSTLUUBG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCSfU7II%2B4pXI%2BC%2BqBYo4gQEiF%2FYHdyvXiUpcY7Py%2F2tQIgc8PNuQo%2FhvposoMVr7ByME3fHO8Ppd6%2FACCuhEHnmMgq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAOS6OzSdSAIUk5XKyrcAzXrVI9OJajt%2F%2BOBIW831tSBGr8vLMbWB5GRaKfl24JzijTMX%2BzfTiDBWjqixMYKFU3btIpEpgH9Yhm22lR5ZarCwhgeGbUNssW%2FS%2Bti%2FXtz6G72B8UFcBjZvjLkzUR4qdSEfTAgz27oqvxRVdMHohzmvDExqJLScNY64eAPnggG31QjUN2G3RTOVuoEY3pZvzfv5hIgFcKFtmfrkw9xxsdMODHbToimix3huubGt%2BLJAHejba2WIWYKOU7%2Bpt4DVLPaoDqhl0ua4CEgPUWbdDcSVChapNhMvCa28Otit97RZNgHd7Xm4qltxBicyH%2F9V2bisjVOXD6lXrYC4hUl0fwoNgpas6X9gNEIGgL4gUcSf0VVog848On2snq%2BwM5X4oVTQLhRbPUBef2pR9UsYouUgBR0Q6VNXepavfgXcLx3opbFbKlfXN%2FQkv%2FkmRaPZFeVL44gXqejqLzBNNMRCMYdhAG%2B6X2Bf6WbWE4gtEjrghpy%2B0K3WMU0wzvOhODBZDBN4mVKXblz6F2w78O%2BcoLn4j0fnLGw8YtrYdaTXODZIWJvVqJa6Q6ArxDZu4Xvx9zOD2kCl4gDN8eEm7zUIyhsOO2L%2BMp5obpowQUDPgAt%2BCe9sPzCJgk71Y8aMKLNir0GOqUBVt7nx4ND2oC3Xnf4%2Fx1A5kdo7xjzEc0nQrRHbyOKHWsPiGrnWVwYGwxZndgoZHPf4trkQX%2FCJDLsqdUg9y34hweHAcY3ByTwBeEG3WGw%2F7kaRrSykCvutEtOVjpq2NhJSnQEqPKRGqfk7%2FHmbeXs4r8NI1QaIKBB08tD6S6IhvwgH5xWD9ux03sqOk9aZJze1HhyaDsPhc31xjdfMoNGCn4yKnAw&X-Amz-Signature=10035ea868c2732510ec1a2f0ac5147856aa6ca0fc8846c3bc289d460593b896&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSTLUUBG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCSfU7II%2B4pXI%2BC%2BqBYo4gQEiF%2FYHdyvXiUpcY7Py%2F2tQIgc8PNuQo%2FhvposoMVr7ByME3fHO8Ppd6%2FACCuhEHnmMgq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAOS6OzSdSAIUk5XKyrcAzXrVI9OJajt%2F%2BOBIW831tSBGr8vLMbWB5GRaKfl24JzijTMX%2BzfTiDBWjqixMYKFU3btIpEpgH9Yhm22lR5ZarCwhgeGbUNssW%2FS%2Bti%2FXtz6G72B8UFcBjZvjLkzUR4qdSEfTAgz27oqvxRVdMHohzmvDExqJLScNY64eAPnggG31QjUN2G3RTOVuoEY3pZvzfv5hIgFcKFtmfrkw9xxsdMODHbToimix3huubGt%2BLJAHejba2WIWYKOU7%2Bpt4DVLPaoDqhl0ua4CEgPUWbdDcSVChapNhMvCa28Otit97RZNgHd7Xm4qltxBicyH%2F9V2bisjVOXD6lXrYC4hUl0fwoNgpas6X9gNEIGgL4gUcSf0VVog848On2snq%2BwM5X4oVTQLhRbPUBef2pR9UsYouUgBR0Q6VNXepavfgXcLx3opbFbKlfXN%2FQkv%2FkmRaPZFeVL44gXqejqLzBNNMRCMYdhAG%2B6X2Bf6WbWE4gtEjrghpy%2B0K3WMU0wzvOhODBZDBN4mVKXblz6F2w78O%2BcoLn4j0fnLGw8YtrYdaTXODZIWJvVqJa6Q6ArxDZu4Xvx9zOD2kCl4gDN8eEm7zUIyhsOO2L%2BMp5obpowQUDPgAt%2BCe9sPzCJgk71Y8aMKLNir0GOqUBVt7nx4ND2oC3Xnf4%2Fx1A5kdo7xjzEc0nQrRHbyOKHWsPiGrnWVwYGwxZndgoZHPf4trkQX%2FCJDLsqdUg9y34hweHAcY3ByTwBeEG3WGw%2F7kaRrSykCvutEtOVjpq2NhJSnQEqPKRGqfk7%2FHmbeXs4r8NI1QaIKBB08tD6S6IhvwgH5xWD9ux03sqOk9aZJze1HhyaDsPhc31xjdfMoNGCn4yKnAw&X-Amz-Signature=5df6cbb3c2531f2cd76a419f9ce48a5b0bfebd298cb898a0e1050987538d45c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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


