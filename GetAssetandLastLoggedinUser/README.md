# S1 Asset and User Pull Script

This script pulls all assets enrolled in S1 along with the last user who is/was logged on the asset.

# Required Variables

* APITOKEN: S1 API Token which can be generated from the console. 
* S1BASEURL: S1 Baseurl for your org. Typically this will be https://yourorg.sentinelone.net/

# Background

This script was build as a means to develop a inventory management of all assets within an organization. Running into a situation where there is no asset management, I found pulling last login user to be the most accurate in my scenario. 
While this is not considered as fully accurate, this can help expedite the process of identifying asset ownerships organization wide given S1 is utilized and it has been pushed to all assets. 
