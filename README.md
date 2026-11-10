## CH

I build [Bite](https://github.com/connabyss/bite), a tool that checks whether a "fixed" commit is really fixed. It takes the fix back out and runs your tests. Get the latest Bite: `pipx install bite-check`.

Some fixes I've had merged upstream:

- **prosemirror-py**: a memory leak a commit said was fixed but wasn't ([#336](https://github.com/fellowapp/prosemirror-py/pull/336)), and a shared-list bug ([#337](https://github.com/fellowapp/prosemirror-py/pull/337))
- **h2** (Python's HTTP/2 library): test for duplicate Host headers the check missed ([#1343](https://github.com/python-hyper/h2/pull/1343))
- **text-to-cad**: its Python 3.11 check missed same-quote nested f-strings ([#708](https://github.com/earthtojake/text-to-cad/pull/708), shipped in [0.8.2](https://github.com/earthtojake/text-to-cad/releases/tag/v0.8.2))
- **Tencent teamai-cli**: secrets leaking through tool arguments ([#1669](https://github.com/Tencent/teamai-cli/pull/1669), [#1671](https://github.com/Tencent/teamai-cli/pull/1671))
- **west** (Zephyr's command-line tool): crash on a reserved project name ([#1013](https://github.com/zephyrproject-rtos/west/pull/1013))
- **kin-openapi**: tests for deepObject array index limits ([#1412](https://github.com/getkin/kin-openapi/pull/1412))
- **midea-lan**: wrong frame length in the 8370 message encoder ([#251](https://github.com/wuwentao/midea-lan/pull/251))
- **mizani**: number labels dropped decimals when values were close ([#90](https://github.com/has2k1/mizani/pull/90))
- **pyclibrary**: nine bug fixes ([#93–#101](https://github.com/MatthieuDartiailh/pyclibrary/pulls?q=is%3Apr+author%3Aconnabyss))

[All contributions](CONTRIBUTIONS.md) · [Writing](https://dev.to/connabyss)
