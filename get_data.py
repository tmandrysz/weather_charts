import urllib
from bs4 import BeautifulSoup

page = urllib.urlopen("http://www.wunderground.com/history/airport/EPWR/2016/03/14/DailyHistory.html").read()
soup = BeautifulSoup(page, 'html.parser')

TemperatureTable = soup.findAll('table', attrs={"class": "responsive airport-history-summary-table", "id": "historyTable"})


def get_historyTable_temperature(historyTable):
    """
    This method parses 'Mean Temperature', 'Max Temperature', 'Min Temperature' from wunderground.com airport-history-summary-table
    :param historyTable: BeautifulSoup table object
    :return: parsed decimal value
    """

    temp_data = {}

    for row in historyTable[0].findAll('tr'):
        cells = row.findAll('td')

        if len(cells) >0 :
            cell_text = cells[0].get_text()
            if cell_text == 'Mean Temperature':
                temp_data['mean_temp'] = int(cells[1].findAll('span', attrs={"class": "wx-value"})[0].get_text())
            elif cell_text == 'Max Temperature':
                temp_data['max_temp'] = int(cells[1].findAll('span', attrs={"class": "wx-value"})[0].get_text())
            elif cell_text == 'Min Temperature':
                temp_data['min_temp'] = int(cells[1].findAll('span', attrs={"class": "wx-value"})[0].get_text())

    return temp_data


print 'Max Temperature: ', get_historyTable_temperature(TemperatureTable)
