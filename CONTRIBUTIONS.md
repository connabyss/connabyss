# Contributions

Fixes and tests I've sent to other projects, most found with [Bite](https://github.com/connabyss/bite).

## Merged

- **prosemirror-py**: a commit said a memory leak was fixed, and it wasn't ([#335](https://github.com/fellowapp/prosemirror-py/issues/335)); fixed in [#336](https://github.com/fellowapp/prosemirror-py/pull/336), plus a shared-list bug in `Mapping` ([#337](https://github.com/fellowapp/prosemirror-py/pull/337))
- **h2** (Python's HTTP/2 library): test for duplicate Host headers the mismatch check misses ([#1343](https://github.com/python-hyper/h2/pull/1343))
- **Tencent teamai-cli**: secrets in tool arguments leaked into session logs and the judge's transcript ([#1669](https://github.com/Tencent/teamai-cli/pull/1669), [#1671](https://github.com/Tencent/teamai-cli/pull/1671))
- **west** (Zephyr's command-line tool): crash when a manifest uses a reserved project name ([#1013](https://github.com/zephyrproject-rtos/west/pull/1013))
- **kin-openapi**: tests for deepObject array index limits ([#1412](https://github.com/getkin/kin-openapi/pull/1412))
- **mkdocs-htmlproofer-plugin**: tests for `ignore_pages`, `ignore_urls` and `warn_on_ignored_urls` ([#126](https://github.com/manuzhang/mkdocs-htmlproofer-plugin/pull/126))
- **drf-pydantic**: five conversion bugs from my report ([#51](https://github.com/georgebv/drf-pydantic/issues/51)), fixed in [#52](https://github.com/georgebv/drf-pydantic/pull/52) to [#56](https://github.com/georgebv/drf-pydantic/pull/56)
- **midea-lan**: the 8370 message encoder got the frame length wrong when no padding was needed ([#251](https://github.com/wuwentao/midea-lan/pull/251))
- **mizani**: number labels dropped decimals when values were close together ([#90](https://github.com/has2k1/mizani/pull/90))
- **pamqp**: tests for three past fixes nothing guarded, including `requeue=False` ([#86](https://github.com/gmr/pamqp/pull/86))
- **pyclibrary**: nine fixes from my report ([#92](https://github.com/MatthieuDartiailh/pyclibrary/issues/92)), in [#93 to #101](https://github.com/MatthieuDartiailh/pyclibrary/pulls?q=is%3Apr+author%3Aconnabyss)
- **django-tailwind-cli**: the watcher's output ([#232](https://github.com/django-commons/django-tailwind-cli/pull/232)), shipped in 4.8.2
- **text-to-cad**: the Python 3.11 check missed same-quote nested f-strings ([#708](https://github.com/earthtojake/text-to-cad/pull/708)), shipped in 0.8.2

## Reported and fixed by the maintainers

- **srptools**: four bugs ([#13](https://github.com/idlesign/srptools/issues/13))
- **resolve-robotics-uri-py**: which match counts as "first" ([#26](https://github.com/gbionics/resolve-robotics-uri-py/issues/26))

## Open

- **kin-openapi**: opening a spec with whole-file `$ref`s re-reads the same files over and over ([#1414](https://github.com/getkin/kin-openapi/pull/1414), [#1415](https://github.com/getkin/kin-openapi/pull/1415))
- [Everything else waiting on review](https://github.com/search?q=author%3Aconnabyss+is%3Apr+is%3Aopen+-user%3Aconnabyss&type=pullrequests)
