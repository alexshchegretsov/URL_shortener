<p align="center"><img src="images/img2.png"></p>
<h1>SHRTN.IT - is a web service that shortens urls</h1>
<p>The service accepts any URLs, saves to the database, encodes its id with "base 62" algorithm and returns to the user.</p>
<h2>Why?</h2>
<p>URL shortening is used to create shorter aliases for long URLs. We call these shortened aliases “short links.” Users are redirected to the original URL when they hit these short links. Short links save a lot of space when displayed, printed, messaged, or tweeted. Additionally, users are less likely to mistype shorter URLs.</p>
<h2></h2>
<pre>
    def test_redirect_to_long_url_GET(self):
        response_1 = self.c.get('/1')
        response_2 = self.c.get('/a')
        self.assertEquals(response_1.status_code, 301)
        self.assertEquals(response_2.status_code, 301)
</pre>
