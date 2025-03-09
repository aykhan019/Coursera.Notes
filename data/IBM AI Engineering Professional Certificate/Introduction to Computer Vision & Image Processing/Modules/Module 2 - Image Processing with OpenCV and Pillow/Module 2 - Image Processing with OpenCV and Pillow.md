

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3KN4HLS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAv731Gv7EDm7%2F%2Fgvw38%2B21lVnD6yhHbTttbDg1E%2FdJ5AiEApQnJrJHgw5dK10%2B6VGJ5%2FGgYDVmHA%2FWPJu0gPv6z8dAq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDSAf%2FSuxJXJcIRYfyrcA7KJ8CljJ55GC81oMohm%2FiHcCb9oJLWEKNcY0LQ1xfue0txh8CCKccCX%2F%2FVYnWY9Mh5wVdWyIKPxM9TCP6cq8Pei%2FCW2EkNo3cicz6Hn6WuKhDRTKghBVl9fsBRjDMFJwDwVv3wmyQ55efIVT%2FSmOtSsonU%2Flko7bEgIhYWHoeq58zsRJDqBiwzmqhTiTYgeRKfKHh%2B6KWg1ZtQYSUfi2Us%2BFijdgtuIAHb%2F0YxeSn2uI3oZsTJitolSD6PpeC0N%2BEE%2F4eaycFlH63B8CKjsGMnepSi6CSuy3xM1HSXeTniqnWVUYC8swOq6PQaPVPokayB87QM7kWdBwwO6wfR5XdJzdq9KSZeI%2BfIATP8tr6W3OxgZkAObRKMQlT%2BatVLHA7KKNHpdCOzVoONTPo4Kg11q2%2FhKbF9MWKE4u8Vj%2Bzfm0wyLscg0Bxu2l0nXKfpO5otcquPs4Z6%2FEMS1nCWnEls4giRxRhblhqTx5BLI6gozO3EikzX%2BUBwm0WYP3g1YEE9aXgh3uQsn%2Buy1ouhlxXRNpwjEqT82S4e41bg%2F0cxmMMvMmzDl4WRsWldVjG65xOGar98SOfab6l5Zr458%2FVc8tSQGkRSVpBKBEeJXy6ZiAZbxriRjTeAQPmuuMLKps74GOqUBtOXVgwQ9r4lHLU4T7v7wRAU5B%2B3LMoSEJnG%2BD7WdSBS9xnVg%2BjdAsLqJUTSRjpYxs1yEfbT4HgJX2YYr99lO7b%2FC%2BQ7R59fOszGh02u55NHycSk24mm6AYynOi4B7BzLr0IKoFMyJR%2BUxwuOBizO65SXkb7sNEYm1r9vHj78t4P7SzzcqWap5HfiBcvAg1b96uGvwGNLcsdlqnktJzyfAwYLVYpQ&X-Amz-Signature=573eea6943d867b64e76eafd9e1179681d57a5842256bad0995626b850c4890e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPQ5ST6S%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsFDxWQVLbJdl%2BlxRb9P%2B4TPWPFou3aHFlEcIhynPjRgIhALusLRAbmB83QUD8mJMnQUDW4b6bEQdC0vnO41%2BkGvltKv8DCGkQABoMNjM3NDIzMTgzODA1IgxDVkD43wtyurN6Eeoq3AORRa5Toynzmy8LVkZgWucXMLQDSoWKvB1FCWdEhO%2BhM3TCAuRYDRWbeZPW1pdHQHvHkgMcKRvv5a2gSkD%2BvOF6F21rLI2ZNTZ%2BK9wTUzw2V8j6dhexnd%2F6xiRMxMJLkDGQyp%2FkFmhNuogf1WL%2FiYfGSDMr0a0FM7InrGjmegXJQKvrNA7Se2k3ip1SQG%2FiMuYmI7BgQ%2FuuALwL678HRGD4QjmdhQglopGPyvrsNdmey8Zb82KgNpKJezDlK8JftC7Y3JNxy3BaOHJZza3leBW2v2wG%2Fwbxa66M25iuthbcvITbXqJfnzo0n5JgfW43R8Z%2BOcHPqWqAzn0MnO8nC%2FnLub%2BFhynIRjK60H4n1yhzWpOpWig29ZouXQt4TyrU5%2FXJR4mxxeq7bGlL0Sj2Fv5084b%2B8%2BRyF604EKjaWcKTJ7UuNW2Ff2WBubq2NNMmwKlCVplsOkHKUgEc9bD7I%2FVYBypZA82tlo%2Fun9pnu5ORLNoZiMh0z6DH%2B%2FVdpIJztpawXaOEkmpnQlbANyeBccgXccGlUMi473fyZTVb0AW3qqFJjLiyBrJko5nPsmWo%2Fjyw4iOoA9N%2BMZFLcUlJGtv%2BNe83KyJZRew8zJgp%2FSfgtZ%2F%2FGKGIYSs2j09VTDDQqbO%2BBjqkAReswQtIH9vO33ethHPFYtqlJd0CrNsdS2KrepNbTmb9ioTdOtd8FhggNBnbwO0mmG5mCr%2FlQ5QqOVIrefqsasBsVdVieiM46y50pmUXCnsJELBQyY0v9dRLyknJP%2BVr0IpuwWaoITU5n%2F7LQs2hw6YsTd2RY5aiE3dLY4HJooR%2F%2ByJ%2BFnMQmy3%2F5EZjw58IupHg3n9bLLNcRJEBqd%2F5vEk%2FPcC5&X-Amz-Signature=3beb3dcfa4821307aa3f61dd6c1c81f15297fda3f7835913498414bc05431853&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPQ5ST6S%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsFDxWQVLbJdl%2BlxRb9P%2B4TPWPFou3aHFlEcIhynPjRgIhALusLRAbmB83QUD8mJMnQUDW4b6bEQdC0vnO41%2BkGvltKv8DCGkQABoMNjM3NDIzMTgzODA1IgxDVkD43wtyurN6Eeoq3AORRa5Toynzmy8LVkZgWucXMLQDSoWKvB1FCWdEhO%2BhM3TCAuRYDRWbeZPW1pdHQHvHkgMcKRvv5a2gSkD%2BvOF6F21rLI2ZNTZ%2BK9wTUzw2V8j6dhexnd%2F6xiRMxMJLkDGQyp%2FkFmhNuogf1WL%2FiYfGSDMr0a0FM7InrGjmegXJQKvrNA7Se2k3ip1SQG%2FiMuYmI7BgQ%2FuuALwL678HRGD4QjmdhQglopGPyvrsNdmey8Zb82KgNpKJezDlK8JftC7Y3JNxy3BaOHJZza3leBW2v2wG%2Fwbxa66M25iuthbcvITbXqJfnzo0n5JgfW43R8Z%2BOcHPqWqAzn0MnO8nC%2FnLub%2BFhynIRjK60H4n1yhzWpOpWig29ZouXQt4TyrU5%2FXJR4mxxeq7bGlL0Sj2Fv5084b%2B8%2BRyF604EKjaWcKTJ7UuNW2Ff2WBubq2NNMmwKlCVplsOkHKUgEc9bD7I%2FVYBypZA82tlo%2Fun9pnu5ORLNoZiMh0z6DH%2B%2FVdpIJztpawXaOEkmpnQlbANyeBccgXccGlUMi473fyZTVb0AW3qqFJjLiyBrJko5nPsmWo%2Fjyw4iOoA9N%2BMZFLcUlJGtv%2BNe83KyJZRew8zJgp%2FSfgtZ%2F%2FGKGIYSs2j09VTDDQqbO%2BBjqkAReswQtIH9vO33ethHPFYtqlJd0CrNsdS2KrepNbTmb9ioTdOtd8FhggNBnbwO0mmG5mCr%2FlQ5QqOVIrefqsasBsVdVieiM46y50pmUXCnsJELBQyY0v9dRLyknJP%2BVr0IpuwWaoITU5n%2F7LQs2hw6YsTd2RY5aiE3dLY4HJooR%2F%2ByJ%2BFnMQmy3%2F5EZjw58IupHg3n9bLLNcRJEBqd%2F5vEk%2FPcC5&X-Amz-Signature=b1f736c4d7100e32dc5c92e4bbbb9a1f3e84e0b7f42b67969fa2a86f1dea6114&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPQ5ST6S%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsFDxWQVLbJdl%2BlxRb9P%2B4TPWPFou3aHFlEcIhynPjRgIhALusLRAbmB83QUD8mJMnQUDW4b6bEQdC0vnO41%2BkGvltKv8DCGkQABoMNjM3NDIzMTgzODA1IgxDVkD43wtyurN6Eeoq3AORRa5Toynzmy8LVkZgWucXMLQDSoWKvB1FCWdEhO%2BhM3TCAuRYDRWbeZPW1pdHQHvHkgMcKRvv5a2gSkD%2BvOF6F21rLI2ZNTZ%2BK9wTUzw2V8j6dhexnd%2F6xiRMxMJLkDGQyp%2FkFmhNuogf1WL%2FiYfGSDMr0a0FM7InrGjmegXJQKvrNA7Se2k3ip1SQG%2FiMuYmI7BgQ%2FuuALwL678HRGD4QjmdhQglopGPyvrsNdmey8Zb82KgNpKJezDlK8JftC7Y3JNxy3BaOHJZza3leBW2v2wG%2Fwbxa66M25iuthbcvITbXqJfnzo0n5JgfW43R8Z%2BOcHPqWqAzn0MnO8nC%2FnLub%2BFhynIRjK60H4n1yhzWpOpWig29ZouXQt4TyrU5%2FXJR4mxxeq7bGlL0Sj2Fv5084b%2B8%2BRyF604EKjaWcKTJ7UuNW2Ff2WBubq2NNMmwKlCVplsOkHKUgEc9bD7I%2FVYBypZA82tlo%2Fun9pnu5ORLNoZiMh0z6DH%2B%2FVdpIJztpawXaOEkmpnQlbANyeBccgXccGlUMi473fyZTVb0AW3qqFJjLiyBrJko5nPsmWo%2Fjyw4iOoA9N%2BMZFLcUlJGtv%2BNe83KyJZRew8zJgp%2FSfgtZ%2F%2FGKGIYSs2j09VTDDQqbO%2BBjqkAReswQtIH9vO33ethHPFYtqlJd0CrNsdS2KrepNbTmb9ioTdOtd8FhggNBnbwO0mmG5mCr%2FlQ5QqOVIrefqsasBsVdVieiM46y50pmUXCnsJELBQyY0v9dRLyknJP%2BVr0IpuwWaoITU5n%2F7LQs2hw6YsTd2RY5aiE3dLY4HJooR%2F%2ByJ%2BFnMQmy3%2F5EZjw58IupHg3n9bLLNcRJEBqd%2F5vEk%2FPcC5&X-Amz-Signature=e13cb905c7621b2d5bf8bac7ec6fb0fcd6afe9259906b2cd1e22d79d92ca53b6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPQ5ST6S%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsFDxWQVLbJdl%2BlxRb9P%2B4TPWPFou3aHFlEcIhynPjRgIhALusLRAbmB83QUD8mJMnQUDW4b6bEQdC0vnO41%2BkGvltKv8DCGkQABoMNjM3NDIzMTgzODA1IgxDVkD43wtyurN6Eeoq3AORRa5Toynzmy8LVkZgWucXMLQDSoWKvB1FCWdEhO%2BhM3TCAuRYDRWbeZPW1pdHQHvHkgMcKRvv5a2gSkD%2BvOF6F21rLI2ZNTZ%2BK9wTUzw2V8j6dhexnd%2F6xiRMxMJLkDGQyp%2FkFmhNuogf1WL%2FiYfGSDMr0a0FM7InrGjmegXJQKvrNA7Se2k3ip1SQG%2FiMuYmI7BgQ%2FuuALwL678HRGD4QjmdhQglopGPyvrsNdmey8Zb82KgNpKJezDlK8JftC7Y3JNxy3BaOHJZza3leBW2v2wG%2Fwbxa66M25iuthbcvITbXqJfnzo0n5JgfW43R8Z%2BOcHPqWqAzn0MnO8nC%2FnLub%2BFhynIRjK60H4n1yhzWpOpWig29ZouXQt4TyrU5%2FXJR4mxxeq7bGlL0Sj2Fv5084b%2B8%2BRyF604EKjaWcKTJ7UuNW2Ff2WBubq2NNMmwKlCVplsOkHKUgEc9bD7I%2FVYBypZA82tlo%2Fun9pnu5ORLNoZiMh0z6DH%2B%2FVdpIJztpawXaOEkmpnQlbANyeBccgXccGlUMi473fyZTVb0AW3qqFJjLiyBrJko5nPsmWo%2Fjyw4iOoA9N%2BMZFLcUlJGtv%2BNe83KyJZRew8zJgp%2FSfgtZ%2F%2FGKGIYSs2j09VTDDQqbO%2BBjqkAReswQtIH9vO33ethHPFYtqlJd0CrNsdS2KrepNbTmb9ioTdOtd8FhggNBnbwO0mmG5mCr%2FlQ5QqOVIrefqsasBsVdVieiM46y50pmUXCnsJELBQyY0v9dRLyknJP%2BVr0IpuwWaoITU5n%2F7LQs2hw6YsTd2RY5aiE3dLY4HJooR%2F%2ByJ%2BFnMQmy3%2F5EZjw58IupHg3n9bLLNcRJEBqd%2F5vEk%2FPcC5&X-Amz-Signature=52080d53faa19dd20e0c0f0cbfa25ac68940c91dfffec012106f57304f4c5ea6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPQ5ST6S%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsFDxWQVLbJdl%2BlxRb9P%2B4TPWPFou3aHFlEcIhynPjRgIhALusLRAbmB83QUD8mJMnQUDW4b6bEQdC0vnO41%2BkGvltKv8DCGkQABoMNjM3NDIzMTgzODA1IgxDVkD43wtyurN6Eeoq3AORRa5Toynzmy8LVkZgWucXMLQDSoWKvB1FCWdEhO%2BhM3TCAuRYDRWbeZPW1pdHQHvHkgMcKRvv5a2gSkD%2BvOF6F21rLI2ZNTZ%2BK9wTUzw2V8j6dhexnd%2F6xiRMxMJLkDGQyp%2FkFmhNuogf1WL%2FiYfGSDMr0a0FM7InrGjmegXJQKvrNA7Se2k3ip1SQG%2FiMuYmI7BgQ%2FuuALwL678HRGD4QjmdhQglopGPyvrsNdmey8Zb82KgNpKJezDlK8JftC7Y3JNxy3BaOHJZza3leBW2v2wG%2Fwbxa66M25iuthbcvITbXqJfnzo0n5JgfW43R8Z%2BOcHPqWqAzn0MnO8nC%2FnLub%2BFhynIRjK60H4n1yhzWpOpWig29ZouXQt4TyrU5%2FXJR4mxxeq7bGlL0Sj2Fv5084b%2B8%2BRyF604EKjaWcKTJ7UuNW2Ff2WBubq2NNMmwKlCVplsOkHKUgEc9bD7I%2FVYBypZA82tlo%2Fun9pnu5ORLNoZiMh0z6DH%2B%2FVdpIJztpawXaOEkmpnQlbANyeBccgXccGlUMi473fyZTVb0AW3qqFJjLiyBrJko5nPsmWo%2Fjyw4iOoA9N%2BMZFLcUlJGtv%2BNe83KyJZRew8zJgp%2FSfgtZ%2F%2FGKGIYSs2j09VTDDQqbO%2BBjqkAReswQtIH9vO33ethHPFYtqlJd0CrNsdS2KrepNbTmb9ioTdOtd8FhggNBnbwO0mmG5mCr%2FlQ5QqOVIrefqsasBsVdVieiM46y50pmUXCnsJELBQyY0v9dRLyknJP%2BVr0IpuwWaoITU5n%2F7LQs2hw6YsTd2RY5aiE3dLY4HJooR%2F%2ByJ%2BFnMQmy3%2F5EZjw58IupHg3n9bLLNcRJEBqd%2F5vEk%2FPcC5&X-Amz-Signature=408deffc1670525c74c9b9b9f717d196386f9772c217ec6ccf6e7c9c4db15a55&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3KN4HLS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAv731Gv7EDm7%2F%2Fgvw38%2B21lVnD6yhHbTttbDg1E%2FdJ5AiEApQnJrJHgw5dK10%2B6VGJ5%2FGgYDVmHA%2FWPJu0gPv6z8dAq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDSAf%2FSuxJXJcIRYfyrcA7KJ8CljJ55GC81oMohm%2FiHcCb9oJLWEKNcY0LQ1xfue0txh8CCKccCX%2F%2FVYnWY9Mh5wVdWyIKPxM9TCP6cq8Pei%2FCW2EkNo3cicz6Hn6WuKhDRTKghBVl9fsBRjDMFJwDwVv3wmyQ55efIVT%2FSmOtSsonU%2Flko7bEgIhYWHoeq58zsRJDqBiwzmqhTiTYgeRKfKHh%2B6KWg1ZtQYSUfi2Us%2BFijdgtuIAHb%2F0YxeSn2uI3oZsTJitolSD6PpeC0N%2BEE%2F4eaycFlH63B8CKjsGMnepSi6CSuy3xM1HSXeTniqnWVUYC8swOq6PQaPVPokayB87QM7kWdBwwO6wfR5XdJzdq9KSZeI%2BfIATP8tr6W3OxgZkAObRKMQlT%2BatVLHA7KKNHpdCOzVoONTPo4Kg11q2%2FhKbF9MWKE4u8Vj%2Bzfm0wyLscg0Bxu2l0nXKfpO5otcquPs4Z6%2FEMS1nCWnEls4giRxRhblhqTx5BLI6gozO3EikzX%2BUBwm0WYP3g1YEE9aXgh3uQsn%2Buy1ouhlxXRNpwjEqT82S4e41bg%2F0cxmMMvMmzDl4WRsWldVjG65xOGar98SOfab6l5Zr458%2FVc8tSQGkRSVpBKBEeJXy6ZiAZbxriRjTeAQPmuuMLKps74GOqUBtOXVgwQ9r4lHLU4T7v7wRAU5B%2B3LMoSEJnG%2BD7WdSBS9xnVg%2BjdAsLqJUTSRjpYxs1yEfbT4HgJX2YYr99lO7b%2FC%2BQ7R59fOszGh02u55NHycSk24mm6AYynOi4B7BzLr0IKoFMyJR%2BUxwuOBizO65SXkb7sNEYm1r9vHj78t4P7SzzcqWap5HfiBcvAg1b96uGvwGNLcsdlqnktJzyfAwYLVYpQ&X-Amz-Signature=b143c8cfc2d1f8c1db93bb27ef76a31175c1dfae26e8ff935810f9ba3e716aae&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3KN4HLS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAv731Gv7EDm7%2F%2Fgvw38%2B21lVnD6yhHbTttbDg1E%2FdJ5AiEApQnJrJHgw5dK10%2B6VGJ5%2FGgYDVmHA%2FWPJu0gPv6z8dAq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDSAf%2FSuxJXJcIRYfyrcA7KJ8CljJ55GC81oMohm%2FiHcCb9oJLWEKNcY0LQ1xfue0txh8CCKccCX%2F%2FVYnWY9Mh5wVdWyIKPxM9TCP6cq8Pei%2FCW2EkNo3cicz6Hn6WuKhDRTKghBVl9fsBRjDMFJwDwVv3wmyQ55efIVT%2FSmOtSsonU%2Flko7bEgIhYWHoeq58zsRJDqBiwzmqhTiTYgeRKfKHh%2B6KWg1ZtQYSUfi2Us%2BFijdgtuIAHb%2F0YxeSn2uI3oZsTJitolSD6PpeC0N%2BEE%2F4eaycFlH63B8CKjsGMnepSi6CSuy3xM1HSXeTniqnWVUYC8swOq6PQaPVPokayB87QM7kWdBwwO6wfR5XdJzdq9KSZeI%2BfIATP8tr6W3OxgZkAObRKMQlT%2BatVLHA7KKNHpdCOzVoONTPo4Kg11q2%2FhKbF9MWKE4u8Vj%2Bzfm0wyLscg0Bxu2l0nXKfpO5otcquPs4Z6%2FEMS1nCWnEls4giRxRhblhqTx5BLI6gozO3EikzX%2BUBwm0WYP3g1YEE9aXgh3uQsn%2Buy1ouhlxXRNpwjEqT82S4e41bg%2F0cxmMMvMmzDl4WRsWldVjG65xOGar98SOfab6l5Zr458%2FVc8tSQGkRSVpBKBEeJXy6ZiAZbxriRjTeAQPmuuMLKps74GOqUBtOXVgwQ9r4lHLU4T7v7wRAU5B%2B3LMoSEJnG%2BD7WdSBS9xnVg%2BjdAsLqJUTSRjpYxs1yEfbT4HgJX2YYr99lO7b%2FC%2BQ7R59fOszGh02u55NHycSk24mm6AYynOi4B7BzLr0IKoFMyJR%2BUxwuOBizO65SXkb7sNEYm1r9vHj78t4P7SzzcqWap5HfiBcvAg1b96uGvwGNLcsdlqnktJzyfAwYLVYpQ&X-Amz-Signature=ba71cacbd71a347422f0860175a05c2c72856387420f02b3649012f6c0a2f93c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3KN4HLS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAv731Gv7EDm7%2F%2Fgvw38%2B21lVnD6yhHbTttbDg1E%2FdJ5AiEApQnJrJHgw5dK10%2B6VGJ5%2FGgYDVmHA%2FWPJu0gPv6z8dAq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDSAf%2FSuxJXJcIRYfyrcA7KJ8CljJ55GC81oMohm%2FiHcCb9oJLWEKNcY0LQ1xfue0txh8CCKccCX%2F%2FVYnWY9Mh5wVdWyIKPxM9TCP6cq8Pei%2FCW2EkNo3cicz6Hn6WuKhDRTKghBVl9fsBRjDMFJwDwVv3wmyQ55efIVT%2FSmOtSsonU%2Flko7bEgIhYWHoeq58zsRJDqBiwzmqhTiTYgeRKfKHh%2B6KWg1ZtQYSUfi2Us%2BFijdgtuIAHb%2F0YxeSn2uI3oZsTJitolSD6PpeC0N%2BEE%2F4eaycFlH63B8CKjsGMnepSi6CSuy3xM1HSXeTniqnWVUYC8swOq6PQaPVPokayB87QM7kWdBwwO6wfR5XdJzdq9KSZeI%2BfIATP8tr6W3OxgZkAObRKMQlT%2BatVLHA7KKNHpdCOzVoONTPo4Kg11q2%2FhKbF9MWKE4u8Vj%2Bzfm0wyLscg0Bxu2l0nXKfpO5otcquPs4Z6%2FEMS1nCWnEls4giRxRhblhqTx5BLI6gozO3EikzX%2BUBwm0WYP3g1YEE9aXgh3uQsn%2Buy1ouhlxXRNpwjEqT82S4e41bg%2F0cxmMMvMmzDl4WRsWldVjG65xOGar98SOfab6l5Zr458%2FVc8tSQGkRSVpBKBEeJXy6ZiAZbxriRjTeAQPmuuMLKps74GOqUBtOXVgwQ9r4lHLU4T7v7wRAU5B%2B3LMoSEJnG%2BD7WdSBS9xnVg%2BjdAsLqJUTSRjpYxs1yEfbT4HgJX2YYr99lO7b%2FC%2BQ7R59fOszGh02u55NHycSk24mm6AYynOi4B7BzLr0IKoFMyJR%2BUxwuOBizO65SXkb7sNEYm1r9vHj78t4P7SzzcqWap5HfiBcvAg1b96uGvwGNLcsdlqnktJzyfAwYLVYpQ&X-Amz-Signature=ee841387910dd87b5e05afe6d4f92efa3e191523250661b917f8e6275f916399&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3KN4HLS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAv731Gv7EDm7%2F%2Fgvw38%2B21lVnD6yhHbTttbDg1E%2FdJ5AiEApQnJrJHgw5dK10%2B6VGJ5%2FGgYDVmHA%2FWPJu0gPv6z8dAq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDSAf%2FSuxJXJcIRYfyrcA7KJ8CljJ55GC81oMohm%2FiHcCb9oJLWEKNcY0LQ1xfue0txh8CCKccCX%2F%2FVYnWY9Mh5wVdWyIKPxM9TCP6cq8Pei%2FCW2EkNo3cicz6Hn6WuKhDRTKghBVl9fsBRjDMFJwDwVv3wmyQ55efIVT%2FSmOtSsonU%2Flko7bEgIhYWHoeq58zsRJDqBiwzmqhTiTYgeRKfKHh%2B6KWg1ZtQYSUfi2Us%2BFijdgtuIAHb%2F0YxeSn2uI3oZsTJitolSD6PpeC0N%2BEE%2F4eaycFlH63B8CKjsGMnepSi6CSuy3xM1HSXeTniqnWVUYC8swOq6PQaPVPokayB87QM7kWdBwwO6wfR5XdJzdq9KSZeI%2BfIATP8tr6W3OxgZkAObRKMQlT%2BatVLHA7KKNHpdCOzVoONTPo4Kg11q2%2FhKbF9MWKE4u8Vj%2Bzfm0wyLscg0Bxu2l0nXKfpO5otcquPs4Z6%2FEMS1nCWnEls4giRxRhblhqTx5BLI6gozO3EikzX%2BUBwm0WYP3g1YEE9aXgh3uQsn%2Buy1ouhlxXRNpwjEqT82S4e41bg%2F0cxmMMvMmzDl4WRsWldVjG65xOGar98SOfab6l5Zr458%2FVc8tSQGkRSVpBKBEeJXy6ZiAZbxriRjTeAQPmuuMLKps74GOqUBtOXVgwQ9r4lHLU4T7v7wRAU5B%2B3LMoSEJnG%2BD7WdSBS9xnVg%2BjdAsLqJUTSRjpYxs1yEfbT4HgJX2YYr99lO7b%2FC%2BQ7R59fOszGh02u55NHycSk24mm6AYynOi4B7BzLr0IKoFMyJR%2BUxwuOBizO65SXkb7sNEYm1r9vHj78t4P7SzzcqWap5HfiBcvAg1b96uGvwGNLcsdlqnktJzyfAwYLVYpQ&X-Amz-Signature=d8d92338d85d3879f83f2345935e04293d682119300b0037882a5c276811b1ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3KN4HLS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAv731Gv7EDm7%2F%2Fgvw38%2B21lVnD6yhHbTttbDg1E%2FdJ5AiEApQnJrJHgw5dK10%2B6VGJ5%2FGgYDVmHA%2FWPJu0gPv6z8dAq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDSAf%2FSuxJXJcIRYfyrcA7KJ8CljJ55GC81oMohm%2FiHcCb9oJLWEKNcY0LQ1xfue0txh8CCKccCX%2F%2FVYnWY9Mh5wVdWyIKPxM9TCP6cq8Pei%2FCW2EkNo3cicz6Hn6WuKhDRTKghBVl9fsBRjDMFJwDwVv3wmyQ55efIVT%2FSmOtSsonU%2Flko7bEgIhYWHoeq58zsRJDqBiwzmqhTiTYgeRKfKHh%2B6KWg1ZtQYSUfi2Us%2BFijdgtuIAHb%2F0YxeSn2uI3oZsTJitolSD6PpeC0N%2BEE%2F4eaycFlH63B8CKjsGMnepSi6CSuy3xM1HSXeTniqnWVUYC8swOq6PQaPVPokayB87QM7kWdBwwO6wfR5XdJzdq9KSZeI%2BfIATP8tr6W3OxgZkAObRKMQlT%2BatVLHA7KKNHpdCOzVoONTPo4Kg11q2%2FhKbF9MWKE4u8Vj%2Bzfm0wyLscg0Bxu2l0nXKfpO5otcquPs4Z6%2FEMS1nCWnEls4giRxRhblhqTx5BLI6gozO3EikzX%2BUBwm0WYP3g1YEE9aXgh3uQsn%2Buy1ouhlxXRNpwjEqT82S4e41bg%2F0cxmMMvMmzDl4WRsWldVjG65xOGar98SOfab6l5Zr458%2FVc8tSQGkRSVpBKBEeJXy6ZiAZbxriRjTeAQPmuuMLKps74GOqUBtOXVgwQ9r4lHLU4T7v7wRAU5B%2B3LMoSEJnG%2BD7WdSBS9xnVg%2BjdAsLqJUTSRjpYxs1yEfbT4HgJX2YYr99lO7b%2FC%2BQ7R59fOszGh02u55NHycSk24mm6AYynOi4B7BzLr0IKoFMyJR%2BUxwuOBizO65SXkb7sNEYm1r9vHj78t4P7SzzcqWap5HfiBcvAg1b96uGvwGNLcsdlqnktJzyfAwYLVYpQ&X-Amz-Signature=05ee9ed2daf025814d004af54b3d48ad7744db1fa1ab63693c7ac31d2082f552&X-Amz-SignedHeaders=host&x-id=GetObject)
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


