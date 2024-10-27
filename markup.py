def to_html(page):
    page = page.replace("<title>", "<div class='title'>")
    page = page.replace("<title font=\"databet\">", "<div class='title databet'>")
    page = page.replace("</title>", "</div>")

    page = page.replace("<author>", "<div class='author'>")
    page = page.replace("</author>", "</div>")
    for a in ["left", "right", "centre"]:
        page = page.replace(f"<block align {a}>", f"<div class='block{a}'>")
    page = page.replace("</block>", "</div>")
    page = page.replace("<spacing>", "<div style='height:10vh'></div>")
    page = page.replace("<spacing small>", "<div style='height:1vh'></div>")
    page = page.replace("<mscroggs.co.uk>", "<span style='font-family:comfortaaregular;font-weight:normal'><span style='color:#2EA3D0'>mscroggs</span><span style='color:FFA366'>.co.uk</span></span>")
    page = page.replace("<icon twitter>", "<span class='icon twitter'>a</span>")
    page = page.replace("<icon website>", "<span class='icon website'>d</span>")
    page = page.replace("<icon mastodon>", "<span class='icon mastodon'>n</span>")
    page = page.replace("<icon bluesky>", "<span class='icon bluesky'>t</span>")
    return page
