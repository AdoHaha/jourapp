Jourapp
=======

this is a small journaling app, designed for small computer such as Raspberry Pi, to keep you writing from whichever computer you choose.


The idea is simple: write min 750 words every day. To do that you will need some motivation and this app intends to do just that. It will count no of words you have written, change background and give you nice alert when you suceeded.

I like to backup my stuff, so it will dropbox your database when you close the app.

There will be some stats provided, so you can know how well you are doing, please help my app by creating some pretty badges :))

For now, my motivation is a ugly red background. It dissapears when you write, becoming white when you pass 750 words mark. So keep writing ;)

Technical info
-----

This is python Flask app, with lots of Coffeescript beauty. There is also simple SQLite DB behind, doing all the hard work. It will be backuped to Dropbox.


Setup
-----

To make it working, you need to be "Dropbox Developer" I suggest visiting http://raspi.tv/2013/how-to-use-dropbox-with-raspberry-pi for excelent guide how to set all on RPi

Your RPi must have *Python2.7.* , *Flask* for Python, *sqlite3* for Python






