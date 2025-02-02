

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZKWU4E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCytD%2B6ycMkKUTUdv%2F1%2F65L4oASICPuJe5cZ4KncdfXxwIhALOOUJYOUjzTnlWFR2g%2B1RikHEpbfHPBrREZKd1%2FO3XXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFte2Ca2TIg8GQ0Qkq3ANU0wrikaso9zGpyubryvrwIs1L%2B7itK2LzrbcI3GNnkEdiBkEk39EM05%2BzNCAkBD8%2FpendWuo0zSK1oQV6nXAW1i578beyv9cdX6qb8SXAZtIkRjuLjDES3VilpoJYDJ%2FKd5KLZMpPIZRm20Qmy9O5Fw7rfjFThM9mnTaCeps5cTK7Ht4Ou9CVLI6U0ykGAJtu%2F65b%2BkeLDXMWbS33W3bqNyk80yyWsqtH7W1Dlrf5%2FYKF4qY5kQIlw0ZZFuzhhNprdES11BGMGqvx8QnqLbYcLTFTKCmnYhAAAx9dYIBBtCLipvvHZaTHbhbMSc2QavxR6xphDSx%2BPlU0VeEtecWbtFlf54Y3LJ4pzA4H9R8DDkkP9CyFEbru1Vr5atIjWWKfTzV6n%2F39qweBUGiOvtxkXLfxWZsz%2Bfg6mlLnmw3qBmH40nMTcK5OW7%2ByfyVwbCyaLkL%2FKuDUoKRL3pTm51SO2qEUgRC87bXeWJNIs%2BQWBgDQ8pP6988UGywIXGSCxsTwqpMLbjYawa1Aice8WbmtPRiQhk2DNFolcpLb5O80T6Ctv9voEIcHUVQAzLNwHkDY5fTK7QxeWLsPnAKUhQ8XDTj7EpEbBXcFqymdsqdE2vKlIB5T9X4W8nZ8ujClnPy8BjqkAaOnxG6ra4DAaGyrWykZEq0GccJj%2B9e84mJsiCZb%2B4jlc4%2FzED%2FbK2SNnC8svT%2F%2FoFYkamY0gVa1hY22a0iQENAGW%2FUiuTGeV3qHPYIxADDKgw2Stx22bFXX%2FD58sHIAwsAYoxJAvrOkoAsrp8MHPHgsJ%2F9rh9PvL%2Bpah91SGfknilpYL%2FCh6zdP6B4QhXZqCHXPQvn00l4HG5fDSVlwfrihDul%2B&X-Amz-Signature=42222a73770831790f9836723d31ee3aa1588e7acea1084e8897e45435ce02a2&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFMJAX24%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgE%2Bv09WucupPjsd3e0UH2%2FAxHH1jjP6amSNqWX7q3OQIhANrwscoglPYLRmRM0bliLFbDn6%2F2hmEA7lLdFe5wkO%2BlKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FW%2F75KKziNkYKnU0q3ANLjpHph4CTcv63VzJ%2BqmdTHgvj%2BrkeAQFbOla85nKl%2FTnBLPTK1F%2FxGR4dHsGvQmME17C%2Bf8XPXPi5yXgwdQnhOT2slNyL54uHn0oDaxx7XMWGM2Dhgja9M%2FaElYx1ts72Tt9BzJDQIslXya43%2FegtXXwPTLk7TBtwI%2BcvxQJn0LMx54qjD1nGGNcBoOIYzyCcZnm89LwxdKdmVsa8gkTSYSCXwJ87oIKiglGNKVIHY%2FADmGPRYfvnAFSqDDgF8so7eQyITWlMg%2FVI%2Fe1LzoolIlm2OZzXIseIVQWUkX%2Bw3kjxMDEucCD6mkSgwxyJEaAVpKBJyAjFo4v%2Fx1k%2B3QtjMC2WAVdrkjRE4L69o%2F74c1WpToVp1g4SD0xXKIyAgzqXjCpge1lZKwf%2FE7%2FM%2FbobNs2Glohy3SagLil7A2qNTT5nnQBDZy8mUnaDTZ%2FYVwDxBeZhJa2KeKEW4ZOLkxTYOUeghHN5mUAlcNao7TxyimpMzYK2GMT%2FfNfHJWIxY0Ew17%2FtA9SAZtAnQ4yHaWhUvIsWMASHOXdAaJCQaCKInF%2FIzQPcwOSfmcAwmsPc5YjECgJFqnXIwB%2Bovb%2B1fT8Id4C1RIbfvfTYfGDRdUIDGksNXMwTLiZTZh3iyjCInPy8BjqkAXDYLv8IL8K%2FGOOpNkAoumGxQ9z0poLNSfvVbR32eg0A8FO4oysP94XeLhr0cDq7R2qna%2BzuOVTQHmkL1Qls8zqza4Yiz83AI%2BX3wz47YDf1yiN42yqaSrxmqG%2FoAEJG81U1dIyE5wu%2FrdYNfumml4yKCLpi%2BrD79%2BEqK%2B6LLcI8SX%2B9h6U7udnkI7CkLvPFITkNldYcldNy1U%2FqJlIx3ON8tUQN&X-Amz-Signature=14b451f314ea8ec91b08e16efe4c83db1fee53014e95d96daf8e94602dffec06&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFMJAX24%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgE%2Bv09WucupPjsd3e0UH2%2FAxHH1jjP6amSNqWX7q3OQIhANrwscoglPYLRmRM0bliLFbDn6%2F2hmEA7lLdFe5wkO%2BlKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FW%2F75KKziNkYKnU0q3ANLjpHph4CTcv63VzJ%2BqmdTHgvj%2BrkeAQFbOla85nKl%2FTnBLPTK1F%2FxGR4dHsGvQmME17C%2Bf8XPXPi5yXgwdQnhOT2slNyL54uHn0oDaxx7XMWGM2Dhgja9M%2FaElYx1ts72Tt9BzJDQIslXya43%2FegtXXwPTLk7TBtwI%2BcvxQJn0LMx54qjD1nGGNcBoOIYzyCcZnm89LwxdKdmVsa8gkTSYSCXwJ87oIKiglGNKVIHY%2FADmGPRYfvnAFSqDDgF8so7eQyITWlMg%2FVI%2Fe1LzoolIlm2OZzXIseIVQWUkX%2Bw3kjxMDEucCD6mkSgwxyJEaAVpKBJyAjFo4v%2Fx1k%2B3QtjMC2WAVdrkjRE4L69o%2F74c1WpToVp1g4SD0xXKIyAgzqXjCpge1lZKwf%2FE7%2FM%2FbobNs2Glohy3SagLil7A2qNTT5nnQBDZy8mUnaDTZ%2FYVwDxBeZhJa2KeKEW4ZOLkxTYOUeghHN5mUAlcNao7TxyimpMzYK2GMT%2FfNfHJWIxY0Ew17%2FtA9SAZtAnQ4yHaWhUvIsWMASHOXdAaJCQaCKInF%2FIzQPcwOSfmcAwmsPc5YjECgJFqnXIwB%2Bovb%2B1fT8Id4C1RIbfvfTYfGDRdUIDGksNXMwTLiZTZh3iyjCInPy8BjqkAXDYLv8IL8K%2FGOOpNkAoumGxQ9z0poLNSfvVbR32eg0A8FO4oysP94XeLhr0cDq7R2qna%2BzuOVTQHmkL1Qls8zqza4Yiz83AI%2BX3wz47YDf1yiN42yqaSrxmqG%2FoAEJG81U1dIyE5wu%2FrdYNfumml4yKCLpi%2BrD79%2BEqK%2B6LLcI8SX%2B9h6U7udnkI7CkLvPFITkNldYcldNy1U%2FqJlIx3ON8tUQN&X-Amz-Signature=69b2350a41fb8f43431e706cb5d4b8f6b90df2a18000d48f0a590aa41b603be3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFMJAX24%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgE%2Bv09WucupPjsd3e0UH2%2FAxHH1jjP6amSNqWX7q3OQIhANrwscoglPYLRmRM0bliLFbDn6%2F2hmEA7lLdFe5wkO%2BlKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FW%2F75KKziNkYKnU0q3ANLjpHph4CTcv63VzJ%2BqmdTHgvj%2BrkeAQFbOla85nKl%2FTnBLPTK1F%2FxGR4dHsGvQmME17C%2Bf8XPXPi5yXgwdQnhOT2slNyL54uHn0oDaxx7XMWGM2Dhgja9M%2FaElYx1ts72Tt9BzJDQIslXya43%2FegtXXwPTLk7TBtwI%2BcvxQJn0LMx54qjD1nGGNcBoOIYzyCcZnm89LwxdKdmVsa8gkTSYSCXwJ87oIKiglGNKVIHY%2FADmGPRYfvnAFSqDDgF8so7eQyITWlMg%2FVI%2Fe1LzoolIlm2OZzXIseIVQWUkX%2Bw3kjxMDEucCD6mkSgwxyJEaAVpKBJyAjFo4v%2Fx1k%2B3QtjMC2WAVdrkjRE4L69o%2F74c1WpToVp1g4SD0xXKIyAgzqXjCpge1lZKwf%2FE7%2FM%2FbobNs2Glohy3SagLil7A2qNTT5nnQBDZy8mUnaDTZ%2FYVwDxBeZhJa2KeKEW4ZOLkxTYOUeghHN5mUAlcNao7TxyimpMzYK2GMT%2FfNfHJWIxY0Ew17%2FtA9SAZtAnQ4yHaWhUvIsWMASHOXdAaJCQaCKInF%2FIzQPcwOSfmcAwmsPc5YjECgJFqnXIwB%2Bovb%2B1fT8Id4C1RIbfvfTYfGDRdUIDGksNXMwTLiZTZh3iyjCInPy8BjqkAXDYLv8IL8K%2FGOOpNkAoumGxQ9z0poLNSfvVbR32eg0A8FO4oysP94XeLhr0cDq7R2qna%2BzuOVTQHmkL1Qls8zqza4Yiz83AI%2BX3wz47YDf1yiN42yqaSrxmqG%2FoAEJG81U1dIyE5wu%2FrdYNfumml4yKCLpi%2BrD79%2BEqK%2B6LLcI8SX%2B9h6U7udnkI7CkLvPFITkNldYcldNy1U%2FqJlIx3ON8tUQN&X-Amz-Signature=c3fc467c6714d14e2d6a405c339c08c8605f3a6863bc77199f08b280121cc956&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFMJAX24%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgE%2Bv09WucupPjsd3e0UH2%2FAxHH1jjP6amSNqWX7q3OQIhANrwscoglPYLRmRM0bliLFbDn6%2F2hmEA7lLdFe5wkO%2BlKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FW%2F75KKziNkYKnU0q3ANLjpHph4CTcv63VzJ%2BqmdTHgvj%2BrkeAQFbOla85nKl%2FTnBLPTK1F%2FxGR4dHsGvQmME17C%2Bf8XPXPi5yXgwdQnhOT2slNyL54uHn0oDaxx7XMWGM2Dhgja9M%2FaElYx1ts72Tt9BzJDQIslXya43%2FegtXXwPTLk7TBtwI%2BcvxQJn0LMx54qjD1nGGNcBoOIYzyCcZnm89LwxdKdmVsa8gkTSYSCXwJ87oIKiglGNKVIHY%2FADmGPRYfvnAFSqDDgF8so7eQyITWlMg%2FVI%2Fe1LzoolIlm2OZzXIseIVQWUkX%2Bw3kjxMDEucCD6mkSgwxyJEaAVpKBJyAjFo4v%2Fx1k%2B3QtjMC2WAVdrkjRE4L69o%2F74c1WpToVp1g4SD0xXKIyAgzqXjCpge1lZKwf%2FE7%2FM%2FbobNs2Glohy3SagLil7A2qNTT5nnQBDZy8mUnaDTZ%2FYVwDxBeZhJa2KeKEW4ZOLkxTYOUeghHN5mUAlcNao7TxyimpMzYK2GMT%2FfNfHJWIxY0Ew17%2FtA9SAZtAnQ4yHaWhUvIsWMASHOXdAaJCQaCKInF%2FIzQPcwOSfmcAwmsPc5YjECgJFqnXIwB%2Bovb%2B1fT8Id4C1RIbfvfTYfGDRdUIDGksNXMwTLiZTZh3iyjCInPy8BjqkAXDYLv8IL8K%2FGOOpNkAoumGxQ9z0poLNSfvVbR32eg0A8FO4oysP94XeLhr0cDq7R2qna%2BzuOVTQHmkL1Qls8zqza4Yiz83AI%2BX3wz47YDf1yiN42yqaSrxmqG%2FoAEJG81U1dIyE5wu%2FrdYNfumml4yKCLpi%2BrD79%2BEqK%2B6LLcI8SX%2B9h6U7udnkI7CkLvPFITkNldYcldNy1U%2FqJlIx3ON8tUQN&X-Amz-Signature=7bbe2f225b16953304f043de42ee9f271e54c1df5630c3abab26dd73e5dc9b5b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFMJAX24%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgE%2Bv09WucupPjsd3e0UH2%2FAxHH1jjP6amSNqWX7q3OQIhANrwscoglPYLRmRM0bliLFbDn6%2F2hmEA7lLdFe5wkO%2BlKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FW%2F75KKziNkYKnU0q3ANLjpHph4CTcv63VzJ%2BqmdTHgvj%2BrkeAQFbOla85nKl%2FTnBLPTK1F%2FxGR4dHsGvQmME17C%2Bf8XPXPi5yXgwdQnhOT2slNyL54uHn0oDaxx7XMWGM2Dhgja9M%2FaElYx1ts72Tt9BzJDQIslXya43%2FegtXXwPTLk7TBtwI%2BcvxQJn0LMx54qjD1nGGNcBoOIYzyCcZnm89LwxdKdmVsa8gkTSYSCXwJ87oIKiglGNKVIHY%2FADmGPRYfvnAFSqDDgF8so7eQyITWlMg%2FVI%2Fe1LzoolIlm2OZzXIseIVQWUkX%2Bw3kjxMDEucCD6mkSgwxyJEaAVpKBJyAjFo4v%2Fx1k%2B3QtjMC2WAVdrkjRE4L69o%2F74c1WpToVp1g4SD0xXKIyAgzqXjCpge1lZKwf%2FE7%2FM%2FbobNs2Glohy3SagLil7A2qNTT5nnQBDZy8mUnaDTZ%2FYVwDxBeZhJa2KeKEW4ZOLkxTYOUeghHN5mUAlcNao7TxyimpMzYK2GMT%2FfNfHJWIxY0Ew17%2FtA9SAZtAnQ4yHaWhUvIsWMASHOXdAaJCQaCKInF%2FIzQPcwOSfmcAwmsPc5YjECgJFqnXIwB%2Bovb%2B1fT8Id4C1RIbfvfTYfGDRdUIDGksNXMwTLiZTZh3iyjCInPy8BjqkAXDYLv8IL8K%2FGOOpNkAoumGxQ9z0poLNSfvVbR32eg0A8FO4oysP94XeLhr0cDq7R2qna%2BzuOVTQHmkL1Qls8zqza4Yiz83AI%2BX3wz47YDf1yiN42yqaSrxmqG%2FoAEJG81U1dIyE5wu%2FrdYNfumml4yKCLpi%2BrD79%2BEqK%2B6LLcI8SX%2B9h6U7udnkI7CkLvPFITkNldYcldNy1U%2FqJlIx3ON8tUQN&X-Amz-Signature=918d2b4c9bd37dcfd1bdb04234f2a504a7535e605f2e8e7143e5b24851952090&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZKWU4E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCytD%2B6ycMkKUTUdv%2F1%2F65L4oASICPuJe5cZ4KncdfXxwIhALOOUJYOUjzTnlWFR2g%2B1RikHEpbfHPBrREZKd1%2FO3XXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFte2Ca2TIg8GQ0Qkq3ANU0wrikaso9zGpyubryvrwIs1L%2B7itK2LzrbcI3GNnkEdiBkEk39EM05%2BzNCAkBD8%2FpendWuo0zSK1oQV6nXAW1i578beyv9cdX6qb8SXAZtIkRjuLjDES3VilpoJYDJ%2FKd5KLZMpPIZRm20Qmy9O5Fw7rfjFThM9mnTaCeps5cTK7Ht4Ou9CVLI6U0ykGAJtu%2F65b%2BkeLDXMWbS33W3bqNyk80yyWsqtH7W1Dlrf5%2FYKF4qY5kQIlw0ZZFuzhhNprdES11BGMGqvx8QnqLbYcLTFTKCmnYhAAAx9dYIBBtCLipvvHZaTHbhbMSc2QavxR6xphDSx%2BPlU0VeEtecWbtFlf54Y3LJ4pzA4H9R8DDkkP9CyFEbru1Vr5atIjWWKfTzV6n%2F39qweBUGiOvtxkXLfxWZsz%2Bfg6mlLnmw3qBmH40nMTcK5OW7%2ByfyVwbCyaLkL%2FKuDUoKRL3pTm51SO2qEUgRC87bXeWJNIs%2BQWBgDQ8pP6988UGywIXGSCxsTwqpMLbjYawa1Aice8WbmtPRiQhk2DNFolcpLb5O80T6Ctv9voEIcHUVQAzLNwHkDY5fTK7QxeWLsPnAKUhQ8XDTj7EpEbBXcFqymdsqdE2vKlIB5T9X4W8nZ8ujClnPy8BjqkAaOnxG6ra4DAaGyrWykZEq0GccJj%2B9e84mJsiCZb%2B4jlc4%2FzED%2FbK2SNnC8svT%2F%2FoFYkamY0gVa1hY22a0iQENAGW%2FUiuTGeV3qHPYIxADDKgw2Stx22bFXX%2FD58sHIAwsAYoxJAvrOkoAsrp8MHPHgsJ%2F9rh9PvL%2Bpah91SGfknilpYL%2FCh6zdP6B4QhXZqCHXPQvn00l4HG5fDSVlwfrihDul%2B&X-Amz-Signature=d7fe3caae86354671ef469e6b819a14e37b8815f0d14b651fb5d7e8ee8a179c4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZKWU4E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCytD%2B6ycMkKUTUdv%2F1%2F65L4oASICPuJe5cZ4KncdfXxwIhALOOUJYOUjzTnlWFR2g%2B1RikHEpbfHPBrREZKd1%2FO3XXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFte2Ca2TIg8GQ0Qkq3ANU0wrikaso9zGpyubryvrwIs1L%2B7itK2LzrbcI3GNnkEdiBkEk39EM05%2BzNCAkBD8%2FpendWuo0zSK1oQV6nXAW1i578beyv9cdX6qb8SXAZtIkRjuLjDES3VilpoJYDJ%2FKd5KLZMpPIZRm20Qmy9O5Fw7rfjFThM9mnTaCeps5cTK7Ht4Ou9CVLI6U0ykGAJtu%2F65b%2BkeLDXMWbS33W3bqNyk80yyWsqtH7W1Dlrf5%2FYKF4qY5kQIlw0ZZFuzhhNprdES11BGMGqvx8QnqLbYcLTFTKCmnYhAAAx9dYIBBtCLipvvHZaTHbhbMSc2QavxR6xphDSx%2BPlU0VeEtecWbtFlf54Y3LJ4pzA4H9R8DDkkP9CyFEbru1Vr5atIjWWKfTzV6n%2F39qweBUGiOvtxkXLfxWZsz%2Bfg6mlLnmw3qBmH40nMTcK5OW7%2ByfyVwbCyaLkL%2FKuDUoKRL3pTm51SO2qEUgRC87bXeWJNIs%2BQWBgDQ8pP6988UGywIXGSCxsTwqpMLbjYawa1Aice8WbmtPRiQhk2DNFolcpLb5O80T6Ctv9voEIcHUVQAzLNwHkDY5fTK7QxeWLsPnAKUhQ8XDTj7EpEbBXcFqymdsqdE2vKlIB5T9X4W8nZ8ujClnPy8BjqkAaOnxG6ra4DAaGyrWykZEq0GccJj%2B9e84mJsiCZb%2B4jlc4%2FzED%2FbK2SNnC8svT%2F%2FoFYkamY0gVa1hY22a0iQENAGW%2FUiuTGeV3qHPYIxADDKgw2Stx22bFXX%2FD58sHIAwsAYoxJAvrOkoAsrp8MHPHgsJ%2F9rh9PvL%2Bpah91SGfknilpYL%2FCh6zdP6B4QhXZqCHXPQvn00l4HG5fDSVlwfrihDul%2B&X-Amz-Signature=7e1f2046e3faebf65615e48ad4c811c898d1c32dab505be871dc2c10b8a1bf1c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZKWU4E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCytD%2B6ycMkKUTUdv%2F1%2F65L4oASICPuJe5cZ4KncdfXxwIhALOOUJYOUjzTnlWFR2g%2B1RikHEpbfHPBrREZKd1%2FO3XXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFte2Ca2TIg8GQ0Qkq3ANU0wrikaso9zGpyubryvrwIs1L%2B7itK2LzrbcI3GNnkEdiBkEk39EM05%2BzNCAkBD8%2FpendWuo0zSK1oQV6nXAW1i578beyv9cdX6qb8SXAZtIkRjuLjDES3VilpoJYDJ%2FKd5KLZMpPIZRm20Qmy9O5Fw7rfjFThM9mnTaCeps5cTK7Ht4Ou9CVLI6U0ykGAJtu%2F65b%2BkeLDXMWbS33W3bqNyk80yyWsqtH7W1Dlrf5%2FYKF4qY5kQIlw0ZZFuzhhNprdES11BGMGqvx8QnqLbYcLTFTKCmnYhAAAx9dYIBBtCLipvvHZaTHbhbMSc2QavxR6xphDSx%2BPlU0VeEtecWbtFlf54Y3LJ4pzA4H9R8DDkkP9CyFEbru1Vr5atIjWWKfTzV6n%2F39qweBUGiOvtxkXLfxWZsz%2Bfg6mlLnmw3qBmH40nMTcK5OW7%2ByfyVwbCyaLkL%2FKuDUoKRL3pTm51SO2qEUgRC87bXeWJNIs%2BQWBgDQ8pP6988UGywIXGSCxsTwqpMLbjYawa1Aice8WbmtPRiQhk2DNFolcpLb5O80T6Ctv9voEIcHUVQAzLNwHkDY5fTK7QxeWLsPnAKUhQ8XDTj7EpEbBXcFqymdsqdE2vKlIB5T9X4W8nZ8ujClnPy8BjqkAaOnxG6ra4DAaGyrWykZEq0GccJj%2B9e84mJsiCZb%2B4jlc4%2FzED%2FbK2SNnC8svT%2F%2FoFYkamY0gVa1hY22a0iQENAGW%2FUiuTGeV3qHPYIxADDKgw2Stx22bFXX%2FD58sHIAwsAYoxJAvrOkoAsrp8MHPHgsJ%2F9rh9PvL%2Bpah91SGfknilpYL%2FCh6zdP6B4QhXZqCHXPQvn00l4HG5fDSVlwfrihDul%2B&X-Amz-Signature=4d44696b3b6ee700bda388681fc1c820d76049916fc423b91c9d2d1430fce7bf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZKWU4E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCytD%2B6ycMkKUTUdv%2F1%2F65L4oASICPuJe5cZ4KncdfXxwIhALOOUJYOUjzTnlWFR2g%2B1RikHEpbfHPBrREZKd1%2FO3XXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFte2Ca2TIg8GQ0Qkq3ANU0wrikaso9zGpyubryvrwIs1L%2B7itK2LzrbcI3GNnkEdiBkEk39EM05%2BzNCAkBD8%2FpendWuo0zSK1oQV6nXAW1i578beyv9cdX6qb8SXAZtIkRjuLjDES3VilpoJYDJ%2FKd5KLZMpPIZRm20Qmy9O5Fw7rfjFThM9mnTaCeps5cTK7Ht4Ou9CVLI6U0ykGAJtu%2F65b%2BkeLDXMWbS33W3bqNyk80yyWsqtH7W1Dlrf5%2FYKF4qY5kQIlw0ZZFuzhhNprdES11BGMGqvx8QnqLbYcLTFTKCmnYhAAAx9dYIBBtCLipvvHZaTHbhbMSc2QavxR6xphDSx%2BPlU0VeEtecWbtFlf54Y3LJ4pzA4H9R8DDkkP9CyFEbru1Vr5atIjWWKfTzV6n%2F39qweBUGiOvtxkXLfxWZsz%2Bfg6mlLnmw3qBmH40nMTcK5OW7%2ByfyVwbCyaLkL%2FKuDUoKRL3pTm51SO2qEUgRC87bXeWJNIs%2BQWBgDQ8pP6988UGywIXGSCxsTwqpMLbjYawa1Aice8WbmtPRiQhk2DNFolcpLb5O80T6Ctv9voEIcHUVQAzLNwHkDY5fTK7QxeWLsPnAKUhQ8XDTj7EpEbBXcFqymdsqdE2vKlIB5T9X4W8nZ8ujClnPy8BjqkAaOnxG6ra4DAaGyrWykZEq0GccJj%2B9e84mJsiCZb%2B4jlc4%2FzED%2FbK2SNnC8svT%2F%2FoFYkamY0gVa1hY22a0iQENAGW%2FUiuTGeV3qHPYIxADDKgw2Stx22bFXX%2FD58sHIAwsAYoxJAvrOkoAsrp8MHPHgsJ%2F9rh9PvL%2Bpah91SGfknilpYL%2FCh6zdP6B4QhXZqCHXPQvn00l4HG5fDSVlwfrihDul%2B&X-Amz-Signature=2d07dc4d3a0fabb07138d11cdcc2777a17dc8b045d6d6354273636958d1e9f99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZKWU4E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCytD%2B6ycMkKUTUdv%2F1%2F65L4oASICPuJe5cZ4KncdfXxwIhALOOUJYOUjzTnlWFR2g%2B1RikHEpbfHPBrREZKd1%2FO3XXKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFte2Ca2TIg8GQ0Qkq3ANU0wrikaso9zGpyubryvrwIs1L%2B7itK2LzrbcI3GNnkEdiBkEk39EM05%2BzNCAkBD8%2FpendWuo0zSK1oQV6nXAW1i578beyv9cdX6qb8SXAZtIkRjuLjDES3VilpoJYDJ%2FKd5KLZMpPIZRm20Qmy9O5Fw7rfjFThM9mnTaCeps5cTK7Ht4Ou9CVLI6U0ykGAJtu%2F65b%2BkeLDXMWbS33W3bqNyk80yyWsqtH7W1Dlrf5%2FYKF4qY5kQIlw0ZZFuzhhNprdES11BGMGqvx8QnqLbYcLTFTKCmnYhAAAx9dYIBBtCLipvvHZaTHbhbMSc2QavxR6xphDSx%2BPlU0VeEtecWbtFlf54Y3LJ4pzA4H9R8DDkkP9CyFEbru1Vr5atIjWWKfTzV6n%2F39qweBUGiOvtxkXLfxWZsz%2Bfg6mlLnmw3qBmH40nMTcK5OW7%2ByfyVwbCyaLkL%2FKuDUoKRL3pTm51SO2qEUgRC87bXeWJNIs%2BQWBgDQ8pP6988UGywIXGSCxsTwqpMLbjYawa1Aice8WbmtPRiQhk2DNFolcpLb5O80T6Ctv9voEIcHUVQAzLNwHkDY5fTK7QxeWLsPnAKUhQ8XDTj7EpEbBXcFqymdsqdE2vKlIB5T9X4W8nZ8ujClnPy8BjqkAaOnxG6ra4DAaGyrWykZEq0GccJj%2B9e84mJsiCZb%2B4jlc4%2FzED%2FbK2SNnC8svT%2F%2FoFYkamY0gVa1hY22a0iQENAGW%2FUiuTGeV3qHPYIxADDKgw2Stx22bFXX%2FD58sHIAwsAYoxJAvrOkoAsrp8MHPHgsJ%2F9rh9PvL%2Bpah91SGfknilpYL%2FCh6zdP6B4QhXZqCHXPQvn00l4HG5fDSVlwfrihDul%2B&X-Amz-Signature=92914d44b244f1a8cea9758b8b15fa282b0e86c2fefe0024941b157fb18e9253&X-Amz-SignedHeaders=host&x-id=GetObject)
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


