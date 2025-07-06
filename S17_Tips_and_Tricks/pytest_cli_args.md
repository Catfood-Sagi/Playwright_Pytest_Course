**CLI Arguments**

**-headed** - to define headed mode  
**--slowmo** = for slow motion, works in miliseconds  
**--browser** = <name of browser>  
**--screenshot** = allow you to take a screenshot of the page after test completion (can be modified using only-on-failure)  
**--device** = to emulate a device like iphone or samsuang galaxy  
**--html** =  you can set a report path like =reports/report.html and it will save a result report of our tests in an HTML file  
**-k** = used to filter which tests to run, it based on a substring matching in the test name or  marker expression  
        it allow us to run a subset of tests my matching keywords in  
    1. Test functions name (can run specific test case)  
    2. Class names  
    3. File names  
    4 Marker expression  
**--tracing** = enable tracing to this we can provide 3 different options  
    1. on  
    2. off  
    3. retain-on-failure  

__tracing__  
Records a retailed trace of your tests execution including
* Screenshot
* DOM Snapshot
* Network requests
* Console logs
* Clicks and actions

helpful tips:
1. You can run playwright show-trace <file name>
2. Can also open it from trace.playwright.dev website

