# Release cycle

## pretix Hosted

Our Software as a Service offering "pretix Hosted" is released using a [continuous delivery](https://en.wikipedia.org/wiki/Continuous_delivery) scheme.
We roll out new versions with improvements, bug fixes, or new features without interrupting the system–often multiple times a day.

## Self-hosted versions of pretix

<!-- md:community -->
<!-- md:enterprise -->

The self-hosted version of pretix that builds the basis for both "pretix Community" and "pretix Enterprise", follows the following release cycle and versioning scheme:

- Feature releases per year with a version number of ``YEAR.NUMBER.0`` (e.g. 2025.5.0 is the fifth feature release of 2025) are usually released in the last week of every month, except for December and sometimes except for either July or August.
  These releases may contain new functionality, removal of functionality, or any other kind of change.
  It is recommended that you study the release notes before upgrading if you are concerned about API or plugin compatibility.

- Bugfix releases with a version number of ``year.number.PATCH`` (e.g. 2025.5.1 is the first bugfix release after 2025.5.0).
  These are not released on a schedule, but when required to fix a critical issue that cannot wait for the next monthly release.
  These releases may not contain any functional changes, unless that functional changes are required to fix a security issue.

If a serious security issue arises, we publish bugfix releases for the **last three feature releases**.
For example, if a security issue becomes known after the release of 2025.5.0, we will publish versions 2025.5.1, 2025.4.1, and 2025.3.1.
This allows you a quick and safe upgrade even if you did not upgrade to the latest feature release yet.
We recommend to always update to new feature releases within three months to ensure compatibility with upcoming security releases.

All new releases are announced on [our blog](https://pretix.eu/about/en/blog/), as well as through our social media channels and newsletter.

### Plugins

Plugins published by us (either as open source packages or as part of pretix Enterprise) usually are published in a new version on the same day as a new feature release of pretix (if there have been any significant changes since the previous feature release of pretix) and are announced as part of the same blog post.
Occasionally there may be plugin updates in between feature releases if there is an urgent need.
We ensure that the latest published versions of a plugin will always be compatible with the latest feature release of pretix.
We therefore recommend updating plugins and the core system at the same time.
Most plugins follow a ``MAJOR.MINOR.PATCH`` version number scheme.

## Android, iOS, and Desktop apps

Our apps, such as pretixSCAN, pretixPOS, pretixPRINT, or pretixLEAD, each follow their own versioning cycle.
While we recommend keeping them always up-to-date, new versions of the apps always stay compatible with old versions of pretix and vice versa for at least a few months, so they do not need to be updated on the same day.
You can view their release history and change log on [pretix Marketplace](https://marketplace.pretix.eu/categories/12/).