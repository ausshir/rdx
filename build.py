#! /usr/bin/env python3

import glob

HEAD_HTML = '''<!DOCTYPE html><html><head>
    <title>rdx -  Apollo For Reddit Inspired Web Viewer</title>
    <meta name="description" content="rdx is a fast, lightweight mobile Web Viewer for Reddit based on Apollo. Mobile friendly reader for Reddit. Browse Reddit without Ads."/>
    <link rel="shortcut icon" href="favicon.ico">   
  <link rel="icon" href="favicon.png"> 
<link rel="manifest" href="/manifest.json" /> <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-title" content="rdx" />
    <meta name="apple-mobile-web-app-status-bar-style" content="default" />
     <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <meta charset="utf-8">
    <link rel="stylesheet" href="styles.css" type="text/css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dashjs/4.7.1/dash.all.min.js"></script>
    </head>  

<body>
    <header id="header">
        <div id="pagetitle">
            <span id="plus" onclick="toggle(\'leftbar\')"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24" fill="#fff" role="img" aria-label="Menu"><path d="M140.001-254.616v-59.999h679.998v59.999H140.001Zm0-195.385v-59.998h679.998v59.998H140.001Zm0-195.384v-59.999h679.998v59.999H140.001Z"></path></svg></span>
            <span id="taptoopenmenu" onclick="toggle(\'subssearch\')"><span id="pagetitletext">Loading...</span>
            <svg aria-hidden="true" focusable="false" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" id="icon-target" style=""><path fill="currentColor" d="M31.3 192h257.3c17.8 0 26.7 21.5 14.1 34.1L174.1 354.8c-7.8 7.8-20.5 7.8-28.3 0L17.2 226.1C4.6 213.5 13.5 192 31.3 192z"></path></svg></span>
            <span id="menu" onclick="toggle(\'rightbar\')"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24" fill="#fff" role="img" aria-label="Sort and other options"><path d="M411.155-260.001V-320h137.306v59.999H411.155Zm-155-190v-59.998H703.46v59.998H256.155ZM140.001-640v-59.999h679.998V-640H140.001Z"/></svg></span>
        </div>
    
    <div id="menus">
        <div id="subssearch" class="hidden">
            <input type="text" id="subssearchi" name="qury" onkeyup="searchsubs(this.value,event)" autocomplete="off">
            <div id="subslist"></div>
        </div>
        <div id="leftbar" class="hidden">
            <div class="list">
                <a href="index.html" class="homelinks halfit">Home</a><a onClick="window.location.reload()" class="homelinks halfit">Refresh</a><a href="saved.html" class="homelinks halfit">Saved</a><a href="subreddit.html?r=popular" class="homelinks halfit">Popular</a>
                <div id="subscribed">Subscribe to subreddits to view them here.</div>        <div id="cthemew"><a onclick="toggletheme(\'dark\')" id="themebtn">Dark mode</a>
              </div> 
            </div>
        </div>
        <div id="rightbar" class="hidden"></div>
    </div>
    </header>
    <div id="body"></div>
    <script src="functions.js">
    <script src="https://cdn.jsdelivr.net/npm/ios-pwa-splash@1.0.0/cdn.min.js"></script>
<script>iosPWASplash(\'5122.png\', \'#4e2a72\');</script>'''

BODY_HTML = '''<div class="footer"><a href="https://www.buymeacoffee.com/overdevsapps" class="bmac"><img src="bmac.png"  width="190" alt="donate"></a><br>If you use rdx for Reddit&reg; please provide <a href="contact.html">Feedback</a> and <a href="https://www.buymeacoffee.com/overdevsapps">Donate</a>.<br><br><small><a href="new.html">What\'s new?</a> | <a href="settings.html">Settings</a> | <a href="https://github.com/avadhesh18/rdx/">Star on Github</a></small></div> <div id="popitup" style="display:none;">
  <span onclick="document.getElementById(\'popitup\').style.display=\'none\'">Cancel</span>
  <div id="helptext"></div><textarea class="cmntarea" id="commentText" placeholder="Write a reply!" required></textarea>
<input id="cmtid" value="" type="hidden"/> <input id="actype" value="" type="hidden"/> <button id="cmntbtn" onclick="apiAction();">Submit</button>
</div> <!-- rdx --></body>'''

RDX_INFO_HTML = '''<div class="infotext">
<h1>Explore Reddit with rdx: A Fast and Lightweight Web Viewer Inspired by Apollo</h1>
<p>Discover a seamless Reddit browsing experience with rdx, a mobile-friendly web viewer designed for speed and simplicity. Based on the now closed Apollo app, rdx allows you to navigate Reddit without the distraction of ads.</p>
<h2>Enjoy Reddit Anywhere: rdx\'s Mobile-Friendly Design and Dark Mode</h2>
<p>Experience the freedom of browsing Reddit on the mobile easily with rdx\'s mobile-friendly design. The interface is optimized for various devices, ensuring a smooth experience across different screen sizes. Additionally, rdx offers a Dark Mode for users who prefer a more comfortable and eye-friendly viewing experience, making it easy to enjoy Reddit in any lighting condition.</p>
<h2>Support rdx Development: Donate and Provide Feedback</h2>
<p>If you find rdx valuable for your Reddit exploration, consider supporting its development. You can contribute by providing feedback on your experience and making a donation here. Your support helps enhance the features and performance of rdx, ensuring a better browsing experience for all users. Additionally, check out the "What\'s New?" section for updates, adjust settings according to your preferences, and explore rdx\'s source code on GitHub.</p> </div> '''

files = glob.glob("html/*.html")

print(f"Files to process: {files}")

for file in files:

    print(f"Processing {file}...")

    with open (file, 'r') as infile:
        
        data = infile.read()
        data = data.replace('<!--headhtml-->', HEAD_HTML)
        data = data.replace('</body>', BODY_HTML)

        if file == 'html/index.html':
            data = data.replace('<!-- rdx -->', RDX_INFO_HTML)

    newfilename = file.replace('html/', 'public/')

    with open(newfilename, 'w') as outfile:
        print(f"Writing to {newfilename}")
        outfile.write(data)
