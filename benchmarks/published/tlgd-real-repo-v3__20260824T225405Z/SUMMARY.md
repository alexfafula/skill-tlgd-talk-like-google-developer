### Run `tlgd-real-repo-v3__20260824T225405Z`

| Agent | Case | Control quality | tlgd quality | Control budget | tlgd budget | Control words | tlgd words | Word change | Control mannerisms | tlgd mannerisms | Control tokens | tlgd tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| agy | conditional-get-304 | 3/3 | 3/3 | 0/3 | 0/3 | 827 | 833 | +1% | 0 | 0 | 156677 | 161424 |
| agy | etag-default | 1/3 | 3/3 | 0/3 | 3/3 | 135 | 43 | -70% | 0 | 0 | 76725 | 62839 |
| agy | locate-res-json | 3/3 | 3/3 | 3/3 | 3/3 | 55 | 31 | -44% | 0 | 0 | 70172 | 52054 |
| agy | validation-commands | 0/3 | 3/3 | 0/3 | 3/3 | 128 | 50 | -67% | 0 | 0 | 80691 | 80832 |
| claude | conditional-get-304 | 3/3 | 3/3 | 0/3 | 0/3 | 951 | 785 | -18% | 0 | 0 | 5691 | 4978 |
| claude | etag-default | 0/3 | 3/3 | 0/3 | 3/3 | 246 | 73 | -70% | 0 | 0 | 1442 | 854 |
| claude | locate-res-json | 3/3 | 3/3 | 0/3 | 3/3 | 126 | 53 | -60% | 0 | 0 | 641 | 571 |
| claude | validation-commands | 0/3 | 2/3 | 0/3 | 3/3 | 221 | 41 | -80% | 0 | 0 | 1363 | 333 |
| codex | conditional-get-304 | 3/3 | 3/3 | 0/3 | 0/3 | 699 | 639 | -9% | 0 | 0 | 309245 | 231755 |
| codex | etag-default | 0/3 | 3/3 | 3/3 | 3/3 | 83 | 50 | -48% | 0 | 0 | 73666 | 74656 |
| codex | locate-res-json | 3/3 | 3/3 | 3/3 | 3/3 | 41 | 34 | -17% | 0 | 0 | 71522 | 69093 |
| codex | validation-commands | 3/3 | 3/3 | 3/3 | 3/3 | 50 | 38 | -24% | 0 | 0 | 73756 | 96494 |

Totals: control quality 22/36, tlgd quality 35/36; control budget 12/36, tlgd budget 27/36.

Words, mannerisms, and tokens are medians over repetitions; word change is the median per-pair change, negative when the treatment is shorter. Tokens are host-reported totals and compare only within one agent and model.
