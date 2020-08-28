# Quotation

## **Starting the app**

First check if you have all the modules and python 3.8 installed. I used [Pipenv](https://pypi.org/project/pipenv/ "PyPI - Pipenv") to create an environment and installed all the modules in it, I truly recommend you to do the same.


First alter the API key at line 8 in the [alpha_vantage.py]("https://github.com/vinigalantine/quotation/tree/master/backend/alpha_vantage.py") file, inside ```backend``` directory.

Then using CMD/PS or Terminal application enter in this directory.

Once you entered the ```backend``` directory start the Uvicorn server with the code bellow:
```
uvicorn main:app
```

After you started the server, just open the ```index.html``` file in the frontend directory on favorite browser.

## **Testing**

If you want to run some tests, just acess the ```backend``` directory and run the code bellow:
```
pytest
```
And then it will return the results of the tests inside ```test_main.py```

### **Observations**

I didn't have much time dedicated to this project, so it's just a simple app.
I had some problems with the API, I couldn't retrieve data about indexes like Ibov, Nasdaq or Dow Jones. I tried using "^BVSP", "BVSP", "^BVMF" and even "BVMF" on the [AlphaVantage API](https://www.alphavantage.co) as I saw in some tutorials but nothing worked for me.