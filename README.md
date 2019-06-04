<h1>SHRTN.IT</h1>
<p align="center"><img src="images/img2.png" width=900px></p>
<h1 align="center">The web service that shortens urls</h1>
<p>The app accepts any URLs, saves to the database, encodes its id with "Base 62 encoding" algorithm and returns to the user.</p>
<h2>Why?</h2>
<p>URL shortening is used to create shorter aliases for long URLs. We call these shortened aliases “short links”. Users are redirected to the original URL when they hit these short links. Short links save a lot of space when displayed, printed, messaged, or tweeted. Additionally, users are less likely to mistype shorter URLs.</p>
<h2>Demo</h2>
  <img src="images/demo3.png" height="420px">
<h2>Key system</h2>
  <img src="images/base62.png" height="420px">
<h2>For developers</h2>
<p>Clone the source locally:</p>
<pre> 
      $ git clone https://github.com/alexshchegretsov/TMS_project_url_shortener.git
      $ cd TMS_project_url_shortener
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
<p>You are still at TMS_project_url_shortener directory, create and run virtual environment:</p>
<pre>
      $ virtualenv -p python3.7 .venv
      $ source .venv/bin/activate
</pre>
<h4>Install all dependencies from requirements.txt:</h4>
<pre>
      $ pip3 install -r requirements.txt
</pre>
<h2>Built with</h2>
<ul>
  <li><a href="https://www.djangoproject.com/">Django</a> - The web framework used</li>
</ul>
<h2>Author</h2>
<a href="#">Alex Shchegretsov</a>
<h2>License</h2>
<p>MIT</p>
