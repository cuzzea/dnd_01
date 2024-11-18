---
layout: default
---

# The Lost Memories of Artemis

## Prologue

During the last exodus of the Seventh Eclipse, many artefacts have been collected by the brotherhood of the sigil. This represents a collection of the most strange and unexplained tales that can be shared with the general people outside the brotherhood, without needing a seal of light.

The memoirs seem to be kept by one individual, named Artemis, or somebody that might of been part of hist party and are found scattered all over the land, from the depths of the Shadowspine Mountains to the shores of the Twilight Sea. The manuscripts vary wildly in their making - some written on ancient parchment with silver ink, others carved into moon-blessed bark, and a few etched onto sheets of strange, opalescent metal. It seems that this specific individual was not concerned about the safety of the memoirs and he did not have the intention of keeping them. We do presume that if not lost, the memoirs would be burned by the writer as a form of release, as we found partial charred remains of what seem to be similar memoirs from the same author. The memoirs are not presented chronologically, but instead how they were found and stored.

We, as the publishers of these manuscript, want to inform you, the reader, that what you will read here is not verified and we consider most of this to be the ramblings of a mad worshiper of the 7 sisters. With that being said, in our research, we did find traces of his stories dating over a millennia, accounts described by him being reported as far as the age of Choros. The most recent of these manuscripts was discovered in the Year of the Seventh Moon (1157 by Imperial Reckoning), bearing ink still fresh as morning dew.

The first edition of this manuscript will mostly contain the writings found around Phandalin, the epicenter of the old Netherese Obelisk. These fragments were discovered in various states - some buried beneath rubble in abandoned mines, others hidden within the hollow spaces of ancient walls, and a particularly interesting collection found in a sealed chest within the Stonehill Inn's cellar. While these memoirs seem to be related to the rumors of the underground city, no concrete evidence has been found so far linking them to the whispered tales of vast chambers and forgotten halls beneath Phandalin's streets.

## Table of Contents

{% for post in site.posts reversed %}
- [{{ post.title }}]({{ post.url | relative_url }})  
> {{ post.excerpt | strip_html | strip_newlines | truncate: 160 }}
{% endfor %}
