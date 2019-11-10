# LRT Status

LRT Status is a web application to pull the latest information about Ottawa's LRT 

## Installation

1. Create your viritual enviroment. Go to the backend folder and  install the following command.

``` pip install -r requirements.txt ```

_requirements.txt is file containing all the latest packages._


2. Create your own virtual enviroment.

``` virutalenv env ```

3. Active the virtual enviroment.

```source env/bin/activate```

_Side Note: if you have terminal (such as zsh or fish), fill the blank after active. 
Example:_ ```source env/bin/activate.fish```

4. Create a `.env` file that contains the following data (PURPOSE:  easy user based aunthetication without revealing it). 

```
FIREBASE_APIKEY=
FIREBASE_DATABASE_URL=
```

5. Install `Next.js` in the frontend folder.
```
yarn install 
yarn dev
```

Now you can visit the website on http://localhost:3000

## Usage
Open up the site on (insert link)

## Meta
Jason Le - @jQwotos
Monica Vu - @Monica-Vu

## Contributing 
1. Fork it (https://github.com/yourname/yourproject/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request