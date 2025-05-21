# Browser support policy

## Tested browsers

We develop our software to work with the following browsers:

- Apple Safari (macOS and iOS)
- Google Chrome (Android and Desktop)
- Microsoft Edge (Desktop)
- Mozilla Firefox (Android and Desktop)

Other browsers (e.g. Brave, Vivaldi) are not officially supported, but since they are mostly based on the same core as Google Chrome, they usually work the same way.
Internet Explorer is no longer supported.

## Browser versions

We support browser versions based on the [baseline](https://web-platform-dx.github.io/web-features/) definitions created by a working group of browser vendors and the web standards community.

For **ticket shops** and the [**pretix Widget**](../../guides/widget.md), we will only require browser features that are considered **widely available** by the baseline project, i.e. they are available across browsers **for at least 2½ years** (30 months).
In other words, everyone with a browser version released in the last 2½ years will be able to buy a ticket without issues.

For the **backend**, we also require web features that are **widely available** for mission-critical features.
However, advanced features may require web features that are **newly available**, i.e. they are available across all of the browsers in their most recent version.