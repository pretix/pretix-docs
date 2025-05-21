# Browser support policy

## Tested browsers

We develop our software to work with the following browsers:

- Apple Safari (macOS and iOS)
- Google Chrome (Android and Desktop)
- Microsoft Edge (Desktop)
- Mozilla Firefox (Android and Desktop)

We do not offer official support for other browsers such as Brave or Vivaldi. 
But since these browsers use the same engines as Google Chrome, we expect them to work the same way. 
We have **stopped** supporting Internet Explorer in release [2024.07](https://pretix.eu/about/de/blog/20240726-release-2024-7/). 

## Browser versions

We support browser versions based on the [baseline](https://web-platform-dx.github.io/web-features/) definitions created by a working group of browser vendors and the web standards community.

For **ticket shops** and the [**pretix Widget**](../../guides/widget.md), we will only require browser features that are considered **widely available** by the baseline project. 
That means that these features have to be available across browsers **for at least 2½ years** (30 months).
In other words, everyone with a browser version released in the last 2½ years will be able to buy a ticket without issues.

For the **backend**, we also require web features that are **widely available** for mission-critical features.
However, advanced features of the pretix backend may require web features that are **newly available**, i.e. they are available across all of the browsers in their most recent version.
