def scrape_webpage(url):
    import chromedriver_autoinstaller
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    
    # Checks if the current version of chromedriver exists and
    # if not, downloads it and adds chromedriver to path.
    chromedriver_autoinstaller.install()
    
    # Setting up Chrome browser options.
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")               # Chrome starts as a daemon
    
    # Starting webdriver with set options
    driver = webdriver.Chrome(options=chrome_options)
    
    # Get-Requests given Website and renders it
    driver.get(url)
    html = driver.page_source
    
    return html