

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MW5UPJB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIFpugouiUurWRxI9AsPy6N9J%2B67jAEhd2FOXPZ3Ei1MwAiEA6f8AJU6mp%2FpHk4m8KsrbFrHv6p7wwvq9BxR3syorOdsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDKqp0vt5Avo%2FrEJ20CrcAzTi7rlj%2BNt5%2B%2FKw8Mo5PhjvgDqo7HnWV7baV%2Ba5GFCprDrii3C3xYtH4MnC1j0Ti6PKE1WCNSUGz72F6G0scGqLTGrW7BZ%2BUJdLLLws64doFJw3B%2FV%2BsixjzcdQMwWTifeydwM7xCoLnq0N8lSxAptQXld5WdACjMcymUclQfCukFDObLCcnEQeAin9NNzKayPuOC1kN7MZpi%2FbxqxzOPjQbvTbZLXTbHegWrvoArDqqPRJ2PSpT8RLdJNVKzu7vUnT6fHILa6eT7SLdIX7tVkIvKmmAX3Cou5thQxIxN59TXRqkTY%2FwI9fVHo3H6Zp0EWAEwQRrwFqizqv8MCydp5YuFszSTDrd7VzteKH4eZ4mntxLPeLixefCI5OjfjaBBi8fDSan%2FEfDOSWV8YGw2JdBEckWMDN9H0gWZiSRyJNGV2eU6aX9e6xWwbUOBf1rq2ln7sgswrzqHnnb3Th3H0IV4JOhwFAA%2B237%2BekI6LCgt2WE1EkTTGIm8lSnfm2gAUFFYIkvAScGbVRqJbHfieBUOVDn07ZOxLNwjbwL9A9lpT2GudhQ%2Fbw%2F51XCweCpDAX8%2BTtEqQjEcsOKjVfrQvuMvQH8GYD9JqOK0VEkV698D%2F8PSWiF4O8rsnEMOKuh70GOqUBmHfGUgbSG8sQpr5mksDjJbJA8qz%2BZGPFyUT4KyoFCCrUaHGsJxiQlEcaUmLDeTC4zAGDdjMgRrJCvQ%2BysqNdWNJWtNpp7DXrF20ouUFjlqF%2BG4RfOgDLokxFW66P6S27fops1FBa23zf0dCnwqpfY4PrjWXhS6DclxtTMvCSj4uTo%2B7or1erU9l1FbBTAjmEiSWs3SKbvuiORG4ZSEpy5Ro9GY4E&X-Amz-Signature=7aff3d444bb43f1b68303d4060554ed424be1161ad5e2e4979c9c9b8604eeb67&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5HFC5DX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQDdKwFonKvYb5KpK9qLDT%2BuoDxYOtIVYeqspWjq9QCsTQIhAO3SU57ULlZVl0E4it%2ByopCx%2BGRhWNOSyuor81i0jFA8Kv8DCCoQABoMNjM3NDIzMTgzODA1Igw0XKH%2Fqdfl%2FxsYp4gq3APNm2ueEif0O4JVDXBUSzL0dxKaVZDymEviOeUCzKUr7yTezpDnHWOQifyfzYzXnzpOlke3MLSI%2FuoM7I0JUF8PcQQy3lEQ3ZrY2hgA44mWFHmbH4j3ZF9MD0CFI8nkc0LInbLmgBSRDlr8hNCqrDnKUtttR5uEMNXd1LW6hE0hQu9B56yZxyjc1yI75yNCt35Gd5b%2BgDYiOBqnCOfnuwEE02adS%2BJsVSLomh8O%2FxMZXXdiHdnNB24Jxls3kytkCxqvkrhcZbOO6cC0MhX8drDJg8JlYInrxrDhaBG9KSyUNm7lj8V%2BXSshFowgvIvNCB2nWfIPA0SSG1rz9%2B76PoOJcWREbiKR8cwKQ0t%2FWQ8ZGQjQJEholT7T%2BOILifNtTOds9tPktNchW%2FJpukJIP2xy1U58bbAfJx0lxRDMYh3ZRWqTGfvto%2B9mR%2BZ970Vhp%2FuP9WIhr823fMRdMcoJNSATbmppnGsxAE13QHz9p7GVs5DwG4Mp9r2SqmFO8SGpCFiovMzwfh3KRC9Z7ZB2ZXqSV1W8%2FX1SnPG39a6VMGHEKoySNFeD60YeIr0sk92SXvSlUd%2Bf1X1BR9bX3tf52RTq%2BRBi%2FBcgRz6gw1S2g8T8zbvYces%2BeZLhWaUjhzCHroe9BjqkAbtVX1pSZizal8KYPod%2Bbgy14WOo8uwjEJXTFXc1POtb8Wssj9eiJG3TeMoIyPCdxRN8fI2lxZIzpOj55C%2Fvte9p3zMlk6%2BxqMJC%2B1JS3h213T0eO6AvDWn2s%2BRqSCrk14UTjpVbIeOTIuJnnSOdrTN6sNhIvqTshDpdGpTquXHNT7H6RXatcRSx6RlDMJpxTibOgPgJfNWkTBdA6yeZzLAh%2F9rH&X-Amz-Signature=aa0a51fc6fcbc3e989de392c7f5575cd16224e1e24201177428ef1b18aa2c350&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5HFC5DX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQDdKwFonKvYb5KpK9qLDT%2BuoDxYOtIVYeqspWjq9QCsTQIhAO3SU57ULlZVl0E4it%2ByopCx%2BGRhWNOSyuor81i0jFA8Kv8DCCoQABoMNjM3NDIzMTgzODA1Igw0XKH%2Fqdfl%2FxsYp4gq3APNm2ueEif0O4JVDXBUSzL0dxKaVZDymEviOeUCzKUr7yTezpDnHWOQifyfzYzXnzpOlke3MLSI%2FuoM7I0JUF8PcQQy3lEQ3ZrY2hgA44mWFHmbH4j3ZF9MD0CFI8nkc0LInbLmgBSRDlr8hNCqrDnKUtttR5uEMNXd1LW6hE0hQu9B56yZxyjc1yI75yNCt35Gd5b%2BgDYiOBqnCOfnuwEE02adS%2BJsVSLomh8O%2FxMZXXdiHdnNB24Jxls3kytkCxqvkrhcZbOO6cC0MhX8drDJg8JlYInrxrDhaBG9KSyUNm7lj8V%2BXSshFowgvIvNCB2nWfIPA0SSG1rz9%2B76PoOJcWREbiKR8cwKQ0t%2FWQ8ZGQjQJEholT7T%2BOILifNtTOds9tPktNchW%2FJpukJIP2xy1U58bbAfJx0lxRDMYh3ZRWqTGfvto%2B9mR%2BZ970Vhp%2FuP9WIhr823fMRdMcoJNSATbmppnGsxAE13QHz9p7GVs5DwG4Mp9r2SqmFO8SGpCFiovMzwfh3KRC9Z7ZB2ZXqSV1W8%2FX1SnPG39a6VMGHEKoySNFeD60YeIr0sk92SXvSlUd%2Bf1X1BR9bX3tf52RTq%2BRBi%2FBcgRz6gw1S2g8T8zbvYces%2BeZLhWaUjhzCHroe9BjqkAbtVX1pSZizal8KYPod%2Bbgy14WOo8uwjEJXTFXc1POtb8Wssj9eiJG3TeMoIyPCdxRN8fI2lxZIzpOj55C%2Fvte9p3zMlk6%2BxqMJC%2B1JS3h213T0eO6AvDWn2s%2BRqSCrk14UTjpVbIeOTIuJnnSOdrTN6sNhIvqTshDpdGpTquXHNT7H6RXatcRSx6RlDMJpxTibOgPgJfNWkTBdA6yeZzLAh%2F9rH&X-Amz-Signature=2e3983b9407e2efb55355a614229170e405ef735441762f6548d967d9342b3d7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5HFC5DX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQDdKwFonKvYb5KpK9qLDT%2BuoDxYOtIVYeqspWjq9QCsTQIhAO3SU57ULlZVl0E4it%2ByopCx%2BGRhWNOSyuor81i0jFA8Kv8DCCoQABoMNjM3NDIzMTgzODA1Igw0XKH%2Fqdfl%2FxsYp4gq3APNm2ueEif0O4JVDXBUSzL0dxKaVZDymEviOeUCzKUr7yTezpDnHWOQifyfzYzXnzpOlke3MLSI%2FuoM7I0JUF8PcQQy3lEQ3ZrY2hgA44mWFHmbH4j3ZF9MD0CFI8nkc0LInbLmgBSRDlr8hNCqrDnKUtttR5uEMNXd1LW6hE0hQu9B56yZxyjc1yI75yNCt35Gd5b%2BgDYiOBqnCOfnuwEE02adS%2BJsVSLomh8O%2FxMZXXdiHdnNB24Jxls3kytkCxqvkrhcZbOO6cC0MhX8drDJg8JlYInrxrDhaBG9KSyUNm7lj8V%2BXSshFowgvIvNCB2nWfIPA0SSG1rz9%2B76PoOJcWREbiKR8cwKQ0t%2FWQ8ZGQjQJEholT7T%2BOILifNtTOds9tPktNchW%2FJpukJIP2xy1U58bbAfJx0lxRDMYh3ZRWqTGfvto%2B9mR%2BZ970Vhp%2FuP9WIhr823fMRdMcoJNSATbmppnGsxAE13QHz9p7GVs5DwG4Mp9r2SqmFO8SGpCFiovMzwfh3KRC9Z7ZB2ZXqSV1W8%2FX1SnPG39a6VMGHEKoySNFeD60YeIr0sk92SXvSlUd%2Bf1X1BR9bX3tf52RTq%2BRBi%2FBcgRz6gw1S2g8T8zbvYces%2BeZLhWaUjhzCHroe9BjqkAbtVX1pSZizal8KYPod%2Bbgy14WOo8uwjEJXTFXc1POtb8Wssj9eiJG3TeMoIyPCdxRN8fI2lxZIzpOj55C%2Fvte9p3zMlk6%2BxqMJC%2B1JS3h213T0eO6AvDWn2s%2BRqSCrk14UTjpVbIeOTIuJnnSOdrTN6sNhIvqTshDpdGpTquXHNT7H6RXatcRSx6RlDMJpxTibOgPgJfNWkTBdA6yeZzLAh%2F9rH&X-Amz-Signature=176f7e123157cbe7c832ac0134e601579c229f1cf22cd8f36ce40adf4ff70b2d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5HFC5DX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQDdKwFonKvYb5KpK9qLDT%2BuoDxYOtIVYeqspWjq9QCsTQIhAO3SU57ULlZVl0E4it%2ByopCx%2BGRhWNOSyuor81i0jFA8Kv8DCCoQABoMNjM3NDIzMTgzODA1Igw0XKH%2Fqdfl%2FxsYp4gq3APNm2ueEif0O4JVDXBUSzL0dxKaVZDymEviOeUCzKUr7yTezpDnHWOQifyfzYzXnzpOlke3MLSI%2FuoM7I0JUF8PcQQy3lEQ3ZrY2hgA44mWFHmbH4j3ZF9MD0CFI8nkc0LInbLmgBSRDlr8hNCqrDnKUtttR5uEMNXd1LW6hE0hQu9B56yZxyjc1yI75yNCt35Gd5b%2BgDYiOBqnCOfnuwEE02adS%2BJsVSLomh8O%2FxMZXXdiHdnNB24Jxls3kytkCxqvkrhcZbOO6cC0MhX8drDJg8JlYInrxrDhaBG9KSyUNm7lj8V%2BXSshFowgvIvNCB2nWfIPA0SSG1rz9%2B76PoOJcWREbiKR8cwKQ0t%2FWQ8ZGQjQJEholT7T%2BOILifNtTOds9tPktNchW%2FJpukJIP2xy1U58bbAfJx0lxRDMYh3ZRWqTGfvto%2B9mR%2BZ970Vhp%2FuP9WIhr823fMRdMcoJNSATbmppnGsxAE13QHz9p7GVs5DwG4Mp9r2SqmFO8SGpCFiovMzwfh3KRC9Z7ZB2ZXqSV1W8%2FX1SnPG39a6VMGHEKoySNFeD60YeIr0sk92SXvSlUd%2Bf1X1BR9bX3tf52RTq%2BRBi%2FBcgRz6gw1S2g8T8zbvYces%2BeZLhWaUjhzCHroe9BjqkAbtVX1pSZizal8KYPod%2Bbgy14WOo8uwjEJXTFXc1POtb8Wssj9eiJG3TeMoIyPCdxRN8fI2lxZIzpOj55C%2Fvte9p3zMlk6%2BxqMJC%2B1JS3h213T0eO6AvDWn2s%2BRqSCrk14UTjpVbIeOTIuJnnSOdrTN6sNhIvqTshDpdGpTquXHNT7H6RXatcRSx6RlDMJpxTibOgPgJfNWkTBdA6yeZzLAh%2F9rH&X-Amz-Signature=6352dd5f1083457a4487da63a70e6d592ca237823c85e554d09b39ba581e575a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5HFC5DX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQDdKwFonKvYb5KpK9qLDT%2BuoDxYOtIVYeqspWjq9QCsTQIhAO3SU57ULlZVl0E4it%2ByopCx%2BGRhWNOSyuor81i0jFA8Kv8DCCoQABoMNjM3NDIzMTgzODA1Igw0XKH%2Fqdfl%2FxsYp4gq3APNm2ueEif0O4JVDXBUSzL0dxKaVZDymEviOeUCzKUr7yTezpDnHWOQifyfzYzXnzpOlke3MLSI%2FuoM7I0JUF8PcQQy3lEQ3ZrY2hgA44mWFHmbH4j3ZF9MD0CFI8nkc0LInbLmgBSRDlr8hNCqrDnKUtttR5uEMNXd1LW6hE0hQu9B56yZxyjc1yI75yNCt35Gd5b%2BgDYiOBqnCOfnuwEE02adS%2BJsVSLomh8O%2FxMZXXdiHdnNB24Jxls3kytkCxqvkrhcZbOO6cC0MhX8drDJg8JlYInrxrDhaBG9KSyUNm7lj8V%2BXSshFowgvIvNCB2nWfIPA0SSG1rz9%2B76PoOJcWREbiKR8cwKQ0t%2FWQ8ZGQjQJEholT7T%2BOILifNtTOds9tPktNchW%2FJpukJIP2xy1U58bbAfJx0lxRDMYh3ZRWqTGfvto%2B9mR%2BZ970Vhp%2FuP9WIhr823fMRdMcoJNSATbmppnGsxAE13QHz9p7GVs5DwG4Mp9r2SqmFO8SGpCFiovMzwfh3KRC9Z7ZB2ZXqSV1W8%2FX1SnPG39a6VMGHEKoySNFeD60YeIr0sk92SXvSlUd%2Bf1X1BR9bX3tf52RTq%2BRBi%2FBcgRz6gw1S2g8T8zbvYces%2BeZLhWaUjhzCHroe9BjqkAbtVX1pSZizal8KYPod%2Bbgy14WOo8uwjEJXTFXc1POtb8Wssj9eiJG3TeMoIyPCdxRN8fI2lxZIzpOj55C%2Fvte9p3zMlk6%2BxqMJC%2B1JS3h213T0eO6AvDWn2s%2BRqSCrk14UTjpVbIeOTIuJnnSOdrTN6sNhIvqTshDpdGpTquXHNT7H6RXatcRSx6RlDMJpxTibOgPgJfNWkTBdA6yeZzLAh%2F9rH&X-Amz-Signature=4b1ea9032c865eda7a6726d2d9a3766c3fdb2d0a273f142f507c4ac92dddff26&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MW5UPJB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIFpugouiUurWRxI9AsPy6N9J%2B67jAEhd2FOXPZ3Ei1MwAiEA6f8AJU6mp%2FpHk4m8KsrbFrHv6p7wwvq9BxR3syorOdsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDKqp0vt5Avo%2FrEJ20CrcAzTi7rlj%2BNt5%2B%2FKw8Mo5PhjvgDqo7HnWV7baV%2Ba5GFCprDrii3C3xYtH4MnC1j0Ti6PKE1WCNSUGz72F6G0scGqLTGrW7BZ%2BUJdLLLws64doFJw3B%2FV%2BsixjzcdQMwWTifeydwM7xCoLnq0N8lSxAptQXld5WdACjMcymUclQfCukFDObLCcnEQeAin9NNzKayPuOC1kN7MZpi%2FbxqxzOPjQbvTbZLXTbHegWrvoArDqqPRJ2PSpT8RLdJNVKzu7vUnT6fHILa6eT7SLdIX7tVkIvKmmAX3Cou5thQxIxN59TXRqkTY%2FwI9fVHo3H6Zp0EWAEwQRrwFqizqv8MCydp5YuFszSTDrd7VzteKH4eZ4mntxLPeLixefCI5OjfjaBBi8fDSan%2FEfDOSWV8YGw2JdBEckWMDN9H0gWZiSRyJNGV2eU6aX9e6xWwbUOBf1rq2ln7sgswrzqHnnb3Th3H0IV4JOhwFAA%2B237%2BekI6LCgt2WE1EkTTGIm8lSnfm2gAUFFYIkvAScGbVRqJbHfieBUOVDn07ZOxLNwjbwL9A9lpT2GudhQ%2Fbw%2F51XCweCpDAX8%2BTtEqQjEcsOKjVfrQvuMvQH8GYD9JqOK0VEkV698D%2F8PSWiF4O8rsnEMOKuh70GOqUBmHfGUgbSG8sQpr5mksDjJbJA8qz%2BZGPFyUT4KyoFCCrUaHGsJxiQlEcaUmLDeTC4zAGDdjMgRrJCvQ%2BysqNdWNJWtNpp7DXrF20ouUFjlqF%2BG4RfOgDLokxFW66P6S27fops1FBa23zf0dCnwqpfY4PrjWXhS6DclxtTMvCSj4uTo%2B7or1erU9l1FbBTAjmEiSWs3SKbvuiORG4ZSEpy5Ro9GY4E&X-Amz-Signature=f1bd0f6da1852350814b45e1d7b7a65957f2daee3f08e1b1a2d238552510c95c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MW5UPJB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIFpugouiUurWRxI9AsPy6N9J%2B67jAEhd2FOXPZ3Ei1MwAiEA6f8AJU6mp%2FpHk4m8KsrbFrHv6p7wwvq9BxR3syorOdsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDKqp0vt5Avo%2FrEJ20CrcAzTi7rlj%2BNt5%2B%2FKw8Mo5PhjvgDqo7HnWV7baV%2Ba5GFCprDrii3C3xYtH4MnC1j0Ti6PKE1WCNSUGz72F6G0scGqLTGrW7BZ%2BUJdLLLws64doFJw3B%2FV%2BsixjzcdQMwWTifeydwM7xCoLnq0N8lSxAptQXld5WdACjMcymUclQfCukFDObLCcnEQeAin9NNzKayPuOC1kN7MZpi%2FbxqxzOPjQbvTbZLXTbHegWrvoArDqqPRJ2PSpT8RLdJNVKzu7vUnT6fHILa6eT7SLdIX7tVkIvKmmAX3Cou5thQxIxN59TXRqkTY%2FwI9fVHo3H6Zp0EWAEwQRrwFqizqv8MCydp5YuFszSTDrd7VzteKH4eZ4mntxLPeLixefCI5OjfjaBBi8fDSan%2FEfDOSWV8YGw2JdBEckWMDN9H0gWZiSRyJNGV2eU6aX9e6xWwbUOBf1rq2ln7sgswrzqHnnb3Th3H0IV4JOhwFAA%2B237%2BekI6LCgt2WE1EkTTGIm8lSnfm2gAUFFYIkvAScGbVRqJbHfieBUOVDn07ZOxLNwjbwL9A9lpT2GudhQ%2Fbw%2F51XCweCpDAX8%2BTtEqQjEcsOKjVfrQvuMvQH8GYD9JqOK0VEkV698D%2F8PSWiF4O8rsnEMOKuh70GOqUBmHfGUgbSG8sQpr5mksDjJbJA8qz%2BZGPFyUT4KyoFCCrUaHGsJxiQlEcaUmLDeTC4zAGDdjMgRrJCvQ%2BysqNdWNJWtNpp7DXrF20ouUFjlqF%2BG4RfOgDLokxFW66P6S27fops1FBa23zf0dCnwqpfY4PrjWXhS6DclxtTMvCSj4uTo%2B7or1erU9l1FbBTAjmEiSWs3SKbvuiORG4ZSEpy5Ro9GY4E&X-Amz-Signature=c9c51c61b7ca41679a400363c5d5dd2c50c3408bf56d1630fb80a3d26b990549&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MW5UPJB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIFpugouiUurWRxI9AsPy6N9J%2B67jAEhd2FOXPZ3Ei1MwAiEA6f8AJU6mp%2FpHk4m8KsrbFrHv6p7wwvq9BxR3syorOdsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDKqp0vt5Avo%2FrEJ20CrcAzTi7rlj%2BNt5%2B%2FKw8Mo5PhjvgDqo7HnWV7baV%2Ba5GFCprDrii3C3xYtH4MnC1j0Ti6PKE1WCNSUGz72F6G0scGqLTGrW7BZ%2BUJdLLLws64doFJw3B%2FV%2BsixjzcdQMwWTifeydwM7xCoLnq0N8lSxAptQXld5WdACjMcymUclQfCukFDObLCcnEQeAin9NNzKayPuOC1kN7MZpi%2FbxqxzOPjQbvTbZLXTbHegWrvoArDqqPRJ2PSpT8RLdJNVKzu7vUnT6fHILa6eT7SLdIX7tVkIvKmmAX3Cou5thQxIxN59TXRqkTY%2FwI9fVHo3H6Zp0EWAEwQRrwFqizqv8MCydp5YuFszSTDrd7VzteKH4eZ4mntxLPeLixefCI5OjfjaBBi8fDSan%2FEfDOSWV8YGw2JdBEckWMDN9H0gWZiSRyJNGV2eU6aX9e6xWwbUOBf1rq2ln7sgswrzqHnnb3Th3H0IV4JOhwFAA%2B237%2BekI6LCgt2WE1EkTTGIm8lSnfm2gAUFFYIkvAScGbVRqJbHfieBUOVDn07ZOxLNwjbwL9A9lpT2GudhQ%2Fbw%2F51XCweCpDAX8%2BTtEqQjEcsOKjVfrQvuMvQH8GYD9JqOK0VEkV698D%2F8PSWiF4O8rsnEMOKuh70GOqUBmHfGUgbSG8sQpr5mksDjJbJA8qz%2BZGPFyUT4KyoFCCrUaHGsJxiQlEcaUmLDeTC4zAGDdjMgRrJCvQ%2BysqNdWNJWtNpp7DXrF20ouUFjlqF%2BG4RfOgDLokxFW66P6S27fops1FBa23zf0dCnwqpfY4PrjWXhS6DclxtTMvCSj4uTo%2B7or1erU9l1FbBTAjmEiSWs3SKbvuiORG4ZSEpy5Ro9GY4E&X-Amz-Signature=e49fcbf307e15f1584d059eef4f5ab4799f6c149fcb455e850edc5eba5174009&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MW5UPJB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIFpugouiUurWRxI9AsPy6N9J%2B67jAEhd2FOXPZ3Ei1MwAiEA6f8AJU6mp%2FpHk4m8KsrbFrHv6p7wwvq9BxR3syorOdsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDKqp0vt5Avo%2FrEJ20CrcAzTi7rlj%2BNt5%2B%2FKw8Mo5PhjvgDqo7HnWV7baV%2Ba5GFCprDrii3C3xYtH4MnC1j0Ti6PKE1WCNSUGz72F6G0scGqLTGrW7BZ%2BUJdLLLws64doFJw3B%2FV%2BsixjzcdQMwWTifeydwM7xCoLnq0N8lSxAptQXld5WdACjMcymUclQfCukFDObLCcnEQeAin9NNzKayPuOC1kN7MZpi%2FbxqxzOPjQbvTbZLXTbHegWrvoArDqqPRJ2PSpT8RLdJNVKzu7vUnT6fHILa6eT7SLdIX7tVkIvKmmAX3Cou5thQxIxN59TXRqkTY%2FwI9fVHo3H6Zp0EWAEwQRrwFqizqv8MCydp5YuFszSTDrd7VzteKH4eZ4mntxLPeLixefCI5OjfjaBBi8fDSan%2FEfDOSWV8YGw2JdBEckWMDN9H0gWZiSRyJNGV2eU6aX9e6xWwbUOBf1rq2ln7sgswrzqHnnb3Th3H0IV4JOhwFAA%2B237%2BekI6LCgt2WE1EkTTGIm8lSnfm2gAUFFYIkvAScGbVRqJbHfieBUOVDn07ZOxLNwjbwL9A9lpT2GudhQ%2Fbw%2F51XCweCpDAX8%2BTtEqQjEcsOKjVfrQvuMvQH8GYD9JqOK0VEkV698D%2F8PSWiF4O8rsnEMOKuh70GOqUBmHfGUgbSG8sQpr5mksDjJbJA8qz%2BZGPFyUT4KyoFCCrUaHGsJxiQlEcaUmLDeTC4zAGDdjMgRrJCvQ%2BysqNdWNJWtNpp7DXrF20ouUFjlqF%2BG4RfOgDLokxFW66P6S27fops1FBa23zf0dCnwqpfY4PrjWXhS6DclxtTMvCSj4uTo%2B7or1erU9l1FbBTAjmEiSWs3SKbvuiORG4ZSEpy5Ro9GY4E&X-Amz-Signature=6dcefb306987d17acd7f00d50ca2372e93ee381ea9340569bf4af81f0918a530&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MW5UPJB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIFpugouiUurWRxI9AsPy6N9J%2B67jAEhd2FOXPZ3Ei1MwAiEA6f8AJU6mp%2FpHk4m8KsrbFrHv6p7wwvq9BxR3syorOdsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDKqp0vt5Avo%2FrEJ20CrcAzTi7rlj%2BNt5%2B%2FKw8Mo5PhjvgDqo7HnWV7baV%2Ba5GFCprDrii3C3xYtH4MnC1j0Ti6PKE1WCNSUGz72F6G0scGqLTGrW7BZ%2BUJdLLLws64doFJw3B%2FV%2BsixjzcdQMwWTifeydwM7xCoLnq0N8lSxAptQXld5WdACjMcymUclQfCukFDObLCcnEQeAin9NNzKayPuOC1kN7MZpi%2FbxqxzOPjQbvTbZLXTbHegWrvoArDqqPRJ2PSpT8RLdJNVKzu7vUnT6fHILa6eT7SLdIX7tVkIvKmmAX3Cou5thQxIxN59TXRqkTY%2FwI9fVHo3H6Zp0EWAEwQRrwFqizqv8MCydp5YuFszSTDrd7VzteKH4eZ4mntxLPeLixefCI5OjfjaBBi8fDSan%2FEfDOSWV8YGw2JdBEckWMDN9H0gWZiSRyJNGV2eU6aX9e6xWwbUOBf1rq2ln7sgswrzqHnnb3Th3H0IV4JOhwFAA%2B237%2BekI6LCgt2WE1EkTTGIm8lSnfm2gAUFFYIkvAScGbVRqJbHfieBUOVDn07ZOxLNwjbwL9A9lpT2GudhQ%2Fbw%2F51XCweCpDAX8%2BTtEqQjEcsOKjVfrQvuMvQH8GYD9JqOK0VEkV698D%2F8PSWiF4O8rsnEMOKuh70GOqUBmHfGUgbSG8sQpr5mksDjJbJA8qz%2BZGPFyUT4KyoFCCrUaHGsJxiQlEcaUmLDeTC4zAGDdjMgRrJCvQ%2BysqNdWNJWtNpp7DXrF20ouUFjlqF%2BG4RfOgDLokxFW66P6S27fops1FBa23zf0dCnwqpfY4PrjWXhS6DclxtTMvCSj4uTo%2B7or1erU9l1FbBTAjmEiSWs3SKbvuiORG4ZSEpy5Ro9GY4E&X-Amz-Signature=bbc36f3a72f1c2548bcdc72c33436493d65bc249876602df75de2bb01e4ad17d&X-Amz-SignedHeaders=host&x-id=GetObject)
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


