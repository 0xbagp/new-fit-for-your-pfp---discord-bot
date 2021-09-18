# Discord Bot for Dressing up Your PFP

This bot was initially created for the [MonkeyDAO](https://twitter.com/monkedao) to help [Solana Monkey Business](https://twitter.com/SolanaMBS) suit up for Christie's in support of [BAYC](https://twitter.com/BoredApeYC). It became a hit within the community and we've had a ton of fun with it, so I thought I'd open source it for you to use in your own community. 

## Magic
![clean_pfp](/docs/img/clean.png) ![suit](/docs/img/fit.png)![pfp_with_fit](/docs/img/final.png)

## Setup

* Replace the json file in the root directory with your own and ensure it's named attributes.json. This should include the PFP IDs and the respective image URL. See the included file as an example  

* Update the `get_pfp_img_url()` function with the keys for your pfp ids and image urls from the json file 

* In the outfits folder, drop the transparent pngs you'd like to use as "fits". These should be named descriptively as whatever you name the files are what the bot will use as the command arguments 

* Update the list called "outfits" with a list of strings that match your outfit file names (omit the .png). So if "suit" is one of your outfits in the list, then suit.png should be in the "outfits" folder 

* The bot command called "newfit" has a conditional statement to check that the pfp id entered is within the correct range. Update these values to match the acceptable ranges of your project.

That's it! Setup the bot and invite it into your server and you should be good to go. 

## How to use it

The basic command format is **!newfit** `<fit> <pfp_id>`. So you might enter **!newfit suit 970**. 

The command **!fits** will list all of the fitst defined in the "outfits" list so the user knows what options are available to them. 

I hope your community has fun with this! 

If your community loves it and you want to throw me a tip you can do so below: 

* **SOL:** C5XYM4RDtEdKm5NhDLhYJ7gH4vNRocna5qYb1pCThNa
* **ETH:** 0xAf1c16F1370dEdad2784287595f9152D8A1575d3
