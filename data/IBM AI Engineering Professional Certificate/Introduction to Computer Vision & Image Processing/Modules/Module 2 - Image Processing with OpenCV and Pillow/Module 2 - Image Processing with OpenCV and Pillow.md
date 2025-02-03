

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVWLRIQQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCTy7eNDS8grtYrrA7KwzQjjoiTgSgixFGHxX1bcoT%2B6wIhAIrZY2eU7nqrrUmcPB5SEF0Pzg5r56gJ0gHcASTJtw%2B7Kv8DCBoQABoMNjM3NDIzMTgzODA1Igyh7X2n1E0RmoHRHj4q3ANNL5nyM7pQqzflg2myWWN5ltKUBwks7gXiKUB%2BJiGTO7fgrBMsR9WBR1WI9%2Bmmw4IH2rbl5i7HtCiCcJvJLk9JMs7KFS515J1Ytrc4re6LTfNpJrXcHRq%2FKtup%2F4L5lDRo9ObxHq1ebVVXsUbyUHj7Y7SxV1L1eyF0hplkD7MLshg%2BoTXzRJUN4wdN9%2BEWrgJ6tyyWF8Zjd19ECcNMFusD59Ofh6H24X%2FPOeqgg3qHjb5sRG4FLx8DcPUaB9GLY4T9b2SIT1zqaX0dfVO7yc%2Bz%2BEO9QD2r1hEAc%2B8tPCgHkjyWDnItKip1e2BwTc1iSM7XKlglMePDoLnhhMyGiGdAzfNKSVgWu%2BEN5SFz3I3C4u2YZpaCRh9bdXQItN%2Fg9nhRLDZKlZVVIWXjGizbyIBPkPaTXaAYn2GtjffCabjzbcVhCK23mTNRF7OxEZCL%2FIsWcXdCbzAHqGGJQwbyYKQXTOVUNmOTroFVh4s8sW56cMo6Ae7UrvloCJBXMMw80Gbkwxxxl8b7z3r3rXef7BVd7Z%2FBKZAW0xUCSsUb89HRA%2BaQIGtfQ%2FKq4pzOWRf2NXM7EPQUMAYeopj4tOGDAt2IvPlHOaWrTyTyUhNL2RM2dOamGRNRmwsh3pIb%2BzCY5oO9BjqkASejPy1gv8xjwICnaZCrCJAp6ziVWvkz%2FeZGvia8TtCt8o073Fq7PKB9YPdb1yZFPGytF9g71CmcqPClNDfwpwo6r0Pex4Zg%2BUfOSve3SkHx8lcToeXle%2FmrUU9f%2BX3w0jPgl6d6MV1rRDq1vq01YR3qCJdwezDE0kmuCelnRkNRYYALbW%2FkWuOx5ai6ZNvUoCAHIa60q5welX%2BhoIUCuLfP4B7s&X-Amz-Signature=0f56ba21ff3515599b83eec7bd22db3ad8fb9c22e3eea3c143c65cb2bf25fe71&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KSLHB6H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIBKS6PJ%2FH4ZA6QVqvhKyOUSJypEZHGQS0iUqE05B6WstAiEA1zBvUBXYPfoPlcx4Vk4OdX%2BXflZ1Lfxpn1LLTrqnLgYq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDJ0w2k%2BwdTY%2FhaI32CrcA%2FxDr7eBubTxkcwHs0psWeTZnIejBlPR3Ble2J6QJwygrr4xvM5IfstIhdGwhjOVkzr4FhUzEZ8%2FqpDPslE%2B0uYBy751sd0HBITbU7bhfDrOJnZWrL86hBcmpFmEM3a5KN0N76vI2fFljH7CiDz2ipWSoWussGc1memRjewgHMpmh7jxL07IfdoVUHsz5lVS%2BTXSAP%2F7%2FtGdfNFlyTiDzTbGMvmitFL5LmgPwF7e1F2UjZ192A%2FXI8Hpl4eRwepUvzoGQyx0tmnDm%2FDUMlVBxsFQoJiwhTGJ6LGugfH9U7Ae38gvMhD%2FnTP3ZMS8YLjalN4bC6urhv3zOZ6cM7mlF6Zx8c0fW2PjLHEqxYlvIqTEoSmTcjfoOiyZOySiU4UYqFaHIKLGK6VOvS4yJf2jeCBt4yyTRGeZLHOOI47YleduFcN95y5AKxuMXu1cAFaJDyshNKIp9pyP8pof%2BLoURb47Fz5x9bfuMRfcAUOGxkSdhXl7oPBbqd4tZ1ytqTvjpL5XxFORL8siXU9BHHFP0NJt9uOBEvnOcXRWLHytUC7oKl0AlJwcsd8%2BvL9fE7oQ3QKmdeTdQer%2FTKuzkSTQ4txBFuGomXAr5CfqcDJE6RjWkgub1bSQyaYtoLfoMPjlg70GOqUBweyqTHKN%2By7U1EtOl79h66LAyTaySjpKk94CfFRB61GTWG3UKAR7TiG%2FSMQDZYmRxPqT7a8DP4PhyIVUVXWC82LKl3PU8040P1NSUXLQ9KZ8yx%2BSkP%2BsR8i0HBmpcj2DB%2FyPykuE4X7gB8unYiequF67%2BjjhMf25I3DQNBIcvzH8O3OqC3oRjfgh66yeXKlf4XC%2FMTqQukIcg0fGseFgLFbZRPwU&X-Amz-Signature=1af429fdd4641be5bc4bf8987a5f293ee173ca8e2a362af97576c326f78e53be&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KSLHB6H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIBKS6PJ%2FH4ZA6QVqvhKyOUSJypEZHGQS0iUqE05B6WstAiEA1zBvUBXYPfoPlcx4Vk4OdX%2BXflZ1Lfxpn1LLTrqnLgYq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDJ0w2k%2BwdTY%2FhaI32CrcA%2FxDr7eBubTxkcwHs0psWeTZnIejBlPR3Ble2J6QJwygrr4xvM5IfstIhdGwhjOVkzr4FhUzEZ8%2FqpDPslE%2B0uYBy751sd0HBITbU7bhfDrOJnZWrL86hBcmpFmEM3a5KN0N76vI2fFljH7CiDz2ipWSoWussGc1memRjewgHMpmh7jxL07IfdoVUHsz5lVS%2BTXSAP%2F7%2FtGdfNFlyTiDzTbGMvmitFL5LmgPwF7e1F2UjZ192A%2FXI8Hpl4eRwepUvzoGQyx0tmnDm%2FDUMlVBxsFQoJiwhTGJ6LGugfH9U7Ae38gvMhD%2FnTP3ZMS8YLjalN4bC6urhv3zOZ6cM7mlF6Zx8c0fW2PjLHEqxYlvIqTEoSmTcjfoOiyZOySiU4UYqFaHIKLGK6VOvS4yJf2jeCBt4yyTRGeZLHOOI47YleduFcN95y5AKxuMXu1cAFaJDyshNKIp9pyP8pof%2BLoURb47Fz5x9bfuMRfcAUOGxkSdhXl7oPBbqd4tZ1ytqTvjpL5XxFORL8siXU9BHHFP0NJt9uOBEvnOcXRWLHytUC7oKl0AlJwcsd8%2BvL9fE7oQ3QKmdeTdQer%2FTKuzkSTQ4txBFuGomXAr5CfqcDJE6RjWkgub1bSQyaYtoLfoMPjlg70GOqUBweyqTHKN%2By7U1EtOl79h66LAyTaySjpKk94CfFRB61GTWG3UKAR7TiG%2FSMQDZYmRxPqT7a8DP4PhyIVUVXWC82LKl3PU8040P1NSUXLQ9KZ8yx%2BSkP%2BsR8i0HBmpcj2DB%2FyPykuE4X7gB8unYiequF67%2BjjhMf25I3DQNBIcvzH8O3OqC3oRjfgh66yeXKlf4XC%2FMTqQukIcg0fGseFgLFbZRPwU&X-Amz-Signature=c8939b4f72d3c7e3973e0a91979a9c9e0b9984b959d382ad3ab44875ba017c38&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KSLHB6H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIBKS6PJ%2FH4ZA6QVqvhKyOUSJypEZHGQS0iUqE05B6WstAiEA1zBvUBXYPfoPlcx4Vk4OdX%2BXflZ1Lfxpn1LLTrqnLgYq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDJ0w2k%2BwdTY%2FhaI32CrcA%2FxDr7eBubTxkcwHs0psWeTZnIejBlPR3Ble2J6QJwygrr4xvM5IfstIhdGwhjOVkzr4FhUzEZ8%2FqpDPslE%2B0uYBy751sd0HBITbU7bhfDrOJnZWrL86hBcmpFmEM3a5KN0N76vI2fFljH7CiDz2ipWSoWussGc1memRjewgHMpmh7jxL07IfdoVUHsz5lVS%2BTXSAP%2F7%2FtGdfNFlyTiDzTbGMvmitFL5LmgPwF7e1F2UjZ192A%2FXI8Hpl4eRwepUvzoGQyx0tmnDm%2FDUMlVBxsFQoJiwhTGJ6LGugfH9U7Ae38gvMhD%2FnTP3ZMS8YLjalN4bC6urhv3zOZ6cM7mlF6Zx8c0fW2PjLHEqxYlvIqTEoSmTcjfoOiyZOySiU4UYqFaHIKLGK6VOvS4yJf2jeCBt4yyTRGeZLHOOI47YleduFcN95y5AKxuMXu1cAFaJDyshNKIp9pyP8pof%2BLoURb47Fz5x9bfuMRfcAUOGxkSdhXl7oPBbqd4tZ1ytqTvjpL5XxFORL8siXU9BHHFP0NJt9uOBEvnOcXRWLHytUC7oKl0AlJwcsd8%2BvL9fE7oQ3QKmdeTdQer%2FTKuzkSTQ4txBFuGomXAr5CfqcDJE6RjWkgub1bSQyaYtoLfoMPjlg70GOqUBweyqTHKN%2By7U1EtOl79h66LAyTaySjpKk94CfFRB61GTWG3UKAR7TiG%2FSMQDZYmRxPqT7a8DP4PhyIVUVXWC82LKl3PU8040P1NSUXLQ9KZ8yx%2BSkP%2BsR8i0HBmpcj2DB%2FyPykuE4X7gB8unYiequF67%2BjjhMf25I3DQNBIcvzH8O3OqC3oRjfgh66yeXKlf4XC%2FMTqQukIcg0fGseFgLFbZRPwU&X-Amz-Signature=0086eea2dbca04e34b730119351911fa3c1862e735ff5d193ee23b88faca3492&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KSLHB6H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIBKS6PJ%2FH4ZA6QVqvhKyOUSJypEZHGQS0iUqE05B6WstAiEA1zBvUBXYPfoPlcx4Vk4OdX%2BXflZ1Lfxpn1LLTrqnLgYq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDJ0w2k%2BwdTY%2FhaI32CrcA%2FxDr7eBubTxkcwHs0psWeTZnIejBlPR3Ble2J6QJwygrr4xvM5IfstIhdGwhjOVkzr4FhUzEZ8%2FqpDPslE%2B0uYBy751sd0HBITbU7bhfDrOJnZWrL86hBcmpFmEM3a5KN0N76vI2fFljH7CiDz2ipWSoWussGc1memRjewgHMpmh7jxL07IfdoVUHsz5lVS%2BTXSAP%2F7%2FtGdfNFlyTiDzTbGMvmitFL5LmgPwF7e1F2UjZ192A%2FXI8Hpl4eRwepUvzoGQyx0tmnDm%2FDUMlVBxsFQoJiwhTGJ6LGugfH9U7Ae38gvMhD%2FnTP3ZMS8YLjalN4bC6urhv3zOZ6cM7mlF6Zx8c0fW2PjLHEqxYlvIqTEoSmTcjfoOiyZOySiU4UYqFaHIKLGK6VOvS4yJf2jeCBt4yyTRGeZLHOOI47YleduFcN95y5AKxuMXu1cAFaJDyshNKIp9pyP8pof%2BLoURb47Fz5x9bfuMRfcAUOGxkSdhXl7oPBbqd4tZ1ytqTvjpL5XxFORL8siXU9BHHFP0NJt9uOBEvnOcXRWLHytUC7oKl0AlJwcsd8%2BvL9fE7oQ3QKmdeTdQer%2FTKuzkSTQ4txBFuGomXAr5CfqcDJE6RjWkgub1bSQyaYtoLfoMPjlg70GOqUBweyqTHKN%2By7U1EtOl79h66LAyTaySjpKk94CfFRB61GTWG3UKAR7TiG%2FSMQDZYmRxPqT7a8DP4PhyIVUVXWC82LKl3PU8040P1NSUXLQ9KZ8yx%2BSkP%2BsR8i0HBmpcj2DB%2FyPykuE4X7gB8unYiequF67%2BjjhMf25I3DQNBIcvzH8O3OqC3oRjfgh66yeXKlf4XC%2FMTqQukIcg0fGseFgLFbZRPwU&X-Amz-Signature=d74704bae3205b3b6899bba97f07a6497bb6d526c80314c182dd37c370a01435&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KSLHB6H%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIBKS6PJ%2FH4ZA6QVqvhKyOUSJypEZHGQS0iUqE05B6WstAiEA1zBvUBXYPfoPlcx4Vk4OdX%2BXflZ1Lfxpn1LLTrqnLgYq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDJ0w2k%2BwdTY%2FhaI32CrcA%2FxDr7eBubTxkcwHs0psWeTZnIejBlPR3Ble2J6QJwygrr4xvM5IfstIhdGwhjOVkzr4FhUzEZ8%2FqpDPslE%2B0uYBy751sd0HBITbU7bhfDrOJnZWrL86hBcmpFmEM3a5KN0N76vI2fFljH7CiDz2ipWSoWussGc1memRjewgHMpmh7jxL07IfdoVUHsz5lVS%2BTXSAP%2F7%2FtGdfNFlyTiDzTbGMvmitFL5LmgPwF7e1F2UjZ192A%2FXI8Hpl4eRwepUvzoGQyx0tmnDm%2FDUMlVBxsFQoJiwhTGJ6LGugfH9U7Ae38gvMhD%2FnTP3ZMS8YLjalN4bC6urhv3zOZ6cM7mlF6Zx8c0fW2PjLHEqxYlvIqTEoSmTcjfoOiyZOySiU4UYqFaHIKLGK6VOvS4yJf2jeCBt4yyTRGeZLHOOI47YleduFcN95y5AKxuMXu1cAFaJDyshNKIp9pyP8pof%2BLoURb47Fz5x9bfuMRfcAUOGxkSdhXl7oPBbqd4tZ1ytqTvjpL5XxFORL8siXU9BHHFP0NJt9uOBEvnOcXRWLHytUC7oKl0AlJwcsd8%2BvL9fE7oQ3QKmdeTdQer%2FTKuzkSTQ4txBFuGomXAr5CfqcDJE6RjWkgub1bSQyaYtoLfoMPjlg70GOqUBweyqTHKN%2By7U1EtOl79h66LAyTaySjpKk94CfFRB61GTWG3UKAR7TiG%2FSMQDZYmRxPqT7a8DP4PhyIVUVXWC82LKl3PU8040P1NSUXLQ9KZ8yx%2BSkP%2BsR8i0HBmpcj2DB%2FyPykuE4X7gB8unYiequF67%2BjjhMf25I3DQNBIcvzH8O3OqC3oRjfgh66yeXKlf4XC%2FMTqQukIcg0fGseFgLFbZRPwU&X-Amz-Signature=413608d9bc70429cd80193888a5a0fb608336ef18131f4b0b04518385d1359dd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVWLRIQQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCTy7eNDS8grtYrrA7KwzQjjoiTgSgixFGHxX1bcoT%2B6wIhAIrZY2eU7nqrrUmcPB5SEF0Pzg5r56gJ0gHcASTJtw%2B7Kv8DCBoQABoMNjM3NDIzMTgzODA1Igyh7X2n1E0RmoHRHj4q3ANNL5nyM7pQqzflg2myWWN5ltKUBwks7gXiKUB%2BJiGTO7fgrBMsR9WBR1WI9%2Bmmw4IH2rbl5i7HtCiCcJvJLk9JMs7KFS515J1Ytrc4re6LTfNpJrXcHRq%2FKtup%2F4L5lDRo9ObxHq1ebVVXsUbyUHj7Y7SxV1L1eyF0hplkD7MLshg%2BoTXzRJUN4wdN9%2BEWrgJ6tyyWF8Zjd19ECcNMFusD59Ofh6H24X%2FPOeqgg3qHjb5sRG4FLx8DcPUaB9GLY4T9b2SIT1zqaX0dfVO7yc%2Bz%2BEO9QD2r1hEAc%2B8tPCgHkjyWDnItKip1e2BwTc1iSM7XKlglMePDoLnhhMyGiGdAzfNKSVgWu%2BEN5SFz3I3C4u2YZpaCRh9bdXQItN%2Fg9nhRLDZKlZVVIWXjGizbyIBPkPaTXaAYn2GtjffCabjzbcVhCK23mTNRF7OxEZCL%2FIsWcXdCbzAHqGGJQwbyYKQXTOVUNmOTroFVh4s8sW56cMo6Ae7UrvloCJBXMMw80Gbkwxxxl8b7z3r3rXef7BVd7Z%2FBKZAW0xUCSsUb89HRA%2BaQIGtfQ%2FKq4pzOWRf2NXM7EPQUMAYeopj4tOGDAt2IvPlHOaWrTyTyUhNL2RM2dOamGRNRmwsh3pIb%2BzCY5oO9BjqkASejPy1gv8xjwICnaZCrCJAp6ziVWvkz%2FeZGvia8TtCt8o073Fq7PKB9YPdb1yZFPGytF9g71CmcqPClNDfwpwo6r0Pex4Zg%2BUfOSve3SkHx8lcToeXle%2FmrUU9f%2BX3w0jPgl6d6MV1rRDq1vq01YR3qCJdwezDE0kmuCelnRkNRYYALbW%2FkWuOx5ai6ZNvUoCAHIa60q5welX%2BhoIUCuLfP4B7s&X-Amz-Signature=4d844d2986605c0b3495ab1d751530daa27b2ad089e38f0ed88d3adb5e65b044&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVWLRIQQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCTy7eNDS8grtYrrA7KwzQjjoiTgSgixFGHxX1bcoT%2B6wIhAIrZY2eU7nqrrUmcPB5SEF0Pzg5r56gJ0gHcASTJtw%2B7Kv8DCBoQABoMNjM3NDIzMTgzODA1Igyh7X2n1E0RmoHRHj4q3ANNL5nyM7pQqzflg2myWWN5ltKUBwks7gXiKUB%2BJiGTO7fgrBMsR9WBR1WI9%2Bmmw4IH2rbl5i7HtCiCcJvJLk9JMs7KFS515J1Ytrc4re6LTfNpJrXcHRq%2FKtup%2F4L5lDRo9ObxHq1ebVVXsUbyUHj7Y7SxV1L1eyF0hplkD7MLshg%2BoTXzRJUN4wdN9%2BEWrgJ6tyyWF8Zjd19ECcNMFusD59Ofh6H24X%2FPOeqgg3qHjb5sRG4FLx8DcPUaB9GLY4T9b2SIT1zqaX0dfVO7yc%2Bz%2BEO9QD2r1hEAc%2B8tPCgHkjyWDnItKip1e2BwTc1iSM7XKlglMePDoLnhhMyGiGdAzfNKSVgWu%2BEN5SFz3I3C4u2YZpaCRh9bdXQItN%2Fg9nhRLDZKlZVVIWXjGizbyIBPkPaTXaAYn2GtjffCabjzbcVhCK23mTNRF7OxEZCL%2FIsWcXdCbzAHqGGJQwbyYKQXTOVUNmOTroFVh4s8sW56cMo6Ae7UrvloCJBXMMw80Gbkwxxxl8b7z3r3rXef7BVd7Z%2FBKZAW0xUCSsUb89HRA%2BaQIGtfQ%2FKq4pzOWRf2NXM7EPQUMAYeopj4tOGDAt2IvPlHOaWrTyTyUhNL2RM2dOamGRNRmwsh3pIb%2BzCY5oO9BjqkASejPy1gv8xjwICnaZCrCJAp6ziVWvkz%2FeZGvia8TtCt8o073Fq7PKB9YPdb1yZFPGytF9g71CmcqPClNDfwpwo6r0Pex4Zg%2BUfOSve3SkHx8lcToeXle%2FmrUU9f%2BX3w0jPgl6d6MV1rRDq1vq01YR3qCJdwezDE0kmuCelnRkNRYYALbW%2FkWuOx5ai6ZNvUoCAHIa60q5welX%2BhoIUCuLfP4B7s&X-Amz-Signature=541845eb8967eeaef0fe5fabc5c5caa886f1ec3bb6aad7a44a0c09baae42de95&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVWLRIQQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCTy7eNDS8grtYrrA7KwzQjjoiTgSgixFGHxX1bcoT%2B6wIhAIrZY2eU7nqrrUmcPB5SEF0Pzg5r56gJ0gHcASTJtw%2B7Kv8DCBoQABoMNjM3NDIzMTgzODA1Igyh7X2n1E0RmoHRHj4q3ANNL5nyM7pQqzflg2myWWN5ltKUBwks7gXiKUB%2BJiGTO7fgrBMsR9WBR1WI9%2Bmmw4IH2rbl5i7HtCiCcJvJLk9JMs7KFS515J1Ytrc4re6LTfNpJrXcHRq%2FKtup%2F4L5lDRo9ObxHq1ebVVXsUbyUHj7Y7SxV1L1eyF0hplkD7MLshg%2BoTXzRJUN4wdN9%2BEWrgJ6tyyWF8Zjd19ECcNMFusD59Ofh6H24X%2FPOeqgg3qHjb5sRG4FLx8DcPUaB9GLY4T9b2SIT1zqaX0dfVO7yc%2Bz%2BEO9QD2r1hEAc%2B8tPCgHkjyWDnItKip1e2BwTc1iSM7XKlglMePDoLnhhMyGiGdAzfNKSVgWu%2BEN5SFz3I3C4u2YZpaCRh9bdXQItN%2Fg9nhRLDZKlZVVIWXjGizbyIBPkPaTXaAYn2GtjffCabjzbcVhCK23mTNRF7OxEZCL%2FIsWcXdCbzAHqGGJQwbyYKQXTOVUNmOTroFVh4s8sW56cMo6Ae7UrvloCJBXMMw80Gbkwxxxl8b7z3r3rXef7BVd7Z%2FBKZAW0xUCSsUb89HRA%2BaQIGtfQ%2FKq4pzOWRf2NXM7EPQUMAYeopj4tOGDAt2IvPlHOaWrTyTyUhNL2RM2dOamGRNRmwsh3pIb%2BzCY5oO9BjqkASejPy1gv8xjwICnaZCrCJAp6ziVWvkz%2FeZGvia8TtCt8o073Fq7PKB9YPdb1yZFPGytF9g71CmcqPClNDfwpwo6r0Pex4Zg%2BUfOSve3SkHx8lcToeXle%2FmrUU9f%2BX3w0jPgl6d6MV1rRDq1vq01YR3qCJdwezDE0kmuCelnRkNRYYALbW%2FkWuOx5ai6ZNvUoCAHIa60q5welX%2BhoIUCuLfP4B7s&X-Amz-Signature=892459b53f172be12409c29c4e3111c2c2cb86f0a666d78a97032f4c85f9ee8f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVWLRIQQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCTy7eNDS8grtYrrA7KwzQjjoiTgSgixFGHxX1bcoT%2B6wIhAIrZY2eU7nqrrUmcPB5SEF0Pzg5r56gJ0gHcASTJtw%2B7Kv8DCBoQABoMNjM3NDIzMTgzODA1Igyh7X2n1E0RmoHRHj4q3ANNL5nyM7pQqzflg2myWWN5ltKUBwks7gXiKUB%2BJiGTO7fgrBMsR9WBR1WI9%2Bmmw4IH2rbl5i7HtCiCcJvJLk9JMs7KFS515J1Ytrc4re6LTfNpJrXcHRq%2FKtup%2F4L5lDRo9ObxHq1ebVVXsUbyUHj7Y7SxV1L1eyF0hplkD7MLshg%2BoTXzRJUN4wdN9%2BEWrgJ6tyyWF8Zjd19ECcNMFusD59Ofh6H24X%2FPOeqgg3qHjb5sRG4FLx8DcPUaB9GLY4T9b2SIT1zqaX0dfVO7yc%2Bz%2BEO9QD2r1hEAc%2B8tPCgHkjyWDnItKip1e2BwTc1iSM7XKlglMePDoLnhhMyGiGdAzfNKSVgWu%2BEN5SFz3I3C4u2YZpaCRh9bdXQItN%2Fg9nhRLDZKlZVVIWXjGizbyIBPkPaTXaAYn2GtjffCabjzbcVhCK23mTNRF7OxEZCL%2FIsWcXdCbzAHqGGJQwbyYKQXTOVUNmOTroFVh4s8sW56cMo6Ae7UrvloCJBXMMw80Gbkwxxxl8b7z3r3rXef7BVd7Z%2FBKZAW0xUCSsUb89HRA%2BaQIGtfQ%2FKq4pzOWRf2NXM7EPQUMAYeopj4tOGDAt2IvPlHOaWrTyTyUhNL2RM2dOamGRNRmwsh3pIb%2BzCY5oO9BjqkASejPy1gv8xjwICnaZCrCJAp6ziVWvkz%2FeZGvia8TtCt8o073Fq7PKB9YPdb1yZFPGytF9g71CmcqPClNDfwpwo6r0Pex4Zg%2BUfOSve3SkHx8lcToeXle%2FmrUU9f%2BX3w0jPgl6d6MV1rRDq1vq01YR3qCJdwezDE0kmuCelnRkNRYYALbW%2FkWuOx5ai6ZNvUoCAHIa60q5welX%2BhoIUCuLfP4B7s&X-Amz-Signature=085deaf2b0f01f937db55684f7a914cb5a5d99cded46005ebb9c987445747609&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVWLRIQQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCTy7eNDS8grtYrrA7KwzQjjoiTgSgixFGHxX1bcoT%2B6wIhAIrZY2eU7nqrrUmcPB5SEF0Pzg5r56gJ0gHcASTJtw%2B7Kv8DCBoQABoMNjM3NDIzMTgzODA1Igyh7X2n1E0RmoHRHj4q3ANNL5nyM7pQqzflg2myWWN5ltKUBwks7gXiKUB%2BJiGTO7fgrBMsR9WBR1WI9%2Bmmw4IH2rbl5i7HtCiCcJvJLk9JMs7KFS515J1Ytrc4re6LTfNpJrXcHRq%2FKtup%2F4L5lDRo9ObxHq1ebVVXsUbyUHj7Y7SxV1L1eyF0hplkD7MLshg%2BoTXzRJUN4wdN9%2BEWrgJ6tyyWF8Zjd19ECcNMFusD59Ofh6H24X%2FPOeqgg3qHjb5sRG4FLx8DcPUaB9GLY4T9b2SIT1zqaX0dfVO7yc%2Bz%2BEO9QD2r1hEAc%2B8tPCgHkjyWDnItKip1e2BwTc1iSM7XKlglMePDoLnhhMyGiGdAzfNKSVgWu%2BEN5SFz3I3C4u2YZpaCRh9bdXQItN%2Fg9nhRLDZKlZVVIWXjGizbyIBPkPaTXaAYn2GtjffCabjzbcVhCK23mTNRF7OxEZCL%2FIsWcXdCbzAHqGGJQwbyYKQXTOVUNmOTroFVh4s8sW56cMo6Ae7UrvloCJBXMMw80Gbkwxxxl8b7z3r3rXef7BVd7Z%2FBKZAW0xUCSsUb89HRA%2BaQIGtfQ%2FKq4pzOWRf2NXM7EPQUMAYeopj4tOGDAt2IvPlHOaWrTyTyUhNL2RM2dOamGRNRmwsh3pIb%2BzCY5oO9BjqkASejPy1gv8xjwICnaZCrCJAp6ziVWvkz%2FeZGvia8TtCt8o073Fq7PKB9YPdb1yZFPGytF9g71CmcqPClNDfwpwo6r0Pex4Zg%2BUfOSve3SkHx8lcToeXle%2FmrUU9f%2BX3w0jPgl6d6MV1rRDq1vq01YR3qCJdwezDE0kmuCelnRkNRYYALbW%2FkWuOx5ai6ZNvUoCAHIa60q5welX%2BhoIUCuLfP4B7s&X-Amz-Signature=298fbc865109fd3c713d2523cf09348a34984e21a8b1d3722f5b27d556ff6602&X-Amz-SignedHeaders=host&x-id=GetObject)
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


