

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBQHQYYY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBYOGUKQHbjDcySi4rojNxvBLWnGurOL%2F%2BAHlcujsuLrAiBLwmUcXR16p%2BT5rc7Fa2ucB3FRw2wyVhsxlK6s4wx7HCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTwLNV2O4dkwNLKOMKtwDqHGbWylMKBO%2BxHKyKQvpqQWaT8w8Pv4LPUc0TMNS5BIHJhabICVDZRpMfJhI7T4JhYgXkRt82wqSFUXwUBjQAz0SObkypAKUCOFijEy9QWnTgLiOnseCeFIAfmZZc7qbn5QBLOUZBwPIOTiv8VtfLE3vYkxc1997wm56HWSVWIjAejwsygkpk5Wt%2BJllcBTr4t9otvFG%2BfjLAqCKzNQIcDL%2FYpy1WB5CxNA%2FsIE%2FqZrUYbdiyWZjLf7IuCzUvk5MeBiKx83Ucya9EEpetKJUrN2qdYhJAdxXM83DuY56ikAbfEwhZiwZW5QKTXE8ySPVY%2BazsU6%2F4fGyXeyuWUg6df8nR%2BM%2F8xdstsEn8JCytMRohQdz3L6uoz4%2Bii9yZfBhV7vvLOAGR1HXB8%2BAZ6DqyPIU2c57CVLdl54t2l4dyaoAAX5pgSvQ9bNhlvDx8IxipUuj5w6T8xUJS%2FSx89uNLSvQ4Uypp00jkgVhEuPht0E4uesUo%2FkNn2rBl0R3owStJ0yVODxD5XDa5q0ofU3BVBRLTBbHQSOaDkFxOhY50HV05GPizaGCj9v4fgcdFC9pL8bpIGhTkXxBnYAkW2lCfswleuGPsL9iTj5HJM2PaiTPcRiOpY6mGsktvDYww%2Fj0vAY6pgE88o9NN6ZwkZKutbij1YofXYhipK4uAu0Kpv9OVaRarhkVLCs9TqcVtFGu32n8WwwBs0oOeWUqPR1nEk6ByivzRMDUzWmNX9AKNGXt9gcjOVWyvFPQrE4gwyEi0CmOfLx2D4sgchS8bAIudX7HewfUJgN1QkhynCad0fBOsay61WSeSkzjMcQPnFQSI2WeodczX4%2FJux7zB4zQRTPTxuf8ED3vp6oy&X-Amz-Signature=2ed8fed4c48c058abc3a7a2ea5ddea6900e7b7332f09e841387547dbb1be435c&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZGTOMB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4rXkm6bdy8GiSbBm%2FzJfnzENYK3tTAVWWUVSnJRIVQAiEA6j6p60a0OnHGiIcPOu5nwYcMJaLdIXvrTkdAObiRkJsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBwreU4MzPUQXjmoCrcA3tmOLyf0sHmUIFjSCCJ1F2EYXgB6OV92MwVo2RmsGhkF7V7a0ZXer64zu55Wbb4qyGgOV1Kba9AlXxRJVM87og1SGcersLbjAT2cHCmc%2BUuE7djubcTfCBDMB%2FuJatq8zwMBI%2BNyh9jwjhr60OeRyedajZXZ4Uukgoy1ixzRs2cVCRPbWLGoemgIMUkJFkFwhLI7WzcruzZhIWqmqS7Ub3Ys9LIhtcmeq77rStC8qWotulLvrRj7xD%2FpnANCbW7lbESGy7uxKai5J0%2B0P63NIP92myZK8AmZGLHW74MUYx6oLiTpzg57v1M8Al1HQUmZkkAhfGyJyiUnN4iX8iXRz8nBd%2BPUPOnliBVPS6vT21SFGzPGmGUhPHHiEpNiFJVy6VWmRTDVjUo0wauL5bDjIpeDIcxx2Tnmh0joriUVvqt0pIhUsuxoq6VZPUzATfRXpAFFXfo%2BiP%2F2Y2Pqkoy851r5oGrCGMjuy8Y5PUrSRWfzPH%2BY48d4sQlu6XkMtkjzRCXCE4bEUCPvKa1hcGHU5oLC0wtdRbCcGwprepou4ey2zR0tyctwRyyQetQUMrREhl2MZBfL3i6ubwQ%2BBA%2Fchwib2xGX10uVzms9bZTZkZZVFbgVSZL%2Bhv8k8zcMJH49LwGOqUBSVRnsfLCgtRMBajgyg8nrFX4iNsVDnfuclWc1smWbigSbc5lrvVyeuzcK7oN0PfMQXN1Hr8GVEM31mBK7T212rPxvpQaWQs%2B9ipN1uDjSBDnMZY%2FXJyUveRJMP1jQujlIFxGRhOcAAetsdcVq%2FiWjXi9rOkULoqrwg%2F%2Fmskc4Rb7eEEJehg97%2FCU846UO7sz8YSgmxaU1bbCyiIFL6Cjk1EdG2X%2B&X-Amz-Signature=3f1996a671b6f9aeea01d02ffe3da69b8251c62b81945db5ddd02c8fd4992b75&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZGTOMB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4rXkm6bdy8GiSbBm%2FzJfnzENYK3tTAVWWUVSnJRIVQAiEA6j6p60a0OnHGiIcPOu5nwYcMJaLdIXvrTkdAObiRkJsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBwreU4MzPUQXjmoCrcA3tmOLyf0sHmUIFjSCCJ1F2EYXgB6OV92MwVo2RmsGhkF7V7a0ZXer64zu55Wbb4qyGgOV1Kba9AlXxRJVM87og1SGcersLbjAT2cHCmc%2BUuE7djubcTfCBDMB%2FuJatq8zwMBI%2BNyh9jwjhr60OeRyedajZXZ4Uukgoy1ixzRs2cVCRPbWLGoemgIMUkJFkFwhLI7WzcruzZhIWqmqS7Ub3Ys9LIhtcmeq77rStC8qWotulLvrRj7xD%2FpnANCbW7lbESGy7uxKai5J0%2B0P63NIP92myZK8AmZGLHW74MUYx6oLiTpzg57v1M8Al1HQUmZkkAhfGyJyiUnN4iX8iXRz8nBd%2BPUPOnliBVPS6vT21SFGzPGmGUhPHHiEpNiFJVy6VWmRTDVjUo0wauL5bDjIpeDIcxx2Tnmh0joriUVvqt0pIhUsuxoq6VZPUzATfRXpAFFXfo%2BiP%2F2Y2Pqkoy851r5oGrCGMjuy8Y5PUrSRWfzPH%2BY48d4sQlu6XkMtkjzRCXCE4bEUCPvKa1hcGHU5oLC0wtdRbCcGwprepou4ey2zR0tyctwRyyQetQUMrREhl2MZBfL3i6ubwQ%2BBA%2Fchwib2xGX10uVzms9bZTZkZZVFbgVSZL%2Bhv8k8zcMJH49LwGOqUBSVRnsfLCgtRMBajgyg8nrFX4iNsVDnfuclWc1smWbigSbc5lrvVyeuzcK7oN0PfMQXN1Hr8GVEM31mBK7T212rPxvpQaWQs%2B9ipN1uDjSBDnMZY%2FXJyUveRJMP1jQujlIFxGRhOcAAetsdcVq%2FiWjXi9rOkULoqrwg%2F%2Fmskc4Rb7eEEJehg97%2FCU846UO7sz8YSgmxaU1bbCyiIFL6Cjk1EdG2X%2B&X-Amz-Signature=be00993281cb0447c95530573cc844143187e7056ef1de10521e27eafd20e33b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZGTOMB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4rXkm6bdy8GiSbBm%2FzJfnzENYK3tTAVWWUVSnJRIVQAiEA6j6p60a0OnHGiIcPOu5nwYcMJaLdIXvrTkdAObiRkJsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBwreU4MzPUQXjmoCrcA3tmOLyf0sHmUIFjSCCJ1F2EYXgB6OV92MwVo2RmsGhkF7V7a0ZXer64zu55Wbb4qyGgOV1Kba9AlXxRJVM87og1SGcersLbjAT2cHCmc%2BUuE7djubcTfCBDMB%2FuJatq8zwMBI%2BNyh9jwjhr60OeRyedajZXZ4Uukgoy1ixzRs2cVCRPbWLGoemgIMUkJFkFwhLI7WzcruzZhIWqmqS7Ub3Ys9LIhtcmeq77rStC8qWotulLvrRj7xD%2FpnANCbW7lbESGy7uxKai5J0%2B0P63NIP92myZK8AmZGLHW74MUYx6oLiTpzg57v1M8Al1HQUmZkkAhfGyJyiUnN4iX8iXRz8nBd%2BPUPOnliBVPS6vT21SFGzPGmGUhPHHiEpNiFJVy6VWmRTDVjUo0wauL5bDjIpeDIcxx2Tnmh0joriUVvqt0pIhUsuxoq6VZPUzATfRXpAFFXfo%2BiP%2F2Y2Pqkoy851r5oGrCGMjuy8Y5PUrSRWfzPH%2BY48d4sQlu6XkMtkjzRCXCE4bEUCPvKa1hcGHU5oLC0wtdRbCcGwprepou4ey2zR0tyctwRyyQetQUMrREhl2MZBfL3i6ubwQ%2BBA%2Fchwib2xGX10uVzms9bZTZkZZVFbgVSZL%2Bhv8k8zcMJH49LwGOqUBSVRnsfLCgtRMBajgyg8nrFX4iNsVDnfuclWc1smWbigSbc5lrvVyeuzcK7oN0PfMQXN1Hr8GVEM31mBK7T212rPxvpQaWQs%2B9ipN1uDjSBDnMZY%2FXJyUveRJMP1jQujlIFxGRhOcAAetsdcVq%2FiWjXi9rOkULoqrwg%2F%2Fmskc4Rb7eEEJehg97%2FCU846UO7sz8YSgmxaU1bbCyiIFL6Cjk1EdG2X%2B&X-Amz-Signature=6885dedc04b666001140faa68a9b3ed27f57510bf149d42bd6f6cd73d995619a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZGTOMB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4rXkm6bdy8GiSbBm%2FzJfnzENYK3tTAVWWUVSnJRIVQAiEA6j6p60a0OnHGiIcPOu5nwYcMJaLdIXvrTkdAObiRkJsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBwreU4MzPUQXjmoCrcA3tmOLyf0sHmUIFjSCCJ1F2EYXgB6OV92MwVo2RmsGhkF7V7a0ZXer64zu55Wbb4qyGgOV1Kba9AlXxRJVM87og1SGcersLbjAT2cHCmc%2BUuE7djubcTfCBDMB%2FuJatq8zwMBI%2BNyh9jwjhr60OeRyedajZXZ4Uukgoy1ixzRs2cVCRPbWLGoemgIMUkJFkFwhLI7WzcruzZhIWqmqS7Ub3Ys9LIhtcmeq77rStC8qWotulLvrRj7xD%2FpnANCbW7lbESGy7uxKai5J0%2B0P63NIP92myZK8AmZGLHW74MUYx6oLiTpzg57v1M8Al1HQUmZkkAhfGyJyiUnN4iX8iXRz8nBd%2BPUPOnliBVPS6vT21SFGzPGmGUhPHHiEpNiFJVy6VWmRTDVjUo0wauL5bDjIpeDIcxx2Tnmh0joriUVvqt0pIhUsuxoq6VZPUzATfRXpAFFXfo%2BiP%2F2Y2Pqkoy851r5oGrCGMjuy8Y5PUrSRWfzPH%2BY48d4sQlu6XkMtkjzRCXCE4bEUCPvKa1hcGHU5oLC0wtdRbCcGwprepou4ey2zR0tyctwRyyQetQUMrREhl2MZBfL3i6ubwQ%2BBA%2Fchwib2xGX10uVzms9bZTZkZZVFbgVSZL%2Bhv8k8zcMJH49LwGOqUBSVRnsfLCgtRMBajgyg8nrFX4iNsVDnfuclWc1smWbigSbc5lrvVyeuzcK7oN0PfMQXN1Hr8GVEM31mBK7T212rPxvpQaWQs%2B9ipN1uDjSBDnMZY%2FXJyUveRJMP1jQujlIFxGRhOcAAetsdcVq%2FiWjXi9rOkULoqrwg%2F%2Fmskc4Rb7eEEJehg97%2FCU846UO7sz8YSgmxaU1bbCyiIFL6Cjk1EdG2X%2B&X-Amz-Signature=2c073f7722ea8dfb38083a99c5a8d793238c051c104243d6873c878d677a1318&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZGTOMB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4rXkm6bdy8GiSbBm%2FzJfnzENYK3tTAVWWUVSnJRIVQAiEA6j6p60a0OnHGiIcPOu5nwYcMJaLdIXvrTkdAObiRkJsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBwreU4MzPUQXjmoCrcA3tmOLyf0sHmUIFjSCCJ1F2EYXgB6OV92MwVo2RmsGhkF7V7a0ZXer64zu55Wbb4qyGgOV1Kba9AlXxRJVM87og1SGcersLbjAT2cHCmc%2BUuE7djubcTfCBDMB%2FuJatq8zwMBI%2BNyh9jwjhr60OeRyedajZXZ4Uukgoy1ixzRs2cVCRPbWLGoemgIMUkJFkFwhLI7WzcruzZhIWqmqS7Ub3Ys9LIhtcmeq77rStC8qWotulLvrRj7xD%2FpnANCbW7lbESGy7uxKai5J0%2B0P63NIP92myZK8AmZGLHW74MUYx6oLiTpzg57v1M8Al1HQUmZkkAhfGyJyiUnN4iX8iXRz8nBd%2BPUPOnliBVPS6vT21SFGzPGmGUhPHHiEpNiFJVy6VWmRTDVjUo0wauL5bDjIpeDIcxx2Tnmh0joriUVvqt0pIhUsuxoq6VZPUzATfRXpAFFXfo%2BiP%2F2Y2Pqkoy851r5oGrCGMjuy8Y5PUrSRWfzPH%2BY48d4sQlu6XkMtkjzRCXCE4bEUCPvKa1hcGHU5oLC0wtdRbCcGwprepou4ey2zR0tyctwRyyQetQUMrREhl2MZBfL3i6ubwQ%2BBA%2Fchwib2xGX10uVzms9bZTZkZZVFbgVSZL%2Bhv8k8zcMJH49LwGOqUBSVRnsfLCgtRMBajgyg8nrFX4iNsVDnfuclWc1smWbigSbc5lrvVyeuzcK7oN0PfMQXN1Hr8GVEM31mBK7T212rPxvpQaWQs%2B9ipN1uDjSBDnMZY%2FXJyUveRJMP1jQujlIFxGRhOcAAetsdcVq%2FiWjXi9rOkULoqrwg%2F%2Fmskc4Rb7eEEJehg97%2FCU846UO7sz8YSgmxaU1bbCyiIFL6Cjk1EdG2X%2B&X-Amz-Signature=a732078c5c2abcb284e10ee9b02c65249defda0d04c0f78c5c2855ed352425be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBQHQYYY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBYOGUKQHbjDcySi4rojNxvBLWnGurOL%2F%2BAHlcujsuLrAiBLwmUcXR16p%2BT5rc7Fa2ucB3FRw2wyVhsxlK6s4wx7HCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTwLNV2O4dkwNLKOMKtwDqHGbWylMKBO%2BxHKyKQvpqQWaT8w8Pv4LPUc0TMNS5BIHJhabICVDZRpMfJhI7T4JhYgXkRt82wqSFUXwUBjQAz0SObkypAKUCOFijEy9QWnTgLiOnseCeFIAfmZZc7qbn5QBLOUZBwPIOTiv8VtfLE3vYkxc1997wm56HWSVWIjAejwsygkpk5Wt%2BJllcBTr4t9otvFG%2BfjLAqCKzNQIcDL%2FYpy1WB5CxNA%2FsIE%2FqZrUYbdiyWZjLf7IuCzUvk5MeBiKx83Ucya9EEpetKJUrN2qdYhJAdxXM83DuY56ikAbfEwhZiwZW5QKTXE8ySPVY%2BazsU6%2F4fGyXeyuWUg6df8nR%2BM%2F8xdstsEn8JCytMRohQdz3L6uoz4%2Bii9yZfBhV7vvLOAGR1HXB8%2BAZ6DqyPIU2c57CVLdl54t2l4dyaoAAX5pgSvQ9bNhlvDx8IxipUuj5w6T8xUJS%2FSx89uNLSvQ4Uypp00jkgVhEuPht0E4uesUo%2FkNn2rBl0R3owStJ0yVODxD5XDa5q0ofU3BVBRLTBbHQSOaDkFxOhY50HV05GPizaGCj9v4fgcdFC9pL8bpIGhTkXxBnYAkW2lCfswleuGPsL9iTj5HJM2PaiTPcRiOpY6mGsktvDYww%2Fj0vAY6pgE88o9NN6ZwkZKutbij1YofXYhipK4uAu0Kpv9OVaRarhkVLCs9TqcVtFGu32n8WwwBs0oOeWUqPR1nEk6ByivzRMDUzWmNX9AKNGXt9gcjOVWyvFPQrE4gwyEi0CmOfLx2D4sgchS8bAIudX7HewfUJgN1QkhynCad0fBOsay61WSeSkzjMcQPnFQSI2WeodczX4%2FJux7zB4zQRTPTxuf8ED3vp6oy&X-Amz-Signature=4d39f5c2a7e947d201cc1336da2c10296fd562b7fc08de870a03199ffd09350f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBQHQYYY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBYOGUKQHbjDcySi4rojNxvBLWnGurOL%2F%2BAHlcujsuLrAiBLwmUcXR16p%2BT5rc7Fa2ucB3FRw2wyVhsxlK6s4wx7HCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTwLNV2O4dkwNLKOMKtwDqHGbWylMKBO%2BxHKyKQvpqQWaT8w8Pv4LPUc0TMNS5BIHJhabICVDZRpMfJhI7T4JhYgXkRt82wqSFUXwUBjQAz0SObkypAKUCOFijEy9QWnTgLiOnseCeFIAfmZZc7qbn5QBLOUZBwPIOTiv8VtfLE3vYkxc1997wm56HWSVWIjAejwsygkpk5Wt%2BJllcBTr4t9otvFG%2BfjLAqCKzNQIcDL%2FYpy1WB5CxNA%2FsIE%2FqZrUYbdiyWZjLf7IuCzUvk5MeBiKx83Ucya9EEpetKJUrN2qdYhJAdxXM83DuY56ikAbfEwhZiwZW5QKTXE8ySPVY%2BazsU6%2F4fGyXeyuWUg6df8nR%2BM%2F8xdstsEn8JCytMRohQdz3L6uoz4%2Bii9yZfBhV7vvLOAGR1HXB8%2BAZ6DqyPIU2c57CVLdl54t2l4dyaoAAX5pgSvQ9bNhlvDx8IxipUuj5w6T8xUJS%2FSx89uNLSvQ4Uypp00jkgVhEuPht0E4uesUo%2FkNn2rBl0R3owStJ0yVODxD5XDa5q0ofU3BVBRLTBbHQSOaDkFxOhY50HV05GPizaGCj9v4fgcdFC9pL8bpIGhTkXxBnYAkW2lCfswleuGPsL9iTj5HJM2PaiTPcRiOpY6mGsktvDYww%2Fj0vAY6pgE88o9NN6ZwkZKutbij1YofXYhipK4uAu0Kpv9OVaRarhkVLCs9TqcVtFGu32n8WwwBs0oOeWUqPR1nEk6ByivzRMDUzWmNX9AKNGXt9gcjOVWyvFPQrE4gwyEi0CmOfLx2D4sgchS8bAIudX7HewfUJgN1QkhynCad0fBOsay61WSeSkzjMcQPnFQSI2WeodczX4%2FJux7zB4zQRTPTxuf8ED3vp6oy&X-Amz-Signature=bea77512b36db2c74b9b16873bca56a08eb4b931dfdeceebf2e63465c8f5529e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBQHQYYY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBYOGUKQHbjDcySi4rojNxvBLWnGurOL%2F%2BAHlcujsuLrAiBLwmUcXR16p%2BT5rc7Fa2ucB3FRw2wyVhsxlK6s4wx7HCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTwLNV2O4dkwNLKOMKtwDqHGbWylMKBO%2BxHKyKQvpqQWaT8w8Pv4LPUc0TMNS5BIHJhabICVDZRpMfJhI7T4JhYgXkRt82wqSFUXwUBjQAz0SObkypAKUCOFijEy9QWnTgLiOnseCeFIAfmZZc7qbn5QBLOUZBwPIOTiv8VtfLE3vYkxc1997wm56HWSVWIjAejwsygkpk5Wt%2BJllcBTr4t9otvFG%2BfjLAqCKzNQIcDL%2FYpy1WB5CxNA%2FsIE%2FqZrUYbdiyWZjLf7IuCzUvk5MeBiKx83Ucya9EEpetKJUrN2qdYhJAdxXM83DuY56ikAbfEwhZiwZW5QKTXE8ySPVY%2BazsU6%2F4fGyXeyuWUg6df8nR%2BM%2F8xdstsEn8JCytMRohQdz3L6uoz4%2Bii9yZfBhV7vvLOAGR1HXB8%2BAZ6DqyPIU2c57CVLdl54t2l4dyaoAAX5pgSvQ9bNhlvDx8IxipUuj5w6T8xUJS%2FSx89uNLSvQ4Uypp00jkgVhEuPht0E4uesUo%2FkNn2rBl0R3owStJ0yVODxD5XDa5q0ofU3BVBRLTBbHQSOaDkFxOhY50HV05GPizaGCj9v4fgcdFC9pL8bpIGhTkXxBnYAkW2lCfswleuGPsL9iTj5HJM2PaiTPcRiOpY6mGsktvDYww%2Fj0vAY6pgE88o9NN6ZwkZKutbij1YofXYhipK4uAu0Kpv9OVaRarhkVLCs9TqcVtFGu32n8WwwBs0oOeWUqPR1nEk6ByivzRMDUzWmNX9AKNGXt9gcjOVWyvFPQrE4gwyEi0CmOfLx2D4sgchS8bAIudX7HewfUJgN1QkhynCad0fBOsay61WSeSkzjMcQPnFQSI2WeodczX4%2FJux7zB4zQRTPTxuf8ED3vp6oy&X-Amz-Signature=2cce7a402ed6ec7780da5f467534e4018b1e3050c8e1f13ab53e6f0ab838feca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBQHQYYY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBYOGUKQHbjDcySi4rojNxvBLWnGurOL%2F%2BAHlcujsuLrAiBLwmUcXR16p%2BT5rc7Fa2ucB3FRw2wyVhsxlK6s4wx7HCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTwLNV2O4dkwNLKOMKtwDqHGbWylMKBO%2BxHKyKQvpqQWaT8w8Pv4LPUc0TMNS5BIHJhabICVDZRpMfJhI7T4JhYgXkRt82wqSFUXwUBjQAz0SObkypAKUCOFijEy9QWnTgLiOnseCeFIAfmZZc7qbn5QBLOUZBwPIOTiv8VtfLE3vYkxc1997wm56HWSVWIjAejwsygkpk5Wt%2BJllcBTr4t9otvFG%2BfjLAqCKzNQIcDL%2FYpy1WB5CxNA%2FsIE%2FqZrUYbdiyWZjLf7IuCzUvk5MeBiKx83Ucya9EEpetKJUrN2qdYhJAdxXM83DuY56ikAbfEwhZiwZW5QKTXE8ySPVY%2BazsU6%2F4fGyXeyuWUg6df8nR%2BM%2F8xdstsEn8JCytMRohQdz3L6uoz4%2Bii9yZfBhV7vvLOAGR1HXB8%2BAZ6DqyPIU2c57CVLdl54t2l4dyaoAAX5pgSvQ9bNhlvDx8IxipUuj5w6T8xUJS%2FSx89uNLSvQ4Uypp00jkgVhEuPht0E4uesUo%2FkNn2rBl0R3owStJ0yVODxD5XDa5q0ofU3BVBRLTBbHQSOaDkFxOhY50HV05GPizaGCj9v4fgcdFC9pL8bpIGhTkXxBnYAkW2lCfswleuGPsL9iTj5HJM2PaiTPcRiOpY6mGsktvDYww%2Fj0vAY6pgE88o9NN6ZwkZKutbij1YofXYhipK4uAu0Kpv9OVaRarhkVLCs9TqcVtFGu32n8WwwBs0oOeWUqPR1nEk6ByivzRMDUzWmNX9AKNGXt9gcjOVWyvFPQrE4gwyEi0CmOfLx2D4sgchS8bAIudX7HewfUJgN1QkhynCad0fBOsay61WSeSkzjMcQPnFQSI2WeodczX4%2FJux7zB4zQRTPTxuf8ED3vp6oy&X-Amz-Signature=982b8afb608a89abf56bc328dad70a88a949685c74c9eb634180a3706e52fc9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBQHQYYY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBYOGUKQHbjDcySi4rojNxvBLWnGurOL%2F%2BAHlcujsuLrAiBLwmUcXR16p%2BT5rc7Fa2ucB3FRw2wyVhsxlK6s4wx7HCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTwLNV2O4dkwNLKOMKtwDqHGbWylMKBO%2BxHKyKQvpqQWaT8w8Pv4LPUc0TMNS5BIHJhabICVDZRpMfJhI7T4JhYgXkRt82wqSFUXwUBjQAz0SObkypAKUCOFijEy9QWnTgLiOnseCeFIAfmZZc7qbn5QBLOUZBwPIOTiv8VtfLE3vYkxc1997wm56HWSVWIjAejwsygkpk5Wt%2BJllcBTr4t9otvFG%2BfjLAqCKzNQIcDL%2FYpy1WB5CxNA%2FsIE%2FqZrUYbdiyWZjLf7IuCzUvk5MeBiKx83Ucya9EEpetKJUrN2qdYhJAdxXM83DuY56ikAbfEwhZiwZW5QKTXE8ySPVY%2BazsU6%2F4fGyXeyuWUg6df8nR%2BM%2F8xdstsEn8JCytMRohQdz3L6uoz4%2Bii9yZfBhV7vvLOAGR1HXB8%2BAZ6DqyPIU2c57CVLdl54t2l4dyaoAAX5pgSvQ9bNhlvDx8IxipUuj5w6T8xUJS%2FSx89uNLSvQ4Uypp00jkgVhEuPht0E4uesUo%2FkNn2rBl0R3owStJ0yVODxD5XDa5q0ofU3BVBRLTBbHQSOaDkFxOhY50HV05GPizaGCj9v4fgcdFC9pL8bpIGhTkXxBnYAkW2lCfswleuGPsL9iTj5HJM2PaiTPcRiOpY6mGsktvDYww%2Fj0vAY6pgE88o9NN6ZwkZKutbij1YofXYhipK4uAu0Kpv9OVaRarhkVLCs9TqcVtFGu32n8WwwBs0oOeWUqPR1nEk6ByivzRMDUzWmNX9AKNGXt9gcjOVWyvFPQrE4gwyEi0CmOfLx2D4sgchS8bAIudX7HewfUJgN1QkhynCad0fBOsay61WSeSkzjMcQPnFQSI2WeodczX4%2FJux7zB4zQRTPTxuf8ED3vp6oy&X-Amz-Signature=6a180fd77fb87ece19729f32a0ee84f2ee67576095c28fe9dad352dd1af308f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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


