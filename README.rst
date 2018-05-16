screenshotapi
=============

An API Client for ScreenshotAPI.io (www.screenshotapi.io)

Will perform a screenshot capture using ScreenshotAPI.io and store the resulting screenshot png file locally on disk given the path prefix specified in the `save_path` argument.

Installation
------------

.. code-block:: shell
  pip install screenshotapi

Usage
-----

.. code-block:: python
  import screenshotapi

  screenshotapi.get_screenshot(
      apikey='get your free apikey at www.screenshotapi.io',
      capture_request = {
            'url': 'http://www.amazon.com',
            'viewport': '1200x800',
            'fullpage': False,
            'webdriver': 'firefox',
            'javascript': True,
            'fresh': False
          },
          save_path = './'
  )

Command Line Usage
------------------

The installer also provids a command line interface.  You can use it as follows.

.. code-block:: shell
  $ export SCREENSHOTAPI_KEY=your-key-goes-here
  $ screenshotapi --url http://amazon.com \
                  --viewport 1200x800 \
                  --webdriver firefox \
                  --save-path ./

Note that you can provide a SCREENSHOTAPI_KEY environment variable that can then be used for subsequent calls, or you can use an --apikey argument on each call.

API Key
-------

To get a free API key, go to www.screenshotapi.io.

