## CH

I build [Bite](https://github.com/connabyss/bite), a tool that checks whether a "fixed" commit is really fixed. It takes the fix back out and runs your tests. Bite 1.0 is out: `pipx install bite-check`.

Some fixes I've had merged upstream:

- **west** (Zephyr's command-line tool): crash on a reserved project name ([#1013](https://github.com/zephyrproject-rtos/west/pull/1013))
- **kin-openapi**: tests for deepObject array index limits ([#1412](https://github.com/getkin/kin-openapi/pull/1412))
- **midea-lan**: wrong frame length in the 8370 message encoder ([#251](https://github.com/wuwentao/midea-lan/pull/251))
- **mizani**: number labels dropped decimals when values were close ([#90](https://github.com/has2k1/mizani/pull/90))
- **pyclibrary**: nine bug fixes ([#93–#101](https://github.com/MatthieuDartiailh/pyclibrary/pulls?q=is%3Apr+author%3Aconnabyss))

[All contributions](CONTRIBUTIONS.md) · [Writing](https://dev.to/connabyss)
