PYTHON AUTO FUSION WEB API
Walter I. Baltzley 2023
=============================================================================
This Package allows the development of automated scripts using multiple
Python automation frameworks.  

Your Directory Hierarchy is as follows:

MULTI_FRAMEWORK_API_FOR WEB_AUTOMATION

   main.py

 - WRAPLETS_SITE(1)
     - Wraplet_1.py
     - Wraplet_2.py
     
 - WRAPLETS_SITE(2)
     - Wraplet_1.py
     - Wraplet_2.py
     
 - 010_FRAMEWORK(1)
    
    _Framework.py
    
    
    - BROWSER_API
        - Navigation.py
        - Buttons.py
        - Text.py
        - Sliders.py
         
    - SITE_1_API
        - Page(1)_Wrappule.py
        - Page(2)_Wrappule.py
    
    - SITE_2_API
        - Page_1_Wrappule.py
        - Page_2_Wrappule.py
     
        
 - 020_FRAMEWORK(2)
 - 030_FRAMEWORK(3)

============================================================================

How To Use the Framework:

main.py is used as the entry-point for execution.  At the beginning 
of this file you include all of your wrapped framework packages so that
they can be called and used at any point in your program. 

Your main() program calls scripts, called "Wraplets" -- A Wraplet is a 
program that makes use of "Wrapules" or modules that make use of wrapped functions 
for a given framework... Wraplets are built to automate functions for a specific 
website.  All wraplets for a site are packaged together in the same directory.  

Wraplets make use of "Wrapules" -- modules containing wrapped functions for a 
given framework... these are stored inside a sub-package for that framework.  
A Wrapule makes use of the BROWSER_API implemented using that particular 
framework.

The BROWSER_API is an interface that allows the user to control various browser
functions -- such as start a browser, navigate tabs and windows, and interact
with common webpage elements.    

The SITE_API uses the wrapped functions in the BROWSER_API to access elements
and perform simple tasks on a given page or a container within a page of a 
given website.  Because each element on a site has a unique identifier, it is 
convenient to group functions based on their location. 

For example, You might generate a wrapule to log into the site, and another to 
access and navigate the site menu.  You might create a third warpule to 
encapsulate button controls, forms, and navigation links.  And another to 
access controls or an embedded web-applications.  

These Wrapules are then assembled into a wraplet to perform complex operations, 
such as log into your email account, clear your inbox, and send a personalized
message to each of your contacts before logging out again.  They can also
be used to automate repetitive tasks, or monitor sites for certain events.  

Wraplets are then called from your main() program.  You can set them up to be 
executed automatically at specific times, or you can call them manually 
from a menu.    



 =============================================================================  




