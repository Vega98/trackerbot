# Trackerbot
Python script that checks if provided webpages were updated and in that case sends you a telegram message.

Requires you to set up a [Telegram bot](https://core.telegram.org/bots "More info here"), and for you to know your personal [Telegram user_id](https://bigone.zendesk.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID- "More info here").

Set it up as you like. I suggest making it a daemon via systemd or crontab.

# How to set it up

Simply edit the python script, where you see 
```python
<...something...>
```
you should place your own info. Multiple pages can be tracked. You can also change the frequency of the cycle editing the last sleep command. Default is 1 minute, i don't suggest lower than that.

Example:
cycle throught webpages every 5 minutes
```python
...
sleep(300)
```
