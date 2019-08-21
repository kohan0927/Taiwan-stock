# Taiwan-stock
This APP shows how to access and crawl the "Taiwan Stock Exchange Corporation (TWSE), https://www.twse.com.tw" smoothly without being notifying as a bot attacker.

# Files
1. stocklist_up.csv
  - Contain the list of stocks.

2. gui.py
  - This file is generated by gui.ui which is made by QT Designer.

3. amount.py
  - Called one of self-defined modules, loadup_thread, to access "Taiwan Stock Exchange Corporation (TWSE), https://www.twse.com.tw".
  - Obtain desired stock's price information.
  - Automatically, smoothly and constantly crawl the web page without being notifiying as a bot attacker by using "selenium" module.   

4. loadup_thread.py
  - Get all price information.

# NOTE:
This project reveals only some sample codes of my actual project. However, you may find some useful functionality or tricks I have created.
