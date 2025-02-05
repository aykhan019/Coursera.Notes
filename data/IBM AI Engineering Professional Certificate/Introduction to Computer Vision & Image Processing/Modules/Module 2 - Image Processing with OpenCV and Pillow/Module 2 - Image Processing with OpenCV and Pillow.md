

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFI2LK3E%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCKmLNFNlxsdpsxKyqj3V2FyP4GtnFLsv8RtDFyPyTG5gIgOvFqmXCUxinq%2FO9V4uKlHA%2FaRR68DzFd%2BjZP5Q9UhJQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLg7AY6SArQsFSQWhCrcA8Dz1%2BfBWsncKYTfMcl612Y9C9fsDjJELgxz3rRoGCihYG1%2FRD%2BtBI9yEzYgbyHKamljjo6XmlljFL88hOXL8h%2FuZY%2BEGUSeJPmdszfMIgFc9PYcGTc%2BXkXjDAaXYaPDKUpdg6XAkbWj2NBRtzzAFjsHxedRrxM2Ct8ekrH35sH78U3sDHOWKJfwRS4XUX4gH%2ByBdbPcM5yK9%2FNisaNc3VCGBRHqhn9wyZRnOzHxfOxMBu8ns8njckHnw1fjK6z%2F65HJIz%2FyXoqcTtMJiwOdVkg4wIdV7OWTpWt6d%2FbUQ5MoogUhTKGnQ1MTNRBM4UvZ1LttuLiiUHia0QCUv4L9tuLejz3YOTZ7mImn4zF6K0euy2UaI7lyMD21W2Es%2FJRSKn8GLMGlBut4AIv3SV%2FmiAxs6T1eRUG83aMQsuVXr7XNei1OIrr0OLwkvaRgtS1RUYcNQ2uf9zB8Q5PaE%2BhlC24DkKmopRBVwkV6HMH1y57aTrgCABL%2BH90oFRnp9lLBWbEnBgsoBybcLZ1%2FvZ1fnT%2Fn0kkEhVvax5WHqgODEuzA2FAjIwvS3iSRY3XhqCumE4ItCoU5nsFTM1FFc0usTrSEB1ksBJkHtIMehJYqvEDIpDxg%2BRH3iwqMQ1IHMMG6jr0GOqUBW78gnCKOxLTeTnSxE0tdUH4MRShyzhiX2mLGxpiMNbawk7q%2Fkx2h0FQAok8iHqG9C6LQyS0CpIVxTsA8TZWcraCyTskoi5FApkMwhZNzpx3P1drhCD0gvYtzAYt%2BTK5VobahI7PnckV4kDcGUb4vFFOm0cApKt5kF0gUJdX4NCygfTzt9wIcfwzllv6UBFdd5JNbXuBXhGqE52gjo%2BF%2FODW2EJzu&X-Amz-Signature=2dd6793b3e650b0580ef5c7ef0f27c52e88f1d87e5e99cee55c54272a936f9ac&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7ZBZFB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDXEQoC1hKSjlBX0YBCKDlBzlIIjtEbU419SGN3IaG%2FwAiAXolU6GJ4KbBYbfHA3DidVa0Tvi66A93N6AzKKGBLxgSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM3nb5JA1hzFHCWC6zKtwDJZ6BG%2FidYvbkLBhd%2FQpl0v6Lc9WVA8rCjR1l7cPISSDV9dCdjX6dcrVpfU8OZZxoibuzA3Hb%2BIHbMB4CXQYaJFbzymSf5HjGeRxFBP3nBge4D0QWBzG%2BJMN67RjVAHrq9twLyMFsYci%2BgH749KbCJP2lB05mSXILuETdDWSk%2B6Ukp%2FwD5D1NmFcwNz9gTEHQ0x9fhH7pYbvMxZnEnvpfVCVgj7uGxQSMAOq3rSiBUe3eow9obEEEYrAPU%2F5UJMXEWCndVMGmvqsBr28Ml%2FpK09tKR883Bq75v0mhk2dBmKfn5TYFEt471%2B4qztVRV7K8SfIzVgVJoJmZupQNeZD5fs5I6gW3JiJhJ6KJbllKndlw52QgAuKfRubX0qsMJrArkrBlEzkOgghcnCQKfJQ%2FKXZBrNo7kR6zPDzH88OWJCm%2FWmUSJEZnar78%2B%2FOMS87ua6BWs6Vv1V5VIx2xWN7Oc7INUYON5pwIt0ZkaUhaR4nNUXbBih%2BSdlSvOaehvbvbDxi34%2B9u5nERgyJg2KbyQcgO1XEIQCLmgRyLRRFj6%2Fg55Fp2I67lzSyAZ3tdHu3XC9p4cdmo7%2FQYozgLsuuT3c4YWhVpbep6vR5b0mvCa%2Bpae1tiqQBYEo7lfRgwi7yOvQY6pgGXa0gLam3UfOKDzKJbfk4oKKlqiZkx6kss3AKfQZ3%2F%2BxvJk76POviIbgs1bjForjecs24QvgWwUNECzSknNkfLKMrrPot7ROzuPxMHEai3zmlyDufbK1rhbKxKRyHKalbV95Wjc1KXDgixzbQ7iqkJ%2B36z5pyIJySo%2FipL9BZefjGr2Nw%2FxGsaiBv9NRso5FGWViE%2BbF5lB9kRqYk2HVHnlUNUn2XS&X-Amz-Signature=878f325d612371c2438070c147a27f824001aa2b4721e5995da7cdfee59beb42&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7ZBZFB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDXEQoC1hKSjlBX0YBCKDlBzlIIjtEbU419SGN3IaG%2FwAiAXolU6GJ4KbBYbfHA3DidVa0Tvi66A93N6AzKKGBLxgSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM3nb5JA1hzFHCWC6zKtwDJZ6BG%2FidYvbkLBhd%2FQpl0v6Lc9WVA8rCjR1l7cPISSDV9dCdjX6dcrVpfU8OZZxoibuzA3Hb%2BIHbMB4CXQYaJFbzymSf5HjGeRxFBP3nBge4D0QWBzG%2BJMN67RjVAHrq9twLyMFsYci%2BgH749KbCJP2lB05mSXILuETdDWSk%2B6Ukp%2FwD5D1NmFcwNz9gTEHQ0x9fhH7pYbvMxZnEnvpfVCVgj7uGxQSMAOq3rSiBUe3eow9obEEEYrAPU%2F5UJMXEWCndVMGmvqsBr28Ml%2FpK09tKR883Bq75v0mhk2dBmKfn5TYFEt471%2B4qztVRV7K8SfIzVgVJoJmZupQNeZD5fs5I6gW3JiJhJ6KJbllKndlw52QgAuKfRubX0qsMJrArkrBlEzkOgghcnCQKfJQ%2FKXZBrNo7kR6zPDzH88OWJCm%2FWmUSJEZnar78%2B%2FOMS87ua6BWs6Vv1V5VIx2xWN7Oc7INUYON5pwIt0ZkaUhaR4nNUXbBih%2BSdlSvOaehvbvbDxi34%2B9u5nERgyJg2KbyQcgO1XEIQCLmgRyLRRFj6%2Fg55Fp2I67lzSyAZ3tdHu3XC9p4cdmo7%2FQYozgLsuuT3c4YWhVpbep6vR5b0mvCa%2Bpae1tiqQBYEo7lfRgwi7yOvQY6pgGXa0gLam3UfOKDzKJbfk4oKKlqiZkx6kss3AKfQZ3%2F%2BxvJk76POviIbgs1bjForjecs24QvgWwUNECzSknNkfLKMrrPot7ROzuPxMHEai3zmlyDufbK1rhbKxKRyHKalbV95Wjc1KXDgixzbQ7iqkJ%2B36z5pyIJySo%2FipL9BZefjGr2Nw%2FxGsaiBv9NRso5FGWViE%2BbF5lB9kRqYk2HVHnlUNUn2XS&X-Amz-Signature=da006479f7dcd8a9d170fdd5df2132a8fd3a948d074df2a2068bf2142a2e6c47&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7ZBZFB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDXEQoC1hKSjlBX0YBCKDlBzlIIjtEbU419SGN3IaG%2FwAiAXolU6GJ4KbBYbfHA3DidVa0Tvi66A93N6AzKKGBLxgSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM3nb5JA1hzFHCWC6zKtwDJZ6BG%2FidYvbkLBhd%2FQpl0v6Lc9WVA8rCjR1l7cPISSDV9dCdjX6dcrVpfU8OZZxoibuzA3Hb%2BIHbMB4CXQYaJFbzymSf5HjGeRxFBP3nBge4D0QWBzG%2BJMN67RjVAHrq9twLyMFsYci%2BgH749KbCJP2lB05mSXILuETdDWSk%2B6Ukp%2FwD5D1NmFcwNz9gTEHQ0x9fhH7pYbvMxZnEnvpfVCVgj7uGxQSMAOq3rSiBUe3eow9obEEEYrAPU%2F5UJMXEWCndVMGmvqsBr28Ml%2FpK09tKR883Bq75v0mhk2dBmKfn5TYFEt471%2B4qztVRV7K8SfIzVgVJoJmZupQNeZD5fs5I6gW3JiJhJ6KJbllKndlw52QgAuKfRubX0qsMJrArkrBlEzkOgghcnCQKfJQ%2FKXZBrNo7kR6zPDzH88OWJCm%2FWmUSJEZnar78%2B%2FOMS87ua6BWs6Vv1V5VIx2xWN7Oc7INUYON5pwIt0ZkaUhaR4nNUXbBih%2BSdlSvOaehvbvbDxi34%2B9u5nERgyJg2KbyQcgO1XEIQCLmgRyLRRFj6%2Fg55Fp2I67lzSyAZ3tdHu3XC9p4cdmo7%2FQYozgLsuuT3c4YWhVpbep6vR5b0mvCa%2Bpae1tiqQBYEo7lfRgwi7yOvQY6pgGXa0gLam3UfOKDzKJbfk4oKKlqiZkx6kss3AKfQZ3%2F%2BxvJk76POviIbgs1bjForjecs24QvgWwUNECzSknNkfLKMrrPot7ROzuPxMHEai3zmlyDufbK1rhbKxKRyHKalbV95Wjc1KXDgixzbQ7iqkJ%2B36z5pyIJySo%2FipL9BZefjGr2Nw%2FxGsaiBv9NRso5FGWViE%2BbF5lB9kRqYk2HVHnlUNUn2XS&X-Amz-Signature=edb8bbfa0103f87365e33980aad416f54a0586adbbdf0edf9680af6de5b6f730&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7ZBZFB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDXEQoC1hKSjlBX0YBCKDlBzlIIjtEbU419SGN3IaG%2FwAiAXolU6GJ4KbBYbfHA3DidVa0Tvi66A93N6AzKKGBLxgSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM3nb5JA1hzFHCWC6zKtwDJZ6BG%2FidYvbkLBhd%2FQpl0v6Lc9WVA8rCjR1l7cPISSDV9dCdjX6dcrVpfU8OZZxoibuzA3Hb%2BIHbMB4CXQYaJFbzymSf5HjGeRxFBP3nBge4D0QWBzG%2BJMN67RjVAHrq9twLyMFsYci%2BgH749KbCJP2lB05mSXILuETdDWSk%2B6Ukp%2FwD5D1NmFcwNz9gTEHQ0x9fhH7pYbvMxZnEnvpfVCVgj7uGxQSMAOq3rSiBUe3eow9obEEEYrAPU%2F5UJMXEWCndVMGmvqsBr28Ml%2FpK09tKR883Bq75v0mhk2dBmKfn5TYFEt471%2B4qztVRV7K8SfIzVgVJoJmZupQNeZD5fs5I6gW3JiJhJ6KJbllKndlw52QgAuKfRubX0qsMJrArkrBlEzkOgghcnCQKfJQ%2FKXZBrNo7kR6zPDzH88OWJCm%2FWmUSJEZnar78%2B%2FOMS87ua6BWs6Vv1V5VIx2xWN7Oc7INUYON5pwIt0ZkaUhaR4nNUXbBih%2BSdlSvOaehvbvbDxi34%2B9u5nERgyJg2KbyQcgO1XEIQCLmgRyLRRFj6%2Fg55Fp2I67lzSyAZ3tdHu3XC9p4cdmo7%2FQYozgLsuuT3c4YWhVpbep6vR5b0mvCa%2Bpae1tiqQBYEo7lfRgwi7yOvQY6pgGXa0gLam3UfOKDzKJbfk4oKKlqiZkx6kss3AKfQZ3%2F%2BxvJk76POviIbgs1bjForjecs24QvgWwUNECzSknNkfLKMrrPot7ROzuPxMHEai3zmlyDufbK1rhbKxKRyHKalbV95Wjc1KXDgixzbQ7iqkJ%2B36z5pyIJySo%2FipL9BZefjGr2Nw%2FxGsaiBv9NRso5FGWViE%2BbF5lB9kRqYk2HVHnlUNUn2XS&X-Amz-Signature=c58d15facb8f527845a183c31880dcf7f3858ab0c90bb86e73c6bbb5b5e33a34&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7ZBZFB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDXEQoC1hKSjlBX0YBCKDlBzlIIjtEbU419SGN3IaG%2FwAiAXolU6GJ4KbBYbfHA3DidVa0Tvi66A93N6AzKKGBLxgSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM3nb5JA1hzFHCWC6zKtwDJZ6BG%2FidYvbkLBhd%2FQpl0v6Lc9WVA8rCjR1l7cPISSDV9dCdjX6dcrVpfU8OZZxoibuzA3Hb%2BIHbMB4CXQYaJFbzymSf5HjGeRxFBP3nBge4D0QWBzG%2BJMN67RjVAHrq9twLyMFsYci%2BgH749KbCJP2lB05mSXILuETdDWSk%2B6Ukp%2FwD5D1NmFcwNz9gTEHQ0x9fhH7pYbvMxZnEnvpfVCVgj7uGxQSMAOq3rSiBUe3eow9obEEEYrAPU%2F5UJMXEWCndVMGmvqsBr28Ml%2FpK09tKR883Bq75v0mhk2dBmKfn5TYFEt471%2B4qztVRV7K8SfIzVgVJoJmZupQNeZD5fs5I6gW3JiJhJ6KJbllKndlw52QgAuKfRubX0qsMJrArkrBlEzkOgghcnCQKfJQ%2FKXZBrNo7kR6zPDzH88OWJCm%2FWmUSJEZnar78%2B%2FOMS87ua6BWs6Vv1V5VIx2xWN7Oc7INUYON5pwIt0ZkaUhaR4nNUXbBih%2BSdlSvOaehvbvbDxi34%2B9u5nERgyJg2KbyQcgO1XEIQCLmgRyLRRFj6%2Fg55Fp2I67lzSyAZ3tdHu3XC9p4cdmo7%2FQYozgLsuuT3c4YWhVpbep6vR5b0mvCa%2Bpae1tiqQBYEo7lfRgwi7yOvQY6pgGXa0gLam3UfOKDzKJbfk4oKKlqiZkx6kss3AKfQZ3%2F%2BxvJk76POviIbgs1bjForjecs24QvgWwUNECzSknNkfLKMrrPot7ROzuPxMHEai3zmlyDufbK1rhbKxKRyHKalbV95Wjc1KXDgixzbQ7iqkJ%2B36z5pyIJySo%2FipL9BZefjGr2Nw%2FxGsaiBv9NRso5FGWViE%2BbF5lB9kRqYk2HVHnlUNUn2XS&X-Amz-Signature=b0853d104a833ff0030a41b63380c75c8ac7aad51843aa4389c4818931297a32&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFI2LK3E%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCKmLNFNlxsdpsxKyqj3V2FyP4GtnFLsv8RtDFyPyTG5gIgOvFqmXCUxinq%2FO9V4uKlHA%2FaRR68DzFd%2BjZP5Q9UhJQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLg7AY6SArQsFSQWhCrcA8Dz1%2BfBWsncKYTfMcl612Y9C9fsDjJELgxz3rRoGCihYG1%2FRD%2BtBI9yEzYgbyHKamljjo6XmlljFL88hOXL8h%2FuZY%2BEGUSeJPmdszfMIgFc9PYcGTc%2BXkXjDAaXYaPDKUpdg6XAkbWj2NBRtzzAFjsHxedRrxM2Ct8ekrH35sH78U3sDHOWKJfwRS4XUX4gH%2ByBdbPcM5yK9%2FNisaNc3VCGBRHqhn9wyZRnOzHxfOxMBu8ns8njckHnw1fjK6z%2F65HJIz%2FyXoqcTtMJiwOdVkg4wIdV7OWTpWt6d%2FbUQ5MoogUhTKGnQ1MTNRBM4UvZ1LttuLiiUHia0QCUv4L9tuLejz3YOTZ7mImn4zF6K0euy2UaI7lyMD21W2Es%2FJRSKn8GLMGlBut4AIv3SV%2FmiAxs6T1eRUG83aMQsuVXr7XNei1OIrr0OLwkvaRgtS1RUYcNQ2uf9zB8Q5PaE%2BhlC24DkKmopRBVwkV6HMH1y57aTrgCABL%2BH90oFRnp9lLBWbEnBgsoBybcLZ1%2FvZ1fnT%2Fn0kkEhVvax5WHqgODEuzA2FAjIwvS3iSRY3XhqCumE4ItCoU5nsFTM1FFc0usTrSEB1ksBJkHtIMehJYqvEDIpDxg%2BRH3iwqMQ1IHMMG6jr0GOqUBW78gnCKOxLTeTnSxE0tdUH4MRShyzhiX2mLGxpiMNbawk7q%2Fkx2h0FQAok8iHqG9C6LQyS0CpIVxTsA8TZWcraCyTskoi5FApkMwhZNzpx3P1drhCD0gvYtzAYt%2BTK5VobahI7PnckV4kDcGUb4vFFOm0cApKt5kF0gUJdX4NCygfTzt9wIcfwzllv6UBFdd5JNbXuBXhGqE52gjo%2BF%2FODW2EJzu&X-Amz-Signature=1072316f18b1843ef4a9214cd7a59ec31602463db6edf3e917f146ea47003dda&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFI2LK3E%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCKmLNFNlxsdpsxKyqj3V2FyP4GtnFLsv8RtDFyPyTG5gIgOvFqmXCUxinq%2FO9V4uKlHA%2FaRR68DzFd%2BjZP5Q9UhJQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLg7AY6SArQsFSQWhCrcA8Dz1%2BfBWsncKYTfMcl612Y9C9fsDjJELgxz3rRoGCihYG1%2FRD%2BtBI9yEzYgbyHKamljjo6XmlljFL88hOXL8h%2FuZY%2BEGUSeJPmdszfMIgFc9PYcGTc%2BXkXjDAaXYaPDKUpdg6XAkbWj2NBRtzzAFjsHxedRrxM2Ct8ekrH35sH78U3sDHOWKJfwRS4XUX4gH%2ByBdbPcM5yK9%2FNisaNc3VCGBRHqhn9wyZRnOzHxfOxMBu8ns8njckHnw1fjK6z%2F65HJIz%2FyXoqcTtMJiwOdVkg4wIdV7OWTpWt6d%2FbUQ5MoogUhTKGnQ1MTNRBM4UvZ1LttuLiiUHia0QCUv4L9tuLejz3YOTZ7mImn4zF6K0euy2UaI7lyMD21W2Es%2FJRSKn8GLMGlBut4AIv3SV%2FmiAxs6T1eRUG83aMQsuVXr7XNei1OIrr0OLwkvaRgtS1RUYcNQ2uf9zB8Q5PaE%2BhlC24DkKmopRBVwkV6HMH1y57aTrgCABL%2BH90oFRnp9lLBWbEnBgsoBybcLZ1%2FvZ1fnT%2Fn0kkEhVvax5WHqgODEuzA2FAjIwvS3iSRY3XhqCumE4ItCoU5nsFTM1FFc0usTrSEB1ksBJkHtIMehJYqvEDIpDxg%2BRH3iwqMQ1IHMMG6jr0GOqUBW78gnCKOxLTeTnSxE0tdUH4MRShyzhiX2mLGxpiMNbawk7q%2Fkx2h0FQAok8iHqG9C6LQyS0CpIVxTsA8TZWcraCyTskoi5FApkMwhZNzpx3P1drhCD0gvYtzAYt%2BTK5VobahI7PnckV4kDcGUb4vFFOm0cApKt5kF0gUJdX4NCygfTzt9wIcfwzllv6UBFdd5JNbXuBXhGqE52gjo%2BF%2FODW2EJzu&X-Amz-Signature=0aee33abc158a25523434c1ff52b0aadab66ae99865b5ee4f145d8ef97171586&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFI2LK3E%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCKmLNFNlxsdpsxKyqj3V2FyP4GtnFLsv8RtDFyPyTG5gIgOvFqmXCUxinq%2FO9V4uKlHA%2FaRR68DzFd%2BjZP5Q9UhJQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLg7AY6SArQsFSQWhCrcA8Dz1%2BfBWsncKYTfMcl612Y9C9fsDjJELgxz3rRoGCihYG1%2FRD%2BtBI9yEzYgbyHKamljjo6XmlljFL88hOXL8h%2FuZY%2BEGUSeJPmdszfMIgFc9PYcGTc%2BXkXjDAaXYaPDKUpdg6XAkbWj2NBRtzzAFjsHxedRrxM2Ct8ekrH35sH78U3sDHOWKJfwRS4XUX4gH%2ByBdbPcM5yK9%2FNisaNc3VCGBRHqhn9wyZRnOzHxfOxMBu8ns8njckHnw1fjK6z%2F65HJIz%2FyXoqcTtMJiwOdVkg4wIdV7OWTpWt6d%2FbUQ5MoogUhTKGnQ1MTNRBM4UvZ1LttuLiiUHia0QCUv4L9tuLejz3YOTZ7mImn4zF6K0euy2UaI7lyMD21W2Es%2FJRSKn8GLMGlBut4AIv3SV%2FmiAxs6T1eRUG83aMQsuVXr7XNei1OIrr0OLwkvaRgtS1RUYcNQ2uf9zB8Q5PaE%2BhlC24DkKmopRBVwkV6HMH1y57aTrgCABL%2BH90oFRnp9lLBWbEnBgsoBybcLZ1%2FvZ1fnT%2Fn0kkEhVvax5WHqgODEuzA2FAjIwvS3iSRY3XhqCumE4ItCoU5nsFTM1FFc0usTrSEB1ksBJkHtIMehJYqvEDIpDxg%2BRH3iwqMQ1IHMMG6jr0GOqUBW78gnCKOxLTeTnSxE0tdUH4MRShyzhiX2mLGxpiMNbawk7q%2Fkx2h0FQAok8iHqG9C6LQyS0CpIVxTsA8TZWcraCyTskoi5FApkMwhZNzpx3P1drhCD0gvYtzAYt%2BTK5VobahI7PnckV4kDcGUb4vFFOm0cApKt5kF0gUJdX4NCygfTzt9wIcfwzllv6UBFdd5JNbXuBXhGqE52gjo%2BF%2FODW2EJzu&X-Amz-Signature=7e7a8119c71c85ca4cf0f5dd5beeca8a10830613ade6a5bb6475d65537697043&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFI2LK3E%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCKmLNFNlxsdpsxKyqj3V2FyP4GtnFLsv8RtDFyPyTG5gIgOvFqmXCUxinq%2FO9V4uKlHA%2FaRR68DzFd%2BjZP5Q9UhJQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLg7AY6SArQsFSQWhCrcA8Dz1%2BfBWsncKYTfMcl612Y9C9fsDjJELgxz3rRoGCihYG1%2FRD%2BtBI9yEzYgbyHKamljjo6XmlljFL88hOXL8h%2FuZY%2BEGUSeJPmdszfMIgFc9PYcGTc%2BXkXjDAaXYaPDKUpdg6XAkbWj2NBRtzzAFjsHxedRrxM2Ct8ekrH35sH78U3sDHOWKJfwRS4XUX4gH%2ByBdbPcM5yK9%2FNisaNc3VCGBRHqhn9wyZRnOzHxfOxMBu8ns8njckHnw1fjK6z%2F65HJIz%2FyXoqcTtMJiwOdVkg4wIdV7OWTpWt6d%2FbUQ5MoogUhTKGnQ1MTNRBM4UvZ1LttuLiiUHia0QCUv4L9tuLejz3YOTZ7mImn4zF6K0euy2UaI7lyMD21W2Es%2FJRSKn8GLMGlBut4AIv3SV%2FmiAxs6T1eRUG83aMQsuVXr7XNei1OIrr0OLwkvaRgtS1RUYcNQ2uf9zB8Q5PaE%2BhlC24DkKmopRBVwkV6HMH1y57aTrgCABL%2BH90oFRnp9lLBWbEnBgsoBybcLZ1%2FvZ1fnT%2Fn0kkEhVvax5WHqgODEuzA2FAjIwvS3iSRY3XhqCumE4ItCoU5nsFTM1FFc0usTrSEB1ksBJkHtIMehJYqvEDIpDxg%2BRH3iwqMQ1IHMMG6jr0GOqUBW78gnCKOxLTeTnSxE0tdUH4MRShyzhiX2mLGxpiMNbawk7q%2Fkx2h0FQAok8iHqG9C6LQyS0CpIVxTsA8TZWcraCyTskoi5FApkMwhZNzpx3P1drhCD0gvYtzAYt%2BTK5VobahI7PnckV4kDcGUb4vFFOm0cApKt5kF0gUJdX4NCygfTzt9wIcfwzllv6UBFdd5JNbXuBXhGqE52gjo%2BF%2FODW2EJzu&X-Amz-Signature=0024af78430b31b067ff8e7234ec374c3165ad587b485393442ae8173ec62f4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFI2LK3E%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCKmLNFNlxsdpsxKyqj3V2FyP4GtnFLsv8RtDFyPyTG5gIgOvFqmXCUxinq%2FO9V4uKlHA%2FaRR68DzFd%2BjZP5Q9UhJQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLg7AY6SArQsFSQWhCrcA8Dz1%2BfBWsncKYTfMcl612Y9C9fsDjJELgxz3rRoGCihYG1%2FRD%2BtBI9yEzYgbyHKamljjo6XmlljFL88hOXL8h%2FuZY%2BEGUSeJPmdszfMIgFc9PYcGTc%2BXkXjDAaXYaPDKUpdg6XAkbWj2NBRtzzAFjsHxedRrxM2Ct8ekrH35sH78U3sDHOWKJfwRS4XUX4gH%2ByBdbPcM5yK9%2FNisaNc3VCGBRHqhn9wyZRnOzHxfOxMBu8ns8njckHnw1fjK6z%2F65HJIz%2FyXoqcTtMJiwOdVkg4wIdV7OWTpWt6d%2FbUQ5MoogUhTKGnQ1MTNRBM4UvZ1LttuLiiUHia0QCUv4L9tuLejz3YOTZ7mImn4zF6K0euy2UaI7lyMD21W2Es%2FJRSKn8GLMGlBut4AIv3SV%2FmiAxs6T1eRUG83aMQsuVXr7XNei1OIrr0OLwkvaRgtS1RUYcNQ2uf9zB8Q5PaE%2BhlC24DkKmopRBVwkV6HMH1y57aTrgCABL%2BH90oFRnp9lLBWbEnBgsoBybcLZ1%2FvZ1fnT%2Fn0kkEhVvax5WHqgODEuzA2FAjIwvS3iSRY3XhqCumE4ItCoU5nsFTM1FFc0usTrSEB1ksBJkHtIMehJYqvEDIpDxg%2BRH3iwqMQ1IHMMG6jr0GOqUBW78gnCKOxLTeTnSxE0tdUH4MRShyzhiX2mLGxpiMNbawk7q%2Fkx2h0FQAok8iHqG9C6LQyS0CpIVxTsA8TZWcraCyTskoi5FApkMwhZNzpx3P1drhCD0gvYtzAYt%2BTK5VobahI7PnckV4kDcGUb4vFFOm0cApKt5kF0gUJdX4NCygfTzt9wIcfwzllv6UBFdd5JNbXuBXhGqE52gjo%2BF%2FODW2EJzu&X-Amz-Signature=86c0a0b39e4cab776adf72e1c1aa7988bd56107d313a578f2c07089aef4c8e26&X-Amz-SignedHeaders=host&x-id=GetObject)
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


