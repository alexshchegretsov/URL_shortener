<h1>SHRTN.IT</h1>
<p align="center"><img src="images/img2.png" width=900px></p>
<h1 align="center">The web service that shortens urls</h1>
<p>The app accepts any URLs, saves to the database, encodes its id with "Base 62 encoding" algorithm and returns to the user.</p>
<h2>Why?</h2>
<p>URL shortening is used to create shorter aliases for long URLs. We call these shortened aliases “short links”. Users are redirected to the original URL when they hit these short links. Short links save a lot of space when displayed, printed, messaged, or tweeted. Additionally, users are less likely to mistype shorter URLs.</p>
<h2>Demo</h2>
  <img src="images/demo5.png" height="420px">
<h2>Scheme</h2>
  <img src="images/base62.png" height="420px">
<h2>For developers</h2>
<p>Clone the source locally:</p>
<pre> 
      $ git clone https://github.com/alexshchegretsov/URL_shortener.git
      $ cd URL_shortener
</pre>
<p>Update package list and install pip for Python 3:</p>
<pre>
      $ sudo apt update
      $ sudo apt install python3-pip
</pre>
<p>Once the installation is complete, verify the installation by checking the pip version:</p>
<pre>
      $ pip3 --version
</pre>
<p>You are still at /URL_shortener/ directory, create and run virtual environment:</p>
<pre>
      $ virtualenv -p python3.7 .venv
      $ source .venv/bin/activate
</pre>
<h4>Install all dependencies from requirements.txt:</h4>
<pre>
      $ pip3 install -r requirements.txt
</pre>
<p>Move to /src/ directory, initialize data base and run server:</p>
<pre>
      $ cd src/
      $ ./manage.py migrate
      $ ./manage.py runserver
</pre>
<p>Open your browser in a new window and go to localhost, for this you need to enter in the input line:</p>
<pre>
      http://127.0.0.1:8000/
</pre>
<h2>Built with</h2>
<ul>
  <li><a href="https://www.djangoproject.com/">Django</a> - The web framework used</li>
  <li><a href="https://milligram.io/">Milligram</a> - A minimalist CSS framework</li>
</ul>
<h2>License</h2>
<p>MIT &copy; <a href="https://github.com/alexshchegretsov">Alex Shchegretsov</a></p>
