try:

    from indeedjobsearch.indeedjobsearch import IndeedJobSearch
    print("All modules loaded .... ")

except Exception as e:
    print("Failed to load Module ")

# create a object of class
jobsearch = IndeedJobSearch(title='Python', location="Bridgeport , CT")

# call method getJobs()
data=jobsearch.getJobs()

# Return Pandas Dataframe
print(data)