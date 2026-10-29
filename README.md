## CH

I build [Bite](https://github.com/connabyss/bite), a referee for AI coding agents. It checks whether “done” really means done. The code is now public, and `bite --free` runs without a key.

### Recent bug fixes

- 🐛 **prosemirror-py**: a commit said a memory leak was fixed. Bite caught that it wasn't. I reported it ([#335](https://github.com/fellowapp/prosemirror-py/issues/335)) and sent a fix ([#336](https://github.com/fellowapp/prosemirror-py/pull/336)), which is waiting on review.
- 🔧 **pyclibrary**: 7 bug fixes merged ([#93–#99](https://github.com/MatthieuDartiailh/pyclibrary/pulls?q=is%3Apr+author%3Aconnabyss)). The owner called them "small and focused".
- 🎨 **django-tailwind-cli**: fixed the watcher's output ([#232](https://github.com/django-commons/django-tailwind-cli/pull/232)). Merged and shipped in 4.8.2.
- 📐 **text-to-cad**: its Python 3.11 check missed a line that breaks on real 3.11. Fixed ([#708](https://github.com/earthtojake/text-to-cad/pull/708)). Merged and shipped in 0.8.2.
- ✅ **srptools**: all 4 bugs in my report ([#13](https://github.com/idlesign/srptools/issues/13)) fixed by the maintainer the same day.

Open now: [18 PRs waiting on review](https://github.com/search?q=author%3Aconnabyss+is%3Apr+is%3Aopen+-user%3Aconnabyss&type=pullrequests), including [llm #1828](https://github.com/simonw/llm/pull/1828), [pyclibrary #100](https://github.com/MatthieuDartiailh/pyclibrary/pull/100) and [#101](https://github.com/MatthieuDartiailh/pyclibrary/pull/101), and [modeltranslation #831](https://github.com/deschler/django-modeltranslation/pull/831) and [#832](https://github.com/deschler/django-modeltranslation/pull/832). Reported, no reply yet: [ChatSBOM #217](https://github.com/WangYihang/ChatSBOM/issues/217).

✍️ Writing: [What I learned fixing bugs in other people's code](https://dev.to/connabyss/what-i-learned-fixing-bugs-in-other-peoples-code-4nch)

⭐ [Every repo Bite has helped](https://github.com/stars/connabyss/lists/repos-bite-helped)
