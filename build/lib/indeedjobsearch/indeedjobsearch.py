
__Author__ = "Soumil Nitin Shah"
__Version__ = '1.1.1'
__Email__ = "soushah@my.bridgeport.edu"
__Website__ = "https://www.soumilshah.herokuapp.com"

try:
    import requests
    import bs4
    from bs4 import BeautifulSoup
    import pandas as pd

except Exception as e:
    print("Some Modules are Missing {}".format(e))


class WebCrawler(object):

    def __init__(self, title = '',location = ""):

        self._url = "https://www.indeed.com/jobs"
        self._headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        self._title = title
        self._location = location

        self.params = {
            'q': self._title,
            'l': self._location,
            'start':40
        }

    def get(self):

        try:

            r = requests.get(url=self._url,
                             headers=self._headers ,
                             params=self.params)
            #print(r.text)
            return r.text

        except Exception as e:

            print("Failed to make response to Indeed")


class DataStructure():

    def __init__(self):

        """Constructor """

        self.data = {
            'title':[],
            'location':[],
            'summary':[],
            'date':[],
            'link':[]
        }


class DataCleaning(object):

    def __init__(self, title = '', location = ""):
        self._title = title                                         # for title of job search
        self._location = location
        self._webcrawler = WebCrawler(self._title, self._location)  # where are you looking for that job
        self.data = self._webcrawler.get()                          # makes a get request and puts the r.text in data variable
        self.datastructure = DataStructure()                        # create a instance of that datastructure object

    def getData(self):

        counter = 10                                                    # Iterate over Pages on Websites

        soup = BeautifulSoup(self.data, 'html.parser')                  # Creates a soup object
        dt = soup.find('div', class_="pagination")                      # finds the pagination from the text

        for x in str(dt).split():                                       # do some processing

            if 'data-pp' in x:
                data = x.split("=")
                token = data[1]

                url = "https://www.indeed.com/jobs"

                headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

                params = {
                    'q': 'Python',
                    'l': 'Bridgeport, CT',
                    'start':counter,
                    'pp':data[1]
                }

                r = requests.get(url=url,
                                 headers=headers,
                                 params=params)

                textdata = r.text
                soup = BeautifulSoup(r.text, 'html.parser')

                for x in soup.findAll('div', class_="jobsearch-SerpJobCard unifiedRow row result"):

                    title = x.find(class_="title").text.strip()                                                  # Finding the elements
                    self.datastructure.data["title"].append(title)                                              # append data to datastructure

                    location = x.find(class_="location accessible-contrast-color-location").text.strip()        # find the location
                    self.datastructure.data["location"].append(location)                                        # append to the datastructure


                    summary = x.find(class_="summary")                                                          # find the summary for the job
                    self.datastructure.data["summary"].append(summary.text)                                     # append to data structure

                    date = x.find(class_="date")                                                                # finds the data of job post
                    self.datastructure.data["date"].append(date)                                                # append to data structure

                    link = x.find('a', href=True)                                                               # get the links
                    base_url = "https://www.indeed.com/"                                                        # make a base link
                    Final = base_url + link["href"]


                    Final = "https://www.indeed.com/" + link["href"]                                            # join the two strings
                    self.datastructure.data["link"].append(Final)                                               # append to data structure


            counter = counter + 10                                                                               # Pagination counter

        # Prepares for pandas Dataframe
        data = list(zip(
            self.datastructure.data["title"],  self.datastructure.data["location"],
            self.datastructure.data["summary"],self.datastructure.data["date"],
            self.datastructure.data["link"]
        ))

        # creates a pandas Dataframe
        df = pd.DataFrame(data=data, columns=["title", "location", "summary", "date", "link" ])
        return df


class Singelton(type):

    _instance = {}          # Creates a instanc

    def __call__(cls, *args, **kwargs):         # create a object

        if cls not in cls._instance:

            cls._instance[cls] = super(Singelton, cls).__call__(*args, **kwargs)

            return  cls._instance[cls]


class IndeedJobSearch(metaclass=Singelton):

    def __init__(self, title = '', location = ""):

        """Constructor """

        self.title = title
        self.location = location
        self.datacleaning = DataCleaning(title=self.title, location=self.location)

    def getJobs(self):

        """

        :return: Pandas DataFrame
        """
        data = self.datacleaning.getData()
        return data

    def saveCsv(self):

        """
        Saves all job in CSV File
        :return: None
        """

        data = self.datacleaning.getData()
        data.to_csv("Jobs.csv")

    def saveExcel(self):

        """
        SAves all jpbsin Excel File
        :return: None
        """

        data = self.datacleaning.getData()
        data.to_excel("job.xls")


# if __name__ == "__main__":
#
#     # Driver code
#     jobsearch = IndeedJobSearch(title='Python', location="Bridgeport , CT")
#     data =jobsearch.getJobs()
#     print(data)
#     # jobsearch.saveExcel()







