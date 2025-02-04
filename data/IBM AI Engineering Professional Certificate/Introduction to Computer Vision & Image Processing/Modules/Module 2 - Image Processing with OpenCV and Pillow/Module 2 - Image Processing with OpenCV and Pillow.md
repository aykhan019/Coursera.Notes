

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TCHIYVA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQCrqh9xujbqUk64l6WhKrhMCeMTDmUeW%2BHeE4GpeFPl0gIhAOu4Hf1deSN2GwmZxLUI3TE3H6RZ%2Fk1vr%2F3E3bYCzZC0Kv8DCCMQABoMNjM3NDIzMTgzODA1IgzkVUqkCy1vDy2eUrQq3APFxgtttMguazsN%2FC0pFrstIFL6aF2w8bGeGqY5HwQtiAzUsbByjLP488GDUNm6WuqkC%2F2PePQGjjNoon%2B8V7LyU82vpu6jQ4KtaPyw7%2Fuena7lhPUPu%2BZGaOyo%2FwaWMEARuDyp%2F11a6ijE5law%2F39isAxwu%2F%2BADxYzQytLP%2BKZ%2BaNUmtGioY3tIf0GWnhCSOUput%2B5yZSJc1LqR1jiNyCkSr6jjaL51LrFnyMGY75HUSY3i9cwMQHSypUV0z49BxORQT%2B%2B6SDreq9gWizebhYmv1kcmRqGvQYmk1M2xElZKv5l1SojJ0wT0v2IEc1r1Ph2gHFaEU%2Btxo5mz61B0aZqMBd5SKfGnE14iyRahjWwm3mTOkaCAIW2pQBZcfsLYGLFjL1Taf5YTzBTY22%2FFUTcCJ41ZoffXXtpCuoSCTWL8bzaBQ8bxDiJ4frUVXF1AR2TBIcKkDQ59kJUR6vyFNh4tAEPZdjglG03f1d1g6bAyt3AeniA6e1QayJCNMRO94Gyr%2FPeJnnZomw%2BhlO%2F%2Fdxz24SVsQBs60%2F58GkxalMsSW56xneWIpZz0NBuAfdLT2KVET4eQZ6fGcAFLr60RLPLQV2d570a%2BmByNyVc8kC6fwmYFyoxWbnZBw4aUTCm6oW9BjqkAdSf2YhD1LQU1JIkgW5qHyBb3fJxvj8JzEbO5r1apH9OCLvI9R%2Bi3dC6YIVBHrDhvU%2FxvQXTPNKcbjBkWUiM%2Ftekqz5NXBTZBq860RiWcF9VjnRsv%2Fgg975ZTexY8mdgXTAyJ5T6IcJAV2ZCzLdh1ZXQ3hbMQEwlwpFZATIntPPzl3mtAbGcLSBp3c2wLp8p8RMgMrHvDJIfgoWB%2FLoNGWQjEhQS&X-Amz-Signature=1e03f1bc51368620b468847abb6862cf8d909b17a5073589003bad5e7317043f&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAYI2Q5W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIF50mUrQBdkK3fGZjW1ka7jDlyWXBd8jqLH9WoV8gFPuAiBGVaGvoyOTRjongUz4CDS6JtZqBSQ5a1odFY32apyW9ir%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMcNl%2Fqa3JAf1d9qHzKtwDmkl9kkfcZ81j8mpxaPcul6WKBgTCBawNEK5ynXtZkyDW9zzm6x8m6rXLKUOZATD1u3PwBGEPuxOhMyOSjMhQvMvdcAt6f%2BekG1cWd%2FQ6fmsonJUxO0pA%2F5vi5q4osqpeLkEUJEaCQm4DeD1avcPm8iDgFxoo1PELHzCq0j%2FYgGGoeVHlo0jQiry3br0gEq13QEon0%2B29J0Of9QFjqa0A4B%2F7qN0%2BtB2zfDTBEcBrqC3f97FlrKjvVhJ3Vd%2FmxgJG0hJW2NSABxB0sJqkrmmGshc8h3lOvC8kyZFt92%2FxiBPOi1pldatjcQPALE8dsK3eryg6uCkfeFjrJTj5pfC7EGcD%2BCm1RZQd%2FhlrPhD7bakO2YGi8f8pf4zqrNuJ7T%2F%2F0nvAwkasDN%2FRiQIFaMKipWnKgNoazbkxZEBJYyqpes180VbyrTrXCVM1wa9DJJ7UjKWLaaFmg1FTm52ppWObQtVNmif15P70ieQ%2FxlJmQJHrj1hbKsGmzMPdSk7bfWY3SaTlo8CgixZVwxk%2BeAANHVk1AwqLciYeFrQMtsAfU%2FWfwaYm8xxJDi9FaYGEXiDK7HgWUbJFZWRInEbuYtiVSuHnZHNsUTo6DLj9gQITweBZSRLYhJ78KxIT%2BzIwjemFvQY6pgGoq8Ca70l8%2FTAhjealcDAlITGA7TfrrpCdNUg5Puq%2FMHjJC1VCULhqeRDlMO7PBZtr2n5KNH18K8HrTNeYir%2FG0t1g3u69wue5CZJYG1%2But130pSs05vxxA0dDUV1CKGWz1%2FGSjQcZJIYRUmXJhSKyi%2F0QU231i1EaCrghLMtrnP%2FUd1JzNsHVQjgOj8NkgwBG6po1oEegLF80utvG505%2Fh3QrxWox&X-Amz-Signature=4bcc066b40403589614a12680bd3c698cd83e3761413dbfeea1e2ea9d164b7aa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAYI2Q5W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIF50mUrQBdkK3fGZjW1ka7jDlyWXBd8jqLH9WoV8gFPuAiBGVaGvoyOTRjongUz4CDS6JtZqBSQ5a1odFY32apyW9ir%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMcNl%2Fqa3JAf1d9qHzKtwDmkl9kkfcZ81j8mpxaPcul6WKBgTCBawNEK5ynXtZkyDW9zzm6x8m6rXLKUOZATD1u3PwBGEPuxOhMyOSjMhQvMvdcAt6f%2BekG1cWd%2FQ6fmsonJUxO0pA%2F5vi5q4osqpeLkEUJEaCQm4DeD1avcPm8iDgFxoo1PELHzCq0j%2FYgGGoeVHlo0jQiry3br0gEq13QEon0%2B29J0Of9QFjqa0A4B%2F7qN0%2BtB2zfDTBEcBrqC3f97FlrKjvVhJ3Vd%2FmxgJG0hJW2NSABxB0sJqkrmmGshc8h3lOvC8kyZFt92%2FxiBPOi1pldatjcQPALE8dsK3eryg6uCkfeFjrJTj5pfC7EGcD%2BCm1RZQd%2FhlrPhD7bakO2YGi8f8pf4zqrNuJ7T%2F%2F0nvAwkasDN%2FRiQIFaMKipWnKgNoazbkxZEBJYyqpes180VbyrTrXCVM1wa9DJJ7UjKWLaaFmg1FTm52ppWObQtVNmif15P70ieQ%2FxlJmQJHrj1hbKsGmzMPdSk7bfWY3SaTlo8CgixZVwxk%2BeAANHVk1AwqLciYeFrQMtsAfU%2FWfwaYm8xxJDi9FaYGEXiDK7HgWUbJFZWRInEbuYtiVSuHnZHNsUTo6DLj9gQITweBZSRLYhJ78KxIT%2BzIwjemFvQY6pgGoq8Ca70l8%2FTAhjealcDAlITGA7TfrrpCdNUg5Puq%2FMHjJC1VCULhqeRDlMO7PBZtr2n5KNH18K8HrTNeYir%2FG0t1g3u69wue5CZJYG1%2But130pSs05vxxA0dDUV1CKGWz1%2FGSjQcZJIYRUmXJhSKyi%2F0QU231i1EaCrghLMtrnP%2FUd1JzNsHVQjgOj8NkgwBG6po1oEegLF80utvG505%2Fh3QrxWox&X-Amz-Signature=bc86df5826251d7a6a6fe289d26389c41c209a12a35e724cab7d304a84c91fd2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAYI2Q5W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIF50mUrQBdkK3fGZjW1ka7jDlyWXBd8jqLH9WoV8gFPuAiBGVaGvoyOTRjongUz4CDS6JtZqBSQ5a1odFY32apyW9ir%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMcNl%2Fqa3JAf1d9qHzKtwDmkl9kkfcZ81j8mpxaPcul6WKBgTCBawNEK5ynXtZkyDW9zzm6x8m6rXLKUOZATD1u3PwBGEPuxOhMyOSjMhQvMvdcAt6f%2BekG1cWd%2FQ6fmsonJUxO0pA%2F5vi5q4osqpeLkEUJEaCQm4DeD1avcPm8iDgFxoo1PELHzCq0j%2FYgGGoeVHlo0jQiry3br0gEq13QEon0%2B29J0Of9QFjqa0A4B%2F7qN0%2BtB2zfDTBEcBrqC3f97FlrKjvVhJ3Vd%2FmxgJG0hJW2NSABxB0sJqkrmmGshc8h3lOvC8kyZFt92%2FxiBPOi1pldatjcQPALE8dsK3eryg6uCkfeFjrJTj5pfC7EGcD%2BCm1RZQd%2FhlrPhD7bakO2YGi8f8pf4zqrNuJ7T%2F%2F0nvAwkasDN%2FRiQIFaMKipWnKgNoazbkxZEBJYyqpes180VbyrTrXCVM1wa9DJJ7UjKWLaaFmg1FTm52ppWObQtVNmif15P70ieQ%2FxlJmQJHrj1hbKsGmzMPdSk7bfWY3SaTlo8CgixZVwxk%2BeAANHVk1AwqLciYeFrQMtsAfU%2FWfwaYm8xxJDi9FaYGEXiDK7HgWUbJFZWRInEbuYtiVSuHnZHNsUTo6DLj9gQITweBZSRLYhJ78KxIT%2BzIwjemFvQY6pgGoq8Ca70l8%2FTAhjealcDAlITGA7TfrrpCdNUg5Puq%2FMHjJC1VCULhqeRDlMO7PBZtr2n5KNH18K8HrTNeYir%2FG0t1g3u69wue5CZJYG1%2But130pSs05vxxA0dDUV1CKGWz1%2FGSjQcZJIYRUmXJhSKyi%2F0QU231i1EaCrghLMtrnP%2FUd1JzNsHVQjgOj8NkgwBG6po1oEegLF80utvG505%2Fh3QrxWox&X-Amz-Signature=7edde2ade0a225e4817ab71f7bbd3db7f0f4298f3ba5751947695eecc726e5dc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAYI2Q5W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIF50mUrQBdkK3fGZjW1ka7jDlyWXBd8jqLH9WoV8gFPuAiBGVaGvoyOTRjongUz4CDS6JtZqBSQ5a1odFY32apyW9ir%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMcNl%2Fqa3JAf1d9qHzKtwDmkl9kkfcZ81j8mpxaPcul6WKBgTCBawNEK5ynXtZkyDW9zzm6x8m6rXLKUOZATD1u3PwBGEPuxOhMyOSjMhQvMvdcAt6f%2BekG1cWd%2FQ6fmsonJUxO0pA%2F5vi5q4osqpeLkEUJEaCQm4DeD1avcPm8iDgFxoo1PELHzCq0j%2FYgGGoeVHlo0jQiry3br0gEq13QEon0%2B29J0Of9QFjqa0A4B%2F7qN0%2BtB2zfDTBEcBrqC3f97FlrKjvVhJ3Vd%2FmxgJG0hJW2NSABxB0sJqkrmmGshc8h3lOvC8kyZFt92%2FxiBPOi1pldatjcQPALE8dsK3eryg6uCkfeFjrJTj5pfC7EGcD%2BCm1RZQd%2FhlrPhD7bakO2YGi8f8pf4zqrNuJ7T%2F%2F0nvAwkasDN%2FRiQIFaMKipWnKgNoazbkxZEBJYyqpes180VbyrTrXCVM1wa9DJJ7UjKWLaaFmg1FTm52ppWObQtVNmif15P70ieQ%2FxlJmQJHrj1hbKsGmzMPdSk7bfWY3SaTlo8CgixZVwxk%2BeAANHVk1AwqLciYeFrQMtsAfU%2FWfwaYm8xxJDi9FaYGEXiDK7HgWUbJFZWRInEbuYtiVSuHnZHNsUTo6DLj9gQITweBZSRLYhJ78KxIT%2BzIwjemFvQY6pgGoq8Ca70l8%2FTAhjealcDAlITGA7TfrrpCdNUg5Puq%2FMHjJC1VCULhqeRDlMO7PBZtr2n5KNH18K8HrTNeYir%2FG0t1g3u69wue5CZJYG1%2But130pSs05vxxA0dDUV1CKGWz1%2FGSjQcZJIYRUmXJhSKyi%2F0QU231i1EaCrghLMtrnP%2FUd1JzNsHVQjgOj8NkgwBG6po1oEegLF80utvG505%2Fh3QrxWox&X-Amz-Signature=c84e4034a54358cd75cb4be9fc90c6e9067e8ae7980e30633b926cce8d7f4b88&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAYI2Q5W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIF50mUrQBdkK3fGZjW1ka7jDlyWXBd8jqLH9WoV8gFPuAiBGVaGvoyOTRjongUz4CDS6JtZqBSQ5a1odFY32apyW9ir%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMcNl%2Fqa3JAf1d9qHzKtwDmkl9kkfcZ81j8mpxaPcul6WKBgTCBawNEK5ynXtZkyDW9zzm6x8m6rXLKUOZATD1u3PwBGEPuxOhMyOSjMhQvMvdcAt6f%2BekG1cWd%2FQ6fmsonJUxO0pA%2F5vi5q4osqpeLkEUJEaCQm4DeD1avcPm8iDgFxoo1PELHzCq0j%2FYgGGoeVHlo0jQiry3br0gEq13QEon0%2B29J0Of9QFjqa0A4B%2F7qN0%2BtB2zfDTBEcBrqC3f97FlrKjvVhJ3Vd%2FmxgJG0hJW2NSABxB0sJqkrmmGshc8h3lOvC8kyZFt92%2FxiBPOi1pldatjcQPALE8dsK3eryg6uCkfeFjrJTj5pfC7EGcD%2BCm1RZQd%2FhlrPhD7bakO2YGi8f8pf4zqrNuJ7T%2F%2F0nvAwkasDN%2FRiQIFaMKipWnKgNoazbkxZEBJYyqpes180VbyrTrXCVM1wa9DJJ7UjKWLaaFmg1FTm52ppWObQtVNmif15P70ieQ%2FxlJmQJHrj1hbKsGmzMPdSk7bfWY3SaTlo8CgixZVwxk%2BeAANHVk1AwqLciYeFrQMtsAfU%2FWfwaYm8xxJDi9FaYGEXiDK7HgWUbJFZWRInEbuYtiVSuHnZHNsUTo6DLj9gQITweBZSRLYhJ78KxIT%2BzIwjemFvQY6pgGoq8Ca70l8%2FTAhjealcDAlITGA7TfrrpCdNUg5Puq%2FMHjJC1VCULhqeRDlMO7PBZtr2n5KNH18K8HrTNeYir%2FG0t1g3u69wue5CZJYG1%2But130pSs05vxxA0dDUV1CKGWz1%2FGSjQcZJIYRUmXJhSKyi%2F0QU231i1EaCrghLMtrnP%2FUd1JzNsHVQjgOj8NkgwBG6po1oEegLF80utvG505%2Fh3QrxWox&X-Amz-Signature=955038a9ceea5d59ce285bd84d4bd946691ac9063bdab705cb3788f8fe9a9715&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TCHIYVA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQCrqh9xujbqUk64l6WhKrhMCeMTDmUeW%2BHeE4GpeFPl0gIhAOu4Hf1deSN2GwmZxLUI3TE3H6RZ%2Fk1vr%2F3E3bYCzZC0Kv8DCCMQABoMNjM3NDIzMTgzODA1IgzkVUqkCy1vDy2eUrQq3APFxgtttMguazsN%2FC0pFrstIFL6aF2w8bGeGqY5HwQtiAzUsbByjLP488GDUNm6WuqkC%2F2PePQGjjNoon%2B8V7LyU82vpu6jQ4KtaPyw7%2Fuena7lhPUPu%2BZGaOyo%2FwaWMEARuDyp%2F11a6ijE5law%2F39isAxwu%2F%2BADxYzQytLP%2BKZ%2BaNUmtGioY3tIf0GWnhCSOUput%2B5yZSJc1LqR1jiNyCkSr6jjaL51LrFnyMGY75HUSY3i9cwMQHSypUV0z49BxORQT%2B%2B6SDreq9gWizebhYmv1kcmRqGvQYmk1M2xElZKv5l1SojJ0wT0v2IEc1r1Ph2gHFaEU%2Btxo5mz61B0aZqMBd5SKfGnE14iyRahjWwm3mTOkaCAIW2pQBZcfsLYGLFjL1Taf5YTzBTY22%2FFUTcCJ41ZoffXXtpCuoSCTWL8bzaBQ8bxDiJ4frUVXF1AR2TBIcKkDQ59kJUR6vyFNh4tAEPZdjglG03f1d1g6bAyt3AeniA6e1QayJCNMRO94Gyr%2FPeJnnZomw%2BhlO%2F%2Fdxz24SVsQBs60%2F58GkxalMsSW56xneWIpZz0NBuAfdLT2KVET4eQZ6fGcAFLr60RLPLQV2d570a%2BmByNyVc8kC6fwmYFyoxWbnZBw4aUTCm6oW9BjqkAdSf2YhD1LQU1JIkgW5qHyBb3fJxvj8JzEbO5r1apH9OCLvI9R%2Bi3dC6YIVBHrDhvU%2FxvQXTPNKcbjBkWUiM%2Ftekqz5NXBTZBq860RiWcF9VjnRsv%2Fgg975ZTexY8mdgXTAyJ5T6IcJAV2ZCzLdh1ZXQ3hbMQEwlwpFZATIntPPzl3mtAbGcLSBp3c2wLp8p8RMgMrHvDJIfgoWB%2FLoNGWQjEhQS&X-Amz-Signature=a801567149980c6ad49ecbab314250635c000851c77d06eaee53dc058fba16d0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TCHIYVA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQCrqh9xujbqUk64l6WhKrhMCeMTDmUeW%2BHeE4GpeFPl0gIhAOu4Hf1deSN2GwmZxLUI3TE3H6RZ%2Fk1vr%2F3E3bYCzZC0Kv8DCCMQABoMNjM3NDIzMTgzODA1IgzkVUqkCy1vDy2eUrQq3APFxgtttMguazsN%2FC0pFrstIFL6aF2w8bGeGqY5HwQtiAzUsbByjLP488GDUNm6WuqkC%2F2PePQGjjNoon%2B8V7LyU82vpu6jQ4KtaPyw7%2Fuena7lhPUPu%2BZGaOyo%2FwaWMEARuDyp%2F11a6ijE5law%2F39isAxwu%2F%2BADxYzQytLP%2BKZ%2BaNUmtGioY3tIf0GWnhCSOUput%2B5yZSJc1LqR1jiNyCkSr6jjaL51LrFnyMGY75HUSY3i9cwMQHSypUV0z49BxORQT%2B%2B6SDreq9gWizebhYmv1kcmRqGvQYmk1M2xElZKv5l1SojJ0wT0v2IEc1r1Ph2gHFaEU%2Btxo5mz61B0aZqMBd5SKfGnE14iyRahjWwm3mTOkaCAIW2pQBZcfsLYGLFjL1Taf5YTzBTY22%2FFUTcCJ41ZoffXXtpCuoSCTWL8bzaBQ8bxDiJ4frUVXF1AR2TBIcKkDQ59kJUR6vyFNh4tAEPZdjglG03f1d1g6bAyt3AeniA6e1QayJCNMRO94Gyr%2FPeJnnZomw%2BhlO%2F%2Fdxz24SVsQBs60%2F58GkxalMsSW56xneWIpZz0NBuAfdLT2KVET4eQZ6fGcAFLr60RLPLQV2d570a%2BmByNyVc8kC6fwmYFyoxWbnZBw4aUTCm6oW9BjqkAdSf2YhD1LQU1JIkgW5qHyBb3fJxvj8JzEbO5r1apH9OCLvI9R%2Bi3dC6YIVBHrDhvU%2FxvQXTPNKcbjBkWUiM%2Ftekqz5NXBTZBq860RiWcF9VjnRsv%2Fgg975ZTexY8mdgXTAyJ5T6IcJAV2ZCzLdh1ZXQ3hbMQEwlwpFZATIntPPzl3mtAbGcLSBp3c2wLp8p8RMgMrHvDJIfgoWB%2FLoNGWQjEhQS&X-Amz-Signature=5764f76866f2e71d6b07e5d2a456d5f3038db03c4d654e7136a4dd9037ba6626&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TCHIYVA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQCrqh9xujbqUk64l6WhKrhMCeMTDmUeW%2BHeE4GpeFPl0gIhAOu4Hf1deSN2GwmZxLUI3TE3H6RZ%2Fk1vr%2F3E3bYCzZC0Kv8DCCMQABoMNjM3NDIzMTgzODA1IgzkVUqkCy1vDy2eUrQq3APFxgtttMguazsN%2FC0pFrstIFL6aF2w8bGeGqY5HwQtiAzUsbByjLP488GDUNm6WuqkC%2F2PePQGjjNoon%2B8V7LyU82vpu6jQ4KtaPyw7%2Fuena7lhPUPu%2BZGaOyo%2FwaWMEARuDyp%2F11a6ijE5law%2F39isAxwu%2F%2BADxYzQytLP%2BKZ%2BaNUmtGioY3tIf0GWnhCSOUput%2B5yZSJc1LqR1jiNyCkSr6jjaL51LrFnyMGY75HUSY3i9cwMQHSypUV0z49BxORQT%2B%2B6SDreq9gWizebhYmv1kcmRqGvQYmk1M2xElZKv5l1SojJ0wT0v2IEc1r1Ph2gHFaEU%2Btxo5mz61B0aZqMBd5SKfGnE14iyRahjWwm3mTOkaCAIW2pQBZcfsLYGLFjL1Taf5YTzBTY22%2FFUTcCJ41ZoffXXtpCuoSCTWL8bzaBQ8bxDiJ4frUVXF1AR2TBIcKkDQ59kJUR6vyFNh4tAEPZdjglG03f1d1g6bAyt3AeniA6e1QayJCNMRO94Gyr%2FPeJnnZomw%2BhlO%2F%2Fdxz24SVsQBs60%2F58GkxalMsSW56xneWIpZz0NBuAfdLT2KVET4eQZ6fGcAFLr60RLPLQV2d570a%2BmByNyVc8kC6fwmYFyoxWbnZBw4aUTCm6oW9BjqkAdSf2YhD1LQU1JIkgW5qHyBb3fJxvj8JzEbO5r1apH9OCLvI9R%2Bi3dC6YIVBHrDhvU%2FxvQXTPNKcbjBkWUiM%2Ftekqz5NXBTZBq860RiWcF9VjnRsv%2Fgg975ZTexY8mdgXTAyJ5T6IcJAV2ZCzLdh1ZXQ3hbMQEwlwpFZATIntPPzl3mtAbGcLSBp3c2wLp8p8RMgMrHvDJIfgoWB%2FLoNGWQjEhQS&X-Amz-Signature=a8f6315f8f41bfe89faee900772030190505fd384aea2303dc367e095a7d439d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TCHIYVA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQCrqh9xujbqUk64l6WhKrhMCeMTDmUeW%2BHeE4GpeFPl0gIhAOu4Hf1deSN2GwmZxLUI3TE3H6RZ%2Fk1vr%2F3E3bYCzZC0Kv8DCCMQABoMNjM3NDIzMTgzODA1IgzkVUqkCy1vDy2eUrQq3APFxgtttMguazsN%2FC0pFrstIFL6aF2w8bGeGqY5HwQtiAzUsbByjLP488GDUNm6WuqkC%2F2PePQGjjNoon%2B8V7LyU82vpu6jQ4KtaPyw7%2Fuena7lhPUPu%2BZGaOyo%2FwaWMEARuDyp%2F11a6ijE5law%2F39isAxwu%2F%2BADxYzQytLP%2BKZ%2BaNUmtGioY3tIf0GWnhCSOUput%2B5yZSJc1LqR1jiNyCkSr6jjaL51LrFnyMGY75HUSY3i9cwMQHSypUV0z49BxORQT%2B%2B6SDreq9gWizebhYmv1kcmRqGvQYmk1M2xElZKv5l1SojJ0wT0v2IEc1r1Ph2gHFaEU%2Btxo5mz61B0aZqMBd5SKfGnE14iyRahjWwm3mTOkaCAIW2pQBZcfsLYGLFjL1Taf5YTzBTY22%2FFUTcCJ41ZoffXXtpCuoSCTWL8bzaBQ8bxDiJ4frUVXF1AR2TBIcKkDQ59kJUR6vyFNh4tAEPZdjglG03f1d1g6bAyt3AeniA6e1QayJCNMRO94Gyr%2FPeJnnZomw%2BhlO%2F%2Fdxz24SVsQBs60%2F58GkxalMsSW56xneWIpZz0NBuAfdLT2KVET4eQZ6fGcAFLr60RLPLQV2d570a%2BmByNyVc8kC6fwmYFyoxWbnZBw4aUTCm6oW9BjqkAdSf2YhD1LQU1JIkgW5qHyBb3fJxvj8JzEbO5r1apH9OCLvI9R%2Bi3dC6YIVBHrDhvU%2FxvQXTPNKcbjBkWUiM%2Ftekqz5NXBTZBq860RiWcF9VjnRsv%2Fgg975ZTexY8mdgXTAyJ5T6IcJAV2ZCzLdh1ZXQ3hbMQEwlwpFZATIntPPzl3mtAbGcLSBp3c2wLp8p8RMgMrHvDJIfgoWB%2FLoNGWQjEhQS&X-Amz-Signature=f1fa842d612fb1ea8ef44d5f794954cceafc842b9f6d9617c7490ebf1ff39efa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TCHIYVA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQCrqh9xujbqUk64l6WhKrhMCeMTDmUeW%2BHeE4GpeFPl0gIhAOu4Hf1deSN2GwmZxLUI3TE3H6RZ%2Fk1vr%2F3E3bYCzZC0Kv8DCCMQABoMNjM3NDIzMTgzODA1IgzkVUqkCy1vDy2eUrQq3APFxgtttMguazsN%2FC0pFrstIFL6aF2w8bGeGqY5HwQtiAzUsbByjLP488GDUNm6WuqkC%2F2PePQGjjNoon%2B8V7LyU82vpu6jQ4KtaPyw7%2Fuena7lhPUPu%2BZGaOyo%2FwaWMEARuDyp%2F11a6ijE5law%2F39isAxwu%2F%2BADxYzQytLP%2BKZ%2BaNUmtGioY3tIf0GWnhCSOUput%2B5yZSJc1LqR1jiNyCkSr6jjaL51LrFnyMGY75HUSY3i9cwMQHSypUV0z49BxORQT%2B%2B6SDreq9gWizebhYmv1kcmRqGvQYmk1M2xElZKv5l1SojJ0wT0v2IEc1r1Ph2gHFaEU%2Btxo5mz61B0aZqMBd5SKfGnE14iyRahjWwm3mTOkaCAIW2pQBZcfsLYGLFjL1Taf5YTzBTY22%2FFUTcCJ41ZoffXXtpCuoSCTWL8bzaBQ8bxDiJ4frUVXF1AR2TBIcKkDQ59kJUR6vyFNh4tAEPZdjglG03f1d1g6bAyt3AeniA6e1QayJCNMRO94Gyr%2FPeJnnZomw%2BhlO%2F%2Fdxz24SVsQBs60%2F58GkxalMsSW56xneWIpZz0NBuAfdLT2KVET4eQZ6fGcAFLr60RLPLQV2d570a%2BmByNyVc8kC6fwmYFyoxWbnZBw4aUTCm6oW9BjqkAdSf2YhD1LQU1JIkgW5qHyBb3fJxvj8JzEbO5r1apH9OCLvI9R%2Bi3dC6YIVBHrDhvU%2FxvQXTPNKcbjBkWUiM%2Ftekqz5NXBTZBq860RiWcF9VjnRsv%2Fgg975ZTexY8mdgXTAyJ5T6IcJAV2ZCzLdh1ZXQ3hbMQEwlwpFZATIntPPzl3mtAbGcLSBp3c2wLp8p8RMgMrHvDJIfgoWB%2FLoNGWQjEhQS&X-Amz-Signature=041615fa3377fb3712bfc58255eef5f4923c0a2111df8f342b671b9320de1080&X-Amz-SignedHeaders=host&x-id=GetObject)
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


