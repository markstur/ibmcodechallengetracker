# IBM Code Challenge Tracker

As an org, we were issued a fun challenge, to crank out a bunch of assets (journeys, tech talks, how-tos, etc). This application measures the progress of journeys and how-tos since that information is easily fetchable, as it's stored in Wrike, our project management tool. This application is built using Python, and based on the [Flask microframework](http://flask.pocoo.org/).

## Before running the app

You'll need to set up a few environment variables:

* `WRIKE_ACCESS_TOKEN`: Used as a bearer access token with the Wrike APIs
* `JOURNEY_ID`: The ID of the `_Journey Status` project in Wrike
* `HOWTO_ID`: The ID of the `_How-To Status` project in Wrike

You can create a `WRIKE_ACCESS_TOKEN` by going into your profile settings in Wrike. As for `JOURNEY_ID` and `HOWTO_ID`, I had to make an API call to Wrike to find them out, you can do this by running the command below:

```bash
$ curl -g -v -X GET -H 'Authorization: bearer <your_access_token' 'https://www.wrike.com/api/v3/folders'
```

I could have done this programmatically in the application, but the IDs shouldn't change, so I decided to set them as environment variables instead.

## Run the app locally

1. [Install Python][]
1. cd into this project's root directory
1. Run `pip install -r requirements.txt` to install the app's dependencies
1. Run `python welcome.py`
1. Access the running app in a browser at <http://localhost:5000>

[Install Python]: https://www.python.org/downloads/

## Pushing to IBM Cloud

1. Clone this repository and change to the directory where your code is located

```bash
$ git clone https://github.com/stevemart/ibmcodechallengetracker
$ cd ibmcodechallengetracker
```

2. Connect to IBM Cloud

```bash
$ bluemix api https://api.ng.bluemix.net
$ bluemix login -u your_user_name
or
$ bluemix login -sso
```

3. Upload new changes

From your cloned directory, redeploy your app to Bluemix by using the bluemix app push command.

```bash
$ bluemix app push ibmcodechallenge-tracker
```

Access your app by browsing to https://ibmcodechallenge-tracker.mybluemix.net

## Contributing back

Pull requests are accepted! If you see an issue, file it.

## TODO

* Track tech-talks
* Track blogs
