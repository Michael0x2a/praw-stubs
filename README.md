# praw-stubs

## Overview

A collection of [PEP 484][pep484] type hint stubs for the [praw][praw] library.

This is a work-in-progress: the majority of the library is currently unannotated.

  [pep484]: https://www.python.org/dev/peps/pep-0484/
  [praw]: https://github.com/praw-dev/praw

## Todo list

Modules that need annotations:

- [x] `praw.__init__`
- [ ] `praw.config`  (almost done; `Config.CONFIG` needs a more precise type)
- [x] `praw.const`
- [ ] `praw.exceptions`
- [ ] `praw.objector` (partially done; needs validation)
- [ ] `praw.reddit`
- [x] `praw.models.__init__.pyi`
- [ ] `praw.models.auth`
- [x] `praw.models.base`
- [ ] `praw.models.comment_forest`
- [ ] `praw.models.front`
- [x] `praw.models.helpers`
- [ ] `praw.models.inbox`
- [ ] `praw.models.modaction`
- [ ] `praw.models.preferences`
- [ ] `praw.models.stylesheet`
- [ ] `praw.models.subreddits`
- [ ] `praw.models.trophy`
- [ ] `praw.models.user`
- [ ] `praw.models.util.pyi` (partially done; `stream_generator` needs more precise types)
- [ ] `praw.models.list.__init__`
- [ ] `praw.models.list.base`
- [ ] `praw.models.list.redditor`
- [ ] `praw.models.list.trophy`
- [ ] `praw.models.listing.__init__`
- [ ] `praw.models.listing.domain`
- [x] `praw.models.listing.generator`
- [ ] `praw.models.listing.listing`
- [x] `praw.models.listing.mixins.__init__`
- [ ] `praw.models.listing.mixins.base` (need to investigate cleaning up generator args)
- [ ] `praw.models.listing.mixins.gilded`
- [ ] `praw.models.listing.mixins.redditor`
- [ ] `praw.models.listing.mixins.rising`
- [x] `praw.models.listing.mixins.submission`
- [ ] `praw.models.listing.mixins.subreddit`
- [ ] `praw.models.reddit.__init__`
- [x] `praw.models.reddit.base`
- [x] `praw.models.reddit.comment`
- [ ] `praw.models.reddit.emoji`
- [ ] `praw.models.reddit.live`
- [ ] `praw.models.reddit.message`
- [ ] `praw.models.reddit.modmail`
- [ ] `praw.models.reddit.more`
- [ ] `praw.models.reddit.multi`
- [ ] `praw.models.reddit.redditor`
- [ ] `praw.models.reddit.submission`
- [ ] `praw.models.reddit.subreddit`
- [ ] `praw.models.reddit.widgets`
- [ ] `praw.models.reddit.wikipage`
- [x] `praw.models.reddit.mixins.__init__`
- [x] `praw.models.reddit.mixins.editable`
- [x] `praw.models.reddit.mixins.gildable`
- [x] `praw.models.reddit.mixins.inboxable`
- [x] `praw.models.reddit.mixins.inboxtoggleable`
- [x] `praw.models.reddit.mixins.messageable`
- [x] `praw.models.reddit.mixins.replyable`
- [x] `praw.models.reddit.mixins.reportable`
- [x] `praw.models.reddit.mixins.savable`
- [x] `praw.models.reddit.mixins.votable`

Potential extensions:

- Consider removing some of the duplicate signatures using whatever mechanism emerges
  out of https://github.com/python/typing/issues/270, if that ever moves forward.

