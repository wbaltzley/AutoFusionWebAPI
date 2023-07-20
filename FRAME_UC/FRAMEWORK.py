#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------
FRAMEWORK.py -- This module is part of the FRAME_UC Package and provides a 
wrapper API for Selenium and Undetected_Chromedriver, which is accessed by 
importing this module and creating an instance of the API() class. 
-----------------------------------------------------------------------------
Created on Mon Jul 10 18:31:55 2023
@author: walter
"""
class API():
    # ==============================================================
    # Import Libraries
    # ===============================================================
    import undetected_chromedriver as uc
    from undetected_chromedriver import By
    from undetected_chromedriver import webdriver
    from undetected_chromedriver.webdriver import ActionChains
    import time
    # ==============================================================
    # Set Options...
    # ==============================================================
    options = uc.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-setuid-sandbox") 
    options.add_argument("--disable-dev-shm-using") 
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-plugins")
    ## options.add_argument("--headless")
    #=================================================================
    # Get Undetected Web Driver
    #=================================================================
    
    myDriver = uc.Chrome() 
    myActions = ActionChains(myDriver)

    # Change the property value of the navigator for webdriver to undefined
    myDriver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # end Framework();
    
        
   
    # ==============================================================
    # Open Webpage... 
    # =============================================================== 
    def open_page(self, URL: str):
        self.myDriver.open(URL)
        
    # end open_page()

    """ This function opens a page in a new window and returns a handle"""    
    def open_page_in_new_window(self, URL: str) -> str:
        self.myDriver.switch_to.new_window(URL)
        return self.myApi.myDriver.get_handle()
    # end open_page_in_new_window()
    

    # ========================================================================
    # Folloiwng Links
    # ======================================================================== 
    """ 
    To make navigation easier, it is best to open links in a new window
    and return a handle for that new window.
    """
    def open_link_in_new_window(self, link: str) ->str:
        
        # get URL for the link
        # open_page_in_new_window
        
        return self.get_newest_handle()
    # end open_link_in_new_window()
    
   
    
   
    
   # ==============================================================
   # Build Ppage Elements... 
   # =============================================================== 
    """This function retrieves a Selenium WebElement Object using the XPATH..."""
      
    def get_element(self, path: str) -> uc.Chrome.WebElement:
        #--------------------------------------------------------------------
        from undetected_chromedriver import By
        myElement= self.myDriver.find_element(By.XPATH, path)
        return myElement
        #--------------------------------------------------------------------
    # end get_element();
    
    
    
    """
    This represents any element that has the ability to be clicked.
    You will need to identify the XPATH for the element.
    """       
    class clicker():
        #--------------------------------------------------------------------
        def __init__(self, path: str):
            self.myElement = API.get_element(path)
        # end init();
        #---------------------------------------------
        def click(self):
            self.myElement.click()
        # end click();
        #---------------------------------------------
    # end button()
    
     
    """
    This Element is used to access and enter text into a field.  You will need
    to identify the XPATH for the text field, and the submit button.
    """           
    class field(): 
        #--------------------------------------------------------------------
        def __init__(self, path1: str, path2: str):
            self.myField= API.get_element(path1)
            self.mySubmit=API.get_element(path2)
        # end init();
        #---------------------------------------------
        def click_field(self):
            self.myField.click()
        # end init();
        #---------------------------------------------
        def enter_text(self, text: str): 
            self.myField.send_keys(text)
        # end enter_text();
        #---------------------------------------------
        def click_submit(self):
            self.mySubmit.click()
        # end click_submit();
        #---------------------------------------------
        def fill_and_submit(self, text: str):
            self.click_field()
            self.sleep(2)
            self.enter_text(text)
            self.sleep(2)
            self.click_submit()
        #---------------------------------------------
    # end field();
    
    
    
    """
    This Element is used to easlily access an option in a single-level drop menu
    You will need to identify the XPATH for the head of the menu, and for the
    menu option you want to access.
    """        
    class click_menu_option():
        #--------------------------------------------------------------------
        def __init__(self, path1: str, path2: str):
            self.menu_head= API.get_element(path1)
            self.selection= API.get_element(path2)
        # end init();
        #---------------------------------------------
        def click(self): 
            self.menu_head.click()
            self.time.sleep(2)
            self.selection.click()
        # end click()
        #---------------------------------------------
    # end clsss drop_menu_option()
    
    
    """
    This Element is a slider with a single sliding element, it is typically 
    used to set the magnitude for a value in a web-application. You will need
    to identify the XPATH for the sliding element.
    """
    class single_slider():
        from undetected_chromedriver import webdriver
        from undetected_chromedriver.webdriver import ActionChains, Keys
        #--------------------------------------------------------------------
        def __init__(self, path: str):
            self.slider= API.get_element(path)
        # end init();
        #---------------------------------------------
        def set_slider(self, val: int):
            API.myActions.drag_and_drop_by_offset(self.slider, val).perform()
        # end set_slider()
        #---------------------------------------------
    # end slider();


    """
    This Element is a slider with a two sliding elements, it is typically 
    used to set a range of values in a web-application. You will need to 
    identify the XPATH for each slider element.
    """
    class range_slider():
        #--------------------------------------------------------------------
        def __init__(self, path1: str, path2: str):
            self.min=  API.get_element(path1)
            self.max=  API.get_element(path2)
        # end init();
        #---------------------------------------------
        def set_low(self, val: int):
            API.myActions.drag_and_drop_by_offset(min, val).perform()
        # end set_slider()
        #---------------------------------------------
        def set_high(self, val: int):
            API.myActions.drag_and_drop_by_offset(max, val).perform()
        # end set_slider()
        #---------------------------------------------
        def set_range(self, val1: int, val2: int):
            self.set_low(val1)
            self.sleep(2)
            self.set_high(val2)
        # end set_slider()
        #---------------------------------------------
    # end slider();
   

    """ This Element represents an image.  """
    class image():
        #--------------------------------------------------------------------
        def __init__(self, path: str):
            self.myImage = API.get_element(path)
        # end init();
        #---------------------------------------------
        def click(self):
           self.myImage.click()
        # end click()
        #---------------------------------------------
        def save(self, loc: str):
            pass
        # end save()
        #--------------------------------------------------------------------
    # end image();
    
    
    """ This Element represents a video """
    class video():
        #--------------------------------------------------------------------
        def __init__(self, path: str):
            self.myVid = API.get_element(path)
        # end init();
        #---------------------------------------------
        
        pass
        
    #--------------------------------------------------------------------
    # end video();
   
    
    # ========================================================================
    # Manipulate The Chrome Browser...
    # ======================================================================== 
    """ 
    These functions are used to open and close windowws, navigate between 
    windows, maximize, minimize, and perform other such window operations. 
    """
    #--------------------------------------------------------------------
    # Gets a handle for the window currently in focus.  Handles are generated
    # for each window opened with the web-driver, and these are stored in an
    # array in the order they were opened...
    #--------------------------------------------------------------------
    def get_curr_handle(self) ->str:
        return self.myDriver.current_window_handle()
    # end get_window()
    
    
    #--------------------------------------------------------------------
    # Used to get the handle for a specific entry
    #--------------------------------------------------------------------
    def get_handle(self, num: int) ->str:   
        return self.myDriver.window_handles[num]
    # end get_handle()
   
    
    #--------------------------------------------------------------------
    # Used to get the handle for a window that was just opened by clicking a 
    # link by accessing the last element in the window_handles array
    #--------------------------------------------------------------------
    def get_newest_handle(self) ->str:
       num = len(self.myDriver.window_handles)
       --num
       return self.get_handle(num)
    # end get_newest_handle()
    
    
    #--------------------------------------------------------------------
    # Used to switch between open windows using its handle  
    #--------------------------------------------------------------------
    def set_window(self, handle: str):
        self.myDriver.switch_to.window(handle)
    # end set_window()
    
    
    
    
    #--------------------------------------------------------------------
   
    
        
        
    

#----------------------------------------------------------------------------
# end class Framework()


























