

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FRGKNOF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDT23vturOOpMnPPo6dhRdBG2EeXi%2BrzNVocfgNfSaQ%2FgIgLdU%2FLksE6GQX22tj6rUiJKK6R6sa7F1fM7Hx27wKIDwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAGX4JNd3WDpsJFmTSrcA8hcdjmhJZ%2BCh6oUY9UrbxJKUPVfZyEQ3GnLySXpS71zMW2knVeIxc%2BtCQlNFjaYRFDhxIX0ojiRdtMKiaamXDza6M3rns5PKhIjN4BBwSUwKRC3yBT4Hp6vHnNSVOkE487%2Bdp0%2BR6QviHYNHouy808cWWplvrlgE3hD8c%2BG0w2fN4nDOTnDGw3AHJ7e%2F9OGIjCQV7UkUPQ9839DFZu%2FiHbNbW5d%2BbB2Ju%2BeYuTz4tihCXyfqlFSqmQgQNsxRnirTHg9qk%2FWakdnXN%2FWjECKSQs%2F8FwXvYQfmnTjraCO3DYaRJP6UP8Rly4ThhGmWubhgl3Jt4OOmyokc5UHDLX0OrGOqvqdCHK%2BtYTjcYercJAqJY%2Bc8ZVX4SE0NVI8zz23iM0Q94LLoXxabXWE5qsOO4Jh8%2Frlw7ZvuY%2BXeEuDlqP2eiNCmviBMBJBhrFDIdJEfoU66TLQzkPE04yFFjO8tREnAaHS0kWPBXQN0hP6UD6e7WPvHwCeGIlDwAI3fAy%2BXqvXw0YmuJlT2TvNKBddjwLy1yb8szPKgvPmXCGF87Lip0rCSV%2BRRxu70AQ0DAr3osOxNbuAwUV42va%2F9oRami450WBoS8njrYq6YjKeTMjG8jOCIQbMuebVtrGOMLS6jr0GOqUBwyTknFaJclcXhg8C29p%2B%2F8fIMI7Am8XIQ8Vr2Sk%2Bj%2BTVaejISsD5G5j8fM2CFOPtuhxMsvfHu9xl9%2B%2BkUYIrw0GBSpjTrnGZdPzVVE6nNMm4cHlqa6R4SPP1iB7%2BB9O6BjGOPJ1Rcna2iQjE1JJ6g%2BhQIeBVIJVRDtO%2BSs2D%2FeJRdKSloO7cT5NTVUlACbyb8FGzFx822Rc0o26J0LwgjeAUPQ%2FH&X-Amz-Signature=0db50d0e32aa6e6ab479bdb2ce501ecc254ca3c973862112394b8e6ed923c195&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RCUB7HM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIB7RRXLFV%2FS2Vo01OzgDq0jtFoAnSqEZF5J3IQoh4U65AiBq3cQxpmRNh1Zt5OkTb2xRhvhC2LmcDFmlWpgem6YZJyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMFc5jH4arEPy1HH1IKtwDUuDwXuxzOj7sP8iinELheT2sB%2BnHmYJ6VnXfOjMOnodKVF5Sx4bDYHjA%2BoZ8azscAvd8tzTniXJ8Dm6ZnPZZ069tmvUewsx%2BXi7A%2BXExP%2BbDtO4pxYBGY1De6y6gcvDBicQ%2FhxZcR1UyRuH%2BEcB5uhM1UfUkmntrY4hLEHMH1YRuEjVlDEVb7xLg2w2WB3P44z130%2B4N2vJU55ZSKrvk9HZJXRDaySmJhSQ9UFECH1CfWyIfzfiyZZTsjYEGRovizLEk9Q8C%2FCEtmF%2BE9K5aj7FKthtqpHSrdwsMQ4Y3aSAIG%2BIiAZDIO02rwrK1WC%2BoMl8HFKK3fMFw78uMgzmf%2BNWiCaz5uP9%2B30sHQPMhLNXep6n71cQdvGbeHgg7ZBZo1z64Z3IQw8hAEg6G%2Bjd81ro1PU5ZaKmUILmDSv35g9mA8HUi%2B6uuA2mUkW7yMyWnShgf3pNcaIJoYYuDBr3bs3i2tcdMIidE4gVKmZ4zT4pGIlG5kC84YgV1ceK8ZZCyyiVfhBrc8hc2HtB9knS%2FVyqcrnns4ioNKmmPVqnWHlZa1o72HtQdOZF1jJ7qyfi9kv8ZRGtP2PhApOKd2O0DNqWezs%2BCrBH0vdLJUUML%2FNYq1w867XRV9LiLxqkw57qOvQY6pgGc2ntRtqGG6I3l0sSP%2FH3bSQBh4onRCtf2v%2BlES2u4CGdYm%2FXC7%2FHhiDgl3n%2BR0DOy1CbmkelG27577mpWwCxMUDTzJH1RnzKN3AeYnzWkjxJQALXuXqhMmzr2JTWFrzglvA0kogpfUuuYZjH5j64EPR9jRk7MvBoOv6r8K8HOoH0Cp3L9jlKeJhroqP%2FRZN710EDUsPzHuN2Q2z1vRpa%2BcTr2c5Ic&X-Amz-Signature=7a8e36e7512e31fa5d920650de6b9e99a386a68525b18a1f134f8f25de707e9e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RCUB7HM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIB7RRXLFV%2FS2Vo01OzgDq0jtFoAnSqEZF5J3IQoh4U65AiBq3cQxpmRNh1Zt5OkTb2xRhvhC2LmcDFmlWpgem6YZJyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMFc5jH4arEPy1HH1IKtwDUuDwXuxzOj7sP8iinELheT2sB%2BnHmYJ6VnXfOjMOnodKVF5Sx4bDYHjA%2BoZ8azscAvd8tzTniXJ8Dm6ZnPZZ069tmvUewsx%2BXi7A%2BXExP%2BbDtO4pxYBGY1De6y6gcvDBicQ%2FhxZcR1UyRuH%2BEcB5uhM1UfUkmntrY4hLEHMH1YRuEjVlDEVb7xLg2w2WB3P44z130%2B4N2vJU55ZSKrvk9HZJXRDaySmJhSQ9UFECH1CfWyIfzfiyZZTsjYEGRovizLEk9Q8C%2FCEtmF%2BE9K5aj7FKthtqpHSrdwsMQ4Y3aSAIG%2BIiAZDIO02rwrK1WC%2BoMl8HFKK3fMFw78uMgzmf%2BNWiCaz5uP9%2B30sHQPMhLNXep6n71cQdvGbeHgg7ZBZo1z64Z3IQw8hAEg6G%2Bjd81ro1PU5ZaKmUILmDSv35g9mA8HUi%2B6uuA2mUkW7yMyWnShgf3pNcaIJoYYuDBr3bs3i2tcdMIidE4gVKmZ4zT4pGIlG5kC84YgV1ceK8ZZCyyiVfhBrc8hc2HtB9knS%2FVyqcrnns4ioNKmmPVqnWHlZa1o72HtQdOZF1jJ7qyfi9kv8ZRGtP2PhApOKd2O0DNqWezs%2BCrBH0vdLJUUML%2FNYq1w867XRV9LiLxqkw57qOvQY6pgGc2ntRtqGG6I3l0sSP%2FH3bSQBh4onRCtf2v%2BlES2u4CGdYm%2FXC7%2FHhiDgl3n%2BR0DOy1CbmkelG27577mpWwCxMUDTzJH1RnzKN3AeYnzWkjxJQALXuXqhMmzr2JTWFrzglvA0kogpfUuuYZjH5j64EPR9jRk7MvBoOv6r8K8HOoH0Cp3L9jlKeJhroqP%2FRZN710EDUsPzHuN2Q2z1vRpa%2BcTr2c5Ic&X-Amz-Signature=355cd7d2c9051f4dfde9694fa4fababaeaf234c2bb2888205ec96160b314328d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RCUB7HM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIB7RRXLFV%2FS2Vo01OzgDq0jtFoAnSqEZF5J3IQoh4U65AiBq3cQxpmRNh1Zt5OkTb2xRhvhC2LmcDFmlWpgem6YZJyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMFc5jH4arEPy1HH1IKtwDUuDwXuxzOj7sP8iinELheT2sB%2BnHmYJ6VnXfOjMOnodKVF5Sx4bDYHjA%2BoZ8azscAvd8tzTniXJ8Dm6ZnPZZ069tmvUewsx%2BXi7A%2BXExP%2BbDtO4pxYBGY1De6y6gcvDBicQ%2FhxZcR1UyRuH%2BEcB5uhM1UfUkmntrY4hLEHMH1YRuEjVlDEVb7xLg2w2WB3P44z130%2B4N2vJU55ZSKrvk9HZJXRDaySmJhSQ9UFECH1CfWyIfzfiyZZTsjYEGRovizLEk9Q8C%2FCEtmF%2BE9K5aj7FKthtqpHSrdwsMQ4Y3aSAIG%2BIiAZDIO02rwrK1WC%2BoMl8HFKK3fMFw78uMgzmf%2BNWiCaz5uP9%2B30sHQPMhLNXep6n71cQdvGbeHgg7ZBZo1z64Z3IQw8hAEg6G%2Bjd81ro1PU5ZaKmUILmDSv35g9mA8HUi%2B6uuA2mUkW7yMyWnShgf3pNcaIJoYYuDBr3bs3i2tcdMIidE4gVKmZ4zT4pGIlG5kC84YgV1ceK8ZZCyyiVfhBrc8hc2HtB9knS%2FVyqcrnns4ioNKmmPVqnWHlZa1o72HtQdOZF1jJ7qyfi9kv8ZRGtP2PhApOKd2O0DNqWezs%2BCrBH0vdLJUUML%2FNYq1w867XRV9LiLxqkw57qOvQY6pgGc2ntRtqGG6I3l0sSP%2FH3bSQBh4onRCtf2v%2BlES2u4CGdYm%2FXC7%2FHhiDgl3n%2BR0DOy1CbmkelG27577mpWwCxMUDTzJH1RnzKN3AeYnzWkjxJQALXuXqhMmzr2JTWFrzglvA0kogpfUuuYZjH5j64EPR9jRk7MvBoOv6r8K8HOoH0Cp3L9jlKeJhroqP%2FRZN710EDUsPzHuN2Q2z1vRpa%2BcTr2c5Ic&X-Amz-Signature=cac0ed6d131cbe59315c35a93f5547f34f71b376160f0b7658697e5bf8c5d07f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RCUB7HM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIB7RRXLFV%2FS2Vo01OzgDq0jtFoAnSqEZF5J3IQoh4U65AiBq3cQxpmRNh1Zt5OkTb2xRhvhC2LmcDFmlWpgem6YZJyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMFc5jH4arEPy1HH1IKtwDUuDwXuxzOj7sP8iinELheT2sB%2BnHmYJ6VnXfOjMOnodKVF5Sx4bDYHjA%2BoZ8azscAvd8tzTniXJ8Dm6ZnPZZ069tmvUewsx%2BXi7A%2BXExP%2BbDtO4pxYBGY1De6y6gcvDBicQ%2FhxZcR1UyRuH%2BEcB5uhM1UfUkmntrY4hLEHMH1YRuEjVlDEVb7xLg2w2WB3P44z130%2B4N2vJU55ZSKrvk9HZJXRDaySmJhSQ9UFECH1CfWyIfzfiyZZTsjYEGRovizLEk9Q8C%2FCEtmF%2BE9K5aj7FKthtqpHSrdwsMQ4Y3aSAIG%2BIiAZDIO02rwrK1WC%2BoMl8HFKK3fMFw78uMgzmf%2BNWiCaz5uP9%2B30sHQPMhLNXep6n71cQdvGbeHgg7ZBZo1z64Z3IQw8hAEg6G%2Bjd81ro1PU5ZaKmUILmDSv35g9mA8HUi%2B6uuA2mUkW7yMyWnShgf3pNcaIJoYYuDBr3bs3i2tcdMIidE4gVKmZ4zT4pGIlG5kC84YgV1ceK8ZZCyyiVfhBrc8hc2HtB9knS%2FVyqcrnns4ioNKmmPVqnWHlZa1o72HtQdOZF1jJ7qyfi9kv8ZRGtP2PhApOKd2O0DNqWezs%2BCrBH0vdLJUUML%2FNYq1w867XRV9LiLxqkw57qOvQY6pgGc2ntRtqGG6I3l0sSP%2FH3bSQBh4onRCtf2v%2BlES2u4CGdYm%2FXC7%2FHhiDgl3n%2BR0DOy1CbmkelG27577mpWwCxMUDTzJH1RnzKN3AeYnzWkjxJQALXuXqhMmzr2JTWFrzglvA0kogpfUuuYZjH5j64EPR9jRk7MvBoOv6r8K8HOoH0Cp3L9jlKeJhroqP%2FRZN710EDUsPzHuN2Q2z1vRpa%2BcTr2c5Ic&X-Amz-Signature=1a3898f5dcfe39c373685a93047063a0cdc376f079600ec060f7a4e9b1a34be4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RCUB7HM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIB7RRXLFV%2FS2Vo01OzgDq0jtFoAnSqEZF5J3IQoh4U65AiBq3cQxpmRNh1Zt5OkTb2xRhvhC2LmcDFmlWpgem6YZJyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMFc5jH4arEPy1HH1IKtwDUuDwXuxzOj7sP8iinELheT2sB%2BnHmYJ6VnXfOjMOnodKVF5Sx4bDYHjA%2BoZ8azscAvd8tzTniXJ8Dm6ZnPZZ069tmvUewsx%2BXi7A%2BXExP%2BbDtO4pxYBGY1De6y6gcvDBicQ%2FhxZcR1UyRuH%2BEcB5uhM1UfUkmntrY4hLEHMH1YRuEjVlDEVb7xLg2w2WB3P44z130%2B4N2vJU55ZSKrvk9HZJXRDaySmJhSQ9UFECH1CfWyIfzfiyZZTsjYEGRovizLEk9Q8C%2FCEtmF%2BE9K5aj7FKthtqpHSrdwsMQ4Y3aSAIG%2BIiAZDIO02rwrK1WC%2BoMl8HFKK3fMFw78uMgzmf%2BNWiCaz5uP9%2B30sHQPMhLNXep6n71cQdvGbeHgg7ZBZo1z64Z3IQw8hAEg6G%2Bjd81ro1PU5ZaKmUILmDSv35g9mA8HUi%2B6uuA2mUkW7yMyWnShgf3pNcaIJoYYuDBr3bs3i2tcdMIidE4gVKmZ4zT4pGIlG5kC84YgV1ceK8ZZCyyiVfhBrc8hc2HtB9knS%2FVyqcrnns4ioNKmmPVqnWHlZa1o72HtQdOZF1jJ7qyfi9kv8ZRGtP2PhApOKd2O0DNqWezs%2BCrBH0vdLJUUML%2FNYq1w867XRV9LiLxqkw57qOvQY6pgGc2ntRtqGG6I3l0sSP%2FH3bSQBh4onRCtf2v%2BlES2u4CGdYm%2FXC7%2FHhiDgl3n%2BR0DOy1CbmkelG27577mpWwCxMUDTzJH1RnzKN3AeYnzWkjxJQALXuXqhMmzr2JTWFrzglvA0kogpfUuuYZjH5j64EPR9jRk7MvBoOv6r8K8HOoH0Cp3L9jlKeJhroqP%2FRZN710EDUsPzHuN2Q2z1vRpa%2BcTr2c5Ic&X-Amz-Signature=0d2aba3c0be4c7548479167e135af7874cda385c3a9d55ba500dcf083aaee1e4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FRGKNOF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDT23vturOOpMnPPo6dhRdBG2EeXi%2BrzNVocfgNfSaQ%2FgIgLdU%2FLksE6GQX22tj6rUiJKK6R6sa7F1fM7Hx27wKIDwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAGX4JNd3WDpsJFmTSrcA8hcdjmhJZ%2BCh6oUY9UrbxJKUPVfZyEQ3GnLySXpS71zMW2knVeIxc%2BtCQlNFjaYRFDhxIX0ojiRdtMKiaamXDza6M3rns5PKhIjN4BBwSUwKRC3yBT4Hp6vHnNSVOkE487%2Bdp0%2BR6QviHYNHouy808cWWplvrlgE3hD8c%2BG0w2fN4nDOTnDGw3AHJ7e%2F9OGIjCQV7UkUPQ9839DFZu%2FiHbNbW5d%2BbB2Ju%2BeYuTz4tihCXyfqlFSqmQgQNsxRnirTHg9qk%2FWakdnXN%2FWjECKSQs%2F8FwXvYQfmnTjraCO3DYaRJP6UP8Rly4ThhGmWubhgl3Jt4OOmyokc5UHDLX0OrGOqvqdCHK%2BtYTjcYercJAqJY%2Bc8ZVX4SE0NVI8zz23iM0Q94LLoXxabXWE5qsOO4Jh8%2Frlw7ZvuY%2BXeEuDlqP2eiNCmviBMBJBhrFDIdJEfoU66TLQzkPE04yFFjO8tREnAaHS0kWPBXQN0hP6UD6e7WPvHwCeGIlDwAI3fAy%2BXqvXw0YmuJlT2TvNKBddjwLy1yb8szPKgvPmXCGF87Lip0rCSV%2BRRxu70AQ0DAr3osOxNbuAwUV42va%2F9oRami450WBoS8njrYq6YjKeTMjG8jOCIQbMuebVtrGOMLS6jr0GOqUBwyTknFaJclcXhg8C29p%2B%2F8fIMI7Am8XIQ8Vr2Sk%2Bj%2BTVaejISsD5G5j8fM2CFOPtuhxMsvfHu9xl9%2B%2BkUYIrw0GBSpjTrnGZdPzVVE6nNMm4cHlqa6R4SPP1iB7%2BB9O6BjGOPJ1Rcna2iQjE1JJ6g%2BhQIeBVIJVRDtO%2BSs2D%2FeJRdKSloO7cT5NTVUlACbyb8FGzFx822Rc0o26J0LwgjeAUPQ%2FH&X-Amz-Signature=2483586b442fbf0041a835aa31ea109360f7300503fc8083749b61dbe88f7487&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FRGKNOF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDT23vturOOpMnPPo6dhRdBG2EeXi%2BrzNVocfgNfSaQ%2FgIgLdU%2FLksE6GQX22tj6rUiJKK6R6sa7F1fM7Hx27wKIDwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAGX4JNd3WDpsJFmTSrcA8hcdjmhJZ%2BCh6oUY9UrbxJKUPVfZyEQ3GnLySXpS71zMW2knVeIxc%2BtCQlNFjaYRFDhxIX0ojiRdtMKiaamXDza6M3rns5PKhIjN4BBwSUwKRC3yBT4Hp6vHnNSVOkE487%2Bdp0%2BR6QviHYNHouy808cWWplvrlgE3hD8c%2BG0w2fN4nDOTnDGw3AHJ7e%2F9OGIjCQV7UkUPQ9839DFZu%2FiHbNbW5d%2BbB2Ju%2BeYuTz4tihCXyfqlFSqmQgQNsxRnirTHg9qk%2FWakdnXN%2FWjECKSQs%2F8FwXvYQfmnTjraCO3DYaRJP6UP8Rly4ThhGmWubhgl3Jt4OOmyokc5UHDLX0OrGOqvqdCHK%2BtYTjcYercJAqJY%2Bc8ZVX4SE0NVI8zz23iM0Q94LLoXxabXWE5qsOO4Jh8%2Frlw7ZvuY%2BXeEuDlqP2eiNCmviBMBJBhrFDIdJEfoU66TLQzkPE04yFFjO8tREnAaHS0kWPBXQN0hP6UD6e7WPvHwCeGIlDwAI3fAy%2BXqvXw0YmuJlT2TvNKBddjwLy1yb8szPKgvPmXCGF87Lip0rCSV%2BRRxu70AQ0DAr3osOxNbuAwUV42va%2F9oRami450WBoS8njrYq6YjKeTMjG8jOCIQbMuebVtrGOMLS6jr0GOqUBwyTknFaJclcXhg8C29p%2B%2F8fIMI7Am8XIQ8Vr2Sk%2Bj%2BTVaejISsD5G5j8fM2CFOPtuhxMsvfHu9xl9%2B%2BkUYIrw0GBSpjTrnGZdPzVVE6nNMm4cHlqa6R4SPP1iB7%2BB9O6BjGOPJ1Rcna2iQjE1JJ6g%2BhQIeBVIJVRDtO%2BSs2D%2FeJRdKSloO7cT5NTVUlACbyb8FGzFx822Rc0o26J0LwgjeAUPQ%2FH&X-Amz-Signature=0933172bed5e97747e5ec8dce2d405a8de92a50cbfbd90573db21034e89ad7e7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FRGKNOF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDT23vturOOpMnPPo6dhRdBG2EeXi%2BrzNVocfgNfSaQ%2FgIgLdU%2FLksE6GQX22tj6rUiJKK6R6sa7F1fM7Hx27wKIDwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAGX4JNd3WDpsJFmTSrcA8hcdjmhJZ%2BCh6oUY9UrbxJKUPVfZyEQ3GnLySXpS71zMW2knVeIxc%2BtCQlNFjaYRFDhxIX0ojiRdtMKiaamXDza6M3rns5PKhIjN4BBwSUwKRC3yBT4Hp6vHnNSVOkE487%2Bdp0%2BR6QviHYNHouy808cWWplvrlgE3hD8c%2BG0w2fN4nDOTnDGw3AHJ7e%2F9OGIjCQV7UkUPQ9839DFZu%2FiHbNbW5d%2BbB2Ju%2BeYuTz4tihCXyfqlFSqmQgQNsxRnirTHg9qk%2FWakdnXN%2FWjECKSQs%2F8FwXvYQfmnTjraCO3DYaRJP6UP8Rly4ThhGmWubhgl3Jt4OOmyokc5UHDLX0OrGOqvqdCHK%2BtYTjcYercJAqJY%2Bc8ZVX4SE0NVI8zz23iM0Q94LLoXxabXWE5qsOO4Jh8%2Frlw7ZvuY%2BXeEuDlqP2eiNCmviBMBJBhrFDIdJEfoU66TLQzkPE04yFFjO8tREnAaHS0kWPBXQN0hP6UD6e7WPvHwCeGIlDwAI3fAy%2BXqvXw0YmuJlT2TvNKBddjwLy1yb8szPKgvPmXCGF87Lip0rCSV%2BRRxu70AQ0DAr3osOxNbuAwUV42va%2F9oRami450WBoS8njrYq6YjKeTMjG8jOCIQbMuebVtrGOMLS6jr0GOqUBwyTknFaJclcXhg8C29p%2B%2F8fIMI7Am8XIQ8Vr2Sk%2Bj%2BTVaejISsD5G5j8fM2CFOPtuhxMsvfHu9xl9%2B%2BkUYIrw0GBSpjTrnGZdPzVVE6nNMm4cHlqa6R4SPP1iB7%2BB9O6BjGOPJ1Rcna2iQjE1JJ6g%2BhQIeBVIJVRDtO%2BSs2D%2FeJRdKSloO7cT5NTVUlACbyb8FGzFx822Rc0o26J0LwgjeAUPQ%2FH&X-Amz-Signature=a278c598591840beb9bc3ce960733ce8aa21f16dc825d11e935f1ebe8a9fc820&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FRGKNOF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDT23vturOOpMnPPo6dhRdBG2EeXi%2BrzNVocfgNfSaQ%2FgIgLdU%2FLksE6GQX22tj6rUiJKK6R6sa7F1fM7Hx27wKIDwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAGX4JNd3WDpsJFmTSrcA8hcdjmhJZ%2BCh6oUY9UrbxJKUPVfZyEQ3GnLySXpS71zMW2knVeIxc%2BtCQlNFjaYRFDhxIX0ojiRdtMKiaamXDza6M3rns5PKhIjN4BBwSUwKRC3yBT4Hp6vHnNSVOkE487%2Bdp0%2BR6QviHYNHouy808cWWplvrlgE3hD8c%2BG0w2fN4nDOTnDGw3AHJ7e%2F9OGIjCQV7UkUPQ9839DFZu%2FiHbNbW5d%2BbB2Ju%2BeYuTz4tihCXyfqlFSqmQgQNsxRnirTHg9qk%2FWakdnXN%2FWjECKSQs%2F8FwXvYQfmnTjraCO3DYaRJP6UP8Rly4ThhGmWubhgl3Jt4OOmyokc5UHDLX0OrGOqvqdCHK%2BtYTjcYercJAqJY%2Bc8ZVX4SE0NVI8zz23iM0Q94LLoXxabXWE5qsOO4Jh8%2Frlw7ZvuY%2BXeEuDlqP2eiNCmviBMBJBhrFDIdJEfoU66TLQzkPE04yFFjO8tREnAaHS0kWPBXQN0hP6UD6e7WPvHwCeGIlDwAI3fAy%2BXqvXw0YmuJlT2TvNKBddjwLy1yb8szPKgvPmXCGF87Lip0rCSV%2BRRxu70AQ0DAr3osOxNbuAwUV42va%2F9oRami450WBoS8njrYq6YjKeTMjG8jOCIQbMuebVtrGOMLS6jr0GOqUBwyTknFaJclcXhg8C29p%2B%2F8fIMI7Am8XIQ8Vr2Sk%2Bj%2BTVaejISsD5G5j8fM2CFOPtuhxMsvfHu9xl9%2B%2BkUYIrw0GBSpjTrnGZdPzVVE6nNMm4cHlqa6R4SPP1iB7%2BB9O6BjGOPJ1Rcna2iQjE1JJ6g%2BhQIeBVIJVRDtO%2BSs2D%2FeJRdKSloO7cT5NTVUlACbyb8FGzFx822Rc0o26J0LwgjeAUPQ%2FH&X-Amz-Signature=34a16520d5d6c61c3af7f943c5011bbb7e57ebeb8fe839a1fb6b461665318458&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FRGKNOF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDT23vturOOpMnPPo6dhRdBG2EeXi%2BrzNVocfgNfSaQ%2FgIgLdU%2FLksE6GQX22tj6rUiJKK6R6sa7F1fM7Hx27wKIDwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAGX4JNd3WDpsJFmTSrcA8hcdjmhJZ%2BCh6oUY9UrbxJKUPVfZyEQ3GnLySXpS71zMW2knVeIxc%2BtCQlNFjaYRFDhxIX0ojiRdtMKiaamXDza6M3rns5PKhIjN4BBwSUwKRC3yBT4Hp6vHnNSVOkE487%2Bdp0%2BR6QviHYNHouy808cWWplvrlgE3hD8c%2BG0w2fN4nDOTnDGw3AHJ7e%2F9OGIjCQV7UkUPQ9839DFZu%2FiHbNbW5d%2BbB2Ju%2BeYuTz4tihCXyfqlFSqmQgQNsxRnirTHg9qk%2FWakdnXN%2FWjECKSQs%2F8FwXvYQfmnTjraCO3DYaRJP6UP8Rly4ThhGmWubhgl3Jt4OOmyokc5UHDLX0OrGOqvqdCHK%2BtYTjcYercJAqJY%2Bc8ZVX4SE0NVI8zz23iM0Q94LLoXxabXWE5qsOO4Jh8%2Frlw7ZvuY%2BXeEuDlqP2eiNCmviBMBJBhrFDIdJEfoU66TLQzkPE04yFFjO8tREnAaHS0kWPBXQN0hP6UD6e7WPvHwCeGIlDwAI3fAy%2BXqvXw0YmuJlT2TvNKBddjwLy1yb8szPKgvPmXCGF87Lip0rCSV%2BRRxu70AQ0DAr3osOxNbuAwUV42va%2F9oRami450WBoS8njrYq6YjKeTMjG8jOCIQbMuebVtrGOMLS6jr0GOqUBwyTknFaJclcXhg8C29p%2B%2F8fIMI7Am8XIQ8Vr2Sk%2Bj%2BTVaejISsD5G5j8fM2CFOPtuhxMsvfHu9xl9%2B%2BkUYIrw0GBSpjTrnGZdPzVVE6nNMm4cHlqa6R4SPP1iB7%2BB9O6BjGOPJ1Rcna2iQjE1JJ6g%2BhQIeBVIJVRDtO%2BSs2D%2FeJRdKSloO7cT5NTVUlACbyb8FGzFx822Rc0o26J0LwgjeAUPQ%2FH&X-Amz-Signature=caae7f47184bed4bd72e019349db62b141aff505d2f361c6de3575ec2196ce6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


