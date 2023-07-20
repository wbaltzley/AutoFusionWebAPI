#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------
This Class represents the site https://www.mage.space for the Undetected
Chromedriver (UC) The site is broken down into pages and uses the UC API to
generate the elements for those pages.  
-----------------------------------------------------------------------------
Created on Sat Jul 15 16:28:03 2023
@author: walter
"""

import FRAMEWORK
myApi = FRAMEWORK.API()


"""
This class represents the homepage or landing page for https://mage.space 
This page operates as a web-application whose controls load additional 
content without actually changing pages.  
"""
class homepage():
    #------------------------------------------------------------------------
    def __init__(self):
        self.myAddress = 'https://mage.space'
    # end init()    
    
    myHandle: str # Holds a handle for easy navigation with Selenium
    
    #------------------------------------------------------------------------
    
    """
    This function opens https://mage.space in a new browser window and returns
    and saves the handle for that window.  
    """
    def load(self):
        self.myHandle = self.myApi.open_page_in_new_window(self.myAddress)
    # end load()
    #------------------------------------------------------------------------
    
    
    """
    This function closes the initial popup that appears when you first load
    https://mage.space; It simply clicks the close button. 
    """ 
    def close_init_popup():
        Xpath = '//*[@id="mantine-R3bm-body"]/div/div[1]/div/button'
        close_button = myApi.clicker(Xpath)
        close_button.click()
    # end close_init_popup()
    
    
    """
    This function logs into https://mage.space using google. It opens the 
    google login page, switches control to that page, logs in, and then switches 
    back to the starting page.  
    """ 
    def login_with_google(self, user: str, pwd: str):
        #---------------------------------------------------------------------
        # Save Handle For Starting Window
        start_window = myApi.get_curr_handle()
        
        
        # Click Login Button in Profile Menu
        menu   = '//*[@id="mantine-R14mlbm-target"]'
        button = '//*[@id="mantine-R14mlbm-dropdown"]/div/button[8]/div[2]'
        loginButton = myApi.click_menu_option(menu, button)
        loginButton.click()
        self.time.sleep(2)
        
        
        # Click Google Option
        button = self.myAPI.clicker('//*[@id="mantine-R3bm-body"]/div/div[2]/button/div/span[2]') 
        button.click()
        self.time.sleep(3)
        
        
        # Switch To Opened Window...
        window_after = self.myApi.get_newest_handle()
        self.myApi.set_window(window_after)
        self.time.sleep(1)
        
        
        # ENTER USERNAME (Email Address) 
        field   = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
        submit  = '//*[@id="identifierNext"]/div/button'
        myEmail = myApi.field(field, submit)
        myEmail.fill_and_submit(user)
        self.time.sleep(1) 
        
        
        # ENTER PASSWORD
        field =  '//*[@id="password"]/div[1]/div/div[1]/input'
        submit = '//*[@id="passwordNext"]/div/button'
        myPass = myApi.field(field, submit)
        myPass.fill_and_submit(pwd)
        self.time.sleep(1)
        
        
        # Return to original window.
        self.myApi.set_window(start_window)
        #---------------------------------------------------------------------
    # end login_with_google()

    """
    These Are the various elements you find on the homepage.  
    """
    




# end homepage();







