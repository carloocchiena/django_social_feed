# Django social feed
Starting from what I did in my previous [Django Boilerplate](https://github.com/carloocchiena/django_boilerplate), I completely refreshed the social media project, adding new features, and strenghtening the existing ones.

## Features included
Users can:
- Create a new profile
- Login with existing accounts
- Update their profile, including avatars
- See the list of all the users, knowing if they are already following them or not
- See profiles details
- Follow and unfollow users
- See the main dashboard with all the posts in chronological order
- Create new posts, uploading a picture and seeing a preview
- Delete their posts
- Delete (deactivate) their profile
- Check the help page

### CSS Framework
While in the past project I used Bulma, this time I sticked again to Bootstrap.<br>
In the end mostly for a matter of recicle and to make the project more scalable.

### What's missing
At the moment it's just a box. There is not a lot to do.
I'd like to add:
- some kind of algo to find new users to follow based on criterias matching user preferences
- some kind of algo to sort posts by criterias matching user preferences

I could have add likes and comments to the posts, but tbh I already hate those features from existing social media and I'd like to find something different to generate a healthier interaction.
