
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]


# indeedjobsearch Bot

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/soumilshah1995)


#### what is Indeed Job Search Bot ?

* Indeed job search bot is a bot that finds you 150 + jobs in less than 5 seconds
* The output can be saved as either CSV or Excel File 
* Refer to examples shown Below



#### Dependencies 

```bash

pip install pandas
pip install bs4
pip install requests
```


## Installation

```bash
pip install indeedjobsearch
```
## Usage


```python
try:

    from indeedjobsearch.indeedjobsearch import IndeedJobSearch
    print("All modules loaded .... ")
    
except Exception as e:
    print("Failed to load Module ")
    
# create a object of class 
jobsearch = IndeedJobSearch(title='Python', location="Bridgeport , CT")

# call method getJobs()
data  = jobsearch.getJobs(

# Return Pandas Dataframe 
print(data)

# Save all the Jobs in Excel File 
jobsearch.saveExcel()

```
* we will add more features to this. if you have any issue running this kindly send a email to the author


## Authors

## Soumil Nitin Shah 
Bachelor in Electronic Engineering |
Masters in Electrical Engineering | 
Master in Computer Engineering |

* Website : https://soumilshah.herokuapp.com
* Github: https://github.com/soumilshah1995
* Linkedin: https://www.linkedin.com/in/shah-soumil/
* Blog: https://soumilshah1995.blogspot.com/
* Youtube : https://www.youtube.com/channel/UC_eOodxvwS_H7x2uLQa-svw?view_as=subscriber
* Facebook Page : https://www.facebook.com/soumilshah1995/
* Email : shahsoumil519@gmail.com



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


