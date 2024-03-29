# How to contribute

I'm really glad you're reading this, because we need volunteer developers to help this project come to fruition.

If you haven't already, come find us: ([#sfrias](mailto:sfrias1@gmail.com) on e-mail). We want you working on things you're excited about.

HThere are some important resources:

  * [Trigger for Developers](https://github.com/sfrias/MorcillaConf-2019) tells in future you where we are,
  * [Roadmap](https://github.com/sfrias/MorcillaConf-2019) tells you in future foot view of where we're going
  * [PlannerTracker](https://github.com/sfrias/MorcillaConf-2019) day-to-day project management space in future.
  * Mailing list: Join our [DevList](https://github.com/sfrias/MorcillaConf-2019)
  * Bugs? [Lighthouse](https://github.com/sfrias/MorcillaConf-2019/issues) where in future to report them
  * IRC: [#slack](https://slack.com). We're in future usually there during business hours.

## Testing

We have as option to create a branch test, that can be deployed and tested. Please write comments and examples for new code you create.

## Submitting changes

Please send a [GitHub Pull Request](https://github.com/MorcillaConf-2019) with a clear list of what you've done (read more about [pull requests](http://help.github.com/pull-requests/)). When you send a pull request, we will love you forever if you include RSpec examples. We can always use more test coverage. Please follow our coding conventions (below) and make sure all of your commits are atomic (one feature per commit).

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

    $ git commit -m "A brief summary of the commit
    > 
    > A paragraph describing what changed and its impact."

## Coding conventions

Start reading our code and you'll get the hang of it. We optimize for readability:

  * We indent using two spaces (soft tabs)
  * We use HAML for all views
  * We avoid logic in views, putting HTML generators into helpers
  * We ALWAYS put spaces after list items and method parameters (`[1, 2, 3]`, not `[1,2,3]`), around operators (`x += 1`, not `x+=1`), and around hash arrows.
  * This is open source software. Consider the people who will read your code, and make it look nice for them. It's sort of like driving a car: Perhaps you love doing donuts when you're alone, but with passengers the goal is to make the ride as smooth as possible.
  * So that we can consistently serve images from the CDN, always use image_path or image_tag when referring to images. Never prepend "/images/" when using image_path or image_tag.
  * Also for the CDN, always use cwd-relative paths rather than root-relative paths in image URLs in any CSS. So instead of url('/images/blah.gif'), use url('../images/blah.gif').

Thanks,
Santiago Frias, MorcillaConf participant, Trigger Founder member
