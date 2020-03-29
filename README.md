# sparksentimeter-website
A Django webpage that shows the trend of stocks, today's top buys, top sells and top holds, top gainers and top losers.

## Background
This Django website is based on a underlying Sentiment Analysis model using Apache Spark framework.

## Steps
1. Setup a Spark cluster. Start Spark cluster by typing `spark-installation-directory/sbin/./start-all.sh`.

2. Submit the scraping job to the Spark cluster by typing `bin/spark-submit scraper.py`
[scraper.py](https://github.com/varsha-varadarajan/sparksentimeter-website/blob/master/stock/utils/scraper.py)

3. Start Django server `python manage.py runserver`

4. Open `http://127.0.0.1:8000/stock/`

Django webpage

![Image of Webpage](https://github.com/varsha-varadarajan/sparksentimeter-images/blob/master/djano.png)
